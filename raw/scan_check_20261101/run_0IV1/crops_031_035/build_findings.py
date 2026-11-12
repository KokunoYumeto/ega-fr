"""Build findings_031_035.json for EGA IV-1 chapter 0, pp. 31-35, and check every fix.

Each fix's "old" must occur exactly once in its page_NNN.tex.
"""
import json
from pathlib import Path

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_0IV1")
OUT = RUN / "findings_031_035.json"

INLINE_NOTE = "Layout only (display vs inline); the formula itself matches."
DOTS_NOTE = "Baseline dots in the print (checked on a crop); the TeX has centred \\cdots."
NO_NOTE = "n with a raised o (n°); the TeX has plain 'no'. ega0-15/16/17 write no~ throughout (see final message)."


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": old, "new": new},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


findings = []

# ---------------------------------------------------------------- page 31
findings += [
    F(31, "(16.3.8), statement display 'codim(V(a), V(Ax_1+...+Ax_r)) = 0'",
      "baseline dots", r"\cdots", "symbol", None, "high",
      r"V(Ax_1+\cdots+Ax_r)", r"V(Ax_1+\ldots+Ax_r)", DOTS_NOTE),
    F(31, "proof of (16.3.8), first sentence: 'q_j (1<=i<=n) les idéaux premiers minimaux parmi ceux qui contiennent a'",
      "q_j (1⩽i⩽n): the range is written with i, not j (enlarged crop)",
      r"$\mathfrak{q}_j$ $(1\leq j\leq n)$", "misprint_in_print", None, "high",
      r"$\mathfrak{q}_j$ $(1\leq j\leq n)$", r"$\mathfrak{q}_j$ $(1\leq i\leq n)$",
      "Misprint: the index of q_j runs over j. The TeX silently corrects it; restore the printed i.",
      corrected=r"$\mathfrak{q}_j$ $(1\leq j\leq n)$"),
    F(31, "proof of (16.3.8): 'on a (14.2.1) codim(V(a), X) = inf_j(codim(V(q_j), X)) = inf_j(dim(A_q_j)) (16.1.3.2)'",
      "in the running text", r"displayed with \[ ... \]", "other", None, "high",
      "on a (14.2.1)\n\\[\n  \\operatorname{codim}(V(\\mathfrak{a}),X)\n  =\\inf_j(\\operatorname{codim}(V(\\mathfrak{q}_j),X))\n  =\\inf_j(\\dim(A_{\\mathfrak{q}_j}))\n\\]\n(16.1.3.2)",
      "on a (14.2.1)\n$\\operatorname{codim}(V(\\mathfrak{a}),X)=\\inf_j(\\operatorname{codim}(V(\\mathfrak{q}_j),X))=\\inf_j(\\dim(A_{\\mathfrak{q}_j}))$\n(16.1.3.2)",
      INLINE_NOTE + " Index position under inf left as is."),
    F(31, "proof of (16.3.8): '(Bourbaki, Alg. comm., chap. II, § 1, n° 1, prop. 2)'",
      "n° (raised o)", "no~1", "symbol", None, "high",
      r"no~1, prop.~2", r"n\textsuperscript{o}~1, prop.~2", NO_NOTE),
    F(31, "proof of (16.3.8): 'On a comme ci-dessus codim(V(a), V(Ax)) = inf_j(...) = inf_j(dim(A_q_j/A_q_j x)); mais'",
      "in the running text", r"displayed with \[ ... \]", "other", None, "high",
      "On a comme ci-dessus\n\\[\n  \\operatorname{codim}(V(\\mathfrak{a}),V(Ax))\n  =\\inf_j(\\dim((A/Ax)_{\\mathfrak{q}_j/Ax}))\n  =\\inf_j(\\dim(A_{\\mathfrak{q}_j}/A_{\\mathfrak{q}_j}x))~;\n\\]\nmais",
      "On a comme ci-dessus\n$\\operatorname{codim}(V(\\mathfrak{a}),V(Ax))=\\inf_j(\\dim((A/Ax)_{\\mathfrak{q}_j/Ax}))=\\inf_j(\\dim(A_{\\mathfrak{q}_j}/A_{\\mathfrak{q}_j}x))$~;\nmais",
      INLINE_NOTE),
    F(31, "proof of (16.3.8): 'aucun des idéaux premiers minimaux de A_q_j on a dim(...)'",
      "no comma after A_q_j (enlarged crop)", "comma before 'on a'", "punctuation", None, "high",
      r"$A_{\mathfrak{q}_j}$, on a", r"$A_{\mathfrak{q}_j}$ on a", "Comma added in the TeX."),
    F(31, "proof of (16.3.8): 'appartenant à a/Ax et tels que codim(V(a/Ax), V(A'x'_2+...+A'x'_r)) = 0. Soit'",
      "in the running text; baseline dots", r"displayed with \[ ... \]; \cdots", "other", None, "high",
      "et tels que\n\\[\n  \\operatorname{codim}(V(\\mathfrak{a}/Ax),\n  V(A'x'_2+\\cdots+A'x'_r))=0.\n\\]\nSoit",
      "et tels que\n$\\operatorname{codim}(V(\\mathfrak{a}/Ax),V(A'x'_2+\\ldots+A'x'_r))=0$.\nSoit",
      INLINE_NOTE + " The same edit also replaces \\cdots by \\ldots for the print's baseline dots (no separate finding)."),
    F(31, "proof of (16.3.8): 'il est immédiat que A/(Ax+Ax_2+...+Ax_s) est de longueur finie'",
      "baseline dots", r"\cdots", "symbol", None, "high",
      r"Ax_2+\cdots+Ax_s", r"Ax_2+\ldots+Ax_s", DOTS_NOTE),
    F(31, "proof of (16.3.9): 'jacent). D'autre part B/aB = B/(s_1B+...+s_mB)'",
      "no comma after 'part': only a tiny speck on the baseline, a word space after 'part', just before B (enlarged crop)",
      "D'autre part,", "punctuation", None, "medium",
      "D'autre part,", "D'autre part",
      "The mark is much smaller than the full stop in 'jacent).' and has no comma tail; read as a speck, not a comma."),
    F(31, "proof of (16.3.9): 'B/aB = B/(s_1B+...+s_mB)'",
      "baseline dots", r"\cdots", "symbol", None, "high",
      r"s_1B+\cdots+s_mB", r"s_1B+\ldots+s_mB", DOTS_NOTE),
    F(31, "proof of (16.3.9): display 'dim(B) <= m + dim(B⊗_A k)'",
      "no punctuation after the display (enlarged crop)", "comma at the end of the display", "punctuation", None, "high",
      r"\dim(B)\leq m+\dim(B\otimes_A k),", r"\dim(B)\leq m+\dim(B\otimes_A k)",
      "Comma added in the TeX."),
    F(31, "proof of (16.3.9), last line: 'est l'annulateur de M (resp. N)'",
      "bold M (wrong fount): much heavier than the N in the same line and than the M of (ii) (enlarged crop)",
      r"$M$", "misprint_in_print", None, "medium",
      r"l'annulateur de $M$", r"l'annulateur de $\mathbf{M}$",
      "Wrong-fount letter; the TeX silently corrects it. Reproduced in the diplomatic text, plain M in the corrected edition.",
      corrected=r"l'annulateur de $M$"),
]

