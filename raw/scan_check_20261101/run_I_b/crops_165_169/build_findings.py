"""Build findings_165_169.json for EGA I pp. 165-169 and check every fix.old
occurs exactly once in its page_NNN.tex (CRLF files).  Read-only on .tex."""
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent.parent
OUT = RUN / "findings_165_169.json"
NL = "\r\n"
CONT = ("Text from ega1-9-fr.tex before \\oldpage[I]{170} (continuation of p. 169); "
        "apply_fixes.py searches only ega1-8-fr.tex from \\oldpage[I]{169}, so this edit will land on the manual list.")

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 165 ----------------
LAB = ("Labels printed upright (checked on a crop); \\item[...] takes the italic of the statement "
       "environment (EGA_FR.tex loads no enumitem). Same pattern as the a)-e) labels on p. 142.")
add(165, "Lemme (8.1.4), label (i)", "label (i) upright", r"\item[(i)] Il existe",
    "convention", 6, "high", r"\item[(i)] Il existe", r"\item[\textup{(i)}] Il existe", LAB)
add(165, "Lemme (8.1.4), label (ii)", "label (ii) upright", r"\item[(ii)] L'idéal",
    "convention", 6, "high", r"\item[(ii)] L'idéal", r"\item[\textup{(ii)}] L'idéal", None)
add(165, "Lemme (8.1.4), label (iii)", "label (iii) upright", r"\item[(iii)] Il existe",
    "convention", 6, "high", r"\item[(iii)] Il existe", r"\item[\textup{(iii)}] Il existe", None)
add(165, "Proposition (8.1.5), label (i)", "label (i) upright", r"\item[(i)] Pour tout",
    "convention", 6, "high", r"\item[(i)] Pour tout", r"\item[\textup{(i)}] Pour tout", None)
add(165, "Proposition (8.1.5), label (ii)", "label (ii) upright", r"\item[(ii)] Pour tout",
    "convention", 6, "high", r"\item[(ii)] Pour tout", r"\item[\textup{(ii)}] Pour tout", None)
add(165, "Proposition (8.1.5), label (iii)", "label (iii) upright", r"\item[(iii)] Si",
    "convention", 6, "high", r"\item[(iii)] Si", r"\item[\textup{(iii)}] Si", None)
add(165, "Proposition (8.1.5), label (iv)", "label (iv) upright", r"\item[(iv)] On a",
    "convention", 6, "high", r"\item[(iv)] On a", r"\item[\textup{(iv)}] On a", None)
add(165, "proof of (8.1.4): 'si Q domine M et N, on a P⊂Q et m(M)=...'",
    "on a P⊂Q et m(M)=m(Q)∩M=... (no comma after P⊂Q)", r"on a $P\subset Q$, et",
    "punctuation", None, "high", r"$P\subset Q$, et", r"$P\subset Q$ et",
    "The TeX adds a comma after P⊂Q (checked on a crop).")
add(165, "proof of (8.1.4): 'm(M)=m(Q)∩M=(m(Q)∩P)∩M, m(N)=(m(Q)∩P)∩N, donc (iii) entraîne (i)'",
    "the two equalities are set inline in the running text",
    "the equalities are set as a displayed formula \\[ ... \\]",
    "other", None, "low",
    r"\[" + NL + r"  \mathfrak m(M)=\mathfrak m(Q)\cap M" + NL
    + r"  =(\mathfrak m(Q)\cap P)\cap M,\qquad" + NL
    + r"  \mathfrak m(N)=(\mathfrak m(Q)\cap P)\cap N," + NL + r"\]",
    r"$\mathfrak m(M)=\mathfrak m(Q)\cap M=(\mathfrak m(Q)\cap P)\cap M$," + NL
    + r"$\mathfrak m(N)=(\mathfrak m(Q)\cap P)\cap N$,",
    "Layout only (display vs inline), as on p. 134; the formulas match. Independent of the comma edit just before it.")
