import sys
import numpy as np
from PIL import Image
from scipy import ndimage
# usage: bars.py page strip x0 y0 x1 y1  -> lists components that look like bars/plus/equals
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
base = r"user\Documents\ega_scan_check_20261101\run_0IV1"
im = np.array(Image.open(rf"{base}\page_{int(page):03d}_s{strip}.png").convert("L"))[y0:y1, x0:x1]
dark = im < 140
lab, n = ndimage.label(dark)
for i, sl in enumerate(ndimage.find_objects(lab), 1):
    h = sl[0].stop - sl[0].start
    w = sl[1].stop - sl[1].start
    comp = lab[sl] == i
    # longest horizontal run in any row
    runs = []
    for row in comp:
        best = cur = 0
        for v in row:
            cur = cur + 1 if v else 0
            best = max(best, cur)
        runs.append(best)
    mr = max(runs)
    if mr >= 10 and (h <= 8 or (w >= 14 and h <= 40 and mr >= 0.8 * w)):
        print(f"x={x0+sl[1].start:5d}-{x0+sl[1].stop:5d} y={y0+sl[0].start:4d}-{y0+sl[0].stop:4d} w={w:3d} h={h:3d} maxrun={mr}")
