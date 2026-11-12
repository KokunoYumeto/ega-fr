import sys
import numpy as np
from PIL import Image
from scipy import ndimage
from skimage.morphology import skeletonize

# usage: strokew.py page strip y0 y1 x0 x1 [thr]
# prints connected components (glyphs) in the band with their bbox and mean stroke width
page, strip = sys.argv[1], sys.argv[2]
y0, y1, x0, x1 = map(int, sys.argv[3:7])
thr = int(sys.argv[7]) if len(sys.argv) > 7 else 140
base = r'user/Documents/ega_scan_check_20261101/run_IV2/'
im = np.array(Image.open(base + 'page_%s_s%s.png' % (page, strip)))
a = im[y0:y1, x0:x1] < thr
lab, n = ndimage.label(a)
dist = ndimage.distance_transform_edt(a)
sk = skeletonize(a)
objs = ndimage.find_objects(lab)
rows = []
for i, sl in enumerate(objs):
    m = lab[sl] == i + 1
    area = m.sum()
    if area < 30:
        continue
    s = sk[sl] & m
    d = dist[sl][s]
    w = 2 * d.mean() if len(d) else 0
    rows.append((sl[1].start + x0, sl[0].start + y0, sl[1].stop - sl[1].start, sl[0].stop - sl[0].start, area, round(w, 2)))
rows.sort()
for r in rows:
    print('x=%d y=%d w=%d h=%d area=%d stroke=%.2f' % r)
