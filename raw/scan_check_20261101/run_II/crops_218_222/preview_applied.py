"""Apply findings_218_222.json to copies of the page texts (in memory) and print the result for review."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
F = json.load(open(RUN / "findings_218_222.json", encoding="utf-8"))
pages = [int(a) for a in sys.argv[1:]] or sorted({x["page"] for x in F})
for p in pages:
    t = (RUN / f"page_{p}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    for x in F:
        if x["page"] == p and x["fix"]:
            assert t.count(x["fix"]["old"]) == 1, x
            t = t.replace(x["fix"]["old"], x["fix"]["new"])
    # crude balance checks
    body = t.split("\n", 1)[1]
    print(f"===== page {p}: braces {body.count('{') - body.count('}')}, dollars {body.count('$') % 2}")
    print(body)
