"""
Tests for GitInterface class.

This module contains comprehensive tests for the GitInterface class,
covering all methods and error scenarios as specified in the architecture.
"""

import pytest
import subprocess
import tempfile
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

from src.core.git import (
    GitInterface,
    GitInterfaceError,
    GitNotAvailableError,
    NotGitRepositoryError,
    GitCommandError
)


class TestGitInterfaceInitialization:
    """Test GitInterface initialization and Git availability validation."""
    
    def test_init_success_when_git_available(self):
        """Test successful initialization when Git is available."""
        with patch('shutil.which', return_value='/usr/bin/git'):
            git = GitInterface()
            assert git is not None
    
    def test_init_fails_when_git_not_available(self):
        """Test initialization fails when Git is not available."""
        with patch('shutil.which', return_value=None):
            with pytest.raises(GitNotAvailableError) as exc_info:
                GitInterface()
            assert "Git no está disponible en el sistema" in str(exc_info.value)


class TestIsGitRepository:
    """Test is_git_repository method."""
    
    def test_is_git_repository_true_in_git_repo(self, temp_git_repo):
        """Test returns True when in a valid Git repository."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 0
            git = GitInterface()
            result = git.is_git_repository()
            assert result is True
    
    def test_is_git_repository_false_when_no_git_dir(self, temp_dir):
        """Test returns False when .git directory doesn't exist."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 0
            git = GitInterface()
            result = git.is_git_repository()
            assert result is False
    
    def test_is_git_repository_false_when_git_status_fails(self, temp_git_repo):
        """Test returns False when git status fails."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 1
            git = GitInterface()
            result = git.is_git_repository()
            assert result is False
    
    def test_is_git_repository_handles_timeout(self, temp_git_repo):
        """Test handles timeout gracefully."""
        with patch('subprocess.run') as mock_run:
            mock_run.side_effect = subprocess.TimeoutExpired('git', 10)
            git = GitInterface()
            result = git.is_git_repository()
            assert result is False


class TestStageAllChanges:
    """Test stage_all_changes method."""
    
    def test_stage_all_changes_success(self, temp_git_repo):
        """Test successful staging of all changes."""
        with patch('subprocess.run') as mock_run:
            # Mock both git status and git add calls
            mock_run.return_value.returncode = 0
            git = GitInterface()
            result = git.stage_all_changes()
            assert result is True
            # Verify git add was called
            assert mock_run.call_count == 2  # git status + git add
            assert mock_run.call_args_list[1] == (
                (['git', 'add', '.'],),
                {'capture_output': True, 'text': True, 'timeout': 30}
            )
    
    def test_stage_all_changes_not_git_repo(self, temp_dir):
        """Test raises NotGitRepositoryError when not in Git repo."""
        git = GitInterface()
        with pytest.raises(NotGitRepositoryError) as exc_info:
            git.stage_all_changes()
        assert "No es un repositorio Git válido" in str(exc_info.value)
    
    def test_stage_all_changes_git_command_fails(self, temp_git_repo):
        """Test raises GitCommandError when git add fails."""
        with patch('subprocess.run') as mock_run:
            # First call (git status) succeeds, second call (git add) fails
            mock_run.side_effect = [
                MagicMock(returncode=0),  # git status
                MagicMock(returncode=1, stderr="fatal: not a git repository")  # git add
            ]
            git = GitInterface()
            with pytest.raises(GitCommandError) as exc_info:
                git.stage_all_changes()
            assert "Error al ejecutar 'git add .'" in str(exc_info.value)
    
    def test_stage_all_changes_timeout(self, temp_git_repo):
        """Test handles timeout gracefully."""
        with patch('subprocess.run') as mock_run:
            # First call (git status) succeeds, second call (git add) times out
            mock_run.side_effect = [
                MagicMock(returncode=0),  # git status
                subprocess.TimeoutExpired('git', 30)  # git add
            ]
            git = GitInterface()
            with pytest.raises(GitCommandError) as exc_info:
                git.stage_all_changes()
            assert "Timeout al ejecutar 'git add .'" in str(exc_info.value)


class TestStageFiles:
    """Test stage_files method."""
    
    def test_stage_files_success(self, temp_git_repo):
        """Test successful staging of specific files."""
        # Create test files first
        Path('file1.py').touch()
        Path('file2.py').touch()
        
        with patch('subprocess.run') as mock_run:
            # First call (git status) succeeds, second call (git add) succeeds
            mock_run.side_effect = [
                MagicMock(returncode=0),  # git status
                MagicMock(returncode=0)   # git add
            ]
            git = GitInterface()
            result = git.stage_files(['file1.py', 'file2.py'])
            assert result is True
            # Verify git add was called with correct files
            assert mock_run.call_count == 2
            assert mock_run.call_args_list[1] == (
                (['git', 'add', 'file1.py', 'file2.py'],),
                {'capture_output': True, 'text': True, 'timeout': 30}
            )
    
    def test_stage_files_not_git_repo(self, temp_dir):
        """Test raises NotGitRepositoryError when not in Git repo."""
        git = GitInterface()
        with pytest.raises(NotGitRepositoryError) as exc_info:
            git.stage_files(['file1.py'])
        assert "No es un repositorio Git válido" in str(exc_info.value)
    
    def test_stage_files_empty_list(self, temp_git_repo):
        """Test raises ValueError when files list is empty."""
        git = GitInterface()
        with pytest.raises(ValueError) as exc_info:
            git.stage_files([])
        assert "La lista de archivos no puede estar vacía" in str(exc_info.value)
    
    def test_stage_files_file_not_found(self, temp_git_repo):
        """Test raises FileNotFoundError when file doesn't exist."""
        git = GitInterface()
        with pytest.raises(FileNotFoundError) as exc_info:
            git.stage_files(['nonexistent.py'])
        assert "El archivo 'nonexistent.py' no existe" in str(exc_info.value)
    
    def test_stage_files_git_command_fails(self, temp_git_repo):
        """Test raises GitCommandError when git add fails."""
        # Create test file first
        Path('file1.py').touch()
        
        with patch('subprocess.run') as mock_run:
            # First call (git status) succeeds, second call (git add) fails
            mock_run.side_effect = [
                MagicMock(returncode=0),  # git status
                MagicMock(returncode=1, stderr="fatal: pathspec 'file1.py' did not match")  # git add
            ]
            git = GitInterface()
            with pytest.raises(GitCommandError) as exc_info:
                git.stage_files(['file1.py'])
            assert "Error al ejecutar 'git add'" in str(exc_info.value)


