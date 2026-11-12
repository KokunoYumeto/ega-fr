"""bars.py PAGE STRIP x0 y0 x1 y1  (displayed 2000-px frame): list thin horizontal bars (dash, minus, = strokes)
with their width/height in original 300-dpi pixels, left to right."""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

base = r"user\Documents\ega_scan_check_20261101\run_IV3"
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
im = Image.open(rf"{base}\page_{int(page):03d}_s{strip}.png").convert("L")
f = im.width / 2000.0
box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
a = np.array(im.crop(box)) < 128
lab, n = ndimage.label(a)
out = []
for i, sl in enumerate(ndimage.find_objects(lab), 1):
    h = sl[0].stop - sl[0].start
    w = sl[1].stop - sl[1].start
    if w >= 12 and h <= 9 and w >= 2.5 * h:
        out.append((sl[1].start + box[0], sl[0].start + box[1], w, h))
for x, y, w, h in sorted(out):
    print(f"x={x} y={y} w={w} h={h}")
