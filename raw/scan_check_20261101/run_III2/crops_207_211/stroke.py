"""Mean horizontal/vertical dark-run length (stroke thickness proxy) in display-frame boxes of a strip.

usage: python -I stroke.py PAGE STRIP label:x0,y0,x1,y1 [label:...]
"""
import sys
import numpy as np
from PIL import Image

page, strip = sys.argv[1], sys.argv[2]
im = Image.open(rf'user\Documents\ega_scan_check_20261101\run_III2\page_{page}_s{strip}.png').convert('L')
r = im.width / 2000.0
a = np.asarray(im)


def runs(mask):
    out = []
    for row in mask:
        n = 0
        for v in row:
            if v:
                n += 1
            elif n:
                out.append(n)
                n = 0
        if n:
            out.append(n)
    return out


for spec in sys.argv[3:]:
    label, box = spec.split(':')
    x0, y0, x1, y1 = (float(v) for v in box.split(','))
    sub = a[int(y0 * r):int(y1 * r), int(x0 * r):int(x1 * r)]
    m = sub < 128
    h = runs(m)
    v = runs(m.T)
    ink = m.mean()
    print(f'{label:14s} hmean={np.mean(h):5.2f} hmed={np.median(h):4.1f} vmed={np.median(v):4.1f} ink={ink:.3f} nruns={len(h)}')
