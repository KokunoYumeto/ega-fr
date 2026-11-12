"""Re-read findings_031_035.json, apply every fix in memory, and show the changed lines."""
import difflib
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
RUN = Path(r"user\Documents\ega_scan_check_20261101\run_0IV1")
data = json.loads((RUN / "findings_031_035.json").read_text(encoding="utf-8"))
keys = {"page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"}
for f in data:
    extra = set(f) - keys - {"corrected"}
    missing = keys - set(f)
    assert not extra and not missing, (f["where"], extra, missing)
    assert ("corrected" in f) == (f["kind"] == "misprint_in_print"), f["where"]
    assert (f["convention"] is not None) == (f["kind"] == "convention"), f["where"]

for p in sorted({f["page"] for f in data}):
    src = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    assert "\r" not in src
    out = src
    for f in data:
        if f["page"] == p and f["fix"]:
            assert out.count(f["fix"]["old"]) == 1, f["where"]
            out = out.replace(f["fix"]["old"], f["fix"]["new"])
    print(f"===== page {p}")
    for line in difflib.unified_diff(src.splitlines(), out.splitlines(), lineterm="", n=0):
        if not line.startswith(("---", "+++")):
            print(line)
