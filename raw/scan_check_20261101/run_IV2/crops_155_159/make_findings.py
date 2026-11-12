# Builds findings_155_159.json; '⏎' stands for a line break (LF) in old/new strings.
import json
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
RUN = E / "run_IV2"
OUT = RUN / "findings_155_159.json"
NL = "⏎"


def F(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else dict(old=old.replace(NL, "\n"), new=new.replace(NL, "\n")), note=note)
    if corrected is not None:
        d["corrected"] = corrected.replace(NL, "\n")
    return d


P157 = "printed p. 157 (the TeX still has this text before \\oldpage[IV-2]{157}, i.e. in the p. 156 segment; see the marker entry)"
L = []
# ---------------------------------------------------------------- p. 155
L += [
    F(155, "first line: 'tel que F|u^{-1}(U) soit plat sur U'", "F|u^{-1}(U): u^{-1}(U) on the baseline after the bar",
      "F|_{u^{-1}(U)} (subscript)", "formula", None, "high",
      r"$\mathcal F|_{u^{-1}(U)}$", r"$\mathcal F|u^{-1}(U)$", "Enlarged crop."),
    F(155, "end of proof of (6.9.3): 'ayant pour espace sous-jacent S — U'", "long dash S—U (bar 41 px; = bars 34-35 px)",
      "minus sign S-U", "convention", 7, "high", r"$S-U$", r"$S\setmin U$",
      "Set difference; \\setmin pending the convention-7 decision."),
    F(155, "heading 6.10", "'... le long d'un sous-préschéma fermé.' (full stop)", "no full stop", "punctuation", None, "high",
      r"sous-préschéma fermé}", r"sous-préschéma fermé.}", "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop)."),
    F(155, "(6.10.1): 'où G_k = j*(J^kF/J^{k+1}F) = j*(J^kF) est un O_Y-Module cohérent'",
      "formula in the running text", "displayed formula", "other", None, "high",
      r"où⏎\[⏎\mathcal G_k=j^*(\mathcal J^k\mathcal F/\mathcal J^{k+1}\mathcal F)⏎=j^*(\mathcal J^k\mathcal F)⏎\]⏎est un",
      r"où $\mathcal G_k=j^*(\mathcal J^k\mathcal F/\mathcal J^{k+1}\mathcal F)=j^*(\mathcal J^k\mathcal F)$⏎est un",
      "Display vs inline only; no connecting word lost."),
    F(155, "(6.10.1): 'le O_Y-Module gradué égal à la somme directe'", "'Module gradué' italic", "upright", "italics", None, "high",
      r"$\mathcal O_Y$-Module gradué égal", r"$\mathcal O_Y$-\emph{Module gradué} égal", "Enlarged crop."),
    F(155, "(6.10.1): 'gr^0(F) = G_0 = F ⊗_{O_Y} O_Y = j*(F)'", "F ⊗_{O_Y} O_Y (subscript O_Y)", "F \\otimes_{\\mathcal O_X} \\mathcal O_Y",
      "misprint_in_print", None, "high", r"\otimes_{\mathcal O_X}\mathcal O_Y", r"\otimes_{\mathcal O_Y}\mathcal O_Y",
      "Enlarged crop: the subscript of ⊗ is O_Y. F is an O_X-Module, so the tensor product is over O_X. The TeX silently corrected the misprint; the fix restores the printed reading.",
      corrected=r"\mathcal F\otimes_{\mathcal O_X}\mathcal O_Y"),
    F(155, "(6.10.1): 'que F est normalement plat le long de Y si'", "'normalement plat le long de' italic", "upright", "italics", None, "high",
      r"est normalement plat le long de $Y$ si", r"est \emph{normalement plat le long de} $Y$ si", ""),
    F(155, "(6.10.1): 'est un O_Y-Module plat.'", "'Module plat' italic", "upright", "italics", None, "high",
      r"$\mathcal O_Y$-Module plat. Il revient", r"$\mathcal O_Y$-\emph{Module plat}. Il revient", ""),
    F(155, "(6.10.1): '((2.1.12) et (0_I, 6.1.2))'", "bold 0", "plain 0", "convention", 2, "high",
      r"$(0_{\mathrm I},6.1.2)$", r"$(\mathbf{0}_{\mathrm I},6.1.2)$", ""),
    F(155, "(6.10.1): 'est localement libre.'", "'localement libre' italic", "upright", "italics", None, "high",
      r"est localement libre.", r"est \emph{localement libre}.", ""),
    F(155, "Proposition (6.10.2): 'Y un sous-préschéma fermé intègre de X'", "'intègre' upright between italic 'fermé' and 'de'",
      "italic (statement environment)", "convention", 6, "high", r"fermé⏎intègre de $X$", r"fermé⏎\textup{intègre} de $X$", "Enlarged crop."),
    F(155, "proof of (6.10.2): 'est quasi-cohérente et de type fini car'", "'de type fini' italic", "upright", "italics", None, "high",
      r"quasi-cohérente et de type fini car", r"quasi-cohérente et \emph{de type fini} car", ""),
    F(155, "proof of (6.10.2): 'B-module quasi-cohérent engendré par gr^1_J(F)'", "gr^1_J(F) (superscript 1, as in gr^1_J(O_X) on the line above)",
      "gr^0_J(F)", "misprint_in_print", None, "high", r"^{0}(\mathcal F)$, c'est", r"^{1}(\mathcal F)$, c'est",
      "Enlarged crop. gr•_J(F) is generated over gr•_J(O_X) by its degree-0 part, so the correct reading is gr^0. The TeX silently corrected the misprint; the fix restores the printed reading.",
      corrected=r"\operatorname{gr}_{\mathcal J}^{0}(\mathcal F)"),
    F(155, "proof of (6.10.2): 'c'est un B-Module de type fini.'", "'de type fini' italic", "upright", "italics", None, "high",
      r"$\mathcal B$-Module de type fini.", r"$\mathcal B$-Module \emph{de type fini}.", ""),
    F(155, "Proposition (6.10.3): 'Les notations étant celles de (6.10.1)'", "reference upright", "italic (statement environment)",
      "convention", 6, "high", r"celles de (6.10.1), supposons que $\mathcal F$", r"celles de \textup{(6.10.1)}, supposons que $\mathcal F$",
      "Reference printed upright inside the italic statement."),
    F(155, "Proposition (6.10.3), label (i)", "(i) upright", "\\item[(i)] (italic)", "convention", 6, "high",
      r"\item[(i)] $Y\cap", r"\item[\textup{(i)}] $Y\cap", "GLOBAL_ISSUES 16."),
    F(155, "Proposition (6.10.3) (i): '(autrement dit, une réunion de composantes connexes de Y)'",
      "'(autrement dit, une' upright; 'réunion de composantes connexes de' italic", "all italic", "convention", 6, "high",
      r"(autrement dit, une réunion", r"\textup{(autrement dit, une} réunion", "Enlarged crop."),
    F(155, "Proposition (6.10.3), label (ii)", "(ii) upright", "\\item[(ii)] (italic)", "convention", 6, "high",
      r"\item[(ii)] Si $\mathcal J$", r"\item[\textup{(ii)}] Si $\mathcal J$", "GLOBAL_ISSUES 16."),
    F(155, "proof of (6.10.3) (i): '(I, 9.1.13)'", "bold I", "plain I", "convention", 2, "high",
      r"(I, 9.1.13)", r"(\textbf{I}, 9.1.13)", ""),
]
# ---------------------------------------------------------------- p. 156
L += [
    F(156, "proof of (6.10.3) (ii): 'forment une suite O_{Y,x}-régulière maximale'", "'maximale' italic", "upright", "italics", None, "high",
      r"-régulière maximale;", r"-régulière \emph{maximale};", ""),
    F(156, "proof of (6.10.3) (ii): 'cette suite est aussi F_x-régulière'", "'régulière' italic", "upright", "italics", None, "high",
      r"est aussi $\mathcal F_x$-régulière", r"est aussi $\mathcal F_x$-\emph{régulière}", "Enlarged crop."),
    F(156, "proof of (6.10.3) (ii): '(0, 15.1.19)'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0, 15.1.19)", r"(\textbf{0}, 15.1.19)", ""),
    F(156, "proof of (6.10.3) (ii): 'est aussi (F_x/F_x^(n))-régulière (loc. cit.)'", "'régulière' italic (like 'loc. cit.')",
      "'régulière' upright", "italics", None, "high",
      r"$-régulière⏎(\emph{loc. cit.})", r"$-\emph{régulière}⏎(\emph{loc. cit.})", ""),
    F(156, "proof of (6.10.3) (ii): 'Mais l'hypothèse entraîne que F_x^(n) ...' after the display",
      "new indented paragraph", "no blank line after \\] (same paragraph)", "other", None, "high",
      r"\]⏎Mais l'hypothèse", r"\]⏎⏎Mais l'hypothèse", ""),
    F(156, "proof of (6.10.3) (ii): 'comme prof(O_{Y,x}/(Σ f_i O_{Y,x})) = 0 (0, 16.4.6) on a aussi'",
      "formula in the running text", "displayed formula", "other", None, "high",
      r"comme⏎\[⏎\operatorname{prof}\left(\mathcal O_{Y,x}/⏎\left(\sum_{i=1}^{p}f_i\mathcal O_{Y,x}\right)\right)=0⏎\]⏎",
      r"comme⏎$\operatorname{prof}(\mathcal O_{Y,x}/(\sum_{i=1}^{p}f_i\mathcal O_{Y,x}))=0$⏎",
      "Display vs inline only."),
    F(156, "proof of (6.10.3) (ii): '(0, 16.4.6) on a aussi,'", "no comma after the reference", "'(0, 16.4.6), on a aussi'",
      "punctuation", None, "high", r"(0, 16.4.6), on a aussi", r"(\textbf{0}, 16.4.6) on a aussi",
      "Enlarged crop. One edit for this finding and the next (convention 2): comma removed and bold 0 together."),
    F(156, "proof of (6.10.3) (ii): '(0, 16.4.6) on a aussi'", "bold 0", "plain 0", "convention", 2, "high", None, None,
      "Covered by the edit of the preceding finding."),
    F(156, "proof of (6.10.3) (ii): 'par la caractérisation (0, 16.4.6, (i))'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0, 16.4.6, (i))", r"(\textbf{0}, 16.4.6, (i))", ""),
    F(156, "proof of (6.10.3) (ii): '... de profondeur nulle, prof(F_x^(n)/(Σ f_i F_x^(n))) = 0, puis'",
      "formula in the running text", "displayed formula", "other", None, "high",
      r"nulle,⏎\[⏎\operatorname{prof}\left(\mathcal F_x^{(n)}/⏎\left(\sum_{i=1}^{p}f_i\mathcal F_x^{(n)}\right)\right)=0,⏎\]⏎",
      r"nulle,⏎$\operatorname{prof}(\mathcal F_x^{(n)}/(\sum_{i=1}^{p}f_i\mathcal F_x^{(n)}))=0$,⏎",
      "Display vs inline only."),
    F(156, "proof of (6.10.3) (ii): 'puis prof(F_x/(Σ f_i F_x)) = 0; les ...'",
      "formula in the running text", "displayed formula", "other", None, "high",
      r"\[⏎\operatorname{prof}\left(\mathcal F_x/⏎\left(\sum_{i=1}^{p}f_i\mathcal F_x\right)\right)=0;⏎\]⏎",
      r"$\operatorname{prof}(\mathcal F_x/(\sum_{i=1}^{p}f_i\mathcal F_x))=0$;⏎",
      "Display vs inline only."),
    F(156, "proof of (6.10.3) (ii): 'les (f_i)_x appartenant à l'idéal maximal'", "(f_i)_x", "(f_i)", "formula", None, "high",
      r"les $(f_i)$ appartenant", r"les $(f_i)_x$ appartenant", "Enlarged crop: subscript x after the parenthesis."),
    F(156, "proof of (6.10.3) (ii): 'formant une suite F_x-régulière, cela montre'", "'régulière' italic", "upright", "italics", None, "high",
      r"suite $\mathcal F_x$-régulière, cela", r"suite $\mathcal F_x$-\emph{régulière}, cela", ""),
    F(156, "proof of (6.10.3) (ii): '(0, 16.4.6, (ii))'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0, 16.4.6, (ii))", r"(\textbf{0}, 16.4.6, (ii))", ""),
    F(156, "Corollaire (6.10.4): '(resp. U_{C_n}(F))'", "'(resp.' upright", "italic", "convention", 6, "high",
      r"(resp. $U_{C_n}(\mathcal F)$)", r"\textup{(resp.} $U_{C_n}(\mathcal F)$)", "'(resp.' printed roman inside the italic statement."),
    F(156, "Corollaire (6.10.4): 'au point x (resp. tels que coprof(F_x) ≤ n)'", "'(resp.' upright", "italic", "convention", 6, "high",
      r"au point $x$ (resp. tels que", r"au point $x$ \textup{(resp.} tels que", "'(resp.' printed roman inside the italic statement."),
    F(156, "Proposition (6.10.5): 'Les notations étant celles de (6.10.1)'", "reference upright", "italic", "convention", 6, "high",
      r"celles de (6.10.1), supposons que $Y$", r"celles de \textup{(6.10.1)}, supposons que $Y$",
      "Reference printed upright inside the italic statement."),
    F(156, "Proposition (6.10.5), label (i)", "(i) upright", "\\item[(i)] (italic)", "convention", 6, "high",
      r"\item[(i)] Il existe", r"\item[\textup{(i)}] Il existe", "GLOBAL_ISSUES 16."),
    F(156, "Proposition (6.10.5), label (ii)", "(ii) upright", "\\item[(ii)] (italic)", "convention", 6, "high",
      r"\item[(ii)] On a", r"\item[\textup{(ii)}] On a", "GLOBAL_ISSUES 16."),
    F(156, "Proposition (6.10.5): 'notons d — 1 le degré de P'", "long dash d—1 (bar 35 px; = bars of this type 25-27 px)",
      "minus sign", "convention", 7, "high", r"notons $d-1$ le degré", r"notons $d\setmin 1$ le degré",
      "Long dash for subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision."),
    F(156, "Proposition (6.10.5), label (iii)", "(iii) upright", "\\item[(iii)] (italic)", "convention", 6, "high",
      r"\item[(iii)] Supposons", r"\item[\textup{(iii)}] Supposons", "GLOBAL_ISSUES 16."),
    F(156, "Proposition (6.10.5) (iii): 'De façon plus précise, ...' after (6.10.5.4)", "new indented paragraph",
      "no blank line after \\end{equation}", "other", None, "high",
      r"\end{equation}⏎De façon", r"\end{equation}⏎⏎De façon", ""),
    F(156, "Proposition (6.10.5) (iii): 'pour F_x (0, 16.3.6) et tels que'", "reference upright with bold 0", "italic, plain 0",
      "convention", 6, "high", r"$\mathcal F_x$ (0, 16.3.6) et tels", r"$\mathcal F_x$ \textup{(\textbf{0}, 16.3.6)} et tels",
      "One edit for this finding and the next (convention 2): upright reference and bold 0 together."),
    F(156, "Proposition (6.10.5) (iii): '(0, 16.3.6)'", "bold 0", "plain 0", "convention", 2, "high", None, None,
      "Covered by the edit of the preceding finding."),
    F(156, "Proposition (6.10.5) (iii): 'on ait V(J_x) = V(Σ f_i O_{X,x}) ∩ Supp(F).'", "formula in the running text", "displayed formula",
      "other", None, "high",
      r"on ait⏎\[⏎V(\mathcal J_x)=V\left(\sum_{i=1}^{d}f_i\mathcal O_{X,x}\right)⏎\cap\operatorname{Supp}(\mathcal F).⏎\]",
      r"on ait⏎$V(\mathcal J_x)=V(\sum_{i=1}^{d}f_i\mathcal O_{X,x})\cap\operatorname{Supp}(\mathcal F)$.",
      "Display vs inline only."),
    # proof of (6.10.5), printed on p. 157 but still in the p. 156 segment
    F(156, "proof of (6.10.5): 'savoir le polynôme H(n+1) — H(n)'; " + P157, "long dash (bar 33 px; = bars of this type 25-27 px)",
      "minus sign", "convention", 7, "high", r"$H(n+1)-H(n)$", r"$H(n+1)\setmin H(n)$",
      "\\setmin pending the convention-7 decision. Apply before the marker entry for p. 157."),
    F(156, "proof of (6.10.5): 'polynôme de Hilbert-Samuel'; " + P157, "hyphen (same length as in the other compounds)",
      "Hilbert--Samuel (en dash)", "punctuation", None, "medium", r"Hilbert--Samuel", r"Hilbert-Samuel",
      "Enlarged crop. Apply before the marker entry for p. 157."),
    F(156, "proof of (6.10.5): 'filtration J_y-préadique (0, 16.2.1)'; " + P157, "bold 0", "plain 0", "convention", 2, "high",
      r"(0, 16.2.1)", r"(\textbf{0}, 16.2.1)", "Apply before the marker entry for p. 157."),
    F(156, "proof of (6.10.5): 'la longueur du O_{X,y}-module O_{Y,y} = O_{X,y}/J_y'; " + P157, "O_{Y,y} = O_{X,y}/J_y",
      "O_{X,y}/J_y ('O_{Y,y} =' missing)", "missing", None, "high",
      r"-module $\mathcal O_{X,y}/\mathcal J_y$;", r"-module $\mathcal O_{Y,y}=\mathcal O_{X,y}/\mathcal J_y$;",
      "Enlarged crop. Apply before the marker entry for p. 157."),
    F(156, "proof of (6.10.5): 'en prenant P = (1/m) R'; " + P157, "fraction 1 over m, then R", "P=R/m", "formula", None, "high",
      r"$P=R/m$", r"$P=\frac{1}{m}R$", "Apply before the marker entry for p. 157."),
    F(156, "proof of (6.10.5): 'On sait en outre (0, 16.2.3)'; " + P157, "bold 0", "plain 0", "convention", 2, "high",
      r"(0, 16.2.3)", r"(\textbf{0}, 16.2.3)", "Apply before the marker entry for p. 157."),
]
# ---------------------------------------------------------------- p. 157
L += [
    F(157, "proof of (6.10.5) (iii): 'q = B^+ = ⊕_{n≥1} B_n'", "B^+ (raised plus)", "B_+", "formula", None, "high",
      r"\mathfrak q=B_+=", r"\mathfrak q=B^+=", "Enlarged crop."),
    F(157, "proof of (6.10.5) (iii): 'Appliquons (0, 16.2.7)'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0, 16.2.7)", r"(\textbf{0}, 16.2.7)", ""),
    F(157, "proof of (6.10.5) (iii): 'Pour n ≥ sup_i (n_i)'", "sup with the index i below", "\\sup(n_i) (no index)", "formula", None, "high",
      r"n\geq\sup(n_i)", r"n\geq\sup_i(n_i)", "Enlarged crop."),
    F(157, "proof of (6.10.5) (iii): 'on a donc (0_I, 1.7.5) dans Spec(A)'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0$_{\rm I}$, 1.7.5)", r"(\textbf{0}$_{\rm I}$, 1.7.5)", ""),
    F(157, "proof of (6.10.5) (iii): 'Comme d'autre part les f_i appartiennent à S, on a'", "'à S' (roman S)", "'à $\\mathfrak J$'",
      "misprint_in_print", None, "high", r"appartiennent à⏎$\mathfrak J$", r"appartiennent à⏎$S$",
      "Enlarged crop. The f_i lie in 𝔍 (f_i ∈ 𝔍^{n_i}), which gives V(𝔍) ⊂ V(Σ f_iA); S = gr_𝔍(A) is wrong here. The TeX silently corrected the misprint; the fix restores the printed reading.",
      corrected=r"appartiennent à $\mathfrak J$"),
    F(157, "proof of (6.10.5) (iii): 'on vient de voir que l'on a dim(A/J) = dim(A/(Σ f_iA)) et il reste'",
      "formula in the running text", "displayed formula", "other", None, "high",
      r"que l'on a⏎\[⏎\dim(A/\mathfrak J)=⏎\dim\left(A/\left(\sum_{i=1}^{d}f_iA\right)\right)⏎\]⏎et il reste",
      r"que l'on a⏎$\dim(A/\mathfrak J)=\dim(A/(\sum_{i=1}^{d}f_iA))$⏎et il reste", "Display vs inline only."),
    F(157, "proof of (6.10.5) (iii): 'à prouver (0, 16.3.7)'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0, 16.3.7)", r"(\textbf{0}, 16.3.7)", ""),
    F(157, "proof of (6.10.5) (iii): 'Or, soit p un idéal premier ...' after the display dim(A) ≥ dim(A/J)+d",
      "new indented paragraph", "no blank line after \\]", "other", None, "high",
      r"\]⏎Or, soit", r"\]⏎⏎Or, soit", ""),
    F(157, "proof of (6.10.5) (iii): '(0, 16.1.4) achève la démonstration'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0, 16.1.4)", r"(\textbf{0}, 16.1.4)", ""),
    F(157, "Proposition (6.10.6): 'tel que, our tout x ∈ U∩Y, on ait'", "'our tout' (no p; the line starts a letter-width to the right of the margin)",
      "'pour tout'", "misprint_in_print", None, "medium", r"tel que, pour tout", r"tel que, our tout",
      "Enlarged crop: no trace of the p. The TeX silently corrected the dropped letter; the fix restores the printed reading. Context: Proposition (6.10.5) to the end of the proof of (6.10.6) (pp. 156-158) is printed in a different typeface (lining figures, light script O, heavier italic letters), apparently a reset passage; weight differences of single letters there are not reported.",
      corrected=r"tel que, pour tout"),
    # marker for p. 157
    F(156, "page break 156/157: printed p. 157 begins with the proof of (6.10.5), 'Comme Y est supposé connexe, ...'",
      "p. 156 ends with the statement of (6.10.5) ('... ∩ Supp(F).'); p. 157 starts 'Comme Y est supposé connexe'",
      "\\oldpage[IV-2]{157} stands before 'Reste à prouver (iii)', one paragraph too late", "marker", None, "high",
      r"\begin{proof}⏎Comme $Y$ est supposé connexe", r"\oldpage[IV-2]{157}⏎\begin{proof}⏎Comme $Y$ est supposé connexe",
      "Inserts the marker before the proof. Apply after every other p. 156 and p. 157 entry above and together with the next entry, which removes the old marker; afterwards 'Comme Y est supposé connexe ... (5.1.12.2).' belongs to p. 157."),
    F(157, "page break 156/157: old marker before 'Reste à prouver (iii)'", "'Reste à prouver (iii)' is the second paragraph of p. 157",
      "\\oldpage[IV-2]{157} plus blank line before 'Reste à prouver'", "marker", None, "high",
      r"\oldpage[IV-2]{157}⏎⏎Reste à prouver", r"Reste à prouver",
      "Apply together with, and after, the previous entry. The blank line after '(5.1.12.2).' remains, so 'Reste à prouver' still opens a paragraph, as printed."),
]
# ---------------------------------------------------------------- p. 158
L += [
    F(158, "proof of (6.10.6): 'Y' = Y_red, qui est un sous-préschéma fermé intègre de Y'", "'intègre' italic", "upright", "italics", None, "high",
      r"fermé intègre de $Y$", r"fermé \emph{intègre} de $Y$", ""),
    F(158, "proof of (6.10.6): 'défini par un Idéal localement nilpotent K de O_Y'", "script K", "\\mathcal J", "symbol", None, "high",
      r"nilpotent⏎$\mathcal J$ de", r"nilpotent⏎$\mathcal K$ de",
      "Enlarged crop: wrong letter. The print names the nilradical of O_Y script K (J is used later in the proof for the Ideal of O_X defining Y)."),
    F(158, "proof of (6.10.6): '(I, 6.1.6)'", "bold I", "plain I", "convention", 2, "high", r"(I, 6.1.6)", r"(\textbf{I}, 6.1.6)", ""),
    F(158, "proof of (6.10.6): 'Il en résulte que gr•_K(O_Y) est un O_{Y'}-Module'", "gr•_K (script K)", "gr•_J", "symbol", None, "high",
      r"$\operatorname{gr}_{\mathcal J}^{\bullet}(\mathcal O_Y)$ est un", r"$\operatorname{gr}_{\mathcal K}^{\bullet}(\mathcal O_Y)$ est un",
      "Wrong letter, as above."),
    F(158, "proof of (6.10.6): 'O_{Y'}-Module cohérent'", "'cohérent' italic", "upright", "italics", None, "high",
      r"-Module cohérent, et comme", r"-Module \emph{cohérent}, et comme", ""),
    F(158, "proof of (6.10.6): 'tel que gr•_K(O_Y)|V soit localement libre'", "gr•_K (script K)", "gr•_J", "symbol", None, "high",
      r"$\operatorname{gr}_{\mathcal J}^{\bullet}(\mathcal O_Y)|V$", r"$\operatorname{gr}_{\mathcal K}^{\bullet}(\mathcal O_Y)|V$",
      "Wrong letter, as above."),
    F(158, "proof of (6.10.6): '(0_I, 5.2.7); autrement dit'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0$_{\rm I}$, 5.2.7)", r"(\textbf{0}$_{\rm I}$, 5.2.7)", ""),
    F(158, "proof of (6.10.6): 'O_Y est normalement plat le long de Y''", "'normalement plat' italic", "upright", "italics", None, "high",
      r"$\mathcal O_Y$ est normalement plat⏎le long", r"$\mathcal O_Y$ est \emph{normalement plat}⏎le long", ""),
    F(158, "proof of (6.10.6): 'le sous-préschéma fermé Y est intègre.'", "'intègre' italic", "upright", "italics", None, "high",
      r"fermé $Y$ est intègre.", r"fermé $Y$ est \emph{intègre}.", ""),
    F(158, "proof of (6.10.6): 'supposer que F est normalement plat le long de Y'", "'normalement plat' italic", "upright", "italics", None, "high",
      r"$\mathcal F$ est normalement plat le⏎long", r"$\mathcal F$ est \emph{normalement plat} le⏎long", ""),
    F(158, "proof of (6.10.6): 'et que prof(F_y/(Σ (f_i)_y F_y)) = 0 (0, 16.4.6).'", "formula in the running text", "displayed formula",
      "other", None, "high",
      r"et que⏎\[⏎\operatorname{prof}\left(\mathcal F_y/⏎\left(\sum_{i=1}^{p}(f_i)_y\mathcal F_y\right)\right)=0⏎\]⏎",
      r"et que⏎$\operatorname{prof}(\mathcal F_y/(\sum_{i=1}^{p}(f_i)_y\mathcal F_y))=0$⏎", "Display vs inline only."),
    F(158, "proof of (6.10.6): '(0, 16.4.6). Si J est l'Idéal'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0, 16.4.6). Si", r"(\textbf{0}, 16.4.6). Si", ""),
    F(158, "proof of (6.10.6): 'isomorphe à O_{X,y}/m_y (0, 16.4.6); le même raisonnement'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0, 16.4.6); le même", r"(\textbf{0}, 16.4.6); le même", ""),
    F(158, "proof of (6.10.6): '(compte tenu de (0_I, 5.3.8 et 5.2.7))'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0$_{\rm I}$, 5.3.8 et 5.2.7)", r"(\textbf{0}$_{\rm I}$, 5.3.8 et 5.2.7)", ""),
    F(158, "proof of (6.10.6): 'un sous-O_X-Module G' de G isomorphe à O_X/J'", "'sous-O_X-Module' and 'isomorphe à' italic", "upright",
      "italics", None, "high",
      r"un sous-$\mathcal O_X$-Module $\mathcal G'$ de $\mathcal G$⏎isomorphe à",
      r"un \emph{sous-$\mathcal O_X$-Module} $\mathcal G'$ de $\mathcal G$⏎\emph{isomorphe à}", "Enlarged crop."),
    F(158, "proof of (6.10.6): 'G' et G'' sont normalement plats le long de Y'", "'normalement plats' italic", "upright", "italics", None, "high",
      r"sont normalement plats le long", r"sont \emph{normalement plats} le long", ""),
    F(158, "proof of (6.10.6): 'donc est un O_{Y,x}-module libre'", "'libre' italic", "upright", "italics", None, "high",
      r"-module libre, et il en est", r"-module \emph{libre}, et il en est", ""),
    F(158, "proof of (6.10.6): 'qu'elle est G''_x-régulière (0, 15.1.19)'", "'régulière' italic", "upright", "italics", None, "high",
      r"qu'elle est $\mathcal G''_x$-régulière", r"qu'elle est $\mathcal G''_x$-\emph{régulière}", ""),
    F(158, "proof of (6.10.6): '(0, 15.1.19)'", "bold 0", "plain 0", "convention", 2, "high", r"(0, 15.1.19)", r"(\textbf{0}, 15.1.19)", ""),
    F(158, "proof of (6.10.6): 'le lemme (0, 15.1.18)'", "bold 0", "plain 0", "convention", 2, "high", r"(0, 15.1.18)", r"(\textbf{0}, 15.1.18)", ""),
    F(158, "proof of (6.10.6): 'Mais par hypothèse prof(...) = 0 (0, 16.4.6); par la caractérisation'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0, 16.4.6); par la", r"(\textbf{0}, 16.4.6); par la", ""),
    F(158, "proof of (6.10.6): 'par la caractérisation (0, 16.4.6) des modules'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0, 16.4.6) des modules", r"(\textbf{0}, 16.4.6) des modules", ""),
    F(158, "proof of (6.10.6): 'on en conclut que prof(G_x/(Σ g_j G_x)) = 0 = prof(F_x/(Σ f_i F_x + Σ g_j F_x)); la suite'",
      "formula in the running text", "displayed formula", "other", None, "high",
      r"on en conclut que⏎\[⏎\operatorname{prof}\left(\mathcal G_x/⏎\left(\sum_{j=1}^{q}g_j\mathcal G_x\right)\right)=0⏎=\operatorname{prof}\left(\mathcal F_x/⏎\left(\sum_{i=1}^{p}f_i\mathcal F_x+⏎\sum_{j=1}^{q}g_j\mathcal F_x\right)\right);⏎\]⏎",
      r"on en conclut que⏎$\operatorname{prof}(\mathcal G_x/(\sum_{j=1}^{q}g_j\mathcal G_x))=0=\operatorname{prof}(\mathcal F_x/(\sum_{i=1}^{p}f_i\mathcal F_x+\sum_{j=1}^{q}g_j\mathcal F_x))$;⏎",
      "Display vs inline only."),
    F(158, "proof of (6.10.6): 'est aussi G_x-régulière;'", "'régulière' italic", "upright", "italics", None, "high",
      r"est aussi $\mathcal G_x$-régulière;", r"est aussi $\mathcal G_x$-\emph{régulière};", ""),
    F(158, "proof of (6.10.6): 'on en déduit (0, 16.4.6) que prof(F_x) = p+q'", "bold 0", "plain 0", "convention", 2, "high",
      r"on en déduit (0, 16.4.6)", r"on en déduit (\textbf{0}, 16.4.6)", ""),
    F(158, "heading 6.11", "'... soient ouverts.' (full stop)", "no full stop", "punctuation", None, "high",
      r"$U_{C_n}(\mathcal F)$ soient ouverts}{", r"$U_{C_n}(\mathcal F)$ soient ouverts.}{",
      "GLOBAL_ISSUES 43/58; the stop goes into the first argument of \\texorpdfstring."),
    F(158, "Lemme (6.11.1): 'Soient X un préschéma localement noethérien, F un O_X-Module cohérent'", "Soient", "Soit", "word", None, "high",
      r"Soit $X$ un préschéma localement noethérien", r"Soient $X$ un préschéma localement noethérien", "GLOBAL_ISSUES 73 pattern."),
    F(158, "Lemme (6.11.1): 'la fonction x ⇝ dim.proj(F_x)'", "wavy arrow", "\\mapsto", "symbol", None, "high",
      r"$x\mapsto\operatorname{dim.proj}(\mathcal F_x)$", r"$x\leadsto\operatorname{dim.proj}(\mathcal F_x)$",
      "Enlarged crop (GLOBAL_ISSUES 33)."),
    F(158, "proof of (6.11.1): 'L_{n-1} → L_{n-2} → . . . → L_0 → M → 0'", "baseline dots (bottoms on the baseline of L and M)", "\\cdots",
      "symbol", None, "high", r"L_{n-2}\longrightarrow\cdots", r"L_{n-2}\longrightarrow\ldots", "GLOBAL_ISSUES 22."),
    F(158, "end of p. 158: the display 'L_{n-1} → ... → M → 0' is followed on p. 159 by 'où les L_i sont ...' (same sentence)",
      "no paragraph break", "blank line before \\oldpage[IV-2]{159}", "other", None, "high",
      r"M\longrightarrow0⏎\]⏎⏎", r"M\longrightarrow0⏎\]⏎",
      "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the p. 159 top-of-page entry."),
]
# ---------------------------------------------------------------- p. 159
L += [
    F(159, "top of page: 'où les L_i sont des A-modules libres ...' continues the sentence of p. 158", "no paragraph break (line starts at the margin)",
      "blank line after \\oldpage[IV-2]{159}", "other", None, "high",
      r"\oldpage[IV-2]{159}⏎⏎où les", r"\oldpage[IV-2]{159}⏎où les", "Apply together with the p. 158 end-of-page entry."),
    F(159, "proof of (6.11.1): 'des A-modules libres de type fini (A étant noethérien)'", "'de type fini' italic", "upright", "italics", None, "high",
      r"libres de type fini ($A$ étant", r"libres \emph{de type fini} ($A$ étant", ""),
    F(159, "proof of (6.11.1): '0 → R → L_{n-1} → L_{n-2} → . . . → L_0 → M → 0'", "baseline dots", "\\cdots", "symbol", None, "high",
      r"\longrightarrow\cdots\longrightarrow L_0", r"\longrightarrow\ldots\longrightarrow L_0", "GLOBAL_ISSUES 22."),
    F(159, "proof of (6.11.1): '0 → R_x → (L_{n-1})_x → . . . → (L_0)_x → M_x → 0'", "baseline dots", "\\cdots", "symbol", None, "high",
      r"(L_{n-1})_x\longrightarrow\cdots", r"(L_{n-1})_x\longrightarrow\ldots", "GLOBAL_ISSUES 22."),
    F(159, "proof of (6.11.1): 'un A_x-module libre de type fini'", "'libre' italic", "upright", "italics", None, "high",
      r"$A_x$-module libre de type fini", r"$A_x$-module \emph{libre} de type fini", ""),
    F(159, "proof of (6.11.1): '(0_III, 10.1.3)'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0$_{\rm III}$, 10.1.3)", r"(\textbf{0}$_{\rm III}$, 10.1.3)", ""),
    F(159, "proof of (6.11.1): '(0_I, 5.2.7)'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0$_{\rm I}$, 5.2.7)", r"(\textbf{0}$_{\rm I}$, 5.2.7)", ""),
    F(159, "Proposition (6.11.2): 'dans un schéma régulier (5.11.1); soit'", "reference upright", "italic", "convention", 6, "high",
      r"régulier (5.11.1); soit", r"régulier \textup{(5.11.1)}; soit", "Reference printed upright inside the italic statement."),
    F(159, "Proposition (6.11.2), label (i)", "(i) upright", "\\item[(i)] (italic)", "convention", 6, "high",
      r"\item[(i)] (M. Auslander)", r"\item[\textup{(i)}] \textup{(M. Auslander)}",
      "GLOBAL_ISSUES 16. One edit for this finding and the next ('(M. Auslander)' upright)."),
    F(159, "Proposition (6.11.2) (i): '(M. Auslander)'", "upright", "italic", "convention", 6, "high", None, None,
      "Covered by the edit of the preceding finding."),
    F(159, "Proposition (6.11.2) (i): 'La fonction x ⇝ coprof(F_x)'", "wavy arrow", "\\mapsto", "symbol", None, "high",
      r"$x\mapsto\operatorname{coprof}(\mathcal F_x)$", r"$x\leadsto\operatorname{coprof}(\mathcal F_x)$", "GLOBAL_ISSUES 33."),
    F(159, "Proposition (6.11.2) (i): '(autrement dit, pour tout entier n, l'ensemble U_{C_n}(F) des x∈X tels que coprof(F_x) ≤ n est ouvert).'",
      "parenthesis upright up to 'est'; 'ouvert' italic", "all italic", "convention", 6, "high",
      r"(autrement dit, pour tout entier $n$, l'ensemble⏎$U_{C_n}(\mathcal F)$ des $x\in X$ tels que⏎$\operatorname{coprof}(\mathcal F_x)\leq n$ est ouvert).",
      r"\textup{(autrement dit, pour tout entier $n$, l'ensemble⏎$U_{C_n}(\mathcal F)$ des $x\in X$ tels que⏎$\operatorname{coprof}(\mathcal F_x)\leq n$ est} ouvert).",
      "Enlarged crop. 'ouvert' keeps the statement's italic (no \\emph inside the italic environment)."),
    F(159, "Proposition (6.11.2), label (ii)", "(ii) upright", "\\item[(ii)] (italic)", "convention", 6, "high",
      r"\item[(ii)] Pour tout entier", r"\item[\textup{(ii)}] Pour tout entier", "GLOBAL_ISSUES 16."),
    F(159, "proof of (6.11.2) (i): 'et comme coprof(G_x) = 0 pour y ∈ Y — X'", "coprof(G_x) (subscript x)", "coprof(G_y)",
      "misprint_in_print", None, "high", r"(\mathcal G_y)=0$ pour", r"(\mathcal G_x)=0$ pour",
      "Enlarged crop. The point is y ∈ Y—X, so the stalk must be G_y. The TeX silently corrected the misprint; the fix restores the printed reading.",
      corrected=r"\operatorname{coprof}(\mathcal G_y)=0"),
    F(159, "proof of (6.11.2) (i): 'pour y ∈ Y — X'", "long dash (set difference, bar 40 px; = bars 34-35 px)", "minus sign", "convention", 7, "high",
      r"$y\in Y-X$", r"$y\in Y\setmin X$", "\\setmin pending the convention-7 decision."),
    F(159, "proof of (6.11.2) (i): 'au cas où X est un schéma affine régulier.'", "'régulier' italic", "upright", "italics", None, "high",
      r"schéma affine régulier. On sait", r"schéma affine \emph{régulier}. On sait", ""),
    F(159, "proof of (6.11.2) (i): 'On sait alors (0, 17.3.4)'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0, 17.3.4)", r"(\textbf{0}, 17.3.4)", ""),
    F(159, "proof of (6.11.2) (i): display 'prof(F_x) = dim(O_{X,x}) — dim.proj(F_x).'", "long dash (bar 41 px; = bars 34-35 px)",
      "minus sign", "convention", 7, "high", r"\dim(\mathcal O_{X,x})-⏎\operatorname{dim.proj}", r"\dim(\mathcal O_{X,x})\setmin⏎\operatorname{dim.proj}",
      "Long dash for subtraction (GLOBAL_ISSUES 23)."),
    F(159, "proof of (6.11.2) (i): 'D'autre part, si S est ...' after the display", "new indented paragraph", "no blank line after \\]",
      "other", None, "high", r"\]⏎D'autre part", r"\]⏎⏎D'autre part", ""),
    F(159, "proof of (6.11.2) (i): 'dim(F_x) = codim(closure of {x}, S) (5.1.12.1)'", "bar over {x} (closure)", "\\{x\\} without the bar",
      "formula", None, "high", r"\operatorname{codim}(\{x\},S)", r"\operatorname{codim}(\overline{\{x\}},S)", "Enlarged crop."),
    F(159, "proof of (6.11.2) (i): display 'dim(F_x) = dim(O_{X,x}) — codim_x(S, X)'", "long dash (bar 42 px)", "minus sign", "convention", 7, "high",
      r"\dim(\mathcal O_{X,x})-\operatorname{codim}_x(S,X)", r"\dim(\mathcal O_{X,x})\setmin\operatorname{codim}_x(S,X)", ""),
    F(159, "proof of (6.11.2) (i): 'et a fortiori biéquidimensionnel'", "'a fortiori' italic", "upright", "italics", None, "high",
      r"et a fortiori⏎biéquidimensionnel", r"et \emph{a fortiori}⏎biéquidimensionnel", ""),
    F(159, "proof of (6.11.2) (i): '(0, 16.5.12)'", "bold 0", "plain 0", "convention", 2, "high", r"(0, 16.5.12)", r"(\textbf{0}, 16.5.12)", ""),
    F(159, "(6.11.2.1): 'coprof(F_x) = dim.proj(F_x) — codim_x(S, X)'", "long dash (bar 42 px)", "minus sign", "convention", 7, "high",
      r"\operatorname{dim.proj}(\mathcal F_x)-\operatorname{codim}_x(S,X)", r"\operatorname{dim.proj}(\mathcal F_x)\setmin\operatorname{codim}_x(S,X)", ""),
    F(159, "proof of (6.11.2) (i): 'et de (0, 14.2.6).'", "bold 0", "plain 0", "convention", 2, "high", r"(0, 14.2.6)", r"(\textbf{0}, 14.2.6)", ""),
]
# ---------------------------------------------------------------- p. 160 file (printed p. 159)
# Dropped: findings_160_164.json already has these four edits (identical), with their ordering notes.
L_p160_dropped = [
    F(160, "printed p. 159, last lines, proof of (6.11.2) (ii): 'les Z_n = X — U_{C_n}(F)' (text in page_160.tex, before the marker move)",
      "long dash (set difference, bar 42 px)", "minus sign", "convention", 7, "high",
      r"$Z_n=X-U_{C_n}(\mathcal F)$", r"$Z_n=X\setmin U_{C_n}(\mathcal F)$",
      "OUTSIDE pp. 155-159 (page_160.tex). Apply before the two marker entries below."),
    F(160, "printed p. 159, last lines: 'l'intersection des Z_n est vide;' (text in page_160.tex, before the marker move)",
      "'vide' italic", "upright", "italics", None, "high", r"est vide; comme", r"est \emph{vide}; comme",
      "OUTSIDE pp. 155-159 (page_160.tex). Apply before the two marker entries below."),
    F(160, "page break 159/160: printed p. 159 ends '... on peut supposer qu'il existe un m'; p. 160 begins 'tel que Z_m = ∅.'",
      "(ii) Comme les U_{C_n}(F) ... qu'il existe un m (8 lines) are on p. 159",
      "\\oldpage[IV-2]{160} stands before '\\item[(ii)] Comme les', eight lines too early", "marker", None, "high",
      r"il existe un $m$ tel⏎que $Z_m=\varnothing$", r"il existe un $m$⏎\oldpage[IV-2]{160}⏎tel⏎que $Z_m=\varnothing$",
      "OUTSIDE pp. 155-159 (page_160.tex). Inserts the marker mid-sentence on its own line. Apply after every other p. 160 entry (including those of the pp. 160-164 batch for this text) and together with the next entry, which removes the old marker."),
    F(160, "page break 159/160: old marker before '\\item[(ii)] Comme les'", "'(ii) Comme les ...' is on p. 159",
      "\\oldpage[IV-2]{160} plus blank line", "marker", None, "high",
      r"\oldpage[IV-2]{160}⏎⏎\item[(ii)] Comme les", r"\item[(ii)] Comme les",
      "OUTSIDE pp. 155-159. Apply together with, and after, the previous entry. The blank line after '(0, 14.2.6).' remains before \\item[(ii)]; afterwards '(ii) Comme les ... un m' belongs to p. 159."),
]

json.dump(L, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---------------- checks: each old occurs once in its page_NNN.tex (LF), and sequential application on the source works
bad = 0
for x in L:
    if not x["fix"]:
        continue
    t = (RUN / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    c = t.count(x["fix"]["old"])
    if c != 1:
        bad += 1
        print("COUNT", c, x["page"], repr(x["fix"]["old"][:60]))
src_path = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex"
src = src_path.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-2\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(t)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


t = src
for x in L:
    if not x["fix"]:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    if seg.count(x["fix"]["old"]) != 1:
        bad += 1
        print("SEQ", seg.count(x["fix"]["old"]), x["page"], repr(x["fix"]["old"][:60]))
        continue
    t = t[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + t[e:]
print("findings", len(L), "problems", bad)
from collections import Counter
cnt = Counter()
for x in L:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for p in sorted({x["page"] for x in L}):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
# show the simulated result around the moved markers
for pat in (r"\oldpage[IV-2]{157}", r"\oldpage[IV-2]{159}", r"\oldpage[IV-2]{160}", r"\oldpage[IV-2]{155}"):
    i = t.find(pat)
    print("----", pat, "count", t.count(pat))
    print(t[i - 160:i + 120])
