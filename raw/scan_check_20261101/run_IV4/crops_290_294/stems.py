"""Print horizontal dark-run widths across a row band inside glyph boxes (original pixel coordinates)."""
import sys
from pathlib import Path
from PIL import Image

RUN = Path(__file__).resolve().parent.parent

def runs(page, strip, x0, x1, y):
    im = Image.open(RUN / f"page_{page}_s{strip}.png").convert("L")
    px = im.load()
    out, cur = [], 0
    for x in range(x0, x1 + 1):
        if px[x, y] < 128:
            cur += 1
        elif cur:
            out.append(cur); cur = 0
    if cur:
        out.append(cur)
    return out

if __name__ == "__main__":
    page, strip = sys.argv[1], sys.argv[2]
    args = [int(v) for v in sys.argv[3:]]
    for i in range(0, len(args), 3):
        x0, x1, y = args[i:i+3]
        print((x0, x1, y), [runs(page, strip, x0, x1, yy) for yy in (y - 2, y, y + 2)])
