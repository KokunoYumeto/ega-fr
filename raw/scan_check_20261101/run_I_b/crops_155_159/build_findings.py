import json, os, sys

RUN = r"user\Documents\ega_scan_check_20261101\run_I_b"
OUT = os.path.join(RUN, "findings_155_159.json")

def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d

R6 = "Reference printed upright inside the italic statement; italic in the TeX environment."
K1 = "Bold italic k printed; plain k in the TeX."

findings = [
# ---------------- page 155 ----------------
F(155, "Définition (7.1.2), first sentence: 'on appelle application rationnelle de X dans Y'",
  "'application rationnelle de X dans Y' italic like the rest of the definition (no change of face)",
  "\\emph{application rationnelle de $X$ dans $Y$} inside the italic definition environment (comes out upright)",
  "convention", 6, "high",
  "\\emph{application rationnelle de $X$ dans $Y$}", "application rationnelle de $X$ dans $Y$",
  "Checked on a full-resolution crop."),
F(155, "Définition (7.1.2): 'on dit qu'une telle classe est une S-application rationnelle s'il existe'",
  "italic, no change of face",
  "\\emph{$S$-application rationnelle} (comes out upright)",
  "convention", 6, "high",
  "\\emph{$S$-application rationnelle}", "$S$-application rationnelle",
  "Checked on a full-resolution crop."),
F(155, "Définition (7.1.2): 'On appelle S-section rationnelle de X toute S-application rationnelle de S dans X'",
  "italic, no change of face",
  "\\emph{$S$-section rationnelle de $X$} (comes out upright)",
  "convention", 6, "high",
  "\\emph{$S$-section rationnelle de $X$}", "$S$-section rationnelle de $X$",
  "Checked on a full-resolution crop."),
F(155, "Définition (7.1.2): 'On appelle fonction rationnelle sur un préschéma X toute X-section rationnelle'",
  "italic, no change of face",
  "\\emph{fonction rationnelle sur un préschéma $X$} (comes out upright)",
  "convention", 6, "high",
  "\\emph{fonction rationnelle sur un préschéma $X$}", "fonction rationnelle sur un préschéma $X$",
  "Checked on a full-resolution crop."),
F(155, "Définition (7.1.2): 'pour la relation définie dans (7.1.1)'",
  "(7.1.1) upright inside the italic statement",
  "(\\hyperref[I.7.1.1-fr]{7.1.1}) inside the italic definition environment",
  "convention", 6, "high",
  "(\\hyperref[I.7.1.1-fr]{7.1.1})", "\\textup{(\\hyperref[I.7.1.1-fr]{7.1.1})}",
  R6 + " Checked on a full-resolution crop."),
F(155, "Définition (7.1.2): the three paragraphs after the statement ('Par abus de langage ...', 'Soient f une application rationnelle de X dans Y ...', 'Si, à tout S-morphisme f : X→Y ...')",
  "the italic statement ends with '(où T est une indéterminée).'; the following paragraphs are roman, with only 'restriction de f à' in italics",
  "\\begin{definition}[7.1.2] runs on to p. 156 and closes only after '(3.3.14).', so these roman paragraphs come out italic and \\emph{restriction de $f$ à $U$} comes out upright",
  "italics", None, "high",
  "indéterminée).", "indéterminée).\n\\end{definition}",
  "Close the definition after its statement. Apply together with the p. 156 edit that removes the \\end{definition} after '(3.3.14).'; either edit alone leaves the environments unbalanced. Once both are applied, \\emph{restriction de $f$ à $U$} comes out italic as printed."),
# ---------------- page 156 ----------------
F(156, "top of the page, continuation of (7.1.2): 'à laquelle appartient f, on définit une application canonique ... s'identifie canoniquement à Γ_rat((X×_S Y)/X) (3.3.14).'",
  "roman",
  "still inside the italic definition environment, which ends after '(3.3.14).' (comes out italic)",
  "italics", None, "high",
  "{3.3.14}).\n\\end{definition}", "{3.3.14}).",
  "Pair of the p. 155 edit that inserts \\end{definition} after '(où $T$ est une indéterminée).'; apply both together."),
F(156, "Proposition (7.1.5): 'C'est un anneau local de dimension 0, et par suite'",
  "the 0 is an upright (roman old-style) figure inside the italic statement",
  "de dimension 0, (text figure inside the italic proposition environment, comes out italic)",
  "convention", 6, "medium",
  "de dimension 0, et par suite", "de dimension \\textup{0}, et par suite",
  "Checked on a crop at 1.5x: the zero is round and upright, unlike the slanted italic o of 'dimension'. Minor."),
F(156, "proof of (7.1.5), last sentence: 'que j_x est nilpotent et O_x=A_x artinien'",
  "𝒪_x=A_x (subscript x)",
  "$\\mathscr{O}_x=A_{\\mathfrak{j}_x}$",
  "formula", None, "high",
  "A_{\\mathfrak{j}_x}", "A_x",
  "Checked on a crop at 2.5x. A_x is the notation of (1.1.1) for A_{j_x}, so the print is correct; the TeX expands it."),
F(156, "(7.1.6): 'leur réunion étant dense dans X (0, 2.1.6)'",
  "bold 0",
  "(\\hyperref[0.2.1.6-fr]{0, 2.1.6})",
  "convention", 2, "high",
  "{0, 2.1.6}", "{\\textbf{0}, 2.1.6}", ""),
# ---------------- page 157 ----------------
F(157, "(7.1.6), second line of p. 157: 'donc U'=⋃_i U_i est dense dans X'",
  "U'=⋃_i U'_i (prime on U_i)",
  "$U'=\\bigcup_i U_i$ (silently corrected)",
  "misprint_in_print", None, "high",
  "$U'=\\bigcup_i U_i$", "$U'=\\bigcup_i U'_i$",
  "Checked on a crop at 4x: the print has a prime on U_i. No U'_i is defined; the sets are U_i=U∩X'_i of the line before, which the same sentence calls pairwise disjoint, so U'_i is a misprint for U_i. The TeX silently corrects it.",
  corrected="U'=\\bigcup_i U_i"),
F(157, "Proposition (7.1.7): 'deux préschémas (resp. S-préschémas)'",
  "'resp.' upright inside the italic statement",
  "(resp. $S$-préschémas) inside the italic proposition environment",
  "convention", 6, "high",
  "(resp. $S$-préschémas)", "(\\textup{resp.} $S$-préschémas)",
  "Checked on a crop."),
F(157, "Proposition (7.1.7): 'des germes de morphismes (resp. S-morphismes)'",
  "'resp.' upright inside the italic statement",
  "(resp. $S$-morphismes) inside the italic proposition environment",
  "convention", 6, "high",
  "(resp.\n$S$-morphismes)", "(\\textup{resp.}\n$S$-morphismes)",
  "Checked on a crop."),
F(157, "Proposition (7.1.7): 'des applications rationnelles (resp. S-applications rationnelles)'",
  "'resp.' upright inside the italic statement",
  "(resp. $S$-applications rationnelles) inside the italic proposition environment",
  "convention", 6, "high",
  "(resp. $S$-applications rationnelles)", "(\\textup{resp.} $S$-applications rationnelles)",
  "Checked on a crop."),
F(157, "Corollaire (7.1.8): 'les anneaux O_{x_i} des points génériques x_i'",
  "subscript printed 'xi' on one level: the i is not set as a smaller second-order index",
  "$\\mathscr{O}_{x_i}$",
  "misprint_in_print", None, "medium",
  "\\mathscr{O}_{x_i}", "\\mathscr{O}_{xi}",
  "The TeX silently corrects the print. Measured on the 300 dpi strip: the i (12 px plus dot) has the size of the first-order subscript i of x_i on the same line and sits only 3 px below the x. Same typesetting slip as on p. 142 ((𝒩_X|U_i)^{ni}) and p. 144 (𝒪_{xi}, A(Z_j)_{gj}).",
  corrected="\\mathscr{O}_{x_i}"),
F(157, "proof of (7.1.9): 'c'est-à-dire à Q^{-1}A (0, 1.4.5)'",
  "bold 0",
  "(\\hyperref[0.1.4.5-fr]{0, 1.4.5})",
  "convention", 2, "high",
  "{0, 1.4.5}", "{\\textbf{0}, 1.4.5}", ""),
# ---------------- page 158 ----------------
F(158, "Corollaire (7.1.12): 'et les autres hypothèses de (7.1.11) satisfaites'",
  "(7.1.11) upright inside the italic statement",
  "(\\hyperref[I.7.1.11-fr]{7.1.11}) inside the italic corollary environment",
  "convention", 6, "high",
  "(\\hyperref[I.7.1.11-fr]{7.1.11}) satisfaites", "\\textup{(\\hyperref[I.7.1.11-fr]{7.1.11})} satisfaites",
  R6 + " Checked on a crop."),
F(158, "Corollaire (7.1.13): 'On suppose remplies les conditions de (7.1.12).'",
  "(7.1.12) upright inside the italic statement",
  "(\\hyperref[I.7.1.12-fr]{7.1.12}) inside the italic corollary environment",
  "convention", 6, "high",
  "remplies les conditions de (\\hyperref[I.7.1.12-fr]{7.1.12})", "remplies les conditions de \\textup{(\\hyperref[I.7.1.12-fr]{7.1.12})}",
  R6 + " Checked on a crop."),
F(158, "Corollaire (7.1.14): 'Sous les conditions de (7.1.12), les S-applications'",
  "(7.1.12) upright inside the italic statement",
  "(\\hyperref[I.7.1.12-fr]{7.1.12}) inside the italic corollary environment",
  "convention", 6, "high",
  "Sous les conditions de (\\hyperref[I.7.1.12-fr]{7.1.12})", "Sous les conditions de \\textup{(\\hyperref[I.7.1.12-fr]{7.1.12})}",
  R6 + " Checked on a crop."),
F(158, "paragraph before (7.1.15): 'R(X)=O_x=k(x) est un corps'",
  "bold italic k",
  "$R(X)=\\mathscr{O}_x=k(x)$",
  "convention", 1, "high",
  "\\mathscr{O}_x=k(x)$ est un corps", "\\mathscr{O}_x=\\boldsymbol{k}(x)$ est un corps", K1),
F(158, "Corollaire (7.1.15): 'On suppose vérifiées les conditions de (7.1.12)'",
  "(7.1.12) upright inside the italic statement",
  "(\\hyperref[I.7.1.12-fr]{7.1.12}) inside the italic corollary environment",
  "convention", 6, "high",
  "vérifiées les conditions de (\\hyperref[I.7.1.12-fr]{7.1.12})", "vérifiées les conditions de \\textup{(\\hyperref[I.7.1.12-fr]{7.1.12})}",
  R6 + " Checked on a crop."),
F(158, "Corollaire (7.1.15): 'aux points géométriques de Y⊗_S k(s)'",
  "bold italic k", "$Y\\otimes_S k(s)$", "convention", 1, "high",
  "$Y\\otimes_S k(s)$ à valeurs", "$Y\\otimes_S \\boldsymbol{k}(s)$ à valeurs", K1),
F(158, "Corollaire (7.1.15): 'dans l'extension R(X) de k(s)'",
  "bold italic k", "de $k(s)$", "convention", 1, "high",
  "l'extension $R(X)$ de $k(s)$", "l'extension $R(X)$ de $\\boldsymbol{k}(s)$", K1),
F(158, "Corollaire (7.1.15): 'd'un k(s)-monomorphisme'",
  "bold italic k", "$k(s)$-monomorphisme", "convention", 1, "high",
  "d'un $k(s)$-monomorphisme", "d'un $\\boldsymbol{k}(s)$-monomorphisme", K1),
F(158, "Corollaire (7.1.15): 'de k(y) dans k(x)=R(X)' (k(y))",
  "bold italic k", "$k(y)$", "convention", 1, "high",
  "de $k(y)$ dans", "de $\\boldsymbol{k}(y)$ dans", K1),
F(158, "Corollaire (7.1.15): 'dans k(x)=R(X)' (k(x))",
  "bold italic k", "$k(x)=R(X)$", "convention", 1, "high",
  "$k(x)=R(X)$", "$\\boldsymbol{k}(x)=R(X)$", K1),
F(158, "Corollaire (7.1.15), line 15 from the bottom of p. 158: 's'identifient aux points géométriques de Y⊗_S k(s)'",
  "aux points géométriques de Y⊗_S k(s)",
  "aux points\ngéométriques de $Y\\otimes_S k(s)$ (printed reading kept)",
  "misprint_in_print", None, "high", None, None,
  "Authors' errata (EGA III, Err_III 11): 'Dans (I, 7.1.15) et (I, 7.1.16), lignes 7 et 15 du bas de la p. 158, supprimer « géométriques ».' An authors' correction rather than a typesetting slip. The TeX keeps the printed reading.",
  corrected="s'identifient aux points de $Y\\otimes_S k(s)$"),
F(158, "proof of (7.1.15): 'ceux de Y⊗_S k(s) (3.6.3)'",
  "bold italic k", "$Y\\otimes_S k(s)$", "convention", 1, "high",
  "$Y\\otimes_S k(s)$ (\\hyperref", "$Y\\otimes_S \\boldsymbol{k}(s)$ (\\hyperref", K1),
F(158, "proof of (7.1.15): 'aux k(s)-monomorphismes'",
  "bold italic k", "$k(s)$-monomorphismes", "convention", 1, "high",
  "$k(s)$-monomorphismes", "$\\boldsymbol{k}(s)$-monomorphismes", K1),
F(158, "proof of (7.1.15): 'k(y)→R(X)'",
  "bold italic k", "$k(y)\\to R(X)$", "convention", 1, "high",
  "$k(y)\\to R(X)$", "$\\boldsymbol{k}(y)\\to R(X)$", K1),
F(158, "Corollaire (7.1.16): 'deux préschémas algébriques (6.4.1) sur k'",
  "(6.4.1) upright inside the italic statement",
  "(\\hyperref[I.6.4.1-fr]{6.4.1}) inside the italic corollary environment",
  "convention", 6, "high",
  "(\\hyperref[I.6.4.1-fr]{6.4.1})", "\\textup{(\\hyperref[I.6.4.1-fr]{6.4.1})}",
  R6 + " Checked on a crop."),
F(158, "Corollaire (7.1.16): 'l'extension R(X) de k (3.4.4).'",
  "(3.4.4) upright inside the italic statement",
  "(\\hyperref[I.3.4.4-fr]{3.4.4}) inside the italic corollary environment",
  "convention", 6, "high",
  "(\\hyperref[I.3.4.4-fr]{3.4.4})", "\\textup{(\\hyperref[I.3.4.4-fr]{3.4.4})}",
  R6 + " Checked on a crop."),
F(158, "Corollaire (7.1.16), line 7 from the bottom of p. 158: 'aux points géométriques de Y à valeurs dans l'extension R(X) de k'",
  "aux points géométriques de Y",
  "aux points\ngéométriques de $Y$ (printed reading kept)",
  "misprint_in_print", None, "high", None, None,
  "Authors' errata (EGA III, Err_III 11), as for (7.1.15): delete « géométriques ». The line count includes the heading 7.2. The TeX keeps the printed reading.",
  corrected="s'identifient aux points de $Y$ à valeurs dans l'extension $R(X)$ de $k$"),
F(158, "(7.2.1): 'est appelé le domaine de définition de f ;'",
  "only 'domaine de définition' in italics; 'de f' roman",
  "\\emph{domaine de définition de $f$}",
  "italics", None, "high",
  "\\emph{domaine de définition de $f$}", "\\emph{domaine de définition} de $f$",
  "Checked on a crop at 2x."),
# ---------------- page 159 ----------------
F(159, "Lemme (7.2.2.1): 'Sous les hypothèses de (7.2.2), soient U_1, U_2'",
  "(7.2.2) upright inside the italic statement",
  "(\\hyperref[I.7.2.2-fr]{7.2.2}) inside the italic lemma environment",
  "convention", 6, "high",
  "(\\hyperref[I.7.2.2-fr]{7.2.2}), soient", "\\textup{(\\hyperref[I.7.2.2-fr]{7.2.2})}, soient",
  R6 + " Checked on a crop."),
F(159, "Lemme (7.2.2.1): 'tels qu'il existe un ouvert V⊂U_1∩U_2 dense dans X'",
  "V⊂U_1∩U_2 dense dans X (no comma)",
  "$V\\subset U_1\\cap U_2$, dense dans",
  "punctuation", None, "high",
  "U_1\\cap U_2$, dense", "U_1\\cap U_2$ dense",
  "Checked on a crop at 3x: no comma after U_2 at the end of the line. Minor."),
F(159, "paragraph after the proof of (7.2.2.1): 'Sous les hypothèses de (7.2.2), on peut donc identifier'",
  "'Sous les hypothèses de' in italics; the reference (7.2.2) upright",
  "\\emph{Sous les hypothèses de (\\hyperref[I.7.2.2-fr]{7.2.2})} (reference inside the emphasis, comes out italic)",
  "italics", None, "high",
  "\\emph{Sous les hypothèses de\n(\\hyperref[I.7.2.2-fr]{7.2.2})}", "\\emph{Sous les hypothèses de}\n(\\hyperref[I.7.2.2-fr]{7.2.2})",
  "Checked on a crop at 1.5x."),
F(159, "Corollaire (7.2.3): 'étant celles de (7.2.2), soit U un ouvert'",
  "(7.2.2) upright inside the italic statement",
  "(\\hyperref[I.7.2.2-fr]{7.2.2}) inside the italic corollary environment",
  "convention", 6, "high",
  "(\\hyperref[I.7.2.2-fr]{7.2.2}), soit $U$", "\\textup{(\\hyperref[I.7.2.2-fr]{7.2.2})}, soit $U$",
  R6 + " Checked on a crop."),
]

