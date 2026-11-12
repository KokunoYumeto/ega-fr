"""Build findings_075_079.json and check every fix.

Checks: (1) each "old" occurs exactly once in its page_NNN.tex (CRLF normalised to LF);
(2) applied in list order to the current release file ega4-17-fr.tex (as apply_fixes.py does: page N = from
\\oldpage[IV-4]{N} to the next marker of another page), each "old" occurs exactly once when its turn comes.
In the strings below, the character "¶" stands for a line break.
"""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\IV4\native\ega4\ega4-17-fr.tex")
OUT = RUN / "findings_075_079.json"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    fix = None if old is None else {"old": old.replace("¶", "\n"), "new": new.replace("¶", "\n")}
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


RESP2 = r"\textup{(resp.}\ non ramifié, \textup{resp.}\ étale\textup{)}"
RESP3 = r"\textup{(resp.}\ non ramifié, \textup{resp.}\ étale, \textup{resp.}\ différentiellement lisse\textup{)}"
G96 = "'(resp.', 'resp.' and ')' are roman inside the italic statement (GLOBAL_ISSUES 96); same form as the p. 61-62 page fixes."
G16 = "Roman-numeral labels in italic statements are upright (GLOBAL_ISSUES 16)."
G88 = "Hand-set label inside an italic statement: upright in the print (GLOBAL_ISSUES 88; same form as the p. 65 and p. 67 page fixes)."
G88r = "Labels in roman text are italic in the print (GLOBAL_ISSUES 88)."

# ---------------------------------------------------------------- page 75
add(75, "page break 74/75 inside 'Si k' est une extension algébriquement | close de k'",
    "printed p. 75 begins 'close de k, X⊗_k k' est alors lisse' in the same sentence and paragraph (page_075_s1.png)",
    "blank line after \\oldpage[IV-4]{75} (and another one before it, at the end of the p. 74 segment): a paragraph break the print lacks",
    "marker", None, "high",
    r"\oldpage[IV-4]{75}¶¶close de", r"\oldpage[IV-4]{75}¶close de",
    "The marker is at the right place. Both blank lines around it must go (\\oldpage ends with \\ignorespaces, which does "
    "not swallow the \\par of a blank line): this edit removes the one after the marker. The one before it ('Si $k'$ est "
    "une extension algébriquement' + blank line) is the last line of the p. 74 segment, left to the pp. 70-74 checker; "
    "not reported here.")
add(75, "proof of (17.7.7) (i): 'X⊗_k k' est alors lisse sur k' et en vertu de (17.7.3, (ii))'",
    "no comma after k' (crop p75_s1_kprime.png)", "'lisse sur $k'$, et en vertu': comma added",
    "punctuation", None, "high", r"lisse sur $k'$, et en vertu", r"lisse sur $k'$ et en vertu")
add(75, "proof of (17.7.7) (i): 'il suffit de prouver que Y est lisse sur k en tout point rationnel sur k.'",
    "'rationnel sur k' italic (crop p75_s1_rationnel.png)", "roman",
    "italics", None, "high", r"en tout point rationnel sur $k$.", r"en tout point \emph{rationnel sur $k$}.")
add(75, "proof of (17.7.7) (ii): 'il suffit donc de montrer que f est quasi-fini au point y'",
    "'quasi-fini' italic (crop p75_s2_quasifini.png)", "roman",
    "italics", None, "high", r"est quasi-fini au point $y$", r"est \emph{quasi-fini} au point $y$")
add(75, "proof of (17.7.7) (ii): 'que O_{Y,y} est une k-algèbre finie. Or,'",
    "'finie' italic (crop p75_s2_quasifini.png); the second 'k-algèbre finie' of the paragraph is roman (p75_s2_finie2.png)",
    "roman", "italics", None, "high", r"$k$-algèbre finie. Or", r"$k$-algèbre \emph{finie}. Or")
