"""v2crop.py PAGE STRIP x0 y0 x1 y1 NAME [SCALE]
Crop a region (original pixel coordinates) of run_IV4/page_PAGE_sSTRIP.png
and save it as run_IV4/crops_100_104/v2_NAME.png (optionally enlarged)."""
import sys
import pathlib
from PIL import Image

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
page, strip = int(sys.argv[1]), sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
im = Image.open(RUN / f"page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
if scale != 1.0:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
out = RUN / "crops_100_104" / f"v2_{name}.png"
c.save(out)
print(im.size, c.size, out)
