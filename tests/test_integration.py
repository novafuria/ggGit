"""
Integration tests for ggGit base structure.

This module contains integration tests that validate the interaction
between different components of the ggGit system. These tests ensure
that the base structure works correctly as a whole and that future
implementations will integrate seamlessly.

Integration tests focus on:
- Component initialization and interaction
- BaseCommand pattern usage
- Error handling across components
- Configuration loading and validation
- Git operations integration
"""

import pytest
from pathlib import Path
from unittest.mock import patch, Mock
import tempfile
import shutil

from src.core.base_commands.base import BaseCommand
from src.core.config import ConfigManager
from src.core.git import GitInterface
from src.core.validation import ArgumentValidator
from src.core.utils.colors import ColorManager
from src.core.utils.logging import LoggingManager


class TestBaseCommandIntegration:
    """Integration tests for BaseCommand and its components."""
    
    def test_base_command_initialization(self, concrete_command):
        """Test that BaseCommand initializes all components correctly."""
        # Verify all components are initialized
        assert hasattr(concrete_command, 'config')
        assert hasattr(concrete_command, 'git')
        assert hasattr(concrete_command, 'validator')
        assert hasattr(concrete_command, 'logger')
        
        # Verify component types
        assert isinstance(concrete_command.config, ConfigManager)
        assert isinstance(concrete_command.git, GitInterface)
        assert isinstance(concrete_command.validator, ArgumentValidator)
        assert isinstance(concrete_command.logger, LoggingManager)
    
    def test_base_command_info_retrieval(self, concrete_command):
        """Test that BaseCommand provides correct information."""
        info = concrete_command.get_command_info()
        
        # Verify required keys are present
        required_keys = [
            'command_class', 'module', 'has_config', 
            'has_git', 'has_validator', 'has_logger'
        ]
        for key in required_keys:
            assert key in info, f"Missing key: {key}"
        
        # Verify values
        assert info['command_class'] == 'ConcreteCommand'
        assert info['has_config'] is True
        assert info['has_git'] is True
        assert info['has_validator'] is True
        assert info['has_logger'] is True
    
    def test_base_command_error_handling(self, concrete_command, mock_click_echo):
        """Test that BaseCommand handles errors correctly."""
        class FailingCommand(BaseCommand):
            def execute(self, *args, **kwargs):
                raise ValueError("Test error")
        
        failing_command = FailingCommand()
        result = failing_command.run("test_arg")
        
        # Verify error handling
        assert result == 1
        mock_click_echo.assert_called_once()
        
        # Verify error message format
        call_args = mock_click_echo.call_args[0][0]
        assert "Error: Test error" in call_args
    
    def test_base_command_successful_execution(self, concrete_command):
        """Test that BaseCommand executes successfully."""
        result = concrete_command.run("test_arg", key="value")
        assert result == 0


class TestComponentIntegration:
    """Integration tests for component interaction."""
    
    def test_config_manager_integration(self, config_manager, sample_config_data):
        """Test ConfigManager integration with other components."""
        # Test that ConfigManager can be initialized
        assert isinstance(config_manager, ConfigManager)
        assert hasattr(config_manager, 'config')
        assert hasattr(config_manager, 'config_paths')
        
        # Test configuration path structure
        paths = config_manager.config_paths
        assert len(paths) == 4  # repo, module, user, default
        assert ".gggit/repo-config.yaml" in paths[0]
        assert "user-config.yaml" in paths[2]
    
    def test_git_interface_integration(self, git_interface, mock_subprocess):
        """Test GitInterface integration with subprocess."""
        # Test that GitInterface can be initialized
        assert isinstance(git_interface, GitInterface)
        
        # Test basic methods exist and return expected types
        assert isinstance(git_interface.is_git_repository(), bool)
        assert isinstance(git_interface.get_current_branch(), (str, type(None)))
        assert isinstance(git_interface.get_staged_files(), list)
        assert isinstance(git_interface.get_unstaged_files(), list)
        assert isinstance(git_interface.get_repository_status(), dict)
    
    def test_argument_validator_integration(self, argument_validator, sample_validation_data):
        """Test ArgumentValidator integration with validation data."""
        assert isinstance(argument_validator, ArgumentValidator)
        
        # Test commit message validation
        valid_messages = sample_validation_data['valid_commit_messages']
        for message in valid_messages:
            # Should not raise exception for valid messages
            try:
                result = argument_validator.validate_commit_message(message)
                assert result is True
            except ValueError:
                pytest.fail(f"Valid message failed validation: {message}")
        
        # Test invalid messages (only length validation is currently implemented)
        invalid_messages = ["", "a" * 100]  # Empty and too long
        for message in invalid_messages:
            try:
                argument_validator.validate_commit_message(message)
                pytest.fail(f"Expected ValueError for message: {message}")
            except ValueError:
                pass  # Expected behavior
    
    def test_color_manager_integration(self, color_manager, mock_click_style):
        """Test ColorManager integration with click."""
        assert isinstance(color_manager, ColorManager)
        
        # Test all color methods exist and return strings
        methods = ['success', 'error', 'warning', 'info', 'operation', 'highlight', 'dim']
        for method_name in methods:
            method = getattr(color_manager, method_name)
            result = method("test message")
            assert isinstance(result, str)
            # Since we're mocking click.style, we expect the mocked return value
            assert result == "styled_message"
    
    def test_logging_manager_integration(self, logging_manager, mock_logging):
        """Test LoggingManager integration with logging module."""
        assert isinstance(logging_manager, LoggingManager)
        assert hasattr(logging_manager, 'log_level')
        assert hasattr(logging_manager, 'log_dir')
        
        # Test logger creation
        logger = logging_manager.get_logger("test_module")
        assert logger is not None