class TestCommit:
    """Test commit method."""
    
    def test_commit_success(self, temp_git_repo):
        """Test successful commit."""
        with patch('subprocess.run') as mock_run, \
             patch.object(GitInterface, 'get_staged_files', return_value=['file1.py']):
            # First call (git status) succeeds, second call (git commit) succeeds
            mock_run.side_effect = [
                MagicMock(returncode=0),  # git status
                MagicMock(returncode=0)   # git commit
            ]
            git = GitInterface()
            result = git.commit("feat: add new feature")
            assert result is True
            # Verify git commit was called
            assert mock_run.call_count == 2
            assert mock_run.call_args_list[1] == (
                (['git', 'commit', '-m', 'feat: add new feature'],),
                {'capture_output': True, 'text': True, 'timeout': 30}
            )
    
    def test_commit_not_git_repo(self, temp_dir):
        """Test raises NotGitRepositoryError when not in Git repo."""
        git = GitInterface()
        with pytest.raises(NotGitRepositoryError) as exc_info:
            git.commit("feat: add feature")
        assert "No es un repositorio Git válido" in str(exc_info.value)
    
    def test_commit_empty_message(self, temp_git_repo):
        """Test raises ValueError when message is empty."""
        git = GitInterface()
        with pytest.raises(ValueError) as exc_info:
            git.commit("")
        assert "El mensaje de commit no puede estar vacío" in str(exc_info.value)
    
    def test_commit_whitespace_only_message(self, temp_git_repo):
        """Test raises ValueError when message is only whitespace."""
        git = GitInterface()
        with pytest.raises(ValueError) as exc_info:
            git.commit("   ")
        assert "El mensaje de commit no puede estar vacío" in str(exc_info.value)
    
    def test_commit_no_staged_changes(self, temp_git_repo):
        """Test raises GitCommandError when no staged changes."""
        with patch.object(GitInterface, 'get_staged_files', return_value=[]):
            git = GitInterface()
            with pytest.raises(GitCommandError) as exc_info:
                git.commit("feat: add feature")
            assert "No hay cambios staged para hacer commit" in str(exc_info.value)
    
    def test_commit_git_command_fails(self, temp_git_repo):
        """Test raises GitCommandError when git commit fails."""
        with patch('subprocess.run') as mock_run, \
             patch.object(GitInterface, 'get_staged_files', return_value=['file1.py']):
            # First call (git status) succeeds, second call (git commit) fails
            mock_run.side_effect = [
                MagicMock(returncode=0),  # git status
                MagicMock(returncode=1, stderr="fatal: nothing to commit")  # git commit
            ]
            git = GitInterface()
            with pytest.raises(GitCommandError) as exc_info:
                git.commit("feat: add feature")
            assert "Error al ejecutar 'git commit'" in str(exc_info.value)


