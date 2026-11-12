"""Average stroke width of the largest dark component inside each box (a rough weight measure for one glyph).

Usage: python inkwidth.py PAGE STRIP label:x0,y0,x1,y1 [label:x0,y0,x1,y1 ...]
Prints, per box: component height, area, area/height (mean horizontal stroke width in px at 300 dpi).
"""
import sys
from pathlib import Path
from PIL import Image

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_0III")
page, strip = int(sys.argv[1]), int(sys.argv[2])
im = Image.open(RUN / f"page_{page:03d}_s{strip}.png").convert("L")
for arg in sys.argv[3:]:
    label, box = arg.split(":")
    print(label)
    x0, y0, x1, y1 = (int(v) for v in box.split(","))
    c = im.crop((x0, y0, x1, y1))
    w, h = c.size
    px = c.load()
    dark = [[px[x, y] < 128 for x in range(w)] for y in range(h)]
    seen = [[False] * w for _ in range(h)]
    best = []
    for y in range(h):
        for x in range(w):
            if dark[y][x] and not seen[y][x]:
                stack, comp = [(x, y)], []
                seen[y][x] = True
                while stack:
                    a, b = stack.pop()
                    comp.append((a, b))
                    for da, db in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        u, v = a + da, b + db
                        if 0 <= u < w and 0 <= v < h and dark[v][u] and not seen[v][u]:
                            seen[v][u] = True
                            stack.append((u, v))
                if len(comp) > 15:
                    cy=[q[1] for q in comp]; cx=[q[0] for q in comp]
                    hh=max(cy)-min(cy)+1
                    print(f"   comp x={x0+min(cx)}-{x0+max(cx)} y={y0+min(cy)}-{y0+max(cy)} h={hh} area={len(comp)} a/h={len(comp)/hh:.2f}")
                if len(comp) > len(best):
                    best = comp
    if not best:
        print(label, "no ink")
        continue
    ys = [p[1] for p in best]
    xs = [p[0] for p in best]
    ht = max(ys) - min(ys) + 1
    print(f"{label:28s} bbox=({min(xs)},{min(ys)})-({max(xs)},{max(ys)}) height={ht:3d} area={len(best):4d} "
          f"area/height={len(best) / ht:5.2f}")
