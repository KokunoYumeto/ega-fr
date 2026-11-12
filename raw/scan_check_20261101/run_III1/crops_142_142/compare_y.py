import pathlib
from PIL import Image, ImageDraw
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
out = run / "crops_142_142"
boxes = [  # (strip, x0, y0, x1, y1)
    (3, 680, 752, 710, 786),    # 1 voisinage V_y (s3)
    (3, 1353, 752, 1383, 786),  # 2 f^-1(V_y) (s3)
    (3, 1467, 752, 1497, 786),  # 3 ->V_y (s3)
    (4, 721, 69, 751, 103),     # 4 reunion des V_y (s4)
]
sc = 10
ims = []
for s, x0, y0, x1, y1 in boxes:
    im = Image.open(run / f"page_142_s{s}.png").convert("L").crop((x0, y0, x1, y1))
    ims.append(im.resize((im.width * sc, im.height * sc), Image.NEAREST))
W = sum(i.width for i in ims) + 60 * (len(ims) - 1)
H = max(i.height for i in ims) + 40
canvas = Image.new("L", (W, H), 255)
d = ImageDraw.Draw(canvas)
x = 0
for k, i in enumerate(ims, 1):
    canvas.paste(i, (x, 40)); d.text((x + 5, 5), str(k), fill=0); x += i.width + 60
canvas.save(out / "y_subscripts_x10.png")
print(canvas.size)
