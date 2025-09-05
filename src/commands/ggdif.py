#!/usr/bin/env python3
"""
ggdif - Show git diff

Usage: ggdif [<options>] [--] [<pathspec>...]
"""

import click
import sys
from core.base_commands.base import BaseCommand
from core.utils.colors import ColorManager


class GgdifCommand(BaseCommand):
    """Command for git diff operations."""
    
    def execute(self, files=None, staged=False):
        """Execute the ggdif command."""
        try:
            result = self.git.diff(files=files, staged=staged)
            
            if result:
                return 0
            else:
                click.echo(ColorManager.error("Error al mostrar diff"))
                return 1
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {str(e)}"))
            return 1


@click.command()
@click.option('--staged', '-s', is_flag=True, help='Show staged changes')
@click.argument('files', nargs=-1, required=False)
def main(staged, files):
    """Show git diff"""
    try:
        # Create and run command
        cmd = GgdifCommand()
        return cmd.run(files=list(files) if files else None, staged=staged)
        
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
