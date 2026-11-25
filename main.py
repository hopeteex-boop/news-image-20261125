#!/usr/bin/env python3
"""Entry point for the news-image-20261125 make.fun entry.

Copies the generated front-page image (entry.png) into the output
directory the grader provides via MAKEFUN_OUTPUT_DIR.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote " + dst)


if __name__ == "__main__":
    main()