add(75, "proof of (17.7.7) (ii): 'fidèlement plat (0_I, 6.6.2)'", "bold 0 with subscript I", "plain 0",
    "convention", 2, "high", r"($0_{\mathrm I}$, 6.6.2)", r"($\mathbf{0}_{\mathrm I}$, 6.6.2)")
add(75, "Proposition (17.7.8): 'Les notations étant celles de (8.8.1), on suppose'",
    "upright (8.8.1) (crop p75_s2_prop1.png)", "italic in the italic statement",
    "convention", 6, "high", r"celles de (8.8.1), on", r"celles de \textup{(8.8.1)}, on")
add(75, "Proposition (17.7.8), label (i)", "upright '(i)' (crop p75_s2_prop_i.png)", "\\item[(i)] (italic)",
    "convention", 6, "high", r"\item[(i)]", r"\item[\textup{(i)}]", G16)
add(75, "Proposition (17.7.8) (i): 'Pour que f soit lisse (resp. non ramifié, resp. étale) au point x, il faut'",
    "'(resp.', 'resp.' and ')' roman (crop p75_s2_prop_i.png)", "italic",
    "convention", 6, "high",
    r"soit lisse (resp. non ramifié, resp. étale) au point $x$, il faut",
    r"soit lisse " + RESP2 + r" au point $x$, il faut", G96)
add(75, "Proposition (17.7.8) (i), end: 'tel que f_λ soit lisse (resp. non ramifié, resp. étale) au point x_λ.'",
    "'(resp.', 'resp.' and ')' roman (crop p75_s2_prop_i.png)", "italic",
    "convention", 6, "high",
    r"tel que $f_\lambda$ soit lisse (resp. non ramifié, resp. étale) au point $x_\lambda$.",
    r"tel que $f_\lambda$ soit lisse " + RESP2 + r" au point $x_\lambda$.", G96)
add(75, "Proposition (17.7.8), label (ii)", "upright '(ii)' (crop p75_s2_prop_ii.png)", "\\item[(ii)] (italic)",
    "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]", G16)
add(75, "Proposition (17.7.8) (ii): 'Pour que f soit lisse (resp. non ramifié, resp. étale), il faut'",
    "'(resp.', 'resp.' and ')' roman (crop p75_s2_prop_ii.png)", "italic",
    "convention", 6, "high",
    r"lisse (resp. non ramifié, resp. étale), il faut",
    r"lisse " + RESP2 + r", il faut", G96)
add(75, "Proposition (17.7.8) (ii), end: 'tel que f_λ soit lisse (resp. non ramifié, resp. étale).'",
    "'(resp.', 'resp.' and ')' roman (crop p75_s2_prop_ii.png)", "italic",
    "convention", 6, "high",
    r"soit lisse (resp. non ramifié, resp. étale).",
    r"soit lisse " + RESP2 + r".", G96)
add(75, "proof of (17.7.8) (i): 'f^{-1}(y)=f_λ^{-1}(y_λ)⊗_{k(y_λ)} k(y)'",
    "bold upright k in the subscript, bold italic k in k(y) (crop p75_s3_otimes.png)", "plain k (twice)",
    "convention", 1, "high",
    r"\otimes_{k(y_\lambda)}k(y)$", r"\otimes_{\mathbf{k}(y_\lambda)}\boldsymbol{k}(y)$",
    "Two occurrences in one formula: the subscript k is bold upright (\\mathbf{k}, GLOBAL_ISSUES 48), the k of k(y) bold italic.")
add(75, "Corollaire (17.7.9), label a)", "label a) upright (crop p75_s4_cor.png)", "\\item[a)] (italic in the italic statement)",
    "convention", 6, "high", r"\item[a)]", r"\item[\textup{a)}]", G88)
add(75, "Corollaire (17.7.9) a): 'de présentation finie et lisse (resp. non ramifié, resp. étale).'",
    "'(resp.', 'resp.' and ')' roman (crop p75_s4_cor.png)", "italic",
    "convention", 6, "high",
    r"et lisse (resp. non ramifié, resp. étale).",
    r"et lisse " + RESP2 + r".", G96)

