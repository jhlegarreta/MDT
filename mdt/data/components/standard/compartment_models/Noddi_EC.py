from mdt.components_loader import bound_function
from mdt.models.compartments import CompartmentConfig, CLCodeFromAdjacentFile
from mot.cl_functions import CerfDawson

__author__ = 'Robbert Harms'
__date__ = "2015-06-21"
__maintainer__ = "Robbert Harms"
__email__ = "robbert.harms@maastrichtuniversity.nl"


class Noddi_EC(CompartmentConfig):

    name = 'Noddi_EC'
    cl_function_name = 'cmNoddi_EC'
    parameter_list = ('g', 'b', 'd', 'dperp0', 'theta', 'phi', 'kappa')
    dependency_list = (CerfDawson(),)

    @bound_function
    def get_extra_results_maps(self, results_dict):
        return self._get_vector_result_maps(results_dict[self.name + '.theta'],
                                            results_dict[self.name + '.phi'])
