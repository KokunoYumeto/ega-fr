"""Horizontal dark-run lengths per row inside a box (stroke widths).

usage: python runs.py PAGE STRIP x0 y0 x1 y1 [THRESH]
"""
import sys
from PIL import Image

RUN = r"user/Documents/ega_scan_check_20261101/run_IV4/"
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
th = int(sys.argv[7]) if len(sys.argv) > 7 else 128
im = Image.open(RUN + "page_%s_s%s.png" % (page, strip)).convert("L")
px = im.load()
for y in range(y0, y1):
    runs = []
    x = x0
    while x < x1:
        if px[x, y] < th:
            s = x
            while x < x1 and px[x, y] < th:
                x += 1
            runs.append((s, x - s))
        else:
            x += 1
    print(y, " ".join("%d@%d" % (w, s) for s, w in runs))
