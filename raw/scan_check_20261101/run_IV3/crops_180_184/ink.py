"""List connected dark components in a region of a strip: bbox, dark-pixel count, mean horizontal run.

usage: python ink.py PAGE STRIP x0 y0 x1 y1 [threshold]
"""
import sys
from PIL import Image

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
thr = int(sys.argv[7]) if len(sys.argv) > 7 else 128
base = r"user\Documents\ega_scan_check_20261101\run_IV3"
im = Image.open(rf"{base}\page_{page:03d}_s{strip}.png").convert("L").crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
dark = [[px[x, y] < thr for x in range(w)] for y in range(h)]
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
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < w and 0 <= ny < h and dark[ny][nx] and not seen[ny][nx]:
                            seen[ny][nx] = True
                            stack.append((nx, ny))
            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]
            bx0, bx1, by0, by1 = min(xs), max(xs), min(ys), max(ys)
            # mean horizontal run length inside the component
            s = set(pts)
            runs = []
            for yy in range(by0, by1 + 1):
                run = 0
                for xx in range(bx0, bx1 + 2):
                    if (xx, yy) in s:
                        run += 1
                    elif run:
                        runs.append(run)
                        run = 0
            mr = sum(runs) / len(runs) if runs else 0
            comps.append((bx0 + x0, by0 + y0, bx1 + x0, by1 + y0, len(pts), mr))
comps.sort()
for c in comps:
    if c[4] >= 15:
        print("bbox x%d-%d y%d-%d  h=%d  px=%d  meanrun=%.2f" % (c[0], c[2], c[1], c[3], c[3] - c[1] + 1, c[4], c[5]))
