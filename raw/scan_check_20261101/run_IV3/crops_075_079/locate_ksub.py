import re

p = (r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\current"
     r"\packages\IV3\native\ega4\ega4-9-fr.tex")
needle = "_{(\\boldsymbol{k}"
lines = open(p, encoding="utf-8").read().split("\n")
pg = None
out = []
for i, l in enumerate(lines, 1):
    m = re.search(r"oldpage\[IV-3\]\{(\d+)\}", l)
    if m:
        pg = int(m.group(1))
    n = l.count(needle)
    if n:
        out.append((i, pg, n))
print(out, sum(n for _, _, n in out))
