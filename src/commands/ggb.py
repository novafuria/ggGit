#!/usr/bin/env python3
"""
ggb - List all branches or create new branch

Usage: ggb [<branch_name>]
"""

import click
import sys
import re
import subprocess
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
                return self._show_branch_options()  # Nueva funcionalidad interactiva
                
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
        
        try:
            if self._branch_exists(clean_name):
                click.echo(ColorManager.warning(f"Rama {clean_name} ya existe, cambiando a ella"))
                try:
                    result = self.git.switch_branch(clean_name)
                    if result:
                        click.echo(ColorManager.success(f"Cambiado a rama '{clean_name}'"))
                        return 0
                    else:
                        click.echo(ColorManager.error(f"Error al cambiar a rama '{clean_name}'"))
                        return 1
                except subprocess.CalledProcessError as e:
                    error_msg = e.stderr if e.stderr else str(e)
                    if "would be overwritten" in error_msg or "local changes" in error_msg:
                        click.echo(ColorManager.warning("Tienes cambios sin commitear que serían sobrescritos"))
                        click.echo(ColorManager.info("Opciones:"))
                        click.echo("  1. Hacer commit de los cambios: git add . && git commit -m 'mensaje'")
                        click.echo("  2. Guardar cambios temporalmente: git stash")
                        click.echo("  3. Descartar cambios: git reset --hard HEAD")
                        return 1
                    else:
                        click.echo(ColorManager.error(f"Error al cambiar a rama '{clean_name}': {error_msg}"))
                        return 1
            else:
                # Create new branch
                try:
                    result = self.git.create_branch(clean_name)
                    if result:
                        click.echo(ColorManager.success(f"Rama '{clean_name}' creada exitosamente"))
                        return 0
                    else:
                        click.echo(ColorManager.error(f"Error al crear rama '{clean_name}'"))
                        return 1
                except subprocess.CalledProcessError as e:
                    click.echo(ColorManager.error(f"Error al crear rama '{clean_name}': {e.stderr}"))
                    return 1
                    
        except ValueError as e:
            click.echo(ColorManager.error(f"Error de validación: {str(e)}"))
            return 1
        except RuntimeError as e:
            click.echo(ColorManager.error(f"Error de Git: {str(e)}"))
            return 1
        except Exception as e:
            click.echo(ColorManager.error(f"Error inesperado: {str(e)}"))
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
    
    def _show_branch_options(self):
        """Show interactive branch options."""
        try:
            click.echo(ColorManager.info("Opciones de ramas:"))
            click.echo("  1. Listar todas las ramas")
            click.echo("  2. Crear nueva rama")
            click.echo("  3. Cambiar a rama existente")
            
            while True:
                try:
                    choice = input("\nSelecciona opción (número): ").strip()
                    
                    if not choice:
                        click.echo(ColorManager.error("Selección requerida"))
                        continue
                    
                    choice_num = int(choice)
                    if choice_num == 1:
                        return self._list_branches()
                    elif choice_num == 2:
                        branch_name = input("Ingresa nombre de la nueva rama: ").strip()
                        if branch_name:
                            return self._create_branch(branch_name)
                        else:
                            click.echo(ColorManager.error("Nombre de rama requerido"))
                            continue
                    elif choice_num == 3:
                        return self._switch_to_branch()
                    else:
                        click.echo(ColorManager.error("Selección inválida. Ingresa 1, 2 o 3"))
                        
                except ValueError:
                    click.echo(ColorManager.error("Selección inválida. Ingresa un número válido"))
                except KeyboardInterrupt:
                    click.echo(ColorManager.warning("\nOperación cancelada"))
                    return 1
                    
        except Exception as e:
            click.echo(ColorManager.error(f"Error al mostrar opciones: {str(e)}"))
            return 1
    
    def _switch_to_branch(self):
        """Switch to an existing branch interactively."""
        try:
            branches = self.git.get_branches()
            
            if not branches:
                click.echo(ColorManager.warning("No hay ramas disponibles"))
                return 0
            
            # Mostrar lista numerada
            click.echo(ColorManager.info("Ramas disponibles:"))
            for i, branch in enumerate(branches, 1):
                current_branch = self.git.get_current_branch()
                if branch == current_branch:
                    click.echo(f"  {i}. {branch} (actual)")
                else:
                    click.echo(f"  {i}. {branch}")
            
            # Obtener selección del usuario
            while True:
                try:
                    choice = input("\nSelecciona rama (número): ").strip()
                    
                    if not choice:
                        click.echo(ColorManager.error("Selección requerida"))
                        continue
                    
                    choice_num = int(choice)
                    if 1 <= choice_num <= len(branches):
                        selected_branch = branches[choice_num - 1]
                        result = self.git.switch_branch(selected_branch)
                        
                        if result:
                            click.echo(ColorManager.success(f"Cambiado a rama {selected_branch}"))
                            return 0
                        else:
                            click.echo(ColorManager.error(f"Error al cambiar a rama {selected_branch}"))
                            return 1
                    else:
                        click.echo(ColorManager.error(f"Selección inválida. Ingresa un número entre 1 y {len(branches)}"))
                        
                except ValueError:
                    click.echo(ColorManager.error("Selección inválida. Ingresa un número válido"))
                except KeyboardInterrupt:
                    click.echo(ColorManager.warning("\nOperación cancelada"))
                    return 1
                    
        except Exception as e:
            click.echo(ColorManager.error(f"Error al cambiar rama: {str(e)}"))
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
