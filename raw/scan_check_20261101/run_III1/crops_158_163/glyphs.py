import sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
# usage: glyphs.py src x0 y0 x1 y1 [thr]
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 128
a = np.asarray(Image.open(src).convert('L').crop((x0, y0, x1, y1)))
b = a < thr
lab, n = ndi.label(b)
dt = ndi.distance_transform_edt(b)
objs = ndi.find_objects(lab)
rows = []
for i, sl in enumerate(objs, 1):
    m = lab[sl] == i
    area = int(m.sum())
    if area < 15:
        continue
    h = sl[0].stop - sl[0].start
    w = sl[1].stop - sl[1].start
    d = dt[sl][m]
    # stroke width estimate: 2*median of local maxima of distance transform
    mx = ndi.maximum_filter(dt[sl], size=3)
    ridge = (dt[sl] == mx) & m & (dt[sl] > 0.9)
    sw = 2 * np.median(dt[sl][ridge]) if ridge.any() else 0
    sw90 = 2 * np.percentile(dt[sl][ridge], 90) if ridge.any() else 0
    rows.append((sl[1].start + x0, sl[0].start + y0, w, h, area, round(area / (w * h), 3), round(float(sw), 2), round(float(sw90), 2)))
rows.sort()
print('x y w h area fill sw_med sw_p90')
for r in rows:
    print(*r)
