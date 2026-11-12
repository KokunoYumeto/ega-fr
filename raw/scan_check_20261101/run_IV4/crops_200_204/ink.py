"""Ink statistics of word boxes: dark-pixel count and mean horizontal stroke width.

usage: python ink.py PAGE STRIP x0 y0 x1 y1 [x0 y0 x1 y1 ...]
"""
import sys
from PIL import Image
import numpy as np

RUN = r"user/Documents/ega_scan_check_20261101/run_IV4"
page, strip = int(sys.argv[1]), int(sys.argv[2])
im = np.array(Image.open(RUN + "/page_%03d_s%d.png" % (page, strip)).convert("L"))
vals = [int(v) for v in sys.argv[3:]]
for k in range(0, len(vals), 4):
    x0, y0, x1, y1 = vals[k:k + 4]
    box = im[y0:y1, x0:x1] < 128
    runs = []
    for row in box:
        r = 0
        for v in row:
            if v:
                r += 1
            elif r:
                runs.append(r)
                r = 0
        if r:
            runs.append(r)
    runs = np.array(runs) if runs else np.array([0])
    print("box %4d %4d %4d %4d dark=%5d median_run=%.1f mean_run=%.2f" % (
        x0, y0, x1, y1, box.sum(), np.median(runs), runs.mean()))
