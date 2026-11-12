import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
RUN = Path(r"user\Documents\ega_scan_check_20261101\run_II")
REL = Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega2\ega2-1-fr.tex")
OUT = RUN / "findings_100_104.json"
NL = "\n"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def boldI(page, where, ref, old=None, new=None, zero=False):
    ch = "0" if zero else "I"
    if old is None:
        old = "{" + ch + ", " + ref + "}"
        new = "{\\textbf{" + ch + "}, " + ref + "}"
    add(page, where, "(" + ch + ", " + ref + ") with bold " + ch, ch + ", " + ref, "convention", 2, "high", old, new)


# ---------------- page 100 ----------------
boldI(100, "proof of (5.3.4): 'des morphismes de type fini (I, 6.3.4)'", "6.3.4")
add(100, "Corollaire (5.3.6)", "no comma after 'quasi-projectifs': 'quasi-projectifs  X⨿X′ est un'",
    "quasi-projectifs, $X\\amalg X'$", "punctuation", None, "high",
    "quasi-projectifs, $X\\amalg X'$", "quasi-projectifs $X\\amalg X'$",
    "checked on an enlarged crop; the TeX adds the comma")
add(100, "Définition (5.4.1), first line: 'est propre s'il vérifie'",
    "'propre' in the same italic as the rest of the definition (no change of face)",
    "\\emph{propre} inside the italic definition environment (comes out upright)", "convention", 6, "high",
    "\\emph{propre}", "propre", "drop \\emph: the print shows no change of face (enlarged crop)")
add(100, "Définition (5.4.1), b)", "no comma after Y′→Y: 'tout morphisme Y′→Y la projection'",
    "tout morphisme $Y'\\to Y$, la projection", "punctuation", None, "high",
    "morphisme $Y'\\to Y$, la", "morphisme $Y'\\to Y$ la", "checked on an enlarged crop; the TeX adds the comma")
boldI(100, "Définition (5.4.1), b): 'morphisme fermé (I, 2.2.6)'", "2.2.6")
add(100, "after (5.4.1): 'les conditions a) et b) sont locales sur Y'", "a) and b) in italics",
    "a) et b) upright", "italics", None, "high",
    "les conditions a) et b)", "les conditions \\emph{a)} et \\emph{b)}")
add(100, "after (5.4.1): 'sont locales sur Y'", "'locales sur' in italics", "locales sur upright", "italics", None,
    "high", "locales sur $Y$. Pour", "\\emph{locales sur} $Y$. Pour")
boldI(100, "after (5.4.1): 's'identifie à X×_Y U′ (I, 4.4.1)'", "4.4.1")
add(100, "after (5.4.1): 'la condition b) de la déf. (5.4.1)'", "b) in italics", "b) upright", "italics", None,
    "high", "condition b) de la déf.", "condition \\emph{b)} de la déf.")
add(100, "after (5.4.1): 'est un schéma affine'", "'affine' in italics", "affine upright", "italics", None, "high",
    "schéma affine. On verra", "schéma \\emph{affine}. On verra")
add(100, "after (5.4.1): 'se borner à vérifier b) lorsque'", "b) in italics", "b) upright", "italics", None, "high",
    "vérifier b) lorsque", "vérifier \\emph{b)} lorsque")
add(100, "Proposition (5.4.2), (iv)", "f×_S g : X×_S Y→X′×_S Y′",
    "f\\times_Sg:X\\times_SX'\\to Y\\times_SY'", "misprint_in_print", None, "high",
    "$f\\times_Sg:X\\times_SX'\\to Y\\times_SY'$", "$f\\times_Sg:X\\times_SY\\to X'\\times_SY'$",
    "the print interchanges Y and X′ (f : X→Y and g : X′→Y′ give f×_S g : X×_S X′→Y×_S Y′); the TeX silently "
    "corrects it; checked on an enlarged crop",
    corrected="f\\times_Sg:X\\times_SX'\\to Y\\times_SY'")

