# usage: python crop.py PAGE STRIP x0 y0 x1 y1 OUTNAME [scale]
# coordinates are in the 2000-px-wide display frame of the strip; converted to original pixels
import sys
from PIL import Image
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(float, sys.argv[3:7])
out = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 3.0
base = r"user\Documents\ega_scan_check_20261101\run_IV4"
im = Image.open(rf"{base}\page_{page}_s{strip}.png")
f = im.width / 2000.0
box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf"{base}\crops_220_224\{out}.png")
print(out, box, c.size)
