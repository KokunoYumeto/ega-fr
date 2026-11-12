import json
from collections import Counter

BASE = r"user\Documents\ega_scan_check_20261101\run_IV3"
OUT = BASE + r"\findings_055_059.json"
NL = "<NL>"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 55
p = 55
add(p, "top of the page, Proposition (9.1.1) continued after the list (i)-(iii): 'Soit alors Ω une extension algébriquement close de k'",
    "'Soit alors …' begins an indented new paragraph",
    "\\end{enumerate} (end of p. 54), the marker and 'Soit alors' with no blank line: set without indent",
    "other", None, "high",
    r"\oldpage[IV-3]{55}<NL>Soit alors", r"\oldpage[IV-3]{55}<NL><NL>Soit alors",
    "GLOBAL_ISSUES 80 (text after \\end{enumerate} without a blank line). The \\end{enumerate} stands before the marker in the p. 54 segment, so the blank line goes after the marker.")
add(p, "(9.1.1) b): 'Il existe K'∈C qui est une extension finie de k.'",
    "'finie' printed roman inside the italic statement",
    "finie (italic in the proposition environment)",
    "convention", 6, "high",
    r"qui est une extension finie de", r"qui est une extension \textup{finie} de",
    "Enlarged crop crops_055_059/p55_b_finie.png. In (9.1.4) b) 'finie' is italic (no change there).")
cf = [
    ("(9.1.1) a): 'C est non vide.'", r"$\mathcal C$ est non vide", r"$\boldsymbol{C}$ est non vide"),
    ("(9.1.1) b): 'Il existe K'∈C'", r"Il existe $K'\in\mathcal C$", r"Il existe $K'\in\boldsymbol{C}$"),
    ("(9.1.1) c): 'On a Ω∈C.'", r"$\Omega\in\mathcal C$", r"$\Omega\in\boldsymbol{C}$"),
    ("proof of (9.1.1): 'il existe une extension K'∈C qui est de la forme A/m'", r"$K'\in\mathcal C$ qui est de", r"$K'\in\boldsymbol{C}$ qui est de"),
    ("Corollaire (9.1.2): 'si C n'est pas vide, C contient toutes les extensions' (2 occurrences)", r"si $\mathcal C$ n'est pas vide, $\mathcal C$ contient", r"si $\boldsymbol{C}$ n'est pas vide, $\boldsymbol{C}$ contient"),
    ("proof of (9.1.2): 'on a k∈C'", r"$k\in\mathcal C$", r"$k\in\boldsymbol{C}$"),
    ("Remarque (9.1.3): 'Fréquemment l'ensemble C est formé des corps'", r"l'ensemble $\mathcal C$ est formé", r"l'ensemble $\boldsymbol{C}$ est formé"),
    ("Remarque (9.1.3): 'un ensemble C' de k-algèbres'", r"ensemble $\mathcal C'$ de", r"ensemble $\boldsymbol{C}'$ de"),
    ("Remarque (9.1.3), (i bis): 'Si A∈C' et s'il existe'", r"\in\mathcal C'$ et s'il", r"\in\boldsymbol{C}'$ et s'il"),
    ("Remarque (9.1.3), (i bis): 'alors A'∈C''", r"$A'\in\mathcal C'$", r"$A'\in\boldsymbol{C}'$"),
    ("proof of (9.1.4): 'en prenant pour C' l'ensemble de toutes les k-algèbres'", r"pour $\mathcal C'$ l'ensemble", r"pour $\boldsymbol{C}'$ l'ensemble"),
]
for where, old, new in cf:
    add(p, where, "bold italic C (the set of extensions / of k-algebras)", "\\mathcal C (calligraphic)",
        "font", None, "high", old, new,
        "Coordinator's reading: the bold italic C is \\boldsymbol{C}. ega4-9-fr.tex writes this set \\mathcal C throughout (18 lines, source lines 30-116).")
add(p, "Corollaire (9.1.2): 'Sous les hypothèses (i), (ii), (iii) de (9.1.1), si k est …'",
    "(i), (ii), (iii) and (9.1.1) printed upright inside the italic statement",
    "italic (corollary environment)",
    "convention", 6, "high",
    r"Sous les hypothèses (i), (ii), (iii) de (9.1.1),",
    r"Sous les hypothèses \textup{(i), (ii), (iii)} de \textup{(9.1.1)},",
    "References inside italic statements are upright in the print (same treatment as \\textup{(8.2.2)} on p. 8).")
