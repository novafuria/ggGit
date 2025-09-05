#!/usr/bin/env python3
"""
ggmerge - Merge branches without fast-forward

Usage: ggmerge [<options>] [<branch>]
"""

import click
import sys
from core.base_commands.base import BaseCommand
from core.utils.colors import ColorManager


class GgmergeCommand(BaseCommand):
    """Command for merging branches without fast-forward."""
    
    def execute(self, branch=None, abort=False, continue_merge=False):
        """Execute the ggmerge command."""
        try:
            if not self.git.is_git_repository():
                click.echo(ColorManager.error("Not a git repository"))
                return 1
            
            if abort:
                return self._abort_merge()
            elif continue_merge:
                return self._continue_merge()
            elif branch:
                return self._merge_branch(branch)
            else:
                click.echo(ColorManager.error("Debe especificar una rama para hacer merge"))
                return 1
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {str(e)}"))
            return 1
    
    def _merge_branch(self, branch_name):
        """Merge specified branch."""
        try:
            result = self.git.merge_branch(branch_name)
            
            if result:
                click.echo(ColorManager.success(f"Merge de {branch_name} completado exitosamente"))
                return 0
            else:
                click.echo(ColorManager.error(f"Error al hacer merge de {branch_name}"))
                return 1
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error al hacer merge: {str(e)}"))
            return 1
    
    def _abort_merge(self):
        """Abort current merge."""
        try:
            result = self.git.merge_abort()
            
            if result:
                click.echo(ColorManager.success("Merge abortado exitosamente"))
                return 0
            else:
                click.echo(ColorManager.error("Error al abortar merge"))
                return 1
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error al abortar merge: {str(e)}"))
            return 1
    
    def _continue_merge(self):
        """Continue current merge."""
        try:
            result = self.git.merge_continue()
            
            if result:
                click.echo(ColorManager.success("Merge continuado exitosamente"))
                return 0
            else:
                click.echo(ColorManager.error("Error al continuar merge"))
                return 1
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error al continuar merge: {str(e)}"))
            return 1


@click.command()
@click.option('--abort', '-a', is_flag=True, help='Abort the current conflict resolution process')
@click.option('--continue', '-c', 'continue_merge', is_flag=True, help='Continue the current conflict resolution process')
@click.argument('branch', required=False)
def main(branch, abort, continue_merge):
    """Merge branches without fast-forward"""
    try:
        # Create and run command
        cmd = GgmergeCommand()
        return cmd.run(branch=branch, abort=abort, continue_merge=continue_merge)
        
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
