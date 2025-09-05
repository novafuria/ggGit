#!/usr/bin/env python3
"""
ggv - Show git version

Usage: ggv
"""

import click
import sys
from core.base_commands.base import BaseCommand
from core.utils.colors import ColorManager


class GgvCommand(BaseCommand):
    """Command for git version operations."""
    
    def execute(self):
        """Execute the ggv command."""
        try:
            version = self.git.get_version()
            click.echo(version)
            return 0
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {str(e)}"))
            return 1


@click.command()
def main():
    """Show git version"""
    try:
        # Create and run command
        cmd = GgvCommand()
        return cmd.run()
        
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
