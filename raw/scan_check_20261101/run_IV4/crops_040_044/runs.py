import sys
from PIL import Image
import numpy as np
# usage: python runs.py PAGE STRIP x0 y0 x1 y1  -> prints dark-run lengths per row (threshold 128)
RUN = r"user/Documents/ega_scan_check_20261101/run_IV4"
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
im = np.array(Image.open(f"{RUN}/page_{int(page):03d}_s{strip}.png").convert('L'))
sub = im[y0:y1, x0:x1] < 128
for r in range(sub.shape[0]):
    row = sub[r]; rl = []; c = 0
    for v in row:
        if v: c += 1
        elif c: rl.append(c); c = 0
    if c: rl.append(c)
    print(y0 + r, ''.join('#' if v else '.' for v in row), rl)
