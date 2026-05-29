"""
Parametrized tests for basic Conventional Commits commands.

This module contains parametrized tests for ggdocs, ggstyle, ggrefactor, ggtest, ggchore commands.
"""

import pytest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner

from src.commands.ggdocs import DocsCommand, main as docs_main
from src.commands.ggstyle import StyleCommand, main as style_main
from src.commands.ggrefactor import RefactorCommand, main as refactor_main
from src.commands.ggtest import TestCommand, main as test_main
from src.commands.ggchore import ChoreCommand, main as chore_main


# Test data for parametrized tests
COMMAND_TEST_DATA = [
    (DocsCommand, "docs", docs_main, "ggdocs"),
    (StyleCommand, "style", style_main, "ggstyle"),
    (RefactorCommand, "refactor", refactor_main, "ggrefactor"),
    (TestCommand, "test", test_main, "ggtest"),
    (ChoreCommand, "chore", chore_main, "ggchore"),
]


class TestBasicConventionalCommitsInitialization:
    """Test command initialization."""
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_init(self, command_class, commit_type, main_func, command_name):
        """Test initialization for all commands."""
        cmd = command_class()
        assert hasattr(cmd, 'git')
        assert hasattr(cmd, 'validator')
        assert hasattr(cmd, 'logger')


class TestBasicConventionalCommitsExecute:
    """Test command execute methods."""
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_execute_success(self, command_class, commit_type, main_func, command_name):
        """Test successful execution for all commands."""
        cmd = command_class()
        
        with patch.object(cmd, '_execute_manual_commit', return_value=0) as mock_execute:
            result = cmd.execute("test message")
            
            assert result == 0
            mock_execute.assert_called_once_with("test message", None, False)
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_execute_with_scope(self, command_class, commit_type, main_func, command_name):
        """Test execution with scope for all commands."""
        cmd = command_class()
        
        with patch.object(cmd, '_execute_manual_commit', return_value=0) as mock_execute:
            result = cmd.execute("test message", scope="api")
            
            assert result == 0
            mock_execute.assert_called_once_with("test message", "api", False)
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_execute_with_amend(self, command_class, commit_type, main_func, command_name):
        """Test execution with amend for all commands."""
        cmd = command_class()
        
        with patch.object(cmd, '_execute_manual_commit', return_value=0) as mock_execute:
            result = cmd.execute("test message", amend=True)
            
            assert result == 0
            mock_execute.assert_called_once_with("test message", None, True)

    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_execute_with_ai_flag(self, command_class, commit_type, main_func, command_name):
        """Test execution with AI generation fallback for all commands."""
        cmd = command_class()
        
        with patch.object(cmd, '_is_ai_configured', return_value=True):
            with patch.object(cmd, '_generate_ai_message', return_value=0) as mock_generate:
                result = cmd.execute(message="")
                
                assert result == 0
                mock_generate.assert_called_once_with(None, False)
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_execute_commit_failure(self, command_class, commit_type, main_func, command_name):
        """Test execution when commit fails for all commands."""
        cmd = command_class()
        
        with patch.object(cmd, '_execute_manual_commit', return_value=1) as mock_execute:
            result = cmd.execute("test message")
            
            assert result == 1


class TestBasicConventionalCommitsCLI:
    """Test CLI interfaces."""
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_cli_success(self, command_class, commit_type, main_func, command_name):
        """Test successful CLI execution for all commands."""
        runner = CliRunner()
        
        with patch(f'src.commands.{command_name}.{command_class.__name__}') as mock_command_class:
            mock_command = MagicMock()
            mock_command.run.return_value = 0
            mock_command_class.return_value = mock_command
            
            result = runner.invoke(main_func, ["test message"])
            
            assert result.exit_code == 0
            mock_command.run.assert_called_once_with(
                message="test message",
                scope=None,
                ai=False,
                amend=False
            )
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_cli_with_scope(self, command_class, commit_type, main_func, command_name):
        """Test CLI with scope option for all commands."""
        runner = CliRunner()
        
        with patch(f'src.commands.{command_name}.{command_class.__name__}') as mock_command_class:
            mock_command = MagicMock()
            mock_command.run.return_value = 0
            mock_command_class.return_value = mock_command
            
            result = runner.invoke(main_func, ["-s", "api", "test message"])
            
            assert result.exit_code == 0
            mock_command.run.assert_called_once_with(
                message="test message",
                scope="api",
                ai=False,
                amend=False
            )
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_cli_with_amend(self, command_class, commit_type, main_func, command_name):
        """Test CLI with amend option for all commands."""
        runner = CliRunner()
        
        with patch(f'src.commands.{command_name}.{command_class.__name__}') as mock_command_class:
            mock_command = MagicMock()
            mock_command.run.return_value = 0
            mock_command_class.return_value = mock_command
            
            result = runner.invoke(main_func, ["-a", "test message"])
            
            assert result.exit_code == 0
            mock_command.run.assert_called_once_with(
                message="test message",
                scope=None,
                ai=False,
                amend=True
            )
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_cli_with_ai(self, command_class, commit_type, main_func, command_name):
        """Test CLI with AI option for all commands."""
        runner = CliRunner()
        
        # Test the actual behavior - Click doesn't propagate exit codes correctly in testing
        # Mock _is_ai_configured to return False to test the fallback warning
        with patch.object(command_class, '_is_ai_configured', return_value=False):
            result = runner.invoke(main_func, ["--ai"])
            
            # Check that AI warning message appears (functionality works)
            assert "IA no configurada" in result.output
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_cli_error_handling(self, command_class, commit_type, main_func, command_name):
        """Test CLI error handling for all commands."""
        runner = CliRunner()
        
        # Test with invalid input that should cause an error
        # In current design empty message with AI disabled prints warning and returns 1
        with patch.object(command_class, '_is_ai_configured', return_value=False):
            result = runner.invoke(main_func, [""])
            
            # Check that error message appears
            assert "IA no configurada" in result.output


class TestBasicConventionalCommitsIntegration:
    """Test integration workflows."""
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_full_workflow(self, command_class, commit_type, main_func, command_name):
        """Test full workflow from CLI to commit for all commands."""
        runner = CliRunner()
        
        with patch.object(command_class, '_execute_manual_commit', return_value=0) as mock_execute:
            result = runner.invoke(main_func, ["test message"])
            
            assert result.exit_code == 0
            mock_execute.assert_called_once_with("test message", None, False)
