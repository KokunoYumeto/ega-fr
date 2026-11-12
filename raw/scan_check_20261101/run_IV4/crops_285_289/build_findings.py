# Builds findings_285_289.json and checks every "old" string.
# Newlines in old/new are written as the pilcrow sign and converted to "\n".
import json, sys

RUN = r"user/Documents/ega_scan_check_20261101/run_IV4"
SRC = (r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/"
       r"diplomatic/packages/IV4/native/ega4/ega4-21b-fr.tex")
NL = "\u00b6"


def nl(s):
    return None if s is None else s.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, old, new, note, conv=None, conf="high", corrected=None, after=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": nl(old), "new": nl(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = nl(corrected)
    d["note"] = note
    d["_after"] = after  # index of a finding that must be applied first (checked, then dropped)
    F.append(d)
    return len(F) - 1


# ---------------------------------------------------------------- p. 285
m285a = add(285, "top of the page (boundary with p. 284): position of \\oldpage[IV-4]{285}",
    "printed p. 284 ends 'Comme les points de X_0 sont fermés dans X, on a ((i_x)_*(A(x))_y = 0 pour tout'; p. 285 begins 'y ≠ x ∈ X_0; cette remarque' (page_284_s4.png, page_285_s1.png)",
    "\\oldpage[IV-4]{285} stands after \\begin{proof}, one printed line too early",
    "marker",
    r"\oldpage[IV-4]{285}¶Comme les points",
    r"Comme les points",
    "BOUNDARY FIX (page break 284/285). Marker move, part 1 of 2 (removes the marker; part 2 is the next entry). "
    "Identical to the entry in findings_280_284.json: apply once. All marker moves of this file are listed last, after "
    "the text fixes, because apply_fixes.py looks for each 'old' in the current segment of its page.")
add(285, "top of the page (boundary with p. 284): new position of \\oldpage[IV-4]{285}",
    "p. 285 begins with 'y ≠ x ∈ X_0;' (mid-sentence)",
    "(marker one line too early, see the entry above)",
    "marker",
    r"pour tout $y\neq x\in X_0$;",
    r"pour tout¶\oldpage[IV-4]{285}¶$y\neq x\in X_0$;",
    "BOUNDARY FIX (page break 284/285), part 2 of 2: mid-sentence break, so no blank lines. Identical to the entry in "
    "findings_280_284.json: apply once. The first letter of p. 285, y, prints without its descender (it looks like v; "
    "crops cmp_y.png, p285_first.png): taken as a damaged sort, not recorded.")
add(285, "first line of the proof of (21.9.2), printed as the last line of p. 284: 'on a ((i_x)_*(A(x))_y = 0'",
    "'((i_x)_*(A(x))_y': three closing parentheses for four opening ones (crop p284_last.png)",
    "'((i_x)_*(A(x)))_y' (silent correction)",
    "misprint_in_print",
    r"on a $((i_x)_*(A(x)))_y=0$",
    r"on a $((i_x)_*(A(x))_y=0$",
    "Printed on p. 284 (last line); in the TeX it stands after \\oldpage[IV-4]{285} until the 284/285 marker move "
    "(listed at the end of this file; apply this entry first). The TeX silently corrects; restore the printed reading. "
    "Identical to the entry in findings_280_284.json: apply once. Does not overlap the two marker edits.",
    corrected=r"on a $((i_x)_*(A(x)))_y=0$")
add(285, "proof of (21.9.2): 'le support de s_k est réduit à x_k,'",
    "'réduit à x_k' without braces (crop p285_s1_bottom.png)",
    "réduit à $\\{x_k\\}$",
    "formula",
    r"est réduit à $\{x_k\}$",
    r"est réduit à $x_k$",
    "")
add(285, "end of the proof of (21.9.2): 'en posant s'_x = 0 dans X—U'",
    "long dash X—U",
    "$X-U$",
    "convention",
    r"$s'_x=0$ dans $X-U$",
    r"$s'_x=0$ dans $X\setmin U$",
    "\\setmin as in the earlier IV-4 fixes.", conv=7)
rem1 = add(285, "heading of (21.9.3): 'Remarques (21.9.3). — (i)'",
    "plural 'Remarques' (page_285_s2.png)",
    "\\begin{remark} prints 'Remarque'",
    "word",
    r"\begin{remark}[21.9.3]",
    r"\begin{remarks}[21.9.3]",
    "Part 1 of 2: apply together with the next entry (\\end{remark} -> \\end{remarks}), otherwise LaTeX error. "
    "The remarks environment is defined in EGA_IV4_FR.tex (GLOBAL_ISSUES 28).")
add(285, "end of Remarques (21.9.3)",
    "plural 'Remarques' (see the entry above)",
    "\\end{remark}",
    "word",
    r"pour $x\in E\cap U$.¶\end{enumerate}¶\end{remark}",
    r"pour $x\in E\cap U$.¶\end{enumerate}¶\end{remarks}",
    "Part 2 of 2 with the entry above; apply both.")
add(285, "(21.9.3) (ii), last sentence: 'prendre pour t la section de ⊕_{x∈X_0}(i_x)_*(A(x))'",
    "index x ∈ X_0 under the second ⊕ (crop p285_s3_ii.png), as under the first one",
    "\\bigoplus_{x\\in E}",
    "formula",
    r"la section de $\bigoplus_{x\in E}(i_x)_*(A(x))$",
    r"la section de $\bigoplus_{x\in X_0}(i_x)_*(A(x))$",
    "The TeX rewrites the print's index.")

