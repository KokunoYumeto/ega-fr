import sys
from PIL import Image

# usage: python strokes.py <strip.png> x0 y0 x1 y1
# prints connected components (dark pixels) with bbox, pixel count and mean horizontal run length
src = sys.argv[1]
x0, y0, x1, y1 = (int(v) for v in sys.argv[2:6])
im = Image.open(src).convert('L').crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
dark = [[px[x, y] < 128 for x in range(w)] for y in range(h)]
seen = [[False] * w for _ in range(h)]
comps = []
for y in range(h):
    for x in range(w):
        if dark[y][x] and not seen[y][x]:
            stack = [(x, y)]
            seen[y][x] = True
            pts = []
            while stack:
                cx, cy = stack.pop()
                pts.append((cx, cy))
                for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
                    if 0 <= nx < w and 0 <= ny < h and dark[ny][nx] and not seen[ny][nx]:
                        seen[ny][nx] = True
                        stack.append((nx, ny))
            if len(pts) < 15:
                continue
            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]
            bx0, bx1, by0, by1 = min(xs), max(xs), min(ys), max(ys)
            # horizontal runs inside the component
            rows = {}
            for (px_, py_) in pts:
                rows.setdefault(py_, []).append(px_)
            runs = []
            for r, xsr in rows.items():
                xsr.sort()
                start = xsr[0]
                prev = xsr[0]
                for v in xsr[1:]:
                    if v != prev + 1:
                        runs.append(prev - start + 1)
                        start = v
                    prev = v
                runs.append(prev - start + 1)
            runs.sort()
            med = runs[len(runs) // 2]
            comps.append((bx0 + x0, by0 + y0, bx1 + x0, by1 + y0, len(pts), med))
comps.sort()
for c in comps:
    print('bbox=(%d,%d)-(%d,%d) h=%d n=%d median_run=%d' % (c[0], c[1], c[2], c[3], c[3] - c[1] + 1, c[4], c[5]))
