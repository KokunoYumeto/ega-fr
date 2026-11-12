import sys
from PIL import Image
import numpy as np
from scipy import ndimage
# usage: measure.py img x0 y0 x1 y1 -> list components (bbox, w, h), sorted by x
img, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
a = np.array(Image.open(img).convert('L').crop((x0, y0, x1, y1)))
b = a < 140
lab, n = ndimage.label(b)
objs = ndimage.find_objects(lab)
rows = []
for i, sl in enumerate(objs):
    ys, xs = sl
    h = ys.stop - ys.start; w = xs.stop - xs.start
    if h * w < 12: continue
    rows.append((xs.start + x0, ys.start + y0, w, h))
for r in sorted(rows):
    print("x=%4d y=%4d w=%3d h=%3d" % r)
