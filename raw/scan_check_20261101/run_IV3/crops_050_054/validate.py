import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
F = json.loads((RUN / "findings_050_054.json").read_text(encoding="utf-8"))
ok = True
pages = sorted({f["page"] for f in F})
for p in pages:
    text = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    cur = text
    for i, f in enumerate(F):
        if f["page"] != p or not f["fix"]:
            continue
        old, new = f["fix"]["old"], f["fix"]["new"]
        n0 = text.count(old)
        n1 = cur.count(old)
        if n0 != 1 or n1 != 1:
            ok = False
            print("PROBLEM", p, i, "orig count", n0, "count at apply time", n1, repr(old[:80]))
        cur = cur.replace(old, new, 1)
        if old == new:
            ok = False
            print("NO-OP", p, i)
    # sanity: the number of \mathcal C left on the page after all fixes
    print(p, "mathcal C left:", cur.count("\\mathcal C"), "| mathbf{Pro} left:", cur.count("\\mathbf{Pro}"),
          "| mathbf{Sch} left:", cur.count("\\mathbf{Sch}"), "| \\[ left:", cur.count("\\["))
kinds = {}
for f in F:
    key = (f["page"], "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal"))
    kinds[key] = kinds.get(key, 0) + 1
for p in pages:
    print(p, "normal", kinds.get((p, "normal"), 0), "convention", kinds.get((p, "convention"), 0), "misprint",
          kinds.get((p, "misprint"), 0))
# misprint fixes must change only the misprinted characters
for f in F:
    if f["kind"] == "misprint_in_print" and f["fix"]:
        o, n = f["fix"]["old"], f["fix"]["new"]
        print("misprint edit", f["page"], repr(o), "->", repr(n), "| corrected:", repr(f.get("corrected")))
print("ALL OK" if ok else "FAILURES")
