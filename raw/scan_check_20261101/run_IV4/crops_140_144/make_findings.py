"""Build findings_140_144.json (pages 140-144 of EGA IV-4, ega4-18-fr.tex)."""
import json
import pathlib

OUT = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4\findings_140_144.json")
NL = "\n"


def F(page, where, scan, tex, kind, conv, old, new, note="", conf="high", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=(None if old is None else dict(old=old, new=new)))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []
# ---------------------------------------------------------------- page 140
L.append(F(140, "(i) of the proof of (18.6.9): 'sont injectifs en vertu de (0_I, 6.5.1)'",
           "bold 0 with subscript I", "plain 0", "convention", 2,
           r"en vertu de ($0_{\mathrm I}$, 6.5.1)", r"en vertu de ($\mathbf{0}_{\mathrm I}$, 6.5.1)"))
L.append(F(140, "Corollaire (18.6.10), label 'a)'",
           "upright a) (crop p140_s4_items.png)", r"\item[$a)$] (italic a, upright parenthesis)",
           "convention", 6, r"\item[$a)$] être un anneau", r"\item[\textup{a)}] être un anneau",
           "GLOBAL_ISSUES 16/88."))
L.append(F(140, "Corollaire (18.6.10) a): 'être un anneau de Cohen-Macaulay (0, 16.5.3);'",
           "reference set upright inside the italic statement: upright parentheses and figures, bold 0 (crop p140_s4_items.png)",
           "italic (statement environment)", "convention", 6,
           r"Cohen-Macaulay (0, 16.5.3);", r"Cohen-Macaulay \textup{(0, 16.5.3)};",
           "Same spot as the next finding (bold 0): apply THIS one first; its 'old' contains the next one's 'old', which this edit leaves unchanged."))
L.append(F(140, "Corollaire (18.6.10) a): '(0, 16.5.3)'",
           "bare bold 0 (no subscript)", "plain 0", "convention", 2,
           r"(0, 16.5.3)", r"(\textbf{0}, 16.5.3)",
           "Apply after the previous finding (\\textup around the same reference)."))
L.append(F(140, "Corollaire (18.6.10), label 'b)'",
           "upright b) (crop p140_s4_items.png)", r"\item[$b)$]",
           "convention", 6, r"\item[$b)$] vérifier", r"\item[\textup{b)}] vérifier"))
L.append(F(140, "Corollaire (18.6.10) b): 'vérifier la propriété (S_n) (5.7.3);'",
           "reference upright (crop p140_s4_items.png)", "italic", "convention", 6,
           r"$(S_n)$ (5.7.3);", r"$(S_n)$ \textup{(5.7.3)};"))
L.append(F(140, "Corollaire (18.6.10), label 'c)'",
           "upright c) (crop p140_s4_items.png)", r"\item[$c)$]",
           "convention", 6, r"\item[$c)$] être régulier", r"\item[\textup{c)}] être régulier"))
L.append(F(140, "Corollaire (18.6.10), label 'd)'",
           "upright d) (crop p140_s4_items.png)", r"\item[$d)$]",
           "convention", 6, r"\item[$d)$] vérifier", r"\item[\textup{d)}] vérifier"))
L.append(F(140, "Corollaire (18.6.10) d): 'vérifier la propriété (R_n) (5.8.2);'",
           "reference upright (crop p140_s4_items.png)", "italic", "convention", 6,
           r"$(R_n)$ (5.8.2);", r"$(R_n)$ \textup{(5.8.2)};"))
# ---------------------------------------------------------------- page 141
L.append(F(141, "Proposition (18.6.12), label 'a)'",
           "upright a) (crop p141_s1_a.png)", r"\item[$a)$]",
           "convention", 6, r"\item[$a)$] $A$ est", r"\item[\textup{a)}] $A$ est",
           "GLOBAL_ISSUES 16/88. Adjacent to (not overlapping) the next finding."))
