import json

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- p. 220 ----------------
add(220, "top of p. 220, Proposition (19.8.1): 'Dans ces conditions :'",
    "italic, like the rest of the statement (crop c220_dans.png)",
    "\\emph{Dans ces conditions:} inside the italic proposition: comes out upright",
    "convention", 6, "high",
    "\\emph{Dans ces conditions:}", "Dans ces conditions:",
    "Not a boundary fix: the marker and its blank lines are right (p. 220 opens with this indented paragraph, after the list 1°, 2° that ends p. 219); only the \\emph goes.")
add(220, "Proposition (19.8.1) (i): item label", "'(i)' upright (crop c220_i.png)",
    "\\item[(i)] italic inside the statement", "convention", 6, "high",
    "\\item[(i)] Supposons $S_\\alpha$", "\\item[\\textup{(i)}] Supposons $S_\\alpha$",
    "Roman-numeral labels in italic statements are upright (GLOBAL_ISSUES 16).")
add(220, "Proposition (19.8.1) (ii): item label", "'(ii)' upright",
    "\\item[(ii)] italic", "convention", 6, "high",
    "\\item[(ii)] Supposons $X_\\alpha$", "\\item[\\textup{(ii)}] Supposons $X_\\alpha$", "GLOBAL_ISSUES 16.")
add(220, "proof of (19.8.1) (i), l. 1: 'on a 𝓕/(Σ_{j=1}^{i-1} f_j𝓕)=p*_λ(𝓕_λ/(Σ_{j=1}^{i-1} f_{jλ}𝓕_λ)), donc'",
    "set in the line after 'on a', plain parentheses, comma after it (crop c220_formula.png)",
    "displayed (\\[...\\]) with \\Bigl/\\Bigr", "formula", None, "high",
    "la projection canonique, on a\n  \\[\n    \\sh F/\\Bigl(\\sum_{j=1}^{i-1}f_j\\sh F\\Bigr)\n    =p_\\lambda^*\\Bigl(\\sh F_\\lambda/\\Bigl(\\sum_{j=1}^{i-1}f_{j\\lambda}\\sh F_\\lambda\\Bigr)\\Bigr),\n  \\]\n  donc on est ramené",
    "la projection canonique, on a $\\sh F/(\\sum_{j=1}^{i-1}f_j\\sh F)=p_\\lambda^*(\\sh F_\\lambda/(\\sum_{j=1}^{i-1}f_{j\\lambda}\\sh F_\\lambda))$, donc on est ramené",
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21/104).")
add(220, "proof of (19.8.1) (i): 'résulte de ce que p_λ est plat (8.3.8) et de (0, 15.1.5)'", "bold 0",
    "plain $0$", "convention", 2, "high", "et de ($0$, 15.1.5)", "et de (\\textbf{0}, 15.1.5)", "")
add(220, "proof of (19.8.1) (i): 'résulte encore de (0, 15.2.5), avec λ=α'", "bold 0",
    "plain $0$", "convention", 2, "high", "encore de ($0$, 15.2.5)", "encore de (\\textbf{0}, 15.2.5)", "")
add(220, "Proposition (19.8.2) (i): item label", "'(i)' upright", "\\item[(i)] italic", "convention", 6, "high",
    "\\item[(i)] Soient $\\sh F_\\alpha$", "\\item[\\textup{(i)}] Soient $\\sh F_\\alpha$", "GLOBAL_ISSUES 16.")
add(220, "Proposition (19.8.2) (i): 'régulière relativement à S (19.2.1), il faut'",
    "reference upright inside the italic statement (crop c220_1921.png)", "italic (environment)",
    "convention", 6, "high",
    "relativement à $S$ (19.2.1), il faut", "relativement à $S$ \\textup{(19.2.1)}, il faut", "")
add(220, "Proposition (19.8.2) (ii): item label", "'(ii)' upright (crop c220_ii.png)", "\\item[(ii)] italic",
    "convention", 6, "high",
    "\\item[(ii)] Soient $Y_\\alpha$", "\\item[\\textup{(ii)}] Soient $Y_\\alpha$", "GLOBAL_ISSUES 16.")
