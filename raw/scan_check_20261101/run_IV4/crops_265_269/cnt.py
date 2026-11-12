import sys, pathlib
src = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-21a-fr.tex").read_text(encoding="utf-8")
for s in pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").split("\n=====\n"):
    s = s.rstrip("\n")
    print(src.count(s), repr(s[:90]))
