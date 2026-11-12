import sys
from PIL import Image

# usage: crop.py page strip x0 y0 x1 y1 out [scale]
# coordinates in the ORIGINAL strip pixels
p, s, x0, y0, x1, y1, out = sys.argv[1:8]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
base = r"user\Documents\ega_scan_check_20261101\run_IV4"
im = Image.open(rf"{base}\page_{int(p):03d}_s{s}.png")
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf"{base}\crops_160_164\{out}")
print(c.size)
