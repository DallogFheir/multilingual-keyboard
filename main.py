from util.create_dist import create_dist
from util.generate_docs import generate_docs
from util.generate_main_files import generate_common, generate_main, copy_files
from util.sort_hotkeys import sort_hotkeys
from pathlib import Path
import click


def generate_docs_func(without_intro: bool) -> None:
    print("Generating docs...")
    generate_docs(without_intro)
    print(f"README.md file created in directory {Path.cwd()}.")


def sort_hotkeys_func() -> None:
    print("Sorting hotkeys in scripts...")
    sort_hotkeys()
    print(f"Hotkeys in scripts sorted.")


def generate_main_files_func(default: str) -> None:
    print("Generating common.ahk...")
    generate_common()
    print("Generating main.ahk...")
    generate_main(default)
    print("Copying other files...")
    copy_files()
    print("Main files generated.")


def generate_dist_func(dist_archive_name: str) -> None:
    print(f"Generating {dist_archive_name}.zip...")
    try:
        create_dist(dist_archive_name)
    except FileNotFoundError:
        print("dist folder not found.")


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx: click.Context) -> None:
    if ctx.invoked_subcommand is None:
        sort_hotkeys_func()
        generate_main_files_func("default")
        generate_docs_func(False)
        generate_dist_func()


@cli.command("docs", help="generate docs for the AHK project")
@click.option(
    "-w",
    "--without-intro",
    is_flag=True,
    flag_value=True,
    help="Exclude the introduction and acknowledgements from the documentation.",
)
def generate_docs_command(without_intro: bool) -> None:
    generate_docs_func(without_intro)


@cli.command("sort", help="sort hotkeys in AHK scripts alphabetically")
def sort_hotkeys_command() -> None:
    sort_hotkeys_func()


@cli.command("main-files", help="generate main.ahk and common.ahk files")
@click.option(
    "-d",
    "--default",
    default="default",
    show_default=True,
    help="Choose the default keyboard name.",
)
def generate_main_files_command(default: str) -> None:
    generate_main_files_func(default)


@cli.command("dist", help="generate dist ZIP archive")
@click.option(
    "-n",
    "--name",
    default="dist",
    show_default=True,
    help="Choose the dist archive name.",
)
def generate_dist_command(name: str) -> None:
    generate_dist_func(name)


if __name__ == "__main__":
    cli()
