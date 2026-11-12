from PIL import Image
D = 'user/Documents/ega_scan_check_20261101/run_III1/'
C = D + 'crops_122_126/'
parts = [
    ('page_126_s2.png', (930, 765, 1030, 820)),   # (4.1.7.8) mu_{x,m}
    ('page_126_s3.png', (2080, 75, 2165, 125)),   # text mu_{x,m}
    ('page_126_s3.png', (2080, 525, 2165, 575)),  # text mu_{x,0}
    ('page_126_s3.png', (1230, 420, 1300, 470)),  # R_k
    ('page_126_s3.png', (1330, 420, 1440, 470)),  # R_{k+m}
    ('page_126_s2.png', (1890, 615, 1930, 660)),  # par x dans
    ('page_126_s2.png', (860, 615, 900, 660)),    # Soit x
]
ims = [Image.open(D + f).crop(b) for f, b in parts]
s = 6
ims = [i.resize((i.width * s, i.height * s), Image.LANCZOS) for i in ims]
W = sum(i.width for i in ims) + 40 * len(ims)
H = max(i.height for i in ims)
out = Image.new('L', (W, H), 255)
x = 0
for i in ims:
    out.paste(i, (x, 0))
    x += i.width + 40
out.save(C + 'p126_compare.png')
print(out.size)
