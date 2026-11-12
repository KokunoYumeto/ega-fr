"""Segment a text line into words by column gaps and report stem-width statistics per word.

Usage: python words.py PAGE STRIP X0 X1 Y0 Y1 [GAP] [THRESH]
Y0..Y1 should be the x-height band of the line.
For each word: x-range, median and mean horizontal dark-run width (runs 2..9 px),
and dark pixels per column (ink density).
"""
import statistics
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
RUN = r"user\Documents\ega_scan_check_20261101\run_IV3"
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, x1, y0, y1 = (int(v) for v in sys.argv[3:7])
gap = int(sys.argv[7]) if len(sys.argv) > 7 else 12
thr = int(sys.argv[8]) if len(sys.argv) > 8 else 128
im = Image.open(RUN + r"\page_%03d_s%d.png" % (page, strip)).convert('L')
px = im.load()
cols = [sum(1 for y in range(y0, y1) if px[x, y] < thr) for x in range(x0, x1)]
words = []
start = None
blank = 0
for i, c in enumerate(cols):
    if c > 0:
        if start is None:
            start = i
        blank = 0
        end = i
    else:
        if start is not None:
            blank += 1
            if blank >= gap:
                words.append((start, end))
                start = None
if start is not None:
    words.append((start, end))
for s, e in words:
    rs = []
    dark = 0
    for y in range(y0, y1):
        x = x0 + s
        while x <= x0 + e:
            if px[x, y] < thr:
                b = x
                while x <= x0 + e and px[x, y] < thr:
                    x += 1
                if 2 <= x - b <= 9:
                    rs.append(x - b)
                dark += x - b
            else:
                x += 1
    w = e - s + 1
    if rs:
        print('x %4d-%4d w %3d median %.1f mean %.2f n %3d density %.2f' % (
            x0 + s, x0 + e, w, statistics.median(rs), statistics.mean(rs), len(rs), dark / w))
