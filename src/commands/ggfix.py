#!/usr/bin/env python3
"""
ggfix - Commit changes adding the fix prefix to the message

Usage: ggfix [options] <message>
"""

import click
import sys
from core.base_commands.base import BaseCommand
from core.base_commands.commit import CommitCommand
from core.utils.colors import ColorManager


class FixCommand(BaseCommand):
    """Command for creating fix commits."""
    
    def execute(self, message, scope=None, ai=False, amend=False):
        """Execute the fix command."""
        # If no message and AI is enabled, generate automatically
        if not message and ai:
            # TODO: Implement AI message generation
            click.echo(ColorManager.warning("AI functionality not yet implemented"))
            return 1
        
        # Validate input
        if message:
            self.validator.validate_commit_message(message)
        
        # Create commit command
        commit_cmd = CommitCommand("fix")
        
        # Execute commit
        result = commit_cmd.execute(message, scope, amend)
        
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
    """Commit changes adding the fix prefix to the message"""
    try:
        # Create and run command
        cmd = FixCommand()
        return cmd.run(message=message, scope=scope, ai=ai, amend=amend)
        
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
