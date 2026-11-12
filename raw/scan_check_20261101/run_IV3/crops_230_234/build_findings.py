import json
import sys
import unicodedata

RUN = r"user\Documents\ega_scan_check_20261101\run_IV3"
OUT = RUN + r"\findings_230_234.json"
N = "\n"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


GI48 = "On the line (not in a subscript), so bold italic \\boldsymbol{k} (GLOBAL_ISSUES 48)."
WAVY = "Wavy maps-to arrow (GLOBAL_ISSUES 33), written \\leadsto as in the earlier page fixes; not convention 3."
SETMIN = "\\setmin pending the convention-7 decision (FIX_POLICY 2.7)."
SUBTR = "Subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision (FIX_POLICY 2.7)."

# ---------------------------------------------------------------- page 230
add(230, "page break 229/230, end of Proposition (15.4.1)",
    "p. 229 ends with the last line of the statement, 'équidimensionnel au point x.' (page_229_s4.png); p. 230 begins with the proof 'En effet ((11.1.1) et (12.1.1, (vi))), ...'",
    "\\oldpage[IV-3]{230} stands one line early, before 'équidimensionnel au point $x$.', and the proposition environment is not closed after the statement",
    "marker", None, "high",
    r"\oldpage[IV-3]{230}" + N + r"équidimensionnel au point $x$." + N + N + r"En effet",
    r"équidimensionnel au point $x$." + N + r"\end{proposition}" + N + N + r"\oldpage[IV-3]{230}" + N + r"En effet",
    "Moves the marker to the start of the proof and closes Proposition (15.4.1) after its statement, so that the proof is set roman as printed (next entry). Apply together with the next entry, which removes the old \\end{proposition} after the proof. No \\begin{proof}: the print has no heading (as the p. 44 fix of (8.12.2)).")

add(230, "proof of (15.4.1), 'En effet ((11.1.1) et (12.1.1, (vi))), ... que f est équidimensionnel au point x.'",
    "roman paragraph after the italic statement",
    "inside the proposition environment (\\end{proposition} only after the proof), so the whole proof is set italic",
    "italics", None, "high",
    r"que $f$ est équidimensionnel au point $x$." + N + r"\end{proposition}",
    r"que $f$ est équidimensionnel au point $x$.",
    "Apply together with the previous (marker) entry, which inserts \\end{proposition} before 'En effet'.")

add(230, "proof of (15.4.1), l. 4: 'associé à F_{f(x')} (0, 16.5.4)'",
    "(0, 16.5.4): bold 0 without subscript (enlarged crop p230_s1_0IV.png)",
    "($\\mathbf{0}_{\\mathrm{IV}}$, 16.5.4)",
    "extra", None, "high",
    r"($\mathbf{0}_{\mathrm{IV}}$, 16.5.4)",
    r"($\mathbf{0}$, 16.5.4)",
    "Same fix as (0, 17.3.7) on p. 210 and (0, 23.2.5) on p. 214.")

add(230, "proof of (15.4.1), l. 6: 'les dimensions des composantes irréductibles de Supp(F_{f(x')}|(U∩X_{f(x')}))'",
    "Supp(𝓕_{f(x')}|(U∩X_{f(x')})): the parenthesis of Supp closes after the restriction (enlarged crop p230_s1_supp.png)",
    "\\operatorname{Supp}(\\mathcal F_{f(x')})|(U\\cap X_{f(x')}): the parenthesis closes after F_{f(x')}",
    "formula", None, "high",
    r"$\operatorname{Supp}(\mathcal F_{f(x')})|(U\cap X_{f(x')})$",
    r"$\operatorname{Supp}(\mathcal F_{f(x')}|(U\cap X_{f(x')}))$",
    "The printed bracketing (support of the restriction) is sound; not a misprint.")

add(230, "Proposition (15.4.2), l. 4: 'Alors (avec les notations de (15.4.1)) les conditions suivantes'",
    "the parenthesis is roman inside the italic statement",
    "italic (inside the proposition environment)",
    "convention", 6, "high",
    r"(avec les notations de (15.4.1))",
    r"\textup{(avec les notations de (15.4.1))}",
    "This 'old' occurs once: in (15.4.3) the same words are broken after '(avec'.")

add(230, "Proposition (15.4.2), condition e'): 'dim(O_{X,x}⊗_{O_y} k(y))'",
    "bold italic k (enlarged crop p230_s2_eprime.png)",
    "\\mathbf{k}(y) (bold upright)",
    "convention", 1, "high",
    r"\otimes_{\mathcal O_y}\mathbf{k}(y))$",
    r"\otimes_{\mathcal O_y}\boldsymbol{k}(y))$",
    GI48)

