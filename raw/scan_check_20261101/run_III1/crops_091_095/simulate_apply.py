import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
F = json.loads((RUN / "findings_091_095.json").read_text(encoding="utf-8"))
texts = {}
bad = 0
for d in F:
    p = d["page"]
    if p not in texts:
        texts[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    fx = d["fix"]
    if not fx:
        continue
    n = texts[p].count(fx["old"])
    if n != 1:
        bad += 1
        print("sequential apply fails:", p, n, repr(fx["old"][:60]))
        continue
    texts[p] = texts[p].replace(fx["old"], fx["new"], 1)
print("sequential application:", "ok" if bad == 0 else f"{bad} failures")
# brace balance check of the edited pages
for p, t in texts.items():
    print(p, "braces", t.count("{") - t.count("}"), "dollars", t.count("$") % 2)
print(texts[94][texts[94].find("posons"):texts[94].find("posons") + 330])
