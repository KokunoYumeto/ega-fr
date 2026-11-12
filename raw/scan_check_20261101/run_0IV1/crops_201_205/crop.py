import sys
from PIL import Image
# usage: crop.py src.png out.png x0 y0 x1 y1 scale   (coordinates in original pixels)
src, out, x0, y0, x1, y1, sc = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7]), float(sys.argv[7])
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width*sc), int(c.height*sc)), Image.LANCZOS)
c.save(out)
print(out, c.size)