add(220, "last line of p. 220: 'une S_α-immersion localement | de présentation finie' (page break 220/221)",
    "p. 221 begins mid-sentence: 'de présentation finie. Pour que' at the left margin (page_221_s1.png)",
    "blank lines before and after \\oldpage[IV-4]{221}: a paragraph break inside the item", "marker", None, "high",
    "$S_\\alpha$-immersion localement\n\n", "$S_\\alpha$-immersion localement\n",
    "The marker is at the right place. Part 1 of 2: the first p. 221 finding removes the blank line after \\oldpage[IV-4]{221}; apply both (\\oldpage ends with \\ignorespaces, which does not skip a \\par).")

# ---------------- p. 221 ----------------
add(221, "top of p. 221: '\\oldpage[IV-4]{221}' + blank line before 'de présentation finie'",
    "mid-sentence page break (see the last p. 220 finding)", "blank line after the marker", "marker", None, "high",
    "\\oldpage[IV-4]{221}\n\n  de présentation finie.", "\\oldpage[IV-4]{221}\n  de présentation finie.",
    "Part 2 of 2 with the last p. 220 finding; both blank lines must go.")
add(221, "proof of (19.8.2) (i), l. 1: 'résulte de (0, 15.1.15)'", "bold 0", "plain $0$", "convention", 2, "high",
    "résulte de ($0$, 15.1.15)", "résulte de (\\textbf{0}, 15.1.15)", "")
add(221, "proof of (19.8.2) (i): '... relativement à S_λ. Soient s l'image de x dans S'",
    "'Soient s l'image' continues the same line and paragraph after 'relativement à S_λ.' (page_221_s2.png, l. 3)",
    "blank line before '  Soient $s$': a paragraph break the print lacks", "other", None, "high",
    "relativement à $S_\\lambda$.\n\n  Soient $s$", "relativement à $S_\\lambda$.\n  Soient $s$", "")
add(221, "proof of (19.8.2) (i): 'puisqu'il en est ainsi de Spec(k(s_μ)) → Spec(k(s_λ))'",
    "both k bold italic (crop c221_Spec.png)", "plain k", "convention", 1, "high",
    "$\\Spec(k(s_\\mu))\\to\\Spec(k(s_\\lambda))$",
    "$\\Spec(\\boldsymbol{k}(s_\\mu))\\to\\Spec(\\boldsymbol{k}(s_\\lambda))$", "Two occurrences in one edit.")
add(221, "proof of (19.8.2) (i): 'les sections f_i⊗1 de 𝓕_s=𝓕⊗_{𝒪_X}k(s)'",
    "subscript 𝒪_X (crops c221_Spec.png, c221_OX.png)", "\\otimes_{\\sh O_S} (rewritten)", "formula", None, "high",
    "$\\sh F_s=\\sh F\\otimes_{\\sh O_S}", "$\\sh F_s=\\sh F\\otimes_{\\sh O_X}",
    "The TeX rewrote the print's notation (GLOBAL_ISSUES 102/104). Not a misprint: EGA writes 𝓕⊗_{𝒪_X}k(s) for the fibre elsewhere too (ega4-9 'F_s=F⊗_{O_X}k(s)', ega4-20 'L_s=L⊗_{O_X}k(s)'). Independent of the next finding (adjacent text, no overlap).")
add(221, "same formula: 'k(s)'", "bold italic k", "plain k", "convention", 1, "high",
    "k(s)$ au-dessus de $X_s$", "\\boldsymbol{k}(s)$ au-dessus de $X_s$", "")
add(221, "proof of (19.8.2) (i): '(𝓕_λ)_{s_λ}=𝓕_λ⊗_{𝒪_{X_λ}}k(s_λ)'",
    "subscript 𝒪_{X_λ} (crop c221_OXl.png)", "\\otimes_{\\sh O_{S_\\lambda}} (rewritten)", "formula", None, "high",
    "=\\sh F_\\lambda\\otimes_{\\sh O_{S_\\lambda}}", "=\\sh F_\\lambda\\otimes_{\\sh O_{X_\\lambda}}",
    "Same rewriting as 𝒪_X above (GLOBAL_ISSUES 102/104); not a misprint. Independent of the next finding.")