# ---------------- page 101 ----------------
boldI(101, "first line: '(i), (ii) et (iii) (I, 3.5.1)'", "3.5.1")
add(101, "proof of (5.4.2): 'la vérification de la condition a) de (5.4.1)'", "a) in italics", "a) upright",
    "italics", None, "high", "la condition a) de", "la condition \\emph{a)} de")
boldI(101, "proof of (5.4.2): 'résultats antérieurs (I, 5.5.1 et 6.3.4)'", "5.5.1",
      old="{I, 5.5.1} et", new="{\\textbf{I}, 5.5.1} et")
add(101, "proof of (5.4.2): 'reste à vérifier la condition b).'", "b) in italics", "b) upright", "italics", None,
    "high", "la condition b). C'est", "la condition \\emph{b)}. C'est")
boldI(101, "proof of (5.4.2): '(I, 4.3.2 et 3.3.3)'", "4.3.2")
boldI(101, "proof of (5.4.2): '(I, 3.3.9.1)'", "3.3.9.1")
boldI(101, "proof of (5.4.2): '(I, 3.3.11)'", "3.3.11")
add(101, "Corollaire (5.4.3), (ii)", "no comma after 'fini': 'séparé et de type fini et si f est surjectif'",
    "de type fini, et si $f$ est surjectif", "punctuation", None, "high",
    "de type fini, et si $f$ est", "de type fini et si $f$ est", "checked on an enlarged crop; the TeX adds the comma")
boldI(101, "proof of (5.4.3): 'par le procédé général (I, 5.5.12)'", "5.5.12")
add(101, "proof of (5.4.3): 'que la condition b) de la déf. (5.4.1)'", "b) in italics", "b) upright", "italics",
    None, "high", "que la condition b) de la déf.", "que la condition \\emph{b)} de la déf.")
boldI(101, "proof of (5.4.3): 'est commutatif (I, 3.2.1)'", "3.2.1")
boldI(101, "proof of (5.4.3): 'il en est ainsi de f (I, 3.5.2)'", "3.5.2")
add(101, "Corollaire (5.4.4): '(et a fortiori fermé)'", "'a fortiori' roman inside the italic statement",
    "a fortiori italic", "convention", 6, "high", "(et a fortiori fermé)", "(et \\textup{a fortiori} fermé)",
    "'(et' and 'fermé)' italic; enlarged crop")
add(101, "Corollaire (5.4.5): '(resp. (Y_i)_{1≤i≤n})'", "'(resp.' and ')' roman inside the italic statement",
    "italic", "convention", 6, "high", "(resp. $(Y_i)_{1\\leq i\\leq n}$)",
    "\\textup{(resp. $(Y_i)_{1\\leq i\\leq n}$)}", "enlarged crop; form as in the earlier (resp. ...) fixes")
add(101, "Corollaire (5.4.5): '(resp. Y)'", "'(resp. Y)' roman inside the italic statement", "italic", "convention",
    6, "high", "(resp. $Y$)", "\\textup{(resp. $Y$)}", "enlarged crop")
add(101, "Corollaire (5.4.5): '(resp. h_i)'", "'(resp. h_i)' roman inside the italic statement", "italic",
    "convention", 6, "high", "(resp. $h_i$)", "\\textup{(resp. $h_i$)}", "enlarged crop")
add(101, "Corollaire (5.4.5): '(resp. Y_i→Y)'", "'(resp. Y_i→Y)' roman inside the italic statement", "italic",
    "convention", 6, "high", "(resp. $Y_i\\to Y$)", "\\textup{(resp. $Y_i\\to Y$)}", "enlarged crop")

# ---------------- page 102 ----------------
add(102, "proof of (5.4.5): 'le préschéma Z somme des X_i'", "'somme' in italics", "somme upright", "italics",
    None, "high", "$Z$ somme des", "$Z$ \\emph{somme} des", "enlarged crop")
add(102, "proof of (5.4.5): 'somme des X_i; soit u le morphisme'", "semicolon after X_i", "comma after $X_i$",
    "punctuation", None, "high", "des $X_i$, soit $u$", "des $X_i$~; soit $u$", "enlarged crop")