add(230, "proof of (15.4.2): 'Comme Supp(F)=X, les conditions e) et e') sont équivalentes ... il résulte de (6.1.4) que e) entraîne a).'",
    "an indented roman paragraph after condition e')",
    "directly after \\end{enumerate}, inside the italic proposition environment: set italic and without indent",
    "italics", None, "high",
    r"\end{enumerate}" + N + r"Comme $\operatorname{Supp}(\mathcal F)=X$",
    r"\end{enumerate}" + N + r"\end{proposition}" + N + N + r"Comme $\operatorname{Supp}(\mathcal F)=X$",
    "Closes the statement before the proof. Apply together with the next entry, which removes the old \\end{proposition} after the proof. No \\begin{proof}: the print has no heading.")

add(230, "proof of (15.4.2), last line (line 23 of p. 230): 'il résulte de (6.1.4) que e) entraîne a)'",
    "(6.1.4)",
    "(6.1.4): the TeX keeps the printed reading",
    "misprint_in_print", None, "high",
    None, None,
    "Authors' errata (EGA IV part 4, Liste 3, entry (IV, 15.4.2), ega4-errata-addenda-list3-fr.tex line 243): 'Ligne 23 de la p. 230, remplacer (6.1.4) par (6.1.5).'",
    corrected=r"(6.1.5)")

add(230, "end of the proof of (15.4.2), before Proposition (15.4.3)",
    "the proof is not part of the statement",
    "\\end{proposition} after the proof",
    "other", None, "high",
    r"que $e)$ entraîne $a)$." + N + r"\end{proposition}",
    r"que $e)$ entraîne $a)$.",
    "Apply together with the previous structural entry ('\\end{enumerate}' + 'Comme'); on its own it leaves the proposition environment unclosed. Independent of the (6.1.4) misprint entry.")

add(230, "Proposition (15.4.3), l. 3: 'Alors (avec les notations de (15.4.1)) les conditions suivantes'",
    "the parenthesis is roman inside the italic statement",
    "italic (inside the proposition environment)",
    "convention", 6, "high",
    r"(avec" + N + r"les notations de (15.4.1))",
    r"\textup{(avec" + N + r"les notations de (15.4.1))}",
    "")

add(230, "proof of (15.4.3), l. 1: 'le k(y)-préschéma Y'_y = h^{-1}(y)'",
    "bold italic k (enlarged crop p230_s3_kpresch.png)",
    "\\mathbf{k}(y) (bold upright)",
    "convention", 1, "high",
    r"$\mathbf{k}(y)$-préschéma",
    r"$\boldsymbol{k}(y)$-préschéma",
    GI48)

add(230, "proof of (15.4.3), l. 2: 'Y'_y = h^{-1}(y) est régulier (0, 17.3.7)'",
    "'régulier' italic (enlarged crop p230_s3_regulier.png)",
    "roman",
    "italics", None, "high",
    r"$Y_y'=h^{-1}(y)$ est régulier",
    r"$Y_y'=h^{-1}(y)$ est \emph{régulier}",
    "Does not overlap the convention-1 entry before it or the (0, 17.3.7) entry after it.")

add(230, "proof of (15.4.3), l. 2: '(0, 17.3.7)'",
    "(0, 17.3.7): bold 0 without subscript (enlarged crop p230_s3_regulier.png)",
    "($\\mathbf{0}_{\\mathrm{IV}}$, 17.3.7)",
    "extra", None, "high",
    r"($\mathbf{0}_{\mathrm{IV}}$, 17.3.7)",
    r"($\mathbf{0}$, 17.3.7)",
    "Same fix as (0, 17.3.7) on p. 210.")

# ---------------------------------------------------------------- page 231
add(231, "heading 15.5: '... Application aux composantes connexes géométriques des fibres d'un morphisme propre.'",
    "final full stop", "no full stop",
    "punctuation", None, "high",
    r"d'un morphisme propre}",
    r"d'un morphisme propre.}",
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop).")

add(231, "Proposition (15.5.1), l. 3: '(ou rang séparable de f^{-1}(z) sur k(z); cf. I, 6.4.8)'",
    "roman parenthesis in the italic statement; only 'rang séparable' italic (enlarged crop p231_s2_rangsep.png)",
    "all italic (inside the proposition environment)",
    "convention", 6, "high",
    r"(ou rang séparable de $f^{-1}(z)$ sur",
    r"\textup{(ou} rang séparable \textup{de} $f^{-1}(z)$ \textup{sur}",
    "'rang séparable' stays italic, as printed. '; cf. I, 6.4.8)' is set upright by the punctuation entry below, k(z) by the convention-1 entry; the three 'old' strings do not overlap.")

