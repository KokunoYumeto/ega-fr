import pathlib
from PIL import Image
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
out = run / "crops_142_142"
# same-scale comparison: V_y (s3 'voisinage V_y'), V_y (s3 'f^-1(V_y)'), V_y (s4 'reunion des V_y'), y in 'de y' (s3), V_y (p.143 top, s1)
pieces = [
    (run / "page_142_s3.png", (650, 715, 790, 800)),
    (run / "page_142_s3.png", (1270, 715, 1410, 800)),
    (run / "page_142_s3.png", (1400, 715, 1540, 800)),
    (run / "page_142_s4.png", (640, 25, 780, 110)),
    (run / "page_142_s3.png", (790, 715, 930, 800)),
]
sc = 5
ims = []
for p, box in pieces:
    im = Image.open(p).convert("L").crop(box)
    ims.append(im.resize((im.width * sc, im.height * sc), Image.LANCZOS))
W = sum(i.width for i in ims) + 40 * (len(ims) - 1)
H = max(i.height for i in ims)
canvas = Image.new("L", (W, H), 255)
x = 0
for i in ims:
    canvas.paste(i, (x, 0)); x += i.width + 40
canvas.save(out / "x_Vy_compare.png")
print(canvas.size)