add(102, "proof of (5.4.5): 'il résulte alors aussitôt de la déf. (5.4.1) que u est propre'", "que u est propre",
    "que $f\\circ u$ est propre", "misprint_in_print", None, "high",
    "que $f\\circ u$ est propre", "que $u$ est propre",
    "the argument needs f∘u proper (its restrictions to the X_i were just shown proper, and (5.4.3, (ii)) is then "
    "applied to f∘u with u surjective); the print has u; the TeX silently corrects it; enlarged crop",
    corrected="f\\circ u")
boldI(102, "proof of (5.4.6): 'Y_1=Y_red (I, 5.1.5)'", "5.1.5")
add(102, "(5.4.7): 'des morphismes dominants'", "'dominants' in italics", "dominants upright", "italics", None,
    "high", "morphismes dominants de", "morphismes \\emph{dominants} de")
add(102, "(5.4.7): 'de préschémas intègres'", "'intègres' in italics", "intègres upright", "italics", None, "high",
    "préschémas intègres.", "préschémas \\emph{intègres}.")
boldI(102, "(5.4.7): 'que nous désignerons encore par X_i (I, 5.2.1)'", "5.2.1")
boldI(102, "(5.4.7): 'un morphisme dominant X_i→Y_i (I, 5.2.2)'", "5.2.2")
boldI(102, "proof of (5.4.8): '(I, 5.5.1 et 6.3.4)'", "5.5.1", old="{I, 5.5.1} et", new="{\\textbf{I}, 5.5.1} et")
add(102, "proof of (5.4.8): '(5.4.2); a fortiori, f×_S 1_{S′} est fermé'", "'a fortiori' in italics",
    "a fortiori upright", "italics", None, "high", "~; a fortiori,", "~; \\emph{a fortiori},")
boldI(102, "proof of (5.4.8): 'sous-préschéma fermé de X×_S Y′ (I, 5.4.2)'", "5.4.2")
add(102, "proof of (5.4.8), diagram: label of the bottom arrow X×_S Y′→Y×_S Y′", "f×1_{S′} (no S under ×)",
    "f\\times_S1_{Y'}", "misprint_in_print", None, "high",
    "\\ar[r]_{f\\times_S1_{Y'}}", "\\ar[r]_{f\\times1_{S'}}",
    "the bottom arrow is f×_S 1_{Y′} (the hypothesis applied with S′=Y′); the print writes f×1_{S′}, here and in "
    "the next sentence; the TeX silently corrects it; enlarged crop",
    corrected="f\\times_S1_{Y'}")
add(102, "proof of (5.4.8), after the diagram: 'que si f×1_{S′} est un morphisme fermé'", "f×1_{S′}",
    "f\\times_S1_{Y'}", "misprint_in_print", None, "high",
    "si $f\\times_S1_{Y'}$ est", "si $f\\times1_{S'}$ est",
    "same misprint as the diagram label; the TeX silently corrects it; enlarged crop",
    corrected="f\\times_S1_{Y'}")
add(102, "proof of (5.4.8), last line: 'il en est de même de f×1_{Y′}'", "f×1_{Y′} (no subscript under ×)",
    "f\\times_Y1_{Y'}", "formula", None, "high", "$f\\times_Y1_{Y'}$", "$f\\times1_{Y'}$",
    "the print uses the label of the diagram's top arrow, which the TeX gives as f\\times1_{Y'}; not a misprint; "
    "enlarged crop")
add(102, "Remarque (5.4.9): 's'il satisfait à la condition b) de la définition (5.4.1)'", "b) in italics",
    "b) upright (judged as if the remark body were roman)", "italics", None, "high",
    "condition b) de la définition", "condition \\emph{b)} de la définition", "enlarged crop")
add(102, "last line of the page: 'Le lecteur observera que' (sentence continues on p. 103)",
    "one sentence across the page break; p. 103 begins flush left with 'dans les propositions'",
    "blank line before \\oldpage[II]{103}", "other", None, "high",
    "Le lecteur observera que" + NL + NL, "Le lecteur observera que" + NL,
    "spurious paragraph break (GLOBAL_ISSUES item 20); apply together with the p. 103 entry that removes the "
    "blank line after the marker")

