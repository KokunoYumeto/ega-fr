"""Check that each fix's old string occurs once in its page segment of the
source file (text from the page's oldpage marker to the next one), and that
the page_NNN.tex body matches that segment.

Usage: python -I check_segments.py <ega4-1-fr.tex> <findings.json> <run dir>
"""
import json
import sys

src_path, findings_path, run = sys.argv[1:4]
src = open(src_path, encoding="utf-8").read()
findings = json.load(open(findings_path, encoding="utf-8"))
pages = sorted({f["page"] for f in findings})
segs = {}
for p in pages:
    a = src.index("\\oldpage[IV-1]{%d}" % p)
    nxt = src.find("\\oldpage[IV-1]{%d}" % (p + 1), a)
    segs[p] = src[a: nxt if nxt >= 0 else len(src)]
bad = 0
for f in findings:
    if f["fix"] is None:
        continue
    n = segs[f["page"]].count(f["fix"]["old"])
    if n != 1:
        bad += 1
        print("segment count", n, f["page"], ascii(f["fix"]["old"]))
print("checked", len(findings), "bad", bad)
for p in pages:
    t = open(f"{run}/page_{p}.tex", encoding="utf-8").read().replace("\r\n", "\n")
    body = t.split("\n", 1)[1].strip()
    print(p, "page body equals source segment:", body == segs[p].strip(),
          "| body contained in segment:", body in segs[p])
