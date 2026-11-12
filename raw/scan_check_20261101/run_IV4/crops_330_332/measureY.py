"""Measure the stem width and ink of the Y glyphs on p. 330 strip 3 (threshold 128)."""
from PIL import Image
RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
im = Image.open(RUN + r"\page_330_s3.png").convert("L")
W, H = im.size
px = im.load()
boxes = {
    "l1 ferme Y(D)": (2000, 40, 2150, 100),
    "l3 x in Y(D)": (460, 160, 600, 220),
    "l4 puisque x in Y(D)": (1120, 215, 1260, 275),
    "l7 canonique Y(D)": (1160, 405, 1300, 465),
    "l10 fermes Y de": (520, 575, 660, 635),
    "l10 canonique Y->X": (1580, 575, 1720, 635),
}
def dark(x, y):
    return px[x, y] < 128
for name, (x0, y0, x1, y1) in boxes.items():
    # find connected columns: locate the Y as the first glyph whose height is close to cap height
    # simple approach: print an ASCII map of the box, downsampled
    cols = []
    rows = []
    for y in range(y0, y1):
        row = ''.join('#' if dark(x, y) else '.' for x in range(x0, x1))
        rows.append(row)
    print("==", name)
    for r in rows[::2]:
        print(r[:100])
