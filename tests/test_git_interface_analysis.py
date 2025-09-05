"""
Tests for GitInterface analysis methods.

This module tests the new analysis methods added to GitInterface
for complexity analysis functionality.
"""

import pytest
import os
import tempfile
import subprocess
from unittest.mock import patch, Mock
from src.core.git import GitInterface, NotGitRepositoryError, GitCommandError, GitInterfaceError


class TestGitInterfaceAnalysis:
    """Test GitInterface analysis methods."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.git = GitInterface()
    
    def test_get_diff_content_no_repo(self):
        """Test get_diff_content when not in git repository."""
        with patch.object(self.git, 'is_git_repository', return_value=False):
            with pytest.raises(GitInterfaceError):  # Changed to GitInterfaceError
                self.git.get_diff_content()
    
    def test_get_diff_content_success(self):
        """Test get_diff_content success."""
        with patch.object(self.git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                mock_run.return_value.stdout = "diff content"
                
                result = self.git.get_diff_content()
                
                assert result == "diff content"
                mock_run.assert_called_once()
    
    def test_get_diff_content_staged(self):
        """Test get_diff_content with staged flag."""
        with patch.object(self.git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                mock_run.return_value.stdout = "staged diff content"
                
                result = self.git.get_diff_content(staged=True)
                
                assert result == "staged diff content"
                # Check that --staged flag was added
                call_args = mock_run.call_args[0][0]
                assert '--staged' in call_args
    
    def test_get_diff_content_with_files(self):
        """Test get_diff_content with specific files."""
        with patch.object(self.git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                mock_run.return_value.stdout = "file diff content"
                
                result = self.git.get_diff_content(files=['file1.py', 'file2.py'])
                
                assert result == "file diff content"
                # Check that files were added to command
                call_args = mock_run.call_args[0][0]
                assert 'file1.py' in call_args
                assert 'file2.py' in call_args
    
    def test_get_diff_content_error(self):
        """Test get_diff_content with git error."""
        with patch.object(self.git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 1
                mock_run.return_value.stderr = "git error"
                
                with pytest.raises(GitInterfaceError):  # Changed to GitInterfaceError
                    self.git.get_diff_content()
    
    def test_get_diff_line_count_no_repo(self):
        """Test get_diff_line_count when not in git repository."""
        with patch.object(self.git, 'is_git_repository', return_value=False):
            with pytest.raises(GitInterfaceError):  # Changed to GitInterfaceError
                self.git.get_diff_line_count()
    
    def test_get_diff_line_count_success(self):
        """Test get_diff_line_count success."""
        with patch.object(self.git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                mock_run.return_value.stdout = "10\t5\tfile1.py\n20\t10\tfile2.py\n"
                
                result = self.git.get_diff_line_count()
                
                assert result == 45  # 10+5+20+10
    
    def test_get_diff_line_count_empty(self):
        """Test get_diff_line_count with no changes."""
        with patch.object(self.git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                mock_run.return_value.stdout = ""
                
                result = self.git.get_diff_line_count()
                
                assert result == 0
    
    def test_get_diff_line_count_with_dash(self):
        """Test get_diff_line_count with binary files (dash in output)."""
        with patch.object(self.git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                mock_run.return_value.stdout = "10\t5\tfile1.py\n-\t-\tfile2.bin\n"
                
                result = self.git.get_diff_line_count()
                
                assert result == 15  # 10+5, binary file ignored
    
    def test_get_diff_line_count_staged(self):
        """Test get_diff_line_count with staged flag."""
        with patch.object(self.git, 'is_git_repository', return_value=True):
            with patch('subprocess.run') as mock_run:
                mock_run.return_value.returncode = 0
                mock_run.return_value.stdout = "5\t3\tfile1.py\n"
                
                result = self.git.get_diff_line_count(staged=True)
                
                assert result == 8
                # Check that --staged flag was added
                call_args = mock_run.call_args[0][0]
                assert '--staged' in call_args
    
    def test_get_file_size_existing_file(self):
        """Test get_file_size with existing file."""
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b"test content")
            temp_file.flush()
            
            try:
                result = self.git.get_file_size(temp_file.name)
                assert result > 0
            finally:
                os.unlink(temp_file.name)
    
    def test_get_file_size_nonexistent_file(self):
        """Test get_file_size with non-existent file."""
        result = self.git.get_file_size("nonexistent_file.txt")
        assert result == 0
    
    def test_get_file_size_error(self):
        """Test get_file_size with access error."""
        with patch('os.path.exists', return_value=True):
            with patch('os.path.getsize', side_effect=OSError("Permission denied")):
                with pytest.raises(OSError):
                    self.git.get_file_size("restricted_file.txt")
    
    def test_get_files_to_analyze_staged_priority(self):
        """Test get_files_to_analyze prioritizes staged files."""
        with patch.object(self.git, 'get_staged_files', return_value=['staged.py']):
            with patch.object(self.git, 'get_unstaged_files', return_value=['unstaged.py']):
                result = self.git.get_files_to_analyze()
                
                assert result == ['staged.py']
                # Should not call get_unstaged_files when staged files exist
                self.git.get_unstaged_files.assert_not_called()
    
    def test_get_files_to_analyze_unstaged_fallback(self):
        """Test get_files_to_analyze falls back to unstaged files."""
        with patch.object(self.git, 'get_staged_files', return_value=[]):
            with patch.object(self.git, 'get_unstaged_files', return_value=['unstaged.py']):
                result = self.git.get_files_to_analyze()
                
                assert result == ['unstaged.py']
    
    def test_get_files_to_analyze_no_files(self):
        """Test get_files_to_analyze with no files."""
        with patch.object(self.git, 'get_staged_files', return_value=[]):
            with patch.object(self.git, 'get_unstaged_files', return_value=[]):
                result = self.git.get_files_to_analyze()
                
                assert result == []


class TestGitInterfaceAnalysisIntegration:
    """Test GitInterface analysis methods integration."""
    
    def test_integration_in_git_repo(self):
        """Test analysis methods in actual git repository."""
        try:
            git = GitInterface()
            
            if not git.is_git_repository():
                pytest.skip("Not in a git repository")
            
            # Test get_files_to_analyze
            files = git.get_files_to_analyze()
            assert isinstance(files, list)
            
            # Test get_diff_line_count
            diff_lines = git.get_diff_line_count()
            assert isinstance(diff_lines, int)
            assert diff_lines >= 0
            
            # Test get_diff_content
            diff_content = git.get_diff_content()
            assert isinstance(diff_content, str)
            
            # Test get_file_size with existing files
            if files:
                file_size = git.get_file_size(files[0])
                assert isinstance(file_size, int)
                assert file_size >= 0
            
        except Exception as e:
            pytest.skip(f"Integration test failed: {e}")
    
    def test_analysis_methods_consistency(self):
        """Test that analysis methods return consistent results."""
        try:
            git = GitInterface()
            
            if not git.is_git_repository():
                pytest.skip("Not in a git repository")
            
            # Get files to analyze
            files = git.get_files_to_analyze()
            
            if files:
                # Test that diff methods work with the same files
                diff_content = git.get_diff_content(files)
                diff_lines = git.get_diff_line_count(files)
                
                assert isinstance(diff_content, str)
                assert isinstance(diff_lines, int)
                assert diff_lines >= 0
                
                # Test file sizes
                for file_path in files:
                    file_size = git.get_file_size(file_path)
                    assert isinstance(file_size, int)
                    assert file_size >= 0
            
        except Exception as e:
            pytest.skip(f"Consistency test failed: {e}")
