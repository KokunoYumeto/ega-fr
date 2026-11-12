"""Print a binarised region of a page strip as ASCII art (# = ink), for comparing glyph weights.

usage: python ascii_glyph.py PAGE STRIP X0 Y0 X1 Y1 [THRESHOLD]
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
thr = int(sys.argv[7]) if len(sys.argv) > 7 else 128
a = np.asarray(Image.open(RUN / f"page_{page:03d}_s{strip}.png").convert("L"))[y0:y1, x0:x1]
for row in a:
    print("".join("#" if v < thr else ("+" if v < 200 else ".") for v in row))