add(p, "Remarque (9.1.3): label of the condition '(i bis)'",
    "(i bis) with 'bis' italic",
    "label=(i bis), no italic",
    "italics", None, "high",
    r"[label=(i bis)]", r"[label=(i \emph{bis})]",
    "GLOBAL_ISSUES 26. Judged with the remark body roman.")
add(p, "Remarque (9.1.3): text of condition (i bis) 'Si A∈C' et s'il existe un homomorphisme … alors A'∈C'.'",
    "the condition is printed in italic inside the roman remark",
    "no italic markup (italic now only because the remark environment is italic)",
    "italics", None, "high",
    r"\item Si $A", r"\item \itshape Si $A",
    "Judged with the remark body roman; \\itshape lasts to \\end{enumerate} (same form as the EGA I p. 114 fix). Leaves the \\boldsymbol{C}' fixes in the same item untouched.")
add(p, "Remarque (9.1.3): 'Lorsqu'il en est ainsi, la condition (i) est trivialement satisfaite' after the (i bis) list",
    "indented new paragraph",
    "follows \\end{enumerate} without a blank line: set without indent",
    "other", None, "high",
    r"\end{enumerate}<NL>Lorsqu'il", r"\end{enumerate}<NL><NL>Lorsqu'il",
    "GLOBAL_ISSUES 80.")
add(p, "Remarque (9.1.3): 'Par contre, lorsque (i bis) n'est pas vérifiée'",
    "(i bis) with 'bis' italic", "(i bis)",
    "italics", None, "high",
    r"lorsque (i bis) n'est", r"lorsque (i \emph{bis}) n'est",
    "GLOBAL_ISSUES 26. Judged with the remark body roman.")
for where, old, new in [
        ("Proposition (9.1.4) a): '(resp. un Ω-morphisme possédant l'une (déterminée)'", r"(resp. un $\Omega$-morphisme", r"(\textup{resp.} un $\Omega$-morphisme"),
        ("Proposition (9.1.4) b): '(resp. un k'-morphisme possédant la propriété considérée)'", r"(resp. un $k'$-morphisme", r"(\textup{resp.} un $k'$-morphisme"),
        ("Proposition (9.1.4) c): '(resp. un K-morphisme possédant la propriété considérée)'", r"(resp. un $K$-morphisme", r"(\textup{resp.} un $K$-morphisme")]:
    add(p, where, "'resp.' printed roman inside the italic statement", "italic (proposition environment)",
        "convention", 6, "high", old, new, "Enlarged crop p55_914a.png.")
add(p, "Proposition (9.1.4) a): 'des propriétés (i) à (xiv) de (8.10.5)).'",
    "(i), (xiv), (8.10.5) upright; 'à', 'de' italic",
    "italic (proposition environment)",
    "convention", 6, "high",
    r"(i) à (xiv) de (8.10.5))", r"\textup{(i)} à \textup{(xiv)} de \textup{(8.10.5)})",
    "Enlarged crop p55_914a.png.")
add(p, "proof of (9.1.4): 'La condition (i bis) de (9.1.3) est alors vérifiée'",
    "(i bis) with 'bis' italic", "(i bis)",
    "italics", None, "high",
    r"La condition (i bis) de", r"La condition (i \emph{bis}) de",
    "GLOBAL_ISSUES 26.")
add(p, "end of the page: '… grâce au fait que les' / p. 56 'propriétés envisagées dans (8.10.5)'",
    "the sentence runs on over the page break (p. 56 starts flush left)",
    "blank line before \\oldpage[IV-3]{56}: paragraph break mid-sentence",
    "marker", None, "high",
    r"grâce au fait que les<NL><NL>", r"grâce au fait que les<NL>",
    "Marker position itself is right.")

# ---------------------------------------------------------------- page 56
p = 56
add(p, "'Le corollaire suivant généralise (II, 6.6.5) :'", "(𝐈𝐈, 6.6.5): bold II", "(II, 6.6.5)",
    "convention", 2, "high", r"généralise (II, 6.6.5)", r"généralise (\textbf{II}, 6.6.5)", "")
add(p, "Corollaire (9.1.5): 'soit projectif (resp. quasi-projectif) sur K'",
    "'resp.' roman inside the italic statement", "italic (corollary environment)",
    "convention", 6, "high",
    r"projectif (resp. quasi-projectif) sur $K$", r"projectif (\textup{resp.} quasi-projectif) sur $K$", "")
add(p, "Corollaire (9.1.5): 'alors X est projectif (resp. quasi-projectif) sur k.'",
    "'resp.' roman inside the italic statement", "italic (corollary environment)",
    "convention", 6, "high",
    r"projectif (resp. quasi-projectif) sur $k$.", r"projectif (\textup{resp.} quasi-projectif) sur $k$.", "")
