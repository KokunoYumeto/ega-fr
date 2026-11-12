# Builds findings_205_209.json for EGA IV-4 pp. 205-209 (checker helper; edits no .tex file).
# usage: python build_findings.py [--write]
import json
import pathlib
import sys

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
OUT = RUN / "findings_205_209.json"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None, fix=True):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=(dict(old=old, new=new) if fix else None))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


G88 = "GLOBAL_ISSUES 88."
G83 = "GLOBAL_ISSUES 83 (italics missing from the TeX)."

# ---------------------------------------------------------------- p. 205
add(205, "top of p. 205: page break 204/205 after the display (19.5.1.1)",
    "p. 205 begins 'La relation H_1(f, M)=0 implique donc' at the left margin (left edge 349 px, like the next lines): "
    "the paragraph continues after the display (19.5.1.1) that ends p. 204",
    "blank lines before and after \\oldpage[IV-4]{205}: a new indented paragraph",
    "marker", None, "high",
    "\\oldpage[IV-4]{205}\n\nLa relation", "\\oldpage[IV-4]{205}\nLa relation",
    "BOUNDARY FIX (page break with p. 204). The marker is at the right place. In the current source the blank line BEFORE "
    "the marker (after \\end{equation} of (19.5.1.1)) is already gone (p. 204 fixes); this edit removes the one after it "
    "(\\oldpage ends with \\ignorespaces, which does not skip a \\par).")
add(205, "l. 2-3: 'f_nH_1(f', M)=H_1(f', M) (III, 1.1.3.5)'", "bold III", "plain III",
    "convention", 2, "high", "(III, 1.1.3.5). Or, par", "(\\textbf{III}, 1.1.3.5). Or, par")
add(205, "l. 3: 'Or, par définition (III, 1.1.1)'", "bold III", "plain III",
    "convention", 2, "high", "(III, 1.1.1)", "(\\textbf{III}, 1.1.1)")
add(205, "l. 4: 'la filtration des M^j pour j≤n—1'",
    "long dash between n and 1 (crop p205_l4.png; the minus in the exponent of M^{n-1} is the short one)",
    "minus sign", "convention", 7, "high", "$j\\leq n-1$", "$j\\leq n\\setmin 1$",
    "Text-size subtraction printed with the long dash, as in the p. 182 fix 'n\\setmin 1'.")
add(205, "Corollaire (19.5.2), l. 1: 'que les f_i (1≤i≤n) appartiennent'",
    "parentheses around the formula upright (crop p205_cor1.png)", "italic parentheses (statement environment)",
    "convention", 6, "high", "que les $f_i$ ($1\\leq i\\leq n$) appartiennent",
    "que les $f_i$ \\textup{($1\\leq i\\leq n$)} appartiennent",
    "GLOBAL_ISSUES 26: parenthesised formula inside an italic statement.")
add(205, "Corollaire (19.5.2), end: 'les quatre conditions a), b), b′), c) de (19.5.1) sont équivalentes'",
    "labels a), b), b′), c) and the reference (19.5.1) upright (crop p205_cor2.png)",
    "$a)$, $b)$, $b')$, $c)$: italic letters; (19.5.1) italic",
    "convention", 6, "high", "conditions $a)$, $b)$, $b')$, $c)$ de (19.5.1) sont",
    "conditions \\textup{a), b), b$'$), c)} de \\textup{(19.5.1)} sont", G88)
add(205, "after Corollaire (19.5.2): 'On sait en effet alors (0_I, 7.3.5)'",
    "bold 0 with a light subscript I (crop p205_0I.png)", "plain 0",
    "convention", 2, "high", "alors ($0_{\\mathrm I}$, 7.3.5) que tout", "alors ($\\mathbf{0}_{\\mathrm I}$, 7.3.5) que tout")
add(205, "Proposition (19.5.3), item a)", "label a) upright", "\\item[a)] italic inside the italic statement",
    "convention", 6, "high", "\\item[a)] La suite $\\mathbf f$ est $M''$", "\\item[\\textup{a)}] La suite $\\mathbf f$ est $M''$")
add(205, "Proposition (19.5.3), item b)", "label b) upright", "\\item[b)] italic",
    "convention", 6, "high", "\\item[b)] La filtration", "\\item[\\textup{b)}] La filtration")
add(205, "Proposition (19.5.3), item c)", "label c) upright", "\\item[c)] italic",
    "convention", 6, "high", "\\item[c)] L'homomorphisme canonique $M'", "\\item[\\textup{c)}] L'homomorphisme canonique $M'")
add(205, "Proposition (19.5.3) b): '(autrement dit, l'homomorphisme canonique gr•_J(M') → gr•_J(M) est injectif).'",
    "the parenthesis is roman, with 'injectif' italic; both parentheses upright (crop p205_items.png)",
    "all italic (statement environment)",
    "convention", 6, "high",
    "(autrement dit, l'homomorphisme canonique $\\operatorname{gr}_{\\mathfrak J}^*(M')\\to\\operatorname{gr}_{\\mathfrak J}^*(M)$ est injectif).",
    "\\textup{(autrement dit, l'homomorphisme canonique $\\operatorname{gr}_{\\mathfrak J}^*(M')\\to\\operatorname{gr}_{\\mathfrak J}^*(M)$ est \\emph{injectif})}.",
    "Apply THIS one before the next finding (gr^\\bullet): its 'old' contains the next one's 'old', which this edit leaves unchanged inside \\textup.")
add(205, "Proposition (19.5.3) b): 'gr•_J(M') → gr•_J(M)'", "gr with a raised bullet (twice)", "^*",
    "symbol", None, "high",
    "canonique $\\operatorname{gr}_{\\mathfrak J}^*(M')\\to\\operatorname{gr}_{\\mathfrak J}^*(M)$ est",
    "canonique $\\operatorname{gr}_{\\mathfrak J}^\\bullet(M')\\to\\operatorname{gr}_{\\mathfrak J}^\\bullet(M)$ est",
    "GLOBAL_ISSUES 60. Apply after the previous finding; this 'old' occurs exactly once before and after it.")
