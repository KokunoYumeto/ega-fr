import os
from PIL import Image

run = r"user/Documents/ega_scan_check_20261101/run_0IV1"
out = os.path.join(run, "crops_016_020")
# name, page, strip, x0, y0, x1, y1, scale (original pixel coordinates)
crops = [
    ("p17_paren", 17, 3, 1300, 530, 2080, 600, 2),
    ("p18_paren", 18, 2, 700, 400, 1500, 465, 2),
    ("p16_ref", 16, 2, 400, 760, 1800, 820, 1),
    ("p18_ref", 18, 3, 450, 580, 2150, 640, 1),
    ("p17_15", 17, 3, 300, 330, 2100, 680, 1),
]
for name, page, strip, x0, y0, x1, y1, s in crops:
    im = Image.open(os.path.join(run, "page_%03d_s%d.png" % (page, strip)))
    c = im.crop((x0, y0, x1, y1))
    if s != 1:
        c = c.resize((c.width * s, c.height * s), Image.LANCZOS)
    c.save(os.path.join(out, name + ".png"))
    print(name, c.size)
