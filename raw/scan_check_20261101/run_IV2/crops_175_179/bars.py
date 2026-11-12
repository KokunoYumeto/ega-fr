import sys
import numpy as np
from PIL import Image
from scipy import ndimage
# usage: bars.py strip.png x0 y0 x1 y1  -> lists horizontal-bar-like components (w, h, x, y) in original px
src = sys.argv[1]; x0, y0, x1, y1 = map(int, sys.argv[2:6])
im = np.array(Image.open(src).convert('L').crop((x0, y0, x1, y1)))
dark = im < 128
lab, n = ndimage.label(dark)
objs = ndimage.find_objects(lab)
rows = []
for i, sl in enumerate(objs, 1):
    h = sl[0].stop - sl[0].start; w = sl[1].stop - sl[1].start
    if w >= 15 and h <= 8 and w / max(h, 1) >= 4:
        rows.append((sl[1].start + x0, sl[0].start + y0, w, h))
for r in sorted(rows):
    print('x=%d y=%d  w=%d h=%d' % r)
