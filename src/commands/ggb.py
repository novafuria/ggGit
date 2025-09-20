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
                        # Switch to the new branch after creating it
                        try:
                            switch_result = self.git.switch_branch(clean_name)
                            if switch_result:
                                click.echo(ColorManager.success(f"Rama '{clean_name}' creada y cambiado a ella"))
                                return 0
                            else:
                                click.echo(ColorManager.warning(f"Rama '{clean_name}' creada pero no se pudo cambiar a ella"))
                                click.echo(ColorManager.info(f"Puedes cambiar manualmente con: git checkout {clean_name}"))
                                return 0
                        except subprocess.CalledProcessError as e:
                            error_msg = e.stderr if e.stderr else str(e)
                            if "would be overwritten" in error_msg or "local changes" in error_msg:
                                click.echo(ColorManager.warning(f"Rama '{clean_name}' creada pero no se pudo cambiar"))
                                click.echo(ColorManager.warning("Tienes cambios que serían sobrescritos"))
                                click.echo(ColorManager.info("Opciones:"))
                                click.echo("  1. Hacer commit de los cambios: git add . && git commit -m 'mensaje'")
                                click.echo("  2. Guardar cambios temporalmente: git stash")
                                click.echo("  3. Descartar cambios: git reset --hard HEAD")
                                click.echo(f"  4. Cambiar manualmente después: git checkout {clean_name}")
                                return 0
                            else:
                                click.echo(ColorManager.error(f"Error al cambiar a rama '{clean_name}': {error_msg}"))
                                return 1
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
    
    def _has_uncommitted_changes(self):
        """Check if there are uncommitted changes."""
        try:
            # Check for unstaged files (modified tracked files)
            unstaged_files = self.git.get_unstaged_files()
            
            # Check for untracked files
            result = subprocess.run(['git', 'ls-files', '--others', '--exclude-standard'], 
                                  capture_output=True, text=True, timeout=10)
            untracked_files = [line.strip() for line in result.stdout.splitlines() if line.strip()] if result.returncode == 0 else []
            
            return len(unstaged_files) > 0 or len(untracked_files) > 0
        except:
            return False
    
    def _handle_uncommitted_changes(self):
        """Handle uncommitted changes before creating/switching branches."""
        try:
            click.echo(ColorManager.warning("Tienes cambios sin commitear"))
            click.echo(ColorManager.info("¿Qué quieres hacer con estos cambios?"))
            click.echo("  1. Conservarlos (stash)")
            click.echo("  2. Descartarlos")
            click.echo("  3. Cancelar operación")
            
            while True:
                try:
                    choice = input("\nSelecciona opción (1-3): ").strip()
                    
                    if choice == "1":
                        # Stash changes (including untracked files)
                        result = subprocess.run(['git', 'stash', '--include-untracked'], capture_output=True, text=True)
                        if result.returncode == 0:
                            click.echo(ColorManager.success("Cambios guardados en stash"))
                            return True
                        else:
                            click.echo(ColorManager.error(f"Error al guardar cambios: {result.stderr}"))
                            return False
                    
                    elif choice == "2":
                        # Discard changes (including untracked files)
                        result1 = subprocess.run(['git', 'reset', '--hard', 'HEAD'], capture_output=True, text=True)
                        result2 = subprocess.run(['git', 'clean', '-fd'], capture_output=True, text=True)
                        if result1.returncode == 0 and result2.returncode == 0:
                            click.echo(ColorManager.success("Cambios descartados"))
                            return True
                        else:
                            click.echo(ColorManager.error(f"Error al descartar cambios: {result1.stderr or result2.stderr}"))
                            return False
                    
                    elif choice == "3":
                        # Cancel operation
                        click.echo(ColorManager.info("Operación cancelada"))
                        return False
                    
                    else:
                        click.echo(ColorManager.error("Selección inválida. Ingresa 1, 2 o 3"))
                        
                except KeyboardInterrupt:
                    click.echo(ColorManager.warning("\nOperación cancelada"))
                    return False
                except Exception as e:
                    click.echo(ColorManager.error(f"Error: {str(e)}"))
                    return False
                    
        except Exception as e:
            click.echo(ColorManager.error(f"Error al manejar cambios: {str(e)}"))
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