add(205, "Proposition (19.5.3): 'Alors on a les implications' after item c)",
    "new indented paragraph (left edge 469 px; the margin is 358 px)",
    "text right after \\end{enumerate}: no indent",
    "other", None, "high", "f_iM)$ est injectif.\n\\end{enumerate}\nAlors on a",
    "f_iM)$ est injectif.\n\\end{enumerate}\n\nAlors on a",
    "GLOBAL_ISSUES 80 pattern.")
add(205, "Proposition (19.5.3): 'Alors on a les implications a)⇒b)⇒c), et a) entraîne'",
    "labels upright (crop p205_alors.png)", "$a)\\Rightarrow b)\\Rightarrow c)$, $a)$: italic letters",
    "convention", 6, "high",
    "les implications $a)\\Rightarrow b)\\Rightarrow c)$, et $a)$ entraîne",
    "les implications \\textup{a)}$\\Rightarrow$\\textup{b)}$\\Rightarrow$\\textup{c)}, et \\textup{a)} entraîne", G88)
add(205, "Proposition (19.5.3): '... est M′-régulière. | Si tout quotient d'un sous-module de M″'",
    "'Si tout quotient' begins a new indented paragraph (left edge 469 px; the line before is full)",
    "same paragraph", "other", None, "high",
    "est $M'$-régulière. Si tout quotient", "est $M'$-régulière.\n\nSi tout quotient", "")
add(205, "Proposition (19.5.3), end: 'les conditions a), b) et c) sont équivalentes'",
    "labels upright", "$a)$, $b)$, $c)$: italic letters",
    "convention", 6, "high", "$-préadique, les conditions $a)$, $b)$ et $c)$ sont équivalentes.",
    "$-préadique, les conditions \\textup{a)}, \\textup{b)} et \\textup{c)} sont équivalentes.", G88)
add(205, "proof of (19.5.3), l. 1-2: 'c) est conséquence de b) ... c) entraîne a) :'",
    "labels wholly italic, parentheses included (crop p205_proof1.png)", "italic letters, upright parentheses",
    "italics", None, "high",
    "Il est clair que $c)$ est conséquence de $b)$. Prouvons que sous les hypothèses de la dernière assertion, $c)$ entraîne $a)$:",
    "Il est clair que \\emph{c)} est conséquence de \\emph{b)}. Prouvons que sous les hypothèses de la dernière assertion, \\emph{c)} entraîne \\emph{a)}:",
    G88)
add(205, "proof of (19.5.3): 'Or, la condition c) exprime'", "label wholly italic", "italic letter, upright parenthesis",
    "italics", None, "high", "la condition $c)$ exprime", "la condition \\emph{c)} exprime", G88)
add(205, "proof of (19.5.3): 'est injectif (III, 1.1.3.5); elle'", "bold III", "plain III",
    "convention", 2, "high", "(III, 1.1.3.5); elle", "(\\textbf{III}, 1.1.3.5); elle")
add(205, "proof of (19.5.3): 'Montrons ensuite que a) entraîne c)'", "labels wholly italic", "italic letters, upright parentheses",
    "italics", None, "high", "Montrons ensuite que $a)$ entraîne $c)$ et", "Montrons ensuite que \\emph{a)} entraîne \\emph{c)} et", G88)
add(205, "proof of (19.5.3): 'la propriété c) n'est autre'", "label wholly italic", "italic letter, upright parenthesis",
    "italics", None, "high", "la propriété $c)$ n'est autre", "la propriété \\emph{c)} n'est autre", G88)
add(205, "end of p. 205: page break 205/206 inside 'l'hypothèse de récurrence montre que | si l'on pose'",
    "p. 206 begins mid-sentence 'si l'on pose f′=(f_1, ..., f_{n-1})' at the left margin",
    "blank line before \\oldpage[IV-4]{206}", "marker", None, "high",
    "récurrence montre que\n\n", "récurrence montre que\n",
    "The marker is at the right place. Part 1 of 2: the first p. 206 finding removes the blank line after \\oldpage[IV-4]{206}; apply both (\\oldpage ends with \\ignorespaces, which does not skip a \\par).")

# ---------------------------------------------------------------- p. 206
add(206, "top of p. 206: 'si l'on pose' (mid-sentence page break)", "continues the sentence of p. 205 at the left margin",
    "blank line after \\oldpage[IV-4]{206}", "marker", None, "high",
    "\\oldpage[IV-4]{206}\n\nsi l'on pose", "\\oldpage[IV-4]{206}\nsi l'on pose",
    "Part 2 of 2 with the last p. 205 finding; apply both.")
add(206, "l. 1: 'en vertu de c) appliqué à f′'", "label wholly italic (crop p206_top.png)", "italic letter, upright parenthesis",
    "italics", None, "high", "en vertu de $c)$ appliqué", "en vertu de \\emph{c)} appliqué", G88)
add(206, "'est exacte, d'où c).'", "label wholly italic (crop p206_mid.png)", "italic letter, upright parenthesis",
    "italics", None, "high", "est exacte, d'où $c)$.", "est exacte, d'où \\emph{c)}.", G88)
add(206, "'Montrons enfin que a) entraîne b).'", "labels wholly italic", "italic letters, upright parentheses",
    "italics", None, "high", "Montrons enfin que $a)$ entraîne $b)$.", "Montrons enfin que \\emph{a)} entraîne \\emph{b)}.", G88)
add(206, "display of the isomorphisms gr•_J(M′) ⥲ gr⁰_J(M′)[T_1, ..., T_n], gr•_J(M) ⥲ gr⁰_J(M)[T_1, ..., T_n]",
    "gr with a raised bullet (crop p206_iso.png)", "^* (twice)", "symbol", None, "high",
    "\\operatorname{gr}_{\\mathfrak J}^*(M')\\xrightarrow{\\sim}\\operatorname{gr}_{\\mathfrak J}^0(M')[T_1,\\ldots,T_n],\n  \\qquad\n  \\operatorname{gr}_{\\mathfrak J}^*(M)\\xrightarrow{\\sim}",
    "\\operatorname{gr}_{\\mathfrak J}^\\bullet(M')\\xrightarrow{\\sim}\\operatorname{gr}_{\\mathfrak J}^0(M')[T_1,\\ldots,T_n],\n  \\qquad\n  \\operatorname{gr}_{\\mathfrak J}^\\bullet(M)\\xrightarrow{\\sim}",
    "GLOBAL_ISSUES 60.")
