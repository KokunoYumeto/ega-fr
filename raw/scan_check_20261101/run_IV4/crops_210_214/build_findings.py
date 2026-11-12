"""Build findings_210_214.json (EGA IV-4 pp. 210-214, ega4-18-fr.tex, sections 19.6-19.7).
'<NL>' in old/new stands for a line break. Every 'old' is asserted to occur in its page text."""
import json

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
OUT = RUN + r"\findings_210_214.json"
F = []
PAGES = {}
for n in range(210, 215):
    PAGES[n] = open(rf"{RUN}\page_{n:03d}.tex", encoding="utf-8", newline="").read().replace("\r\n", "\n")


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    fix = None if old is None else {"old": old.replace("<NL>", "\n"), "new": new.replace("<NL>", "\n")}
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


K_NOTE = "Wrong letter \\mathfrak R for the print's Fraktur K (GLOBAL_ISSUES 63; glyph as on p. 188, crop c211_K1.png); the ideals are 𝔍, 𝔎, 𝔏 = 𝔍 + 𝔎."
B_NOTE = "The print's gr has a raised bullet (gr^•), the TeX ^* (crop c210_grJ.png)."
KB_NOTE = K_NOTE + " " + B_NOTE

# ---------------------------------------------------------------- p. 210 (with the 209/210 boundary)
add(210, "top of p. 210: 'où les flèches verticales sont les homomorphismes canoniques ...'",
    "continues the sentence after the display (19.6.1.1), flush left, no indent (page_210_s1.png)",
    "blank line after \\oldpage[IV-4]{210}", "marker", None, "high",
    r"\oldpage[IV-4]{210}<NL><NL>où les flèches", r"\oldpage[IV-4]{210}<NL>où les flèches",
    "BOUNDARY FIX (page break 209/210). The marker is at the right place; both blank lines must go (\\oldpage ends with "
    "\\ignorespaces). The blank line BEFORE the marker (end of the p. 209 segment) is already gone in the current source "
    "(findings_205_209, applied); this edit removes the one after it.")
add(210, "(19.6.1), display 'R''_k = R_k + 𝔍R_{k-1} + ... + 𝔍^{k-1}R_1 + 𝔍^kR_0'",
    "baseline dots between the plus signs (crops c210_disp1.png, c210_dots.png)", "\\cdots", "symbol", None, "high",
    r"+\cdots+\mathfrak J^{k-1}R_1", r"+\ldots+\mathfrak J^{k-1}R_1", "")
add(210, "(19.6.2), l. 1: 'On a défini en (0, 15.1.5.2)'", "bare bold 0 (crop c210_ref0b.png)", "($0$, 15.1.5.2)",
    "convention", 2, "high", r"($0$, 15.1.5.2)", r"(\textbf{0}, 15.1.5.2)", "")
add(210, "(19.6.2), display line ψ_N", "no punctuation at the end of the line (crop c210_psi.png)", "comma after gr'_•(N)",
    "punctuation", None, "high", r"\operatorname{gr}_\bullet'(N),\\", r"\operatorname{gr}_\bullet'(N)\\", "")
add(210, "(19.6.2), display line ψ_M", "no punctuation at the end of the line (crop c210_psi.png)", "comma after gr'_•(M)",
    "punctuation", None, "high", r"\operatorname{gr}_\bullet'(M),\\", r"\operatorname{gr}_\bullet'(M)\\", "")
add(210, "(19.6.2), display line ψ_R", "no punctuation at the end of the display (crop c210_psi.png)",
    "comma after gr''_•(R)", "punctuation", None, "high",
    r"\operatorname{gr}_\bullet''(R),<NL>\end{align*}", r"\operatorname{gr}_\bullet''(R)<NL>\end{align*}", "")
add(210, "diagram (19.6.2.1): label j' of the upper left vertical arrow",
    "j' on the LEFT of the arrow (gr'(j) on the right of the right-hand arrow) (crop c210_diag_top.png)",
    "\\ar[d]^{j'}: label on the right", "formula", None, "high", r"\ar[d]^{j'}", r"\ar[d]_{j'}",
    "In xymatrix ^ puts the label of a downward arrow on its right, _ on its left.")
add(210, "diagram (19.6.2.1): label p' of the lower left vertical arrow",
    "p' on the LEFT of the arrow (crop c210_diag_mid.png)", "\\ar[d]^{p'}: label on the right", "formula", None, "high",
    r"\ar[d]^{p'}", r"\ar[d]_{p'}", "")
for lab, tlab in [("a)", "a)"), ("b)", "b)"), ("c)", "c)"), ("d)", "d)"), ("d$'$)", "d$'$)"), ("e)", "e)"), ("f)", "f)")]:
    shown = lab.replace("$'$", "'")
    add(210, f"Proposition (19.6.3), label {shown}",
        "label upright (crops c210_prop_a_c.png, c210_prop_d_f.png)", "\\item[" + lab + "] set italic by the environment",
        "convention", 6, "high", "\\item[" + lab + "]", "\\item[\\textup{" + tlab + "}]",
        "GLOBAL_ISSUES 16/88 (labels upright inside italic statements).")
add(210, "Proposition (19.6.3) c): '(autrement dit gr'_•(R) est engendré comme gr^•_𝔍(A)-module par Im(gr_•(R) → gr'_•(R)))'",
    "the whole parenthesis roman, parentheses upright; gr with a raised bullet (crops c210_prop_a_c.png, c210_grJ.png)",
    "italic (environment); \\operatorname{gr}_{\\mathfrak J}^*", "convention", 6, "high",
    r"(autrement dit $\operatorname{gr}_\bullet'(R)$ est engendré comme $\operatorname{gr}_{\mathfrak J}^*(A)$-module par $\operatorname{Im}(\operatorname{gr}_\bullet(R)\to\operatorname{gr}_\bullet'(R))$)",
    r"\textup{(autrement dit $\operatorname{gr}_\bullet'(R)$ est engendré comme $\operatorname{gr}_{\mathfrak J}^\bullet(A)$-module par $\operatorname{Im}(\operatorname{gr}_\bullet(R)\to\operatorname{gr}_\bullet'(R))$)}",
    "One edit for convention 6 (roman parenthesis) and the symbol fix gr^• for gr^*; count it under both.")

# ---------------------------------------------------------------- p. 211
for lab in ["f$'$)", "g)", "h)"]:
    shown = lab.replace("$'$", "'")
    add(211, f"Proposition (19.6.3), label {shown}", "label upright (page_211_s1.png)",
        "\\item[" + lab + "] set italic by the environment", "convention", 6, "high",
        "\\item[" + lab + "]", "\\item[\\textup{" + lab + "}]", "GLOBAL_ISSUES 16/88.")
add(211, "Proposition (19.6.3): 'On a alors les implications suivantes :'",
    "new paragraph, indented like the item labels (page_211_s1.png)", "follows \\end{enumerate} without a blank line: no indent",
    "other", None, "high", r"\end{enumerate}<NL>On a alors les implications suivantes:",
    r"\end{enumerate}<NL><NL>On a alors les implications suivantes:", "Paragraph after the list, indented as printed (GLOBAL_ISSUES 80 pattern).")
add(211, "Proposition (19.6.3), diagram of implications 'a) ⇒ e) ⇒ b) ⇔ c) ⇔ h)', 'g) ⇒ d) ⇔ d') ⇔ f) ⇔ f')'",
    "all ten labels upright roman (crop c211_diag.png)", "labels in math mode: italic letters", "convention", 6, "high",
    r"  a) \ar@{=>}[r] \ar@{=>}[dr] & e) \ar@{=>}[r] \ar@{=>}[dr] & b) \ar@{<=>}[r] & c) \ar@{<=>}[r] & h) \\<NL>  & g) \ar@{=>}[r] & d) \ar@{<=>}[r] & d') \ar@{<=>}[r] & f) \ar@{<=>}[r] & f')",
    r"  \textup{a)} \ar@{=>}[r] \ar@{=>}[dr] & \textup{e)} \ar@{=>}[r] \ar@{=>}[dr] & \textup{b)} \ar@{<=>}[r] & \textup{c)} \ar@{<=>}[r] & \textup{h)} \\<NL>  & \textup{g)} \ar@{=>}[r] & \textup{d)} \ar@{<=>}[r] & \textup{d$'$)} \ar@{<=>}[r] & \textup{f)} \ar@{<=>}[r] & \textup{f$'$)}",
    "GLOBAL_ISSUES 88 (labels upright inside italic statements); arrows unchanged.")
add(211, "Proposition (19.6.3): 'En outre, lorsque tout module quotient ...'",
    "new indented paragraph after the diagram (page_211_s2.png)", "follows \\] without a blank line: no indent",
    "other", None, "high", r"\]<NL>En outre, lorsque", r"\]<NL><NL>En outre, lorsque",
    "Paragraph after a display, indented as printed (GLOBAL_ISSUES 47 pattern).")
