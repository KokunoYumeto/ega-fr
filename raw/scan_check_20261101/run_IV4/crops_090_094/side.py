import sys
from PIL import Image

# usage: side.py scale outname  page:strip:x0:y0:x1:y1 [page:strip:x0:y0:x1:y1 ...]
# crops several regions (original strip pixels) and sets them side by side
run = r'user\Documents\ega_scan_check_20261101\run_IV4'
scale = float(sys.argv[1])
out = sys.argv[2]
parts = []
for spec in sys.argv[3:]:
    p, s, x0, y0, x1, y1 = map(int, spec.split(':'))
    im = Image.open(rf'{run}\page_{p:03d}_s{s}.png')
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    parts.append(c)
gap = 30
W = sum(c.width for c in parts) + gap * (len(parts) - 1)
H = max(c.height for c in parts)
canvas = Image.new('L', (W, H), 255)
x = 0
for c in parts:
    canvas.paste(c, (x, 0))
    x += c.width + gap
canvas.save(rf'{run}\crops_090_094\{out}')
print(canvas.size)
