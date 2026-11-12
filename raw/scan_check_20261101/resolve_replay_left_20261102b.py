"""Resolve the second set of replay leftovers of 2 Nov 2026 (REPLAY_CURRENT_MANUAL.json) by hand on the corrected
edition, as resolve_replay_left_20261102.py did for the first set.

Each leftover is a diplomatic fix whose "old" no longer occurs once on its page in the corrected edition, because that
edition corrects the text there. "adapt" applies the same typographic fix to the corrected wording (old2 -> new2,
unique in the page); "skip" when the corrected edition rewrote the passage or already has the printed reading. Both
the adapted edit and the original entry (so that replay_to_current.py does not list it again) are logged to
FIXLOG_CURRENT.jsonl.
usage: python -I resolve_replay_left_20261102b.py [--dry]"""
import json
import pathlib
import re
import sys

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
dry = "--dry" in sys.argv
D = {  # (file name, page, start of the original old) -> decision
    ("ega3-1-fr.tex", 119, "le morphisme\n$f_0:X_0"):
        ("adapt", "le morphisme\n$f_0:X_0\\to S_0$ d\u00e9duit de",
         "\\emph{le morphisme}\n$f_0:X_0\\to S_0$ \\emph{d\u00e9duit de}"),
    ("ega3-1-fr.tex", 120, "\\]\npar "):
        ("adapt", "\\mathcal F=\\varprojlim_k\\mathcal F_k\n\\]\npar (",
         "\\mathcal F=\\varprojlim_k\\mathcal F_k\n\\]\n("),
    ("ega3-1-fr.tex", 121, "\\widetilde{S'}"):
        ("skip", "the corrected edition rewrote this passage (S and M as tensor products); no \\widetilde{S'} there"),
    ("ega3-1-fr.tex", 121, "\\widetilde{M'}"):
        ("skip", "the corrected edition rewrote this passage (S and M as tensor products); no \\widetilde{M'} there"),
    ("ega3-1-fr.tex", 115, "$\\mathcal G\\in K'$"):
        ("adapt", "$\\mathcal G\\in K'$ de support $Y$ tel que", "$\\mathcal G\\in\\boldsymbol{K}'$ de support $Y$ tel que"),
    ("ega3-1-fr.tex", 102, "propres sur $Y$ (II"):
        ("adapt", "soit propre sur $Y$ (II, 5.4.10).", "soit propre sur $Y$ \\textup{(\\textbf{II}, 5.4.10)}."),
    ("ega3-1-fr.tex", 102, "i_*(\\mathcal F(n))$, et"):
        ("skip", "the corrected edition rewrote this step of the proof; 'i_*(F(n)), et de m\u00eame' is not there"),
    ("ega3-1-fr.tex", 132, "point ferm\u00e9e"):
        ("skip", "the corrected edition already reads 'l'unique point ferm\u00e9 de'"),
    ("ega3-1-fr.tex", 162, ": 0, 8.1.1."):
        ("adapt", "$\\boldsymbol{C}$) : 0, 8.1.1.", "$\\boldsymbol{C}$) : \\textbf{0}, 8.1.1."),
    ("ega3-1-fr.tex", 162, "morphismes de $C$)"):
        ("adapt", "($Y$ objet de $C$, $w$ morphisme de $C$)",
         "($Y$ objet de $\\boldsymbol{C}$, $w$ morphisme de $\\boldsymbol{C}$)"),
    ("ega0-20-fr.tex", 120, "le $A$-homomorphisme"):
        ("adapt", "l'$A$-homomorphisme\n$\\alpha:x\\mapsto", "l'$A$-homomorphisme\n$\\alpha:x\\leadsto"),
    ("ega0-20-fr.tex", 117, "est nulle dans"):
        ("adapt", "est nulle sur $\\rho(A)$", "est \\emph{nulle sur} $\\rho(A)$"),
    ("ega4-2-fr.tex", 75, "soit g\u00e9om\u00e9triquement r\u00e9duit (4.6.11)"):
        ("adapt", "soit g\u00e9om\u00e9triquement r\u00e9duit (4.6.13).", "soit \\emph{g\u00e9om\u00e9triquement r\u00e9duit} (4.6.13)."),
    ("ega4-2-fr.tex", 118, "contenant $Z-X$"):
        ("adapt", "contenant $X-Z$,", "contenant $X\\setmin Z$,"),
    ("ega4-2-fr.tex", 96, "les deux membres de (5.5.7.1) sont"):
        ("adapt", "soit cat\u00e9naire; alors les deux membres de (5.5.7.1) sont \u00e9gaux.",
         "soit cat\u00e9naire; alors les deux membres de \\textup{(5.5.7.1)} sont \u00e9gaux."),
    ("ega4-2-fr.tex", 177, "v)-w^2"):
        ("adapt", "(t\\setmin v)^2-w^2(2v", "(t\\setmin v)^2\\setmin w^2(2v"),
    ("ega4-2-fr.tex", 169, "(6.12.4, II))"):
        ("adapt", "(6.12.4, II),", "(6.12.4; II),"),
}
items = json.loads((E / "REPLAY_CURRENT_MANUAL.json").read_text(encoding="utf-8"))
log = None if dry else open(E / "FIXLOG_CURRENT.jsonl", "a", encoding="utf-8")
used = set()
for x in items:
    cur = pathlib.Path(x["current_file"])
    keys = [k for k in D if k[0] == cur.name and k[1] == int(x["page"]) and x["old"].startswith(k[2])]
    if len(keys) != 1:
        print("NO DECISION", cur.name, x["page"], repr(x["old"][:60]))
        continue
    used.add(keys[0])
    dec = D[keys[0]]
    if dec[0] == "adapt":
        t = cur.read_text(encoding="utf-8")
        part = x.get("part") or "I"
        cuts = [(int(m.group(1)), m.start()) for m in
                re.finditer(r"\\oldpage\[" + re.escape(part) + r"\]\{(\d+)\}", t)]
        i = [k for k, (n, s) in enumerate(cuts) if n == int(x["page"])][0]
        s, e = cuts[i][1], (cuts[i + 1][1] if i + 1 < len(cuts) else len(t))
        n = t[s:e].count(dec[1])
        if n != 1:
            print(f"SKIP-ADAPT {cur.name} p.{x['page']}: adapted old occurs {n} times: {dec[1][:60]!r}")
            continue
        t = t[:s] + t[s:e].replace(dec[1], dec[2]) + t[e:]
        if not dry:
            cur.write_text(t, encoding="utf-8", newline="")
            log.write(json.dumps(dict(file=str(cur), part=part, page=int(x["page"]), old=dec[1], new=dec[2],
                                      source="hand_adapted_20261102b"), ensure_ascii=False) + "\n")
    if not dry:
        log.write(json.dumps(dict(file=str(cur), part=x.get("part"), page=int(x["page"]), old=x["old"], new=x["new"],
                                  source="hand_resolved_20261102b", decision=dec[0],
                                  why=dec[1] if dec[0] == "skip" else "adapted to the corrected wording"),
                             ensure_ascii=False) + "\n")
    print(("would " if dry else "") + dec[0], cur.name, x["page"])
print("unused decisions:", [k for k in D if k not in used])