add(211, "Proposition (19.6.3): '(ce qui sera le cas lorsque A est noethérien, que les f_i appartiennent au radical de A et que les gr_k(M) sont des A-modules de type fini)'",
    "the whole parenthesis roman, parentheses upright (page_211_s2.png)", "italic (environment)", "convention", 6, "high",
    r"(ce qui sera le cas lorsque $A$ est noethérien, que les $f_i$ appartiennent au radical de $A$ et que les $\operatorname{gr}_k(M)$ sont des $A$-modules de type fini)",
    r"\textup{(ce qui sera le cas lorsque $A$ est noethérien, que les $f_i$ appartiennent au radical de $A$ et que les $\operatorname{gr}_k(M)$ sont des $A$-modules de type fini)}", "")
add(211, "Proposition (19.6.3): 'alors les conditions a) à h) sont toutes équivalentes'",
    "labels a), h) upright, 'à' italic (page_211_s2.png)", "$a)$ à $h)$: italic letters", "convention", 6, "high",
    r"alors les conditions $a)$ à $h)$ sont toutes", r"alors les conditions \textup{a)} à \textup{h)} sont toutes",
    "GLOBAL_ISSUES 88.")
add(211, "proof of (19.6.3): 'l'équivalence de d) et f) résulte du diagramme'", "labels italic, parentheses included (page_211_s2.png)",
    "$d)$, $f)$: upright parentheses", "italics", None, "high",
    r"l'équivalence de $d)$ et $f)$ résulte", r"l'équivalence de \emph{d)} et \emph{f)} résulte", "GLOBAL_ISSUES 88.")
add(211, "proof of (19.6.3): 'ainsi que celle de d') et f')'", "labels italic", "$d')$, $f')$", "italics", None, "high",
    r"ainsi que celle de $d')$ et $f')$;", r"ainsi que celle de \emph{d$'$)} et \emph{f$'$)};", "GLOBAL_ISSUES 88.")
add(211, "proof of (19.6.3): 'par ailleurs f) et f') sont trivialement équivalentes'", "labels italic", "$f)$, $f')$", "italics", None, "high",
    r"par ailleurs $f)$ et $f')$ sont", r"par ailleurs \emph{f)} et \emph{f$'$)} sont", "GLOBAL_ISSUES 88.")
add(211, "proof of (19.6.3): 'l'équivalence de d), d'), f) et f')'", "labels italic", "$d)$, $d')$, $f)$, $f')$", "italics", None, "high",
    r"l'équivalence de $d)$, $d')$, $f)$ et $f')$.", r"l'équivalence de \emph{d)}, \emph{d$'$)}, \emph{f)} et \emph{f$'$)}.",
    "GLOBAL_ISSUES 88.")
add(211, "proof of (19.6.3): 'l'équivalence de b) et c) découle aussi'", "labels italic (page_211_s2.png)", "$b)$, $c)$", "italics", None, "high",
    r"l'équivalence de $b)$ et $c)$ découle", r"l'équivalence de \emph{b)} et \emph{c)} découle", "GLOBAL_ISSUES 88.")
add(211, "proof of (19.6.3): 'la condition c) équivaut à dire'", "label italic", "$c)$", "italics", None, "high",
    r"la condition $c)$ équivaut à dire", r"la condition \emph{c)} équivaut à dire", "GLOBAL_ISSUES 88.")
add(211, "proof of (19.6.3): 'à la condition h); on a donc prouvé l'équivalence de b), c) et h)'",
    "labels italic (page_211_s2.png, page_211_s3.png)", "$h)$, $b)$, $c)$, $h)$", "italics", None, "high",
    r"à la condition $h)$; on a donc prouvé l'équivalence de $b)$, $c)$ et $h)$.",
    r"à la condition \emph{h)}; on a donc prouvé l'équivalence de \emph{b)}, \emph{c)} et \emph{h)}.", "GLOBAL_ISSUES 88.")
add(211, "proof of (19.6.3): 'Il est trivial que e) équivaut à la conjonction de c) et d), donc aussi de b) et d).'",
    "labels italic (page_211_s3.png)", "math labels", "italics", None, "high",
    r"Il est trivial que $e)$ équivaut à la conjonction de $c)$ et $d)$, donc aussi de $b)$ et $d)$.",
    r"Il est trivial que \emph{e)} équivaut à la conjonction de \emph{c)} et \emph{d)}, donc aussi de \emph{b)} et \emph{d)}.",
    "GLOBAL_ISSUES 88.")
add(211, "proof of (19.6.3): 'Notons maintenant que a) implique b) et que b) implique a)'", "labels italic", "math labels",
    "italics", None, "high",
    r"Notons maintenant que $a)$ implique $b)$ et que $b)$ implique $a)$ sous",
    r"Notons maintenant que \emph{a)} implique \emph{b)} et que \emph{b)} implique \emph{a)} sous", "GLOBAL_ISSUES 88.")
add(211, "proof of (19.6.3): 'les implications a) ⇒ g) ⇒ f'), et l'implication f') ⇒ a)'", "labels italic (page_211_s3.png)",
    "$a)\\Rightarrow g)\\Rightarrow f')$, $f')\\Rightarrow a)$", "italics", None, "high",
    r"les implications $a)\Rightarrow g)\Rightarrow f')$, et l'implication $f')\Rightarrow a)$ sous",
    r"les implications \emph{a)} $\Rightarrow$ \emph{g)} $\Rightarrow$ \emph{f$'$)}, et l'implication \emph{f$'$)} $\Rightarrow$ \emph{a)} sous",
    "GLOBAL_ISSUES 88 (same form as the p. 176 fix).")
add(211, "proof of (19.6.3): 'On a donc prouvé que a) entraîne e) (équivalente à la conjonction de b) et f'))'",
    "labels italic", "math labels", "italics", None, "high",
    r"On a donc prouvé que $a)$ entraîne $e)$ (équivalente à la conjonction de $b)$ et $f')$),",
    r"On a donc prouvé que \emph{a)} entraîne \emph{e)} (équivalente à la conjonction de \emph{b)} et \emph{f$'$)}),",
    "GLOBAL_ISSUES 88.")
add(211, "Corollaire (19.6.4), l. 1: 'Soient 𝔎 un idéal de A, 𝔏 = 𝔍 + 𝔎.'", "Fraktur K twice (crops c211_cor_l1.png, c211_K1.png)",
    "\\mathfrak R", "symbol", None, "high",
    r"Soient $\mathfrak R$ un idéal de $A$, $\mathfrak L=\mathfrak J+\mathfrak R$.",
    r"Soient $\mathfrak K$ un idéal de $A$, $\mathfrak L=\mathfrak J+\mathfrak K$.", K_NOTE)
add(211, "Corollaire (19.6.4): 'soit la filtration 𝔎-préadique'", "Fraktur K (crop c211_cor_l2.png)", "\\mathfrak R",
    "symbol", None, "high", r"soit la filtration $\mathfrak R$-préadique", r"soit la filtration $\mathfrak K$-préadique", K_NOTE)
add(211, "Corollaire (19.6.4): 'Considérons gr_•(R) (resp. gr'_•(R))'", "'(resp. ...)' roman, parentheses upright (crop c211_cor_l2.png)",
    "italic (environment)", "convention", 6, "high",
    r"(resp. $\operatorname{gr}_\bullet'(R)$)", r"\textup{(resp. $\operatorname{gr}_\bullet'(R)$)}", "")
add(211, "Corollaire (19.6.4): 'comme un module gradué sur gr^•_𝔎(A)'", "Fraktur K, raised bullet (crop c211_cor_l2.png)",
    "\\operatorname{gr}_{\\mathfrak R}^*", "symbol", None, "high",
    r"gradué sur $\operatorname{gr}_{\mathfrak R}^*(A)$", r"gradué sur $\operatorname{gr}_{\mathfrak K}^\bullet(A)$", KB_NOTE)
add(211, "Corollaire (19.6.4): '(resp. gr^•_𝔏(A)).'", "'(resp. ...)' roman, parentheses upright; raised bullet (crop c211_cor_l2.png)",
    "italic (environment); \\operatorname{gr}_{\\mathfrak L}^*", "convention", 6, "high",
    r"(resp. $\operatorname{gr}_{\mathfrak L}^*(A)$)", r"\textup{(resp. $\operatorname{gr}_{\mathfrak L}^\bullet(A)$)}",
    "One edit for convention 6 and the symbol fix gr^• for gr^*; count it under both.")
add(211, "Corollaire (19.6.4), label (i)", "label upright (page_211_s3.png)", "\\item[(i)] set italic by the environment",
    "convention", 6, "high", r"\item[(i)]", r"\item[\textup{(i)}]", "GLOBAL_ISSUES 16.")
add(211, "Corollaire (19.6.4) (i): 'comme gr^•_𝔎(A)-module. Alors'", "Fraktur K, raised bullet", "\\operatorname{gr}_{\\mathfrak R}^*",
    "symbol", None, "high", r"comme $\operatorname{gr}_{\mathfrak R}^*(A)$-module. Alors",
    r"comme $\operatorname{gr}_{\mathfrak K}^\bullet(A)$-module. Alors", KB_NOTE)
add(211, "Corollaire (19.6.4) (i): 'la condition c) de (19.6.3) équivaut'", "label c) and the reference upright (crop c211_i_cde.png)",
    "italic (environment)", "convention", 6, "high",
    r"la condition $c)$ de (19.6.3) équivaut", r"la condition \textup{c)} de \textup{(19.6.3)} équivaut", "GLOBAL_ISSUES 88.")
