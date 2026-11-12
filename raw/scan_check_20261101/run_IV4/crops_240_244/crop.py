import sys
from PIL import Image
# usage: crop.py page strip x0 y0 x1 y1 out [scale]   (coords in ORIGINAL pixels)
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
out = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
base = "user/Documents/ega_scan_check_20261101/run_IV4"
im = Image.open(f"{base}/page_{page}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
if scale != 1.0:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(f"{base}/crops_240_244/{out}")
print(im.size, c.size)
