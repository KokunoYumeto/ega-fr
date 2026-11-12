"""Apply findings_218_223.json to copies of the page texts (in memory) and print the result for review."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
RUN = Path(r"user/Documents/ega_scan_check_20261101/run_III2")
F = json.loads((RUN / "findings_218_223.json").read_text(encoding="utf-8"))
pages = [int(a) for a in sys.argv[1:]] or list(range(218, 224))
for p in pages:
    t = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    for x in F:
        if x["page"] == p and x["fix"]:
            assert t.count(x["fix"]["old"]) == 1, (p, x["fix"]["old"])
            t = t.replace(x["fix"]["old"], x["fix"]["new"])
    print(f"===== {p}")
    print(t)