add(p, "proof of (9.1.5): '(II, 5.5.4, (ii) et 5.5.3)'", "bold II", "(II, 5.5.4, (ii) et 5.5.3)",
    "convention", 2, "high", r"(II, 5.5.4, (ii) et 5.5.3)", r"(\textbf{II}, 5.5.4, (ii) et 5.5.3)",
    "The projective P^r_K, P^r_k, P^r_{k'} in this proof are bold UPRIGHT in the print (\\mathbf P correct; measured with crops_055_059/slant.py).")
add(p, "proof of (9.1.5): 'On conclut alors par (II, 6.6.5).'", "bold II", "(II, 6.6.5)",
    "convention", 2, "high", r"par (II, 6.6.5)", r"par (\textbf{II}, 6.6.5)", "")
add(p, "subsection heading 9.2", "'9.2. Propriétés constructibles et ind-constructibles.' (final full stop)",
    "no full stop", "punctuation", None, "high",
    r"\subsection{Propriétés constructibles et ind-constructibles}",
    r"\subsection{Propriétés constructibles et ind-constructibles.}",
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop).")
add(p, "Définition (9.2.1): 'Soit P(X, F, k) une relation.'", "bold italic P", "\\mathbf P",
    "convention", 10, "high", r"Soit $\mathbf P(X", r"Soit $\boldsymbol{P}(X",
    "Every property letter P on pp. 56-59, inside the italic statements too, leans like the bold italic P of the roman text (left-edge slant +15 to +27 px per 100 px; the upright projective P of p. 56 measures about 0): crops_055_059/slant.py, pcomp1.png.")
add(p, "Définition (9.2.1): 'On dit que P est une propriété'", "bold italic P", "\\mathbf P",
    "convention", 10, "high", r"que $\mathbf P$ est une", r"que $\boldsymbol{P}$ est une", "")
add(p, "Définition (9.2.1): 'une propriété constructible (resp. ind-constructible) de préschémas algébriques'",
    "'constructible' and 'ind-constructible' italic like the rest of the statement; 'resp.' roman",
    "\\emph{constructible}, \\emph{ind-constructible} inside the italic definition (come out upright); 'resp.' italic",
    "convention", 6, "high",
    r"propriété \emph{constructible} (resp. \emph{ind-constructible}) de",
    r"propriété constructible (\textup{resp.} ind-constructible) de",
    "Crop p56_def_a.png. FIX_POLICY 2.6: drop \\emph where the print shows no change of face.")
add(p, "Définition (9.2.1): item labels (i), (ii)", "(i), (ii) upright", "label=(\\roman*) inside the italic definition: italic labels",
    "convention", 6, "high",
    r"\begin{enumerate}[label=(\roman*)]", r"\begin{enumerate}[label=\textup{(\roman*)}]",
    "GLOBAL_ISSUES 16. Covers both labels.")
add(p, "Définition (9.2.1) (i): 'pour que P(X, F, k) soit vraie'", "bold italic P", "\\mathbf P",
    "convention", 10, "high", r"pour que $\mathbf P(X", r"pour que $\boldsymbol{P}(X", "")
add(p, "Définition (9.2.1) (i): 'il faut et il suffit que P(X_(k'), F⊗_k k', k') soit vraie'", "bold italic P", "\\mathbf P",
    "convention", 10, "high", r"$\mathbf P(X_{(k')}", r"$\boldsymbol{P}(X_{(k')}", "")
add(p, "Définition (9.2.1) (ii): 'X_s=u^{-1}(s)=X×_S Spec(k(s))'", "bold italic k in k(s)", "k(s)",
    "convention", 1, "high", r"\operatorname{Spec}(k(s))", r"\operatorname{Spec}(\boldsymbol{k}(s))", "Crop z56_k1.png.")
add(p, "Définition (9.2.1) (ii): 'F_s=F⊗_{O_S} k(s)'", "bold italic k in k(s)", "k(s)",
    "convention", 1, "high", r"\otimes_{\mathcal O_S}k(s)", r"\otimes_{\mathcal O_S}\boldsymbol{k}(s)", "")
add(p, "Définition (9.2.1) (ii): 'tels que P(X_s, F_s, k(s)) soit vraie'", "bold italic P", "\\mathbf P",
    "convention", 10, "high", r"$\mathbf P(X_s", r"$\boldsymbol{P}(X_s", "")
add(p, "Définition (9.2.1) (ii): 'P(X_s, F_s, k(s))'", "bold italic k in k(s)", "k(s)",
    "convention", 1, "high", r"F_s,k(s))$", r"F_s,\boldsymbol{k}(s))$", "")
