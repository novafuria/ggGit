#!/usr/bin/env python3
"""
ggbuild - Commit changes adding the build prefix to the message

Usage: ggbuild [options] <message>
"""

import click
import sys
from src.core.base_commands.base import BaseCommand
from src.core.base_commands.commit import CommitCommand
from src.core.utils.colors import ColorManager


class BuildCommand(BaseCommand):
    """Command for creating build system commits."""
    
    def execute(self, message, scope=None, ai=False, amend=False):
        """Execute the build command."""
        # If no message and AI is enabled, generate automatically
        if not message and ai:
            click.echo(ColorManager.warning("AI functionality not yet implemented"))
            return 1
        
        # Create commit command
        commit_cmd = CommitCommand("build")
        
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
    """Commit changes adding the build prefix to the message"""
    try:
        # Create and run command
        cmd = BuildCommand()
        return cmd.run(message=message, scope=scope, ai=ai, amend=amend)
        
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
