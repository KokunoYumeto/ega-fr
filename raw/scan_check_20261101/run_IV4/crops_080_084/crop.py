import sys
from PIL import Image

# usage: crop.py PAGE STRIP x0 y0 x1 y1 NAME [SCALE]
# coordinates are in the original strip pixels
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
src = r'user/Documents/ega_scan_check_20261101/run_IV4/page_%03d_s%d.png' % (page, strip)
im = Image.open(src).crop((x0, y0, x1, y1))
if scale != 1.0:
    im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
out = r'user/Documents/ega_scan_check_20261101/run_IV4/crops_080_084/%s.png' % name
im.save(out)
print(out, im.size)