# ---------------------------------------------------------------- p. 286
add(286, "top of the page: position of \\oldpage[IV-4]{286}",
    "printed p. 285 ends 'Pour le 1°, il suffit de noter que pour tout ouvert U de X tout diviseur D∈Div(U), les points maximaux du support S de D sont tels que'; p. 286 begins 'prof(O_{X,x}) = 1 (21.1.9)' (crop p285_s4_end.png, page_286_s1.png)",
    "\\oldpage[IV-4]{286} stands before 'Pour le 1°', two printed lines too early",
    "marker",
    r"\oldpage[IV-4]{286}¶Pour le 1",
    r"Pour le 1",
    "Marker move inside these pages, part 1 of 2 (removes the marker); part 2 is the next entry. The p. 285 paragraph "
    "then runs on without a break, as printed. Apply after the text fixes of p. 286 (the 'et' misprint lies in between).")
add(286, "new position of \\oldpage[IV-4]{286}",
    "p. 286 begins with 'prof(O_{X,x}) = 1' (mid-sentence)",
    "(marker too early, see the entry above)",
    "marker",
    r"sont tels que $\operatorname{prof}(\sh{O}_{X,x})=1$",
    r"sont tels que¶\oldpage[IV-4]{286}¶$\operatorname{prof}(\sh{O}_{X,x})=1$",
    "Part 2 of 2: mid-sentence break, no blank lines. Independent of the next entry (no overlap).")
add(286, "proof of (21.9.4), printed on p. 285 (last line but one): 'pour tout ouvert U de X tout diviseur D∈Div(U)'",
    "no 'et' between 'de X' and 'tout diviseur' (crop p285_s4_end.png)",
    "'pour tout ouvert $U$ de $X$ et tout diviseur' (silent correction)",
    "misprint_in_print",
    r"de $X$ et tout diviseur $D",
    r"de $X$ tout diviseur $D",
    "Printed on p. 285; the text lies in the p. 286 segment until the marker 286 move (listed at the end of this file; "
    "apply this entry first; no overlap). The print drops the 'et'; the TeX silently adds it.",
    corrected=r"de $X$ et tout diviseur $D")
add(286, "proof of (21.9.5): 'Cela résulte de (21.9.4) et de (21.9.3, (ii)).'",
    "(21.9.3, (ii))",
    "\\sref{IV.21.9.3}, (ii) prints '(21.9.3), (ii)'",
    "punctuation",
    r"\sref{IV.21.9.3}, (ii).",
    r"\sref{IV.21.9.3}[(ii)].",
    "")
add(286, "Corollaire (21.9.6): 'de la forme D'—D''",
    "long dash used for the minus sign (crop p286_s2_cor6.png)",
    "$D'-D''$",
    "convention",
    r"$D'-D''$",
    r"$D'\setmin D''$",
    "Subtraction printed with the long dash (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.", conv=7)
add(286, "after the proof of (21.9.7): 'théorème de Riemann-Roch'",
    "hyphen (crop p286_riemann.png)",
    "Riemann--Roch (en dash)",
    "punctuation",
    r"Riemann--Roch",
    r"Riemann-Roch",
    "As Cohen-Macaulay (GLOBAL_ISSUES 74).")
add(286, "(21.9.8), l. 2: 'la prop. (21.9.4) ramène'",
    "abbreviation 'prop.' (crop p286_s3_2198.png)",
    "'la proposition'",
    "word",
    r"la proposition \sref{IV.21.9.4}",
    r"la prop.~\sref{IV.21.9.4}",
    "")
add(286, "(21.9.8), second paragraph: 'Lorsque A est un anneau local régulier de dimension 1'",
    "'régulier' italic (crop p286_s3_lorsque.png)",
    "upright",
    "italics",
    r"anneau local régulier de dimension $1$ (autrement",
    r"anneau local \emph{régulier} de dimension $1$ (autrement",
    "")
add(286, "Proposition (21.9.9): 'localement noethérien régulier de dimension ≤ 1'",
    "'régulier' set roman inside the italic statement (crop p286_s3_prop2199.png)",
    "italic (whole statement italic)",
    "convention",
    r"noethérien régulier de dimension $\leq1$.",
    r"noethérien \textup{régulier} de dimension $\leq1$.",
    "", conv=6)
add(286, "(21.9.10): 'théorème de Krull-Akizuki'",
    "hyphen (page_286_s4.png)",
    "Krull--Akizuki (en dash)",
    "punctuation",
    r"Krull--Akizuki",
    r"Krull-Akizuki",
    "As Riemann-Roch above.")

# ---------------------------------------------------------------- p. 287
add(287, "Proposition (21.9.11): 'Dans ces conditions :' after the conditions 1°, 2°",
    "new indented paragraph (crop p287_s1_i.png)",
    "follows \\end{enumerate} without a blank line, so it is set without the indent",
    "other",
    r"\end{enumerate}¶Dans ces",
    r"\end{enumerate}¶¶Dans ces",
    "GLOBAL_ISSUES 80/99 pattern. Does not overlap the next entry.")
add(287, "Proposition (21.9.11): labels (i), (ii)",
    "labels upright in the italic statement (crops p287_s1_i.png, p287_s2_b.png)",
    "enumerate label (\\roman*) comes out italic in the proposition",
    "convention",
    r"\begin{enumerate}[label=(\roman*)]¶  \item Soit $Z_0$",
    r"\begin{enumerate}[label=\textup{(\roman*)}]¶  \item Soit $Z_0$",
    "GLOBAL_ISSUES 16; one edit covers both labels.", conv=6)