add(165, "(8.2.1.1): 'Γ(U, O_X)=∩_{x∈U} O_x'",
    "display ends with O_x, no full stop", r"\bigcap_{x\in U}\mathscr{O}_x.",
    "punctuation", None, "high", r"\bigcap_{x\in U}\mathscr{O}_x.", r"\bigcap_{x\in U}\mathscr{O}_x",
    "The TeX adds a full stop after the display (checked on a crop); the paragraph (8.2.1) ends with the display.")

# ---------------- page 166 ----------------
add(166, "Proposition (8.2.2): '« O_x et O_y sont apparentés » (8.1.4) entre points x, y'",
    "(8.1.4) upright inside the italic statement", r"(\hyperref[I.8.1.4-fr]{8.1.4}) entre points",
    "convention", 6, "high", r"(\hyperref[I.8.1.4-fr]{8.1.4}) entre points",
    r"\textup{(\hyperref[I.8.1.4-fr]{8.1.4})} entre points",
    "Reference printed upright inside the italic statement (checked on a crop).")
add(166, "proof of (8.2.2), 1st paragraph: 'comme a⊂m_x équivaut à x∈V(a)=W∩F pour x∈U'",
    "x∈V(𝔞)=W∩F", r"$x\in V(\mathfrak a)=W\cap F$", "misprint_in_print", None, "low",
    None, None,
    "The TeX keeps the printed reading (checked on a crop: '=' and 'W∩F'). F is the trace on W of the closed set "
    "V(a) of U, so F=W∩V(a); since F⊂W, the printed V(a)=W∩F would say V(a)=F, which fails when V(a) has points "
    "outside W. For x∈W, a⊂m_x ⟺ x∈V(a) ⟺ x∈F, which is what the argument uses. Apparently V(a) and F interchanged; "
    "not in the authors' errata lists (EGA II, EGA III). Mathematical slip, not typographical; the exact intended wording is a guess.",
    corrected=r"$x\in V(\mathfrak a)$ pour $x\in U$, et $W\cap V(\mathfrak a)=F$")
add(166, "proof of (8.2.2), last paragraph: 'on a évidemment x=z et y=z, d'où x=y'",
    "x=z et y=z (no comma after x=z)", r"$x=z$, et $y=z$",
    "punctuation", None, "high", r"$x=z$, et $y=z$", r"$x=z$ et $y=z$",
    "The TeX adds a comma after x=z (checked on a crop).")
add(166, "Corollaire (8.2.4): 'l'application x→O_x est injective'",
    "plain arrow x→O_x", r"$x\mapsto\mathscr{O}_x$",
    "convention", 3, "high", r"$x\mapsto\mathscr{O}_x$", r"$x\to\mathscr{O}_x$",
    "Plain arrow in the print (checked on a crop).")

# ---------------- page 167 ----------------
add(167, "(8.2.6): 'tels que O_y⊂O_{x_i} pour un indice i au moins'",
    "subscript printed 'xi' on one level: the i is not lowered as a second-order index",
    r"\mathscr{O}_{x_i}", "misprint_in_print", None, "medium",
    r"\mathscr{O}_{x_i}", r"\mathscr{O}_{xi}",
    "The TeX silently corrects the print. Checked on a crop at 3x: x and i have the same size and baseline. "
    "Same typesetting slip as O_{xi} on pp. 144 and 157.",
    corrected=r"\mathscr{O}_{x_i}")
add(167, "(8.2.6): 'puisque Γ(U, O_X)=∩_{x∈U} O_x par (8.2.1.1). La famille'",
    "... ∩ O_x par (8.2.1.1). La famille ...",
    r"\bigcap_{x\in U}\mathscr{O}_x$ (\hyperref[I.8.2.1.1-fr]{8.2.1.1}). La famille",
    "missing", None, "high",
    r"(\hyperref[I.8.2.1.1-fr]{8.2.1.1}). La famille", r"par (\hyperref[I.8.2.1.1-fr]{8.2.1.1}). La famille",
    "The word 'par' before the reference is missing in the TeX.")
