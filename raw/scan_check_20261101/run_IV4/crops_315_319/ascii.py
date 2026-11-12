"""Print a region of a strip as ASCII art (# dark, + mid, . light).

usage: python ascii.py PAGE STRIP x0 y0 x1 y1
"""
import sys
from PIL import Image

page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
base = r"user\Documents\ega_scan_check_20261101\run_IV4"
im = Image.open(rf"{base}\page_{page}_s{strip}.png").convert("L").crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
for y in range(h):
    row = "".join("#" if px[x, y] < 100 else "+" if px[x, y] < 170 else "." for x in range(w))
    print(f"{y0 + y:4d} {row}")
