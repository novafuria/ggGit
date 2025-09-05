"""
Tests for git interactive commands.

This module contains tests for the interactive functionality added to
ggmerge and ggb commands.
"""

import pytest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner

from src.commands.ggmerge import GgmergeCommand, main as ggmerge_main
from src.commands.ggb import GgbCommand, main as ggb_main


class TestGitInteractiveCommandsInitialization:
    """Test command initialization."""
    
    def test_ggmerge_init(self):
        """Test GgmergeCommand initialization."""
        cmd = GgmergeCommand()
        assert hasattr(cmd, 'git')
        assert hasattr(cmd, 'validator')
        assert hasattr(cmd, 'logger')
    
    def test_ggb_init(self):
        """Test GgbCommand initialization."""
        cmd = GgbCommand()
        assert hasattr(cmd, 'git')
        assert hasattr(cmd, 'validator')
        assert hasattr(cmd, 'logger')


class TestGgmergeInteractive:
    """Test ggmerge interactive functionality."""
    
    def test_show_merge_options_success(self):
        """Test successful interactive merge selection."""
        cmd = GgmergeCommand()
        
        with patch.object(cmd.git, 'is_git_repository', return_value=True):
            with patch.object(cmd.git, 'get_mergeable_branches', return_value=['feature/test', 'develop']):
                with patch('builtins.input', return_value='1'):
                    with patch.object(cmd, '_merge_branch', return_value=0) as mock_merge:
                        result = cmd._show_merge_options()
                        
                        assert result == 0
                        mock_merge.assert_called_once_with('feature/test')
    
    def test_show_merge_options_no_branches(self):
        """Test show_merge_options when no branches available."""
        cmd = GgmergeCommand()
        
        with patch.object(cmd.git, 'is_git_repository', return_value=True):
            with patch.object(cmd.git, 'get_mergeable_branches', return_value=[]):
                with patch('src.commands.ggmerge.ColorManager.warning') as mock_warning:
                    result = cmd._show_merge_options()
                    
                    assert result == 0
                    mock_warning.assert_called_once_with("No hay ramas disponibles para merge")
    
    def test_show_merge_options_invalid_selection(self):
        """Test show_merge_options with invalid selection."""
        cmd = GgmergeCommand()
        
        with patch.object(cmd.git, 'is_git_repository', return_value=True):
            with patch.object(cmd.git, 'get_mergeable_branches', return_value=['feature/test']):
                with patch('builtins.input', side_effect=['invalid', '1']):
                    with patch.object(cmd, '_merge_branch', return_value=0) as mock_merge:
                        with patch('src.commands.ggmerge.ColorManager.error') as mock_error:
                            result = cmd._show_merge_options()
                            
                            assert result == 0
                            mock_error.assert_called_once_with("Selección inválida. Ingresa un número válido")
                            mock_merge.assert_called_once_with('feature/test')
    
    def test_show_merge_options_out_of_range(self):
        """Test show_merge_options with out of range selection."""
        cmd = GgmergeCommand()
        
        with patch.object(cmd.git, 'is_git_repository', return_value=True):
            with patch.object(cmd.git, 'get_mergeable_branches', return_value=['feature/test']):
                with patch('builtins.input', side_effect=['5', '1']):
                    with patch.object(cmd, '_merge_branch', return_value=0) as mock_merge:
                        with patch('src.commands.ggmerge.ColorManager.error') as mock_error:
                            result = cmd._show_merge_options()
                            
                            assert result == 0
                            mock_error.assert_called_once_with("Selección inválida. Ingresa un número entre 1 y 1")
                            mock_merge.assert_called_once_with('feature/test')
    
    def test_show_merge_options_empty_selection(self):
        """Test show_merge_options with empty selection."""
        cmd = GgmergeCommand()
        
        with patch.object(cmd.git, 'is_git_repository', return_value=True):
            with patch.object(cmd.git, 'get_mergeable_branches', return_value=['feature/test']):
                with patch('builtins.input', side_effect=['', '1']):
                    with patch.object(cmd, '_merge_branch', return_value=0) as mock_merge:
                        with patch('src.commands.ggmerge.ColorManager.error') as mock_error:
                            result = cmd._show_merge_options()
                            
                            assert result == 0
                            mock_error.assert_called_once_with("Selección requerida")
                            mock_merge.assert_called_once_with('feature/test')
    
    def test_show_merge_options_keyboard_interrupt(self):
        """Test show_merge_options with keyboard interrupt."""
        cmd = GgmergeCommand()
        
        with patch.object(cmd.git, 'is_git_repository', return_value=True):
            with patch.object(cmd.git, 'get_mergeable_branches', return_value=['feature/test']):
                with patch('builtins.input', side_effect=KeyboardInterrupt):
                    with patch('src.commands.ggmerge.ColorManager.warning') as mock_warning:
                        result = cmd._show_merge_options()
                        
                        assert result == 1
                        mock_warning.assert_called_once_with("\nOperación cancelada")
    
    def test_execute_interactive_mode(self):
        """Test execute method in interactive mode."""
        cmd = GgmergeCommand()
        
        with patch.object(cmd.git, 'is_git_repository', return_value=True):
            with patch.object(cmd, '_show_merge_options', return_value=0) as mock_show:
                result = cmd.execute()
                
                assert result == 0
                mock_show.assert_called_once()


