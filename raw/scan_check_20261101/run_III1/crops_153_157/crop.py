import sys
from PIL import Image

# usage: python crop.py <page> <strip> <x0> <y0> <x1> <y1> <scale> <outname>
# coordinates in ORIGINAL strip pixels (2476 px wide)
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
src = r'user\Documents\ega_scan_check_20261101\run_III1\page_%s_s%s.png' % (page, strip)
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(r'user\Documents\ega_scan_check_20261101\run_III1\crops_153_157\%s' % out)
print(c.size)
