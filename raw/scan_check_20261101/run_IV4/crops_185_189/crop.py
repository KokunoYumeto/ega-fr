"""crop.py PAGE STRIP x0 y0 x1 y1 NAME [SCALE]: crop a region (original pixel coords) of page_PAGE_sSTRIP.png."""
import sys
from PIL import Image
page, strip, x0, y0, x1, y1, name = sys.argv[1:8]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
src = rf"user\Documents\ega_scan_check_20261101\run_IV4\page_{int(page):03d}_s{strip}.png"
im = Image.open(src).crop((int(x0), int(y0), int(x1), int(y1)))
if scale != 1.0:
    im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
out = rf"user\Documents\ega_scan_check_20261101\run_IV4\crops_185_189\{name}.png"
im.save(out)
print(out, im.size)
