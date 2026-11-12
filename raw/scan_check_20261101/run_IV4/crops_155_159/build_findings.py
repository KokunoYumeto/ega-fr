"""Build findings_155_159.json and check every "old" against the page files and the current source.

'¶' in the strings below stands for a line break (LF).
"""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex")
OUT = RUN / "findings_155_159.json"

REM = "Judged as roman remark text (remark font is document-wide)."


def F(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else dict(old=old.replace("¶", "\n"), new=new.replace("¶", "\n")))
    if kind == "misprint_in_print":
        d["corrected"] = corrected.replace("¶", "\n")
    d["note"] = note
    return d


L = []
# ---------------------------------------------------------------- p. 155
L += [
    F(155, "top of page: page break 154/155 inside 'Cela | étant'",
      "p. 155 begins mid-sentence with 'étant, il résulte d'abord' (Remarque (18.9.7.6) continues)",
      r"blank line after \oldpage[IV-4]{155}", "marker", None, "high",
      r"\oldpage[IV-4]{155}¶¶étant, il", r"\oldpage[IV-4]{155}¶étant, il",
      r"BOUNDARY FIX (page break with p. 154). The marker is at the right place. The blank line before it is "
      r"already removed in the current source ('Cela' + newline + \oldpage[IV-4]{155}: part 1 of 2, reported "
      r"by the 150-154 checker); this removes the one after it (\oldpage ends with \ignorespaces, which does "
      r"not skip a \par)."),
    F(155, "Remarque (18.9.7.6), line 1: 'il résulte d'abord de (0, 16.1.5)'", "bold 0", "plain 0",
      "convention", 2, "high", "d'abord de (0, 16.1.5)", r"d'abord de (\textbf{0}, 16.1.5)"),
    F(155, "Remarque (18.9.7.6), line 1: 'et (0, 16.1.4.1)'", "bold 0", "plain 0",
      "convention", 2, "high", "et (0, 16.1.4.1)", r"et (\textbf{0}, 16.1.4.1)"),
    F(155, "Remarque (18.9.7.6), line 3: 'que A soit universellement caténaire (5.6.2)'",
      "'universellement caténaire' italic", r"roman (no \emph)", "italics", None, "high",
      "soit universellement caténaire (5.6.2)", r"soit \emph{universellement caténaire} (5.6.2)", REM),
    F(155, "end of Remarque (18.9.7.6): 'il suffit donc d'appliquer (0, 16.1.5).'", "bold 0", "plain 0",
      "convention", 2, "high", "d'appliquer (0, 16.1.5)", r"d'appliquer (\textbf{0}, 16.1.5)"),
    F(155, "Lemme (18.9.7.7), end: 'X—T est connexe.'", "long dash", "minus sign", "convention", 7, "high",
      "$X-T$ est connexe.", r"$X\setmin T$ est connexe.", r"\setmin as in the earlier IV-4 fixes."),
    F(155, "proof of (18.9.7.7), line 2: 'Spec(O_X,x)—{x} est connexe'", "long dash", "minus sign",
      "convention", 7, "high", r"$\Spec(\sh{O}_{X,x})-\{x\}$", r"$\Spec(\sh{O}_{X,x})\setmin\{x\}$"),
    F(155, "proof of (18.9.7.7): 'posons U = Y—{y}'", "long dash", "minus sign", "convention", 7, "high",
      r"$U=Y-\{y\}$", r"$U=Y\setmin\{y\}$"),
    F(155, "diagram of (18.9.7.7): label g_1 of the top arrow X_1 → X",
      "g_1 above the arrow",
      r"\ar[l]^{g_1}: on a leftward arrow ^ sets the label below it (test compile crops_155_159/diag_test.png)",
      "other", None, "high", r"X_1 \ar[l]^{g_1}", r"X_1 \ar[l]_{g_1}",
      "Label side as in the print (GLOBAL_ISSUES 30 pattern). Independent of the next finding."),
    F(155, "same diagram: label g of the bottom arrow Y_1 → Y",
      "g below the arrow", r"\ar[l]_{g} sets the label above it (diag_test.png)",
      "other", None, "high", r"Y_1 \ar[l]_{g}", r"Y_1 \ar[l]^{g}",
      "Label side as in the print (GLOBAL_ISSUES 30 pattern)."),
    F(155, "proof of (18.9.7.7): 'non réduits à 0 (III, 7.8.6.1)'", "bold III", "plain III",
      "convention", 2, "high", "(III, 7.8.6.1)", r"(\textbf{III}, 7.8.6.1)"),
    F(155, "case C), last line: 'donc X—{b}, qui est l'ensemble des points maximaux'", "long dash",
      "minus sign", "convention", 7, "high", r"$X-\{b\}$, qui est", r"$X\setmin\{b\}$, qui est"),
    F(155, "end of p. 155: page break 155/156 inside 'est égal à | l'ensemble sous-jacent'",
      "p. 156 begins mid-sentence with 'l'ensemble sous-jacent à f^{-1}(η)'",
      r"blank lines before and after \oldpage[IV-4]{156}", "marker", None, "high",
      "est égal à¶¶", "est égal à¶",
      r"The marker is at the right place. Part 1 of 2: the first p. 156 finding removes the blank line after "
      r"\oldpage[IV-4]{156}; apply both (\oldpage ends with \ignorespaces, which does not skip a \par)."),
]
# ---------------------------------------------------------------- p. 156
L += [
    F(156, "top of page: page break 155/156", "mid-sentence continuation 'l'ensemble sous-jacent ...'",
      r"blank line after \oldpage[IV-4]{156}", "marker", None, "high",
      r"\oldpage[IV-4]{156}¶¶l'ensemble", r"\oldpage[IV-4]{156}¶l'ensemble",
      "Part 2 of 2 with the last p. 155 finding; both blank lines must go."),
    F(156, "line 1: 'la fibre f^{-1}(η) est somme des Spec(k(ξ_i))'", "bold italic k", "plain k",
      "convention", 1, "high", r"$\Spec(k(\xi_i))$", r"$\Spec(\boldsymbol{k}(\xi_i))$"),
    F(156, "end of case C): 'donc f^{-1}(η) = X—{b} est réduit à un seul point'", "long dash", "minus sign",
      "convention", 7, "high", r"$f^{-1}(\eta)=X-\{b\}$", r"$f^{-1}(\eta)=X\setmin\{b\}$"),
    F(156, "Corollaire (18.9.8), line 1: 'Avec les notations de (18.9.7),'",
      "reference upright inside the italic statement (crop p156_cond_i.png)", "italic in the statement",
      "convention", 6, "high", "notations de (18.9.7), supposons",
      r"notations de \textup{(18.9.7)}, supposons"),
    F(156, "Corollaire (18.9.8), line 1: 'supposons vérifiée la condition (i)'",
      "(i) upright (crop p156_cond_i.png)", "italic in the statement",
      "convention", 6, "high", "vérifiée la condition (i) de", r"vérifiée la condition \textup{(i)} de"),
    F(156, "Corollaire (18.9.8), line 2: 'de (18.9.7) et'", "reference upright (crop p156_cor1898.png)",
      "italic in the statement", "convention", 6, "high", "(18.9.7) et", r"\textup{(18.9.7)} et",
      "Adjacent to (not overlapping) the previous and the next finding."),
    F(156, "Corollaire (18.9.8), line 2: 'et l'une des deux conditions suivantes :'",
      "'l'une' roman inside the italic statement; 'et' and 'des deux conditions suivantes' italic "
      "(crop p156_cor1898.png)", "italic", "convention", 6, "high",
      "l'une des deux conditions", r"\emph{l'une} des deux conditions",
      r"Roman (emphasised) word in the italic statement; \emph gives upright there."),
    F(156, "Corollaire (18.9.8), item (ii′)", "label upright (crop p156_items.png)",
      r"\item[(ii$'$)] (italic in the statement)", "convention", 6, "high",
      r"\item[(ii$'$)]", r"\item[\textup{(ii$'$)}]", "GLOBAL_ISSUES 16."),
    F(156, "Corollaire (18.9.8) (ii′): 'A est un anneau strictement local (18.8.2).'",
      "reference upright (crop p156_items.png)", "italic in the statement", "convention", 6, "high",
      "strictement local (18.8.2).", r"strictement local \textup{(18.8.2)}."),
    F(156, "Corollaire (18.9.8), item (ii″)", "label upright (crop p156_items.png)",
      r"\item[(ii$''$)] (italic in the statement)", "convention", 6, "high",
      r"\item[(ii$''$)]", r"\item[\textup{(ii$''$)}]", "GLOBAL_ISSUES 16."),
    F(156, "Corollaire (18.9.8) (ii″): 'k(B) est une extension primaire de k(A)'",
      "bold italic k (twice)", "plain k", "convention", 1, "high",
      r"et $k(B)$ est une extension primaire de $k(A)$.",
      r"et $\boldsymbol{k}(B)$ est une extension primaire de $\boldsymbol{k}(A)$."),
    F(156, "Corollaire (18.9.8): 'Alors toutes les fibres ...' after the list",
      "indented as a new paragraph (crop p156_items.png)",
      r"text right after \end{enumerate} (set without the indent)", "other", None, "high",
      r"\end{enumerate}¶Alors", r"\end{enumerate}¶¶Alors",
      "Paragraph after the list, indented as printed (GLOBAL_ISSUES 80 pattern). Adjacent to (not "
      "overlapping) the next finding."),
    F(156, "Corollaire (18.9.8), last line: 'Alors toutes les fibres X_y'",
      "'toutes' roman inside the italic statement (crop p156_alors.png)", "italic",
      "convention", 6, "high", "toutes les fibres $X_y$", r"\emph{toutes} les fibres $X_y$",
      r"Roman (emphasised) word in the italic statement; \emph gives upright there."),
    F(156, "Corollaire (18.9.8), last line: 'X_y (y ∈ Y) sont géométriquement connexes'",
      "parentheses upright (crop p156_alors.png)", "italic parentheses in the statement",
      "convention", 6, "high", r"($y\in Y$) sont", r"\textup{($y\in Y$)} sont"),
    F(156, "proof of (18.9.8): 'k(A′) = k(A), k(B′) = k(B)'", "bold italic k (four times)", "plain k",
      "convention", 1, "high", r"$k(A')=k(A)$, $k(B')=k(B)$",
      r"$\boldsymbol{k}(A')=\boldsymbol{k}(A)$, $\boldsymbol{k}(B')=\boldsymbol{k}(B)$"),
    F(156, "Corollaire (18.9.9): '(i.e. ((7.6.4) et (7.7.2)), dont les fibres formelles (7.3.13) sont "
           "géométriquement réduites)'",
      "the whole parenthesis roman, only 'fibres formelles' italic (crops p156_cor1899.png, p156_cor1899b.png)",
      r"italic in the statement, with an upright \emph{i.e.}", "convention", 6, "high",
      r"(\emph{i.e.} ((7.6.4) et (7.7.2)), dont les fibres formelles (7.3.13) sont géométriquement réduites)",
      r"\textup{(i.e. ((7.6.4) et (7.7.2)), dont les \emph{fibres formelles} (7.3.13) sont géométriquement réduites)}",
      r"Inside \textup the \emph gives italic, as printed; 'i.e.' is roman like the rest of the parenthesis."),
    F(156, "proof of (18.9.9): 'et que k(B) = k(A).'", "bold italic k (twice)", "plain k",
      "convention", 1, "high", r"que $k(B)=k(A)$.", r"que $\boldsymbol{k}(B)=\boldsymbol{k}(A)$."),
    F(156, "end of p. 156: page break 156/157 inside 'Les conclusions | de ces deux propositions'",
      "p. 157 begins mid-sentence with 'de ces deux propositions'",
      r"blank lines before and after \oldpage[IV-4]{157}", "marker", None, "high",
      "Les conclusions¶¶", "Les conclusions¶",
      r"The marker is at the right place. Part 1 of 2: the first p. 157 finding removes the blank line after "
      r"\oldpage[IV-4]{157}; apply both."),
]
# ---------------------------------------------------------------- p. 157
L += [
    F(157, "top of page: page break 156/157", "mid-sentence continuation 'de ces deux propositions ...'",
      r"blank line after \oldpage[IV-4]{157}", "marker", None, "high",
      r"\oldpage[IV-4]{157}¶¶de ces deux", r"\oldpage[IV-4]{157}¶de ces deux",
      "Part 2 of 2 with the last p. 156 finding; both blank lines must go."),
    F(157, "Corollaire (18.9.11): 'un morphisme réduit (i.e. (6.8.1) plat et à fibres géométriquement "
           "réduites)'",
      "the whole parenthesis roman (crop p157_cor18911.png)",
      r"italic in the statement, with an upright \emph{i.e.}", "convention", 6, "high",
      r"(\emph{i.e.} (6.8.1) plat et à fibres géométriquement réduites)",
      r"\textup{(i.e. (6.8.1) plat et à fibres géométriquement réduites)}"),
    F(157, "Corollaire (18.9.11), end: 'X—T est connexe.'", "long dash (crop p157_cor18911.png)",
      "minus sign", "convention", 7, "high",
      "rare dans $Y$, $X-T$ est connexe.", r"rare dans $Y$, $X\setmin T$ est connexe."),
    F(157, "proof of (18.9.11): 'Spec(O_X,x)—{x} est connexe'", "long dash", "minus sign",
      "convention", 7, "high", r"$\Spec(\sh{O}_{X,x})-\{x\}$", r"$\Spec(\sh{O}_{X,x})\setmin\{x\}$"),
    F(157, "heading 18.10: '... géométriquement unibranche ou normal.'", "final full stop",
      "no full stop", "punctuation", None, "high",
      r"\subsection{Préschémas étales sur un préschéma géométriquement unibranche ou normal}",
      r"\subsection{Préschémas étales sur un préschéma géométriquement unibranche ou normal.}",
      "GLOBAL_ISSUES 43/58; most titles in ega4-18-fr.tex already have it (18.12 also lacks it)."),
    F(157, "Théorème (18.10.1), item (i)", "label upright", r"\item[(i)] (italic in the statement)",
      "convention", 6, "high", r"\item[(i)] $f$ est non ramifié", r"\item[\textup{(i)}] $f$ est non ramifié",
      "GLOBAL_ISSUES 16."),
    F(157, "Théorème (18.10.1), item (ii)", "label upright", r"\item[(ii)] (italic in the statement)",
      "convention", 6, "high", r"\item[(ii)] l'homomorphisme", r"\item[\textup{(ii)}] l'homomorphisme",
      "GLOBAL_ISSUES 16."),
    F(157, "Théorème (18.10.1): 'De plus, s'il en est ainsi, ...' after the list",
      "indented as a new paragraph", r"text right after \end{enumerate} (set without the indent)",
      "other", None, "high", r"\end{enumerate}¶De plus", r"\end{enumerate}¶¶De plus",
      "Paragraph after the list, indented as printed (GLOBAL_ISSUES 80 pattern)."),
    F(157, "Théorème (18.10.1): 'remplacer la condition (ii) par la condition'", "(ii) upright",
      "italic in the statement", "convention", 6, "high",
      "remplacer la condition (ii) par", r"remplacer la condition \textup{(ii)} par"),
    F(157, "Théorème (18.10.1): '(ii bis) On a dim O_Y,y ≤ dim O_X,x.'",
      "'(ii' and ')' upright, 'bis' italic (crop p157_iibis.png)", r"\emph{(ii bis)}: all upright",
      "convention", 6, "high", r"\emph{(ii bis)}", r"\textup{(ii \emph{bis})}",
      r"GLOBAL_ISSUES 26; same form as the p. 104 fix \item[\textup{(ii \emph{bis})}]."),
    F(157, "proof of (18.10.1), line 1 of the second paragraph: 'f′ = f_(Y) : X′ → Y′'",
      "subscript (Y) without a prime (crops p157_fprime.png, p157_fY_zoom.png)",
      "f_{(Y')} (silent correction)", "misprint_in_print", None, "high",
      "f'=f_{(Y')}", "f'=f_{(Y)}",
      "f′ is the base change of f by g : Y′ → Y, f_(Y′) as in (17.7.1). The fix restores the printed reading "
      "only.", corrected="f'=f_{(Y')}"),
    F(157, "proof of (18.10.1): 'g : Y′ → Y est plat (18.8.8)'", "'plat' italic (crop p157_plat.png)",
      r"roman (no \emph)", "italics", None, "high", "est plat (18.8.8)", r"est \emph{plat} (18.8.8)"),
    F(157, "proof of (18.10.1): 'que f′ est étale au point x′ (17.7.1, (ii))'",
      "(17.7.1, (ii)) (crop p157_plat.png)", "(17.7.1, (iii))", "number", None, "high",
      "(17.7.1, (iii))", "(17.7.1, (ii))",
      "(17.7.1) has only (i) and (ii); (ii) is the statement used here (g flat, f′ étale at x′ implies f étale "
      "at x), so the print is right and the TeX is wrong."),
    F(157, "proof of (18.10.1): 'est dominant (I, 1.2.7)'", "bold I (crop p157_I127.png)", "plain I",
      "convention", 2, "high", "dominant (I, 1.2.7)", r"dominant (\textbf{I}, 1.2.7)",
      "Genuine EGA I reference (bold I), not EGA IV's own (1.x.y)."),
    F(157, "proof of (18.10.1): 'A′ est intègre (18.8.15)'", "'intègre' italic (crop p157_integre.png)",
      r"roman (no \emph)", "italics", None, "high",
      "$A'$ est intègre (18.8.15)", r"$A'$ est \emph{intègre} (18.8.15)"),
    F(157, "end of p. 157: page break 157/158 inside 'puisque g | est plat (2.3.4)'",
      "p. 158 begins mid-sentence with 'est plat (2.3.4)'",
      r"blank lines before and after \oldpage[IV-4]{158}", "marker", None, "high",
      "puisque $g$¶¶", "puisque $g$¶",
      r"The marker is at the right place. Part 1 of 2: the first p. 158 finding removes the blank line after "
      r"\oldpage[IV-4]{158}; apply both."),
]
# ---------------------------------------------------------------- p. 158
L += [
    F(158, "top of page: page break 157/158", "mid-sentence continuation 'est plat (2.3.4); ...'",
      r"blank line after \oldpage[IV-4]{158}", "marker", None, "high",
      r"\oldpage[IV-4]{158}¶¶est plat (2.3.4)", r"\oldpage[IV-4]{158}¶est plat (2.3.4)",
      "Part 2 of 2 with the last p. 157 finding; both blank lines must go."),
    F(158, "line 1: 'point générique de g^{-1}(y_1) (0_I, 2.1.8)'", "bold 0 with subscript I (crop p158_0I.png)",
      r"($0_{\mathrm I}$, 2.1.8)", "convention", 2, "high",
      r"($0_{\mathrm I}$, 2.1.8)", r"($\mathbf{0}_{\mathrm I}$, 2.1.8)"),
    F(158, "line 2: 'les fibres de g sont des espaces discrets (18.8.12)'",
      "'discrets' italic (crop p158_discrets.png)", r"roman (no \emph)", "italics", None, "high",
      "des espaces discrets (18.8.12)", r"des espaces \emph{discrets} (18.8.12)"),
    F(158, "line 5: 'O_Y′,y′ → O_X′,x′ est injectif (I, 1.2.7)'", "bold I", "plain I",
      "convention", 2, "high", "injectif (I, 1.2.7)", r"injectif (\textbf{I}, 1.2.7)",
      "Genuine EGA I reference (bold I), not EGA IV's own (1.x.y)."),
    F(158, "line 6: '(donc (18.8.3, d)), il y a un voisinage'",
      "label d) wholly italic (the first closing parenthesis is italic), then one upright parenthesis "
      "(crops p158_donc.png, p158_dparens.png)",
      "$d$)) (italic d, both parentheses upright)", "italics", None, "high",
      r"(18.8.3, $d$))", r"(18.8.3, \emph{d)})",
      r"GLOBAL_ISSUES 88; same form as '(18.8.1, \emph{c)})' on p. 145. See the next finding (misprint, no edit)."),
    F(158, "same place: '(donc (18.8.3, d)), il y a'",
      "after the label d) only one closing parenthesis follows: the '(' before 'donc' is never closed",
      "two closing parentheses: keeps the printed reading once the label fix above is applied",
      "misprint_in_print", None, "medium", None, None,
      r"Missing closing parenthesis. The corrected reading assumes the label fix above (\emph{d)}).",
      corrected=r"(donc (18.8.3, \emph{d)})), il y a"),
    F(158, "line 6: 'f′|U soit une immersion fermée de U dans Y′'", "'immersion fermée' italic (crop p158_imm.png)",
      r"roman (no \emph)", "italics", None, "high",
      "une immersion fermée de $U$", r"une \emph{immersion fermée} de $U$"),
    F(158, "line 8: 'et puisqu'il est injectif, il est bijectif.'", "'bijectif' italic (crop p158_imm.png)",
      r"roman (no \emph)", "italics", None, "high", "il est bijectif. Mais", r"il est \emph{bijectif}. Mais"),
    F(158, "line 8: 'O_X′,x′ est un O_Y′,y′-module plat'", "'plat' italic (crop p158_imm.png)",
      r"roman (no \emph)", "italics", None, "high", "-module plat, et $f'$", r"-module \emph{plat}, et $f'$"),
    F(158, "second paragraph: 'X →(f_1) Y_1 → Y (I, 6.5.1)'", "bold I", "plain I", "convention", 2, "high",
      "(I, 6.5.1)", r"(\textbf{I}, 6.5.1)", "Genuine EGA I reference (bold I)."),
    F(158, "second paragraph: 'puisque Y est intègre (0, 16.1.2.2)'",
      "bare bold 0, no subscript (crop p158_0_16122.png)", "($0$, 16.1.2.2)", "convention", 2, "high",
      "($0$, 16.1.2.2)", r"(\textbf{0}, 16.1.2.2)"),
    F(158, "heading 'Remarques (18.10.2). —'", "plural 'Remarques'",
      r"\begin{remark} prints 'Remarque'", "word", None, "high",
      r"\begin{remark}[18.10.2]", r"\begin{remarks}[18.10.2]",
      r"Part 1 of 2: apply together with the p. 159 edit \end{enumerate}\n\end{remark} -> \end{remarks} "
      r"(otherwise LaTeX error). The remarks environment is defined in EGA_IV4_FR.tex (GLOBAL_ISSUES 28)."),
    F(158, "Remarques (18.10.2) (ii): 'g^{-1}(y) est géométriquement réduit sur k(y)'", "bold italic k",
      "plain k", "convention", 1, "high", "sur $k(y)$ (17.4.1)", r"sur $\boldsymbol{k}(y)$ (17.4.1)"),
    F(158, "Remarques (18.10.2) (ii): 'que g est plat au point x'", "'plat' italic", r"roman (no \emph)",
      "italics", None, "high", "$g$ est plat au point $x$, donc", r"$g$ est \emph{plat} au point $x$, donc",
      REM + " Adjacent to (not overlapping) the next finding."),
    F(158, "Remarques (18.10.2) (ii): 'donc f est étale en ce point (18.4.9)'", "'étale' italic",
      r"roman (no \emph)", "italics", None, "high",
      "$f$ est étale en ce point (18.4.9)", r"$f$ est \emph{étale} en ce point (18.4.9)", REM),
    F(158, "Remarques (18.10.2) (iii): 'que f soit localement de type fini'", "'localement de type fini' italic",
      r"roman (no \emph)", "italics", None, "high",
      "soit localement de type fini (et non", r"soit \emph{localement de type fini} (et non", REM),
    F(158, "Remarques (18.10.2) (iii): 'une O_Y,y-algèbre essentiellement étale (18.6.1)'",
      "'essentiellement étale' italic", r"roman (no \emph)", "italics", None, "high",
      "-algèbre essentiellement étale (18.6.1)", r"-algèbre \emph{essentiellement étale} (18.6.1)", REM),
]
# ---------------------------------------------------------------- p. 159
L += [
    F(159, "Remarques (18.10.2) (iii), conditions 1° and 2°",
      "both conditions set italic in the roman remark",
      "no italics of their own (only the environment's italic)", "convention", 6, "high",
      r"\item[$1^\circ$] $f$ est formellement", r"\item[$1^\circ$] \itshape $f$ est formellement",
      r"Judged as if the remark body were roman (document-wide remark item); \itshape lasts to "
      r"\end{enumerate} and covers 2° too. Same form as the conditions a″), d) of pp. 132, 134, 144. With the "
      r"current italic remark nothing changes visibly."),
    F(159, "proof of (iii): 'il suffit de montrer que f est plat au point x'", "'plat' italic (crop p159_top.png)",
      r"roman (no \emph)", "italics", None, "high",
      "que $f$ est plat au point $x$. Or", r"que $f$ est \emph{plat} au point $x$. Or", REM),
    F(159, "proof of (iii): 'où A est strictement local'", "'strictement local' italic (crop p159_top.png)",
      r"roman (no \emph)", "italics", None, "high",
      "$A$ est strictement local et", r"$A$ est \emph{strictement local} et", REM),
    F(159, "proof of (iii): 'donc bijectif en vertu de l'hypothèse'", "'bijectif' italic", r"roman (no \emph)",
      "italics", None, "high", "donc bijectif en vertu", r"donc \emph{bijectif} en vertu", REM),
    F(159, "(iii), last paragraph: 'que Y soit localement intègre au point y'",
      "'localement intègre' italic (crop p159_supposons.png)", r"roman (no \emph)", "italics", None, "high",
      "soit localement intègre au point", r"soit \emph{localement intègre} au point", REM),
    F(159, "(iii), last paragraph: 'au point y (I, 2.1.8)'", "bold I (crop p159_supposons.png)", "plain I",
      "convention", 2, "high", "(I, 2.1.8)", r"(\textbf{I}, 2.1.8)", "Genuine EGA I reference (bold I)."),
    F(159, "(iii), last paragraph: 'les conditions 1° et 2° précédentes (jointe au fait que ...)'",
      "'jointe' (crop p159_jointe.png)", "'jointe' (keeps the printed reading)", "misprint_in_print", None,
      "medium", None, None,
      "Agreement with 'les conditions 1° et 2° précédentes' requires 'jointes'.",
      corrected="(jointes au fait que"),
    F(159, "(iii), last paragraph: 'entraînent déjà que f est étale au point x.'",
      "'étale au point x' italic, 'est' roman (crop p159_supposons.png)", r"roman (no \emph)", "italics",
      None, "high", "que $f$ est étale au point $x$. En effet", r"que $f$ est \emph{étale au point $x$}. En effet",
      REM),
    F(159, "end of Remarques (18.10.2)", "plural remarks (heading on p. 158)", r"\end{remark}", "word", None,
      "high", r"\end{enumerate}¶\end{remark}", r"\end{enumerate}¶\end{remarks}",
      r"Part 2 of 2 with the p. 158 edit \begin{remark}[18.10.2] -> \begin{remarks}[18.10.2]; apply both "
      r"together."),
    F(159, "proof of (18.10.3), line 2: 'en tous les points où il est plat'", "'plat' italic (crop p159_proof.png)",
      r"roman (no \emph)", "italics", None, "high", "où il est plat, et", r"où il est \emph{plat}, et"),
    F(159, "proof of (18.10.3), line 2: 'O_Y,η = k(η) est un corps'", "bold italic k", "plain k",
      "convention", 1, "high", r"$\sh{O}_{Y,\eta}=k(\eta)$", r"$\sh{O}_{Y,\eta}=\boldsymbol{k}(\eta)$"),
    F(159, "proof of (18.10.3), line 3: 'où f est étale est donc non vide'", "'non vide' italic (crop p159_proof.png)",
      r"roman (no \emph)", "italics", None, "high", "est donc non vide. Montrons", r"est donc \emph{non vide}. Montrons"),
    F(159, "proof of (18.10.3), line 4: 'l'homomorphisme O_Y,f(x) → O_X,x est injectif.'",
      "'injectif' italic (crop p159_proof.png)", r"roman (no \emph)", "italics", None, "high",
      "est injectif. Soit en effet", r"est \emph{injectif}. Soit en effet"),
    F(159, "proof of (18.10.3): 'on conclut que f est plat au point x, autrement dit x ∈ U'", "'plat' italic",
      r"roman (no \emph)", "italics", None, "high",
      "on conclut que $f$ est plat au point $x$", r"on conclut que $f$ est \emph{plat} au point $x$"),
]

