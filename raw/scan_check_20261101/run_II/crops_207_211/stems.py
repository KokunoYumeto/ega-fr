import sys
from statistics import median
from PIL import Image

# usage: python stems.py PAGE STRIP label:x0:y0:x1:y1 [label:x0:y0:x1:y1 ...]
# prints the median and mean horizontal black-run length (stem width) and ink fraction in each box
base = r"user/Documents/ega_scan_check_20261101/run_II"
page, strip = sys.argv[1], sys.argv[2]
im = Image.open(f"{base}/page_{page}_s{strip}.png").convert("L")
W, H = im.size
px = im.load()
for spec in sys.argv[3:]:
    label, x0, y0, x1, y1 = spec.split(":")
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
    runs = []
    ink = 0
    for y in range(y0, y1):
        r = 0
        for x in range(x0, x1):
            if px[x, y] < 128:
                r += 1
                ink += 1
            elif r:
                runs.append(r)
                r = 0
        if r:
            runs.append(r)
    area = (x1 - x0) * (y1 - y0)
    runs = [r for r in runs if r >= 2]
    print(f"{label:28s} median_run={median(runs) if runs else 0:5.1f} mean_run={sum(runs)/len(runs) if runs else 0:5.2f} ink={ink/area:5.3f} n={len(runs)}")
    im.crop((x0, y0, x1, y1)).resize(((x1 - x0) * 3, (y1 - y0) * 3)).save(f"{base}/crops_207_211/box_{page}_{strip}_{label}.png")
