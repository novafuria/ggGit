#!/usr/bin/env python3
"""
ggb - List all branches or create new branch

Usage: ggb [<branch_name>]
"""

import click
import sys
import re
from core.base_commands.base import BaseCommand
from core.utils.colors import ColorManager


class GgbCommand(BaseCommand):
    """Command for listing all branches or creating new branches."""
    
    def execute(self, branch_name=None):
        """Execute the ggb command."""
        try:
            if not self.git.is_git_repository():
                click.echo(ColorManager.error("Not a git repository"))
                return 1
            
            if branch_name:
                return self._create_branch(branch_name)
            else:
                return self._list_branches()
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {str(e)}"))
            return 1
    
    def _list_branches(self):
        """List all branches."""
        branches = self.git.get_all_branches()
        current_branch = self.git.get_current_branch()
        
        self._display_branches(branches, current_branch)
        return 0
    
    def _create_branch(self, branch_name):
        """Create branch with name conversion."""
        clean_name = self._convert_branch_name(branch_name)
        
        if not self._validate_branch_name(clean_name):
            click.echo(ColorManager.error("Nombre de rama inválido"))
            return 1
        
        if self._branch_exists(clean_name):
            click.echo(ColorManager.warning(f"Rama {clean_name} ya existe, cambiando a ella"))
            result = self.git.switch_branch(clean_name)
        else:
            result = self.git.create_branch(clean_name)
        
        if result:
            click.echo(ColorManager.success(f"Rama {clean_name} creada/cambiada exitosamente"))
            return 0
        else:
            click.echo(ColorManager.error("Error al crear/cambiar rama"))
            return 1
    
    def _convert_branch_name(self, name):
        """Convert branch name (spaces to hyphens)."""
        if not name:
            return ""
        
        # Convert to lowercase
        name = name.lower()
        
        # Replace spaces with hyphens
        name = name.replace(' ', '-')
        
        # Remove multiple consecutive hyphens
        name = re.sub(r'-+', '-', name)
        
        # Remove leading/trailing hyphens
        name = name.strip('-')
        
        return name
    
    def _validate_branch_name(self, name):
        """Validate branch name."""
        if not name or not name.strip():
            return False
        if len(name) > 255:
            return False
        if name.startswith('.') or name.endswith('.'):
            return False
        if '..' in name or '~' in name or '^' in name:
            return False
        return True
    
    def _branch_exists(self, branch_name):
        """Check if branch exists."""
        try:
            branches = self.git.get_branches()
            return branch_name in branches
        except:
            return False
    
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
@click.argument('branch_name', required=False)
def main(branch_name):
    """List all branches or create new branch"""
    try:
        # Create and run command
        cmd = GgbCommand()
        return cmd.run(branch_name=branch_name)
        
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
