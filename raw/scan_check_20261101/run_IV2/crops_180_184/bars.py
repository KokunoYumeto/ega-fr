"""Measure the longest horizontal dark run per row in a box (original pixels).

Usage: python -I bars.py PAGE STRIP x0 y0 x1 y1 [threshold]
Prints, for each row with a run >= 15 px, the row index and the runs (start, length).
"""
import sys
from PIL import Image

run = r"user\Documents\ega_scan_check_20261101\run_IV2"
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
thr = int(sys.argv[7]) if len(sys.argv) > 7 else 128
im = Image.open(rf"{run}\page_{page:03d}_s{strip}.png").convert("L")
px = im.load()
for y in range(y0, y1):
    runs = []
    start = None
    for x in range(x0, x1 + 1):
        dark = x < x1 and px[x, y] < thr
        if dark and start is None:
            start = x
        elif not dark and start is not None:
            if x - start >= int(sys.argv[8] if len(sys.argv) > 8 else 15):
                runs.append((start, x - start))
            start = None
    if runs:
        print(y, runs)
