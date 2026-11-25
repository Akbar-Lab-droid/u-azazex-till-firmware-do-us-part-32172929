"""Entry program for make.fun bounty u-azazex-till-firmware-do-us-part-32172929.

Reads the committed entry.txt and writes it to the output directory
given by MAKEFUN_OUTPUT_DIR (default "out").
"""

import os
import shutil  # stdlib only: no network, no third-party deps

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.txt")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
