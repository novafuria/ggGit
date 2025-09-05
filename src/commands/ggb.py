#!/usr/bin/env python3
"""
ggb - List all branches

Usage: ggb
"""

import click
import sys
from core.base_commands.base import BaseCommand
from core.utils.colors import ColorManager


class GgbCommand(BaseCommand):
    """Command for listing all branches."""
    
    def execute(self):
        """Execute the ggb command."""
        try:
            if not self.git.is_git_repository():
                click.echo(ColorManager.error("Not a git repository"))
                return 1
            
            branches = self.git.get_all_branches()
            current_branch = self.git.get_current_branch()
            
            self._display_branches(branches, current_branch)
            return 0
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {str(e)}"))
            return 1
    
    def _display_branches(self, branches, current_branch):
        """Display branches with colors and indicators."""
        # Display local branches
        if branches["local"]:
            click.echo(ColorManager.info("Ramas locales:"))
            for branch in branches["local"]:
                if branch == current_branch:
                    click.echo(ColorManager.success(f"* {branch}"))
                else:
                    click.echo(f"  {branch}")
        else:
            click.echo(ColorManager.warning("No hay ramas locales"))
        
        # Display remote branches
        if branches["remote"]:
            click.echo(ColorManager.info("\nRamas remotas:"))
            for branch in branches["remote"]:
                click.echo(ColorManager.info(f"  {branch} (remote)"))
        else:
            click.echo(ColorManager.warning("\nNo hay ramas remotas"))


@click.command()
def main():
    """List all branches"""
    try:
        # Create and run command
        cmd = GgbCommand()
        return cmd.run()
        
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
