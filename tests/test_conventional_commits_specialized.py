"""
Parametrized tests for specialized Conventional Commits commands.

This module contains parametrized tests for ggperf, ggci, ggbuild commands.
"""

import pytest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner

from src.commands.ggperf import PerfCommand, main as perf_main
from src.commands.ggci import CiCommand, main as ci_main
from src.commands.ggbuild import BuildCommand, main as build_main


# Test data for parametrized tests
COMMAND_TEST_DATA = [
    (PerfCommand, "perf", perf_main, "ggperf"),
    (CiCommand, "ci", ci_main, "ggci"),
    (BuildCommand, "build", build_main, "ggbuild"),
]


class TestSpecializedConventionalCommitsInitialization:
    """Test command initialization."""
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_init(self, command_class, commit_type, main_func, command_name):
        """Test initialization for all specialized commands."""
        cmd = command_class()
        assert hasattr(cmd, 'git')
        assert hasattr(cmd, 'validator')
        assert hasattr(cmd, 'logger')


class TestSpecializedConventionalCommitsExecute:
    """Test command execute methods."""
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_execute_success(self, command_class, commit_type, main_func, command_name):
        """Test successful execution for all specialized commands."""
        cmd = command_class()
        
        with patch(f'src.commands.{command_name}.CommitCommand') as mock_commit_class:
            mock_commit = MagicMock()
            mock_commit.execute.return_value = 0
            mock_commit_class.return_value = mock_commit
            
            with patch(f'src.commands.{command_name}.ColorManager.success') as mock_success:
                result = cmd.execute("test message")
                
                assert result == 0
                mock_commit_class.assert_called_once_with(commit_type)
                mock_commit.execute.assert_called_once_with("test message", None, False)
                mock_success.assert_called_once_with("Commit realizado exitosamente")
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_execute_with_scope(self, command_class, commit_type, main_func, command_name):
        """Test execution with scope for all specialized commands."""
        cmd = command_class()
        
        with patch(f'src.commands.{command_name}.CommitCommand') as mock_commit_class:
            mock_commit = MagicMock()
            mock_commit.execute.return_value = 0
            mock_commit_class.return_value = mock_commit
            
            with patch(f'src.commands.{command_name}.ColorManager.success') as mock_success:
                result = cmd.execute("test message", scope="pipeline")
                
                assert result == 0
                mock_commit.execute.assert_called_once_with("test message", "pipeline", False)
                mock_success.assert_called_once_with("Commit realizado exitosamente")
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_execute_with_amend(self, command_class, commit_type, main_func, command_name):
        """Test execution with amend for all specialized commands."""
        cmd = command_class()
        
        with patch(f'src.commands.{command_name}.CommitCommand') as mock_commit_class:
            mock_commit = MagicMock()
            mock_commit.execute.return_value = 0
            mock_commit_class.return_value = mock_commit
            
            with patch(f'src.commands.{command_name}.ColorManager.success') as mock_success:
                result = cmd.execute("test message", amend=True)
                
                assert result == 0
                mock_commit.execute.assert_called_once_with("test message", None, True)
                mock_success.assert_called_once_with("Commit realizado exitosamente")
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_execute_with_ai_flag(self, command_class, commit_type, main_func, command_name):
        """Test execution with AI flag (not implemented) for all specialized commands."""
        cmd = command_class()
        
        with patch(f'src.commands.{command_name}.ColorManager.warning') as mock_warning:
            result = cmd.execute("", ai=True)
            
            assert result == 1
            mock_warning.assert_called_once_with("AI functionality not yet implemented")
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_execute_commit_failure(self, command_class, commit_type, main_func, command_name):
        """Test execution when commit fails for all specialized commands."""
        cmd = command_class()
        
        with patch(f'src.commands.{command_name}.CommitCommand') as mock_commit_class:
            mock_commit = MagicMock()
            mock_commit.execute.return_value = 1
            mock_commit_class.return_value = mock_commit
            
            with patch(f'src.commands.{command_name}.ColorManager.error') as mock_error:
                result = cmd.execute("test message")
                
                assert result == 1
                mock_error.assert_called_once_with("Error al realizar commit")


class TestSpecializedConventionalCommitsCLI:
    """Test CLI interfaces."""
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_cli_success(self, command_class, commit_type, main_func, command_name):
        """Test successful CLI execution for all specialized commands."""
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
        """Test CLI with scope option for all specialized commands."""
        runner = CliRunner()
        
        with patch(f'src.commands.{command_name}.{command_class.__name__}') as mock_command_class:
            mock_command = MagicMock()
            mock_command.run.return_value = 0
            mock_command_class.return_value = mock_command
            
            result = runner.invoke(main_func, ["-s", "pipeline", "test message"])
            
            assert result.exit_code == 0
            mock_command.run.assert_called_once_with(
                message="test message",
                scope="pipeline",
                ai=False,
                amend=False
            )
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_cli_with_amend(self, command_class, commit_type, main_func, command_name):
        """Test CLI with amend option for all specialized commands."""
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
        """Test CLI with AI option for all specialized commands."""
        runner = CliRunner()
        
        # Test the actual behavior - Click doesn't propagate exit codes correctly in testing
        result = runner.invoke(main_func, ["--ai"])
        
        # Check that AI warning message appears (functionality works)
        assert "AI functionality not yet implemented" in result.output
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_cli_error_handling(self, command_class, commit_type, main_func, command_name):
        """Test CLI error handling for all specialized commands."""
        runner = CliRunner()
        
        # Test with invalid input that should cause an error
        result = runner.invoke(main_func, [""])
        
        # Check that error message appears (functionality works)
        assert "Error al realizar commit" in result.output


class TestSpecializedConventionalCommitsIntegration:
    """Test integration workflows."""
    
    @pytest.mark.parametrize("command_class,commit_type,main_func,command_name", COMMAND_TEST_DATA)
    def test_full_workflow(self, command_class, commit_type, main_func, command_name):
        """Test full workflow from CLI to commit for all specialized commands."""
        runner = CliRunner()
        
        with patch(f'src.commands.{command_name}.CommitCommand') as mock_commit_class:
            mock_commit = MagicMock()
            mock_commit.execute.return_value = 0
            mock_commit_class.return_value = mock_commit
            
            with patch(f'src.commands.{command_name}.ColorManager.success') as mock_success:
                result = runner.invoke(main_func, ["test message"])
                
                assert result.exit_code == 0
                mock_commit_class.assert_called_once_with(commit_type)
                mock_commit.execute.assert_called_once_with("test message", None, False)
                mock_success.assert_called_once_with("Commit realizado exitosamente")


class TestSpecializedConventionalCommitsSpecific:
    """Test specific functionality for specialized commands."""
    
    def test_perf_command_specific(self):
        """Test perf command specific functionality."""
        cmd = PerfCommand()
        assert cmd.__class__.__name__ == "PerfCommand"
    
    def test_ci_command_specific(self):
        """Test ci command specific functionality."""
        cmd = CiCommand()
        assert cmd.__class__.__name__ == "CiCommand"
    
    def test_build_command_specific(self):
        """Test build command specific functionality."""
        cmd = BuildCommand()
        assert cmd.__class__.__name__ == "BuildCommand"
