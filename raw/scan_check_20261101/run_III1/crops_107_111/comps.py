"""List connected ink components (height > minh) in a region of a strip: x, y, w, h, density, ink pixels.

usage: python -I comps.py STRIP.png x0 y0 x1 y1 [minh]
"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
minh = int(sys.argv[6]) if len(sys.argv) > 6 else 10
im = np.array(Image.open(src).convert("L"))
sub = im[y0:y1, x0:x1] < 140
lab, n = ndimage.label(sub)
rows = []
for i, sl in enumerate(ndimage.find_objects(lab)):
    h = sl[0].stop - sl[0].start
    w = sl[1].stop - sl[1].start
    if h >= minh:
        g = lab[sl] == i + 1
        rows.append((x0 + sl[1].start, y0 + sl[0].start, w, h, round(g.sum() / (w * h), 3), int(g.sum())))
for r in sorted(rows):
    print(r)
