from mdt.models.compartments import CompartmentConfig, CLCodeFromAdjacentFile
from mdt.components_loader import CompartmentModelsLoader, bound_function

__author__ = 'Robbert Harms'
__date__ = "2015-06-21"
__maintainer__ = "Robbert Harms"
__email__ = "robbert.harms@maastrichtuniversity.nl"


compartment_loader = CompartmentModelsLoader()


class GDRCylindersFixedRadii(CompartmentConfig):

    name = 'GDRCylindersFixedRadii'
    cl_function_name = 'cmGDRCylindersFixedRadii'
    parameter_list = ('g', 'G', 'Delta', 'delta', 'd', 'theta', 'phi', 'gamma_radii',
                      'gamma_cyl_weights', 'nmr_gamma_cyl_weights')
    dependency_list = (compartment_loader.load('CylinderGPD'),)

    @bound_function
    def get_extra_results_maps(self, results_dict):
        return self._get_vector_result_maps(results_dict[self.name + '.theta'],
                                            results_dict[self.name + '.phi'])
