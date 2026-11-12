"""Print the x of the first dark pixel of each text line in a strip.

usage: python linestarts.py PAGE STRIP
"""
import sys
from PIL import Image
import numpy as np

RUN = r"user/Documents/ega_scan_check_20261101/run_IV4"
page, strip = int(sys.argv[1]), int(sys.argv[2])
im = np.array(Image.open(RUN + "/page_%03d_s%d.png" % (page, strip)).convert("L"))
dark = im < 128
rows = dark[:, 200:].sum(axis=1)
inline = rows > 3
lines = []
y = 0
H = len(inline)
while y < H:
    if inline[y]:
        y0 = y
        while y < H and inline[y]:
            y += 1
        if y - y0 >= 8:
            lines.append((y0, y))
    y += 1
for y0, y1 in lines:
    cols = dark[y0:y1, :].any(axis=0)
    xs = np.nonzero(cols)[0]
    xs = xs[xs > 150]
    if len(xs):
        print("y %4d-%4d  x_first %4d  x_last %4d" % (y0, y1, xs[0], xs[-1]))
