"""Crop a region of a strip image (coordinates in original pixels) and save it, optionally upscaled.
usage: python crop.py PAGE STRIP x0 y0 x1 y1 NAME [SCALE]"""
import sys, pathlib
from PIL import Image
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
im = Image.open(run / f"page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
if scale != 1.0:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
out = run / "crops_015_019" / f"{name}.png"
c.save(out)
print(out, c.size, im.size)