add(231, "Proposition (15.5.1), l. 3: 'sur k(z)'",
    "bold italic k (enlarged crop p231_s2_rangsep.png)",
    "\\mathbf{k}(z) (bold upright)",
    "convention", 1, "high",
    r"$\mathbf{k}(z)$",
    r"$\boldsymbol{k}(z)$",
    GI48)

add(231, "Proposition (15.5.1), l. 3: 'sur k(z); cf. I, 6.4.8)'",
    "semicolon after k(z) (enlarged crop p231_s2_rangsep.png)",
    "comma: '$\\mathbf{k}(z)$, cf.'",
    "punctuation", None, "high",
    r", cf. \textbf{I}, 6.4.8)",
    r"\textup{; cf. \textbf{I}, 6.4.8)}",
    "The edit also sets '; cf. I, 6.4.8)' upright (roman in the print, convention 6).")

add(231, "Proposition (15.5.1) (i): 'La fonction z⇝n(z) est semi-continue inférieurement'",
    "wavy arrow (enlarged crop p231_s2_wavy.png)", "\\mapsto",
    "symbol", None, "high",
    r"fonction $z\mapsto n(z)$ est semi-continue",
    r"fonction $z\leadsto n(z)$ est semi-continue",
    WAVY)

add(231, "Proposition (15.5.1) (ii): 'si la fonction z⇝n(z) est constante dans un voisinage de y'",
    "wavy arrow", "\\mapsto",
    "symbol", None, "high",
    r"$z\mapsto n(z)$ est constante dans un",
    r"$z\leadsto n(z)$ est constante dans un",
    WAVY)

add(231, "Proposition (15.5.1) (ii), end: 'alors f est propre au point y (15.7.1).'",
    "reference roman in the italic statement (enlarged crop p231_s2_1571.png)",
    "italic",
    "convention", 6, "high",
    r"(15.7.1)",
    r"\textup{(15.7.1)}",
    "")

add(231, "Proposition (15.5.1) (iii): 'si la fonction z⇝n(z) est localement constante dans Y'",
    "wavy arrow", "\\mapsto",
    "symbol", None, "high",
    r"$z\mapsto n(z)$ est localement constante dans",
    r"$z\leadsto n(z)$ est localement constante dans",
    WAVY)

add(231, "proof of (15.5.1) (i), l. 2: 'on sait que la fonction z⇝n(z) est localement constructible (9.7.9)'",
    "wavy arrow", "\\mapsto",
    "symbol", None, "high",
    r"$z\mapsto n(z)$ est localement constructible",
    r"$z\leadsto n(z)$ est localement constructible",
    WAVY)

add(231, "Corollaire (15.5.2), l. 1: 'Sous les hypothèses générales de (15.5.1), soit y'",
    "reference roman in the italic statement (enlarged crop p231_s3_1551.png)",
    "italic",
    "convention", 6, "high",
    r"générales de (15.5.1), soit",
    r"générales de \textup{(15.5.1)}, soit",
    "")

add(231, "after (15.5.2.1), l. 3: 'et que z' soit générisation de z, on a'",
    "'soit générisation' without article (enlarged crop p231_s3_generisation.png)",
    "'soit une générisation'",
    "extra", None, "high",
    r"$z'$ soit une générisation",
    r"$z'$ soit générisation",
    "")

add(231, "after (15.5.2.1), l. 4: 'n(z')=n(y') (I, 6.4.12)'",
    "bold I", "plain I",
    "convention", 2, "high",
    r"(I, 6.4.12)",
    r"(\textbf{I}, 6.4.12)",
    "A genuine EGA I reference.")

add(231, "after (15.5.2.1), l. 5: 'il suffit donc de démontrer (15.5.2.1) pour un g convenable'",
    "'un' italic (enlarged crop p231_s3_ung.png)",
    "roman",
    "italics", None, "high",
    r"pour un $g$ convenable",
    r"pour \emph{un} $g$ convenable",
    "")

add(231, "Lemme (15.5.2.2), l. 1: 'Sous les hypothèses générales de (15.5.1), si y est un point de Y'",
    "reference roman in the italic statement",
    "italic",
    "convention", 6, "high",
    r"générales de (15.5.1), si",
    r"générales de \textup{(15.5.1)}, si",
    "")