add(167, "Proposition (8.2.7): 'f : X→Y un morphisme dominant (2.2.6)'",
    "(2.2.6) upright inside the italic statement", r"(\hyperref[I.2.2.6-fr]{2.2.6})",
    "convention", 6, "high", r"(\hyperref[I.2.2.6-fr]{2.2.6})",
    r"\textup{(\hyperref[I.2.2.6-fr]{2.2.6})}", "Checked on a crop.")
add(167, "Proposition (8.2.7): 'K (resp. L) le corps des fonctions rationnelles'",
    "'(resp. L)' upright inside the italic statement", r"$K$ (resp. $L$)",
    "convention", 6, "high", r"$K$ (resp. $L$)", r"$K$ \textup{(resp. $L$)}", "Checked on a crop.")
add(167, "Proposition (8.2.7): 'sur X (resp. Y). Alors L'",
    "'(resp. Y)' upright inside the italic statement", r"sur $X$ (resp. $Y$)",
    "convention", 6, "high", r"sur $X$ (resp. $Y$)", r"sur $X$ \textup{(resp. $Y$)}", "Checked on a crop.")
add(167, "proof of (8.2.7): 'ψ(a) est le point générique de Y (0, 2.1.5)'",
    "bold 0 in (0, 2.1.5)", r"(\hyperref[0.2.1.5-fr]{0, 2.1.5})",
    "convention", 2, "high", r"(\hyperref[0.2.1.5-fr]{0, 2.1.5})",
    r"(\hyperref[0.2.1.5-fr]{\textbf{0}, 2.1.5})", None)
add(167, "proof of (8.2.7): 'le seul anneau local de Y dominé par O_x, puisque deux anneaux'",
    "dominé par O_x, puisque (comma after O_x)", r"dominé par $\mathscr{O}_x$ puisque",
    "punctuation", None, "high", r"dominé par $\mathscr{O}_x$ puisque",
    r"dominé par $\mathscr{O}_x$, puisque", "Comma missing in the TeX (checked on a crop).")
add(167, "Proposition (8.2.8): 'Soient X un préschéma irréductible'",
    "'irréductible' set in roman inside the italic statement (emphasis)", r"un préschéma irréductible",
    "convention", 6, "high", r"un préschéma irréductible", r"un préschéma \textup{irréductible}",
    "Checked on a crop: upright letters between italic words ('un préschéma' and 'f : X→Y une immersion').")
add(167, "Proposition (8.2.8): 'une immersion locale (resp. un isomorphisme local)'",
    "'(resp.' upright inside the italic statement", r"(resp. un isomorphisme local)~;",
    "convention", 6, "high", r"(resp. un isomorphisme local)~;", r"\textup{(resp.} un isomorphisme local)~;",
    "Checked on a crop.")
add(167, "Proposition (8.2.8): 'Alors f est une immersion (resp. une immersion ouverte)'",
    "'(resp.' upright inside the italic statement", r"immersion (resp. une immersion ouverte)",
    "convention", 6, "high", r"immersion (resp. une immersion ouverte)",
    r"immersion \textup{(resp.} une immersion ouverte)", "Checked on a crop.")
add(167, "proof of (8.2.8): 'on peut supposer X et Y réduits'",
    "'réduits' in italics", r"$X$ et $Y$ réduits",
    "italics", None, "high", r"$X$ et $Y$ réduits", r"$X$ et $Y$ \emph{réduits}",
    "Checked on a crop.")

# ---------------- page 168 ----------------
add(168, "proof of (8.2.8): 'Y est, lui aussi, irréductible (0, 2.1.5)'",
    "bold 0 in (0, 2.1.5)", r"(\hyperref[0.2.1.5-fr]{0, 2.1.5})",
    "convention", 2, "high", r"(\hyperref[0.2.1.5-fr]{0, 2.1.5})",
    r"(\hyperref[0.2.1.5-fr]{\textbf{0}, 2.1.5})", None)

