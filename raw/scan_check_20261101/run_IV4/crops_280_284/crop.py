import sys
from PIL import Image

# usage: crop.py page strip x0 y0 x1 y1 scale outname
base = r'user/Documents/ega_scan_check_20261101/run_IV4/'
out = base + 'crops_280_284/'
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = [int(v) for v in sys.argv[3:7]]
scale = float(sys.argv[7])
name = sys.argv[8]
im = Image.open(base + 'page_%d_s%d.png' % (page, strip))
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out + name)
print(out + name, c.size)