add(231, "Lemme (15.5.2.2), ll. 3-4: 'tels que : 1° g(z)=y, g(z')=y'; 2° si l'on pose f'=f_(Z), ...'",
    "the two conditions 1°, 2° run on inside the statement paragraph",
    "set as an enumerate list (each condition on its own line, hanging labels)",
    "other", None, "medium",
    r"tels que~:" + N + r"\begin{enumerate}[label=\emph{\arabic*\textsuperscript{\textdegree}}]" + N
    + r"  \item $g(z)=y$, $g(z')=y'$~;" + N
    + r"  \item si l'on pose $f'=f_{(Z)}$, $n(y)$ est le nombre de points de $f'^{-1}(z)$ et $n(y')$ est le nombre de points de $f'^{-1}(z')$." + N
    + r"\end{enumerate}",
    r"tels que~: \textup{1\textsuperscript{\textdegree}} $g(z)=y$, $g(z')=y'$~; \textup{2\textsuperscript{\textdegree}} si l'on pose $f'=f_{(Z)}$, $n(y)$ est le nombre de points de $f'^{-1}(z)$ et $n(y')$ est le nombre de points de $f'^{-1}(z')$.",
    "Layout, like a formula displayed where the print has it inline (GLOBAL_ISSUES 21); no word changes. One atomic edit (removes \\begin and \\end{enumerate} together); labels kept as the TeX writes them, upright as printed.")

add(231, "last line of p. 231: 'dans Y tels que si z_1 et z'_1 sont le point fermé'",
    "no comma after 'tels que' (enlarged crop p231_s4_telsque.png)",
    "'tels que, si'",
    "punctuation", None, "high",
    r"tels que, si $z_1$",
    r"tels que si $z_1$",
    "")

# ---------------------------------------------------------------- page 232
add(232, "l. 1: 'on peut donc déjà supposer que Y est spectre d'un anneau de valuation discrète A'",
    "'est spectre' without article (enlarged crop p232_s1_spectre.png)",
    "'est le spectre'",
    "extra", None, "high",
    r"déjà supposer que $Y$ est le spectre",
    r"déjà supposer que $Y$ est spectre",
    "Same construction as 'f^{-1}(y) est réunion des ...' later on the page; not a misprint.")

add(232, "l. 3: 'Pour tout x∈f^{-1}(y), k(x) est une extension finie'",
    "bold italic k", "\\mathbf{k}(x)",
    "convention", 1, "high",
    r"$\mathbf{k}(x)$ est une extension",
    r"$\boldsymbol{k}(x)$ est une extension",
    GI48)

add(232, "l. 3: 'extension finie de k(y) par hypothèse (II, 6.2.2)'",
    "bold italic k", "\\mathbf{k}(y)",
    "convention", 1, "high",
    r"finie de $\mathbf{k}(y)$ par hypothèse",
    r"finie de $\boldsymbol{k}(y)$ par hypothèse",
    GI48)

add(232, "l. 4: 'il existe une extension algébrique finie k de k(y)'",
    "'finie' italic (enlarged crop p232_s1_finie_nombre.png)",
    "roman",
    "italics", None, "high",
    r"algébrique finie $k$",
    r"algébrique \emph{finie} $k$",
    "")

add(232, "l. 4: 'finie k de k(y) telle que'",
    "bold italic k", "\\mathbf{k}(y)",
    "convention", 1, "high",
    r"de $\mathbf{k}(y)$ telle que",
    r"de $\boldsymbol{k}(y)$ telle que",
    GI48 + " The subscript k of ⊗_{k(y)} is bold upright in the print, as in the TeX.")

add(232, "ll. 4-5: 'telle que le nombre de points de f^{-1}(y)⊗_{k(y)}k soit égal à n(y)'",
    "'nombre de points' italic (enlarged crop p232_s1_finie_nombre.png)",
    "roman",
    "italics", None, "high",
    r"le nombre de points de $f^{-1}(y)\otimes",
    r"le \emph{nombre de points} de $f^{-1}(y)\otimes",
    "The later 'le nombre de points de f^{-1}(y')⊗K' (l. 9) is roman in the print.")

add(232, "l. 6: 'le corps résiduel est fini sur k(y) et contient k'",
    "bold italic k", "\\mathbf{k}(y)",
    "convention", 1, "high",
    r"fini sur $\mathbf{k}(y)$ et contient",
    r"fini sur $\boldsymbol{k}(y)$ et contient",
    GI48)

add(232, "l. 8: 'il y a une extension finie K de k(y')'",
    "'finie' italic",
    "roman",
    "italics", None, "high",
    r"extension finie $K$",
    r"extension \emph{finie} $K$",
    "")

