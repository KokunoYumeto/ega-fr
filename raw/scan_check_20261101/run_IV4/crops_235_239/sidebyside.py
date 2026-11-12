"""sidebyside.py OUT scale SRC1 x0 y0 x1 y1 [SRC2 x0 y0 x1 y1 ...] -- paste crops next to each other."""
import sys
from PIL import Image
out, scale = sys.argv[1], float(sys.argv[2])
args = sys.argv[3:]
ims = []
while args:
    src, x0, y0, x1, y1 = args[0], *map(int, args[1:5])
    args = args[5:]
    im = Image.open(src).convert("L").crop((x0, y0, x1, y1))
    ims.append(im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS))
W = sum(i.width for i in ims) + 20 * (len(ims) - 1)
H = max(i.height for i in ims)
canvas = Image.new("L", (W, H), 255)
x = 0
for i in ims:
    canvas.paste(i, (x, 0))
    x += i.width + 20
canvas.save(out)
# darkness: mean ink per crop
for n, i in enumerate(ims):
    px = list(i.getdata())
    print(n, "ink", round(sum(255 - p for p in px) / len(px), 1))