add(211, "Corollaire (19.6.4), label c')", "label upright (page_211_s4.png)", "\\item[c$'$)] set italic by the environment",
    "convention", 6, "high", r"\item[c$'$)]", r"\item[\textup{c$'$)}]", "GLOBAL_ISSUES 88.")
add(211, "Corollaire (19.6.4) c'): 'comme gr^•_𝔏(A)-module'", "raised bullet (page_211_s4.png)", "\\operatorname{gr}_{\\mathfrak L}^*",
    "symbol", None, "high",
    r"dans $\operatorname{gr}_\bullet'(R)$ par $\psi_R'$ engendre $\operatorname{gr}_\bullet'(R)$ comme $\operatorname{gr}_{\mathfrak L}^*(A)$-module",
    r"dans $\operatorname{gr}_\bullet'(R)$ par $\psi_R'$ engendre $\operatorname{gr}_\bullet'(R)$ comme $\operatorname{gr}_{\mathfrak L}^\bullet(A)$-module", B_NOTE)
add(211, "Corollaire (19.6.4), label (ii)", "label upright (crop c211_ii_ede.png)", "\\item[(ii)] set italic by the environment",
    "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]", "GLOBAL_ISSUES 16.")
add(211, "Corollaire (19.6.4) (ii): 'la condition e) de (19.6.3), et de plus'", "label e) and the reference upright (crop c211_ii_ede.png)",
    "italic (environment)", "convention", 6, "high",
    r"la condition $e)$ de (19.6.3), et de plus", r"la condition \textup{e)} de \textup{(19.6.3)}, et de plus", "GLOBAL_ISSUES 88.")
add(211, "Corollaire (19.6.4) (ii): '(ce qui sera le cas lorsque A est noethérien, les f_i dans le radical de A et les gr_k(N) des A-modules de type fini)'",
    "the whole parenthesis roman, parentheses upright (page_211_s4.png)", "italic (environment)", "convention", 6, "high",
    r"(ce qui sera le cas lorsque $A$ est noethérien, les $f_i$ dans le radical de $A$ et les $\operatorname{gr}_k(N)$ des $A$-modules de type fini)",
    r"\textup{(ce qui sera le cas lorsque $A$ est noethérien, les $f_i$ dans le radical de $A$ et les $\operatorname{gr}_k(N)$ des $A$-modules de type fini)}", "")
add(211, "Corollaire (19.6.4) (ii): 'engendre gr_•(R) comme gr^•_𝔎(A)-module, il faut'", "Fraktur K, raised bullet",
    "\\operatorname{gr}_{\\mathfrak R}^*", "symbol", None, "high",
    r"comme $\operatorname{gr}_{\mathfrak R}^*(A)$-module, il faut", r"comme $\operatorname{gr}_{\mathfrak K}^\bullet(A)$-module, il faut", KB_NOTE)
add(211, "Corollaire (19.6.4) (ii), last line: 'comme gr^•_𝔏(A)-module.'", "raised bullet", "\\operatorname{gr}_{\\mathfrak L}^*",
    "symbol", None, "high",
    r"que son image par $\psi_R'$ engendre $\operatorname{gr}_\bullet'(R)$ comme $\operatorname{gr}_{\mathfrak L}^*(A)$-module.",
    r"que son image par $\psi_R'$ engendre $\operatorname{gr}_\bullet'(R)$ comme $\operatorname{gr}_{\mathfrak L}^\bullet(A)$-module.", B_NOTE)

# ---------------------------------------------------------------- p. 212
add(212, "proof of (19.6.4) (i), display 'ψ_A : (gr^•_𝔎(A)⊗_A(A/𝔍))[T_1,...,T_n] → gr'_•(A) = gr^•_𝔏(A)'",
    "Fraktur K; raised bullets (page_212_s1.png)", "\\mathfrak R; ^* twice", "symbol", None, "high",
    r"\psi_A:(\operatorname{gr}_{\mathfrak R}^*(A)\otimes_A(A/\mathfrak J))[T_1,\ldots,T_n]\longrightarrow\operatorname{gr}_\bullet'(A)=\operatorname{gr}_{\mathfrak L}^*(A)",
    r"\psi_A:(\operatorname{gr}_{\mathfrak K}^\bullet(A)\otimes_A(A/\mathfrak J))[T_1,\ldots,T_n]\longrightarrow\operatorname{gr}_\bullet'(A)=\operatorname{gr}_{\mathfrak L}^\bullet(A)", KB_NOTE)
add(212, "proof of (19.6.4) (i): '(0, 15.1.5.2). Le fait'", "bare bold 0 (page_212_s1.png)", "($0$, 15.1.5.2)",
    "convention", 2, "high", r"($0$, 15.1.5.2). Le fait", r"(\textbf{0}, 15.1.5.2). Le fait", "")
add(212, "proof of (19.6.4) (i): 'la sous-gr^•_𝔏(A)-algèbre'", "raised bullet", "\\operatorname{gr}_{\\mathfrak L}^*",
    "symbol", None, "high", r"la sous-$\operatorname{gr}_{\mathfrak L}^*(A)$-algèbre", r"la sous-$\operatorname{gr}_{\mathfrak L}^\bullet(A)$-algèbre", B_NOTE)
add(212, "proof of (19.6.4) (i): 'd'où l'équivalence de c) et c')'", "labels italic (page_212_s1.png)", "$c)$, $c')$",
    "italics", None, "high", r"d'où l'équivalence de $c)$ et $c')$.", r"d'où l'équivalence de \emph{c)} et \emph{c$'$)}.",
    "GLOBAL_ISSUES 88.")
add(212, "proof of (19.6.4), second part: label 'ii)'",
    "'ii)' without the opening parenthesis, while the first part has '(i)' (crops c212_ii.png, c212_i.png)",
    "\\item[(ii)] (silently corrected)", "misprint_in_print", None, "high",
    r"\item[(ii)]", r"\item[ii)]",
    "Missing opening parenthesis in the print; the diplomatic text restores 'ii)'.", corrected=r"\item[(ii)]")
add(212, "proof of (19.6.4) (ii): 'Puisque e) est vérifiée, il en est de même de c)'", "labels italic (crop c212_ii.png)",
    "$e)$, $c)$", "italics", None, "high",
    r"Puisque $e)$ est vérifiée, il en est de même de $c)$", r"Puisque \emph{e)} est vérifiée, il en est de même de \emph{c)}",
    "GLOBAL_ISSUES 88. Does not overlap the misprint edit before it.")
add(212, "proof of (19.6.4) (ii): 'considéré comme gr^•_𝔏(A)-module'", "raised bullet", "\\operatorname{gr}_{\\mathfrak L}^*",
    "symbol", None, "high", r"considéré comme $\operatorname{gr}_{\mathfrak L}^*(A)$-module",
    r"considéré comme $\operatorname{gr}_{\mathfrak L}^\bullet(A)$-module", B_NOTE)
add(212, "proof of (19.6.4) (ii): '[T_1,...,T_n] comme gr^•_𝔏(A)-module, et en vertu'", "raised bullet (crop c212_line5z.png)",
    "\\operatorname{gr}_{\\mathfrak L}^*", "symbol", None, "high",
    r"[T_1,\ldots,T_n]$ comme $\operatorname{gr}_{\mathfrak L}^*(A)$-module, et en vertu",
    r"[T_1,\ldots,T_n]$ comme $\operatorname{gr}_{\mathfrak L}^\bullet(A)$-module, et en vertu", B_NOTE)
add(212, "proof of (19.6.4) (ii): 'remplacer l'anneau gr^•_𝔏(A) par (gr^•_𝔎(A)⊗_A(A/𝔍))'", "Fraktur K; raised bullets",
    "\\mathfrak R; ^* twice", "symbol", None, "high",
    r"remplacer l'anneau $\operatorname{gr}_{\mathfrak L}^*(A)$ par $(\operatorname{gr}_{\mathfrak R}^*(A)\otimes_A(A/\mathfrak J))",
    r"remplacer l'anneau $\operatorname{gr}_{\mathfrak L}^\bullet(A)$ par $(\operatorname{gr}_{\mathfrak K}^\bullet(A)\otimes_A(A/\mathfrak J))", KB_NOTE)
add(212, "proof of (19.6.4) (ii): 'sur l'anneau gr^•_𝔎(A)⊗_A(A/𝔍), ou aussi en tant que gr^•_𝔎(A)-module'",
    "Fraktur K twice; raised bullets (page_212_s2.png)", "\\mathfrak R; ^*", "symbol", None, "high",
    r"sur l'anneau $\operatorname{gr}_{\mathfrak R}^*(A)\otimes_A(A/\mathfrak J)$, ou aussi en tant que $\operatorname{gr}_{\mathfrak R}^*(A)$-module.",
    r"sur l'anneau $\operatorname{gr}_{\mathfrak K}^\bullet(A)\otimes_A(A/\mathfrak J)$, ou aussi en tant que $\operatorname{gr}_{\mathfrak K}^\bullet(A)$-module.", KB_NOTE)
add(212, "proof of (19.6.4) (ii): 'le sous-gr^•_𝔎(A)-module gradué'", "Fraktur K; raised bullet", "\\mathfrak R; ^*",
    "symbol", None, "high", r"le sous-$\operatorname{gr}_{\mathfrak R}^*(A)$-module gradué",
    r"le sous-$\operatorname{gr}_{\mathfrak K}^\bullet(A)$-module gradué", KB_NOTE)