add(206, "after the display: '(0, 15.1.7), et comme on a vu'", "bold 0", "plain 0",
    "convention", 2, "high", "($0$, 15.1.7), et comme", "(\\textbf{0}, 15.1.7), et comme")
add(206, "'il en est de même de gr•_J(M′) → gr•_J(M).'", "gr with a raised bullet", "^* (twice)", "symbol", None, "high",
    "de même de $\\operatorname{gr}_{\\mathfrak J}^*(M')\\to\\operatorname{gr}_{\\mathfrak J}^*(M)$",
    "de même de $\\operatorname{gr}_{\\mathfrak J}^\\bullet(M')\\to\\operatorname{gr}_{\\mathfrak J}^\\bullet(M)$", "GLOBAL_ISSUES 60.")
add(206, "'l'équivalence des conditions a), b), c) de (19.5.3)'", "labels wholly italic (crop p206_onnotera.png)",
    "italic letters, upright parentheses", "italics", None, "high",
    "l'équivalence des conditions $a)$, $b)$, $c)$ de", "l'équivalence des conditions \\emph{a)}, \\emph{b)}, \\emph{c)} de", G88)
add(206, "'lorsque A est noethérien, M″ un A-module de type fini et que les f_i appartiennent au radical de A.'",
    "'est noethérien' and 'un A-module de type fini et que les f_i appartiennent au radical de' italic; "
    "'en particulier lorsque' roman (crop p206_onnotera.png)", "roman", "italics", None, "high",
    "lorsque $A$ est noethérien, $M''$ un $A$-module de type fini et que les $f_i$ appartiennent au radical de $A$.",
    "lorsque $A$ \\emph{est noethérien}, $M''$ \\emph{un $A$-module de type fini et que les $f_i$ appartiennent au radical de} $A$.",
    G83)
add(206, "(19.5.4): 'Rappelons (0, 15.1.5)'", "bold 0", "plain 0",
    "convention", 2, "high", "Rappelons ($0$, 15.1.5) que", "Rappelons (\\textbf{0}, 15.1.5) que")
add(206, "(19.5.4), display M′_k = M_k + 𝔍M_{k-1} + ... + 𝔍^{k-1}M_1 + 𝔍^kM_0",
    "baseline dots: measured, the dots (rows 402-409) rest on the baseline (408), below the bar of the + (397-399)",
    "\\cdots (centred)", "symbol", None, "high",
    "M_k'=M_k+\\mathfrak JM_{k-1}+\\cdots+", "M_k'=M_k+\\mathfrak JM_{k-1}+\\ldots+", "")
add(206, "(19.5.4): 'de degré 0 (0, 15.1.5.2)'", "bold 0", "plain 0",
    "convention", 2, "high", "de degré $0$ ($0$, 15.1.5.2)", "de degré $0$ (\\textbf{0}, 15.1.5.2)")
add(206, "(19.5.4), display ψ_M : (gr•(M)⊗_A(A/𝔍))[T_1, ..., T_n] → gr′•(M)",
    "no full stop after the display (crop p206_psi.png)", "full stop after gr′•(M)", "punctuation", None, "high",
    "\\operatorname{gr}_\\bullet'(M).\n\\]", "\\operatorname{gr}_\\bullet'(M)\n\\]", "")
add(206, "(19.5.4): 'l'homomorphisme canonique surjectif (0, 15.1.1.1)'", "bold 0", "plain 0",
    "convention", 2, "high", "surjectif ($0$, 15.1.1.1)", "surjectif (\\textbf{0}, 15.1.1.1)")
add(206, "(19.5.4), display φ_{gr•(M)} : ... → gr•_J(gr•(M))", "gr_J with a raised bullet", "^*", "symbol", None, "high",
    "\\longrightarrow\\operatorname{gr}_{\\mathfrak J}^*(\\operatorname{gr}_\\bullet(M))",
    "\\longrightarrow\\operatorname{gr}_{\\mathfrak J}^\\bullet(\\operatorname{gr}_\\bullet(M))",
    "GLOBAL_ISSUES 60. Shares text with the next finding; either order works (each leaves the other's 'old' intact).")
add(206, "(19.5.4), display φ_{gr•(M)}", "no full stop after the display (crop p206_phi.png)", "full stop", "punctuation", None, "high",
    "(\\operatorname{gr}_\\bullet(M)).\n\\]", "(\\operatorname{gr}_\\bullet(M))\n\\]", "")
add(206, "Théorème (19.5.5), l. 1: 'Avec les notations de (19.5.4),'", "reference upright (crop p206_thm.png)",
    "italic (statement environment)", "convention", 6, "high",
    "Avec les notations de (19.5.4), considérons", "Avec les notations de \\textup{(19.5.4)}, considérons", "")
add(206, "Théorème (19.5.5), item a)", "label upright", "\\item[a)] italic", "convention", 6, "high",
    "\\item[a)] La suite $\\mathbf f$ est $\\operatorname{gr}_\\bullet(M)$",
    "\\item[\\textup{a)}] La suite $\\mathbf f$ est $\\operatorname{gr}_\\bullet(M)$")
add(206, "Théorème (19.5.5), item b)", "label upright", "\\item[b)] italic", "convention", 6, "high",
    "\\item[b)] L'homomorphisme canonique $\\psi_M$", "\\item[\\textup{b)}] L'homomorphisme canonique $\\psi_M$")
add(206, "Théorème (19.5.5), item c)", "label upright", "\\item[c)] italic", "convention", 6, "high",
    "\\item[c)] L'homomorphisme canonique $\\varphi", "\\item[\\textup{c)}] L'homomorphisme canonique $\\varphi")
