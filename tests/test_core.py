"""
Tests for core modules.
"""

import unittest
from src.core.config import ConfigManager
from src.core.git import GitInterface
from src.core.validation import ArgumentValidator


class TestConfigManager(unittest.TestCase):
    """Test cases for ConfigManager."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.config = ConfigManager()
    
    def test_config_initialization(self):
        """Test ConfigManager initialization."""
        self.assertIsInstance(self.config, ConfigManager)
        self.assertIsInstance(self.config.config, dict)


class TestGitInterface(unittest.TestCase):
    """Test cases for GitInterface."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.git = GitInterface()
    
    def test_git_initialization(self):
        """Test GitInterface initialization."""
        self.assertIsInstance(self.git, GitInterface)


class TestArgumentValidator(unittest.TestCase):
    """Test cases for ArgumentValidator."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.validator = ArgumentValidator()
    
    def test_validator_initialization(self):
        """Test ArgumentValidator initialization."""
        self.assertIsInstance(self.validator, ArgumentValidator)
    
    def test_validate_commit_message_empty(self):
        """Test validation of empty commit message."""
        with self.assertRaises(ValueError):
            self.validator.validate_commit_message("")
    
    def test_validate_commit_message_too_long(self):
        """Test validation of commit message that's too long."""
        long_message = "a" * 73
        with self.assertRaises(ValueError):
            self.validator.validate_commit_message(long_message)
    
    def test_validate_commit_message_valid(self):
        """Test validation of valid commit message."""
        self.assertTrue(self.validator.validate_commit_message("Valid commit message"))


if __name__ == '__main__':
    unittest.main()