# ---------------------------------------------------------------- page 32
findings += [
    F(32, "proof of (16.3.9): 'qui s'identifie (I, 9.1.13) à'",
      "bold I", "plain I", "convention", 2, "high",
      "(I, 9.1.13)", r"(\textbf{I}, 9.1.13)", "Bold chapter numeral in the reference (enlarged crop)."),
    F(32, "proof of (16.3.9): 'à Supp(M) ×_Spec(A) Supp(N) = Spec((B/s)⊗_A(A/r)) = Spec(B/(s+rB)). Comme'",
      "in the running text", r"displayed with \[ ... \]", "other", None, "high",
      "\\[\n  \\operatorname{Supp}(M)\\times_{\\operatorname{Spec}(A)}\\operatorname{Supp}(N)\n  =\\operatorname{Spec}((B/\\mathfrak{s})\\otimes_A(A/\\mathfrak{r}))\n  =\\operatorname{Spec}(B/(\\mathfrak{s}+\\mathfrak{r}B)).\n\\]\nComme",
      "$\\operatorname{Supp}(M)\\times_{\\operatorname{Spec}(A)}\\operatorname{Supp}(N)=\\operatorname{Spec}((B/\\mathfrak{s})\\otimes_A(A/\\mathfrak{r}))=\\operatorname{Spec}(B/(\\mathfrak{s}+\\mathfrak{r}B))$.\nComme",
      INLINE_NOTE),
    F(32, "proof of (16.3.9): display 'dim(B/(s+rB)) <= dim(A/r) + dim(B/(s+mB))'",
      "no punctuation after the display (enlarged crop)", "comma at the end of the display", "punctuation", None, "high",
      r"\dim(B/(\mathfrak{s}+\mathfrak{m}B)),", r"\dim(B/(\mathfrak{s}+\mathfrak{m}B))",
      "Comma added in the TeX."),
    F(32, "heading 16.4",
      "'16.4. Profondeur et coprofondeur (¹).' (full stop after the footnote mark)", "no full stop", "punctuation", None, "high",
      "général.}}", "général.}.}",
      "None of the 54 \\subsection titles in ega0-14 ... ega0-23 has the printed final full stop (see final message)."),
    F(32, "footnote to heading 16.4: 'Dans la 3^e partie du chap. III'",
      "3 with a superior e", "3e", "symbol", None, "high",
      "la 3e partie", r"la 3\textsuperscript{e} partie", "Enlarged crop."),
    F(32, "proof of (16.4.1), display 'N = M/(x_1M+...+x_{r-1}M);'",
      "baseline dots", r"\cdots", "symbol", None, "high",
      r"x_1M+\cdots+x_{r-1}M", r"x_1M+\ldots+x_{r-1}M", DOTS_NOTE),
    F(32, "proof of (16.4.1), display 'dim(M/(x_1M+...+x_rM)) = dim(M) - r;'",
      "baseline dots", r"\cdots", "symbol", None, "high",
      r"x_1M+\cdots+x_rM", r"x_1M+\ldots+x_rM", DOTS_NOTE),
    F(32, "Lemme (16.4.2): 'il faut et il suffit que l'on ait Hom_A(k, M/(x_1M+...+x_nM)) ≠ 0.'",
      "in the running text (end of the statement); baseline dots", r"displayed with \[ ... \]; \cdots", "other", None, "high",
      "que l'on ait\n\\[\n  \\operatorname{Hom}_A(k,M/(x_1M+\\cdots+x_nM))\\neq0.\n\\]\n\\end{lemma}",
      "que l'on ait\n$\\operatorname{Hom}_A(k,M/(x_1M+\\ldots+x_nM))\\neq0$.\n\\end{lemma}",
      INLINE_NOTE + " The same edit also replaces \\cdots by \\ldots (no separate finding)."),
    F(32, "proof of (16.4.2): 'dans N = M/(x_1M+...+x_nM) n'est injective'",
      "baseline dots", r"\cdots", "symbol", None, "high",
      r"$N=M/(x_1M+\cdots+x_nM)$", r"$N=M/(x_1M+\ldots+x_nM)$", DOTS_NOTE),
    F(32, "proof of (16.4.2): '(Bourbaki, Alg. comm., chap. IV, § 1, n° 1, cor. 2 de la prop. 2)'",
      "n° (raised o)", "no~1", "symbol", None, "high",
      r"no~1, cor.~2", r"n\textsuperscript{o}~1, cor.~2", NO_NOTE),
]

