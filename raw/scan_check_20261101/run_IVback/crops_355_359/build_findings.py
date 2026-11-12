import json
import sys

NL = "¶"  # pilcrow stands for a line break in the strings below


def F(page, where, scan, tex, kind, old, new, note="", conv=None, conf="high", corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


def heading(page, n):
    """Full stop and subscript weight of a (Err_IV, n) heading."""
    return [
        F(page, f"heading (Err_IV, {n})", f"'(Err_IV, {n}) Dans ...': no full stop after the closing parenthesis",
          f"\\paragraph{{(Err\\textsubscript{{IV}}, {n}).}}", "punctuation",
          f"{n}).}}", f"{n})}}",
          "Same pattern as the EGA II errata headings (GLOBAL_ISSUES 32); every (Err_IV, n) heading of pp. 355-358 lacks the "
          "full stop in the print. Independent of the subscript fix on the same heading (the two 'old' strings share only the "
          "unchanged number)."),
        F(page, f"heading (Err_IV, {n}): subscript IV", "bold 'Err' and bold number, light (medium-weight) subscript IV "
          "(4x crop crops_355_359/p355_err32_4x.png)",
          "\\textsubscript{IV} inside \\paragraph comes out bold", "font",
          f"Err\\textsubscript{{IV}}, {n}", f"Err\\textsubscript{{\\textmd{{IV}}}}, {n}",
          "As the light subscript of the EGA III errata headings (run_III2 p. 218). Applies to every (Err_IV, n) heading."),
    ]


def conv2(page, where, old, new, note=""):
    if "mathbf{0}" in new or "textbf{0}" in new:
        roman = "0"
    elif "textbf{IV}" in new:
        roman = "IV"
    else:
        roman = "I"
    return F(page, where, f"bold {roman} in the reference", f"plain {roman}", "convention", old, new, note, conv=2)


def conv7(page, where, old, new, note=""):
    return F(page, where, "long dash for set difference", "minus sign", "convention", old, new, note, conv=7)


def emph(page, where, scan, old, new, note="", conf="high"):
    return F(page, where, scan, "no emphasis (roman)", "italics", old, new, note, conf=conf)


out = []

# ---------------------------------------------------------------- page 355
p = 355
out += [
    emph(p, "proof of (10.4.12) (ii), l. 1: '(8.1.2, a))'", "label a) italic, letter and parenthesis (crop p355_812a.png)",
         "{8.1.2}}, a)), on peut", "{8.1.2}}, \\emph{a)}), on peut",
         "Condition label in roman text: the whole label italic."),
    emph(p, "proof of (10.4.12) (ii), l. 2: 'un schéma local'", "'local' italic",
         "un schéma local. Les", "un schéma \\emph{local}. Les"),
    emph(p, "proof of (10.4.12) (ii), l. 4-5: 'p est fini'", "'fini' italic",
         "$p$ est fini, $f'$", "$p$ est \\emph{fini}, $f'$"),
    emph(p, "proof of (10.4.12) (ii), l. 5: 'f' est un isomorphisme'", "'isomorphisme' italic",
         "est un isomorphisme et¶l'homomorphisme", "est un \\emph{isomorphisme} et¶l'homomorphisme"),
    emph(p, "proof of (10.4.12) (ii), l. 5: 'est injectif'", "'injectif' italic",
         "p_*(\\sh{O}_{X'})$ est injectif.", "p_*(\\sh{O}_{X'})$ est \\emph{injectif}."),
    F(p, "Corollaire (10.4.13): '(par exemple si k est de caractéristique 0)'",
      "the parenthesis is set in roman inside the italic statement", "italic (corollary environment)", "convention",
      "(par exemple si $k$ est de caractéristique 0), $f$ est un",
      "\\textup{(par exemple si $k$ est de caractéristique 0)}, $f$ est un", "", conv=6),
    F(p, "heading of (10.4.14)", "plural 'Remarques (10.4.14). —' (page_355_s2.png)", "\\begin{remark} prints 'Remarque'",
      "word", "\\begin{remark}[10.4.14]", "\\begin{remarks}[10.4.14]",
      "Part 1 of 2: apply together with the next entry (\\end{remark} -> \\end{remarks}), otherwise LaTeX error. The remarks "
      "environment is defined in EGA_IV4_FR.tex (GLOBAL_ISSUES 28)."),
    F(p, "end of Remarques (10.4.14)", "plural (see the previous entry)", "\\end{remark}", "word",
      "défini par $\\mathfrak J$.¶\\end{enumerate}¶\\end{remark}", "défini par $\\mathfrak J$.¶\\end{enumerate}¶\\end{remarks}",
      "Part 2 of 2 with the previous entry; apply both."),
    emph(p, "(10.4.14) (i): 'que X est réduit'", "'réduit' italic (remark body judged as roman)",
         "que $X$ est réduit pour la seconde", "que $X$ est \\emph{réduit} pour la seconde",
         "Remark body judged as roman (document-wide remark item)."),
    conv2(p, "(10.4.14) (i): '(0, 18.2.3)'", "($0$, 18.2.3)", "(\\textbf{0}, 18.2.3)",
          "Bare bold 0 in the print (no subscript)."),
    emph(p, "(10.4.14) (ii): 'un préschéma noethérien'", "'noethérien' italic",
         "un préschéma noethérien. Nous", "un préschéma \\emph{noethérien}. Nous"),
    emph(p, "(10.4.14) (ii): 'préschéma japonais'", "'japonais' italic",
         "préschéma¶japonais, le raisonnement", "préschéma¶\\emph{japonais}, le raisonnement"),
    emph(p, "(10.4.14) (ii): 'montre que f est fini'", "'fini' italic",
         "montre que $f$ est fini;", "montre que $f$ est \\emph{fini};"),
    F(p, "(10.4.14) (ii): 'k(x) est parfait'", "bold italic k", "plain k", "convention",
      "$k(x)$ est parfait", "$\\boldsymbol{k}(x)$ est parfait", "", conv=1),
    emph(p, "(10.4.14) (iii): 'radiciels non surjectifs'", "'non surjectifs' italic",
         "radiciels non¶surjectifs de", "radiciels \\emph{non¶surjectifs} de"),
    emph(p, "(10.4.14) (iii): 'intègres non noethériens'", "'non noethériens' italic",
         "intègres non noethériens :", "intègres \\emph{non noethériens} :"),
    F(p, "(10.4.14) (iii): 'A=k[(T_λ)]_{λ∈L}'",
      "the index λ∈L stands after the closing bracket: k[(T_λ)]_{λ∈L} (crop p355_kTL.png)",
      "k[(T_\\lambda)_{\\lambda\\in L}] (index inside the brackets)", "formula",
      "$A=k[(T_\\lambda)_{\\lambda\\in L}]$", "$A=k[(T_\\lambda)]_{\\lambda\\in L}$",
      "The print's notation, reproduced as printed."),
    conv7(p, "(10.4.14) (iii): 'où L—H est infini'", "où $L-H$ est infini", "où $L\\setmin H$ est infini",
          "Only the running-text L—H; in the subscript λ∈L−H the print has a short minus (crop p355_kTLH.png), which stays."),
    F(p, "(10.4.14) (iii): 'isomorphe à k[(T_λ)]_{λ∈L−H}'",
      "index after the closing bracket: k[(T_λ)]_{λ∈L−H} (crop p355_kTLH.png)",
      "k[(T_\\lambda)_{\\lambda\\in L-H}]", "formula",
      "$k[(T_\\lambda)_{\\lambda\\in L-H}]$", "$k[(T_\\lambda)]_{\\lambda\\in L-H}$", ""),
]
out += heading(p, 32)
out += [
    conv2(p, "(Err_IV, 32): 'Dans (IV, 11.3.14)'", "(IV, 11.3.14)", "(\\textbf{IV}, 11.3.14)"),
    emph(p, "(Err_IV, 32): 'avant « Soient »'", "'Soient' italic (crop p355_soient.png)",
         "avant « Soient »,", "avant « \\emph{Soient} »,"),
    emph(p, "(Err_IV, 32): added (ii) 'Inversement, soit f : X→Y un morphisme plat. Si X est unibranche (resp. ...'",
         "the added statement is italic, except '(resp.' and the closing parentheses, which are roman "
         "(crops p355_ii_stmt.png, p355_paren1.png, p355_paren2.png: both closing parentheses upright)",
         "\\textup{(ii)} Inversement, soit $f:X\\to Y$ un morphisme plat. Si $X$¶"
         "est unibranche (resp. géométriquement unibranche) en un point $x$, $Y$¶"
         "est unibranche (resp. géométriquement unibranche) au point $y=f(x)$.",
         "\\textup{(ii)} \\emph{Inversement, soit $f:X\\to Y$ un morphisme plat. Si $X$¶"
         "est unibranche} (resp. \\emph{géométriquement unibranche}) \\emph{en un point $x$, $Y$¶"
         "est unibranche} (resp. \\emph{géométriquement unibranche}) \\emph{au point $y=f(x)$.}",
         "The label (ii) stays upright."),
    emph(p, "(Err_IV, 32): added (ii) of the proof: 'A étant un anneau local réduit'", "'réduit' italic",
         "anneau local réduit, et", "anneau local \\emph{réduit}, et"),
    F(p, "page break 355/356 inside 'on en déduit qu'il en est de même | de Spec(A)'",
      "p. 355 ends 'qu'il en est de même', p. 356 begins 'de Spec(A); puisque A est réduit' in the same paragraph "
      "(page_355_s4.png, page_356_s1.png)",
      "blank line before \\oldpage[IV]{356}: a paragraph break the print lacks", "marker",
      "qu'il en est de¶même¶¶", "qu'il en est de¶même¶",
      "The marker itself is at the right place (page_356.tex begins 'de $\\operatorname{Spec}(A)$'); only the blank line at "
      "the end of page_355.tex goes (GLOBAL_ISSUES 20)."),
]

# ---------------------------------------------------------------- page 356
p = 356
out += [
    emph(p, "l. 1: 'il est donc intègre'", "'intègre' italic",
         "il est donc¶intègre. Soient", "il est donc¶\\emph{intègre}. Soient"),
    conv2(p, "l. 8: 'au-dessus de x (I, 3.4.7)'", "$x$ (I, 3.4.7)", "$x$ (\\textbf{I}, 3.4.7)"),
    F(p, "l. 8: '... ce n'est pas possible. Soit 𝔑 le nilradical'",
      "same paragraph: 'Soit 𝔑 le nilradical' follows on the same line", "blank line: new paragraph", "other",
      "ce n'est pas possible.¶¶Soit $\\mathfrak N$", "ce n'est pas possible.¶Soit $\\mathfrak N$",
      "Paragraph break the print does not have."),
    F(p, "l. 10: 'donc R/R𝔑=S^{-1}B/S^{-1}𝔑=S^{-1}(B/𝔑) est contenu'", "formula set in the running text",
      "displayed (\\[...\\])", "formula",
      "donc¶\\[¶ R/R\\mathfrak N=S^{-1}B/S^{-1}\\mathfrak N=S^{-1}(B/\\mathfrak N)¶\\]¶est contenu",
      "donc¶$R/R\\mathfrak N=S^{-1}B/S^{-1}\\mathfrak N=S^{-1}(B/\\mathfrak N)$¶est contenu", ""),
    F(p, "l. 11-12: 'il en est donc de même de B'_red=B'/(B'∩R𝔑) qui est entier'", "formula set in the running text",
      "displayed (\\[...\\])", "formula",
      "de même de¶\\[¶ B'_{\\mathrm{red}}=B'/(B'\\cap R\\mathfrak N)¶\\]¶qui est entier",
      "de même de¶$B'_{\\mathrm{red}}=B'/(B'\\cap R\\mathfrak N)$¶qui est entier", ""),
    emph(p, "l. 13: 'est un anneau local'", "'local' italic",
         "est un anneau local, donc", "est un anneau \\emph{local}, donc"),
    F(p, "l. 14: '... établit notre assertion. Si l'on suppose en outre'",
      "same paragraph: 'Si l'on suppose' follows on the same line", "blank line: new paragraph", "other",
      "notre assertion.¶¶Si l'on suppose", "notre assertion.¶Si l'on suppose",
      "Paragraph break the print does not have."),
    F(p, "l. 16: 'du corps résiduel k(x) de B'", "bold italic k", "plain k", "convention",
      "résiduel $k(x)$ de $B$", "résiduel $\\boldsymbol{k}(x)$ de $B$", "", conv=1),
    F(p, "l. 17: 'égal à k(x)⊗...'", "bold italic k in k(x)", "plain k", "convention",
      "égal à $k(x)\\otimes", "égal à $\\boldsymbol{k}(x)\\otimes", "Independent of the next entry (no overlap).", conv=1),
    F(p, "l. 17: subscript of ⊗_{k(y)}", "bold UPRIGHT k in the subscript; k' after it is a plain italic k "
      "(crop p356_kxky.png)", "plain k", "convention",
      "\\otimes_{k(y)}k'", "\\otimes_{\\mathbf{k}(y)}k'", "GLOBAL_ISSUES 48: in subscripts the residue-field k is bold upright.",
      conv=1),
    F(p, "l. 19: 'radicielle de k(y)'", "bold italic k", "plain k", "convention",
      "radicielle de $k(y)$, donc", "radicielle de $\\boldsymbol{k}(y)$, donc", "", conv=1),
]
out += heading(p, 33)
out += [
    conv2(p, "(Err_IV, 33): 'Dans (IV, 12.1.2)'", "{IV, 12.1.2}", "{\\textbf{IV}, 12.1.2}"),
    F(p, "(Err_IV, 33): '(l'ensemble des points fermés de Z étant identifié à C)'",
      "'identifié à C);' with no exponent 2 (crop p356_identC.png)", "$\\mathbb C^2$", "misprint_in_print",
      "$\\mathbb C^2$", "$\\mathbb C$",
      "The TeX silently corrects: the closed points of the plane Z = Spec(C[U, V]) form C^2. The fix restores the printed "
      "reading (only the exponent is removed).", conf="high", corrected="$\\mathbb C^2$"),
    F(p, "(Err_IV, 33): '... étant l'ensemble {a, b}. Considérons alors le schéma X'",
      "same paragraph: 'Considérons alors' follows on the same line", "blank line: new paragraph", "other",
      "l'ensemble $\\{a,b\\}$.¶¶Considérons alors", "l'ensemble $\\{a,b\\}$.¶Considérons alors",
      "Paragraph break the print does not have."),
    F(p, "(Err_IV, 33): '(loc. cit.)'", "both parentheses italic, like the words (crop p356_loccit.png)",
      "(\\emph{loc. cit.}): upright parentheses", "italics",
      "(\\emph{loc. cit.})", "\\emph{(loc. cit.)}", "Parentheses around a wholly italic phrase (GLOBAL_ISSUES 101)."),
    emph(p, "(Err_IV, 33): '(et même étale)'", "'étale' italic, parentheses and 'et même' roman",
         "(et même étale)", "(et même \\emph{étale})"),
    conv7(p, "(Err_IV, 33): 'l'ouvert Z_1—D'", "l'ouvert $Z_1-D$ de", "l'ouvert $Z_1\\setmin D$ de",
          "Crop p356_Z1D.png."),
]
out += heading(p, 34)
out += [
    conv2(p, "(Err_IV, 34): 'Dans le titre de (IV, 13.2)'", "(IV, 13.2),", "(\\textbf{IV}, 13.2),"),
    conv2(p, "(Err_IV, 34): 'dans (IV, 13.2.2)'", "(IV, 13.2.2),", "(\\textbf{IV}, 13.2.2),"),
]

# ---------------------------------------------------------------- page 357
p = 357
out += [
    F(p, "l. 1-2: '... sont équidimensionnelles (0_IV, 14.1.3), on dit que f est équidimensionnel.'",
      "italic up to 'équidimensionnelles'; '(0_IV, 14.1.3),' roman; 'on dit que f est' italic; the defined word "
      "'équidimensionnel.' roman (crop p357_l1_3.png)",
      "one \\emph covers the whole addition", "convention",
      "$f^{-1}(f(x))$ de $f$ sont équidimensionnelles (", "$f^{-1}(f(x))$ de $f$ sont équidimensionnelles} (",
      "Part 1 of 2 (closes the \\emph before the reference); apply with the next entry. Independent of the convention-2 "
      "entry for (0_IV, 14.1.3) (the 'old' strings share only unchanged characters).", conv=6),
    F(p, "l. 2: 'on dit que f est équidimensionnel.'", "'on dit que f est' italic, 'équidimensionnel.' roman",
      "inside the \\emph", "convention",
      "14.1.3), on dit que $f$ est équidimensionnel.} Ligne 6",
      "14.1.3), \\emph{on dit que $f$ est} équidimensionnel. Ligne 6",
      "Part 2 of 2 with the previous entry; apply both (the previous one closes the \\emph whose closing brace this one "
      "removes).", conv=6),
    conv2(p, "l. 2: '(0_IV, 14.1.3)'", "($0_{\\mathrm{IV}}$,¶14.1.3)", "($\\mathbf{0}_{\\mathrm{IV}}$,¶14.1.3)",
          "Bold 0 with a light subscript IV in the print."),
    emph(p, "l. 3: 'remplacer « équidimensionnelles » par « localement équidimensionnelles »'",
         "both quoted phrases italic (crop p357_l1_3.png)",
         "remplacer « équidimensionnelles » par « localement¶équidimensionnelles »",
         "remplacer « \\emph{équidimensionnelles} » par « \\emph{localement¶équidimensionnelles} »"),
]
out += heading(p, 35)
out += [
    conv2(p, "(Err_IV, 35): 'Dans le titre de (IV, 13.3)'", "(IV, 13.3),", "(\\textbf{IV}, 13.3),"),
    F(p, "(Err_IV, 35): 'ligne 4 du bas de la p. 94'", "'p. 94' (crop p357_p94.png)", "p.~94 (as printed)",
      "misprint_in_print", None, None,
      "The TeX keeps the printed reading. The title of (13.3) is near the foot of EGA IV p. 194 (ega4-13-fr.tex: "
      "\\subsection 13.3 between \\oldpage[IV-3]{194} and {195}; Err_IV 34 has the 13.2 changes up to p. 194).",
      corrected="p.~194"),
    conv2(p, "(Err_IV, 35): 'Dans (IV, 13.3.2)'", "(IV, 13.3.2),", "(\\textbf{IV}, 13.3.2),"),
    F(p, "(Err_IV, 35): 'sont équidimensionnelles (0_IV, 14.1.3), on dit que f est équidimensionnel.'",
      "italic up to 'équidimensionnelles'; '(0_IV, 14.1.3),' roman; 'on dit que f est' italic; 'équidimensionnel.' roman",
      "one \\emph covers the whole addition", "convention",
      "de¶$f$ sont équidimensionnelles (", "de¶$f$ sont équidimensionnelles} (",
      "Part 1 of 2; apply with the next entry. Independent of the convention-2 entry for this (0_IV, 14.1.3).", conv=6),
    F(p, "(Err_IV, 35): 'on dit que f est équidimensionnel.'", "'on dit que f est' italic, 'équidimensionnel.' roman",
      "inside the \\emph", "convention",
      "14.1.3), on dit que¶$f$ est équidimensionnel.} Dans",
      "14.1.3), \\emph{on dit que¶$f$ est} équidimensionnel. Dans",
      "Part 2 of 2 with the previous entry; apply both.", conv=6),
    conv2(p, "(Err_IV, 35): '(0_IV, 14.1.3)'", "($0_{\\mathrm{IV}}$, 14.1.3)", "($\\mathbf{0}_{\\mathrm{IV}}$, 14.1.3)",
          "Bold 0 with a light subscript IV."),
    conv2(p, "(Err_IV, 35): 'Dans (IV, 13.3.7)'", "(IV, 13.3.7),", "(\\textbf{IV}, 13.3.7),"),
    emph(p, "(Err_IV, 35), (13.3.7): '« équidimensionnel » par « localement équidimensionnel »'",
         "both quoted phrases italic (only here and in Err_IV 36, 41; the other quotations of Err_IV 34-35 are roman)",
         "p.~198,¶remplacer « équidimensionnel » par « localement équidimensionnel ».",
         "p.~198,¶remplacer « \\emph{équidimensionnel} » par « \\emph{localement équidimensionnel} »."),
    conv2(p, "(Err_IV, 35): 'Dans (IV, 13.3.9)'", "{IV, 13.3.9}", "{\\textbf{IV}, 13.3.9}"),
]
out += heading(p, 36)
out += [
    emph(p, "(Err_IV, 36): '« équidimensionnel » par « localement équidimensionnel »'", "both quoted phrases italic",
         "p.~199, remplacer¶« équidimensionnel » par « localement équidimensionnel ».",
         "p.~199, remplacer¶« \\emph{équidimensionnel} » par « \\emph{localement équidimensionnel} »."),
]
out += heading(p, 37)
out += [
    conv2(p, "(Err_IV, 37): 'Dans (IV, 14.4.1), ligne 5'", "(IV, 14.4.1), ligne 5", "(\\textbf{IV}, 14.4.1), ligne 5"),
    emph(p, "(Err_IV, 37): '« localement de type fini » par « localement de présentation finie »'",
         "both quoted phrases italic",
         "« localement¶de type fini » par « localement de présentation finie ». L'énoncé",
         "« \\emph{localement¶de type fini} » par « \\emph{localement de présentation finie} ». L'énoncé"),
    conv2(p, "(Err_IV, 37): 'L'énoncé actuel de (IV, 14.4.1)'", "{IV, 14.4.1}}) est", "{\\textbf{IV}, 14.4.1}}) est"),
    emph(p, "(Err_IV, 37): 'est inexact'", "'inexact' italic", "inexact,¶même lorsque", "\\emph{inexact},¶même lorsque"),
    emph(p, "(Err_IV, 37): 'est une immersion fermée'", "'immersion fermée' italic (the later 'l'immersion fermée {y}→Y' "
         "is roman)", "est une immersion fermée,", "est une \\emph{immersion fermée},"),
    emph(p, "(Err_IV, 37): 'tout idéal premier 𝔭'", "'premier' italic", "idéal premier¶$\\mathfrak p$",
         "idéal \\emph{premier}¶$\\mathfrak p$"),
    emph(p, "(Err_IV, 37): 'les conditions b) et b')'", "labels b) and b') italic, letters and parentheses "
         "(crop p357_bb.png)", "conditions b) et b') de", "conditions \\emph{b)} et \\emph{b')} de",
         "Condition labels in roman text."),
    conv2(p, "(Err_IV, 37): last line, 'de (IV, 14.4.1).'", "{IV, 14.4.1}}).", "{\\textbf{IV}, 14.4.1}})."),
]
out += heading(p, 38)
out += [
    conv2(p, "(Err_IV, 38): 'Dans (IV, 14.4.1.3)'", "(IV, 14.4.1.3)", "(\\textbf{IV}, 14.4.1.3)"),
    emph(p, "(Err_IV, 38): both quoted phrases", "« localement quasi-fini et dominant » and « localement quasi-fini, "
         "localement de présentation finie et dominant » italic",
         "« localement¶quasi-fini et dominant » par « localement quasi-fini, localement de¶présentation finie et dominant »",
         "« \\emph{localement¶quasi-fini et dominant} » par « \\emph{localement quasi-fini, localement de¶présentation finie "
         "et dominant} »"),
]
out += heading(p, 39)
out += [
    conv2(p, "(Err_IV, 39): 'Dans (IV, 14.4.2)'", "(IV, 14.4.2)", "(\\textbf{IV}, 14.4.2)"),
    emph(p, "(Err_IV, 39): both quoted phrases", "« localement de type fini », « localement de présentation finie » italic",
         "p.~211, remplacer « localement¶de type fini » par « localement de présentation finie ».",
         "p.~211, remplacer « \\emph{localement¶de type fini} » par « \\emph{localement de présentation finie} »."),
]
out += heading(p, 40)
out += [
    conv2(p, "(Err_IV, 40): 'Dans (IV, 14.4.3)'", "(IV, 14.4.3)", "(\\textbf{IV}, 14.4.3)"),
    emph(p, "(Err_IV, 40): both quoted phrases", "« localement de type fini », « localement de présentation finie » italic",
         "« localement de¶type fini » par « localement de présentation finie ».",
         "« \\emph{localement de¶type fini} » par « \\emph{localement de présentation finie} »."),
]
out += heading(p, 41)
out += [
    conv2(p, "(Err_IV, 41): 'Dans (IV, 14.4.4)'", "{IV, 14.4.4}", "{\\textbf{IV}, 14.4.4}"),
    emph(p, "(Err_IV, 41): '« localement de type fini » par « localement de présentation finie »'",
         "both quoted phrases italic",
         "remplacer « localement de type fini » par¶« localement de présentation finie ». Lignes 10",
         "remplacer « \\emph{localement de type fini} » par¶« \\emph{localement de présentation finie} ». Lignes 10"),
    emph(p, "(Err_IV, 41): '« équidimensionnel » par « localement équidimensionnel »'", "both quoted phrases italic",
         "du bas, remplacer¶« équidimensionnel » par « localement équidimensionnel ».",
         "du bas, remplacer¶« \\emph{équidimensionnel} » par « \\emph{localement équidimensionnel} »."),
]
out += heading(p, 42)
out += [conv2(p, "(Err_IV, 42): 'Dans (IV, 14.4.8)'", "(IV, 14.4.8)", "(\\textbf{IV}, 14.4.8)")]
out += heading(p, 43)
out += [conv2(p, "(Err_IV, 43): 'Dans (IV, 14.4.10)'", "(IV, 14.4.10)", "(\\textbf{IV}, 14.4.10)")]
out += heading(p, 44)
out += [
    conv2(p, "(Err_IV, 44): 'Dans (IV, 15.5.6.1)'", "(IV, 15.5.6.1)", "(\\textbf{IV}, 15.5.6.1)"),
    emph(p, "(Err_IV, 44), added text: 'n'admet qu'un seul point générique'", "'un seul' italic",
         "n'admet qu'un seul point", "n'admet qu'\\emph{un seul} point"),
    F(p, "page break 357/358 inside 'on considère l'espace Y=X/R, | quotient de X par la relation'",
      "p. 357 ends 'l'espace Y=X/R,', p. 358 begins 'quotient de X par la relation d'équivalence' in the same sentence "
      "(page_357_s4.png, page_358_s1.png)",
      "blank line before \\oldpage[IV]{358}: a paragraph break inside the quote", "marker",
      "l'espace $Y=X/R$,¶¶", "l'espace $Y=X/R$,¶",
      "The marker itself is at the right place; only the blank line at the end of page_357.tex goes (GLOBAL_ISSUES 20)."),
]

# ---------------------------------------------------------------- page 358
p = 358
out += [
    emph(p, "(Err_IV, 44) addition, l. 2: 'est saturé pour R'", "'saturé' italic", "est saturé pour", "est \\emph{saturé} pour"),
    emph(p, "(Err_IV, 44) addition, l. 2-3: 'l'image réciproque'", "'image réciproque' italic (l' roman)",
         "est l'image réciproque de celle", "est l'\\emph{image réciproque} de celle"),
    conv7(p, "(Err_IV, 44) addition, l. 6: 'X—Z est connexe'", "dire que $X-Z$ est", "dire que $X\\setmin Z$ est"),
    conv7(p, "(Err_IV, 44) addition, l. 6: 'Y—S est connexe'", "que $Y-S$ est", "que $Y\\setmin S$ est"),
    conv7(p, "(Err_IV, 44) addition, l. 7: 'T_x—{x}'", "$T_x-\\{x\\}$", "$T_x\\setmin\\{x\\}$"),
    conv7(p, "(Err_IV, 44) addition, l. 8: 'π(T_x)—{π(x)}'", "$\\pi(T_x)-\\{\\pi(x)\\}$", "$\\pi(T_x)\\setmin\\{\\pi(x)\\}$"),
]
out += heading(p, 45)
out += [
    conv2(p, "(Err_IV, 45): 'Dans (IV, 15.6.1)'", "(IV, 15.6.1)", "(\\textbf{IV}, 15.6.1)"),
    emph(p, "(Err_IV, 45): 'supprimer « localement noethérien »'", "quoted phrase italic",
         "supprimer « localement¶noethérien »", "supprimer « \\emph{localement¶noethérien} »"),
]
out += heading(p, 46)
out += [
    conv2(p, "(Err_IV, 46): 'Dans (IV, 15.6.3)'", "(IV, 15.6.3)", "(\\textbf{IV}, 15.6.3)"),
    emph(p, "(Err_IV, 46): 'au lieu de « supposons que pour tout y∈Y »'", "quoted phrase italic",
         "au lieu de « supposons que¶pour tout $y\\in Y$ »", "au lieu de « \\emph{supposons que¶pour tout $y\\in Y$} »"),
    emph(p, "(Err_IV, 46): 'lire : « supposons que f soit localement de présentation finie et que pour tout y∈Y »'",
         "quoted phrase italic",
         "lire : « supposons que $f$ soit localement de¶présentation finie et que pour tout $y\\in Y$ »",
         "lire : « \\emph{supposons que $f$ soit localement de¶présentation finie et que pour tout $y\\in Y$} »"),
]
out += heading(p, 47)
out += [
    conv2(p, "(Err_IV, 47): 'Dans (IV, 15.6.7)'", "(IV, 15.6.7)", "(\\textbf{IV}, 15.6.7)"),
    emph(p, "(Err_IV, 47): 'après « noethérien »'", "'noethérien' italic", "après « noethérien »",
         "après « \\emph{noethérien} »"),
    emph(p, "(Err_IV, 47): '« ou si la condition β) de (15.6.6, (iii)) est vérifiée »'",
         "'ou si la condition', 'de', 'est vérifiée' italic; β) and the reference (15.6.6, (iii)) upright "
         "(crop p358_beta.png)",
         "« ou si la condition $\\beta$) de¶({\\hyperref[canon-index.ega4.c04.prop.15-6-6]{15.6.6}}, (iii)) est vérifiée »",
         "« \\emph{ou si la condition} $\\beta$) \\emph{de}¶({\\hyperref[canon-index.ega4.c04.prop.15-6-6]{15.6.6}}, (iii)) "
         "\\emph{est vérifiée} »",
         "The reference stays outside the \\emph (upright, as printed)."),
    emph(p, "(Err_IV, 47) added text: 'le fait que a) entraîne b')'", "labels a), b') italic, letters and parentheses "
         "(crop p358_ab1.png)", "fait que a) entraîne b') résulte", "fait que \\emph{a)} entraîne \\emph{b')} résulte",
         "Condition labels in roman text."),
    emph(p, "(Err_IV, 47) added text: 'le fait que b') entraîne a)'", "labels b'), a) italic (crop p358_ab2.png)",
         "le fait que b')¶entraîne a) résulte", "le fait que \\emph{b')}¶entraîne \\emph{a)} résulte",
         "Condition labels in roman text."),
]
out += heading(p, 48)
out += [
    conv2(p, "(Err_IV, 48): 'Dans (IV, 20.1.5)'", "(IV, 20.1.5), ligne 13", "(\\textbf{IV}, 20.1.5), ligne 13"),
    conv2(p, "(Err_IV, 48): '(IV, 20.1.6)'", "(IV, 20.1.6)", "(\\textbf{IV}, 20.1.6)"),
    conv2(p, "(Err_IV, 48): '(IV, 20.1.7)'", "(IV, 20.1.7)", "(\\textbf{IV}, 20.1.7)"),
]
out += heading(p, 49)
out += [
    conv2(p, "(Err_IV, 49): 'Dans (IV, 20.2.13)'", "(IV, 20.2.13), ajouter", "(\\textbf{IV}, 20.2.13), ajouter"),
    conv2(p, "(Err_IV, 49): 'définie dans (IV, 20.1.5)'", "{IV, 20.1.5}}) coïncide", "{\\textbf{IV}, 20.1.5}}) coïncide"),
    conv2(p, "(Err_IV, 49): 'celle de (I, 7.4.1)'", "celle de (I, 7.4.1)", "celle de (\\textbf{I}, 7.4.1)"),
]
out += heading(p, 50)
out += [conv2(p, "(Err_IV, 50): 'Dans (IV, 20.2.14)'", "(IV, 20.2.14)", "(\\textbf{IV}, 20.2.14)")]
out += heading(p, 51)
out += [conv2(p, "(Err_IV, 51): 'Dans (IV, 20.6.2)'", "(IV, 20.6.2)", "(\\textbf{IV}, 20.6.2)")]
out += heading(p, 52)
out += [conv2(p, "(Err_IV, 52): 'Dans (IV, 20.6.4)'", "(IV, 20.6.4)", "(\\textbf{IV}, 20.6.4)")]
out += heading(p, 53)
out += [
    conv2(p, "(Err_IV, 53): 'Dans (IV, 21.4)'", "(IV, 21.4), après", "(\\textbf{IV}, 21.4), après"),
    F(p, "Proposition (21.4.9), l. 2: 'on suppose en outre, soit que f est quasi-compact'",
      "'soit' roman inside the italic statement (crop p358_soit.png)", "italic (proposition environment)", "convention",
      "en outre, soit que", "en outre, \\textup{soit} que", "", conv=6),
    F(p, "Proposition (21.4.9), l. 2: 'soit que f est ouvert'", "'soit' roman inside the italic statement",
      "italic (proposition environment)", "convention",
      "quasi-compact, soit que $f$ est ouvert", "quasi-compact, \\textup{soit} que $f$ est ouvert", "", conv=6),
    F(p, "Proposition (21.4.9), l. 4-5: 'en posant Y_1=Spec(O_{Y,y}), X_1=X×_Y Y_1, f_1=f_(Y_1) : X_1→Y_1, l'image'",
      "the three formulas run in the line, separated by commas", "displayed with \\qquad", "formula",
      "en posant¶\\[¶ Y_1=\\operatorname{Spec}(\\sh{O}_{Y,y}),\\qquad¶ X_1=X\\times_YY_1,\\qquad¶ f_1=f_{(Y_1)}:X_1\\to Y_1,¶\\]¶"
      "l'image réciproque",
      "en posant¶$Y_1=\\operatorname{Spec}(\\sh{O}_{Y,y})$,¶$X_1=X\\times_YY_1$,¶$f_1=f_{(Y_1)}:X_1\\to Y_1$,¶"
      "l'image réciproque", ""),
]

# ---------------------------------------------------------------- page 359
p = 359
out += [
    F(p, "proof of (21.4.9), l. 3-4: 'l'application D_U ⇝ f_U^*(D_U) de Div(U)'", "formula in the running text",
      "displayed (\\[...\\])", "formula",
      "l'application¶\\[¶ D_U\\longmapsto f_U^*(D_U)¶\\]¶de", "l'application¶$D_U\\longmapsto f_U^*(D_U)$¶de",
      "Apply BEFORE the arrow fix (next entry), whose 'old' lies inside this one's."),
    F(p, "proof of (21.4.9), l. 4: arrow of D_U ⇝ f_U^*(D_U)", "wavy arrow (crop p359_wavy.png)", "\\longmapsto", "symbol",
      "D_U\\longmapsto f_U^*(D_U)", "D_U\\leadsto f_U^*(D_U)", "Apply AFTER the previous entry (display to inline)."),
    F(p, "proof of (21.4.9), l. 5: 'et si D'|f^{-1}(U_1)=f_{U_1}^*(D_1) et D'|f^{-1}(U_2)=f_{U_2}^*(D_2), on a'",
      "both formulas in the running text, joined by 'et'", "displayed with \\qquad and a comma; the 'et' is lost", "formula",
      "et si¶\\[¶ D'|f^{-1}(U_1)=f_{U_1}^*(D_1),\\qquad¶ D'|f^{-1}(U_2)=f_{U_2}^*(D_2),¶\\]¶on a",
      "et si¶$D'|f^{-1}(U_1)=f_{U_1}^*(D_1)$ et¶$D'|f^{-1}(U_2)=f_{U_2}^*(D_2)$,¶on a", ""),
    emph(p, "proof of (21.4.9), l. 6: 'un plus grand ouvert'", "'plus grand' italic", "un plus grand ouvert",
         "un \\emph{plus grand} ouvert"),
    F(p, "proof of (21.4.9), l. 7: 'tel que D'|f^{-1}(U)=f_U^*(D_U), où D_U∈Div(U); il s'agit'",
      "formulas in the running text, joined by 'où'", "displayed with \\qquad; the 'où' is lost", "formula",
      "tel que¶\\[¶ D'|f^{-1}(U)=f_U^*(D_U),¶ \\qquad D_U\\in\\operatorname{Div}(U);¶\\]¶il s'agit",
      "tel que¶$D'|f^{-1}(U)=f_U^*(D_U)$, où $D_U\\in\\operatorname{Div}(U)$;¶il s'agit", ""),
    conv7(p, "proof of (21.4.9), l. 8: 'point maximal de Y—U; on va montrer'", "point maximal de $Y-U$; on va",
          "point maximal de $Y\\setmin U$; on va"),
    F(p, "proof of (21.4.9), heading I): 'I) Cas où f est quasi-compact.'",
      "label I) upright, the title 'Cas où f est quasi-compact.' italic", "\\textup over label and title: all roman",
      "italics",
      "\\textup{I) Cas où $f$ est quasi-compact.}", "\\textup{I)} \\emph{Cas où $f$ est quasi-compact.}", ""),
    emph(p, "I), l. 2: '(8.1.2, a))'", "label a) italic, letter and parenthesis",
         "{8.1.2}},¶a)), on est ramené", "{8.1.2}},¶\\emph{a)}), on est ramené", "Condition label in roman text."),
    conv7(p, "I), l. 5: 'point maximal de Y—U, l'ouvert'", "de $Y-U$, l'ouvert", "de $Y\\setmin U$, l'ouvert"),
    conv7(p, "I), l. 6: 'Y_1—{y}'", "$Y_1-\\{y\\}$", "$Y_1\\setmin\\{y\\}$"),
    conv7(p, "I), l. 6: 'U=Y—{y}. Par hypothèse'", "$U=Y-\\{y\\}$. Par", "$U=Y\\setmin\\{y\\}$. Par"),
    F(p, "I), l. 10: 'où ℒ'_U=f_U^*(ℒ_U) et s'=s∘f_U. Notons'", "formulas in the running text, joined by 'et'",
      "displayed with \\qquad; the 'et' is lost", "formula",
      "où¶\\[¶ \\sh{L}'_U=f_U^*(\\sh{L}_U),\\qquad s'=s\\circ f_U.¶\\]¶Notons",
      "où¶$\\sh{L}'_U=f_U^*(\\sh{L}_U)$ et $s'=s\\circ f_U$.¶Notons", ""),
    F(p, "I), l. 11: 'et posons ℒ=i_*(ℒ_U) et ℒ'=j_*(ℒ'_U). Comme f'", "formulas in the running text, joined by 'et'",
      "displayed with \\qquad; the 'et' is lost", "formula",
      "posons¶\\[¶ \\sh{L}=i_*(\\sh{L}_U),\\qquad¶ \\sh{L}'=j_*(\\sh{L}'_U).¶\\]¶Comme",
      "posons¶$\\sh{L}=i_*(\\sh{L}_U)$ et¶$\\sh{L}'=j_*(\\sh{L}'_U)$.¶Comme", ""),
    emph(p, "I), l. 13: 'pour tout x∈f^{-1}(y) (6.3.1)'", "'tout' italic (the later 'pour tout x∈f^{-1}(y), on a "
         "D'=f^*(D)' is roman)", "pour tout $x\\in f^{-1}(y)$¶{\\hyperref", "pour \\emph{tout} $x\\in f^{-1}(y)$¶{\\hyperref"),
    F(p, "I), l. 13-14: '... (6.3.1). Or, D' est classe d'équivalence'",
      "'Or,' begins the next line flush left: no new paragraph (crop p359_Or.png)", "blank line: new paragraph", "other",
      "(6.3.1)}}.¶¶Or, $D'$", "(6.3.1)}}.¶Or, $D'$", "Paragraph break the print does not have."),
    F(p, "I), l. 14: 'ℒ'' est un O_{X'}-Module inversible'", "subscript X' with a prime (crop p359_Xp1.png)",
      "$\\sh{O}_X$", "misprint_in_print",
      "$\\sh{L}''$ est un $\\sh{O}_X$-Module", "$\\sh{L}''$ est un $\\sh{O}_{X'}$-Module",
      "The TeX silently corrects. In this proof f : X→Y and D' is a divisor on X; there is no X'. Three such primes on "
      "this page (also the next two entries).", corrected="$\\sh{O}_X$"),
    F(p, "I), l. 15: 'au-dessus de X''", "X' with a prime (crop p359_Xp2.png)", "$X$", "misprint_in_print",
      "au-dessus de $X$; $\\sh{L}'_U$", "au-dessus de $X'$; $\\sh{L}'_U$", "The TeX silently corrects.",
      corrected="$X$"),
    F(p, "I), l. 17: 'ℒ' est un O_{X'}-Module inversible isomorphe à ℒ'''", "subscript X' with a prime "
      "(crop p359_Xp3.png)", "$\\sh{O}_X$", "misprint_in_print",
      "$\\sh{O}_X$-Module inversible isomorphe", "$\\sh{O}_{X'}$-Module inversible isomorphe", "The TeX silently corrects.",
      corrected="$\\sh{O}_X$"),
    conv7(p, "I), l. 21: 'U=Y—{y} est schématiquement dense'", "$U=Y-\\{y\\}$ est", "$U=Y\\setmin\\{y\\}$ est"),
    conv7(p, "I), l. 25: 'f^{-1}(U)=X—f^{-1}(y)'", "$f^{-1}(U)=X-f^{-1}(y)$", "$f^{-1}(U)=X\\setmin f^{-1}(y)$"),
    F(p, "proof of (21.4.9), heading II): 'II) Cas où f est ouvert.'",
      "label II) upright, the title 'Cas où f est ouvert.' italic", "\\textup over label and title: all roman", "italics",
      "\\textup{II) Cas où $f$ est ouvert.}", "\\textup{II)} \\emph{Cas où $f$ est ouvert.}", ""),
    emph(p, "II), l. 4: 'il existe un ouvert quasi-compact T⊂X'", "'quasi-compact' italic",
         "un ouvert quasi-compact $T\\subset X$", "un ouvert \\emph{quasi-compact} $T\\subset X$"),
    F(p, "II), l. 5: 'le morphisme f|T est quasi-compact (1.1.1)'", "(1.1.1): EGA IV's own reference, no 'I,' "
      "(old-style figures, crop p359_111.png)", "(I, 1.1.1)", "extra",
      "quasi-compact (I, 1.1.1);", "quasi-compact (1.1.1);",
      "The item-78 misreading (GLOBAL_ISSUES 78/103)."),
]

json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out))