add(221, "same formula: 'k(s_λ)'", "bold italic k (crop c221_OXl.png)", "plain k", "convention", 1, "high",
    "k(s_\\lambda)$ au-dessus de $(X_\\lambda)", "\\boldsymbol{k}(s_\\lambda)$ au-dessus de $(X_\\lambda)", "")
add(221, "end of page_221.tex: the heading '19.9. Suites 𝓕-régulières et profondeur.' (it opens printed p. 222)",
    "p. 221 ends with Remarque (19.8.3); p. 222 begins with the heading 19.9 (page_221_s4.png, page_222_s1.png)",
    "\\subsection{...19.9}, its \\EGAReaderTarget and \\label stand before \\oldpage[IV-4]{222}", "marker", None, "high",
    "\\subsection{\\texorpdfstring{Suites $\\sh F$-régulières et profondeur.}{Suites F-régulières et profondeur.}}\n\\EGAReaderTarget{ega4.c04.subsec.19-9}{subsection:IV.19.9}\n\\label{IV.19.9}\n\n",
    "",
    "The marker stands too late (after the heading). Two-part move (the heading moves, not the marker, so each edit stays in its own page segment), as for 18.2 at marker 111: part 1 of 2 removes the heading from the end of the p. 221 segment; the first p. 222 finding re-inserts it after \\oldpage[IV-4]{222}. Apply both or neither.")

# ---------------- p. 222 ----------------
add(222, "top of p. 222: heading 19.9", "'19.9. Suites 𝓕-régulières et profondeur.' is the first line of p. 222",
    "heading missing after \\oldpage[IV-4]{222} (it stands at the end of the p. 221 segment)", "marker", None, "high",
    "\\oldpage[IV-4]{222}\n\n\\begin{env}[19.9.1]",
    "\\oldpage[IV-4]{222}\n\n\\subsection{\\texorpdfstring{Suites $\\sh F$-régulières et profondeur.}{Suites F-régulières et profondeur.}}\n\\EGAReaderTarget{ega4.c04.subsec.19-9}{subsection:IV.19.9}\n\\label{IV.19.9}\n\n\\begin{env}[19.9.1]",
    "Part 2 of 2 with the last p. 221 finding (which removes these three lines from the end of the p. 221 segment). Apply both or neither.")
add(222, "(19.9.1.2): 'inf_{z∈T∩Spec(𝒪_{X,t})} prof(𝓕_z)'",
    "variable z under inf and in 𝓕_z (crop c222_inf.png; (19.9.1.1) has x, crop c222_inf1.png)",
    "x in both places (renamed)", "formula", None, "high",
    "\\inf_{x\\in T\\cap\\Spec(\\sh O_{X,t})}\\operatorname{prof}(\\sh F_x),",
    "\\inf_{z\\in T\\cap\\Spec(\\sh O_{X,t})}\\operatorname{prof}(\\sh F_z),",
    "The TeX renamed the print's variable (GLOBAL_ISSUES 102/104).")
add(222, "proof of (19.9.2), l. 1: 'résultant aussitôt de (0, 16.4.5)'", "bold 0", "plain $0$", "convention", 2, "high",
    "aussitôt de ($0$, 16.4.5)", "aussitôt de (\\textbf{0}, 16.4.5)", "")
add(222, "proof of (19.9.2): '... prouvons sa nécessité. | Raisonnons par récurrence sur r'",
    "'Raisonnons' begins a new indented paragraph (same indent as 'La suffisance'; crop c222_rais.png)",
    "same paragraph", "other", None, "high",
    "prouvons sa nécessité. Raisonnons", "prouvons sa nécessité.\n\nRaisonnons", "")
add(222, "proof of (19.9.2): 'puisque prof_{A_𝔭}(M_𝔭)≥r—1 pour tout'",
    "long dash (crop c222_rminus.png; the minus in the subscripts r-1 is the short one)", "minus sign",
    "convention", 7, "high", "\\geq r-1$ pour tout", "\\geq r\\setmin 1$ pour tout",
    "Long dash for subtraction (GLOBAL_ISSUES 23); \\setmin as in the earlier IV-4 fixes.")
