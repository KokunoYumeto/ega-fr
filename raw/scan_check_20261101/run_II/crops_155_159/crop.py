"""crop.py PAGE STRIP x0 y0 x1 y1 SCALE NAME -- coordinates in original strip pixels."""
import sys, pathlib
from PIL import Image
d = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
page, strip, x0, y0, x1, y1, scale, name = sys.argv[1:9]
im = Image.open(d / f"page_{int(page):03d}_s{strip}.png")
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
out = d / "crops_155_159" / f"{name}.png"
c.save(out)
print(out, c.size)
