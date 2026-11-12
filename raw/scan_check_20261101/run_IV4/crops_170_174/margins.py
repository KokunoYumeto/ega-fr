"""Right-most and left-most ink column of each text line in a strip.
usage: python -I margins.py PAGE STRIP [threshold]"""
import sys
import pathlib
from PIL import Image
import numpy as np

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
page, strip = int(sys.argv[1]), int(sys.argv[2])
thr = int(sys.argv[3]) if len(sys.argv) > 3 else 128
im = np.array(Image.open(RUN / f"page_{page:03d}_s{strip}.png").convert("L"))
ink = im < thr
rows = ink.sum(axis=1)
lines = []
inl = False
for y, r in enumerate(rows):
    if r > 3 and not inl:
        inl, y0 = True, y
    elif r <= 3 and inl:
        inl = False
        lines.append((y0, y))
if inl:
    lines.append((y0, len(rows)))
for y0, y1 in lines:
    cols = np.where(ink[y0:y1].any(axis=0))[0]
    if len(cols):
        print(f"rows {y0:4d}-{y1:4d}  left {cols[0]:4d}  right {cols[-1]:4d}")
