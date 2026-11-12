"""v2side.py NAME SCALE PAGE:STRIP:x0:y0:x1:y1 [PAGE:STRIP:x0:y0:x1:y1 ...]
Put several crops (original pixel coordinates of run_IV4/page_PAGE_sSTRIP.png) side by side at the same scale,
save as crops_100_104/v2_NAME.png, and print for each crop the number of dark pixels (< 128) and the mean darkness
of the dark pixels (a rough weight measure)."""
import sys
import pathlib
from PIL import Image

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
name, scale = sys.argv[1], float(sys.argv[2])
crops = []
for spec in sys.argv[3:]:
    p, s, x0, y0, x1, y1 = spec.split(":")
    im = Image.open(RUN / f"page_{int(p):03d}_s{s}.png").convert("L")
    c = im.crop((int(x0), int(y0), int(x1), int(y1)))
    px = list(c.getdata())
    dark = [v for v in px if v < 128]
    print(spec, "dark px", len(dark), "mean dark value", round(sum(dark) / len(dark), 1) if dark else None)
    crops.append(c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS))
W = sum(c.width for c in crops) + 20 * (len(crops) - 1)
H = max(c.height for c in crops)
out = Image.new("L", (W, H), 255)
x = 0
for c in crops:
    out.paste(c, (x, 0))
    x += c.width + 20
out.save(RUN / "crops_100_104" / f"v2_{name}.png")
print("saved", out.size)
