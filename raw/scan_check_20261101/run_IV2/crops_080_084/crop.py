"""crop.py PAGE STRIP X0 Y0 X1 Y1 NAME [SCALE]: crop a region (original pixel coords) of page_PAGE_sSTRIP.png, enlarge."""
import sys, pathlib
from PIL import Image
here = pathlib.Path(__file__).resolve().parent
run = here.parent
page, strip, x0, y0, x1, y1, name = sys.argv[1:8]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(run / f"page_{int(page):03d}_s{strip}.png")
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
out = here / f"{name}.png"
c.save(out)
print(out, c.size)
