"""
Tests for extended GitInterface methods.

This module contains tests for the new methods added to GitInterface
for git utility commands.
"""

import pytest
import subprocess
from unittest.mock import patch, MagicMock

from src.core.git import GitInterface, GitInterfaceError, GitCommandError, GitNotAvailableError


class TestGitInterfaceExtended:
    """Test extended GitInterface methods."""
    
    def test_diff_basic(self):
        """Test basic diff functionality."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                
                result = git.diff()
                
                assert result is True
                mock_run.assert_called_once_with(['git', 'diff'], capture_output=False, text=True)
    
    def test_diff_with_files(self):
        """Test diff with specific files."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                
                result = git.diff(files=['file1.txt', 'file2.txt'])
                
                assert result is True
                mock_run.assert_called_once_with(['git', 'diff', 'file1.txt', 'file2.txt'], capture_output=False, text=True)
    
    def test_diff_staged(self):
        """Test diff with staged changes."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                
                result = git.diff(staged=True)
                
                assert result is True
                mock_run.assert_called_once_with(['git', 'diff', '--staged'], capture_output=False, text=True)
    
    def test_diff_not_git_repo(self):
        """Test diff when not in git repository."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=False):
            with pytest.raises(GitInterfaceError, match="Not a git repository"):
                git.diff()
    
    def test_unstage_files_basic(self):
        """Test basic unstage functionality."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                
                result = git.unstage_files()
                
                assert result is True
                mock_run.assert_called_once_with(['git', 'reset', 'HEAD'], capture_output=True, text=True)
    
    def test_unstage_files_specific(self):
        """Test unstage with specific files."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                
                result = git.unstage_files(files=['file1.txt', 'file2.txt'])
                
                assert result is True
                mock_run.assert_called_once_with(['git', 'reset', 'HEAD', 'file1.txt', 'file2.txt'], capture_output=True, text=True)
    
    def test_unstage_files_not_git_repo(self):
        """Test unstage when not in git repository."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=False):
            with pytest.raises(GitInterfaceError, match="Not a git repository"):
                git.unstage_files()
    
    def test_reset_hard(self):
        """Test reset --hard HEAD."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                
                result = git.reset_hard()
                
                assert result is True
                mock_run.assert_called_once_with(['git', 'reset', '--hard', 'HEAD'], capture_output=True, text=True)
    
    def test_reset_hard_not_git_repo(self):
        """Test reset --hard when not in git repository."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=False):
            with pytest.raises(GitInterfaceError, match="Not a git repository"):
                git.reset_hard()
    
    def test_pull_basic(self):
        """Test basic pull functionality."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                
                result = git.pull()
                
                assert result is True
                mock_run.assert_called_once_with(['git', 'pull'], capture_output=True, text=True)
    
    def test_pull_with_remote_and_branch(self):
        """Test pull with remote and branch."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                
                result = git.pull(remote='origin', branch='main')
                
                assert result is True
                mock_run.assert_called_once_with(['git', 'pull', 'origin', 'main'], capture_output=True, text=True)
    
    def test_pull_not_git_repo(self):
        """Test pull when not in git repository."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=False):
            with pytest.raises(GitInterfaceError, match="Not a git repository"):
                git.pull()
    
    def test_push_basic(self):
        """Test basic push functionality."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                
                result = git.push()
                
                assert result is True
                mock_run.assert_called_once_with(['git', 'push'], capture_output=True, text=True)
    
    def test_push_with_remote_and_branch(self):
        """Test push with remote and branch."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                
                result = git.push(remote='origin', branch='main')
                
                assert result is True
                mock_run.assert_called_once_with(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
    
    def test_push_not_git_repo(self):
        """Test push when not in git repository."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=False):
            with pytest.raises(GitInterfaceError, match="Not a git repository"):
                git.push()
    
    def test_get_version_success(self):
        """Test get_version success."""
        git = GitInterface()
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 0
            mock_run.return_value.stdout = "git version 2.34.1"
            
            result = git.get_version()
            
            assert result == "git version 2.34.1"
            mock_run.assert_called_once_with(['git', '--version'], capture_output=True, text=True)
    
    def test_get_version_git_not_installed(self):
        """Test get_version when Git is not installed."""
        git = GitInterface()
        
        with patch('subprocess.run', side_effect=FileNotFoundError):
            with pytest.raises(GitNotAvailableError, match="Git is not installed"):
                git.get_version()
    
    def test_get_version_git_not_available(self):
        """Test get_version when Git is not available."""
        git = GitInterface()
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 1
            
            with pytest.raises(GitNotAvailableError, match="Git is not available"):
                git.get_version()
    
    def test_diff_command_error(self):
        """Test diff when git command fails."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run', side_effect=subprocess.CalledProcessError(1, 'git')):
                with pytest.raises(GitCommandError, match="Git diff failed"):
                    git.diff()
    
    def test_unstage_files_command_error(self):
        """Test unstage_files when git command fails."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run', side_effect=subprocess.CalledProcessError(1, 'git')):
                with pytest.raises(GitCommandError, match="Git unstage failed"):
                    git.unstage_files()
    
    def test_reset_hard_command_error(self):
        """Test reset_hard when git command fails."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run', side_effect=subprocess.CalledProcessError(1, 'git')):
                with pytest.raises(GitCommandError, match="Git reset --hard failed"):
                    git.reset_hard()
    
    def test_pull_command_error(self):
        """Test pull when git command fails."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run', side_effect=subprocess.CalledProcessError(1, 'git')):
                with pytest.raises(GitCommandError, match="Git pull failed"):
                    git.pull()
    
    def test_push_command_error(self):
        """Test push when git command fails."""
        git = GitInterface()
        
        with patch.object(git, 'is_git_repository', return_value=True):
            with patch('subprocess.run', side_effect=subprocess.CalledProcessError(1, 'git')):
                with pytest.raises(GitCommandError, match="Git push failed"):
                    git.push()
    
    def test_get_version_command_error(self):
        """Test get_version when git command fails."""
        git = GitInterface()
        
        with patch('subprocess.run', side_effect=subprocess.CalledProcessError(1, 'git')):
            with pytest.raises(GitCommandError, match="Git version command failed"):
                git.get_version()
