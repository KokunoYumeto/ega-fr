"""Measure the connected components in a crop: bbox, area, area/height (mean horizontal thickness).

Usage: python strokes.py page:strip:x0:y0:x1:y1 [...]
Prints the components (threshold 140) sorted by x, with area >= 15 px.
"""
import sys
from PIL import Image

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"


def components(img, thr=140):
    w, h = img.size
    px = img.load()
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
                xs = [p[0] for p in pts]
                ys = [p[1] for p in pts]
                comps.append((min(xs), min(ys), max(xs), max(ys), len(pts), pts))
    return comps


for spec in sys.argv[1:]:
    page, strip, x0, y0, x1, y1 = spec.split(":")
    im = Image.open(rf"{RUN}\page_{page}_s{strip}.png").convert("L")
    c = im.crop((int(x0), int(y0), int(x1), int(y1)))
    comps = [k for k in components(c) if k[4] >= 15]
    comps.sort(key=lambda k: k[0])
    print("==", spec)
    for (a, b, cc, d, n, pts) in comps:
        hgt = d - b + 1
        wid = cc - a + 1
        # mean horizontal run length per row
        rows = {}
        for (x, y) in pts:
            rows.setdefault(y, []).append(x)
        runs = []
        for y, xs in rows.items():
            xs.sort()
            run = 1
            for i in range(1, len(xs)):
                if xs[i] == xs[i - 1] + 1:
                    run += 1
                else:
                    runs.append(run)
                    run = 1
            runs.append(run)
        mean_run = sum(runs) / len(runs)
        print(f"  x={a:4d}-{cc:4d} y={b:3d}-{d:3d} w={wid:3d} h={hgt:3d} area={n:5d} meanrun={mean_run:5.2f}")
