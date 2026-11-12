"""crop.py PAGE STRIP x0 y0 x1 y1 OUTNAME [SCALE]
Coordinates in the original strip pixels. Writes OUTNAME.png into this folder."""
import sys
from PIL import Image
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
out = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
src = r'user/Documents/ega_scan_check_20261101/run_IV4/page_%03d_s%d.png' % (page, strip)
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
if scale != 1.0:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(r'user/Documents/ega_scan_check_20261101/run_IV4/crops_085_089/%s.png' % out)
print(im.size, c.size)
