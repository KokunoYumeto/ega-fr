"""Connected components (dark pixels) in a region: components.py IMG x0 y0 x1 y1 [threshold]
Prints bbox, height, width, ink (dark px), and mean horizontal / vertical dark-run lengths (stroke thickness)."""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

img, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 128
a = np.asarray(Image.open(img).convert('L'))[y0:y1, x0:x1]
dark = a < thr
lab, n = ndimage.label(dark, structure=np.ones((3, 3)))
objs = ndimage.find_objects(lab)


def runs(mask, axis):
    m = mask if axis == 1 else mask.T
    lens = []
    for row in m:
        c = 0
        for v in row:
            if v:
                c += 1
            elif c:
                lens.append(c)
                c = 0
        if c:
            lens.append(c)
    return (sum(lens) / len(lens)) if lens else 0


rows = []
for i, sl in enumerate(objs, 1):
    m = lab[sl] == i
    ink = int(m.sum())
    if ink < 15:
        continue
    ys, xs = sl
    rows.append((xs.start + x0, ys.start + y0, xs.stop + x0, ys.stop + y0, ink, runs(m, 1), runs(m, 0)))
rows.sort()
for r in rows:
    print('x %4d-%4d y %4d-%4d  h %3d w %3d  ink %5d  hrun %.2f vrun %.2f' % (r[0], r[2], r[1], r[3], r[3] - r[1], r[2] - r[0], r[4], r[5], r[6]))
