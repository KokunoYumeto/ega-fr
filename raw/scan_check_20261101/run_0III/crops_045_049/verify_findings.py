"""Check findings_045_049.json: each fix's old occurs exactly once in its page file (LF), and all fixes of a page
apply one after another in file order and in reverse order (no overlapping edits). Also checks brace balance of
each page after all edits and reports math-mode dollar parity changes."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0III")
F = json.load(open(RUN / "findings_045_049.json", encoding="utf-8"))
pages = {}
for p in range(45, 50):
    t = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    pages[p] = t
bad = 0
for i, x in enumerate(F):
    fx = x.get("fix")
    if not fx:
        continue
    c = pages[x["page"]].count(fx["old"])
    if c != 1:
        bad += 1
        print("COUNT", c, "finding", i, x["page"], x["where"][:70])
for order in ("forward", "reverse"):
    for p in range(45, 50):
        t = pages[p]
        idx = [i for i, x in enumerate(F) if x["page"] == p and x.get("fix")]
        if order == "reverse":
            idx = idx[::-1]
        for i in idx:
            fx = F[i]["fix"]
            if t.count(fx["old"]) != 1:
                bad += 1
                print(order, "FAILS at finding", i, "page", p, F[i]["where"][:70])
                continue
            t = t.replace(fx["old"], fx["new"])
        if order == "forward":
            def bal(s):
                return s.count("{") - s.count("}") - (s.count("\\{") - s.count("\\}"))
            print("page", p, "brace balance before/after:", bal(pages[p]), bal(t),
                  "| $ count before/after:", pages[p].count("$") % 2, t.count("$") % 2,
                  "| \\[ \\] before/after:", pages[p].count("\\[") - pages[p].count("\\]"), t.count("\\[") - t.count("\\]"))
            (RUN / "crops_045_049" / f"applied_{p:03d}.tex").write_text(t, encoding="utf-8")
print("problems:", bad, "| findings:", len(F))