# ---------------------------------------------------------------- page 76
add(76, "Corollaire (17.7.9), label b)", "label b) upright (crop p76_s1_cor_bc.png)", "\\item[b)] (italic in the italic statement)",
    "convention", 6, "high", r"\item[b)]", r"\item[\textup{b)}]", G88)
add(76, "Corollaire (17.7.9) b): 'et que f_0 soit lisse (resp. non ramifié, resp. étale).'",
    "'(resp.', 'resp.' and ')' roman (crop p76_s1_cor_bc.png)", "italic",
    "convention", 6, "high",
    r"que $f_0$ soit lisse (resp. non ramifié, resp. étale).",
    r"que $f_0$ soit lisse " + RESP2 + r".", G96)
add(76, "Corollaire (17.7.9), label c)", "label c) upright (crop p76_s1_cor_bc.png)", "\\item[c)] (italic in the italic statement)",
    "convention", 6, "high", r"\item[c)]", r"\item[\textup{c)}]", G88)
add(76, "Corollaire (17.7.9) c): 'Les conditions de b) sont vérifiées'",
    "label b) upright inside the italic statement (crop p76_s1_cor_bc.png)", "plain b) (italic in the italic statement)",
    "convention", 6, "high", r"Les conditions de b) sont", r"Les conditions de \textup{b)} sont",
    "GLOBAL_ISSUES 88. Independent of the \\item[b)] edit above.")
add(76, "Proposition (17.7.10): 'Supposons que h soit plat au point x'",
    "'plat' roman inside the italic statement (crop p76_s2_prop1710.png)", "italic (no change of face)",
    "convention", 6, "high", r"que $h$ soit plat au point $x$", r"que $h$ soit \textup{plat} au point $x$",
    "The authors' emphasis of the hypotheses and conclusions, set roman in the italic statement (as 'localement noethérien' in (17.4.4), p. 65).")
add(76, "Proposition (17.7.10): 'et que f soit non ramifié au point y.'",
    "'non ramifié' roman inside the italic statement (crop p76_s2_prop1710.png)", "italic (no change of face)",
    "convention", 6, "high", r"$f$ soit non ramifié au point $y$.", r"$f$ soit \textup{non ramifié} au point $y$.")
add(76, "Proposition (17.7.10): 'Alors f est étale au point y'",
    "'étale' roman inside the italic statement (crop p76_s2_prop1710.png)", "italic (no change of face)",
    "convention", 6, "high", r"Alors $f$ est étale au point $y$", r"Alors $f$ est \textup{étale} au point $y$")
add(76, "Proposition (17.7.10): 'et g est plat au point x.'",
    "'plat' roman inside the italic statement (crop p76_s2_prop1710.png)", "italic (no change of face)",
    "convention", 6, "high", r"et $g$ est plat au point $x$.", r"et $g$ est \textup{plat} au point $x$.",
    "Adjacent to the 'étale' edit before it; the two do not overlap.")
add(76, "proof of (17.7.10): 'on peut supposer en outre que S, X et Y sont noethériens; enfin'",
    "'noethériens' italic (crop p76_s2_proof.png)", "roman",
    "italics", None, "high", r"sont noethériens; enfin", r"sont \emph{noethériens}; enfin")
add(76, "proof of (17.7.10): 'un anneau local noethérien B complet, de corps'",
    "'complet' italic (crop p76_s2_proof.png); the later 'A est complet' is roman", "roman",
    "italics", None, "high", r"$B$ complet, de corps", r"$B$ \emph{complet}, de corps")
add(76, "proof of (17.7.10): 'de corps résiduel algébriquement clos et un homomorphisme local'",
    "'algébriquement clos' italic (crop p76_s2_proof.png); the later 'un corps résiduel algébriquement clos.' is roman", "roman",
    "italics", None, "high", r"résiduel algébriquement clos et un", r"résiduel \emph{algébriquement clos} et un")
