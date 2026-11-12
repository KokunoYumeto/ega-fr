import json, glob, os, sys

root = r"user\Documents\ega_scan_check_20261101"
n = 0
seen = set()
for f in sorted(glob.glob(os.path.join(root, "run_*", "findings_*.json"))):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        fx = x.get("fix") or {}
        if x.get("convention") == 2 and fx and ("textsubscript" in fx.get("old", "") or "_{\\mathrm" in fx.get("old", "") or "_\\mathrm" in fx.get("old", "")):
            key = (fx["old"], fx["new"])
            n += 1
            if len(seen) < 25 and key not in seen:
                seen.add(key)
                print(os.path.basename(os.path.dirname(f)) + "/" + os.path.basename(f), "|", repr(fx["old"]), "->", repr(fx["new"]))
print("total", n)
