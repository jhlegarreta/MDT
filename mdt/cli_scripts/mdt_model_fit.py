#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
import argparse
import os
import mdt
from argcomplete.completers import FilesCompleter

from mdt.shell_utils import BasicShellApplication
from mot import cl_environments
import textwrap

__author__ = 'Robbert Harms'
__date__ = "2015-08-18"
__maintainer__ = "Robbert Harms"
__email__ = "robbert.harms@maastrichtuniversity.nl"


class ModelFit(BasicShellApplication):

    def _get_arg_parser(self):
        description = "Fit one of the models to the given data."
        description += mdt.shell_utils.get_citation_message()

        epilog = textwrap.dedent("""
            Examples of use:
                mdt-model-fit "BallStick (Cascade)" data.nii.gz data.prtcl roi_mask_0_50.nii.gz
                mdt-model-fit "BallStick (Cascade)" data.nii.gz data.prtcl data_mask.nii.gz
                mdt-model-fit "BallStick (Cascade)" data.nii.gz data.prtcl data_mask.nii.gz --no-recalculate
                mdt-model-fit "BallStick (Cascade)" data.nii.gz data.prtcl data_mask.nii.gz --cl-device-ind 1
                mdt-model-fit "BallStick (Cascade)" data.nii.gz data.prtcl data_mask.nii.gz --cl-device-ind {0, 1}
        """)

        available_devices = list((ind for ind, env in enumerate(cl_environments.CLEnvironmentFactory.all_devices())))

        parser = argparse.ArgumentParser(description=description, epilog=epilog,
                                         formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument('model', metavar='model', choices=mdt.get_models_list(),
                            help='model name, see mdt-list-models')
        parser.add_argument('dwi',
                            action=mdt.shell_utils.get_argparse_extension_checker(['.nii', '.nii.gz', '.hdr', '.img']),
                            help='the diffusion weighted image').completer = FilesCompleter(['nii', 'gz', 'hdr', 'img'],
                                                                                            directories=False)
        parser.add_argument('protocol',
                            action=mdt.shell_utils.get_argparse_extension_checker(['.prtcl']),
                            help='the protocol file, see mdt-generate-protocol').completer = FilesCompleter(['prtcl'],
                                                                                 directories=False)
        parser.add_argument('mask',
                            action=mdt.shell_utils.get_argparse_extension_checker(['.nii', '.nii.gz', '.hdr', '.img']),
                            help='the (brain) mask to use').completer = FilesCompleter(['nii', 'gz', 'hdr', 'img'],
                                                                               directories=False)
        parser.add_argument('-o', '--output_folder',
                            help='the directory for the output, defaults to "output/<mask_name>" '
                                 'in the same directory as the dwi volume').completer = FilesCompleter()

        parser.add_argument('--cl-device-ind', type=int, nargs='*', choices=available_devices,
                            help="The index of the device we would like to use. This follows the indices "
                                 "in mdt-list-devices and defaults to the first GPU.")

        parser.add_argument('--gradient-deviations',
                            action=mdt.shell_utils.get_argparse_extension_checker(['.nii', '.nii.gz', '.hdr', '.img']),
                            help="The volume with the gradient deviations to use, in HCP WUMINN format.").\
            completer = FilesCompleter(['nii', 'gz', 'hdr', 'img'], directories=False)

        parser.add_argument('--recalculate', dest='recalculate', action='store_true',
                            help="Recalculate the model(s) if the output exists. (default)")
        parser.add_argument('--no-recalculate', dest='recalculate', action='store_false',
                            help="Do not recalculate the model(s) if the output exists.")
        parser.set_defaults(recalculate=True)

        parser.add_argument('--only-recalculate-last', dest='only_recalculate_last', action='store_true',
                            help="Only recalculate the last model in a cascade. (default)")
        parser.add_argument('--recalculate-all', dest='only_recalculate_last', action='store_false',
                            help="Recalculate all models in a cascade.")
        parser.set_defaults(only_recalculate_last=True)

        parser.add_argument('--double', dest='double_precision', action='store_true',
                            help="Calculate in double precision.")
        parser.add_argument('--float', dest='double_precision', action='store_false',
                            help="Calculate in single precision. (default)")
        parser.set_defaults(double_precision=False)

        return parser

    def run(self, args):
        mask_name = os.path.splitext(os.path.basename(os.path.realpath(args.mask)))[0]
        mask_name = mask_name.replace('.nii', '')
        output_folder = args.output_folder or os.path.join(os.path.dirname(args.dwi), 'output', mask_name)

        mdt.fit_model(args.model,
                      mdt.load_problem_data(os.path.realpath(args.dwi),
                                            os.path.realpath(args.protocol),
                                            os.path.realpath(args.mask)),
                      output_folder, recalculate=args.recalculate,
                      only_recalculate_last=args.only_recalculate_last, cl_device_ind=args.cl_device_ind,
                      double_precision=args.double_precision, gradient_deviations=args.gradient_deviations)


if __name__ == '__main__':
    ModelFit().start()