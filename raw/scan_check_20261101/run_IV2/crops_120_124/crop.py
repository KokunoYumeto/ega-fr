"""crop.py PAGE STRIP X0 Y0 X1 Y1 NAME [ZOOM]: coordinates in the strip's original pixels."""
import sys, pathlib
from PIL import Image
page, strip, x0, y0, x1, y1, name = sys.argv[1:8]
zoom = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
d = pathlib.Path(__file__).resolve().parent
src = d.parent / f"page_{int(page):03d}_s{strip}.png"
im = Image.open(src)
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
c = c.resize((int(c.width * zoom), int(c.height * zoom)), Image.LANCZOS)
out = d / f"{name}.png"
c.save(out)
print(out, im.size)
