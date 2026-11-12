import sys
import numpy as np
from PIL import Image
from scipy import ndimage

# usage: strokes.py SRC y0 y1 [x0 x1]
# lists connected components (glyphs) in the band with their horizontal-run stroke statistics
src = sys.argv[1]
y0, y1 = int(sys.argv[2]), int(sys.argv[3])
x0 = int(sys.argv[4]) if len(sys.argv) > 4 else 0
x1 = int(sys.argv[5]) if len(sys.argv) > 5 else None
im = np.array(Image.open(src).convert('L')).astype(float)
band = im[y0:y1, x0:x1]
dark = band < 140
lab, n = ndimage.label(dark)
objs = ndimage.find_objects(lab)
rows = []
for i, sl in enumerate(objs):
    ys, xs = sl
    h = ys.stop - ys.start
    w = xs.stop - xs.start
    if h < 8 and w < 8:
        continue
    sub = (lab[sl] == i + 1)
    runs = []
    for r in sub:
        c = 0
        for v in r:
            if v:
                c += 1
            elif c:
                runs.append(c); c = 0
        if c:
            runs.append(c)
    runs = [r for r in runs if r <= 14]
    if not runs:
        continue
    rows.append((xs.start + x0, ys.start + y0, w, h, np.median(runs), np.mean(runs), int(sub.sum())))
rows.sort()
for r in rows:
    print('x=%5d y=%4d w=%3d h=%3d  medrun=%.1f meanrun=%.2f ink=%d' % r)
