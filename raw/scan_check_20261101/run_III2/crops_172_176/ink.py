import sys
from PIL import Image

# usage: python ink.py <strip png> <x0> <y0> <x1> <y1> [thr]   (display-frame coords, scaled by width/2000)
# prints dark-pixel count, bbox of dark pixels, and the max horizontal run per row
src = sys.argv[1]
x0, y0, x1, y1 = (float(v) for v in sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 140
im = Image.open(src).convert('L')
f = im.width / 2000.0
X0, Y0, X1, Y1 = (int(round(v * f)) for v in (x0, y0, x1, y1))
px = im.load()
n = 0
xs, ys = [], []
for y in range(Y0, Y1):
    for x in range(X0, X1):
        if px[x, y] < thr:
            n += 1
            xs.append(x)
            ys.append(y)
if n:
    print('ink', n, 'bbox', min(xs), min(ys), max(xs), max(ys), 'w', max(xs) - min(xs) + 1, 'h', max(ys) - min(ys) + 1)
else:
    print('no ink')
