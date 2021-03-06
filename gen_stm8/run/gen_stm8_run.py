#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
 Module
     gen_stm8_run.py
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
     Main entry point for tool gen_stm8.
"""

import sys

try:
    from gen_stm8 import GenSTM8
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2019, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


if __name__ == '__main__':
    TOOL = GenSTM8(verbose=False)
    TOOL.process(verbose=False)
