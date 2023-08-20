from pathlib import Path, PureWindowsPath
from textwrap import dedent


def generate_common():
    """Generates common.ahk file."""
    src_dir = Path.cwd() / "src"
    includes = [
        f"#include {str(file.relative_to(src_dir))}\n"
        for file in sorted(
            (src_dir / "subscripts" / "common").iterdir(), key=lambda k: k.stem
        )
        if file.suffix == ".ahk"
    ]

    with open(src_dir / "common.ahk", "w", encoding="utf-8-sig") as f:
        f.writelines(includes)


def generate_main(default: str):
    """Generates main.ahk file.

    Args:
        default (str): Default keyboard name.
    """
    src_dir = Path.cwd() / "src"
    icons_dir = src_dir / "icons" / "keyboards"
    keyboards_dir = src_dir / "subscripts" / "keyboards"

    icon_not_found_message = (
        "Warning: icon {}.ico not found in "
        + str(icons_dir)
        + ". Using default AHK icon."
    )
    hotkey_template = dedent(
        """\
        {}::
            keyboard := "{}"
            curIcon := "{}"
            Menu, Tray, Icon, {}
        return"""
    )
    if_template = dedent(
        """\
        #If keyboard = "{0}"
            #include subscripts\\keyboards\\{0}.ahk
        #If"""
    )

    default_keyboard = keyboards_dir / f"{default}.ahk"
    if not default_keyboard.exists():
        raise FileNotFoundError(
            f"Default keyboard {default}.ahk not found in {keyboards_dir}."
        )
    default_icon = default
    default_icon_path = icons_dir / f"{default}.ico"
    default_icon_path_str = str(PureWindowsPath(default_icon_path.relative_to(src_dir)))
    if not default_icon_path.exists():
        default_icon = "*"
        default_icon_path_str = "*"
        print(icon_not_found_message.format(default))
    auto_execute_section = dedent(
        f"""\
        keyboard := "{default}"
        curIcon := "{default_icon}"
        Menu, Tray, Icon, {default_icon_path_str}"""
    )

    hotkeys = {}
    if_statements = {}
    order_dict = {}
    for keyboard in keyboards_dir.iterdir():
        if keyboard.suffix == ".ahk":
            with open(keyboard, encoding="utf-8-sig") as f:
                hotkey = f.readlines()[2].removeprefix("; ").strip()

            name = keyboard.stem
            icon_path = icons_dir / f"{name}.ico"
            icon_path_str = str(icon_path.relative_to(src_dir))
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
        Path(__file__).parent / "templates" / "main.template.ahk", encoding="utf-8-sig"
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

    with open(src_dir / "main.ahk", "w", encoding="utf-8-sig") as f:
        f.write(final_template)
