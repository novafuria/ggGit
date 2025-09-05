#!/usr/bin/env python3
"""
gga - Add file contents to the index

Usage: gga [<file>...]
"""

import click
import sys
from core.base_commands.base import BaseCommand
from core.utils.colors import ColorManager


class GgaCommand(BaseCommand):
    """Command for git add operations."""
    
    def execute(self, files=None, all=False):
        """Execute the gga command."""
        try:
            if all or not files:
                result = self.git.stage_all_changes()
            else:
                result = self.git.stage_files(files)
            
            if result:
                click.echo(ColorManager.success("Archivos agregados exitosamente"))
                return 0
            else:
                click.echo(ColorManager.error("Error al agregar archivos"))
                return 1
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {str(e)}"))
            return 1


@click.command()
@click.option('--all', '-a', is_flag=True, help='Add all changes')
@click.argument('files', nargs=-1, required=False)
def main(all, files):
    """Add file contents to the index"""
    try:
        # Create and run command
        cmd = GgaCommand()
        return cmd.run(files=list(files) if files else None, all=all)
        
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
