"""crop.py PAGE STRIP x0 y0 x1 y1 OUTNAME [scale]  (coordinates in original strip pixels)"""
import sys
from PIL import Image
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
out = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
d = 'user/Documents/ega_scan_check_20261101/run_IVback/'
im = Image.open(d + f'page_{page}_s{strip}.png')
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(d + 'crops_345_349/' + out)
print(im.size, c.size)
