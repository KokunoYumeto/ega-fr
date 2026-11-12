import pathlib
import numpy as np
from PIL import Image
from scipy import ndimage
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
def comps(s, box):
    a = np.array(Image.open(run / f"page_142_s{s}.png").convert("L").crop(box)) < 140
    lab, n = ndimage.label(a)
    res = []
    for i, sl in enumerate(ndimage.find_objects(lab), 1):
        g = lab[sl] == i
        if g.sum() < 30:
            continue
        rows = g.sum(axis=1)  # ink per row: the stem width in the middle rows of an I
        h = g.shape[0]
        mid = rows[h // 3: 2 * h // 3]
        res.append((box[0] + sl[1].start, box[1] + sl[0].start, sl[1].stop - sl[1].start, h, int(g.sum()), float(np.median(mid))))
    return sorted(res)
print("(II, 5.4.3) region")
for r in comps(4, (1795, 270, 1875, 330)): print("  x%d y%d w%d h%d ink %d stem(mid rows) %.1f" % r)
print("(II, 6.1.1 region")
for r in comps(4, (755, 95, 840, 160)): print("  x%d y%d w%d h%d ink %d stem(mid rows) %.1f" % r)
print("et I, 4.2.4 region")
for r in comps(4, (1240, 95, 1300, 160)): print("  x%d y%d w%d h%d ink %d stem(mid rows) %.1f" % r)
print("(II, 4.2.7) region")
for r in comps(2, (1925, 770, 2010, 835)): print("  x%d y%d w%d h%d ink %d stem(mid rows) %.1f" % r)
print("roman VIII region")
for r in comps(1, (900, 605, 1010, 665)): print("  x%d y%d w%d h%d ink %d stem(mid rows) %.1f" % r)
