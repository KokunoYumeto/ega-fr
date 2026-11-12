import sys
from PIL import Image

# usage: ascii.py <png> <x0> <y0> <x1> <y1> [thresh]
# prints the box as ASCII art: '#' dark, '+' mid, '.' light
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
thresh = int(sys.argv[6]) if len(sys.argv) > 6 else 128
im = Image.open(src).convert('L')
px = im.load()
for y in range(y0, y1):
    row = []
    for x in range(x0, x1):
        v = px[x, y]
        row.append('#' if v < thresh else ('+' if v < 200 else '.'))
    print('%4d %s' % (y, ''.join(row)))
