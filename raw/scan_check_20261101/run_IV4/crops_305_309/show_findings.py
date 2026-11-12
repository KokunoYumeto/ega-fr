"""Print the findings of findings_305_309.json one per line for review."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
F = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4\findings_305_309.json")
for i, e in enumerate(json.load(open(F, encoding="utf-8"))):
    fx = e["fix"]
    print(i, e["page"], e["kind"], e["convention"], e["confidence"], "|", e["where"][:80], "|",
          repr(fx["old"])[:70] if fx else None, "=>", repr(fx["new"])[:80] if fx else None,
          "| corrected:" + e["corrected"] if "corrected" in e else "")
