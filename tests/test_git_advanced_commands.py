"""
Parametrized tests for git advanced commands.

This module contains parametrized tests for ggb (extended), ggmerge, ggbreak commands.
"""

import pytest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner

from src.commands.ggb import GgbCommand, main as ggb_main
from src.commands.ggmerge import GgmergeCommand, main as ggmerge_main
from src.commands.ggbreak import GgbreakCommand, main as ggbreak_main


# Test data for parametrized tests
COMMAND_TEST_DATA = [
    (GgbCommand, ggb_main, "ggb"),
    (GgmergeCommand, ggmerge_main, "ggmerge"),
    (GgbreakCommand, ggbreak_main, "ggbreak"),
]


class TestGitAdvancedCommandsInitialization:
    """Test command initialization."""
    
    @pytest.mark.parametrize("command_class,main_func,command_name", COMMAND_TEST_DATA)
    def test_init(self, command_class, main_func, command_name):
        """Test initialization for all git advanced commands."""
        cmd = command_class()
        assert hasattr(cmd, 'git')
        assert hasattr(cmd, 'validator')
        assert hasattr(cmd, 'logger')


class TestGitAdvancedCommandsExecute:
    """Test command execute methods."""
    
    @pytest.mark.parametrize("command_class,main_func,command_name", COMMAND_TEST_DATA)
    def test_execute_success(self, command_class, main_func, command_name):
        """Test successful execution for all git advanced commands."""
        cmd = command_class()
        
        # Mock the git method based on command type
        if command_name == "ggb":
            with patch.object(cmd.git, 'is_git_repository', return_value=True):
                with patch.object(cmd, '_list_branches', return_value=0):
                    result = cmd.execute()
                    assert result == 0
        
        elif command_name == "ggmerge":
            with patch.object(cmd.git, 'is_git_repository', return_value=True):
                with patch.object(cmd.git, 'merge_branch', return_value=True):
                    with patch('src.commands.ggmerge.ColorManager.success') as mock_success:
                        result = cmd.execute(branch="feature/test")
                        assert result == 0
                        mock_success.assert_called_once_with("Merge de feature/test completado exitosamente")
        
        elif command_name == "ggbreak":
            with patch.object(cmd.git, 'is_git_repository', return_value=True):
                with patch.object(cmd.git, 'get_staged_files', return_value=[]):
                    with patch.object(cmd.git, 'stage_all_changes', return_value=True):
                        with patch.object(cmd.git, 'commit', return_value=True):
                            with patch('src.commands.ggbreak.ColorManager.success') as mock_success:
                                result = cmd.execute(message="test message")
                                assert result == 0
                                mock_success.assert_called_once_with("Commit con break realizado exitosamente")
    
    @pytest.mark.parametrize("command_class,main_func,command_name", COMMAND_TEST_DATA)
    def test_execute_failure(self, command_class, main_func, command_name):
        """Test execution failure for all git advanced commands."""
        cmd = command_class()
        
        # Mock the git method to return False/None based on command type
        if command_name == "ggb":
            with patch.object(cmd.git, 'is_git_repository', return_value=False):
                with patch('src.commands.ggb.ColorManager.error') as mock_error:
                    result = cmd.execute()
                    assert result == 1
                    mock_error.assert_called_once_with("Not a git repository")
        
        elif command_name == "ggmerge":
            with patch.object(cmd.git, 'is_git_repository', return_value=False):
                with patch('src.commands.ggmerge.ColorManager.error') as mock_error:
                    result = cmd.execute()
                    assert result == 1
                    mock_error.assert_called_once_with("Not a git repository")
        
        elif command_name == "ggbreak":
            with patch.object(cmd.git, 'is_git_repository', return_value=False):
                with patch('src.commands.ggbreak.ColorManager.error') as mock_error:
                    result = cmd.execute(message="test")
                    assert result == 1
                    mock_error.assert_called_once_with("Not a git repository")


class TestGitAdvancedCommandsCLI:
    """Test CLI interfaces."""
    
    @pytest.mark.parametrize("command_class,main_func,command_name", COMMAND_TEST_DATA)
    def test_cli_success(self, command_class, main_func, command_name):
        """Test successful CLI execution for all git advanced commands."""
        runner = CliRunner()
        
        with patch(f'src.commands.{command_name}.{command_class.__name__}') as mock_command_class:
            mock_command = MagicMock()
            mock_command.run.return_value = 0
            mock_command_class.return_value = mock_command
            
            # Test basic execution
            if command_name == "ggbreak":
                result = runner.invoke(main_func, ["test message"])
            else:
                result = runner.invoke(main_func, [])
            
            assert result.exit_code == 0
            mock_command.run.assert_called_once()
    
    @pytest.mark.parametrize("command_class,main_func,command_name", COMMAND_TEST_DATA)
    def test_cli_error_handling(self, command_class, main_func, command_name):
        """Test CLI error handling for all git advanced commands."""
        runner = CliRunner()
        
        with patch(f'src.commands.{command_name}.{command_class.__name__}') as mock_command_class:
            mock_command = MagicMock()
            mock_command.run.side_effect = Exception("Test error")
            mock_command_class.return_value = mock_command
            
            # Provide required arguments based on command
            if command_name == "ggbreak":
                result = runner.invoke(main_func, ["test message"])
            else:
                result = runner.invoke(main_func, [])
            
            # Check for error message in output
            assert "Error: Test error" in result.output


