"""
Parametrized tests for git navigation commands.

This module contains parametrized tests for ggmain, ggdevelop, ggb commands.
"""

import pytest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner

from src.commands.ggmain import GgmainCommand, main as ggmain_main
from src.commands.ggdevelop import GgdevelopCommand, main as ggdevelop_main
from src.commands.ggb import GgbCommand, main as ggb_main


# Test data for parametrized tests
COMMAND_TEST_DATA = [
    (GgmainCommand, ggmain_main, "ggmain"),
    (GgdevelopCommand, ggdevelop_main, "ggdevelop"),
    (GgbCommand, ggb_main, "ggb"),
]


class TestGitNavigationCommandsInitialization:
    """Test command initialization."""
    
    @pytest.mark.parametrize("command_class,main_func,command_name", COMMAND_TEST_DATA)
    def test_init(self, command_class, main_func, command_name):
        """Test initialization for all git navigation commands."""
        cmd = command_class()
        assert hasattr(cmd, 'git')
        assert hasattr(cmd, 'validator')
        assert hasattr(cmd, 'logger')


class TestGitNavigationCommandsExecute:
    """Test command execute methods."""
    
    @pytest.mark.parametrize("command_class,main_func,command_name", COMMAND_TEST_DATA)
    def test_execute_success(self, command_class, main_func, command_name):
        """Test successful execution for all git navigation commands."""
        cmd = command_class()
        
        # Mock the git method based on command type
        if command_name == "ggmain":
            with patch.object(cmd.git, 'is_git_repository', return_value=True):
                with patch.object(cmd.git, 'switch_branch', return_value=True):
                    with patch('src.commands.ggmain.ColorManager.success') as mock_success:
                        result = cmd.execute()
                        assert result == 0
                        mock_success.assert_called_once_with("Cambiado a rama main")
        
        elif command_name == "ggdevelop":
            with patch.object(cmd.git, 'is_git_repository', return_value=True):
                with patch.object(cmd.git, 'switch_branch', return_value=True):
                    with patch('src.commands.ggdevelop.ColorManager.success') as mock_success:
                        result = cmd.execute()
                        assert result == 0
                        mock_success.assert_called_once_with("Cambiado a rama develop")
        
        elif command_name == "ggb":
            with patch.object(cmd.git, 'is_git_repository', return_value=True):
                with patch.object(cmd.git, 'get_all_branches', return_value={"local": ["main"], "remote": []}):
                    with patch.object(cmd.git, 'get_current_branch', return_value="main"):
                        with patch.object(cmd, '_display_branches') as mock_display:
                            result = cmd.execute()
                            assert result == 0
                            mock_display.assert_called_once_with({"local": ["main"], "remote": []}, "main")
    
    @pytest.mark.parametrize("command_class,main_func,command_name", COMMAND_TEST_DATA)
    def test_execute_failure(self, command_class, main_func, command_name):
        """Test execution failure for all git navigation commands."""
        cmd = command_class()
        
        # Mock the git method to return False/None based on command type
        if command_name == "ggmain":
            with patch.object(cmd.git, 'is_git_repository', return_value=False):
                with patch('src.commands.ggmain.ColorManager.error') as mock_error:
                    result = cmd.execute()
                    assert result == 1
                    mock_error.assert_called_once_with("Not a git repository")
        
        elif command_name == "ggdevelop":
            with patch.object(cmd.git, 'is_git_repository', return_value=False):
                with patch('src.commands.ggdevelop.ColorManager.error') as mock_error:
                    result = cmd.execute()
                    assert result == 1
                    mock_error.assert_called_once_with("Not a git repository")
        
        elif command_name == "ggb":
            with patch.object(cmd.git, 'is_git_repository', return_value=False):
                with patch('src.commands.ggb.ColorManager.error') as mock_error:
                    result = cmd.execute()
                    assert result == 1
                    mock_error.assert_called_once_with("Not a git repository")
    
    @pytest.mark.parametrize("command_class,main_func,command_name", COMMAND_TEST_DATA)
    def test_execute_switch_failure(self, command_class, main_func, command_name):
        """Test execution failure when switch_branch fails."""
        cmd = command_class()
        
        if command_name in ["ggmain", "ggdevelop"]:
            with patch.object(cmd.git, 'is_git_repository', return_value=True):
                with patch.object(cmd.git, 'switch_branch', return_value=False):
                    with patch(f'src.commands.{command_name}.ColorManager.error') as mock_error:
                        result = cmd.execute()
                        assert result == 1
                        if command_name == "ggmain":
                            mock_error.assert_called_once_with("Error al cambiar a rama main")
                        else:
                            mock_error.assert_called_once_with("Error al cambiar a rama develop")


