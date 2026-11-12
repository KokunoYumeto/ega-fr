"""Flag words whose stroke width is well above the line's median (possible wrong-fount bold).

Usage: python boldscan.py <strip.png> [ratio]
Prints line y-range, word x-range and the ratio of the word's mean horizontal dark-run
length to the median of the line. Only a pointer for visual checking.
"""
import sys
import numpy as np
from PIL import Image

src = sys.argv[1]
ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 1.22
a = np.array(Image.open(src).convert("L")) < 140
H, W = a.shape
rows = a.sum(axis=1)
# line segmentation
lines = []
inl = False
for y in range(H):
    if rows[y] > 3 and not inl:
        y0 = y
        inl = True
    elif rows[y] <= 3 and inl:
        if y - y0 > 12:
            lines.append((y0, y))
        inl = False


def mean_run(block):
    runs = []
    for row in block:
        r = 0
        for v in row:
            if v:
                r += 1
            elif r:
                runs.append(r)
                r = 0
        if r:
            runs.append(r)
    runs = [r for r in runs if r <= 25]
    return (sum(runs) / len(runs), len(runs)) if runs else (0, 0)


for (y0, y1) in lines:
    blk = a[y0:y1]
    cols = blk.sum(axis=0)
    # word segmentation: gaps of >= 14 blank columns
    words = []
    x = 0
    while x < W:
        if cols[x] > 0:
            xs = x
            gap = 0
            while x < W and gap < 14:
                gap = gap + 1 if cols[x] == 0 else 0
                x += 1
            words.append((xs, x - gap))
        else:
            x += 1
    stats = []
    for (xs, xe) in words:
        m, n = mean_run(blk[:, xs:xe])
        if n >= 40:
            stats.append((xs, xe, m))
    if len(stats) < 3:
        continue
    med = float(np.median([s[2] for s in stats]))
    for (xs, xe, m) in stats:
        if med and m / med >= ratio:
            print(f"y {y0}-{y1}  x {xs}-{xe}  run {m:.2f}  line median {med:.2f}  ratio {m/med:.2f}")