add(212, "Théorème (19.7.1), l. 1: '𝔎 un idéal de A'", "Fraktur K (page_212_s2.png)", "\\mathfrak R", "symbol", None, "high",
    r"un anneau, $\mathfrak R$ un idéal de $A$", r"un anneau, $\mathfrak K$ un idéal de $A$", K_NOTE)
add(212, "Théorème (19.7.1): 'qui est (A/𝔎)-régulière'", "Fraktur K", "\\mathfrak R", "symbol", None, "high",
    r"qui est $(A/\mathfrak R)$-régulière", r"qui est $(A/\mathfrak K)$-régulière", K_NOTE)
add(212, "Théorème (19.7.1): '𝔍 = f_1A + ... + f_nA'", "baseline dots (page_212_s2.png)", "\\cdots", "symbol", None, "high",
    r"\mathfrak J=f_1A+\cdots+f_nA", r"\mathfrak J=f_1A+\ldots+f_nA", "")
add(212, "Théorème (19.7.1): '𝔏 = 𝔍 + 𝔎, M un A-module.'", "Fraktur K", "\\mathfrak R", "symbol", None, "high",
    r"$\mathfrak L=\mathfrak J+\mathfrak R$, $M$ un $A$-module.", r"$\mathfrak L=\mathfrak J+\mathfrak K$, $M$ un $A$-module.", K_NOTE)
add(212, "Théorème (19.7.1): 'On a dans ce cas (gr^•_𝔎(M))⊗_A(A/𝔍) = ... , car (𝔎^nM/𝔎^{n+1}M)⊗_A(A/𝔍) = ... M, et la dernière égalité'",
    "both formulas set in the running text (lines 2-3 of page_212_s3.png); Fraktur K throughout; raised bullets",
    "two displays (\\[...\\]); \\mathfrak R (12 times); ^* (3 times)", "formula", None, "high",
    r"On a dans ce cas<NL>\[<NL>  (\operatorname{gr}_{\mathfrak R}^*(M))\otimes_A(A/\mathfrak J)<NL>  =(\operatorname{gr}_{\mathfrak R}^*(M))\otimes_A(A/\mathfrak L)<NL>  =(\operatorname{gr}_{\mathfrak R}^*(M))\otimes_{A/\mathfrak R}(A/\mathfrak L),<NL>\]<NL>car<NL>\[<NL>  (\mathfrak R^nM/\mathfrak R^{n+1}M)\otimes_A(A/\mathfrak J)<NL>  =\mathfrak R^nM/(\mathfrak R^{n+1}+\mathfrak J\mathfrak R^n)M<NL>  =\mathfrak R^nM/(\mathfrak R^{n+1}+\mathfrak L\mathfrak R^n)M,<NL>\]<NL>et la dernière égalité",
    r"On a dans ce cas $(\operatorname{gr}_{\mathfrak K}^\bullet(M))\otimes_A(A/\mathfrak J)=(\operatorname{gr}_{\mathfrak K}^\bullet(M))\otimes_A(A/\mathfrak L)=(\operatorname{gr}_{\mathfrak K}^\bullet(M))\otimes_{A/\mathfrak K}(A/\mathfrak L)$, car $(\mathfrak K^nM/\mathfrak K^{n+1}M)\otimes_A(A/\mathfrak J)=\mathfrak K^nM/(\mathfrak K^{n+1}+\mathfrak J\mathfrak K^n)M=\mathfrak K^nM/(\mathfrak K^{n+1}+\mathfrak L\mathfrak K^n)M$, et la dernière égalité",
    "Inline as printed (GLOBAL_ISSUES 21 pattern); no connecting word lost or added. One edit for the layout and the symbol "
    "fixes inside it (𝔎 for \\mathfrak R 12 times, gr^• for gr^* 3 times); count it under both.")
add(212, "Théorème (19.7.1): 'résulte de Bourbaki, Alg., chap. II, 3^e éd., § 3, n° 7, cor. 2 de la prop. 6.'",
    "the reference roman with italic 'Alg.' (crop c212_bourbaki1.png)", "italic (environment), \\emph{Alg.} upright",
    "convention", 6, "high",
    r"résulte de Bourbaki, \emph{Alg.}, chap. II, 3\textsuperscript{e} éd., § 3, n\textsuperscript{o} 7, cor. 2 de la prop. 6.",
    r"résulte de \textup{Bourbaki, \emph{Alg.}, chap. II, 3\textsuperscript{e} éd., § 3, n\textsuperscript{o} 7, cor. 2 de la prop. 6}.",
    "Adjacent to (not overlapping) the previous edit.")
add(212, "Théorème (19.7.1), label a)", "label upright (page_212_s3.png)", "\\item[a)] set italic by the environment",
    "convention", 6, "high", r"\item[a)]", r"\item[\textup{a)}]", "GLOBAL_ISSUES 88.")
add(212, "Théorème (19.7.1) a): 'gr^•_𝔎(M) est un (A/𝔎)-module plat.'", "Fraktur K twice; raised bullet", "\\mathfrak R; ^*",
    "symbol", None, "high", r"$\operatorname{gr}_{\mathfrak R}^*(M)$ est un $(A/\mathfrak R)$-module plat.",
    r"$\operatorname{gr}_{\mathfrak K}^\bullet(M)$ est un $(A/\mathfrak K)$-module plat.", KB_NOTE)
add(212, "Théorème (19.7.1), label b)", "label upright", "\\item[b)] set italic by the environment",
    "convention", 6, "high", r"\item[b)]", r"\item[\textup{b)}]", "GLOBAL_ISSUES 88.")
add(212, "Théorème (19.7.1) b): 'gr^•_𝔏(M) est un (A/𝔏)-module plat et'", "raised bullet (crop c212_b0.png)", "^*",
    "symbol", None, "high", r"$\operatorname{gr}_{\mathfrak L}^*(M)$ est un $(A/\mathfrak L)$-module plat et",
    r"$\operatorname{gr}_{\mathfrak L}^\bullet(M)$ est un $(A/\mathfrak L)$-module plat et", B_NOTE)
add(212, "Théorème (19.7.1) b): 'l'homomorphisme canonique (0, 15.1.5.2)'", "bold 0; the reference upright (crop c212_b0.png)",
    "plain 0, italic reference", "convention", 2, "high",
    r"canonique ($0$, 15.1.5.2)", r"canonique \textup{(\textbf{0}, 15.1.5.2)}",
    "One edit for convention 2 (bold 0) and convention 6 (upright reference in the italic statement); count it under both.")
add(212, "Théorème (19.7.1) b), display 'ψ_M : ((gr^•_𝔎(M))⊗_A(A/𝔏))[T_1,...,T_n] → gr^•_𝔏(M)'", "Fraktur K; raised bullets",
    "\\mathfrak R; ^* twice", "symbol", None, "high",
    r"\psi_M:((\operatorname{gr}_{\mathfrak R}^*(M))\otimes_A(A/\mathfrak L))[T_1,\ldots,T_n]\longrightarrow\operatorname{gr}_{\mathfrak L}^*(M)",
    r"\psi_M:((\operatorname{gr}_{\mathfrak K}^\bullet(M))\otimes_A(A/\mathfrak L))[T_1,\ldots,T_n]\longrightarrow\operatorname{gr}_{\mathfrak L}^\bullet(M)", KB_NOTE)
add(212, "Théorème (19.7.1), label c)", "label upright", "\\item[c)] set italic by the environment",
    "convention", 6, "high", r"\item[c)]", r"\item[\textup{c)}]", "GLOBAL_ISSUES 88.")
add(212, "Théorème (19.7.1) c): '(gr^•_𝔎(M))⊗_{A/𝔎}(A/𝔏) est un (A/𝔏)-module plat et la suite f est (gr^•_𝔎(M))-régulière.'",
    "Fraktur K three times; raised bullets", "\\mathfrak R; ^*", "symbol", None, "high",
    r"$(\operatorname{gr}_{\mathfrak R}^*(M))\otimes_{A/\mathfrak R}(A/\mathfrak L)$ est un $(A/\mathfrak L)$-module plat et la suite $\mathbf f$ est $(\operatorname{gr}_{\mathfrak R}^*(M))$-régulière.",
    r"$(\operatorname{gr}_{\mathfrak K}^\bullet(M))\otimes_{A/\mathfrak K}(A/\mathfrak L)$ est un $(A/\mathfrak L)$-module plat et la suite $\mathbf f$ est $(\operatorname{gr}_{\mathfrak K}^\bullet(M))$-régulière.", KB_NOTE)
add(212, "Théorème (19.7.1), label d)", "label upright", "\\item[d)] set italic by the environment",
    "convention", 6, "high", r"\item[d)]", r"\item[\textup{d)}]", "GLOBAL_ISSUES 88.")
