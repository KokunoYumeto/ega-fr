# Builds findings_211_215.json; "⏎" in old/new stands for a newline (LF).
import json, sys, os

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, "findings_211_215.json")
NL = "⏎"

def page_text(n):
    with open(os.path.join(RUN, "page_%03d.tex" % n), encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n")

F = []
def add(page, where, scan, tex, kind, old=None, new=None, conv=None, conf="high",
        corrected=None, note="", nofix=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if nofix else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

MARK = r"\oldpage[0\textsubscript{IV-1}]"

# ---------------------------------------------------------------- page 211
add(211, "top of the page: 'par (16.5.11). Or, comme A_𝔭 est régulier' continues the sentence of p. 210",
    "no paragraph break: p. 211 begins at the left margin, mid-sentence ('r-s = … = dim(A_𝔭) par (16.5.11)')",
    "blank line after the marker (and another before it, after the closing \\] of the p. 210 display)",
    "other", MARK + "{211}" + NL + NL + "par (16.5.11)", MARK + "{211}" + NL + "par (16.5.11)",
    note="Spurious paragraph break. Apply together with the removal of the blank line BEFORE the marker, which lies in the p. 210 segment (ega0-22-fr.tex: '=\\dim(A_{\\mathfrak p})\\n\\]\\n\\n\\oldpage[0\\textsubscript{IV-1}]{211}' -> '…\\]\\n\\oldpage…'); both blank lines must go.")
add(211, "Théorème (22.7.3), after condition 3°: 'Soient 𝔮 un idéal de A, B=A/𝔮, …'",
    "new indented paragraph after the list (indented like the items 1°-3°)",
    "'Soient' follows \\end{enumerate} without a blank line (unindented continuation)",
    "other", r"\end{enumerate}" + NL + r"Soient $\mathfrak q$", r"\end{enumerate}" + NL + NL + r"Soient $\mathfrak q$",
    conf="medium", note="Same form as earlier page fixes (pp. 18, 48, 75).")
add(211, "Théorème (22.7.3), label of condition a)", "a) upright (crop p211_labels)",
    "\\item[a)] italic in the theorem environment", "convention",
    r"\item[a)]", r"\item[\textup{a)}]", conv=6)
add(211, "Théorème (22.7.3), label of condition b)", "b) upright (crop p211_labels)",
    "\\item[b)] italic in the theorem environment", "convention",
    r"\item[b)]", r"\item[\textup{b)}]", conv=6)
add(211, "Théorème (22.7.3) b): 'et que l'on ait det(D_i f_j)∉𝔭'",
    "det(D_if_j): no parentheses around f_j (crop p211_b_det)",
    "\\det(D_i(f_j))", "formula",
    r"$\det(D_i(f_j))\notin\mathfrak p$." + NL + r"  \item", r"$\det(D_if_j)\notin\mathfrak p$." + NL + r"  \item",
    note="Independent of the b') label edit (either order).")
add(211, "Théorème (22.7.3), label of condition b')", "b') upright (crop p211_labels)",
    "\\item[b')] italic in the theorem environment", "convention",
    r"[b')] Il existe une", r"[\textup{b')}] Il existe une", conv=6)
add(211, "Théorème (22.7.3) b'): 'engendrent cet idéal de A_𝔭 et que l'on ait'",
    "no comma after A_𝔭 in b') (b) has one; crop p211_bp_det)",
    "'de $A_{\\mathfrak p}$, et'", "punctuation",
    r"$(1\leq i\leq m)$, tels que les images des $f_i$ dans" + NL + r"  $\mathfrak qA_{\mathfrak p}$ engendrent cet idéal de $A_{\mathfrak p}$, et",
    r"$(1\leq i\leq m)$, tels que les images des $f_i$ dans" + NL + r"  $\mathfrak qA_{\mathfrak p}$ engendrent cet idéal de $A_{\mathfrak p}$ et")
add(211, "Théorème (22.7.3) b'): 'et que l'on ait det(D_i f_j)∉𝔭.'",
    "det(D_if_j): no parentheses around f_j (crop p211_bp_det)",
    "\\det(D_i(f_j))", "formula",
    r"$\det(D_i(f_j))\notin\mathfrak p$." + NL + r"\end{enumerate}", r"$\det(D_if_j)\notin\mathfrak p$." + NL + r"\end{enumerate}")
add(211, "proof of (22.7.3), case A): 'A) k est de caractéristique 0.'",
    "the label A) is upright (crop p211_A); only 'est de caractéristique' is italic",
    "\\emph{A)}: italic in the roman proof", "italics",
    r"\emph{A)} $k$", r"A) $k$")
add(211, "proof of (22.7.3), case A): 'les deux conditions étant équivalentes'",
    "'condiıions': the t is printed as a letter without ascender, crossbar or dot (5x crop p211_cond2)",
    "conditions: silent correction", "misprint_in_print",
    r"les deux conditions", r"les deux condi{\i}ions", conf="medium", corrected="conditions",
    note="Wrong or damaged sort for t. The reading is certain; medium only because it is typographical: drop the edit if such slips are not reproduced (same treatment as 'ıout' on p. 149).")
add(211, "proof of (22.7.3), end of case A): 'l'équivalence de a), b) et b') (avec k'=K_0 dans b'))'",
    "a), b), b') and the second b') in italic (crop p211_val)",
    "all four labels upright", "italics",
    r"l'équivalence de a), b) et b') (avec $k'=K_0$ dans b')).",
    r"l'équivalence de \emph{a)}, \emph{b)} et \emph{b')} (avec $k'=K_0$ dans \emph{b')}).")
add(211, "proof of (22.7.3), case B): 'B) k est de caractéristique p>0.'",
    "the label B) is upright (crop p211_B)",
    "\\emph{B)}: italic in the roman proof", "italics",
    r"\emph{B)} $k$", r"B) $k$")
add(211, "proof of (22.7.3), case B): 'que la condition a) équivaut'",
    "a) in italic (crop p211_condA)", "a) upright", "italics",
    r"la condition a) équivaut", r"la condition \emph{a)} équivaut")
add(211, "proof of (22.7.3), case B): '(où L=k(𝔭))'",
    "bold italic k in k(𝔭) (crop p211_condA)", "plain k", "convention",
    r"(où $L=k(\mathfrak p)$)", r"(où $L=\boldsymbol{k}(\mathfrak p)$)", conv=1)
add(211, "proof of (22.7.3), case B): 'est injectif. Donc (19.1.12, c))'",
    "'injectif' in italic (crop p211_inj); the later 'est injectif entraîne' is roman",
    "injectif upright", "italics",
    r"injectif. Donc", r"\emph{injectif}. Donc")
add(211, "proof of (22.7.3), case B): '(19.1.12, c)) montre donc déjà que b) implique a)'",
    "c), b), a) in italic (crop p211_inj)", "upright", "italics",
    r"(19.1.12, c)) montre donc déjà que b) implique a)~;",
    r"(19.1.12, \emph{c)}) montre donc déjà que \emph{b)} implique \emph{a)}~;")
add(211, "proof of (22.7.3), case B): 'comme par ailleurs b') implique trivialement b)'",
    "b'), b) in italic (crop p211_inj)", "upright", "italics",
    r"ailleurs b') implique trivialement b),", r"ailleurs \emph{b')} implique trivialement \emph{b)},")
add(211, "proof of (22.7.3), case B): 'que j_0 est injectif entraîne b').'",
    "b') in italic (crop p211_inj)", "upright", "italics",
    r"injectif entraîne b').", r"injectif entraîne \emph{b')}.")
add(211, "end of the page, after display (22.7.3.1): the sentence continues on p. 212 ('… l'homomorphisme composé (22.7.3.1) est injectif')",
    "no paragraph break: p. 212 begins 'est injectif.' at the left margin",
    "blank line between \\end{equation} and the page-212 marker (and another after the marker)",
    "other", r"\tag{22.7.3.1}" + NL + r"\end{equation}" + NL + NL, r"\tag{22.7.3.1}" + NL + r"\end{equation}" + NL,
    note="Removes the blank line before \\oldpage[0\\textsubscript{IV-1}]{212}; apply together with the p. 212 finding that removes the blank line after that marker.")

# ---------------------------------------------------------------- page 212
add(212, "top of the page: 'est injectif.' continues the sentence of p. 211 (after display (22.7.3.1))",
    "no paragraph break: p. 212 begins at the left margin",
    "blank line after the marker", "other",
    MARK + "{212}" + NL + NL + "est", MARK + "{212}" + NL + "est",
    note="Apply together with the p. 211 finding that removes the blank line before this marker.")
add(212, "line 1: 'est injectif. Considérons encore le diagramme commutatif'",
    "'injectif' in italic", "injectif upright", "italics",
    r"injectif. Considérons", r"\emph{injectif}. Considérons")
add(212, "after (22.7.3.2): 'et que l'hypothèse a) implique que'",
    "a) in italic (crop p212_hypa)", "a) upright", "italics",
    r"l'hypothèse a) implique", r"l'hypothèse \emph{a)} implique")
add(212, "display (22.7.3.3): 'Ker(i')=Ker(i)'",
    "Ker(i')=Ker(i)", "\\operatorname{Ker}(i')=\\operatorname{Ker}(i) (keeps the printed reading)",
    "misprint_in_print", nofix=True, corrected=r"\operatorname{Ker}(i')=\operatorname{Ker}(i_0).",
    note="Authors' errata, Liste 3 (EGA IV part 4, ega4-errata-addenda-list3-fr.tex, '(0_IV, 22.7.3)'): 'Ligne 21 du bas de la p. 212, remplacer Ker(i) par Ker(i_0)'; line 21 from the bottom is display (22.7.3.3). The diplomatic TeX keeps the print.")
add(212, "after the exact sequence (p/p²)⊗L → Ω̂ → Ω̂ → 0: 'Or, les hypothèses faites permettent'",
    "new indented paragraph (crop p212_or)", "no blank line after \\]: the sentence continues the paragraph unindented",
    "other", r"\longrightarrow0." + NL + r"\]" + NL + r"Or, les", r"\longrightarrow0." + NL + r"\]" + NL + NL + r"Or, les")
add(212, "after the display rg_L(Ω̂…)=dim(A/𝔭)+…: 'Mais on a'",
    "new indented paragraph (crop p212_mais); the later 'par (16.5.11)', 'puisque', 'en vertu de' are at the margin",
    "no blank line after \\]", "other",
    r"\Omega^1_{K_0/k'}." + NL + r"\]" + NL + r"Mais on a", r"\Omega^1_{K_0/k'}." + NL + r"\]" + NL + NL + r"Mais on a")
add(212, "display 'dim(A/𝔭)=dim(A)—dim(A_𝔭)'",
    "long dash for the subtraction (crop p212_dims)", "minus sign", "convention",
    r"\dim(A)-\dim(A_{\mathfrak p})", r"\dim(A)\setmin\dim(A_{\mathfrak p})", conv=7,
    note="Long dash used for a subtraction (GLOBAL_ISSUES 23); \\setmin as in the earlier fixes, pending the convention-7 decision.")
add(212, "'par (16.5.11)' between the displays", "no comma after (16.5.11) (crop p212_dims)",
    "'par (16.5.11),'", "punctuation", r"par (16.5.11),", r"par (16.5.11)")
add(212, "display 'dim(A_𝔭)=rg_L((𝔭/𝔭²)⊗_L L)'",
    "⊗_L: subscript L, not A (3x crop p212_tensL)", "\\otimes_AL: silent correction",
    "misprint_in_print", r"\mathfrak p^2)\otimes_AL\bigr)", r"\mathfrak p^2)\otimes_LL\bigr)",
    corrected=r"(\mathfrak p/\mathfrak p^2)\otimes_AL",
    note="Authors' errata, Liste 3 ('(0_IV, 22.7.3)'): 'Ligne 12 du bas de la p. 212, remplacer (p/p²)⊗_L L par (p/p²)⊗_A L'.")
add(212, "'puisque A_𝔭 est régulier (17.1.1) et enfin'", "no comma after (17.1.1) (crop p212_dims)",
    "'(17.1.1), et enfin'", "punctuation", r"(17.1.1), et enfin", r"(17.1.1) et enfin")
add(212, "display (20.6.22.1): 'Υ_{L/k} → (𝔭A_𝔭)/(𝔭A_𝔭)² → Ω¹_{A_𝔭/k}⊗_{A_𝔭} L'",
    "no punctuation at the end of the display (crop p212_ups)", "comma after L", "punctuation",
    r"\otimes_{A_{\mathfrak p}}L," + NL + r"\]", r"\otimes_{A_{\mathfrak p}}L" + NL + r"\]")
add(212, "last paragraph: 'que χ_{A_𝔭/k} est un homomorphisme injectif'",
    "'injectif' in italic", "injectif upright", "italics",
    r"homomorphisme injectif, donc", r"homomorphisme \emph{injectif}, donc")

# ---------------------------------------------------------------- page 213
add(213, "Remarque (22.7.4): 'que la condition b') est encore équivalente'",
    "b') in italic in the roman remark", "plain b') (italic only through the remark environment)", "italics",
    r"la condition b') est encore", r"la condition \emph{b')} est encore",
    note="Judged as if the remark body were roman (document-wide remark item).")
add(213, "Corollaire (22.7.5): 'Sous les hypothèses générales de (22.7.3), l'ensemble'",
    "(22.7.3) upright inside the italic statement (crop p213_cor5)", "(22.7.3) italic (corollary environment)",
    "convention", r"générales de (22.7.3), l'ensemble", r"générales de \textup{(22.7.3)}, l'ensemble", conv=6)
add(213, "proof of (22.7.5): 'vérifient le critère b) de (22.7.3)'",
    "b) in italic", "b) upright", "italics",
    r"le critère b) de (22.7.3)", r"le critère \emph{b)} de (22.7.3)")
add(213, "proof of (22.7.5): 'on a aussi f=det(D_i f_i)∉𝔭''",
    "det(D_if_i): the second subscript is i, no descender (6x crop p213_det2)", "\\det(D_if_j): silent correction",
    "misprint_in_print", r"\det(D_if_j)", r"\det(D_if_i)", corrected=r"\det(D_if_j)",
    note="The determinant of (22.7.3, b)) is det(D_i f_j). Not in the authors' errata.")
add(213, "proof of (22.7.6): 'B est une algèbre sur un corps premier k'",
    "'premier' in italic (crop p213_1988)", "premier upright", "italics",
    r"corps premier $k$", r"corps \emph{premier} $k$")
add(213, "proof of (22.7.6): 'donc (19.8.8, (i)) de la forme A/𝔮'",
    "(19.8.8, (i)) (4x crop p213_1988c)", "(19.8.8, (ii))", "number",
    r"donc (19.8.8, (ii))", r"donc (19.8.8, (i))",
    note="The print is right: (19.8.8, (i)) is the statement that a complete noetherian local ring containing a field is a quotient of a power-series ring (ega0-19b-fr.tex, theorem 19.8.8).")
add(213, "Remarques (22.7.7) (i): '(IV, 6.12.7)'", "bold IV", "plain IV", "convention",
    r"(IV, 6.12.7)", r"(\textbf{IV}, 6.12.7)", conv=2)
add(213, "Remarques (22.7.7) (ii): 'que [k:k^p] soit fini.'", "'fini' in italic",
    "fini upright (remarks body judged as roman)", "italics",
    r"soit fini. Prenons", r"soit \emph{fini}. Prenons")
add(213, "Remarques (22.7.7) (ii): 'l'idéal principal Af, où f=U^p—Σ X_n T^{np}; A est un anneau factoriel' (1 of 2)",
    "the formula is in the running text (same line as 'q égal à …' and 'A est un anneau factoriel'; crop p213_sum)",
    "set as a display \\[ … \\]", "other",
    r"où" + NL + r"  \[" + NL + r"    f=", r"où $f=",
    note="First half of the display-to-inline change; the second half is the next edit but one ('X_nT^{np}~;\\n  \\]\\n'). Apply both or neither; the convention-7 edit between them is independent.")
add(213, "Remarques (22.7.7) (ii): 'f=U^p—Σ_{n=0}^∞ X_n T^{np}'",
    "long dash for the subtraction (crop p213_sum)", "minus sign", "convention",
    r"U^p-\sum", r"U^p\setmin\sum", conv=7,
    note="GLOBAL_ISSUES 23; \\setmin pending the convention-7 decision.")
add(213, "Remarques (22.7.7) (ii): '… X_n T^{np}; A est un anneau factoriel' (2 of 2)",
    "inline formula followed by ';' in the running line", "display closed by \\]", "other",
    r"X_nT^{np}~;" + NL + r"  \]" + NL, r"X_nT^{np}$~;" + NL,
    note="Second half of the display-to-inline change; apply together with the first half ('où\\n  \\[\\n    f=').")
add(213, "Remarques (22.7.7) (ii): 'les k-dérivations de A dans lui-même'",
    "'dérıvations': the first i after r has no dot (6x crop p213_deriv2)", "dérivations: silent correction",
    "misprint_in_print", r"$k$-dérivations de $A$", r"$k$-dér{\i}vations de $A$", conf="medium", corrected="dérivations",
    note="Dotless i (missing dot or wrong sort); drop the edit if such slips are not reproduced (as 'ıout', p. 149).")
add(213, "Remarques (22.7.7) (ii), last line: 'les critères b) et b') de (22.7.3)'",
    "b), b') in italic", "upright (remarks body judged as roman)", "italics",
    r"les critères b) et b') de", r"les critères \emph{b)} et \emph{b')} de")
add(213, "§ 23, first sentence: 'seront complétés dans IV, (7.6) et (7.7)'", "bold IV", "plain IV", "convention",
    r"complétés dans IV, (7.6)", r"complétés dans \textbf{IV}, (7.6)", conv=2,
    note="In ega0-23-fr.tex, before its first page marker (lines 1-14).")
add(213, "end of the page, Définition (23.1.1): '… la fermeture intégrale A' de A dans K' est' / p. 214 'un A-module de type fini'",
    "no paragraph break: p. 214 begins at the left margin, mid-sentence",
    "blank line before the page-214 marker (and another after it)", "other",
    r"$A'$ de $A$ dans $K'$ est" + NL + NL, r"$A'$ de $A$ dans $K'$ est" + NL,
    note="In ega0-23-fr.tex, before its first page marker; apply together with the p. 214 finding that removes the blank line after \\oldpage[0\\textsubscript{IV-1}]{214}.")

# ---------------------------------------------------------------- page 214
add(214, "top of the page: 'un A-module de type fini' continues Définition (23.1.1)",
    "no paragraph break: p. 214 begins at the left margin, mid-sentence", "blank line after the marker", "other",
    MARK + "{214}" + NL + NL + "un $A$-module", MARK + "{214}" + NL + "un $A$-module",
    note="Apply together with the p. 213 finding that removes the blank line before this marker (ega0-23-fr.tex, before its first marker).")
add(214, "Définition (23.1.1), line 1: '(autrement dit, une A-algèbre finie)'",
    "roman '(autrement dit, une A-algèbre' and ')', italic 'finie' inside the italic definition (crop p214_l1)",
    "all italic (definition environment)", "convention",
    r"(autrement dit, une $A$-algèbre finie)", r"\textup{(autrement dit, une $A$-algèbre} finie\textup{)}", conv=6)
add(214, "Proposition (23.1.2): 'pour toute extension radicielle finie K' de K'",
    "'radicielle' upright inside the italic statement (crop p214_rad)", "italic (proposition environment)", "convention",
    r"radicielle finie $K'$", r"\textup{radicielle} finie $K'$", conv=6)
add(214, "proof of (23.1.2): 'pour toute extension quasi-galoisienne finie L de K'",
    "'quasi-galoisienne' in italic", "upright", "italics",
    r"extension quasi-galoisienne finie", r"extension \emph{quasi-galoisienne} finie")
add(214, "proof of (23.1.2): 'Or L est une extension galoisienne de la plus grande'",
    "'galoisienne' in italic", "upright", "italics",
    r"extension galoisienne de la", r"extension \emph{galoisienne} de la")
add(214, "proof of (23.1.2): 'dans une extension séparable de K''",
    "'séparable' in italic", "upright", "italics",
    r"extension séparable de $K'$", r"extension \emph{séparable} de $K'$")
add(214, "after (23.1.2): 'lorsque K est de caractéristique 0'",
    "'caractéristique' in italic (crop p214_car)", "upright", "italics",
    r"de caractéristique $0$", r"de \emph{caractéristique} $0$")
add(214, "Théorème (23.1.3), label (i)", "(i) upright", "\\item[(i)] italic in the theorem environment", "convention",
    r"\item[(i)]", r"\item[\textup{(i)}]", conv=6)
add(214, "Théorème (23.1.3), label (ii)", "(ii) upright", "\\item[(ii)] italic in the theorem environment", "convention",
    r"\item[(ii)]", r"\item[\textup{(ii)}]", conv=6)
add(214, "Théorème (23.1.3), label (iii)", "(iii) upright", "\\item[(iii)] italic in the theorem environment", "convention",
    r"\item[(iii)]", r"\item[\textup{(iii)}]", conv=6)
add(214, "Théorème (23.1.3), after the list: 'Alors A est un anneau japonais.'",
    "new indented paragraph (indented like the items)", "'Alors' follows \\end{enumerate} without a blank line",
    "other", r"\end{enumerate}" + NL + r"Alors $A$ est", r"\end{enumerate}" + NL + NL + r"Alors $A$ est",
    conf="medium", note="Same form as earlier page fixes (pp. 18, 48, 75).")
add(214, "proof of (23.1.3.1), last line: 'on en conclut s'sb'=x^{n-1}as'",
    "s'sb'=x^{n-1}as: no prime on the last s (crop p214_rec)", "$s'sb'=x^{n-1}as$ (keeps the printed reading)",
    "misprint_in_print", nofix=True, conf="medium", corrected=r"$s'sb'=x^{n-1}as'$",
    note="From s'sb=x^nas' (printed two lines earlier) and b=xb', cancelling the non-zero-divisor x gives s'sb'=x^{n-1}as'. Not in the authors' errata.")
add(214, "end of the page: 'comme V est intégralement clos, le même' / p. 215 'raisonnement que ci-dessus'",
    "no paragraph break: p. 215 begins at the left margin, mid-sentence",
    "blank line before the page-215 marker (and another after it)", "other",
    r"clos, le même" + NL + NL, r"clos, le même" + NL,
    note="Apply together with the p. 215 finding that removes the blank line after the marker.")

# ---------------------------------------------------------------- page 215
add(215, "top of the page: 'raisonnement que ci-dessus' continues the sentence of p. 214",
    "no paragraph break", "blank line after the marker", "other",
    MARK + "{215}" + NL + NL + "raisonnement", MARK + "{215}" + NL + "raisonnement",
    note="Apply together with the p. 214 finding that removes the blank line before this marker.")
add(215, "line 4: 'dont l'idéal maximal 𝔪' est l'ensemble des x'^q∈K' tels que x'^q∈𝔪'",
    "x'^q∈K' (crop p215_l4)", "$x'\\in K'$: silent correction", "misprint_in_print",
    r"$x'\in K'$ tels que $x'^q\in\mathfrak m$", r"$x'^q\in K'$ tels que $x'^q\in\mathfrak m$",
    corrected=r"$x'\in K'$ tels que $x'^q\in\mathfrak m$",
    note="Authors' errata, Liste 3 ('(0_IV, 23.1.3)'): 'Ligne 4 de la p. 215, remplacer x'^q∈K' par x'∈K''.")
add(215, "proof of (23.1.3.2): 'et posons x'=z'y'^n avec z'∈K''",
    "z'y'^n: prime on y (6x crop p215_zy2)", "$x'=z'y^n$: silent correction", "misprint_in_print",
    r"$x'=z'y^n$", r"$x'=z'y'^n$", corrected=r"$x'=z'y^n$",
    note="y is the element with y^q=x (no y' is defined); the proof then uses x'^q=z'^qx^n. Not in the authors' errata.")
add(215, "proof of (23.1.3.2), line 9 of the page: 'On a x'^q∈A''",
    "x'^q∈A'", "$x'^q\\in A'$ (keeps the printed reading)", "misprint_in_print", nofix=True,
    corrected=r"$x'^q\in A$",
    note="Authors' errata, Liste 3 ('(0_IV, 23.1.3)'): 'Ligne 9 de la p. 215, remplacer x'^q∈A' par x'^q∈A'.")
add(215, "proof of (23.1.3.2): 'x' est somme de produits t'_1 … t'_n'",
    "baseline dots (6x crop p215_dots)", "\\cdots", "symbol",
    r"t'_1\cdots t'_n", r"t'_1\ldots t'_n")
add(215, "'induite par la topologie 𝔪'-préadique de V''",
    "'-préadique' in italic (crop p215_preadic)", "upright", "italics",
    r"$\mathfrak m'$-préadique de $V'$", r"$\mathfrak m'$-\emph{préadique} de $V'$")
add(215, "'Prouvons ensuite que A'/xA' est un A-module de type fini.'",
    "'de type fini' in italic (crop p215_tf)", "upright", "italics",
    r"de type fini. Comme", r"\emph{de type fini}. Comme")
add(215, "'c'est-à-dire du corps résiduel de V''",
    "'corps résiduel' in italic (crop p215_cr)", "upright", "italics",
    r"du corps résiduel de $V'$", r"du \emph{corps résiduel} de $V'$")
add(215, "'qui est une extension finie du corps résiduel V/𝔪 de V'",
    "'finie' in italic (crop p215_cr)", "upright", "italics",
    r"extension finie du corps résiduel", r"extension \emph{finie} du corps résiduel")
add(215, "'A' est un sous-anneau de son complété Â' pour cette topologie'",
    "hat over A only, prime outside the hat (6x crop p215_hat)", "\\widehat{A'} (hat over A')", "formula",
    r"complété $\widehat{A'}$", r"complété $\widehat{A}'$",
    note="Same pattern as convention 8, with a hat (as pp. 91, 93).")
add(215, "'la topologie xA-préadique, Â' est un A-module de type fini'",
    "hat over A only, prime outside the hat (6x crop p215_hat2)", "\\widehat{A'}", "formula",
    r"$\widehat{A'}$ est un", r"$\widehat{A}'$ est un",
    note="Same pattern as convention 8, with a hat.")
add(215, "'en vertu de (0_I, 7.2.9)'", "bold 0", "plain 0", "convention",
    r"(0\textsubscript{I}, 7.2.9)", r"(\textbf{0}\textsubscript{I}, 7.2.9)", conv=2)
add(215, "'donc il en est de même de A, C.Q.F.D.'",
    "A without prime (4x crop p215_deA)", "$A'$: silent correction", "misprint_in_print",
    r"de même de $A'$, C.Q.F.D.", r"de même de $A$, C.Q.F.D.", corrected=r"$A'$",
    note="The conclusion is that A' (contained in its completion) is a finite A-module; 'A' is trivial. Not in the authors' errata.")
add(215, "Théorème (23.1.5) (Nagata): 'Tout anneau local noethérien intègre complet A est un anneau japonais.'",
    "'complet' upright inside the italic statement (crop p215_thm)", "italic (theorem environment)", "convention",
    r"intègre complet $A$", r"intègre \textup{complet} $A$", conv=6)
add(215, "proof of (23.1.5): 'un anneau local complet et régulier'",
    "'régulier' in italic (crop p215_reg)", "upright", "italics",
    r"complet et régulier, tel", r"complet et \emph{régulier}, tel")
add(215, "proof of (23.1.5): 'tel que A soit une B-algèbre finie;'",
    "'finie' in italic (crop p215_reg)", "upright", "italics",
    r"$B$-algèbre finie~;", r"$B$-algèbre \emph{finie}~;")
add(215, "end of the page: 'il suffit évidemment de prouver' / p. 216 'que B est un anneau japonais'",
    "no paragraph break: p. 216 begins at the left margin, mid-sentence (crop p216_top)",
    "blank line before the page-216 marker (and another after it, in the p. 216 segment)", "other",
    r"évidemment de prouver" + NL + NL, r"évidemment de prouver" + NL,
    note="Apply together with the removal of the blank line after \\oldpage[0\\textsubscript{IV-1}]{216} (p. 216 segment: '{216}\\n\\nque $B$' -> '{216}\\nque $B$').")

# ---------------------------------------------------------------- checks
ok = True
for n in range(211, 216):
    t = page_text(n)
    spans = []
    for d in F:
        if d["page"] != n or d["fix"] is None:
            continue
        o = d["fix"]["old"]
        c = t.count(o)
        if c != 1:
            ok = False
            print("COUNT", n, c, repr(o)[:90])
            continue
        s = t.index(o)
        spans.append((s, s + len(o), o))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP", n, repr(a[2])[:60], repr(b[2])[:60])
    # sequential application in list order
    u = t
    for d in F:
        if d["page"] == n and d["fix"] is not None:
            o, w = d["fix"]["old"], d["fix"]["new"]
            if u.count(o) != 1:
                ok = False
                print("SEQ", n, repr(o)[:80])
            u = u.replace(o, w, 1)

from collections import Counter
cnt = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for n in range(211, 216):
    print(n, "normal", cnt[(n, "normal")], "convention", cnt[(n, "convention")], "misprint", cnt[(n, "misprint")])
print("total", len(F), "checks ok" if ok else "CHECKS FAILED")
if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        json.dump(F, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("wrote", OUT)
