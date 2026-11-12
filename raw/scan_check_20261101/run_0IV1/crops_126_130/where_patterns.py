import re
BS = "\\"
f = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\ega0-20-fr.tex"
t = open(f, encoding="utf-8").read()
marks = [(m.start(), int(m.group(1))) for m in re.finditer(re.escape(BS + "oldpage[0" + BS + "textsubscript{IV-1}]{") + r"(\d+)\}", t)]
def page_of(pos):
    p = None
    for s, n in marks:
        if s <= pos:
            p = n
    return p
pats = {
    "sref+item": re.compile(re.escape(BS + "sref{") + r"[^}]*\},\s*\(([ivx]+|[a-z])\)"),
    "mathrm{I}_": re.compile(re.escape(BS + "mathrm{I}_") + r"(\{[^}]*\}|.)"),
    "mathfrak{R}": re.compile(re.escape(BS + "mathfrak{R}")),
}
for name, p in pats.items():
    hits = [(page_of(m.start()), t.count("\n", 0, m.start()) + 1, m.group(0)) for m in p.finditer(t)]
    print(name, len(hits))
    if name != "mathfrak{R}":
        for h in hits:
            print("   p.", h[0], "line", h[1], h[2])
    else:
        from collections import Counter
        print("   by page:", dict(Counter(h[0] for h in hits)))