add(287, "Proposition (21.9.11) (ii): 'un ouvert affine U_0 contenant (Ass(O_{X_0}))∪Z_0'",
    "outer parentheses around Ass(O_{X_0}) (crop p287_s2_b.png)",
    "$\\operatorname{Ass}(\\sh{O}_{X_0})\\cup Z_0$",
    "formula",
    r"contenant $\operatorname{Ass}(\sh{O}_{X_0})\cup Z_0$",
    r"contenant $(\operatorname{Ass}(\sh{O}_{X_0}))\cup Z_0$",
    "The same parentheses are printed on p. 288 (aux points de (Ass(O_{X_0}))∪Z_0), but not in 'l'ensemble Ass(O_{X_0})∪Z_0 est fini'.")
add(287, "Proposition (21.9.11) (ii): '(condition automatiquement vérifiée lorsqu'il existe un O_{X_0}-Module ample (II, 4.5.4))'",
    "the opening and the closing parenthesis are upright (crops p287_paren_open.png, p287_paren_close.png); the words inside are italic",
    "both parentheses italic (proposition environment)",
    "convention",
    r"(condition automatiquement vérifiée lorsqu'il existe un $\sh{O}_{X_0}$-Module ample \sref[II]{II.4.5.4}).",
    r"\textup{(}condition automatiquement vérifiée lorsqu'il existe un $\sh{O}_{X_0}$-Module ample \sref[II]{II.4.5.4}\textup{)}.",
    "Only the two parentheses change (GLOBAL_ISSUES 26/101: fixed by the print); the closing one stands next to the reference.",
    conv=6)
add(287, "proof of (21.9.11) (i), l. 2: 'le support T de D_0 est un ensemble fini discret et fermé dans X_0'",
    "'fini' (italic) after 'ensemble' (crop p287_s2_c.png)",
    "'est un ensemble discret et fermé' (word missing)",
    "missing",
    r"est un ensemble discret et fermé dans $X_0$.",
    r"est un ensemble \emph{fini} discret et fermé dans $X_0$.",
    "")
add(287, "proof of (21.9.11) (i): '... V^{(x)}∩Ass(O_X) = ∅. Or, si z∈Ass(O_X)'",
    "'Or,' continues the same paragraph (crop p287_s3_a.png)",
    "blank line before 'Or, si' (paragraph break)",
    "other",
    r"=\emp$.¶¶Or, si",
    r"=\emp$.¶Or, si",
    "")
add(287, "proof of (21.9.11) (i): 'pour un z∈V^{(x)}∩Ass(O_X); V^{(x)} contiendrait donc'",
    "semicolon after Ass(O_X) (crop p287_s3_b.png)",
    "full stop",
    "punctuation",
    r"\cap\operatorname{Ass}(\sh{O}_X)$.¶$V^{(x)}$ contiendrait",
    r"\cap\operatorname{Ass}(\sh{O}_X)$;¶$V^{(x)}$ contiendrait",
    "")
add(287, "proof of (21.9.11) (i): 'l'image ḡ^{(x)} de g^{(x)} dans Γ(U∩X_0, O_{X_0})'",
    "'Γ(U∩X_0, O_{X_0})': U without the superscript (x) (crop p287_s3_b.png)",
    "\\Gamma(U^{(x)}\\cap X_0,\\sh{O}_{X_0}) (silent correction)",
    "misprint_in_print",
    r"dans $\Gamma(U^{(x)}\cap X_0,\sh{O}_{X_0})$",
    r"dans $\Gamma(U\cap X_0,\sh{O}_{X_0})$",
    "g^{(x)} is a section over U^{(x)}; U is not defined in this proof. The TeX silently corrects; restore the printed reading.",
    corrected=r"dans $\Gamma(U^{(x)}\cap X_0,\sh{O}_{X_0})$")

# ---------------------------------------------------------------- p. 288 (printed p. 288)
add(288, "l. 1: 'autrement dit que V^{(x)} est fermé dans X.'",
    "'fermé dans' italic (crop p288_s1_a.png)",
    "upright",
    "italics",
    r"est fermé dans $X$.¶On peut alors",
    r"est \emph{fermé dans} $X$.¶On peut alors",
    "")
add(288, "l. 2: 'définir un diviseur D^{(x)} sur X par la condition'",
    "'sur' italic (crop p288_s1_a.png)",
    "upright",
    "italics",
    r"un diviseur $D^{(x)}$ sur $X$ par",
    r"un diviseur $D^{(x)}$ \emph{sur} $X$ par",
    "")
add(288, "l. 2: 'D^{(x)}|(X—V^{(x)}) = 0'",
    "long dash X—V^{(x)}",
    "$X-V^{(x)}$",
    "convention",
    r"$D^{(x)}|(X-V^{(x)})=0$",
    r"$D^{(x)}|(X\setmin V^{(x)})=0$",
    "", conv=7)
add(288, "l. 3: 'dans U^{(x)}∩(X—V^{(x)})'",
    "long dash",
    "$X-V^{(x)}$",
    "convention",
    r"$U^{(x)}\cap(X-V^{(x)})$",
    r"$U^{(x)}\cap(X\setmin V^{(x)})$",
    "", conv=7)
add(288, "l. 4: 'est une section inversible,'",
    "'inversible' italic (crop p288_s1_a.png)",
    "upright",
    "italics",
    r"une section inversible, donc",
    r"une section \emph{inversible}, donc",
    "")
add(288, "l. 5: 'X—V^{(x)} sont égales'",
    "long dash",
    "$X-V^{(x)}$",
    "convention",
    r"et $X-V^{(x)}$ sont égales",
    r"et $X\setmin V^{(x)}$ sont égales",
    "", conv=7)
