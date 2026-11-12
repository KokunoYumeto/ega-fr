"""blobs.py IMG X0 Y0 X1 Y1  (displayed 2000-px frame) -> bounding boxes (original px, relative to crop) of dark blobs."""
import sys
from PIL import Image

img = Image.open(sys.argv[1]).convert('L')
f = img.size[0] / 2000.0
x0, y0, x1, y1 = (int(round(float(v) * f)) for v in sys.argv[2:6])
c = img.crop((x0, y0, x1, y1))
w, h = c.size
px = c.load()
dark = [[px[x, y] < 128 for x in range(w)] for y in range(h)]
seen = [[False] * w for _ in range(h)]
blobs = []
for y in range(h):
    for x in range(w):
        if dark[y][x] and not seen[y][x]:
            stack = [(x, y)]
            seen[y][x] = True
            xs, ys = [], []
            while stack:
                a, b = stack.pop()
                xs.append(a); ys.append(b)
                for da in (-1, 0, 1):
                    for db in (-1, 0, 1):
                        u, v = a + da, b + db
                        if 0 <= u < w and 0 <= v < h and dark[v][u] and not seen[v][u]:
                            seen[v][u] = True
                            stack.append((u, v))
            blobs.append((min(xs), min(ys), max(xs), max(ys), len(xs)))
blobs.sort()
for b in blobs:
    if b[4] >= 15:
        print('x %4d-%4d  y %3d-%3d  n=%d' % (b[0], b[2], b[1], b[3], b[4]))
