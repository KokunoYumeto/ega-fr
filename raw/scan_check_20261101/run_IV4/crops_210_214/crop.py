import sys
from PIL import Image

# usage: python crop.py page strip x0 y0 x1 y1 scale outname
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
src = r'user/Documents/ega_scan_check_20261101/run_IV4/page_%03d_s%d.png' % (page, strip)
im = Image.open(src).crop((x0, y0, x1, y1))
if scale != 1:
    im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
im.save(r'user/Documents/ega_scan_check_20261101/run_IV4/crops_210_214/' + out)
print(im.size)
