"""The four places of FRENCH_RECHECK.md, checked against the print on 5 Nov: all four are misprints of the print, which
the French TeX follows. Diplomatic edition: unchanged (it keeps the print). Corrected edition: the correct reading,
logged in FIXLOG_CURRENT.jsonl (source french_recheck); each misprint recorded in MISPRINTS.json.
usage: python -I apply_french_recheck.py [--apply]"""
import json
import pathlib
import sys

E = pathlib.Path(__file__).parent
CUR = E / "ega-fr" / "editions" / "2026-10-24-r20" / "current" / "packages" / "IV1" / "native" / "ega4"
P = "0\\textsubscript{IV-1}"
ITEMS = [
    # (file, page, old, new, count expected, misprint record)
    ("ega0-15-fr.tex", 17,
     "$M/(\\sum_{j=1}^{i-1}f_jM)$ $(1\\leq i\\leq n)$",
     "$M/(\\sum_{j=1}^{i-1}f_jM)$ $(1\\leq i\\leq n+1)$", 1,
     {"where": "(15.1.15), hypothesis: 'chacun des A-modules M/(sum_{j<i} f_jM) (1<=i<=n) soit plat'",
      "print": "(1 ≤ i ≤ n)", "correct": "(1 ≤ i ≤ n+1)",
      "note": "The proof needs M/(f_1M+...+f_nM) flat as well (for the last step, f'_n regular): with i <= n only, "
              "A = M = k[t], f_1 = t, A' = k gives f'_1 = 0, not M'-regular. Correct both displays (hypothesis and "
              "conclusion) together. Found by the English hand pass (the English has n+1)."}),
    ("ega0-15-fr.tex", 17,
     "$M'/(\\sum_{j=1}^{i-1}f'_jM')$ $(1\\leq i\\leq n)$",
     "$M'/(\\sum_{j=1}^{i-1}f'_jM')$ $(1\\leq i\\leq n+1)$", 1,
     {"where": "(15.1.15), conclusion: 'les A'-modules M'/(sum_{j<i} f'_jM') (1<=i<=n) sont plats'",
      "print": "(1 ≤ i ≤ n)", "correct": "(1 ≤ i ≤ n+1)",
      "note": "Together with the hypothesis of (15.1.15) (previous entry): flatness for i = n+1 follows by base change."}),
    ("ega0-17-fr.tex", 49,
     "on sait alors (16.4.6, (i)) que l'on a",
     "on sait alors (16.4.6, (ii)) que l'on a", 1,
     {"where": "proof of (17.3.4), case m > 0: 'on sait alors (16.4.6, (i)) que l'on a prof(M/xM) = m-1'",
      "print": "(16.4.6, (i))", "correct": "(16.4.6, (ii))",
      "note": "prof(M/xM) = prof(M) - 1 for an M-regular x in m is (16.4.6, (ii)), formula (16.4.6.1); the first "
              "citation of (16.4.6, (i)) in the same proof (case m = 0) is right. Found by the English hand pass."}),
]
apply = "--apply" in sys.argv
mis = json.loads((E / "MISPRINTS.json").read_text(encoding="utf-8"))
for fname, page, old, new, cnt, rec in ITEMS:
    f = CUR / fname
    t = f.read_text(encoding="utf-8")
    n = t.count(old)
    print(fname, page, "occurrences", n, "(expected", cnt, ")", "already" if new in t and n == 0 else "")
    if n != cnt or not apply:
        continue
    f.write_text(t.replace(old, new), encoding="utf-8", newline="")
    with open(E / "FIXLOG_CURRENT.jsonl", "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"file": str(f), "part": P, "page": page, "old": old, "new": new, "source": "french_recheck",
                             "why": rec["note"]}, ensure_ascii=False) + "\n")
    mis.append(dict(part=P, page=page, where=rec["where"], print=rec["print"], correct=rec["correct"],
                    tex_did="the printed reading (both editions)", note=rec["note"] + " Checked against the print and "
                    "corrected in the corrected edition on 5 Nov.", source="FRENCH_RECHECK.md"))
if apply:
    (E / "MISPRINTS.json").write_text(json.dumps(mis, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("MISPRINTS now", len(mis))