add(288, "proof of (21.9.11) (ii): 'dense dans X_0 (20.2.13, (iv)) il suffit pour cela'",
    "'(20.2.13, (iv))', and no comma after it (crop p288_s1_b.png)",
    "\\sref{IV.20.2.13}, (iv), prints '(20.2.13), (iv),'",
    "punctuation",
    r"\sref{IV.20.2.13}, (iv), il suffit",
    r"\sref{IV.20.2.13}[(iv)] il suffit",
    "One edit for the reference form and the comma the print does not have.")
add(288, "proof of (21.9.11) (ii): 'telle que t(z_0) ≠ 0 aux points de (Ass(O_{X_0}))∪Z_0 (3.1.9)'",
    "outer parentheses around Ass(O_{X_0}) (page_288_s2.png)",
    "$\\operatorname{Ass}(\\sh{O}_{X_0})\\cup Z_0$",
    "formula",
    r"aux points de $\operatorname{Ass}(\sh{O}_{X_0})\cup Z_0$",
    r"aux points de $(\operatorname{Ass}(\sh{O}_{X_0}))\cup Z_0$",
    "As in (21.9.11) (ii) on p. 287.")
add(288, "proof of (21.9.12), l. 2: 'A est de plus noethérien.'",
    "'noethérien' italic (crop p288_s2_noeth.png)",
    "upright",
    "italics",
    r"est de plus noethérien.",
    r"est de plus \emph{noethérien}.",
    "")
iv = add(288, "proof of (21.9.12): 'le changement de base S→S_α (8.10.5, (v));'",
    "(8.10.5, (v))",
    "\\sref{IV.8.10.5}, (v) prints '(8.10.5), (v)'",
    "punctuation",
    r"\sref{IV.8.10.5}, (v);",
    r"\sref{IV.8.10.5}[(v)];",
    "Apply BEFORE the next entry (the misprint edit takes its 'old' from the text after this one).")
add(288, "proof of (21.9.12): the v of '(8.10.5, (v))'",
    "the v is bold: mid-stroke runs 5.5 px against 3.2 px for the v of 'avec' in the same line, same height (crop p288_v.png)",
    "light v",
    "misprint_in_print",
    r"\sref{IV.8.10.5}[(v)]",
    r"\sref{IV.8.10.5}[(\textbf{v})]",
    "Wrong-fount letter (GLOBAL_ISSUES 29/97: recorded as a misprint, reproduced in the diplomatic text). Apply AFTER the "
    "previous entry: this 'old' exists only once that edit is made. Mid-line, not an end-of-line heavy impression.",
    corrected=r"\sref{IV.8.10.5}[(v)]", after=iv)
add(288, "proof of (21.9.12): '(8.6.3); on a, pour λ ≥ α, dim(X'_{0λ}) = dim(X'_0) ≤ 1'",
    "no clause 'pour λ ≥ α, posons X'_{0λ} = X'_{0α} ×_{S_α} S_λ'; the print reads 'on a, pour λ≥α, dim(X'_{0λ}) = ...' (crop p288_s3_a.png)",
    "added clause defining X'_{0λ}, then 'on a $\\dim(X'_{0\\lambda})$'",
    "extra",
    r"\sref{IV.8.6.3};¶pour $\lambda\geq\alpha$, posons $X'_{0\lambda}=X'_{0\alpha}\times_{S_\alpha}S_\lambda$;¶on a $\dim(X'_{0\lambda})",
    r"\sref{IV.8.6.3};¶on a, pour $\lambda\geq\alpha$, $\dim(X'_{0\lambda})",
    "The TeX adds a definition the print leaves to 'les notations habituelles (8.8.1)' and moves 'pour λ ≥ α' (GLOBAL_ISSUES 102/104 pattern).")
add(288, "proof of (21.9.12), last line of the page: 'par changement de base S→S_λ (8.5.2 et 8.5.5);'",
    "one pair of parentheses: (8.5.2 et 8.5.5) (page_288_s4.png)",
    "\\sref{IV.8.5.2} et \\sref{IV.8.5.5} prints '(8.5.2) et (8.5.5)'",
    "punctuation",
    r"S_\lambda$ \sref{IV.8.5.2} et \sref{IV.8.5.5}",
    r"S_\lambda$ (\EGAUnavailableHyperref{IV.8.5.2}{8.5.2} et \EGAUnavailableHyperref{IV.8.5.5}{8.5.5})",
    "\\EGAUnavailableHyperref (IV-4 preamble) links as \\sref does, defined label or not (as the p. 230 and p. 244 fixes).")
m289a = add(288, "end of the page: new position of \\oldpage[IV-4]{289}",
    "printed p. 288 ends '(8.5.2 et 8.5.5); il suffit de'; p. 289 begins 'considérer un O_{X_λ}-Module inversible L_λ' (page_288_s4.png, page_289_s1.png)",
    "\\oldpage[IV-4]{289} stands after \\begin{env}[21.10.1]\\label{IV.21.10.1}, about a printed page too late (the rest of the proof of (21.9.12), Remarque (21.9.13), the 21.10 heading and its introduction are printed on p. 289)",
    "marker",
    r"il suffit de considérer un $\sh{O}_{X_\lambda}$-Module",
    r"il suffit de¶\oldpage[IV-4]{289}¶considérer un $\sh{O}_{X_\lambda}$-Module",
    "MARKER 289 MISPLACED. Marker move, part 1 of 2 (inserts the marker at the printed break: mid-sentence, no blank lines); "
    "part 2 is the next entry (removes the old marker). Apply both, after the text fixes: the p. 288 entries marked "
    "'printed p. 289' concern text printed on p. 289 that lies in the p. 288 segment until this move.")
