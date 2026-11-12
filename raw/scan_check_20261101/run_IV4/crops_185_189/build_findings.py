"""Build findings_185_189.json (EGA IV-4 pp. 185-189). '<NL>' in old/new stands for a line break."""
import json

OUT = r"user\Documents\ega_scan_check_20261101\run_IV4\findings_185_189.json"
F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    fix = None if old is None else {"old": old.replace("<NL>", "\n"), "new": new.replace("<NL>", "\n")}
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 185
add(185, "top of p. 185: page break 184/185 inside '... n'est autre par définition que 𝓛^{⊗n} | (II, 3.7.9, (i)).'",
    "p. 185 begins mid-sentence with '(II, 3.7.9, (i)).' at the left margin, no indent (page_184_s4.png, page_185_s1.png)",
    "blank line after \\oldpage[IV-4]{185} (with the blank line before it: a paragraph break the print lacks)",
    "marker", None, "high",
    r"\oldpage[IV-4]{185}<NL><NL>", r"\oldpage[IV-4]{185}<NL>",
    "BOUNDARY FIX (page break 184/185). The marker is at the right place; both blank lines must go. The blank line "
    "BEFORE the marker (end of the p. 184 segment) is already gone in the current source (findings_180_184, applied); "
    "this edit removes the one after it.")
add(185, "l. 1: '(II, 3.7.9, (i)).'", "(II, 3.7.9, (i)) (crop c185_l1.png)", "(II, 3.7.9, (ii))",
    "number", None, "high", "3.7.9, (ii))", "3.7.9, (i))",
    "EGA II (3.7.9, (i)) is the canonical homomorphism r*(O_P(n)) -> L^{⊗n} used here, so the print is right. "
    "Shares '3.7.9' with the next (convention-2) edit; either order works.")
add(185, "l. 1: '(II, 3.7.9, (i))'", "bold II", "plain II", "convention", 2, "high",
    "(II, 3.7.9", r"(\textbf{II}, 3.7.9", "")
add(185, "l. 2: 'ample (II, 4.6.6))'", "bold II", "plain II", "convention", 2, "high",
    "(II, 4.6.6)", r"(\textbf{II}, 4.6.6)", "")
add(185, "l. 2: '(II, 4.5.6, (i))'", "bold II", "plain II", "convention", 2, "high",
    "(II, 4.5.6, (i))", r"(\textbf{II}, 4.5.6, (i))", "")
add(185, "l. 3: 'à celles de (II, 4.6.3)'", "bold II (crop c185_l2.png)", "plain II", "convention", 2, "high",
    "(II, 4.6.3)", r"(\textbf{II}, 4.6.3)", "")
add(185, "§ 19 introduction, l. 1: 'une étude des immersions régulières (16.9.2)'",
    "'immersions régulières' italic (crop c185_intro.png)", "upright", "italics", None, "high",
    "étude des immersions régulières (16.9.2)", r"étude des \emph{immersions régulières} (16.9.2)", "")
add(185, "proof of (19.1.2): 'on sait (0, 17.1.9)'", "bare bold 0", "($0$, 17.1.9)", "convention", 2, "high",
    "($0$, 17.1.9)", r"(\textbf{0}, 17.1.9)", "")
add(185, "proof of (19.1.2): 'de A (0, 16.4.1)'", "bare bold 0", "($0$, 16.4.1)", "convention", 2, "high",
    "($0$, 16.4.1)", r"(\textbf{0}, 16.4.1)", "")
add(185, "proof of (19.1.2): 'on déduit de (0, 17.1.7)'", "bare bold 0", "($0$, 17.1.7)", "convention", 2, "high",
    "($0$, 17.1.7)", r"(\textbf{0}, 17.1.7)", "")
add(185, "Définition (19.1.3), l. 3: 'soit un O_U/J-Module localement libre'",
    "O_U/J without parentheses (crop c185_OU.png)", "$(\\sh{O}_U/\\mathscr J)$-Module", "formula", None, "high",
    r"soit un $(\sh{O}_U/\mathscr J)$-Module", r"soit un $\sh{O}_U/\mathscr J$-Module", "")
add(185, "Définition (19.1.3): '(ce qui est le cas si Y est quasi-régulièrement immergé dans X)'",
    "the whole parenthetical roman, parentheses upright (crop c185_def2.png)", "italic (definition environment)",
    "convention", 6, "high",
    r"(ce qui est le cas si $Y$ est quasi-régulièrement immergé dans $X$)",
    r"\textup{(ce qui est le cas si $Y$ est quasi-régulièrement immergé dans $X$)}", "")
add(185, "Définition (19.1.3): 'on appelle codimension transversale de Y dans X au point y et on note'",
    "the defined words italic like the rest of the statement, no change of face (crop c185_def2.png)",
    "\\emph{...} inside the italic environment: upright", "italics", None, "high",
    r"\emph{codimension transversale de $Y$ dans $X$ au point $y$}",
    r"codimension transversale de $Y$ dans $X$ au point $y$",
    "FIX_POLICY 2.6: drop \\emph where the print shows no change of face (as in (17.10.1), p. 81).")
add(185, "Définition (19.1.3): 'le rang du (O_y/J_y)-module libre'",
    "O with subscript y only (crop c185_Oy.png)", "\\sh{O}_{U,y}", "formula", None, "high",
    r"$(\sh{O}_{U,y}/", r"$(\sh{O}_y/",
    "Independent of the next finding (misprint in the same parenthesis); the two 'old' strings do not overlap.")
