import sys
from PIL import Image
# usage: crop.py page strip x0 y0 x1 y1 scale outname   (coords in displayed 2000-px frame)
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = [float(v) for v in sys.argv[3:7]]
scale = float(sys.argv[7]); out = sys.argv[8]
base = "user/Documents/ega_scan_check_20261101/run_IV2/"
im = Image.open(f"{base}page_{int(page):03d}_s{strip}.png")
f = im.width / 2000.0
box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(f"{base}crops_055_059/{out}.png")
print(c.size)