add(288, "printed p. 289, l. 4: 'vérifions que X et X_0 satisfont aux conditions de (21.9.11, (ii))'",
    "X_0 without the prime (crop p289_s1_a.png)",
    "$X'_0$ (silent correction)",
    "misprint_in_print",
    r"vérifions que $X$ et $X'_0$ satisfont",
    r"vérifions que $X$ et $X_0$ satisfont",
    "Printed on p. 289. The conditions of (21.9.11) are verified for the closed subscheme X'_0 (the next sentence has dim(X'_0)); "
    "X_0 is only the set f^{-1}(s_0). The TeX silently corrects; restore the printed reading.",
    conf="medium", corrected=r"vérifions que $X$ et $X'_0$ satisfont")
add(288, "printed p. 289, l. 5: 'aux conditions de (21.9.11, (ii)).'",
    "(21.9.11, (ii))",
    "\\sref{IV.21.9.11}, (ii) prints '(21.9.11), (ii)'",
    "punctuation",
    r"aux conditions de \sref{IV.21.9.11}, (ii).",
    r"aux conditions de \sref{IV.21.9.11}[(ii)].",
    "Printed on p. 289. Does not overlap the entry above.")
add(288, "printed p. 289, l. 6: 'considérons un sous-préschéma Y de X ayant Y pour ensemble sous-jacent;'",
    "'un sous-préschéma Y de X ayant Y pour ensemble sous-jacent' (crop p289_Y.png)",
    "'un sous-préschéma réduit $Y$ de $X$ ayant une partie localement fermée $Y$ pour ensemble sous-jacent'",
    "extra",
    r"un sous-préschéma réduit $Y$ de $X$ ayant une partie localement fermée $Y$ pour",
    r"un sous-préschéma $Y$ de $X$ ayant $Y$ pour",
    "Printed on p. 289. The TeX adds 'réduit' and 'une partie localement fermée' (rewording, GLOBAL_ISSUES 102/104 pattern).")
add(288, "printed p. 289, l. 8: 'on peut appliquer (18.5.11, c)) et on voit que'",
    "'(18.5.11, c))' with an italic c), no comma after it (crop p289_c.png)",
    "\\sref{IV.18.5.11}, c), prints '(18.5.11), c),' with an upright c",
    "punctuation",
    r"\sref{IV.18.5.11}, c), et on voit",
    r"\sref{IV.18.5.11}[\emph{c)}] et on voit",
    "Printed on p. 289. One edit for the reference form, the italic label and the comma the print does not have.")
add(288, "printed p. 289, l. 8-9: 'Y est somme des sous-préschémas ouverts Y_i'",
    "'somme' and 'ouverts' italic (crop p289_s1_b.png)",
    "upright",
    "italics",
    r"$Y$ est somme des sous-préschémas ouverts $Y_i",
    r"$Y$ est \emph{somme} des sous-préschémas \emph{ouverts} $Y_i",
    "Printed on p. 289. Does not overlap the entry above.")
add(288, "printed p. 289: 'que f∘j_i soit un morphisme fini.'",
    "'fini' italic (crop p289_s2_a.png)",
    "upright",
    "italics",
    r"soit un morphisme fini.¶Comme",
    r"soit un morphisme \emph{fini}.¶Comme",
    "Printed on p. 289. The second 'morphisme fini' of the next sentence is roman in the print.")
add(288, "printed p. 289: 'donc Y_i est fermé dans X;'",
    "'fermé dans' italic (crop p289_s2_a.png)",
    "upright",
    "italics",
    r"donc $Y_i$ est fermé dans $X$;",
    r"donc $Y_i$ est \emph{fermé dans} $X$;",
    "Printed on p. 289.")
add(288, "printed p. 289: 'l'hypothèse supplémentaire de (21.9.11, (ii)).'",
    "(21.9.11, (ii)) (crop p289_s2_b.png)",
    "\\sref{IV.21.9.11}, (ii) prints '(21.9.11), (ii)'",
    "punctuation",
    r"supplémentaire de \sref{IV.21.9.11}, (ii).",
    r"supplémentaire de \sref{IV.21.9.11}[(ii)].",
    "Printed on p. 289.")
add(288, "printed p. 289, Remarque (21.9.13): 'il existe, en vertu de (21.9.12) un O_X-Module inversible'",
    "no comma after (21.9.12) (crop p289_vertu.png)",
    "'en vertu de \\sref{IV.21.9.12}, un' (silent correction)",
    "misprint_in_print",
    r"en vertu de \sref{IV.21.9.12}, un",
    r"en vertu de \sref{IV.21.9.12} un",
    "Printed on p. 289. The print opens the incise with a comma but does not close it; the TeX silently adds the comma.",
    conf="medium", corrected=r"en vertu de \sref{IV.21.9.12}, un")
add(288, "printed p. 289, end of Remarque (21.9.13): 'd'où la conclusion (II, 5.3.1 et II, 5.5.3).'",
    "one pair of parentheses (crop p289_s2_c.png)",
    "(\\sref[II]{II.5.3.1} et \\sref[II]{II.5.5.3}) prints '((II, 5.3.1) et (II, 5.5.3))'",
    "punctuation",
    r"(\sref[II]{II.5.3.1} et \sref[II]{II.5.5.3})",
    r"(\textbf{II}, \EGAUnavailableHyperref{II.5.3.1}{5.3.1} et \textbf{II}, \EGAUnavailableHyperref{II.5.5.3}{5.5.3})",
    "Printed on p. 289. The doubled parentheses of GLOBAL_ISSUES 107 (ega4-21b line 917); not real here. Same construction as the p. 244 fix.")
