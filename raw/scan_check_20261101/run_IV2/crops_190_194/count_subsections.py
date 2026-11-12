import re

path = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex"
t = open(path, encoding="utf-8").read()
subs = re.findall(r"\\subsection\*?\{((?:[^{}]|\{[^{}]*\})*)\}", t)
with_stop = [s for s in subs if s.rstrip().endswith(".")]
print("subsections:", len(subs), "with final full stop:", len(with_stop))
for s in subs:
    print(("  . " if s.rstrip().endswith(".") else "    ") + s[:70])