add(76, "proof of (17.7.10): 'faisant de B un A-module fidèlement plat (0_III, 10.3.1)'",
    "'fidèlement plat' italic (crop p76_s2_proof.png)", "roman",
    "italics", None, "high", r"$A$-module fidèlement plat", r"$A$-module \emph{fidèlement plat}",
    "Independent of the convention-2 edit of the reference that follows.")
add(76, "proof of (17.7.10): '(0_III, 10.3.1)'", "bold 0 with subscript III", "plain 0",
    "convention", 2, "high", r"($0_{\mathrm{III}}$, 10.3.1)", r"($\mathbf{0}_{\mathrm{III}}$, 10.3.1)")
add(76, "proof of (17.7.10): 'anneau local noethérien complet (0_I, 7.4.2)'", "bold 0 with subscript I", "plain 0",
    "convention", 2, "high", r"($0_{\mathrm I}$, 7.4.2)", r"($\mathbf{0}_{\mathrm I}$, 7.4.2)")
add(76, "proof of (17.7.10): 'l'homomorphisme O_{S,s}→O_{Y,y} est surjectif (17.4.4)'",
    "'surjectif' italic (crop p76_s3_top.png); 'injectif' and 'bijectif' further on are roman", "roman",
    "italics", None, "high", r"est surjectif (17.4.4)", r"est \emph{surjectif} (17.4.4)")
add(76, "proof of (17.7.10): 'est injectif (0_I, 6.5.1)'", "bold 0 with subscript I", "plain 0",
    "convention", 2, "high", r"($0_{\mathrm I}$, 6.5.1)", r"($\mathbf{0}_{\mathrm I}$, 6.5.1)")
add(76, "Proposition (17.7.11): 'par le changement de base Spec(k(s))→S. Alors :'",
    "bold italic k (crop p76_s3_prop1711.png)", "plain k",
    "convention", 1, "high", r"$\Spec(k(s))\to S$. Alors", r"$\Spec(\boldsymbol{k}(s))\to S$. Alors")
add(76, "Proposition (17.7.11), label (i)", "upright '(i)'", "\\item[(i)] (italic)",
    "convention", 6, "high", r"\item[(i)]", r"\item[\textup{(i)}]", G16)
add(76, "Proposition (17.7.11) (i): '(resp. non ramifié, resp. étale, resp. différentiellement lisse) au point x'",
    "'(resp.', the two 'resp.' and ')' roman (page_076_s3.png)", "italic",
    "convention", 6, "high",
    r"(resp. non ramifié, resp. étale, resp. différentiellement lisse) au point $x$, est",
    RESP3 + r" au point $x$, est", G96)
add(76, "Proposition (17.7.11), label (ii)", "upright '(ii)'", "\\item[(ii)] (italic)",
    "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]", G16)
add(76, "Proposition (17.7.11) (ii): '(resp. non ramifié, resp. étale, resp. différentiellement lisse) en tous les points'",
    "'(resp.', the two 'resp.' and ')' roman (page_076_s4.png)", "italic",
    "convention", 6, "high",
    r"(resp. non ramifié, resp. étale, resp. différentiellement lisse) en tous",
    RESP3 + r" en tous", G96)
add(76, "Proposition (17.7.11), label (iii)", "upright '(iii)'", "\\item[(iii)] (italic)",
    "convention", 6, "high", r"\item[(iii)]", r"\item[\textup{(iii)}]", G16)
add(76, "Proposition (17.7.11) (iii): '(resp. non ramifié, resp. étale, resp. différentiellement lisse) est localement constructible'",
    "'(resp.', the two 'resp.' and ')' roman (page_076_s4.png)", "italic",
    "convention", 6, "high",
    r"(resp. non ramifié, resp. étale, resp. différentiellement lisse) est localement",
    RESP3 + r" est localement", G96)
