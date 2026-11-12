"""measure.py PAGE STRIP X0 Y0 X1 Y1: print ink column runs (word extents) and mean stroke darkness in the box (display coords)."""
import sys, pathlib
from PIL import Image
import numpy as np
page, strip, x0, y0, x1, y1 = sys.argv[1:7]
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
im = Image.open(run / f"page_{int(page):03d}_s{strip}.png").convert("L")
f = im.width / 2000.0
box = tuple(int(round(float(v) * f)) for v in (x0, y0, x1, y1))
a = np.array(im.crop(box)).astype(float)
ink = a < 128
cols = ink.any(axis=0)
runs = []
start = None
gap = 0
for i, c in enumerate(cols):
    if c:
        if start is None:
            start = i
        gap = 0
        last = i
    else:
        if start is not None:
            gap += 1
            if gap > 12:  # word gap in original px
                runs.append((start + box[0], last + box[0]))
                start = None
                gap = 0
if start is not None:
    runs.append((start + box[0], last + box[0]))
print("word extents (orig px):", [(s, e, e - s) for s, e in runs])
# stem thickness: for each row, lengths of horizontal ink runs; report median run length
lens = []
for row in ink:
    n = 0
    for v in row:
        if v:
            n += 1
        elif n:
            lens.append(n)
            n = 0
    if n:
        lens.append(n)
lens = np.array(lens)
print("horizontal ink run length: median %.1f mean %.2f  ink fraction %.4f" % (np.median(lens), lens.mean(), ink.mean()))
