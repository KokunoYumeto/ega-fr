import json, glob, re, sys
sys.stdout.reconfigure(encoding="utf-8")
base = r"user\Documents\ega_scan_check_20261101"
pat = re.compile(r"\\emph\{[A-Z]{1,4}\)")
for fn in sorted(glob.glob(base + r"\run_IV*\findings_*.json")):
    try:
        d = json.load(open(fn, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        f = x.get("fix") or {}
        o = f.get("old", "") if isinstance(f, dict) else ""
        if pat.search(o):
            print(fn.split("\\")[-2:], x.get("page"), x.get("kind"), x.get("convention"))
            print("   ", json.dumps(f, ensure_ascii=False)[:300])
            print("   ", (x.get("note") or "")[:200])
