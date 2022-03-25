# -*- coding: utf-8 -*-

'''
 Module
     __init__.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
     gen_stm8 is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     gen_stm8 is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Defined class GenSTM8 with attribute(s) and method(s).
     Load a base info, create an CLI interface and run operation(s).
'''

import sys
from os import getcwd
from os.path import dirname, realpath

try:
    from six import add_metaclass
    from gen_stm8.pro import STM8Setup
    from ats_utilities.splash import Splash
    from ats_utilities.logging import ATSLogger
    from ats_utilities.cli.cfg_cli import CfgCLI
    from ats_utilities.cooperative import CooperativeMeta
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.success import success_message
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, https://vroncevic.github.io/gen_stm8'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_stm8/blob/dev/LICENSE'
__version__ = '1.2.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@add_metaclass(CooperativeMeta)
class GenSTM8(CfgCLI):
    '''
        Defined class GenSTM8 with attribute(s) and method(s).
        Load a base info, create an CLI interface and run operation(s).
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | CONFIG - tool info file path.
                | LOG - tool log file path.
                | LOGO - logo for splash screen.
                | OPS - list of tool options.
                | logger - logger object API.
            :methods:
                | __init__ - initial constructor.
                | process - process and generate STM8 project.
                | __str__ - dunder method for GenSTM8.
    '''

    GEN_VERBOSE = 'GEN_STM8'
    CONFIG = '/conf/gen_stm8.cfg'
    LOG = '/log/gen_stm8.log'
    LOGO = '/conf/gen_stm8.logo'
    OPS = ['-g', '--gen', '-v', '--verbose', '--version']

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        current_dir = dirname(realpath(__file__))
        gen_stm8_property = {
            'ats_organization': 'vroncevic',
            'ats_repository': 'gen_stm8',
            'ats_name': 'gen_stm8',
            'ats_logo_path': '{0}{1}'.format(current_dir, GenSTM8.LOGO),
            'ats_use_github_infrastructure': True
        }
        splash = Splash(gen_stm8_property, verbose=verbose)
        base_info = '{0}{1}'.format(current_dir, GenSTM8.CONFIG)
        CfgCLI.__init__(self, base_info, verbose=verbose)
        verbose_message(GenSTM8.GEN_VERBOSE, verbose, 'init tool info')
        self.logger = ATSLogger(
            GenSTM8.GEN_VERBOSE.lower(),
            '{0}{1}'.format(current_dir, GenSTM8.LOG),
            verbose=verbose
        )
        if self.tool_operational:
            self.add_new_option(
                GenSTM8.OPS[0], GenSTM8.OPS[1], dest='gen',
                help='generate STM8 project'
            )
            self.add_new_option(
                GenSTM8.OPS[2], GenSTM8.OPS[3],
                action='store_true', default=False,
                help='activate verbose mode'
            )
            self.add_new_option(
                GenSTM8.OPS[4], action='version', version=__version__
            )

    def process(self, verbose=False):
        '''
            Process and run operation.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        status = False
        if self.tool_operational:
            num_of_args_sys = len(sys.argv)
            if num_of_args_sys > 1:
                operation = sys.argv[1]
                if operation not in GenSTM8.OPS:
                    sys.argv.append('-h')
            else:
                sys.argv.append('-h')
            args = self.parse_args(sys.argv[1:])
            project_path = '{0}/{1}'.format(getcwd(), getattr(args, 'gen'))
            project_exists = Path(project_path).exists()
            if not project_exists:
                if bool(getattr(args, 'gen')):
                    generator = STM8Setup(
                        getattr(args, 'gen'),
                        verbose=getattr(args, 'verbose') or verbose
                    )
                    print(
                        '{0} {1} [{2}]'.format(
                            '[{0}]'.format(GenSTM8.VERBOSE.lower()),
                            'generating STM8 project skeleton',
                            getattr(args, 'gen')
                        )
                    )
                    status = generator.gen_pro_setup(
                        verbose=getattr(args, 'verbose') or verbose
                    )
                    if status:
                        success_message(GenSTM8.VERBOSE, 'done\n')
                        self.logger.write_log(
                            '{0} {1} done'.format(
                                'generating STM8 project', getattr(args, 'gen')
                            ), ATSLogger.ATS_INFO
                        )
                    else:
                        error_message(GenSTM8.VERBOSE, 'generation failed')
                        self.logger.write_log(
                            'generation failed', ATSLogger.ATS_ERROR
                        )
                else:
                    error_message(GenSTM8.GEN_VERBOSE, 'provide project name')
                    self.logger.write_log(
                        'provide project name', ATSLogger.ATS_ERROR
                    )
            else:
                error_message(GenSTM8.VERBOSE, 'project already exist')
                self.logger.write_log(
                    'project already exist', ATSLogger.ATS_ERROR
                )
        else:
            error_message(GenSTM8.VERBOSE, 'tool is not operational')
            self.logger.write_log(
                'tool is not operational', ATSLogger.ATS_ERROR
            )
        return status

    def __str__(self):
        '''
            Dunder method for GenSTM8.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, CfgCLI.__str__(self), str(self.logger)
        )
