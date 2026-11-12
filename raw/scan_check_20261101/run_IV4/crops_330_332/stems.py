"""Print an ASCII map (threshold 128) of a box of a strip, every row, every column.

Usage: python stems.py PAGE STRIP x0 y0 x1 y1
"""
import sys
from PIL import Image

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
im = Image.open(rf"{RUN}\page_{page}_s{strip}.png").convert("L")
px = im.load()
for y in range(y0, y1):
    print(f"{y:4d} " + "".join("#" if px[x, y] < 128 else "." for x in range(x0, x1)))
