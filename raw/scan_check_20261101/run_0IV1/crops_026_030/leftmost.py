"""Leftmost and rightmost dark pixel per text line of a strip: python leftmost.py PAGE STRIP [THRESH]
Groups rows with ink into lines and prints (y0, y1, leftmost x, rightmost x)."""
import pathlib
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
page, strip = int(sys.argv[1]), int(sys.argv[2])
th = int(sys.argv[3]) if len(sys.argv) > 3 else 110
im = Image.open(RUN / f"page_{page:03d}_s{strip}.png").convert("L")
w, h = im.size
px = im.load()
rows = []
for y in range(h):
    xs = [x for x in range(150, w - 150) if px[x, y] < th]
    rows.append((min(xs), max(xs)) if len(xs) > 3 else None)
y = 0
while y < h:
    if rows[y] is None:
        y += 1
        continue
    y0 = y
    lo, hi = rows[y]
    while y < h and rows[y] is not None:
        lo, hi = min(lo, rows[y][0]), max(hi, rows[y][1])
        y += 1
    if y - y0 > 8:
        print(y0, y, lo, hi)
