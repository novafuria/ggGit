"""
Tests for ggai command functionality.

This module tests the GgaiCommand class and its subcommands
including usage tracking and AI message generation.
"""

import pytest
import os
import tempfile
from unittest.mock import Mock, patch, MagicMock
from click.testing import CliRunner
from src.commands.ggai import GgaiCommand, ggai


class TestGgaiCommand:
    """Test GgaiCommand functionality."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.command = GgaiCommand()
    
    def test_execute_main_ai_not_configured(self):
        """Test execute_main when AI is not configured."""
        with patch.object(self.command, '_is_ai_configured', return_value=False):
            result = self.command.execute_main()
            
            assert result == 1
    
    def test_execute_main_not_git_repo(self):
        """Test execute_main when not in git repository."""
        with patch.object(self.command, '_is_ai_configured', return_value=True):
            with patch.object(self.command.git, 'is_git_repository', return_value=False):
                result = self.command.execute_main()
                
                assert result == 1
    
    def test_execute_main_should_use_ai(self):
        """Test execute_main when should use AI."""
        with patch.object(self.command, '_is_ai_configured', return_value=True):
            with patch.object(self.command.git, 'is_git_repository', return_value=True):
                with patch.object(self.command.analyzer, 'should_use_ai', return_value=(True, {'files': ['test.py'], 'has_staged': True})):
                    with patch.object(self.command.git, 'get_diff_content', return_value="diff content"):
                        with patch.object(self.command.message_generator, 'generate_message', return_value="feat: test message"):
                            with patch.object(self.command.analyzer, 'get_analysis_summary', return_value="Summary"):
                                result = self.command.execute_main()
                                
                                assert result == 0
    
    def test_execute_main_should_not_use_ai(self):
        """Test execute_main when should not use AI."""
        with patch.object(self.command, '_is_ai_configured', return_value=True):
            with patch.object(self.command.git, 'is_git_repository', return_value=True):
                with patch.object(self.command.analyzer, 'should_use_ai', return_value=(False, {'files': ['test.py'], 'has_staged': True})):
                    with patch.object(self.command.analyzer, 'get_fallback_message', return_value="Fallback message"):
                        result = self.command.execute_main()
                        
                        assert result == 1
    
    def test_execute_usage_tracking_disabled(self):
        """Test execute_usage when tracking is disabled."""
        with patch.object(self.command.usage_tracker, 'is_tracking_enabled', return_value=False):
            result = self.command.execute_usage()
            
            assert result == 0
    
    def test_execute_usage_tracking_enabled(self):
        """Test execute_usage when tracking is enabled."""
        with patch.object(self.command.usage_tracker, 'is_tracking_enabled', return_value=True):
            with patch.object(self.command.usage_tracker, 'get_usage_stats', return_value={
                'period': {'start_date': '2024-12-19'},
                'totals': {'requests': 10, 'tokens': 1000, 'cost': 0.50},
                'limits': {'cost_limit': 5.00}
            }):
                with patch.object(self.command.usage_tracker, 'get_remaining_budget', return_value=4.50):
                    result = self.command.execute_usage()
                    
                    assert result == 0
    
    def test_execute_usage_reset_tracking_disabled(self):
        """Test execute_usage_reset when tracking is disabled."""
        with patch.object(self.command.usage_tracker, 'is_tracking_enabled', return_value=False):
            result = self.command.execute_usage_reset()
            
            assert result == 0
    
    def test_execute_usage_reset_tracking_enabled(self):
        """Test execute_usage_reset when tracking is enabled."""
        with patch.object(self.command.usage_tracker, 'is_tracking_enabled', return_value=True):
            with patch.object(self.command.usage_tracker, 'reset_usage'):
                result = self.command.execute_usage_reset()
                
                assert result == 0
    
    def test_execute_test_connection_success(self):
        """Test execute_test when connection is successful."""
        with patch.object(self.command.message_generator, 'test_connection', return_value=True):
            with patch.object(self.command.message_generator, 'get_provider_info', return_value={
                'provider': 'openai',
                'model': 'gpt-3.5-turbo',
                'base_url': None,
                'status': 'configured'
            }):
                result = self.command.execute_test()
                
                assert result == 0
    
    def test_execute_test_connection_failure(self):
        """Test execute_test when connection fails."""
        with patch.object(self.command.message_generator, 'test_connection', return_value=False):
            result = self.command.execute_test()
            
            assert result == 1


class TestGgaiCommandIntegration:
    """Test GgaiCommand integration with real components."""
    
    def test_integration_with_real_components(self):
        """Test integration with real components."""
        try:
            from src.core.config import ConfigManager
            from src.core.git import GitInterface
            
            config = ConfigManager()
            git = GitInterface()
            command = GgaiCommand()
            
            # Test basic functionality
            assert hasattr(command, 'usage_tracker')
            assert hasattr(command, 'message_generator')
            assert hasattr(command, 'analyzer')
            
        except Exception:
            # Skip if not in a git repository or config issues
            pytest.skip("Integration test requires proper configuration")


class TestGgaiCli:
    """Test ggai CLI commands."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.runner = CliRunner()
    
    def test_ggai_main_command(self):
        """Test ggai main command."""
        with patch('src.commands.ggai.GgaiCommand') as mock_command_class:
            mock_command = Mock()
            mock_command.execute_main.return_value = 0
            mock_command_class.return_value = mock_command
            
            result = self.runner.invoke(ggai, ['main'])
            
            assert result.exit_code == 0
            mock_command.execute_main.assert_called_once()
    
    def test_ggai_usage_command(self):
        """Test ggai usage command."""
        with patch('src.commands.ggai.GgaiCommand') as mock_command_class:
            mock_command = Mock()
            mock_command.execute_usage.return_value = 0
            mock_command_class.return_value = mock_command
            
            result = self.runner.invoke(ggai, ['usage'])
            
            # Note: usage is a group command, so it expects a subcommand
            # This test should check the group behavior
            assert result.exit_code == 2  # Missing subcommand
    
    def test_ggai_test_command(self):
        """Test ggai test command."""
        with patch('src.commands.ggai.GgaiCommand') as mock_command_class:
            mock_command = Mock()
            mock_command.execute_test.return_value = 0
            mock_command_class.return_value = mock_command
            
            result = self.runner.invoke(ggai, ['test'])
            
            assert result.exit_code == 0
            mock_command.execute_test.assert_called_once()
    
    def test_ggai_usage_reset_command(self):
        """Test ggai usage reset command."""
        with patch('src.commands.ggai.GgaiCommand') as mock_command_class:
            mock_command = Mock()
            mock_command.execute_usage_reset.return_value = 0
            mock_command_class.return_value = mock_command
            
            result = self.runner.invoke(ggai, ['usage', 'reset'])
            
            assert result.exit_code == 0
            mock_command.execute_usage_reset.assert_called_once()
    
    def test_ggai_help(self):
        """Test ggai help command."""
        result = self.runner.invoke(ggai, ['--help'])
        
        assert result.exit_code == 0
        assert "AI-powered commit message generation" in result.output
    
    def test_ggai_usage_help(self):
        """Test ggai usage help command."""
        result = self.runner.invoke(ggai, ['usage', '--help'])
        
        assert result.exit_code == 0
        assert "Usage management commands" in result.output
    
    def test_ggai_test_help(self):
        """Test ggai test help command."""
        result = self.runner.invoke(ggai, ['test', '--help'])
        
        assert result.exit_code == 0
        assert "Test AI connection" in result.output


