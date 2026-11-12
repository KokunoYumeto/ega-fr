import sys
from PIL import Image, ImageDraw

# usage: compose.py out.png scale src1 x0 y0 x1 y1 label1 [src2 x0 y0 x1 y1 label2 ...]
out = sys.argv[1]
scale = float(sys.argv[2])
args = sys.argv[3:]
tiles = []
for i in range(0, len(args), 6):
    src, x0, y0, x1, y1, label = args[i:i + 6]
    im = Image.open(src).convert('L').crop((int(x0), int(y0), int(x1), int(y1)))
    im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
    tiles.append((im, label))
W = sum(t[0].width for t in tiles) + 20 * (len(tiles) + 1)
H = max(t[0].height for t in tiles) + 60
canvas = Image.new('L', (W, H), 255)
d = ImageDraw.Draw(canvas)
x = 20
for im, label in tiles:
    canvas.paste(im, (x, 10))
    d.text((x, H - 40), label, fill=0)
    x += im.width + 20
canvas.save(out)
print(out, canvas.size)
