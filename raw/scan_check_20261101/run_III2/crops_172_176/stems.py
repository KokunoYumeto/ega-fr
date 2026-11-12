import sys
from PIL import Image

# usage: python stems.py <strip png> <x0> <y0> <x1> <y1>  (display-frame coords, x1.24 applied)
# prints, for each row of the region, the lengths of dark runs (horizontal stroke widths in px)
src = sys.argv[1]
x0, y0, x1, y1 = (float(v) for v in sys.argv[2:6])
im = Image.open(src).convert('L')
f = im.width / 2000.0
X0, Y0, X1, Y1 = (int(round(v * f)) for v in (x0, y0, x1, y1))
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 128
px = im.load()
allruns = []
for y in range(Y0, Y1):
    runs = []
    run = 0
    for x in range(X0, X1):
        if px[x, y] < thr:
            run += 1
        else:
            if run:
                runs.append(run)
            run = 0
    if run:
        runs.append(run)
    allruns.append((y, runs))
for y, runs in allruns:
    print(y, runs)
