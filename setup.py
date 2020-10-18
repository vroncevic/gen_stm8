#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
 Module
     setup.py
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
     Define setup for gen_stm8 package.
"""

from os.path import abspath, dirname, join
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

THIS_DIR, LONG_DESCRIPTION = abspath(dirname(__file__)), None
with open(join(THIS_DIR, 'README.md')) as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name='gen_stm8',
    version='1.0.0',
    description='STM8 project skeleton generator',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_stm8/',
    license='GPL 2020 Free software to use and distributed it.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords='STM, STM8, project, C, Unix, Linux',
    platforms='POSIX',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)'
    ],
    packages=['gen_stm8', 'gen_stm8.stm8_pro'],
    install_requires=['ats-utilities'],
    data_files=[
        ('/usr/local/bin/', ['gen_stm8/run/gen_stm8_run.py']),
        ('/usr/local/bin/', ['gen_stm8/run/factory_reset.sh']),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_stm8/conf/',
            ['gen_stm8/conf/gen_stm8.cfg']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_stm8/conf/',
            ['gen_stm8/conf/gen_stm8_util.cfg']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_stm8/conf/template/',
            ['gen_stm8/conf/template/Makefile.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_stm8/conf/template/',
            ['gen_stm8/conf/template/stm8s.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_stm8/conf/template/',
            ['gen_stm8/conf/template/module.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_stm8/conf/',
            ['gen_stm8/conf/project.yaml']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_stm8/log/',
            ['gen_stm8/log/gen_stm8.log']
        )
    ]
)
