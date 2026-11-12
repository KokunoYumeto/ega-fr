import json, glob, re, sys
sys.stdout.reconfigure(encoding="utf-8")
base = r"user\Documents\ega_scan_check_20261101"
pat_old = re.compile(r"\$[a-g]'*\)\$")
seen = 0
kinds = {}
for fn in sorted(glob.glob(base + r"\run_*\findings_*.json")):
    try:
        d = json.load(open(fn, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        f = x.get("fix") or {}
        o = f.get("old", "") or ""
        nw = f.get("new", "") or ""
        if pat_old.search(o) and "textup{" in nw:
            k = (x.get("kind"), x.get("convention"))
            kinds[k] = kinds.get(k, 0) + 1
            seen += 1
            if seen <= 5:
                print(fn.split("\\")[-2:], json.dumps(x, ensure_ascii=False)[:450])
                print("--")
print(seen, kinds)
