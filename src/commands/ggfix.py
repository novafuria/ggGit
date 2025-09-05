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
        try:
            # Check if AI should be used
            if not message and self._is_ai_configured():
                return self._generate_ai_message(scope, amend)
            
            # Check if message is required
            if not message:
                click.echo(ColorManager.warning("IA no configurada. Usa 'ggconfig set ai.enabled true'"))
                click.echo(ColorManager.info("O proporciona un mensaje manual: ggfix 'mensaje'"))
                return 1
            
            # Execute manual commit
            return self._execute_manual_commit(message, scope, amend)
            
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {e}"))
            return 1
    
    def _get_commit_prefix(self):
        """Get the commit prefix for this command."""
        return "fix"


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
