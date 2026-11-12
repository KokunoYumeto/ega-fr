"""Print the ink runs (columns with dark pixels) of a region, to measure gaps between glyphs.

usage: python gap.py PAGE STRIP X0 Y0 X1 Y1   (displayed-pixel coordinates, factor width/2000)
"""
import sys
from pathlib import Path
from PIL import Image

RUN = Path(__file__).resolve().parent.parent
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
im = Image.open(RUN / f"page_{page:03d}_s{strip}.png").convert("L")
f = im.width / 2000.0
box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
reg = im.crop(box)
w, h = reg.size
px = reg.load()
cols = []
for x in range(w):
    dark = [y for y in range(h) if px[x, y] < 140]
    cols.append((min(dark), max(dark)) if dark else None)
runs = []
start = None
for x in range(w + 1):
    c = cols[x] if x < w else None
    if c is not None and start is None:
        start = x
    elif c is None and start is not None:
        ys = [cols[i] for i in range(start, x)]
        runs.append((start + box[0], x - 1 + box[0], min(a for a, b in ys) + box[1], max(b for a, b in ys) + box[1]))
        start = None
prev = None
for r in runs:
    gap = r[0] - prev - 1 if prev is not None else None
    print(f"x {r[0]}-{r[1]} (w {r[1]-r[0]+1})  y {r[2]}-{r[3]}  gap_before {gap}")
    prev = r[1]