L.append(F(141, "Proposition (18.6.12) a): 'A est unibranche (0, 23.2.1) (resp. réduit et unibranche).'",
           "'(0, 23.2.1) (resp.' upright, 'réduit et unibranche' italic, closing parenthesis upright (crops p141_s1_a.png, p141_s1_unibr.png)",
           "all italic", "convention", 6,
           r"unibranche (0, 23.2.1) (resp. réduit et unibranché).",
           r"unibranche \textup{(0, 23.2.1) (resp.} réduit et unibranché\textup{)}.",
           "Apply THIS one first: its 'old' contains the 'old' of the next two findings (bold 0; the accent of 'unibranché'), which this edit leaves unchanged."))
L.append(F(141, "Proposition (18.6.12) a): '(0, 23.2.1)'",
           "bare bold 0", "plain 0", "convention", 2,
           r"(0, 23.2.1)", r"(\textbf{0}, 23.2.1)",
           "Apply after the previous finding (\\textup around the same spot)."))
L.append(F(141, "Proposition (18.6.12) a): '(resp. réduit et unibranche)'",
           "'unibranche', no accent (crop p141_s1_unibr.png)", "'unibranché'", "word", None,
           r"unibranché", r"unibranche",
           "The TeX adds an accent; the print has the adjective 'unibranche', as earlier in the same line and in (18.6.13). Apply after the convention-6 finding above (its 'old' contains this word)."))
L.append(F(141, "Proposition (18.6.12), label 'b)'",
           "upright b) (crop p141_s1_bc.png)", r"\item[$b)$]",
           "convention", 6, r"\item[$b)$] Pour toute", r"\item[\textup{b)}] Pour toute"))
L.append(F(141, "Proposition (18.6.12) b): 'Spec(A′) est irréductible (resp. intègre).'",
           "'(resp.' and the closing parenthesis upright, 'intègre' italic (crop p141_s1_bc2.png)",
           "all italic", "convention", 6,
           r"$\Spec(A')$ est irréductible (resp. intègre).",
           r"$\Spec(A')$ est irréductible \textup{(resp.} intègre\textup{)}."))
L.append(F(141, "Proposition (18.6.12), label 'c)'",
           "upright c) (crop p141_s1_bc2.png)", r"\item[$c)$]",
           "convention", 6, r"\item[$c)$] $\Spec", r"\item[\textup{c)}] $\Spec",
           "Adjacent to (not overlapping) the next finding."))
L.append(F(141, "Proposition (18.6.12) c): 'Spec(ʰA) est irréductible (resp. intègre).'",
           "'(resp.' and the closing parenthesis upright, 'intègre' italic (crop p141_s1_bc2.png)",
           "all italic", "convention", 6,
           r"{}^h\!A)$ est irréductible (resp. intègre).",
           r"{}^h\!A)$ est irréductible \textup{(resp.} intègre\textup{)}."))
L.append(F(141, "proof of (18.6.12): 'le cas où A est réduit, donc aussi A′ (17.5.7)'",
           "'réduit' italic (crop p141_s2_reduit.png)", "upright", "italics", None,
           r"le cas où $A$ est réduit, donc aussi", r"le cas où $A$ est \emph{réduit}, donc aussi"))
L.append(F(141, "proof of (18.6.12): 'la condition b) signifie que tous les A_α sont intègres'",
           "b) italic with italic parenthesis", r"$b)$", "italics", None,
           r"la condition $b)$ signifie", r"la condition \emph{b)} signifie",
           "Labels in roman text are italic in the print (GLOBAL_ISSUES 88)."))
L.append(F(141, "proof of (18.6.12): 'donc b) entraîne c).'",
           "labels italic", r"$b)$, $c)$", "italics", None,
           r"donc $b)$ entraîne $c)$.", r"donc \emph{b)} entraîne \emph{c)}.",
           "Two labels, one edit."))