add(206, "Théorème (19.5.5) c): '(autrement dit (0, 15.1.7), la suite f est gr•(M)-quasi-régulière).'",
    "the parenthesis is roman except '-quasi-régulière' (italic); parentheses upright (crop p206_thm.png)",
    "all italic", "convention", 6, "high",
    "est bijectif (autrement dit ($0$, 15.1.7), la suite $\\mathbf f$ est $\\operatorname{gr}_\\bullet(M)$-quasi-régulière).",
    "est bijectif \\textup{(autrement dit ($0$, 15.1.7), la suite $\\mathbf f$ est $\\operatorname{gr}_\\bullet(M)$\\emph{-quasi-régulière})}.",
    "Apply THIS one before the next finding (bold 0): its 'old' contains the next one's 'old', which this edit leaves unchanged inside \\textup.")
add(206, "Théorème (19.5.5) c): '(autrement dit (0, 15.1.7)'", "bold 0", "plain 0",
    "convention", 2, "high", "dit ($0$, 15.1.7)", "dit (\\textbf{0}, 15.1.7)",
    "Apply after the previous finding; this 'old' occurs exactly once before and after it.")

# ---------------------------------------------------------------- p. 207
add(207, "Théorème (19.5.5), display 'a) ⇒ b) ⇒ c).'", "labels upright (crop p207_top.png)", "italic letters (math)",
    "convention", 6, "high",
    "  a)\\Rightarrow b)\\Rightarrow c).\n", "  \\textup{a)}\\Rightarrow\\textup{b)}\\Rightarrow\\textup{c)}.\n", G88)
add(207, "Théorème (19.5.5): '(ce qui est le cas lorsque A est noethérien, ... de type fini)'",
    "the whole parenthesis roman, parentheses upright (crop p207_top.png)", "italic", "convention", 6, "high",
    "(ce qui est le cas lorsque $A$ est noethérien, que les $f_i$ sont dans le radical de $A$ et que les $\\operatorname{gr}_k(M)$ sont des $A$-modules de type fini)",
    "\\textup{(ce qui est le cas lorsque $A$ est noethérien, que les $f_i$ sont dans le radical de $A$ et que les $\\operatorname{gr}_k(M)$ sont des $A$-modules de type fini)}",
    "")
add(207, "Théorème (19.5.5), end: 'alors les conditions a), b) et c) sont équivalentes'", "labels upright",
    "italic letters", "convention", 6, "high",
    "alors les conditions $a)$, $b)$ et $c)$ sont équivalentes.",
    "alors les conditions \\textup{a)}, \\textup{b)} et \\textup{c)} sont équivalentes.", G88)
add(207, "footnote (1): 'L'implication b)⇒c), sans hypothèse de séparation'", "labels wholly italic (crop p207_fn.png)",
    "italic letters, upright parentheses", "italics", None, "high",
    "L'implication $b)\\Rightarrow c)$, sans", "L'implication \\emph{b)}$\\Rightarrow$\\emph{c)}, sans", G88)
add(207, "proof of (19.5.5), l. 1: 'L'implication a)⇒b) a été démontrée'", "labels wholly italic (crop p207_proof.png)",
    "italic letters, upright parentheses", "italics", None, "high",
    "L'implication $a)\\Rightarrow b)$ a été", "L'implication \\emph{a)}$\\Rightarrow$\\emph{b)} a été", G88)
add(207, "proof of (19.5.5), l. 1: 'dans (0, 15.1.8)'", "bold 0", "plain 0", "convention", 2, "high",
    "dans ($0$, 15.1.8)", "dans (\\textbf{0}, 15.1.8)")
add(207, "proof of (19.5.5), l. 1: 'l'implication c)⇒a) sous l'hypothèse'", "labels wholly italic",
    "italic letters, upright parentheses", "italics", None, "high",
    "l'implication $c)\\Rightarrow a)$ sous", "l'implication \\emph{c)}$\\Rightarrow$\\emph{a)} sous", G88)
add(207, "proof of (19.5.5), l. 2: 'un cas particulier de (0, 15.1.9)'", "bold 0", "plain 0", "convention", 2, "high",
    "particulier de ($0$, 15.1.9)", "particulier de (\\textbf{0}, 15.1.9)")
add(207, "proof of (19.5.5), l. 3: 'que b) implique c)'", "labels wholly italic", "italic letters, upright parentheses",
    "italics", None, "high", "que $b)$ implique $c)$, ce qui", "que \\emph{b)} implique \\emph{c)}, ce qui", G88)
add(207, "'f^q = f_1^{q_1}f_2^{q_2}...f_n^{q_n}.'", "baseline dots (crop p207_fq.png)", "\\cdots (centred)",
    "symbol", None, "high", "f_2^{q_2}\\cdots f_n^{q_n}", "f_2^{q_2}\\ldots f_n^{q_n}", "")
add(207, "(19.5.5.1), statement 'Pour que l'application ψ_M soit injective ... la condition suivante soit vérifiée :'",
    "the whole statement italic, '(et par suite bijective)' with italic parentheses (crop p207_19551.png)",
    "roman (env environment)", "italics", None, "high",
    "Pour que l'application $\\psi_M$ soit injective (et par suite bijective), il faut et il suffit que pour $p\\geq0$ et $q\\geq0$ la condition suivante soit vérifiée:",
    "\\emph{Pour que l'application $\\psi_M$ soit injective (et par suite bijective), il faut et il suffit que pour $p\\geq0$ et $q\\geq0$ la condition suivante soit vérifiée:}",
    G83)
add(207, "(19.5.5.1), condition (I_{q,p}): 'Pour toute famille (x^p_q)_{|q|=q} d'éléments de M_p, la relation'",
    "italic (crop p207_19551.png)", "roman", "italics", None, "high",
    "$(\\mathrm I_{q,p})$ Pour toute famille $(x_{\\mathbf q}^p)_{|\\mathbf q|=q}$ d'éléments de $M_p$, la relation",
    "$(\\mathrm I_{q,p})$ \\emph{Pour toute famille $(x_{\\mathbf q}^p)_{|\\mathbf q|=q}$ d'éléments de $M_p$, la relation}",
    G83)
