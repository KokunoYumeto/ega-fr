"""Build findings_195_199.json and check every 'old' (exactly once in page_NNN.tex and in the current source segment)."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex")
OUT = RUN / "findings_195_199.json"
NL = "\u23ce"  # placeholder for a line break in the strings below


def s(x):
    return None if x is None else x.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None, nofix=False):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if nofix else dict(old=s(old), new=s(new)))
    if kind == "misprint_in_print":
        d["corrected"] = s(corrected)
    d["note"] = note
    F.append(d)


C6L = "GLOBAL_ISSUES 16/88 (labels upright inside italic statements)."
C7 = "Long dash for set difference; \\setmin pending the convention-7 decision."
FRAK = "Wrong letter \\mathfrak R for the print's Fraktur K (GLOBAL_ISSUES 63; same as pp. 188-189)."
GRB = "Raised bullet in the print (the print's gr^\\bullet, not ^*)."

# ---------------------------------------------------------------- p. 195
add(195, "top of p. 195: page break 194/195 inside item (ii) of the proof of Lemme (19.3.2.1), '... ; on en | conclut que x et y sont inversibles'",
    "p. 195 begins mid-sentence with 'conclut que x et y sont inversibles' at the left margin, no indent (page_195_s1.png)",
    "blank line after \\oldpage[IV-4]{195} (and one before it at the end of the p. 194 segment): a paragraph break the print lacks",
    "marker", None, "high",
    r"\oldpage[IV-4]{195}⏎⏎conclut que", r"\oldpage[IV-4]{195}⏎conclut que",
    "BOUNDARY FIX (page break with p. 194). The marker is at the right place; both blank lines must go (\\oldpage ends with \\ignorespaces, which does not skip a \\par). The blank line BEFORE the marker is already gone in the current source (findings_190_194, applied); this edit removes the one after it.")
add(195, "item (iii) of the proof of Lemme (19.3.2.1): 'topologie r-adique de E (0_I, 7.3.5)'",
    "(0_I, 7.3.5) with a bold 0", "($0_{\\mathrm I}$, 7.3.5)", "convention", 2, "high",
    r"($0_{\mathrm I}$, 7.3.5)", r"($\mathbf{0}_{\mathrm I}$, 7.3.5)")
add(195, "'Ce lemme étant établi, il résulte du théorème de Cohen (0, 19.8.8)'",
    "(0, 19.8.8) with a bold 0", "($0$, 19.8.8)", "convention", 2, "high",
    r"($0$, 19.8.8)", r"(\textbf{0}, 19.8.8)")
add(195, "proof of Corollaire (19.3.4): 'du schéma régulier Y=Spec(k[T_1,...,T_n]) (0, 17.3.7)'",
    "(0, 17.3.7) with a bold 0", "($0$, 17.3.7)", "convention", 2, "high",
    r"($0$, 17.3.7)", r"(\textbf{0}, 17.3.7)")
add(195, "proof of Corollaire (19.3.4): 'que l'immersion Y→X est régulière au point x'",
    "Y→X (crop p195_YX.png)", "$Y\\to X$ (printed reading kept)", "misprint_in_print", None, "high",
    None, None,
    "X is the closed subprescheme of Y = Spec(k[T_1,...,T_n]) defined two lines above, so the immersion is X→Y. The TeX keeps the printed reading. Same slip in the next finding (Y'→X'). Not in the errata.",
    corrected=r"$X\to Y$", nofix=True)
add(195, "proof of Corollaire (19.3.4): 'si et seulement si l'immersion Y'→X' l'est au point x''",
    "Y'→X' (crop p195_YX.png)", "$Y'\\to X'$ (printed reading kept)", "misprint_in_print", None, "high",
    None, None,
    "X' = X⊗_k k' is a closed subprescheme of Y' = Y⊗_k k', so the immersion is X'→Y'. The TeX keeps the printed reading.",
    corrected=r"$X'\to Y'$", nofix=True)
add(195, "Corollaire (19.3.5), label a)", "label a) upright inside the italic statement (crop p195_ab.png)",
    "\\item[a)] (italic in the corollary environment)", "convention", 6, "high",
    r"\item[a)] L'idéal", r"\item[\textup{a)}] L'idéal", C6L)
add(195, "Corollaire (19.3.5), label b)", "label b) upright inside the italic statement (crop p195_ab.png)",
    "\\item[b)] (italic in the corollary environment)", "convention", 6, "high",
    r"\item[b)] $B$ est un", r"\item[\textup{b)}] $B$ est un", C6L)

# ---------------------------------------------------------------- p. 196
add(196, "proof of (19.3.5): 'En vertu de (19.2.4), la condition a) équivaut'",
    "whole label a) italic in roman text (crop p196_cond_a.png)", "$a)$ (italic a, upright parenthesis)", "italics", None, "high",
    r"la condition $a)$ équivaut", r"la condition \emph{a)} équivaut", "GLOBAL_ISSUES 88.")
add(196, "proof of (19.3.5): 'la platitude de B sur A (0_I, 6.1.2)'",
    "(0_I, 6.1.2) with a bold 0", "($0_{\\mathrm I}$, 6.1.2)", "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.1.2)", r"($\mathbf{0}_{\mathrm I}$, 6.1.2)")
add(196, "Définition (19.3.6): 'Soit f: X→S un morphisme plat localement de présentation finie.'",
    "'plat' set in roman inside the italic definition (crop p196_s1_def.png)", "plat (italic)", "convention", 6, "high",
    r"un morphisme plat localement de présentation finie. On dit", r"un morphisme \textup{plat} localement de présentation finie. On dit",
    "In Corollaire (19.3.8) and (19.3.10) the same words are all italic, as the TeX has them.")
add(196, "Définition (19.3.6): 'On dit que X est une intersection complète relativement à S en un point x'",
    "only 'intersection complète relativement à S' is roman; 'en un point x, si la fibre' is italic (crop p196_s1_def.png)",
    "\\emph{intersection complète relativement à $S$ en un point} $x$", "convention", 6, "high",
    r"\emph{intersection complète relativement à $S$ en un point} $x$", r"\emph{intersection complète relativement à $S$} en un point $x$",
    "The \\emph (upright inside the italic environment) is narrowed to the words the print sets roman.")
add(196, "Définition (19.3.6), second sentence: 'On dit que X est une intersection complète relativement à S, ou que le morphisme f est un morphisme d'intersection complète, si ...'",
    "the whole sentence is italic: no roman words (crop p196_s2_def.png)",
    "\\emph{intersection complète relativement à $S$} and \\emph{morphisme d'intersection complète} (upright)", "convention", 6, "high",
    r"est une \emph{intersection complète relativement à $S$}, ou que le morphisme $f$ est un \emph{morphisme d'intersection complète}, si",
    r"est une intersection complète relativement à $S$, ou que le morphisme $f$ est un morphisme d'intersection complète, si",
    "FIX_POLICY 2.6: drop \\emph where the print shows no change of face. Independent of the previous finding (the two 'old' strings do not overlap).")
add(196, "proof of Corollaire (19.3.8): 'Comme E=Y—f(X—U)'",
    "two long dashes (crop p196_s3_EY.png)", "$E=Y-f(X-U)$ (minus signs)", "convention", 7, "high",
    r"$E=Y-f(X-U)$", r"$E=Y\setmin f(X\setmin U)$",
    "Two long dashes in one edit. " + C7 + " The Y is the print's misprint (next finding), kept.")
add(196, "proof of Corollaire (19.3.8): 'Comme E=Y—f(X—U)'",
    "E = Y—f(X—U) (crop p196_s3_EY.png)", "$E=Y-f(X-U)$ (printed reading kept)", "misprint_in_print", None, "high",
    None, None,
    "E is the set of s∈S whose fibre is a complete intersection at all its points, so E = S—f(X—U); (19.3.8) has no Y (f: X→S). The TeX keeps the printed Y. In the corrected edition change only Y to S (after the convention-7 edit above). Not in the errata.",
    corrected=r"$E=S\setmin f(X\setmin U)$", nofix=True)
add(196, "Proposition (19.3.9), label (i)", "label (i) upright inside the italic statement", "\\item[(i)] (italic)", "convention", 6, "high",
    r"\item[(i)] Toute", r"\item[\textup{(i)}] Toute", "GLOBAL_ISSUES 16.")
add(196, "Proposition (19.3.9), label (ii)", "label (ii) upright inside the italic statement", "\\item[(ii)] (italic)", "convention", 6, "high",
    r"\item[(ii)] Soit", r"\item[\textup{(ii)}] Soit", "GLOBAL_ISSUES 16.")
add(196, "Proposition (19.3.9), label (iii)", "label (iii) upright inside the italic statement", "\\item[(iii)] (italic)", "convention", 6, "high",
    r"\item[(iii)] Si", r"\item[\textup{(iii)}] Si", "GLOBAL_ISSUES 16.")
add(196, "foot of p. 196: page break 196/197, '... il en est de | même de f''",
    "p. 196 ends 'il en est de', p. 197 begins 'même de f' (2.1.4)' at the left margin (mid-sentence)",
    "blank line before \\oldpage[IV-4]{197} (and one after it)", "marker", None, "high",
    r"il en est de⏎⏎", r"il en est de⏎",
    "The marker is at the right place. Part 1 of 2: the first p. 197 finding removes the blank line after \\oldpage[IV-4]{197}; apply both (\\oldpage ends with \\ignorespaces, which does not skip a \\par).")

# ---------------------------------------------------------------- p. 197
add(197, "top of p. 197: 'même de f' (2.1.4)'", "continuation of the sentence of p. 196, no indent",
    "blank line after \\oldpage[IV-4]{197}", "marker", None, "high",
    r"\oldpage[IV-4]{197}⏎⏎même de $f'$", r"\oldpage[IV-4]{197}⏎même de $f'$",
    "Part 2 of 2 with the last p. 196 finding; both blank lines must go.")
add(197, "proof of Corollaire (19.3.10): 'puisque A et A' ont même corps résiduel (I, 3.6.4)'",
    "(I, 3.6.4) with a bold I", "(I, 3.6.4)", "convention", 2, "high",
    r"(I, 3.6.4)", r"(\textbf{I}, 3.6.4)",
    "Genuine EGA I reference (bold I in the print), not EGA IV's own (1.3.6.4).")
add(197, "proof of (19.3.10): 'le séparé complété (E⊗_A Â)^ de l'anneau E⊗_A Â'",
    "a raised circumflex after the closing parenthesis (crop p197_s2_hat2.png)", "(E\\otimes_A\\widehat A)^{\\wedge} (prints a wedge)", "symbol", None, "high",
    r"(E\otimes_A\widehat A)^{\wedge}", r"(E\otimes_A\widehat A)^{\widehat{\,}}",
    "Same form as the earlier page fixes of the raised circumflex (p. 171; EGA II p. 194); \\superhat pending (GLOBAL_ISSUES 31/47).")
add(197, "proof of (19.3.10): 'isomorphe au séparé complété de Ê⊗_Â Â ≅ Ê'",
    "a plain ⊗ (no hat) with the subscript Â (crops p197_s2_tens.png, p197_s2_otimes.png)",
    "\\widehat E\\widehat\\otimes_A\\widehat A\\cong\\widehat E (completed tensor product over A)", "formula", None, "high",
    r"\widehat E\widehat\otimes_A\widehat A\cong\widehat E", r"\widehat E\otimes_{\widehat A}\widehat A\cong\widehat E",
    "The TeX rewrote the printed formula (GLOBAL_ISSUES 46/102 pattern).")
add(197, "proof of (19.3.10): 'donc au séparé complété Ê de E (0_I, 7.7.1)'",
    "(0_I, 7.7.1) with a bold 0", "($0_{\\mathrm I}$, 7.7.1)", "convention", 2, "high",
    r"($0_{\mathrm I}$, 7.7.1)", r"($\mathbf{0}_{\mathrm I}$, 7.7.1)")
add(197, "proof of (19.3.10): 'les anneaux de polynômes sur un corps sont des anneaux réguliers (0, 17.3.7)'",
    "(0, 17.3.7) with a bold 0", "($0$, 17.3.7)", "convention", 2, "high",
    r"réguliers ($0$, 17.3.7)", r"réguliers (\textbf{0}, 17.3.7)")
add(197, "proof of (19.3.10): 'on peut par hypothèse l'écrire A'/K'",
    "Fraktur K 𝔎: arched top with the flag at the right, no separate left curl (crops p197_frakK_a.png, p197_frakK_b.png, p197_s4_K1.png, p197_s4_K2.png; compared with the 𝔎 of 0_IV pp. 66/80 and the ℜ of p. 180)",
    "\\mathfrak R", "symbol", None, "high",
    r"l'écrire $A'/\mathfrak R$", r"l'écrire $A'/\mathfrak K$",
    FRAK + " Edit 1 of 5; all six \\mathfrak R of the page are this letter.")
add(197, "proof of (19.3.10): 'où A' est un anneau local régulier et K un idéal de A''",
    "Fraktur K", "\\mathfrak R", "symbol", None, "high",
    r"et $\mathfrak R$ un idéal", r"et $\mathfrak K$ un idéal", "Edit 2 of 5 (see edit 1).")
add(197, "proof of (19.3.10): 'un idéal de A' (0, 19.8.8)'",
    "(0, 19.8.8) with a bold 0", "($0$, 19.8.8)", "convention", 2, "high",
    r"($0$, 19.8.8)", r"(\textbf{0}, 19.8.8)", "Independent of the Fraktur edits on the same line (no overlap).")
add(197, "proof of (19.3.10): 'entraîne que K est engendré par une suite régulière'",
    "Fraktur K", "\\mathfrak R", "symbol", None, "high",
    r"entraîne que $\mathfrak R$ est engendré", r"entraîne que $\mathfrak K$ est engendré", "Edit 3 of 5 (see edit 1).")
add(197, "proof of (19.3.10): 'engendrant l'idéal K'=K[T_1,...,T_r]'",
    "Fraktur K twice", "\\mathfrak R twice", "symbol", None, "high",
    r"$\mathfrak R'=\mathfrak R[T_1,\ldots,T_r]$", r"$\mathfrak K'=\mathfrak K[T_1,\ldots,T_r]$", "Edit 4 of 5 (see edit 1).")
add(197, "proof of (19.3.10): '(0, 15.1.4)'",
    "(0, 15.1.4) with a bold 0", "($0$, 15.1.4)", "convention", 2, "high",
    r"($0$, 15.1.4)", r"(\textbf{0}, 15.1.4)")
add(197, "proof of (19.3.10): 'comme C'/K'=C'",
    "Fraktur K", "\\mathfrak R", "symbol", None, "high",
    r"$C'/\mathfrak R'=C$", r"$C'/\mathfrak K'=C$", "Edit 5 of 5 (see edit 1).")
add(197, "end of the proof of (19.3.10): 'puisque C' est un anneau régulier (0, 17.3.7).'",
    "(0, 17.3.7) with a bold 0", "($0$, 17.3.7)", "convention", 2, "high",
    r"régulier ($0$, 17.3.7).", r"régulier (\textbf{0}, 17.3.7).")
add(197, "heading 19.4 'Application : critères de régularité et de lissité pour les préschémas éclatés.'",
    "p. 197 ends with '(0, 17.3.7).'; the heading 19.4 is printed at the top of p. 198 (page_197_s4.png, page_198_s1.png)",
    "\\subsection{Application: ...} and its \\EGAReaderTarget stand before \\oldpage[IV-4]{198}, i.e. on p. 197", "marker", None, "high",
    r"\subsection{Application: critères", r"\oldpage[IV-4]{198}⏎⏎\subsection{Application: critères",
    "Marker 198 stands too late. Part 1 of 2: inserts the marker before the heading (a new heading: the blank lines stay, as at markers 63, 72, 111); the first p. 198 finding deletes the old marker. Apply both (apply_fixes.py treats the span between the two 198 markers as page 198). Same form as the 189/190 boundary fix for heading 19.2.")

# ---------------------------------------------------------------- p. 198
add(198, "top of p. 198 (old marker position)", "p. 198 begins with the heading 19.4, then (19.4.1)",
    "\\oldpage[IV-4]{198} after the heading", "marker", None, "high",
    r"\oldpage[IV-4]{198}⏎⏎\begin{env}[19.4.1]", r"\begin{env}[19.4.1]",
    "Part 2 of 2 with the last p. 197 finding (which re-inserts \\oldpage[IV-4]{198} before the 19.4 heading).")
add(198, "(19.4.1): 'Rappelons (II, 8.1.3)'", "(II, 8.1.3) with a bold II", "(II, 8.1.3)", "convention", 2, "high",
    r"Rappelons (II, 8.1.3)", r"Rappelons (\textbf{II}, 8.1.3)")
add(198, "display (19.4.1.1) '0 → O_X'(1) → O_X' → O_Y' → 0'",
    "no full stop after the display: the sentence goes on with 'où J O_X' est l'image de ũ_0' (crop p198_disp.png)",
    "\\longrightarrow0. (full stop)", "punctuation", None, "high",
    r"\longrightarrow\sh{O}_{Y'}\longrightarrow0.", r"\longrightarrow\sh{O}_{Y'}\longrightarrow0")
add(198, "(19.4.1): 'est l'image de ũ_0 (II, 8.1.7 et 8.1.8)'", "(II, 8.1.7 et 8.1.8) with a bold II", "(II, 8.1.7 et 8.1.8)", "convention", 2, "high",
    r"(II, 8.1.7 et 8.1.8)", r"(\textbf{II}, 8.1.7 et 8.1.8)")
add(198, "Lemme (19.4.2): 'Proj(gr•_J(O_X))'", "gr with a raised bullet (crop p198_gr.png)", "\\operatorname{gr}_{\\mathscr J}^*", "symbol", None, "high",
    r"\operatorname{Proj}(\operatorname{gr}_{\mathscr J}^*(\sh{O}_X))", r"\operatorname{Proj}(\operatorname{gr}_{\mathscr J}^\bullet(\sh{O}_X))", GRB)
add(198, "proof of (19.4.2): 'La seconde assertion résulte de (II, 3.5.3)'",
    "(II, 3.5.3) (crop p198_II353.png)", "(II, 3.3.3)", "number", None, "high",
    r".3.3) appliqué", r".5.3) appliqué",
    "EGA II (3.5.3) is the base change of Proj, applied here to Y→X. Independent of the next (convention-2) finding: the two 'old' strings do not overlap.")
add(198, "proof of (19.4.2): '(II, 3.5.3)'", "(II, ...) with a bold II", "(II, 3.3.3)", "convention", 2, "high",
    r"résulte de (II, 3", r"résulte de (\textbf{II}, 3")
add(198, "proof of (19.4.2): 'S⊗_{O_X} O_Y = gr•_J(O_X)'", "gr with a raised bullet (crop p198_S2.png)", "\\operatorname{gr}_{\\mathscr J}^*", "symbol", None, "high",
    r"=\operatorname{gr}_{\mathscr J}^*(\sh{O}_X)$ par définition", r"=\operatorname{gr}_{\mathscr J}^\bullet(\sh{O}_X)$ par définition", GRB)
add(198, "proof of (19.4.3): 'et gr•_J(O_X) est isomorphe à'", "gr with a raised bullet (crop p198_S.png)", "\\operatorname{gr}_{\\mathscr J}^*", "symbol", None, "high",
    r"fini et $\operatorname{gr}_{\mathscr J}^*(\sh{O}_X)$ est isomorphe", r"fini et $\operatorname{gr}_{\mathscr J}^\bullet(\sh{O}_X)$ est isomorphe", GRB)
add(198, "proof of (19.4.3): 'S•_{O_Y}(N_{Y/X}) (16.9.8)'", "bold S with a raised bullet (crop p198_S.png)", "\\mathbf S_{\\sh{O}_Y}^*", "symbol", None, "high",
    r"\mathbf S_{\sh{O}_Y}^*(", r"\mathbf S_{\sh{O}_Y}^\bullet(",
    "Raised bullet in the print, as for gr. The bold P of P(N_{Y/X}) is upright in the print (crop p198_P.png): \\mathbf P stays.")
add(198, "Proposition (19.4.4): 'Avec les notations de (19.4.1),'", "reference upright inside the italic statement (crop p198_prop4.png)",
    "(19.4.1) (italic)", "convention", 6, "high",
    r"Avec les notations de (19.4.1),", r"Avec les notations de \textup{(19.4.1)},")
add(198, "Corollaire (19.4.5): 'Sous les hypothèses générales de (19.4.4),'", "reference upright inside the italic statement (crop p198_s4_d.png)",
    "(19.4.4) (italic)", "convention", 6, "high",
    r"générales de (19.4.4),", r"générales de \textup{(19.4.4)},")
add(198, "foot of p. 198: page break 198/199 inside Corollaire (19.4.5), '... (7.8.6, (iii))) | et si Y est régulier'",
    "p. 199 begins mid-sentence with 'et si Y est régulier' at the left margin (page_199_s1.png)",
    "blank line before \\oldpage[IV-4]{199} (and one after it)", "marker", None, "high",
    r"(iii)))⏎⏎", r"(iii)))⏎",
    "The marker is at the right place. Part 1 of 2: the first p. 199 finding removes the blank line after \\oldpage[IV-4]{199}; apply both. Apply this BEFORE the next finding (convention 6 on the same parenthetical): after that edit the text reads '(iii)))}' and this 'old' no longer matches.")
add(198, "Corollaire (19.4.5): 'Si Reg(X) est ouvert ((6.12), par exemple si X est excellent (7.8.6, (iii)))'",
    "the parenthetical is roman, with 'excellent' italic (crops p198_s4_a.png, p198_s4_b.png)",
    "all italic (corollary environment)", "convention", 6, "high",
    r"((6.12), par exemple si $X$ est excellent (7.8.6, (iii)))", r"\textup{((6.12), par exemple si $X$ est \emph{excellent} (7.8.6, (iii)))}",
    "Inside \\textup the \\emph gives italic. Apply after the previous (marker) finding. The print shows a gap and no point between 7 and 8 in '(7.8.6': taken as a point that did not print, not reported.")

# ---------------------------------------------------------------- p. 199
add(199, "top of p. 199: 'et si Y est régulier'", "continuation of Corollaire (19.4.5) from p. 198, no indent",
    "blank line after \\oldpage[IV-4]{199}", "marker", None, "high",
    r"\oldpage[IV-4]{199}⏎⏎et si $Y$", r"\oldpage[IV-4]{199}⏎et si $Y$",
    "Part 2 of 2 with the marker finding at the end of p. 198; both blank lines must go.")
add(199, "Corollaire (19.4.5): 'régulier aux points de U—Y'", "long dash (crop p199_s1_top.png)", "$U-Y$", "convention", 7, "high",
    r"points de $U-Y$.", r"points de $U\setmin Y$.", C7)
add(199, "proof of (19.4.5): 'un schéma local de point fermé x;'",
    "the x is bold italic: side by side with the x's of 'point x'_1', 'point x_1 puisque' and 'x'_1' on the same strip it is clearly heavier, mid-line, like the wrong-fount x of p. 71 (crops p199_x_side.png, p199_x_cmp4.png, cmp_p71bold_p199.png)",
    "$x$ (silent correction)", "misprint_in_print", None, "medium",
    r"fermé $x$; l'hypothèse", r"fermé $\boldsymbol{x}$; l'hypothèse",
    "Wrong-fount letter recorded as a misprint (GLOBAL_ISSUES 29/99). Measured ink: stroke 4.4 px against 3.3-4.0 px for the other italic x's of the strip (glyph_ink.py); less heavy than the p. 38 n, hence medium confidence. The fix restores the printed reading.",
    corrected=r"fermé $x$; l'hypothèse")
add(199, "proof of (19.4.5): 'Y est régulier (0, 17.3.2), donc'", "(0, 17.3.2) with a bold 0", "($0$, 17.3.2)", "convention", 2, "high",
    r"régulier ($0$, 17.3.2), donc", r"régulier (\textbf{0}, 17.3.2), donc")
add(199, "proof of (19.4.5): 'et par suite (II, 7.2.1)'", "(II, 7.2.1) with a bold II", "(II, 7.2.1)", "convention", 2, "high",
    r"par suite (II, 7.2.1)", r"par suite (\textbf{II}, 7.2.1)")
add(199, "proof of (19.4.5): 'au-dessus de x_1 (II, 8.1.3)'", "(II, 8.1.3) with a bold II", "(II, 8.1.3)", "convention", 2, "high",
    r"de $x_1$ (II, 8.1.3)", r"de $x_1$ (\textbf{II}, 8.1.3)")
add(199, "proof of (19.4.5): 'en lui appliquant (19.4.4) et utilisant (0, 17.3.2)'", "(0, 17.3.2) with a bold 0", "($0$, 17.3.2)", "convention", 2, "high",
    r"utilisant ($0$, 17.3.2)", r"utilisant (\textbf{0}, 17.3.2)")
add(199, "proof of (19.4.5): 'puisque X'—Y' est isomorphe à X—Y'", "two long dashes", "$X'-Y'$, $X-Y$", "convention", 7, "high",
    r"$X'-Y'$ est isomorphe à $X-Y$", r"$X'\setmin Y'$ est isomorphe à $X\setmin Y$", "Two long dashes in one edit. " + C7)
add(199, "proof of (19.4.5): 'isomorphe à X—Y (II, 8.1.3). Si Y'", "(II, 8.1.3) with a bold II", "(II, 8.1.3)", "convention", 2, "high",
    r"(II, 8.1.3). Si", r"(\textbf{II}, 8.1.3). Si", "Independent of the previous finding (no overlap).")
add(199, "proof of (19.4.5): 'tout point de X—Y qui est générisation'", "long dash", "$X-Y$", "convention", 7, "high",
    r"tout point de $X-Y$ qui", r"tout point de $X\setmin Y$ qui", C7)
add(199, "proof of (19.4.5): 'donc ouvert (0_III, 9.2.5)'", "(0_III, 9.2.5) with a bold 0", "($0_{\\mathrm{III}}$, 9.2.5)", "convention", 2, "high",
    r"($0_{\mathrm{III}}$, 9.2.5)", r"($\mathbf{0}_{\mathrm{III}}$, 9.2.5)")
add(199, "Proposition (19.4.6), label (i)", "label (i) upright inside the italic statement (crop p199_s2_i.png)", "\\item[(i)] (italic)", "convention", 6, "high",
    r"\item[(i)] Les conditions", r"\item[\textup{(i)}] Les conditions", "GLOBAL_ISSUES 16.")
add(199, "Proposition (19.4.6) (i), label a)", "label a) upright (crop p199_s2_a.png)", "\\item[a)] (italic)", "convention", 6, "high",
    r"\item[a)]", r"\item[\textup{a)}]", C6L)
add(199, "Proposition (19.4.6) (i) a): 'gr•_J(O_X) est une O_X-Algèbre g-plate'", "gr with a raised bullet (crop p199_s2_a.png)", "\\operatorname{gr}_{\\mathscr J}^*", "symbol", None, "high",
    r"$\operatorname{gr}_{\mathscr J}^*(\sh{O}_X)$ est une", r"$\operatorname{gr}_{\mathscr J}^\bullet(\sh{O}_X)$ est une",
    GRB + " Independent of the label edit before it (no overlap). The heavier 'g-plate.' at the end of the line is line-end heaviness (item 100), not reported.")
add(199, "Proposition (19.4.6) (i), label b)", "label b) upright", "\\item[b)] (italic)", "convention", 6, "high",
    r"\item[b)]", r"\item[\textup{b)}]", C6L)
add(199, "Proposition (19.4.6) (i) b): '(en d'autres termes, le n-ème voisinage infinitésimal Y^(n) de Y dans X (16.1.2) est S-plat)'",
    "the parenthetical is roman, with 'n-ème voisinage infinitésimal' and 'plat' italic (crops p199_s2_b1.png, p199_s2_b2.png)",
    "all italic (proposition environment)", "convention", 6, "high",
    r"(en d'autres termes, le $n$-ème voisinage infinitésimal $Y^{(n)}$ de $Y$ dans $X$ (16.1.2) est $S$-plat)",
    r"\textup{(en d'autres termes, le \emph{$n$-ème voisinage infinitésimal} $Y^{(n)}$ de $Y$ dans $X$ (16.1.2) est $S$-\emph{plat})}",
    "Inside \\textup the \\emph gives italic.")
add(199, "Proposition (19.4.6) (i), label c)", "label c) upright (crop p199_s2_c1.png)", "\\item[c)] (italic)", "convention", 6, "high",
    r"\item[c)]", r"\item[\textup{c)}]",
    C6L + " The heavier 'et tout entier' on this line lies in a band of heavier impression across pp. 199 strips 2-3 (also 'des Tor montre', 'M est un'), not a wrong fount: not reported.")
add(199, "Proposition (19.4.6) (i): 'Lorsqu'il en est ainsi, Y' est S-plat'", "indented new paragraph after c) (page_199_s2.png)",
    "follows \\end{enumerate} without a blank line (set without indent)", "other", None, "high",
    r"\end{enumerate}⏎  Lorsqu'il en est ainsi", r"\end{enumerate}⏎⏎  Lorsqu'il en est ainsi",
    "Paragraph after the list, indented as printed (GLOBAL_ISSUES 80 pattern); inside item (i) the proposition's italic continues.")
add(199, "Proposition (19.4.6), label (ii)", "label (ii) upright (crop p199_s3_ii.png)", "\\item[(ii)] (italic)", "convention", 6, "high",
    r"\item[(ii)] Supposons", r"\item[\textup{(ii)}] Supposons", "GLOBAL_ISSUES 16.")
add(199, "Proposition (19.4.6) (ii): 'les conditions équivalentes de (i) soient satisfaites'", "(i) upright (crop p199_s3_ii.png)",
    "(i) (italic)", "convention", 6, "high",
    r"de (i) soient satisfaites", r"de \textup{(i)} soient satisfaites")
add(199, "Proposition (19.4.6) (ii): 'l'ensemble des points de X (resp. X') où X (resp. X') est S-plat'",
    "both '(resp. X')' upright (crop p199_s3_resp.png)", "(resp. $X'$) twice (italic)", "convention", 6, "high",
    r"(resp. $X'$) où $X$ (resp. $X'$) est", r"\textup{(resp. $X'$)} où $X$ \textup{(resp. $X'$)} est",
    "GLOBAL_ISSUES 101: parentheses with 'resp.' are upright.")
add(199, "Proposition (19.4.6) (ii): 'est un voisinage de Y (resp. Y').'", "'(resp. Y')' upright (crop p199_s3_resp.png)", "(resp. $Y'$) (italic)", "convention", 6, "high",
    r"de $Y$ (resp. $Y'$).", r"de $Y$ \textup{(resp. $Y'$)}.")
add(199, "proof of (19.4.6) (i): 'L'équivalence de a) et b) résulte'", "whole labels italic in roman text (crop p199_proof_abc.png)",
    "$a)$, $b)$", "italics", None, "high",
    r"L'équivalence de $a)$ et $b)$ résulte", r"L'équivalence de \emph{a)} et \emph{b)} résulte", "GLOBAL_ISSUES 88.")
add(199, "proof of (19.4.6) (i): 'résulte aussitôt de (0_I, 6.1.2)'", "(0_I, 6.1.2) with a bold 0", "($0_{\\mathrm I}$, 6.1.2)", "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.1.2)", r"($\mathbf{0}_{\mathrm I}$, 6.1.2)")
add(199, "proof of (19.4.6) (i): 'pour montrer l'équivalence de b) et c),'", "whole labels italic (crop p199_proof_abc.png)",
    "$b)$, $c)$", "italics", None, "high",
    r"l'équivalence de $b)$ et $c)$,", r"l'équivalence de \emph{b)} et \emph{c)},", "GLOBAL_ISSUES 88.")
add(199, "proof of (19.4.6) (i): 'la condition c) implique'", "whole label italic (crop p199_proof_c.png)", "$c)$", "italics", None, "high",
    r"la condition $c)$ implique", r"la condition \emph{c)} implique", "GLOBAL_ISSUES 88.")
add(199, "proof of (19.4.6): 'si l'on pose C=gr•_J(B)'", "gr with a raised bullet (crop p199_s4_gr.png)", "\\operatorname{gr}_{\\mathfrak J}^*", "symbol", None, "high",
    r"C=\operatorname{gr}_{\mathfrak J}^*(B)", r"C=\operatorname{gr}_{\mathfrak J}^\bullet(B)", GRB)
add(199, "proof of (19.4.6): 'en vertu de (19.4.2) et de (II, 2.3.6), un'", "(II, 2.3.6) with a bold II", "(II, 2.3.6)", "convention", 2, "high",
    r"(II, 2.3.6)", r"(\textbf{II}, 2.3.6)")
add(199, "foot of p. 199: page break 199/200, '... et de (II, 2.3.6), un | voisinage ouvert affine'",
    "p. 199 ends with 'un' (mid-sentence); the TeX's p. 200 begins 'voisinage ouvert affine'",
    "blank line before \\oldpage[IV-4]{200} (and one after it)", "marker", None, "high",
    r", un⏎⏎", r", un⏎",
    "BOUNDARY FIX (page break with p. 200). The marker is at the right place by the end of p. 199. Part 1 of 2: this removes the blank line before \\oldpage[IV-4]{200}; the blank line AFTER it lies in the p. 200 segment and must go too: '\\oldpage[IV-4]{200}\\n\\nvoisinage' -> '\\oldpage[IV-4]{200}\\nvoisinage' (for the 200-204 checker or the coordinator). Independent of the previous (convention-2) finding: no overlap.")

# ---------------------------------------------------------------- checks
t = SRC.read_text(encoding="utf-8")
mk = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in mk.finditer(t)]


def seg(p):
    i = [k for k, (n, _) in enumerate(cuts) if n == p][0]
    return t[cuts[i][1]:cuts[i + 1][1]]


ok = True
for x in F:
    if not x["fix"]:
        continue
    old = x["fix"]["old"]
    pg = (RUN / f"page_{x['page']}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    n1, n2 = pg.count(old), seg(x["page"]).count(old)
    if n1 != 1 or n2 != 1:
        ok = False
        print("BAD", x["page"], repr(old), n1, n2)
    if old == x["fix"]["new"]:
        ok = False
        print("NOOP", x["page"], repr(old))
print("all olds unique:", ok, "findings:", len(F))
counts = {}
for x in F:
    c = counts.setdefault(x["page"], [0, 0, 0])
    if x["kind"] == "misprint_in_print":
        c[2] += 1
    elif x["kind"] == "convention":
        c[1] += 1
    else:
        c[0] += 1
print(counts)
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("written", OUT)
