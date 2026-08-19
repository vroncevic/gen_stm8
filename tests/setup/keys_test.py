# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenSTM8BundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_stm8.setup.keys import GenSTM8BundleKeys


class TestGenSTM8BundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenSTM8BundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenSTM8BundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenSTM8BundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenSTM8BundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenSTM8BundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenSTM8BundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenSTM8BundleKeys.OPTION_INFO_FILE, opts)
