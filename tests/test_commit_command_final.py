"""
Final tests for CommitCommand class.

This module contains working tests for the CommitCommand class,
focusing on the core functionality with proper mocking.
"""

import pytest
import subprocess
from unittest.mock import patch, MagicMock

from src.core.base_commands.commit import CommitCommand


class TestCommitCommandInitialization:
    """Test CommitCommand initialization."""
    
    def test_init_with_commit_type(self):
        """Test initialization with commit type."""
        cmd = CommitCommand("feat")
        assert cmd.commit_type == "feat"
        assert hasattr(cmd, 'git')
        assert hasattr(cmd, 'validator')
        assert hasattr(cmd, 'logger')
    
    def test_init_with_different_types(self):
        """Test initialization with different commit types."""
        types = ["feat", "fix", "break", "docs", "style"]
        for commit_type in types:
            cmd = CommitCommand(commit_type)
            assert cmd.commit_type == commit_type


class TestFormatCommitMessage:
    """Test format_commit_message method."""
    
    def test_format_message_without_scope(self):
        """Test formatting message without scope."""
        cmd = CommitCommand("feat")
        result = cmd.format_commit_message("add new feature")
        assert result == "feat: add new feature"
    
    def test_format_message_with_scope(self):
        """Test formatting message with scope."""
        cmd = CommitCommand("fix")
        result = cmd.format_commit_message("resolve bug", "auth")
        assert result == "fix(auth): resolve bug"
    
    def test_format_message_with_different_types(self):
        """Test formatting with different commit types."""
        test_cases = [
            ("feat", "add feature", None, "feat: add feature"),
            ("fix", "fix bug", "ui", "fix(ui): fix bug"),
            ("break", "breaking change", "api", "break(api): breaking change"),
            ("docs", "update docs", None, "docs: update docs"),
        ]
        
        for commit_type, message, scope, expected in test_cases:
            cmd = CommitCommand(commit_type)
            result = cmd.format_commit_message(message, scope)
            assert result == expected


