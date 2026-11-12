import sys
from PIL import Image
# usage: crop.py page strip x0 y0 x1 y1 scale outname   (coords in ORIGINAL pixels)
page, strip, x0, y0, x1, y1, scale, out = sys.argv[1:9]
base = r"user\Documents\ega_scan_check_20261101\run_IV3"
im = Image.open(rf"{base}\page_{int(page):03d}_s{strip}.png")
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
s = float(scale)
c = c.resize((int(c.width*s), int(c.height*s)), Image.LANCZOS)
c.save(rf"{base}\crops_110_114\{out}.png")
print(c.size)
