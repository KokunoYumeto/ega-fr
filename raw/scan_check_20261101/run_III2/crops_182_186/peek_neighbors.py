import json, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
base = r"user\Documents\ega_scan_check_20261101\run_III2"
for name in ("findings_177_181.json", "findings_187_191.json"):
    d = json.load(open(base + "\\" + name, encoding="utf-8"))
    print("==", name, len(d), collections.Counter((x["kind"], x["convention"]) for x in d).most_common())
    for x in d:
        fx = x.get("fix") or {}
        s = (fx.get("old") or "") + " => " + (fx.get("new") or "")
        if any(k in s for k in ("kappa", "Ab}", "textup", "setmin", "\\]\n\n", "\n\n")) or x["kind"] in ("formula", "misprint_in_print", "punctuation"):
            print(x["page"], x["kind"], x["convention"], "|", x["where"][:60], "|", repr(s[:150]), "|", (x.get("note") or "")[:120])
