"""stems.py IMG x0 y0 x1 y1: print dark-run widths (threshold 128) on every row of the box, then the median width of
runs per row; used to compare stroke weights of letters."""
import sys
from statistics import median
from PIL import Image
im = Image.open(sys.argv[1]).convert("L")
x0, y0, x1, y1 = map(int, sys.argv[2:6])
widths = []
for y in range(y0, y1):
    runs, run = [], 0
    for x in range(x0, x1):
        if im.getpixel((x, y)) < 128:
            run += 1
        elif run:
            runs.append(run); run = 0
    if run:
        runs.append(run)
    if runs:
        widths.extend(runs)
print("median run", median(widths) if widths else None, "n", len(widths))
