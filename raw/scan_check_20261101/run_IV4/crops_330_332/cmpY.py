"""Side-by-side comparison of the Y glyphs on p. 330 strip 3 (each box in original strip pixels)."""
import sys
from PIL import Image
RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
im = Image.open(RUN + r"\page_330_s3.png").convert("L")
boxes = [
    (2000, 40, 2150, 100),   # line 1: ferme Y(D)
    (460, 160, 600, 220),    # line 3: x in Y(D)
    (1120, 215, 1260, 275),  # line 4: puisque x in Y(D)
    (1160, 405, 1300, 465),  # line 7: immersion canonique Y(D)
    (520, 575, 660, 635),    # line 10: fermes Y de X
    (1580, 575, 1720, 635),  # line 10: injection canonique Y->X
]
scale = 5
tiles = []
for b in boxes:
    c = im.crop(b).resize(((b[2]-b[0])*scale, (b[3]-b[1])*scale), Image.LANCZOS)
    tiles.append(c)
W = sum(t.width for t in tiles) + 30*(len(tiles)-1)
H = max(t.height for t in tiles)
out = Image.new("L", (W, H), 200)
x = 0
for t in tiles:
    out.paste(t, (x, 0)); x += t.width + 30
out.save(RUN + r"\crops_330_332\p330_Y_compare.png")
print(out.size)
