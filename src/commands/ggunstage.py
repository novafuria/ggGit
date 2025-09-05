#!/usr/bin/env python3
"""
ggunstage - Unstage files from index

Usage: ggunstage [<file>...]
"""

import click
import sys
from core.base_commands.base import BaseCommand
from core.utils.colors import ColorManager


class GgunstageCommand(BaseCommand):
    """Command for git unstage operations."""
    
    def execute(self, files=None):
        """Execute the ggunstage command."""
        try:
            result = self.git.unstage_files(files=files)
            
            if result:
                click.echo(ColorManager.success("Archivos removidos del stage exitosamente"))
                return 0
            else:
                click.echo(ColorManager.error("Error al remover archivos del stage"))
                return 1
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {str(e)}"))
            return 1


@click.command()
@click.argument('files', nargs=-1, required=False)
def main(files):
    """Unstage files from index"""
    try:
        # Create and run command
        cmd = GgunstageCommand()
        return cmd.run(files=list(files) if files else None)
        
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