add(222, "proof of (19.9.2): 'N=M/(g_1M+...+g_{r-1}M)'", "baseline dots (crop c222_rminus.png)", "\\cdots",
    "symbol", None, "high", "g_1M+\\cdots+g_{r-1}M", "g_1M+\\ldots+g_{r-1}M", "\\cdots where the print has baseline dots.")
add(222, "proof of (19.9.2): 'une suite M_𝔭-régulière (0, 15.1.14)'", "bold 0", "plain $0$", "convention", 2, "high",
    "régulière ($0$, 15.1.14); on conclut", "régulière (\\textbf{0}, 15.1.14); on conclut", "")
add(222, "proof of (19.9.2): 'on conclut donc de (0, 16.4.6)'", "bold 0", "plain $0$", "convention", 2, "high",
    "on conclut donc de ($0$, 16.4.6)", "on conclut donc de (\\textbf{0}, 16.4.6)", "")
add(222, "proof of (19.9.2): 'prof_{A_𝔭}(N_𝔭)=prof_{A_𝔭}(M_𝔭)—(r—1)≥1'", "two long dashes (crop c222_prof.png)",
    "minus signs", "convention", 7, "high", "-(r-1)\\geq1", "\\setmin(r\\setmin 1)\\geq1",
    "Two occurrences in one edit (GLOBAL_ISSUES 23).")
add(222, "proof of (19.9.2): '𝔭A_𝔭 n'est pas associé à M_𝔭 (0, 16.4.6), donc'", "bold 0", "plain $0$",
    "convention", 2, "high", "à $M_{\\mathfrak p}$ ($0$, 16.4.6), donc", "à $M_{\\mathfrak p}$ (\\textbf{0}, 16.4.6), donc", "")
add(222, "Proposition (19.9.3): label a)", "'a)' upright (crop c222_items.png)", "\\item[a)] italic inside the statement",
    "convention", 6, "high", "\\item[a)] Il existe", "\\item[\\textup{a)}] Il existe", "GLOBAL_ISSUES 88.")
add(222, "Proposition (19.9.3): label b)", "'b)' upright", "\\item[b)] italic", "convention", 6, "high",
    "\\item[b)] Il existe", "\\item[\\textup{b)}] Il existe", "GLOBAL_ISSUES 88.")
add(222, "Proposition (19.9.3) b): 'telles que f_i(x)=0 (0_I, 5.5.1) pour'",
    "bold 0 with a light upright subscript I; the reference upright (crop c222_0I.png)",
    "plain 0, italic (environment)", "convention", 2, "high",
    "($0_{\\mathrm I}$, 5.5.1)", "\\textup{($\\mathbf{0}_{\\mathrm I}$, 5.5.1)}",
    "One edit for convention 2 (bold 0) and convention 6 (upright reference inside the italic statement).")
add(222, "Proposition (19.9.3): label c)", "'c)' upright", "\\item[c)] italic", "convention", 6, "high",
    "\\item[c)] On a", "\\item[\\textup{c)}] On a", "GLOBAL_ISSUES 88.")
add(222, "Proposition (19.9.3): 'En outre, l'ensemble des y∈Y ...' after the list",
    "indented new paragraph (left edge at the paragraph indent, like the items; crop c222_enoutre.png)",
    "follows \\end{enumerate} without a blank line (no indent)", "other", None, "high",
    "\\end{enumerate}\nEn outre, l'ensemble", "\\end{enumerate}\n\nEn outre, l'ensemble",
    "GLOBAL_ISSUES 80 pattern.")
add(222, "proof of (19.9.3), l. 1: 'trivialement de a). L'équivalence de a) et b) découle'",
    "labels wholly italic, parentheses included (crop c222_proof.png)", "$a)$ etc.: italic letters, upright parentheses",
    "italics", None, "high",
    "résulte trivialement de $a)$. L'équivalence de $a)$ et $b)$ découle",
    "résulte trivialement de \\emph{a)}. L'équivalence de \\emph{a)} et \\emph{b)} découle", "GLOBAL_ISSUES 88.")