# ---------------------------------------------------------------- page 33
findings += [
    F(33, "proof of (16.4.2), first line: '(Bourbaki, Alg. comm., chap. II, § 1, n° 1, prop. 2)'",
      "n° (raised o)", "no~1", "symbol", None, "high",
      r"no~1, prop.~2", r"n\textsuperscript{o}~1, prop.~2", NO_NOTE),
    F(33, "Lemme (16.4.3): 'Alors les A-modules Hom_A(k, M/(x_1M+...+x_nM)) et Ext^n_A(k, M) sont isomorphes'",
      "in the running text; baseline dots", r"displayed with \[ ... \] and \quad\text{et}\quad; \cdots", "other", None, "high",
      "Alors les $A$-modules\n\\[\n  \\operatorname{Hom}_A(k,M/(x_1M+\\cdots+x_nM))\n  \\quad\\text{et}\\quad \\operatorname{Ext}^n_A(k,M)\n\\]\nsont isomorphes",
      "Alors les $A$-modules\n$\\operatorname{Hom}_A(k,M/(x_1M+\\ldots+x_nM))$ et $\\operatorname{Ext}^n_A(k,M)$\nsont isomorphes",
      INLINE_NOTE + " The same edit also replaces \\cdots by \\ldots (no separate finding)."),
    F(33, "proof of (16.4.3), display 'Hom_A(k, M/(x_1M+...+x_nM)) = Hom_A(k, N/(x_2N+...+x_nN))'",
      "baseline dots (twice)", r"\cdots (twice)", "symbol", None, "high",
      "M/(x_1M+\\cdots+x_nM))\n  =\\operatorname{Hom}_A(k,N/(x_2N+\\cdots+x_nN))",
      "M/(x_1M+\\ldots+x_nM))\n  =\\operatorname{Hom}_A(k,N/(x_2N+\\ldots+x_nN))",
      DOTS_NOTE),
    F(33, "proof of (16.4.3): 'En vertu de l'hypothèse de récurrence' after (16.4.3.1)",
      "new indented paragraph after the display (16.4.3.1)", "no blank line after \\end{equation}: same paragraph",
      "other", None, "high",
      "\\end{equation}\nEn vertu de l'hypothèse", "\\end{equation}\n\nEn vertu de l'hypothèse",
      "Paragraph break missing in the TeX."),
    F(33, "proof of (16.4.3), display 'Hom_A(k, M/(x_1M+...+x_{n-1}M)),'",
      "baseline dots", r"\cdots", "symbol", None, "high",
      r"x_1M+\cdots+x_{n-1}M", r"x_1M+\ldots+x_{n-1}M", DOTS_NOTE),
    F(33, "proof of (16.4.3): 'de l'homothétie de rapport x_1 dans tout A-module Ext^m_A(k, T)'",
      "Ext^m_A(k, T): superscript m (enlarged crop)", "Ext^n_A(k, T)", "formula", None, "high",
      r"$\operatorname{Ext}^n_A(k,T)$", r"$\operatorname{Ext}^m_A(k,T)$",
      "The print uses a free index m here ('tout A-module Ext^m'); the TeX changed it to n. Not a misprint: the sentence holds for every degree."),
    F(33, "Définition (16.4.5): 'On appelle profondeur de M'",
      "'profondeur' in italic like the rest of the statement (enlarged crop)",
      r"\emph{profondeur} inside the italic definition environment (comes out upright)",
      "convention", 6, "high",
      r"\emph{profondeur}", "profondeur",
      "Printed italic word left upright by \\emph inside \\itshape: drop \\emph."),
    F(33, "after Définition (16.4.5): 'On a donc prof(M) = +∞ si et seulement si M = 0, et, par (16.4.1)', (16.4.5.1), 'On a évidemment prof(M^k) = prof(M) pour tout k > 0.'",
      "the statement ends at 'formée d'éléments de m.'; the two sentences that follow are roman (also 'si' in (16.4.5.1)) and each starts a new indented paragraph",
      "both sentences and (16.4.5.1) inside the italic definition environment, no paragraph breaks",
      "other", None, "high",
      "$\\mathfrak{m}$. On a donc $\\operatorname{prof}(M)=+\\infty$ si et seulement si\n$M=0$, et, par (16.4.1)\n\\begin{equation}\n\\label{0.16.4.5.1-fr}\n\\tag{16.4.5.1}\n  \\operatorname{prof}(M)\\leq\\dim(M)\\quad\\text{si}\\quad M\\neq0.\n\\end{equation}\nOn a évidemment $\\operatorname{prof}(M^k)=\\operatorname{prof}(M)$ pour tout\n$k>0$.\n\\end{definition}",
      "$\\mathfrak{m}$.\n\\end{definition}\n\nOn a donc $\\operatorname{prof}(M)=+\\infty$ si et seulement si\n$M=0$, et, par (16.4.1)\n\\begin{equation}\n\\label{0.16.4.5.1-fr}\n\\tag{16.4.5.1}\n  \\operatorname{prof}(M)\\leq\\dim(M)\\quad\\text{si}\\quad M\\neq0.\n\\end{equation}\n\nOn a évidemment $\\operatorname{prof}(M^k)=\\operatorname{prof}(M)$ pour tout\n$k>0$.",
      "One edit: moves \\end{definition} to the end of the printed statement and adds the two paragraph breaks."),
    F(33, "Proposition (16.4.6)(i): '(ou encore qu'il existe un sous-module de M isomorphe au corps résiduel k = A/m de A)'",
      "the parenthesis is roman inside the italic statement (enlarged crop)",
      "inside the italic proposition environment (comes out italic)", "convention", 6, "high",
      "(ou encore qu'il existe un sous-module\n  de $M$ isomorphe au corps résiduel $k=A/\\mathfrak{m}$ de $A$)",
      "\\textup{(ou encore qu'il existe un sous-module\n  de $M$ isomorphe au corps résiduel $k=A/\\mathfrak{m}$ de $A$)}",
      "Roman words inside an italic statement."),
]