L.append(F(141, "proof of (18.6.12): 'Il est clair que ... donc c) entraîne b).'",
           "labels italic (crop p141_s2_montrons.png)", r"$c)$, $b)$", "italics", None,
           r"donc $c)$ entraîne $b)$", r"donc \emph{c)} entraîne \emph{b)}",
           "Adjacent to (not overlapping) the next finding."))
L.append(F(141, "proof of (18.6.12): '... donc c) entraîne b). Montrons que c) entraîne a).'",
           "'Montrons' begins a line at the left margin, without indent: the sentence continues the paragraph 'Il est clair que ...' (crop p141_s2_montrons.png)",
           "blank line before 'Montrons': a paragraph break the print does not have", "other", None,
           "." + NL + NL + "Montrons", "." + NL + "Montrons",
           "Adjacent to (not overlapping) the findings before and after it."))
L.append(F(141, "proof of (18.6.12): 'Montrons que c) entraîne a).'",
           "labels italic (crop p141_s2_montrons.png)", r"$c)$, $a)$", "italics", None,
           r"$c)$ entraîne $a)$. Notons", r"\emph{c)} entraîne \emph{a)}. Notons"))
L.append(F(141, "proof of (18.6.12): 'Prouvons enfin que a) implique c).'",
           "labels italic", r"$a)$, $c)$", "italics", None,
           r"Prouvons enfin que $a)$ implique $c)$.", r"Prouvons enfin que \emph{a)} implique \emph{c)}."))
L.append(F(141, "Proposition (18.6.14), label '(i)'",
           "upright (i)", r"\item[(i)] (italic)", "convention", 6,
           r"\item[(i)] Toute limite", r"\item[\textup{(i)}] Toute limite", "GLOBAL_ISSUES 16."))
L.append(F(141, "Proposition (18.6.14), label '(ii)'",
           "upright (ii)", r"\item[(ii)] (italic)", "convention", 6,
           r"\item[(ii)] Le foncteur", r"\item[\textup{(ii)}] Le foncteur", "GLOBAL_ISSUES 16."))
L.append(F(141, "Proposition (18.6.14), label '(iii)'",
           "upright (iii)", r"\item[(iii)] (italic)", "convention", 6,
           r"\item[(iii)] Tout anneau", r"\item[\textup{(iii)}] Tout anneau",
           "GLOBAL_ISSUES 16. The parentheses inside (i)-(iii) ('(où les homomorphismes ...)', '(les homomorphismes ...)') are italic in the print, as in the TeX (crops p141_s3_ou1.png, p141_s4_les.png)."))
L.append(F(141, "proof of (18.6.14) (i): 'qui est local (0_III, 10.3.1.3)'",
           "bold 0 with subscript III", "plain 0", "convention", 2,
           r"($0_{\mathrm{III}}$, 10.3.1.3)", r"($\mathbf{0}_{\mathrm{III}}$, 10.3.1.3)"))
L.append(F(141, "end of p. 141: page break 141/142 inside '... n un idéal premier | de C au-dessus'",
           "p. 142 begins mid-sentence with 'de C au-dessus' at the left margin, no indent",
           r"blank lines before and after \oldpage[IV-4]{142}", "marker", None,
           r"$\mathfrak n$ un idéal premier" + NL + NL, r"$\mathfrak n$ un idéal premier" + NL,
           "The marker is at the right place. Part 1 of 2: the first p. 142 finding removes the blank line after \\oldpage[IV-4]{142}; apply both."))
# ---------------------------------------------------------------- page 142
L.append(F(142, "top of p. 142: page break 141/142",
           "p. 142 begins mid-sentence ('de C au-dessus de l'idéal maximal ...')",
           r"blank line after \oldpage[IV-4]{142}", "marker", None,
           r"\oldpage[IV-4]{142}" + NL + NL + r"de $C$", r"\oldpage[IV-4]{142}" + NL + r"de $C$",
           "Part 2 of 2 with the last p. 141 finding; both blank lines must go."))