add(232, "l. 8: 'finie K de k(y') telle que'",
    "bold italic k", "\\mathbf{k}(y')",
    "convention", 1, "high",
    r"de $\mathbf{k}(y')$ telle que",
    r"de $\boldsymbol{k}(y')$ telle que",
    GI48)

add(232, "l. 9: 'si w est une valuation de k(y') associée à A'",
    "bold italic k", "\\mathbf{k}(y')",
    "convention", 1, "high",
    r"valuation de $\mathbf{k}(y')$ associée",
    r"valuation de $\boldsymbol{k}(y')$ associée",
    GI48)

add(232, "2nd paragraph, last line: 'on a k(x)=k(y)'",
    "bold italic k (twice)", "\\mathbf{k}(x)=\\mathbf{k}(y)",
    "convention", 1, "high",
    r"on a $\mathbf{k}(x)=\mathbf{k}(y)$",
    r"on a $\boldsymbol{k}(x)=\boldsymbol{k}(y)$",
    "Two occurrences in one edit. " + GI48)

add(232, "2nd paragraph, last line: '(resp. k(x')=k(y'))'",
    "bold italic k (twice)", "\\mathbf{k}(x')=\\mathbf{k}(y')",
    "convention", 1, "high",
    r"(resp. $\mathbf{k}(x')=\mathbf{k}(y')$)",
    r"(resp. $\boldsymbol{k}(x')=\boldsymbol{k}(y')$)",
    "Two occurrences in one edit. " + GI48)

add(232, "3rd paragraph, l. 3: 'la restriction X_i→Y de f à tout X_i est un morphisme dominant'",
    "'dominant' italic",
    "roman",
    "italics", None, "high",
    r"morphisme dominant, et comme",
    r"morphisme \emph{dominant}, et comme",
    "")

add(232, "3rd paragraph, l. 4: 'est réduite au point générique de X_i, d'où (en désignant ...'",
    "comma after X_i (enlarged crop p232_s2_douX.png)",
    "semicolon: '$X_i$~; d'où'",
    "punctuation", None, "high",
    r"point générique de $X_i$~; d'où",
    r"point générique de $X_i$, d'où",
    "")

add(232, "line after (15.5.2.3): 'et pour prouver (15.5.2.1), il suffit d'établir'",
    "no comma after 'et' (enlarged crop p232_s3_etpour.png)",
    "'et, pour prouver'",
    "punctuation", None, "high",
    r"et, pour prouver (15.5.2.1)",
    r"et pour prouver (15.5.2.1)",
    "")

add(232, "after (15.5.2.3), l. 2: 'on peut supposer X intègre'",
    "'intègre' italic (enlarged crop p232_s3_etpour.png)",
    "roman",
    "italics", None, "high",
    r"supposer $X$ intègre",
    r"supposer $X$ \emph{intègre}",
    "")

add(232, "after (15.5.2.3), l. 2: 'et le morphisme f birationnel'",
    "'birationnel' italic",
    "roman",
    "italics", None, "high",
    r"$f$ birationnel",
    r"$f$ \emph{birationnel}",
    "")

add(232, "after (15.5.2.3), l. 3: 'où K=k(y') est le corps des fractions'",
    "bold italic k", "\\mathbf{k}(y')",
    "convention", 1, "high",
    r"$K=\mathbf{k}(y')$",
    r"$K=\boldsymbol{k}(y')$",
    GI48)

add(232, "after (15.5.2.3), l. 6: 'une telle section est unique (I, 7.2.2)'",
    "'unique' italic",
    "roman",
    "italics", None, "high",
    r"section est unique",
    r"section est \emph{unique}",
    "")

add(232, "proof of (ii), l. 2: 'sont égaux pour toute générisation y' de y'",
    "'toute' italic",
    "roman",
    "italics", None, "high",
    r"pour toute générisation",
    r"pour \emph{toute} générisation",
    "")

add(232, "proof of (ii): '... et il s'agit alors de montrer que f est propre. | Utilisons (15.5.2.2) et notons que ...'",
    "'Utilisons' begins a new indented paragraph",
    "same paragraph",
    "other", None, "high",
    r"montrer que $f$ est propre. Utilisons",
    r"montrer que $f$ est propre." + N + N + r"Utilisons",
    "Missing paragraph break.")

