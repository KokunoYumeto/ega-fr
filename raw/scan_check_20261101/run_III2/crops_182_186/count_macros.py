import re, sys
sys.stdout.reconfigure(encoding="utf-8")
p = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega3\ega3-7-fr.tex"
t = open(p, encoding="utf-8").read()
for pat in [r"\mathcal K", r"\kappa", r"\mathbf{Ab}", r"\longmapsto", r"\mapsto", r"\leadsto", r"\["]:
    n = t.count(pat)
    if pat == r"\mapsto":
        n -= t.count(r"\longmapsto") * 0  # \longmapsto does not contain the substring \mapsto
    print(pat, n)
