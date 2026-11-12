import sys
from PIL import Image

# usage: crop.py <page> <strip> <x0> <y0> <x1> <y1> <out_name> [scale]
# coordinates are in original-image pixels
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
out = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
src = r'user/Documents/ega_scan_check_20261101/run_0IV1/page_%03d_s%s.png' % (int(page), strip)
im = Image.open(src).crop((x0, y0, x1, y1))
im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
im.save(r'user/Documents/ega_scan_check_20261101/run_0IV1/crops_101_105/' + out)
print(im.size)
