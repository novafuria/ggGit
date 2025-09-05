"""
Parametrized tests for git utility commands.

This module contains parametrized tests for gga, ggs, ggl, ggdif, ggunstage, ggreset, ggpl, ggpp, ggv commands.
"""

import pytest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner

from src.commands.gga import GgaCommand, main as gga_main
from src.commands.ggs import GgsCommand, main as ggs_main
from src.commands.ggl import GglCommand, main as ggl_main
from src.commands.ggdif import GgdifCommand, main as ggdif_main
from src.commands.ggunstage import GgunstageCommand, main as ggunstage_main
from src.commands.ggreset import GgresetCommand, main as ggreset_main
from src.commands.ggpl import GgplCommand, main as ggpl_main
from src.commands.ggpp import GgppCommand, main as ggpp_main
from src.commands.ggv import GgvCommand, main as ggv_main


# Test data for parametrized tests
COMMAND_TEST_DATA = [
    (GgaCommand, gga_main, "gga"),
    (GgsCommand, ggs_main, "ggs"),
    (GglCommand, ggl_main, "ggl"),
    (GgdifCommand, ggdif_main, "ggdif"),
    (GgunstageCommand, ggunstage_main, "ggunstage"),
    (GgresetCommand, ggreset_main, "ggreset"),
    (GgplCommand, ggpl_main, "ggpl"),
    (GgppCommand, ggpp_main, "ggpp"),
    (GgvCommand, ggv_main, "ggv"),
]


class TestGitUtilityCommandsInitialization:
    """Test command initialization."""
    
    @pytest.mark.parametrize("command_class,main_func,command_name", COMMAND_TEST_DATA)
    def test_init(self, command_class, main_func, command_name):
        """Test initialization for all git utility commands."""
        cmd = command_class()
        assert hasattr(cmd, 'git')
        assert hasattr(cmd, 'validator')
        assert hasattr(cmd, 'logger')


class TestGitUtilityCommandsExecute:
    """Test command execute methods."""
    
    @pytest.mark.parametrize("command_class,main_func,command_name", COMMAND_TEST_DATA)
    def test_execute_success(self, command_class, main_func, command_name):
        """Test successful execution for all git utility commands."""
        cmd = command_class()
        
        # Mock the git method based on command type
        if command_name == "gga":
            with patch.object(cmd.git, 'stage_all_changes', return_value=True):
                with patch('src.commands.gga.ColorManager.success') as mock_success:
                    result = cmd.execute()
                    assert result == 0
                    mock_success.assert_called_once_with("Archivos agregados exitosamente")
        
        elif command_name == "ggs":
            with patch.object(cmd.git, 'is_git_repository', return_value=True):
                with patch('subprocess.run') as mock_run:
                    mock_run.return_value.returncode = 0
                    result = cmd.execute()
                    assert result == 0
        
        elif command_name == "ggl":
            with patch.object(cmd.git, 'is_git_repository', return_value=True):
                with patch('subprocess.run') as mock_run:
                    mock_run.return_value.returncode = 0
                    result = cmd.execute()
                    assert result == 0
        
        elif command_name == "ggdif":
            with patch.object(cmd.git, 'diff', return_value=True):
                result = cmd.execute()
                assert result == 0
        
        elif command_name == "ggunstage":
            with patch.object(cmd.git, 'unstage_files', return_value=True):
                with patch('src.commands.ggunstage.ColorManager.success') as mock_success:
                    result = cmd.execute()
                    assert result == 0
                    mock_success.assert_called_once_with("Archivos removidos del stage exitosamente")
        
        elif command_name == "ggreset":
            with patch.object(cmd.git, 'reset_hard', return_value=True):
                with patch('src.commands.ggreset.ColorManager.success') as mock_success:
                    result = cmd.execute()
                    assert result == 0
                    mock_success.assert_called_once_with("Reset --hard HEAD ejecutado exitosamente")
        
        elif command_name == "ggpl":
            with patch.object(cmd.git, 'pull', return_value=True):
                with patch('src.commands.ggpl.ColorManager.success') as mock_success:
                    result = cmd.execute()
                    assert result == 0
                    mock_success.assert_called_once_with("Pull ejecutado exitosamente")
        
        elif command_name == "ggpp":
            with patch.object(cmd.git, 'push', return_value=True):
                with patch('src.commands.ggpp.ColorManager.success') as mock_success:
                    result = cmd.execute()
                    assert result == 0
                    mock_success.assert_called_once_with("Push ejecutado exitosamente")
        
        elif command_name == "ggv":
            with patch.object(cmd.git, 'get_version', return_value="git version 2.34.1"):
                with patch('click.echo') as mock_echo:
                    result = cmd.execute()
                    assert result == 0
                    mock_echo.assert_called_once_with("git version 2.34.1")
    
    @pytest.mark.parametrize("command_class,main_func,command_name", COMMAND_TEST_DATA)
    def test_execute_failure(self, command_class, main_func, command_name):
        """Test execution failure for all git utility commands."""
        cmd = command_class()
        
        # Mock the git method to return False/None based on command type
        if command_name == "gga":
            with patch.object(cmd.git, 'stage_all_changes', return_value=False):
                with patch('src.commands.gga.ColorManager.error') as mock_error:
                    result = cmd.execute()
                    assert result == 1
                    mock_error.assert_called_once_with("Error al agregar archivos")
        
        elif command_name == "ggs":
            with patch.object(cmd.git, 'is_git_repository', return_value=False):
                with patch('src.commands.ggs.ColorManager.error') as mock_error:
                    result = cmd.execute()
                    assert result == 1
                    mock_error.assert_called_once_with("Not a git repository")
        
        elif command_name == "ggl":
            with patch.object(cmd.git, 'is_git_repository', return_value=False):
                with patch('src.commands.ggl.ColorManager.error') as mock_error:
                    result = cmd.execute()
                    assert result == 1
                    mock_error.assert_called_once_with("Not a git repository")
        
        elif command_name == "ggdif":
            with patch.object(cmd.git, 'diff', return_value=False):
                with patch('src.commands.ggdif.ColorManager.error') as mock_error:
                    result = cmd.execute()
                    assert result == 1
                    mock_error.assert_called_once_with("Error al mostrar diff")
        
        elif command_name == "ggunstage":
            with patch.object(cmd.git, 'unstage_files', return_value=False):
                with patch('src.commands.ggunstage.ColorManager.error') as mock_error:
                    result = cmd.execute()
                    assert result == 1
                    mock_error.assert_called_once_with("Error al remover archivos del stage")
        
        elif command_name == "ggreset":
            with patch.object(cmd.git, 'reset_hard', return_value=False):
                with patch('src.commands.ggreset.ColorManager.error') as mock_error:
                    result = cmd.execute()
                    assert result == 1
                    mock_error.assert_called_once_with("Error al ejecutar reset --hard HEAD")
        
        elif command_name == "ggpl":
            with patch.object(cmd.git, 'pull', return_value=False):
                with patch('src.commands.ggpl.ColorManager.error') as mock_error:
                    result = cmd.execute()
                    assert result == 1
                    mock_error.assert_called_once_with("Error al ejecutar pull")
        
        elif command_name == "ggpp":
            with patch.object(cmd.git, 'push', return_value=False):
                with patch('src.commands.ggpp.ColorManager.error') as mock_error:
                    result = cmd.execute()
                    assert result == 1
                    mock_error.assert_called_once_with("Error al ejecutar push")
        
        elif command_name == "ggv":
            with patch.object(cmd.git, 'get_version', side_effect=Exception("Git not found")):
                with patch('src.commands.ggv.ColorManager.error') as mock_error:
                    result = cmd.execute()
                    assert result == 1
                    mock_error.assert_called_once_with("Error: Git not found")