# ---------------------------------------------------------------- page 233
add(233, "l. 2: 'les nombres de points des fibres f^{-1}(y) et f'^{-1}(y') respectivement'",
    "f'^{-1}(y') (primed f; enlarged crop p233_s1_fibres.png)",
    "$f'^{-1}(y')$: the TeX keeps the printed reading",
    "misprint_in_print", None, "medium",
    None, None,
    "After the base change the morphism is again called f: compare (i), p. 232, 'sont les nombres de points de f^{-1}(y) et f^{-1}(y')'; f' (= f_(Z) in (15.5.2.2)) has no fibre over y'. Not in the authors' errata (Liste 3).",
    corrected=r"f^{-1}(y')")

add(233, "display (15.5.2.4): 'n(y) ⩽ Σ_i n_i(y) ⩽ Σ_i n_i(y') = n(y')'",
    "no punctuation after the formula (enlarged crop p233_s1_eq.png)",
    "full stop after n(y')",
    "punctuation", None, "high",
    r"=n(y')." + N + r"\end{equation}",
    r"=n(y')" + N + r"\end{equation}",
    "")

add(233, "line after (15.5.2.4): 'et pour que les membres extrêmes soient égaux'",
    "no comma after 'et'",
    "'et, pour que'",
    "punctuation", None, "high",
    r"et, pour que les membres",
    r"et pour que les membres",
    "")

add(233, "proof of (iii), l. 2: 'et la fonction y⇝n(y) constante dans Y'",
    "wavy arrow", "\\mapsto",
    "symbol", None, "high",
    r"$y\mapsto n(y)$ constante",
    r"$y\leadsto n(y)$ constante",
    WAVY)

add(233, "proof of (iii), l. 7: 'il résulte du critère de Chevalley (14.4.4) que f_i est universellement ouvert'",
    "'universellement ouvert' italic",
    "roman",
    "italics", None, "high",
    r"que $f_i$ est universellement ouvert.",
    r"que $f_i$ est \emph{universellement ouvert}.",
    "")

add(233, "proof of (iii), line 16 of p. 233: 'd'autre part, comme les X_i∩f^{-1}(y) sont deux à deux disjoints, Σ_i n_i(y')=n(y')'",
    "X_i∩f^{-1}(y) (no prime; enlarged crop p233_s2_finv_y.png)",
    "$X_i\\cap f^{-1}(y)$: the TeX keeps the printed reading",
    "misprint_in_print", None, "high",
    None, None,
    "Authors' errata (EGA IV part 4, Liste 3, entry (IV, 15.5.2), ega4-errata-addenda-list3-fr.tex line 246): 'Ligne 16 de la p. 233, remplacer f^{-1}(y) par f^{-1}(y')'. The disjointness of the X_i∩f^{-1}(y) is the conclusion of the proof; here the generic fibre is meant.",
    corrected=r"X_i\cap f^{-1}(y')")

add(233, "proof of (iii), ll. 16-17: '... sont deux à deux disjoints, Σ_i n_i(y')=n(y'); on a donc encore'",
    "no 'on a' before the formula (enlarged crop p233_s2_disjoints.png)",
    "'disjoints, on a $\\sum_i n_i(y')=n(y')$'",
    "extra", None, "high",
    r"disjoints, on a $\sum_i n_i(y')=n(y')$",
    r"disjoints, $\sum_i n_i(y')=n(y')$",
    "Does not touch the misprint entry before it (fix null).")

add(233, "Proposition (15.5.3), l. 3: 'le nombre géométrique de composantes connexes (4.5.2) de f^{-1}(y)'",
    "reference roman in the italic statement (enlarged crop p233_s3_452.png)",
    "italic",
    "convention", 6, "high",
    r"connexes (4.5.2) de",
    r"connexes \textup{(4.5.2)} de",
    "")

add(233, "Proposition (15.5.3), l. 5: 'la fonction y⇝n(y) est semi-continue inférieurement au point y_0'",
    "wavy arrow", "\\mapsto",
    "symbol", None, "high",
    r"$y\mapsto n(y)$ est semi-continue",
    r"$y\leadsto n(y)$ est semi-continue",
    WAVY)

add(233, "proof of (15.5.3), l. 2: 'et f' : X→Y un morphisme surjectif dont les fibres'",
    "no verb before 'un morphisme surjectif' (enlarged crop p233_s3_stein.png)",
    "'et $f':X\\to Y$ est un morphisme surjectif'",
    "extra", None, "high",
    r"et $f':X\to Y$ est un morphisme surjectif",
    r"et $f':X\to Y$ un morphisme surjectif",
    "The formula itself is the misprint entry that follows; this edit leaves it unchanged.")

