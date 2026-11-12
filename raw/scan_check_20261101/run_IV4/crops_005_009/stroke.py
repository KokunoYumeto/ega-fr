"""Mean horizontal dark-run length (a rough stroke-width measure) in regions of a strip.

Usage: python stroke.py <strip.png> <threshold> <name:x0:y0:x1:y1> [...]
"""
import sys
from PIL import Image

src = sys.argv[1]
thr = int(sys.argv[2])
im = Image.open(src).convert("L")
px = im.load()
for spec in sys.argv[3:]:
    name, x0, y0, x1, y1 = spec.split(":")
    x0, y0, x1, y1 = map(int, (x0, y0, x1, y1))
    runs = []
    for y in range(y0, y1):
        run = 0
        for x in range(x0, x1):
            if px[x, y] < thr:
                run += 1
            elif run:
                runs.append(run)
                run = 0
        if run:
            runs.append(run)
    runs = [r for r in runs if r <= 25]
    dark = sum(1 for y in range(y0, y1) for x in range(x0, x1) if px[x, y] < thr)
    mean = sum(runs) / len(runs) if runs else 0
    print(f"{name}: runs={len(runs)} mean_run={mean:.2f} dark_px={dark}")
