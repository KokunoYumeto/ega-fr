import os
D = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\current\packages\BASE\native\ega3"
pats = [r"\mathfrak{Tor}", r"\boldsymbol{\mathscr{T}\!or}", r"\mathscr{T}\!or", r"\operatorname{Tor}",
        r"\mathbf{Tor}", r"\kappa(", r"\boldsymbol{k}(", r"\mathbf{k}(", r"\leadsto", r"\mapsto"]
for fn in ["ega3-6-fr.tex", "ega3-7-fr.tex"]:
    s = open(os.path.join(D, fn), encoding="utf-8").read()
    print(fn, {p: s.count(p) for p in pats})
G = r"user\Documents\ega_scan_check_20261101\GLOBAL_ISSUES.md"
g = open(G, encoding="utf-8").read()
for line in g.splitlines():
    if any(w in line for w in ("Tor", "kappa", "roundhand", "hypertor", "item 42", "52.", "53.", "54.", "55.")):
        print("GI:", line[:300])
print(os.path.getmtime(G))
