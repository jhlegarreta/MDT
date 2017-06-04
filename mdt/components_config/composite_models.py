from copy import deepcopy
import numpy as np
import six
from mdt.components_loader import ComponentConfig, ComponentBuilder, method_binding_meta, get_component_class
from mdt.models.composite import DMRICompositeModel
from mdt.models.parsers.CompositeModelExpressionParser import parse
from mot.model_building.evaluation_models import EvaluationModel
from mot.model_building.trees import CompartmentModelTree
from mot.model_building.utils import ModelPrior, SimpleModelPrior

__author__ = 'Robbert Harms'
__date__ = "2017-02-14"
__maintainer__ = "Robbert Harms"
__email__ = "robbert.harms@maastrichtuniversity.nl"


class DMRICompositeModelConfig(ComponentConfig):
    """The cascade config to inherit from.

    These configs are loaded on the fly by the DMRICompositeModelBuilder

    Attributes:
        name (str): the name of the model, defaults to the class name
        in_vivo_suitable (boolean): flag indicating if the model is suitable for in vivo data
        ex_vivo_suitable (boolean): flag indicating if the model is suitable for ex vivo data
        description (str): model description
        post_optimization_modifiers (list): a list of modification callbacks for use after optimization. Example:

            .. code-block:: python

                post_optimization_modifiers = [('SNIF', lambda d: 1 - d['Wcsf.w']),
                                           ...]

        model_expression (str): the model expression. For the syntax see:
            mdt.models.parsers.CompositeModelExpression.ebnf
        evaluation_model (EvaluationModel or str): the evaluation model to use during optimization,
            also a string can be given with one of 'Gaussian', 'OffsetGaussian' or 'Rician'.
        signal_noise_model (SignalNoiseModel): optional signal noise decorator
        inits (dict): indicating the initialization values for the parameters. Example:

            .. code-block:: python

                inits = {'Stick.theta': np.pi}

        fixes (dict): indicating the constant value for the given parameters. Example:

            .. code-block:: python

                fixes = {'Ball.d': 3.0e-9,
                         'NODDI_EC.kappa': SimpleAssignment('NODDI_IC.kappa'),
                         'NODDI_EC.theta': 'NODDI_IC.theta'}

            Next to values, this also accepts strings as dependencies (or dependecy objects directly).

        upper_bounds (dict): indicating the upper bounds for the given parameters. Example:

            .. code-block:: python

                upper_bounds = {'Stick.theta': pi}

        lower_bounds (dict): indicating the lower bounds for the given parameters. Example:

            .. code-block:: python

                lower_bounds = {'Stick.theta': 0}

        enforce_weights_sum_to_one (boolean): set to False to disable the automatic Weight-sum-to-one dependency.
            By default it is True and we add them.

        volume_selection (dict): the volume selection by this model. This can be used to limit the volumes used
            in the analysis to only the volumes included in the specification.
            Set to None, or an empty dict to disable.
            The options available are:

               * ``unweighted_threshold`` (float): the threshold differentiating between
                 weighted and unweighted volumes
               * ``use_unweighted`` (bool): if we want to use unweighted volumes or not
               * ``use_weighted`` (bool): if we want to use the diffusion weigthed volumes or not
               * ``min_bval`` (float): the minimum b-value to include
               * ``max_bval`` (float): the maximum b-value to include

            If the method ``_get_suitable_volume_indices`` is overwritten, this does nothing.

        prior (str, mot.model_building.utils.ModelPrior or None): a model wide prior. This is used in conjunction with
            the compartment priors and the parameter priors. If a string is given we will automatically construct a
            :class:`mot.model_building.utils.ModelPrior` from that string.
    """
    name = ''
    in_vivo_suitable = True
    ex_vivo_suitable = True
    description = ''
    post_optimization_modifiers = []
    model_expression = ''
    evaluation_model = 'OffsetGaussian'
    signal_noise_model = None
    inits = {}
    fixes = {}
    upper_bounds = {}
    lower_bounds = {}
    enforce_weights_sum_to_one = True
    volume_selection = None
    prior = None

    @classmethod
    def meta_info(cls):
        meta_info = deepcopy(ComponentConfig.meta_info())
        meta_info.update({'name': cls.name,
                          'in_vivo_suitable': cls.in_vivo_suitable,
                          'ex_vivo_suitable': cls.ex_vivo_suitable,
                          'description': cls.description})
        return meta_info