add(185, "Définition (19.1.3): '(O_y/𝔍_y)-module libre 𝒥_y/𝒥_y²'",
    "Fraktur 𝔍_y (same glyph as the 𝔍 of (19.1.2)), while 𝒥_y/𝒥²_y after it is script (crop c185_Oy.png)",
    "\\mathscr J_y (silently corrected)", "misprint_in_print", None, "high",
    r"\mathscr J_y)$-module libre", r"\mathfrak J_y)$-module libre",
    "The statement defines only the script Ideal 𝒥; its stalk is 𝒥_y, as in 𝒥_y/𝒥²_y right after, so the Fraktur 𝔍_y "
    "is a wrong letter. The diplomatic text restores the printed Fraktur; independent of the subscript edit above.",
    corrected=r"\mathscr J_y)$-module libre")
add(185, "Définition (19.1.3): 'on appelle de même codimension transversale de f au point z∈Z'",
    "italic like the rest of the statement, no change of face (crop c185_def3.png)",
    "\\emph{...} inside the italic environment: upright", "italics", None, "high",
    r"\emph{codimension transversale de $f$ au point $z\in Z$}",
    r"codimension transversale de $f$ au point $z\in Z$", "FIX_POLICY 2.6.")
add(185, "Définition (19.1.3), last line but one: 'la codimension tranversale dans X'",
    "'tranversale' (no s after the n; crop c185_tranv.png)", "'transversale' (silently corrected)",
    "misprint_in_print", None, "high",
    "la codimension transversale dans", "la codimension tranversale dans",
    "Not in the errata. Independent of the \\emph edit just before it (no overlap).",
    corrected="la codimension transversale dans")
add(185, "last line of p. 185: page break 185/186 inside '... d'une composante irréduc-|tible de Y'",
    "p. 186 continues the word and the sentence ('tible de Y contenant y;', page_186_s1.png)",
    "blank lines before and after \\oldpage[IV-4]{186}: a paragraph break the print lacks", "marker", None, "high",
    "d'une composante<NL><NL>", "d'une composante<NL>",
    "The marker is at the right place (the TeX keeps the whole word 'irréductible' after it). Part 1 of 2 with the "
    "first p. 186 finding: both blank lines must go.")

# ---------------------------------------------------------------- p. 186
add(186, "top of p. 186: page break 185/186", "mid-sentence continuation 'tible de Y contenant y;'",
    "blank line after \\oldpage[IV-4]{186}", "marker", None, "high",
    r"\oldpage[IV-4]{186}<NL><NL>", r"\oldpage[IV-4]{186}<NL>",
    "Part 2 of 2 with the last p. 185 finding; apply both.")
add(186, "l. 6: 'de rang (m+n—1 choose n—1)'", "long dashes in m+n—1 and n—1 (crop c186_binom.png)",
    "minus signs", "convention", 7, "high",
    r"de rang $\binom{m+n-1}{n-1}$", r"de rang $\binom{m+n\setmin 1}{n\setmin 1}$",
    "Two long dashes in one edit (GLOBAL_ISSUES 23: long dash used for subtraction).")
add(186, "l. 7: 'est donc r(m+n—1 choose n—1)'", "long dashes (crop c186_binom.png)", "minus signs",
    "convention", 7, "high",
    r"est donc $r\binom{m+n-1}{n-1}$", r"est donc $r\binom{m+n\setmin 1}{n\setmin 1}$", "Two long dashes in one edit.")
add(186, "l. 9: 'ce qui prouve la proposition (0, 16.2.3)'", "bare bold 0", "($0$, 16.2.3)", "convention", 2, "high",
    "($0$, 16.2.3)", r"(\textbf{0}, 16.2.3)", "")
add(186, "'(même lorsque X n'est pas localement noethérien)'", "only 'même' italic (crop c186_meme.png)",
    "the whole parenthetical in \\emph", "italics", None, "high",
    r"(\emph{même lorsque $X$ n'est pas localement noethérien})",
    r"(\emph{même} lorsque $X$ n'est pas localement noethérien)", "")
add(186, "Proposition (19.1.5), label (i)", "label (i) upright (crop c186_prop.png)",
    "\\item[(i)] italic in the proposition environment", "convention", 6, "high",
    r"\item[(i)]", r"\item[\textup{(i)}]", "GLOBAL_ISSUES 16.")
add(186, "Proposition (19.1.5), label (ii)", "label (ii) upright", "\\item[(ii)] italic", "convention", 6, "high",
    r"\item[(ii)]", r"\item[\textup{(ii)}]", "GLOBAL_ISSUES 16.")
add(186, "(19.1.5) (ii), l. 1: 'une immersion régulière (resp. quasi-régulière) g : X'→X'",
    "'(resp.' and ')' upright, 'quasi-régulière' italic (crop c186_comma.png)", "all italic (environment)",
    "convention", 6, "high",
    "(resp. quasi-régulière), $g", r"\textup{(resp.}\ quasi-régulière\textup{)}, $g",
    "Same form as (16.9.1), p. 46. Apply before the next finding (misprint, comma).")
add(186, "(19.1.5) (ii), l. 1: '(resp. quasi-régulière) g : X'→X un morphisme plat'",
    "no comma after '(resp. quasi-régulière)' (crop c186_comma.png)", "comma (silently corrected)",
    "misprint_in_print", None, "high",
    r"\textup{)}, $g:X'\to X$ un morphisme plat", r"\textup{)} $g:X'\to X$ un morphisme plat",
    "The comma separating the two hypotheses is missing in the print. 'old' is the text after the previous "
    "(convention-6) edit: apply it second.",
    corrected=r"\textup{)}, $g:X'\to X$ un morphisme plat")
