import sys
from PIL import Image

# usage: crop.py page strip x0 y0 x1 y1 scale outname
base = 'user/Documents/ega_scan_check_20261101/run_0IV1/'
p, s, x0, y0, x1, y1 = (int(v) for v in sys.argv[1:7])
scale = float(sys.argv[7])
out = sys.argv[8]
im = Image.open(f'{base}page_{p}_s{s}.png')
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(f'{base}crops_216_220/{out}')
print(c.size)
