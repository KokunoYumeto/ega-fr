import json, glob, collections, sys
sys.stdout.reconfigure(encoding="utf-8")
c = collections.Counter()
ex = {}
for f in glob.glob(r"user\Documents\ega_scan_check_20261101\run_*\findings_*.json"):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        fx = x.get("fix") or {}
        new = fx.get("new") or ""
        old = fx.get("old") or ""
        if "\emph{" in new and "\emph{" not in old:
            key = (x.get("kind"), x.get("convention"))
            c[key] += 1
            ex.setdefault(key, (f.split("\\")[-2] + "/" + f.split("\\")[-1], x.get("where", "")[:70]))
for k, v in c.most_common():
    print(v, k, ex[k])
