"""Dry check (no writes): each fix's old occurs once in its page segment of the release file; apply in memory."""
import json, re, pathlib

SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-16-fr.tex")
F = json.load(open(r"user\Documents\ega_scan_check_20261101\run_IV4\findings_015_019.json", encoding="utf-8"))
t = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")

def seg(text, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(text)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            return s, cuts[i + 1][1] if i + 1 < len(cuts) else len(text)
    return None, None

bad = 0
for x in F:
    fx = x["fix"]
    if not fx:
        continue
    s, e = seg(t, x["page"])
    c = t[s:e].count(fx["old"])
    if c != 1:
        bad += 1
        print("BAD", x["page"], c, repr(fx["old"][:70]))
        continue
    t = t[:s] + t[s:e].replace(fx["old"], fx["new"]) + t[e:]
print("bad:", bad)
i = t.find("\\oldpage[IV-4]{17}")
print(t[i - 60:i + 120])
