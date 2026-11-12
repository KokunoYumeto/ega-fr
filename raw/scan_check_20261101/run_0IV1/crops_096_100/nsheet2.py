import json
import cv2
import numpy as np

base = r"user\Documents\ega_scan_check_20261101\run_0IV1"
out = base + r"\crops_096_100"
res = json.load(open(out + r"\nthick.json"))
seen = set()
uniq = []
for d in res:
    key = (d["page"], d["x"] // 6, (d["y"] if d["strip"] != 3 else d["y"]) // 6, d["strip"])
    uniq.append(d)
sel = uniq[:24] + uniq[len(uniq) // 2: len(uniq) // 2 + 6]
tiles = []
for d in sel:
    img = cv2.imread(rf"{base}\page_{d['page']:03d}_s{d['strip']}.png", cv2.IMREAD_GRAYSCALE)
    x, y, w, h = d["x"], d["y"], d["w"], d["h"]
    c = img[max(0, y - 30):y + h + 12, max(0, x - 70):x + w + 25]
    c = cv2.resize(c, None, fx=2.5, fy=2.5, interpolation=cv2.INTER_LANCZOS4)
    canvas = np.full((175, 330), 255, np.uint8)
    hh, ww = min(c.shape[0], 155), min(c.shape[1], 330)
    canvas[20:20 + hh, :ww] = c[:hh, :ww]
    cv2.putText(canvas, f"{d['page']}s{d['strip']} {x},{y} t{d['thick']}", (2, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.42, 0, 1)
    tiles.append(canvas)
per = 6
rows = []
for i in range(0, len(tiles), per):
    chunk = tiles[i:i + per]
    chunk += [np.full((175, 330), 255, np.uint8)] * (per - len(chunk))
    rows.append(np.hstack(chunk))
cv2.imwrite(out + r"\nthick_sheet.png", np.vstack(rows))
print(len(tiles))