# verify every fix.old occurs exactly once in its page file
ok = True
texts = {}
for p in (155, 156, 157, 158, 159):
    # universal newlines, as apply_fixes.py reads the sources (page files are CRLF)
    with open(os.path.join(RUN, "page_%d.tex" % p), encoding="utf-8") as fh:
        texts[p] = fh.read()

# every p. 155 finding lies in the continuation text (ega1-7-fr.tex before its first \oldpage marker)
cont = texts[155].split("% (continued in ega1-7-fr.tex, before its first page marker)")[1]
for f in findings:
    if f["page"] == 155:
        if f["fix"] and cont.count(f["fix"]["old"]) != 1:
            print("NOT in continuation:", f["fix"]["old"])
            sys.exit(1)
        f["note"] = (f["note"] + " " if f["note"] else "") + \
            "Located in the continuation part of p. 155: ega1-7-fr.tex, before its first \\oldpage marker (region 'before_first_marker')."
for i, f in enumerate(findings):
    if f["fix"] is None:
        continue
    n = texts[f["page"]].count(f["fix"]["old"])
    if n != 1:
        ok = False
        print("BAD old (count %d) #%d p%d: %r" % (n, i, f["page"], f["fix"]["old"]))
# misprints with fix null: check that the printed reading is in the TeX
for needle, p in (("aux points\ngéométriques de $Y\\otimes_S k(s)$", 158), ("aux points\ngéométriques de $Y$ à valeurs", 158)):
    if texts[p].count(needle) != 1:
        ok = False
        print("BAD kept-reading check p%d: %r" % (p, needle))

if not ok:
    sys.exit(1)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
c = Counter()
for f in findings:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    c[(f["page"], k)] += 1
for p in (155, 156, 157, 158, 159):
    print(p, "normal", c[(p, "normal")], "convention", c[(p, "convention")], "misprint", c[(p, "misprint")])
print("total", len(findings), "written to", OUT)
