"""Crop a region of a strip image and enlarge it.
usage: python crop.py IN.png x0 y0 x1 y1 OUT.png [ZOOM]
Coordinates are in the displayed 2000-px-wide frame; they are scaled to the original width."""
import sys

from PIL import Image

src, x0, y0, x1, y1, out = sys.argv[1], *map(float, sys.argv[2:6]), sys.argv[6]
zoom = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(src)
s = im.size[0] / 2000.0
box = tuple(int(round(v * s)) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((int(c.size[0] * zoom), int(c.size[1] * zoom)), Image.LANCZOS)
c.save(out)
print(out, box, c.size)
