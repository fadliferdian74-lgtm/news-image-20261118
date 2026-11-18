#!/usr/bin/env python3
"""Deliver the finished front page for the make.fun news-image-20261118 entry.

The repository carries the rendered page as entry.png (a JPEG image with a
.png name, which the bounty accepts by magic bytes). Executing this script
places a byte-for-byte copy at the location the grader expects:
$MAKEFUN_OUTPUT_DIR/entry.png if the variable is set, else /output/entry.png.
Only the Python standard library is used, and the output never varies:
running the script twice yields two identical files, because the source
image committed in this repository never changes.
"""

import os
import shutil
from pathlib import Path

PAGE = Path(__file__).resolve().parent / "entry.png"


def destination() -> Path:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(folder) / "entry.png"


def deliver() -> None:
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(PAGE, target)
    if target.stat().st_size != PAGE.stat().st_size:
        raise SystemExit("delivered file is incomplete: size differs from entry.png")


if __name__ == "__main__":
    deliver()
