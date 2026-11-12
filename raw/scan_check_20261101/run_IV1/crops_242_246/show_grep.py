import json, glob, os, sys

root = r"user\Documents\ega_scan_check_20261101"
pat = sys.argv[1]
lim = int(sys.argv[2]) if len(sys.argv) > 2 else 15
n = 0
for f in sorted(glob.glob(os.path.join(root, "run_*", "findings_*.json"))):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        fx = x.get("fix") or {}
        s = json.dumps(x, ensure_ascii=False)
        if pat in s:
            n += 1
            if n <= lim:
                print(os.path.basename(os.path.dirname(f)) + "/" + os.path.basename(f), "| conv", x.get("convention"), "|", x.get("kind"), "|", json.dumps(fx, ensure_ascii=False)[:300])
                print("   note:", (x.get("note") or "")[:300])
print("total", n)
