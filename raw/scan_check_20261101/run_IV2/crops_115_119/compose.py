"""compose.py OUT SCALE spec [spec ...]; spec = page:strip:x0:y0:x1:y1 (original strip pixels).
Puts the crops side by side (same scale), separated by grey bars, and prints the mean darkness
(0 = white, 255 = black) of the darkest 25 per cent of pixels in each crop."""
import sys
from PIL import Image, ImageOps
out, scale = sys.argv[1], float(sys.argv[2])
tiles = []
for spec in sys.argv[3:]:
    page, strip, x0, y0, x1, y1 = spec.split(':')
    im = Image.open(r'user\Documents\ega_scan_check_20261101\run_IV2\page_%s_s%s.png' % (page, strip)).convert('L')
    c = im.crop((int(x0), int(y0), int(x1), int(y1)))
    px = sorted(255 - p for p in c.getdata())
    k = max(1, len(px) // 4)
    ink = sum(px[-k:]) / k
    dark = sum(1 for p in px if p > 128)
    print(spec, 'top-quartile darkness %.1f, dark pixels %d' % (ink, dark))
    tiles.append(c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS))
h = max(t.height for t in tiles)
w = sum(t.width for t in tiles) + 20 * (len(tiles) - 1)
canvas = Image.new('L', (w, h), 255)
x = 0
for t in tiles:
    canvas.paste(t, (x, 0))
    x += t.width
    if x < w:
        canvas.paste(160, (x, 0, x + 20, h))
        x += 20
canvas.save(r'user\Documents\ega_scan_check_20261101\run_IV2\crops_115_119\%s' % out)
