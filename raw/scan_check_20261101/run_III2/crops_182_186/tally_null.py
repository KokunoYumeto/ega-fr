import json, glob, collections, sys
sys.stdout.reconfigure(encoding="utf-8")
c = collections.Counter()
ex = []
for f in glob.glob(r"user\Documents\ega_scan_check_20261101\run_*\findings_*.json"):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        if not x.get("fix") and x.get("kind") != "misprint_in_print":
            c[(x.get("kind"), x.get("convention"))] += 1
            if len(ex) < 8:
                ex.append((f.split("\\")[-2], x.get("page"), x.get("kind"), (x.get("note") or "")[:150]))
print(c.most_common())
for e in ex:
    print(e)
