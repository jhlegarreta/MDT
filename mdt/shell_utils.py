import argparse
import textwrap

import argcomplete

__author__ = 'Robbert Harms'
__date__ = "2015-10-16"
__maintainer__ = "Robbert Harms"
__email__ = "robbert.harms@maastrichtuniversity.nl"


def get_argparse_extension_checker(choices):

    class Act(argparse.Action):
        def __call__(self, parser, namespace, fname, option_string=None):
            is_valid = any(map(lambda choice: fname[-len(choice):] == choice, choices))
            if is_valid:
                setattr(namespace, self.dest, fname)
            else:
                option_string = '({})'.format(option_string) if option_string else ''
                parser.error("File doesn't end with one of {}{}".format(choices, option_string))

    return Act


class BasicShellApplication(object):

    def run(self):
        parser = self._get_arg_parser()
        argcomplete.autocomplete(parser)
        args = parser.parse_args()
        self._run(args)

    def _run(self, args):
        """Run the application with the given arguments.

        Args:
            args: the arguments from the argparser.
        """

    def _get_arg_parser(self):
        """Create the auto parser. This should be implemented by the implementing class.

        To enable autocomplete in your shell please execute activate-global-python-argcomplete in your shell.

        """
        description = textwrap.dedent("""
            Basic parser introduction here.

            Can be multiline.
        """)

        epilog = textwrap.dedent("""
            Examples of use:
                mdt-model-fit "BallStick (Cascade)" data.nii.gz data.prtcl roi_mask_0_50.nii.gz
        """)
        parser = argparse.ArgumentParser(description=description, epilog=epilog,
                                         formatter_class=argparse.RawTextHelpFormatter)
        return parser

    def _get_citation_message(self):
        return get_citation_message()


def get_citation_message():
    """The citation message used in the shell scripts.

    Returns:
        str: the citation message for use in the description of every shell script
    """
    return textwrap.dedent("""
        If you use any of the scripts/functions/tools from MDT in your research, please cite the following paper:
            <citation here>
    """)


