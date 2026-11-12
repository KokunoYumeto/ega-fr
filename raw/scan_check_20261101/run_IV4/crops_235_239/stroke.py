"""stroke.py SRC x0 y0 x1 y1 [x0 y0 x1 y1 ...] -- per box: median and mean horizontal dark-run width (px, threshold 140)
over the rows of the box, and dark-pixel count. Used to compare the weight of the same letter at the same size."""
import sys
from statistics import median
from PIL import Image
src = sys.argv[1]
im = Image.open(src).convert("L")
vals = list(map(int, sys.argv[2:]))
for k in range(0, len(vals), 4):
    x0, y0, x1, y1 = vals[k:k + 4]
    box = im.crop((x0, y0, x1, y1))
    w, h = box.size
    px = box.load()
    runs, dark = [], 0
    for y in range(h):
        run = 0
        for x in range(w):
            if px[x, y] < 140:
                run += 1
                dark += 1
            elif run:
                runs.append(run)
                run = 0
        if run:
            runs.append(run)
    print((x0, y0, x1, y1), "runs", len(runs), "median", median(runs) if runs else 0,
          "mean", round(sum(runs) / len(runs), 2) if runs else 0, "dark", dark)
