import sys
from PIL import Image

# usage: ink.py <strip png> x0 y0 x1 y1 [x0 y0 x1 y1 ...]
# prints, per box: dark-pixel count (<128) and the median length of horizontal dark runs
im = Image.open(sys.argv[1]).convert("L")
vals = [int(v) for v in sys.argv[2:]]
for i in range(0, len(vals), 4):
    x0, y0, x1, y1 = vals[i:i + 4]
    c = im.crop((x0, y0, x1, y1))
    w, h = c.size
    px = c.load()
    dark = 0
    runs = []
    for y in range(h):
        run = 0
        for x in range(w):
            if px[x, y] < 128:
                dark += 1
                run += 1
            else:
                if run:
                    runs.append(run)
                run = 0
        if run:
            runs.append(run)
    runs.sort()
    med = runs[len(runs) // 2] if runs else 0
    print((x0, y0, x1, y1), "dark", dark, "median run", med, "runs", len(runs))