add(212, "Théorème (19.7.1) d): 'gr^•_𝔏(M) ... pour tout 𝔭 ∈ Ass_{A/𝔎}(A/𝔏), (gr^•_𝔎(M))_𝔭 est un (A/𝔎)_𝔭-module plat.'",
    "Fraktur K three times; raised bullets", "\\mathfrak R; ^*", "symbol", None, "high",
    r"$\operatorname{gr}_{\mathfrak L}^*(M)$ est un $(A/\mathfrak L)$-module plat, et pour tout $\mathfrak p\in\operatorname{Ass}_{A/\mathfrak R}(A/\mathfrak L)$, $(\operatorname{gr}_{\mathfrak R}^*(M))_{\mathfrak p}$ est un $(A/\mathfrak R)_{\mathfrak p}$-module plat.",
    r"$\operatorname{gr}_{\mathfrak L}^\bullet(M)$ est un $(A/\mathfrak L)$-module plat, et pour tout $\mathfrak p\in\operatorname{Ass}_{A/\mathfrak K}(A/\mathfrak L)$, $(\operatorname{gr}_{\mathfrak K}^\bullet(M))_{\mathfrak p}$ est un $(A/\mathfrak K)_{\mathfrak p}$-module plat.", KB_NOTE)
add(212, "Théorème (19.7.1): 'On a alors les implications'", "new paragraph, indented like the item labels (page_212_s3.png)",
    "follows \\end{enumerate} without a blank line: no indent", "other", None, "high",
    r"\end{enumerate}<NL>On a alors les implications", r"\end{enumerate}<NL><NL>On a alors les implications",
    "Paragraph after the list, indented as printed (GLOBAL_ISSUES 80 pattern).")
add(212, "Théorème (19.7.1), diagram 'a) ⇒ c) ⇒ b)', 'a) ⇒ d)'", "labels upright roman (page_212_s4.png)",
    "labels in math mode: italic letters", "convention", 6, "high",
    r"  a) \ar@{=>}[r] \ar@{=>}[dr] & c) \ar@{=>}[r] & b) \\<NL>  & d)",
    r"  \textup{a)} \ar@{=>}[r] \ar@{=>}[dr] & \textup{c)} \ar@{=>}[r] & \textup{b)} \\<NL>  & \textup{d)}", "GLOBAL_ISSUES 88.")
add(212, "Théorème (19.7.1): 'Lorsque tout quotient d'un sous-module ...'", "new indented paragraph after the diagram (page_212_s4.png)",
    "follows \\] without a blank line: no indent", "other", None, "high",
    r"\]<NL>Lorsque tout quotient", r"\]<NL><NL>Lorsque tout quotient", "Paragraph after a display, indented as printed.")
add(212, "Théorème (19.7.1): 'd'un gr^p_𝔎(M)'", "Fraktur K (crop c212_pgeq0.png)", "\\mathfrak R", "symbol", None, "high",
    r"d'un $\operatorname{gr}_{\mathfrak R}^p(M)$", r"d'un $\operatorname{gr}_{\mathfrak K}^p(M)$", K_NOTE)
add(212, "Théorème (19.7.1): '(p ≥ 0)'", "parentheses upright (crop c212_pgeq0.png)", "italic text parentheses (environment)",
    "convention", 6, "high", r"($p\geq0$)", r"\textup{($p\geq0$)}", "")
add(212, "Théorème (19.7.1): '(Bourbaki, Alg. comm., chap. III, § 5, n° 1)'", "roman, with italic 'Alg. comm.' (crop c212_lorsque.png)",
    "italic (environment), \\emph{Alg. comm.} upright", "convention", 6, "high",
    r"(Bourbaki, \emph{Alg. comm.}, chap. III, § 5, n\textsuperscript{o} 1)",
    r"\textup{(Bourbaki, \emph{Alg. comm.}, chap. III, § 5, n\textsuperscript{o} 1)}",
    "'III' measured: same stem width as the ordinary 'II' two lines above (6 px), not bold.")
add(212, "Théorème (19.7.1): 'les conditions a), b) et c) sont équivalentes'", "labels upright, 'et' italic (crop c212_lorsque.png)",
    "$a)$, $b)$, $c)$: italic letters", "convention", 6, "high",
    r"les conditions $a)$, $b)$ et $c)$ sont équivalentes.", r"les conditions \textup{a)}, \textup{b)} et \textup{c)} sont équivalentes.",
    "GLOBAL_ISSUES 88.")

# ---------------------------------------------------------------- p. 213
add(213, "Théorème (19.7.1), last paragraph: 'que la suite f est gr^•_𝔎(A)-régulière'", "Fraktur K; raised bullet (page_213_s1.png)",
    "\\mathfrak R; ^*", "symbol", None, "high",
    r"la suite $\mathbf f$ est $\operatorname{gr}_{\mathfrak R}^*(A)$-régulière et que",
    r"la suite $\mathbf f$ est $\operatorname{gr}_{\mathfrak K}^\bullet(A)$-régulière et que", KB_NOTE)
add(213, "Théorème (19.7.1): 'les conditions a), b), c), d) sont équivalentes'", "labels upright (page_213_s1.png)",
    "$a)$ ... $d)$: italic letters", "convention", 6, "high",
    r"les conditions $a)$, $b)$, $c)$, $d)$ sont équivalentes.",
    r"les conditions \textup{a)}, \textup{b)}, \textup{c)}, \textup{d)} sont équivalentes.", "GLOBAL_ISSUES 88.")
add(213, "proof of (19.7.1): 'L'implication a) ⇒ c) est immédiate'", "labels italic (page_213_s1.png)",
    "$a)\\Rightarrow c)$", "italics", None, "high",
    r"L'implication $a)\Rightarrow c)$ est immédiate", r"L'implication \emph{a)} $\Rightarrow$ \emph{c)} est immédiate", "GLOBAL_ISSUES 88.")
add(213, "proof of (19.7.1): '(0, 15.1.13)'", "bare bold 0", "($0$, 15.1.13)", "convention", 2, "high",
    r"($0$, 15.1.13)", r"(\textbf{0}, 15.1.13)", "")
add(213, "proof of (19.7.1): 'Si c) est vérifiée'", "label italic", "$c)$", "italics", None, "high",
    r"Si $c)$ est vérifiée", r"Si \emph{c)} est vérifiée", "GLOBAL_ISSUES 88.")
add(213, "proof of (19.7.1): 'gr^•_𝔎(M)⊗_A(A/𝔏) = gr^•_𝔎(M)⊗_{A/𝔎}(A/𝔏)'", "Fraktur K three times; raised bullets",
    "\\mathfrak R; ^*", "symbol", None, "high",
    r"en outre, $\operatorname{gr}_{\mathfrak R}^*(M)\otimes_A(A/\mathfrak L)=\operatorname{gr}_{\mathfrak R}^*(M)\otimes_{A/\mathfrak R}(A/\mathfrak L)$",
    r"en outre, $\operatorname{gr}_{\mathfrak K}^\bullet(M)\otimes_A(A/\mathfrak L)=\operatorname{gr}_{\mathfrak K}^\bullet(M)\otimes_{A/\mathfrak K}(A/\mathfrak L)$", KB_NOTE)
add(213, "proof of (19.7.1): 'de (gr^•_𝔎(M)⊗_A(A/𝔏))[T_1,...,T_n], et par suite de gr^•_𝔏(M)'", "Fraktur K; raised bullets",
    "\\mathfrak R; ^*", "symbol", None, "high",
    r"de même de $(\operatorname{gr}_{\mathfrak R}^*(M)\otimes_A(A/\mathfrak L))[T_1,\ldots,T_n]$, et par suite de $\operatorname{gr}_{\mathfrak L}^*(M)$",
    r"de même de $(\operatorname{gr}_{\mathfrak K}^\bullet(M)\otimes_A(A/\mathfrak L))[T_1,\ldots,T_n]$, et par suite de $\operatorname{gr}_{\mathfrak L}^\bullet(M)$", KB_NOTE)
add(213, "proof of (19.7.1): 'donc c) entraîne b). Le fait que a) implique b) montre aussitôt que a) implique aussi d).'",
    "labels italic (page_213_s1.png)", "math labels", "italics", None, "high",
    r"donc $c)$ entraîne $b)$. Le fait que $a)$ implique $b)$ montre aussitôt que $a)$ implique aussi $d)$.",
    r"donc \emph{c)} entraîne \emph{b)}. Le fait que \emph{a)} implique \emph{b)} montre aussitôt que \emph{a)} implique aussi \emph{d)}.",
    "GLOBAL_ISSUES 88.")
add(213, "proof of (19.7.1): 'Lorsque tout quotient d'un gr^p_𝔎(M)'", "Fraktur K", "\\mathfrak R", "symbol", None, "high",
    r"Lorsque tout quotient d'un $\operatorname{gr}_{\mathfrak R}^p(M)$", r"Lorsque tout quotient d'un $\operatorname{gr}_{\mathfrak K}^p(M)$", K_NOTE)
add(213, "proof of (19.7.1): 'que la condition b) entraîne que'", "label italic", "$b)$", "italics", None, "high",
    r"que la condition $b)$ entraîne que", r"que la condition \emph{b)} entraîne que", "GLOBAL_ISSUES 88.")
