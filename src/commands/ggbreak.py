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
    
    def execute(self, message, scope=None, ai=False, amend=False):
        """Execute the ggbreak command."""
        try:
            # Check if AI should be used
            if not message and self._is_ai_configured():
                return self._generate_ai_message(scope, amend)
            
            # Check if message is required
            if not message:
                click.echo(ColorManager.warning("IA no configurada. Usa 'ggconfig set ai.enabled true'"))
                click.echo(ColorManager.info("O proporciona un mensaje manual: ggbreak 'mensaje'"))
                return 1
            
            # Execute manual commit
            return self._execute_manual_commit(message, scope, amend)
            
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {e}"))
            return 1
    
    def _get_commit_prefix(self):
        """Get the commit prefix for this command."""
        return "break"


@click.command()
@click.option('--amend', '-a', is_flag=True, help='Amend the last commit with the new message')
@click.option('--scope', '-s', help='Add a scope to the prefix (e.g. break(scope): message)')
@click.option('--ai', is_flag=True, help='Usar IA para generar mensaje')
@click.argument('message', required=False)
def main(message, scope, amend, ai):
    """Commit changes adding the break prefix to the message"""
    try:
        # Create and run command
        cmd = GgbreakCommand()
        return cmd.run(message=message, scope=scope, ai=ai, amend=amend)
        
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())