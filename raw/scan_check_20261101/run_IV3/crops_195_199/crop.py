import sys
from PIL import Image
# usage: crop.py strip.png x0 y0 x1 y1 scale out.png   (coords in original pixels)
src, x0, y0, x1, y1, sc, out = sys.argv[1], *map(int, sys.argv[2:6]), float(sys.argv[6]), sys.argv[7]
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width*sc), int(c.height*sc)), Image.LANCZOS)
c.save(out)
print(out, c.size)
