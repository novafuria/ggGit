"""
Tests for command modules.
"""

import unittest
from src.core.base_commands.commit import CommitCommand


class TestCommitCommand(unittest.TestCase):
    """Test cases for CommitCommand."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.commit_cmd = CommitCommand("feat")
    
    def test_commit_command_initialization(self):
        """Test CommitCommand initialization."""
        self.assertIsInstance(self.commit_cmd, CommitCommand)
        self.assertEqual(self.commit_cmd.commit_type, "feat")
    
    def test_format_commit_message_with_scope(self):
        """Test formatting commit message with scope."""
        message = "Add new feature"
        scope = "auth"
        expected = "feat(auth): Add new feature"
        result = self.commit_cmd.format_commit_message(message, scope)
        self.assertEqual(result, expected)
    
    def test_format_commit_message_without_scope(self):
        """Test formatting commit message without scope."""
        message = "Add new feature"
        expected = "feat: Add new feature"
        result = self.commit_cmd.format_commit_message(message)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
