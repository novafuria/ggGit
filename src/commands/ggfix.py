#!/usr/bin/env python3
"""
ggfix - Commit changes adding the fix prefix to the message

Usage: ggfix [options] <message>
"""

import click
import sys
from core.config import ConfigManager
from core.git import GitInterface
from core.validation import ArgumentValidator
from core.base_commands.commit import CommitCommand


@click.command()
@click.option('--scope', '-s', help='Scope del commit')
@click.option('--ai', is_flag=True, help='Usar IA para generar mensaje')
@click.option('--amend', '-a', is_flag=True, help='Amend the last commit')
@click.argument('message', required=False)
def main(scope, ai, amend, message):
    """Commit changes adding the fix prefix to the message"""
    try:
        # Initialize components
        config = ConfigManager()
        git = GitInterface()
        validator = ArgumentValidator()
        
        # If no message and AI is enabled, generate automatically
        if not message and ai:
            # TODO: Implement AI message generation
            click.echo(click.style("AI functionality not yet implemented", fg="yellow"))
            return 1
        
        # Validate input
        if message:
            validator.validate_commit_message(message)
        
        # Create commit command
        commit_cmd = CommitCommand("fix")
        
        # Execute commit
        result = commit_cmd.execute(message, scope, amend)
        
        if result == 0:
            click.echo(click.style("✅ Commit realizado exitosamente", fg="green"))
        else:
            click.echo(click.style("❌ Error al realizar commit", fg="red"))
            return result
        
    except Exception as e:
        click.echo(click.style(f"❌ Error: {str(e)}", fg="red"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
