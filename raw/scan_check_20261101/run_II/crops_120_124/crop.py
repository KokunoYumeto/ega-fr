import sys
from PIL import Image

# usage: crop.py <page> <strip> <x0> <y0> <x1> <y1> <outname> [scale]
# coordinates in original pixels of the strip image
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
out = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
base = r'user/Documents/ega_scan_check_20261101/run_II/'
im = Image.open(base + 'page_%s_s%s.png' % (page, strip))
c = im.crop((x0, y0, x1, y1))
if scale != 1.0:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(base + 'crops_120_124/' + out)
print(c.size)
