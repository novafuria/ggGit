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
                return self._show_merge_options()  # Nueva funcionalidad interactiva
                
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
    
    def _show_merge_options(self):
        """Show interactive list of branches for merge."""
        try:
            branches = self.git.get_mergeable_branches()
            
            if not branches:
                click.echo(ColorManager.warning("No hay ramas disponibles para merge"))
                return 0
            
            # Mostrar lista numerada
            click.echo(ColorManager.info("Ramas disponibles para merge:"))
            for i, branch in enumerate(branches, 1):
                click.echo(f"  {i}. {branch}")
            
            # Obtener selección del usuario
            while True:
                try:
                    choice = input("\nSelecciona rama para merge (número): ").strip()
                    
                    if not choice:
                        click.echo(ColorManager.error("Selección requerida"))
                        continue
                    
                    choice_num = int(choice)
                    if 1 <= choice_num <= len(branches):
                        selected_branch = branches[choice_num - 1]
                        return self._merge_branch(selected_branch)
                    else:
                        click.echo(ColorManager.error(f"Selección inválida. Ingresa un número entre 1 y {len(branches)}"))
                        
                except ValueError:
                    click.echo(ColorManager.error("Selección inválida. Ingresa un número válido"))
                except KeyboardInterrupt:
                    click.echo(ColorManager.warning("\nOperación cancelada"))
                    return 1
                    
        except Exception as e:
            click.echo(ColorManager.error(f"Error al mostrar opciones: {str(e)}"))
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
