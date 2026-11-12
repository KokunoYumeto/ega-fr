import pathlib
from PIL import Image
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
out = run / "crops_045_049"
jobs = [
    ("p45_labels", "page_045_s1.png", (330, 290, 900, 640), 1),
    ("p49_resp", "page_049_s2.png", (330, 250, 2445, 420), 1),
    ("p49_refs_stmt", "page_049_s1.png", (240, 590, 1200, 700), 1),
    ("p47_ref_stmt", "page_047_s1.png", (250, 730, 1200, 790), 2),
    ("p48_ref_stmt", "page_048_s3.png", (430, 680, 1300, 740), 2),
    ("p49_ref_8_13_1", "page_049_s3.png", (330, 220, 1500, 280), 1),
]
for name, strip, box, s in jobs:
    im = Image.open(run / strip)
    w, h = im.size
    b = (max(0, box[0]), max(0, box[1]), min(w, box[2]), min(h, box[3]))
    c = im.crop(b)
    if s != 1:
        c = c.resize((c.width * s, c.height * s), Image.LANCZOS)
    c.save(out / f"{name}.png")
    print(name, b, c.size)
