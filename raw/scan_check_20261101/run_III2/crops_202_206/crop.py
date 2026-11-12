import sys
from PIL import Image
# usage: crop.py src.png out.png x0 y0 x1 y1 [scale]  (coordinates in displayed units of 2000-wide view; multiplied by factor)
src, out = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = [float(v) for v in sys.argv[3:7]]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(src)
f = im.width / 2000.0
box = (int(x0*f), int(y0*f), int(x1*f), int(y1*f))
c = im.crop(box)
c = c.resize((int(c.width*scale), int(c.height*scale)), Image.LANCZOS)
c.save(out)
print(out, c.size)
