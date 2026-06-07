#!/usr/bin/env python3
"""
ggpl - Pull from remote repository

Usage: ggpl [<remote>] [<branch>]
"""

import sys

import click

from core.base_commands.base import BaseCommand
from core.utils.colors import ColorManager


class GgplCommand(BaseCommand):
    """Command for git pull operations."""

    def execute(
        self,
        remote=None,
        branch=None,
        all_remotes=True,
        tags=True,
        force=True,
        prune=True,
    ):
        """Execute the ggpl command."""
        try:
            result = self.git.pull(
                remote=remote,
                branch=branch,
                all_remotes=all_remotes,
                tags=tags,
                force=force,
                prune=prune,
            )

            if result:
                click.echo(ColorManager.success("Pull ejecutado exitosamente"))
                return 0
            else:
                click.echo(ColorManager.error("Error al ejecutar pull"))
                return 1

        except Exception as e:
            click.echo(ColorManager.error(f"Error: {str(e)}"))
            return 1


@click.command()
@click.option(
    "--all-remotes/--no-all",
    "all_remotes",
    default=True,
    help="Pull from all remotes",
)
@click.option(
    "--tags/--no-tags", "tags", default=True, help="Fetch all tags from remote"
)
@click.option(
    "--force/--no-force",
    "force",
    default=True,
    help="Force update of local tags/refs",
)
@click.option(
    "--prune/--no-prune",
    "prune",
    default=True,
    help="Prune remote-tracking tags/refs that no longer exist",
)
@click.argument("remote", required=False)
@click.argument("branch", required=False)
def main(all_remotes, tags, force, prune, remote, branch):
    """Pull from remote repository"""
    try:
        # Create and run command
        cmd = GgplCommand()
        return cmd.run(
            remote=remote,
            branch=branch,
            all_remotes=all_remotes,
            tags=tags,
            force=force,
            prune=prune,
        )

    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
