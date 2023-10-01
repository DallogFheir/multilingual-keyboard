from pathlib import Path

SRC_PATH = Path.cwd() / "src"
ICONS_PATH = SRC_PATH / "icons"
KEYBOARDS_PATH = SRC_PATH / "keyboards"
SCRIPTS_PATH = SRC_PATH / "scripts"
DIST_PATH = Path.cwd() / "dist"

HOTKEY_REGEX = r"^(?!;)(.+?)::.*?Send, (.+?)(?: ; ?(.*?))?\nreturn$"
