"""
Tests for BaseCommand class.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from src.core.base_commands.base import BaseCommand


class ConcreteCommand(BaseCommand):
    """Concrete implementation of BaseCommand for testing."""
    
    def execute(self, *args, **kwargs):
        """Concrete implementation of execute method."""
        return 0


class TestBaseCommand:
    """Test cases for BaseCommand class."""
    
    def test_init(self):
        """Test BaseCommand initialization."""
        cmd = ConcreteCommand()
        
        # Check that components are initialized
        assert hasattr(cmd, 'config')
        assert hasattr(cmd, 'git')
        assert hasattr(cmd, 'validator')
    
    def test_validate_args_default_implementation(self):
        """Test default validate_args implementation."""
        cmd = ConcreteCommand()
        result = cmd.validate_args(["arg1", "arg2"])
        
        # Default implementation should return True
        assert result is True
    
    def test_setup_logging_default_implementation(self):
        """Test default setup_logging implementation."""
        cmd = ConcreteCommand()
        
        # Should not raise any exception
        cmd.setup_logging()
    
    def test_run_success(self):
        """Test run method with successful execution."""
        cmd = ConcreteCommand()
        
        result = cmd.run("test_arg")
        
        assert result == 0
    
    def test_run_with_exception(self):
        """Test run method with exception handling."""
        class FailingCommand(BaseCommand):
            def execute(self, *args, **kwargs):
                raise ValueError("Test error")
        
        cmd = FailingCommand()
        
        with patch('click.echo') as mock_echo:
            result = cmd.run("test_arg")
        
        assert result == 1
        mock_echo.assert_called_once()
        # Check that error message contains the exception
        call_args = mock_echo.call_args[0][0]
        assert "Error: Test error" in call_args
    
    def test_run_calls_setup_logging(self):
        """Test that run method calls setup_logging."""
        cmd = ConcreteCommand()
        
        with patch.object(cmd, 'setup_logging') as mock_setup:
            cmd.run("test_arg")
        
        mock_setup.assert_called_once()
    
    def test_run_calls_execute(self):
        """Test that run method calls execute with correct arguments."""
        cmd = ConcreteCommand()
        
        with patch.object(cmd, 'execute') as mock_execute:
            mock_execute.return_value = 0
            cmd.run("arg1", "arg2", key="value")
        
        mock_execute.assert_called_once_with("arg1", "arg2", key="value")
    
    def test_abstract_method_raises_error(self):
        """Test that BaseCommand cannot be instantiated directly."""
        with pytest.raises(TypeError):
            BaseCommand()
    
    def test_concrete_command_can_be_instantiated(self):
        """Test that concrete command can be instantiated."""
        cmd = ConcreteCommand()
        assert isinstance(cmd, BaseCommand)
    
    def test_execute_must_be_implemented(self):
        """Test that execute method must be implemented in subclasses."""
        class IncompleteCommand(BaseCommand):
            pass
        
        # Should not be able to instantiate without implementing execute
        with pytest.raises(TypeError):
            IncompleteCommand()
    
    @patch('src.core.base_commands.base.ConfigManager')
    @patch('src.core.base_commands.base.GitInterface')
    @patch('src.core.base_commands.base.ArgumentValidator')
    def test_init_creates_components(self, mock_validator, mock_git, mock_config):
        """Test that __init__ creates the required components."""
        cmd = ConcreteCommand()
        
        mock_config.assert_called_once()
        mock_git.assert_called_once()
        mock_validator.assert_called_once()
    
    def test_run_returns_execute_result(self):
        """Test that run method returns the result from execute."""
        class CustomCommand(BaseCommand):
            def execute(self, *args, **kwargs):
                return 42
        
        cmd = CustomCommand()
        result = cmd.run("test")
        
        assert result == 42
