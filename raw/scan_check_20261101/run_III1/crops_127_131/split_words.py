import json
import pathlib
import re

# 1) words hyphenated across an \oldpage marker in the EGA III release file (how the transcription writes them)
rel = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega3\ega3-1-fr.tex")
t = rel.read_text(encoding="utf-8")
pat = re.compile(r"(\S{0,14})-[ \t]*\n(?:[ \t]*\n)*\\oldpage\[[^\]]*\]\{\d+\}[^\n]*\n(?:[ \t]*\n)*(\S{0,14})")
hits = [m.group(0) for m in pat.finditer(t)]
print("hyphen before a marker in ega3-1:", len(hits))
for h in hits[:12]:
    print("  ", repr(h))
# also words split across a marker with a % join
pat2 = re.compile(r"(\S{0,14})%[ \t]*\n\\oldpage\[[^\]]*\]\{\d+\}[^\n]*\n(\S{0,14})")
h2 = [m.group(0) for m in pat2.finditer(t)]
print("percent-joined splits:", len(h2))
for h in h2[:6]:
    print("  ", repr(h))

# 2) earlier fixes in FIXLOG that touch a hyphen next to a page marker
n = 0
with open(r"user\Documents\ega_scan_check_20261101\FIXLOG.jsonl", encoding="utf-8") as f:
    for line in f:
        d = json.loads(line)
        o, nw = d.get("old") or "", d.get("new") or ""
        if "oldpage" in o + nw and re.search(r"-\s*\n", o) and n < 10:
            n += 1
            print("FIX", d.get("part"), d.get("page"), repr(o)[:150], "=>", repr(nw)[:150])
print("fixes found:", n)
