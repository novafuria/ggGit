"""
CLI abstraction module for ggGit.

This module provides base CLI functionality and abstractions
for command-line interface operations.
"""

import click
from typing import Optional, List, Any


class CLIBase:
    """Base class for CLI operations."""
    
    def __init__(self):
        """Initialize CLI base."""
        pass
    
    def print_success(self, message: str) -> None:
        """Print success message with green color."""
        click.echo(click.style(f"✅ {message}", fg="green"))
    
    def print_error(self, message: str) -> None:
        """Print error message with red color."""
        click.echo(click.style(f"❌ {message}", fg="red"))
    
    def print_warning(self, message: str) -> None:
        """Print warning message with yellow color."""
        click.echo(click.style(f"⚠️ {message}", fg="yellow"))
    
    def print_info(self, message: str) -> None:
        """Print info message with blue color."""
        click.echo(click.style(f"ℹ️ {message}", fg="blue"))
