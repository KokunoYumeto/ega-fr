"""Slant of a parenthesis glyph: mean ink x in the top and bottom fifth of its rows.
usage: python -I slant.py PAGE STRIP x0 y0 x1 y1 [threshold]"""
import sys
import pathlib
from PIL import Image
import numpy as np

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
thr = int(sys.argv[7]) if len(sys.argv) > 7 else 140
im = np.array(Image.open(RUN / f"page_{page:03d}_s{strip}.png").convert("L"))[y0:y1, x0:x1]
ink = im < thr
rows = np.where(ink.any(axis=1))[0]
cols = np.where(ink.any(axis=0))[0]
top, bot = rows[0], rows[-1]
h = bot - top + 1
print(f"glyph rows {top+y0}-{bot+y0} (h={h}), cols {cols[0]+x0}-{cols[-1]+x0}")
k = max(1, h // 5)
for name, rr in (("top", range(top, top + k)), ("mid", range(top + 2 * k, top + 3 * k)), ("bottom", range(bot - k + 1, bot + 1))):
    xs = [x for r in rr for x in np.where(ink[r])[0]]
    print(f"{name:6s}: mean x {np.mean(xs) + x0:.1f}  min {min(xs) + x0}  max {max(xs) + x0}")
for r in range(top, bot + 1):
    print(f"{r + y0:4d} " + "".join("#" if v else "." for v in ink[r]))
