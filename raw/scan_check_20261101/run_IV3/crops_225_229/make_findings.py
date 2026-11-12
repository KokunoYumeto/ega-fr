# Builds findings_225_229.json for the EGA IV-3 scan check of pp. 225-229
# and checks that every fix's "old" occurs exactly once in its page file.
import json, os, sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, "findings_225_229.json")

def page_text(n):
    with open(os.path.join(RUN, "page_%03d.tex" % n), encoding="utf-8") as fh:
        return fh.read().replace("\r\n", "\n")

F = []
def add(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None, fixnull=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if fixnull else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

SETMIN = "Subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision (FIX_POLICY 2.7)."
RESP = "'(resp.' and the closing parenthesis printed roman inside the italic statement; the words inside stay italic."
LABELS = "Roman-numeral labels printed upright (GLOBAL_ISSUES 16); one edit covers all labels of the list."
PARA = "Text after the list is an indented new paragraph in the print (GLOBAL_ISSUES 80)."
TITLE = "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop)."

# ---------------------------------------------------------------- page 225
add(225, "top of page_225.tex: \\oldpage[IV-3]{225} before 'Posons S=Spec(A), ... on a donc par définition'",
    "p. 225 begins 'P=Proj(B), où B est la A-algèbre graduée ...'; the lines 'Posons S=Spec(A), et considérons le S-schéma P obtenu en faisant éclater le point fermé s de S (II, 8.1.3); si m est l'idéal maximal de A, on a donc par définition' are the last two lines of p. 224 (page_224_s4.png)",
    "marker stands three source lines too early, before 'Posons'",
    "marker", None, "high",
    r"""\oldpage[IV-3]{225}
Posons $S=\operatorname{Spec}(A)$, et considérons le $S$-schéma $P$ obtenu en
faisant éclater le point fermé $s$ de $S$ (\textbf{II}, 8.1.3)~; si $\mathfrak m$
est l'idéal maximal de $A$, on a donc par définition
$P=\operatorname{Proj}(B)$""",
    r"""Posons $S=\operatorname{Spec}(A)$, et considérons le $S$-schéma $P$ obtenu en
faisant éclater le point fermé $s$ de $S$ (\textbf{II}, 8.1.3)~; si $\mathfrak m$
est l'idéal maximal de $A$, on a donc par définition
\oldpage[IV-3]{225}
$P=\operatorname{Proj}(B)$""",
    "Mid-sentence page break: the moved marker gets no blank line around it. The moved lines match the print of p. 224 word for word. The pp. 220-224 checker may report the same move (their page_224.tex lacks these lines); apply once.")

add(225, "l. 4: 'isomorphe à une algèbre de polynômes k[t_1, ..., t_e]'",
    "'algèbre de polynômes' italic", "upright", "italics", None, "high",
    "à une algèbre de polynômes", r"à une \emph{algèbre de polynômes}")

add(225, "l. 4: '(t_i indéterminées) (0, 17.1.1)'",
    "(0, 17.1.1): bold 0 with no subscript (enlarged crop p225_s1_ref0.png)",
    "($\\mathbf{0}_{\\mathrm{IV}}$, 17.1.1): subscript IV added", "extra", None, "high",
    r"($\mathbf{0}_{\mathrm{IV}}$, 17.1.1)", r"($\mathbf{0}$, 17.1.1)",
    "The other IV-3 files write the print's (0, 14.3.3) as ($\\mathbf 0$, 14.3.3). ega4-15 has two more $\\mathbf{0}_{\\mathrm{IV}}$ (16.5.4 on p. 230, where the print also has (0, 16.5.4) without subscript, and 17.3.7 on p. 231).")

add(225, "l. 8: 'l'on a k(ζ)=k(t_1, ..., t_{e-1})'",
    "bold italic k in k(ζ) (enlarged crop p225_s1_kzeta.png); k(t_1, ...) is a light italic k",
    "$\\mathbf{k}(\\zeta)$ (bold upright)", "convention", 1, "high",
    r"$\mathbf{k}(\zeta)", r"$\boldsymbol{k}(\zeta)")

add(225, "l. 12: 'dim(O_{P,ζ})=dim(O_s)—(e—1)'",
    "two long dashes for the minus signs (enlarged crop p225_s2_minus.png)",
    "\\dim(\\mathcal O_s)-(e-1)", "convention", 7, "high",
    r"\dim(\mathcal O_s)-(e-1)$", r"\dim(\mathcal O_s)\setmin(e\setmin 1)$",
    SETMIN + " One edit for both dashes.")

add(225, "l. 13: 'que dim(h^{-1}(s))=e—1'",
    "long dash (enlarged crop p225_s2_minus.png)", "$\\dim(h^{-1}(s))=e-1$", "convention", 7, "high",
    r"$\dim(h^{-1}(s))=e-1$", r"$\dim(h^{-1}(s))=e\setmin 1$",
    SETMIN + " The minus signs in the exponents and subscripts (h^{-1}, P_k^{e-1}, t_{e-1}) are ordinary short minus signs and stay.")

add(225, "l. 17: 'cette fois k(y') est une extension séparable'",
    "bold italic k", "$\\mathbf{k}(y')$ (bold upright)", "convention", 1, "high",
    r"$\mathbf{k}(y')$ est", r"$\boldsymbol{k}(y')$ est")

add(225, "l. 17: 'extension séparable de k(y), et par suite (4.7.9)'",
    "bold italic k", "$\\mathbf{k}(y)$ (bold upright)", "convention", 1, "high",
    r"de $\mathbf{k}(y)$, et par suite", r"de $\boldsymbol{k}(y)$, et par suite")

add(225, "l. 20: 'défini par l'Idéal tO_{X'}'",
    "'l'Idéal' with a capital I (enlarged crop p225_s2_Fzi.png)", "l'idéal", "word", None, "high",
    "par l'idéal $t", "par l'Idéal $t")

add(225, "l. 21: '(F'_{η'})_{z'}=F'_{z'_i}'",
    "left side printed (F'_{η'})_{z'}: subscript z' without the index i; the right side has F'_{z'_i} (enlarged crop p225_s2_Fzi_zoom.png)",
    "$(\\mathcal F'_{\\eta'})_{z_i'}=\\mathcal F'_{z_i'}$: z_i' on both sides (silent correction)",
    "misprint_in_print", None, "high",
    r"$(\mathcal F'_{\eta'})_{z_i'}=", r"$(\mathcal F'_{\eta'})_{z'}=",
    "The identity is needed at each z'_i (the right side and (15.1.1.5) have z'_i); the TeX silently corrects. The fix restores the printed reading in the diplomatic text.",
    corrected=r"$(\mathcal F'_{\eta'})_{z_i'}=\mathcal F'_{z_i'}$")

add(225, "Corollaire (15.1.2), l. 1: 'Les hypothèses étant celles de (15.1.1), supposons'",
    "the reference (15.1.1) upright inside the italic statement (enlarged crop p225_s3_cor152.png)",
    "(15.1.1) italic", "convention", 6, "high",
    "celles de (15.1.1), supposons de plus", r"celles de \textup{(15.1.1)}, supposons de plus")

add(225, "Corollaire (15.1.2), l. 2: '(resp. que O_y soit régulier et long((F_y)_z)=1)'",
    "'(resp.' and the closing parenthesis roman, 'que ... soit régulier et' italic",
    "all italic", "convention", 6, "high",
    r"""(resp. que $\mathcal O_y$ soit régulier et
$\operatorname{long}((\mathcal F_y)_z)=1$).""",
    r"""\textup{(resp.} que $\mathcal O_y$ soit régulier et
$\operatorname{long}((\mathcal F_y)_z)=1$\textup{)}.""", RESP)

add(225, "Corollaire (15.1.2), end: '(resp. long((F_η)_{z_i})=1)'",
    "'(resp.' and the closing parenthesis roman", "italic", "convention", 6, "high",
    r"""(resp.
$\operatorname{long}((\mathcal F_\eta)_{z_i})=1$).""",
    r"""\textup{(resp.
$\operatorname{long}((\mathcal F_\eta)_{z_i})=1$)}.""")

add(225, "Corollaire (15.1.3), 2°: 'F_y=F⊗_{O_Y}k(y)'",
    "bold italic k (enlarged crop p225_s3_cor153.png)", "$\\mathbf{k}(y)$ (bold upright)", "convention", 1, "high",
    r"\otimes_{\mathcal O_Y}\mathbf{k}(y)$", r"\otimes_{\mathcal O_Y}\boldsymbol{k}(y)$")

add(225, "Corollaire (15.1.3), 2°: 'géométriquement réduit sur k(y), autrement dit'",
    "bold italic k", "$\\mathbf{k}(y)$ (bold upright)", "convention", 1, "high",
    r"sur $\mathbf{k}(y)$, autrement", r"sur $\boldsymbol{k}(y)$, autrement")

add(225, "Corollaire (15.1.3), 2°: '(resp. O_y est régulier et long((F_y)_z)=1)'",
    "'(resp.' and the closing parenthesis roman, 'est régulier et' italic",
    "all italic", "convention", 6, "high",
    r"""(resp. $\mathcal O_y$ est régulier et
$\operatorname{long}((\mathcal F_y)_z)=1$).""",
    r"""\textup{(resp.} $\mathcal O_y$ est régulier et
$\operatorname{long}((\mathcal F_y)_z)=1$\textup{)}.""", RESP)

add(225, "Corollaire (15.1.3), end: '(resp. long((F_η)_{z'})=1)'",
    "'(resp.' and the closing parenthesis roman", "italic", "convention", 6, "high",
    r"""(resp.
$\operatorname{long}((\mathcal F_\eta)_{z'})=1$).""",
    r"""\textup{(resp.
$\operatorname{long}((\mathcal F_\eta)_{z'})=1$)}.""")

# ---------------------------------------------------------------- page 226
add(226, "heading 15.2: 'Platitude des morphismes universellement ouverts à fibres géométriquement réduites.'",
    "title ends with a full stop", "no full stop", "punctuation", None, "high",
    r"\subsection{Platitude des morphismes universellement ouverts à fibres géométriquement réduites}",
    r"\subsection{Platitude des morphismes universellement ouverts à fibres géométriquement réduites.}",
    TITLE)

add(226, "Théorème (15.2.2): labels (i)-(iv)",
    "labels (i), (ii), (iii), (iv) upright", "enumerate labels italic inside the italic theorem",
    "convention", 6, "high",
    r"""suivantes~:
\begin{enumerate}[label=(\roman*)]""",
    r"""suivantes~:
\begin{enumerate}[label=\textup{(\roman*)}]""", LABELS)

add(226, "Théorème (15.2.2), (iii): 'F_y=F⊗_{O_Y}k(y)'",
    "bold italic k (enlarged crop p226_s3_iii.png)", "$\\mathbf{k}(y)$ (bold upright)", "convention", 1, "high",
    r"\otimes_{\mathcal O_Y}\mathbf{k}(y)$ est", r"\otimes_{\mathcal O_Y}\boldsymbol{k}(y)$ est")

add(226, "Théorème (15.2.2), (iii): 'au point x (4.6.22)'",
    "reference upright (enlarged crop p226_s3_iii.png)", "italic", "convention", 6, "high",
    "(4.6.22)", r"\textup{(4.6.22)}")

add(226, "Théorème (15.2.2): 'Alors F est f-plat au point x.' after the list",
    "indented new paragraph", "follows \\end{enumerate} without a blank line (no indent)", "other", None, "high",
    r"""\end{enumerate}
Alors $\mathcal F$""",
    r"""\end{enumerate}

Alors $\mathcal F$""", PARA)

add(226, "proof of (15.2.2), l. 1: 'Comme O_y est réduit et noethérien'",
    "'réduit' italic (enlarged crop p226_s3_proof.png)", "upright", "italics", None, "high",
    "est réduit et noethérien", r"est \emph{réduit} et noethérien")

# ---------------------------------------------------------------- page 227
add(227, "Lemme (15.2.2.1): labels (i)-(iii)",
    "labels upright", "enumerate labels italic inside the italic lemma", "convention", 6, "high",
    r"""conditions suivantes~:
\begin{enumerate}[label=(\roman*)]""",
    r"""conditions suivantes~:
\begin{enumerate}[label=\textup{(\roman*)}]""", LABELS)

add(227, "Lemme (15.2.2.1), (iii): 'F_y=F⊗_{O_y}k(y)'",
    "bold italic k (enlarged crop p227_s1_iii.png)", "$\\mathbf{k}(y)$ (bold upright)", "convention", 1, "high",
    r"\otimes_{\mathcal O_y}\mathbf{k}(y)$", r"\otimes_{\mathcal O_y}\boldsymbol{k}(y)$")

add(227, "Lemme (15.2.2.1), (iii): 'est réduit au point x (3.2.2)'",
    "reference upright (enlarged crop p227_s1_iii.png)", "italic", "convention", 6, "high",
    "au point $x$ (3.2.2).", r"au point $x$ \textup{(3.2.2)}.")

add(227, "Lemme (15.2.2.1): 'Alors F est f-plat au point x.' after the list",
    "indented new paragraph", "follows \\end{enumerate} without a blank line (no indent)", "other", None, "high",
    r"""\end{enumerate}
Alors $\mathcal F$""",
    r"""\end{enumerate}

Alors $\mathcal F$""", PARA)

add(227, "Corollaire (15.2.3): labels (i)-(iii)",
    "labels upright", "enumerate labels italic inside the italic corollary", "convention", 6, "high",
    r"""conditions
suivantes~:
\begin{enumerate}[label=(\roman*)]""",
    r"""conditions
suivantes~:
\begin{enumerate}[label=\textup{(\roman*)}]""", LABELS)

add(227, "Corollaire (15.2.3), (ii): '(sur k(y))'",
    "bold italic k (enlarged crop p227_s2_sur.png)", "$\\mathbf{k}(y)$ (bold upright)", "convention", 1, "high",
    r"(sur $\mathbf{k}(y)$)", r"(sur $\boldsymbol{k}(y)$)",
    "The parentheses of '(sur k(y))' are italic in the print, as in the TeX.")

add(227, "Corollaire (15.2.3), (ii): 'au point x (4.6.9)'",
    "reference upright (enlarged crop p227_s2_sur.png)", "italic", "convention", 6, "high",
    "(4.6.9)", r"\textup{(4.6.9)}")

add(227, "Corollaire (15.2.3): 'Sous ces conditions f est plat au point x.' after the list",
    "indented new paragraph", "follows \\end{enumerate} without a blank line (no indent)", "other", None, "high",
    r"""\end{enumerate}
Sous ces conditions""",
    r"""\end{enumerate}

Sous ces conditions""", PARA)

add(227, "Remarques (15.2.4), (ii): 'universellement ouvert au point x seulement'",
    "'au point' italic, 'seulement' roman (enlarged crop p227_s3_aupoint.png)",
    "\\emph{au point $x$ seulement}", "italics", None, "high",
    r"\emph{au point $x$ seulement}", r"\emph{au point $x$} seulement",
    "Judged with the remark body as roman (document-wide remark font).")

add(227, "Remarques (15.2.4), (iii): 'considéré comme k(y)-préschéma'",
    "bold italic k (enlarged crop p227_s3_iii.png)", "$\\mathbf{k}(y)$ (bold upright)", "convention", 1, "high",
    r"comme $\mathbf{k}(y)$-préschéma", r"comme $\boldsymbol{k}(y)$-préschéma")

add(227, "Remarques (15.2.4), (iii): 'n'a pas de cycles premiers associés immergés.'",
    "the clause is italic (enlarged crop p227_s3_iii.png)", "upright (no \\emph)", "italics", None, "high",
    r"""n'a pas de cycles premiers associés
  immergés.""",
    r"""\emph{n'a pas de cycles premiers associés
  immergés}.""",
    "Judged with the remark body as roman (document-wide remark font).")

add(227, "Remarques (15.2.4), (iii): 'Y=Spec(K[S, T]/(S^3—T^2))'",
    "long dash (enlarged crop p227_s3_iii.png)", "S^3-T^2", "convention", 7, "high",
    r"\operatorname{Spec}(K[S,T]/(S^3-T^2))", r"\operatorname{Spec}(K[S,T]/(S^3\setmin T^2))",
    SETMIN)

add(227, "Remarques (15.2.4), (iii): 'et pour X sa normalisée (II, 6.3.8)'",
    "'normalisée' italic (enlarged crop p227_s3_iii.png)", "upright", "italics", None, "high",
    "sa normalisée", r"sa \emph{normalisée}",
    "Judged with the remark body as roman (document-wide remark font).")

add(227, "Remarques (15.2.4), (iii): 'A=K[S, T]/(S^3—T^2)'",
    "long dash", "S^3-T^2", "convention", 7, "high",
    r"$A=K[S,T]/(S^3-T^2)$", r"$A=K[S,T]/(S^3\setmin T^2)$", SETMIN)

add(227, "Remarques (15.2.4), (iii): 'n'est pas un k(y)-préschéma réduit'",
    "bold italic k", "$\\mathbf{k}(y)$ (bold upright)", "convention", 1, "high",
    r"un $\mathbf{k}(y)$-préschéma réduit", r"un $\boldsymbol{k}(y)$-préschéma réduit")

# ---------------------------------------------------------------- page 228
add(228, "Remarques (15.2.4), (iv): 'On peut alors prendre Y=Spec(A), ...' after the list 1), 2)",
    "indented new paragraph", "follows \\end{enumerate} without a blank line", "other", None, "high",
    r"""\end{enumerate}
  On peut alors prendre""",
    r"""\end{enumerate}

  On peut alors prendre""",
    PARA + " The paragraph lies inside item (iv) of the outer list, where the indent depends on \\listparindent.")

add(228, "Remarques (15.2.4), (v): 'le corps résiduel k' est séparable sur k(y)'",
    "'séparable' italic (enlarged crop p228_s2_v.png)", "upright", "italics", None, "high",
    "est séparable", r"est \emph{séparable}",
    "Judged with the remark body as roman. Independent of the next entry (no overlap).")

add(228, "Remarques (15.2.4), (v): 'séparable sur k(y); en effet'",
    "bold italic k (enlarged crop p228_s2_v.png)", "$\\mathbf{k}(y)$ (bold upright)", "convention", 1, "high",
    r"$\mathbf{k}(y)$~; en effet", r"$\boldsymbol{k}(y)$~; en effet")

add(228, "Remarques (15.2.4), (v): 'μ_i(k(z')|k')'",
    "bold italic k in k(z'); k' light italic (enlarged crop p228_s2_v.png)",
    "\\mathbf{k}(z') (bold upright)", "convention", 1, "high",
    r"$\mu_i(\mathbf{k}(z')\mid k')$", r"$\mu_i(\boldsymbol{k}(z')\mid k')$")

add(228, "Remarques (15.2.4), (v): 'μ_i(k(z)|k(y))'",
    "two bold italic k (enlarged crop p228_s2_v.png)", "\\mathbf{k}(z), \\mathbf{k}(y) (bold upright)",
    "convention", 1, "high",
    r"$\mu_i(\mathbf{k}(z)\mid\mathbf{k}(y))$", r"$\mu_i(\boldsymbol{k}(z)\mid\boldsymbol{k}(y))$",
    "Two occurrences, one edit.")

add(228, "Remarques (15.2.4), (v): 'lorsque O_y est unibranche et dominé'",
    "'unibranche' italic (enlarged crop p228_s2_v.png)", "upright", "italics", None, "high",
    "est unibranche et", r"est \emph{unibranche} et",
    "Judged with the remark body as roman (document-wide remark font).")

add(228, "Remarques (15.2.4), (v): 'est extension séparable de k(y)'",
    "'séparable' italic", "upright", "italics", None, "high",
    "extension séparable de", r"extension \emph{séparable} de",
    "Judged with the remark body as roman. Independent of the next entry (no overlap).")

add(228, "Remarques (15.2.4), (v): 'séparable de k(y), en vertu de (11.6.4)'",
    "bold italic k", "$\\mathbf{k}(y)$ (bold upright)", "convention", 1, "high",
    r"$\mathbf{k}(y)$, en vertu de", r"$\boldsymbol{k}(y)$, en vertu de")

add(228, "Remarques (15.2.4), (v): 'O_y est un anneau régulier, d'après (15.1.1.6)'",
    "'régulier' italic", "upright", "italics", None, "high",
    "anneau régulier, d'après", r"anneau \emph{régulier}, d'après",
    "Judged with the remark body as roman (document-wide remark font).")

add(228, "Remarques (15.2.4), (v): 'des anneaux locaux intégralement clos noethériens'",
    "'intégralement clos' italic", "upright", "italics", None, "high",
    "intégralement clos noethériens", r"\emph{intégralement clos} noethériens",
    "Judged with the remark body as roman (document-wide remark font).")

add(228, "heading 15.3: 'Applications : critères de réduction et d'irréductibilité.'",
    "title ends with a full stop", "no full stop", "punctuation", None, "high",
    r"\subsection{Applications : critères de réduction et d'irréductibilité}",
    r"\subsection{Applications : critères de réduction et d'irréductibilité.}", TITLE)

add(228, "Proposition (15.3.1), l. 3: 'les conditions (i), (ii) et (iii) de (15.2.2). Alors :'",
    "(i), (ii), (iii) and (15.2.2) upright, 'et', 'de' italic (enlarged crop p228_s3_cond.png)",
    "all italic", "convention", 6, "high",
    r"""les conditions (i), (ii) et (iii) de
(15.2.2). Alors""",
    r"""les conditions \textup{(i), (ii)} et \textup{(iii)} de
\textup{(15.2.2)}. Alors""", "Three groups, one edit.")

add(228, "Proposition (15.3.1): labels (i), (ii)",
    "labels upright", "enumerate labels italic inside the italic proposition", "convention", 6, "high",
    r"\begin{enumerate}[label=(\roman*)]", r"\begin{enumerate}[label=\textup{(\roman*)}]",
    LABELS + " Independent of the previous entry (no overlap).")

add(228, "Proposition (15.3.1), (i): 'géométriquement réduit sur k(f(x')) au point x''",
    "bold italic k (enlarged crop p228_s3_cond.png)", "$\\mathbf{k}(f(x'))$ (bold upright)", "convention", 1, "high",
    r"$\mathbf{k}(f(x'))$", r"$\boldsymbol{k}(f(x'))$")

add(228, "proof of (15.3.1), l. 3: 'que F est f-plat au point x, donc aussi (11.1.1)'",
    "'f-plat' italic (enlarged crop p228_s4_fplat.png)", "$f$-plat, 'plat' upright", "italics", None, "high",
    "$f$-plat au point $x$, donc aussi", r"$f$-\emph{plat} au point $x$, donc aussi")

# ---------------------------------------------------------------- page 229
add(229, "Proposition (15.3.2): 'celles de (15.3.1), supposons que les conditions (i), (ii), (iii) de (15.2.2) soient vérifiées'",
    "(15.3.1), (i), (ii), (iii) and (15.2.2) upright, 'de' italic (enlarged crop p229_s1_prop.png)",
    "all italic", "convention", 6, "high",
    r"""celles de (15.3.1), supposons que les conditions (i), (ii),
(iii) de (15.2.2) soient""",
    r"""celles de \textup{(15.3.1)}, supposons que les conditions \textup{(i), (ii),
(iii)} de \textup{(15.2.2)} soient""", "Three groups, one edit.")

add(229, "Corollaire (15.3.3), l. 1: 'Les notations étant celles de (15.3.1), supposons vérifiées'",
    "reference upright (enlarged crop p229_s2_cor.png)", "italic", "convention", 6, "high",
    "celles de (15.3.1), supposons vérifiées", r"celles de \textup{(15.3.1)}, supposons vérifiées")

add(229, "Corollaire (15.3.3): labels (i)-(iv)",
    "labels upright", "enumerate labels italic inside the italic corollary", "convention", 6, "high",
    r"""suivantes~:
\begin{enumerate}[label=(\roman*)]""",
    r"""suivantes~:
\begin{enumerate}[label=\textup{(\roman*)}]""", LABELS)

add(229, "Corollaire (15.3.3), (iii): 'géométriquement ponctuellement intègre sur k(y)'",
    "bold italic k (enlarged crop p229_s2_cor.png)", "$\\mathbf{k}(y)$ (bold upright)", "convention", 1, "high",
    r"$\mathbf{k}(y)$ au point", r"$\boldsymbol{k}(y)$ au point",
    "Independent of the next entry (no overlap).")

add(229, "Corollaire (15.3.3), (iii): 'au point x (4.6.22)'",
    "reference upright (enlarged crop p229_s2_cor.png)", "italic", "convention", 6, "high",
    "(4.6.22)", r"\textup{(4.6.22)}")

add(229, "Corollaire (15.3.3): 'Alors x n'appartient qu'à une seule composante irréductible de X.' after the list",
    "indented new paragraph", "follows \\end{enumerate} without a blank line (no indent)", "other", None, "high",
    r"""\end{enumerate}
Alors $x$""",
    r"""\end{enumerate}

Alors $x$""", PARA)

add(229, "Remarques (15.3.4), (ii): 'La remarque (15.2.4, (vi)) montre que'",
    "(15.2.4, (vi)) (enlarged crop p229_s3_rem.png); Remarques (15.2.4) has only the items (i)-(v) (pp. 227-228)",
    "(15.2.4, (vi)): the TeX keeps the printed reading", "misprint_in_print", None, "medium",
    None, None,
    "The item meant is (v), the one that treats a regular O_y (p. 228). No erratum found in ega4-errata-addenda-list3. The reading (v) is an inference from the content of (15.2.4).",
    corrected="(15.2.4, (v))", fixnull=True)

add(229, "Remarques (15.3.4), (ii): 'O_y est régulier, Supp(F)=X'",
    "'régulier' italic (enlarged crop p229_s3_rem.png)", "upright", "italics", None, "high",
    "est régulier,", r"est \emph{régulier},",
    "Judged with the remark body as roman. The later 'que O_y est régulier par celle' is roman in the print, as in the TeX.")

add(229, "Remarques (15.3.4), (ii): 'F_y est intègre au point x.'",
    "'intègre au point x' italic (enlarged crop p229_s3_rem.png)", "upright", "italics", None, "high",
    r"""est intègre au point
  $x$. Nous""",
    r"""est \emph{intègre au point}
  $x$. Nous""", "Judged with the remark body as roman (document-wide remark font).")

add(229, "heading 15.4: 'Compléments sur les morphismes de Cohen-Macaulay.'",
    "title ends with a full stop", "no full stop", "punctuation", None, "high",
    r"\subsection{Compléments sur les morphismes de Cohen-Macaulay}",
    r"\subsection{Compléments sur les morphismes de Cohen-Macaulay.}", TITLE)

add(229, "Proposition (15.4.1), l. 3: 'F_{f(z)}=F⊗_{O_{f(z)}}k(f(z))'",
    "bold italic k (enlarged crop p229_s4_kfz.png)", "\\mathbf{k}(f(z)) (bold upright)", "convention", 1, "high",
    r"\otimes_{\mathcal O_{f(z)}}\mathbf{k}(f(z))", r"\otimes_{\mathcal O_{f(z)}}\boldsymbol{k}(f(z))")

add(230, "end of p. 229 / top of page_230.tex: '... Alors f est | équidimensionnel au point x.' then 'En effet ((11.1.1) ...'",
    "p. 229 ends with 'Alors f est équidimensionnel au point x.' (page_229_s4.png); p. 230 begins with the indented paragraph 'En effet ((11.1.1) et (12.1.1, (vi))), ...' (page_230_s1.png)",
    "\\oldpage[IV-3]{230} stands before 'équidimensionnel au point $x$.', one line too early",
    "marker", None, "high",
    r"""\oldpage[IV-3]{230}
équidimensionnel au point $x$.

En effet""",
    r"""équidimensionnel au point $x$.

\oldpage[IV-3]{230}
En effet""",
    "OUTSIDE pp. 225-229: 'old' lies in page_230.tex (checked unique there). The pp. 230-234 checker may report the same move; apply once. The same lines are touched by any p. 230 fix that ends the italic proposition environment of (15.4.1) after 'équidimensionnel au point $x$.' (the proof 'En effet ...' is printed roman but sits inside \\begin{proposition}...\\end{proposition}): reconcile the two edits.")

# ---------------------------------------------------------------- checks
ok = True
cache = {}
for i, d in enumerate(F):
    fx = d["fix"]
    if fx is None:
        continue
    p = d["page"]
    if p not in cache:
        cache[p] = page_text(p)
    n = cache[p].count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE/ABSENT (%d): entry %d page %d: %r" % (n, i, p, fx["old"]))
    if fx["old"] == fx["new"]:
        ok = False
        print("old == new: entry %d" % i)

# overlap check between fixes on the same page (character ranges)
from collections import defaultdict
ranges = defaultdict(list)
for i, d in enumerate(F):
    fx = d["fix"]
    if fx is None:
        continue
    t = cache[d["page"]]
    s = t.find(fx["old"])
    ranges[d["page"]].append((s, s + len(fx["old"]), i))
for p, rs in ranges.items():
    rs.sort()
    for a, b in zip(rs, rs[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP page %d: entries %d and %d" % (p, a[2], b[2]))

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
c = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    c[(d["page"], k)] += 1
for p in sorted({d["page"] for d in F}):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("entries", len(F), "checks", "OK" if ok else "FAILED")
