"""Measure a word's ink: bounding box, mean horizontal run length (stroke thickness), dark-pixel density.

Usage: python -I measure.py <strip.png> <x0> <y0> <x1> <y1> [label]
"""
import sys
from PIL import Image

src, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
label = sys.argv[6] if len(sys.argv) > 6 else ""
im = Image.open(src).convert("L").crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
dark = [[px[x, y] < 128 for x in range(w)] for y in range(h)]
cols = [x for x in range(w) if any(dark[y][x] for y in range(h))]
rows = [y for y in range(h) if any(dark[y][x] for x in range(w))]
runs = []
for y in range(h):
    r = 0
    for x in range(w):
        if dark[y][x]:
            r += 1
        elif r:
            runs.append(r); r = 0
    if r:
        runs.append(r)
n = sum(sum(row) for row in dark)
bw, bh = (max(cols) - min(cols) + 1, max(rows) - min(rows) + 1) if cols else (0, 0)
print(f"{label:10s} bbox {bw}x{bh}  dark {n}  density {n / (bw * bh):.3f}  mean run {sum(runs) / len(runs):.2f}")