L.append(F(142, "proof of (18.6.14) (i): 'autrement dit que k(m′) → k(n) soit un isomorphisme' (first k)",
           "bold italic k (crop p142_s1_kk.png)", "plain k", "convention", 1,
           r"$k(\mathfrak m')", r"$\boldsymbol{k}(\mathfrak m')"))
L.append(F(142, "same formula, second k: 'k(n)'",
           "bold italic k (crop p142_s1_kk.png)", "plain k", "convention", 1,
           r"k(\mathfrak n)$ soit", r"\boldsymbol{k}(\mathfrak n)$ soit",
           "Independent of the previous finding (no shared characters)."))
L.append(F(142, "'et de la transitivité des fibres (I, 3.6.4)'",
           "bold I (crop p142_s1_I364.png)", "plain I", "convention", 2,
           r"fibres (I, 3.6.4)", r"fibres (\textbf{I}, 3.6.4)",
           "Genuine EGA I reference (bold I followed by a comma), not EGA IV's own (1.x.y)."))
L.append(F(142, "'nécessairement isomorphe à A_λ (18.5.11, b))'",
           "b) italic with italic parenthesis, then the upright closing parenthesis (crop p142_s2_b.png)",
           r"$b)$ (upright parenthesis)", "italics", None,
           r"(18.5.11, $b)$)", r"(18.5.11, \emph{b)})", "GLOBAL_ISSUES 88."))
L.append(F(142, "'isomorphe à Spec(A_λ) (I, 6.5.4)'",
           "bold I (crop p142_s2_I654.png)", "plain I", "convention", 2,
           r"(I, 6.5.4)", r"(\textbf{I}, 6.5.4)",
           "Genuine EGA I reference (bold I followed by a comma)."))
L.append(F(142, "proof of (18.6.14) (ii), after the display: 'Mais comme A′ est hensélien par (i), cela prouve notre assertion.'",
           "new indented paragraph after the display (crop p142_s2_mais.png)",
           r"no blank line after \]: no paragraph break, no indent", "other", None,
           r"\]" + NL + r"Mais comme $A'$", r"\]" + NL + NL + r"Mais comme $A'$",
           "GLOBAL_ISSUES 47 pattern."))
L.append(F(142, "(18.7.1): 'Nous désignerons dans ce numéro par P(Z, k)'",
           "bold italic P", r"\mathbf P", "convention", 10,
           r"par $\mathbf P(Z,k)$", r"par $\boldsymbol{P}(Z,k)$"))
L.append(F(142, "(18.7.1): 'la propriété Q(A, k) satisfait à la condition suivante'",
           "bold italic Q", r"\mathbf Q (bold upright)", "font", None,
           r"propriété $\mathbf Q(A,k)$ satisfait", r"propriété $\boldsymbol{Q}(A,k)$ satisfait",
           "The property letter Q is bold italic like the P of convention 10 (same treatment as IV-3 pp. 57, 61)."))
L.append(F(142, "(18.7.1): 'la propriété Q(A, k) est équivalente à Q(A, k′)' (first Q)",
           "bold italic Q", r"\mathbf Q", "font", None,
           r"propriété $\mathbf Q(A,k)$ est", r"propriété $\boldsymbol{Q}(A,k)$ est",
           "As the previous finding."))
L.append(F(142, "(18.7.1): '... est équivalente à Q(A, k′)' (second Q)",
           "bold italic Q", r"\mathbf Q", "font", None,
           r"à $\mathbf Q(A,k')$", r"à $\boldsymbol{Q}(A,k')$",
           "As the previous finding."))
L.append(F(142, "(18.7.1): 'toutes les propriétés P considérées dans (7.3.8)'",
           "bold italic P", r"\mathbf P", "convention", 10,
           r"propriétés $\mathbf P$ considérées", r"propriétés $\boldsymbol{P}$ considérées"))
