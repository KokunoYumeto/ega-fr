import sys
import numpy as np
from PIL import Image
# usage: stroke.py page strip x0 y0 x1 y1 [threshold]
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
thr = int(sys.argv[7]) if len(sys.argv) > 7 else 128
base = r"user/Documents/ega_scan_check_20261101/run_IV4"
im = Image.open(f"{base}/page_{page:03d}_s{strip}.png").convert('L')
a = np.array(im.crop((x0, y0, x1, y1))) < thr
runs = []
for row in a:
    r = 0
    for v in row:
        if v: r += 1
        elif r: runs.append(r); r = 0
    if r: runs.append(r)
runs = np.array(runs)
print('dark px', a.sum(), 'h-runs', len(runs), 'median run', np.median(runs) if len(runs) else 0, 'mean run', runs.mean() if len(runs) else 0, 'p90', np.percentile(runs,90) if len(runs) else 0)
