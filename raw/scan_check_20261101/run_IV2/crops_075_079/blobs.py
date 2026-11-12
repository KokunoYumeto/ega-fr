"""List small dark connected components (dots) in a region: python blobs.py STRIP x0 y0 x1 y1 [maxarea]
Prints each small blob's bbox (strip coordinates) plus the region's text baseline estimate."""
import sys
from PIL import Image
import numpy as np
from scipy import ndimage
src, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
maxarea = int(sys.argv[6]) if len(sys.argv) > 6 else 400
a = np.array(Image.open(src).convert("L").crop((x0, y0, x1, y1)))
dark = a < 128
lab, n = ndimage.label(dark)
objs = ndimage.find_objects(lab)
rows = []
for i, sl in enumerate(objs, 1):
    area = int((lab[sl] == i).sum())
    ys, xs = sl
    rows.append((xs.start + x0, ys.start + y0, xs.stop + x0, ys.stop + y0, area))
rows.sort()
for r in rows:
    tag = "DOT?" if r[4] <= maxarea and (r[2]-r[0]) < 25 and (r[3]-r[1]) < 25 else ""
    print(r, tag)
