import sys
from PIL import Image
# usage: crop.py page strip x0 y0 x1 y1 scale outname   (coords in ORIGINAL pixels)
src = r"user\Documents\ega_scan_check_20261101\run_II\page_%03d_s%d.png" % (int(sys.argv[1]), int(sys.argv[2]))
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
out = r"user\Documents\ega_scan_check_20261101\run_II\crops_160_164\%s.png" % sys.argv[8]
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width*scale), int(c.height*scale)), Image.LANCZOS)
c.save(out)
print(out, c.size, im.size)
