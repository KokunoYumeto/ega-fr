"""Side-by-side comparison sheet: python compare.py OUTNAME SCALE PAGE:STRIP:X0:Y0:X1:Y1[:LABEL] ...
Pastes the boxes next to each other (same scale) with a thin gap, into this folder."""
import pathlib
import sys

from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
name, scale = sys.argv[1], float(sys.argv[2])
tiles = []
for spec in sys.argv[3:]:
    p = spec.split(":")
    page, strip, x0, y0, x1, y1 = (int(v) for v in p[:6])
    im = Image.open(RUN / f"page_{page:03d}_s{strip}.png").convert("L").crop((x0, y0, x1, y1))
    im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
    tiles.append((im, p[6] if len(p) > 6 else ""))
H = max(t.height for t, _ in tiles) + 30
W = sum(t.width for t, _ in tiles) + 20 * len(tiles)
sheet = Image.new("L", (W, H), 255)
d = ImageDraw.Draw(sheet)
x = 0
for t, lab in tiles:
    sheet.paste(t, (x, 30))
    d.text((x + 2, 2), lab, fill=0)
    x += t.width + 20
out = HERE / f"{name}.png"
sheet.save(out)
print(out)
