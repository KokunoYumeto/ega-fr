"""crop.py IMG X0 Y0 X1 Y1 OUT [SCALE]
Coordinates are in the displayed 2000-px-wide frame (multiplied by 1.24 to the 2480-px original)."""
import sys
from PIL import Image

img, x0, y0, x1, y1, out = sys.argv[1], *map(float, sys.argv[2:6]), sys.argv[6]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(img)
f = im.size[0] / 2000.0
box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((int(c.size[0] * scale), int(c.size[1] * scale)), Image.LANCZOS)
c.save(out)
print(out, c.size)