add(186, "(19.1.5) (ii), l. 3: 'est une immersion régulière (resp. quasi-régulière), et pour tout'",
    "'(resp.' and ')' upright, 'quasi-régulière' italic (crop c186_ii.png)", "all italic (environment)",
    "convention", 6, "high",
    "(resp. quasi-régulière), et pour tout", r"\textup{(resp.}\ quasi-régulière\textup{)}, et pour tout", "")
add(186, "Proposition (19.1.5), label (iii)", "label (iii) upright (crop c186_iii.png)", "\\item[(iii)] italic",
    "convention", 6, "high", r"\item[(iii)]", r"\item[\textup{(iii)}]", "GLOBAL_ISSUES 16.")
add(186, "(19.1.5) (iii): 'la suite d'homomorphismes canoniques (16.2.7.1)'",
    "reference upright inside the italic statement (crop c186_iii.png)", "italic (environment)",
    "convention", 6, "high", "canoniques (16.2.7.1)", r"canoniques \textup{(16.2.7.1)}", "")
add(186, "Proposition (19.1.5), label (iv)", "label (iv) upright (crop c186_abc.png)", "\\item[(iv)] italic",
    "convention", 6, "high", r"\item[(iv)]", r"\item[\textup{(iv)}]", "GLOBAL_ISSUES 16.")
add(186, "(19.1.5) (iv), label a)", "label a) upright (crop c186_abc.png)", "\\item[a)] italic",
    "convention", 6, "high", r"\item[a)]", r"\item[\textup{a)}]", "GLOBAL_ISSUES 88.")
add(186, "(19.1.5) (iv), label b)", "label b) upright", "\\item[b)] italic",
    "convention", 6, "high", r"\item[b)]", r"\item[\textup{b)}]", "GLOBAL_ISSUES 88.")
add(186, "(19.1.5) (iv), label c)", "label c) upright (crop c186_cv.png)", "\\item[c)] italic",
    "convention", 6, "high", r"\item[c)]", r"\item[\textup{c)}]", "GLOBAL_ISSUES 88.")
add(186, "(19.1.5) (iv) c): 'la suite d'homomorphismes canoniques (19.1.5.1), restreinte'",
    "reference upright inside the italic statement (crop c186_cv.png)", "italic (environment)",
    "convention", 6, "high", "canoniques (19.1.5.1), restreinte", r"canoniques \textup{(19.1.5.1)}, restreinte", "")
add(186, "Proposition (19.1.5), label (v)", "label (v) upright (crop c186_cv.png)", "\\item[(v)] italic",
    "convention", 6, "high", r"\item[(v)]", r"\item[\textup{(v)}]", "GLOBAL_ISSUES 16.")

# ------------------------------------------- text printed on p. 186 that the TeX has in the p. 187 segment
add(187, "printed p. 186, last line (TeX: start of the p. 187 segment), (19.1.5) (v): "
         "'(ce qui entraîne, par (19.1.1), que f est une immersion régulière au point g(z))'",
    "the parenthetical roman with upright parentheses, only 'immersion régulière' italic (crop c186_cv.png)",
    "all italic (environment)", "convention", 6, "high",
    r"(ce qui entraîne, par (19.1.1), que $f$ est une immersion régulière au point $g(z)$)",
    r"\textup{(ce qui entraîne, par (19.1.1), que $f$ est une \emph{immersion régulière} au point $g(z)$)}",
    "Printed on p. 186. Apply BEFORE the three marker findings that follow (they move this text into the p. 186 "
    "segment). The \\emph keeps the print's italic 'immersion régulière' inside the roman parenthetical.")
add(186, "end of the p. 186 segment: '... et x=f(g(z)) un point régulier' + blank line",
    "printed p. 186 ends with 'de X (ce qui entraîne, par (19.1.1), que f est une immersion régulière au point "
    "g(z)); alors,' (page_186_s4.png); p. 187 begins mid-sentence 'pour que f∘g soit ...' (page_187_s1.png)",
    "\\oldpage[IV-4]{187} stands one line too early, before 'de $X$ (ce qui entraîne', with blank lines around it",
    "marker", None, "high",
    "$x=f(g(z))$ un point régulier<NL><NL>", "$x=f(g(z))$ un point régulier<NL>",
    "Part 1 of 3 (apply all three together): removes the blank line at the end of the p. 186 segment.")
add(187, "start of page_187.tex: \\oldpage[IV-4]{187} before 'de X (ce qui entraîne'",
    "printed p. 187 begins 'pour que f∘g soit une immersion régulière au point z' (page_187_s1.png)",
    "marker and blank line before 'de $X$'", "marker", None, "high",
    r"\oldpage[IV-4]{187}<NL><NL>de $X$", "de $X$",
    "Part 2 of 3: deletes the marker and its blank line here.")
add(187, "page break 186/187 inside '... g(z)); alors, | pour que f∘g soit'",
    "page break after 'alors,' mid-sentence (page_186_s4.png, page_187_s1.png)", "no marker here",
    "marker", None, "high",
    "; alors, pour que $f\\circ g$", "; alors,<NL>\\oldpage[IV-4]{187}<NL>pour que $f\\circ g$",
    "Part 3 of 3: re-inserts the marker at the printed page break, without blank lines (mid-sentence). Its 'old' "
    "starts at the ';' after the parenthetical edited above; no overlap.")

# ---------------------------------------------------------------- p. 187
add(187, "proof of (19.1.5) (ii): 'défini par l'Idéal g*(J)O_X' (I, 4.4.5)'",
    "bold I followed by a comma (crop c187_OXp_z.png)", "plain I", "convention", 2, "high",
    "(I, 4.4.5)", r"(\textbf{I}, 4.4.5)", "Genuine EGA I reference (bold I), not EGA IV's own (1.4.4.5).")
