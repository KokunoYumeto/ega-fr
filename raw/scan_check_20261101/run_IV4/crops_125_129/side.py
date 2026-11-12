import sys
from PIL import Image
# usage: side.py out scale  page strip x0 y0 x1 y1  [page strip x0 y0 x1 y1 ...]
base = r"user\Documents\ega_scan_check_20261101\run_IV4"
out = sys.argv[1]; scale = float(sys.argv[2]); a = sys.argv[3:]
crops = []
for i in range(0, len(a), 6):
    p, s, x0, y0, x1, y1 = map(int, a[i:i+6])
    im = Image.open(rf"{base}\page_{p:03d}_s{s}.png").convert("L")
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((int(c.width*scale), int(c.height*scale)), Image.LANCZOS)
    crops.append(c)
W = sum(c.width for c in crops) + 20*(len(crops)-1); H = max(c.height for c in crops)
res = Image.new("L", (W, H), 255); x = 0
for c in crops:
    res.paste(c, (x, 0)); x += c.width + 20
res.save(rf"{base}\crops_125_129\{out}")
print(res.size)
