"""glyph.py PAGE STRIP X0 Y0 X1 Y1: largest dark connected component in the box: pixel count, bbox, mean horizontal run width."""
import sys, pathlib
from PIL import Image
run = pathlib.Path(__file__).parent.parent
page, strip, x0, y0, x1, y1 = sys.argv[1:7]
im = Image.open(run / f"page_{int(page):03d}_s{strip}.png").convert("L").crop((int(x0), int(y0), int(x1), int(y1)))
w, h = im.size; px = im.load()
seen = set(); best = []
for y in range(h):
    for x in range(w):
        if px[x, y] < 128 and (x, y) not in seen:
            comp = []; st = [(x, y)]; seen.add((x, y))
            while st:
                a, b = st.pop(); comp.append((a, b))
                for da in (-1, 0, 1):
                    for db in (-1, 0, 1):
                        c, d = a + da, b + db
                        if 0 <= c < w and 0 <= d < h and (c, d) not in seen and px[c, d] < 128:
                            seen.add((c, d)); st.append((c, d))
            if len(comp) > len(best): best = comp
xs = [p[0] for p in best]; ys = [p[1] for p in best]
print("pixels", len(best), "bbox", min(xs), min(ys), max(xs), max(ys), "w", max(xs) - min(xs) + 1, "h", max(ys) - min(ys) + 1)