add(p, "Définition (9.2.1) (ii): 'l'un des ensembles E, S—E'", "long dash S—E", "S-E",
    "convention", 7, "high", r"$E$, $S-E$", r"$E$, $S\setmin E$", "")
add(p, "Définition (9.2.1) (ii): '(resp. l'ensemble E)'", "'resp.' roman inside the italic statement", "italic",
    "convention", 6, "high", r"(resp. l'ensemble $E$)", r"(\textup{resp.} l'ensemble $E$)", "Crop p56_ii_end.png.")
add(p, "Définition (9.2.1) (ii): '(et par suite est un voisinage de η)'", "the whole parenthesis printed roman", "italic",
    "convention", 6, "high",
    r"(et par suite est un voisinage de $\eta$)", r"\textup{(et par suite est un voisinage de $\eta$)}", "Crop p56_ii_end.png.")
add(p, "Définition (9.2.1) (ii): '(resp. contient un ouvert non vide s'il contient η)'", "'resp.' roman", "italic",
    "convention", 6, "high", r"(resp. contient", r"(\textup{resp.} contient", "")

# ---------------------------------------------------------------- page 57
p = 57
P57 = [
    ("Remarques (9.2.2) (ii): 'soit P(X, Z, k) une relation'", r"$\mathbf P(X,Z,k)$ une relation", r"$\boldsymbol{P}(X,Z,k)$ une relation"),
    ("Remarques (9.2.2) (ii): 'que P est une propriété constructible (resp. ind-constructible)'", r"$\mathbf P$ est une propriété constructible (resp.", r"$\boldsymbol{P}$ est une propriété constructible (resp."),
    ("Remarques (9.2.2) (ii) 1°: 'pour que P(X, Z, k) soit vraie'", r"$\mathbf P(X,Z,k)$ soit vraie", r"$\boldsymbol{P}(X,Z,k)$ soit vraie"),
    ("Remarques (9.2.2) (ii) 1°: 'P(X_(k'), p^{-1}(Z), k') soit vraie'", r"$\mathbf P(X_{(k')}", r"$\boldsymbol{P}(X_{(k')}"),
    ("Remarques (9.2.2) (ii) 2°: 'tels que P(X_s, Z_s, k(s))'", r"$\mathbf P(X_s,Z_s", r"$\boldsymbol{P}(X_s,Z_s"),
    ("Remarques (9.2.2) (iii): 'Si P est une propriété constructible'", r"Si $\mathbf P$ est une", r"Si $\boldsymbol{P}$ est une"),
    ("Remarques (9.2.2) (iii): '« non P »'", r"non $\mathbf P$~»", r"non $\boldsymbol{P}$~»"),
    ("Remarques (9.2.2) (iii): 'Si P, Q sont deux propriétés'", r"Si $\mathbf P$,", r"Si $\boldsymbol{P}$,"),
    ("Remarques (9.2.2) (iii): '« P ou Q »'", r"«~$\mathbf P$ ou", r"«~$\boldsymbol{P}$ ou"),
    ("Remarques (9.2.2) (iii): '« P et Q »'", r"«~$\mathbf P$ et", r"«~$\boldsymbol{P}$ et"),
    ("Remarques (9.2.2) (iv): 'Soit P(X, F, k) une relation vérifiant'", r"Soit $\mathbf P(X,\mathcal F,k)$", r"Soit $\boldsymbol{P}(X,\mathcal F,k)$"),
    ("Remarques (9.2.2) (iv): 'tels que P(X_s, F_s, k(s)) soit vraie'", r"$\mathbf P(X_s,\mathcal F_s", r"$\boldsymbol{P}(X_s,\mathcal F_s"),
    ("Remarques (9.2.2) (iv): 'tels que P(X'_{s'}, F'_{s'}, k(s'))'", r"$\mathbf P(X'_{s'}", r"$\boldsymbol{P}(X'_{s'}"),
    ("Remarques (9.2.2) (iv): 'au cas où il figure dans P plusieurs préschémas'", r"figure dans $\mathbf P$", r"figure dans $\boldsymbol{P}$"),
    ("Remarques (9.2.2) (v): 'la plupart des propriétés P vérifiant la condition'", r"propriétés $\mathbf P$ vérifiant", r"propriétés $\boldsymbol{P}$ vérifiant"),
]
for where, old, new in P57:
    add(p, where, "bold italic P", "\\mathbf P", "convention", 10, "high", old, new, "")