add(76, "page break 76/77 inside 'l'ensemble F ... n'est | autre que Y—f(X—E)'",
    "p. 76 ends 'considérée dans (ii) n'est', p. 77 begins 'autre que' in the same sentence (page_076_s4.png, page_077_s1.png)",
    "blank line before \\oldpage[IV-4]{77} (and another after it): a paragraph break inside the sentence",
    "marker", None, "high", r"considérée dans (ii) n'est¶¶", r"considérée dans (ii) n'est¶",
    "GLOBAL_ISSUES 20/99. Part 1 of 2: the p. 77 marker finding removes the blank line after \\oldpage[IV-4]{77}; "
    "apply both (either one alone leaves the paragraph break).")

# ---------------------------------------------------------------- page 77
add(77, "top of page_077.tex: blank line after \\oldpage[IV-4]{77}",
    "p. 77 begins 'autre que Y—f(X—E)', continuing the sentence of p. 76",
    "blank line between the marker and 'autre que': a paragraph break inside the sentence",
    "marker", None, "high", r"\oldpage[IV-4]{77}¶¶autre que", r"\oldpage[IV-4]{77}¶autre que",
    "Part 2 of 2 with the p. 76 marker finding (blank line before the marker). \\oldpage ends with \\ignorespaces, "
    "which does not swallow the \\par of a blank line, so both blank lines must go.")
add(77, "'autre que Y—f(X—E), donc (ii) résulte'", "long dash twice (set difference)", "minus signs",
    "convention", 7, "high", r"$Y-f(X-E)$", r"$Y\setmin f(X\setmin E)$", "Two occurrences in one formula.")
add(77, "'considérée dans (iii) est S—h(Y—F), donc'", "long dash twice (set difference)", "minus signs",
    "convention", 7, "high", r"$S-h(Y-F)$", r"$S\setmin h(Y\setmin F)$", "Two occurrences in one formula.")
add(77, "'Prouvons d'abord (i) lorsqu'il s'agit de la propriété d'être lisse.' | 'La question étant locale sur X'",
    "the sentence is a paragraph of its own: 'La question étant locale sur X' opens a new indented paragraph (crop p77_s1_lisse_par.png)",
    "one paragraph", "other", None, "high",
    r"\emph{lisse}. La question", r"\emph{lisse}.¶¶La question", "Missing paragraph break.")
add(77, "'on se ramène au cas où A est noethérien.'", "'noethérien' italic (page_077_s2.png)", "roman",
    "italics", None, "high", r"$A$ est noethérien.", r"$A$ est \emph{noethérien}.")
add(77, "'En vertu de (0_III, 9.2.3)'", "bold 0 with subscript III", "plain 0",
    "convention", 2, "high", r"($0_{\mathrm{III}}$, 9.2.3)", r"($\mathbf{0}_{\mathrm{III}}$, 9.2.3)")
add(77, "'contenu dans E (resp. dans X—E). Désignant'", "long dash (set difference)", "minus sign",
    "convention", 7, "high", r"dans $X-E$). Désignant", r"dans $X\setmin E$). Désignant")
add(77, "2°: 'Supposons en second lieu que x∈X—E, et que'", "long dash (set difference)", "minus sign",
    "convention", 7, "high", r"$x\in X-E$, et que", r"$x\in X\setmin E$, et que")
add(77, "2°: 'et que le morphisme f_η ne soit pas plat au point x.'", "'ne soit pas plat' italic (page_077_s3.png)", "roman",
    "italics", None, "high", r"ne soit pas plat au point", r"\emph{ne soit pas plat} au point")
add(77, "Lemme (17.7.11.1): 'F un O_X-Module quasi-cohérent de présentation finie'",
    "'Module' with a capital M (crop p77_s3_lemme.png)", "'-module'",
    "word", None, "high", r"$\sh{O}_X$-module quasi-cohérent", r"$\sh{O}_X$-Module quasi-cohérent")
