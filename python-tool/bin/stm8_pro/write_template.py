# -*- coding: UTF-8 -*-
# write_template.py
# Copyright (C) 2020 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# gen_stm8 is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gen_stm8 is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys
from inspect import stack
from os import getcwd, chmod
from string import Template

try:
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config.config_context_manager import ConfigFile
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ##################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(object):
    """
        Define class WriteTemplate with attribute(s) and method(s).
        Write template content with parameters to a project setup.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __SETUP_FILES - File names for setup project
            method:
                __init__ - Initial constructor
                write - Write a template content to a project setup
    """

    __slots__ = ('VERBOSE', '__SETUP_FILES')
    VERBOSE = 'GEN_STM8::STM8_PRO::WRITE_TEMPLATE'
    __SETUP_FILES = {
        1: 'stm8l.h', 2: 'main.c', 3: 'Makefile'
    }

    def __init__(self, verbose=False):
        """
            Initial constructor
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(WriteTemplate.VERBOSE, verbose, 'Initial writer')

    def write(self, project_content, project_name, verbose=False):
        """
            Write setup content to file.
            :param project_content: Template content for project
            :type project_content: <str>
            :param project_name: Parameter project name
            :type project_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
            :exception: ATSBadCallError | ATSTypeError
        """
        status, template = False, None
        func, current_dir = stack()[0][3], getcwd()
        setup_txt = 'First argument: expected project_content <dict> object'
        setup_msg = "{0} {1} {2}".format('def', func, setup_txt)
        project_txt = 'First argument: expected project_name <str> object'
        project_msg = "{0} {1} {2}".format('def', func, project_txt)
        if project_content is None or not project_content:
            raise ATSBadCallError(setup_msg)
        if not isinstance(project_content, dict):
            raise ATSTypeError(setup_msg)
        if project_name is None or not project_name:
            raise ATSBadCallError(project_msg)
        if not isinstance(project_name, str):
            raise ATSTypeError(project_msg)
            
        for tmp_index in WriteTemplate.__SETUP_FILES.keys():
            setup = "{0}/{1}".format(
                current_dir, WriteTemplate.__SETUP_FILES[tmp_index]
            )
            verbose_message(
                WriteTemplate.VERBOSE, verbose,
                'Write project setup file', setup
            )
            project = {'PRO': "{0}".format(project_name)}
            template = Template(project_content[tmp_index])
            if template:
                with open(setup, 'w') as setup_file:
                    setup_file.write(template.substitute(project))
                    chmod(setup, 0o666)
                    status = True
        return True if status else False