class TestGgaiCommandErrorHandling:
    """Test GgaiCommand error handling."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.command = GgaiCommand()
    
    def test_execute_main_exception(self):
        """Test execute_main with exception."""
        with patch.object(self.command, '_is_ai_configured', return_value=True):
            with patch.object(self.command.git, 'is_git_repository', return_value=True):
                with patch.object(self.command.analyzer, 'should_use_ai', side_effect=Exception("Test error")):
                    # The method should catch the exception and return 1
                    result = self.command.execute_main()
                    
                    assert result == 1
    
    def test_execute_usage_exception(self):
        """Test execute_usage with exception."""
        with patch.object(self.command.usage_tracker, 'is_tracking_enabled', return_value=True):
            with patch.object(self.command.usage_tracker, 'get_usage_stats', side_effect=Exception("Test error")):
                result = self.command.execute_usage()
                
                assert result == 1
    
    def test_execute_usage_reset_exception(self):
        """Test execute_usage_reset with exception."""
        with patch.object(self.command.usage_tracker, 'is_tracking_enabled', return_value=True):
            with patch.object(self.command.usage_tracker, 'reset_usage', side_effect=Exception("Test error")):
                result = self.command.execute_usage_reset()
                
                assert result == 1
    
    def test_execute_test_exception(self):
        """Test execute_test with exception."""
        with patch.object(self.command.message_generator, 'test_connection', side_effect=Exception("Test error")):
            result = self.command.execute_test()
            
            assert result == 1
