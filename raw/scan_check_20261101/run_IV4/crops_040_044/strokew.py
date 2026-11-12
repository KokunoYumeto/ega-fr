import sys
import numpy as np
from PIL import Image
from scipy import ndimage
from skimage.morphology import skeletonize

# Mean stroke width (2 x distance-to-background along the skeleton) of a box.
# usage: python strokew.py PAGE STRIP x0 y0 x1 y1 LABEL [PAGE STRIP x0 y0 x1 y1 LABEL ...]
RUN = r"user/Documents/ega_scan_check_20261101/run_IV4"
args = sys.argv[1:]
for i in range(0, len(args), 7):
    page, strip = int(args[i]), int(args[i + 1])
    x0, y0, x1, y1 = map(int, args[i + 2:i + 6])
    label = args[i + 6]
    im = np.array(Image.open(f"{RUN}/page_{page:03d}_s{strip}.png").convert('L'))
    b = im[y0:y1, x0:x1] < 140
    dt = ndimage.distance_transform_edt(b)
    sk = skeletonize(b)
    vals = dt[sk]
    if vals.size == 0:
        print(label, 'empty')
        continue
    print(f"{label:28s} mean={2*vals.mean():.2f} median={2*np.median(vals):.2f} n={vals.size}")
