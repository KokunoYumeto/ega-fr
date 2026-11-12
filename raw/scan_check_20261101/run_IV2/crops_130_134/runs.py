"""Print the longest horizontal dark runs in a region of a strip (display coordinates).

usage: python runs.py PAGE STRIP X0 Y0 X1 Y1 [MINLEN]
Reports, per row, the dark runs at least MINLEN original pixels long (threshold 140),
merged across gaps of at most 2 px, so a dash or rule shows up as one run.
"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image

RUN = Path(__file__).resolve().parent.parent
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(float, sys.argv[3:7])
minlen = int(sys.argv[7]) if len(sys.argv) > 7 else 12
img = Image.open(RUN / f"page_{page:03d}_s{strip}.png").convert("L")
f = img.width / 2000.0
X0, Y0, X1, Y1 = (int(round(v * f)) for v in (x0, y0, x1, y1))
a = np.array(img)[Y0:Y1, X0:X1] < 140
for r in range(a.shape[0]):
    row = a[r]
    runs = []
    c = 0
    n = len(row)
    while c < n:
        if row[c]:
            s = c
            while c < n and (row[c] or (c + 2 < n and (row[c + 1] or row[c + 2]))):
                c += 1
            runs.append((s + X0, c - s))
        c += 1
    long = [(s, l) for s, l in runs if l >= minlen]
    if long:
        print(r + Y0, long)
