"""Read-only: check every fix's old string against the release file's page segments (LF)."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
rel = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\IV1\native\ega4\ega0-21-fr.tex")
t = rel.read_bytes().decode("utf-8")
print("CR in release:", "\r" in t)
F = json.load(open(r"user\Documents\ega_scan_check_20261101\run_0IV1\findings_166_170.json",
                   encoding="utf-8"))
marker = re.compile(r"\\oldpage\[0\\textsubscript\{IV-1\}\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
segs = {}
for i, (n, s) in enumerate(cuts):
    e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
    segs[n] = (s, e)

# apply sequentially, as apply_fixes.py does, on a copy in memory
cur = t
bad = 0
for i, x in enumerate(F):
    if not x["fix"]:
        continue
    cuts2 = [(int(m.group(1)), m.start()) for m in marker.finditer(cur)]
    s = e = None
    for j, (n, st) in enumerate(cuts2):
        if n == x["page"]:
            s = st
            e = cuts2[j + 1][1] if j + 1 < len(cuts2) else len(cur)
            break
    seg = cur[s:e]
    old, new = x["fix"]["old"], x["fix"]["new"]
    c = seg.count(old)
    if c != 1:
        bad += 1
        print("BAD", i, x["page"], c, repr(old)[:90])
        continue
    cur = cur[:s] + seg.replace(old, new) + cur[e:]
print("bad", bad)

for p in range(166, 171):
    s, e = segs[p]
    pg = pathlib.Path(rf"user\Documents\ega_scan_check_20261101\run_0IV1\page_{p}.tex").read_text(
        encoding="utf-8")
    body = pg.split("\n", 1)[1]
    seg = t[s:e]
    print(p, "release segment == page file body:", seg.rstrip("\n") == body.rstrip("\n"))
