import sys
from PIL import Image

# usage: crop.py <strip png> <x0> <y0> <x1> <y1> <out png> [scale]
# coordinates are in ORIGINAL image pixels
src, x0, y0, x1, y1, out = sys.argv[1:7]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(src)
box = tuple(int(v) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(out, c.size)