add(77, "proof of (17.7.11.1): 'contenu dans E (resp. dans X—E). Le cas où'", "long dash (set difference)", "minus sign",
    "convention", 7, "high", r"dans $X-E$). Le cas", r"dans $X\setmin E$). Le cas")
add(77, "proof of (17.7.11.1): 'qu'il existe deux O_Y-Modules cohérents G, H'",
    "'Modules' with a capital M (crop p77_s4_modules.png); 'O_Y-homomorphisme' after it is lower case", "'-modules'",
    "word", None, "high", r"$\sh{O}_Y$-modules cohérents", r"$\sh{O}_Y$-Modules cohérents")
add(77, "page break 77/78 inside '... (9.4.2), donc | Supp(Ker(1⊗u_s)) = ...'",
    "p. 77 ends '(9.4.2), donc', p. 78 begins 'Supp(Ker(1⊗u_s))=' in the same sentence (page_077_s4.png, page_078_s1.png)",
    "blank line before \\oldpage[IV-4]{78} (and another after it): a paragraph break inside the sentence",
    "marker", None, "high", r"(9.4.2), donc¶¶", r"(9.4.2), donc¶",
    "GLOBAL_ISSUES 20/99. Part 1 of 2: the p. 78 marker finding removes the blank line after \\oldpage[IV-4]{78}; "
    "apply both (either one alone leaves the paragraph break).")

# ---------------------------------------------------------------- page 78
add(78, "top of page_078.tex: blank line after \\oldpage[IV-4]{78}",
    "p. 78 begins 'Supp(Ker(1⊗u_s))=(Supp(Ker(1⊗u)))_s', continuing the sentence of p. 77",
    "blank line between the marker and the formula: a paragraph break inside the sentence",
    "marker", None, "high", r"\oldpage[IV-4]{78}¶¶$\operatorname{Supp}", r"\oldpage[IV-4]{78}¶$\operatorname{Supp}",
    "Part 2 of 2 with the p. 77 marker finding (blank line before the marker); both blank lines must go.")
add(78, "'(Supp(Ker(1⊗u)))_s (I, 9.1.13.1); il résulte enfin'", "bold I (crop p78_s1_top.png)", "plain I",
    "convention", 2, "high", r"(I, 9.1.13.1)", r"(\textbf{I}, 9.1.13.1)")
add(78, "3°: 'Supposons maintenant que x∈X—E, que le morphisme'", "long dash (set difference)", "minus sign",
    "convention", 7, "high", r"$x\in X-E$, que le", r"$x\in X\setmin E$, que le")
add(78, "3°: 'que le morphisme f_η soit plat au point x, mais'", "'plat' italic (crop p78_s1_3deg.png)", "roman",
    "italics", None, "high", r"soit plat au point $x$, mais", r"soit \emph{plat} au point $x$, mais")
add(78, "'équivaut à dire que f_s est à la fois lisse et quasi-fini au point x (17.6.1)'",
    "'lisse' and 'quasi-fini' italic (crop p78_s2_lisse_qf.png)", "roman",
    "italics", None, "high", r"à la fois lisse et quasi-fini", r"à la fois \emph{lisse} et \emph{quasi-fini}")
add(78, "'il faut et il suffit que p_{g(x)} soit lisse au point Δ_f(x)'", "'lisse' italic (crop p78_s3_p.png)", "roman",
    "italics", None, "high", r"$p_{g(x)}$ soit lisse au point", r"$p_{g(x)}$ soit \emph{lisse} au point")
add(78, "'de dire que (Δ_f)_{g(x)} est étale au point x; il suffit'", "'étale' italic (crop p78_s3_etale.png)", "roman",
    "italics", None, "high", r"$(\Delta_f)_{g(x)}$ est étale au point", r"$(\Delta_f)_{g(x)}$ est \emph{étale} au point")

