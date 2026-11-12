import sys
import numpy as np
from PIL import Image
# usage: strokes.py src y0 y1 [x0 x1]  -> words (by column gaps) with mean horizontal dark-run length
src, y0, y1 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
im = np.array(Image.open(src).convert("L"))
x0 = int(sys.argv[4]) if len(sys.argv) > 4 else 0
x1 = int(sys.argv[5]) if len(sys.argv) > 5 else im.shape[1]
band = im[y0:y1, x0:x1] < 128
col = band.sum(axis=0)
words, inword, start, gap = [], False, 0, 0
for x, c in enumerate(col):
    if c > 0:
        if not inword:
            inword, start = True, x
        gap = 0
    else:
        if inword:
            gap += 1
            if gap > 12:
                words.append((start, x - gap)); inword = False
if inword:
    words.append((start, len(col) - 1))
for a, b in words:
    w = band[:, a:b + 1]
    runs = []
    for row in w:
        r = 0
        for v in row:
            if v: r += 1
            elif r: runs.append(r); r = 0
        if r: runs.append(r)
    vr = []
    for colv in w.T:
        r = 0
        for v in colv:
            if v: r += 1
            elif r: vr.append(r); r = 0
        if r: vr.append(r)
    print(f"x {a + x0:5d}-{b + x0:5d}  w {b - a + 1:4d}  hrun {np.median(runs) if runs else 0:5.1f}  mean {np.mean(runs) if runs else 0:5.2f}  vrun_med {np.median(vr) if vr else 0:5.1f}")
