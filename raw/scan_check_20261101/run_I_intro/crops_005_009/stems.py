"""List tall narrow glyphs (capital I, lowercase l) in a strip with their stem width, to tell bold from regular.

usage: python -I stems.py STRIP [y0 y1]   (original pixel rows; default whole strip)
Prints x, y, height, width, stem width (median dark-pixel run at mid-height) and a darkness sum."""
import pathlib
import sys

import numpy as np
from PIL import Image
from scipy import ndimage

d = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_I_intro")
im = np.array(Image.open(d / sys.argv[1]).convert("L"))
y0 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
y1 = int(sys.argv[3]) if len(sys.argv) > 3 else im.shape[0]
dark = im < 128
lab, n = ndimage.label(dark, structure=np.ones((3, 3)))
rows = []
for i, sl in enumerate(ndimage.find_objects(lab), start=1):
    ys, xs = sl
    h, w = ys.stop - ys.start, xs.stop - xs.start
    if not (28 <= h <= 46 and 6 <= w <= 30):
        continue
    if not (y0 <= ys.start < y1):
        continue
    comp = lab[sl] == i
    mid = comp[int(h * 0.35):int(h * 0.65)]
    runs = mid.sum(axis=1)
    if runs.max() > 0.75 * w and w > 16:  # not a stem shape at mid-height
        continue
    stem = float(np.median(runs))
    rows.append((ys.start, xs.start, h, w, stem, int(comp.sum())))
for r in sorted(rows, key=lambda r: (r[0] // 40, r[1])):
    print("y=%4d x=%4d h=%2d w=%2d stem=%4.1f area=%4d" % r)