for where, old, new in [
        ("Remarques (9.2.2) (iii): 'Si P, Q sont deux propriétés'", r"$\mathbf Q$ sont deux", r"$\boldsymbol{Q}$ sont deux"),
        ("Remarques (9.2.2) (iii): '« P ou Q »'", r"$\mathbf Q$~» et", r"$\boldsymbol{Q}$~» et"),
        ("Remarques (9.2.2) (iii): '« P et Q »'", r"$\mathbf Q$~»~;", r"$\boldsymbol{Q}$~»~;")]:
    add(p, where, "bold italic Q (property letter)", "\\mathbf Q (bold upright)", "font", None, "high", old, new,
        "Same pattern as convention 10, for the property letter Q (not the rationals). Crop p57_iii_PQ.png.")
add(p, "Remarques (9.2.2) (ii) 2°: 'P(X_s, Z_s, k(s)) soit vraie'", "bold italic k in k(s)", "k(s)",
    "convention", 1, "high", r",k(s))$ soit vraie. Alors", r",\boldsymbol{k}(s))$ soit vraie. Alors", "")
add(p, "Remarques (9.2.2) (ii) 2°: 'Alors l'un des ensembles E, S—E (resp. l'ensemble E)'", "long dash S—E", "S-E",
    "convention", 7, "high", r"$S-E$ (resp. l'ensemble", r"$S\setmin E$ (resp. l'ensemble", "")
add(p, "Remarques (9.2.2) (ii), 'On notera …': 'que Z est une partie constructible de X, et non seulement que'",
    "'de' and 'non seulement' italic", "upright (judged with the remark body roman)",
    "italics", None, "high",
    r"constructible de $X$, et non seulement", r"constructible \emph{de} $X$, et \emph{non seulement}",
    "Crop p57_onnotera.png. Judged with the remark body roman.")
add(p, "Remarques (9.2.2) (ii), 'On notera …': 'Z_s est une partie constructible de X_s pour tout s'",
    "'de' italic", "upright (judged with the remark body roman)",
    "italics", None, "high",
    r"constructible de $X_s$", r"constructible \emph{de} $X_s$", "Crop p57_onnotera.png.")
add(p, "Remarques (9.2.2) (iii): 'et si S—E et S—E' contiennent chacun'", "long dashes", "S-E, S-E'",
    "convention", 7, "high", r"si $S-E$ et $S-E'$ contiennent", r"si $S\setmin E$ et $S\setmin E'$ contiennent", "Two occurrences.")
add(p, "Remarques (9.2.2) (iii): 'S—(E∪E')=(S—E)∩(S—E')'", "long dashes", "S-(E\\cup E')=(S-E)\\cap(S-E')",
    "convention", 7, "high", r"$S-(E\cup E')=(S-E)\cap(S-E')$", r"$S\setmin(E\cup E')=(S\setmin E)\cap(S\setmin E')$", "Three occurrences.")
add(p, "Remarques (9.2.2) (iv): 'P(X_s, F_s, k(s)) soit vraie. Soit d'autre part'", "bold italic k in k(s)", "k(s)",
    "convention", 1, "high", r",k(s))$ soit vraie. Soit", r",\boldsymbol{k}(s))$ soit vraie. Soit", "")
add(p, "Remarques (9.2.2) (iv): 'la transitivité des fibres (I, 3.6.4)'", "(𝐈, 3.6.4): bold I", "(I, 3.6.4)",
    "convention", 2, "high", r"(I, 3.6.4)", r"(\textbf{I}, 3.6.4)", "")
add(p, "Remarques (9.2.2) (iv): 'l'ensemble des s'∈S' tels que P(X'_{s'}, F'_{s'}, k(s')) soit vraie est égal à g^{-1}(E)'",
    "F'_{s'} printed with a ROMAN F (serif capital), although the sheaf is defined two lines above as script F' = F⊗_{O_S}O_{S'}",
    "\\mathcal F'_{s'} (silently corrected)",
    "misprint_in_print", None, "high",
    r"\mathcal F'_{s'}", r"F'_{s'}",
    "Wrong fount in the print (roman for script), as GLOBAL_ISSUES 29 treats wrong-font letters. The diplomatic text keeps the printed roman F'. Crops p57_iv_Fprime.png (roman F') and p57_iv_posons.png (script F' in the definition).",
    corrected=r"\mathcal F'_{s'}")
add(p, "Remarques (9.2.2) (iv): 'k(s')'", "bold italic k in k(s')", "k(s')",
    "convention", 1, "high", r",k(s'))$", r",\boldsymbol{k}(s'))$", "")
