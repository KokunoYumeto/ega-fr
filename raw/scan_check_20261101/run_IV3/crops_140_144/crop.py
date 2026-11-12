"""crop.py PAGE STRIP X0 Y0 X1 Y1 NAME [ZOOM]: crop page_PAGE_sSTRIP.png (coordinates in ORIGINAL pixels), enlarge, save NAME.png here."""
import sys, pathlib
from PIL import Image
here = pathlib.Path(__file__).parent
run = here.parent
page, strip, x0, y0, x1, y1, name = sys.argv[1:8]
zoom = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(run / f"page_{int(page):03d}_s{strip}.png")
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
c = c.resize((int(c.width * zoom), int(c.height * zoom)), Image.LANCZOS)
c.save(here / f"{name}.png")
print(c.size)
