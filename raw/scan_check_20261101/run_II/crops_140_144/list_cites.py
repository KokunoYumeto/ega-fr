import re
p = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\current\packages\BASE\native\ega2\ega2-1-fr.tex"
t = open(p, encoding="utf-8").read()
marks = [(m.start(), m.group(1)) for m in re.finditer(r"\\oldpage\[II\]\{(\d+)\}", t)]
for m in re.finditer(r"\\cite\[[^\]]*\]\{[^}]*\}", t):
    pg = [q for s, q in marks if s < m.start()]
    print(pg[-1] if pg else "?", m.group(0))