# ---------------------------------------------------------------- page 143
L.append(F(143, "Proposition (18.7.2): 'Pour que ʰA soit un P-anneau'",
           "bold italic P", r"\mathbf P", "convention", 10,
           r"un $\mathbf P$-anneau", r"un $\boldsymbol{P}$-anneau"))
L.append(F(143, "Proposition (18.7.2): 'un P-anneau (7.3.13), il faut et il suffit'",
           "reference upright inside the italic statement", "italic", "convention", 6,
           r"(7.3.13), il faut", r"\textup{(7.3.13)}, il faut"))
L.append(F(143, "proof of (18.7.2): 'k(y_i) est une extension algébrique séparable'",
           "bold italic k", "plain k", "convention", 1,
           r"$k(y_i)$ est une", r"$\boldsymbol{k}(y_i)$ est une"))
L.append(F(143, "proof of (18.7.2): 'séparable de k(x)'",
           "bold italic k", "plain k", "convention", 1,
           r"séparable de $k(x)$", r"séparable de $\boldsymbol{k}(x)$"))
L.append(F(143, "proof of (18.7.2): 'l'hypothèse faite sur P dans (18.7.1)'",
           "bold italic P", r"\mathbf P", "convention", 10,
           r"faite sur $\mathbf P$ dans", r"faite sur $\boldsymbol{P}$ dans"))
L.append(F(143, "Proposition (18.7.5): '(5.6.2) (resp. formellement caténaire (7.1.9), resp. strictement formellement caténaire (7.2.6))'",
           "references, 'resp.' and the parentheses upright; 'formellement caténaire', 'strictement formellement caténaire' italic (crop p143_s2_1875.png)",
           "all italic", "convention", 6,
           r"(5.6.2) (resp. formellement caténaire (7.1.9), resp. strictement formellement caténaire (7.2.6)), il en est",
           r"\textup{(5.6.2) (resp.} formellement caténaire \textup{(7.1.9), resp.} strictement formellement caténaire \textup{(7.2.6))}, il en est"))
L.append(F(143, "Lemme (18.7.5.1): '(resp. universellement caténaires)'",
           "'(resp.' and the closing parenthesis upright, 'universellement caténaires' italic (crops p143_s3_resp.png, p143_s3_resp2.png)",
           "all italic", "convention", 6,
           r"(resp. universellement caténaires), il", r"\textup{(resp.} universellement caténaires\textup{)}, il"))
L.append(F(143, "proof of (18.7.5.1): 'p_0 ⊃ p_1 ⊃ ... ⊃ p_r'",
           "baseline dots (crop p143_s3_dots_z.png)", r"\cdots (centred dots)", "symbol", None,
           r"\mathfrak p_1\supset\cdots\supset", r"\mathfrak p_1\supset\ldots\supset"))
L.append(F(143, "proof of (18.7.5.1): 'p_0α ⊃ p_1α ⊃ ... ⊃ p_rα'",
           "baseline dots (crop p143_s3_dots.png)", r"\cdots", "symbol", None,
           r"\mathfrak p_{1\alpha}\supset\cdots\supset", r"\mathfrak p_{1\alpha}\supset\ldots\supset"))
L.append(F(143, "proof of (18.7.5.1): 'et il sufffit de montrer que pour α assez grand'",
           "'sufffit' with three f (crop p143_s3_sufffit_z3.png)", "'suffit' (silent correction)",
           "misprint_in_print", None,
           r"il suffit de montrer", r"il sufffit de montrer",
           "A doubled f sort. The fix restores the printed reading; only the letter changes.",
           corrected=r"il suffit de montrer"))
L.append(F(143, "proof of (18.7.5.1): 'cette chaîne est saturée.'",
           "'saturée' italic (crop p143_s3_saturee.png)", "upright", "italics", None,
           r"cette chaîne est saturée.", r"cette chaîne est \emph{saturée}."))
