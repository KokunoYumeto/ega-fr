"""Ink area of the largest connected component fully inside each display-frame box.

usage: python -I glyph_ink.py PAGE STRIP label:x0,y0,x1,y1 [...]
"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

page, strip = sys.argv[1], sys.argv[2]
im = Image.open(rf'user\Documents\ega_scan_check_20261101\run_III2\page_{page}_s{strip}.png').convert('L')
r = im.width / 2000.0
a = np.asarray(im)
for spec in sys.argv[3:]:
    label, box = spec.split(':')
    x0, y0, x1, y1 = (float(v) for v in box.split(','))
    sub = a[int(y0 * r):int(y1 * r), int(x0 * r):int(x1 * r)] < 140
    lab, n = ndimage.label(sub)
    best = None
    for i, sl in enumerate(ndimage.find_objects(lab), start=1):
        ys, xs = sl
        if ys.start == 0 or xs.start == 0 or ys.stop == sub.shape[0] or xs.stop == sub.shape[1]:
            continue  # touches the box edge: not fully inside
        area = int((lab[sl] == i).sum())
        if best is None or area > best[0]:
            best = (area, ys.stop - ys.start, xs.stop - xs.start)
    if best:
        area, h, w = best
        # mean stroke width ~ area / skeleton length; approximate skeleton length by (h + w)
        print(f'{label:12s} area={area:4d} h={h:3d} w={w:3d} area/(h+w)={area / (h + w):5.2f}')
    else:
        print(label, 'no inner component')
