import sys
from PIL import Image
# usage: stem.py src.png x0 y0 x1 y1 [threshold]
# prints, for each row of the box, the runs of dark pixels (start, length)
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 128
im = Image.open(src).convert('L')
for y in range(y0, y1, max(1, (y1 - y0) // 12)):
    runs = []
    start = None
    for x in range(x0, x1):
        dark = im.getpixel((x, y)) < thr
        if dark and start is None:
            start = x
        if not dark and start is not None:
            runs.append((start, x - start))
            start = None
    if start is not None:
        runs.append((start, x1 - start))
    print(y, runs)
