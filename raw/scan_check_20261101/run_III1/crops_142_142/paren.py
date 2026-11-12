import pathlib
from PIL import Image
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
out = run / "crops_142_142"
im = Image.open(run / "page_142_s3.png").convert("L")
# '(i) Si f_z est un morphisme fini (resp. une immersion fermee), il' and the next-line '(resp. une'
a = im.crop((560, 315, 1660, 375)); a.resize((a.width * 2, a.height * 2), Image.LANCZOS).save(out / "paren_i.png")
b = im.crop((1560, 372, 2180, 432)); b.resize((b.width * 3, b.height * 3), Image.LANCZOS).save(out / "paren_ii.png")
print("ok")
