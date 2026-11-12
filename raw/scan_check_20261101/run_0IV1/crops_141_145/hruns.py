import sys
from PIL import Image

# usage: hruns.py <png> <x0> <y0> <x1> <y1> [minlen] [thresh]
# prints horizontal dark runs (length >= minlen) per row inside the box,
# merged over rows: reports (row, start, end, length) for long runs.
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
minlen = int(sys.argv[6]) if len(sys.argv) > 6 else 15
thresh = int(sys.argv[7]) if len(sys.argv) > 7 else 128
im = Image.open(src).convert('L')
px = im.load()
for y in range(y0, y1):
    runs = []
    start = None
    for x in range(x0, x1 + 1):
        dark = x < x1 and px[x, y] < thresh
        if dark and start is None:
            start = x
        elif not dark and start is not None:
            if x - start >= minlen:
                runs.append((start, x - 1, x - start))
            start = None
    if runs:
        print(y, runs)
