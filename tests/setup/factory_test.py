# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenSTM8BundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_stm8.setup.bundle import GenSTM8Bundle
from gen_stm8.setup.factory import GenSTM8BundleFactory


class TestGenSTM8BundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenSTM8BundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenSTM8Bundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_stm8/infrastructure/config/gen_stm8.cfg'}
        bundle = GenSTM8BundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenSTM8Bundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenSTM8BundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenSTM8BundleFactory.get_version(), '1.0.5')
