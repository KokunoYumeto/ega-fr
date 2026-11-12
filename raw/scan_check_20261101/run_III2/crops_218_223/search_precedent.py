"""Search earlier findings for marker fixes that split a word (percent sign before \\oldpage)."""
import glob
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
BASE = r"user/Documents/ega_scan_check_20261101/"
n = 0
for f in sorted(glob.glob(BASE + "run_*/findings_*.json")) + sorted(glob.glob(BASE + "MANUAL_*.json")):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    if not isinstance(d, list):
        continue
    for x in d:
        fx = x.get("fix") or {}
        if not isinstance(fx, dict):
            continue
        nw = fx.get("new") or ""
        if "%\n\\oldpage" in nw or ("\\oldpage" in nw and "-%" in nw) or "-}%" in nw:
            n += 1
            if n <= 8:
                print(f, x.get("page"), x.get("kind"), repr(nw[:220]), "|", (x.get("note") or "")[:220])
                print()
print(n)
