import sys
import numpy as np
from PIL import Image
from scipy import ndimage
src = sys.argv[1]
im = np.array(Image.open(src).convert('L'))
bw = im < 128
lab, n = ndimage.label(bw)
objs = ndimage.find_objects(lab)
rows = []
for k, sl in enumerate(objs, 1):
    h = sl[0].stop - sl[0].start; w = sl[1].stop - sl[1].start
    if h <= 5 and 25 <= w <= 60:
        rows.append((sl[0].start, sl[1].start, w, h))
rows.sort()
# pair bars that are stacked (equals signs) vs single dashes
used = set()
for i, (y, x, w, h) in enumerate(rows):
    if i in used: continue
    partner = None
    for j, (y2, x2, w2, h2) in enumerate(rows):
        if j != i and j not in used and abs(x2 - x) <= 3 and 4 <= y2 - y <= 12:
            partner = j; break
    if partner is not None:
        used.add(partner); print(f"EQUALS x{x} y{y} w{w}")
    else:
        print(f"DASH   x{x} y{y} w{w}")
