"""List convention-7 findings of earlier IV-4 checkers whose 'where' or note mentions subtraction."""
import json, glob, re, sys

base = r"user\Documents\ega_scan_check_20261101\run_IV4"
pat = re.compile(sys.argv[1]) if len(sys.argv) > 1 else re.compile(r"1\s*[-—]|subtract|minus", re.I)
for f in sorted(glob.glob(base + r"\findings_*.json")):
    d = json.load(open(f, encoding="utf-8"))
    for x in d:
        if x.get("convention") != 7:
            continue
        fx = x.get("fix") or {}
        text = " ".join([x.get("where", ""), x.get("scan", ""), x.get("note") or "", fx.get("old", "")])
        if pat.search(text):
            print(f.split("\\")[-1], x["page"], repr(x["where"])[:90], "|", repr(fx.get("old"))[:60], "->", repr(fx.get("new"))[:60], "|", (x.get("note") or "")[:120])