add(233, "proof of (15.5.3), l. 2: Stein factorization 'f=g∘f' ..., où g : Y'→Y est un morphisme fini et f' : X→Y'",
    "f' : X→Y (no prime on the target; enlarged crop p233_s3_XtoY.png)",
    "$f':X\\to Y$: the TeX keeps the printed reading",
    "misprint_in_print", None, "high",
    None, None,
    "f = g∘f' with g : Y'→Y forces f' : X→Y' (Stein factorization, III, 4.3.3). Not in the authors' errata (Liste 3).",
    corrected=r"f':X\to Y'")

add(233, "proof of (15.5.3), l. 9: 'on en conclut que g est universellement ouvert en tout point de g^{-1}(y_0)'",
    "'universellement ouvert en tout point de' italic",
    "roman",
    "italics", None, "high",
    r"$g$ est universellement ouvert en tout point de",
    r"$g$ est \emph{universellement ouvert en tout point de}",
    "")

# ---------------------------------------------------------------- page 234
add(234, "Corollaire (15.5.4), end (top of p. 234): 'alors, avec les notations de (15.5.3), la fonction'",
    "reference roman in the italic statement (enlarged crop p234_s1_1553.png)",
    "italic",
    "convention", 6, "high",
    r"notations de (15.5.3), la fonction",
    r"notations de \textup{(15.5.3)}, la fonction",
    "")

add(234, "Corollaire (15.5.4), end: 'la fonction z⇝n(z) est semi-continue inférieurement au point y'",
    "wavy arrow", "\\mapsto",
    "symbol", None, "high",
    r"$z\mapsto n(z)$ est semi-continue",
    r"$z\leadsto n(z)$ est semi-continue",
    WAVY)

add(234, "proof of (15.5.4), last line: 'il suffit alors d'appliquer à g la proposition (15.5.1, (i))'",
    "(15.5.1, (i)) (enlarged crop p234_s1_1551.png)",
    "(15.5.1), (i)",
    "punctuation", None, "high",
    r"(15.5.1), (i) en tenant",
    r"(15.5.1, (i)) en tenant",
    "")

add(234, "Remarques (15.5.5) (i), l. 2: 'la fonction y⇝n(y) n'est pas nécessairement localement constante'",
    "wavy arrow", "\\mapsto",
    "symbol", None, "high",
    r"$y\mapsto n(y)$ n'est pas nécessairement",
    r"$y\leadsto n(y)$ n'est pas nécessairement",
    WAVY)

add(234, "Remarques (15.5.5) (i), l. 4: 'A=k[S, T]/(S²+T²—1)'",
    "long dash for the minus (enlarged crop p234_s2_minus.png)",
    "minus sign",
    "convention", 7, "high",
    r"S^2+T^2-1",
    r"S^2+T^2\setmin 1",
    SUBTR)

add(234, "Remarques (15.5.5) (i), l. 4: 'idéaux maximaux (T—1) et (T+1)'",
    "long dash for the minus",
    "minus sign",
    "convention", 7, "high",
    r"$(T-1)$",
    r"$(T\setmin 1)$",
    SUBTR)

add(234, "Remarques (15.5.5) (i), last line: 'assurant que y⇝n(y) est localement constante (15.5.7)'",
    "wavy arrow", "\\mapsto",
    "symbol", None, "high",
    r"que $y\mapsto n(y)$ est localement constante",
    r"que $y\leadsto n(y)$ est localement constante",
    WAVY)

add(234, "Remarques (15.5.5) (iii), l. 2: 'que le morphisme f est ouvert (même si'",
    "'ouvert' italic in the roman remark",
    "no emphasis",
    "italics", None, "high",
    r"$f$ est ouvert (même",
    r"$f$ est \emph{ouvert} (même",
    "Inside the remarks environment (italic in the TeX); judged as a roman body, as the print sets remarks.")

add(234, "Remarques (15.5.5) (iv), l. 1: 'l'hypothèse que le morphisme f est séparé, comme le montre'",
    "'séparé' italic in the roman remark",
    "no emphasis",
    "italics", None, "high",
    r"$f$ est séparé, comme",
    r"$f$ est \emph{séparé}, comme",
    "Inside the remarks environment (italic in the TeX); judged as a roman body, as the print sets remarks.")

add(234, "Remarques (15.5.5) (iv), last line: 'mais z⇝n(z) n'est pas semi-continue inférieurement'",
    "wavy arrow", "\\mapsto",
    "symbol", None, "high",
    r"mais $z\mapsto n(z)$ n'est pas",
    r"mais $z\leadsto n(z)$ n'est pas",
    WAVY)

