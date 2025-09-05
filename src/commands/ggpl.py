#!/usr/bin/env python3
"""
ggpl - Pull from remote repository

Usage: ggpl [<remote>] [<branch>]
"""

import click
import sys
from core.base_commands.base import BaseCommand
from core.utils.colors import ColorManager


class GgplCommand(BaseCommand):
    """Command for git pull operations."""
    
    def execute(self, remote=None, branch=None):
        """Execute the ggpl command."""
        try:
            result = self.git.pull(remote=remote, branch=branch)
            
            if result:
                click.echo(ColorManager.success("Pull ejecutado exitosamente"))
                return 0
            else:
                click.echo(ColorManager.error("Error al ejecutar pull"))
                return 1
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {str(e)}"))
            return 1


@click.command()
@click.argument('remote', required=False)
@click.argument('branch', required=False)
def main(remote, branch):
    """Pull from remote repository"""
    try:
        # Create and run command
        cmd = GgplCommand()
        return cmd.run(remote=remote, branch=branch)
        
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
