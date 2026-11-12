"""Check that every fix's 'old' occurs exactly once in its page file (CRLF normalized to LF),
and that the fixes of each page can be applied in sequence."""
import json
import pathlib
import sys
from collections import Counter, defaultdict

run = pathlib.Path(r"user/Documents/ega_scan_check_20261101/run_II")
findings = json.loads((run / "findings_185_189.json").read_text(encoding="utf-8"))
ok = True
by_page = defaultdict(list)
kinds = defaultdict(Counter)
for i, f in enumerate(findings):
    for key in ("page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"):
        if key not in f:
            print("missing key", key, "in finding", i)
            ok = False
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        print("misprint without corrected:", i)
        ok = False
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    kinds[f["page"]][k] += 1
    if f["fix"] is None:
        continue
    text = (run / f"page_{f['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    n = text.count(f["fix"]["old"])
    if n != 1:
        print(f"page {f['page']} finding {i}: old occurs {n} times: {f['fix']['old']!r}")
        ok = False
    by_page[f["page"]].append(f["fix"])
for page, fixes in sorted(by_page.items()):
    text = (run / f"page_{page:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    for fx in fixes:
        n = text.count(fx["old"])
        if n != 1:
            print(f"sequential: page {page}: old occurs {n} times: {fx['old']!r}")
            ok = False
            continue
        text = text.replace(fx["old"], fx["new"])
    out = run / "crops_185_189" / f"applied_{page:03d}.tex"
    out.write_text(text, encoding="utf-8", newline="\n")
for page in sorted(kinds):
    c = kinds[page]
    print(page, f"{c['normal']}/{c['convention']}/{c['misprint']}")
print("total", len(findings), "OK" if ok else "PROBLEMS")
sys.exit(0 if ok else 1)