class TestExecuteCommitCommand:
    """Test execute method with proper mocking."""
    
    def test_execute_success_without_scope(self):
        """Test successful execution without scope."""
        cmd = CommitCommand("feat")
        
        # Mock the instance attributes
        with patch.object(cmd, 'git') as mock_git, \
             patch.object(cmd, 'validator') as mock_validator:
            
            # Mock git interface methods
            mock_git.is_git_repository.return_value = True
            mock_git.get_staged_files.return_value = []
            mock_git.get_unstaged_files.return_value = ['test_file.py']
            mock_git.stage_all_changes.return_value = True
            mock_git.commit.return_value = True
            
            # Mock validator
            mock_validator.validate_commit_message.return_value = True
            
            result = cmd.execute("add new feature")
            assert result == 0
    
    def test_execute_success_with_scope(self):
        """Test successful execution with scope."""
        cmd = CommitCommand("fix")
        
        with patch.object(cmd, 'git') as mock_git, \
             patch.object(cmd, 'validator') as mock_validator:
            
            # Mock git interface methods
            mock_git.is_git_repository.return_value = True
            mock_git.get_staged_files.return_value = []
            mock_git.get_unstaged_files.return_value = ['test_file.py']
            mock_git.stage_all_changes.return_value = True
            mock_git.commit.return_value = True
            
            # Mock validator
            mock_validator.validate_commit_message.return_value = True
            mock_validator.validate_scope.return_value = True
            
            result = cmd.execute("fix bug", scope="auth")
            assert result == 0
    
    def test_execute_success_with_amend(self):
        """Test successful execution with amend flag."""
        cmd = CommitCommand("feat")
        
        with patch.object(cmd, 'git') as mock_git, \
             patch.object(cmd, 'validator') as mock_validator, \
             patch.object(cmd, '_execute_amend_commit') as mock_amend:
            
            # Mock git interface methods
            mock_git.is_git_repository.return_value = True
            mock_git.get_staged_files.return_value = ['test_file.py']
            mock_git.get_unstaged_files.return_value = []
            
            # Mock validator
            mock_validator.validate_commit_message.return_value = True
            
            # Mock amend commit
            mock_amend.return_value = True
            
            result = cmd.execute("update feature", amend=True)
            assert result == 0
    
    def test_execute_validation_error_empty_message(self):
        """Test execution with empty message validation error."""
        cmd = CommitCommand("feat")
        
        with patch.object(cmd, 'validator') as mock_validator:
            mock_validator.validate_commit_message.side_effect = ValueError("Commit message cannot be empty")
            
            result = cmd.execute("")
            assert result == 1
    
    def test_execute_validation_error_long_message(self):
        """Test execution with message too long validation error."""
        cmd = CommitCommand("feat")
        
        with patch.object(cmd, 'validator') as mock_validator:
            mock_validator.validate_commit_message.side_effect = ValueError("Commit message too long")
            
            result = cmd.execute("a" * 100)
            assert result == 1
    
    def test_execute_validation_error_invalid_scope(self):
        """Test execution with invalid scope validation error."""
        cmd = CommitCommand("feat")
        
        with patch.object(cmd, 'validator') as mock_validator:
            mock_validator.validate_commit_message.return_value = True
            mock_validator.validate_scope.side_effect = ValueError("Invalid scope format")
            
            result = cmd.execute("add feature", scope="INVALID_SCOPE")
            assert result == 1
    
    def test_execute_not_git_repository(self):
        """Test execution when not in git repository."""
        cmd = CommitCommand("feat")
        
        with patch.object(cmd, 'git') as mock_git, \
             patch.object(cmd, 'validator') as mock_validator:
            
            mock_git.is_git_repository.return_value = False
            mock_validator.validate_commit_message.return_value = True
            
            result = cmd.execute("add feature")
            assert result == 1
    
    def test_execute_no_changes_to_commit(self):
        """Test execution when there are no changes to commit."""
        cmd = CommitCommand("feat")
        
        with patch.object(cmd, 'git') as mock_git, \
             patch.object(cmd, 'validator') as mock_validator:
            
            mock_git.is_git_repository.return_value = True
            mock_git.get_staged_files.return_value = []
            mock_git.get_unstaged_files.return_value = []
            mock_validator.validate_commit_message.return_value = True
            
            result = cmd.execute("add feature")
            assert result == 1
    
    def test_execute_stage_fails(self):
        """Test execution when staging fails."""
        cmd = CommitCommand("feat")
        
        with patch.object(cmd, 'git') as mock_git, \
             patch.object(cmd, 'validator') as mock_validator:
            
            mock_git.is_git_repository.return_value = True
            mock_git.get_staged_files.return_value = []
            mock_git.get_unstaged_files.return_value = ['test_file.py']
            mock_git.stage_all_changes.return_value = False
            mock_validator.validate_commit_message.return_value = True
            
            result = cmd.execute("add feature")
            assert result == 1
    
    def test_execute_commit_fails(self):
        """Test execution when commit fails."""
        cmd = CommitCommand("feat")
        
        with patch.object(cmd, 'git') as mock_git, \
             patch.object(cmd, 'validator') as mock_validator:
            
            mock_git.is_git_repository.return_value = True
            mock_git.get_staged_files.return_value = []
            mock_git.get_unstaged_files.return_value = ['test_file.py']
            mock_git.stage_all_changes.return_value = True
            mock_git.commit.return_value = False
            mock_validator.validate_commit_message.return_value = True
            
            result = cmd.execute("add feature")
            assert result == 1
    
    def test_execute_amend_fails(self):
        """Test execution when amend commit fails."""
        cmd = CommitCommand("feat")
        
        with patch.object(cmd, 'git') as mock_git, \
             patch.object(cmd, 'validator') as mock_validator, \
             patch.object(cmd, '_execute_amend_commit') as mock_amend:
            
            mock_git.is_git_repository.return_value = True
            mock_git.get_staged_files.return_value = ['test_file.py']
            mock_git.get_unstaged_files.return_value = []
            mock_amend.return_value = False
            mock_validator.validate_commit_message.return_value = True
            
            result = cmd.execute("update feature", amend=True)
            assert result == 1


class TestExecuteAmendCommit:
    """Test _execute_amend_commit method."""
    
    def test_execute_amend_success(self):
        """Test successful amend commit execution."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 0
            cmd = CommitCommand("feat")
            result = cmd._execute_amend_commit("update feature")
            assert result is True
            mock_run.assert_called_once_with(
                ['git', 'commit', '--amend', '-m', 'update feature'],
                capture_output=True,
                text=True,
                timeout=30
            )
    
    def test_execute_amend_fails(self):
        """Test amend commit execution failure."""
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 1
            mock_run.return_value.stderr = "fatal: no changes to amend"
            cmd = CommitCommand("feat")
            result = cmd._execute_amend_commit("update feature")
            assert result is False
    
    def test_execute_amend_timeout(self):
        """Test amend commit execution timeout."""
        with patch('subprocess.run') as mock_run:
            mock_run.side_effect = subprocess.TimeoutExpired('git', 30)
            cmd = CommitCommand("feat")
            result = cmd._execute_amend_commit("update feature")
            assert result is False
    
    def test_execute_amend_called_process_error(self):
        """Test amend commit execution with CalledProcessError."""
        with patch('subprocess.run') as mock_run:
            mock_run.side_effect = subprocess.CalledProcessError(1, 'git', stderr="error")
            cmd = CommitCommand("feat")
            result = cmd._execute_amend_commit("update feature")
            assert result is False
