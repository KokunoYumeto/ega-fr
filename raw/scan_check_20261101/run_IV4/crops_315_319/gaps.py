"""Print the blank column runs (gaps) wider than a threshold along a text line of a strip.

usage: python gaps.py PAGE STRIP x0 y0 x1 y1 [min_gap]
"""
import sys
from PIL import Image

page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
min_gap = int(sys.argv[7]) if len(sys.argv) > 7 else 6
base = r"user\Documents\ega_scan_check_20261101\run_IV4"
im = Image.open(rf"{base}\page_{page}_s{strip}.png").convert("L").crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
ink = [any(px[x, y] < 140 for y in range(h)) for x in range(w)]
x = 0
while x < w:
    if not ink[x]:
        s = x
        while x < w and not ink[x]:
            x += 1
        if x - s >= min_gap:
            print(f"gap {x0 + s}-{x0 + x} width {x - s}")
    else:
        x += 1