add(207, "(I_{q,p}), display: 'Σ f^q x^p_q ∈ Σ_{i=1}^q 𝔍^{q-i}M_{p-i} + M′_{p+q+1}'",
    "M_{p−i}, with a minus sign (crop p207_disp1.png)", "M_{p+i} (silent correction)",
    "misprint_in_print", None, "high",
    "\\mathfrak J^{q-i}M_{p+i}+M_{p+q+1}'", "\\mathfrak J^{q-i}M_{p-i}+M_{p+q+1}'",
    "The TeX silently corrects. Correct reading M_{p+i}: by (19.5.5.1) itself (Q′_k)_{i+1} is the image of "
    "Σ_{h=0}^{k-i-1} 𝔍^{k-i-h-1}M_{i+h+1} (= Σ_{i′=1}^{q} 𝔍^{q-i′}M_{p+i′} for i=p, k-i=q), and (A_{q,p}), "
    "(19.5.5.5) and the proof of (19.5.5.4) use M_{p+i}. Not in the IV-4 errata list (Liste 3).",
    corrected="\\mathfrak J^{q-i}M_{p+i}+M_{p+q+1}'")
add(207, "(I_{q,p}), after the display: 'implique x^p_q ∈ M_{p+1}+𝔍M_p pour tout q tel que |q|=q.'",
    "italic (crop p207_impl.png)", "roman", "italics", None, "high",
    "M_{p+q+1}'\n\\]\nimplique $x_{\\mathbf q}^p\\in M_{p+1}+\\mathfrak JM_p$ pour tout $\\mathbf q$ tel que $|\\mathbf q|=q$.",
    "M_{p+q+1}'\n\\]\n\\emph{implique $x_{\\mathbf q}^p\\in M_{p+1}+\\mathfrak JM_p$ pour tout $\\mathbf q$ tel que $|\\mathbf q|=q$.}",
    G83 + " Shares 'M_{p+q+1}′' with the misprint finding above; the two apply in either order.")
add(207, "(19.5.5.1), proof: 'On procède comme dans (0, 15.1.6)'", "bold 0", "plain 0", "convention", 2, "high",
    "comme dans ($0$, 15.1.6)", "comme dans (\\textbf{0}, 15.1.6)")
add(207, "(19.5.5.1), proof: 'membre de (0, 15.1.5.2)'", "bold 0", "plain 0", "convention", 2, "high",
    "membre de ($0$, 15.1.5.2)", "membre de (\\textbf{0}, 15.1.5.2)")
add(207, "(19.5.5.1), display (Q_k)_i = Σ_{j≤k-i}(Σ_{|j|=j}(gr_{k-j}(M)⊗_A(A/𝔍))T^j)",
    "multi-index bold upright j (|j| = j) and bold T in T^j (crop p207_Qk.png)",
    "multi-index renamed l (|\\mathbf l|=j, T^{\\mathbf l}), light T",
    "formula", None, "high",
    "\\sum_{|\\mathbf l|=j}(\\operatorname{gr}_{k-j}(M)\\otimes_A(A/\\mathfrak J))T^{\\mathbf l}",
    "\\sum_{|\\mathbf j|=j}(\\operatorname{gr}_{k-j}(M)\\otimes_A(A/\\mathfrak J))\\mathbf T^{\\mathbf j}",
    "Renamed variable (GLOBAL_ISSUES 102 pattern); bold T^j as bold f^q.")
add(207, "(19.5.5.1), display gr_i(Q_k) = Σ_{|j|=k-i}((M_i/M_{i+1})⊗_A(A/𝔍))T^j = Σ_{|j|=k-i}(M_i/(𝔍M_i+M_{i+1}))T^j;",
    "bold j and bold T, twice (crop p207_grQ.png)", "\\mathbf l and light T", "formula", None, "high",
    "\\sum_{|\\mathbf l|=k-i}((M_i/M_{i+1})\\otimes_A(A/\\mathfrak J))T^{\\mathbf l}\n  =\\sum_{|\\mathbf l|=k-i}(M_i/(\\mathfrak JM_i+M_{i+1}))T^{\\mathbf l}",
    "\\sum_{|\\mathbf j|=k-i}((M_i/M_{i+1})\\otimes_A(A/\\mathfrak J))\\mathbf T^{\\mathbf j}\n  =\\sum_{|\\mathbf j|=k-i}(M_i/(\\mathfrak JM_i+M_{i+1}))\\mathbf T^{\\mathbf j}",
    "As the previous finding.")
add(207, "after the display gr_i(Q_k) = ...; : 'd'autre part, (Q′_k)_{i+1} est l'image de'",
    "printed p. 207 continues without a paragraph break: 'd'autre part' at the left margin, on p. 207 (the page ends "
    "with the display Σ f^q x^p_q ∈ M_{p+1}+𝔍^{q+1}M_p in the proof of (19.5.5.2), crops of p. 207 strips 3-4)",
    "blank line, then \\oldpage[IV-4]{208} and another blank line before 'd'autre part'",
    "marker", None, "high",
    ";\n\\]\n\n", ";\n\\]\n",
    "MARKER 208 STANDS NINE PRINTED LINES TOO EARLY (printed p. 207 runs on to the display at the end of the first "
    "paragraph of the proof of (19.5.5.2)). Part 1 of 3 (apply in this order): this removes the blank line before "
    "the old marker; part 2 (first p. 208 finding) inserts the marker before 'pour une famille'; part 3 (later p. 208 "
    "finding, listed after the edits of the text printed on p. 207) removes the old marker and the blank line after it.")

# ---------------------------------------------------------------- p. 208 segment (text up to the new marker is printed on p. 207)
add(208, "page break 207/208 inside 'une relation [display Σ f^q x^p_q ∈ M_{p+1}+𝔍^{q+1}M_p] | pour une famille (x^p_q)'",
    "printed p. 208 begins 'pour une famille (x^p_q)_{|q|=q} d'éléments de M_p entraîne' at the left margin; "
    "printed p. 207 ends with that display (above the footnote)",
    "\\oldpage[IV-4]{208} stands before 'd'autre part, (Q′_k)_{i+1}'", "marker", None, "high",
    "+\\mathfrak J^{q+1}M_p\n\\]\npour une famille",
    "+\\mathfrak J^{q+1}M_p\n\\]\n\\oldpage[IV-4]{208}\npour une famille",
    "Part 2 of 3 of the marker move (mid-sentence: no blank lines). Until part 3 is applied the file has two "
    "\\oldpage[IV-4]{208} (apply_fixes.py treats the span as page 208).")