add(213, "proof of (19.7.1): '(gr^•_𝔎(M))-régulière; en outre, comme (gr^•_𝔎(M)⊗_{A/𝔎}(A/𝔏))[T_1,...,T_n], isomorphe à gr^•_𝔏(M)'",
    "Fraktur K three times; raised bullets (page_213_s1.png, page_213_s2.png)", "\\mathfrak R; ^*", "symbol", None, "high",
    r"est $(\operatorname{gr}_{\mathfrak R}^*(M))$-régulière; en outre, comme $(\operatorname{gr}_{\mathfrak R}^*(M)\otimes_{A/\mathfrak R}(A/\mathfrak L))[T_1,\ldots,T_n]$, isomorphe à $\operatorname{gr}_{\mathfrak L}^*(M)$",
    r"est $(\operatorname{gr}_{\mathfrak K}^\bullet(M))$-régulière; en outre, comme $(\operatorname{gr}_{\mathfrak K}^\bullet(M)\otimes_{A/\mathfrak K}(A/\mathfrak L))[T_1,\ldots,T_n]$, isomorphe à $\operatorname{gr}_{\mathfrak L}^\bullet(M)$", KB_NOTE)
add(213, "proof of (19.7.1): 'il en est de même de gr^•_𝔎(M)⊗_{A/𝔎}(A/𝔏), qui en est un facteur direct'",
    "Fraktur K twice; raised bullet", "\\mathfrak R; ^*", "symbol", None, "high",
    r"il en est de même de $\operatorname{gr}_{\mathfrak R}^*(M)\otimes_{A/\mathfrak R}(A/\mathfrak L)$, qui",
    r"il en est de même de $\operatorname{gr}_{\mathfrak K}^\bullet(M)\otimes_{A/\mathfrak K}(A/\mathfrak L)$, qui", KB_NOTE)
add(213, "proof of (19.7.1): 'que b) entraîne alors c). D'autre part, sous la même hypothèse, c) entraîne a)'",
    "labels italic (page_213_s2.png)", "math labels", "italics", None, "high",
    r"cela prouve donc que $b)$ entraîne alors $c)$. D'autre part, sous la même hypothèse, $c)$ entraîne $a)$ en vertu",
    r"cela prouve donc que \emph{b)} entraîne alors \emph{c)}. D'autre part, sous la même hypothèse, \emph{c)} entraîne \emph{a)} en vertu",
    "GLOBAL_ISSUES 88.")
add(213, "proof of (19.7.1): '(0, 15.1.21)'", "bare bold 0 (crop c213_refs.png)", "($0$, 15.1.21)", "convention", 2, "high",
    r"($0$, 15.1.21)", r"(\textbf{0}, 15.1.21)", "")
add(213, "proof of (19.7.1): '(0_III, 10.2.1)'", "bold 0 with a roman subscript III (crop c213_0III.png)", "plain 0",
    "convention", 2, "high", r"($0_{\mathrm{III}}$, 10.2.1)", r"($\mathbf{0}_{\mathrm{III}}$, 10.2.1)", "")
add(213, "proof of (19.7.1): 'de A, d) entraîne a).'", "labels italic (page_213_s2.png)", "$d)$, $a)$", "italics", None, "high",
    r"de $A$, $d)$ entraîne $a)$.", r"de $A$, \emph{d)} entraîne \emph{a)}.", "GLOBAL_ISSUES 88.")
add(213, "proof of (19.7.1): 'Il suffit de prouver que d) entraîne b), puisque'", "labels italic", "$d)$, $b)$", "italics", None, "high",
    r"Il suffit de prouver que $d)$ entraîne $b)$, puisque", r"Il suffit de prouver que \emph{d)} entraîne \emph{b)}, puisque",
    "GLOBAL_ISSUES 88.")
add(213, "proof of (19.7.1): 'tout quotient d'un sous-module d'un gr^p_𝔎(M) est alors'", "Fraktur K", "\\mathfrak R", "symbol", None, "high",
    r"d'un sous-module d'un $\operatorname{gr}_{\mathfrak R}^p(M)$ est alors", r"d'un sous-module d'un $\operatorname{gr}_{\mathfrak K}^p(M)$ est alors", K_NOTE)
add(213, "proof of (19.7.1): 'en vertu du fait que gr^p_𝔎(M) est un A-module'", "Fraktur K", "\\mathfrak R", "symbol", None, "high",
    r"en vertu du fait que $\operatorname{gr}_{\mathfrak R}^p(M)$ est un", r"en vertu du fait que $\operatorname{gr}_{\mathfrak K}^p(M)$ est un", K_NOTE)
add(213, "proof of (19.7.1): 'la suite f est gr^•_𝔎(A)-régulière, elle est aussi gr^•_𝔎(N)-régulière'",
    "Fraktur K twice; raised bullets (page_213_s3.png)", "\\mathfrak R; ^*", "symbol", None, "high",
    r"Comme par hypothèse la suite $\mathbf f$ est $\operatorname{gr}_{\mathfrak R}^*(A)$-régulière, elle est aussi $\operatorname{gr}_{\mathfrak R}^*(N)$-régulière",
    r"Comme par hypothèse la suite $\mathbf f$ est $\operatorname{gr}_{\mathfrak K}^\bullet(A)$-régulière, elle est aussi $\operatorname{gr}_{\mathfrak K}^\bullet(N)$-régulière", KB_NOTE)
add(213, "proof of (19.7.1): 'd'un gr^k_𝔎(M) est alors séparé'", "Fraktur K", "\\mathfrak R", "symbol", None, "high",
    r"d'un $\operatorname{gr}_{\mathfrak R}^k(M)$", r"d'un $\operatorname{gr}_{\mathfrak K}^k(M)$", K_NOTE)
add(213, "diagram (19.7.1.1), first row", "Fraktur K twice; raised bullets (page_213_s3.png)", "\\mathfrak R; ^*", "symbol", None, "high",
    r"(\operatorname{gr}_{\mathfrak R}^*(R,N)\otimes_{A/\mathfrak R}(A/\mathfrak L))[T_1,\ldots,T_n] \ar[r]^-{\psi_R'} \ar[d] & \operatorname{gr}_{\mathfrak L}^*(R,N)",
    r"(\operatorname{gr}_{\mathfrak K}^\bullet(R,N)\otimes_{A/\mathfrak K}(A/\mathfrak L))[T_1,\ldots,T_n] \ar[r]^-{\psi_R'} \ar[d] & \operatorname{gr}_{\mathfrak L}^\bullet(R,N)", KB_NOTE)
add(213, "diagram (19.7.1.1), second row", "Fraktur K twice; raised bullets", "\\mathfrak R; ^*", "symbol", None, "high",
    r"(\operatorname{gr}_{\mathfrak R}^*(N)\otimes_{A/\mathfrak R}(A/\mathfrak L))[T_1,\ldots,T_n] \ar[r]^-{\psi_N} \ar[d] & \operatorname{gr}_{\mathfrak L}^*(N)",
    r"(\operatorname{gr}_{\mathfrak K}^\bullet(N)\otimes_{A/\mathfrak K}(A/\mathfrak L))[T_1,\ldots,T_n] \ar[r]^-{\psi_N} \ar[d] & \operatorname{gr}_{\mathfrak L}^\bullet(N)", KB_NOTE)
add(213, "diagram (19.7.1.1), third row", "Fraktur K twice; raised bullets (page_213_s4.png)", "\\mathfrak R; ^*", "symbol", None, "high",
    r"(\operatorname{gr}_{\mathfrak R}^*(M)\otimes_{A/\mathfrak R}(A/\mathfrak L))[T_1,\ldots,T_n] \ar[r]^-{\psi_M} \ar[d] & \operatorname{gr}_{\mathfrak L}^*(M)",
    r"(\operatorname{gr}_{\mathfrak K}^\bullet(M)\otimes_{A/\mathfrak K}(A/\mathfrak L))[T_1,\ldots,T_n] \ar[r]^-{\psi_M} \ar[d] & \operatorname{gr}_{\mathfrak L}^\bullet(M)", KB_NOTE)
add(213, "after (19.7.1.1): 'où gr^•_𝔎(R, N) (resp. gr^•_𝔏(R, N)) est le gradué associé à R pour la filtration des R∩𝔎^mN'",
    "Fraktur K twice; raised bullets (page_213_s4.png)", "\\mathfrak R; ^*", "symbol", None, "high",
    r"où $\operatorname{gr}_{\mathfrak R}^*(R,N)$ (resp. $\operatorname{gr}_{\mathfrak L}^*(R,N)$) est le gradué associé à $R$ pour la filtration des $R\cap\mathfrak R^mN$",
    r"où $\operatorname{gr}_{\mathfrak K}^\bullet(R,N)$ (resp. $\operatorname{gr}_{\mathfrak L}^\bullet(R,N)$) est le gradué associé à $R$ pour la filtration des $R\cap\mathfrak K^mN$", KB_NOTE)
add(213, "page break 213/214: '... et que ψ_N | est bijectif.' (end of the p. 213 segment)",
    "p. 214 begins mid-sentence with 'est bijectif.', flush left, no indent (page_213_s4.png, page_214_s1.png)",
    "blank line before \\oldpage[IV-4]{214} (with the one after it: a paragraph break the print lacks)", "marker", None, "high",
    r"et que $\psi_N$<NL><NL>", r"et que $\psi_N$<NL>",
    "The marker is at the right place; both blank lines must go. The other one is the first p. 214 finding.")

