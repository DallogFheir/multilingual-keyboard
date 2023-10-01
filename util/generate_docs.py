from pathlib import Path
import re
from textwrap import dedent
from github_slugger import GithubSlugger
import mdformat
from .templates.intro import INTRO
from .common import KEYBOARDS_PATH, SCRIPTS_PATH, HOTKEY_REGEX

SYMBOL = "Symbol"
UNICODE = "Unicode"
DESCRIPTION = "Description"
HOTSTRING_HOTKEY = "Hotstring / hotkey"
UPPERCASE = "Uppercase"

TABLE_HEADERS = [SYMBOL, UNICODE, DESCRIPTION, HOTSTRING_HOTKEY]
TABLE_HEADERS_UPPERCASE = [SYMBOL, UPPERCASE, UNICODE, DESCRIPTION, HOTSTRING_HOTKEY]

COMBINING_DIACRITIC_RANGE = (768, 879)
DIACRITIC_PLACEHOLDER = "◌"


def parse_hotkey(hotkey: str) -> str:
    keys = []
    if hotkey.startswith("::"):
        hotkey = hotkey.removeprefix("::")
    else:
        for key_symbol, key in [("!", "Alt"), ("+", "Shift")]:
            if hotkey.startswith(key_symbol):
                keys.append(key)
                hotkey = hotkey.removeprefix(key_symbol)
    keys.append(hotkey.removeprefix("::"))

    return " + ".join(f"`` {key} ``" if "`" in key else f"`{key}`" for key in keys)


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
        HOTKEY_REGEX,
        script,
        re.DOTALL | re.MULTILINE,
    ):
        hotkey, symbol, description = rule_match

        if len(description) == 0:
            hotkey_uppercase = hotkey.replace("+", "", 1)
            hotstring_uppercase = hotkey.lower()
            if (
                with_uppercase
                and re.match(r"^(!)?\+", hotkey) is not None
                and hotkey_uppercase in rows
            ):
                rows[hotkey_uppercase][UPPERCASE] = symbol
            elif with_uppercase and hotstring_uppercase in rows:
                rows[hotstring_uppercase][UPPERCASE] = symbol
                rows[hotstring_uppercase][
                    HOTSTRING_HOTKEY
                ] += f" / {parse_hotkey(hotkey)}"

            continue

        # append placeholder to combining diacritics
        symbol_original = symbol
        if COMBINING_DIACRITIC_RANGE[0] <= ord(symbol) <= COMBINING_DIACRITIC_RANGE[1]:
            symbol = DIACRITIC_PLACEHOLDER + symbol

        hotkey_original = hotkey
        keys_string = parse_hotkey(hotkey)

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
        unicode_symbol = "U+" + f"{ord(hotkey['symbol_original']):x}".zfill(4).upper()
        unicode_symbol_link = f"https://codepoints.net/{unicode_symbol}"
        unicode_uppercase = "U+" + f"{ord(hotkey[UPPERCASE]):x}".zfill(4).upper()
        unicode_uppercase_link = f"https://codepoints.net/{unicode_uppercase}"

        hotkey[UNICODE] = (
            f"[{unicode_symbol}]({unicode_symbol_link})"
            if hotkey[UPPERCASE] == " "
            else f"[{unicode_symbol}]({unicode_symbol_link}) / [{unicode_uppercase}]({unicode_uppercase_link})"
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


def parse_files(title: str, path: Path, slugger: GithubSlugger) -> str | None:
    subsections = []
    section_slug = slugger.slug(title)

    order = {}
    for file in path.iterdir():
        if file.is_file() and file.suffix == ".ahk":
            with open(file, encoding="utf-8-sig") as f:
                script_lines = f.read().splitlines()

            if script_lines[0].startswith("; ") and script_lines[1].startswith("; "):
                subsection_title = script_lines[0].removeprefix("; ")
                subsection_description = script_lines[1].removeprefix("; ")

                hotkey = None
                start_idx = 2
                if title == "Keyboards":
                    hotkey = script_lines[2].removeprefix("; ")
                    start_idx += 1
                uppercase_flag = script_lines[start_idx].strip() == "; UPPERCASE"

                table = generate_table(
                    "\n".join(
                        script_lines[start_idx + 1 if uppercase_flag else start_idx :]
                    ),
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
                        f"⬆️ go back to [top](#multilingual-keyboard) | [Hotkeys & hotstrings](#hotkeys--hotstrings) | [{title}](#{section_slug}) | [{subsection_title}](#{subsection_slug}) ⬆️"
                    )

                    if hotkey is not None:
                        subsection_description = (
                            f"**Hotkey to switch to keyboard:** {parse_hotkey(hotkey)}\n\n"
                            + subsection_description
                        )

                    formatted_subsection = subsection_template.format(
                        subsection_title, subsection_description, table, links
                    )

                    order[formatted_subsection] = (
                        hotkey if hotkey is not None else file.stem
                    )

                    subsections.append(formatted_subsection)

    subsections.sort(key=lambda k: order[k])

    if len(subsections) > 0:
        subsections_string = "\n\n".join(subsections)
        return f"""### {title}\n\n{subsections_string}"""


def generate_docs(without_intro: bool) -> None:
    """Generates documentation for the multilingual keyboard project."""
    slugger = GithubSlugger()
    sections = []
    for title, path in (("Keyboards", KEYBOARDS_PATH), ("Common", SCRIPTS_PATH)):
        res = parse_files(title, path, slugger)
        if res is not None:
            sections.append(res)

    document = (
        "# Multilingual Keyboard\n\n"
        + ("" if without_intro else INTRO)
        + ("" if len(sections) == 0 else "## Hotkeys & hotstrings\n\n")
        + "\n\n".join(sections)
        + "\n"
    )

    with open(Path.cwd() / "README.md", "w", encoding="utf-8") as f:
        f.write(mdformat.text(document, extensions=("gfm",)))
