"""crop.py PAGE STRIP x0 y0 x1 y1 NAME [SCALE]: crop original-pixel box of page_PAGE_sSTRIP.png, enlarge, save NAME.png here."""
import sys, pathlib
from PIL import Image
here = pathlib.Path(__file__).resolve().parent
run = here.parent
page, strip, x0, y0, x1, y1, name = sys.argv[1:8]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(run / f"page_{int(page):03d}_s{strip}.png")
box = tuple(int(v) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
out = here / f"{name}.png"
c.save(out)
print(out, c.size)