add(222, "proof of (19.9.3), l. 2: 'et de (0, 15.1.14). Il est clair'", "bold 0", "plain $0$", "convention", 2, "high",
    "et de ($0$, 15.1.14). Il est clair", "et de (\\textbf{0}, 15.1.14). Il est clair", "")
add(222, "proof of (19.9.3), l. 3: 'Il est clair que a) entraîne c),'", "labels wholly italic", "italic letters, upright parentheses",
    "italics", None, "high",
    "Il est clair que $a)$ entraîne $c)$, tout", "Il est clair que \\emph{a)} entraîne \\emph{c)}, tout", "GLOBAL_ISSUES 88.")
add(222, "proof of (19.9.3), l. 4: 'que c) implique b). Il résulte de c) et de la définition'",
    "labels wholly italic", "italic letters, upright parentheses", "italics", None, "high",
    "montrons inversement que $c)$ implique $b)$. Il résulte de $c)$ et de la définition",
    "montrons inversement que \\emph{c)} implique \\emph{b)}. Il résulte de \\emph{c)} et de la définition",
    "GLOBAL_ISSUES 88. Independent of the next finding (no overlap).")
add(222, "last line of p. 222: 'de la définition (19.9.1.1) que l'on | peut appliquer' (page break 222/223)",
    "p. 223 begins mid-sentence: 'peut appliquer (19.9.2)' at the left margin (page_223_s1.png)",
    "blank lines before and after \\oldpage[IV-4]{223}", "marker", None, "high",
    "(19.9.1.1) que l'on\n\n", "(19.9.1.1) que l'on\n",
    "The marker is at the right place. Part 1 of 2: the first p. 223 finding removes the blank line after \\oldpage[IV-4]{223}; apply both.")

# ---------------- p. 223 ----------------
add(223, "top of p. 223: '\\oldpage[IV-4]{223}' + blank line before 'peut appliquer'",
    "mid-sentence page break (see the last p. 222 finding)", "blank line after the marker", "marker", None, "high",
    "\\oldpage[IV-4]{223}\n\npeut appliquer", "\\oldpage[IV-4]{223}\npeut appliquer",
    "Part 2 of 2 with the last p. 222 finding; both blank lines must go.")
add(223, "proof of (19.9.3), end: 'utilisant (0, 15.2.4)'", "bold 0", "plain $0$", "convention", 2, "high",
    "utilisant ($0$, 15.2.4)", "utilisant (\\textbf{0}, 15.2.4)", "")
add(223, "Corollaire (19.9.4): 'Avec les notations de (19.9.3), la fonction'",
    "reference upright inside the italic statement (crop c223_cor4.png)", "italic (environment)", "convention", 6, "high",
    "Avec les notations de (19.9.3), la fonction", "Avec les notations de \\textup{(19.9.3)}, la fonction", "")
add(223, "Corollaire (19.9.4): 'la fonction y⇝prof_{Y,y}(𝓕)'", "wavy arrow (crop c223_wavy.png)", "\\mapsto",
    "symbol", None, "high",
    "$y\\mapsto\\operatorname{prof}_{Y,y}(\\sh F)$", "$y\\leadsto\\operatorname{prof}_{Y,y}(\\sh F)$", "")
add(223, "Proposition (19.9.5): 'Avec les notations de (19.9.3), soient'", "reference upright", "italic (environment)",
    "convention", 6, "high",
    "Avec les notations de (19.9.3), soient", "Avec les notations de \\textup{(19.9.3)}, soient", "")
add(223, "proof of (19.9.5): 'on a (loc. cit.) prof(𝓕'_{z''})'",
    "the parentheses are italic like 'loc. cit.' (slant 0.24, against 0.00 for upright parentheses on the page; crop c223_loccit_full.png)",
    "(\\emph{loc. cit.}): upright parentheses", "italics", None, "high",
    "on a (\\emph{loc. cit.})", "on a \\emph{(loc. cit.)}", "Same fix as at earlier '(loc. cit.)' (FIXLOG).")