# ---------------- page 103 ----------------
add(103, "first line: 'dans les propositions (5.4.2) à (5.4.8)'",
    "no paragraph break: the first line continues the sentence of p. 102, flush left",
    "blank line after \\oldpage[II]{103}", "other", None, "high",
    "\\oldpage[II]{103}" + NL + NL + "dans les", "\\oldpage[II]{103}" + NL + "dans les",
    "spurious paragraph break (GLOBAL_ISSUES item 20); apply together with the p. 102 entry 'Le lecteur observera "
    "que'. \\oldpage ends with \\ignorespaces, so joining the lines leaves a single space")
boldI(103, "(5.4.10): 'd'espace sous-jacent Z (I, 5.2.1)'", "5.2.1",
      old="$Z$ (\\hyperref[I.5.2.1-fr]{I, 5.2.1})", new="$Z$ (\\hyperref[I.5.2.1-fr]{\\textbf{I}, 5.2.1})")
add(103, "(5.4.10): '(I, 5.2.1), est propre. Comme'", "'propre' in italics", "propre upright", "italics", None,
    "high", "est propre." + NL + "Comme", "est \\emph{propre}." + NL + "Comme")
boldI(103, "(5.4.10): '(5.4.6) et (I, 5.5.1, (vi))'", "5.5.1, (vi)")
add(103, "(5.4.10): 'la propriété précédente ne dépend pas du'", "'ne dépend pas' in italics",
    "ne dépend pas upright", "italics", None, "high", "précédente ne dépend pas du",
    "précédente \\emph{ne dépend pas} du")
add(103, "(5.4.10): 'Si g : X′→X est un morphisme propre'", "'propre' in italics", "propre upright", "italics",
    None, "high", "$g:X'\\to X$ est un morphisme propre,", "$g:X'\\to X$ est un morphisme \\emph{propre},",
    "enlarged crop")
add(103, "(5.4.10): 'g^{-1}(Z) est une partie propre de X′'", "'propre' in italics", "propre upright", "italics",
    None, "high", "une partie propre de $X'$~:", "une partie \\emph{propre} de $X'$~:", "enlarged crop")
add(103, "(5.4.10): 'si X″ est un Y-schéma de type fini'", "'schéma' in italics", "schéma upright", "italics",
    None, "high", "$Y$-schéma de type fini et $u", "$Y$-\\emph{schéma} de type fini et $u", "enlarged crop")
add(103, "(5.4.10): 'u(Z) est une partie propre de X″'", "'propre' in italics", "propre upright", "italics", None,
    "high", "partie propre de $X''$~;", "partie \\emph{propre} de $X''$~;", "enlarged crop")
boldI(103, "(5.4.10): 'ayant u(Z) pour espace sous-jacent (I, 5.2.1)'", "5.2.1",
      old="{I, 5.2.1}), de sorte", new="{\\textbf{I}, 5.2.1}), de sorte")
add(103, "(5.4.10): display T→T″→X″", "no comma after the display", "T\\xrightarrow{v}T''\\xrightarrow{j}X'',",
    "punctuation", None, "high", "\\xrightarrow{j}X'',", "\\xrightarrow{j}X''",
    "extra comma in the TeX; enlarged crop")
boldI(103, "(5.4.10): 'l'injection canonique (I, 5.2.2)'", "5.2.2")
add(103, "after (5.4.10), 2°: '(et en particulier est fermée dans X″)'", "'fermée dans' in italics",
    "fermée dans upright", "italics", None, "high", "est fermée dans $X''$)", "est \\emph{fermée dans} $X''$)")
add(103, "Proposition (5.5.1), a): 'à un sous-préschéma fermé d'un fibré projectif'",
    "'fermé' roman inside the italic statement", "fermé italic", "convention", 6, "high",
    "sous-préschéma fermé d'un", "sous-préschéma \\textup{fermé} d'un", "enlarged crop")
add(103, "proof of (5.5.1): 'La condition a) entraîne b)'", "a) and b) in italics", "a), b) upright", "italics",
    None, "high", "La condition a) entraîne b)", "La condition \\emph{a)} entraîne \\emph{b)}")
