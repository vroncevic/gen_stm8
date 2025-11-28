#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Module
    setup.py
Copyright
    Copyright (C) 2018 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines setup for tool gen_stm8.
'''

from __future__ import print_function
from typing import List, Optional
from os.path import abspath, dirname, join
from setuptools import setup

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_stm8'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_stm8/blob/dev/LICENSE'
__version__: str = '1.4.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

TOOL_DIR: str = 'gen_stm8/'
CONF: str = 'conf'
TEMPLATE: str = 'conf/template'
LOG: str = 'log'
THIS_DIR: str = abspath(dirname(__file__))
long_description: Optional[str] = None
with open(join(THIS_DIR, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()
PROGRAMMING_LANG: str = 'Programming Language :: Python ::'
VERSIONS: List[str] = ['3.10', '3.11', '3.12']
SUPPORTED_PY_VERSIONS: List[str] = [
    f'{PROGRAMMING_LANG} {VERSION}' for VERSION in VERSIONS
]
PYP_CLASSIFIERS: List[str] = SUPPORTED_PY_VERSIONS
setup(
    name='gen_stm8',
    version='1.4.7',
    description='STM8 project skeleton generator',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_stm8/',
    license='GPL-3.0-or-later',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='STM, STM8, project, C, Unix, Linux',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=['gen_stm8', 'gen_stm8.pro'],
    install_requires=['ats-utilities'],
    package_data={
        'gen_stm8': [
            'py.typed',
            f'{CONF}/gen_stm8.logo',
            f'{CONF}/gen_stm8.cfg',
            f'{CONF}/gen_stm8_util.cfg',
            f'{CONF}/project.yaml',
            f'{TEMPLATE}/Makefile.template',
            f'{TEMPLATE}/module.template',
            f'{TEMPLATE}/stm8s.template',
            f'{LOG}/gen_stm8.log'
        ]
    },
    data_files=[
        ('/usr/local/bin/', [f'{TOOL_DIR}run/gen_stm8_run.py']),
        ('/usr/local/bin/', [f'{TOOL_DIR}run/factory_reset.sh'])
    ]
)
