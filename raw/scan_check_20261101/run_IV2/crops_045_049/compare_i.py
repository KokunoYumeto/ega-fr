"""Put several small glyph crops side by side (same scale) and report the darkest-row stroke widths.
usage: python compare_i.py OUTNAME SCALE page:strip:x0:y0:x1:y1 [...]"""
import pathlib
import sys

from PIL import Image, ImageDraw

out_name, scale = sys.argv[1], int(sys.argv[2])
here = pathlib.Path(__file__).resolve().parent
run = here.parent
tiles = []
for spec in sys.argv[3:]:
    page, strip, x0, y0, x1, y1 = (int(v) for v in spec.split(":"))
    im = Image.open(run / f"page_{page:03d}_s{strip}.png").convert("L")
    c = im.crop((x0, y0, x1, y1))
    # stroke statistics: dark pixel count and widest dark run per row
    px = c.load()
    dark = 0
    widest = 0
    for yy in range(c.height):
        run_len = 0
        for xx in range(c.width):
            if px[xx, yy] < 110:
                dark += 1
                run_len += 1
                widest = max(widest, run_len)
            else:
                run_len = 0
    print(spec, "dark px:", dark, "widest run:", widest)
    tiles.append(c.resize((c.width * scale, c.height * scale), Image.NEAREST))
w = sum(t.width for t in tiles) + 20 * (len(tiles) + 1)
h = max(t.height for t in tiles) + 40
canvas = Image.new("L", (w, h), 255)
x = 20
for t in tiles:
    canvas.paste(t, (x, 20))
    x += t.width + 20
canvas.save(here / f"{out_name}.png")
print(here / f"{out_name}.png")
