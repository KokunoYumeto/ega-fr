"""Show how earlier checkers classified paragraph breaks at page markers and env label issues."""
import glob
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
root = sys.argv[1]
shown = 0
for f in sorted(glob.glob(root + "/run_*/findings_*.json")):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        fix = x.get("fix") or {}
        old = fix.get("old", "") if isinstance(fix, dict) else ""
        if "\\oldpage" in old and "\n\n" in old and shown < 6:
            shown += 1
            print(f, x.get("kind"), repr(old[:80]), "->", repr(fix.get("new", "")[:80]))
            print("   note:", (x.get("note") or "")[:200])