add(208, "(19.5.5.2), statement 'Pour que la suite f soit gr•(M)-quasi-régulière, ... soit vérifiée :' (printed on p. 207)",
    "the whole statement italic except gr•(M) (crop p207_19552.png)", "roman (env)", "italics", None, "high",
    "Pour que la suite $\\mathbf f$ soit $\\operatorname{gr}_\\bullet(M)$-quasi-régulière, il suffit que, pour $p\\geq0$ et $q\\geq0$, la condition suivante soit vérifiée:",
    "\\emph{Pour que la suite $\\mathbf f$ soit $\\operatorname{gr}_\\bullet(M)$-quasi-régulière, il suffit que, pour $p\\geq0$ et $q\\geq0$, la condition suivante soit vérifiée:}",
    G83 + " Printed on p. 207; the text lies before the new marker 208, so apply this before part 3 of the marker move.")
add(208, "condition (S_{q,p}) (printed on p. 207): 'Pour toute famille ... la relation Σ_{|q|=q} f^q x^p_q ∈ M_{p+1} implique x^p_q ∈ M_{p+1}+𝔍M_p pour tout q tel que |q|=q.'",
    "italic; the relation Σ f^q x^p_q ∈ M_{p+1} is set in the line, at the end of the first line (crop p207_19552.png)",
    "roman; the relation displayed", "italics", None, "high",
    "$(\\mathrm S_{q,p})$ Pour toute famille $(x_{\\mathbf q}^p)_{|\\mathbf q|=q}$ d'éléments de $M_p$, la relation\n\\[\n  \\sum_{|\\mathbf q|=q}\\mathbf f^{\\mathbf q}x_{\\mathbf q}^p\\in M_{p+1}\n\\]\nimplique $x_{\\mathbf q}^p\\in M_{p+1}+\\mathfrak JM_p$ pour tout $\\mathbf q$ tel que $|\\mathbf q|=q$.",
    "$(\\mathrm S_{q,p})$ \\emph{Pour toute famille $(x_{\\mathbf q}^p)_{|\\mathbf q|=q}$ d'éléments de $M_p$, la relation $\\sum_{|\\mathbf q|=q}\\mathbf f^{\\mathbf q}x_{\\mathbf q}^p\\in M_{p+1}$ implique $x_{\\mathbf q}^p\\in M_{p+1}+\\mathfrak JM_p$ pour tout $\\mathbf q$ tel que $|\\mathbf q|=q$.}",
    G83 + " One edit for the italics and the formula set inline (no connecting word lost or added). Printed on p. 207: apply before part 3 of the marker move.")
add(208, "old position of \\oldpage[IV-4]{208} (before 'd'autre part, (Q′_k)_{i+1}', printed on p. 207)",
    "no page break there", "\\oldpage[IV-4]{208} with a blank line after it", "marker", None, "high",
    "\\oldpage[IV-4]{208}\n\nd'autre part,", "d'autre part,",
    "Part 3 of 3 of the marker move: apply after the two edits above (the new marker is then in place).")
add(208, "l. 3: 'Σ f^q(x^p_q — y^p_q) ∈ M_{p+1}'", "long dash (crop p208_l3.png)", "minus sign",
    "convention", 7, "high",
    "\\mathbf f^{\\mathbf q}(x_{\\mathbf q}^p-y_{\\mathbf q}^p)", "\\mathbf f^{\\mathbf q}(x_{\\mathbf q}^p\\setmin y_{\\mathbf q}^p)", "")
add(208, "l. 4: 'entraîne alors x^p_q — y^p_q ∈ M_{p+1}+𝔍M_p'", "long dash, longer than the + (crop p208_l4.png)",
    "minus sign", "convention", 7, "high",
    "alors $x_{\\mathbf q}^p-y_{\\mathbf q}^p\\in", "alors $x_{\\mathbf q}^p\\setmin y_{\\mathbf q}^p\\in", "")
add(208, "(19.5.5.3), statement 'Pour tout r≥0, si les conditions (I_{q,p}) ... pour p+q<r.'",
    "italic (crop p208_19553.png)", "roman (env)", "italics", None, "high",
    "Pour tout $r\\geq0$, si les conditions $(\\mathrm I_{q,p})$ sont vérifiées pour $p+q<r$, alors les conditions $(\\mathrm S_{q,p})$ sont vérifiées pour $p+q<r$.",
    "\\emph{Pour tout $r\\geq0$, si les conditions $(\\mathrm I_{q,p})$ sont vérifiées pour $p+q<r$, alors les conditions $(\\mathrm S_{q,p})$ sont vérifiées pour $p+q<r$.}",
    G83)
add(208, "condition (A_{q,p}): 'Pour toute famille ... la relation Σ f^q x^p_q ∈ M_{p+1} implique Σ f^q x^p_q ∈ Σ_{i=1}^q 𝔍^{q-i}M_{p+i}.'",
    "italic; both relations set in the line (the first at the end of l. 1, the second after 'implique' on l. 2; crop p208_A.png)",
    "roman; both relations displayed", "italics", None, "high",
    "$(\\mathrm A_{q,p})$ Pour toute famille $(x_{\\mathbf q}^p)_{|\\mathbf q|=q}$ d'éléments de $M_p$, la relation\n\\[\n  \\sum_{|\\mathbf q|=q}\\mathbf f^{\\mathbf q}x_{\\mathbf q}^p\\in M_{p+1}\n\\]\nimplique\n\\[\n  \\sum_{|\\mathbf q|=q}\\mathbf f^{\\mathbf q}x_{\\mathbf q}^p\\in\\sum_{i=1}^q\\mathfrak J^{q-i}M_{p+i}.\n\\]",
    "$(\\mathrm A_{q,p})$ \\emph{Pour toute famille $(x_{\\mathbf q}^p)_{|\\mathbf q|=q}$ d'éléments de $M_p$, la relation $\\sum_{|\\mathbf q|=q}\\mathbf f^{\\mathbf q}x_{\\mathbf q}^p\\in M_{p+1}$ implique $\\sum_{|\\mathbf q|=q}\\mathbf f^{\\mathbf q}x_{\\mathbf q}^p\\in\\sum_{i=1}^q\\mathfrak J^{q-i}M_{p+i}$.}",
    G83 + " One edit for the italics and the two formulas set inline (no connecting word lost or added).")
