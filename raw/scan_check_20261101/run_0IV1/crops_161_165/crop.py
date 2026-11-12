"""crop.py PAGE STRIP X0 Y0 X1 Y1 NAME [SCALE]: crop page_PAGE_sSTRIP.png using coordinates in the 2000-px display frame, upscale x2."""
import sys, pathlib
from PIL import Image
page, strip, x0, y0, x1, y1, name = sys.argv[1], sys.argv[2], *map(float, sys.argv[3:7]), sys.argv[7]
run = pathlib.Path(__file__).resolve().parent.parent
im = Image.open(run / f"page_{int(page):03d}_s{strip}.png")
f = im.size[0] / 2000.0
box = tuple(int(v * f) for v in (x0, y0, x1, y1))
c = im.crop(box)
up = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
c = c.resize((int(c.size[0] * up), int(c.size[1] * up)), Image.LANCZOS)
out = pathlib.Path(__file__).resolve().parent / f"{name}.png"
c.save(out)
print(out, c.size)
