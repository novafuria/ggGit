#!/usr/bin/env python3
"""
ggl - Show git log

Usage: ggl [<options>] [--] [<pathspec>...]
"""

import click
import sys
import subprocess
from core.base_commands.base import BaseCommand
from core.utils.colors import ColorManager


class GglCommand(BaseCommand):
    """Command for git log operations."""
    
    def execute(self, options=None, pathspec=None):
        """Execute the ggl command."""
        try:
            if not self.git.is_git_repository():
                click.echo(ColorManager.error("Not a git repository"))
                return 1
            
            # Build git log command with default format
            cmd = ['git', 'log', '--oneline', '--graph', '--all', '--decorate']
            if options:
                cmd.extend(options)
            if pathspec:
                cmd.extend(pathspec)
            
            # Execute git log
            result = subprocess.run(cmd, capture_output=False, text=True)
            
            if result.returncode == 0:
                return 0
            else:
                click.echo(ColorManager.error("Error al mostrar log"))
                return 1
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {str(e)}"))
            return 1


@click.command()
@click.argument('args', nargs=-1, required=False)
def main(args):
    """Show git log"""
    try:
        # Create and run command
        cmd = GglCommand()
        return cmd.run(options=list(args) if args else None)
        
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