L.append(F(143, "proof of (18.7.5.1): 'On a donc 1 = codim(V(p_i), V(p_{i+1})) = codim(V(p_iα), V(p_{i+1,α})) puisque B ...'",
           "the formula is set in the line, between 'On a donc' and 'puisque' (crop p143_s3_codim.png)",
           "displayed formula", "formula", None,
           r"On a donc" + NL + r"\[" + NL + r"1=\operatorname{codim}(V(\mathfrak p_i),V(\mathfrak p_{i+1}))" + NL
           + r"=\operatorname{codim}(V(\mathfrak p_{i\alpha}),V(\mathfrak p_{i+1,\alpha}))" + NL + r"\]" + NL + "puisque",
           r"On a donc $1=\operatorname{codim}(V(\mathfrak p_i),V(\mathfrak p_{i+1}))=\operatorname{codim}(V(\mathfrak p_{i\alpha}),V(\mathfrak p_{i+1,\alpha}))$ puisque",
           "Formula displayed in the TeX where the print sets it inline; no connecting word lost or added."))
L.append(F(143, "proof of (18.7.5.1): '((6.1.4) et (0_I, 6.2.3))'",
           "bold 0 with subscript I", "plain 0", "convention", 2,
           r"($0_{\mathrm I}$, 6.2.3)", r"($\mathbf{0}_{\mathrm I}$, 6.2.3)"))
L.append(F(143, "proof of (18.7.5): 'si A est intègre et formellement caténaire, ʰA est formellement équidimensionnel'",
           "only 'intègre' italic; 'et formellement caténaire' roman", r"\emph{intègre et formellement caténaire}",
           "italics", None,
           r"\emph{intègre et formellement caténaire}", r"\emph{intègre} et formellement caténaire"))
# ---------------------------------------------------------------- page 144
L.append(F(144, "proof of (18.7.5): 'vérifient la propriété (S_1) (7.2.5, b))'",
           "b) italic with italic parenthesis (crop p144_s1_b.png)", r"$b)$", "italics", None,
           r"(7.2.5, $b)$)", r"(7.2.5, \emph{b)})", "GLOBAL_ISSUES 88."))
L.append(F(144, "proof of (18.7.5): 'appliqué au cas où P(Z, k) est la propriété (S_1)'",
           "bold italic P", r"\mathbf P", "convention", 10,
           r"où $\mathbf P(Z,k)$ est", r"où $\boldsymbol{P}(Z,k)$ est"))
L.append(F(144, "Corollaire (18.7.6): 'est excellent (7.8.2), il en est de même'",
           "reference upright inside the italic statement", "italic", "convention", 6,
           r"excellent (7.8.2), il", r"excellent \textup{(7.8.2)}, il"))
L.append(F(144, "Remarque (18.7.7): 'homomorphismes canoniques de E_i sur k(m_i)'",
           "bold italic k (crop p144_s2_kmi_z.png)", "plain k", "convention", 1,
           r"sur $k(\mathfrak m_i)$", r"sur $\boldsymbol{k}(\mathfrak m_i)$"))
L.append(F(144, "Remarque (18.7.7): 'et k(m′_i) (i = 1, 2)'",
           "bold italic k (crop p144_s2_kmi_z.png)", "plain k", "convention", 1,
           r"$k(\mathfrak m'_i)$", r"$\boldsymbol{k}(\mathfrak m'_i)$"))
L.append(F(144, "Proposition (18.8.1), label 'a)'",
           "upright a)", r"\item[$a)$]", "convention", 6,
           r"\item[$a)$] $A$ est un anneau hensélien", r"\item[\textup{a)}] $A$ est un anneau hensélien",
           "GLOBAL_ISSUES 16/88. The k of 'son corps résiduel k' is light italic in the print, as in the TeX."))
L.append(F(144, "Proposition (18.8.1), label 'b)'",
           "upright b)", r"\item[$b)$]", "convention", 6,
           r"\item[$b)$] $A$ est un anneau hensélien", r"\item[\textup{b)}] $A$ est un anneau hensélien"))
