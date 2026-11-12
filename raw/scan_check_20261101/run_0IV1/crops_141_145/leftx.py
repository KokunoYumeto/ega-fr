import sys
from PIL import Image

# usage: leftx.py <png> <y0> <y1> [x_from] [thresh]
# prints the leftmost dark pixel x in the band y0..y1 (rows), starting at x_from
src = sys.argv[1]
y0, y1 = int(sys.argv[2]), int(sys.argv[3])
xf = int(sys.argv[4]) if len(sys.argv) > 4 else 0
thresh = int(sys.argv[5]) if len(sys.argv) > 5 else 128
im = Image.open(src).convert('L')
px = im.load()
best = None
for y in range(y0, y1):
    for x in range(xf, im.width):
        if px[x, y] < thresh:
            if best is None or x < best:
                best = x
            break
print(src, (y0, y1), 'leftmost dark x =', best)