add(288, "printed p. 289: heading '21.10. Images réciproques et images directes de cycles 1-codimensionnels.'",
    "the title ends with a full stop (crop p289_s3_title.png)",
    "no full stop",
    "punctuation",
    r"\subsection{Images réciproques et images directes de cycles 1-codimensionnels}",
    r"\subsection{Images réciproques et images directes de cycles 1-codimensionnels.}",
    "Printed on p. 289. As the 21.8 and 21.9 titles.")
add(288, "printed p. 289, 21.10 introduction: 'et pour les cycles 1-codimensionnels,'",
    "'cycles 1-codimensionnels' italic, the figure 1 roman (crop p289_s3_intro.png)",
    "upright",
    "italics",
    r"pour les cycles $1$-codimensionnels, ces",
    r"pour les \emph{cycles $1$-codimensionnels}, ces",
    "Printed on p. 289.")
add(288, "printed p. 289, 21.10 introduction: 'pour les diviseurs (21.4 et 21.5),'",
    "one pair of parentheses (crop p289_s3_intro.png)",
    "\\sref{IV.21.4} et \\sref{IV.21.5} prints '(21.4) et (21.5)'",
    "punctuation",
    r"diviseurs \sref{IV.21.4} et \sref{IV.21.5}, compte",
    r"diviseurs (\hyperref[IV.21.4]{21.4} et \hyperref[IV.21.5]{21.5}), compte",
    "Printed on p. 289. Labels IV.21.4 and IV.21.5 exist (ega4-21a), so plain \\hyperref keeps the links (as the p. 226 fix).")

# ---------------------------------------------------------------- p. 289 segment (printed p. 289, then p. 290)
add(289, "old position of \\oldpage[IV-4]{289}",
    "printed p. 289 begins 'considérer un O_{X_λ}-Module inversible' (page_289_s1.png)",
    "\\oldpage[IV-4]{289} after \\label{IV.21.10.1}",
    "marker",
    r"\oldpage[IV-4]{289}¶Soient",
    r"Soient",
    "Marker move, part 2 of 2: removes the old marker; part 1 is the previous entry (inserts the marker before "
    "'considérer'). Apply both, in this order (apply_fixes.py then treats the span between the two copies as page 289).",
    after=m289a)
add(289, "(21.10.1), l. 3: '(i.e. tel que dim O_{X',x'} = 1)'",
    "no parentheses around O_{X',x'} (crop p289_dim.png)",
    "$\\dim(\\sh{O}_{X',x'})=1$",
    "formula",
    r"(i.e.\ tel que $\dim(\sh{O}_{X',x'})=1$)",
    r"(i.e.\ tel que $\dim\sh{O}_{X',x'}=1$)",
    "")
add(289, "(21.10.1), l. 4: 'on ait l'une des trois conditions'",
    "'une' italic (crop p289_s3_2101.png)",
    "upright",
    "italics",
    r"on ait l'une des trois",
    r"on ait l'\emph{une} des trois",
    "")
add(289, "(21.10.1) (ii): 'x ∈ X^{(1)} et O_{X',x'} est un O_{X,x}-module plat;'",
    "'et', 'est un' and '-module plat' italic (crop p289_s4_a.png)",
    "upright (env is roman)",
    "italics",
    r"\item $x\in X^{(1)}$ et $\sh{O}_{X',x'}$ est un $\sh{O}_{X,x}$-module plat;",
    r"\item $x\in X^{(1)}$ \emph{et} $\sh{O}_{X',x'}$ \emph{est un} $\sh{O}_{X,x}$\emph{-module plat};",
    "")
add(289, "(21.10.1) (iii): 'l'anneau O_{X,x} est factoriel et m_{x'} ∉ Ass(O_{X',x'}).'",
    "'l'anneau' and 'est factoriel et' italic (crop p289_s4_a.png)",
    "upright",
    "italics",
    r"\item l'anneau $\sh{O}_{X,x}$ est factoriel et $\mathfrak{m}_{x'}",
    r"\item \emph{l'anneau} $\sh{O}_{X,x}$ \emph{est factoriel et} $\mathfrak{m}_{x'}",
    "")
add(289, "(21.10.1): 'Sous ces conditions, nous nous proposons' after the list (i)-(iii)",
    "new indented paragraph (crop p289_s4_a.png)",
    "follows \\end{enumerate} without a blank line, so it is set without the indent",
    "other",
    r"\end{enumerate}¶Sous ces conditions",
    r"\end{enumerate}¶¶Sous ces conditions",
    "GLOBAL_ISSUES 80/99 pattern.")
add(289, "(21.10.1): 'cycle 1-codimensionnel Z sur X de support contenu dans T,'",
    "'de support contenu dans' italic (crop p289_s4_a.png)",
    "upright",
    "italics",
    r"sur $X$ de support contenu dans $T$, de définir",
    r"sur $X$ \emph{de support contenu dans} $T$, de définir",
    "")
m290a = add(289, "end of the page (boundary with p. 290): new position of \\oldpage[IV-4]{290}",
    "printed p. 289 ends '... Z' = f^*(Z), de sorte'; p. 290 begins 'que Z ⇝ f^*(Z) soit un homomorphisme' (page_289_s4.png, page_290_s1.png)",
    "\\oldpage[IV-4]{290} stands before \\begin{env}[21.10.2]: the rest of (21.10.1) (printed on p. 290) is in the p. 289 segment",
    "marker",
    r"$Z'=f^*(Z)$, de sorte que",
    r"$Z'=f^*(Z)$, de sorte¶\oldpage[IV-4]{290}¶que",
    "BOUNDARY FIX (page break 289/290). Marker move, part 1 of 2 (inserts the marker: mid-sentence, no blank lines); "
    "part 2, the removal of the old marker, lies in the p. 290 segment (outside these pages; next entry, page 290): "
    "'\\oldpage[IV-4]{290}\\n\\begin{env}[21.10.2]' -> '\\begin{env}[21.10.2]'. Apply both, after the text fixes: the "
    "p. 289 entries marked 'printed p. 290' concern the end of (21.10.1), printed on p. 290, which lies in the p. 289 "
    "segment until this move; they were checked against page_290_s1/s2.png.")
