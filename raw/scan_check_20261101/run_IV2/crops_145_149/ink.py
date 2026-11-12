"""List the connected ink components in a region of a page strip, with stroke-weight measures.

usage: python ink.py PAGE STRIP X0 Y0 X1 Y1 [THRESHOLD]
For each component (left to right): bbox (strip pixels), ink pixel count, mean horizontal and vertical run length
(a bold glyph has longer runs than a light one of the same size).
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
thr = int(sys.argv[7]) if len(sys.argv) > 7 else 128
img = np.asarray(Image.open(RUN / f"page_{page:03d}_s{strip}.png").convert("L"))[y0:y1, x0:x1]
ink = img < thr
lab, n = ndimage.label(ink)


def runs(mask, axis):
    m = mask if axis == 1 else mask.T
    lengths = []
    for row in m:
        r = 0
        for v in row:
            if v:
                r += 1
            elif r:
                lengths.append(r); r = 0
        if r:
            lengths.append(r)
    return float(np.mean(lengths)) if lengths else 0.0


out = []
for i, sl in enumerate(ndimage.find_objects(lab), start=1):
    comp = lab[sl] == i
    cnt = int(comp.sum())
    if cnt < 15:
        continue
    ys, xs = sl
    out.append((xs.start + x0, ys.start + y0, xs.stop + x0, ys.stop + y0, cnt, runs(comp, 1), runs(comp, 0)))
for b in sorted(out):
    print("bbox=(%d,%d,%d,%d) w=%d h=%d ink=%d hrun=%.2f vrun=%.2f" % (b[0], b[1], b[2], b[3], b[2] - b[0], b[3] - b[1], b[4], b[5], b[6]))