# ---------------------------------------------------------------- p. 214
add(214, "top of p. 214: 'est bijectif. Il s'agit, ...'", "continues the sentence of p. 213, no indent (page_214_s1.png)",
    "blank line after \\oldpage[IV-4]{214}", "marker", None, "high",
    r"\oldpage[IV-4]{214}<NL><NL>est \emph{bijectif}", r"\oldpage[IV-4]{214}<NL>est \emph{bijectif}",
    "Removes the blank line after the marker; the one before it is the last p. 213 finding (both needed).")
add(214, "(19.7.1.2): 'B = gr^•_𝔎A⊗_{A/𝔎}(A/𝔏), P = gr^•_𝔎(N)⊗_{A/𝔎}(A/𝔏), Q = gr^•_𝔏(R, N)'",
    "Fraktur K four times; raised bullets (page_214_s1.png)", "\\mathfrak R; ^*", "symbol", None, "high",
    r"$B=\operatorname{gr}_{\mathfrak R}^*A\otimes_{A/\mathfrak R}(A/\mathfrak L)$, $P=\operatorname{gr}_{\mathfrak R}^*(N)\otimes_{A/\mathfrak R}(A/\mathfrak L)$, $Q=\operatorname{gr}_{\mathfrak L}^*(R,N)$",
    r"$B=\operatorname{gr}_{\mathfrak K}^\bullet A\otimes_{A/\mathfrak K}(A/\mathfrak L)$, $P=\operatorname{gr}_{\mathfrak K}^\bullet(N)\otimes_{A/\mathfrak K}(A/\mathfrak L)$, $Q=\operatorname{gr}_{\mathfrak L}^\bullet(R,N)$", KB_NOTE)
add(214, "(19.7.1.2): 's'identifie à gr^•_𝔏(N)'", "raised bullet", "^*", "symbol", None, "high",
    r"s'identifie à $\operatorname{gr}_{\mathfrak L}^*(N)$", r"s'identifie à $\operatorname{gr}_{\mathfrak L}^\bullet(N)$", B_NOTE)
add(214, "(19.7.1.3): 'nous allons d'abord voir que l'on a (19.7.1.3) Q = (Q∩P)[T_1,...,T_n].'",
    "(19.7.1.3) is the equation number of a display that ends the sentence of (19.7.1.2); bold number at the left of the formula line (page_214_s1.png)",
    "\\end{env} after 'l'on a', then a new env [19.7.1.3] whose heading stands on its own line above the display", "other", None, "high",
    r"nous allons d'abord voir que l'on a<NL>\end{env}<NL><NL>\begin{env}[19.7.1.3]<NL>\label{IV.19.7.1.3}<NL>\[<NL>  Q=(Q\cap P)[T_1,\ldots,T_n].<NL>\]<NL>\end{env}",
    r"nous allons d'abord voir que l'on a<NL>\begin{equation}<NL>  Q=(Q\cap P)[T_1,\ldots,T_n].<NL>  \tag{19.7.1.3}\label{IV.19.7.1.3}<NL>\end{equation}<NL>\end{env}",
    "Equation number set as an env heading (GLOBAL_ISSUES 64 pattern; same form as (18.3.6.4) on 0_IV p. 62 and (19.5.5.5) "
    "in findings_205_209); label kept. DOCUMENT-WIDE: 14 more env-wrapped numbered displays in ega4-18 after p. 214 "
    "(19.7.1.9-19.7.1.17, 19.7.1.19-19.7.1.23).")
add(214, "'c'est un sous-B[T_1,...,T_n]-module de P[T_1,...,T_n]/((Q∩P)[T_1,...,T_n]) = (P/(Q∩P))[T_1,...,T_n]. En tant que'",
    "the formula set in the running text (page_214_s1.png, page_214_s2.png)", "displayed", "formula", None, "high",
    r"-module de<NL>\[<NL>  P[T_1,\ldots,T_n]/((Q\cap P)[T_1,\ldots,T_n])=(P/(Q\cap P))[T_1,\ldots,T_n].<NL>\]<NL>En tant que",
    r"-module de $P[T_1,\ldots,T_n]/((Q\cap P)[T_1,\ldots,T_n])=(P/(Q\cap P))[T_1,\ldots,T_n]$. En tant que",
    "Inline as printed; no connecting word lost or added.")
add(214, "'qui n'est autre que gr^•_𝔏(M) en vertu du diagramme (19.7.1.1)'", "raised bullet", "^*", "symbol", None, "high",
    r"qui n'est autre que $\operatorname{gr}_{\mathfrak L}^*(M)$", r"qui n'est autre que $\operatorname{gr}_{\mathfrak L}^\bullet(M)$", B_NOTE)
add(214, "(19.7.1.4): 'Ass_{A/𝔏}(Z) ⊂ Ass_{A/𝔏}(gr^•_𝔏(M)).'", "raised bullet (page_214_s2.png)", "^*", "symbol", None, "high",
    r"\operatorname{Ass}_{A/\mathfrak L}(Z)\subset\operatorname{Ass}_{A/\mathfrak L}(\operatorname{gr}_{\mathfrak L}^*(M)).",
    r"\operatorname{Ass}_{A/\mathfrak L}(Z)\subset\operatorname{Ass}_{A/\mathfrak L}(\operatorname{gr}_{\mathfrak L}^\bullet(M)).", B_NOTE)
add(214, "'on a par suite Ass_{A/𝔏}(gr^•_𝔏(M)) ⊂ Ass_{A/𝔏}(A/𝔏)'", "raised bullet", "^*", "symbol", None, "high",
    r"on a par suite $\operatorname{Ass}_{A/\mathfrak L}(\operatorname{gr}_{\mathfrak L}^*(M))",
    r"on a par suite $\operatorname{Ass}_{A/\mathfrak L}(\operatorname{gr}_{\mathfrak L}^\bullet(M))", B_NOTE)
add(214, "'de la forme 𝔭/(𝔏/𝔎), où 𝔭 ∈ Ass_{A/𝔎}(A/𝔏)'", "Fraktur K twice (page_214_s2.png)", "\\mathfrak R", "symbol", None, "high",
    r"de la forme $\mathfrak p/(\mathfrak L/\mathfrak R)$, où $\mathfrak p\in\operatorname{Ass}_{A/\mathfrak R}(A/\mathfrak L)$",
    r"de la forme $\mathfrak p/(\mathfrak L/\mathfrak K)$, où $\mathfrak p\in\operatorname{Ass}_{A/\mathfrak K}(A/\mathfrak L)$", K_NOTE)
add(214, "'Z_𝔭 = 0 pour tout 𝔭 ∈ Ass_{A/𝔎}(A/𝔏). Or, si 𝔭 = 𝔯/𝔎'", "Fraktur K twice", "\\mathfrak R", "symbol", None, "high",
    r"$Z_{\mathfrak p}=0$ pour tout $\mathfrak p\in\operatorname{Ass}_{A/\mathfrak R}(A/\mathfrak L)$. Or, si $\mathfrak p=\mathfrak r/\mathfrak R$",
    r"$Z_{\mathfrak p}=0$ pour tout $\mathfrak p\in\operatorname{Ass}_{A/\mathfrak K}(A/\mathfrak L)$. Or, si $\mathfrak p=\mathfrak r/\mathfrak K$", K_NOTE)
add(214, "'on a (gr^•_𝔎(M))_𝔭 = gr^•_{𝔎_𝔯}(M_𝔯)'", "Fraktur K twice; raised bullets (crop c214_AK.png)", "\\mathfrak R; ^*",
    "symbol", None, "high",
    r"on a $(\operatorname{gr}_{\mathfrak R}^*(M))_{\mathfrak p}=\operatorname{gr}_{\mathfrak R_{\mathfrak r}}^*(M_{\mathfrak r})$",
    r"on a $(\operatorname{gr}_{\mathfrak K}^\bullet(M))_{\mathfrak p}=\operatorname{gr}_{\mathfrak K_{\mathfrak r}}^\bullet(M_{\mathfrak r})$", KB_NOTE)
add(214, "'et (A/K)_𝔭 = A_𝔯/K_𝔯, et les images des f_i'",
    "roman capital K twice, not a Fraktur letter (crops c214_AK.png, c214_s3top.png)",
    "(A/\\mathfrak L)_{\\mathfrak p}=A_{\\mathfrak r}/\\mathfrak L_{\\mathfrak r}: a third reading, neither the print's nor the intended one",
    "misprint_in_print", None, "high",
    r"$(A/\mathfrak L)_{\mathfrak p}=A_{\mathfrak r}/\mathfrak L_{\mathfrak r}$", r"$(A/K)_{\mathfrak p}=A_{\mathfrak r}/K_{\mathfrak r}$",
    "Wrong-fount K (roman for Fraktur 𝔎). The step applies the implication a) => b) to A_𝔯, 𝔎_𝔯, M_𝔯, and hypothesis d) gives "
    "flatness of (gr^•_𝔎(M))_𝔭 over (A/𝔎)_𝔭, so the identity needed is (A/𝔎)_𝔭 = A_𝔯/𝔎_𝔯; the TeX's 𝔏 is true but not "
    "what is printed or meant. No erratum in Liste 3. Diplomatic: the printed roman K (written $K$ like the other capitals). "
    "CORRECTED EDITION: its text has the TeX's 𝔏 here too, so it needs the corrected reading 𝔎 (not a no-op).",
    corrected=r"$(A/\mathfrak K)_{\mathfrak p}=A_{\mathfrak r}/\mathfrak K_{\mathfrak r}$")
