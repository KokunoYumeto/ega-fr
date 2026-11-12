import sys
import numpy as np
from PIL import Image
from scipy import ndimage

# usage: cc.py page strip x0 y0 x1 y1 [thr]
# lists connected components (dark pixels) in the box: bbox (original strip coords), ink count,
# mean darkness; sorted by x
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
thr = int(sys.argv[7]) if len(sys.argv) > 7 else 128
base = r'user/Documents/ega_scan_check_20261101/run_0IV1/'
im = np.asarray(Image.open(base + 'page_%d_s%d.png' % (page, strip)).convert('L'), dtype=np.int32)
sub = im[y0:y1, x0:x1]
mask = sub < thr
lab, n = ndimage.label(mask, structure=np.ones((3, 3)))
objs = ndimage.find_objects(lab)
rows = []
for k, sl in enumerate(objs, 1):
    if sl is None:
        continue
    comp = (lab[sl] == k)
    cnt = int(comp.sum())
    if cnt < 4:
        continue
    ys, xs = sl
    dark = int((255 - sub[sl][comp]).sum())
    rows.append((xs.start + x0, ys.start + y0, xs.stop + x0, ys.stop + y0, cnt, dark))
rows.sort()
for r in rows:
    print('x %4d-%4d  y %4d-%4d  w %3d h %3d  px %4d  ink %6d' % (r[0], r[2], r[1], r[3], r[2] - r[0], r[3] - r[1], r[4], r[5]))