add(208, "(19.5.5.4), statement 'Quels que soient p≥0 et q≥1, ... (I_{0,p+q}).'", "italic (crop p208_19554.png)",
    "roman (env)", "italics", None, "high",
    "Quels que soient $p\\geq0$ et $q\\geq1$, la condition $(\\mathrm A_{q+1,p})$ est entraînée par la conjonction des conditions $(\\mathrm A_{q,p})$, $(\\mathrm I_{q-1,p+1})$, $(\\mathrm I_{q-2,p+2})$, $\\ldots$, $(\\mathrm I_{0,p+q})$.",
    "\\emph{Quels que soient $p\\geq0$ et $q\\geq1$, la condition $(\\mathrm A_{q+1,p})$ est entraînée par la conjonction des conditions $(\\mathrm A_{q,p})$, $(\\mathrm I_{q-1,p+1})$, $(\\mathrm I_{q-2,p+2})$, $\\ldots$, $(\\mathrm I_{0,p+q})$.}",
    G83)
add(208, "'pour 1≤q<r—p'", "long dash (crop p208_rp.png)", "minus sign", "convention", 7, "high",
    "$1\\leq q<r-p$", "$1\\leq q<r\\setmin p$", "")
add(208, "'Notons que la condition (A_{q,p}) équivaut aussi à' + display (19.5.5.5)",
    "(19.5.5.5) is the bold number of the display, on the same line as 𝔍^qM_p∩M_{p+1} ⊂ Σ 𝔍^{q-i}M_{p+i}. "
    "(crop p208_19555.png); the sentence runs on into the display",
    "\\end{env} after 'équivaut aussi à', then \\begin{env}[19.5.5.5] (number set as a heading on its own line) and the display",
    "other", None, "high",
    "équivaut aussi à\n\\end{env}\n\n\\begin{env}[19.5.5.5]\n\\label{IV.19.5.5.5}\n\\[\n  \\mathfrak J^qM_p\\cap M_{p+1}\\subset\\sum_{i=1}^q\\mathfrak J^{q-i}M_{p+i}.\n\\]",
    "équivaut aussi à\n\\begin{equation}\n  \\mathfrak J^qM_p\\cap M_{p+1}\\subset\\sum_{i=1}^q\\mathfrak J^{q-i}M_{p+i}.\n  \\tag{19.5.5.5}\\label{IV.19.5.5.5}\n\\end{equation}",
    "GLOBAL_ISSUES 64 pattern (equation number set as an env heading), same form as (18.3.6.4) on 0_IV p. 62. "
    "Removes one \\end{env} and one \\begin{env}: the \\end{env} after 'terminé la démonstration de (19.5.5).' (p. 209) "
    "then closes (19.5.5.4). The label keeps its name and now carries the tag (not referenced elsewhere).")
add(208, "'Supposons que, pour 1≤i<j (j≥1), on ait prouvé que' after the display m = Σ(...).",
    "new indented paragraph (left edge 523 px; margin 407 px)", "no blank line after \\]: no indent",
    "other", None, "high", "\\]\nSupposons que, pour", "\\]\n\nSupposons que, pour", "GLOBAL_ISSUES 47 pattern.")
add(208, "display 'y^{p+i}_q ∈ 𝔍M_{p+i}+M_{p+i+1}   (pour |q|=q—i).'",
    "long dash in q—i, longer than the + of the same display (crop p208_qi.png)", "minus sign",
    "convention", 7, "high", "(\\text{pour }|\\mathbf q|=q-i)", "(\\text{pour }|\\mathbf q|=q\\setmin i)", "")
add(208, "display 'm — Σ_{i<j}(Σ f^q y^{p+i}_q) ∈ M′_{p+q+1},'", "long dash after m (crop p208_msum.png)", "minus sign",
    "convention", 7, "high", "m-\\sum_{i<j}", "m\\setmin\\sum_{i<j}", "")
add(208, "end of the display 'm — Σ_{i<j}(...) ∈ M′_{p+q+1},' before the new paragraph 'Puisque par hypothèse'",
    "comma after M′_{p+q+1} (crop p208_comma.png), then a new indented paragraph beginning with a capital",
    "full stop (silent correction)", "misprint_in_print", None, "high",
    "M_{p+q+1}'.", "M_{p+q+1}',",
    "The TeX silently corrects the printed comma to a full stop; the sentence ends there and 'Puisque' begins a new "
    "paragraph. Adjacent to (not overlapping) the next finding.", corrected="M_{p+q+1}'.")
add(208, "'Puisque par hypothèse (I_{q-j,p+j}) est vérifiée, on en déduit'", "new indented paragraph (left edge 526 px; margin 411 px)",
    "no blank line after \\]: no indent", "other", None, "high",
    "\\]\nPuisque par hypothèse", "\\]\n\nPuisque par hypothèse", "GLOBAL_ISSUES 47 pattern.")
add(208, "end of p. 208: page break 208/209 after the display y^{p+j}_q ∈ 𝔍M_{p+j}+M_{p+j+1}",
    "p. 209 begins mid-sentence 'et, par récurrence sur j,' at the left margin", "blank line before \\oldpage[IV-4]{209}",
    "marker", None, "high", "+M_{p+j+1}\n\\]\n\n", "+M_{p+j+1}\n\\]\n",
    "The marker is at the right place. Part 1 of 2: the first p. 209 finding removes the blank line after \\oldpage[IV-4]{209}; apply both.")

