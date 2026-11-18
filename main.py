#!/usr/bin/env python3
"""Entry program for the make.fun bounty 'news-image-20261118'.

The finished front-page image ships in this repository as entry.png.
Running this program copies it, byte for byte, to the output location:
$MAKEFUN_OUTPUT_DIR/entry.png when that variable is set, otherwise
/output/entry.png. Standard library only, no network, deterministic.
"""

import os
import shutil

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.png")


def main() -> None:
    dest = output_path()
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copyfile(SOURCE, dest)


if __name__ == "__main__":
    main()
