"""crop.py PAGE STRIP x0 y0 x1 y1 NAME [SCALE] -- coordinates in the 2000-px display frame of the strip (x1.23 = original)."""
import sys, pathlib
from PIL import Image
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
here = pathlib.Path(__file__).resolve().parent
src = here.parent / f"page_{page:03d}_s{strip}.png"
im = Image.open(src)
f = im.size[0] / 2000.0
box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((int(c.size[0] * scale), int(c.size[1] * scale)), Image.LANCZOS)
out = here / f"{name}.png"
c.save(out)
print(out, c.size)