# ---------------------------------------------------------------- p. 209
add(209, "top of p. 209: 'et, par récurrence sur j' (mid-sentence page break)", "continues at the left margin",
    "blank line after \\oldpage[IV-4]{209}", "marker", None, "high",
    "\\oldpage[IV-4]{209}\n\net, par récurrence", "\\oldpage[IV-4]{209}\net, par récurrence",
    "Part 2 of 2 with the last p. 208 finding; apply both.")
add(209, "l. 1: 'vérifiée pour tout j tel que'", "'tout' italic (crop p209_top.png)", "roman", "italics", None, "high",
    "pour tout $j$ tel que", "pour \\emph{tout} $j$ tel que", G83)
add(209, "Remarques (19.5.6) (ii): 'l'hypothèse de séparation de (0, 15.1.9)'", "bold 0", "plain 0",
    "convention", 2, "high", "séparation de ($0$, 15.1.9)", "séparation de (\\textbf{0}, 15.1.9)")
add(209, "Remarques (19.5.6) (ii): 'l'implication c)⇒a) dans (19.5.1)'", "labels wholly italic (crop p209_rem.png)",
    "italic letters, upright parentheses", "italics", None, "high",
    "l'implication $c)\\Rightarrow a)$ dans", "l'implication \\emph{c)}$\\Rightarrow$\\emph{a)} dans",
    G88 + " Judged with the remark body roman (document-wide remark item).")
add(209, "Remarques (19.5.6) (iii): 'l'implication c)⇒b) n'est plus valable'", "labels wholly italic",
    "italic letters, upright parentheses", "italics", None, "high",
    "l'implication $c)\\Rightarrow b)$ n'est", "l'implication \\emph{c)}$\\Rightarrow$\\emph{b)} n'est",
    G88 + " Judged with the remark body roman.")
add(209, "Remarques (19.5.6) (iii): '(0, 15.1.12, (iii))'", "bold 0", "plain 0", "convention", 2, "high",
    "($0$, 15.1.12, (iii))", "(\\textbf{0}, 15.1.12, (iii))")
add(209, "(19.6.1), heading: '(19.6.1). Soient A un anneau'",
    "bold full stop after the number (crop p209_1961.png); (19.4.1), (19.5.4) and (19.6.2) have none",
    "no stop (the env prints only '(19.6.1)'): silent correction", "misprint_in_print", None, "medium",
    "\\begin{env}[19.6.1]\n", "\\begin{env}[19.6.1]\\unskip\\textbf{.}\\ %\n",
    "Stray stop after the paragraph number. The \\unskip removes the space the env puts after the number, so the bold "
    "stop follows the parenthesis; the % keeps the line structure without an extra space (test compile: "
    "'(19.6.1). Soient'). Corrected reading: no stop, as the TeX has now.",
    corrected="\\begin{env}[19.6.1]\n")
add(209, "(19.6.1), l. 2: '𝔍 = f_1A + ... + f_nA'",
    "baseline dots: measured, the dots (rows 87-93) rest on the baseline (92-93), below the bar of the + (82-84)",
    "\\cdots (centred)", "symbol", None, "high", "\\mathfrak J=f_1A+\\cdots+f_nA$ l'idéal qu'elle",
    "\\mathfrak J=f_1A+\\ldots+f_nA$ l'idéal qu'elle", "")
add(209, "(19.6.1), display N′_k = N_k + 𝔍N_{k-1} + ... + 𝔍^{k-1}N_1 + 𝔍^kN_0", "baseline dots (rows 497-502, baseline 500)",
    "\\cdots", "symbol", None, "high", "+\\mathfrak JN_{k-1}+\\cdots+", "+\\mathfrak JN_{k-1}+\\ldots+", "")
add(209, "(19.6.1): 'M′_k = p(N′_k) = M_k + 𝔍M_{k-1} + ... + 𝔍^{k-1}M_1 + 𝔍^kM_0'", "baseline dots (rows 578-583, as in the line above)",
    "\\cdots", "symbol", None, "high", "=p(N_k')=M_k+\\mathfrak JM_{k-1}+\\cdots+", "=p(N_k')=M_k+\\mathfrak JM_{k-1}+\\ldots+", "")
add(209, "diagram (19.6.1.1), bottom row: labels gr′(j), gr′(p)", "labels BELOW the arrows (crop p209_diag.png)",
    "\\ar[r]^-{...}: labels above", "other", None, "high",
    "\\ar[r]^-{\\operatorname{gr}'(j)} & \\operatorname{gr}_\\bullet'(N) \\ar[r]^-{\\operatorname{gr}'(p)}",
    "\\ar[r]_-{\\operatorname{gr}'(j)} & \\operatorname{gr}_\\bullet'(N) \\ar[r]_-{\\operatorname{gr}'(p)}", "")
add(209, "end of p. 209: page break 209/210 after the diagram (19.6.1.1)",
    "p. 210 begins 'où les flèches verticales sont les homomorphismes canoniques' at the left margin (continuation)",
    "blank line before \\oldpage[IV-4]{210}", "marker", None, "high",
    "\\label{IV.19.6.1.1}\n\\end{equation}\n\n", "\\label{IV.19.6.1.1}\n\\end{equation}\n",
    "The marker is at the right place. Part 1 of 2: the blank line after \\oldpage[IV-4]{210} (p. 210 segment, next batch) must go too.")


def norm(s):
    return s.replace("\r\n", "\n")


def check_pages():
    ok = True
    pages = {p: norm((RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8")) for p in range(205, 210)}
    for i, x in enumerate(F):
        if x["fix"] is None:
            continue
        c = pages[x["page"]].count(x["fix"]["old"])
        if c != 1:
            ok = False
            print("PAGE COUNT", c, i, x["page"], repr(x["fix"]["old"][:80]))
    return ok


if __name__ == "__main__":
    ok = check_pages()
    print("findings:", len(F), "page check ok" if ok else "PAGE CHECK FAILED")
    from collections import Counter
    cnt = Counter()
    for x in F:
        k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
        cnt[(x["page"], k)] += 1
    for p in range(205, 210):
        print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
    if "--write" in sys.argv and ok:
        OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("written", OUT)
