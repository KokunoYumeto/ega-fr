import sys
from PIL import Image

# usage: measure.py <png> <x0> <y0> <x1> <y1>
# prints horizontal dark runs (len >= 15 px) per row inside the box
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
im = Image.open(src).convert("L")
px = im.load()
for y in range(y0, y1):
    runs, start = [], None
    for x in range(x0, x1 + 1):
        dark = x < x1 and px[x, y] < 128
        if dark and start is None:
            start = x
        elif not dark and start is not None:
            if x - start >= 15:
                runs.append((start, x - start))
            start = None
    if runs:
        print(y, runs)
