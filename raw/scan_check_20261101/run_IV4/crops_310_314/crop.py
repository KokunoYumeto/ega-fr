import sys
from PIL import Image
# usage: crop.py page strip x0 y0 x1 y1 (display coords) name [upscale]
run = r"user/Documents/ega_scan_check_20261101/run_IV4"
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(float, sys.argv[3:7])
name = sys.argv[7]
up = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(f"{run}/page_{page}_s{strip}.png")
f = im.width / 2000.0
box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((int(c.width * up), int(c.height * up)), Image.LANCZOS)
out = f"{run}/crops_310_314/{name}.png"
c.save(out)
print(out, box, c.size)
