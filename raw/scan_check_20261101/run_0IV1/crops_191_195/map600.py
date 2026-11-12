import sys
import subprocess
from PIL import Image

# usage: map600.py page  -> renders page at 300 and 600 dpi (crops folder), prints strip offsets
# then: map600.py page strip x0 y0 x1 y1 scale out  -> crop the 600-dpi page for a strip box (strip coords at 300 dpi)
SCAN = r'user/Documents/Free or receipted/free/lesson-sources/numdam/PMIHES_1964__20__5_0.pdf'
OFF = -1
D = r'user/Documents/ega_scan_check_20261101/run_0IV1/crops_191_195/'
page = int(sys.argv[1])
import os
p300 = D + 'p%d_300.png' % page
p600 = D + 'p%d_600.png' % page
if not os.path.exists(p300):
    subprocess.run(['pdftoppm', '-png', '-r', '300', '-f', str(page + OFF), '-l', str(page + OFF), '-singlefile', SCAN, p300[:-4]], check=True)
if not os.path.exists(p600):
    subprocess.run(['pdftoppm', '-png', '-r', '600', '-mono', '-f', str(page + OFF), '-l', str(page + OFF), '-singlefile', SCAN, p600[:-4]], check=True)
im = Image.open(p300).convert('L')
w, h = im.size
box = Image.eval(im, lambda v: 255 - v).getbbox() or (0, 0, w, h)
left, right, top, bottom = max(0, box[0] - 20), min(w, box[2] + 20), max(0, box[1] - 20), min(h, box[3] + 20)
step = (bottom - top) / 4
offs = []
for i in range(4):
    y0 = int(top + i * step) - (40 if i else 0)
    offs.append((left, max(top, y0)))
if len(sys.argv) == 2:
    print('offsets', offs)
    sys.exit()
strip = int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
lx, ty = offs[strip - 1]
big = Image.open(p600).convert('L')
c = big.crop((2 * (x0 + lx), 2 * (y0 + ty), 2 * (x1 + lx), 2 * (y1 + ty)))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.NEAREST)
c.save(D + out)
print(out, c.size, 'origin600', 2 * (x0 + lx), 2 * (y0 + ty))
