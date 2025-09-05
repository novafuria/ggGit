"""
Tests for GitInterface merge methods.

This module contains tests for the new merge methods added to GitInterface
for git advanced branch management commands.
"""

import pytest
import subprocess
from unittest.mock import patch, MagicMock

from src.core.git import GitInterface, GitInterfaceError, GitCommandError, NotGitRepositoryError


class TestGitInterfaceMerge:
    """Test GitInterface merge methods."""
    
    def test_merge_branch_success(self):
        """Test successful merge_branch."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                mock_run.return_value.stderr = ""
                
                result = git.merge_branch("feature/test")
                
                assert result is True
                mock_run.assert_called_once_with(['git', 'merge', 'feature/test'], capture_output=True, text=True)
    
    def test_merge_branch_not_git_repo(self):
        """Test merge_branch when not in git repository."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=False):
            with pytest.raises(NotGitRepositoryError, match="Not a git repository"):
                git.merge_branch("feature/test")
    
    def test_merge_branch_command_error(self):
        """Test merge_branch when git command fails."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 1
                mock_run.return_value.stderr = "Merge conflict"
                
                with pytest.raises(GitCommandError, match="Git merge failed"):
                    git.merge_branch("feature/test")
    
    def test_merge_abort_success(self):
        """Test successful merge_abort."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                mock_run.return_value.stderr = ""
                
                result = git.merge_abort()
                
                assert result is True
                mock_run.assert_called_once_with(['git', 'merge', '--abort'], capture_output=True, text=True)
    
    def test_merge_abort_not_git_repo(self):
        """Test merge_abort when not in git repository."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=False):
            with pytest.raises(NotGitRepositoryError, match="Not a git repository"):
                git.merge_abort()
    
    def test_merge_abort_command_error(self):
        """Test merge_abort when git command fails."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 1
                mock_run.return_value.stderr = "No merge in progress"
                
                with pytest.raises(GitCommandError, match="Git merge --abort failed"):
                    git.merge_abort()
    
    def test_merge_continue_success(self):
        """Test successful merge_continue."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                mock_run.return_value.stderr = ""
                
                result = git.merge_continue()
                
                assert result is True
                mock_run.assert_called_once_with(['git', 'merge', '--continue'], capture_output=True, text=True)
    
    def test_merge_continue_not_git_repo(self):
        """Test merge_continue when not in git repository."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=False):
            with pytest.raises(NotGitRepositoryError, match="Not a git repository"):
                git.merge_continue()
    
    def test_merge_continue_command_error(self):
        """Test merge_continue when git command fails."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 1
                mock_run.return_value.stderr = "No merge in progress"
                
                with pytest.raises(GitCommandError, match="Git merge --continue failed"):
                    git.merge_continue()
    
    def test_merge_branch_subprocess_error(self):
        """Test merge_branch when subprocess raises CalledProcessError."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run', side_effect=subprocess.CalledProcessError(1, 'git')):
                with pytest.raises(GitCommandError, match="Git merge failed"):
                    git.merge_branch("feature/test")
    
    def test_merge_abort_subprocess_error(self):
        """Test merge_abort when subprocess raises CalledProcessError."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run', side_effect=subprocess.CalledProcessError(1, 'git')):
                with pytest.raises(GitCommandError, match="Git merge --abort failed"):
                    git.merge_abort()
    
    def test_merge_continue_subprocess_error(self):
        """Test merge_continue when subprocess raises CalledProcessError."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run', side_effect=subprocess.CalledProcessError(1, 'git')):
                with pytest.raises(GitCommandError, match="Git merge --continue failed"):
                    git.merge_continue()
