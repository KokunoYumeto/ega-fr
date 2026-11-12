"""Count earlier checker fixes that turned italic capitals into upright ones (GLOBAL_ISSUES item 17)."""
import glob
import json
import re
import sys

base = sys.argv[1]
pat = re.compile(r"\\mathrm\{?[A-Z]\}?|\\mathrm [A-Z]|\\textup\{[A-Z]\}")
cnt = 0
ex = []
files = []
for sub in ("run_0IV1", "run_III1", "run_II", "run_0III", "run_III2"):
    files += sorted(glob.glob(f"{base}/{sub}/findings_*.json"))
for f in files:
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        fx = x.get("fix") or {}
        if not isinstance(fx, dict):
            continue
        new = fx.get("new", "")
        old = fx.get("old", "")
        if pat.search(new) and not pat.search(old):
            cnt += 1
            if len(ex) < 20:
                ex.append((f.split("/")[-2] + "/" + f.split("/")[-1][-20:], x.get("page"), x.get("kind"),
                           (x.get("scan") or "")[:100], old[:50], new[:60]))
print("count", cnt)
for e in ex:
    print(e)