add(p, "end of the page: '… et où toutes les fibres X_s' / p. 58 'sauf la fibre générique'",
    "the sentence runs on over the page break (p. 58 starts flush left)",
    "blank line before \\oldpage[IV-3]{58}: paragraph break mid-sentence",
    "marker", None, "high",
    r"toutes les fibres $X_s$<NL><NL>", r"toutes les fibres $X_s$<NL>",
    "Marker position itself is right.")

# ---------------------------------------------------------------- page 58
p = 58
add(p, "l. 1, Remarques (9.2.2) (v) end: 'sauf la fibre générique X_η'", "'sauf' italic", "upright (judged with the remark body roman)",
    "italics", None, "high", r"sauf la fibre générique", r"\emph{sauf} la fibre générique", "Crop p58_sauf.png.")
add(p, "l. 1: 'sont projectives sur k(s)'", "bold italic k in k(s)", "k(s)",
    "convention", 1, "high", r"projectives sur $k(s)$", r"projectives sur $\boldsymbol{k}(s)$", "")
add(p, "Proposition (9.2.3): 'Soient P une propriété constructible'", "bold italic P", "\\mathbf P",
    "convention", 10, "high", r"\label{IV.9.2.3-fr}<NL>Soient $\mathbf P$", r"\label{IV.9.2.3-fr}<NL>Soient $\boldsymbol{P}$", "")
add(p, "Proposition (9.2.3): '(resp. ind-constructible) de préschémas algébriques, S un préschéma'", "'resp.' roman", "italic",
    "convention", 6, "high", r"(resp. ind-constructible) de<NL>préschémas algébriques, $S$", r"(\textup{resp.} ind-constructible) de<NL>préschémas algébriques, $S$", "")
add(p, "Proposition (9.2.3): 'tels que P(X_s, F_s, k(s)) soit vraie'", "bold italic P", "\\mathbf P",
    "convention", 10, "high", r"$\mathbf P(X_s", r"$\boldsymbol{P}(X_s", "")
add(p, "Proposition (9.2.3): 'P(X_s, F_s, k(s))'", "bold italic k in k(s)", "k(s)",
    "convention", 1, "high", r",k(s))$ soit vraie est", r",\boldsymbol{k}(s))$ soit vraie est", "")
add(p, "Proposition (9.2.3): 'est localement constructible (resp. ind-constructible). En outre'", "'resp.' roman", "italic",
    "convention", 6, "high", r"(resp. ind-constructible). En outre", r"(\textup{resp.} ind-constructible). En outre", "")
add(p, "Proposition (9.2.3): 'un des deux ensembles E, S—E est un voisinage de η'", "long dash S—E", "S-E",
    "convention", 7, "high", r"$S-E$ est un voisinage", r"$S\setmin E$ est un voisinage", "")
add(p, "Proposition (9.2.3): '(resp. E est un voisinage de η s'il contient ce point)'", "'resp.' roman", "italic",
    "convention", 6, "high", r"(resp. $E$ est un voisinage", r"(\textup{resp.} $E$ est un voisinage", "")
add(p, "proof of (9.2.3), display 'P((X_0)_{s_0}, (F_0)_{s_0}, k(s_0))'", "bold italic P", "\\mathbf P",
    "convention", 10, "high", r"\mathbf P((X_0)", r"\boldsymbol{P}((X_0)", "Crop p58_disp.png.")
add(p, "proof of (9.2.3), same display: 'k(s_0)'", "bold italic k in k(s_0)", "k(s_0)",
    "convention", 1, "high", r",k(s_0))", r",\boldsymbol{k}(s_0))", "")
add(p, "proof of (9.2.3): 'donc un schéma noethérien. Utilisons'", "'noethérien' italic", "upright",
    "italics", None, "high", r"donc un schéma noethérien", r"donc un schéma \emph{noethérien}", "")
add(p, "proof of (9.2.3): 'en remplaçant S par un sous-schéma fermé intègre de S'", "'intègre' italic", "upright",
    "italics", None, "high", r"intègre de $S$", r"\emph{intègre} de $S$", "")
add(p, "after the proof of (9.2.3): 's'applique aussi lorsqu'il figure dans P plusieurs préschémas'", "bold italic P", "\\mathbf P",
    "convention", 10, "high", r"figure dans $\mathbf P$", r"figure dans $\boldsymbol{P}$", "")
add(p, "Corollaire (9.2.4): 'Soient P une propriété constructible'", "bold italic P", "\\mathbf P",
    "convention", 10, "high", r"\label{IV.9.2.4-fr}<NL>Soient $\mathbf P$", r"\label{IV.9.2.4-fr}<NL>Soient $\boldsymbol{P}$", "")
