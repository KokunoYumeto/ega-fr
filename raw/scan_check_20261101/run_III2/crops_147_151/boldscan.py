import sys
import numpy as np
from PIL import Image
# usage: boldscan.py src [thr]  -> lines (row projection) and words with heavy strokes
src = sys.argv[1]
thr = float(sys.argv[2]) if len(sys.argv) > 2 else 6.3
im = np.array(Image.open(src).convert("L")) < 128
rows = im.sum(axis=1)
lines, inl, s = [], False, 0
for y, r in enumerate(rows):
    if r > 3 and not inl: inl, s = True, y
    elif r <= 3 and inl:
        inl = False
        if y - s > 15: lines.append((s, y))
for (y0, y1) in lines:
    band = im[y0:y1]
    col = band.sum(axis=0)
    words, inword, start, gap = [], False, 0, 0
    for x, c in enumerate(col):
        if c > 0:
            if not inword: inword, start = True, x
            gap = 0
        elif inword:
            gap += 1
            if gap > 12: words.append((start, x - gap)); inword = False
    if inword: words.append((start, len(col) - 1))
    means = []
    for a, b in words:
        w = band[:, a:b + 1]
        runs = []
        for row in w:
            r = 0
            for v in row:
                if v: r += 1
                elif r: runs.append(r); r = 0
            if r: runs.append(r)
        means.append(np.mean(runs) if runs else 0)
    med = np.median(means) if means else 0
    flag = [(a, b, m) for (a, b), m in zip(words, means) if m > thr and m > med * 1.22]
    if flag:
        print(f"line y {y0}-{y1} median {med:.2f}: " + "; ".join(f"x{a}-{b} m{m:.2f}" for a, b, m in flag))
