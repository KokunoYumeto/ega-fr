import sys
from PIL import Image
# usage: crop.py page strip x0 y0 x1 y1 scale outname   (coords in original strip pixels)
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
src = r"user\Documents\ega_scan_check_20261101\run_II\page_%s_s%s.png" % (page, strip)
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width*scale), int(c.height*scale)), Image.LANCZOS)
c.save(r"user\Documents\ega_scan_check_20261101\run_II\crops_195_199\%s" % out)
print(out, c.size)