add(p, "Corollaire (9.2.4): '(resp. ind-constructible) de préschémas algébriques, X, Y deux S-préschémas'", "'resp.' roman", "italic",
    "convention", 6, "high", r"(resp. ind-constructible) de<NL>préschémas algébriques, $X$", r"(\textup{resp.} ind-constructible) de<NL>préschémas algébriques, $X$", "")
add(p, "Corollaire (9.2.4): 'X_s=X×_S Spec(k(s))'", "bold italic k in k(s)", "k(s)",
    "convention", 1, "high", r"X\times_S\operatorname{Spec}(k(s))", r"X\times_S\operatorname{Spec}(\boldsymbol{k}(s))", "")
add(p, "Corollaire (9.2.4): 'Y_s=Y×_S Spec(k(s))'", "bold italic k in k(s)", "k(s)",
    "convention", 1, "high", r"Y\times_S\operatorname{Spec}(k(s))", r"Y\times_S\operatorname{Spec}(\boldsymbol{k}(s))", "")
add(p, "Corollaire (9.2.4): 'la propriété P(f_s^{-1}(y), k(y)) soit vraie'", "bold italic P", "\\mathbf P",
    "convention", 10, "high", r"$\mathbf P(f_s^{-1}", r"$\boldsymbol{P}(f_s^{-1}", "")
add(p, "Corollaire (9.2.4): 'k(y)'", "bold italic k in k(y)", "k(y)",
    "convention", 1, "high", r",k(y))$ soit vraie, est", r",\boldsymbol{k}(y))$ soit vraie, est", "")
add(p, "Corollaire (9.2.4), end: 'localement constructible (resp. ind-constructible).'", "'resp.' roman", "italic",
    "convention", 6, "high", r"(resp. ind-constructible).<NL>\end{corollary}", r"(\textup{resp.} ind-constructible).<NL>\end{corollary}", "")
add(p, "proof of (9.2.4): 'tels que P(f^{-1}(y), k(y)) soit vraie'", "bold italic P", "\\mathbf P",
    "convention", 10, "high", r"$\mathbf P(f^{-1}", r"$\boldsymbol{P}(f^{-1}", "")
add(p, "proof of (9.2.4): 'k(y)'", "bold italic k in k(y)", "k(y)",
    "convention", 1, "high", r",k(y))$ soit vraie. Comme", r",\boldsymbol{k}(y))$ soit vraie. Comme", "")
add(p, "proof of (9.2.4), end: 'on a donc E=S—g(Y—Z).'", "long dashes", "E=S-g(Y-Z)",
    "convention", 7, "high", r"$E=S-g(Y-", r"$E=S\setmin g(Y\setmin", "Two occurrences.")
add(p, "end of the page: '… on a donc E=S—g(Y—Z).' / p. 59 'Or, f est de présentation finie'",
    "p. 59 'Or, f …' continues the paragraph (flush left, no indent)",
    "blank line before \\oldpage[IV-3]{59}: paragraph break the print does not have",
    "marker", None, "high",
    r"Z)$.<NL><NL>", r"Z)$.<NL>", "Marker position itself is right.")

# ---------------------------------------------------------------- page 59
p = 59
add(p, "l. 2: 'donc Y—Z est localement constructible'", "long dash Y—Z", "Y-Z",
    "convention", 7, "high", r"$Y-Z$", r"$Y\setmin Z$", "")
add(p, "l. 3: 'g(Y—Z) est localement constructible'", "long dash", "g(Y-Z)",
    "convention", 7, "high", r"$g(Y-Z)$", r"$g(Y\setmin Z)$", "")
add(p, "Remarque (9.2.5): 'On notera que si P est une propriété'", "bold italic P", "\\mathbf P",
    "convention", 10, "high", r"si $\mathbf P$ est", r"si $\boldsymbol{P}$ est", "")
add(p, "Remarque (9.2.5): 'alors P satisfait aussi à la condition'", "bold italic P", "\\mathbf P",
    "convention", 10, "high", r"alors $\mathbf P$ satisfait", r"alors $\boldsymbol{P}$ satisfait", "")
add(p, "Proposition (9.2.6): 'Désignons par P une des propriétés suivantes'", "bold italic P (measured slant, crop p59_P_desig.png)", "\\mathbf P",
    "convention", 10, "high", r"par $\mathbf P$ une", r"par $\boldsymbol{P}$ une", "")
add(p, "Proposition (9.2.6): item labels (i)-(iv)", "(i), (ii), (iii), (iv) upright", "label=(\\roman*) inside the italic proposition: italic labels",
    "convention", 6, "high", r"\begin{enumerate}[label=(\roman*)]", r"\begin{enumerate}[label=\textup{(\roman*)}]",
    "GLOBAL_ISSUES 16. Covers all four labels.")
