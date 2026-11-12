import re
base = r"user\Documents\ega_scan_check_20261101\ega-fr\source\ega3"
for f in ["ega3-6-fr.tex", "ega3-7-fr.tex"]:
    lines = open(base + "\\" + f, encoding="utf-8").read().split("\n")
    page = None
    hits = []
    tE = []
    t667 = []
    for i, l in enumerate(lines, 1):
        m = re.search(r"\\oldpage\[III\]\{(\d+)\}", l)
        if m:
            page = int(m.group(1))
        for mm in re.finditer(r"\$0_\{\\mathrm I\}\$, (\d+)\.", l):
            if mm.group(1) in ("10", "11", "12", "13"):
                hits.append((page, i, mm.group(1)))
        if re.search(r"\{\}\^\{\([a-z]'?\)\}\\mathscr E", l):
            tE.append(page)
        if "(6.6.7, $t$)" in l:
            t667.append(page)
    print(f, "0_I refs to 10-13:", [(p, s) for p, i, s in hits])
    from collections import Counter
    print("  (t)mathscr E by page:", dict(Counter(tE)))
    print("  (6.6.7, $t$) by page:", dict(Counter(t667)))