add(223, "proof of (19.9.5), last sentence: 'g(Spec(𝒪_{X',y'}))=Spec(𝒪_{X,g(y)})'",
    "'g(y)' without a prime, no room for one (crop c223_gy.png; the primes of X', y' just before are clear)",
    "\\Spec(\\sh O_{X,g(y')}) (silent correction)", "misprint_in_print", None, "high",
    "\\Spec(\\sh O_{X,g(y')})", "\\Spec(\\sh O_{X,g(y)})",
    "g is defined on X' and y is a point of X, so g(y) means nothing; the image of y' is meant (g(y')=y). The fix restores the printed reading.",
    corrected="\\Spec(\\sh O_{X,g(y')})")
add(223, "Proposition (19.9.6): the parenthesis '(en désignant par X_{f(y)} ... et en posant Y_{f(y)}=X_{f(y)}∩Y) :'",
    "both parentheses upright (slant 0.00 and -0.06, against 0.24 for the italic parentheses of '(loc. cit.)'; crops c223_paren_open.png, c223_paren_close.png); the words inside italic",
    "italic parentheses (environment)", "convention", 6, "high",
    "(en désignant par $X_{f(y)}$ la fibre de $f$ au point $f(y)$, par $\\sh F_{f(y)}$ l'image réciproque de $\\sh F$ dans $X_{f(y)}$, et en posant $Y_{f(y)}=X_{f(y)}\\cap Y$):",
    "\\textup{(}en désignant par $X_{f(y)}$ la fibre de $f$ au point $f(y)$, par $\\sh F_{f(y)}$ l'image réciproque de $\\sh F$ dans $X_{f(y)}$, et en posant $Y_{f(y)}=X_{f(y)}\\cap Y$\\textup{)}:",
    "Only the two parentheses change; the italic words stay (GLOBAL_ISSUES 26/101: fixed by the print).")
add(223, "Proposition (19.9.6): label a)", "'a)' upright (crop c223_items.png)", "\\item[a)] italic", "convention", 6, "high",
    "\\item[a)] On a", "\\item[\\textup{a)}] On a", "GLOBAL_ISSUES 88.")
add(223, "Proposition (19.9.6): label b)", "'b)' upright", "\\item[b)] italic", "convention", 6, "high",
    "\\item[b)] Il existe", "\\item[\\textup{b)}] Il existe", "GLOBAL_ISSUES 88.")
add(223, "Proposition (19.9.6) b): '(cf. (19.2.1) pour la terminologie)'",
    "'(cf. (19.2.1)' upright, 'pour la terminologie' italic, the closing parenthesis upright (slant 0.00; crops c223_cf.png, c223_nologie_paren.png)",
    "all italic (environment)", "convention", 6, "high",
    "(cf. (19.2.1) pour la terminologie)", "\\textup{(cf. (19.2.1)} pour la terminologie\\textup{)}", "")
add(223, "Proposition (19.9.6): 'L'ensemble V_n des y∈Y ...' after the list",
    "indented new paragraph (crop c223_Vn.png)", "follows \\end{enumerate} without a blank line (no indent)",
    "other", None, "high",
    "\\end{enumerate}\nL'ensemble $V_n$", "\\end{enumerate}\n\nL'ensemble $V_n$", "GLOBAL_ISSUES 80 pattern.")
add(223, "Proposition (19.9.6), end: 'V_n est rétrocompact dans X (0_III, 9.1.1).'",
    "bold 0 with a light subscript III; the reference upright (crop c223_0III.png)", "plain 0, italic (environment)",
    "convention", 2, "high",
    "($0_{\\mathrm{III}}$, 9.1.1)", "\\textup{($\\mathbf{0}_{\\mathrm{III}}$, 9.1.1)}",
    "One edit for convention 2 (bold 0) and convention 6 (upright reference inside the italic statement).")
add(223, "proof of (19.9.6), l. 1: 'la condition a) équivaut'", "label wholly italic (crop c223_conda.png)",
    "$a)$: italic letter, upright parenthesis", "italics", None, "high",
    "la condition $a)$ équivaut", "la condition \\emph{a)} équivaut", "GLOBAL_ISSUES 88.")