add(187, "proof of (19.1.5) (ii): '(qui engendre g*(J)O_X) en vertu de (0, 15.2.5)'",
    "O_X without prime (crop c187_OX_z.png; the prime of O_X' two lines above is clear, crop c187_OXp_z.png)",
    "\\sh{O}_{X'} (silently corrected)", "misprint_in_print", None, "high",
    r"engendre $g^*(\mathscr J)\sh{O}_{X'}$)", r"engendre $g^*(\mathscr J)\sh{O}_X$)",
    "The sequence (f_i ⊗ 1) consists of sections of O_X' and generates the Ideal g*(J)O_X' of O_X' (as printed "
    "two lines above); the print drops the prime.",
    corrected=r"engendre $g^*(\mathscr J)\sh{O}_{X'}$)")
add(187, "'en vertu de (0, 15.2.5)'", "bare bold 0", "($0$, 15.2.5)", "convention", 2, "high",
    "($0$, 15.2.5)", r"(\textbf{0}, 15.2.5)", "")
add(187, "proof of (iii): 'l'endomorphisme de (O_X/J)/(Σ_{j=m+1}^{i-1} f̄_i(O_X/J)) défini par f̄_i'",
    "set in the line (crop c187_endo.png)", "displayed, with \\big/ and \\Bigl( \\Bigr)", "formula", None, "high",
    r"l'endomorphisme de<NL>\[<NL>  (\sh{O}_X/\mathscr J)\big/\Bigl(\sum_{j=m+1}^{i-1}\overline f_j(\sh{O}_X/\mathscr J)\Bigr)<NL>\]<NL>défini par",
    r"l'endomorphisme de $(\sh{O}_X/\mathscr J)/(\sum_{j=m+1}^{i-1}\overline f_j(\sh{O}_X/\mathscr J))$ défini par",
    "Inline as printed. Apply before the next finding (misprint in the same formula).")
add(187, "same formula: 'Σ_{j=m+1}^{i-1} f̄_i(O_X/J)'",
    "subscript i on f̄ inside the sum over j (crop c187_endo_z.png)", "\\overline f_j (silently corrected)",
    "misprint_in_print", None, "high",
    r"\overline f_j(\sh{O}_X/\mathscr J))$ défini par", r"\overline f_i(\sh{O}_X/\mathscr J))$ défini par",
    "The summation index is j. 'old' is the text after the previous (inline) edit: apply it second.",
    corrected=r"\overline f_j(\sh{O}_X/\mathscr J))$ défini par")
add(187, "proof of (iii): 'alors (O_X/J)/(Σ_{j=m+1}^{i-1}(O_X/J)), restreint à U'",
    "set in the line (crop c187_alors.png)", "displayed, with \\big/ and \\Bigl( \\Bigr)", "formula", None, "high",
    r"; alors<NL>\[<NL>  (\sh{O}_X/\mathscr J)\big/\Bigl(\sum_{j=m+1}^{i-1}\overline f_j(\sh{O}_X/\mathscr J)\Bigr),<NL>\]<NL>restreint à $U$",
    r"; alors $(\sh{O}_X/\mathscr J)/(\sum_{j=m+1}^{i-1}\overline f_j(\sh{O}_X/\mathscr J))$, restreint à $U$",
    "Inline as printed. Apply before the next finding (misprint in the same formula).")
add(187, "same formula: 'Σ_{j=m+1}^{i-1}(O_X/J)'",
    "no f̄_j between the Σ and (O_X/J) (crop c187_alors.png)", "\\overline f_j present (silently corrected)",
    "misprint_in_print", None, "high",
    r"\sum_{j=m+1}^{i-1}\overline f_j(\sh{O}_X/\mathscr J))$, restreint",
    r"\sum_{j=m+1}^{i-1}(\sh{O}_X/\mathscr J))$, restreint",
    "The module is the one of the hypothesis two lines above, (O_X/J)/(Σ f̄_j(O_X/J)); the print omits f̄_j. "
    "'old' is the text after the previous (inline) edit: apply it second.",
    corrected=r"\sum_{j=m+1}^{i-1}\overline f_j(\sh{O}_X/\mathscr J))$, restreint")
add(187, "proof of (iii): 'O_U/((J|U)+Σ_{j=m+1}^{i-1} f_jO_U)=O_U/(Σ_{j=1}^{i-1} f_jO_U), et on voit donc'",
    "set in the line, at the start of a line (crop c187_OU.png)", "displayed, with \\big/ and \\Bigl( \\Bigr)",
    "formula", None, "high",
    r"isomorphe à<NL>\[<NL>  \sh{O}_U\big/\Bigl((\mathscr J|U)+\sum_{j=m+1}^{i-1}f_j\sh{O}_U\Bigr)<NL>  =\sh{O}_U\big/\Bigl(\sum_{j=1}^{i-1}f_j\sh{O}_U\Bigr),<NL>\]<NL>et on voit",
    r"isomorphe à $\sh{O}_U/((\mathscr J|U)+\sum_{j=m+1}^{i-1}f_j\sh{O}_U)=\sh{O}_U/(\sum_{j=1}^{i-1}f_j\sh{O}_U)$, et on voit",
    "Inline as printed.")
add(187, "proof of (iii): 'forment une base de cet O_X/K-Module (16.9.5)'",
    "O_X/K without parentheses (crop c187_base.png)", "$(\\sh{O}_X/\\mathscr K)$-Module", "formula", None, "high",
    r"cet $(\sh{O}_X/\mathscr K)$-Module (16.9.5)", r"cet $\sh{O}_X/\mathscr K$-Module (16.9.5)", "")
