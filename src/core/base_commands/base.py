"""
Base command class for ggGit.

This module provides the base command class that all ggGit commands
should extend for consistent behavior and shared functionality.
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Any
from ..cli import CLIBase
from ..config import ConfigManager
from ..git import GitInterface
from ..validation import ArgumentValidator


class BaseCommand(ABC):
    """Base class for all ggGit commands."""
    
    def __init__(self):
        """Initialize base command."""
        self.cli = CLIBase()
        self.config = ConfigManager()
        self.git = GitInterface()
        self.validator = ArgumentValidator()
    
    @abstractmethod
    def execute(self, *args, **kwargs) -> int:
        """Execute the command. Must be implemented by subclasses."""
        pass
    
    def validate_args(self, args: List[str]) -> bool:
        """Validate command arguments."""
        # TODO: Implement common argument validation
        return True
    
    def setup_logging(self) -> None:
        """Setup logging for the command."""
        # TODO: Implement logging setup
        pass
    
    def run(self, *args, **kwargs) -> int:
        """Run the command with error handling."""
        try:
            self.setup_logging()
            return self.execute(*args, **kwargs)
        except Exception as e:
            self.cli.print_error(f"Error: {str(e)}")
            return 1