class TestGitUtilityCommandsCLI:
    """Test CLI interfaces."""
    
    @pytest.mark.parametrize("command_class,main_func,command_name", COMMAND_TEST_DATA)
    def test_cli_success(self, command_class, main_func, command_name):
        """Test successful CLI execution for all git utility commands."""
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
        """Test CLI error handling for all git utility commands."""
        runner = CliRunner()
        
        with patch(f'src.commands.{command_name}.{command_class.__name__}') as mock_command_class:
            mock_command = MagicMock()
            mock_command.run.side_effect = Exception("Test error")
            mock_command_class.return_value = mock_command
            
            result = runner.invoke(main_func, [])
            
            # Check for error message in output
            assert "Error: Test error" in result.output


class TestGitUtilityCommandsSpecific:
    """Test specific functionality for git utility commands."""
    
    def test_gga_with_files(self):
        """Test gga with specific files."""
        cmd = GgaCommand()
        
        with patch.object(cmd.git, 'stage_files', return_value=True):
            with patch('src.commands.gga.ColorManager.success') as mock_success:
                result = cmd.execute(files=['file1.txt', 'file2.txt'])
                
                assert result == 0
                cmd.git.stage_files.assert_called_once_with(['file1.txt', 'file2.txt'])
                mock_success.assert_called_once_with("Archivos agregados exitosamente")
    
    def test_gga_with_all_flag(self):
        """Test gga with all flag."""
        cmd = GgaCommand()
        
        with patch.object(cmd.git, 'stage_all_changes', return_value=True):
            with patch('src.commands.gga.ColorManager.success') as mock_success:
                result = cmd.execute(all=True)
                
                assert result == 0
                cmd.git.stage_all_changes.assert_called_once()
                mock_success.assert_called_once_with("Archivos agregados exitosamente")
    
    def test_ggdif_with_staged(self):
        """Test ggdif with staged flag."""
        cmd = GgdifCommand()
        
        with patch.object(cmd.git, 'diff', return_value=True):
            result = cmd.execute(staged=True)
            
            assert result == 0
            cmd.git.diff.assert_called_once_with(files=None, staged=True)
    
    def test_ggunstage_with_files(self):
        """Test ggunstage with specific files."""
        cmd = GgunstageCommand()
        
        with patch.object(cmd.git, 'unstage_files', return_value=True):
            with patch('src.commands.ggunstage.ColorManager.success') as mock_success:
                result = cmd.execute(files=['file1.txt', 'file2.txt'])
                
                assert result == 0
                cmd.git.unstage_files.assert_called_once_with(files=['file1.txt', 'file2.txt'])
                mock_success.assert_called_once_with("Archivos removidos del stage exitosamente")
    
    def test_ggpl_with_remote_and_branch(self):
        """Test ggpl with remote and branch."""
        cmd = GgplCommand()
        
        with patch.object(cmd.git, 'pull', return_value=True):
            with patch('src.commands.ggpl.ColorManager.success') as mock_success:
                result = cmd.execute(remote='origin', branch='main')
                
                assert result == 0
                cmd.git.pull.assert_called_once_with(remote='origin', branch='main')
                mock_success.assert_called_once_with("Pull ejecutado exitosamente")
    
    def test_ggpp_with_remote_and_branch(self):
        """Test ggpp with remote and branch."""
        cmd = GgppCommand()
        
        with patch.object(cmd.git, 'push', return_value=True):
            with patch('src.commands.ggpp.ColorManager.success') as mock_success:
                result = cmd.execute(remote='origin', branch='main')
                
                assert result == 0
                cmd.git.push.assert_called_once_with(remote='origin', branch='main')
                mock_success.assert_called_once_with("Push ejecutado exitosamente")