# ---------------------------------------------------------------- page 79
add(79, "heading 17.8: 'Critères de lissité et non-ramification par fibres.'",
    "full stop after the title (page_079_s1.png)", "no full stop",
    "punctuation", None, "high",
    r"\subsection{Critères de lissité et non-ramification par fibres}",
    r"\subsection{Critères de lissité et non-ramification par fibres.}",
    "GLOBAL_ISSUES 43/58; same form as the earlier subsection-title page fixes (17.2 p. 59, 17.5 p. 67).")
add(79, "Proposition (17.8.1): 'par le changement de base Spec(k(s))→S, soit non ramifié.'",
    "bold italic k (page_079_s1.png)", "plain k",
    "convention", 1, "high", r"\Spec(k(s))\to S$, soit non ramifié", r"\Spec(\boldsymbol{k}(s))\to S$, soit non ramifié")
add(79, "proof of (17.8.1): 'de ce morphisme (17.4.1, d))'", "label d) italic, parenthesis included (crop p79_s1_cela.png)",
    "$d$): italic d, upright parenthesis", "italics", None, "high", r"(17.4.1, $d$))", r"(17.4.1, \emph{d)})", G88r)
add(79, "Proposition (17.8.2): 'on suppose en outre que h est plat.'",
    "'plat' roman inside the italic statement (crop p79_s2_prop2.png)", "italic (no change of face)",
    "convention", 6, "high", r"$h$ est plat. Pour", r"$h$ est \textup{plat}. Pour",
    "The authors' emphasis of the added hypothesis, as in (17.7.10) p. 76.")
add(79, "Proposition (17.8.2): 'soit lisse (resp. étale), il faut et il suffit'",
    "'(resp.' and ')' roman (crop p79_s2_prop2.png)", "italic",
    "convention", 6, "high", r"(resp. étale), il faut", r"\textup{(resp.}\ étale\textup{)}, il faut", G96)
add(79, "Proposition (17.8.2): 'par le changement de base Spec(k(s))→S soit lisse'",
    "bold italic k (crop p79_s2_prop2.png)", "plain k",
    "convention", 1, "high", r"\Spec(k(s))\to S$ soit lisse", r"\Spec(\boldsymbol{k}(s))\to S$ soit lisse")
add(79, "Proposition (17.8.2): 'soit lisse (resp. étale). Lorsqu'il en est ainsi'",
    "'(resp.' and ')' roman (crop p79_s2_prop2.png)", "italic",
    "convention", 6, "high", r"(resp. étale). Lorsqu'il", r"\textup{(resp.}\ étale\textup{)}. Lorsqu'il",
    G96 + " Does not overlap the k edit before it.")
add(79, "proof of (17.8.2): 'le fait d'être lisse est une propriété des fibres de ce morphisme'",
    "'fibres' italic (crop p79_s2_proof2.png)", "roman",
    "italics", None, "high", r"propriété des fibres de ce", r"propriété des \emph{fibres} de ce")
add(79, "proof of (17.8.2): '(17.5.1, b))'", "label b) italic, parenthesis included (crop p79_s2_proof2.png)",
    "$b$): italic b, upright parenthesis", "italics", None, "high", r"(17.5.1, $b$))", r"(17.5.1, \emph{b)})", G88r)
add(79, "heading 17.9: 'Morphismes étales et immersions ouvertes.'",
    "full stop after the title (page_079_s3.png)", "no full stop",
    "punctuation", None, "high",
    r"\subsection{Morphismes étales et immersions ouvertes}",
    r"\subsection{Morphismes étales et immersions ouvertes.}",
    "GLOBAL_ISSUES 43/58; same form as the earlier subsection-title page fixes.")
add(79, "Théorème (17.9.1), label a)", "label a) upright (crop p79_s3_thm.png)", "\\item[a)] (italic in the italic statement)",
    "convention", 6, "high", r"\item[a)]", r"\item[\textup{a)}]", G88)
