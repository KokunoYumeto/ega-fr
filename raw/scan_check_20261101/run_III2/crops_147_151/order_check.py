"""Apply the fixes of findings_147_151.json in forward and in reverse order to the page files; report any edit whose
'old' is not unique at its turn, and whether both orders give the same text."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III2")
F = [x for x in json.load(open(RUN / "findings_147_151.json", encoding="utf-8")) if x.get("fix")]
for order in ("forward", "reverse"):
    seq = F if order == "forward" else list(reversed(F))
    texts = {p: (RUN / f"page_{p}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for p in range(147, 152)}
    bad = 0
    for x in seq:
        t = texts[x["page"]]
        if t.count(x["fix"]["old"]) != 1:
            bad += 1
            print(order, "FAIL", x["page"], repr(x["fix"]["old"])[:80])
            continue
        texts[x["page"]] = t.replace(x["fix"]["old"], x["fix"]["new"])
    print(order, "failures", bad)
    if order == "forward":
        fwd = dict(texts)
    else:
        print("same result:", all(fwd[p] == texts[p] for p in fwd))
