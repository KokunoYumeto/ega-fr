import sys
from PIL import Image
# usage: crop.py page strip x0 y0 x1 y1 scale outname   (coords in ORIGINAL strip pixels)
page, strip, x0, y0, x1, y1, scale, out = sys.argv[1:9]
d = r"user/Documents/ega_scan_check_20261101/run_IVback/"
im = Image.open(d + f"page_{page}_s{strip}.png")
x0, y0, x1, y1 = map(int, (x0, y0, x1, y1))
c = im.crop((x0, y0, x1, y1))
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
c.save(d + "crops_333_337/" + out)
print(c.size)
