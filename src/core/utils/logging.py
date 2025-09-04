"""
Logging module for ggGit.

This module provides centralized logging functionality
for debugging and troubleshooting.

The LoggingManager class provides a unified logging interface that
handles both file and console logging with configurable levels.
It creates structured log files in the user's .gggit directory and
provides specialized logging methods for different types of events.

Log files are organized by date and include detailed context information
to aid in debugging and monitoring command execution.
"""

import logging
import os
from pathlib import Path
from typing import Optional, Dict, Any
from datetime import datetime


class LoggingManager:
    """
    Manages logging configuration and provides logging utilities for ggGit.
    
    This class provides a centralized logging system that handles both
    file and console output with configurable log levels. It creates
    structured log files and provides specialized logging methods for
    different types of events (commands, errors, debug info, etc.).
    
    Log files are stored in ~/.gggit/logs/ and include timestamps,
    log levels, and contextual information for easy debugging.
    
    Attributes:
        log_level (str): Current logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_dir (Path): Directory where log files are stored
        
    Example:
        logger = LoggingManager(log_level="DEBUG")
        
        # Get a module-specific logger
        cmd_logger = logger.get_logger("command")
        cmd_logger.info("Command executed successfully")
        
        # Log command execution
        logger.log_command_execution("ggfeat", ["add user auth"])
        
        # Log errors with context
        try:
            risky_operation()
        except Exception as e:
            logger.log_error(e, "risky_operation")
    """
    
    def __init__(self, log_level: str = "INFO"):
        """
        Initialize logging manager.
        
        Sets up the logging system with the specified log level and
        creates the necessary log directory structure.
        
        Args:
            log_level (str): Initial logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            
        Note:
            This method will be implemented in STORY-1.2.3 - comandos base
        """
        self.log_level = log_level
        self.log_dir = Path.home() / ".gggit" / "logs"
        self._setup_logging()
    
    def _setup_logging(self) -> None:
        """
        Setup logging configuration.
        
        Creates the log directory and configures the logging system
        with both file and console handlers. The configuration includes
        timestamps, log levels, and structured formatting.
        """
        # Create log directory if it doesn't exist
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        # Configure root logger
        root_logger = logging.getLogger('gggit')
        root_logger.setLevel(getattr(logging, self.log_level.upper()))
        
        # Clear any existing handlers
        root_logger.handlers.clear()
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # File handler for main logs
        main_log_file = self.log_dir / 'main.log'
        file_handler = logging.FileHandler(main_log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)
        
        # File handler for errors
        error_log_file = self.log_dir / 'error.log'
        error_handler = logging.FileHandler(error_log_file, encoding='utf-8')
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(formatter)
        root_logger.addHandler(error_handler)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(getattr(logging, self.log_level.upper()))
        console_handler.setFormatter(formatter)
        root_logger.addHandler(console_handler)
        
        # Prevent propagation to root logger
        root_logger.propagate = False
    
    def get_logger(self, name: str) -> logging.Logger:
        """
        Get logger instance for specific module.
        
        Creates a logger instance with the gggit namespace prefix
        for the specified module. This ensures consistent naming
        and easy filtering of log messages.
        
        Args:
            name (str): Module name for the logger
            
        Returns:
            logging.Logger: Configured logger instance
            
        Example:
            logger = logging_manager.get_logger("command")
            logger.info("This will appear as gggit.command")
        """
        # Create logger with gggit.{name} namespace
        logger_name = f"gggit.{name}"
        logger = logging.getLogger(logger_name)
        
        # Set level to match the logging manager
        logger.setLevel(getattr(logging, self.log_level.upper()))
        
        # Don't add handlers if they already exist (prevent duplicates)
        if not logger.handlers:
            # Get the root gggit logger to inherit its handlers
            root_logger = logging.getLogger('gggit')
            for handler in root_logger.handlers:
                logger.addHandler(handler)
        
        # Prevent propagation to avoid duplicate logs
        logger.propagate = False
        
        return logger
    
    def set_level(self, level: str) -> None:
        """
        Set logging level for all loggers.
        
        Changes the logging level for all loggers in the ggGit
        namespace. This affects both file and console output.
        
        Args:
            level (str): New logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            
        Raises:
            ValueError: If level is not a valid logging level
        """
        # Validate logging level
        valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if level.upper() not in valid_levels:
            raise ValueError(f"Invalid logging level: {level}. Must be one of {valid_levels}")
        
        # Update internal log_level attribute
        self.log_level = level.upper()
        
        # Update root logger level
        root_logger = logging.getLogger('gggit')
        root_logger.setLevel(getattr(logging, self.log_level))
        
        # Update console handler level
        for handler in root_logger.handlers:
            if isinstance(handler, logging.StreamHandler) and not isinstance(handler, logging.FileHandler):
                handler.setLevel(getattr(logging, self.log_level))
        
        # Update all existing gggit.* loggers
        for logger_name in logging.Logger.manager.loggerDict:
            if logger_name.startswith('gggit.'):
                logger = logging.getLogger(logger_name)
                logger.setLevel(getattr(logging, self.log_level))
    
    def log_command_execution(self, command: str, args: list) -> None:
        """
        Log command execution with arguments.
        
        Logs the execution of a command with its arguments for
        debugging and audit purposes. This is automatically called
        by BaseCommand.setup_logging().
        
        Args:
            command (str): Name of the command being executed
            args (list): List of arguments passed to the command
            
        Example:
            logger.log_command_execution("ggfeat", ["add user auth", "--scope", "auth"])
        """
        # Get command logger
        logger = self.get_logger("command")
        
        # Format command and args for logging
        args_str = " ".join(str(arg) for arg in args) if args else ""
        message = f"Executing command: {command}"
        if args_str:
            message += f" with args: {args_str}"
        
        # Log with INFO level
        logger.info(message)
    
    def log_error(self, error: Exception, context: str = "") -> None:
        """
        Log error with context and stack trace.
        
        Logs an error with full context information including
        the stack trace for debugging purposes.
        
        Args:
            error (Exception): The exception that occurred
            context (str): Additional context about where the error occurred
            
        Example:
            try:
                risky_operation()
            except ValueError as e:
                logger.log_error(e, "risky_operation")
        """
        # Get error logger
        logger = self.get_logger("error")
        
        # Format error message with context
        message = f"Error occurred"
        if context:
            message += f" in {context}"
        message += f": {str(error)}"
        
        # Log with ERROR level and exc_info=True for stack trace
        logger.error(message, exc_info=True)
    
    def log_performance(self, operation: str, duration: float, details: Optional[Dict[str, Any]] = None) -> None:
        """
        Log performance metrics for operations.
        
        Logs performance information for operations that may be
        slow or resource-intensive. Useful for monitoring and optimization.
        
        Args:
            operation (str): Name of the operation
            duration (float): Duration in seconds
            details (Optional[Dict[str, Any]]): Additional performance details
            
        Example:
            start_time = time.time()
            # ... perform operation ...
            duration = time.time() - start_time
            logger.log_performance("git_commit", duration, {"files_count": 5})
            
        Note:
            This method will be implemented in STORY-1.2.3 - comandos base
        """
        # TODO: Implement performance logging
        # 1. Get performance logger
        # 2. Format performance metrics
        # 3. Log with INFO level
        pass
    
    def log_config_change(self, key: str, old_value: Any, new_value: Any, level: str) -> None:
        """
        Log configuration changes.
        
        Logs when configuration values are changed, including
        the old and new values and the configuration level.
        
        Args:
            key (str): Configuration key that was changed
            old_value (Any): Previous value
            new_value (Any): New value
            level (str): Configuration level (repo, user, etc.)
            
        Example:
            logger.log_config_change("commit.format", "simple", "conventional", "user")
            
        Note:
            This method will be implemented in STORY-1.2.3 - comandos base
        """
        # TODO: Implement configuration change logging
        # 1. Get config logger
        # 2. Format configuration change details
        # 3. Log with INFO level
        pass
    
    def get_log_file_path(self, log_type: str = "main") -> Path:
        """
        Get the path to a specific log file.
        
        Args:
            log_type (str): Type of log file (main, error, performance, etc.)
            
        Returns:
            Path: Path to the log file
            
        Note:
            This method will be implemented in STORY-1.2.3 - comandos base
        """
        # TODO: Implement log file path generation
        # 1. Generate log file name based on type and date
        # 2. Return full path to log file
        return self.log_dir / f"{log_type}.log"
    
    def cleanup_old_logs(self, days_to_keep: int = 30) -> None:
        """
        Clean up old log files.
        
        Removes log files older than the specified number of days
        to prevent disk space issues.
        
        Args:
            days_to_keep (int): Number of days of logs to keep
            
        Note:
            This method will be implemented in STORY-1.2.3 - comandos base
        """
        # TODO: Implement log cleanup
        # 1. Find log files older than specified days
        # 2. Remove old log files
        # 3. Log cleanup activity
        pass
