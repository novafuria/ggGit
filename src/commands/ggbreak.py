#!/usr/bin/env python3
"""
ggbreak - Commit changes adding the break prefix to the message

Usage: ggbreak [options] -s <scope> <message>
"""

import click
import sys
from core.base_commands.base import BaseCommand
from core.utils.colors import ColorManager


class GgbreakCommand(BaseCommand):
    """Command for committing changes with break prefix."""
    
    def execute(self, message, scope=None, amend=False):
        """Execute the ggbreak command."""
        try:
            if not message or not message.strip():
                click.echo(ColorManager.error("Message is required"))
                return 1
            
            if not self.git.is_git_repository():
                click.echo(ColorManager.error("Not a git repository"))
                return 1
            
            # Build commit message with break prefix
            prefix = "break"
            if scope:
                prefix = f"{prefix}({scope})"
            
            commit_message = f"{prefix}: {message}"
            
            # Check if there are staged changes
            staged_files = self.git.get_staged_files()
            if not staged_files:
                # Stage all changes if nothing is staged
                self.git.stage_all_changes()
            
            # Commit with the break message
            result = self.git.commit(commit_message)
            
            if result:
                click.echo(ColorManager.success("Commit con break realizado exitosamente"))
                return 0
            else:
                click.echo(ColorManager.error("Error al realizar commit con break"))
                return 1
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {str(e)}"))
            return 1


@click.command()
@click.option('--amend', '-a', is_flag=True, help='Amend the last commit with the new message')
@click.option('--scope', '-s', help='Add a scope to the prefix (e.g. break(scope): message)')
@click.argument('message', required=True)
def main(message, scope, amend):
    """Commit changes adding the break prefix to the message"""
    try:
        # Create and run command
        cmd = GgbreakCommand()
        return cmd.run(message=message, scope=scope, amend=amend)
        
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())