"""Measure the ink of one glyph (connected component) in a page strip.

Usage: python ink.py PAGE STRIP X0 Y0 X1 Y1 [LABEL]
Box in the 2000-px display frame of the strip. Reports, for every connected
dark component inside the box: bbox (original px), area (dark px), and the
mean horizontal run length (a stroke-width proxy).
"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
label = sys.argv[7] if len(sys.argv) > 7 else ""
src = f"user/Documents/ega_scan_check_20261101/run_IV2/page_{page}_s{strip}.png"
im = Image.open(src).convert("L")
f = im.size[0] / 2000.0
bx = [int(round(v * f)) for v in (x0, y0, x1, y1)]
a = np.array(im)[bx[1]:bx[3], bx[0]:bx[2]]
dark = a < 128
lab, n = ndimage.label(dark)
rows = []
for i in range(1, n + 1):
    ys, xs = np.nonzero(lab == i)
    area = len(ys)
    if area < 15:
        continue
    h = ys.max() - ys.min() + 1
    w = xs.max() - xs.min() + 1
    m = (lab == i)
    runs = []
    for r in m:
        d = np.diff(np.concatenate([[0], r.astype(int), [0]]))
        s = np.nonzero(d == 1)[0]
        e = np.nonzero(d == -1)[0]
        runs.extend(e - s)
    rows.append((xs.min() + bx[0], ys.min() + bx[1], w, h, area, float(np.mean(runs))))
rows.sort()
print(label)
for r in rows:
    print("  x=%d y=%d w=%d h=%d area=%d meanrun=%.2f" % r)