add(223, "proof of (19.9.6): 'une suite (g_i)_{1≤i≤n} de sections de 𝓕 au-dessus de U, de sorte que'",
    "script F (crop c223_secF2.png)", "\\sh J (silent correction)", "misprint_in_print", None, "high",
    "de sections de $\\sh J$ au-dessus de $U$, de sorte", "de sections de $\\sh F$ au-dessus de $U$, de sorte",
    "The g_i lift the h_i ∈ 𝒥_{f(y)} and must vanish on U∩Y (condition b)): sections of the Ideal 𝒥, not of the Module 𝓕. The fix restores the printed reading.",
    corrected="de sections de $\\sh J$ au-dessus de $U$")
add(223, "proof of (19.9.6): 'L'équivalence de a) et b) résulte alors de (11.3.8)'", "labels wholly italic (crop c223_deab.png)",
    "italic letters, upright parentheses", "italics", None, "high",
    "L'équivalence de $a)$ et $b)$ résulte", "L'équivalence de \\emph{a)} et \\emph{b)} résulte", "GLOBAL_ISSUES 88.")
add(223, "proof of (19.9.6): '... est ouvert dans Y. Reste à prouver la dernière assertion'",
    "'Reste à prouver' continues the same line and paragraph (page_223_s4.png, l. 1)",
    "blank line before 'Reste à prouver': a paragraph break the print lacks", "other", None, "high",
    "est ouvert dans $Y$.\n\nReste à prouver", "est ouvert dans $Y$.\nReste à prouver", "")
add(223, "page break 223/224 inside 'on peut en outre (8.3.11) supposer | que Y=p^{-1}(Y_0)'",
    "p. 223 ends with 'supposer'; p. 224 begins 'que Y=p^{-1}(Y_0), où p : X→X_0 est la projection canonique' (page_223_s4.png, page_224_s1.png)",
    "\\oldpage[IV-4]{224} stands before Corollaire (19.9.7), about ten printed lines too late", "marker", None, "high",
    "(8.3.11) supposer que $Y", "(8.3.11) supposer\n\\oldpage[IV-4]{224}\nque $Y",
    "Marker move, part 1 of 2: inserts the marker at the printed break (mid-sentence, no blank lines). Apply after all other p. 223 findings (none lies in the moved text 'que Y=... rétrocompact dans X.'); the first p. 224 finding removes the old marker.")
add(224, "old \\oldpage[IV-4]{224} before Corollaire (19.9.7)",
    "'Corollaire (19.9.7)' stands in the middle of printed p. 224, after the paragraph that ends '... V_n est rétrocompact dans X.'",
    "the p. 224 marker stands here", "marker", None, "high",
    "\\oldpage[IV-4]{224}\n\n\\begin{corollary}[19.9.7]", "\\begin{corollary}[19.9.7]",
    "Marker move, part 2 of 2: removes the old marker (apply after the last p. 223 finding, which inserts the new one). The blank line before it (end of the p. 223 segment) stays before the corollary.")
add(224, "Corollaire (19.9.7): 'Sous les hypothèses générales de (19.9.6), la fonction'",
    "reference upright (crop c224_1996.png)", "italic (environment)", "convention", 6, "high",
    "Sous les hypothèses générales de (19.9.6), la fonction",
    "Sous les hypothèses générales de \\textup{(19.9.6)}, la fonction", "")
add(224, "Corollaire (19.9.7): 'la fonction y⇝prof_{Y_{f(y)},y}(𝓕_{f(y)})'", "wavy arrow (crop c224_wavy.png)",
    "\\mapsto", "symbol", None, "high",
    "$y\\mapsto\\operatorname{prof}_{Y_{f(y)},y}(\\sh F_{f(y)})$",
    "$y\\leadsto\\operatorname{prof}_{Y_{f(y)},y}(\\sh F_{f(y)})$", "")
