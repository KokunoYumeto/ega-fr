"""Check findings_107_111.json: each fix's "old" occurs exactly once in its page_NNN.tex (LF-normalised), and the
fixes apply one after another in list order (as apply_fixes.py does). Also replays the non-misprint fixes alone
(corrected-edition replay) to make sure they apply without the misprint reversions. Read-only on the .tex files."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
F = json.loads((RUN / "findings_107_111.json").read_text(encoding="utf-8"))
pages = sorted({x["page"] for x in F})
orig = {p: (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for p in pages}
bad = 0
for p in pages:
    seq = orig[p].split("\n", 1)[1]  # segment from \oldpage on
    cur = seq
    for i, x in enumerate([x for x in F if x["page"] == p]):
        fx = x["fix"]
        if not fx:
            continue
        n0 = orig[p].count(fx["old"])
        n1 = cur.count(fx["old"])
        if n0 != 1 or n1 != 1:
            bad += 1
            print("PROBLEM p", p, i, repr(fx["old"][:60]), "in original:", n0, "at application:", n1)
        else:
            cur = cur.replace(fx["old"], fx["new"])
    # corrected-edition replay: skip misprint reversions
    cur2 = seq
    for x in [x for x in F if x["page"] == p and x["kind"] != "misprint_in_print"]:
        fx = x["fix"]
        if cur2.count(fx["old"]) != 1:
            bad += 1
            print("REPLAY PROBLEM p", p, repr(fx["old"][:60]), cur2.count(fx["old"]))
        else:
            cur2 = cur2.replace(fx["old"], fx["new"])
    # balance checks on the result
    for name, txt in (("diplomatic", cur), ("corrected", cur2)):
        d = txt.count("$") % 2
        lb, rb = txt.count("\\["), txt.count("\\]")
        br = txt.count("{") - txt.count("}")
        if d or lb != rb or br:
            print("BALANCE", p, name, "odd $:", d, "\\[ vs \\]:", lb, rb, "brace diff:", br)
counts = {}
for x in F:
    c = counts.setdefault(x["page"], [0, 0, 0])
    c[1 if x["kind"] == "convention" else 2 if x["kind"] == "misprint_in_print" else 0] += 1
print("problems:", bad)
print("counts (normal/convention/misprint):", counts)
