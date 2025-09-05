#!/usr/bin/env python3
"""
ggrefactor - Commit changes adding the refactor prefix to the message

Usage: ggrefactor [options] <message>
"""

import click
import sys
from core.base_commands.base import BaseCommand
from core.base_commands.commit import CommitCommand
from core.utils.colors import ColorManager


class RefactorCommand(BaseCommand):
    """Command for creating refactor commits."""
    
    def execute(self, message, scope=None, ai=False, amend=False):
        """Execute the refactor command."""
        # If no message and AI is enabled, generate automatically
        if not message and ai:
            click.echo(ColorManager.warning("AI functionality not yet implemented"))
            return 1
        
        # Create commit command
        commit_cmd = CommitCommand("refactor")
        
        # Execute commit (validation included in CommitCommand)
        result = commit_cmd.execute(message, scope, amend)
        
        # Handle result
        if result == 0:
            click.echo(ColorManager.success("Commit realizado exitosamente"))
        else:
            click.echo(ColorManager.error("Error al realizar commit"))
            return result
        
        return result


@click.command()
@click.option('--scope', '-s', help='Scope del commit')
@click.option('--ai', is_flag=True, help='Usar IA para generar mensaje')
@click.option('--amend', '-a', is_flag=True, help='Amend the last commit')
@click.argument('message', required=False)
def main(scope, ai, amend, message):
    """Commit changes adding the refactor prefix to the message"""
    try:
        # Create and run command
        cmd = RefactorCommand()
        return cmd.run(message=message, scope=scope, ai=ai, amend=amend)
        
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
