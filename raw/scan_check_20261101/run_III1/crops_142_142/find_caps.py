import pathlib
import numpy as np
from PIL import Image
from scipy import ndimage
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
def tall(s, y0, y1, x0=0, x1=None):
    im = np.array(Image.open(run / f"page_142_s{s}.png").convert("L"))
    a = im[y0:y1, x0:x1] < 140
    lab, n = ndimage.label(a)
    out = []
    for i, sl in enumerate(ndimage.find_objects(lab), 1):
        g = lab[sl] == i
        h, w = g.shape
        if 27 <= h <= 36 and w <= 26:
            rows = g.sum(axis=1)
            out.append((x0 + sl[1].start, y0 + sl[0].start, w, h, int(g.sum()), float(np.median(rows[h // 3: 2 * h // 3]))))
    return sorted(out)
for label, args in [("strip4 line '(II, 6.1.1 et I, 4.2.4)'", (4, 95, 165)),
                    ("strip4 line '(II, 5.4.3)'", (4, 265, 335)),
                    ("strip2 line '(II, 4.2.7)'", (2, 770, 840)),
                    ("strip1 line 'chap. VIII'", (1, 600, 670))]:
    print(label)
    for r in tall(*args):
        print("   x%d y%d w%d h%d ink %d stem %.1f" % r)
