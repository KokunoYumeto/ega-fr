import sys
import numpy as np
from PIL import Image
from scipy import ndimage
# usage: measure.py src x0 y0 x1 y1  -> components (area, bbox) in crop at native resolution
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
im = np.array(Image.open(src).convert('L').crop((x0, y0, x1, y1)))
b = im < 128
lab, n = ndimage.label(b)
objs = ndimage.find_objects(lab)
res = []
for i, sl in enumerate(objs):
    area = int((lab[sl] == i+1).sum())
    if area < 15: continue
    h = sl[0].stop - sl[0].start; w = sl[1].stop - sl[1].start
    # stroke width estimate: 2*mean of distance transform over skeleton approx -> use max of EDT
    comp = (lab == i+1)
    edt = ndimage.distance_transform_edt(comp)
    res.append((sl[1].start + x0, sl[0].start + y0, w, h, area, round(float(edt.max()), 2), round(float(edt[edt > 0].mean()), 2)))
for r in sorted(res):
    print('x=%d y=%d w=%d h=%d area=%d edtmax=%s edtmean=%s' % r)
