from collections import namedtuple
from pathlib import Path
import re
from textwrap import dedent

INTRO = """# Multilingual Keyboard

description here

# Hotkeys & hotstrings

"""

TABLE_HEADER = "| Symbol{} | Description{} | Hotstring / hotkey{} |"
TABLE_SEPARATOR = "| {} | {} | {} |"

TableRow = namedtuple("TableRow", ["symbol", "description", "hotkey"])


def generate_table(script_lines):
    rows = []
    max_length_symbol = 6
    max_length_description = 11
    max_length_hotkey = 18
    for i in range(0, len(script_lines), 3):
        hotkey = script_lines[i]
        symbol_with_description = script_lines[i + 1]

        # parse the returned symbol and description
        rematch = re.fullmatch(r"\s*Send, (.+?)(?: ; (.+))?", symbol_with_description)
        if rematch is None:
            continue

        symbol, description = rematch.groups()
        if description is None:
            continue

        # parse the hotkey / hotstring
        keys = []
        if hotkey.startswith("::"):
            hotkey = hotkey.removeprefix("::")
        else:
            for key_symbol, key in [("!", "Alt"), ("+", "Shift")]:
                if hotkey.startswith(key_symbol):
                    keys.append(key)
                    hotkey = hotkey.removeprefix(key_symbol)

        keys.append(hotkey.removesuffix("::"))
        keys_string = " + ".join(f"`{key}`" for key in keys)

        if len(symbol) > max_length_symbol:
            max_length_symbol = len(symbol)
        if len(description) > max_length_description:
            max_length_description = len(description)
        if len(keys_string) > max_length_hotkey:
            max_length_hotkey = len(keys_string)

        rows.append(TableRow(symbol, description, keys_string))

    if len(rows) == 0:
        return ""

    space_fillers = (
        " " * (max_length_symbol - 6),
        " " * (max_length_description - 11),
        " " * (max_length_hotkey - 18),
    )
    hyphen_fillers = (
        "-" * max_length_symbol,
        "-" * max_length_description,
        "-" * max_length_hotkey,
    )
    table = [
        TABLE_HEADER.format(*space_fillers),
        TABLE_SEPARATOR.format(*hyphen_fillers),
    ]

    for row in rows:
        table.append(
            f"| {row.symbol}{' ' * (max_length_symbol - len(row.symbol))} "
            f"| {row.description}{' ' * (max_length_description - len(row.description))} "
            f"| {row.hotkey}{' ' * (max_length_hotkey - len(row.hotkey))} |"
        )

    return "\n".join(table)


def generate_docs():
    keyboards_path = Path.cwd() / "subscripts" / "language_scripts"
    common_path = Path.cwd() / "subscripts" / "common"

    sections = []
    for title, path in (("Keyboards", keyboards_path), ("Common", common_path)):
        subsections = []

        for file in path.iterdir():
            if file.is_file() and file.suffix == ".ahk":
                with open(file, encoding="utf-8-sig") as f:
                    script_lines = f.read().splitlines()

                if script_lines[0].startswith("; ") and script_lines[1].startswith(
                    "; "
                ):
                    subsection_title = script_lines[0].removeprefix("; ")
                    subsection_description = script_lines[1].removeprefix("; ")
                    table = generate_table(script_lines[2:])

                    subsection_template = dedent(
                        """\
                        #### {}
                        
                        {}
                        
                        {}"""
                    )
                    subsections.append(
                        subsection_template.format(
                            subsection_title, subsection_description, table
                        )
                    )

        if len(subsections) > 0:
            subsections_string = "\n\n".join(subsections)
            sections.append(f"""### {title}\n\n{subsections_string}""")

    document = INTRO + "\n\n".join(sections)

    with open(Path.cwd() / "README.md", "w", encoding="utf-8") as f:
        f.write(document)