add(187, "proof of (iii): 'd'une base du O_X/K-Module g*(J/J²)'",
    "O_X/K without parentheses (crop c187_module.png)", "$(\\sh{O}_X/\\mathscr K)$-Module", "formula", None, "high",
    r"du $(\sh{O}_X/\mathscr K)$-Module", r"du $\sh{O}_X/\mathscr K$-Module", "")
add(187, "proof of (iii): 'forment une base de cet O_X-K-Module. Cela achève'",
    "no parentheses (crop c187_OXK_z.png)", "$(\\sh{O}_X/\\mathscr K)$-Module", "formula", None, "high",
    r"cet $(\sh{O}_X/\mathscr K)$-Module. Cela", r"cet $\sh{O}_X/\mathscr K$-Module. Cela",
    "Apply before the next finding (misprint in the same formula).")
add(187, "same place: 'cet O_X-K-Module'", "a hyphen between O_X and K where a slash is meant (crop c187_OXK_z.png)",
    "slash (silently corrected)", "misprint_in_print", None, "high",
    r"cet $\sh{O}_X/\mathscr K$-Module. Cela", r"cet $\sh{O}_X$-$\mathscr K$-Module. Cela",
    "(K/J)/(K/J)² is an O_X/K-Module, as in the two lines above. 'old' is the text after the previous edit: "
    "apply it second.",
    corrected=r"cet $\sh{O}_X/\mathscr K$-Module. Cela")
add(187, "last lines: 'Le fait que a) implique c) résulte de (iii). Prouvons que c) implique a).'",
    "labels wholly italic (crop c187_passons.png)", "$a)$, $c)$: italic letters, upright parentheses",
    "italics", None, "high",
    "Le fait que $a)$ implique $c)$ résulte de (iii). Prouvons que $c)$ implique $a)$.",
    r"Le fait que \emph{a)} implique \emph{c)} résulte de (iii). Prouvons que \emph{c)} implique \emph{a)}.",
    "Four labels in one edit (GLOBAL_ISSUES 88).")
add(187, "end of p. 187: page break 187/188 inside 'de sorte que O_{Y,g(z)}=A/𝔍, | O_{Z,z}=A/𝔎'",
    "p. 188 continues the sentence at the left margin (page_187_s4.png, page_188_s1.png)",
    "blank lines before and after \\oldpage[IV-4]{188}", "marker", None, "high",
    r"=A/\mathfrak J$,<NL><NL>", r"=A/\mathfrak J$,<NL>",
    "The marker is at the right place. Part 1 of 2 with the first p. 188 finding: both blank lines must go.")

# ---------------------------------------------------------------- p. 188
add(188, "top of p. 188: page break 187/188", "mid-sentence continuation", "blank line after \\oldpage[IV-4]{188}",
    "marker", None, "high", r"\oldpage[IV-4]{188}<NL><NL>", r"\oldpage[IV-4]{188}<NL>",
    "Part 2 of 2 with the last p. 187 finding; apply both.")

K = "Fraktur K (crops c188_K.png, c188_K_z.png: the glyph of the print's 𝔎 on p. 98, crop p98_frak_line.png in " \
    "crops_095_099, not the ℜ of p. 180)"
KN = "Wrong letter \\mathfrak R for the print's Fraktur K (GLOBAL_ISSUES 63); the ideals 𝔍 ⊂ 𝔎 correspond to the " \
     "Ideals 𝒥 ⊂ 𝒦 of p. 187. All 64 \\mathfrak R of the pp. 188-189 segments are this letter."
add(188, "l. 1: 'O_{Z,z}=A/𝔎 avec 𝔍⊂𝔎. Par hypothèse, 𝔍 et 𝔎 sont'", K + "; three times",
    "\\mathfrak R", "symbol", None, "high",
    r"$\sh{O}_{Z,z}=A/\mathfrak R$ avec $\mathfrak J\subset\mathfrak R$. Par hypothèse, $\mathfrak J$ et $\mathfrak R$ sont",
    r"$\sh{O}_{Z,z}=A/\mathfrak K$ avec $\mathfrak J\subset\mathfrak K$. Par hypothèse, $\mathfrak J$ et $\mathfrak K$ sont",
    KN)
add(188, "display: '0→𝔍/𝔍𝔎→𝔎/𝔎²→(𝔎/𝔍)/(𝔎/𝔍)²→0'", "Fraktur K five times", "\\mathfrak R", "symbol", None, "high",
    r"0\longrightarrow\mathfrak J/\mathfrak J\mathfrak R\longrightarrow\mathfrak R/\mathfrak R^2\longrightarrow(\mathfrak R/\mathfrak J)/(\mathfrak R/\mathfrak J)^2\longrightarrow0",
    r"0\longrightarrow\mathfrak J/\mathfrak J\mathfrak K\longrightarrow\mathfrak K/\mathfrak K^2\longrightarrow(\mathfrak K/\mathfrak J)/(\mathfrak K/\mathfrak J)^2\longrightarrow0",
    "Wrong letter (see the first p. 188 finding).")
add(188, "'de 𝔎 dont les images f'_j dans 𝔎/𝔎² forment une base de cet (A/𝔎)-module'", "Fraktur K four times",
    "\\mathfrak R", "symbol", None, "high",
    r"de $\mathfrak R$ dont les images $f'_j$ dans $\mathfrak R/\mathfrak R^2$ forment une base de cet $(A/\mathfrak R)$-module, et tels",
    r"de $\mathfrak K$ dont les images $f'_j$ dans $\mathfrak K/\mathfrak K^2$ forment une base de cet $(A/\mathfrak K)$-module, et tels",
    "Wrong letter.")