# ---------------------------------------------------------------- checks
src = SRC.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-4\]\{(\d+)\}", src)]
segs = {}
for i, (n, s) in enumerate(cuts):
    if 155 <= n <= 159:
        segs[n] = src[s:cuts[i + 1][1]]
pages = {n: (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for n in range(155, 160)}
ok = True
for n in range(155, 160):
    body = pages[n].split("\n", 1)[1]  # drop the '% from ...' line
    if body != segs[n]:
        print("segment differs from page file:", n); ok = False
# uniqueness before any edit, and sequential application within each segment
work = dict(segs)
for x in L:
    fx = x["fix"]
    if not fx:
        continue
    n = x["page"]
    c0 = pages[n].count(fx["old"])
    c1 = work[n].count(fx["old"])
    if c0 != 1 or c1 != 1:
        print("NOT UNIQUE", n, repr(fx["old"]), c0, c1); ok = False
        continue
    work[n] = work[n].replace(fx["old"], fx["new"])
# every edit must also be unique in the original page file independently of the others
for x in L:
    fx = x["fix"]
    if fx and segs[x["page"]].count(fx["old"]) != 1:
        print("not unique in original segment", x["page"], repr(fx["old"])); ok = False
json.dump(L, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in L:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for n in range(155, 160):
    print(n, cnt[(n, "normal")], cnt[(n, "convention")], cnt[(n, "misprint")])
print("total", len(L), "OK" if ok else "PROBLEMS")
