"""
Integration tests for CommitCommand class.

This module contains end-to-end integration tests for the CommitCommand class,
testing the complete flow with real Git operations.
"""

import pytest
import tempfile
import os
import subprocess
from pathlib import Path

from src.core.base_commands.commit import CommitCommand


class TestCommitCommandIntegration:
    """Test CommitCommand with real Git operations."""
    
    def test_ggfeat_integration(self, temp_git_repo):
        """Test ggfeat command end-to-end."""
        # Create test file
        test_file = Path('test_feature.py')
        test_file.write_text('def new_feature():\n    pass\n')
        
        # Test ggfeat command
        cmd = CommitCommand("feat")
        result = cmd.execute("add new feature function")
        
        assert result == 0
        
        # Verify commit was created
        commit_result = subprocess.run(
            ['git', 'log', '--oneline', '-1'],
            capture_output=True,
            text=True,
            cwd=temp_git_repo
        )
        assert commit_result.returncode == 0
        assert "feat: add new feature function" in commit_result.stdout
    
    def test_ggfix_integration(self, temp_git_repo):
        """Test ggfix command end-to-end."""
        # Create test file
        test_file = Path('test_fix.py')
        test_file.write_text('def buggy_function():\n    return 1/0\n')
        
        # Test ggfix command
        cmd = CommitCommand("fix")
        result = cmd.execute("fix division by zero", scope="math")
        
        assert result == 0
        
        # Verify commit was created
        commit_result = subprocess.run(
            ['git', 'log', '--oneline', '-1'],
            capture_output=True,
            text=True,
            cwd=temp_git_repo
        )
        assert commit_result.returncode == 0
        assert "fix(math): fix division by zero" in commit_result.stdout
    
    def test_ggbreak_integration(self, temp_git_repo):
        """Test ggbreak command end-to-end."""
        # Create test file
        test_file = Path('test_breaking.py')
        test_file.write_text('def old_api():\n    pass\n')
        
        # Test ggbreak command
        cmd = CommitCommand("break")
        result = cmd.execute("remove deprecated API", scope="api")
        
        assert result == 0
        
        # Verify commit was created
        commit_result = subprocess.run(
            ['git', 'log', '--oneline', '-1'],
            capture_output=True,
            text=True,
            cwd=temp_git_repo
        )
        assert commit_result.returncode == 0
        assert "break(api): remove deprecated API" in commit_result.stdout
    
    def test_commit_with_amend(self, temp_git_repo):
        """Test commit with amend flag."""
        # Create initial commit
        test_file = Path('test_amend.py')
        test_file.write_text('def initial_function():\n    pass\n')
        
        # First commit
        cmd = CommitCommand("feat")
        result = cmd.execute("add initial function")
        assert result == 0
        
        # Amend the commit
        result = cmd.execute("add initial function with better description", amend=True)
        assert result == 0
        
        # Verify amended commit
        commit_result = subprocess.run(
            ['git', 'log', '--oneline', '-1'],
            capture_output=True,
            text=True,
            cwd=temp_git_repo
        )
        assert commit_result.returncode == 0
        assert "feat: add initial function with better description" in commit_result.stdout
        
        # Verify only one commit exists
        log_result = subprocess.run(
            ['git', 'log', '--oneline'],
            capture_output=True,
            text=True,
            cwd=temp_git_repo
        )
        assert log_result.returncode == 0
        assert len(log_result.stdout.strip().split('\n')) == 1
    
    def test_validation_errors(self, temp_git_repo):
        """Test validation errors in real scenario."""
        # Test empty message
        cmd = CommitCommand("feat")
        result = cmd.execute("")
        assert result == 1
        
        # Test message too long
        long_message = "a" * 100
        result = cmd.execute(long_message)
        assert result == 1
        
        # Test invalid scope
        result = cmd.execute("add feature", scope="INVALID_SCOPE")
        assert result == 1
    
    def test_no_changes_scenario(self, temp_git_repo):
        """Test scenario when there are no changes to commit."""
        # Try to commit without any changes
        cmd = CommitCommand("feat")
        result = cmd.execute("add feature")
        assert result == 1
    
    def test_staged_files_scenario(self, temp_git_repo):
        """Test scenario with already staged files."""
        # Create and stage a file manually
        test_file = Path('staged_file.py')
        test_file.write_text('def staged_function():\n    pass\n')
        
        # Stage the file manually
        subprocess.run(['git', 'add', 'staged_file.py'], cwd=temp_git_repo, check=True)
        
        # Commit should work with staged files
        cmd = CommitCommand("feat")
        result = cmd.execute("add staged function")
        assert result == 0
        
        # Verify commit was created
        commit_result = subprocess.run(
            ['git', 'log', '--oneline', '-1'],
            capture_output=True,
            text=True,
            cwd=temp_git_repo
        )
        assert commit_result.returncode == 0
        assert "feat: add staged function" in commit_result.stdout


# Fixtures for integration testing
@pytest.fixture
def temp_git_repo():
    """Create a temporary Git repository for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        original_cwd = os.getcwd()
        os.chdir(tmpdir)
        
        # Initialize Git repository
        subprocess.run(['git', 'init'], check=True)
        subprocess.run(['git', 'config', 'user.email', 'test@example.com'], check=True)
        subprocess.run(['git', 'config', 'user.name', 'Test User'], check=True)
        
        yield tmpdir
        os.chdir(original_cwd)
