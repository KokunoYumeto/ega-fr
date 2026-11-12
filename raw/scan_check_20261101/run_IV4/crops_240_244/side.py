import sys
from PIL import Image, ImageDraw
# usage: side.py out scale  page:strip:x0:y0:x1:y1:label ...
base = "user/Documents/ega_scan_check_20261101/run_IV4"
out = sys.argv[1]
scale = float(sys.argv[2])
tiles = []
for spec in sys.argv[3:]:
    p, s, x0, y0, x1, y1, lab = spec.split(":")
    im = Image.open(f"{base}/page_{p}_s{s}.png").convert("L")
    c = im.crop((int(x0), int(y0), int(x1), int(y1)))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    tiles.append((c, lab))
W = sum(t.width for t, _ in tiles) + 20 * (len(tiles) + 1)
H = max(t.height for t, _ in tiles) + 40
canvas = Image.new("L", (W, H), 255)
d = ImageDraw.Draw(canvas)
x = 20
for t, lab in tiles:
    canvas.paste(t, (x, 30))
    d.text((x, 5), lab, fill=0)
    x += t.width + 20
canvas.save(f"{base}/crops_240_244/{out}")
print(canvas.size)
