from pathlib import Path, PureWindowsPath
import re
import shutil
from textwrap import dedent
from .common import SRC_PATH, ICONS_PATH, KEYBOARDS_PATH, DIST_PATH, HOTKEY_REGEX


def generate_common():
    """Generates common.ahk file."""

    if not DIST_PATH.exists():
        DIST_PATH.mkdir()

    scripts_dir = Path.cwd() / "src" / "scripts"
    hotstrings = []

    for file in scripts_dir.iterdir():
        with open(file, encoding="utf-8", newline="\n") as f:
            script = f.read()
            file_hotstrings = re.findall(
                HOTKEY_REGEX,
                script,
                re.DOTALL | re.MULTILINE,
            )

            for file_hotstring_match in file_hotstrings:
                hotstrings.append(file_hotstring_match)

    hotstrings.sort(key=lambda k: len(k[0].removeprefix("::")), reverse=True)

    with open(DIST_PATH / "common.ahk", "w", encoding="utf-8", newline="\n") as f:
        f.writelines(
            [
                f"{hotstring}::\n    Send, {replacement} ; {description}\nreturn\n"
                for hotstring, replacement, description in hotstrings
            ]
        )


def generate_main(default: str):
    """Generates main.ahk file.

    Args:
        default (str): Default keyboard name.
    """

    if not DIST_PATH.exists():
        DIST_PATH.mkdir()

    keyboard_icons_path = ICONS_PATH / "keyboards"
    icon_not_found_message = (
        "Warning: icon {}.ico not found in "
        + str(keyboard_icons_path)
        + ". Using default AHK icon."
    )
    hotkey_template = dedent(
        """\
        {}::
        {{
            keyboard := "{}"
            curIcon := "{}"
            TraySetIcon "{}"
        }}"""
    )
    if_template = dedent(
        """\
        #HotIf keyboard = "{0}"
            #include keyboards\\{0}.ahk
        #HotIf"""
    )

    default_keyboard = KEYBOARDS_PATH / f"{default}.ahk"
    if not default_keyboard.exists():
        raise FileNotFoundError(
            f"Default keyboard {default}.ahk not found in {KEYBOARDS_PATH}."
        )
    default_icon = default
    default_icon_path = keyboard_icons_path / f"{default}.ico"
    default_icon_path_str = str(
        PureWindowsPath(default_icon_path.relative_to(SRC_PATH))
    )
    if not default_icon_path.exists():
        default_icon = "*"
        default_icon_path_str = "*"
        print(icon_not_found_message.format(default))
    auto_execute_section = dedent(
        f'''\
        keyboard := "{default}"
        curIcon := "{default_icon}"
        TraySetIcon "{default_icon_path_str}"'''
    )

    hotkeys = {}
    if_statements = {}
    order_dict = {}
    for keyboard in KEYBOARDS_PATH.iterdir():
        if keyboard.suffix == ".ahk":
            with open(keyboard, encoding="utf-8", newline="\n") as f:
                hotkey = f.readlines()[2].removeprefix("; ").strip()

            name = keyboard.stem
            icon_path = keyboard_icons_path / f"{name}.ico"
            icon_path_str = str(PureWindowsPath(icon_path.relative_to(SRC_PATH)))
            icon = name
            if not icon_path.exists():
                icon = "*"
                icon_path_str = "*"
                print(icon_not_found_message.format(name))

            hotkeys[name] = hotkey_template.format(hotkey, name, icon, icon_path_str)
            if_statements[name] = if_template.format(name)
            order_dict[name] = hotkey

    order = sorted(order_dict, key=lambda k: order_dict[k])

    with open(
        Path(__file__).parent / "templates" / "main.template.ahk", encoding="utf-8"
    ) as f:
        template = f.read()

    final_template = (
        template.replace("{AUTO_EXECUTE_SECTION}", auto_execute_section)
        .replace(
            "{HOTKEYS}",
            "\n\n".join(
                hotkey
                for _, hotkey in sorted(
                    hotkeys.items(), key=lambda k: order.index(k[0])
                )
            ),
        )
        .replace(
            "{IF_STATEMENTS}",
            "\n\n".join(
                if_statement
                for _, if_statement in sorted(
                    if_statements.items(), key=lambda k: order.index(k[0])
                )
            ),
        )
    )

    with open(DIST_PATH / "main.ahk", "w", encoding="utf-8", newline="\n") as f:
        f.write(final_template)


def copy_files():
    if not DIST_PATH.exists():
        DIST_PATH.mkdir()

    shutil.copytree(
        SRC_PATH,
        DIST_PATH,
        ignore=shutil.ignore_patterns("scripts"),
        dirs_exist_ok=True,
    )