add(188, "'leurs images dans 𝔍/𝔍𝔎 forment une base de cet (A/𝔎)-module'", "Fraktur K twice", "\\mathfrak R",
    "symbol", None, "high",
    r"$\mathfrak J/\mathfrak J\mathfrak R$ forment une base de cet $(A/\mathfrak R)$-module. Les",
    r"$\mathfrak J/\mathfrak J\mathfrak K$ forment une base de cet $(A/\mathfrak K)$-module. Les", "Wrong letter.")
add(188, "'engendrent donc 𝔎'", "Fraktur K", "\\mathfrak R", "symbol", None, "high",
    r"engendrent donc $\mathfrak R$", r"engendrent donc $\mathfrak K$", "Wrong letter.")
add(188, "'comme 𝔎 est un idéal régulier, il résulte de (16.9.5)'", "Fraktur K", "\\mathfrak R", "symbol", None,
    "high", r"comme $\mathfrak R$ est un idéal régulier, il résulte", r"comme $\mathfrak K$ est un idéal régulier, il résulte",
    "Wrong letter.")
add(188, "'dans 𝔎/𝔍 forment donc une suite régulière'", "Fraktur K", "\\mathfrak R", "symbol", None, "high",
    r"dans $\mathfrak R/\mathfrak J$ forment donc", r"dans $\mathfrak K/\mathfrak J$ forment donc", "Wrong letter.")
add(188, "'ce qui achève de prouver que c) entraîne a) dans (iv)'", "labels wholly italic (crop c188_s2top.png)",
    "$c)$, $a)$", "italics", None, "high",
    "que $c)$ entraîne $a)$ dans (iv)", r"que \emph{c)} entraîne \emph{a)} dans (iv)", "GLOBAL_ISSUES 88.")
add(188, "'l'équivalence de a) et b) dans (iv)'", "labels wholly italic (crop c188_cor.png)", "$a)$, $b)$",
    "italics", None, "high", "de $a)$ et $b)$ dans (iv)", r"de \emph{a)} et \emph{b)} dans (iv)", "GLOBAL_ISSUES 88.")
add(188, "Corollaire (19.1.6): '𝔍, 𝔎 deux idéaux ... tels que 𝔍⊂𝔎, A'=A/𝔍, 𝔎'=𝔎/𝔍'", "Fraktur K four times",
    "\\mathfrak R", "symbol", None, "high",
    r"$\mathfrak J$, $\mathfrak R$ deux idéaux de $A$ contenus dans son idéal maximal $\mathfrak m$ et tels que $\mathfrak J\subset\mathfrak R$, $A'=A/\mathfrak J$, $\mathfrak R'=\mathfrak R/\mathfrak J$",
    r"$\mathfrak J$, $\mathfrak K$ deux idéaux de $A$ contenus dans son idéal maximal $\mathfrak m$ et tels que $\mathfrak J\subset\mathfrak K$, $A'=A/\mathfrak J$, $\mathfrak K'=\mathfrak K/\mathfrak J$",
    "Wrong letter. The heavier 'contenus' at the end of the first line is heavy impression (not reported).")
add(188, "Corollaire (19.1.6), label (i)", "label (i) upright (crop c188_cor2.png)", "\\item[(i)] italic",
    "convention", 6, "high", r"\item[(i)]", r"\item[\textup{(i)}]", "GLOBAL_ISSUES 16.")
add(188, "(19.1.6) (i): 'Si 𝔍 et 𝔎' sont des idéaux réguliers, il en est de même de 𝔎.'", "Fraktur K twice",
    "\\mathfrak R", "symbol", None, "high",
    r"$\mathfrak J$ et $\mathfrak R'$ sont des idéaux réguliers, il en est de même de $\mathfrak R$.",
    r"$\mathfrak J$ et $\mathfrak K'$ sont des idéaux réguliers, il en est de même de $\mathfrak K$.", "Wrong letter.")
add(188, "Corollaire (19.1.6), label (ii)", "label (ii) upright", "\\item[(ii)] italic",
    "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]", "GLOBAL_ISSUES 16.")
add(188, "(19.1.6) (ii): 'Si 𝔎 et 𝔎' sont des idéaux réguliers'", "Fraktur K twice", "\\mathfrak R", "symbol",
    None, "high", r"Si $\mathfrak R$ et $\mathfrak R'$ sont", r"Si $\mathfrak K$ et $\mathfrak K'$ sont", "Wrong letter.")
add(188, "Corollaire (19.1.6), label (iii)", "label (iii) upright", "\\item[(iii)] italic",
    "convention", 6, "high", r"\item[(iii)]", r"\item[\textup{(iii)}]", "GLOBAL_ISSUES 16.")
add(188, "(19.1.6) (iii): 'Pour que l'idéal 𝔎 soit régulier, il faut et il suffit que 𝔎' le soit.'",
    "Fraktur K twice", "\\mathfrak R", "symbol", None, "high",
    r"l'idéal $\mathfrak R$ soit régulier, il faut et il suffit que $\mathfrak R'$ le soit",
    r"l'idéal $\mathfrak K$ soit régulier, il faut et il suffit que $\mathfrak K'$ le soit", "Wrong letter.")
add(188, "proof of (ii): 'u : 𝔎/𝔎² → 𝔎'/𝔎'² = 𝔎/(𝔎²+𝔍)'", "Fraktur K six times (crop c188_u.png)", "\\mathfrak R",
    "symbol", None, "high",
    r"$u:\mathfrak R/\mathfrak R^2\to\mathfrak R'/\mathfrak R'^2=\mathfrak R/(\mathfrak R^2+\mathfrak J)$",
    r"$u:\mathfrak K/\mathfrak K^2\to\mathfrak K'/\mathfrak K'^2=\mathfrak K/(\mathfrak K^2+\mathfrak J)$", "Wrong letter.")
