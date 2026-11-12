"""Segment one text line into words and report stroke widths in a horizontal band.

usage: python words.py PAGE STRIP y_top y_bottom band_top band_bottom [x_min x_max]
Prints, for each word (gap >= 12 px), its x-range and the mean/median length of the dark runs
inside the band (stroke width at mid x-height).
"""
import sys
from PIL import Image
import numpy as np

RUN = r"user/Documents/ega_scan_check_20261101/run_IV4"
page, strip = int(sys.argv[1]), int(sys.argv[2])
yt, yb, bt, bb = (int(v) for v in sys.argv[3:7])
xmin = int(sys.argv[7]) if len(sys.argv) > 7 else 300
xmax = int(sys.argv[8]) if len(sys.argv) > 8 else 2300
im = np.array(Image.open(RUN + "/page_%03d_s%d.png" % (page, strip)).convert("L"))
dark = im < 128
line = dark[yt:yb, :]
cols = line.any(axis=0)
words = []
x = xmin
while x < xmax:
    if cols[x]:
        x0 = x
        gap = 0
        while x < xmax and gap < 12:
            if cols[x]:
                gap = 0
            else:
                gap += 1
            x += 1
        words.append((x0, x - gap))
    x += 1
for x0, x1 in words:
    band = dark[bt:bb, x0:x1]
    runs = []
    for row in band:
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
    print("x %4d-%4d  w=%3d  runs=%3d  mean=%.2f  median=%.1f" % (
        x0, x1, x1 - x0, len(runs), runs.mean(), np.median(runs)))
