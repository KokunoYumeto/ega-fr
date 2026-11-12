"""List connected components (glyphs) in a region with bbox, ink area and mean horizontal stroke width.
usage: python glyphs.py IMAGE X0 Y0 X1 Y1 [MINAREA]   (original pixel coordinates)"""
import sys

import numpy as np
from PIL import Image
from scipy import ndimage

img, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
minarea = int(sys.argv[6]) if len(sys.argv) > 6 else 30
a = np.array(Image.open(img).convert("L"))[y0:y1, x0:x1]
dark = a < 128
lab, n = ndimage.label(dark)
for i, sl in enumerate(ndimage.find_objects(lab), 1):
    m = lab[sl] == i
    area = int(m.sum())
    if area < minarea:
        continue
    runs = []
    for row in m:
        r = 0
        for v in row:
            if v:
                r += 1
            elif r:
                runs.append(r)
                r = 0
        if r:
            runs.append(r)
    vruns = []
    for col in m.T:
        r = 0
        for v in col:
            if v:
                r += 1
            elif r:
                vruns.append(r)
                r = 0
        if r:
            vruns.append(r)
    print(f"x={sl[1].start + x0} y={sl[0].start + y0} w={sl[1].stop - sl[1].start} h={sl[0].stop - sl[0].start} "
          f"area={area} hrun_med={np.median(runs):.1f} vrun_med={np.median(vruns):.1f}")
