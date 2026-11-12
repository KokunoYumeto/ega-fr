"""Like heavy_scan.py but with a lower threshold and grouping of adjacent flagged glyphs into runs.
usage: python heavy_scan2.py factor page_NNN_sK.png [...]"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

factor = float(sys.argv[1])
for fn in sys.argv[2:]:
    img = np.array(Image.open(fn).convert("L"))
    dark = img < 128
    lab, n = ndimage.label(dark)
    objs = ndimage.find_objects(lab)
    rows = []
    for i, sl in enumerate(objs, start=1):
        if sl is None:
            continue
        h = sl[0].stop - sl[0].start
        w = sl[1].stop - sl[1].start
        if not (16 <= h <= 40 and 8 <= w <= 45):
            continue
        comp = lab[sl] == i
        area = comp.sum()
        er = ndimage.binary_erosion(comp)
        b = area - er.sum()
        sw = 2 * area / max(b, 1)
        rows.append((sl[1].start, sl[0].start, w, h, area, sw))
    if not rows:
        continue
    arr = np.array(rows, dtype=float)
    med = np.median(arr[:, 5])
    flagged = []
    for r in rows:
        x, y, w, h, area, sw = r
        band = arr[(np.abs(arr[:, 0] - x) < 250) & (np.abs(arr[:, 1] - y) < 25)]
        lmed = np.median(band[:, 5]) if len(band) > 5 else med
        if sw > factor * lmed:
            flagged.append((int(x), int(y), int(w), int(h), int(area), round(sw, 2), round(lmed, 2)))
    flagged.sort(key=lambda t: (t[1] // 30, t[0]))
    print(fn, "median %.2f, %d flagged" % (med, len(flagged)))
    for f in flagged:
        print("   ", f)
