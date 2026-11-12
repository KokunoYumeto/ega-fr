from PIL import Image
D = 'user/Documents/ega_scan_check_20261101/run_III1/'
C = D + 'crops_122_126/'
parts = [
    ('page_126_s2.png', (990, 780, 1030, 820)),   # (4.1.7.8) subscript m of mu_{x,m}
    ('page_126_s3.png', (2125, 90, 2165, 125)),   # text mu_{x,m}: subscript m
    ('page_126_s2.png', (1240, 610, 1290, 650)),  # superscript m of J^m in (4.1.7.7)
    ('page_126_s2.png', (1340, 610, 1400, 660)),  # (m >= 0) italic m in text
    ('page_126_s3.png', (1180, 410, 1240, 450)),  # superscript m of J^m in (4.1.7.10)
    ('page_126_s3.png', (1390, 435, 1440, 475)),  # m of R_{k+m}
]
ims = [Image.open(D + f).crop(b) for f, b in parts]
s = 7
ims = [i.resize((i.width * s, i.height * s), Image.LANCZOS) for i in ims]
W = sum(i.width for i in ims) + 40 * len(ims)
H = max(i.height for i in ims)
out = Image.new('L', (W, H), 255)
x = 0
for i in ims:
    out.paste(i, (x, 0))
    x += i.width + 40
out.save(C + 'p126_compare_m.png')
print(out.size)
