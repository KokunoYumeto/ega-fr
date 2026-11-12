import re, sys, pathlib
src = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega1\ega0-1-fr.tex")
t = src.read_text(encoding="utf-8")
for n in sys.argv[1:]:
    tag = "\\oldpage[0\\textsubscript{I}]{" + n + "}"
    s = t.find(tag)
    print("== marker", n, "at char", s, "count", t.count(tag))
    print(repr(t[s-160:s+70]))
