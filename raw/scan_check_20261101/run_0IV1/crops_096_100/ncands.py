import cv2
import numpy as np

base = r"user\Documents\ega_scan_check_20261101\run_0IV1"
cands = [
    ("ref-normal 98s2", 98, 2, 1077, 302), ("A 98s2 F_bn disp", 98, 2, 1565, 302), ("B 98s2 E_an diag", 98, 2, 1534, 834),
    ("C 98s3 F_bn.", 98, 3, 1864, 590), ("D 98s4 f_an o", 98, 4, 1077, 214), ("E 99s2 F_gn", 99, 2, 1261, 215),
    ("F 98s1 E_mn", 98, 1, 1383, 688), ("G 98s2 j<=n", 98, 2, 930, 484), ("H 98s3 E_gn diag", 98, 3, 1532, 240),
    ("ref 99s2 E_an.", 99, 2, 668, 410), ("ref 97s1 E_an", 97, 1, 656, 650), ("I 98s2 F_bn.", 98, 2, 2106, 481),
    ("J 98s2 j<=n.", 98, 2, 2110, 619), ("K 98s3 F_dn", 98, 3, 1347, 242), ("L 98s2 F_bn diag", 98, 2, 1349, 836),
    ("M 96s1 2027", 96, 1, 2027, 226), ("N 99s1 1244", 99, 1, 1244, 514), ("O 97s1 1295", 97, 1, 1295, 503),
]
tiles = []
for name, page, strip, x, y in cands:
    img = cv2.imread(rf"{base}\page_{page:03d}_s{strip}.png", cv2.IMREAD_GRAYSCALE)
    c = img[y - 6:y + 26, x - 6:x + 30]
    c = cv2.resize(c, None, fx=6, fy=6, interpolation=cv2.INTER_LANCZOS4)
    canvas = np.full((c.shape[0] + 22, max(c.shape[1], 220)), 255, np.uint8)
    canvas[22:, :c.shape[1]] = c
    cv2.putText(canvas, name, (2, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.45, 0, 1)
    tiles.append(canvas)
H = max(t.shape[0] for t in tiles)
W = max(t.shape[1] for t in tiles)
tiles = [np.pad(t, ((0, H - t.shape[0]), (0, W - t.shape[1])), constant_values=255) for t in tiles]
rows = [np.hstack(tiles[i:i + 6]) for i in range(0, len(tiles), 6)]
cv2.imwrite(base + r"\crops_096_100\ncands.png", np.vstack(rows))
