"""
Base command class for ggGit.

This module provides the base command class that all ggGit commands
should extend for consistent behavior and shared functionality.

The BaseCommand class follows the Template Method pattern, providing:
- Standardized initialization of core components
- Common error handling and logging setup
- Abstract execute method that subclasses must implement
- Consistent interface for all ggGit commands

Usage:
    class MyCommand(BaseCommand):
        def execute(self, *args, **kwargs) -> int:
            # Implement command logic here
            return 0
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Any, Dict
import os
import click
from ..utils.colors import ColorManager
from ..config import ConfigManager
from ..git import GitInterface
from ..validation import ArgumentValidator
from ..utils.logging import LoggingManager


class BaseCommand(ABC):
    """
    Base class for all ggGit commands.
    
    This class provides a standardized foundation for all ggGit commands,
    ensuring consistent behavior, error handling, and component access.
    
    Attributes:
        config (ConfigManager): Configuration management instance
        git (GitInterface): Git operations interface
        validator (ArgumentValidator): Input validation utilities
        logger (LoggingManager): Logging management instance
        
    Example:
        class FeatureCommand(BaseCommand):
            def execute(self, message: str, scope: Optional[str] = None) -> int:
                # Validate inputs
                self.validator.validate_commit_message(message)
                if scope:
                    self.validator.validate_scope(scope)
                
                # Use git interface
                if not self.git.is_git_repository():
                    click.echo(ColorManager.error("Not a git repository"))
                    return 1
                
                # Execute command logic
                return 0
    """
    
    def __init__(self):
        """
        Initialize base command with all required components.
        
        This method initializes the core components that all commands need:
        - ConfigManager for configuration access
        - GitInterface for git operations
        - ArgumentValidator for input validation
        - LoggingManager for logging functionality
        
        Subclasses should call super().__init__() in their constructors
        and can add command-specific initialization after this call.
        """
        self.config = ConfigManager()
        self.git = GitInterface()
        self.validator = ArgumentValidator()
        self.logger = LoggingManager()
    
    @abstractmethod
    def execute(self, *args, **kwargs) -> int:
        """
        Execute the command logic.
        
        This method must be implemented by all subclasses and contains
        the main command logic. It should:
        1. Validate inputs using self.validator
        2. Use self.git for git operations
        3. Use self.config for configuration access
        4. Use self.logger for logging
        5. Return 0 for success, non-zero for failure
        
        Args:
            *args: Positional arguments passed to the command
            **kwargs: Keyword arguments passed to the command
            
        Returns:
            int: Exit code (0 for success, non-zero for failure)
            
        Raises:
            ValueError: For invalid input arguments
            RuntimeError: For command execution failures
        """
        pass
    
    def validate_args(self, args: List[str]) -> bool:
        """
        Validate command arguments.
        
        This method provides common argument validation that can be
        overridden by subclasses for command-specific validation.
        
        Args:
            args: List of command arguments to validate
            
        Returns:
            bool: True if arguments are valid, False otherwise
            
        Note:
            Subclasses should override this method for specific validation
            requirements. The base implementation always returns True.
        """
        return True
    
    def setup_logging(self) -> None:
        """
        Setup logging for the command.
        
        This method configures logging for the command execution.
        It can be overridden by subclasses for command-specific logging setup.
        
        Note:
            The base implementation uses the LoggingManager instance
            created in __init__. Subclasses can override for custom logging.
        """
        # Log command execution start
        command_name = self.__class__.__name__
        self.logger.log_command_execution(command_name, [])
    
    def run(self, *args, **kwargs) -> int:
        """
        Run the command with standardized error handling.
        
        This method provides the main entry point for command execution,
        handling common concerns like logging setup and error handling.
        
        Args:
            *args: Positional arguments to pass to execute()
            **kwargs: Keyword arguments to pass to execute()
            
        Returns:
            int: Exit code from execute() method, or 1 if an error occurs
        """
        try:
            self.setup_logging()
            return self.execute(*args, **kwargs)
        except Exception as e:
            # Log the error
            self.logger.log_error(e, f"{self.__class__.__name__}.execute")
            
            # Display user-friendly error message
            click.echo(ColorManager.error(f"Error: {str(e)}"))
            return 1
    
    def _is_ai_configured(self) -> bool:
        """
        Check if AI is configured and available.
        
        This method verifies that AI functionality is properly configured
        by checking the required configuration settings and environment variables.
        
        Returns:
            bool: True if AI is configured and available, False otherwise
            
        Note:
            This method checks:
            - ai.enabled is True
            - ai.provider is set
            - ai.api_key_env environment variable is available
        """
        # Verificar configuración básica
        if not self.config.get_config('ai.enabled', False):
            return False
        
        # Verificar proveedor
        provider = self.config.get_config('ai.provider')
        if not provider:
            return False
        
        # Verificar API key
        api_key_env = self.config.get_config('ai.api_key_env')
        if not api_key_env or not os.getenv(api_key_env):
            return False
        
        return True
    
    def _generate_ai_message(self, scope=None, amend=False):
        """
        Generate commit message using AI.
        
        This method integrates with the AI system to generate commit messages
        based on the current changes, using complexity analysis to decide
        between AI generation and educational fallback.
        
        Args:
            scope (str, optional): Scope for the commit message
            amend (bool): Whether to amend the last commit
            
        Returns:
            int: Exit code (0 for success, 1 for failure)
        """
        try:
            from ..ai import ComplexityAnalyzer, AiMessageGenerator, AiUsageTracker
            
            # Create AI components
            analyzer = ComplexityAnalyzer(self.git, self.config)
            usage_tracker = AiUsageTracker(self.config)
            generator = AiMessageGenerator(self.config, usage_tracker)
            
            # Analyze complexity
            should_use_ai, analysis = analyzer.should_use_ai()
            
            if should_use_ai:
                # Generate with AI
                files = analysis['files']
                diff_content = self.git.get_diff_content(files, staged=analysis['has_staged'])
                message = generator.generate_message(files, diff_content)
                
                # Add scope if provided
                if scope:
                    prefix = message.split(':', 1)[0]
                    suffix = message.split(':', 1)[1] if ':' in message else message
                    message = f"{prefix}({scope}): {suffix}"
                
                # Execute commit with generated message
                return self._execute_manual_commit(message, scope, amend)
            else:
                # Show fallback
                fallback = analyzer.get_fallback_message(analysis)
                click.echo(ColorManager.warning(fallback))
                return 1
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error generando mensaje con IA: {e}"))
            return 1
    
    def _execute_manual_commit(self, message, scope=None, amend=False):
        """
        Execute commit with manual message.
        
        This method handles the common commit logic for all commands,
        including validation, prefix handling, and commit execution.
        
        Args:
            message (str): Commit message
            scope (str, optional): Scope for the commit message
            amend (bool): Whether to amend the last commit
            
        Returns:
            int: Exit code (0 for success, 1 for failure)
        """
        try:
            # Validate message
            if not message or not message.strip():
                click.echo(ColorManager.error("Message is required"))
                return 1
            
            # Validate input
            if message:
                self.validator.validate_commit_message(message)
            
            # Create commit command
            from .commit import CommitCommand
            commit_cmd = CommitCommand(self._get_commit_prefix())
            
            # Execute commit
            result = commit_cmd.execute(message, scope, amend)
            
            if result == 0:
                click.echo(ColorManager.success("Commit realizado exitosamente"))
            else:
                click.echo(ColorManager.error("Error al realizar commit"))
                return result
            
            return result
            
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {e}"))
            return 1
    
    def _get_commit_prefix(self):
        """
        Get the commit prefix for this command.
        
        This method should be overridden by subclasses to return
        the appropriate prefix (feat, fix, docs, etc.).
        
        Returns:
            str: Commit prefix
        """
        return "chore"  # Default fallback
    
    def get_command_info(self) -> Dict[str, Any]:
        """
        Get information about this command.
        
        Returns:
            Dict containing command metadata for debugging and help
        """
        return {
            "command_class": self.__class__.__name__,
            "module": self.__class__.__module__,
            "has_config": hasattr(self, 'config'),
            "has_git": hasattr(self, 'git'),
            "has_validator": hasattr(self, 'validator'),
            "has_logger": hasattr(self, 'logger')
        }
