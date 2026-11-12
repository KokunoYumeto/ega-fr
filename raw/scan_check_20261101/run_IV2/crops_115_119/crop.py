"""crop.py PAGE STRIP x0 y0 x1 y1 SCALE OUTNAME
Coordinates are in the ORIGINAL strip pixels (2480 wide)."""
import sys
from PIL import Image
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
src = r'user\Documents\ega_scan_check_20261101\run_IV2\page_%s_s%s.png' % (page, strip)
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(r'user\Documents\ega_scan_check_20261101\run_IV2\crops_115_119\%s' % out)
print(im.size, c.size)