add(234, "Lemme (15.5.6.1), l. 3: 'alors T_x—{x} est connexe'",
    "long dash (set difference)", "minus sign",
    "convention", 7, "high",
    r"alors $T_x-\{x\}$ est connexe",
    r"alors $T_x\setmin\{x\}$ est connexe",
    SETMIN)

add(234, "Lemme (15.5.6.1), l. 4: 'si X est connexe, X—Z est connexe'",
    "long dash (set difference)", "minus sign",
    "convention", 7, "high",
    r"$X-Z$ est connexe.",
    r"$X\setmin Z$ est connexe.",
    SETMIN)

add(234, "proof of (15.5.6.1), l. 1: 'supposons que l'ouvert U=X—Z'",
    "long dash (set difference)", "minus sign",
    "convention", 7, "high",
    r"$U=X-Z$",
    r"$U=X\setmin Z$",
    SETMIN)

add(234, "proof of (15.5.6.1), l. 2: 'deux ouverts non vides sans point commun U', U'', et désignons'",
    "'U', U'',' (comma; enlarged crop p234_s3_UU.png)",
    "'$U'$ et $U''$,'",
    "word", None, "high",
    r"sans point commun $U'$ et $U''$, et",
    r"sans point commun $U'$, $U''$, et",
    "")

add(234, "proof of (15.5.6.1): 'Ceci prouve que les intersections de T_x—{x} avec U' et U''",
    "long dash (set difference)", "minus sign",
    "convention", 7, "high",
    r"intersections de $T_x-\{x\}$ avec",
    r"intersections de $T_x\setmin\{x\}$ avec",
    SETMIN)

add(234, "proof of (15.5.6.1): '(X'∩X'')∩(T_x—{x})=∅'",
    "long dash (set difference)", "minus sign",
    "convention", 7, "high",
    r"\cap(T_x-\{x\})=\varnothing",
    r"\cap(T_x\setmin\{x\})=\varnothing",
    SETMIN)

add(234, "proof of (15.5.6.1): 'avec T_x—{x} sont deux fermés non vides'",
    "long dash (set difference)", "minus sign",
    "convention", 7, "high",
    r"avec $T_x-\{x\}$ sont",
    r"avec $T_x\setmin\{x\}$ sont",
    SETMIN)

add(234, "proof of (15.5.6.1): 'disjoints dans T_x—{x}, dont la réunion'",
    "long dash (set difference)", "minus sign",
    "convention", 7, "high",
    r"dans $T_x-\{x\}$, dont",
    r"dans $T_x\setmin\{x\}$, dont",
    SETMIN)

add(234, "proof of (15.5.6.1): 'dont la réunion est T_x—{x}; or cela'",
    "long dash (set difference)", "minus sign",
    "convention", 7, "high",
    r"est $T_x-\{x\}$~; or",
    r"est $T_x\setmin\{x\}$~; or",
    SETMIN)

add(234, "proof of (15.5.6.1), last line: 'l'hypothèse que T_x—{x} est connexe. C.Q.F.D.'",
    "long dash (set difference)", "minus sign",
    "convention", 7, "high",
    r"que $T_x-\{x\}$ est connexe. C.Q.F.D.",
    r"que $T_x\setmin\{x\}$ est connexe. C.Q.F.D.",
    SETMIN)

# ---------------------------------------------------------------- checks
ok = True
texts = {}
for p in range(230, 235):
    # page files are CRLF; the release files use LF, so compare with LF line breaks
    with open(RUN + "\\page_%03d.tex" % p, encoding="utf-8") as fh:
        texts[p] = fh.read().replace("\r\n", "\n")
for d in F:
    for k in ("where", "scan", "tex", "note"):
        d[k] = unicodedata.normalize("NFC", d[k])
    if d["fix"]:
        for k in ("old", "new"):
            d["fix"][k] = unicodedata.normalize("NFC", d["fix"][k])
        c = texts[d["page"]].count(d["fix"]["old"])
        if c != 1:
            ok = False
            print("OLD COUNT", c, d["page"], repr(d["fix"]["old"]))
# overlap check: spans of olds on each page must be disjoint
for p in range(230, 235):
    spans = []
    for d in F:
        if d["page"] == p and d["fix"]:
            i = texts[p].find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["where"][:50]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print("OVERLAP", p, a, b)

counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0, 0])
    if d["kind"] == "convention":
        c[1] += 1
    elif d["kind"] == "misprint_in_print":
        c[2] += 1
    else:
        c[0] += 1
print(counts, "total", len(F))
if ok or "--force" in sys.argv:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("written", OUT)
else:
    print("NOT written")
