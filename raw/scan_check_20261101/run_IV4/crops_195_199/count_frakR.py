import re, pathlib
D = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4")
mk = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
fr = re.compile(r"\\mathfrak\s*\{?R")
for fn in ["ega4-16-fr.tex", "ega4-17-fr.tex", "ega4-18-fr.tex", "ega4-20-fr.tex", "ega4-21a-fr.tex", "ega4-21b-fr.tex", "ega4-21c-fr.tex"]:
    t = (D / fn).read_text(encoding="utf-8")
    cuts = [(int(m.group(1)), m.start()) for m in mk.finditer(t)]
    cnt = {}
    for m in fr.finditer(t):
        pg = 0
        for n, s in cuts:
            if s <= m.start():
                pg = n
        cnt[pg] = cnt.get(pg, 0) + 1
    print(fn, sum(cnt.values()), dict(sorted(cnt.items())))