add(103, "proof of (5.5.1): 'La condition b) implique a)'", "b) and a) in italics", "b), a) upright", "italics",
    None, "high", "La condition b) implique a)", "La condition \\emph{b)} implique \\emph{a)}")

# ---------------- page 104 ----------------
add(104, "Définition (5.5.2): 'est projectif sur Y'", "same italic as the rest of the definition (no change of face)",
    "\\emph{projectif sur $Y$} inside the italic definition environment (comes out upright)", "convention", 6,
    "high", "\\emph{projectif sur $Y$}", "projectif sur $Y$", "drop \\emph; enlarged crop")
add(104, "Définition (5.5.2): 'ou est un Y-schéma projectif'", "same italic as the rest of the definition",
    "\\emph{$Y$-schéma projectif} (comes out upright)", "convention", 6, "high",
    "\\emph{$Y$-schéma projectif}", "$Y$-schéma projectif", "drop \\emph; enlarged crop")
add(104, "Définition (5.5.2): 'les conditions équivalentes a) et b)'", "a) roman inside the italic statement",
    "a) italic", "convention", 6, "high", "équivalentes a)", "équivalentes \\textup{a)}", "enlarged crop")
add(104, "Définition (5.5.2): 'les conditions équivalentes a) et b)'", "b) roman inside the italic statement",
    "b) italic", "convention", 6, "high", "b)" + NL + "de (", "\\textup{b)}" + NL + "de (", "enlarged crop")
add(104, "Définition (5.5.2): 'est projectif s'il fait de X'", "same italic as the rest of the definition",
    "\\emph{projectif} (comes out upright)", "convention", 6, "high",
    "\\emph{projectif} s'il", "projectif s'il", "drop \\emph; enlarged crop")
add(104, "after (5.5.2): 'un O_X-Module très ample relativement à f'",
    "only 'très ample' in italics; 'relativement à f' roman",
    "\\emph{très ample relativement à $f$}", "italics", None, "high",
    "\\emph{très ample relativement à $f$}", "\\emph{très ample} relativement à $f$", "enlarged crop")
add(104, "proof of (5.5.3), (i): 'il résulte aussitôt de (5.5.1, b))'", "b) in italics", "b) upright",
    "italics", None, "high", "{5.5.1, b)}", "{5.5.1, \\emph{b)}}", "enlarged crop")
add(104, "proof of (5.5.3), (i): 'Proj(S)×_Y Spec(k(y))'", "bold italic k", "k(y)", "convention", 1, "high",
    "\\operatorname{Spec}(k(y))", "\\operatorname{Spec}(\\boldsymbol{k}(y))", "enlarged crop")
boldI(104, "proof of (5.5.3), (i): '(I, 3.6.1)'", "3.6.1")
add(104, "proof of (5.5.3), (i): 'donc à Proj(S⊗_A k(y))'", "bold italic k", "k(y)", "convention", 1, "high",
    "\\operatorname{Proj}(S\\otimes_Ak(y))", "\\operatorname{Proj}(S\\otimes_A\\boldsymbol{k}(y))")
add(104, "proof of (5.5.3), (i): 'si et seulement si S⊗_A k(y) vérifie'", "bold italic k", "k(y)", "convention", 1,
    "high", "si $S\\otimes_Ak(y)$", "si $S\\otimes_A\\boldsymbol{k}(y)$", "enlarged crop")
add(104, "proof of (5.5.3), (i): 'S_n⊗_A k(y)=0'", "bold italic k", "k(y)", "convention", 1, "high",
    "$S_n\\otimes_Ak(y)=0$", "$S_n\\otimes_A\\boldsymbol{k}(y)=0$")
boldI(104, "proof of (5.5.3), (i): 'pour n assez grand (0, 1.7.4)'", "1.7.4", zero=True)
boldI(104, "proof of (5.5.3), (i): 'ayant X′ pour espace sous-jacent (I, 5.2.1)'", "5.2.1")
add(104, "proof of (5.5.3), (i): 'il est clair (5.5.1, a))'", "a) in italics", "a) upright", "italics", None,
    "high", "{5.5.1, a)}", "{5.5.1, \\emph{a)}}", "enlarged crop")
