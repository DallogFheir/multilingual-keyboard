from pathlib import Path
import re
from textwrap import dedent
from github_slugger import GithubSlugger
import mdformat

INTRO = """# Multilingual Keyboard

description here

## Hotkeys & hotstrings

"""

SYMBOL = "Symbol"
UNICODE = "Unicode"
DESCRIPTION = "Description"
HOTSTRING_HOTKEY = "Hotstring / hotkey"
UPPERCASE = "Uppercase"

TABLE_HEADERS = [SYMBOL, UNICODE, DESCRIPTION, HOTSTRING_HOTKEY]
TABLE_HEADERS_UPPERCASE = [SYMBOL, UPPERCASE, UNICODE, DESCRIPTION, HOTSTRING_HOTKEY]

COMBINING_DIACRITIC_RANGE = (768, 879)
DIACRITIC_PLACEHOLDER = "◌"


def generate_table(script: str, with_uppercase: bool = False) -> str:
    """Generates a Markdown table for the given AHK script.

    Args:
        script (str): AHK script.
        with_uppercase (bool, optional): Flag indicating the script contains lowercase/uppercase character pairs. Defaults to False.

    Returns:
        str: Generated Markdown table markup.
    """
    rows = {}

    for rule_match in re.findall(
        r"^(.+?)::.*?Send, (.+?)(?: ; ?(.*?))?\nreturn$",
        script,
        re.DOTALL | re.MULTILINE,
    ):
        hotkey, symbol, description = rule_match

        if len(description) == 0:
            hotkey_uppercase = hotkey.replace("+", "", 1)
            if (
                with_uppercase
                and re.match(r"^(!)?\+", hotkey) is not None
                and hotkey_uppercase in rows
            ):
                rows[hotkey_uppercase][UPPERCASE] = symbol

            continue

        # append placeholder to combining diacritics
        symbol_original = symbol
        if COMBINING_DIACRITIC_RANGE[0] <= ord(symbol) <= COMBINING_DIACRITIC_RANGE[1]:
            symbol = DIACRITIC_PLACEHOLDER + symbol

        # parse the hotkey / hotstring
        keys = []
        hotkey_original = hotkey
        if hotkey.startswith("::"):
            hotkey = hotkey.removeprefix("::")
        else:
            for key_symbol, key in [("!", "Alt"), ("+", "Shift")]:
                if hotkey.startswith(key_symbol):
                    keys.append(key)
                    hotkey = hotkey.removeprefix(key_symbol)
        keys.append(hotkey.removeprefix("::"))

        keys_string = " + ".join(
            f"`` {key} ``" if "`" in key else f"`{key}`" for key in keys
        )

        rows[hotkey_original] = {
            SYMBOL: symbol,
            UNICODE: "",
            UPPERCASE: " ",
            DESCRIPTION: description,
            HOTSTRING_HOTKEY: keys_string,
            "symbol_original": symbol_original,
        }

    if len(rows) == 0:
        return ""

    for hotkey in rows.values():
        unicode_symbol = f"{ord(hotkey['symbol_original']):x}".zfill(4)
        unicode_uppercase = f"{ord(hotkey[UPPERCASE]):x}".zfill(4)

        hotkey[UNICODE] = (
            f"`U+{unicode_symbol}`".upper()
            if hotkey[UPPERCASE] == " "
            else f"`U+{unicode_symbol}` / `U+{unicode_uppercase}`".upper()
        )

    headers = TABLE_HEADERS_UPPERCASE if with_uppercase else TABLE_HEADERS
    table = []

    for row in rows.values():
        table.append(f"| {' | '.join(row[header] for header in headers)} |")

    return "\n".join(
        [
            f"| {' | '.join(header for header in headers)} |",
            f"|:{':|:'.join('-' for _ in headers)}:|",
        ]
        + table
    )


def generate_docs() -> None:
    """Generates documentation for the multilingual keyboard project."""
    keyboards_path = Path.cwd() / "subscripts" / "keyboards"
    common_path = Path.cwd() / "subscripts" / "common"

    slugger = GithubSlugger()
    sections = []
    for title, path in (("Keyboards", keyboards_path), ("Common", common_path)):
        subsections = []
        section_slug = slugger.slug(title)

        for file in path.iterdir():
            if file.is_file() and file.suffix == ".ahk":
                with open(file, encoding="utf-8-sig") as f:
                    script_lines = f.read().splitlines()

                if script_lines[0].startswith("; ") and script_lines[1].startswith(
                    "; "
                ):
                    subsection_title = script_lines[0].removeprefix("; ")
                    subsection_description = script_lines[1].removeprefix("; ")
                    uppercase_flag = script_lines[2].strip() == "; UPPERCASE"

                    table = generate_table(
                        "\n".join(script_lines[3 if uppercase_flag else 2 :]),
                        with_uppercase=uppercase_flag,
                    )

                    subsection_template = dedent(
                        """\
                        #### {}
                        
                        {}
                        
                        {}
                        
                        {}"""
                    )
                    if len(table) > 0:
                        subsection_slug = slugger.slug(subsection_title)
                        links = dedent(
                            f"""\
                                ⬆️ [go back to top](#multilingual-keyboard)
                                ⬆️ [go back to Hotkeys & hotstrings](#hotstrings--hotkeys)
                                ⬆️ [go back to {title}](#{section_slug})
                                ⬆️ [go back to {subsection_title}](#{subsection_slug})"""
                        )

                        subsections.append(
                            subsection_template.format(
                                subsection_title, subsection_description, table, links
                            )
                        )

        if len(subsections) > 0:
            subsections_string = "\n\n".join(subsections)
            sections.append(f"""### {title}\n\n{subsections_string}""")

    document = INTRO + "\n\n".join(sections) + "\n"

    with open(Path.cwd() / "README.md", "w", encoding="utf-8") as f:
        f.write(mdformat.text(document, extensions=("gfm",)))
