"""
Tests for GitInterface branch methods.

This module contains tests for the new branch methods added to GitInterface
for git navigation commands.
"""

import pytest
import subprocess
from unittest.mock import patch, MagicMock

from src.core.git import GitInterface, GitInterfaceError, GitCommandError, NotGitRepositoryError


class TestGitInterfaceBranches:
    """Test GitInterface branch methods."""
    
    def test_get_branches_success(self):
        """Test successful get_branches."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                mock_run.return_value.stdout = "main\ndevelop\nfeature/test\n"
                
                result = git.get_branches()
                
                assert result == ["main", "develop", "feature/test"]
                mock_run.assert_called_once_with(['git', 'branch', '--format=%(refname:short)'], capture_output=True, text=True)
    
    def test_get_branches_empty(self):
        """Test get_branches with no branches."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                mock_run.return_value.stdout = ""
                
                result = git.get_branches()
                
                assert result == []
    
    def test_get_branches_not_git_repo(self):
        """Test get_branches when not in git repository."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=False):
            with pytest.raises(NotGitRepositoryError, match="Not a git repository"):
                git.get_branches()
    
    def test_get_branches_command_error(self):
        """Test get_branches when git command fails."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 1
                mock_run.return_value.stderr = "Error message"
                
                with pytest.raises(GitCommandError, match="Git branch command failed"):
                    git.get_branches()
    
    def test_get_remote_branches_success(self):
        """Test successful get_remote_branches."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                mock_run.return_value.stdout = "origin/main\norigin/develop\norigin/HEAD\n"
                
                result = git.get_remote_branches()
                
                assert result == ["origin/main", "origin/develop"]
                mock_run.assert_called_once_with(['git', 'branch', '-r', '--format=%(refname:short)'], capture_output=True, text=True)
    
    def test_get_remote_branches_empty(self):
        """Test get_remote_branches with no remote branches."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                mock_run.return_value.stdout = ""
                
                result = git.get_remote_branches()
                
                assert result == []
    
    def test_get_remote_branches_not_git_repo(self):
        """Test get_remote_branches when not in git repository."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=False):
            with pytest.raises(NotGitRepositoryError, match="Not a git repository"):
                git.get_remote_branches()
    
    def test_get_remote_branches_command_error(self):
        """Test get_remote_branches when git command fails."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 1
                mock_run.return_value.stderr = "Error message"
                
                with pytest.raises(GitCommandError, match="Git branch -r command failed"):
                    git.get_remote_branches()
    
    def test_get_all_branches_success(self):
        """Test successful get_all_branches."""
        git = GitInterface()
        
        with patch.object(git, 'get_branches', return_value=["main", "develop"]):
            with patch.object(git, 'get_remote_branches', return_value=["origin/main", "origin/develop"]):
                result = git.get_all_branches()
                
                assert result == {
                    "local": ["main", "develop"],
                    "remote": ["origin/main", "origin/develop"]
                }
    
    def test_get_all_branches_not_git_repo(self):
        """Test get_all_branches when not in git repository."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=False):
            with pytest.raises(NotGitRepositoryError, match="Not a git repository"):
                git.get_all_branches()
    
    def test_get_all_branches_error(self):
        """Test get_all_branches when an error occurs."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch.object(git, 'get_branches', side_effect=Exception("Test error")):
                with pytest.raises(GitInterfaceError, match="Unexpected error in get_all_branches"):
                    git.get_all_branches()
    
    def test_get_branches_with_whitespace(self):
        """Test get_branches with whitespace in output."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                mock_run.return_value.stdout = "  main  \n  develop  \n  \n  feature/test  \n"
                
                result = git.get_branches()
                
                assert result == ["main", "develop", "feature/test"]
    
    def test_get_remote_branches_filters_head(self):
        """Test get_remote_branches filters out HEAD reference."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                mock_run.return_value.stdout = "origin/main\norigin/develop\norigin/HEAD\norigin/feature/test\n"
                
                result = git.get_remote_branches()
                
                assert result == ["origin/main", "origin/develop", "origin/feature/test"]
                assert "origin/HEAD" not in result