add(289, "printed p. 290, l. 1: 'que Z ⇝ f^*(Z) soit'",
    "wavy arrow (crop p290_s1_a.png)",
    "\\mapsto",
    "symbol",
    r"$Z\mapsto f^*(Z)$",
    r"$Z\leadsto f^*(Z)$",
    "Printed on p. 290. Does not overlap the marker 290 insertion (that edit ends at 'que').")
add(289, "printed p. 290, l. 1: 'soit un homomorphisme de groupes ordonnés'",
    "'homomorphisme' italic (crop p290_s1_a.png)",
    "upright",
    "italics",
    r"soit un homomorphisme de groupes",
    r"soit un \emph{homomorphisme} de groupes",
    "Printed on p. 290.")
add(289, "printed p. 290, (21.10.1.1): 'Z = Σ n_x . {x}-bar'",
    "baseline period between n_x and {x}-bar (crop p290_nx.png)",
    "n_x\\cdot\\overline{\\{x\\}}",
    "symbol",
    r"T\cap X^{(1)}}n_x\cdot\overline{\{x\}}",
    r"T\cap X^{(1)}}n_x.\overline{\{x\}}",
    "Printed on p. 290. GLOBAL_ISSUES 65 (coordinator note: the print's baseline period, not \\cdot).")
add(289, "printed p. 290, 2°: 'de longueur finie λ_{x'}'",
    "'finie' italic (crop p290_s1_b.png)",
    "upright",
    "italics",
    r"de longueur finie $\lambda_{x'}$",
    r"de longueur \emph{finie} $\lambda_{x'}$",
    "Printed on p. 290.")
add(289, "printed p. 290, 3°: 'il résulte de (21.4.5, (ii)) que'",
    "(21.4.5, (ii)) (crop p290_s2_a.png)",
    "\\sref{IV.21.4.5}, (ii) prints '(21.4.5), (ii)'",
    "punctuation",
    r"\sref{IV.21.4.5}, (ii) que",
    r"\sref{IV.21.4.5}[(ii)] que",
    "Printed on p. 290.")
en1 = add(289, "printed p. 290, end of 3°: '... est canoniquement isomorphe à Z. On a donc un homomorphisme canonique composé'",
    "'On a donc ...' continues the paragraph of 3° on the same line; after the display (21.10.1.2) 'Si Z_x est le cycle' begins a new indented paragraph (page_290_s2.png)",
    "\\end{enumerate} before 'On a donc', so it starts a new unindented line",
    "other",
    r"isomorphe à $\bb{Z}$.¶\end{enumerate}¶On a donc",
    r"isomorphe à $\bb{Z}$.¶On a donc",
    "Printed on p. 290. Part 1 of 2: apply together with the entry that moves \\end{enumerate} to after the display "
    "(otherwise the list is not closed).", conf="medium")
add(289, "printed p. 290, display (21.10.1.2): first arrow",
    "label cyc^{-1} above a tilde above the arrow (isomorphism arrow; crop p290_s2_b.png)",
    "\\xrightarrow{\\operatorname{cyc}^{-1}} (no tilde)",
    "symbol",
    r"\xrightarrow{\operatorname{cyc}^{-1}}",
    r"\xrightarrow{\overset{\operatorname{cyc}^{-1}}{\sim}}",
    "Printed on p. 290. Same form as \\xrightarrow{\\overset{\\pi}{\\sim}} in ega4-21a (21.3.x).")
add(289, "printed p. 290, after the display (21.10.1.2): end of the list 1°-3°",
    "'Si Z_x est le cycle' begins a new indented paragraph",
    "(see part 1)",
    "other",
    r"\tag{21.10.1.2}¶\]¶Si $Z_x$",
    r"\tag{21.10.1.2}¶\]¶\end{enumerate}¶¶Si $Z_x$",
    "Printed on p. 290. Part 2 of 2 with the entry that removes \\end{enumerate} before 'On a donc'; apply both.",
    conf="medium", after=en1)
add(289, "printed p. 290, last sentence of (21.10.1): 'Σ n_y . ({y}-bar ∩ Spec(O_{X,x}))'",
    "baseline period between n_y and the parenthesis (crop p290_ny.png)",
    "n_y(\\overline{\\{y\\}}\\cap... (no period)",
    "missing",
    r"n_y(\overline{\{y\}}",
    r"n_y.(\overline{\{y\}}",
    "Printed on p. 290. As n_x.{x}-bar in (21.10.1.1).")
add(289, "printed p. 290, last sentence of (21.10.1): 'on prend alors pour n_{x'} l'image de Z_x'",
    "'l'image de' italic (crop p290_s2_b.png)",
    "only 'image' italic",
    "italics",
    r"$n_{x'}$ l'\emph{image} de $Z_x$",
    r"$n_{x'}$ \emph{l'image de} $Z_x$",
    "Printed on p. 290.")
