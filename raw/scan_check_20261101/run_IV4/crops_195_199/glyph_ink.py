"""Ink measure of single glyphs: connected components (dark pixels) inside given boxes of a strip image.
usage: python glyph_ink.py IMAGE x0 y0 x1 y1 [x0 y0 x1 y1 ...]
Prints, for each box, the components with their bbox, pixel count and mean stroke estimate (area / skeleton-ish length)."""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

img = np.array(Image.open(sys.argv[1]).convert("L"))
vals = list(map(int, sys.argv[2:]))
for k in range(0, len(vals), 4):
    x0, y0, x1, y1 = vals[k:k + 4]
    sub = img[y0:y1, x0:x1] < 128
    lab, n = ndimage.label(sub)
    print("box", (x0, y0, x1, y1))
    for i in range(1, n + 1):
        ys, xs = np.where(lab == i)
        if len(ys) < 15:
            continue
        h = ys.max() - ys.min() + 1
        w = xs.max() - xs.min() + 1
        # stroke width estimate: area / (number of boundary pixels / 2)
        comp = lab == i
        er = ndimage.binary_erosion(comp)
        boundary = comp.sum() - er.sum()
        sw = 2 * comp.sum() / max(boundary, 1)
        print("  comp bbox x%d-%d y%d-%d  w=%d h=%d area=%d  stroke~%.2f" % (xs.min() + x0, xs.max() + x0, ys.min() + y0, ys.max() + y0, w, h, comp.sum(), sw))