class TestGetCurrentBranch:
    """Test get_current_branch method."""
    
    def test_get_current_branch_success(self, temp_git_repo):
        """Test successful branch retrieval."""
        with patch('subprocess.run') as mock_run:
            # First call (git status) succeeds, second call (git branch) succeeds
            mock_run.side_effect = [
                MagicMock(returncode=0),  # git status
                MagicMock(returncode=0, stdout="main\n")  # git branch
            ]
            git = GitInterface()
            result = git.get_current_branch()
            assert result == "main"
            # Verify git branch was called
            assert mock_run.call_count == 2
            assert mock_run.call_args_list[1] == (
                (['git', 'branch', '--show-current'],),
                {'capture_output': True, 'text': True, 'timeout': 10}
            )
    
    def test_get_current_branch_not_git_repo(self, temp_dir):
        """Test returns None when not in Git repo."""
        git = GitInterface()
        result = git.get_current_branch()
        assert result is None
    
    def test_get_current_branch_detached_head(self, temp_git_repo):
        """Test returns None when in detached HEAD state."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 0
            mock_run.return_value.stdout = ""
            git = GitInterface()
            result = git.get_current_branch()
            assert result is None
    
    def test_get_current_branch_git_command_fails(self, temp_git_repo):
        """Test returns None when git command fails."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 1
            git = GitInterface()
            result = git.get_current_branch()
            assert result is None


class TestGetStagedFiles:
    """Test get_staged_files method."""
    
    def test_get_staged_files_success(self, temp_git_repo):
        """Test successful retrieval of staged files."""
        with patch('subprocess.run') as mock_run:
            # First call (git status) succeeds, second call (git diff) succeeds
            mock_run.side_effect = [
                MagicMock(returncode=0),  # git status
                MagicMock(returncode=0, stdout="file1.py\nfile2.py\n")  # git diff
            ]
            git = GitInterface()
            result = git.get_staged_files()
            assert result == ["file1.py", "file2.py"]
            # Verify git diff was called
            assert mock_run.call_count == 2
            assert mock_run.call_args_list[1] == (
                (['git', 'diff', '--cached', '--name-only'],),
                {'capture_output': True, 'text': True, 'timeout': 10}
            )
    
    def test_get_staged_files_not_git_repo(self, temp_dir):
        """Test returns empty list when not in Git repo."""
        git = GitInterface()
        result = git.get_staged_files()
        assert result == []
    
    def test_get_staged_files_no_staged_files(self, temp_git_repo):
        """Test returns empty list when no staged files."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 0
            mock_run.return_value.stdout = ""
            git = GitInterface()
            result = git.get_staged_files()
            assert result == []
    
    def test_get_staged_files_git_command_fails(self, temp_git_repo):
        """Test returns empty list when git command fails."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 1
            git = GitInterface()
            result = git.get_staged_files()
            assert result == []


class TestGetUnstagedFiles:
    """Test get_unstaged_files method."""
    
    def test_get_unstaged_files_success(self, temp_git_repo):
        """Test successful retrieval of unstaged files."""
        with patch('subprocess.run') as mock_run:
            # First call (git status) succeeds, second call (git diff) succeeds
            mock_run.side_effect = [
                MagicMock(returncode=0),  # git status
                MagicMock(returncode=0, stdout="file1.py\nfile2.py\n")  # git diff
            ]
            git = GitInterface()
            result = git.get_unstaged_files()
            assert result == ["file1.py", "file2.py"]
            # Verify git diff was called
            assert mock_run.call_count == 2
            assert mock_run.call_args_list[1] == (
                (['git', 'diff', '--name-only'],),
                {'capture_output': True, 'text': True, 'timeout': 10}
            )
    
    def test_get_unstaged_files_not_git_repo(self, temp_dir):
        """Test returns empty list when not in Git repo."""
        git = GitInterface()
        result = git.get_unstaged_files()
        assert result == []
    
    def test_get_unstaged_files_no_unstaged_files(self, temp_git_repo):
        """Test returns empty list when no unstaged files."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 0
            mock_run.return_value.stdout = ""
            git = GitInterface()
            result = git.get_unstaged_files()
            assert result == []
    
    def test_get_unstaged_files_git_command_fails(self, temp_git_repo):
        """Test returns empty list when git command fails."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 1
            git = GitInterface()
            result = git.get_unstaged_files()
            assert result == []


# Fixtures for testing
@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        original_cwd = os.getcwd()
        os.chdir(tmpdir)
        yield tmpdir
        os.chdir(original_cwd)


@pytest.fixture
def temp_git_repo():
    """Create a temporary Git repository for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        original_cwd = os.getcwd()
        os.chdir(tmpdir)
        
        # Initialize Git repository
        subprocess.run(['git', 'init'], check=True)
        
        yield tmpdir
        os.chdir(original_cwd)