add(289, "printed p. 290, last sentence of (21.10.1): 'par l'hcmomorphisme (21.10.1.2)'",
    "'l'hcmomorphisme': a c (width 16 px, like the c of 'cycle' two lines up; the o's of the word are 18-19 px) in place of the first o (crops p290_hcmo.png, p290_hcmo_zoom.png, cmp_c.png)",
    "'l'homomorphisme' (silent correction)",
    "misprint_in_print",
    r"par l'homomorphisme \sref{IV.21.10.1.2}",
    r"par l'hcmomorphisme \sref{IV.21.10.1.2}",
    "Printed on p. 290 (in the p. 289 segment until the marker 290 move). Wrong sort c for o. The heavier-looking 'mom' of "
    "this word is uneven impression (stem widths 5 px against 4 px in 'l'homomorphisme' three lines up; the o between "
    "the m's is not heavier): not recorded.",
    conf="medium", corrected=r"par l'homomorphisme \sref{IV.21.10.1.2}")

# ---------------------------------------------------------------- p. 290 segment (outside these pages)
add(290, "top of the p. 290 segment: old position of \\oldpage[IV-4]{290}",
    "printed p. 290 begins 'que Z ⇝ f^*(Z) soit un homomorphisme' inside (21.10.1); (21.10.2) begins in the middle of p. 290 (page_290_s1.png, page_290_s2.png)",
    "\\oldpage[IV-4]{290} before \\begin{env}[21.10.2]",
    "marker",
    r"\oldpage[IV-4]{290}¶\begin{env}[21.10.2]",
    r"\begin{env}[21.10.2]",
    "OUTSIDE THESE PAGES (p. 290 segment, next batch): BOUNDARY FIX 289/290, part 2 of 2 with the marker insertion "
    "before 'que $Z\\mapsto f^*(Z)$' (previous entry, page 289). Apply both, in this order. The blank line before the "
    "old marker then simply separates \\end{env} and \\begin{env}[21.10.2].", after=m290a)


# ---------------------------------------------------------------- order: content fixes first, marker moves last
# (apply_fixes.py looks for "old" inside the CURRENT segment of its page; moving a marker first would move text
# out of the segment named by the content fixes)
order_markers = []
for d in F:
    if d["kind"] == "marker":
        order_markers.append(d)
content = [d for d in F if d["kind"] != "marker"]
# marker order: 285 remove, 285 insert, 286 remove, 286 insert, 289 insert (p. 288), 289 remove, 290 insert, 290 remove
def mkey(d):
    o = d["fix"]["old"]
    if "{285}" in o: return 0
    if "pour tout $y" in o: return 1
    if "{286}" in o: return 2
    if "sont tels que" in o: return 3
    if "il suffit de considérer" in o: return 4
    if "{289}" in o: return 5
    if "de sorte que" in o: return 6
    if "{290}" in o: return 7
    raise SystemExit("unknown marker entry")
order_markers.sort(key=mkey)
idx_old = {id(d): i for i, d in enumerate(F)}
F_sorted = content + order_markers
# remap _after (indices into the old F) to the new positions, and check the order respects them
pos = {id(d): i for i, d in enumerate(F_sorted)}
for d in F_sorted:
    if d["_after"] is not None:
        pre = F[d["_after"]]
        assert pos[id(pre)] < pos[id(d)], "dependency order broken"
F = F_sorted

# ---------------------------------------------------------------- checks
src = open(SRC, encoding="utf-8", newline="").read()
assert "\r\n" not in src
pages = {}
for p in range(285, 291):
    t = open(f"{RUN}/page_{p}.tex", encoding="utf-8", newline="").read().replace("\r\n", "\n")
    pages[p] = t

ok = True
# 1) every old occurs exactly once in its page file and in the source (sequential ones checked after their predecessor)
for i, d in enumerate(F):
    fx = d["fix"]
    if fx is None:
        continue
    old = fx["old"]
    if d["_after"] is None or d["kind"] != "misprint_in_print":
        cp = pages[d["page"]].count(old)
        cs = src.count(old)
        if cp != 1 or cs != 1:
            print("COUNT PROBLEM", i, d["page"], cp, cs, repr(old)[:120]); ok = False

# 2) apply all fixes in list order exactly as apply_fixes.py does: "old" must occur once in the CURRENT segment of
#    its page (from \oldpage[IV-4]{N} to the next marker with another number; gap rule when the marker is absent),
#    and, as a stricter check, once in the whole file.
import re
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s0) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s0, cuts[j][1] if j < len(cuts) else len(t)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


s = src
for i, d in enumerate(F):
    fx = d["fix"]
    if fx is None:
        continue
    a, b = locate(s, d["page"])
    seg = s[a:b]
    if seg.count(fx["old"]) != 1 or s.count(fx["old"]) != 1:
        print("SEQUENTIAL PROBLEM", i, d["page"], seg.count(fx["old"]), s.count(fx["old"]), repr(fx["old"])[:120]); ok = False
        continue
    s = s[:a] + seg.replace(fx["old"], fx["new"]) + s[b:]

# markers: each of 285..290 exactly once
for p in range(284, 292):
    c = s.count("\\oldpage[IV-4]{%d}" % p)
    if c != 1:
        print("marker count", p, c); ok = False

# misprint new strings: the misprint edit changes only the misprinted characters (sanity: show the diff)
import difflib
for i, d in enumerate(F):
    if d["kind"] == "misprint_in_print":
        a, b = d["fix"]["old"], d["fix"]["new"]
        sm = difflib.SequenceMatcher(None, a, b)
        print("misprint", d["page"], [op for op in sm.get_opcodes() if op[0] != "equal"])

open(f"{RUN}/crops_285_289/ega4-21b_after_fixes_preview.txt", "w", encoding="utf-8", newline="").write(s)
print("findings:", len(F), "ok:", ok)

out = []
for d in F:
    d = dict(d)
    d.pop("_after")
    out.append(d)
if ok:
    json.dump(out, open(f"{RUN}/findings_285_289.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("written")