add(79, "Théorème (17.9.1), label b)", "label b) upright (crop p79_s3_thm.png)", "\\item[b)] (italic in the italic statement)",
    "convention", 6, "high", r"\item[b)]", r"\item[\textup{b)}]", G88)
add(79, "Théorème (17.9.1), label c)", "label c) upright (crop p79_s3_thm.png)", "\\item[c)] (italic in the italic statement)",
    "convention", 6, "high", r"\item[c)]", r"\item[\textup{c)}]", G88)
add(79, "proof of (17.9.1): 'Il résulte de (1.4.3, (i)) que a) implique b).'", "labels a), b) italic (crop p79_s3_thm.png)",
    "plain labels", "italics", None, "high", r"que a) implique b).", r"que \emph{a)} implique \emph{b)}.", G88r)
add(79, "proof of (17.9.1): 'La condition b) implique que'", "label b) italic", "plain b)",
    "italics", None, "high", r"La condition b) implique", r"La condition \emph{b)} implique", G88r)
add(79, "proof of (17.9.1): 'isomorphe à Spec(k(y)) (8.11.5.1)'", "bold italic k (crop p79_s3_thm.png)", "plain k",
    "convention", 1, "high", r"\Spec(k(y))", r"\Spec(\boldsymbol{k}(y))")
add(79, "proof of (17.9.1): 'donc b) entraîne c), en vertu de'", "labels b), c) italic", "plain labels",
    "italics", None, "high", r"donc b) entraîne c), en", r"donc \emph{b)} entraîne \emph{c)}, en", G88r)
add(79, "proof of (17.9.1): '(17.6.2, c))'", "label c) italic, parenthesis included", "$c$): italic c, upright parenthesis",
    "italics", None, "high", r"(17.6.2, $c$))", r"(17.6.2, \emph{c)})", G88r)
add(79, "proof of (17.9.1): 'Reste à voir que c) implique a).'", "labels c), a) italic", "plain labels",
    "italics", None, "high", r"que c) implique a).", r"que \emph{c)} implique \emph{a)}.", G88r)
add(79, "page break 79/80 inside 'on peut se borner au cas | où Y=Spec(A)'",
    "p. 79 ends 'on peut se borner au cas', p. 80 begins 'où Y=Spec(A), A étant un anneau local' (page_079_s4.png; top of page_080_s1.png)",
    "blank line before \\oldpage[IV-4]{80} (and another after it, in the p. 80 segment): a paragraph break inside the sentence",
    "marker", None, "high", r"se borner au cas¶¶", r"se borner au cas¶",
    "GLOBAL_ISSUES 20/99. The marker is at the right place. The blank line after \\oldpage[IV-4]{80} (p. 80 segment, "
    "before 'où $Y=\\Spec(A)$') must go too; it is outside this batch and not reported here.")

# ---------------------------------------------------------------- checks
pages = {}
for p in range(75, 80):
    pages[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
bad = 0
for x in F:
    if x["fix"]:
        n = pages[x["page"]].count(x["fix"]["old"])
        if n != 1:
            bad += 1
            print("NOT UNIQUE in page file:", x["page"], n, repr(x["fix"]["old"][:80]))

t = SRC.read_text(encoding="utf-8")
assert "\r\n" not in t
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")


def locate(text, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(text)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(text)
    return None, None


for x in F:
    if not x["fix"]:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    n = seg.count(x["fix"]["old"])
    if n != 1:
        bad += 1
        print("SEQUENTIAL FAIL:", x["page"], n, repr(x["fix"]["old"][:80]))
        continue
    t = t[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + t[e:]
(RUN / "crops_075_079" / "simulated_ega4-17.txt").write_text(t, encoding="utf-8", newline="")
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
cnt = {}
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print("findings", len(F), "problems", bad)
for p in sorted(cnt):
    print(p, cnt[p])
