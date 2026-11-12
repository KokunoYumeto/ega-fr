"""Print connected components in a box: bbox, size; to compare dot height with baseline and arrow shaft.
usage: python dots.py PAGE STRIP x0 y0 x1 y1"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

d = r"user\Documents\ega_scan_check_20261101\run_IV2"
p, s, x0, y0, x1, y1 = sys.argv[1:7]
x0, y0, x1, y1 = map(int, (x0, y0, x1, y1))
a = np.array(Image.open(rf"{d}\page_{int(p):03d}_s{s}.png").convert("L"))[y0:y1, x0:x1] < 128
lab, n = ndimage.label(a)
for i, sl in enumerate(ndimage.find_objects(lab)):
    h = sl[0].stop - sl[0].start
    w = sl[1].stop - sl[1].start
    if h * w < 20:
        continue
    print(f"x={sl[1].start + x0:4d}-{sl[1].stop + x0:4d} y={sl[0].start + y0:4d}-{sl[0].stop + y0:4d} w={w:3d} h={h:3d}")
