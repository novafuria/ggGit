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
        """Execute commit command."""
        try:
            # Initialize Git interface
            git = GitInterface()
            
            # Check if we're in a git repository
            if not git.is_git_repository():
                self.logger.error("No es un repositorio Git válido")
                return 1
            
            # Stage all changes
            if not git.stage_all_changes():
                self.logger.error("Error al stagear cambios")
                return 1
            
            # Format commit message
            commit_message = self.format_commit_message(message, scope)
            
            # Execute commit
            if not git.commit(commit_message):
                self.logger.error("Error al realizar commit")
                return 1
            
            return 0
            
        except Exception as e:
            self.logger.error(f"Error inesperado: {str(e)}")
            return 1
    
    def format_commit_message(self, message: str, scope: Optional[str] = None) -> str:
        """Format commit message according to Conventional Commits."""
        if scope:
            return f"{self.commit_type}({scope}): {message}"
        return f"{self.commit_type}: {message}"
