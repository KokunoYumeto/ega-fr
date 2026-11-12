import sys, io
D = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex"
R = r"user\Documents\ega_scan_check_20261101\run_IV4"
src = open(D, encoding="utf-8", newline="").read()
print("CR in source:", src.count("\r"))
for n in range(150, 155):
    p = open(R + rf"\page_{n}.tex", encoding="utf-8", newline="").read()
    print(n, "CR in page:", p.count("\r"))
    p = p.replace("\r\n", "\n")
    lines = p.split("\n")
    body = "\n".join(lines[1:])
    a = src.index("\oldpage[IV-4]{%d}" % n)
    b = src.index("\oldpage[IV-4]{%d}" % (n + 1))
    seg = src[a:b]
    if body.strip() == seg.strip():
        print(n, "same as current")
    else:
        import difflib
        print(n, "DIFFERS")
        for l in difflib.unified_diff(body.strip().split("\n"), seg.strip().split("\n"), lineterm="", n=0):
            print("   ", l[:3000])