add(214, "'une suite gr^•_{𝔎_𝔯}(A_𝔯)-régulière'", "Fraktur K; raised bullet (crop c214_s3top.png)", "\\mathfrak R; ^*",
    "symbol", None, "high",
    r"une suite $\operatorname{gr}_{\mathfrak R_{\mathfrak r}}^*(A_{\mathfrak r})$-régulière",
    r"une suite $\operatorname{gr}_{\mathfrak K_{\mathfrak r}}^\bullet(A_{\mathfrak r})$-régulière", KB_NOTE)
add(214, "'(0, 15.1.14)'", "bare bold 0 (page_214_s3.png)", "($0$, 15.1.14)", "convention", 2, "high",
    r"($0$, 15.1.14)", r"(\textbf{0}, 15.1.14)", "")
add(214, "'appliquant à A_𝔯, 𝔎_𝔯 et M_𝔯'", "Fraktur K", "\\mathfrak R", "symbol", None, "high",
    r"$\mathfrak R_{\mathfrak r}$ et $M_{\mathfrak r}$", r"$\mathfrak K_{\mathfrak r}$ et $M_{\mathfrak r}$", K_NOTE)
add(214, "'l'implication a) ⇒ b) de l'énoncé, on voit que l'hypothèse d) entraîne'", "labels italic (page_214_s3.png)",
    "math labels", "italics", None, "high",
    r"l'implication $a)\Rightarrow b)$ de l'énoncé, on voit que l'hypothèse $d)$ entraîne",
    r"l'implication \emph{a)} $\Rightarrow$ \emph{b)} de l'énoncé, on voit que l'hypothèse \emph{d)} entraîne", "GLOBAL_ISSUES 88.")
add(214, "'où on a posé Q' = gr^•_𝔎(R, N)⊗_{A/𝔎}(A/𝔏)'", "Fraktur K twice; raised bullet", "\\mathfrak R; ^*", "symbol", None, "high",
    r"$Q'=\operatorname{gr}_{\mathfrak R}^*(R,N)\otimes_{A/\mathfrak R}(A/\mathfrak L)$",
    r"$Q'=\operatorname{gr}_{\mathfrak K}^\bullet(R,N)\otimes_{A/\mathfrak K}(A/\mathfrak L)$", KB_NOTE)
add(214, "(19.7.1.5): 'de même degré de gr^•_𝔎(R, N)⊗_{A/𝔎}(A/𝔏)'", "Fraktur K twice; raised bullet", "\\mathfrak R; ^*",
    "symbol", None, "high",
    r"de même degré de $\operatorname{gr}_{\mathfrak R}^*(R,N)\otimes_{A/\mathfrak R}(A/\mathfrak L)$",
    r"de même degré de $\operatorname{gr}_{\mathfrak K}^\bullet(R,N)\otimes_{A/\mathfrak K}(A/\mathfrak L)$", KB_NOTE)
add(214, "(19.7.1.5): 'qui appartiennent à (𝔎^mN + 𝔏^{m+1}N)/𝔏^{m+1}N'", "Fraktur K", "\\mathfrak R", "symbol", None, "high",
    r"qui appartiennent à $(\mathfrak R^mN+\mathfrak L^{m+1}N)/\mathfrak L^{m+1}N$",
    r"qui appartiennent à $(\mathfrak K^mN+\mathfrak L^{m+1}N)/\mathfrak L^{m+1}N$", K_NOTE)
add(214, "(19.7.1.5): 'images d'éléments de gr^m_𝔎(R, N)⊗_{A/𝔎}(A/𝔏)'", "Fraktur K twice", "\\mathfrak R", "symbol", None, "high",
    r"$\operatorname{gr}_{\mathfrak R}^m(R,N)\otimes_{A/\mathfrak R}(A/\mathfrak L)$",
    r"$\operatorname{gr}_{\mathfrak K}^m(R,N)\otimes_{A/\mathfrak K}(A/\mathfrak L)$", K_NOTE)
add(214, "(19.7.1.5): 'appartenant à ((R∩𝔎^mN) + 𝔏^{m+1}N)/𝔏^{m+1}N'", "Fraktur K", "\\mathfrak R", "symbol", None, "high",
    r"appartenant à $((R\cap\mathfrak R^mN)+\mathfrak L^{m+1}N)/\mathfrak L^{m+1}N$",
    r"appartenant à $((R\cap\mathfrak K^mN)+\mathfrak L^{m+1}N)/\mathfrak L^{m+1}N$", K_NOTE)
add(214, "(19.7.1.5), display '((R∩𝔏^mN) + 𝔏^{m+1}N) ∩ (𝔎^mN + 𝔏^{m+1}N) ⊂ (R∩𝔎^mN) + 𝔏^{m+1}N.'",
    "Fraktur K twice (page_214_s4.png)", "\\mathfrak R", "symbol", None, "high",
    r"((R\cap\mathfrak L^mN)+\mathfrak L^{m+1}N)\cap(\mathfrak R^mN+\mathfrak L^{m+1}N)\subset(R\cap\mathfrak R^mN)+\mathfrak L^{m+1}N.",
    r"((R\cap\mathfrak L^mN)+\mathfrak L^{m+1}N)\cap(\mathfrak K^mN+\mathfrak L^{m+1}N)\subset(R\cap\mathfrak K^mN)+\mathfrak L^{m+1}N.", K_NOTE)
add(214, "(19.7.1.5): 'Comme 𝔎 ⊂ 𝔏, on vérifie aussitôt'", "new indented paragraph after the display (page_214_s4.png)",
    "follows \\] without a blank line: no indent", "other", None, "high",
    r"\]<NL>Comme", r"\]<NL><NL>Comme", "Paragraph after a display, indented as printed.")
add(214, "(19.7.1.5): 'Comme 𝔎 ⊂ 𝔏'", "Fraktur K", "\\mathfrak R", "symbol", None, "high",
    r"$\mathfrak R\subset\mathfrak L$, on vérifie", r"$\mathfrak K\subset\mathfrak L$, on vérifie", K_NOTE)
add(214, "(19.7.1.5): 'est égal à (R∩(𝔎^mN + 𝔏^{m+1}N)) + 𝔏^{m+1}N'", "Fraktur K", "\\mathfrak R", "symbol", None, "high",
    r"est égal à $(R\cap(\mathfrak R^mN+\mathfrak L^{m+1}N))+\mathfrak L^{m+1}N$",
    r"est égal à $(R\cap(\mathfrak K^mN+\mathfrak L^{m+1}N))+\mathfrak L^{m+1}N$", K_NOTE)
add(214, "(19.7.1.6): 'si bien que tout se réduit à prouver (19.7.1.6) R∩(𝔎^mN + 𝔏^{m+1}N) ⊂ (R∩𝔎^mN) + 𝔏^{m+1}N.'",
    "(19.7.1.6) is the equation number of the display that ends the sentence of (19.7.1.5) (page_214_s4.png)",
    "\\end{env} after 'prouver', then a new env [19.7.1.6] whose heading stands on its own line above the display",
    "other", None, "high",
    r"si bien que tout se réduit à prouver<NL>\end{env}<NL><NL>\begin{env}[19.7.1.6]<NL>\label{IV.19.7.1.6}<NL>\[<NL>  R\cap(\mathfrak R^mN+\mathfrak L^{m+1}N)\subset(R\cap\mathfrak R^mN)+\mathfrak L^{m+1}N.<NL>\]<NL>\end{env}",
    r"si bien que tout se réduit à prouver<NL>\begin{equation}<NL>  R\cap(\mathfrak R^mN+\mathfrak L^{m+1}N)\subset(R\cap\mathfrak R^mN)+\mathfrak L^{m+1}N.<NL>  \tag{19.7.1.6}\label{IV.19.7.1.6}<NL>\end{equation}<NL>\end{env}",
    "Same structure fix as (19.7.1.3). APPLY BEFORE the next finding (the Fraktur fix inside this display); the formula line "
    "is left unchanged here.")
add(214, "(19.7.1.6), display 'R∩(𝔎^mN + 𝔏^{m+1}N) ⊂ (R∩𝔎^mN) + 𝔏^{m+1}N.'", "Fraktur K twice", "\\mathfrak R", "symbol", None, "high",
    r"R\cap(\mathfrak R^mN+\mathfrak L^{m+1}N)\subset(R\cap\mathfrak R^mN)+\mathfrak L^{m+1}N.",
    r"R\cap(\mathfrak K^mN+\mathfrak L^{m+1}N)\subset(R\cap\mathfrak K^mN)+\mathfrak L^{m+1}N.",
    K_NOTE + " Apply AFTER the previous finding (its 'old' contains this formula line).")

# ---------------------------------------------------------------- checks and output
for i, x in enumerate(F):
    fx = x["fix"]
    if fx and x["page"] in PAGES:
        c = PAGES[x["page"]].count(fx["old"])
        assert c == 1, (i, x["page"], c, fx["old"][:80])
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
cnt = {}
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print(len(F), "findings")
for p in sorted(cnt):
    print(p, cnt[p])
