"""Enlarge a region of a 300-dpi page strip (run_I_a/page_NNN_sK.png).
usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 [SCALE]
coordinates are pixels of the original strip (as displayed x 1.12 or so); writes crops_fix_090_097/zPAGE_sSTRIP_X0_Y0.png"""
import pathlib
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 3.0
src = HERE.parent / f"page_{page:03d}_s{strip}.png"
im = Image.open(src)
box = im.crop((x0, y0, x1, y1))
box = box.resize((int(box.width * scale), int(box.height * scale)), Image.LANCZOS)
out = HERE / f"z{page}_s{strip}_{x0}_{y0}.png"
box.save(out)
print(out, box.width, box.height)
