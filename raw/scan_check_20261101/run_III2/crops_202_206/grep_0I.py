import re, os
D = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\current\packages\BASE\native\ega3"
pat = re.compile(r"0_\{\\mathrm I\}\$,\s*((?:8|9|1[0-3])\.[0-9.]*)")
for fn in ["ega3-6-fr.tex", "ega3-7-fr.tex"]:
    s = open(os.path.join(D, fn), encoding="utf-8").read()
    for m in pat.finditer(s):
        print(fn, s.count("\n", 0, m.start()) + 1, repr(m.group(0)))
