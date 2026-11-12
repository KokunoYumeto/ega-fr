"""Check findings_232_236.json: valid JSON, each fix 'old' occurs exactly once in its
page_NNN.tex (CRLF normalised to LF), no stray control characters, and counts per page."""
import json
import sys
from collections import Counter, defaultdict

run = sys.argv[1]
data = json.load(open(run + "/findings_232_236.json", encoding="utf-8"))
pages = {}
ok = True
counts = defaultdict(Counter)
for i, f in enumerate(data):
    p = f["page"]
    if p not in pages:
        pages[p] = open(f"{run}/page_{p:03d}.tex", encoding="utf-8", newline="").read().replace("\r\n", "\n")
    text = pages[p]
    for key in ("page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"):
        if key not in f:
            print(i, "missing key", key); ok = False
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        print(i, "misprint without corrected"); ok = False
    if f["kind"] != "misprint_in_print" and "corrected" in f:
        print(i, "corrected on non-misprint"); ok = False
    if (f["kind"] == "convention") != (f["convention"] is not None):
        print(i, "convention field mismatch"); ok = False
    cat = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    counts[p][cat] += 1
    fx = f["fix"]
    if fx is None:
        continue
    for s in (fx["old"], fx["new"]):
        bad = [c for c in s if ord(c) < 32 and c != "\n"]
        if bad:
            print(i, "control chars", [hex(ord(c)) for c in bad]); ok = False
    n = text.count(fx["old"])
    if n != 1:
        print(i, p, "old occurs", n, "times:", repr(fx["old"])); ok = False
# overlapping edits on the same page
for p in pages:
    spans = []
    for i, f in enumerate(data):
        if f["page"] == p and f["fix"]:
            s = pages[p].find(f["fix"]["old"])
            spans.append((s, s + len(f["fix"]["old"]), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            print("overlap on page", p, "entries", a[2], b[2]); ok = False
print("entries", len(data), "ok" if ok else "PROBLEMS")
for p in sorted(counts):
    c = counts[p]
    print(p, f"{c['normal']}/{c['convention']}/{c['misprint']}")