class TestGgbInteractive:
    """Test ggb interactive functionality."""
    
    def test_show_branch_options_list_branches(self):
        """Test show_branch_options selecting list branches."""
        cmd = GgbCommand()
        
        with patch('builtins.input', return_value='1'):
            with patch.object(cmd, '_list_branches', return_value=0) as mock_list:
                result = cmd._show_branch_options()
                
                assert result == 0
                mock_list.assert_called_once()
    
    def test_show_branch_options_create_branch(self):
        """Test show_branch_options selecting create branch."""
        cmd = GgbCommand()
        
        with patch('builtins.input', side_effect=['2', 'test-branch']):
            with patch.object(cmd, '_create_branch', return_value=0) as mock_create:
                result = cmd._show_branch_options()
                
                assert result == 0
                mock_create.assert_called_once_with('test-branch')
    
    def test_show_branch_options_switch_branch(self):
        """Test show_branch_options selecting switch branch."""
        cmd = GgbCommand()
        
        with patch('builtins.input', return_value='3'):
            with patch.object(cmd, '_switch_to_branch', return_value=0) as mock_switch:
                result = cmd._show_branch_options()
                
                assert result == 0
                mock_switch.assert_called_once()
    
    def test_show_branch_options_invalid_selection(self):
        """Test show_branch_options with invalid selection."""
        cmd = GgbCommand()
        
        with patch('builtins.input', side_effect=['5', '1']):
            with patch.object(cmd, '_list_branches', return_value=0) as mock_list:
                with patch('src.commands.ggb.ColorManager.error') as mock_error:
                    result = cmd._show_branch_options()
                    
                    assert result == 0
                    mock_error.assert_called_once_with("Selección inválida. Ingresa 1, 2 o 3")
                    mock_list.assert_called_once()
    
    def test_show_branch_options_empty_selection(self):
        """Test show_branch_options with empty selection."""
        cmd = GgbCommand()
        
        with patch('builtins.input', side_effect=['', '1']):
            with patch.object(cmd, '_list_branches', return_value=0) as mock_list:
                with patch('src.commands.ggb.ColorManager.error') as mock_error:
                    result = cmd._show_branch_options()
                    
                    assert result == 0
                    mock_error.assert_called_once_with("Selección requerida")
                    mock_list.assert_called_once()
    
    def test_show_branch_options_keyboard_interrupt(self):
        """Test show_branch_options with keyboard interrupt."""
        cmd = GgbCommand()
        
        with patch('builtins.input', side_effect=KeyboardInterrupt):
            with patch('src.commands.ggb.ColorManager.warning') as mock_warning:
                result = cmd._show_branch_options()
                
                assert result == 1
                mock_warning.assert_called_once_with("\nOperación cancelada")
    
    def test_switch_to_branch_success(self):
        """Test switch_to_branch successful switch."""
        cmd = GgbCommand()
        
        with patch.object(cmd.git, 'get_branches', return_value=['main', 'develop']):
            with patch.object(cmd.git, 'get_current_branch', return_value='main'):
                with patch('builtins.input', return_value='2'):
                    with patch.object(cmd.git, 'switch_branch', return_value=True):
                        with patch('src.commands.ggb.ColorManager.success') as mock_success:
                            result = cmd._switch_to_branch()
                            
                            assert result == 0
                            mock_success.assert_called_once_with("Cambiado a rama develop")
    
    def test_switch_to_branch_no_branches(self):
        """Test switch_to_branch when no branches available."""
        cmd = GgbCommand()
        
        with patch.object(cmd.git, 'get_branches', return_value=[]):
            with patch('src.commands.ggb.ColorManager.warning') as mock_warning:
                result = cmd._switch_to_branch()
                
                assert result == 0
                mock_warning.assert_called_once_with("No hay ramas disponibles")
    
    def test_switch_to_branch_switch_failed(self):
        """Test switch_to_branch when switch fails."""
        cmd = GgbCommand()
        
        with patch.object(cmd.git, 'get_branches', return_value=['main', 'develop']):
            with patch.object(cmd.git, 'get_current_branch', return_value='main'):
                with patch('builtins.input', return_value='2'):
                    with patch.object(cmd.git, 'switch_branch', return_value=False):
                        with patch('src.commands.ggb.ColorManager.error') as mock_error:
                            result = cmd._switch_to_branch()
                            
                            assert result == 1
                            mock_error.assert_called_once_with("Error al cambiar a rama develop")
    
    def test_execute_interactive_mode(self):
        """Test execute method in interactive mode."""
        cmd = GgbCommand()
        
        with patch.object(cmd.git, 'is_git_repository', return_value=True):
            with patch.object(cmd, '_show_branch_options', return_value=0) as mock_show:
                result = cmd.execute()
                
                assert result == 0
                mock_show.assert_called_once()


