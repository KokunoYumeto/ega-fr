"""Flag glyphs whose stroke width is well above the local norm (candidate wrong-fount letters).
usage: python heavy_scan.py page_NNN_s1.png [...]
For each strip: connected components of x-height-ish size; stroke ~ 2*area/boundary; report components whose stroke
exceeds the median of components of similar height in the same strip by a factor; also the strip's per-column-band
median, to separate an inking band from an isolated glyph."""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

for fn in sys.argv[1:]:
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
    # local median in 300-px column bands
    flagged = []
    for r in rows:
        x, y, w, h, area, sw = r
        band = arr[(np.abs(arr[:, 0] - x) < 250) & (np.abs(arr[:, 1] - y) < 120)]
        lmed = np.median(band[:, 5]) if len(band) > 5 else med
        if sw > 1.25 * lmed and sw > 1.2 * med:
            flagged.append((int(x), int(y), int(w), int(h), int(area), round(sw, 2), round(lmed, 2)))
    print(fn, "median stroke %.2f, %d glyphs, %d flagged" % (med, len(rows), len(flagged)))
    for f in flagged:
        print("   ", f)
