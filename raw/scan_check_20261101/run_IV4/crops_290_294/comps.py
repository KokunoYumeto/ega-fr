"""List connected ink components (bounding box, ink count) in a region of a strip (display coordinates)."""
import sys
from pathlib import Path
from PIL import Image

RUN = Path(__file__).resolve().parent.parent

def main():
    page, strip = sys.argv[1], sys.argv[2]
    x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
    minsize = int(sys.argv[7]) if len(sys.argv) > 7 else 30
    im = Image.open(RUN / f"page_{page}_s{strip}.png").convert("L")
    s = im.size[0] / 2000.0
    bx = tuple(int(round(v * s)) for v in (x0, y0, x1, y1))
    c = im.crop(bx)
    w, h = c.size
    px = c.load()
    seen = [[False] * w for _ in range(h)]
    comps = []
    for y in range(h):
        for x in range(w):
            if px[x, y] < 128 and not seen[y][x]:
                stack = [(x, y)]
                seen[y][x] = True
                pts = []
                while stack:
                    a, b = stack.pop()
                    pts.append((a, b))
                    for da in (-1, 0, 1):
                        for db in (-1, 0, 1):
                            na, nb = a + da, b + db
                            if 0 <= na < w and 0 <= nb < h and not seen[nb][na] and px[na, nb] < 128:
                                seen[nb][na] = True
                                stack.append((na, nb))
                if len(pts) >= minsize:
                    xs = [p[0] for p in pts]
                    ys = [p[1] for p in pts]
                    comps.append((min(xs) + bx[0], min(ys) + bx[1], max(xs) + bx[0], max(ys) + bx[1], len(pts)))
    comps.sort()
    for cbox in comps:
        print("orig box", cbox[:4], "w,h", cbox[2] - cbox[0] + 1, cbox[3] - cbox[1] + 1, "ink", cbox[4])

if __name__ == "__main__":
    main()
