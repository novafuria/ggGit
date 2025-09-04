#!/usr/bin/env python3
"""
ggconfig - Configuration management command for ggGit.

This command allows users to view, set, and manage ggGit configurations
through a command-line interface.
"""

import sys
import click
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.base_commands.config import ConfigCommand
from core.utils.colors import ColorManager


@click.command()
@click.argument('action', type=click.Choice(['get', 'set', 'list', 'reset']))
@click.argument('key', required=False)
@click.argument('value', required=False)
@click.option('--level', '-l', 
              type=click.Choice(['repo', 'module', 'user', 'default']), 
              default='user',
              help='Configuration level to operate on')
@click.option('--help-action', is_flag=True, help='Show help for specific action')
def main(action, key, value, level, help_action):
    """
    ggconfig - Manage ggGit configuration
    
    ACTIONS:
        get KEY          Get configuration value for KEY
        set KEY VALUE    Set configuration value for KEY to VALUE
        list             List all configuration values
        reset [KEY]      Reset configuration (optionally for specific KEY)
    
    EXAMPLES:
        ggconfig get ui.colors.success
        ggconfig set ui.colors.success bright_green --level user
        ggconfig list
        ggconfig reset user
    """
    if help_action:
        show_action_help(action)
        return
    
    try:
        # Create ConfigCommand instance
        config_cmd = ConfigCommand()
        
        # Execute the action
        result = config_cmd.execute(action, key, value, level)
        
        # Exit with result code
        sys.exit(result)
        
    except Exception as e:
        ColorManager.error(f"Error: {e}")
        sys.exit(1)


def show_action_help(action):
    """Show help for specific action."""
    help_text = {
        'get': """
GET - Retrieve configuration value

Usage: ggconfig get KEY [--level LEVEL]

Examples:
    ggconfig get ui.colors.success
    ggconfig get git.default_branch --level repo
    ggconfig get ai.enabled --level user
        """,
        'set': """
SET - Set configuration value

Usage: ggconfig set KEY VALUE [--level LEVEL]

Examples:
    ggconfig set ui.colors.success bright_green
    ggconfig set git.default_branch main --level repo
    ggconfig set ai.enabled true --level user
        """,
        'list': """
LIST - List all configuration values

Usage: ggconfig list [--level LEVEL]

Examples:
    ggconfig list
    ggconfig list --level user
    ggconfig list --level repo
        """,
        'reset': """
RESET - Reset configuration

Usage: ggconfig reset [KEY] [--level LEVEL]

Examples:
    ggconfig reset user
    ggconfig reset repo
    ggconfig reset ui.colors.success --level user
        """
    }
    
    if action in help_text:
        print(help_text[action])
    else:
        print(f"No help available for action: {action}")


if __name__ == '__main__':
    main()