add(188, "'Comme par hypothèse 𝔎/𝔎² et 𝔎'/𝔎'² sont des (A/𝔎)-modules libres'", "Fraktur K five times",
    "\\mathfrak R", "symbol", None, "high",
    r"$\mathfrak R/\mathfrak R^2$ et $\mathfrak R'/\mathfrak R'^2$ sont des $(A/\mathfrak R)$-modules libres",
    r"$\mathfrak K/\mathfrak K^2$ et $\mathfrak K'/\mathfrak K'^2$ sont des $(A/\mathfrak K)$-modules libres", "Wrong letter.")
add(188, "'le noyau de u est un (A/𝔎)-module projectif'", "Fraktur K", "\\mathfrak R", "symbol", None, "high",
    r"un $(A/\mathfrak R)$-module \emph{projectif}", r"un $(A/\mathfrak K)$-module \emph{projectif}", "Wrong letter.")
add(188, "'puisque A/𝔎 est un anneau local noethérien'", "Fraktur K", "\\mathfrak R", "symbol", None, "high",
    r"puisque $A/\mathfrak R$ est un anneau", r"puisque $A/\mathfrak K$ est un anneau", "Wrong letter.")
add(188, "'(0_III, 10.1.3)'", "bold 0 with subscript III", "plain 0", "convention", 2, "high",
    r"($0_{\mathrm{III}}$, 10.1.3)", r"($\mathbf{0}_{\mathrm{III}}$, 10.1.3)", "")
add(188, "'une base de 𝔎/𝔎² dont les p premiers éléments forment une base de (𝔎²+𝔍)/𝔎²'", "Fraktur K four times",
    "\\mathfrak R", "symbol", None, "high",
    r"base de $\mathfrak R/\mathfrak R^2$ dont les $p$ premiers éléments forment une base de $(\mathfrak R^2+\mathfrak J)/\mathfrak R^2$",
    r"base de $\mathfrak K/\mathfrak K^2$ dont les $p$ premiers éléments forment une base de $(\mathfrak K^2+\mathfrak J)/\mathfrak K^2$",
    "Wrong letter.")
add(188, "'un système de générateurs (f_i)_{1≤i≤p+q} de 𝔎, formant'", "Fraktur K", "\\mathfrak R", "symbol", None,
    "high", r"de $\mathfrak R$, formant", r"de $\mathfrak K$, formant", "Wrong letter.")
add(188, "end of p. 188: page break 188/189 inside '... des g_j (2≤j≤q) | et de 𝔠 dans cet anneau quotient'",
    "p. 189 continues the sentence at the left margin (page_188_s4.png, page_189_s1.png)",
    "blank lines before and after \\oldpage[IV-4]{189}", "marker", None, "high",
    r"($2\leq j\leq q$)<NL><NL>", r"($2\leq j\leq q$)<NL>",
    "The marker is at the right place. Part 1 of 2 with the first p. 189 finding: both blank lines must go.")

# ---------------------------------------------------------------- p. 189
add(189, "top of p. 189: page break 188/189", "mid-sentence continuation 'et de 𝔠 dans cet anneau quotient'",
    "blank line after \\oldpage[IV-4]{189}", "marker", None, "high",
    r"\oldpage[IV-4]{189}<NL><NL>", r"\oldpage[IV-4]{189}<NL>", "Part 2 of 2 with the last p. 188 finding; apply both.")
add(189, "proof of (19.1.6) (iii), l. 1: 'si 𝔎 est régulier, il en est de même de 𝔎''", "Fraktur K twice",
    "\\mathfrak R", "symbol", None, "high",
    r"si $\mathfrak R$ est régulier, il en est de même de $\mathfrak R'$",
    r"si $\mathfrak K$ est régulier, il en est de même de $\mathfrak K'$",
    "Wrong letter \\mathfrak R for the print's Fraktur K (see p. 188).")
add(189, "'on sait (0, 17.1.9)'", "bare bold 0", "($0$, 17.1.9)", "convention", 2, "high",
    "($0$, 17.1.9)", r"(\textbf{0}, 17.1.9)", "")
add(189, "'f∉𝔪² (0, 17.1.8)'", "bare bold 0", "($0$, 17.1.8)", "convention", 2, "high",
    "($0$, 17.1.8)", r"(\textbf{0}, 17.1.8)", "")
add(189, "'Soient 𝔍_1, 𝔎_1 les images canoniques de 𝔍, 𝔎 dans A_1; on a 𝔍_1⊂𝔎_1'", "Fraktur K three times",
    "\\mathfrak R", "symbol", None, "high",
    r"Soient $\mathfrak J_1$, $\mathfrak R_1$ les images canoniques de $\mathfrak J$, $\mathfrak R$ dans $A_1$; on a $\mathfrak J_1\subset\mathfrak R_1$",
    r"Soient $\mathfrak J_1$, $\mathfrak K_1$ les images canoniques de $\mathfrak J$, $\mathfrak K$ dans $A_1$; on a $\mathfrak J_1\subset\mathfrak K_1$",
    "Wrong letter.")
add(189, "'Montrons que 𝔎_1 est un idéal régulier ... de générateurs de 𝔎'", "Fraktur K three times", "\\mathfrak R",
    "symbol", None, "high",
    r"Montrons que $\mathfrak R_1$ est un idéal régulier dans $A_1$; comme $\mathfrak R$ est un idéal régulier dans $A$, il suffit de montrer que $f$ fait partie d'un système régulier de générateurs de $\mathfrak R$",
    r"Montrons que $\mathfrak K_1$ est un idéal régulier dans $A_1$; comme $\mathfrak K$ est un idéal régulier dans $A$, il suffit de montrer que $f$ fait partie d'un système régulier de générateurs de $\mathfrak K$",
    "Wrong letter.")
