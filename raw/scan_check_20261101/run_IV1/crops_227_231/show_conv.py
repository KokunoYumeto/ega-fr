"""Show a few recent findings with a given convention number (or a substring in the fix).

usage: python -I show_conv.py <convention-number|text> [max]
"""
import glob
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
E = r"user\Documents\ega_scan_check_20261101"
arg = sys.argv[1]
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 5
files = sorted(glob.glob(os.path.join(E, "run_*", "findings_*.json")), key=os.path.getmtime)
n = 0
for fn in files[::-1]:
    try:
        d = json.load(open(fn, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        hit = False
        if arg.isdigit():
            hit = x.get("convention") == int(arg)
        else:
            f = x.get("fix") or {}
            hit = arg in (f.get("old") or "") or arg in (f.get("new") or "") or arg in (x.get("note") or "")
        if hit:
            print(os.path.basename(os.path.dirname(fn)) + "/" + os.path.basename(fn), json.dumps(x, ensure_ascii=False)[:500])
            n += 1
            break
    if n >= mx:
        break
