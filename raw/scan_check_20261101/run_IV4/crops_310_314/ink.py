import sys
from PIL import Image
import numpy as np
run = r"user/Documents/ega_scan_check_20261101/run_IV4"
# args: page strip then groups of label x0 y0 x1 y1 (display coords of a 2000-wide frame)
page, strip = sys.argv[1], sys.argv[2]
im = np.array(Image.open(f"{run}/page_{page}_s{strip}.png").convert("L")).astype(float)
f = im.shape[1] / 2000.0
a = sys.argv[3:]
for i in range(0, len(a), 5):
    lab = a[i]; x0, y0, x1, y1 = [int(round(float(v) * f)) for v in a[i+1:i+5]]
    c = im[y0:y1, x0:x1]
    dark = c < 128
    ys, xs = np.nonzero(dark)
    if len(ys) == 0:
        print(lab, 'no ink'); continue
    by0, by1, bx0, bx1 = ys.min(), ys.max(), xs.min(), xs.max()
    h = by1 - by0 + 1; w = bx1 - bx0 + 1
    # horizontal run lengths per row (max run) in the middle 60% of rows
    runs = []
    for r in range(by0 + int(0.2*h), by1 - int(0.2*h) + 1):
        row = dark[r, bx0:bx1+1]; best = cur = 0
        for v in row:
            cur = cur + 1 if v else 0; best = max(best, cur)
        runs.append(best)
    # vertical run lengths per column (max run) in the middle 60% of columns
    vr = []
    for col in range(bx0 + int(0.2*w), bx1 - int(0.2*w) + 1):
        colv = dark[by0:by1+1, col]; best = cur = 0
        for v in colv:
            cur = cur + 1 if v else 0; best = max(best, cur)
        vr.append(best)
    print(f"{lab}: box h={h} w={w} ink={dark.sum()} ink/(h*h)={dark.sum()/(h*h):.3f} medHrun={np.median(runs):.1f} medVrun={np.median(vr):.1f}")
