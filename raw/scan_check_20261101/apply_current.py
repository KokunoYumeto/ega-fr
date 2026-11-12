"""Apply hand-checked items (old -> new) to the CORRECTED (current) release sources inside an explicit region.

usage: python apply_manual.py ITEMS.json [--dry]
Each item: {"file": <release file name, e.g. ega1-6-fr.tex>, "part": "I", "page": N,
            "region": "page" | "before_first_marker" | "file", "old": ..., "new": ..., "why": ...}
"page" = from \\oldpage[PART]{N} to the next marker; "before_first_marker" = the file's opening text,
which continues the previous page. CRLF in old/new is turned into LF. The old text must occur exactly once
in the region. Applied items are appended to FIXLOG.jsonl.
"""
import json
import pathlib
import re
import sys

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
ROOT = E / "ega-fr/editions/2026-10-24-r20/current/packages"
dry = "--dry" in sys.argv
items = json.load(open([a for a in sys.argv[1:] if a != "--dry"][0], encoding="utf-8"))
log = None if dry else open(E / "FIXLOG_CURRENT.jsonl", "a", encoding="utf-8")
for x in items:
    path = next(ROOT.rglob(x["file"]))
    t = path.read_text(encoding="utf-8")
    old = x["old"].replace("\r\n", "\n")
    new = x["new"].replace("\r\n", "\n")
    part = x.get("part", "I")
    marker = re.compile(r"\\oldpage\[" + re.escape(part) + r"\]\{(\d+)\}")
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    if x["region"] == "page":
        i = [k for k, (n, s) in enumerate(cuts) if n == int(x["page"])][0]
        s, e = cuts[i][1], (cuts[i + 1][1] if i + 1 < len(cuts) else len(t))
    elif x["region"] == "before_first_marker":
        s, e = 0, cuts[0][1]
    else:
        s, e = 0, len(t)
    seg = t[s:e]
    n = seg.count(old)
    if n != 1:
        print(f"SKIP p.{x['page']} {x['file']}: old occurs {n} times in the region: {old[:60]!r}")
        continue
    t = t[:s] + seg.replace(old, new) + t[e:]
    if not dry:
        path.write_text(t, encoding="utf-8", newline="")
        log.write(json.dumps(dict(file=str(path), part=part, page=int(x["page"]), old=old, new=new,
                                  kind=x.get("kind", "manual"), why=x.get("why"), source="apply_current"),
                             ensure_ascii=False) + "\n")
    print(f"{'would apply' if dry else 'applied'} p.{x['page']} {x['file']} ({x['region']}): {old[:50]!r}")