add(p, "Proposition (9.2.6) (iv): 'Z̄=Z∪{—∞}'", "long dash for the minus sign of —∞", "-\\infty",
    "convention", 7, "high", r"\cup\{-\infty\}", r"\cup\{\setmin\infty\}", "GLOBAL_ISSUES 23/49 (long dash for minus).")
add(p, "Proposition (9.2.6): 'Alors P est constructible.' after the list", "indented new line/paragraph",
    "follows \\end{enumerate} without a blank line: set without indent",
    "other", None, "high", r"\end{enumerate}<NL>Alors", r"\end{enumerate}<NL><NL>Alors", "GLOBAL_ISSUES 80.")
add(p, "Proposition (9.2.6): 'Alors P est constructible.'", "bold italic P", "\\mathbf P",
    "convention", 10, "high", r"$\mathbf P$ est constructible.", r"$\boldsymbol{P}$ est constructible.", "Crop p59_P_alors.png.")
add(p, "proof of (9.2.6): 'pour Φ l'ensemble {—∞}'", "long dash minus", "-\\infty",
    "convention", 7, "high", r"$\{-\infty\}$ et", r"$\{\setmin\infty\}$ et", "")
add(p, "proof of (9.2.6): 'et l'ensemble {—∞, 0}'", "long dash minus", "-\\infty",
    "convention", 7, "high", r"$\{-\infty,0\}$", r"$\{\setmin\infty,0\}$", "")
add(p, "proof of (9.2.6): 'dans le cas (iii), la propriété P vérifie la conclusion'", "bold italic P", "\\mathbf P",
    "convention", 10, "high", r"propriété $\mathbf P$ vérifie", r"propriété $\boldsymbol{P}$ vérifie", "")
add(p, "Proposition (9.2.6.1): 'la fonction s⇝dim(f^{-1}(s))'", "wavy arrow ⇝", "\\mapsto",
    "symbol", None, "high", r"$s\mapsto\dim(f^{-1}(s))$", r"$s\leadsto\dim(f^{-1}(s))$", "GLOBAL_ISSUES 33. Crop p59_wavy1.png.")
add(p, "Corollaire (9.2.6.2): 'la fonction s⇝dim(X_s) soit constante'", "wavy arrow ⇝", "\\mapsto",
    "symbol", None, "high", r"$s\mapsto\dim(X_s)$", r"$s\leadsto\dim(X_s)$", "Crop p59_wavy2.png.")
add(p, "end of the page: '… un recouvrement fini (U_j) de X par des' / p. 60 'ouverts affines partout denses'",
    "the sentence runs on over the page break (p. 60 starts flush left)",
    "blank line before \\oldpage[IV-3]{60}: paragraph break mid-sentence",
    "marker", None, "high",
    r"par<NL>des<NL><NL>", r"par<NL>des<NL>", "Marker position itself is right.")

# ---------------------------------------------------------------- checks
ok = True
bypage = {}
for f in F:
    bypage.setdefault(f["page"], []).append(f)
for pg, items in sorted(bypage.items()):
    txt = open(rf"{BASE}\page_{pg:03d}.tex", encoding="utf-8").read().replace("\r\n", "\n")
    spans = []
    for f in items:
        if not f["fix"]:
            continue
        o = f["fix"]["old"]
        n = txt.count(o)
        if n != 1:
            ok = False
            print(f"p{pg}: old occurs {n} times: {o!r}")
            continue
        i = txt.index(o)
        spans.append((i, i + len(o), o))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            ok = False
            print(f"p{pg}: overlap {a[2]!r} / {b[2]!r}")
    # apply all fixes in order to be sure each still applies
    t2 = txt
    for f in items:
        if f["fix"]:
            assert t2.count(f["fix"]["old"]) == 1, (pg, f["fix"]["old"])
            t2 = t2.replace(f["fix"]["old"], f["fix"]["new"], 1)
    leftover = [s for s in (r"\mathcal C", r"\mathbf P", r"\mathbf Q", "(i bis)", r"\mapsto") if s in t2]
    print(f"p{pg}: {len(items)} findings; left after applying: {leftover}")

cnt = Counter()
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    cnt[(f["page"], k)] += 1
for pg in sorted(bypage):
    print(pg, cnt[(pg, "normal")], cnt[(pg, "convention")], cnt[(pg, "misprint")])
print("all checks ok" if ok else "PROBLEMS")
if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
    print("written", OUT, len(F))
