#!/usr/bin/env python3
"""
ggdevelop - Checkout develop branch

Usage: ggdevelop
"""

import click
import sys
from core.base_commands.base import BaseCommand
from core.utils.colors import ColorManager


class GgdevelopCommand(BaseCommand):
    """Command for checkout to develop branch."""
    
    def execute(self):
        """Execute the ggdevelop command."""
        try:
            if not self.git.is_git_repository():
                click.echo(ColorManager.error("Not a git repository"))
                return 1
            
            result = self.git.switch_branch("develop")
            
            if result:
                click.echo(ColorManager.success("Cambiado a rama develop"))
                return 0
            else:
                click.echo(ColorManager.error("Error al cambiar a rama develop"))
                return 1
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {str(e)}"))
            return 1


@click.command()
def main():
    """Checkout develop branch"""
    try:
        # Create and run command
        cmd = GgdevelopCommand()
        return cmd.run()
        
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