class TestGitNavigationCommandsCLI:
    """Test CLI interfaces."""
    
    @pytest.mark.parametrize("command_class,main_func,command_name", COMMAND_TEST_DATA)
    def test_cli_success(self, command_class, main_func, command_name):
        """Test successful CLI execution for all git navigation commands."""
        runner = CliRunner()
        
        with patch(f'src.commands.{command_name}.{command_class.__name__}') as mock_command_class:
            mock_command = MagicMock()
            mock_command.run.return_value = 0
            mock_command_class.return_value = mock_command
            
            # Test basic execution
            result = runner.invoke(main_func, [])
            
            assert result.exit_code == 0
            mock_command.run.assert_called_once()
    
    @pytest.mark.parametrize("command_class,main_func,command_name", COMMAND_TEST_DATA)
    def test_cli_error_handling(self, command_class, main_func, command_name):
        """Test CLI error handling for all git navigation commands."""
        runner = CliRunner()
        
        with patch(f'src.commands.{command_name}.{command_class.__name__}') as mock_command_class:
            mock_command = MagicMock()
            mock_command.run.side_effect = Exception("Test error")
            mock_command_class.return_value = mock_command
            
            result = runner.invoke(main_func, [])
            
            # Check for error message in output
            assert "Error: Test error" in result.output


class TestGitNavigationCommandsSpecific:
    """Test specific functionality for git navigation commands."""
    
    def test_ggmain_switch_success(self):
        """Test ggmain successful switch."""
        cmd = GgmainCommand()
        
        with patch.object(cmd.git, 'is_git_repository', return_value=True):
            with patch.object(cmd.git, 'switch_branch', return_value=True):
                with patch('src.commands.ggmain.ColorManager.success') as mock_success:
                    result = cmd.execute()
                    
                    assert result == 0
                    cmd.git.switch_branch.assert_called_once_with("main")
                    mock_success.assert_called_once_with("Cambiado a rama main")
    
    def test_ggdevelop_switch_success(self):
        """Test ggdevelop successful switch."""
        cmd = GgdevelopCommand()
        
        with patch.object(cmd.git, 'is_git_repository', return_value=True):
            with patch.object(cmd.git, 'switch_branch', return_value=True):
                with patch('src.commands.ggdevelop.ColorManager.success') as mock_success:
                    result = cmd.execute()
                    
                    assert result == 0
                    cmd.git.switch_branch.assert_called_once_with("develop")
                    mock_success.assert_called_once_with("Cambiado a rama develop")
    
    def test_ggb_display_branches(self):
        """Test ggb display branches functionality."""
        cmd = GgbCommand()
        
        branches = {
            "local": ["main", "develop", "feature/test"],
            "remote": ["origin/main", "origin/develop"]
        }
        current_branch = "main"
        
        with patch('click.echo') as mock_echo:
            cmd._display_branches(branches, current_branch)
            
            # Check that click.echo was called with expected messages
            assert mock_echo.call_count >= 5  # At least 5 calls for the branches and headers
    
    def test_ggb_display_branches_empty(self):
        """Test ggb display branches with empty branches."""
        cmd = GgbCommand()
        
        branches = {
            "local": [],
            "remote": []
        }
        current_branch = None
        
        with patch('click.echo') as mock_echo:
            cmd._display_branches(branches, current_branch)
            
            # Check that click.echo was called with warning messages
            assert mock_echo.call_count >= 2  # At least 2 calls for the warning messages
    
    def test_ggb_execute_success(self):
        """Test ggb successful execution."""
        cmd = GgbCommand()
        
        with patch.object(cmd.git, 'is_git_repository', return_value=True):
            with patch.object(cmd.git, 'get_all_branches', return_value={"local": ["main"], "remote": []}):
                with patch.object(cmd.git, 'get_current_branch', return_value="main"):
                    with patch.object(cmd, '_display_branches') as mock_display:
                        result = cmd.execute()
                        
                        assert result == 0
                        cmd.git.get_all_branches.assert_called_once()
                        cmd.git.get_current_branch.assert_called_once()
                        mock_display.assert_called_once_with({"local": ["main"], "remote": []}, "main")