class TestGitAdvancedCommandsSpecific:
    """Test specific functionality for git advanced commands."""
    
    def test_ggb_create_branch_success(self):
        """Test ggb successful branch creation."""
        cmd = GgbCommand()
        
        with patch.object(cmd.git, 'is_git_repository', return_value=True):
            with patch.object(cmd, '_create_branch', return_value=0):
                result = cmd.execute(branch_name="nueva funcionalidad")
                
                assert result == 0
                cmd._create_branch.assert_called_once_with("nueva funcionalidad")
    
    def test_ggb_convert_branch_name(self):
        """Test ggb branch name conversion."""
        cmd = GgbCommand()
        
        # Test space to hyphen conversion
        result = cmd._convert_branch_name("nueva funcionalidad")
        assert result == "nueva-funcionalidad"
        
        # Test multiple spaces
        result = cmd._convert_branch_name("feature  nueva   funcionalidad")
        assert result == "feature-nueva-funcionalidad"
        
        # Test empty string
        result = cmd._convert_branch_name("")
        assert result == ""
    
    def test_ggb_validate_branch_name(self):
        """Test ggb branch name validation."""
        cmd = GgbCommand()
        
        # Valid names
        assert cmd._validate_branch_name("valid-name") is True
        assert cmd._validate_branch_name("feature/test") is True
        
        # Invalid names
        assert cmd._validate_branch_name("") is False
        assert cmd._validate_branch_name("name..") is False
        assert cmd._validate_branch_name(".name") is False
        assert cmd._validate_branch_name("name~") is False
    
    def test_ggb_branch_exists(self):
        """Test ggb branch exists check."""
        cmd = GgbCommand()
        
        with patch.object(cmd.git, 'get_branches', return_value=["main", "develop"]):
            assert cmd._branch_exists("main") is True
            assert cmd._branch_exists("feature") is False
    
    def test_ggmerge_merge_branch_success(self):
        """Test ggmerge successful merge."""
        cmd = GgmergeCommand()
        
        with patch.object(cmd.git, 'is_git_repository', return_value=True):
            with patch.object(cmd.git, 'merge_branch', return_value=True):
                with patch('src.commands.ggmerge.ColorManager.success') as mock_success:
                    result = cmd.execute(branch="feature/test")
                    
                    assert result == 0
                    cmd.git.merge_branch.assert_called_once_with("feature/test")
                    mock_success.assert_called_once_with("Merge de feature/test completado exitosamente")
    
    def test_ggmerge_abort_success(self):
        """Test ggmerge successful abort."""
        cmd = GgmergeCommand()
        
        with patch.object(cmd.git, 'is_git_repository', return_value=True):
            with patch.object(cmd.git, 'merge_abort', return_value=True):
                with patch('src.commands.ggmerge.ColorManager.success') as mock_success:
                    result = cmd.execute(abort=True)
                    
                    assert result == 0
                    cmd.git.merge_abort.assert_called_once()
                    mock_success.assert_called_once_with("Merge abortado exitosamente")
    
    def test_ggmerge_continue_success(self):
        """Test ggmerge successful continue."""
        cmd = GgmergeCommand()
        
        with patch.object(cmd.git, 'is_git_repository', return_value=True):
            with patch.object(cmd.git, 'merge_continue', return_value=True):
                with patch('src.commands.ggmerge.ColorManager.success') as mock_success:
                    result = cmd.execute(continue_merge=True)
                    
                    assert result == 0
                    cmd.git.merge_continue.assert_called_once()
                    mock_success.assert_called_once_with("Merge continuado exitosamente")
    
    def test_ggbreak_commit_success(self):
        """Test ggbreak successful commit."""
        cmd = GgbreakCommand()
        
        with patch.object(cmd.git, 'is_git_repository', return_value=True):
            with patch.object(cmd.git, 'get_staged_files', return_value=[]):
                with patch.object(cmd.git, 'stage_all_changes', return_value=True):
                    with patch.object(cmd.git, 'commit', return_value=True):
                        with patch('src.commands.ggbreak.ColorManager.success') as mock_success:
                            result = cmd.execute(message="test message")
                            
                            assert result == 0
                            cmd.git.commit.assert_called_once_with("break: test message")
                            mock_success.assert_called_once_with("Commit con break realizado exitosamente")
    
    def test_ggbreak_commit_with_scope(self):
        """Test ggbreak commit with scope."""
        cmd = GgbreakCommand()
        
        with patch.object(cmd.git, 'is_git_repository', return_value=True):
            with patch.object(cmd.git, 'get_staged_files', return_value=["file.txt"]):
                with patch.object(cmd.git, 'commit', return_value=True):
                    with patch('src.commands.ggbreak.ColorManager.success') as mock_success:
                        result = cmd.execute(message="test message", scope="auth")
                        
                        assert result == 0
                        cmd.git.commit.assert_called_once_with("break(auth): test message")
                        mock_success.assert_called_once_with("Commit con break realizado exitosamente")
    
    def test_ggbreak_empty_message(self):
        """Test ggbreak with empty message."""
        cmd = GgbreakCommand()
        
        with patch('src.commands.ggbreak.ColorManager.error') as mock_error:
            result = cmd.execute(message="")
            
            assert result == 1
            mock_error.assert_called_once_with("Message is required")
