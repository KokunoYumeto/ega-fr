"""Connected components of ink in a box: python components.py PAGE STRIP X0 Y0 X1 Y1 [THRESH]
Prints each component with >= 30 px: bbox (absolute coordinates), width, height, pixel count, fill ratio,
and the mean horizontal run width (stroke weight)."""
import pathlib
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
page, strip, x0, y0, x1, y1 = (int(a) for a in sys.argv[1:7])
th = int(sys.argv[7]) if len(sys.argv) > 7 else 128
im = Image.open(RUN / f"page_{page:03d}_s{strip}.png").convert("L")
px = im.load()
seen = set()
for y in range(y0, y1):
    for x in range(x0, x1):
        if (x, y) in seen or px[x, y] >= th:
            continue
        stack, comp = [(x, y)], []
        seen.add((x, y))
        while stack:
            cx, cy = stack.pop()
            comp.append((cx, cy))
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    nx, ny = cx + dx, cy + dy
                    if x0 <= nx < x1 and y0 <= ny < y1 and (nx, ny) not in seen and px[nx, ny] < th:
                        seen.add((nx, ny))
                        stack.append((nx, ny))
        if len(comp) < 30:
            continue
        xs = [p[0] for p in comp]
        ys = [p[1] for p in comp]
        bx0, bx1, by0, by1 = min(xs), max(xs), min(ys), max(ys)
        w, h = bx1 - bx0 + 1, by1 - by0 + 1
        rows = {}
        for cx, cy in comp:
            rows.setdefault(cy, []).append(cx)
        runs = []
        for cy, rxs in rows.items():
            rxs.sort()
            s = rxs[0]
            prev = rxs[0]
            for v in rxs[1:] + [None]:
                if v is None or v != prev + 1:
                    runs.append(prev - s + 1)
                    if v is not None:
                        s = v
                if v is not None:
                    prev = v
        print(f"bbox x{bx0}-{bx1} y{by0}-{by1}  w{w} h{h}  px{len(comp)}  fill{len(comp)/(w*h):.2f}  "
              f"meanrun{sum(runs)/len(runs):.2f}")
