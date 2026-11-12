"""Search earlier findings files for fixes whose old/new match patterns.

usage: python search_findings.py OLD_REGEX [NEW_NOT_REGEX] [LIMIT]
"""
import glob
import json
import re
import sys

BASE = r"user/Documents/ega_scan_check_20261101"
old_re = re.compile(sys.argv[1].replace("BS", chr(92)*2))
new_not = re.compile(sys.argv[2].replace("BS", chr(92)*2)) if len(sys.argv) > 2 and sys.argv[2] else None
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 30
n = 0
for f in sorted(glob.glob(BASE + "/run_*/findings_*.json")):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        fx = x.get("fix") or {}
        o = fx.get("old") or ""
        nw = fx.get("new") or ""
        if old_re.search(o) and (new_not is None or not new_not.search(nw)):
            n += 1
            if n <= limit:
                print(f.split("/")[-1], x["page"], "|", x.get("kind"), x.get("convention"), "|",
                      o[:70].replace("\n", " "), "=>", nw[:80].replace("\n", " "), "|",
                      (x.get("note") or "")[:200])
print(n)
