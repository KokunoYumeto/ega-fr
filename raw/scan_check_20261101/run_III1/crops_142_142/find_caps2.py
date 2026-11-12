import pathlib
import numpy as np
from PIL import Image
from scipy import ndimage
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
im = np.array(Image.open(run / "page_142_s4.png").convert("L"))
y0, y1, x0, x1 = 95, 165, 995, 1130
a = im[y0:y1, x0:x1] < 140
lab, n = ndimage.label(a)
for i, sl in enumerate(ndimage.find_objects(lab), 1):
    g = lab[sl] == i
    h, w = g.shape
    if g.sum() > 40:
        rows = g.sum(axis=1)
        print("x%d y%d w%d h%d ink %d midrow %.1f" % (x0 + sl[1].start, y0 + sl[0].start, w, h, int(g.sum()), float(np.median(rows[h // 3: 2 * h // 3]))))