L.append(F(144, "Proposition (18.8.1), label 'c)'",
           "upright c)", r"\item[$c)$]", "convention", 6,
           r"\item[$c)$] Pour tout morphisme étale", r"\item[\textup{c)}] Pour tout morphisme étale"))
L.append(F(144, "proof of (18.8.1): 'L'hypothèse c) implique'",
           "c) italic with italic parenthesis", r"$c)$", "italics", None,
           r"L'hypothèse $c)$ implique", r"L'hypothèse \emph{c)} implique", "GLOBAL_ISSUES 88."))
L.append(F(144, "proof of (18.8.1): 'la condition b) de (18.5.11) est vérifiée'",
           "b) italic", r"$b)$", "italics", None,
           r"la condition $b)$ de (18.5.11)", r"la condition \emph{b)} de (18.5.11)"))
L.append(F(144, "proof of (18.8.1): 'donc c) implique b).'",
           "labels italic", r"$c)$, $b)$", "italics", None,
           r"donc $c)$ implique $b)$.", r"donc \emph{c)} implique \emph{b)}."))
L.append(F(144, "proof of (18.8.1): 'b) implique a) en vertu de (18.5.11, b)).'",
           "labels italic (the last one followed by the upright closing parenthesis)", r"$b)$, $a)$, $b)$", "italics", None,
           r"clos, $b)$ implique $a)$ en vertu de (18.5.11, $b)$).",
           r"clos, \emph{b)} implique \emph{a)} en vertu de (18.5.11, \emph{b)}).",
           "Three labels, one edit."))
L.append(F(144, "proof of (18.8.1): 'Enfin, il résulte aussi de (18.5.11, b)) que a) implique c).'",
           "labels italic", r"$b)$, $a)$, $c)$", "italics", None,
           r"aussi de (18.5.11, $b)$) que $a)$ implique $c)$.",
           r"aussi de (18.5.11, \emph{b)}) que \emph{a)} implique \emph{c)}.",
           "Three labels, one edit."))
L.append(F(144, "Définition (18.8.2): 'les conditions équivalentes de (18.8.1).'",
           "reference upright inside the italic definition (crop p144_s3_def.png)", "italic", "convention", 6,
           r"équivalentes de (18.8.1).", r"équivalentes de \textup{(18.8.1)}."))
L.append(F(144, "Définition (18.8.2): 'On appelle schéma strictement local un schéma'",
           "'schéma' italic, only 'strictement local' roman (crop p144_s3_def.png)",
           r"\emph{schéma strictement local}: 'schéma' upright too", "convention", 6,
           r"\emph{schéma strictement local}", r"schéma \emph{strictement local}",
           "Printed italic word left upright by \\emph inside the itshape environment. The first '\\emph{strictement local}' of the definition matches the print (roman)."))
L.append(F(144, "Remarque (18.8.3), condition d): label and text",
           "label d) upright; the condition d) is printed italic inside the roman remark (scan strip 4)",
           r"\item[$d)$] in the italic remark environment; no italic markup of its own", "convention", 6,
           r"\item[$d)$] Pour tout morphisme localement de type fini",
           r"\item[\textup{d)}] \itshape Pour tout morphisme localement de type fini",
           "As condition d) of Remarque (18.5.18), p. 134: judged as if the remark body were roman; \\itshape lasts to \\end{enumerate}. With the current italic remark only the label changes."))
L.append(F(144, "Remarque (18.8.3) d): 'extension finie séparable de k(s) = k'",
           "k(s) bold italic, the k after '=' light (crop p144_s4_ks_z.png)", "plain $k(s)=k$", "convention", 1,
           r"séparable de $k(s)=k$", r"séparable de $\boldsymbol{k}(s)=k$"))

json.dump(L, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
print(len(L), "findings written to", OUT)
