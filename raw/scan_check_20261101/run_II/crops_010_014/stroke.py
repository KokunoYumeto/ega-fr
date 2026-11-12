"""Mean horizontal dark-run length (a stroke-width proxy) inside boxes of one strip image.

Usage: python stroke.py <strip.png> name:x0,y0,x1,y1 [name:x0,y0,x1,y1 ...]
"""
import sys
from PIL import Image

im = Image.open(sys.argv[1]).convert("L")
for spec in sys.argv[2:]:
    name, box = spec.split(":")
    x0, y0, x1, y1 = map(int, box.split(","))
    reg = im.crop((x0, y0, x1, y1))
    w, h = reg.size
    px = reg.load()
    runs = []
    dark = 0
    for y in range(h):
        run = 0
        for x in range(w):
            if px[x, y] < 128:
                run += 1
                dark += 1
            elif run:
                runs.append(run)
                run = 0
        if run:
            runs.append(run)
    mean = sum(runs) / len(runs) if runs else 0
    print(f"{name}: mean dark run {mean:.2f} px over {len(runs)} runs, dark px {dark}")
