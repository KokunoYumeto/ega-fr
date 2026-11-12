"""crop.py PAGE STRIP X0 Y0 X1 Y1 ZOOM NAME  -- coordinates in DISPLAYED pixels of the 2000-px-wide strip view;
converted with the strip's own scale (orig_width/2000). Writes NAME.png next to this script."""
import sys, pathlib
from PIL import Image
here = pathlib.Path(__file__).resolve().parent
run = here.parent
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
zoom = float(sys.argv[7]); name = sys.argv[8]
im = Image.open(run / f"page_{page:03d}_s{strip}.png")
f = im.size[0] / 2000.0
box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((int(c.size[0] * zoom), int(c.size[1] * zoom)), Image.LANCZOS)
c.save(here / f"{name}.png")
print(name, box, c.size)
