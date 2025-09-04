"""
Tests for LoggingManager class.

This module contains comprehensive tests for the LoggingManager class,
covering all methods and functionality as specified in the architecture.
"""

import pytest
import tempfile
import os
import logging
from pathlib import Path
from unittest.mock import patch, MagicMock

from src.core.utils.logging import LoggingManager


class TestLoggingManagerInitialization:
    """Test LoggingManager initialization."""
    
    def test_init_with_default_level(self):
        """Test initialization with default log level."""
        logger = LoggingManager()
        assert logger.log_level == "INFO"
        assert logger.log_dir == Path.home() / ".gggit" / "logs"
    
    def test_init_with_custom_level(self):
        """Test initialization with custom log level."""
        logger = LoggingManager("DEBUG")
        assert logger.log_level == "DEBUG"
        assert logger.log_dir == Path.home() / ".gggit" / "logs"
    
    def test_init_creates_log_directory(self):
        """Test that initialization creates log directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                logger = LoggingManager()
                assert logger.log_dir.exists()
                assert logger.log_dir.is_dir()


class TestSetupLogging:
    """Test _setup_logging method."""
    
    def test_setup_logging_creates_handlers(self):
        """Test that _setup_logging creates proper handlers."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                logger = LoggingManager()
                root_logger = logging.getLogger('gggit')
                
                # Should have file and console handlers
                assert len(root_logger.handlers) >= 2
                
                # Check handler types
                handler_types = [type(h).__name__ for h in root_logger.handlers]
                assert 'FileHandler' in handler_types
                assert 'StreamHandler' in handler_types
    
    def test_setup_logging_creates_log_files(self):
        """Test that _setup_logging creates log files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                logger = LoggingManager()
                
                # Check that log files exist
                assert (logger.log_dir / 'main.log').exists()
                assert (logger.log_dir / 'error.log').exists()


class TestGetLogger:
    """Test get_logger method."""
    
    def test_get_logger_returns_correct_logger(self):
        """Test that get_logger returns logger with correct name."""
        logger = LoggingManager()
        test_logger = logger.get_logger("test")
        
        assert test_logger.name == "gggit.test"
        assert isinstance(test_logger, logging.Logger)
    
    def test_get_logger_has_handlers(self):
        """Test that get_logger returns logger with handlers."""
        logger = LoggingManager()
        test_logger = logger.get_logger("test")
        
        # Should have handlers (inherited from root logger)
        assert len(test_logger.handlers) > 0
    
    def test_get_logger_different_modules(self):
        """Test get_logger with different module names."""
        logger = LoggingManager()
        
        cmd_logger = logger.get_logger("command")
        error_logger = logger.get_logger("error")
        git_logger = logger.get_logger("git")
        
        assert cmd_logger.name == "gggit.command"
        assert error_logger.name == "gggit.error"
        assert git_logger.name == "gggit.git"


class TestSetLevel:
    """Test set_level method."""
    
    def test_set_level_valid_levels(self):
        """Test set_level with valid logging levels."""
        logger = LoggingManager("INFO")
        
        for level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            logger.set_level(level)
            assert logger.log_level == level
    
    def test_set_level_case_insensitive(self):
        """Test set_level is case insensitive."""
        logger = LoggingManager("INFO")
        
        logger.set_level("debug")
        assert logger.log_level == "DEBUG"
        
        logger.set_level("Error")
        assert logger.log_level == "ERROR"
    
    def test_set_level_invalid_level(self):
        """Test set_level with invalid level raises ValueError."""
        logger = LoggingManager("INFO")
        
        with pytest.raises(ValueError, match="Invalid logging level"):
            logger.set_level("INVALID")
    
    def test_set_level_updates_loggers(self):
        """Test that set_level updates existing loggers."""
        logger = LoggingManager("INFO")
        
        # Create some loggers
        cmd_logger = logger.get_logger("command")
        error_logger = logger.get_logger("error")
        
        # Change level
        logger.set_level("DEBUG")
        
        # Check that loggers have new level
        assert cmd_logger.level == logging.DEBUG
        assert error_logger.level == logging.DEBUG


class TestLogCommandExecution:
    """Test log_command_execution method."""
    
    def test_log_command_execution_with_args(self):
        """Test logging command execution with arguments."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                logger = LoggingManager()
                
                # Mock the logger to capture messages
                with patch.object(logger, 'get_logger') as mock_get_logger:
                    mock_logger = MagicMock()
                    mock_get_logger.return_value = mock_logger
                    
                    logger.log_command_execution("ggfeat", ["add feature", "--scope", "test"])
                    
                    # Verify logger was called
                    mock_logger.info.assert_called_once()
                    call_args = mock_logger.info.call_args[0][0]
                    assert "Executing command: ggfeat" in call_args
                    assert "add feature --scope test" in call_args
    
    def test_log_command_execution_without_args(self):
        """Test logging command execution without arguments."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                logger = LoggingManager()
                
                with patch.object(logger, 'get_logger') as mock_get_logger:
                    mock_logger = MagicMock()
                    mock_get_logger.return_value = mock_logger
                    
                    logger.log_command_execution("ggfeat", [])
                    
                    mock_logger.info.assert_called_once()
                    call_args = mock_logger.info.call_args[0][0]
                    assert "Executing command: ggfeat" in call_args
                    assert "with args:" not in call_args


class TestLogError:
    """Test log_error method."""
    
    def test_log_error_with_context(self):
        """Test logging error with context."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                logger = LoggingManager()
                
                with patch.object(logger, 'get_logger') as mock_get_logger:
                    mock_logger = MagicMock()
                    mock_get_logger.return_value = mock_logger
                    
                    error = ValueError("Test error")
                    logger.log_error(error, "test_function")
                    
                    mock_logger.error.assert_called_once()
                    call_args = mock_logger.error.call_args[0][0]
                    assert "Error occurred in test_function" in call_args
                    assert "Test error" in call_args
                    
                    # Check that exc_info=True was passed
                    assert mock_logger.error.call_args[1]['exc_info'] is True
    
    def test_log_error_without_context(self):
        """Test logging error without context."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                logger = LoggingManager()
                
                with patch.object(logger, 'get_logger') as mock_get_logger:
                    mock_logger = MagicMock()
                    mock_get_logger.return_value = mock_logger
                    
                    error = ValueError("Test error")
                    logger.log_error(error)
                    
                    mock_logger.error.assert_called_once()
                    call_args = mock_logger.error.call_args[0][0]
                    assert "Error occurred" in call_args
                    assert "Test error" in call_args
                    assert "in " not in call_args


class TestGetLogFilePath:
    """Test get_log_file_path method."""
    
    def test_get_log_file_path_default(self):
        """Test get_log_file_path with default log type."""
        logger = LoggingManager()
        path = logger.get_log_file_path()
        
        assert path == logger.log_dir / "main.log"
    
    def test_get_log_file_path_custom_type(self):
        """Test get_log_file_path with custom log type."""
        logger = LoggingManager()
        path = logger.get_log_file_path("error")
        
        assert path == logger.log_dir / "error.log"
    
    def test_get_log_file_path_different_types(self):
        """Test get_log_file_path with different log types."""
        logger = LoggingManager()
        
        main_path = logger.get_log_file_path("main")
        error_path = logger.get_log_file_path("error")
        perf_path = logger.get_log_file_path("performance")
        
        assert main_path == logger.log_dir / "main.log"
        assert error_path == logger.log_dir / "error.log"
        assert perf_path == logger.log_dir / "performance.log"


class TestLoggingIntegration:
    """Test logging integration with real file output."""
    
    def test_logging_creates_files(self):
        """Test that logging creates log files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                logger = LoggingManager("DEBUG")
                
                # Check that files were created
                main_log = logger.log_dir / "main.log"
                error_log = logger.log_dir / "error.log"
                
                assert main_log.exists()
                assert error_log.exists()
