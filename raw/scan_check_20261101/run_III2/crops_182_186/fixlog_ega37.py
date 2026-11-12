import json, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
c = collections.Counter()
rows = []
for line in open(r"user\Documents\ega_scan_check_20261101\FIXLOG.jsonl", encoding="utf-8"):
    x = json.loads(line)
    if "ega3-7" in x.get("file", ""):
        c[(x.get("page"), x.get("source"))] += 1
        rows.append(x)
print(sorted(c.items()))
for x in rows:
    s = x["old"] + " => " + x["new"]
    if any(k in s for k in ("kappa", "Ab}", "leadsto", "boldsymbol")):
        print(x["page"], x.get("kind"), x.get("convention"), repr(x["old"][:70]), "=>", repr(x["new"][:90]))
