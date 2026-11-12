import sys
from PIL import Image
import numpy as np
from scipy import ndimage
run = r"user/Documents/ega_scan_check_20261101/run_IV4"
# args: page strip x0 y0 x1 y1 (display coords, 2000-wide); prints connected components (orig px)
page, strip = sys.argv[1], sys.argv[2]
im = np.array(Image.open(f"{run}/page_{page}_s{strip}.png").convert("L")).astype(float)
f = im.shape[1] / 2000.0
x0, y0, x1, y1 = [int(round(float(v) * f)) for v in sys.argv[3:7]]
c = im[y0:y1, x0:x1]
dark = c < 140
lab, n = ndimage.label(dark)
objs = ndimage.find_objects(lab)
rows = []
for i, sl in enumerate(objs):
    ys, xs = sl
    h = ys.stop - ys.start; w = xs.stop - xs.start
    ink = int((lab[sl] == i + 1).sum())
    if ink < 15: continue
    # stroke thickness estimate: ink / skeleton length approx via distance transform
    m = (lab[sl] == i + 1)
    dt = ndimage.distance_transform_edt(m)
    thick = 2 * dt[m].mean()
    rows.append((xs.start + x0, ys.start + y0, w, h, ink, thick))
for r in sorted(rows):
    print("x=%d y=%d w=%d h=%d ink=%d meanthick=%.2f" % r)
