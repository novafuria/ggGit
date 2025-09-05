#!/usr/bin/env python3
"""
ggreset - Reset --hard HEAD

Usage: ggreset
"""

import click
import sys
from core.base_commands.base import BaseCommand
from core.utils.colors import ColorManager


class GgresetCommand(BaseCommand):
    """Command for git reset --hard operations."""
    
    def execute(self):
        """Execute the ggreset command."""
        try:
            result = self.git.reset_hard()
            
            if result:
                click.echo(ColorManager.success("Reset --hard HEAD ejecutado exitosamente"))
                return 0
            else:
                click.echo(ColorManager.error("Error al ejecutar reset --hard HEAD"))
                return 1
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {str(e)}"))
            return 1


@click.command()
def main():
    """Reset --hard HEAD"""
    try:
        # Create and run command
        cmd = GgresetCommand()
        return cmd.run()
        
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
