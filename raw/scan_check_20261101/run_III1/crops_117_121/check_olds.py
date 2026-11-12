"""Read-only checks of findings_117_121.json.

1. every fix "old" occurs exactly once in its page_NNN.tex (CRLF normalised to LF);
2. applying the fixes in file order to the release segment (\\oldpage[III]{N} .. next marker of ega3-1-fr.tex,
   in memory only) finds each "old" exactly once at the moment it is applied, as apply_fixes.py requires;
3. no fix "old" lies before the page's \\oldpage marker in page_NNN.tex.
Nothing is written.
"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\BASE\native\ega3\ega3-1-fr.tex")
findings = json.load(open(RUN / "findings_117_121.json", encoding="utf-8"))
marker = re.compile(r"\\oldpage\[III\]\{(\d+)\}")
rel = REL.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(rel)]
segs = {}
for i, (n, s) in enumerate(cuts):
    segs[n] = rel[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(rel)]

bad = 0
work = {}
for i, x in enumerate(findings):
    fix = x.get("fix")
    if not fix:
        continue
    p = x["page"]
    page = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    c = page.count(fix["old"])
    pos = page.find(fix["old"])
    mpos = page.find(f"\\oldpage[III]{{{p}}}")
    if c != 1 or pos < mpos:
        bad += 1
        print(f"[page file] #{i} p{p}: count {c}, before marker {pos < mpos}: {fix['old']!r}")
    seg = work.setdefault(p, segs[p])
    c2 = seg.count(fix["old"])
    if c2 != 1:
        bad += 1
        print(f"[release seq] #{i} p{p}: count {c2}: {fix['old']!r}")
    else:
        work[p] = seg.replace(fix["old"], fix["new"])

# the page files should equal the release segments up to the trailing continuation comment
for p in sorted({x["page"] for x in findings}):
    page = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    body = page[page.find("\\oldpage"):]
    if body.strip() != segs[p].strip():
        print(f"note: page_{p:03d}.tex differs from the release segment")
print("problems:", bad, "| findings:", len(findings), "| with fix:", sum(1 for x in findings if x.get("fix")))
