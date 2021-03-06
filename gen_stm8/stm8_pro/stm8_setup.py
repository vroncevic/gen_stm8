# -*- coding: UTF-8 -*-

"""
 Module
     stm8_setup.py
 Copyright
     Copyright (C) 2019 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Define class STM8Setup with attribute(s) and method(s).
     Generate STM8 project skeleton.
"""

import sys
from inspect import stack

try:
    from gen_stm8.stm8_pro.read_template import ReadTemplate
    from gen_stm8.stm8_pro.write_template import WriteTemplate
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2019, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class STM8Setup(object):
    """
        Define class STM8Setup with attribute(s) and method(s).
        Generate STM8 project skeleton.
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | __reader - Reader API
                | __writer - Writer API
            :methods:
                | __init__ - Initial constructor
                | get_reader - Getter for template reader
                | get_writer - Getter for template writer
                | gen_pro_setup - Generate project skeleton
    """

    __slots__ = ('VERBOSE', '__reader', '__writer')
    VERBOSE = 'GEN_STM8::STM8_PRO::STM8_SETUP'

    def __init__(self, verbose=False):
        """
            Initial constructor.

            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(STM8Setup.VERBOSE, verbose, 'Initial setup')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)

    def get_reader(self):
        """
            Getter for template reader.

            :return: Template reader object
            :rtype: <ReadTemplate>
            :exceptions: None
        """
        return self.__reader

    def get_writer(self):
        """
            Getter for template writer.

            :return: Template writer object
            :rtype: <WriteTemplate>
            :exceptions: None
        """
        return self.__writer

    def gen_pro_setup(self, project_name, verbose=False):
        """
            Generate project structure.

            :param project_name: PRoject name
            :type project_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func, status, project_data = stack()[0][3], False, {}
        project_txt = 'Argument: expected project_name <str> object'
        project_msg = "{0} {1} {2}".format('def', func, project_txt)
        if project_name is None or not project_name:
            raise ATSBadCallError(project_msg)
        if not isinstance(project_name, str):
            raise ATSTypeError(project_msg)
        verbose_message(
            STM8Setup.VERBOSE, verbose, 'Generating project', project_name
        )
        project_data['templates'] = self.__reader.read(verbose=verbose)
        project_data['name'] = project_name
        if project_data:
            status = self.__writer.write(project_data, verbose=verbose)
        return True if status else False