class DMRICompositeModelBuilder(ComponentBuilder):

    def create_class(self, template):
        """Creates classes with as base class DMRICompositeModel

        Args:
            template (DMRICompositeModelConfig): the composite model config template
                to use for creating the class with the right init settings.
        """
        class AutoCreatedDMRICompositeModel(method_binding_meta(template, DMRICompositeModel)):

            def __init__(self):
                super(AutoCreatedDMRICompositeModel, self).__init__(
                    deepcopy(template.name),
                    CompartmentModelTree(parse(template.model_expression)),
                    deepcopy(_resolve_evaluation_model(template.evaluation_model)),
                    signal_noise_model=deepcopy(template.signal_noise_model),
                    enforce_weights_sum_to_one=template.enforce_weights_sum_to_one)

                self.add_post_optimization_modifiers(deepcopy(template.post_optimization_modifiers))

                for full_param_name, value in template.inits.items():
                    self.init(full_param_name, deepcopy(value))

                for full_param_name, value in template.fixes.items():
                    self.fix(full_param_name, deepcopy(value))

                for full_param_name, value in template.lower_bounds.items():
                    self.set_lower_bound(full_param_name, deepcopy(value))

                for full_param_name, value in template.upper_bounds.items():
                    self.set_upper_bound(full_param_name, deepcopy(value))

                self.nmr_parameters_for_bic_calculation = self.get_nmr_estimable_parameters()

                self._model_priors.extend(_resolve_model_prior(
                    template.prior, self._model_functions_info.get_model_parameter_list()))

                self._model_priors.extend(_convert_compartment_priors_to_model_priors(
                    self._model_functions_info.get_model_list()))


            def _get_suitable_volume_indices(self, problem_data):
                volume_selection = template.volume_selection

                if not volume_selection:
                    return super(AutoCreatedDMRICompositeModel, self)._get_suitable_volume_indices(problem_data)

                use_unweighted = volume_selection.get('use_unweighted', True)
                use_weighted = volume_selection.get('use_weighted', True)
                unweighted_threshold = volume_selection.get('unweighted_threshold', 25e6)

                protocol = problem_data.protocol

                if protocol.has_column('g') and protocol.has_column('b'):
                    if use_weighted:
                        if 'min_bval' in volume_selection and 'max_bval' in volume_selection:
                            protocol_indices = protocol.get_indices_bval_in_range(start=volume_selection['min_bval'],
                                                                                  end=volume_selection['max_bval'])
                        else:
                            protocol_indices = protocol.get_weighted_indices(unweighted_threshold)
                    else:
                        protocol_indices = []

                    if use_unweighted:
                        protocol_indices = list(protocol_indices) + \
                                           list(protocol.get_unweighted_indices(unweighted_threshold))
                else:
                    return list(range(protocol.length))

                return np.unique(protocol_indices)

        return AutoCreatedDMRICompositeModel


def _resolve_evaluation_model(evaluation_model):
    """Resolve the evaluation model from string if necessary.

    The composite models accept evaluation models from string and evaluation models as object. This function
    resolves the strings if a string is given, else it returns the object passed.

    Args:
        evaluation_model (str or object): the evaluation model to resolve to an object

    Returns:
        mot.model_building.evaluation_models.EvaluationModel: the evaluation model to use
    """
    if isinstance(evaluation_model, six.string_types):
        return get_component_class('evaluation_models', evaluation_model + 'EvaluationModel')()
    else:
        return evaluation_model


def _resolve_model_prior(prior, model_parameters):
    """Resolve the model priors.

    Args:
        model_prior (None or str or mot.model_building.utils.ModelPrior): the prior defined in the composite model
            template.
        model_parameters (str): the (model, parameter) tuple for all the parameters in the model

    Returns:
        list of mot.model_building.utils.ModelPrior: list of model priors
    """
    if prior is None:
        return []

    if isinstance(prior, ModelPrior):
        return [prior]

    parameters = []
    for m, p in model_parameters:
        dotted_name = '{}.{}'.format(m.name, p.name)
        bar_name = dotted_name.replace('.', '_')

        if dotted_name in prior:
            prior = prior.replace(dotted_name, bar_name)
            parameters.append(dotted_name)
        elif bar_name in prior:
            parameters.append(dotted_name)

    return [SimpleModelPrior(prior, parameters, 'model_prior')]


def _convert_compartment_priors_to_model_priors(compartments):
    """Convert the compartment prior to model priors for use in the composite model.

    The compartment priors (and the parameters there-in) are defined only relative to the given compartment.
    This function converts these priors to ModelPriors to make the parameters absolutely named.
    """
    priors = []
    for compartment in compartments:
        if hasattr(compartment, 'prior') and compartment.prior:
            priors.append(_CompartmentToModelPrior(compartment.prior, compartment.name))
    return priors


class _CompartmentToModelPrior(ModelPrior):
    def __init__(self, compartment_prior, compartment_name):
        """Simple prior class for easily converting the compartment priors to model priors"""
        self._prior_function = compartment_prior.get_prior_function()
        self._parameters = ['{}.{}'.format(compartment_name, p)
                            for p in compartment_prior.get_function_parameters()]
        self._function_name = compartment_prior.get_prior_function_name()

    def get_prior_function(self):
        return self._prior_function

    def get_function_parameters(self):
        return self._parameters

    def get_function_name(self):
        return self._function_name
