import json, collections
F = json.load(open(r"user\Documents\ega_scan_check_20261101\run_II\findings_145_149.json", encoding="utf-8"))
bad = [f for f in F if f["fix"] and any(ch in f["fix"]["new"] + f["fix"]["old"] for ch in "\t\x08\x0c")]
print("control chars:", len(bad))
c = collections.Counter()
BS = chr(92)
for f in F:
    if f["fix"]:
        for tok in ("textup{", "textbf{", "boldsymbol{k}", "emph{"):
            c[tok] += f["fix"]["new"].count(BS + tok)
print(dict(c))
for f in F:
    if f["kind"] in ("misprint_in_print", "other", "punctuation") or "provient" in (f["fix"] or {}).get("old", ""):
        print(f["page"], f["kind"], json.dumps(f["fix"], ensure_ascii=False), "| corrected:", f.get("corrected"))
