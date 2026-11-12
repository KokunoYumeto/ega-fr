"""List thin horizontal bars (minus signs, dashes, = bars) in a region of a strip image.
usage: python bars.py IMAGE X0 Y0 X1 Y1   (original pixel coordinates)
Prints each bar-like connected component: x0, y0, width, height."""
import sys

import numpy as np
from PIL import Image
from scipy import ndimage

img, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
a = np.array(Image.open(img).convert("L"))[y0:y1, x0:x1]
dark = a < 128
lab, n = ndimage.label(dark)
for i, sl in enumerate(ndimage.find_objects(lab), 1):
    h = sl[0].stop - sl[0].start
    w = sl[1].stop - sl[1].start
    if h <= 9 and w >= 12:
        print(f"bar x={sl[1].start + x0} y={sl[0].start + y0} w={w} h={h}")
