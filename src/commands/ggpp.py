#!/usr/bin/env python3
"""
ggpp - Push to remote repository

Usage: ggpp [<remote>] [<branch>]
"""

import click
import sys
from core.base_commands.base import BaseCommand
from core.utils.colors import ColorManager


class GgppCommand(BaseCommand):
    """Command for git push operations."""
    
    def execute(self, remote=None, branch=None):
        """Execute the ggpp command."""
        try:
            result = self.git.push(remote=remote, branch=branch)
            
            if result:
                click.echo(ColorManager.success("Push ejecutado exitosamente"))
                return 0
            else:
                click.echo(ColorManager.error("Error al ejecutar push"))
                return 1
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {str(e)}"))
            return 1


@click.command()
@click.argument('remote', required=False)
@click.argument('branch', required=False)
def main(remote, branch):
    """Push to remote repository"""
    try:
        # Create and run command
        cmd = GgppCommand()
        return cmd.run(remote=remote, branch=branch)
        
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