class TestCommandPatternIntegration:
    """Integration tests for command pattern usage."""
    
    def test_commit_command_integration(self):
        """Test CommitCommand integration with BaseCommand."""
        from src.core.base_commands.commit import CommitCommand
        
        # Test initialization
        commit_cmd = CommitCommand("feat")
        assert isinstance(commit_cmd, BaseCommand)
        assert commit_cmd.commit_type == "feat"
        
        # Test message formatting
        message = commit_cmd.format_commit_message("add feature", "auth")
        assert message == "feat(auth): add feature"
        
        message_no_scope = commit_cmd.format_commit_message("add feature")
        assert message_no_scope == "feat: add feature"
    
    def test_config_command_integration(self):
        """Test ConfigCommand integration with BaseCommand."""
        from src.core.base_commands.config import ConfigCommand
        
        # Test initialization
        config_cmd = ConfigCommand()
        assert isinstance(config_cmd, BaseCommand)
        
        # Test configuration access methods exist
        assert hasattr(config_cmd, 'get_config_value')
        assert hasattr(config_cmd, 'set_config_value')
        assert hasattr(config_cmd, 'list_config')


class TestErrorHandlingIntegration:
    """Integration tests for error handling across components."""
    
    def test_error_propagation_through_base_command(self, concrete_command, mock_click_echo):
        """Test that errors propagate correctly through BaseCommand."""
        class ErrorCommand(BaseCommand):
            def execute(self, *args, **kwargs):
                raise RuntimeError("Integration test error")
        
        error_command = ErrorCommand()
        result = error_command.run("test")
        
        # Verify error is handled
        assert result == 1
        mock_click_echo.assert_called_once()
        
        # Verify error message contains the original error
        call_args = mock_click_echo.call_args[0][0]
        assert "Integration test error" in call_args
    
    def test_validation_error_handling(self, argument_validator):
        """Test that validation errors are handled correctly."""
        # Test empty commit message
        with pytest.raises(ValueError, match="Commit message cannot be empty"):
            argument_validator.validate_commit_message("")
        
        # Test long commit message
        long_message = "a" * 100
        with pytest.raises(ValueError, match="Commit message too long"):
            argument_validator.validate_commit_message(long_message)
        
        # Test invalid scope
        with pytest.raises(ValueError, match="Scope must contain only lowercase letters"):
            argument_validator.validate_scope("Invalid-Scope")


class TestConfigurationIntegration:
    """Integration tests for configuration system."""
    
    def test_configuration_loading_structure(self, config_manager):
        """Test that configuration loading structure is correct."""
        # Test that configuration paths are properly structured
        paths = config_manager.config_paths
        
        # Verify priority order (highest to lowest)
        assert "repo-config.yaml" in paths[0]  # Repository config
        assert "modules" in paths[1]  # Module configs
        assert "user-config.yaml" in paths[2]  # User config
        assert "default-config.yaml" in paths[3]  # Default config
    
    def test_configuration_methods_exist(self, config_manager):
        """Test that all configuration methods exist and are callable."""
        methods = [
            'load_hierarchical_config',
            'get_config',
            'set_config',
            'validate_config',
            'get_config_level',
            'list_config_keys',
            'reset_config'
        ]
        
        for method_name in methods:
            method = getattr(config_manager, method_name)
            assert callable(method), f"Method {method_name} is not callable"


class TestGitIntegration:
    """Integration tests for Git operations."""
    
    def test_git_interface_methods_exist(self, git_interface):
        """Test that all Git interface methods exist and are callable."""
        methods = [
            'is_git_repository',
            'stage_all_changes',
            'stage_files',
            'commit',
            'get_current_branch',
            'get_staged_files',
            'get_unstaged_files',
            'get_repository_status',
            'get_commit_history',
            'create_branch',
            'switch_branch'
        ]
        
        for method_name in methods:
            method = getattr(git_interface, method_name)
            assert callable(method), f"Method {method_name} is not callable"
    
    def test_git_interface_return_types(self, git_interface):
        """Test that Git interface methods return correct types."""
        # Test boolean methods
        assert isinstance(git_interface.is_git_repository(), bool)
        assert isinstance(git_interface.stage_all_changes(), bool)
        assert isinstance(git_interface.stage_files([]), bool)
        assert isinstance(git_interface.commit("test"), bool)
        
        # Test string methods
        branch = git_interface.get_current_branch()
        assert isinstance(branch, (str, type(None)))
        
        # Test list methods
        staged = git_interface.get_staged_files()
        unstaged = git_interface.get_unstaged_files()
        history = git_interface.get_commit_history()
        
        assert isinstance(staged, list)
        assert isinstance(unstaged, list)
        assert isinstance(history, list)
        
        # Test dict methods
        status = git_interface.get_repository_status()
        assert isinstance(status, dict)


@pytest.mark.integration
class TestEndToEndIntegration:
    """End-to-end integration tests."""
    
    def test_full_command_execution_flow(self, concrete_command, mock_click_echo):
        """Test the complete command execution flow."""
        # Test successful execution
        result = concrete_command.run("test_arg", key="value")
        assert result == 0
        
        # Test that setup_logging was called (implicitly)
        # This is verified by the fact that no errors occurred
    
    def test_error_flow_integration(self, mock_click_echo):
        """Test complete error handling flow."""
        class ErrorCommand(BaseCommand):
            def execute(self, *args, **kwargs):
                raise ValueError("End-to-end test error")
        
        error_command = ErrorCommand()
        result = error_command.run("test")
        
        # Verify complete error handling
        assert result == 1
        mock_click_echo.assert_called_once()
        
        # Verify error message format
        call_args = mock_click_echo.call_args[0][0]
        assert "Error: End-to-end test error" in call_args
