# -*- coding: UTF-8 -*-

'''
Module
    gen_stm8_command_test.py
Info
    Unit tests for GenSTM8CommandDefinition and GenSTM8CommandExecutor.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from gen_stm8.core.service.iservice import IService
from gen_stm8.infrastructure.command.gen_stm8_command_definition import GenSTM8CommandDefinition
from gen_stm8.infrastructure.command.gen_stm8_command_executor import GenSTM8CommandExecutor


class TestGenSTM8Command(unittest.TestCase):

    def test_definition(self) -> None:
        definition = GenSTM8CommandDefinition()
        self.assertEqual(definition.name, 'create')
        self.assertEqual(definition.help_text, 'Generate STM8 project skeleton')
        self.assertEqual(len(definition.options), 2)
        self.assertTrue(isinstance(str(definition), str))

    def test_executor_execute_success(self) -> None:
        definition = GenSTM8CommandDefinition()
        executor = GenSTM8CommandExecutor(definition)
        
        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = True
        mock_service.execute.return_value = {'returncode': 0}
        
        params = {'name': 'test', 'output': '.'}
        result = executor.execute(params=params, service=mock_service)
        
        self.assertEqual(result['returncode'], 0)
        mock_service.execute.assert_called_once_with(params=params)

    def test_executor_execute_not_initialized(self) -> None:
        definition = GenSTM8CommandDefinition()
        executor = GenSTM8CommandExecutor(definition)
        
        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = False
        
        result = executor.execute(params={}, service=mock_service)
        self.assertEqual(result['returncode'], 1)
        self.assertIn('service not initialized', result['stderr'])

    def test_executor_str_representation(self) -> None:
        definition = GenSTM8CommandDefinition()
        executor = GenSTM8CommandExecutor(definition)
        self.assertTrue(isinstance(str(executor), str))
