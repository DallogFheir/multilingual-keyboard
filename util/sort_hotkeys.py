from pathlib import Path
import re


def sort_hotkeys() -> None:
    """Sorts hotkeys in AHK scripts in directories 'common' and 'keyboards' alphabetically (lowercase letters before their uppercase counterparts)."""
    keyboards_path = Path.cwd() / "subscripts" / "keyboards"
    common_path = Path.cwd() / "subscripts" / "common"

    for path in (keyboards_path, common_path):
        for file in path.iterdir():
            if file.is_file() and file.suffix == ".ahk":
                with open(file, encoding="utf-8") as f:
                    script = f.read()

                rest = re.fullmatch(
                    r"((?:.|\n)*?)((?:\n?.+\n.*\nreturn)+)((?:.|\n)*)", script
                )

                if rest is not None:
                    before, middle, after = rest.groups()

                    if middle.startswith("\n"):
                        before += "\n"
                        middle = middle.removeprefix("\n")

                    rules = []
                    for rule_match in re.findall(
                        r"^((?:.+?)::.*?Send, (.+?)(?: ; ?(?:.*?))?\nreturn)$",
                        middle,
                        re.DOTALL | re.MULTILINE,
                    ):
                        whole, symbol = rule_match

                        rules.append((symbol, whole))

                    new_script = (
                        before
                        + "\n".join(
                            rule[1]
                            for rule in sorted(
                                rules,
                                key=lambda k: (
                                    ord(k[0].lower()),
                                    -ord(k[0]),
                                ),
                            )
                        )
                        + after
                    )

                    with open(file, "w", encoding="utf-8") as f:
                        f.write(new_script)
