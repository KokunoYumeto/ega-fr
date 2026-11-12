import sys
from PIL import Image
# usage: compose.py out scale src1 x0 y0 x1 y1 [src2 x0 y0 x1 y1 ...]
out = sys.argv[1]; s = float(sys.argv[2]); a = sys.argv[3:]
parts = []
for i in range(0, len(a), 5):
    im = Image.open(a[i]).convert('L')
    x0, y0, x1, y1 = map(int, a[i+1:i+5])
    c = im.crop((x0, y0, x1, y1))
    parts.append(c.resize((int(c.width*s), int(c.height*s)), Image.LANCZOS))
W = sum(p.width for p in parts) + 20*(len(parts)-1)
H = max(p.height for p in parts)
canvas = Image.new('L', (W, H), 255)
x = 0
for p in parts:
    canvas.paste(p, (x, 0)); x += p.width + 20
canvas.save(out); print(out, canvas.size)
