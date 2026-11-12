"""Measure horizontal dark-run widths (stroke thickness) in a small box of a strip.

usage: python stroke.py PAGE STRIP x0 y0 x1 y1 [threshold]
Prints, for each row, the lengths of dark runs; then the median of the longest run per row.
"""
import sys
from statistics import median
from PIL import Image

page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
th = int(sys.argv[7]) if len(sys.argv) > 7 else 128
base = r"user\Documents\ega_scan_check_20261101\run_IV4"
im = Image.open(rf"{base}\page_{page}_s{strip}.png").convert("L").crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
longest = []
for y in range(h):
    runs, cur = [], 0
    for x in range(w):
        if px[x, y] < th:
            cur += 1
        elif cur:
            runs.append(cur)
            cur = 0
    if cur:
        runs.append(cur)
    if runs:
        longest.append(max(runs))
    print(y, runs)
if longest:
    print("median longest run:", median(longest), "rows with ink:", len(longest))
