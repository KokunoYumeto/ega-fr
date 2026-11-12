import sys
from PIL import Image

# usage: slant.py page:strip:x0:y0:x1:y1:label ...
# Estimates the slant of the left edge of the main stem of a glyph inside the box:
# for rows between 35% and 75% of the glyph's ink height, take the leftmost ink pixel;
# fit x = a*y + b; report dx per 100 px of height (positive = top leans right).
base = r"user\Documents\ega_scan_check_20261101\run_IV3"
for spec in sys.argv[1:]:
    p, s, x0, y0, x1, y1, lab = spec.split(":")
    im = Image.open(rf"{base}\page_{int(p):03d}_s{int(s)}.png").convert("L")
    c = im.crop((int(x0), int(y0), int(x1), int(y1)))
    w, h = c.size
    px = c.load()
    thr = 128
    rows = [y for y in range(h) if any(px[x, y] < thr for x in range(w))]
    if not rows:
        print(lab, "no ink"); continue
    top, bot = rows[0], rows[-1]
    H = bot - top + 1
    pts = []
    for y in range(top + int(0.35 * H), top + int(0.75 * H) + 1):
        xs = [x for x in range(w) if px[x, y] < thr]
        if xs:
            pts.append((y, xs[0]))
    n = len(pts)
    my = sum(y for y, _ in pts) / n
    mx = sum(x for _, x in pts) / n
    num = sum((y - my) * (x - mx) for y, x in pts)
    den = sum((y - my) ** 2 for y, _ in pts)
    a = num / den if den else 0.0
    # x increases rightwards, y downwards: a top-right lean gives negative a
    print(f"{lab}: ink height {H}px, left-edge slope dx/dy = {a:+.3f}  (lean {-a*100:+.1f} px per 100 px)")
