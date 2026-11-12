import sys
from PIL import Image, ImageOps
# usage: enhance.py page strip x0 y0 x1 y1 scale outname  (coords in ORIGINAL pixels); strong contrast to reveal faint type
page, strip, x0, y0, x1, y1, scale, out = sys.argv[1:9]
base = r"user\Documents\ega_scan_check_20261101\run_IV3"
im = Image.open(rf"{base}\page_{int(page):03d}_s{strip}.png").convert("L")
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
# map anything darker than 245 to black-ish to show faint marks
c = c.point(lambda v: 0 if v < 200 else (90 if v < 240 else (180 if v < 252 else 255)))
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.NEAREST)
c.save(rf"{base}\crops_110_114\{out}.png")
print(c.size)
