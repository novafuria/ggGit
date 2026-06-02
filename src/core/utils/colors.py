"""
Color management module for ggGit.

This module provides a unified color system for consistent
output formatting across all commands.
"""

from typing import Optional

import click


class ColorManager:
    """Manages color output for ggGit commands."""

    @staticmethod
    def success(message: str) -> str:
        """Format success message in green."""
        return click.style(f"✅ {message}", fg="green")

    @staticmethod
    def error(message: str) -> str:
        """Format error message in red."""
        return click.style(f"❌ {message}", fg="red")

    @staticmethod
    def warning(message: str) -> str:
        """Format warning message in yellow."""
        return click.style(f"⚠️ {message}", fg="yellow")

    @staticmethod
    def info(message: str) -> str:
        """Format info message in blue."""
        return click.style(f"ℹ️ {message}", fg="blue")

    @staticmethod
    def operation(message: str) -> str:
        """Format operation message in cyan."""
        return click.style(f"🔄 {message}", fg="cyan")

    @staticmethod
    def highlight(message: str) -> str:
        """Format highlighted message in bold."""
        return click.style(message, bold=True)

    @staticmethod
    def dim(message: str) -> str:
        """Format dimmed message."""
        return click.style(message, dim=True)
