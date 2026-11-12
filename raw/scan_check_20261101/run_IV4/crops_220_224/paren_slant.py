# usage: python paren_slant.py PAGE STRIP x0 y0 x1 y1  (display coords, 2000-px frame); the box must contain one glyph only
# prints the x-centroid of the dark pixels in the top and bottom 12% of the glyph's height, and the slant (dx/height)
import sys
from PIL import Image
import numpy as np
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(float, sys.argv[3:7])
base = r"user\Documents\ega_scan_check_20261101\run_IV4"
im = Image.open(rf"{base}\page_{page}_s{strip}.png").convert("L")
f = im.width / 2000.0
box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
a = np.array(im.crop(box)) < 128
ys, xs = np.nonzero(a)
if len(ys) == 0:
    print("no ink"); sys.exit()
top, bot = ys.min(), ys.max()
h = bot - top + 1
band = max(2, int(0.12 * h))
tx = xs[ys < top + band].mean()
bx = xs[ys > bot - band].mean()
print(f"box={box} height={h}px top_x={tx:.1f} bottom_x={bx:.1f} slant={(tx-bx)/h:.3f}")