# ---------------- page 169 (continuation from ega1-9-fr.tex) ----------------
R = "'(resp.' upright inside the italic statement"
add(169, "Proposition (9.1.1): 'Soit X un préschéma (resp. un préschéma localement noethérien)'",
    R, r"$X$ un préschéma (resp.", "convention", 6, "high",
    r"$X$ un préschéma (resp.", r"$X$ un préschéma \textup{(resp.}", "Checked on a crop. " + CONT)
add(169, "Proposition (9.1.1): 'quasi-cohérents (resp. cohérents) ; alors'",
    R, r"(resp. cohérents)", "convention", 6, "high",
    r"(resp. cohérents)", r"\textup{(resp.} cohérents)", CONT)
add(169, "Proposition (9.1.1): 'F⊗G est quasi-cohérent (resp. cohérent) et de type fini'",
    R, r"\mathscr{G}$ est quasi-cohérent (resp.", "convention", 6, "high",
    r"\mathscr{G}$ est quasi-cohérent (resp.", r"\mathscr{G}$ est quasi-cohérent \textup{(resp.}", CONT)
add(169, "Proposition (9.1.1): 'si G est quasi-cohérent (resp. cohérent), alors'",
    R, r"(resp. cohérent), alors", "convention", 6, "high",
    r"(resp. cohérent), alors", r"\textup{(resp.} cohérent), alors", CONT)
add(169, "Proposition (9.1.1): 'Hom(F, G) est quasi-cohérent (resp. cohérent).'",
    R, r"(resp. cohérent).", "convention", 6, "high",
    r"(resp. cohérent).", r"\textup{(resp.} cohérent).", CONT)
add(169, "Définition (9.1.2): 'F (resp. G) un O_X-Module'",
    "'(resp. G)' upright inside the italic statement", r"$\mathscr{F}$ (resp. $\mathscr{G}$) un",
    "convention", 6, "high", r"$\mathscr{F}$ (resp. $\mathscr{G}$) un",
    r"$\mathscr{F}$ \textup{(resp. $\mathscr{G}$)} un", "Checked on a crop. " + CONT)
add(169, "Définition (9.1.2): 'un O_X-Module (resp. un O_Y-Module) quasi-cohérent'",
    R, r"-Module (resp. un", "convention", 6, "high",
    r"-Module (resp. un", r"-Module \textup{(resp.} un", CONT)
add(169, "Définition (9.1.2): 'sur O_S (ou sur S)'",
    "'(ou' upright inside the italic statement ('sur' italic)", r"(ou sur $S$)",
    "convention", 6, "high", r"(ou sur $S$)", r"\textup{(ou} sur $S$)", "Checked on a crop. " + CONT)
add(169, "Définition (9.1.2): 'F⊗_{O_S}G (ou F⊗_S G)'",
    "'(ou' upright inside the italic statement", r"\mathscr{G}$ (ou",
    "convention", 6, "high", r"\mathscr{G}$ (ou", r"\mathscr{G}$ \textup{(ou}", CONT)
add(169, "after (9.1.2): 'le produit tensoriel F_1⊗_S F_2⊗_S ... ⊗_S F_n'",
    "baseline dots: F_1⊗_S F_2⊗_S . . . ⊗_S F_n", r"\otimes_S\cdots\otimes_S",
    "formula", None, "high", r"\otimes_S\cdots\otimes_S", r"\otimes_S\ldots\otimes_S",
    "Dots on the baseline in the print (checked on a crop); same treatment as p. 113. " + CONT)
add(169, "after (9.1.2): 'sur le préschéma Z=X_1×_S X_2 ... ×_S X_n'",
    "Z=X_1×_S X_2 . . . ×_S X_n: no ×_S between X_2 and the dots; baseline dots",
    r"Z=X_1\times_S X_2\times_S\cdots\times_S X_n", "misprint_in_print", None, "medium",
    r"X_2\times_S\cdots\times_S X_n", r"X_2\ldots\times_S X_n",
    "The TeX silently supplies the missing ×_S (checked on a crop: X_2 is followed directly by the dots). "
    "The tensor product in the line above has ⊗_S after F_2, so the omission is a slip. Also baseline dots. " + CONT,
    corrected=r"Z=X_1\times_S X_2\times_S\ldots\times_S X_n")
