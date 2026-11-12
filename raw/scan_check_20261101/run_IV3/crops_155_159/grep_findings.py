import glob
import json
import re
import sys

# usage: grep_findings.py <regex> [field: old|new|any] [glob]
pat = re.compile(sys.argv[1])
field = sys.argv[2] if len(sys.argv) > 2 else "any"
pattern = sys.argv[3] if len(sys.argv) > 3 else r"user\Documents\ega_scan_check_20261101\run_*\findings_*.json"
n = 0
for f in sorted(glob.glob(pattern)):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        fx = x.get("fix") or {}
        old, new = fx.get("old") or "", fx.get("new") or ""
        hay = {"old": old, "new": new}.get(field, json.dumps(x, ensure_ascii=False))
        if pat.search(hay):
            n += 1
            print(f.split("\\")[-2] + "/" + f.split("\\")[-1], x.get("page"), x.get("kind"), x.get("convention"), "|",
                  old[:90].replace("\n", "/"), "->", new[:90].replace("\n", "/"), "|", (x.get("note") or "")[:160])
            if n >= int(sys.argv[4]) if len(sys.argv) > 4 else n >= 15:
                raise SystemExit
