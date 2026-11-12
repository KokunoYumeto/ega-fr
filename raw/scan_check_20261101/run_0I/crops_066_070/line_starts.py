"""Print the left edge (first dark column) of each text line of a strip, to see paragraph indents.
usage: python line_starts.py PAGE STRIP"""
import sys
from PIL import Image

page, strip = int(sys.argv[1]), int(sys.argv[2])
im = Image.open(rf"user/Documents/ega_scan_check_20261101/run_0I/page_{page:03d}_s{strip}.png").convert("L")
w, h = im.size
px = im.load()
rows = [sum(1 for x in range(0, w, 2) if px[x, y] < 128) for y in range(h)]
y = 0
while y < h:
    if rows[y] > 3:
        y0 = y
        while y < h and rows[y] > 0:
            y += 1
        y1 = y
        if y1 - y0 > 15:
            left = min((x for x in range(w) for yy in range(y0, y1, 2) if px[x, yy] < 128), default=None)
            right = max((x for x in range(w - 1, -1, -1) for yy in range(y0, y1, 2) if px[x, yy] < 128), default=None)
            print(f"rows {y0}-{y1}: left {left} right {right}")
    y += 1
