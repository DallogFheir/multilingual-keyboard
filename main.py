from util.generate_docs import generate_docs
from util.sort_hotkeys import sort_hotkeys
from pathlib import Path
import click


@click.group()
def cli():
    pass


@cli.command("docs", help="generate docs for the AHK project")
def generate_docs_command():
    click.echo("Generating docs...")
    generate_docs()
    click.echo(f"README.md file created in directory {Path.cwd()}.")


@cli.command("sort", help="sort hotkeys in AHK scripts alphabetically")
def sort_hotkeys_command():
    click.echo("Sorting hotkeys in scripts...")
    sort_hotkeys()
    click.echo(f"Hotkeys in scripts sorted.")


if __name__ == "__main__":
    cli()
