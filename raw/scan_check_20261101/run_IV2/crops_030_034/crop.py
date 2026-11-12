import sys
from PIL import Image
# usage: crop.py page strip x0 y0 x1 y1 outname [scale]
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
out = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
base = r"user/Documents/ega_scan_check_20261101/run_IV2/"
im = Image.open(base + f"page_{int(page):03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(base + "crops_030_034/" + out)
print(im.size, c.size)
