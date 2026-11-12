"""allM.py PAGE STRIP Y0 Y1 [minw maxw]: list connected components in a horizontal band with bbox width 38-48 and height 30-36 (capital M size), with pixel counts."""
import sys, pathlib
from PIL import Image
run = pathlib.Path(__file__).parent.parent
page, strip, y0, y1 = sys.argv[1:5]
im = Image.open(run / f"page_{int(page):03d}_s{strip}.png").convert("L")
W, H = im.size
im = im.crop((0, int(y0), W, int(y1)))
w, h = im.size; px = im.load()
seen = set()
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
            xs = [p[0] for p in comp]; ys = [p[1] for p in comp]
            bw, bh = max(xs) - min(xs) + 1, max(ys) - min(ys) + 1
            if 38 <= bw <= 48 and 30 <= bh <= 36:
                print("x", min(xs), "y", min(ys) + int(y0), "w", bw, "h", bh, "px", len(comp))
