import sys, json
from PIL import Image, ImageDraw
# usage: stack.py out.png scale '[["176",4,x0,y0,x1,y1,"label"], ...]'
d = r"user/Documents/ega_scan_check_20261101/run_0IV1"
out = sys.argv[1]
scale = float(sys.argv[2])
items = json.loads(sys.argv[3])
crops = []
for page, strip, x0, y0, x1, y1, label in items:
    im = Image.open(f"{d}/page_{page}_s{strip}.png").convert("L")
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    crops.append((label, c))
W = max(c.width for _, c in crops) + 10
H = sum(c.height + 30 for _, c in crops)
canvas = Image.new("L", (W, H), 255)
dr = ImageDraw.Draw(canvas)
y = 0
for label, c in crops:
    dr.text((5, y + 5), label, fill=0)
    canvas.paste(c, (5, y + 25))
    y += c.height + 30
canvas.save(f"{d}/crops_176_180/{out}")
print(canvas.size)
