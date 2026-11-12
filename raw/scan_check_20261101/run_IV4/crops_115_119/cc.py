import sys
from PIL import Image

# usage: cc.py src.png x0 y0 x1 y1 [minh] [thr]
# Lists connected components (8-neighbour) of dark pixels in the region whose
# height is at least minh; for each: bbox (in page coordinates), the mean x of
# its top and bottom 15% rows, and shift/height (about 0 upright, >0.12 slanted).
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
minh = int(sys.argv[6]) if len(sys.argv) > 6 else 30
thr = int(sys.argv[7]) if len(sys.argv) > 7 else 140
im = Image.open(src).convert('L').crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
seen = [[False] * w for _ in range(h)]
comps = []
for y in range(h):
    for x in range(w):
        if px[x, y] < thr and not seen[y][x]:
            stack = [(x, y)]
            seen[y][x] = True
            pts = []
            while stack:
                cx, cy = stack.pop()
                pts.append((cx, cy))
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < w and 0 <= ny < h and not seen[ny][nx] and px[nx, ny] < thr:
                            seen[ny][nx] = True
                            stack.append((nx, ny))
            comps.append(pts)
for pts in comps:
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    H = max(ys) - min(ys) + 1
    if H < minh:
        continue
    top, bot = min(ys), max(ys)
    band = max(2, int(H * 0.15))
    tx = [p[0] for p in pts if p[1] < top + band]
    bx = [p[0] for p in pts if p[1] > bot - band]
    mt = sum(tx) / len(tx)
    mb = sum(bx) / len(bx)
    print('bbox=(%d,%d)-(%d,%d) h=%d w=%d top_x=%.1f bot_x=%.1f shift/h=%.3f n=%d' % (
        x0 + min(xs), y0 + top, x0 + max(xs), y0 + bot, H, max(xs) - min(xs) + 1,
        x0 + mt, x0 + mb, (mt - mb) / H, len(pts)))
