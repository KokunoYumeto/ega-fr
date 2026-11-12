import re, sys
sys.stdout.reconfigure(encoding="utf-8")
base = r"user\Documents\ega_scan_check_20261101"
src = open(base + r"\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex", encoding="utf-8").read()
assert "\r" not in src, "source has CR"

def segment(n):
    a = src.index("\\oldpage[IV-4]{%d}" % n)
    b = src.index("\\oldpage[IV-4]{%d}" % (n + 1))
    return src[a:b]

for n in range(160, 165):
    page = open(base + r"\run_IV4\page_%03d.tex" % n, encoding="utf-8").read().replace("\r\n", "\n")
    body = page.split("\n", 1)[1]  # drop '% from ...' line
    seg = segment(n)
    print(n, "identical" if body == seg else "DIFFERENT", len(body), len(seg))
    if body != seg:
        import difflib
        for l in difflib.unified_diff(seg.split("\n"), body.split("\n"), lineterm=""):
            print("   ", l[:200])
