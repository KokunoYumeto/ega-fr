"""List the connected dark components in a region of a strip (original pixel coordinates).

usage: python ink.py PAGE STRIP X0 Y0 X1 Y1 [MINPIX]
Prints, for each component: bounding box (original coords), width, height, dark-pixel count, ink density.
"""
import sys
from pathlib import Path
from PIL import Image

RUN = Path(__file__).resolve().parent.parent

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
minpix = int(sys.argv[7]) if len(sys.argv) > 7 else 15

img = Image.open(RUN / f"page_{page:03d}_s{strip}.png").convert("L")
w, h = x1 - x0, y1 - y0
px = img.crop((x0, y0, x1, y1)).load()
dark = [[px[i, j] < 140 for j in range(h)] for i in range(w)]
seen = [[False] * h for _ in range(w)]
comps = []
for i in range(w):
    for j in range(h):
        if dark[i][j] and not seen[i][j]:
            stack = [(i, j)]
            seen[i][j] = True
            pts = []
            while stack:
                a, b = stack.pop()
                pts.append((a, b))
                for da in (-1, 0, 1):
                    for db in (-1, 0, 1):
                        c, d = a + da, b + db
                        if 0 <= c < w and 0 <= d < h and dark[c][d] and not seen[c][d]:
                            seen[c][d] = True
                            stack.append((c, d))
            if len(pts) >= minpix:
                xs = [p[0] for p in pts]
                ys = [p[1] for p in pts]
                bx0, bx1, by0, by1 = min(xs), max(xs), min(ys), max(ys)
                bw, bh = bx1 - bx0 + 1, by1 - by0 + 1
                comps.append((bx0 + x0, by0 + y0, bx1 + x0, by1 + y0, bw, bh, len(pts), len(pts) / (bw * bh)))
comps.sort()
for c in comps:
    print("box=(%d,%d)-(%d,%d) w=%d h=%d ink=%d density=%.2f" % c)
