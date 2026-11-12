"""Check findings_275_279.json: (1) each fix's old occurs exactly once in its page_NNN.tex (CRLF normalised);
(2) replay all fixes in list order on an in-memory copy of the current release file with apply_fixes.py's
segment logic (no file is written except the replay copy in this folder); (3) report problems.
usage: python simulate.py"""
import json
import pathlib
import re

D = pathlib.Path(__file__).resolve().parent
R = D.parent
SRC = (R.parent / "ega-fr" / "editions" / "2026-10-24-r20" / "diplomatic" / "packages" / "IV4" / "native"
       / "ega4" / "ega4-21b-fr.tex")
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(t)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


findings = json.loads((R / "findings_275_279.json").read_text(encoding="utf-8"))
pages = {p: (R / f"page_{p}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for p in range(275, 280)}
t = SRC.read_text(encoding="utf-8")
orig = t
bad = 0
keys = {"page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"}
for k, x in enumerate(findings):
    miss = keys - set(x)
    if miss:
        print(k, "missing keys", miss); bad += 1
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print(k, "misprint without corrected"); bad += 1
    if (x["kind"] == "convention") != (x["convention"] is not None):
        print(k, "kind/convention mismatch"); bad += 1
    fix = x.get("fix")
    if not fix:
        continue
    old, new = fix["old"], fix["new"]
    c = pages[x["page"]].count(old)
    if c != 1:
        print(k, "page", x["page"], "old occurs", c, "times in page file:", repr(old[:80])); bad += 1
    s, e = locate(t, x["page"])
    seg = t[s:e]
    c2 = seg.count(old)
    if c2 != 1:
        print(k, "page", x["page"], "REPLAY: old occurs", c2, "times in segment:", repr(old[:80])); bad += 1
        continue
    t = t[:s] + seg.replace(old, new) + t[e:]
print("problems:", bad, "findings:", len(findings), "with fix:", sum(1 for x in findings if x.get("fix")))
(D / "replay_ega4-21b.tex").write_text(t, encoding="utf-8", newline="")
# show the replayed segment of pp. 275-279 marker positions
for m in marker.finditer(t):
    n = int(m.group(1))
    if 274 <= n <= 280:
        print(n, repr(t[max(0, m.start() - 60):m.end() + 60]))