add(224, "Proposition (19.9.8): '(resp. prof((𝓕_{f(x)})_x)≥2). Alors'",
    "'(resp.' and both parentheses upright (slant 0.00; crop c224_resp1.png)", "italic (environment)",
    "convention", 6, "high",
    "(resp. $\\operatorname{prof}((\\sh F_{f(x)})_x)\\geq2$). Alors",
    "\\textup{(resp. $\\operatorname{prof}((\\sh F_{f(x)})_x)\\geq2$)}. Alors", "")
add(224, "Proposition (19.9.8): 'si j : X—Z→X est l'injection canonique'", "long dash (crop c224_XZ2.png)",
    "minus sign", "convention", 7, "high", "$j:X-Z\\to X$", "$j:X\\setmin Z\\to X$", "")
add(224, "Proposition (19.9.8), end: 'relatif à j est injectif (resp. bijectif).'",
    "'(resp.' and both parentheses upright (slants -0.005 and 0.006), 'bijectif' italic (crop c224_bij3.png)",
    "all italic (environment)", "convention", 6, "high",
    "relatif à $j$ est injectif (resp. bijectif).", "relatif à $j$ est injectif \\textup{(resp.} bijectif\\textup{)}.", "")
add(224, "proof of (19.9.8): 'en remplaçant le couple (X, Z) par (X, Z') et (X—Z, Z'∩(X—Z))'",
    "two long dashes (crop c224_XZ.png)", "minus signs", "convention", 7, "high",
    "$(X-Z,Z'\\cap(X-Z))$", "$(X\\setmin Z,Z'\\cap(X\\setmin Z))$", "Two occurrences in one edit.")
add(224, "proof of (19.9.8): 'où 𝔍 est un idéal de type fini de l'anneau B'", "'de type fini' italic (crop c224_ital.png)",
    "roman", "italics", None, "high",
    "est un idéal de type fini de l'anneau", "est un idéal \\emph{de type fini} de l'anneau", "GLOBAL_ISSUES 83.")
add(224, "proof of (19.9.8): 'M un B-module de présentation finie qui est un A-module plat.'", "'plat' italic",
    "roman", "italics", None, "high",
    "qui est un $A$-module plat.", "qui est un $A$-module \\emph{plat}.", "GLOBAL_ISSUES 83.")
add(224, "proof of (19.9.8): 'au cas où N est un A-module de présentation finie. En effet'",
    "'de présentation finie' italic", "roman", "italics", None, "high",
    "est un $A$-module de présentation finie. En effet", "est un $A$-module \\emph{de présentation finie}. En effet",
    "GLOBAL_ISSUES 83.")
add(224, "proof of (19.9.8): 'si l'on pose 𝒢_α=Ñ_α'", "tilde over N only, subscript α outside it",
    "\\widetilde{N_\\alpha}", "convention", 8, "high", "\\widetilde{N_\\alpha}", "\\widetilde{N}_\\alpha", "")
add(224, "proof of (19.9.8), display: 'Γ(X, ℋ) → Γ(X—Z, ℋ)'", "long dash (crop c224_GXZ.png)", "minus sign",
    "convention", 7, "high", "\\Gamma(X-Z,\\sh H)", "\\Gamma(X\\setmin Z,\\sh H)", "")
add(224, "last line of p. 224: 'un B_0-module de type fini M_0 qui est | un A_0-module plat' (page break 224/225)",
    "p. 225 begins mid-sentence: 'un A_0-module plat et un A_0-module N_0' at the left margin (page_225_s1.png, crop c225_top.png)",
    "blank lines before and after \\oldpage[IV-4]{225}", "marker", None, "high",
    "de type fini $M_0$ qui est\n\n", "de type fini $M_0$ qui est\n",
    "BOUNDARY FIX (page break with p. 225). The marker is at the right place. Part 1 of 2: the blank line AFTER \\oldpage[IV-4]{225} lies in the p. 225 segment (next batch: '\\oldpage[IV-4]{225}\\n\\nun $A_0$-module' -> '\\oldpage[IV-4]{225}\\nun $A_0$-module'); both must go.")

out = r"user\Documents\ega_scan_check_20261101\run_IV4\findings_220_224.json"
with open(out, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print(len(F), "findings written")
