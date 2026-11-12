import sys
from PIL import Image
# usage: crop.py page strip x0 y0 x1 y1 outname [scale]
# coordinates in ORIGINAL strip pixels
d = r"user/Documents/ega_scan_check_20261101/run_0IV1"
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
out = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(f"{d}/page_{page}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width*scale), int(c.height*scale)), Image.LANCZOS)
c.save(f"{d}/crops_176_180/{out}.png")
print(im.size, c.size)
