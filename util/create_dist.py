from pathlib import Path
from zipfile import ZipFile
from .common import DIST_PATH


def create_dist() -> None:
    if not DIST_PATH.exists():
        raise FileNotFoundError

    dist_files = DIST_PATH.glob("./**/*")

    with ZipFile(Path.cwd() / "dist.zip", "w") as zip:
        for file in dist_files:
            if file.is_file():
                file_path = file.relative_to(DIST_PATH)
                zip.write(file.absolute(), file_path)