add(189, "'dans 𝔎/(𝔎²+𝔪𝔎)=𝔎/𝔪𝔎 ... autrement dit que f∉𝔪𝔎'", "Fraktur K six times (crop c189_K.png)",
    "\\mathfrak R", "symbol", None, "high",
    r"dans $\mathfrak R/(\mathfrak R^2+\mathfrak m\mathfrak R)=\mathfrak R/\mathfrak m\mathfrak R$ fait partie d'une base de cet $(A/\mathfrak m)$-espace vectoriel, autrement dit que $f\notin\mathfrak m\mathfrak R$",
    r"dans $\mathfrak K/(\mathfrak K^2+\mathfrak m\mathfrak K)=\mathfrak K/\mathfrak m\mathfrak K$ fait partie d'une base de cet $(A/\mathfrak m)$-espace vectoriel, autrement dit que $f\notin\mathfrak m\mathfrak K$",
    "Wrong letter.")
add(189, "'(A_1/𝔍_1)-module libre de rang q—1'", "long dash (crop c189_q1.png)", "minus sign", "convention", 7,
    "high", "de rang $q-1$", r"de rang $q\setmin 1$", "GLOBAL_ISSUES 23.")
add(189, "'𝔎'_1=𝔎_1/𝔍_1 est un idéal régulier ... et comme 𝔎' s'identifie à 𝔎'_1 ..., 𝔎' est régulier'",
    "Fraktur K five times (crop c189_q1.png)", "\\mathfrak R", "symbol", None, "high",
    r"$\mathfrak R'_1=\mathfrak R_1/\mathfrak J_1$ est un idéal régulier de $A_1/\mathfrak J_1$, et comme $\mathfrak R'$ s'identifie à $\mathfrak R'_1$ dans l'isomorphisme canonique entre $A/\mathfrak J$ et $A_1/\mathfrak J_1$, $\mathfrak R'$ est régulier",
    r"$\mathfrak K'_1=\mathfrak K_1/\mathfrak J_1$ est un idéal régulier de $A_1/\mathfrak J_1$, et comme $\mathfrak K'$ s'identifie à $\mathfrak K'_1$ dans l'isomorphisme canonique entre $A/\mathfrak J$ et $A_1/\mathfrak J_1$, $\mathfrak K'$ est régulier",
    "Wrong letter.")
add(189, "Remarques (19.1.7) (ii): 'support fermé dans X (0_I, 5.2.2)'", "bold 0 with subscript I", "plain 0",
    "convention", 2, "high", r"($0_{\mathrm I}$, 5.2.2)", r"($\mathbf{0}_{\mathrm I}$, 5.2.2)", "")
add(189, "Remarques (19.1.7) (ii): 'comme dans (I, 4.1.3 et 4.2.1)'", "bold I followed by a comma", "plain I",
    "convention", 2, "high", "(I, 4.1.3 et 4.2.1)", r"(\textbf{I}, 4.1.3 et 4.2.1)",
    "Genuine EGA I references (subpreschemes, immersions), not EGA IV's own (1.4.1.3).")
add(189, "Remarques (19.1.7) (ii): 'les résultats de (19.1.4, (i) à (iv))'", "(19.1.4, (i) à (iv)) (crop c189_1914.png)",
    "(19.1.4, (i) à (iv)) (keeps the print)", "misprint_in_print", None, "medium", None, None,
    "(19.1.4) has no items; the results (i)-(iv) meant, with Y' defined in (ii), are those of Proposition (19.1.5). "
    "Not in the errata. The diplomatic TeX keeps the printed reading.",
    corrected="(19.1.5, (i) à (iv))")
add(189, "(19.1.8): 'K_0(f, M) (III, 1.1.3)'", "bold III", "plain III", "convention", 2, "high",
    "(III, 1.1.3)", r"(\textbf{III}, 1.1.3)", "")
add(189, "(19.1.8): '(cf. (III, 1.1.4))'", "bold III", "plain III", "convention", 2, "high",
    "(III, 1.1.4)", r"(\textbf{III}, 1.1.4)", "")
add(189, "end of p. 189 / heading 19.2", "printed p. 189 ends with '... à paraître prochainement.' (page_189_s4.png); "
    "the heading '19.2. Immersions transversalement régulières.' is the first line of p. 190 (page_190_s1.png)",
    "the \\subsection heading 19.2 stands before \\oldpage[IV-4]{190} (in the p. 189 segment)", "marker", None, "high",
    r"\end{env}<NL><NL>\subsection{Immersions transversalement",
    r"\end{env}<NL><NL>\oldpage[IV-4]{190}<NL><NL>\subsection{Immersions transversalement",
    "BOUNDARY FIX (page break 189/190), part 1 of 2: inserts the marker before the heading (new paragraph: blank lines "
    "stay). Part 2 (next finding, page 190) deletes the later marker; apply both, once (the 190-194 checker may "
    "report the same move).")
add(190, "start of page_190.tex: \\oldpage[IV-4]{190} after the 19.2 heading",
    "printed p. 190 begins with the heading 19.2 (page_190_s1.png)", "marker after the heading, before (19.2.1)",
    "marker", None, "high",
    r"\oldpage[IV-4]{190}<NL><NL>\begin{definition}[19.2.1]", r"\begin{definition}[19.2.1]",
    "BOUNDARY FIX, part 2 of 2 with the last p. 189 finding (outside pp. 185-189: the p. 190 segment). Apply after "
    "part 1, or together with it; skip if the 190-194 checker's equivalent edit is applied.")

json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(F), "findings written")
