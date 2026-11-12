import sys
from PIL import Image

# usage: side.py OUT scale SRC1 x0 y0 x1 y1 SRC2 x0 y0 x1 y1 [...]
out = sys.argv[1]
scale = float(sys.argv[2])
args = sys.argv[3:]
crops = []
while args:
    src = args[0]
    x0, y0, x1, y1 = (int(v) for v in args[1:5])
    args = args[5:]
    c = Image.open(src).convert('L').crop((x0, y0, x1, y1))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    crops.append(c)
W = sum(c.width for c in crops) + 20 * (len(crops) - 1)
H = max(c.height for c in crops)
canvas = Image.new('L', (W, H), 255)
x = 0
for c in crops:
    canvas.paste(c, (x, 0))
    x += c.width + 20
canvas.save(out)
print(out, canvas.size)
