import sys
from PIL import Image

# usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME
# coordinates are in the original strip pixels
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
base = 'user/Documents/ega_scan_check_20261101/run_II'
im = Image.open(f'{base}/page_{page}_s{strip}.png')
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(f'{base}/crops_115_119/{out}')
print(c.size)
