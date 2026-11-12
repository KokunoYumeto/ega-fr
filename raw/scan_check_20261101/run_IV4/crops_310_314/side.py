import sys
from PIL import Image
# usage: side.py out up page strip x0 y0 x1 y1 [page strip x0 y0 x1 y1 ...]  (display coords, 2000-wide)
run = r"user/Documents/ega_scan_check_20261101/run_IV4"
out = sys.argv[1]; up = float(sys.argv[2]); a = sys.argv[3:]
tiles = []
for i in range(0, len(a), 6):
    page, strip = a[i], a[i+1]
    x0, y0, x1, y1 = map(float, a[i+2:i+6])
    im = Image.open(f"{run}/page_{page}_s{strip}.png").convert("L")
    f = im.width / 2000.0
    c = im.crop(tuple(int(round(v * f)) for v in (x0, y0, x1, y1)))
    c = c.resize((int(c.width * up), int(c.height * up)), Image.LANCZOS)
    tiles.append(c)
W = sum(t.width for t in tiles) + 20 * (len(tiles) - 1); H = max(t.height for t in tiles)
canvas = Image.new("L", (W, H), 255); x = 0
for t in tiles:
    canvas.paste(t, (x, 0)); x += t.width + 20
canvas.save(f"{run}/crops_310_314/{out}.png"); print(out, canvas.size)
