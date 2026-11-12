import sys
from PIL import Image

# usage: crop.py page strip x0 y0 x1 y1 scale outname
# coordinates in original strip pixels
run = r'user\Documents\ega_scan_check_20261101\run_IV4'
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
im = Image.open(rf'{run}\page_{page:03d}_s{strip}.png')
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf'{run}\crops_090_094\{out}')
print(c.size)
