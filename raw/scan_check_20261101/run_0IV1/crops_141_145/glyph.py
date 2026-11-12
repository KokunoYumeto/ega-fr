import sys
from PIL import Image

# usage: glyph.py <png> <x0> <y0> <x1> <y1> [thresh]
# prints the dark-pixel count, bounding box of dark pixels, and the max
# horizontal and vertical run lengths (a rough stroke-width measure).
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
thresh = int(sys.argv[6]) if len(sys.argv) > 6 else 128
im = Image.open(src).convert('L')
px = im.load()
cnt = 0
xs, ys = [], []
for y in range(y0, y1):
    for x in range(x0, x1):
        if px[x, y] < thresh:
            cnt += 1
            xs.append(x)
            ys.append(y)
if not cnt:
    print('no dark pixels')
    sys.exit()
bx0, bx1, by0, by1 = min(xs), max(xs), min(ys), max(ys)
# median horizontal run length through the glyph
runs = []
for y in range(by0, by1 + 1):
    r = 0
    for x in range(bx0, bx1 + 2):
        if x <= bx1 and px[x, y] < thresh:
            r += 1
        elif r:
            runs.append(r)
            r = 0
runs.sort()
med = runs[len(runs) // 2] if runs else 0
print('dark', cnt, 'bbox', (bx0, by0, bx1, by1), 'w', bx1 - bx0 + 1, 'h', by1 - by0 + 1,
      'median hrun', med, 'ink ratio %.2f' % (cnt / ((bx1 - bx0 + 1) * (by1 - by0 + 1))))
