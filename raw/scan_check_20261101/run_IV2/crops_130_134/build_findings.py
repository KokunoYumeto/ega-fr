"""Build findings_130_134.json for EGA IV-2 pp. 130-134 and check every fix.

Strings use the pilcrow sign as the line-break placeholder (replaced by LF).
Check: every non-null fix "old" occurs exactly once in its page_NNN.tex (CRLF normalised to LF),
both in the original page text and when the page's fixes are applied in list order.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
OUT = RUN / "findings_130_134.json"
NL = "¶"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    fix = None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


BLANK = "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20)."

# ---------------------------------------------------------------- p. 130
add(130, "top of page: 'immergés (5.7.7). L'idéal p^(1) ...' continues the sentence ending p. 129 ('... n'a pas d'idéaux premiers associés')",
    "no paragraph break: 'associés | immergés'", "blank lines before and after \\oldpage[IV-2]{130}",
    "other", None, "high",
    r"\oldpage[IV-2]{130}¶¶immergés", r"\oldpage[IV-2]{130}¶immergés",
    BLANK + " Apply together with removing the blank line BEFORE the marker, which lies in the p. 129 segment "
    "(ega4-2-fr.tex: 'd'idéaux premiers associés' + blank line + '\\oldpage[IV-2]{130}' -> no blank line), outside pp. 130-134.")
add(130, "Corollaire (5.12.10), label a)", "a) upright", "\\item[a)] (italic in the corollary environment)",
    "convention", 6, "high", r"\item[a)] $A$ est quotient", r"\item[\textup{a)}] $A$ est quotient",
    "Enlarged crop: the label is upright.")
add(130, "Corollaire (5.12.10), label b)", "b) upright", "\\item[b)] (italic)",
    "convention", 6, "high", r"\item[b)] $A$ est universellement", r"\item[\textup{b)}] $A$ est universellement")
add(130, "Corollaire (5.12.10): 'posons ℑ = x_1A + ... + x_nA'", "baseline dots x_1A + . . . + x_nA", "\\cdots (centred)",
    "symbol", None, "high", r"x_1A+\cdots+x_nA", r"x_1A+\ldots+x_nA", "Enlarged crop: the dots sit on the baseline (GLOBAL_ISSUES 22).")
add(130, "Corollaire (5.12.10), label (i)", "(i) upright", "\\item[(i)] (italic)",
    "convention", 6, "high", r"\item[(i)] Il n'existe", r"\item[\textup{(i)}] Il n'existe", "GLOBAL_ISSUES 16.")
add(130, "Corollaire (5.12.10), label (ii)", "(ii) upright", "\\item[(ii)] (italic)",
    "convention", 6, "high", r"\item[(ii)] L'idéal maximal", r"\item[\textup{(ii)}] L'idéal maximal", "GLOBAL_ISSUES 16.")
add(130, "Corollaire (5.12.10) (ii): '(donc A_p est un anneau local régulier de dimension n)'",
    "parenthesis upright except 'régulier', which is italic",
    "whole parenthesis italic (corollary environment)",
    "convention", 6, "high",
    r"(donc $A_{\mathfrak p}$ est un anneau local¶régulier de dimension $n$)",
    r"\textup{(donc $A_{\mathfrak p}$ est un anneau local¶\emph{régulier} de dimension $n$)}",
    "Enlarged crop: '(donc A_p est un anneau local' and 'de dimension n)' roman, 'régulier' italic; \\emph inside \\textup gives the italic word.")
add(130, "Corollaire (5.12.10), label (iii)", "(iii) upright", "\\item[(iii)] (italic)",
    "convention", 6, "high", r"\item[(iii)] L'anneau", r"\item[\textup{(iii)}] L'anneau", "GLOBAL_ISSUES 16.")
add(130, "Corollaire (5.12.10): 'l'anneau quotient A/(x_1A + ... + x_iA)'", "baseline dots", "\\cdots",
    "symbol", None, "high", r"A/(x_1A+\cdots+x_iA)", r"A/(x_1A+\ldots+x_iA)", "GLOBAL_ISSUES 22.")
add(130, "Corollaire (5.12.10): 'de dimension dim(A) — i'", "long dash dim(A)—i (bar 41 px; the + bars on the line above 34-35 px)",
    "minus sign", "convention", 7, "high", r"$\dim(A)-i$", r"$\dim(A)\setmin i$",
    "Long dash for subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.")
add(130, "proof of (5.12.10): 'Soit ℑ' = x_1A + ... + x_{n-1}A'", "baseline dots", "\\cdots",
    "symbol", None, "high", r"x_1A+\cdots+x_{n-1}A", r"x_1A+\ldots+x_{n-1}A", "GLOBAL_ISSUES 22.")
add(130, "proof of (5.12.10): 'on a ht(q) ≤ n — 1'", "long dash n—1 (bar 40-41 px; = bars 33-35 px)", "minus sign",
    "convention", 7, "high", r"(\mathfrak q)\leq n-1$", r"(\mathfrak q)\leq n\setmin 1$",
    "The subscript minus of x_{n-1} is a short minus in the print (no change).")
add(130, "proof of (5.12.10): '(0, 16.3.1)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 16.3.1)", r"(\textbf{0}, 16.3.1)")
add(130, "proof of (5.12.10): 'p'/q est de hauteur 1 dans A/q par le Hauptidealsatz'",
    "de hauteur 1 (no ≤ sign)", "de hauteur $\\leq1$", "extra", None, "high",
    r"de hauteur $\leq1$ dans", r"de hauteur $1$ dans",
    "Enlarged crop: no ≤ before the 1. The printed reading is correct as it stands (x_n ∉ q, since otherwise q ⊃ ℑ ⊃ p, against ht(q) ≤ n-1), "
    "so it is not a misprint; the TeX's ≤ is an editorial change.")
add(130, "proof of (5.12.10): 'par le Hauptidealsatz (0, 16.3.2)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 16.3.2)", r"(\textbf{0}, 16.3.2)")
add(130, "proof of (5.12.10): 'caténaire (0, 16.1.4)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 16.1.4)", r"(\textbf{0}, 16.1.4)")
add(130, "end of page: 'd'où q ⊂ p,' continues on p. 131 'et q est induit ...'",
    "no paragraph break", "blank line before \\oldpage[IV-2]{131}", "other", None, "high",
    r"$\mathfrak q\subset\mathfrak p$,¶¶", r"$\mathfrak q\subset\mathfrak p$,¶",
    BLANK + " Apply together with the p. 131 top-of-page entry (blank line after the marker).")

# ---------------------------------------------------------------- p. 131
add(131, "top of page: 'et q est induit sur A ...' continues the sentence of p. 130",
    "no paragraph break", "blank line after \\oldpage[IV-2]{131}", "other", None, "high",
    r"\oldpage[IV-2]{131}¶¶et $\mathfrak q$", r"\oldpage[IV-2]{131}¶et $\mathfrak q$",
    "Apply together with the p. 130 end-of-page entry (blank line before the marker).")
add(131, "proof of (5.12.10): 'et de (0, 17.1.7)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0,¶17.1.7)", r"(\textbf{0},¶17.1.7)")
add(131, "proof of (5.12.10): 'donc q = A∩ℑ'A_p est l'unique idéal premier ...'",
    "formula in the running text", "displayed formula", "other", None, "high",
    r"donc¶\[¶\mathfrak q=A\cap\mathfrak J'A_{\mathfrak p}¶\]¶est",
    r"donc¶$\mathfrak q=A\cap\mathfrak J'A_{\mathfrak p}$¶est",
    "Display vs inline only; no connecting word lost.")
add(131, "proof of (5.12.10): 'est l'unique idéal premier non immergé'", "'unique' italic", "upright",
    "italics", None, "high", r"l'unique idéal", r"l'\emph{unique} idéal")
add(131, "proof of (5.12.10): 'et il est de hauteur n — 1,'", "long dash (bar 40-42 px)", "minus sign",
    "convention", 7, "high", r"hauteur $n-1$, puisque", r"hauteur $n\setmin 1$, puisque")
add(131, "proof of (5.12.10): 'puisque ℑ'A_p est de hauteur n — 1'", "long dash (bar 41 px)", "minus sign",
    "convention", 7, "high", r"est de hauteur $n-1$ et", r"est de hauteur $n\setmin 1$ et")
add(131, "proof of (5.12.10): 'et q de hauteur ≤ n — 1.'", "long dash (bar 39-41 px)", "minus sign",
    "convention", 7, "high", r"\leq n-1$. En outre", r"\leq n\setmin 1$. En outre")
add(131, "proof of (5.12.10): 'En outre qA_p = ℑ'A_p et comme A_q = (A_p)_{qA_p}'",
    "qA_p = ℑ'A_p (Fraktur p subscripts)", "qA_q = ℑ'A_q", "formula", None, "high",
    r"$\mathfrak qA_{\mathfrak q}=\mathfrak J'A_{\mathfrak q}$",
    r"$\mathfrak qA_{\mathfrak p}=\mathfrak J'A_{\mathfrak p}$",
    "Enlarged crop: both subscripts are the Fraktur p of the neighbouring A_p, not the q. The printed reading is correct "
    "(q is the trace of the prime ℑ'A_p, so qA_p = ℑ'A_p).")
add(131, "proof of (5.12.10): 'si A vérifie l'hypothèse a)'", "'a)' italic", "upright a)",
    "italics", None, "high", r"l'hypothèse a)", r"l'hypothèse \emph{a)}")
add(131, "proof of (5.12.10): '(resp. b))'", "'b)' italic, outer parenthesis upright", "upright b)",
    "italics", None, "high", r"(resp. b))", r"(resp. \emph{b)})")
add(131, "proof of (5.12.10): 'comme B_n = A_p/qA_p et nB_n = pA_p/qA_p, le fait que'",
    "both formulas in the running text, joined by 'et'", "one display, the two formulas joined by \\qquad ('et' lost)",
    "missing", None, "high",
    r"idéal; comme¶\[¶B_{\mathfrak n}=A_{\mathfrak p}/\mathfrak qA_{\mathfrak p},\qquad¶\mathfrak nB_{\mathfrak n}¶=\mathfrak pA_{\mathfrak p}/\mathfrak qA_{\mathfrak p},¶\]¶le fait que",
    r"idéal; comme¶$B_{\mathfrak n}=A_{\mathfrak p}/\mathfrak qA_{\mathfrak p}$ et¶$\mathfrak nB_{\mathfrak n}¶=\mathfrak pA_{\mathfrak p}/\mathfrak qA_{\mathfrak p}$,¶le fait que",
    "Formula displayed where the print has it inline; the connecting word 'et' restored (GLOBAL_ISSUES 21/51).")
add(131, "proof of (5.12.10): 'qui montre que A/(x_1A + ... + x_iA)'", "baseline dots", "\\cdots",
    "symbol", None, "high", r"A/(x_1A+\cdots+x_iA)", r"A/(x_1A+\ldots+x_iA)", "GLOBAL_ISSUES 22.")
add(131, "proof of (5.12.10): 'de dimension dim(A) — i pour'", "long dash (bar 40-41 px)", "minus sign",
    "convention", 7, "high", r"$\dim(A)-i$ pour", r"$\dim(A)\setmin i$ pour")
add(131, "proof of (5.12.10): 'pour 0 ≤ i ≤ n — 1'", "long dash (bar 39-40 px)", "minus sign",
    "convention", 7, "high", r"$0\leq i\leq n-1$ et que", r"$0\leq i\leq n\setmin 1$ et que")
add(131, "proof of (5.12.10): 'dim(A/p) = dim(A) — dim(A_p)'", "long dash (bar 40 px; = bars 34-35 px)", "minus sign",
    "convention", 7, "high", r"\dim(A)-\dim(A_{\mathfrak p})", r"\dim(A)\setmin\dim(A_{\mathfrak p})")
add(131, "heading 5.13", "'... à la limite inductive.' (full stop)", "no full stop", "punctuation", None, "high",
    r"\subsection{Propriétés de permanence par passage à la limite inductive}",
    r"\subsection{Propriétés de permanence par passage à la limite inductive.}",
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop); same fix as p. 5.")
add(131, "5.13, first paragraph: 'désigne un système inductif d'anneaux dont'", "'système inductif d'anneaux' italic",
    "upright", "italics", None, "high",
    r"désigne un système¶inductif d'anneaux dont", r"désigne un \emph{système¶inductif d'anneaux} dont")
add(131, "5.13, first paragraph: 'est préordonné filtrant;'", "'filtrant' italic", "upright",
    "italics", None, "high", r"préordonné filtrant;", r"préordonné \emph{filtrant};")
add(131, "Proposition (5.13.1), label (i)", "(i) upright", "\\item[(i)] (italic)",
    "convention", 6, "high", r"\item[(i)] Pour tout indice", r"\item[\textup{(i)}] Pour tout indice", "GLOBAL_ISSUES 16.")
add(131, "Proposition (5.13.1), label (ii)", "(ii) upright", "\\item[(ii)] (italic)",
    "convention", 6, "high", r"\item[(ii)] Inversement", r"\item[\textup{(ii)}] Inversement", "GLOBAL_ISSUES 16.")
add(131, "proof of (5.13.1): 'provient de l'exactitute du foncteur lim'", "exactitute", "exactitude",
    "misprint_in_print", None, "high", r"l'exactitude", r"l'exactitute",
    "Enlarged crop. The TeX silently corrected the misprint; the fix restores the printed reading.",
    corrected=r"l'exactitude")
add(131, "proof of (5.13.1): 'la famille croissante des φ_α(a_α), donc, si'", "comma after φ_α(a_α)", "semicolon",
    "punctuation", None, "high",
    r"$\varphi_\alpha(\mathfrak a_\alpha)$;¶donc,", r"$\varphi_\alpha(\mathfrak a_\alpha)$,¶donc,")
add(131, "proof of (5.13.1): 'l'existence d'un γ ≥ β tel que φ_γβ(φ_βα(x_α)) = φ_γβ(y_β), et par suite'",
    "inline formula φ_γβ(φ_βα(x_α)) = φ_γβ(y_β)", "displayed formula φ_γα(x_α) = φ_γβ(y_β)",
    "formula", None, "high",
    r"tel que¶\[¶\varphi_{\gamma\alpha}(x_\alpha)=\varphi_{\gamma\beta}(y_\beta),¶\]¶et par suite",
    r"tel que¶$\varphi_{\gamma\beta}(\varphi_{\beta\alpha}(x_\alpha))=\varphi_{\gamma\beta}(y_\beta)$,¶et par suite",
    "Two differences in one edit: the print sets the formula inline, and its left side is φ_γβ(φ_βα(x_α)) "
    "(the TeX had simplified it to φ_γα(x_α), equal by transitivity; not a misprint).")

# ---------------------------------------------------------------- p. 132
add(132, "Proposition (5.13.3), label (i)", "(i) upright", "\\item[(i)] (italic)",
    "convention", 6, "high", r"\item[(i)] Pour tout indice", r"\item[\textup{(i)}] Pour tout indice", "GLOBAL_ISSUES 16.")
add(132, "Proposition (5.13.3), label (ii)", "(ii) upright", "\\item[(ii)] (italic)",
    "convention", 6, "high", r"\item[(ii)] Si de plus", r"\item[\textup{(ii)}] Si de plus", "GLOBAL_ISSUES 16.")
add(132, "Proposition (5.13.3), label (iii)", "(iii) upright", "\\item[(iii)] (italic)",
    "convention", 6, "high", r"\item[(iii)] Si $A$", r"\item[\textup{(iii)}] Si $A$", "GLOBAL_ISSUES 16.")
add(132, "proof of (5.13.3) (ii): 'que les A_α — p_α forment'", "long dash (set difference, bar 40-41 px)", "minus sign",
    "convention", 7, "high", r"$A_\alpha-\mathfrak p_\alpha$ forment", r"$A_\alpha\setmin\mathfrak p_\alpha$ forment")
add(132, "proof of (5.13.3) (ii): 'dont A — p est la limite inductive'", "long dash (bar 38-40 px)", "minus sign",
    "convention", 7, "high", r"dont $A-\mathfrak p$ est", r"dont $A\setmin\mathfrak p$ est")
add(132, "proof of (5.13.3) (ii): '(où les homomorphismes de transition sont locaux)'", "'locaux' italic", "upright",
    "italics", None, "high", r"de transition sont locaux)", r"de transition sont \emph{locaux})")
add(132, "proof of (5.13.3) (ii): 'dont la limite inductive ψ : lim((A_α)_{p_α}) → A_p est un homomorphisme surjectif'",
    "inline formula, lim with double parentheses ((A_α)_{p_α})", "displayed formula, \\varinjlim (A_α)_{p_α} (single parentheses)",
    "formula", None, "high",
    r"inductive¶\[¶\psi:\varinjlim (A_\alpha)_{\mathfrak p_\alpha}¶\longrightarrow A_{\mathfrak p}¶\]¶est un",
    r"inductive¶$\psi:\varinjlim((A_\alpha)_{\mathfrak p_\alpha})¶\longrightarrow A_{\mathfrak p}$¶est un",
    "Two differences in one edit: inline in the print, and the print has the extra pair of parentheses.")
add(132, "proof of (5.13.3) (ii): 's_α ∈ A_α — p_α sont tels que'", "long dash (bar 40-41 px)", "minus sign",
    "convention", 7, "high", r"s_\alpha\in A_\alpha-\mathfrak p_\alpha$ sont", r"s_\alpha\in A_\alpha\setmin\mathfrak p_\alpha$ sont")
add(132, "proof of (5.13.3) (ii): 'il existe s' ∈ A — p'", "long dash (bar 40-42 px)", "minus sign",
    "convention", 7, "high", r"s'\in A-\mathfrak p$", r"s'\in A\setmin\mathfrak p$")
add(132, "proof of (5.13.3) (ii): 'avec s'_α ∈ A_α — p_α'", "long dash (bar 40 px)", "minus sign",
    "convention", 7, "high", r"s'_\alpha\in A_\alpha-\mathfrak p_\alpha$", r"s'_\alpha\in A_\alpha\setmin\mathfrak p_\alpha$")
add(132, "proof of (5.13.3) (ii): '= 0 dans (A_β)_{p_β}, et prouve donc'", "comma after (A_β)_{p_β}", "no comma",
    "punctuation", None, "high",
    r"$(A_\beta)_{\mathfrak p_\beta}$ et prouve", r"$(A_\beta)_{\mathfrak p_\beta}$, et prouve")
add(132, "proof of (5.13.3) (ii): 'de x_α/s_α dans lim((A_α)_{p_α}) est nulle'", "double parentheses ((A_α)_{p_α})",
    "single parentheses", "formula", None, "high",
    r"\varinjlim(A_\alpha)_{\mathfrak p_\alpha}$ est nulle", r"\varinjlim((A_\alpha)_{\mathfrak p_\alpha})$ est nulle")
add(132, "proof of (5.13.3) (iii): 'les éléments de A_α — p_α sont inversibles'", "long dash (bar 40 px)", "minus sign",
    "convention", 7, "high", r"$A_\alpha-\mathfrak p_\alpha$ sont inversibles", r"$A_\alpha\setmin\mathfrak p_\alpha$ sont inversibles")
add(132, "Corollaire (5.13.4): 'unibranches (resp. géométriquement unibranches)'", "'(resp.' upright", "italic",
    "convention", 6, "high", r"unibranches¶(resp.", r"unibranches¶\textup{(resp.}",
    "'(resp.' printed roman inside the italic statement.")
add(132, "Corollaire (5.13.4): '(0, 23.2.1)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 23.2.1)", r"\textup{(\textbf{0}, 23.2.1)}",
    "One edit for this finding and the next (convention 6): bold numeral and the upright reference together.")
add(132, "Corollaire (5.13.4): same reference '(0, 23.2.1)'", "upright reference", "italic", "convention", 6, "high",
    None, None, "Covered by the edit of the preceding finding (convention 2), which adds the \\textup.")
add(132, "Corollaire (5.13.4): 'A est unibranche (resp. géométriquement unibranche)'", "'(resp.' upright", "italic",
    "convention", 6, "high", r"unibranche¶(resp.", r"unibranche¶\textup{(resp.}",
    "'(resp.' printed roman inside the italic statement.")
add(132, "end of page: 'A' = lim A'_α s'identifie à' continues on p. 133 'un sous-anneau de K'",
    "no paragraph break", "blank line before \\oldpage[IV-2]{133}", "other", None, "high",
    r"s'identifie à¶¶", r"s'identifie à¶",
    BLANK + " Apply together with the p. 133 top-of-page entry (blank line after the marker).")

# ---------------------------------------------------------------- p. 133
add(133, "top of page: 'un sous-anneau de K, ...' continues the sentence of p. 132",
    "no paragraph break", "blank line after \\oldpage[IV-2]{133}", "other", None, "high",
    r"\oldpage[IV-2]{133}¶¶un sous-anneau", r"\oldpage[IV-2]{133}¶un sous-anneau",
    "Apply together with the p. 132 end-of-page entry (blank line before the marker).")
add(133, "proof of (5.13.4): 'une équation de dépendance intégrale z^n + Σ c_i z^{n-i} = 0, où les c_i ∈ A'",
    "formula in the running text", "displayed formula", "other", None, "high",
    r"intégrale¶\[¶z^n+\sum_{i=1}^{n}c_i z^{n-i}=0,¶\]¶où les",
    r"intégrale¶$z^n+\sum_{i=1}^{n}c_i z^{n-i}=0$,¶où les",
    "Display vs inline only; no connecting word lost (index position of Σ ignored).")
add(133, "proof of (5.13.4): 'on sait (0_III, 10.3.1.3)'", "bold 0", "plain 0", "convention", 2, "high",
    r"$(0_{\mathrm{III}}, 10.3.1.3)$", r"$(\mathbf{0}_{\mathrm{III}}, 10.3.1.3)$")
add(133, "(5.13.5): 'est un schéma normal,'", "'normal' italic", "upright (env body is roman)",
    "italics", None, "high", r"schéma normal,", r"schéma \emph{normal},")
add(133, "(5.13.5): 'A_p est intègre et intégralement clos.'", "'intègre et intégralement clos' italic", "upright",
    "italics", None, "high", r"est intègre et¶intégralement clos. On notera", r"est \emph{intègre et¶intégralement clos}. On notera")
add(133, "(5.13.5): 'que A est réduit et que'", "'réduit' italic", "upright",
    "italics", None, "high", r"est réduit et que", r"est \emph{réduit} et que")
add(133, "(5.13.5): 'ne peut contenir qu'un seul idéal premier minimal'", "'un seul' italic", "upright",
    "italics", None, "high", r"qu'un seul idéal", r"qu'\emph{un seul} idéal")
add(133, "(5.13.5): 'n'appartient qu'à une seule composante irréductible'", "'une seule' italic", "upright",
    "italics", None, "high", r"qu'à une seule composante", r"qu'à \emph{une seule} composante")
add(133, "(5.13.5): 'A/q est intégralement clos comme intersection'", "first 'intégralement clos' italic (the second upright)",
    "upright", "italics", None, "high", r"est intégralement clos comme", r"est \emph{intégralement clos} comme")
add(133, "(5.13.5): '(I, 8.2.1.1)'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 8.2.1.1)", r"(\textbf{I}, 8.2.1.1)")
add(133, "(5.13.5): 'Si A est noethérien et normal'", "'noethérien' and 'normal' italic", "upright",
    "italics", None, "high", r"est noethérien et normal,", r"est \emph{noethérien} et \emph{normal},")
add(133, "(5.13.5): '(I, 5.1.4)'", "bold I", "plain I", "convention", 2, "high",
    r"(I,¶5.1.4)", r"(\textbf{I},¶5.1.4)")
add(133, "Corollaire (5.13.6): 'Supposons que les A_β soient normaux'", "A_β", "A_α", "formula", None, "high",
    r"Supposons que les $A_\alpha$ soient normaux", r"Supposons que les $A_\beta$ soient normaux",
    "Enlarged crop: subscript β. Same meaning (bound index of the family), so not a misprint.")
add(133, "proof of (5.13.6): 'comme lim(B_α)_{p'_α} = lim(A_α)_{p_α} = A_p est un anneau local'",
    "formula in the running text", "displayed formula", "other", None, "high",
    r"comme¶\[¶\varinjlim(B_\alpha)_{\mathfrak p'_\alpha}¶=\varinjlim(A_\alpha)_{\mathfrak p_\alpha}=A_{\mathfrak p}¶\]¶est un anneau local",
    r"comme¶$\varinjlim(B_\alpha)_{\mathfrak p'_\alpha}¶=\varinjlim(A_\alpha)_{\mathfrak p_\alpha}=A_{\mathfrak p}$¶est un anneau local",
    "Display vs inline only; no connecting word lost.")
add(133, "proof of (5.13.7): 'A_p = lim((A_α)_{p_α}) par (5.13.3)'", "double parentheses ((A_α)_{p_α})",
    "single parentheses", "formula", None, "high",
    r"(A_\alpha)_{\mathfrak p_\alpha}$ par (5.13.3)", r"((A_\alpha)_{\mathfrak p_\alpha})$ par (5.13.3)",
    "Independent of the next (misprint) edit: the two 'old' strings do not overlap.")
add(133, "proof of (5.13.7): 'A_p = lim((A_α)_{p_α})': the lim has no arrow", "lim without the arrow (the lim just before, p = lim p_α, has it)",
    "\\varinjlim", "misprint_in_print", None, "high",
    r"$A_{\mathfrak p}=\varinjlim", r"$A_{\mathfrak p}=\lim",
    "Enlarged crop: nothing under this lim. The TeX silently corrected it; the fix restores the printed reading. "
    "The 'old' does not overlap the preceding parenthesis edit (either order works).",
    corrected=r"\varinjlim")
add(133, "proof of (5.13.7): '(0_I, 6.3.2)'", "bold 0", "plain 0", "convention", 2, "high",
    r"$(0_{\mathrm I}, 6.3.2)$", r"$(\mathbf{0}_{\mathrm I}, 6.3.2)$")
add(133, "proof of (5.13.7): 'sont en outre des anneaux locaux.'", "'locaux' italic", "upright",
    "italics", None, "high", r"des anneaux locaux. Pour", r"des anneaux \emph{locaux}. Pour")
add(133, "end of page: 'il existe i_0 tel que, pour i ≥ i_0,' continues on p. 134 'on ait Tor_i^A(M, N) = 0'",
    "no paragraph break", "blank line before \\oldpage[IV-2]{134}", "other", None, "high",
    r"pour $i\geq i_0$,¶¶", r"pour $i\geq i_0$,¶",
    BLANK + " Apply together with the p. 134 top-of-page entry (blank line after the marker).")

# ---------------------------------------------------------------- p. 134
add(134, "top of page: 'on ait Tor_i^A(M, N) = 0 ...' continues the sentence of p. 133",
    "no paragraph break", "blank line after \\oldpage[IV-2]{134}", "other", None, "high",
    r"\oldpage[IV-2]{134}¶¶on ait", r"\oldpage[IV-2]{134}¶on ait",
    "Apply together with the p. 133 end-of-page entry (blank line before the marker).")
add(134, "proof of (5.13.7): '(0, 17.3.1 et 17.2.6)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 17.3.1 et 17.2.6)", r"(\textbf{0}, 17.3.1 et 17.2.6)")
add(134, "proof of (5.13.7): 'A est un A_α-module plat (0_I, 6.1.2)'", "bold 0", "plain 0", "convention", 2, "high",
    r"$(0_{\mathrm I}, 6.1.2)$", r"$(\mathbf{0}_{\mathrm I}, 6.1.2)$")
add(134, "proof of (5.13.7): 'donc on a Tor_i^A(M, N) = Tor_i^{A_α}(M_α, N_α) ⊗_{A_α} A à un isomorphisme près'",
    "formula in the running text", "displayed formula", "other", None, "high",
    r"donc on a¶\[¶\operatorname{Tor}^A_i(M,N)¶=\operatorname{Tor}^{A_\alpha}_i(M_\alpha,N_\alpha)¶ \otimes_{A_\alpha}A¶\]¶à un",
    r"donc on a¶$\operatorname{Tor}^A_i(M,N)¶=\operatorname{Tor}^{A_\alpha}_i(M_\alpha,N_\alpha)¶ \otimes_{A_\alpha}A$¶à un",
    "Display vs inline only; no connecting word lost.")
add(134, "proof of (5.13.7): 'à un isomorphisme près (III, 6.3.9)'", "bold III", "plain III", "convention", 2, "high",
    r"(III, 6.3.9)", r"(\textbf{III}, 6.3.9)")
add(134, "proof of (5.13.8): 'Il résulte de (I, 2.4.2)'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 2.4.2)", r"(\textbf{I}, 2.4.2)")
add(134, "proof of (5.13.8): 'que le morphisme Spec(A_p) → Spec((A_α)_{p_α}) est un homéomorphisme surjectif'",
    "formula in the running text", "displayed formula", "other", None, "high",
    r"le morphisme¶\[¶\operatorname{Spec}(A_{\mathfrak p})¶\longrightarrow\operatorname{Spec}((A_\alpha)_{\mathfrak p_\alpha})¶\]¶est",
    r"le morphisme¶$\operatorname{Spec}(A_{\mathfrak p})¶\longrightarrow\operatorname{Spec}((A_\alpha)_{\mathfrak p_\alpha})$¶est",
    "Display vs inline only; no connecting word lost.")
add(134, "proof of (5.13.8): '(0_I, 6.3.2)'", "bold 0", "plain 0", "convention", 2, "high",
    r"$(0_{\mathrm I}, 6.3.2)$", r"$(\mathbf{0}_{\mathrm I}, 6.3.2)$")
add(134, "§ 6, introduction: 'f^{-1}(y) = X ×_Y Spec(k(y))'", "bold italic k", "plain k", "convention", 1, "high",
    r"\operatorname{Spec}(k(y))", r"\operatorname{Spec}(\boldsymbol{k}(y))")
add(134, "§ 6, introduction: 'et alors B ⊗_A k(y)'", "bold italic k", "plain k", "convention", 1, "high",
    r"B\otimes_A k(y)", r"B\otimes_A \boldsymbol{k}(y)")
add(134, "§ 6, introduction: 'sous l'hypothèse que le morphisme f est plat.'", "'plat' italic", "upright",
    "italics", None, "high", r"$f$ est plat. Les", r"$f$ est \emph{plat}. Les")
add(134, "§ 6, introduction: 'O_x ⊗_{O_y} k(y)'", "bold italic k", "plain k", "convention", 1, "high",
    r"\otimes_{\mathcal O_y}k(y)", r"\otimes_{\mathcal O_y}\boldsymbol{k}(y)")
add(134, "end of page: 'pour trouver des' continues on p. 135 'critères permettant ...'",
    "no paragraph break", "blank line before \\oldpage[IV-2]{135}", "other", None, "high",
    r"trouver¶des¶¶", r"trouver¶des¶",
    BLANK + " Apply together with removing the blank line AFTER \\oldpage[IV-2]{135} ('\\oldpage[IV-2]{135}' + blank line + "
    "'critères' -> no blank line), which lies in the p. 135 segment, outside pp. 130-134.")


# ---------------------------------------------------------------- checks
def page_text(p):
    return (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")


ok = True
for p in sorted({x["page"] for x in F}):
    orig = page_text(p)
    cur = orig
    for x in F:
        if x["page"] != p or not x["fix"]:
            continue
        o, n = x["fix"]["old"], x["fix"]["new"]
        c0, c1 = orig.count(o), cur.count(o)
        if c0 != 1 or c1 != 1:
            ok = False
            print("PROBLEM", p, repr(o[:60]), "orig", c0, "sequential", c1)
        cur = cur.replace(o, n, 1)
    # write the patched text for a visual check (scratch only)
    (HERE / f"patched_{p}.tex").write_text(cur, encoding="utf-8")

counts = {}
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    counts.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", OUT, len(F), "findings; all unique:", ok)
for p in sorted(counts):
    print(p, counts[p])
