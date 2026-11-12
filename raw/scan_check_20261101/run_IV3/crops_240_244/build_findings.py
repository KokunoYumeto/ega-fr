"""Build findings_240_244.json for the EGA IV-3 scan check (pages 240-244) and verify every fix's 'old'
occurs exactly once in its LF-normalized page_NNN.tex. Read-only on the .tex files."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = "user/Documents/ega_scan_check_20261101/run_IV3/"
OUT = RUN + "findings_240_244.json"

K1 = ("The TeX has bold upright \\mathbf{k}; on the line the print's k is bold italic "
      "(subscript k stays \\mathbf{k}, GLOBAL_ISSUES 48).")
WAVY = "GLOBAL_ISSUES 33; not convention 3."
REF6 = "Reference printed upright inside the italic statement."
SUB7 = "Subtraction, not set difference (GLOBAL_ISSUES 23); \\setmin as for convention 7."
TERM = ("In the continuation of page_242.tex: ega4-15-terminal-fr.tex, text before its first page marker "
        "(\\oldpage[IV-3]{243}).")


def f(page, where, scan, tex, kind, fix, confidence="high", convention=None, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": convention,
         "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


def fx(old, new):
    return {"old": old, "new": new}


F = []
# ---------------------------------------------------------------- page 240
F += [
    f(240, "proof of (15.6.6), (ii), l. 1: 'comme X^0_y est la seule composante irréductible de f^{-1}(y)'",
      "'seule' italic (crop p240_seule.png)", "'seule' upright", "italics",
      fx(r"la seule composante", r"la \emph{seule} composante")),
    f(240, "proof of (15.6.6), (iii) case β), l. 5-6: 'montrent que dim(X^0_{y_0})≤dim(X^0_{y'}) | d'où dim(X^0_{y_0})=dim(X^0_{y'})'",
      "no comma after dim(X^0_{y'}) at the end of the line (crop p240_dou.png; nothing between ')' and the margin)",
      "', d'où' (comma): silent correction", "misprint_in_print",
      fx(r"\leqslant\dim(X_{y'}^0)$, d'où", r"\leqslant\dim(X_{y'}^0)$ d'où"), confidence="medium",
      corrected=r"\leqslant\dim(X_{y'}^0)$, d'où",
      note="The reading is certain; classed as a dropped comma (EGA sets a comma before 'd'où'). If the coordinator "
           "prefers to treat it as authorial punctuation, apply the same edit to both editions."),
    f(240, "proof of (15.6.6), (iv), l. 8: 'on peut de plus supposer Y noethérien; il résulte alors'",
      "'noethérien' italic (crop p240_noeth.png)", "'noethérien' upright", "italics",
      fx(r"plus supposer $Y$ noethérien", r"plus supposer $Y$ \emph{noethérien}")),
    f(240, "Corollaire (15.6.7), l. 1: 'les conditions préliminaires de (15.6.6) sur f'",
      "'(15.6.6)' upright (crop p240_cor.png)", "italic (corollary environment)", "convention",
      fx(r"préliminaires de (15.6.6) sur", r"préliminaires de \textup{(15.6.6)} sur"), convention=6, note=REF6),
    f(240, "Corollaire (15.6.7), l. 2: 'soit géométriquement intègre sur k(y)'",
      "bold italic k (crop p240_cor.png)", "\\mathbf{k}(y)", "convention",
      fx(r"intègre sur $\mathbf{k}(y)$", r"intègre sur $\boldsymbol{k}(y)$"), convention=1, note=K1),
    f(240, "Corollaire (15.6.7), a): 'La fonction y⇝dim(X^0_y) est localement constante'",
      "wavy arrow (crop p240_wavy.png)", "\\mapsto", "symbol",
      fx(r"La fonction $y\mapsto", r"La fonction $y\leadsto"), note=WAVY),
]
# ---------------------------------------------------------------- page 241
F += [
    f(241, "proof of (15.6.7), l. 1: 'Le fait que a) entraîne b) résulte de (15.6.6, (ii))'",
      "'a)' and 'b)' italic, parenthesis included (crop p241_ab_proof.png)", "upright a), b)", "italics",
      fx(r"Le fait que a) entraîne b) résulte", r"Le fait que \emph{a)} entraîne \emph{b)} résulte")),
    f(241, "proof of (15.6.7), l. 2: 'Si b) est vérifiée'",
      "'b)' italic (crop p241_ab_proof.png)", "upright b)", "italics",
      fx(r"Si b) est vérifiée", r"Si \emph{b)} est vérifiée")),
    f(241, "proof of (15.6.7), l. 4-5: 'L'équivalence de b) et b') a déja été prouvée'",
      "'b)' and 'b')' italic (crop p241_deja.png)", "upright b), b$'$)", "italics",
      fx(r"L'équivalence de b) et b$'$)", r"L'équivalence de \emph{b)} et \emph{b$'$)}"),
      note="Listed before the misprint entry of the same sentence; the two edits do not overlap."),
    f(241, "proof of (15.6.7), l. 5: 'a déja été prouvée lorsque Y est localement noethérien'",
      "'déja' without the grave accent on the final a (crop p241_deja_zoom.png)",
      "'déjà': silent correction", "misprint_in_print",
      fx(r"a déjà été prouvée", r"a déja été prouvée"), corrected=r"a déjà été prouvée",
      note="Elsewhere the print has 'déjà' (p. 240 l. 9; proof of (15.6.9) on this page)."),
    f(241, "Proposition (15.6.8), l. 3: 'soit propre sur k(y), X^0 est propre sur Y au point y'",
      "bold italic k", "\\mathbf{k}(y)", "convention",
      fx(r"soit propre sur $\mathbf{k}(y)$, $X^0$", r"soit propre sur $\boldsymbol{k}(y)$, $X^0$"),
      convention=1, note=K1),
    f(241, "Proposition (15.6.8), l. 4-5: '(i.e. (15.7.1), il existe un voisinage ouvert U de y dans Y tel que X^0∩f^{-1}(U) soit fermé dans f^{-1}(U) et propre sur U)'",
      "the whole parenthesis roman inside the italic statement (crop p241_ie.png)",
      "italic (proposition environment)", "convention",
      fx(r"(i.e. (15.7.1), il existe un voisinage ouvert $U$ de $y$ dans $Y$ tel que $X^0\cap f^{-1}(U)$ soit fermé dans $f^{-1}(U)$ et propre sur $U$)",
         r"\textup{(i.e. (15.7.1), il existe un voisinage ouvert $U$ de $y$ dans $Y$ tel que $X^0\cap f^{-1}(U)$ soit fermé dans $f^{-1}(U)$ et propre sur $U$)}"),
      convention=6),
    f(241, "proof of (15.6.8), l. 1: '(où on utilise (8.10.5, (v), et où on remplace (9.7.11) par (9.6.7))'",
      "'(8.10.5, (v),': one closing parenthesis after (v), so '(8.10.5' is never closed (crop p241_810v.png)",
      "'(8.10.5, (v)),': silent correction", "misprint_in_print",
      fx(r"(8.10.5, (v)),", r"(8.10.5, (v),"), corrected=r"(8.10.5, (v)),",
      note="The diplomatic text takes the printed (unbalanced) reading."),
    f(241, "Corollaire (15.6.9), l. 2: 'et f localement de type fini, ou que f soit de présentation finie'",
      "'ou' roman inside the italic statement (crop p241_ou.png)", "italic (corollary environment)", "convention",
      fx(r"fini, ou que $f$", r"fini, \textup{ou} que $f$"), convention=6,
      note="As in (15.6.6) on p. 239."),
    f(241, "Corollaire (15.6.9), l. 4: 'Soit y un point de Y tel que X^0_y soit propre sur k(y). Alors'",
      "bold italic k", "\\mathbf{k}(y)", "convention",
      fx(r"soit propre sur $\mathbf{k}(y)$. Alors", r"soit propre sur $\boldsymbol{k}(y)$. Alors"),
      convention=1, note=K1),
    f(241, "proof of (15.6.9), l. 4: 'l'hypothèse que X^0_y soit propre sur k(y) entraîne'",
      "bold italic k", "\\mathbf{k}(y)", "convention",
      fx(r"soit propre sur $\mathbf{k}(y)$ entraîne", r"soit propre sur $\boldsymbol{k}(y)$ entraîne"),
      convention=1, note=K1),
    f(241, "Remarques (15.6.10) (i), l. 6: 'l'idéal principal (πt—1) est maximal'",
      "long dash for the minus sign (crop p241_pit.png)", "\\pi t-1", "convention",
      fx(r"$(\pi t-1)$", r"$(\pi t\setmin 1)$"), convention=7, note=SUB7),
    f(241, "Remarques (15.6.10) (i), last line: 'et correspond donc à un point fermé x_1 de X_1'",
      "'fermé' italic (crop p241_ferme.png)", "'fermé' without \\emph", "italics",
      fx(r"un point fermé $x_1$", r"un point \emph{fermé} $x_1$"),
      note="Remark body judged as roman (document-wide remark-font item); \\emph{maximal} just before is already there."),
    f(241, "Remarques (15.6.10) (i), last line: 'qui se projette au point générique y' de Y'",
      "'point générique' italic (crop p241_ferme.png)", "no \\emph", "italics",
      fx(r"se projette au point générique $y'$", r"se projette au \emph{point générique} $y'$"),
      note="Remark body judged as roman."),
    f(241, "Remarques (15.6.10) (i), last line: 'est tel que k(x_1)=K'",
      "bold italic k (crop p241_ferme.png)", "\\mathbf{k}(x_1)", "convention",
      fx(r"tel que $\mathbf{k}(x_1)", r"tel que $\boldsymbol{k}(x_1)"), convention=1, note=K1),
    f(241, "last line of p. 241 / first line of p. 242: '... est tel que k(x_1)=K. | Considérons d'autre part le point fermé x_2'",
      "p. 242 begins flush left (no indent, crops p242_top.png, p242_margin.png): remark (i) runs on as one paragraph until 'Voir cependant la prop. (15.6.9).'",
      "blank line before \\oldpage[IV-3]{242} (paragraph break)", "marker",
      fx("=K$.\n\n", "=K$.\n"),
      note="Marker position itself is right (GLOBAL_ISSUES 20); no blank line after the marker (ega4-15-fr.tex, blank line 923, marker line 924). Disjoint from the k(x_1) edit."),
]
# ---------------------------------------------------------------- page 242
F += [
    f(242, "Remarques (15.6.10) (i), l. 1: 'l'idéal maximal (u—1/π)+(v)'",
      "long dash for the minus sign (crop p242_u_pi.png)", "u-\\frac{1}{\\pi}", "convention",
      fx(r"\left(u-\frac{1}{\pi}\right)", r"\left(u\setmin\frac{1}{\pi}\right)"), convention=7, note=SUB7),
    f(242, "Remarques (15.6.10) (i), l. 2: 'on a aussi k(x_2)=K'",
      "bold italic k (crop p242_top.png)", "\\mathbf{k}(x_2)", "convention",
      fx(r"on a aussi $\mathbf{k}(x_2)=K$", r"on a aussi $\boldsymbol{k}(x_2)=K$"), convention=1, note=K1),
    f(242, "Remarques (15.6.10) (ii), last line: 'on ne peut se dispenser de l'hypothèse que X^y est réduit'",
      "'X^y': X with a raised small italic y as exponent, no 0 and no subscript (crop p242_Xy.png)",
      "X_{y_0}^0: silent correction", "misprint_in_print",
      fx(r"l'hypothèse que $X_{y_0}^0$ est réduit", r"l'hypothèse que $X^y$ est réduit"),
      corrected=r"l'hypothèse que $X_{y_0}^0$ est réduit",
      note="The hypothesis of (15.6.4) at the point y_0, as the same sentence's 'voisinage de X^0_{y_0}' shows."),
    f(242, "Remarques (15.6.10) (iii), l. 1: 'aux Y-préschémas en groupes localement de type fini'",
      "'préschémas en groupes' italic, both words (crop p242_groupes.png)", "only 'en groupes' in \\emph", "italics",
      fx(r"$Y$-préschémas \emph{en groupes}", r"$Y$-\emph{préschémas en groupes}"),
      note="Remark body judged as roman."),
    f(242, "Remarques (15.6.10) (iii), l. 3: 'et l'on montre que G_y est toujours géométriquement irréductible'",
      "'G_y': no superscript 0 (crop p242_Gy.png; the 0 of dim(G^0_y) on the same line is clear)",
      "G_y^0: silent correction", "misprint_in_print",
      fx(r"l'on montre que $G_y^0$ est toujours", r"l'on montre que $G_y$ est toujours"),
      corrected=r"l'on montre que $G_y^0$ est toujours",
      note="G_y itself need not be irreducible; the claim is for the component G^0_y (cf. dim(G^0_y)=dim(G_y) next)."),
    f(242, "Remarques (15.6.10) (iii), l. 4: 'la fonction z⇝dim(G_z) est semi-continue supérieurement'",
      "wavy arrow (crop p242_wavy1.png)", "\\mapsto", "symbol",
      fx(r"$z\mapsto\dim(G_z)$ est semi-continue", r"$z\leadsto\dim(G_z)$ est semi-continue"), note=WAVY),
    f(242, "Remarques (15.6.10) (iii), l. 6: 'G_y est géométriquement réduit sur k(y) en un de ses points'",
      "bold italic k (crop p242_tous.png)", "\\mathbf{k}(y)", "convention",
      fx(r"réduit sur $\mathbf{k}(y)$ en un de ses points", r"réduit sur $\boldsymbol{k}(y)$ en un de ses points"),
      convention=1, note=K1),
    f(242, "Remarques (15.6.10) (iii), l. 6: 'G_y est lisse (6.8.1) sur k(y)'",
      "bold italic k (crop p242_tous.png)", "\\mathbf{k}(y)", "convention",
      fx(r"(6.8.1) sur $\mathbf{k}(y)$", r"(6.8.1) sur $\boldsymbol{k}(y)$"), convention=1, note=K1),
    f(242, "Remarques (15.6.10) (iii), l. 7: 'en tous ses points'",
      "'tous' italic (crop p242_tous.png)", "no \\emph", "italics",
      fx(r"en tous ses points", r"en \emph{tous} ses points"), note="Remark body judged as roman."),
    f(242, "Remarques (15.6.10) (iii), l. 7: 'alors f est lisse en tous les points de G^0_y'",
      "'lisse' italic (crop p242_tous.png)", "no \\emph", "italics",
      fx(r"alors $f$ est lisse en tous", r"alors $f$ est \emph{lisse} en tous"), note="Remark body judged as roman."),
    f(242, "Remarques (15.6.10) (iii), l. 10: 'la fonction z⇝dim(G_z) est localement constante'",
      "wavy arrow (crop p242_wavy2.png)", "\\mapsto", "symbol",
      fx(r"$z\mapsto\dim(G_z)$ est localement constante", r"$z\leadsto\dim(G_z)$ est localement constante"),
      note=WAVY),
    f(242, "heading 15.7: 'Appendice : Critères valuatifs de propreté locale.'",
      "final full stop", "no full stop", "punctuation",
      fx(r"propreté locale}", r"propreté locale.}"),
      note="GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop). " + TERM),
    f(242, "Définition (15.7.1), l. 2: 'On dit que f est propre au point y s'il existe'",
      "the defined term 'propre au point' roman inside the italic statement (crop p242_def.png); the second term 'propre sur Y au point y' is italic",
      "italic (definition environment)", "convention",
      fx(r"$f$ est propre au point $y$ s'il", r"$f$ est \textup{propre au point} $y$ s'il"), convention=6,
      note=TERM),
    f(242, "Définition (15.7.1), l. 5: 'et propre sur U (II, 5.4.10)'",
      "'(II, 5.4.10)' upright (crop p242_def2.png)", "italic (definition environment)", "convention",
      fx(r"(\textbf{II}, 5.4.10)", r"\textup{(\textbf{II}, 5.4.10)}"), convention=6, note=REF6 + " " + TERM),
    f(242, "Définition (15.7.1), l. 5-6: '(ce qui revient à dire que ... la restriction Z→Y de f à Z est propre au point y)'",
      "the parenthesis roman, only 'propre au point y' italic (crop p242_def2.png)",
      "all italic (definition environment)", "convention",
      fx(r"(ce qui revient à dire que pour tout sous-préschéma fermé de $X$ ayant $Z$ pour espace sous-jacent, la restriction $Z\to Y$ de $f$ à $Z$ est propre au point $y$)",
         r"\textup{(ce qui revient à dire que pour tout sous-préschéma fermé de $X$ ayant $Z$ pour espace sous-jacent, la restriction $Z\to Y$ de $f$ à $Z$ est \emph{propre au point $y$})}"),
      convention=6, note="Roman words in the italic statement; 'propre au point y' emphasized by italics inside them (\\emph inside \\textup). " + TERM),
    f(242, "Proposition (15.7.2) c), l. 2: '(auquel cas on a nécessairement f(x)=y)'",
      "the whole parenthesis roman inside the italic statement (crop p242_auquel.png)",
      "italic (proposition environment)", "convention",
      fx(r"(auquel cas on a nécessairement $f(x)=y$)", r"\textup{(auquel cas on a nécessairement $f(x)=y$)}"),
      convention=6, note=TERM),
    f(242, "Proposition (15.7.2) c), l. 1: 'et dominant O domine un anneau local O_x de X'",
      "bare script O at the end of the line, no subscript (crop p242_domO.png)",
      "\\mathcal O (keeps the printed reading)", "misprint_in_print", None,
      corrected=r"dominant $\mathcal O_y$ domine",
      note="The TeX keeps the printed reading. The local ring O_y is meant (b): Y_1=Spec(O_y); proof of (15.7.4): "
           "'dominant O_y'). " + TERM),
]
# ---------------------------------------------------------------- page 243
F += [
    f(243, "proof of (15.7.2), l. 1: 'Le fait que a) implique b) résulte de (II, 5.4.2)'",
      "'a)' and 'b)' italic (crop p243_labels.png)", "upright a), b)", "italics",
      fx(r"Le fait que a) implique b) résulte", r"Le fait que \emph{a)} implique \emph{b)} résulte")),
    f(243, "proof of (15.7.2), l. 1: 'et l'implication b)⇒c) résulte de (II, 7.3.10)'",
      "'b)' and 'c)' italic, the arrow upright (crop p243_labels.png)", "upright b), c)", "italics",
      fx(r"l'implication b) $\Rightarrow$ c) résulte", r"l'implication \emph{b)} $\Rightarrow$ \emph{c)} résulte")),
    f(243, "proof of (15.7.2), l. 2: 'Reste donc à montrer que c) entraîne a).'",
      "'c)' and 'a)' italic (crop p243_labels.png)", "upright c), a)", "italics",
      fx(r"montrer que c) entraîne a).", r"montrer que \emph{c)} entraîne \emph{a)}.")),
    f(243, "proof of (15.7.2), diagram, bottom arrow 'Y ←— X'",
      "the bottom arrow has no label (crops p243_diag_bottom.png, p243_diag_top.png; j, p, g are printed)",
      "label f (X\\ar[l]^-{f})", "extra",
      fx(r"X\ar[l]^-{f}", r"X\ar[l]"),
      note="The other labels match the print (j above, p left, g right)."),
    f(243, "proof of (15.7.2), l. after the diagram: 'et l'on peut, en remplaçant p par p_red, supposer P intègre (I, 5.2.2 et II, 5.5.5, (vi))'",
      "italic lower-case p and p_red (crop p243_pred.png)", "$P$ par $P_{\\mathrm{red}}$", "formula",
      fx(r"en remplaçant $P$ par $P_{\mathrm{red}}$", r"en remplaçant $p$ par $p_{\mathrm{red}}$"),
      note="Not a misprint: p_red : P_red → Y is the morphism of the cited (II, 5.5.5, (vi)) (f projective implies "
           "f_red projective)."),
    f(243, "proof of (15.7.2): 'car alors la restriction de j à j^{-1}(p^{-1}(U))=g^{-1}(f^{-1}(U))=V sera un isomorphisme'",
      "the formula is set in the running text", "displayed with \\[ ... \\]", "other",
      fx("\\[\nj^{-1}\\bigl(p^{-1}(U)\\bigr)=g^{-1}\\bigl(f^{-1}(U)\\bigr)=V\n\\]",
         "$j^{-1}(p^{-1}(U))=g^{-1}(f^{-1}(U))=V$"),
      note="Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting word lost; ordinary "
           "parentheses as printed."),
    f(243, "proof of (15.7.2): 'est surjective, la restriction f^{-1}(U)→U sera propre (II, 5.4.3)'",
      "no 'de f' after f^{-1}(U)→U (crop p243_restr.png)", "'... \\to U$ de $f$ sera propre'", "extra",
      fx(r"\to U$ de $f$ sera propre", r"\to U$ sera propre"), note="Words added by the TeX."),
    f(243, "proof of (15.7.2): 'Comme T=P—j(X') est fermé dans P'",
      "long dash for the set difference (crop p243_restr.png)", "P-j(X')", "convention",
      fx(r"$T=P-j(X')$", r"$T=P\setmin j(X')$"), convention=7, note="\\setmin is defined in the IV-3 preamble."),
    f(243, "proof of (15.7.2), 3rd line from the end: 'dont les anneaux locaux O_z et O_{j(x')}=O_{x'} sont apparentés'",
      "'O_z' without prime (crop p243_Oz.png)", "\\mathcal O_z (keeps the printed reading)", "misprint_in_print",
      None, corrected=r"$\mathcal O_{z'}$",
      note="The TeX keeps the printed reading. The point is z' (z'∈P, p(z')=y, A dominant O_{z'}; 'z' et j(x')' in the same sentence)."),
    f(243, "Remarque (15.7.3), l. 2: 'en remplaçant dans la condition c) les anneaux de valuation discrète'",
      "'c)' italic (crop p243_rem_c.png)", "upright c)", "italics",
      fx(r"la condition c) les anneaux", r"la condition \emph{c)} les anneaux"),
      note="Remark body judged as roman."),
    f(243, "Corollaire (15.7.4), l. 3: '(ce qui est le cas lorsque Z est fini, ou lorsque Z est constructible (0_III, 9.2.2))'",
      "the parenthesis roman, only 'fini' and 'constructible' italic (crop p243_cequi.png)",
      "all italic (corollary environment)", "convention",
      fx(r"(ce qui est le cas lorsque $Z$ est fini, ou lorsque $Z$ est constructible ($\mathbf{0}_{\mathrm{III}}$, 9.2.2))",
         r"\textup{(ce qui est le cas lorsque $Z$ est \emph{fini}, ou lorsque $Z$ est \emph{constructible} ($\mathbf{0}_{\mathrm{III}}$, 9.2.2))}"),
      convention=6, note="Roman words in the italic statement; 'fini' and 'constructible' emphasized by italics inside them."),
]
# ---------------------------------------------------------------- page 244
F += [
    f(244, "Corollaire (15.7.4) c), end (l. 1 of p. 244): 'pour tout point x'∈Z'∩f'^{-1}(η') rationnel sur k(η')'",
      "bold italic k", "\\mathbf k(\\eta')", "convention",
      fx(r"(\eta')$ rationnel sur $\mathbf k(\eta')$", r"(\eta')$ rationnel sur $\boldsymbol{k}(\eta')$"),
      convention=1, note=K1),
    f(244, "proof of (15.7.4), l. 1: 'Le fait que a) entraîne b) résulte de ce que'",
      "'a)' and 'b)' italic (crop p244_labels1.png)", "upright a), b)", "italics",
      fx(r"Le fait que a) entraîne b) résulte", r"Le fait que \emph{a)} entraîne \emph{b)} résulte")),
    f(244, "proof of (15.7.4), l. 2: 'Le fait que b) entraîne c) résulte de (II, 7.3.3)'",
      "'b)' and 'c)' italic (crop p244_labels1.png)", "upright b), c)", "italics",
      fx(r"Le fait que b) entraîne c) résulte", r"Le fait que \emph{b)} entraîne \emph{c)} résulte")),
    f(244, "proof of (15.7.4), l. 3: 'Reste donc à voir que c) implique a).'",
      "'c)' and 'a)' italic (crop p244_labels1.png)", "upright c), a)", "italics",
      fx(r"voir que c) implique a).", r"voir que \emph{c)} implique \emph{a)}.")),
    f(244, "proof of (15.7.4), l. 10: 'Montrons pour cela que f vérifie la condition c) de (15.7.2)'",
      "'c)' italic", "upright c)", "italics",
      fx(r"la condition c) de (15.7.2)", r"la condition \emph{c)} de (15.7.2)")),
    f(244, "proof of (15.7.4), l. 11: 'ayant R(X)=k(z) pour corps des fractions'",
      "bold italic k (crop p244_ks.png)", "\\mathbf k(z)", "convention",
      fx(r"$R(X)=\mathbf k(z)$", r"$R(X)=\boldsymbol{k}(z)$"), convention=1, note=K1),
    f(244, "proof of (15.7.4), l. 12: 'avec les notations de c), on a donc g(y')=y'",
      "'c)' italic (crop p244_ks.png)", "upright c)", "italics",
      fx(r"avec les notations de c), on a", r"avec les notations de \emph{c)}, on a")),
    f(244, "proof of (15.7.4), l. 13: 'Comme par définition k(η')=k(z)', first k",
      "bold italic k (crop p244_ks.png)", "\\mathbf k(\\eta')", "convention",
      fx(r"par définition $\mathbf k(\eta')", r"par définition $\boldsymbol{k}(\eta')"), convention=1, note=K1),
    f(244, "proof of (15.7.4), l. 13: 'Comme par définition k(η')=k(z)', second k",
      "bold italic k (crop p244_ks.png)", "\\mathbf k(z)", "convention",
      fx(r"=\mathbf k(z)$, il existe", r"=\boldsymbol{k}(z)$, il existe"), convention=1,
      note=K1 + " Disjoint from the previous entry."),
    f(244, "proof of (15.7.4), l. 13: 'il existe un k(η)-morphisme'",
      "bold italic k (crop p244_ks.png)", "\\mathbf k(\\eta)", "convention",
      fx(r"un $\mathbf k(\eta)$-morphisme", r"un $\boldsymbol{k}(\eta)$-morphisme"), convention=1, note=K1),
    f(244, "proof of (15.7.4), l. 14: 'Spec(k(η')) → Spec(k(z))', first k",
      "bold italic k (crop p244_ks.png)", "\\mathbf k(\\eta')", "convention",
      fx(r"\operatorname{Spec}(\mathbf k(\eta'))", r"\operatorname{Spec}(\boldsymbol{k}(\eta'))"), convention=1, note=K1),
    f(244, "proof of (15.7.4), l. 14: 'Spec(k(η')) → Spec(k(z))', second k",
      "bold italic k (crop p244_ks.png)", "\\mathbf k(z)", "convention",
      fx(r"\operatorname{Spec}(\mathbf k(z))", r"\operatorname{Spec}(\boldsymbol{k}(z))"), convention=1, note=K1),
    f(244, "proof of (15.7.4), l. 14: 'donc une k(η')-section de f'^{-1}(η')'",
      "bold italic k (crop p244_ks.png)", "\\mathbf k(\\eta')", "convention",
      fx(r"une $\mathbf k(\eta')$-section", r"une $\boldsymbol{k}(\eta')$-section"), convention=1, note=K1),
    f(244, "proof of (15.7.4), l. 15: 'z' est donc rationnel sur k(η')'",
      "bold italic k (crop p244_ks.png)", "\\mathbf k(\\eta')", "convention",
      fx(r"donc rationnel sur $\mathbf k(\eta')$", r"donc rationnel sur $\boldsymbol{k}(\eta')$"), convention=1, note=K1),
    f(244, "proof of (15.7.4), l. 16: 'On conclut donc de l'hypothèse c) qu'il existe'",
      "'c)' italic", "upright c)", "italics",
      fx(r"l'hypothèse c) qu'il existe", r"l'hypothèse \emph{c)} qu'il existe")),
    f(244, "Corollaire (15.7.5) c), l. 4: 'pour tout x'∈f'^{-1}(η'), rationnel sur k(η')'",
      "bold italic k", "\\mathbf k(\\eta')", "convention",
      fx(r"(\eta')$, rationnel sur $\mathbf k(\eta')$", r"(\eta')$, rationnel sur $\boldsymbol{k}(\eta')$"),
      convention=1, note=K1),
    f(244, "Corollaire (15.7.6) b), l. 2: 'image fermée de X par f (I, 9.5.3 et 9.5.1)'",
      "'(I, 9.5.3 et 9.5.1)' upright, 'et' included (crop p244_I953.png)", "italic (corollary environment)",
      "convention", fx(r"(\textbf{I}, 9.5.3 et 9.5.1)", r"\textup{(\textbf{I}, 9.5.3 et 9.5.1)}"),
      convention=6, note=REF6),
    f(244, "Corollaire (15.7.6) d), l. 2: 'toute Y'-section rationnelle (I, 7.1.2)'",
      "'(I, 7.1.2)' upright (crop p244_I712.png)", "italic (corollary environment)", "convention",
      fx(r"(\textbf{I}, 7.1.2)", r"\textup{(\textbf{I}, 7.1.2)}"), convention=6, note=REF6),
    f(244, "proof of (15.7.6), l. 1: 'Il est clair que b) entraîne a).'",
      "'b)' and 'a)' italic", "upright b), a)", "italics",
      fx(r"Il est clair que b) entraîne a).", r"Il est clair que \emph{b)} entraîne \emph{a)}.")),
    f(244, "proof of (15.7.6), l. 1: 'Pour voir que a) entraîne c), remarquons'",
      "'a)' and 'c)' italic", "upright a), c)", "italics",
      fx(r"Pour voir que a) entraîne c), remarquons", r"Pour voir que \emph{a)} entraîne \emph{c)}, remarquons")),
    f(244, "proof of (15.7.6), l. 2: 'remarquons d'abord que a) entraîne que h(Z)'",
      "'a)' italic", "upright a)", "italics",
      fx(r"d'abord que a) entraîne que", r"d'abord que \emph{a)} entraîne que")),
]

# ---------------------------------------------------------------- checks
texts = {}
for n in range(240, 245):
    texts[n] = open(RUN + f"page_{n:03d}.tex", encoding="utf-8", newline="").read().replace("\r\n", "\n")
bad = 0
for d in F:
    fix = d["fix"]
    if fix is None:
        continue
    c = texts[d["page"]].count(fix["old"])
    if c != 1:
        bad += 1
        print("NOT UNIQUE", d["page"], c, repr(fix["old"]))
# fixes on the same page must not overlap
for n in range(240, 245):
    spans = []
    for d in F:
        if d["page"] == n and d["fix"]:
            i = texts[n].find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["fix"]["old"][:40]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            bad += 1
            print("OVERLAP", n, a, b)
# simulate applying all fixes in order: each old must still be found once after the earlier edits
for n in range(240, 245):
    t = texts[n]
    for d in F:
        if d["page"] == n and d["fix"]:
            if t.count(d["fix"]["old"]) != 1:
                bad += 1
                print("SEQUENTIAL FAIL", n, repr(d["fix"]["old"]))
            t = t.replace(d["fix"]["old"], d["fix"]["new"], 1)
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0, 0])
    if d["kind"] == "misprint_in_print":
        c[2] += 1
    elif d["kind"] == "convention":
        c[1] += 1
    else:
        c[0] += 1
print("problems:", bad)
print("counts (normal/convention/misprint):", counts, "total", len(F))
if not bad:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("written", OUT)
