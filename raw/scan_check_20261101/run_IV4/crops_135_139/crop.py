import sys
from PIL import Image
# usage: crop.py page strip x0 y0 x1 y1 outname [scale]
p, s = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
out = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(r'user/Documents/ega_scan_check_20261101/run_IV4/page_%s_s%s.png' % (p, s))
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(im.size, c.size)
