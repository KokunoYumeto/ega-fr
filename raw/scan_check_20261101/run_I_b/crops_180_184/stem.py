import sys
import numpy as np
from PIL import Image
# usage: stem.py src x0 y0 x1 y1 : prints dark-run widths per row (threshold 128) in the box
src = sys.argv[1]; x0, y0, x1, y1 = map(int, sys.argv[2:6])
a = np.array(Image.open(src).convert('L').crop((x0, y0, x1, y1)))
d = a < 128
for r in range(d.shape[0]):
    row = d[r]; runs = []; c = 0; start = None
    for i, v in enumerate(row):
        if v:
            if c == 0: start = i
            c += 1
        elif c:
            runs.append((start, c)); c = 0
    if c: runs.append((start, c))
    print(r + y0, runs)
