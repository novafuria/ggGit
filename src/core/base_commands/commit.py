"""
Commit command base class for ggGit.

This module provides the base functionality for commit-related commands
like ggfeat, ggfix, ggbreak, etc.
"""

from typing import Optional
from .base import BaseCommand
from ..git import GitInterface


class CommitCommand(BaseCommand):
    """Base class for commit commands."""
    
    def __init__(self, commit_type: str):
        """Initialize commit command with specific type."""
        super().__init__()
        self.commit_type = commit_type
    
    def execute(self, message: str, scope: Optional[str] = None, amend: bool = False) -> int:
        """
        Execute commit command with validation and Git operations.
        
        This method performs a complete commit operation including:
        - Input validation using ArgumentValidator
        - Git repository verification
        - Change detection and staging
        - Commit message formatting
        - Git commit execution (regular or amend)
        
        Args:
            message (str): Commit message (validated for length and format)
            scope (Optional[str]): Optional scope for Conventional Commits format
            amend (bool): If True, amend the last commit instead of creating new one
            
        Returns:
            int: Exit code (0 for success, 1 for failure)
            
        Raises:
            ValueError: For invalid input arguments (message, scope)
            GitInterfaceError: For Git-related errors
        """
        try:
            # Validate inputs using ArgumentValidator
            self.validator.validate_commit_message(message)
            if scope:
                self.validator.validate_scope(scope)
            
            # Check if we're in a git repository
            if not self.git.is_git_repository():
                self.logger.log_error(Exception("No es un repositorio Git válido"), "execute")
                return 1
            
            # Check if there are changes to commit (only for regular commits, not amend)
            if not amend:
                staged_files = self.git.get_staged_files()
                unstaged_files = self.git.get_unstaged_files()
                
                if not staged_files and not unstaged_files:
                    self.logger.log_error(Exception("No hay cambios para hacer commit"), "execute")
                    return 1
                
                # Stage all changes if there are unstaged files
                if unstaged_files:
                    if not self.git.stage_all_changes():
                        self.logger.log_error(Exception("Error al stagear cambios"), "execute")
                        return 1
            
            # Format commit message
            commit_message = self.format_commit_message(message, scope)
            
            # Execute commit (with amend if requested)
            if amend:
                if not self._execute_amend_commit(commit_message):
                    self.logger.log_error(Exception("Error al realizar commit --amend"), "execute")
                    return 1
            else:
                if not self.git.commit(commit_message):
                    self.logger.log_error(Exception("Error al realizar commit"), "execute")
                    return 1
            
            return 0
            
        except ValueError as e:
            self.logger.log_error(e, "execute")
            return 1
        except Exception as e:
            self.logger.log_error(e, "execute")
            return 1
    
    def _execute_amend_commit(self, message: str) -> bool:
        """
        Execute git commit --amend with the given message.
        
        This method performs a git commit --amend operation with proper
        error handling for timeouts and command failures.
        
        Args:
            message (str): Commit message for the amended commit
            
        Returns:
            bool: True if amend was successful, False otherwise
        """
        try:
            import subprocess
            result = subprocess.run(
                ['git', 'commit', '--amend', '-m', message],
                capture_output=True,
                text=True,
                timeout=30
            )
            return result.returncode == 0
        except subprocess.TimeoutExpired:
            self.logger.log_error(Exception("Timeout al ejecutar 'git commit --amend'"), "_execute_amend_commit")
            return False
        except subprocess.CalledProcessError as e:
            self.logger.log_error(Exception(f"Error al ejecutar 'git commit --amend' (código {e.returncode}): {e.stderr}"), "_execute_amend_commit")
            return False
        except Exception as e:
            self.logger.log_error(e, "_execute_amend_commit")
            return False
    
    def format_commit_message(self, message: str, scope: Optional[str] = None) -> str:
        """
        Format commit message according to Conventional Commits specification.
        
        Creates a properly formatted commit message using the commit type
        and optional scope. Format: "type(scope): message" or "type: message".
        
        Args:
            message (str): The commit message content
            scope (Optional[str]): Optional scope for the commit
            
        Returns:
            str: Formatted commit message following Conventional Commits
        """
        if scope:
            return f"{self.commit_type}({scope}): {message}"
        return f"{self.commit_type}: {message}"
