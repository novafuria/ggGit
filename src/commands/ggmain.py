#!/usr/bin/env python3
"""
ggmain - Checkout main branch

Usage: ggmain
"""

import click
import sys
from core.base_commands.base import BaseCommand
from core.utils.colors import ColorManager


class GgmainCommand(BaseCommand):
    """Command for checkout to main branch."""
    
    def execute(self):
        """Execute the ggmain command."""
        try:
            if not self.git.is_git_repository():
                click.echo(ColorManager.error("Not a git repository"))
                return 1
            
            result = self.git.switch_branch("main")
            
            if result:
                click.echo(ColorManager.success("Cambiado a rama main"))
                return 0
            else:
                click.echo(ColorManager.error("Error al cambiar a rama main"))
                return 1
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {str(e)}"))
            return 1


@click.command()
def main():
    """Checkout main branch"""
    try:
        # Create and run command
        cmd = GgmainCommand()
        return cmd.run()
        
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
