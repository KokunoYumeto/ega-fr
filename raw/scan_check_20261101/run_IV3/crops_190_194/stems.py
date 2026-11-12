"""Measure dark horizontal run widths (stem widths) in a box, row by row.

Usage: python stems.py PAGE STRIP X0 X1 Y0 Y1 [THRESH]
For each row prints the list of dark run lengths; then the median run length
over all rows (runs of length 2..20 only), and the dark-pixel count of the box.
"""
import statistics
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
RUN = r"user\Documents\ega_scan_check_20261101\run_IV3"
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, x1, y0, y1 = (int(v) for v in sys.argv[3:7])
thr = int(sys.argv[7]) if len(sys.argv) > 7 else 128
im = Image.open(RUN + r"\page_%03d_s%d.png" % (page, strip)).convert('L')
px = im.load()
allruns = []
dark = 0
for y in range(y0, y1):
    runs = []
    x = x0
    while x < x1:
        if px[x, y] < thr:
            s = x
            while x < x1 and px[x, y] < thr:
                x += 1
            runs.append(x - s)
        else:
            x += 1
    dark += sum(runs)
    allruns += [r for r in runs if 2 <= r <= 20]
    print(y, runs)
print('median run', statistics.median(allruns) if allruns else None,
      'mean', round(statistics.mean(allruns), 2) if allruns else None,
      'dark px', dark)