# ---------------------------------------------------------------- page 34
findings += [
    F(34, "proof of (16.4.6)(i): '(Bourbaki, Alg. comm., chap. IV, § 1, n° 1, cor. 2 de la prop. 2)'",
      "n° (raised o)", "no~1", "symbol", None, "high",
      "no~1,\ncor.~2", "n\\textsuperscript{o}~1,\ncor.~2", NO_NOTE),
    F(34, "proof of (16.4.6)(i): '(Bourbaki, Alg. comm., chap. II, § 1, n° 1, prop. 2)'",
      "n° (raised o)", "no~1", "symbol", None, "high",
      r"no~1, prop.~2", r"n\textsuperscript{o}~1, prop.~2", NO_NOTE),
    F(34, "proof of (16.4.6)(ii): 'est une suite (M/xM)-régulière maximale; d'où la conclusion.'",
      "semicolon before 'd'où' (enlarged crop)", "comma", "punctuation", None, "high",
      r"$(M/xM)$-régulière maximale, d'où", r"$(M/xM)$-régulière maximale~; d'où", ""),
    F(34, "proof of Lemme (16.4.6.3): 'Ass(M'') = Ass(M) — {p}'",
      "long dash for set difference (enlarged crop)", "minus sign", "convention", 7, "high",
      r"\operatorname{Ass}(M)-\{\mathfrak{p}\}", r"\operatorname{Ass}(M)\setmin\{\mathfrak{p}\}",
      "As in the other convention-7 fixes (\\setmin, to be redefined as the long dash)."),
    F(34, "proof of Lemme (16.4.6.3): '(Bourbaki, Alg. comm., chap. IV, § 1, n° 1, prop. 4)'",
      "n° (raised o)", "no~1", "symbol", None, "high",
      r"no~1, prop.~4", r"n\textsuperscript{o}~1, prop.~4", NO_NOTE),
    F(34, "proof of Lemme (16.4.6.3): '(loc. cit., § 1, n° 1, cor. 2 de la prop. 2)'",
      "n° (raised o)", "no~1", "symbol", None, "high",
      r"no~1, cor.~2", r"n\textsuperscript{o}~1, cor.~2", NO_NOTE),
    F(34, "proof of Lemme (16.4.6.3): '(loc. cit., § 1, n° 3, prop. 7)'",
      "n° (raised o)", "no~3", "symbol", None, "high",
      r"no~3, prop.~7", r"n\textsuperscript{o}~3, prop.~7", NO_NOTE),
    F(34, "proof of Lemme (16.4.6.3): 'M'/tM' = M'⊗_A(A/tA) (0_I, 1.7.5)'",
      "bold 0", "plain 0", "convention", 2, "high",
      r"($0_{\mathrm I}$, 1.7.5)", r"($\mathbf{0}_{\mathrm I}$, 1.7.5)", ""),
    F(34, "proof of Lemme (16.4.6.3): '(Bourbaki, loc. cit., § 1, n° 3, cor. 1 de la prop. 7)'",
      "n° (raised o)", "no~3", "symbol", None, "high",
      "no~3,\ncor.~1", "n\\textsuperscript{o}~3,\ncor.~1", NO_NOTE),
    F(34, "after the proof of Lemme (16.4.6.3): 'Ce lemme étant établi, revenons à la démonstration de (iii).'",
      "a new indented paragraph; no heading or bracketed title",
      "\\begin{proof}[Suite de la démonstration de (16.4.6)]: the preamble's proof environment takes no argument, so the bracketed words are typeset",
      "extra", None, "high",
      r"\begin{proof}[Suite de la démonstration de (16.4.6)]", r"\begin{proof}",
      "Removes the printed bracket text; the 'Démonstration. ---' heading left by the environment is the document-wide proof-heading item. Same construction 3 times in ega0-19 and twice in ega0-22 (see final message)."),
    F(34, "proof of (16.4.6)(iv): 'à un isomorphisme canonique près (0_I, 7.3.3)'",
      "bold 0", "plain 0", "convention", 2, "high",
      r"($0_{\mathrm I}$, 7.3.3)", r"($\mathbf{0}_{\mathrm I}$, 7.3.3)", ""),
    F(34, "proof of (16.4.6)(iv): 'on a des isomorphismes canoniques Ext^i_A(k, M)⊗_A Â ⥲ Ext^i_Â(k, M⊗_A Â) puisque'",
      "in the running text", r"displayed with \[ ... \]", "other", None, "high",
      "isomorphismes canoniques\n\\[\n  \\operatorname{Ext}^i_A(k,M)\\otimes_A\\widehat{A}\n  \\xrightarrow{\\sim}\n  \\operatorname{Ext}^i_{\\widehat{A}}\n  (k,M\\otimes_A\\widehat{A})\n\\]\npuisque",
      "isomorphismes canoniques\n$\\operatorname{Ext}^i_A(k,M)\\otimes_A\\widehat{A}\\xrightarrow{\\sim}\\operatorname{Ext}^i_{\\widehat{A}}(k,M\\otimes_A\\widehat{A})$\npuisque",
      INLINE_NOTE),
    F(34, "proof of (16.4.6)(iv): 'à un isomorphisme canonique près (0_III, 12.3.5)'",
      "bold 0", "plain 0", "convention", 2, "high",
      r"($0_{\mathrm{III}}$, 12.3.5)", r"($\mathbf{0}_{\mathrm{III}}$, 12.3.5)", ""),
    F(34, "proof of (16.4.6)(iv): 'un A-module fidèlement plat (0_I, 7.3.5)'",
      "bold 0", "plain 0", "convention", 2, "high",
      r"($0_{\mathrm I}$, 7.3.5)", r"($\mathbf{0}_{\mathrm I}$, 7.3.5)", ""),
    F(34, "(16.4.6.4): 'on peut avoir aussi bien prof(...) < prof_A(M) que ...'",
      "'aussi bien' italic (enlarged crop)", "roman (env is upright)", "italics", None, "high",
      "aussi bien", r"\emph{aussi bien}", ""),
]

