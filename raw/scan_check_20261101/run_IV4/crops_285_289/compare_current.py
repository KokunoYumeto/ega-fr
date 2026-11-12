import difflib, re
B = r"user/Documents/ega_scan_check_20261101/"
src = open(B + r"ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-21b-fr.tex", encoding="utf-8").read()
m = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
cuts = [(int(x.group(1)), x.start()) for x in m.finditer(src)]
print([c for c in cuts if 283 <= c[0] <= 291])
for p in range(284, 291):
    i = [k for k, (n, s) in enumerate(cuts) if n == p]
    if not i:
        print(p, "marker missing"); continue
    i = i[0]; s = cuts[i][1]; e = cuts[i + 1][1] if i + 1 < len(cuts) else len(src)
    seg = src[s:e]
    pg = open(B + r"run_IV4/page_%d.tex" % p, encoding="utf-8").read().replace("\r\n", "\n").split("\n", 1)[1]
    same = seg.rstrip("\n") == pg.rstrip("\n")
    print(p, "same as page file:", same)
    if not same and p != 290:
        for d in difflib.unified_diff(pg.split("\n"), seg.split("\n"), lineterm="", n=0):
            print("   ", d[:300])
    if p == 290 and not same:
        print("   290 segment start:", repr(seg[:120]))
