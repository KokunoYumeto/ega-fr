"""crop.py PAGE STRIP NAME x0 y0 x1 y1 [scale]
Coordinates in the displayed (2000 px wide) frame of the strip; converted to original pixels here."""
import sys
from PIL import Image

base = r"user\Documents\ega_scan_check_20261101\run_IV3"
page, strip, name = sys.argv[1], sys.argv[2], sys.argv[3]
x0, y0, x1, y1 = (float(v) for v in sys.argv[4:8])
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(rf"{base}\page_{int(page):03d}_s{strip}.png")
f = im.width / 2000.0
box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
out = rf"{base}\crops_090_094\{name}.png"
c.save(out)
print(out, box, c.size)