add(104, "proof of (5.5.3), (ii): 'j est fermée par (5.4.4)'", "'fermée' in italics", "fermée upright", "italics",
    None, "high", "$j$ est fermée par", "$j$ est \\emph{fermée} par")
add(104, "Remarques (5.5.4), (i): '1° f soit propre'", "'propre' in italics", "propre upright", "italics", None,
    "high", "$f$ soit propre~;", "$f$ soit \\emph{propre}~;",
    "the TeX sets (5.5.4) with a manual heading and a roman body, so \\emph gives italics; enlarged crop")
add(104, "Remarques (5.5.4), (i): '2° ... L très ample relativement à f'", "'très ample' in italics",
    "très ample upright", "italics", None, "high", "$\\mathcal{L}$ très ample", "$\\mathcal{L}$ \\emph{très ample}",
    "enlarged crop")
add(104, "Remarques (5.5.4), (i): '3° ... soit de type fini'", "'de type fini' in italics", "de type fini upright",
    "italics", None, "high", "soit de type fini. Alors", "soit \\emph{de type fini}. Alors", "enlarged crop")
add(104, "Remarques (5.5.4), (i): 'Alors f est un morphisme projectif :'", "'projectif' in italics",
    "projectif upright", "italics", None, "high", "projectif~: en effet", "\\emph{projectif}~: en effet",
    "enlarged crop")
add(104, "Remarques (5.5.4), (i): 'r est une immersion fermée (5.4.4)'", "'fermée' in italics", "fermée upright",
    "italics", None, "high", "immersion fermée (", "immersion \\emph{fermée} (", "enlarged crop")
add(104, "Remarques (5.5.4), (i): 'lorsque Y est localement noethérien'", "'localement noethérien' in italics",
    "localement noethérien upright", "italics", None, "high", "est localement noethérien, la",
    "est \\emph{localement noethérien}, la", "enlarged crop")
add(104, "Remarques (5.5.4), (i): 'les conditions 1° et 2° caractérisent dans ce cas'", "'caractérisent' in italics",
    "caractérisent upright", "italics", None, "high", "caractérisent dans", "\\emph{caractérisent} dans",
    "enlarged crop")
add(104, "Remarques (5.5.4), (i): 'd'un O_X-Module ample pour f'", "'ample' in italics", "ample upright",
    "italics", None, "high", "Module ample pour", "Module \\emph{ample} pour", "enlarged crop")
add(104, "Remarques (5.5.4), (ii): 'Pour qu'un Y-schéma X soit projectif'", "'projectif' in italics",
    "projectif upright", "italics", None, "high", "$X$ soit projectif, il", "$X$ soit \\emph{projectif}, il",
    "enlarged crop")
add(104, "Remarques (5.5.4), (ii): 'à un sous-Y-schéma fermé d'un fibré projectif'", "'fermé' in italics",
    "fermé upright", "italics", None, "high", "sous-$Y$-schéma fermé d'un", "sous-$Y$-schéma \\emph{fermé} d'un",
    "enlarged crop")

# ---------------- checks ----------------
pages = {}
for p in range(100, 105):
    pages[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
rel = REL.read_text(encoding="utf-8")
ok = True
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    n = pages[d["page"]].count(fx["old"])
    m = rel.count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE on page", d["page"], n, repr(fx["old"]))
    if m != 1:
        print("  (release file count", m, ")", d["page"], repr(fx["old"]))
# overlap check: apply all fixes of a page in sequence, in both orders
for p in range(100, 105):
    fl = [d["fix"] for d in F if d["page"] == p and d["fix"]]
    for order in (fl, list(reversed(fl))):
        t = pages[p]
        for fx in order:
            if t.count(fx["old"]) != 1:
                ok = False
                print("OVERLAP on page", p, repr(fx["old"]))
            t = t.replace(fx["old"], fx["new"], 1)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
c = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    c[(d["page"], k)] += 1
for p in range(100, 105):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("total", len(F), "ok" if ok else "PROBLEMS")
