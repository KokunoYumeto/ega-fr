"""List connected dark components in a region of a strip image.

usage: glyphs.py IMAGE x0 y0 x1 y1 [min_px]
Prints, for each component (sorted left to right): bbox (absolute coords),
width x height, dark-pixel count, mean horizontal run length and mean
vertical run length (stroke-weight proxies).
"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

img = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
min_px = int(sys.argv[6]) if len(sys.argv) > 6 else 40

a = np.asarray(Image.open(img).convert("L"))[y0:y1, x0:x1]
dark = a < 128
lab, n = ndimage.label(dark, structure=np.ones((3, 3)))
objs = ndimage.find_objects(lab)
rows = []
for i, sl in enumerate(objs, start=1):
    m = lab[sl] == i
    cnt = int(m.sum())
    if cnt < min_px:
        continue
    # horizontal runs
    hr = []
    for r in m:
        run = 0
        for v in r:
            if v:
                run += 1
            elif run:
                hr.append(run); run = 0
        if run:
            hr.append(run)
    vr = []
    for c in m.T:
        run = 0
        for v in c:
            if v:
                run += 1
            elif run:
                vr.append(run); run = 0
        if run:
            vr.append(run)
    ys, xs = sl
    rows.append((xs.start + x0, ys.start + y0, xs.stop + x0, ys.stop + y0,
                 xs.stop - xs.start, ys.stop - ys.start, cnt,
                 sum(hr) / len(hr), sum(vr) / len(vr)))
rows.sort()
for r in rows:
    print("bbox=(%d,%d,%d,%d) %dx%d px=%d hrun=%.2f vrun=%.2f" % r)
