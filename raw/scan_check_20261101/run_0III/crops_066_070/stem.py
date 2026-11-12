import sys
from PIL import Image

# usage: stem.py SRC x0 y0 x1 y1 [threshold]
# prints, for each row in the box, the lengths of dark runs (to compare stroke widths)
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 128
im = Image.open(src).convert('L')
for y in range(y0, y1):
    runs = []
    run = 0
    for x in range(x0, x1):
        if im.getpixel((x, y)) < thr:
            run += 1
        elif run:
            runs.append(run)
            run = 0
    if run:
        runs.append(run)
    print(y, runs)