# ---------------------------------------------------------------- page 35
findings += [
    F(35, "(16.4.6.4): 'les éléments de J sont annulés par ceux de m_0 — p_0'",
      "long dash for set difference (enlarged crop)", "minus sign", "convention", 7, "high",
      r"\mathfrak{m}_0-\mathfrak{p}_0", r"\mathfrak{m}_0\setmin\mathfrak{p}_0", ""),
    F(35, "(16.4.6.4), last line: 'prof(A_p) = prof(A_0)_p_0 ≥ 1 si p_0 ≠ 0'",
      "prof(A_0)_{p_0}: one pair of parentheses, the index p_0 outside (enlarged crop)",
      r"\operatorname{prof}((A_0)_{\mathfrak{p}_0})", "misprint_in_print", None, "medium",
      r"=\operatorname{prof}((A_0)_{\mathfrak{p}_0})\geq1", r"=\operatorname{prof}(A_0)_{\mathfrak{p}_0}\geq1",
      "The localization needs its own parentheses, as in '(A_0)_{p_0}' two lines earlier; the TeX silently supplies them. Medium only for the misprint classification: the print may be a deliberate abbreviation.",
      corrected=r"\operatorname{prof}((A_0)_{\mathfrak{p}_0})"),
    F(35, "proof of (16.4.7): 'est aussi idéal premier minimal, donc est le seul idéal premier de A'",
      "'donc est le seul' (enlarged crop)", "'donc c'est le seul'", "word", None, "high",
      "donc c'est le seul", "donc est le seul", "The TeX adds c'."),
    F(35, "proof of (16.4.8): 'en posant N = M/(ρ(x_1)M+...+ρ(x_n)M)'",
      "baseline dots", r"\cdots", "symbol", None, "high",
      r"\rho(x_1)M+\cdots+\rho(x_n)M", r"\rho(x_1)M+\ldots+\rho(x_n)M", DOTS_NOTE),
    F(35, "proof of (16.4.8): 'N_[ρ] = M_[ρ]/(x_1M_[ρ]+...+x_nM_[ρ])'",
      "baseline dots", r"\cdots", "symbol", None, "high",
      r"x_1M_{[\rho]}+\cdots+x_nM_{[\rho]}", r"x_1M_{[\rho]}+\ldots+x_nM_{[\rho]}", DOTS_NOTE),
    F(35, "proof of (16.4.8): 'et finalement un A-module de longueur finie.'",
      "'de longueur finie' italic", "roman", "italics", None, "high",
      "de longueur finie. D'autre part", r"\emph{de longueur finie}. D'autre part", ""),
    F(35, "proof of (16.4.8): 'P est aussi un sous-module du B-module M'",
      "'B-module' emphasized: B roman as always, 'module' italic (enlarged crop)", "roman", "italics", None, "high",
      "du\n$B$-module $M$, et", "du\n\\emph{$B$-module} $M$, et",
      "Emphasis on B-module (the print keeps math letters roman inside italics, as in 'A-module' of the italic statements)."),
    F(35, "Définition (16.4.9): 'Soient A un anneau local noethérien M un A-module de type fini.'",
      "no comma after 'noethérien' (enlarged crop)", "'noethérien, $M$'", "misprint_in_print", None, "high",
      "noethérien, $M$ un $A$-module de type fini. Si", "noethérien $M$ un $A$-module de type fini. Si",
      "Misprint: missing comma; the TeX silently corrects it.",
      corrected="noethérien, $M$ un $A$-module de type fini. Si"),
    F(35, "Définition (16.4.9): 'on appelle coprofondeur de M'",
      "'coprofondeur' in italic like the rest of the statement (enlarged crop)",
      r"\emph{coprofondeur} inside the italic definition environment (comes out upright)",
      "convention", 6, "high",
      r"\emph{coprofondeur}", "coprofondeur",
      "Printed italic word left upright by \\emph inside \\itshape: drop \\emph."),
    F(35, "after Définition (16.4.9): 'On a coprof(M^k) = coprof(M) pour tout k > 0.'",
      "roman, a new paragraph after the statement", "inside the italic definition environment (comes out italic)",
      "italics", None, "high",
      "$\\operatorname{coprof}(M)=0$.\n\nOn a $\\operatorname{coprof}(M^k)=\\operatorname{coprof}(M)$ pour tout $k>0$.\n\\end{definition}",
      "$\\operatorname{coprof}(M)=0$.\n\\end{definition}\n\nOn a $\\operatorname{coprof}(M^k)=\\operatorname{coprof}(M)$ pour tout $k>0$.",
      "One edit: moves \\end{definition} to the end of the printed statement (as for (16.4.5) on p. 33)."),
]

# ---------------------------------------------------------------- checks
ok = True
texts = {}
for f in findings:
    p = f["page"]
    if p not in texts:
        texts[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    fx = f["fix"]
    if fx is None:
        continue
    n = texts[p].count(fx["old"])
    if n != 1:
        ok = False
        print(f"PAGE {p}: old occurs {n} times: {fx['old']!r}")
    if fx["old"] == fx["new"]:
        ok = False
        print(f"PAGE {p}: old == new: {fx['old']!r}")

# overlapping olds on the same page
for p, t in texts.items():
    spans = []
    for f in findings:
        if f["page"] == p and f["fix"]:
            i = t.find(f["fix"]["old"])
            spans.append((i, i + len(f["fix"]["old"]), f["where"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            ok = False
            print(f"PAGE {p}: overlapping fixes:\n  {a[2]}\n  {b[2]}")

# counts per page
for p in sorted(texts):
    fs = [f for f in findings if f["page"] == p]
    conv = sum(f["kind"] == "convention" for f in fs)
    mis = sum(f["kind"] == "misprint_in_print" for f in fs)
    print(f"p. {p}: {len(fs) - conv - mis}/{conv}/{mis}")

if ok:
    OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT, len(findings), "findings")
else:
    print("NOT written")
