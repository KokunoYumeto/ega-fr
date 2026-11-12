"""Build findings_036_040.json for run_0IV1 pages 36-40 and check every fix.

Each "old" must occur exactly once in its page_NNN.tex (CRLF normalised to LF), and the
fixes of a page must still apply one after another, in list order and in reverse order.
"""
import json
from pathlib import Path

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_0IV1")
OUT = RUN / "findings_036_040.json"
NL = "<NL>"

CONT39 = ("In the page-39 continuation: ega0-17-fr.tex, before its first page marker "
          "\\oldpage[0\\textsubscript{IV-1}]{40} (outside the page-39 segment).")
C7 = ("Long dash used for a subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision. "
      "\\setmin is not defined in the IV1 preamble EGA_IV1_FR.tex.")
BUL = ("The print's superscript is a raised bullet (enlarged crop), not an asterisk.")
DOTS = "Baseline dots in the print (enlarged crop); GLOBAL_ISSUES 22."
NO = "n with raised o in the print; same form as elsewhere in the edition."


def F(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv,
             confidence=conf, fix=None if old is None else dict(old=old.replace(NL, "\n"),
                                                                new=new.replace(NL, "\n")))
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []
# ---------------------------------------------------------------- page 36
L += [
    F(36, "Prop. (16.4.10) (i), item label", "label (i) upright",
      r"\item[(i)] inside the italic proposition: label italic", "convention", 6, "high",
      r"\item[(i)]", r"\item[\textup{(i)}]", "GLOBAL_ISSUES 16."),
    F(36, "Prop. (16.4.10) (ii), item label", "label (ii) upright",
      r"\item[(ii)] inside the italic proposition: label italic", "convention", 6, "high",
      r"\item[(ii)]", r"\item[\textup{(ii)}]", "GLOBAL_ISSUES 16."),
    F(36, "after (16.4.10): 'Nous montrerons plus tard (IV, 6.11.5)'", "bold IV",
      "(IV, 6.11.5), plain IV", "convention", 2, "high",
      r"(IV, 6.11.5)", r"(\textbf{IV}, 6.11.5)", "GLOBAL_ISSUES 4."),
    F(36, "Prop. (16.4.11): 'Sous les hypothèses de (16.4.8), on a'",
      "reference (16.4.8) upright in the italic statement (crop)", "italic (statement environment)",
      "convention", 6, "high", r"(16.4.8), on a", r"\textup{(16.4.8)}, on a"),
    F(36, "heading 16.5", "'16.5. Modules de Cohen-Macaulay.' with a final full stop",
      r"\subsection{Modules de Cohen-Macaulay}", "punctuation", None, "high",
      r"\subsection{Modules de Cohen-Macaulay}", r"\subsection{Modules de Cohen-Macaulay.}",
      "GLOBAL_ISSUES 43 holds for the 0_IV files too: none of the 52 \\subsection titles in "
      "ega0-14 ... ega0-23 has the printed final full stop."),
    F(36, "Déf. (16.5.1): 'M est un module de Cohen-Macaulay si'",
      "italic like the rest of the definition, no change of face (crop)",
      r"\emph{module de Cohen-Macaulay} inside the italic definition: upright", "convention", 6, "high",
      r"\emph{module de Cohen-Macaulay}", r"module de Cohen-Macaulay",
      "\\emph inside the \\itshape environment sets the words upright."),
    F(36, "Déf. (16.5.1): 'On dit que A est un anneau de Cohen-Macaulay si'",
      "italic like the rest of the definition, no change of face (crop)",
      r"\emph{anneau de Cohen-Macaulay} inside the italic definition: upright", "convention", 6, "high",
      r"\emph{anneau de Cohen-Macaulay}", r"anneau de Cohen-Macaulay",
      "\\emph inside the \\itshape environment sets the words upright."),
    F(36, "after (16.5.1): 'Un anneau local réduit A de dimension 1 est un anneau de Cohen-Macaulay'",
      "'réduit' and 'de dimension' italic; A and 1 roman (crop)", "all roman", "italics", None, "high",
      r"local réduit $A$ de dimension $1$", r"local \emph{réduit} $A$ \emph{de dimension} $1$"),
    F(36, "after (16.5.1): '(Bourbaki, Alg. comm., chap. IV, § 2, n° 5, prop. 10)'", "n° 5", "no~5",
      "symbol", None, "high", r"no~5", r"n\textsuperscript{o}~5", NO),
    F(36, "after (16.5.1): '(Bourbaki, Alg. comm., chap. VII, § 1, n° 4, prop. 8)'", "n° 4", "no~4",
      "symbol", None, "high", r"no~4", r"n\textsuperscript{o}~4", NO),
    F(36, "after (16.5.1): '(Bourbaki, Alg. comm., chap. II, § 1, n° 1, prop. 2)'", "n° 1", "no~1",
      "symbol", None, "high", r"no~1", r"n\textsuperscript{o}~1", NO),
    F(36, "after (16.5.1): 'On en conclut qu'un anneau local intégralement clos de dimension 2'",
      "'intégralement clos de dimension' italic; 2 roman (crop)", "roman", "italics", None, "high",
      r"local intégralement clos de dimension $2$", r"local \emph{intégralement clos de dimension} $2$"),
    F(36, "Prop. (16.5.3): 'Sous les hypothèses de (16.4.8), pour que M soit'",
      "reference (16.4.8) upright in the italic statement (crop)", "italic (statement environment)",
      "convention", 6, "high", r"(16.4.8), pour que", r"\textup{(16.4.8)}, pour que"),
]
# ---------------------------------------------------------------- page 37
L += [
    F(37, "Prop. (16.5.5), label a)", "label a) upright (crop)",
      r"\item[a)] inside the italic proposition: label italic", "convention", 6, "high",
      r"\item[a)] $x$ est", r"\item[\textup{a)}] $x$ est"),
    F(37, "Prop. (16.5.5), label b)", "label b) upright (crop)",
      r"\item[b)] inside the italic proposition: label italic", "convention", 6, "high",
      r"\item[b)] $\dim(M/xM)", r"\item[\textup{b)}] $\dim(M/xM)"),
    F(37, "Prop. (16.5.5) b): 'dim(M/xM)=dim(M)—1'", "long dash (crop)", r"\dim(M)-1 (minus sign)",
      "convention", 7, "high", r"=\dim(M)-1$~;", r"=\dim(M)\setmin 1$~;", C7),
    F(37, "Prop. (16.5.5), label c)", "label c) upright (crop)",
      r"\item[c)] inside the italic proposition: label italic", "convention", 6, "high",
      r"\item[c)] $x$ n'appartient", r"\item[\textup{c)}] $x$ n'appartient"),
    F(37, "Prop. (16.5.5), last sentence: 'En outre, M/xM est alors un modulede Cohen-Macaulay.'",
      "'modulede': no space between 'module' and 'de' (crop)", "module de (silently corrected)",
      "misprint_in_print", None, "high", r"est alors un module de", r"est alors un modulede",
      "Diplomatic text restores the printed reading.", corrected=r"est alors un module de"),
    F(37, "proof of (16.5.5): '(Bourbaki, Alg. comm., chap. IV, § 1, n° 1, cor. 2 de la prop. 2)'",
      "n° 1", "no~1", "symbol", None, "high", r"no~1", r"n\textsuperscript{o}~1", NO),
    F(37, "Cor. (16.5.6): 'Sous les hypothèses de (16.5.5), soit'",
      "reference (16.5.5) upright in the italic statement (crop)", "italic (statement environment)",
      "convention", 6, "high", r"(16.5.5), soit", r"\textup{(16.5.5)}, soit"),
    F(37, "Cor. (16.5.6), label a)", "label a) upright (crop)",
      r"\item[a)] inside the italic corollary: label italic", "convention", 6, "high",
      r"\item[a)] La suite", r"\item[\textup{a)}] La suite"),
    F(37, "Cor. (16.5.6), label b)", "label b) upright (crop)",
      r"\item[b)] inside the italic corollary: label italic", "convention", 6, "high",
      r"\item[b)] On a", r"\item[\textup{b)}] On a"),
    F(37, "Cor. (16.5.6) b): 'dim(M/(x_1M+...+x_rM))'", "baseline dots", r"\cdots", "symbol", None, "high",
      r"\dim(M/(x_1M+\cdots", r"\dim(M/(x_1M+\ldots", DOTS),
    F(37, "Cor. (16.5.6) b): '=dim(M)—r'", "long dash (crop)", r"\dim(M)-r (minus sign)",
      "convention", 7, "high", r"x_rM))=\dim(M)-r$", r"x_rM))=\dim(M)\setmin r$", C7),
    F(37, "Cor. (16.5.6), label c)", "label c) upright (crop)",
      r"\item[c)] inside the italic corollary: label italic", "convention", 6, "high",
      r"\item[c)] Les", r"\item[\textup{c)}] Les"),
    F(37, "Cor. (16.5.6), last sentence: 'N=M/(x_1M+...+x_rM) est un module'", "baseline dots (crop)",
      r"\cdots", "symbol", None, "high",
      r"$N=M/(x_1M+\cdots+x_rM)$ est", r"$N=M/(x_1M+\ldots+x_rM)$ est", DOTS),
    F(37, "Cor. (16.5.6), last sentence: 'dim(A/p)=dim(M)—r'", "long dash", r"\dim(M)-r (minus sign)",
      "convention", 7, "high", r"\mathfrak{p})=\dim(M)-r$", r"\mathfrak{p})=\dim(M)\setmin r$", C7),
    F(37, "proof of (16.5.6): 'On sait déjà que b) et c) sont équivalentes'", "b) and c) italic (crop)",
      "roman", "italics", None, "high",
      r"que b) et c) sont", r"que \emph{b)} et \emph{c)} sont"),
    F(37, "proof of (16.5.6): 'et que a) entraîne c) (16.4.1)'", "a) and c) italic (crop)", "roman",
      "italics", None, "high", r"que a) entraîne c)", r"que \emph{a)} entraîne \emph{c)}"),
    F(37, "proof of (16.5.6): 'Pour voir que c) implique a)'", "c) and a) italic (crop)", "roman",
      "italics", None, "high", r"que c) implique a)", r"que \emph{c)} implique \emph{a)}"),
    F(37, "proof of (16.5.6): 'dim(M/x_1M)=dim(M)—1 (16.3.6)'", "long dash", r"\dim(M)-1 (minus sign)",
      "convention", 7, "high", r"\dim(M)-1$ (16.3.6)", r"\dim(M)\setmin 1$ (16.3.6)", C7),
    F(37, "proof of (16.5.6): 'P/(x_2P+...+x_rP)=N'", "baseline dots (crop)", r"\cdots", "symbol", None,
      "high", r"$P/(x_2P+\cdots", r"$P/(x_2P+\ldots", DOTS),
    F(37, "Remarque (16.5.7): 'les systèmes de paramètres pour M et les suites M-régulières maximales'",
      "'et les' italic too: one italic phrase from 'systèmes' to 'd'éléments de' (crop)",
      r"two \emph groups with 'et les' roman between them", "italics", None, "high",
      r"pour $M$} et les \emph{suites", r"pour $M$ et les suites",
      "Judged with the remark body roman (document-wide remark item)."),
    F(37, "Remarque (16.5.7): 'tel qu'il y ait une suite M-régulière'", "'une' italic (crop)", "roman",
      "italics", None, "high", r"ait une suite", r"ait \emph{une} suite"),
    F(37, "Remarque (16.5.7): '(16.5.6) caractérise aussi les modules'", "'caractérise' italic, 'aussi' roman (crop)",
      r"\emph{caractérise aussi}", "italics", None, "high",
      r"\emph{caractérise aussi}", r"\emph{caractérise} aussi"),
    F(37, "Prop. (16.5.8): 'associé à N=M/(x_1M+...+x_rM), on ait'", "baseline dots (crop)", r"\cdots",
      "symbol", None, "high",
      r"$N=M/(x_1M+\cdots+x_rM)$, on ait", r"$N=M/(x_1M+\ldots+x_rM)$, on ait", DOTS),
]
# ---------------------------------------------------------------- page 38
L += [
    F(38, "Prop. (16.5.9): 'posons r=dim(M)—dim(M/pM)'", "long dash (crop)", "minus sign",
      "convention", 7, "high",
      r"$r=\dim(M)-\dim(M/\mathfrak{p}M)$", r"$r=\dim(M)\setmin\dim(M/\mathfrak{p}M)$", C7),
    F(38, "Prop. (16.5.9), display 'dim(M/(x_1M+...+x_rM))'", "baseline dots (crop)", r"\cdots",
      "symbol", None, "high", r"\dim(M/(x_1M+\cdots", r"\dim(M/(x_1M+\ldots", DOTS),
    F(38, "Prop. (16.5.9): 'Ass(M/(x_1M+...+x_rM))'", "baseline dots (crop)", r"\cdots", "symbol", None,
      "high", r"\operatorname{Ass}(M/(x_1M+\cdots", r"\operatorname{Ass}(M/(x_1M+\ldots", DOTS),
    F(38, "proof of (16.5.9): '(Bourbaki, Alg. comm., chap. II, § 1, n° 1, prop. 2)'", "n° 1", "no~1",
      "symbol", None, "high", r"no~1, prop.~2", r"n\textsuperscript{o}~1, prop.~2", NO),
    F(38, "proof of (16.5.9): '(Bourbaki, Alg. comm., chap. IV, § 1, n° 1, cor. 2 de la prop. 2)'", "n° 1",
      "no~1", "symbol", None, "high", r"no~1, cor.~2", r"n\textsuperscript{o}~1, cor.~2", NO),
    F(38, "proof of (16.5.9): 'de dimension dim(M)—1'", "long dash (crop)", "minus sign",
      "convention", 7, "high", r"de dimension $\dim(M)-1$", r"de dimension $\dim(M)\setmin 1$", C7),
    F(38, "proof of (16.5.9): 'dim(N)—dim(N/pN)=r—1'", "two long dashes (crop)", "two minus signs",
      "convention", 7, "high", r"$\dim(N)-\dim(N/\mathfrak{p}N)=r-1$",
      r"$\dim(N)\setmin\dim(N/\mathfrak{p}N)=r\setmin 1$", C7 + " Two occurrences in one formula."),
    F(38, "proof of (16.5.9): '... formée d'éléments de p. Si on pose P=...'",
      "one paragraph: 'Si on pose' follows on the same line (crop)",
      "blank line before 'Si on pose' (paragraph break)", "other", None, "high",
      r"$\mathfrak{p}$." + NL + NL + "Si on pose", r"$\mathfrak{p}$." + NL + "Si on pose"),
    F(38, "proof of (16.5.9): 'Si on pose P=M/(x_1M+...+x_rM)'", "baseline dots (crop)", r"\cdots",
      "symbol", None, "high", r"$P=M/(x_1M+\cdots", r"$P=M/(x_1M+\ldots", DOTS),
    F(38, "proof of (16.5.9): 'p∈Supp(P) (0_I, 1.7.5)'", "bold 0 with subscript I (crop)",
      r"$0_{\mathrm I}$", "convention", 2, "high",
      r"($0_{\mathrm I}$, 1.7.5)", r"($\mathbf{0}_{\mathrm I}$, 1.7.5)", "GLOBAL_ISSUES 35."),
    F(38, "proof of (16.5.9): '(Bourbaki, Alg. comm., chap. IV, § 1, n° 4, th. 2)'", "n° 4", "no~4",
      "symbol", None, "high", r"no~4, th.~2", r"n\textsuperscript{o}~4, th.~2", NO),
    F(38, "proof of (16.5.9): 'et comme dim(P)=dim(P/pP)⩽dim(A/p)⩽dim(A/p')=dim(P), on a'",
      "formula inline in the running text (crop)", r"displayed with \[ ... \]", "formula", None, "high",
      r"et comme" + NL + r"\[" + NL + r"  \dim(P)=\dim(P/\mathfrak{p}P)" + NL + r"  \leq\dim(A/\mathfrak{p})"
      + NL + r"  \leq\dim(A/\mathfrak{p}')=\dim(P)," + NL + r"\]" + NL + "on a nécessairement",
      r"et comme" + NL + r"$\dim(P)=\dim(P/\mathfrak{p}P)" + NL + r"\leq\dim(A/\mathfrak{p})"
      + NL + r"\leq\dim(A/\mathfrak{p}')=\dim(P)$," + NL + "on a nécessairement",
      "GLOBAL_ISSUES 21 (inline formulas set as displays)."),
    F(38, "Cor. (16.5.10): 'Sous les mêmes hypothèses que dans (16.5.9) :'",
      "reference (16.5.9) upright in the italic statement (crop)", "italic (statement environment)",
      "convention", 6, "high", r"dans (16.5.9)~:", r"dans \textup{(16.5.9)}~:"),
    F(38, "Cor. (16.5.10), label (i)", "label (i) upright (crop)",
      r"\item[(i)] inside the italic corollary: label italic", "convention", 6, "high",
      r"\item[(i)]", r"\item[\textup{(i)}]", "GLOBAL_ISSUES 16."),
    F(38, "Cor. (16.5.10), label (ii)", "label (ii) upright (crop)",
      r"\item[(ii)] inside the italic corollary: label italic", "convention", 6, "high",
      r"\item[(ii)]", r"\item[\textup{(ii)}]", "GLOBAL_ISSUES 16."),
    F(38, "proof of (16.5.10), display: 'r=dim(M)—dim(M/pM)'", "long dash (crop)", "minus sign",
      "convention", 7, "high", r"\geq r=\dim(M)-\dim(M/\mathfrak{p}M)",
      r"\geq r=\dim(M)\setmin\dim(M/\mathfrak{p}M)", C7),
]
# ---------------------------------------------------------------- page 39
L += [
    F(39, "proof of (16.5.11): 'Spec(A/p) (0_I, 1.7.5)'", "bold 0 with subscript I", r"$0_{\mathrm I}$",
      "convention", 2, "high", r"($0_{\mathrm I}$, 1.7.5)", r"($\mathbf{0}_{\mathrm I}$, 1.7.5)",
      "GLOBAL_ISSUES 35."),
    F(39, "Cor. (16.5.12): 'vérifiant les conditions de (16.5.11) (en particulier'",
      "reference (16.5.11) upright in the italic statement; the parentheses of '(en particulier ...)' italic (crop)",
      "italic (statement environment)", "convention", 6, "high",
      r"de (16.5.11) (en", r"de \textup{(16.5.11)} (en"),
    F(39, "Cor. (16.5.12): 'est caténaire.'", "italic like the rest of the statement, no change of face (crop)",
      r"\emph{caténaire} inside the italic corollary: upright", "convention", 6, "high",
      r"est \emph{caténaire}", r"est caténaire",
      "\\emph inside the \\itshape environment sets the word upright."),
    F(39, "(16.5.13): 'S^{-1}M est un S^{-1}A-module de Cohen Macaulay (resp.'",
      "'Cohen Macaulay' without the hyphen (crop)", "Cohen-Macaulay (silently corrected)",
      "misprint_in_print", None, "high",
      r"$S^{-1}A$-module de Cohen-Macaulay", r"$S^{-1}A$-module de Cohen Macaulay",
      "Diplomatic text restores the printed reading.", corrected=r"$S^{-1}A$-module de Cohen-Macaulay"),
    F(39, "heading 17.1", "'17.1. Définition des anneaux réguliers.' with a final full stop",
      r"\subsection{Définition des anneaux réguliers}", "punctuation", None, "high",
      r"\subsection{Définition des anneaux réguliers}", r"\subsection{Définition des anneaux réguliers.}",
      CONT39 + " GLOBAL_ISSUES 43."),
    F(39, "Prop. (17.1.1) a): 'de k-modules gradués (15.1.1.1)'",
      "reference (15.1.1.1) upright in the italic statement (crop)", "italic (statement environment)",
      "convention", 6, "high", r"gradués" + NL + r"  (15.1.1.1)", r"gradués" + NL + r"  \textup{(15.1.1.1)}",
      CONT39),
    F(39, "Prop. (17.1.1) a), display: 'φ : S•_k(m/m²) → gr•_m(A)' (S)", "S with a raised bullet: S•_k",
      r"\mathbf{S}^*_k", "symbol", None, "high", r"\mathbf{S}^*_k", r"\mathbf{S}^\bullet_k", CONT39 + " " + BUL),
    F(39, "Prop. (17.1.1) a), display: 'φ : S•_k(m/m²) → gr•_m(A)' (gr)", "gr with a raised bullet: gr•_m",
      r"\operatorname{gr}^*_{\mathfrak{m}}", "symbol", None, "high",
      r"\operatorname{gr}^*_{\mathfrak{m}}(A)", r"\operatorname{gr}^\bullet_{\mathfrak{m}}(A)", CONT39 + " " + BUL),
    F(39, "proof of (17.1.1): 'donc b) et c) sont équivalentes'", "b) and c) italic (crop)", "roman",
      "italics", None, "high", r"donc b) et c) sont", r"donc \emph{b)} et \emph{c)} sont", CONT39),
    F(39, "proof of (17.1.1): 'S•(m/m²) est isomorphe à l'anneau de poly-'", "S with a raised bullet (crop)",
      r"\mathbf{S}^*", "symbol", None, "high",
      r"$\mathbf{S}^*(\mathfrak{m}/\mathfrak{m}^2)$", r"$\mathbf{S}^\bullet(\mathfrak{m}/\mathfrak{m}^2)$",
      CONT39 + " " + BUL),
]
# ---------------------------------------------------------------- page 40
L += [
    F(40, "proof of (17.1.1): 'la filtration m-préadique (0_I, 7.3.5)'", "bold 0 with subscript I (crop)",
      r"$0_{\mathrm I}$", "convention", 2, "high",
      r"($0_{\mathrm I}$, 7.3.5)", r"($\mathbf{0}_{\mathrm I}$, 7.3.5)", "GLOBAL_ISSUES 35."),
    F(40, "proof of (17.1.1): 'que les conditions a) et d) sont équivalentes'", "a) and d) italic (crop)",
      "roman", "italics", None, "high",
      r"les conditions a) et d)", r"les conditions \emph{a)} et \emph{d)}"),
    F(40, "proof of (17.1.1): 'on voit que d) entraîne c).'", "d) and c) italic (crop)", "roman", "italics",
      None, "high", r"on voit que d) entraîne c).", r"on voit que \emph{d)} entraîne \emph{c)}."),
    F(40, "proof of (17.1.1): 'Reste à prouver que c) entraîne a).'", "c) and a) italic (crop)", "roman",
      "italics", None, "high",
      r"Reste à prouver que c) entraîne a).", r"Reste à prouver que \emph{c)} entraîne \emph{a)}."),
    F(40, "proof of (17.1.1): '... entraîne a). Posons pour abréger'",
      "'Posons pour abréger' starts a line at the margin, not indented: same paragraph (crop)",
      "blank line before 'Posons' (paragraph break)", "other", None, "high",
      NL + NL + "Posons pour abréger", NL + "Posons pour abréger"),
    F(40, "proof of (17.1.1): 'S=S•(m/m²)=k[T_1, ..., T_n]'", "S with a raised bullet (crop)",
      r"\mathbf{S}^*", "symbol", None, "high", r"\mathbf{S}^*(", r"\mathbf{S}^\bullet(", BUL),
    F(40, "proof of (17.1.1): 'G=gr•_m(A)'", "gr with a raised bullet (crop)", r"\operatorname{gr}^*",
      "symbol", None, "high", r"\mathrm{G}=\operatorname{gr}^*", r"\mathrm{G}=\operatorname{gr}^\bullet", BUL),
    F(40, "(17.1.1.1): binomial (s+n—1 over n—1)", "two long dashes (crop)", "two minus signs",
      "convention", 7, "high",
      r"\binom{s+n-1}{n-1}" + NL + r"  =\operatorname{long}(\mathrm{S}_s)",
      r"\binom{s+n\setmin 1}{n\setmin 1}" + NL + r"  =\operatorname{long}(\mathrm{S}_s)",
      C7 + " Two occurrences in one formula."),
    F(40, "proof of (17.1.1): 'long(S_{s-h})=(s—h+n—1 over n—1)'",
      "three long dashes in the binomial; the subscript s-h has a short minus (crop)", "minus signs",
      "convention", 7, "high", r"=\binom{s-h+n-1}{n-1}$", r"=\binom{s\setmin h+n\setmin 1}{n\setmin 1}$",
      C7 + " Three occurrences in one formula; the subscript S_{s-h} keeps its minus."),
    F(40, "(17.1.1.2): 'long(G_s)⩽(s+n—1 over n—1)—(s—h+n—1 over n—1)'",
      "six long dashes, including the one between the binomials (crop)", "minus signs",
      "convention", 7, "high", r"\leq\binom{s+n-1}{n-1}-\binom{s-h+n-1}{n-1}.",
      r"\leq\binom{s+n\setmin 1}{n\setmin 1}\setmin\binom{s\setmin h+n\setmin 1}{n\setmin 1}.",
      C7 + " Six occurrences in one formula."),
    F(40, "proof of (17.1.1): 'de degré ⩽n—2'", "long dash (crop)", "minus sign", "convention", 7, "high",
      r"$\leq n-2$", r"$\leq n\setmin 2$", C7),
    F(40, "proof of (17.1.1): 'égal à n—1'", "long dash (crop)", "minus sign", "convention", 7, "high",
      r"égal à $n-1$", r"égal à $n\setmin 1$", C7),
    F(40, "Déf. (17.1.2): 'les conditions équivalentes de (17.1.1) est régulier'",
      "reference (17.1.1) upright in the italic definition (crop)", "italic (definition environment)",
      "convention", 6, "high", r"(17.1.1) est", r"\textup{(17.1.1)} est"),
    F(40, "Déf. (17.1.2): 'est régulier.'", "italic like the rest of the definition, no change of face (crop)",
      r"\emph{régulier} inside the italic definition: upright", "convention", 6, "high",
      r"\emph{régulier}", r"régulier", "\\emph inside the \\itshape environment sets the word upright."),
    F(40, "proof of (17.1.3): 'résulte de (17.1.1, d))'", "d) italic, the closing parenthesis roman (crop)",
      "roman", "italics", None, "high", r"(17.1.1, d))", r"(17.1.1, \emph{d)})"),
    F(40, "proof of (17.1.3): 'gr•_m(A) est intègre'", "gr with a raised bullet (crop)",
      r"\operatorname{gr}^*", "symbol", None, "high",
      r"régulier, $\operatorname{gr}^*", r"régulier, $\operatorname{gr}^\bullet", BUL),
    F(40, "proof of (17.1.3): '(Bourbaki, Alg. comm., chap. III, § 2, n° 3, cor. de la prop. 1'", "n° 3",
      "no~3", "symbol", None, "high", r"no~3", r"n\textsuperscript{o}~3", NO),
    F(40, "proof of (17.1.3): 'chap. V, § 1, n° 5, prop. 15)'", "n° 5", "no~5", "symbol", None, "high",
      r"no~5", r"n\textsuperscript{o}~5", NO),
    F(40, "Exemples (17.1.4) (ii): 'chap. VI, § 3, n° 6, prop. 9'", "n° 6", "no~6", "symbol", None, "high",
      r"no~6", r"n\textsuperscript{o}~6", NO),
    F(40, "Exemples (17.1.4) (iii): 'A/(T_1A+...+T_iA)'", "baseline dots (crop)", r"\cdots", "symbol", None,
      "high", r"\mathrm{T}_1A+\cdots+", r"\mathrm{T}_1A+\ldots+", DOTS),
]

# ---------------------------------------------------------------- checks
ok = True
pages = {}
for x in L:
    pages.setdefault(x["page"], []).append(x)
for p, xs in sorted(pages.items()):
    t = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    for x in xs:
        if x["fix"] is None:
            continue
        n = t.count(x["fix"]["old"])
        if n != 1:
            ok = False
            print(f"p{p}: old occurs {n} times: {x['fix']['old']!r}")
    for order in (xs, list(reversed(xs))):
        u = t
        for x in order:
            if x["fix"] is None:
                continue
            n = u.count(x["fix"]["old"])
            if n != 1:
                ok = False
                print(f"p{p}: sequential application fails ({n}): {x['fix']['old']!r}")
            else:
                u = u.replace(x["fix"]["old"], x["fix"]["new"])

counts = {}
for x in L:
    c = counts.setdefault(x["page"], [0, 0, 0])
    if x["kind"] == "misprint_in_print":
        c[2] += 1
    elif x["kind"] == "convention":
        c[1] += 1
    else:
        c[0] += 1
print("counts (normal/convention/misprint):", {p: "/".join(map(str, c)) for p, c in sorted(counts.items())})
print("total", len(L), "checks", "OK" if ok else "FAILED")
if ok:
    OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("written", OUT)