class TestGitInteractiveCommandsCLI:
    """Test CLI interfaces for interactive commands."""
    
    def test_ggmerge_cli_interactive_mode(self):
        """Test ggmerge CLI in interactive mode."""
        runner = CliRunner()
        
        with patch('src.commands.ggmerge.GgmergeCommand') as mock_command_class:
            mock_command = MagicMock()
            mock_command.run.return_value = 0
            mock_command_class.return_value = mock_command
            
            result = runner.invoke(ggmerge_main, [])
            
            assert result.exit_code == 0
            mock_command.run.assert_called_once()
    
    def test_ggb_cli_interactive_mode(self):
        """Test ggb CLI in interactive mode."""
        runner = CliRunner()
        
        with patch('src.commands.ggb.GgbCommand') as mock_command_class:
            mock_command = MagicMock()
            mock_command.run.return_value = 0
            mock_command_class.return_value = mock_command
            
            result = runner.invoke(ggb_main, [])
            
            assert result.exit_code == 0
            mock_command.run.assert_called_once()
    
    def test_ggmerge_cli_with_branch(self):
        """Test ggmerge CLI with specific branch."""
        runner = CliRunner()
        
        with patch('src.commands.ggmerge.GgmergeCommand') as mock_command_class:
            mock_command = MagicMock()
            mock_command.run.return_value = 0
            mock_command_class.return_value = mock_command
            
            result = runner.invoke(ggmerge_main, ['feature/test'])
            
            assert result.exit_code == 0
            mock_command.run.assert_called_once_with(branch='feature/test', abort=False, continue_merge=False)
    
    def test_ggb_cli_with_branch(self):
        """Test ggb CLI with specific branch."""
        runner = CliRunner()
        
        with patch('src.commands.ggb.GgbCommand') as mock_command_class:
            mock_command = MagicMock()
            mock_command.run.return_value = 0
            mock_command_class.return_value = mock_command
            
            result = runner.invoke(ggb_main, ['test-branch'])
            
            assert result.exit_code == 0
            mock_command.run.assert_called_once_with(branch_name='test-branch')
