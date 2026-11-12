import re, sys, difflib
sys.stdout.reconfigure(encoding="utf-8")
run = r"user\Documents\ega_scan_check_20261101\run_IV4"
src = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex"
t = open(src, encoding="utf-8").read()
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
for page in range(125, 130):
    i = [k for k, (n, s) in enumerate(cuts) if n == page][0]
    seg = t[cuts[i][1]:cuts[i + 1][1]]
    p = open(rf"{run}\page_{page:03d}.tex", encoding="utf-8").read().replace("\r\n", "\n")
    body = p.split("\n", 1)[1]  # drop the '% from' line
    if body.rstrip() == seg.rstrip():
        print(page, "identical (up to trailing whitespace)")
    else:
        print(page, "DIFFERS")
        for l in difflib.unified_diff(seg.splitlines(), body.splitlines(), lineterm="", n=0):
            print("   ", l[:200])