add(169, "after (9.1.2): 'c'est un O_Z-module quasi-cohérent'",
    "O_Z-module with lowercase 'module'", r"$\mathscr{O}_Z$-module",
    "misprint_in_print", None, "medium", None, None,
    "The TeX keeps the printed reading (checked on a crop). EGA writes sheaves of modules as O_X-Module with a capital M; "
    "this is the only lowercase 'O-module' in the EGA I sources (about 150 'O-Module'), and the same sentence has "
    "'F_i un O_{X_i}-Module quasi-cohérent' two lines earlier. Text in ega1-9-fr.tex before \\oldpage[I]{170} (continuation of p. 169).",
    corrected=r"$\mathscr{O}_Z$-Module")
add(169, "after (9.1.2): 'en vertu de (9.1.1) et de (0, 5.1.4)'",
    "bold 0 in (0, 5.1.4)", r"(\hyperref[0.5.1.4-fr]{0, 5.1.4})",
    "convention", 2, "high", r"(\hyperref[0.5.1.4-fr]{0, 5.1.4})",
    r"(\hyperref[0.5.1.4-fr]{\textbf{0}, 5.1.4})", CONT)
add(169, "after (9.1.2): 'en vertu de (9.1.1), (0, 5.3.11) et (6.1.1)'",
    "bold 0 in (0, 5.3.11)", r"(\hyperref[0.5.3.11-fr]{0, 5.3.11})",
    "convention", 2, "high", r"(\hyperref[0.5.3.11-fr]{0, 5.3.11})",
    r"(\hyperref[0.5.3.11-fr]{\textbf{0}, 5.3.11})", CONT)
add(169, "after (9.1.2): 'q*(O_Y)=O_{X×_S Y} (0, 4.3.4)'",
    "bold 0 in (0, 4.3.4)", r"(\hyperref[0.4.3.4-fr]{0, 4.3.4})",
    "convention", 2, "high", r"(\hyperref[0.4.3.4-fr]{0, 4.3.4})",
    r"(\hyperref[0.4.3.4-fr]{\textbf{0}, 4.3.4})", CONT)
add(169, "Proposition (9.1.3): 'Soit M (resp. N) un B-module'",
    "'(resp. N)' upright inside the italic statement", r"$M$ (resp. $N$)",
    "convention", 6, "high", r"$M$ (resp. $N$)", r"$M$ \textup{(resp. $N$)}", "Checked on a crop. " + CONT)
add(169, "Proposition (9.1.3): 'un B-module (resp. C-module)'",
    R + " ('C-module' italic)", r"(resp. $C$-module)",
    "convention", 6, "high", r"(resp. $C$-module)", r"\textup{(resp.} $C$-module)", CONT)
add(169, "Proposition (9.1.3): 'F=M~ (resp. G=N~) le faisceau quasi-cohérent associé'",
    R, r"\widetilde{M}$ (resp.", "convention", 6, "high",
    r"\widetilde{M}$ (resp.", r"\widetilde{M}$ \textup{(resp.}", CONT)

# ---------------- checks ----------------
bad = 0
for x in F:
    fx = x["fix"]
    if fx is None:
        continue
    t = (RUN / f"page_{x['page']:03d}.tex").read_bytes().decode("utf-8")
    n = t.count(fx["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE/ABSENT", x["page"], n, repr(fx["old"]))
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
c = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    c[(x["page"], k)] += 1
for p in (165, 166, 167, 168, 169):
    print(p, {k: c[(p, k)] for k in ("normal", "convention", "misprint")})
print("total", len(F), "bad", bad, "->", OUT)
