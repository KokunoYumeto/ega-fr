import json
from pathlib import Path

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_0III")
data = json.loads((RUN / "findings_010_014.json").read_text(encoding="utf-8"))
keys = {"page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"}
kinds = {"word", "formula", "symbol", "font", "italics", "missing", "extra", "number",
         "punctuation", "misprint_in_print", "convention", "marker", "other"}
bad = 0
for f in data:
    missing = keys - f.keys()
    if missing:
        bad += 1; print("missing keys", missing, f["where"])
    if f["kind"] not in kinds:
        bad += 1; print("bad kind", f["kind"])
    if (f["kind"] == "misprint_in_print") != ("corrected" in f):
        bad += 1; print("corrected field mismatch", f["where"])
    if (f["kind"] == "convention") != (f["convention"] is not None):
        bad += 1; print("convention number mismatch", f["where"])
    if f["fix"] is None:
        continue
    t = (RUN / f"page_{f['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    n = t.count(f["fix"]["old"])
    if n != 1:
        bad += 1; print(f"old occurs {n}x on p{f['page']}: {f['fix']['old']!r}")
print(len(data), "findings;", "all checks passed" if not bad else f"{bad} problems")
