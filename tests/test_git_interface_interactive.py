"""
Tests for GitInterface interactive methods.

This module contains tests for the new interactive methods added to GitInterface
for git interactive commands.
"""

import pytest
import subprocess
from unittest.mock import patch, MagicMock

from src.core.git import GitInterface, GitInterfaceError, GitCommandError, NotGitRepositoryError


class TestGitInterfaceInteractive:
    """Test GitInterface interactive methods."""
    
    def test_get_mergeable_branches_success(self):
        """Test successful get_mergeable_branches."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch.object(git, 'get_current_branch', return_value='main'):
                with patch.object(git, 'get_branches', return_value=['main', 'feature/test', 'develop']):
                    result = git.get_mergeable_branches()
                    
                    assert result == ['feature/test', 'develop']
    
    def test_get_mergeable_branches_not_git_repo(self):
        """Test get_mergeable_branches when not in git repository."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=False):
            with pytest.raises(NotGitRepositoryError, match="Not a git repository"):
                git.get_mergeable_branches()
    
    def test_get_mergeable_branches_no_current_branch(self):
        """Test get_mergeable_branches when no current branch."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch.object(git, 'get_current_branch', return_value=None):
                result = git.get_mergeable_branches()
                
                assert result == []
    
    def test_get_mergeable_branches_filters_remote(self):
        """Test get_mergeable_branches filters remote branches."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch.object(git, 'get_current_branch', return_value='main'):
                with patch.object(git, 'get_branches', return_value=['main', 'feature/test', 'origin/develop']):
                    result = git.get_mergeable_branches()
                    
                    assert result == ['feature/test']
    
    def test_get_branch_info_success(self):
        """Test successful get_branch_info."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                # Mock show-branch command
                mock_run.side_effect = [
                    MagicMock(returncode=0, stdout="branch info"),
                    MagicMock(returncode=0, stdout="abc123 Last commit message"),
                    MagicMock(returncode=0, stdout="* feature/test abc123 Last commit message")
                ]
                
                result = git.get_branch_info("feature/test")
                
                assert result["name"] == "feature/test"
                assert result["last_commit"] == "abc123 Last commit message"
                assert result["status"] == "* feature/test abc123 Last commit message"
                assert result["exists"] is True
    
    def test_get_branch_info_not_git_repo(self):
        """Test get_branch_info when not in git repository."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=False):
            with pytest.raises(NotGitRepositoryError, match="Not a git repository"):
                git.get_branch_info("feature/test")
    
    def test_get_branch_info_command_error(self):
        """Test get_branch_info when git command fails."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 1
                mock_run.return_value.stderr = "Branch not found"
                
                with pytest.raises(GitCommandError, match="Git show-branch failed"):
                    git.get_branch_info("nonexistent")
    
    def test_is_branch_mergeable_success(self):
        """Test successful is_branch_mergeable."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch.object(git, 'get_branches', return_value=['main', 'feature/test']):
                with patch.object(git, 'get_current_branch', return_value='main'):
                    result = git.is_branch_mergeable("feature/test")
                    
                    assert result is True
    
    def test_is_branch_mergeable_not_git_repo(self):
        """Test is_branch_mergeable when not in git repository."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=False):
            with pytest.raises(NotGitRepositoryError, match="Not a git repository"):
                git.is_branch_mergeable("feature/test")
    
    def test_is_branch_mergeable_branch_not_exists(self):
        """Test is_branch_mergeable when branch doesn't exist."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch.object(git, 'get_branches', return_value=['main', 'feature/test']):
                with patch.object(git, 'get_current_branch', return_value='main'):
                    result = git.is_branch_mergeable("nonexistent")
                    
                    assert result is False
    
    def test_is_branch_mergeable_current_branch(self):
        """Test is_branch_mergeable when branch is current branch."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch.object(git, 'get_branches', return_value=['main', 'feature/test']):
                with patch.object(git, 'get_current_branch', return_value='main'):
                    result = git.is_branch_mergeable("main")
                    
                    assert result is False
    
    def test_is_branch_mergeable_remote_branch(self):
        """Test is_branch_mergeable when branch is remote."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch.object(git, 'get_branches', return_value=['main', 'origin/develop']):
                with patch.object(git, 'get_current_branch', return_value='main'):
                    result = git.is_branch_mergeable("origin/develop")
                    
                    assert result is False
    
    def test_get_mergeable_branches_subprocess_error(self):
        """Test get_mergeable_branches when subprocess raises CalledProcessError."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch.object(git, 'get_current_branch', side_effect=subprocess.CalledProcessError(1, 'git')):
                with pytest.raises(GitCommandError, match="Git command failed"):
                    git.get_mergeable_branches()
    
    def test_get_branch_info_subprocess_error(self):
        """Test get_branch_info when subprocess raises CalledProcessError."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run', side_effect=subprocess.CalledProcessError(1, 'git')):
                with pytest.raises(GitCommandError, match="Git command failed"):
                    git.get_branch_info("feature/test")
    
    def test_is_branch_mergeable_subprocess_error(self):
        """Test is_branch_mergeable when subprocess raises CalledProcessError."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch.object(git, 'get_branches', side_effect=subprocess.CalledProcessError(1, 'git')):
                with pytest.raises(GitCommandError, match="Git command failed"):
                    git.is_branch_mergeable("feature/test")
