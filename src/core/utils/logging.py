"""
Logging module for ggGit.

This module provides centralized logging functionality
for debugging and troubleshooting.
"""

import logging
import os
from pathlib import Path
from typing import Optional


class LoggingManager:
    """Manages logging configuration for ggGit."""
    
    def __init__(self, log_level: str = "INFO"):
        """Initialize logging manager."""
        self.log_level = log_level
        self.log_dir = Path.home() / ".gggit" / "logs"
        self._setup_logging()
    
    def _setup_logging(self) -> None:
        """Setup logging configuration."""
        # Create log directory if it doesn't exist
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        # Configure logging
        logging.basicConfig(
            level=getattr(logging, self.log_level.upper()),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_dir / "gggit.log"),
                logging.StreamHandler()
            ]
        )
    
    def get_logger(self, name: str) -> logging.Logger:
        """Get logger instance for specific module."""
        return logging.getLogger(f"gggit.{name}")
    
    def set_level(self, level: str) -> None:
        """Set logging level."""
        self.log_level = level
        logging.getLogger().setLevel(getattr(logging, level.upper()))
    
    def log_command_execution(self, command: str, args: list) -> None:
        """Log command execution."""
        logger = self.get_logger("command")
        logger.info(f"Executing command: {command} with args: {args}")
    
    def log_error(self, error: Exception, context: str = "") -> None:
        """Log error with context."""
        logger = self.get_logger("error")
        logger.error(f"Error in {context}: {str(error)}", exc_info=True)
