import sys, json
sys.dont_write_bytecode = True
sys.stdout.reconfigure(encoding="utf-8")

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex"
OUT = RUN + r"\findings_180_184.json"

F = []


def add(page, where, scan, tex, kind, old, new, note="", conv=None, conf="high", corrected=None, nofix=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if nofix else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


G83 = "GLOBAL_ISSUES 83 (italics lost in 18.10 and later)."
G88 = "GLOBAL_ISSUES 88."
G16 = "GLOBAL_ISSUES 16/88 (labels upright inside italic statements)."

# ------------------------------------------------------------------ p. 180
add(180, "top of p. 180: page break 179/180 inside 'si n=dim(A)=dim(A′), | il existe un k′-homomorphisme local'",
    "p. 180 begins mid-sentence with 'il existe un k′-homomorphisme local' at the left margin; p. 179 ends 'En particulier, si n=dim(A)=dim(A′),' (crop c179_bottom.png)",
    "blank line after \\oldpage[IV-4]{180}", "marker",
    "\\oldpage[IV-4]{180}\n\nil existe un", "\\oldpage[IV-4]{180}\nil existe un",
    "BOUNDARY FIX (page break with p. 179). The marker is at the right place. In the current source the blank line BEFORE the marker is already gone (p. 179 fixes); this edit removes the one after it (\\oldpage ends with \\ignorespaces, which does not skip a \\par).")
add(180, "Corollaire (18.11.12), last line: 'soit une extension finie séparable du corps des fractions'",
    "'séparable' roman inside the italic statement (crop c180_l2.png)", "italic (environment)", "convention",
    "extension finie séparable du corps des fractions", "extension finie \\textup{séparable} du corps des fractions",
    "The statement began on p. 179; this edit lies in the p. 180 segment.", conv=6)
add(180, "proof of (18.11.12), l. 4: 'vu l'équivalence d)⇔c) de (18.11.10)'",
    "labels d), c) wholly italic, parentheses included (crop c180_dc.png)", "$d)\\Leftrightarrow c)$: italic letters, upright parentheses", "italics",
    "l'équivalence $d)\\Leftrightarrow c)$ de", "l'équivalence \\emph{d)}$\\Leftrightarrow$\\emph{c)} de", G88)
add(180, "proof of (18.11.12): 'soit une extension séparable de k′ (6.7.6)'",
    "'séparable' italic", "roman", "italics",
    "soit une extension séparable de $k'$ (6.7.6)", "soit une extension \\emph{séparable} de $k'$ (6.7.6)", G83)
add(180, "proof of (18.11.12): '(0, 19.8.9)'", "bold 0", "plain 0", "convention",
    "Or on sait (0, 19.8.9)", "Or on sait (\\textbf{0}, 19.8.9)", "", conv=2)
add(180, "proof of (18.11.12): 'K est donc une extension finie du corps des fractions K_1'",
    "'finie' italic", "roman", "italics",
    "$K$ est donc une extension finie du corps", "$K$ est donc une extension \\emph{finie} du corps", G83)
add(180, "proof of (18.11.12): 'de C, qui est séparable sur k'",
    "'séparable' italic", "roman", "italics",
    "de $C$, qui est séparable sur $k$", "de $C$, qui est \\emph{séparable} sur $k$", G83)
add(180, "proof of (18.11.12): '(0, 21.9.6.4)'", "bold 0", "plain 0", "convention",
    "(0, 21.9.6.4)", "(\\textbf{0}, 21.9.6.4)", "", conv=2)
add(180, "proof of (18.11.12): 'on peut donc écrire K⊗_k k^{p^{-∞}} = K⊗_{K_1}(K_1⊗_k k^{p^{-∞}}) et ...'",
    "the formula is set in the line, between 'écrire' and 'et' (page_180_s2.png)", "displayed formula", "formula",
    "on peut donc écrire\n\\[\n  K\\otimes_k k^{p^{-\\infty}}=K\\otimes_{K_1}(K_1\\otimes_k k^{p^{-\\infty}})\n\\]\net $K_1",
    "on peut donc écrire $K\\otimes_k k^{p^{-\\infty}}=K\\otimes_{K_1}(K_1\\otimes_k k^{p^{-\\infty}})$ et $K_1",
    "Display vs inline only; no connecting word lost.")
add(180, "proof of (18.11.12): 'est un corps, extension radicielle de K_1'",
    "'corps' italic", "roman", "italics",
    "est un corps, extension radicielle", "est un \\emph{corps}, extension radicielle", G83)
add(180, "proof of (18.11.12): 'donc un anneau artinien. La conclusion'",
    "'artinien' italic", "roman", "italics",
    "donc un anneau artinien. La conclusion", "donc un anneau \\emph{artinien}. La conclusion", G83)
add(180, "Lemme (18.11.12.1), label a)", "label 'a)' upright (crop c180_a.png)", "\\item[$a)$]: italic a", "convention",
    "\\item[$a)$] L'anneau", "\\item[\\textup{a)}] L'anneau", G16, conv=6)
add(180, "Lemme (18.11.12.1), label b)", "label 'b)' upright (crop c180_b.png)", "\\item[$b)$]: italic b", "convention",
    "\\item[$b)$] Il existe une extension $k'$ de $k$ de type fini", "\\item[\\textup{b)}] Il existe une extension $k'$ de $k$ de type fini", G16, conv=6)
add(180, "Lemme (18.11.12.1), label c)", "label 'c)' upright (crop c180_c.png)", "\\item[$c)$]: italic c", "convention",
    "\\item[$c)$] Il existe une extension finie radicielle", "\\item[\\textup{c)}] Il existe une extension finie radicielle", G16, conv=6)
add(180, "proof of (18.11.12.1): 'Montrons d'abord que c) entraîne a).'",
    "labels c), a) wholly italic", "$c)$, $a)$: italic letters, upright parentheses", "italics",
    "Montrons d'abord que $c)$ entraîne $a)$.", "Montrons d'abord que \\emph{c)} entraîne \\emph{a)}.", G88)
add(180, "proof of (18.11.12.1): 'comme il est égal à (A⊗_{k′}k^{p^{-∞}})/(𝔑⊗_{k′}k^{p^{-∞}}), on voit que'",
    "the formula is set in the line (crop c180_l3r.png)", "displayed formula", "formula",
    "et comme il est égal à\n\\[\n  (A\\otimes_{k'}k^{p^{-\\infty}})/(\\mathfrak N\\otimes_{k'}k^{p^{-\\infty}}),\n\\]\non voit que",
    "et comme il est égal à $(A\\otimes_{k'}k^{p^{-\\infty}})/(\\mathfrak N\\otimes_{k'}k^{p^{-\\infty}})$, on voit que",
    "Display vs inline only. The Fraktur N of this paragraph is right (crops c180_N1zoom.png, c180_l2r.png, c180_l3r.png, c180_l4.png).")
add(180, "proof of (18.11.12.1): 'Inversement, prouvons que a) entraîne c).'",
    "labels a), c) wholly italic", "$a)$, $c)$: italic letters, upright parentheses", "italics",
    "prouvons que $a)$ entraîne $c)$.", "prouvons que \\emph{a)} entraîne \\emph{c)}.", G88)
FR = ("In the 'Inversement' paragraph the print uses a Fraktur R for the nilradical (ℜ, ℜ_0: loop and leg of an R; crops c180_R3zoom.png, "
      "c180_l9.png, c180_l10zoom.png, c180_s4zoom.png), against the Fraktur N (𝔑) of the preceding paragraph (crop c180_N1zoom.png). "
      "The letter is introduced in this paragraph ('Soit ℜ le nilradical') and used consistently, so it is not recorded as a misprint.")
add(180, "proof of (18.11.12.1), 'Inversement' paragraph: 'Soit ℜ le nilradical de l'anneau local artinien B'",
    "Fraktur R", "\\mathfrak N", "symbol",
    "Soit $\\mathfrak N$ le nilradical", "Soit $\\mathfrak R$ le nilradical", FR + " Edit 1 of 5.")
add(180, "proof of (18.11.12.1): 'de la forme y_i=Σ_j x_ij⊗ξ_ij, où x_ij∈K, ξ_ij∈k^{p^{-∞}}. Soient'",
    "formulas set in the line, joined by 'où' (page_180_s3.png)", "one display joining them with \\qquad and \\quad; 'où' missing", "missing",
    "de la forme\n\\[\n  y_i=\\sum_j x_{ij}\\otimes\\xi_{ij},\\qquad x_{ij}\\in K,\\quad \\xi_{ij}\\in k^{p^{-\\infty}}.\n\\]\nSoient $k'$",
    "de la forme $y_i=\\sum_j x_{ij}\\otimes\\xi_{ij}$, où $x_{ij}\\in K$, $\\xi_{ij}\\in k^{p^{-\\infty}}$. Soient $k'$",
    "Inline as printed, with the lost connecting word (GLOBAL_ISSUES 51 pattern).")
add(180, "'Inversement' paragraph: 'ℜ_0 l'idéal de B_0'", "Fraktur R", "\\mathfrak N_0", "symbol",
    "$\\mathfrak N_0$ l'idéal de", "$\\mathfrak R_0$ l'idéal de", "Edit 2 of 5 (see edit 1).")
add(180, "'Inversement' paragraph: 'on a ℜ_0⊗_{k′}k^{p^{-∞}}=ℜ, et par suite ℜ∩B_0=ℜ_0, ℜ_0 contient'", "Fraktur R (4 times)", "\\mathfrak N (4 times)", "symbol",
    "on a $\\mathfrak N_0\\otimes_{k'}k^{p^{-\\infty}}=\\mathfrak N$, et par suite $\\mathfrak N\\cap B_0=\\mathfrak N_0$, $\\mathfrak N_0$ contient",
    "on a $\\mathfrak R_0\\otimes_{k'}k^{p^{-\\infty}}=\\mathfrak R$, et par suite $\\mathfrak R\\cap B_0=\\mathfrak R_0$, $\\mathfrak R_0$ contient",
    "Edit 3 of 5 (see edit 1).")
add(180, "'Inversement' paragraph: 'Comme B/ℜ=(B_0/ℜ_0)⊗_{k′}k^{p^{-∞}}'", "Fraktur R (twice)", "\\mathfrak N (twice)", "symbol",
    "Comme $B/\\mathfrak N=(B_0/\\mathfrak N_0)\\otimes", "Comme $B/\\mathfrak R=(B_0/\\mathfrak R_0)\\otimes", "Edit 4 of 5 (see edit 1).")
add(180, "'Inversement' paragraph: 'on en conclut que B_0/ℜ_0=(K⊗_k k′)_red'", "Fraktur R", "\\mathfrak N_0", "symbol",
    "que $B_0/\\mathfrak N_0=(K\\otimes_k k')", "que $B_0/\\mathfrak R_0=(K\\otimes_k k')", "Edit 5 of 5 (see edit 1).")
add(180, "last paragraph: 'Il est clair que c) entraîne b). Inversement, supposons b) vérifiée'",
    "labels wholly italic (page_180_s4.png)", "$c)$, $b)$, $b)$: italic letters, upright parentheses", "italics",
    "Il est clair que $c)$ entraîne $b)$. Inversement, supposons $b)$ vérifiée",
    "Il est clair que \\emph{c)} entraîne \\emph{b)}. Inversement, supposons \\emph{b)} vérifiée", G88)
add(180, "last paragraph: 'Appliquant l'équivalence de a) et c)'",
    "labels wholly italic", "$a)$, $c)$: italic letters, upright parentheses", "italics",
    "l'équivalence de $a)$ et $c)$ à l'extension", "l'équivalence de \\emph{a)} et \\emph{c)} à l'extension", G88)
add(180, "end of p. 180: page break 180/181 inside 'mais cet anneau est égal | à K⊗_k k_1^{p^{-∞}} = ...'",
    "p. 181 begins mid-sentence with 'à K⊗_k k_1^{p^{-∞}}' at the left margin", "blank lines before and after \\oldpage[IV-4]{181}", "marker",
    "mais cet anneau est égal\n\n", "mais cet anneau est égal\n",
    "The marker is at the right place. Part 1 of 2: the first p. 181 finding removes the blank line after \\oldpage[IV-4]{181}; apply both (\\oldpage ends with \\ignorespaces, which does not skip a \\par).")

# ------------------------------------------------------------------ p. 181
add(181, "top of p. 181: page break 180/181", "mid-sentence continuation 'à K⊗_k k_1^{p^{-∞}} = ...'",
    "blank line after \\oldpage[IV-4]{181}", "marker",
    "\\oldpage[IV-4]{181}\n\n", "\\oldpage[IV-4]{181}\n",
    "Part 2 of 2 with the last p. 180 finding; both blank lines must go. Independent of the next finding (adjacent text, no overlap).")
add(181, "l. 1: 'à K⊗_k k_1^{p^{-∞}} = (K⊗_k k^{p^{-∞}})⊗_{k^{p^{-∞}}} k_1^{p^{-∞}}, donc'",
    "the formula is set in the line (page_181_s1.png)", "displayed formula", "formula",
    "à\n\\[\n  K\\otimes_k k_1^{p^{-\\infty}}=(K\\otimes_k k^{p^{-\\infty}})\\otimes_{k^{p^{-\\infty}}}k_1^{p^{-\\infty}},\n\\]\ndonc",
    "à $K\\otimes_k k_1^{p^{-\\infty}}=(K\\otimes_k k^{p^{-\\infty}})\\otimes_{k^{p^{-\\infty}}}k_1^{p^{-\\infty}}$, donc",
    "Display vs inline only.")
add(181, "l. 2: 'on a ainsi prouvé que b) entraîne a),'",
    "labels wholly italic", "$b)$, $a)$: italic letters, upright parentheses", "italics",
    "prouvé que $b)$ entraîne $a)$,", "prouvé que \\emph{b)} entraîne \\emph{a)},", G88)
add(181, "heading 18.12: '... (généralisations de résultats antérieurs).'", "final full stop", "no full stop", "punctuation",
    "(généralisations de résultats antérieurs)}", "(généralisations de résultats antérieurs).}",
    "GLOBAL_ISSUES 43/58; 18.10 was page-fixed the same way (p. 157).")
add(181, "proof of (18.12.1): '(II, 6.1.5)'", "bold II", "plain II", "convention",
    "de $j'$ (II, 6.1.5)", "de $j'$ (\\textbf{II}, 6.1.5)", "", conv=2)
add(181, "proof of (18.12.1): '(II, 6.1.10)'", "bold II", "plain II", "convention",
    "dans $X'$ (II, 6.1.10)", "dans $X'$ (\\textbf{II}, 6.1.10)", "", conv=2)
add(181, "proof of (18.12.1): 'f est donc séparé, et on peut'", "'séparé' italic (crop c181_s2l6b.png)", "roman", "italics",
    "$f$ est donc séparé, et on peut", "$f$ est donc \\emph{séparé}, et on peut", G83)
add(181, "proof of (18.12.1): 'on en déduit que f^{-1}(y) = ⋂_λ f_λ^{-1}(y), et comme'",
    "the formula is set in the line (page_181_s2.png)", "displayed formula", "formula",
    "on en déduit que\n\\[\n  f^{-1}(y)=\\bigcap_\\lambda f_\\lambda^{-1}(y),\n\\]\net comme",
    "on en déduit que $f^{-1}(y)=\\bigcap_\\lambda f_\\lambda^{-1}(y)$, et comme", "Display vs inline only.")
add(181, "proof of (18.12.1): 'fermés dans l'espace noethérien Z_y'", "'noethérien' italic (crop c181_s2l11b.png)", "roman", "italics",
    "dans l'espace noethérien", "dans l'espace \\emph{noethérien}", G83)
add(181, "proof of (18.12.1): 'Z_y = Spec(k(y)[T_1, ..., T_r])'", "bold italic k (crop c181_s2l12a.png)", "plain k", "convention",
    "\\Spec(k(y)[T_1,\\ldots,T_r])", "\\Spec(\\boldsymbol{k}(y)[T_1,\\ldots,T_r])", "", conv=1)
add(181, "proof of (18.12.1): 'ramené au cas où f est de présentation finie.'", "'présentation finie' italic", "roman", "italics",
    "ramené au cas où $f$ est de présentation finie.", "ramené au cas où $f$ est de \\emph{présentation finie}.", G83)
add(181, "proof of (18.12.1): '... de présentation finie. Notons en outre que'",
    "'Notons en outre' continues the same line: no paragraph break (page_181_s2.png/s3.png)", "blank line before 'Notons en outre' (new paragraph)", "other",
    "\n\nNotons en outre que", "\nNotons en outre que", "Independent of the previous finding (no overlap).")
add(181, "proof of (18.12.1): 'se borner au cas où f est quasi-fini.'", "'quasi-fini' italic", "roman", "italics",
    "se borner au cas où $f$ est quasi-fini.", "se borner au cas où $f$ est \\emph{quasi-fini}.", G83)
add(181, "proof of (18.12.1): 'qui est fini sur Y″ (18.5.11, c))'", "'fini' italic; label c) wholly italic, then an upright parenthesis (crop c181_c.png)",
    "roman 'fini'; 'c))' upright", "italics",
    "qui est fini sur $Y''$ (18.5.11, c))", "qui est \\emph{fini} sur $Y''$ (18.5.11, \\emph{c)})", G83 + " " + G88)
add(181, "proof of (18.12.1): 'de O_{Y,y}-algèbres étales ((18.6.1)'", "'étales' italic (crop c181_etales.png)", "roman", "italics",
    "-algèbres étales ((18.6.1)", "-algèbres \\emph{étales} ((18.6.1)", G83)
add(181, "proof of (18.12.1): '((18.6.1) et (8.1.2, a))).'",
    "three closing parentheses after the label: 'a)' wholly italic, then two upright ones closing (8.1.2, ...) and ((18.6.1) ... (crop c181_etales.png)",
    "'(8.1.2, a)).': one closing parenthesis missing; label upright", "missing",
    "(8.1.2, a)).", "(8.1.2, \\emph{a)})).", "The TeX loses the parenthesis that closes '((18.6.1) et ...'. The label is set italic in the same edit (GLOBAL_ISSUES 88).")
add(181, "proof of (18.12.1): 'il résulte encore de (8.1.2, a)) et de (17.7.8)'", "label a) wholly italic, then an upright parenthesis (crop c181_resulte.png)",
    "'a))' upright", "italics",
    "encore de (8.1.2, a)) et de", "encore de (8.1.2, \\emph{a)}) et de", G88)
add(181, "proof of (18.12.1), last line: 'V′_α est fini sur Y′_α. C.Q.F.D.'", "'fini' italic", "roman", "italics",
    "$V'_\\alpha$ est fini sur $Y'_\\alpha$. C.Q.F.D.", "$V'_\\alpha$ est \\emph{fini} sur $Y'_\\alpha$. C.Q.F.D.", G83)
add(181, "Remarque (18.12.2): 'tel en plus que si y′=f′(X′), l'homomorphisme'",
    "capital X′ (crop c181_yfX.png)", "$y'=f'(X')$ (keeps the printed reading)", "misprint_in_print",
    None, None, "y′ is the image of the point x′ of (18.12.1); f′(X′) is a set. The TeX keeps the printed reading.",
    conf="medium", corrected="$y'=f'(x')$", nofix=True)
add(181, "Remarque (18.12.2): 'l'homomorphisme k(y)→k(y′)'", "bold italic k (twice; crop c181_yfX.png)", "plain k", "convention",
    "l'homomorphisme $k(y)\\to k(y')$", "l'homomorphisme $\\boldsymbol{k}(y)\\to\\boldsymbol{k}(y')$", "", conv=1)
add(181, "Remarque (18.12.2): 'soit bijectif.'", "'bijectif' italic (crop c181_yfX.png)", "no \\emph (the remark body is italic only through the environment)", "italics",
    "(y')$ soit bijectif.", "(y')$ soit \\emph{bijectif}.", "Emphasis judged as if the remark body were roman (document-wide remark font). Works before or after the previous finding (bold k): the changed characters do not overlap.")
add(181, "Corollaire (18.12.3): 'tel que k(y′)=k(y)'", "bold italic k (twice)", "plain k", "convention",
    "tel que $k(y')=k(y)$, et une décomposition", "tel que $\\boldsymbol{k}(y')=\\boldsymbol{k}(y)$, et une décomposition", "", conv=1)
add(181, "Corollaire (18.12.3): 'sous-préschémas X′_1, X′_2 induits sur des ouverts'", "no comma after X′_2 (crop c181_X2.png)",
    "comma after $X'_2$", "punctuation",
    "$X'_2$, induits sur des ouverts", "$X'_2$ induits sur des ouverts", "")
add(181, "Corollaire (18.12.3), last line: 'X′_2∩f′^{-1}(y′))=ø.'", "two closing parentheses after y′ (crops c181_empty.png, c181_yparen.png)",
    "$X'_2\\cap f'^{-1}(y')=\\varnothing$ (silent correction)", "misprint_in_print",
    "que l'on ait $X'_2\\cap f'^{-1}(y')=\\varnothing$.", "que l'on ait $X'_2\\cap f'^{-1}(y'))=\\varnothing$.",
    "Extra parenthesis in the print. The TeX silently corrected it; this edit restores the printed reading.",
    corrected="que l'on ait $X'_2\\cap f'^{-1}(y')=\\varnothing$.")
add(181, "proof of (18.12.3): 'tel que k(y_1)=k(y) et si l'on pose'", "bold italic k (twice)", "plain k", "convention",
    "tel que $k(y_1)=k(y)$ et si l'on pose", "tel que $\\boldsymbol{k}(y_1)=\\boldsymbol{k}(y)$ et si l'on pose", "", conv=1)
add(181, "proof of (18.12.3): 'S_1=X×_Y Y_1, f_1=f_(S_1) : S_1 → Y_1'", "subscript (S_1) (crop c181_fS1.png)",
    "$f_1=f_{(S_1)}$ (keeps the printed reading)", "misprint_in_print", None, None,
    "f_1: S_1 = X×_Y Y_1 → Y_1 is the base change of f by Y_1 → Y, written f_(Y_1) in EGA's notation (cf. f′=f_(Y′) in (18.12.1), (18.12.3)). The TeX keeps the printed reading.",
    conf="medium", corrected="$f_1=f_{(Y_1)}$", nofix=True)
add(181, "end of p. 181: the marker \\oldpage[IV-4]{182} stands too late",
    "printed p. 181 ends '... il existe un point x_1 de f_1^{-1}(y_1)'; p. 182 begins 'tel que S_1 soit somme de deux ouverts V_1, X_1, V_1 étant fini sur Y_1 et un voisinage de x_1. En vertu de la relation ...' in one paragraph (page_181_s4.png, page_182_s1.png)",
    "the clause 'tel que $S_1$ soit somme ... de $x_1$.' and a paragraph break stand before \\oldpage[IV-4]{182}", "marker",
    "de $f_1^{-1}(y_1)$ tel que $S_1$ soit somme de deux ouverts $V_1$, $X_1$, $V_1$ étant fini sur $Y_1$ et un voisinage de $x_1$.\n\n",
    "de $f_1^{-1}(y_1)$\n",
    "Two-part move (the text moves, not the marker, so each edit stays in its own page segment). Part 1 of 2: the first p. 182 finding puts the clause after the marker and joins it to 'En vertu de la relation' (no paragraph break in the print). Apply both.")

# ------------------------------------------------------------------ p. 182
add(182, "top of p. 182: the clause 'tel que S_1 soit somme ... de x_1.' begins the page; 'En vertu de la relation' continues the same paragraph",
    "p. 182 l. 1: 'tel que S_1 soit somme de deux ouverts V_1, X_1, V_1 étant fini sur Y_1 et un voisinage de x_1. En vertu de la relation' (page_182_s1.png)",
    "the clause is at the end of the p. 181 segment; blank line after \\oldpage[IV-4]{182}", "marker",
    "\\oldpage[IV-4]{182}\n\nEn vertu de la relation",
    "\\oldpage[IV-4]{182}\ntel que $S_1$ soit somme de deux ouverts $V_1$, $X_1$, $V_1$ étant fini sur $Y_1$ et un voisinage de $x_1$. En vertu de la relation",
    "Part 2 of 2 with the last p. 181 finding (which removes the clause and the blank line from the end of the p. 181 segment).")
add(182, "l. 2: 'En vertu de la relation k(y_1)=k(y), la fibre'", "bold italic k (twice)", "plain k", "convention",
    "$k(y_1)=k(y)$, la fibre", "$\\boldsymbol{k}(y_1)=\\boldsymbol{k}(y)$, la fibre", "Independent of the previous finding (no overlap).", conv=1)
add(182, "l. 2: 'fini, discret et a n—1 points'", "long dash for the minus sign (crop c182_n1.png)", "-", "convention",
    "a $n-1$ points", "a $n\\setmin 1$ points", "Long dash for subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.", conv=7)
add(182, "l. 4: 'tel que k(y′)=k(y_1), et, si'", "bold italic k (twice)", "plain k", "convention",
    "tel que $k(y')=k(y_1)$, et, si", "tel que $\\boldsymbol{k}(y')=\\boldsymbol{k}(y_1)$, et, si", "", conv=1)
add(182, "proof of (18.12.4): 'à un point quelconque y de Y'", "'quelconque' italic", "roman", "italics",
    "un point quelconque $y$ de $Y$", "un point \\emph{quelconque} $y$ de $Y$", G83)
add(182, "proof of (18.12.4): 'un ouvert de Y en vertu de (11.3.1) puisque'",
    "(11.3.1): light old-style figures and full stops, no bold numeral, no comma (crop c182_1131.png)", "(II, 3.1)", "number",
    "en vertu de (II, 3.1) puisque", "en vertu de (11.3.1) puisque",
    "EGA IV's own (11.3.1) (flat morphisms locally of finite presentation are open), misread as an EGA II reference (GLOBAL_ISSUES 78 pattern).")
add(182, "Remarque (18.12.5): 'pour tout morphisme étale Y′→Y'", "'étale' italic (crop c182_etale.png)", "no \\emph", "italics",
    "pour tout morphisme étale $Y'\\to Y$.", "pour tout morphisme \\emph{étale} $Y'\\to Y$.",
    "Emphasis judged as if the remark body were roman (document-wide remark font).")
add(182, "Corollaire (18.12.6), label a)", "label 'a)' upright (crop c182_ab.png)", "\\item[$a)$]: italic a", "convention",
    "\\item[$a)$] $f$ est une immersion fermée.", "\\item[\\textup{a)}] $f$ est une immersion fermée.", G16, conv=6)
add(182, "Corollaire (18.12.6), label b)", "label 'b)' upright (crop c182_ab.png)", "\\item[$b)$]: italic b", "convention",
    "\\item[$b)$] $f$ est un monomorphisme propre.", "\\item[\\textup{b)}] $f$ est un monomorphisme propre.", G16, conv=6)
add(182, "Corollaire (18.12.6), label c)", "label 'c)' upright (page_182_s2.png)", "\\item[$c)$]: italic c", "convention",
    "\\item[$c)$] $f$ est propre et", "\\item[\\textup{c)}] $f$ est propre et", G16, conv=6)
add(182, "Corollaire (18.12.6) c): 'le k(y)-préschéma ... réduit sur k(y) (c'est-à-dire vide ou k(y)-isomorphe à Spec(k(y'", "bold italic k (4 times; crop c182_c2.png)", "plain k", "convention",
    "le $k(y)$-préschéma $X_y=f^{-1}(y)$ est radiciel et géométriquement réduit sur $k(y)$ (c'est-à-dire vide ou $k(y)$-isomorphe à $\\Spec(k(y",
    "le $\\boldsymbol{k}(y)$-préschéma $X_y=f^{-1}(y)$ est radiciel et géométriquement réduit sur $\\boldsymbol{k}(y)$ (c'est-à-dire vide ou $\\boldsymbol{k}(y)$-isomorphe à $\\Spec(\\boldsymbol{k}(y",
    "Apply BEFORE the next finding (misprint at the end of the same clause); the two edits do not overlap.", conv=1)
add(182, "Corollaire (18.12.6) c), end: 'à Spec(k(y)).'", "only two closing parentheses: the one opened before 'c'est-à-dire' is not closed (crops c182_close.png, c182_c2.png)",
    "'$\\Spec(k(y))$).': the third parenthesis added (silent correction)", "misprint_in_print",
    "(y))$).\n\\end{enumerate}", "(y))$.\n\\end{enumerate}",
    "Apply after the previous finding (convention 1); its 'old' is the text after that edit. In Proposition (18.12.7) the same clause has all three parentheses (crop c182_close2.png).",
    corrected="(y))$).\n\\end{enumerate}")
add(182, "Proposition (18.12.7): 'un k(y)-préschéma radiciel et géométriquement réduit sur k(y) (c'est-à-dire vide ou k(y)-isomorphe à Spec(k(y)))'",
    "bold italic k (4 times; crop c182_p7.png)", "plain k", "convention",
    "soit un $k(y)$-préschéma radiciel et géométriquement réduit sur $k(y)$ (c'est-à-dire vide ou $k(y)$-isomorphe à $\\Spec(k(y))$)",
    "soit un $\\boldsymbol{k}(y)$-préschéma radiciel et géométriquement réduit sur $\\boldsymbol{k}(y)$ (c'est-à-dire vide ou $\\boldsymbol{k}(y)$-isomorphe à $\\Spec(\\boldsymbol{k}(y))$)",
    "", conv=1)
add(182, "proof of (18.12.7): 'qu'on peut supposer f affine, donc séparé'", "'affine' italic", "roman", "italics",
    "qu'on peut supposer $f$ affine, donc séparé", "qu'on peut supposer $f$ \\emph{affine}, donc séparé", G83)
add(182, "proof of (18.12.7.1): '(II, 1.2.5)'", "bold II", "plain II", "convention",
    "(II, 1.2.5).", "(\\textbf{II}, 1.2.5).", "", conv=2)
add(182, "proof of (18.12.7): 'soit un morphisme fini; comme on peut supposer'", "'fini' italic", "roman", "italics",
    "soit un morphisme fini; comme", "soit un morphisme \\emph{fini}; comme", G83)
add(182, "proof of (18.12.7): 'de type fini, donc propre, et il suffit'", "'propre' italic (crop c182_qf2.png)", "roman", "italics",
    "de type fini, donc propre, et il suffit", "de type fini, donc \\emph{propre}, et il suffit", G83)
add(182, "proof of (18.12.7): 'soit un morphisme quasi-fini (18.12.4)'", "'quasi-fini' italic (crop c182_qf2.png); the later 'soit quasi-fini (13.1.4)' is roman",
    "roman", "italics",
    "soit un morphisme quasi-fini (18.12.4)", "soit un morphisme \\emph{quasi-fini} (18.12.4)", G83)
add(182, "proof of (18.12.8): 'Les conditions sont nécessaires (II, 6.1.10)'", "bold II", "plain II", "convention",
    "sont nécessaires (II, 6.1.10)", "sont nécessaires (\\textbf{II}, 6.1.10)", "", conv=2)
add(182, "proof of (18.12.8): 'entier sur A (II, 6.1.1)'", "bold II", "plain II", "convention",
    "entier sur $A$ (II, 6.1.1)", "entier sur $A$ (\\textbf{II}, 6.1.1)", "", conv=2)
add(182, "proof of (18.12.8): 'se factorise en X →g X′ →h Y, où h'", "the formula is set in the line (page_182_s4.png)", "displayed formula", "formula",
    "se factorise en\n\\[\n  X\\xrightarrow{g}X'\\xrightarrow{h}Y,\n\\]\noù $h$", "se factorise en $X\\xrightarrow{g}X'\\xrightarrow{h}Y$, où $h$",
    "Display vs inline only.")
add(182, "proof of (18.12.8): 'g est dominant puisque'", "'dominant' italic", "roman", "italics",
    "$g$ est dominant puisque", "$g$ est \\emph{dominant} puisque", G83)
add(182, "proof of (18.12.8): 'injectif (I, 1.2.7)'", "bold I and comma: a real EGA I reference (crop c182_I127.png)", "plain I", "convention",
    "injectif (I, 1.2.7)", "injectif (\\textbf{I}, 1.2.7)", "", conv=2)
add(182, "proof of (18.12.8), last line: '(II, 5.4.3 et'", "bold II", "plain II", "convention",
    "fermé (II, 5.4.3 et", "fermé (\\textbf{II}, 5.4.3 et", "Independent of the next finding (the changed characters do not overlap).", conv=2)
add(182, "end of p. 182: page break 182/183 inside the reference '(II, 5.4.3 et | 5.4.9)'",
    "p. 183 begins '5.4.9), donc surjectif' at the left margin", "blank lines before and after \\oldpage[IV-4]{183}", "marker",
    "5.4.3 et\n\n", "5.4.3 et\n",
    "The marker is at the right place. Part 1 of 2: the first p. 183 finding removes the blank line after \\oldpage[IV-4]{183}; apply both.")

# ------------------------------------------------------------------ p. 183
add(183, "top of p. 183: page break 182/183", "mid-reference continuation '5.4.9), donc'", "blank line after \\oldpage[IV-4]{183}", "marker",
    "\\oldpage[IV-4]{183}\n\n5.4.9)", "\\oldpage[IV-4]{183}\n5.4.9)", "Part 2 of 2 with the last p. 182 finding; both blank lines must go.")
add(183, "l. 1: 'donc surjectif puisqu'il est dominant'", "'surjectif' italic", "roman", "italics",
    "donc surjectif puisqu'il", "donc \\emph{surjectif} puisqu'il", G83)
add(183, "l. 1: 'on en conclut (II, 5.4.3 et 5.4.9)'", "bold II", "plain II", "convention",
    "on en conclut (II, 5.4.3 et 5.4.9)", "on en conclut (\\textbf{II}, 5.4.3 et 5.4.9)", "", conv=2)
add(183, "l. 2: 'donc propre puisqu'il est de type fini et séparé'", "'propre' italic", "roman", "italics",
    "donc propre puisqu'il est de type fini", "donc \\emph{propre} puisqu'il est de type fini", G83)
add(183, "l. 2: 'le morphisme h^{-1}(y) → Spec(k(y))'", "bold italic k", "plain k", "convention",
    "$h^{-1}(y)\\to\\Spec(k(y))$", "$h^{-1}(y)\\to\\Spec(\\boldsymbol{k}(y))$", "", conv=1)
add(183, "l. 3: 'est propre et affine, donc fini (III, 4.4.2)'", "'fini' italic", "roman", "italics",
    "est propre et affine, donc fini", "est propre et affine, donc \\emph{fini}", G83)
add(183, "l. 3: '(III, 4.4.2)'", "bold III", "plain III", "convention",
    "(III, 4.4.2)", "(\\textbf{III}, 4.4.2)", "", conv=2)
add(183, "l. 3: 'autrement dit h est quasi-fini;'", "'quasi-fini' italic", "roman", "italics",
    "autrement dit $h$ est quasi-fini;", "autrement dit $h$ est \\emph{quasi-fini};", G83)
add(183, "l. 4: 'que h est fini, ce qui prouve'", "'fini' italic", "roman", "italics",
    "que $h$ est fini, ce qui prouve", "que $h$ est \\emph{fini}, ce qui prouve", G83)
add(183, "Remarque (18.12.9): 'f^{-1}(y) → Spec(k(y))'", "bold italic k", "plain k", "convention",
    "$f^{-1}(y)\\to\\Spec(k(y))$ déduit de $f$", "$f^{-1}(y)\\to\\Spec(\\boldsymbol{k}(y))$ déduit de $f$", "", conv=1)
add(183, "Corollaire (18.12.11): '(resp. un morphisme localement de type fini).'",
    "'(resp.' and the closing parenthesis upright, 'un morphisme localement de type fini' italic (crop c183_resp1.png)", "all italic (environment)", "convention",
    "(resp. un morphisme localement de type fini).", "\\textup{(resp.} un morphisme localement de type fini\\textup{)}.",
    "Same form as the earlier page fixes of '(resp. ...)' in italic statements.", conv=6)
add(183, "Corollaire (18.12.11): 'homéomorphisme universel (2.4.2)'", "reference upright (crop c183_resp2a.png)", "italic (environment)", "convention",
    "universel (2.4.2), il faut", "universel \\textup{(2.4.2)}, il faut", "", conv=6)
add(183, "Corollaire (18.12.11): 'entier (resp. fini), radiciel'", "'(resp.' and ')' upright, 'fini' italic (crop c183_resp2b.png)", "all italic (environment)", "convention",
    "entier (resp. fini), radiciel", "entier \\textup{(resp.} fini\\textup{)}, radiciel", "", conv=6)
add(183, "proof of (18.12.12): 'soit Z=Spec(𝒜) (II, 1.3.1)'", "bold II", "plain II", "convention",
    "(II, 1.3.1)", "(\\textbf{II}, 1.3.1)", "", conv=2)
add(183, "proof of (18.12.12): 'se factorise canoniquement en X →g Z →h Y, h étant affine'", "the formula is set in the line (page_183_s2.png)",
    "displayed formula", "formula",
    "se factorise canoniquement en\n\\[\n  X\\xrightarrow{g}Z\\xrightarrow{h}Y,\n\\]\n$h$ étant affine",
    "se factorise canoniquement en $X\\xrightarrow{g}Z\\xrightarrow{h}Y$, $h$ étant affine", "Display vs inline only.")
add(183, "proof of (18.12.12): 'l'automorphisme identique de 𝒜 (II, 1.2.7);'", "bold II", "plain II", "convention",
    "(II, 1.2.7); il suffira", "(\\textbf{II}, 1.2.7); il suffira", "", conv=2)
add(183, "proof of (18.12.12): 'g est une immersion ouverte, ou,'", "'immersion ouverte' italic (crop c183_immouv.png)", "roman", "italics",
    "$g$ est une immersion ouverte, ou,", "$g$ est une \\emph{immersion ouverte}, ou,", G83)
add(183, "proof of (18.12.12): 'que g est étale et radiciel. Il suffira'", "'étale' and 'radiciel' italic, 'et' roman", "roman", "italics",
    "que $g$ est étale et radiciel. Il suffira", "que $g$ est \\emph{étale} et \\emph{radiciel}. Il suffira", G83)
add(183, "proof of (18.12.12): 'à un isomorphisme canonique près, f′_*(O_X′)=𝒜⊗_{O_Y}O_Y′=𝒜′ (2.3.1)'", "the formula is set in the line (page_183_s2.png)",
    "displayed formula", "formula",
    "à un isomorphisme canonique près,\n\\[\n  f'_*(\\sh{O}_{X'})=\\mathscr A\\otimes_{\\sh{O}_Y}\\sh{O}_{Y'}=\\mathscr A'\n\\]\n(2.3.1)",
    "à un isomorphisme canonique près, $f'_*(\\sh{O}_{X'})=\\mathscr A\\otimes_{\\sh{O}_Y}\\sh{O}_{Y'}=\\mathscr A'$ (2.3.1)", "Display vs inline only.")
add(183, "proof of (18.12.12): 'dans la factorisation canonique X′ →g′ Z′ →h′ Y′ de f′'", "the formula is set in the line (page_183_s2.png)",
    "displayed formula", "formula",
    "la factorisation canonique\n\\[\n  X'\\xrightarrow{g'}Z'\\xrightarrow{h'}Y'\n\\]\nde $f'$",
    "la factorisation canonique $X'\\xrightarrow{g'}Z'\\xrightarrow{h'}Y'$ de $f'$", "Display vs inline only.")
add(183, "proof of (18.12.12): 'de f′ (II, 1.2.7), on a h′=h_(Y′)'", "bold II", "plain II", "convention",
    "(II, 1.2.7), on a $h'", "(\\textbf{II}, 1.2.7), on a $h'", "Independent of the previous finding (no overlap).", conv=2)
add(183, "proof of (18.12.12): 'et g′=g_(Y′.' at the end of the line", "no closing parenthesis after Y′; a raised full stop follows (crops c183_gY.png, c183_gYz.png; h_(Y′) just before has it)",
    "$g'=g_{(Y')}$. (silent correction)", "misprint_in_print",
    "$g'=g_{(Y')}$.", "$g'=g_{(Y'}$.",
    "Missing parenthesis in the print. The TeX silently corrected it; this edit restores the printed reading (the full stop's raised position is not reproduced).",
    conf="medium", corrected="$g'=g_{(Y')}$.")
add(183, "proof of (18.12.12): 'en produit direct des deux O_Y-Algèbres quasi-cohérentes 𝒜′_1, 𝒜′_2'", "O_Y without prime (crop c183_OYz.png)",
    "$\\sh{O}_{Y'}$ (silent correction)", "misprint_in_print",
    "des deux $\\sh{O}_{Y'}$-Algèbres", "des deux $\\sh{O}_Y$-Algèbres",
    "𝒜′ = 𝒜⊗O_Y′ and its factors live on Y′ (Z′_i = Spec(𝒜′_i) over Y′), so O_Y′ is meant. The TeX silently corrected the print; this edit restores the printed reading.",
    conf="medium", corrected="des deux $\\sh{O}_{Y'}$-Algèbres")
add(183, "proof of (18.12.12): 'g′_1=g′|X′_1 est un isomorphisme de X′_1 sur Z′_1'", "'isomorphisme' italic, 'de' roman (crop c183_iso.png)", "roman", "italics",
    "est un isomorphisme de $X'_1$ sur $Z'_1$", "est un \\emph{isomorphisme} de $X'_1$ sur $Z'_1$", G83)
add(183, "proof of (18.12.12): 'on voit que g′ est étale et radiciel en chaque point'", "'étale' and 'radiciel' italic (crop c183_etrad.png)", "roman", "italics",
    "on voit que $g'$ est étale et radiciel en chaque point", "on voit que $g'$ est \\emph{étale} et \\emph{radiciel} en chaque point", G83)
add(183, "proof of (18.12.12): '(I, 3.5.2)'", "bold I and comma: a real EGA I reference (crop c183_I352.png)", "plain I", "convention",
    "(I, 3.5.2)", "(\\textbf{I}, 3.5.2)", "", conv=2)
add(183, "proof of (18.12.12): 'le morphisme g′_y′ : f′^{-1}(y′) → h′^{-1}(y′) déduit de g′'", "the formula is set in the line (page_183_s3.png)",
    "displayed formula", "formula",
    "le morphisme\n\\[\n  g'_{y'}:f'^{-1}(y')\\longrightarrow h'^{-1}(y')\n\\]\ndéduit de $g'$",
    "le morphisme $g'_{y'}:f'^{-1}(y')\\longrightarrow h'^{-1}(y')$ déduit de $g'$", "Display vs inline only.")
add(183, "proof of (18.12.12): 'comme k(y′)=k(y), le morphisme g_y'", "bold italic k (twice)", "plain k", "convention",
    "comme $k(y')=k(y)$, le morphisme", "comme $\\boldsymbol{k}(y')=\\boldsymbol{k}(y)$, le morphisme", "", conv=1)
add(183, "proof of (18.12.13): 'que f est quasi-affine, donc quasi-projectif'", "'quasi-affine' italic", "roman", "italics",
    "que $f$ est quasi-affine, donc", "que $f$ est \\emph{quasi-affine}, donc", G83)
add(183, "proof of (18.12.13): 'une propriété locale sur Y'", "'locale' italic", "roman", "italics",
    "une propriété locale sur $Y$", "une propriété \\emph{locale} sur $Y$", G83)
add(183, "proof of (18.12.13): 'lorsque Y est affine.'", "'affine' italic", "roman", "italics",
    "lorsque $Y$ est affine.", "lorsque $Y$ est \\emph{affine}.", G83)
add(183, "Remarque (18.12.14): 'se sert du « Main theorem » sous sa forme locale'", "lower-case t: 'theorem' (crop c183_mt.png); the heading of (18.12.13) has 'Theorem'",
    "« Main Theorem »", "word",
    "se sert du « Main Theorem » sous", "se sert du « Main theorem » sous", "")
add(183, "Remarque (18.12.14): 'quasi-cohérente, fermeture intégrale de O_Y dans 𝒜'", "'fermeture intégrale' italic", "no \\emph", "italics",
    "quasi-cohérente, fermeture intégrale de", "quasi-cohérente, \\emph{fermeture intégrale} de",
    "Emphasis judged as if the remark body were roman (document-wide remark font).")
add(183, "Remarque (18.12.14): '(II, 6.3.2)'", "bold II", "plain II", "convention",
    "(II, 6.3.2)", "(\\textbf{II}, 6.3.2)", "", conv=2)
add(183, "Remarque (18.12.14): 'C′ étant une C-algèbre étale (17.3.2)'", "'étale' italic", "no \\emph", "italics",
    "une $C$-algèbre étale (17.3.2)", "une $C$-algèbre \\emph{étale} (17.3.2)", "Emphasis judged as if the remark body were roman.")
add(183, "Remarque (18.12.14): 'isomorphe au produit A′_1×A′_2'", "'produit' italic", "no \\emph", "italics",
    "isomorphe au produit $A'_1", "isomorphe au \\emph{produit} $A'_1", "Emphasis judged as if the remark body were roman.")
add(183, "Remarque (18.12.14): 'une C′-algèbre finie. Il suffira'", "'finie' italic", "no \\emph", "italics",
    "une $C'$-algèbre finie. Il suffira", "une $C'$-algèbre \\emph{finie}. Il suffira", "Emphasis judged as if the remark body were roman.")
add(183, "end of p. 183: page break 183/184 inside 'B′=B⊗_C C′, qui | s'identifie'", "p. 184 begins mid-sentence with 's'identifie par platitude'",
    "blank lines before and after \\oldpage[IV-4]{184}", "marker",
    "$B'=B\\otimes_C C'$, qui\n\n", "$B'=B\\otimes_C C'$, qui\n",
    "The marker is at the right place. Part 1 of 2: the first p. 184 finding removes the blank line after \\oldpage[IV-4]{184}; apply both.")

# ------------------------------------------------------------------ p. 184
add(184, "top of p. 184: page break 183/184", "mid-sentence continuation 's'identifie par platitude'", "blank line after \\oldpage[IV-4]{184}", "marker",
    "\\oldpage[IV-4]{184}\n\ns'identifie", "\\oldpage[IV-4]{184}\ns'identifie", "Part 2 of 2 with the last p. 183 finding; both blank lines must go.")
add(184, "l. 1-2: 'en produit A′_1×A″_2 où A″_2 est une sous-C′-algèbre'", "no comma after A″_2 (crop c184_A2.png)", "comma", "punctuation",
    "$A'_1\\times A''_2$, où", "$A'_1\\times A''_2$ où", "")
add(184, "l. 3: 'sera somme de Z′_1=Spec(A′_1) et de T_2, et g′|X′_1'", "T_2 without primes (crops c184_T2.png, c184_T2z.png)",
    "$T''_2$ (silent correction)", "misprint_in_print",
    "et de $T''_2$, et", "et de $T_2$, et",
    "The scheme T″_2 = Spec(A″_2) defined just before is meant. The TeX silently corrected the print; this edit restores the printed reading.",
    corrected="et de $T''_2$, et")
add(184, "l. 3: 'sera un isomorphisme de X′_1 sur Z′_1'", "'isomorphisme de' italic, 'de' included (crop c184_T2.png)", "no \\emph", "italics",
    "sera un isomorphisme de $X'_1$", "sera un \\emph{isomorphisme de} $X'_1$", "Emphasis judged as if the remark body were roman.")
add(184, "Proposition (18.12.15): 'C′ une C-algèbre étale, A une C-algèbre'", "'étale' roman inside the italic statement (crop c184_p15l1.png)", "italic (environment)", "convention",
    "$C$-algèbre étale, $A$", "$C$-algèbre \\textup{étale}, $A$", "", conv=6)
add(184, "proof of (18.12.15): 'que A est une C-algèbre de type fini, donc de la forme'", "'de type fini' italic", "roman", "italics",
    "une $C$-algèbre de type fini, donc de la forme", "une $C$-algèbre \\emph{de type fini}, donc de la forme", G83)
add(184, "proof of (18.12.15): 'il en résultera que B′ = lim→(B_λ⊗_C C′) sera la fermeture'", "the formula is set in the line (crop c184_lim.png)",
    "displayed formula", "formula",
    "il en résultera que\n\\[\n  B'=\\varinjlim_\\lambda(B_\\lambda\\otimes_C C')\n\\]\nsera la fermeture",
    "il en résultera que $B'=\\varinjlim_\\lambda(B_\\lambda\\otimes_C C')$ sera la fermeture",
    "Display vs inline only. Apply BEFORE the next finding (its 'old' lies inside this one's).")
add(184, "proof of (18.12.15): 'lim→' under which the print has no index", "lim with the arrow, no λ (crop c184_lim.png)", "\\varinjlim_\\lambda", "symbol",
    "\\varinjlim_\\lambda(B_\\lambda", "\\varinjlim(B_\\lambda",
    "GLOBAL_ISSUES 30 pattern (lim index the print lacks). Apply after the previous finding.")
add(184, "proof of (18.12.15): 'lorsque A est une C-algèbre de présentation finie.'", "'présentation finie' italic (page_184_s2.png)", "roman", "italics",
    "lorsque $A$ est une $C$-algèbre de présentation finie.", "lorsque $A$ est une $C$-algèbre de \\emph{présentation finie}.", G83)
add(184, "proof of (18.12.15): 'se ramener au cas où C est noethérien. En effet'", "'noethérien' italic", "roman", "italics",
    "au cas où $C$ est noethérien. En effet", "au cas où $C$ est \\emph{noethérien}. En effet", G83)
add(184, "proof of (18.12.15): 'une C_α-algèbre étale C′_α tels que'", "'étale' italic", "roman", "italics",
    "-algèbre étale $C'_\\alpha$", "-algèbre \\emph{étale} $C'_\\alpha$", G83)
add(184, "proof of (18.12.15): 'limite inductive des A′_β=A_β⊗_{C_β}C′_β=A_α⊗_{C_α}C′_β pour β≥α'", "the formula is set in the line (page_184_s2.png)",
    "displayed formula", "formula",
    "limite inductive des\n\\[\n  A'_\\beta=A_\\beta\\otimes_{C_\\beta}C'_\\beta=A_\\alpha\\otimes_{C_\\alpha}C'_\\beta\n\\]\npour",
    "limite inductive des $A'_\\beta=A_\\beta\\otimes_{C_\\beta}C'_\\beta=A_\\alpha\\otimes_{C_\\alpha}C'_\\beta$ pour", "Display vs inline only.")
add(184, "proof of (18.12.15): 'lorsque C′ est supposé étale sur C noethérien'", "'étale' italic", "roman", "italics",
    "est supposé étale sur", "est supposé \\emph{étale} sur", G83)
add(184, "proof of (18.12.15): 'ramènent sans utiliser (6.14.1)'", "'sans utiliser' italic", "roman", "italics",
    "ramènent sans utiliser (6.14.1)", "ramènent \\emph{sans utiliser} (6.14.1)", G83)
add(184, "proof of (18.12.15): 'au cas où C est intègre, A le corps des fractions'", "'intègre' italic", "roman", "italics",
    "au cas où $C$ est intègre, $A$", "au cas où $C$ est \\emph{intègre}, $A$", G83)
add(184, "proof of (18.12.15): 'Spec(B′)→Spec(B) est étale, il résulte de (17.5.7)'", "'étale' italic", "roman", "italics",
    "\\Spec(B)$ est étale, il résulte", "\\Spec(B)$ est \\emph{étale}, il résulte", G83)
add(184, "Proposition (18.12.16): 'ample relativement à S (II, 4.6.1)'", "bold II; the reference upright (crop c184_461.png)", "plain II, italic reference", "convention",
    "relativement à $S$ (II, 4.6.1)", "relativement à $S$ \\textup{(\\textbf{II}, 4.6.1)}",
    "One edit for convention 2 (bold II) and convention 6 (upright reference). Apply before the next finding (adjacent, no overlap).", conv=2)
add(184, "Proposition (18.12.16): '(II, 4.6.1), le O_X-Module f*(ℒ)'", "the article 'le' set in roman inside the italic statement (wrong fount; crop c184_le.png against the italic 'le morphisme' of b″) on the same page)",
    "italic (environment; silent correction)", "misprint_in_print",
    ", le $\\sh{O}_X$-Module $f^*(\\mathscr L)$", ", \\textup{le} $\\sh{O}_X$-Module $f^*(\\mathscr L)$",
    "Wrong-fount word recorded as a misprint (GLOBAL_ISSUES 29; cf. IV-4 pp. 7, 42-43): the compositor kept the roman of the reference. Its 'old' starts after the previous finding's.",
    conf="medium", corrected=", le $\\sh{O}_X$-Module $f^*(\\mathscr L)$")
add(184, "proof of (18.12.16): 'donc (II, 5.1.6) le'", "bold II", "plain II", "convention",
    "donc (II, 5.1.6) le", "donc (\\textbf{II}, 5.1.6) le", "", conv=2)
add(184, "proof of (18.12.16): 'On en déduit (II, 4.6.13, (ii))'", "bold II", "plain II", "convention",
    "On en déduit (II, 4.6.13, (ii))", "On en déduit (\\textbf{II}, 4.6.13, (ii))", "", conv=2)
add(184, "proof of (18.12.16): 'que O_X⊗_{O_X}f*(ℒ^{⊗n})=f*(ℒ^{⊗n}) est ample'", "the formula is set in the line (page_184_s3.png)",
    "displayed formula", "formula",
    "que\n\\[\n  \\sh{O}_X\\otimes_{\\sh{O}_X}f^*(\\mathscr L^{\\otimes n})=f^*(\\mathscr L^{\\otimes n})\n\\]\nest ample",
    "que $\\sh{O}_X\\otimes_{\\sh{O}_X}f^*(\\mathscr L^{\\otimes n})=f^*(\\mathscr L^{\\otimes n})$ est ample",
    "Display vs inline only. Independent of the previous finding (no overlap).")
add(184, "proof of (18.12.16): '(II, 4.6.9, (i))'", "bold II", "plain II", "convention",
    "(II, 4.6.9, (i))", "(\\textbf{II}, 4.6.9, (i))", "", conv=2)
add(184, "Corollaire (18.12.17): 'Avec les notations de (II, 4.5.2),'", "bold II; the reference upright (crop c184_c17a.png)", "plain II, italic reference", "convention",
    "Avec les notations de (II, 4.5.2),", "Avec les notations de \\textup{(\\textbf{II}, 4.5.2)},", "One edit for conventions 2 and 6.", conv=2)
add(184, "Corollaire (18.12.17): 'les conditions de (II, 4.5.2)'", "bold II; the reference upright (crop c184_c17a.png)", "plain II, italic reference", "convention",
    "les conditions de (II, 4.5.2)", "les conditions de \\textup{(\\textbf{II}, 4.5.2)}", "One edit for conventions 2 and 6.", conv=2)
add(184, "Corollaire (18.12.17): '(qui équivalent au fait que ℒ est ample)'", "the parenthesis set in roman, 'ample' italic (crop c184_c17b.png)",
    "all italic (environment)", "convention",
    "(qui équivalent au fait que $\\mathscr L$ est ample)", "\\textup{(qui équivalent au fait que $\\mathscr L$ est \\emph{ample})}", "", conv=6)
add(184, "Corollaire (18.12.17), label b″)", "label upright (crop c184_b2.png)", "\\item[$b'')$]: italic b", "convention",
    "\\item[$b'')$] $h$ est séparé", "\\item[\\textup{b$''$)}] $h$ est séparé", G16, conv=6)
add(184, "Corollaire (18.12.17), label b‴)", "label upright (crop c184_b3.png)", "\\item[$b''')$]: italic b", "convention",
    "\\item[$b''')$] On a", "\\item[\\textup{b$'''$)}] On a", G16, conv=6)
add(184, "proof of (18.12.17): 'qui est séparé (II, 2.4.2)'", "bold II", "plain II", "convention",
    "(II, 2.4.2)", "(\\textbf{II}, 2.4.2)", "", conv=2)
add(184, "proof of (18.12.17): '... et on a h=g∘u. | Comme tout morphisme radiciel'", "'Comme tout morphisme radiciel' begins a new indented paragraph (crop c184_par.png)",
    "same paragraph", "other",
    "et on a $h=g\\circ u$. Comme tout", "et on a $h=g\\circ u$.\n\nComme tout", "")
add(184, "proof of (18.12.17): 'Comme tout morphisme radiciel est séparé (1.8.7.1)'",
    "(1.8.7.1): light old-style figures, no bold numeral, no comma (crop c184_1871.png)", "(I, 1.8.7.1)", "number",
    "est séparé (I, 1.8.7.1)", "est séparé (1.8.7.1)", "EGA IV's own (1.8.7.1) misread as an EGA I reference (GLOBAL_ISSUES 78). Independent of the previous finding (no overlap).")
add(184, "proof of (18.12.17): 'b‴) entraîne que h est séparé, donc entraîne b″).'", "labels wholly italic (page_184_s4.png)",
    "$b''')$, $b'')$: italic letters, upright parentheses", "italics",
    "$b''')$ entraîne que $h$ est séparé, donc entraîne $b'')$.", "\\emph{b$'''$)} entraîne que $h$ est séparé, donc entraîne \\emph{b$''$)}.", G88)
add(184, "proof of (18.12.17): 'Comme la condition b) de'", "label wholly italic", "$b)$", "italics",
    "la condition $b)$ de", "la condition \\emph{b)} de", G88)
add(184, "proof of (18.12.17): '(II, 4.5.2) entraîne évidemment'", "bold II", "plain II", "convention",
    "(II, 4.5.2) entraîne", "(\\textbf{II}, 4.5.2) entraîne", "", conv=2)
add(184, "proof of (18.12.17): 'évidemment b‴), il reste à voir que b″) entraîne'", "labels wholly italic", "$b''')$, $b'')$", "italics",
    "évidemment $b''')$, il reste à voir que $b'')$ entraîne", "évidemment \\emph{b$'''$)}, il reste à voir que \\emph{b$''$)} entraîne", G88)
add(184, "proof of (18.12.17): '(I, 6.3.4)'", "bold I and comma: a real EGA I reference (crop c184_I634.png)", "plain I", "convention",
    "(I, 6.3.4)", "(\\textbf{I}, 6.3.4)", "", conv=2)
add(184, "proof of (18.12.17): 'l'hypothèse b″) entraîne'", "label wholly italic", "$b'')$", "italics",
    "l'hypothèse $b'')$ entraîne", "l'hypothèse \\emph{b$''$)} entraîne", G88)
add(184, "proof of (18.12.17): '(I, 5.5.1)'", "bold I and comma: a real EGA I reference (crop c184_I551.png)", "plain I", "convention",
    "(I, 5.5.1)", "(\\textbf{I}, 5.5.1)", "", conv=2)
add(184, "proof of (18.12.17): 'dans l'ouvert Y′=⋃_j D_+(f_j) de Y.'", "the formula is set in the line (page_184_s4.png)", "displayed formula", "formula",
    "dans l'ouvert\n\\[\n  Y'=\\bigcup_j D_+(f_j)\n\\]\nde $Y$.", "dans l'ouvert $Y'=\\bigcup_j D_+(f_j)$ de $Y$.", "Display vs inline only.")
add(184, "proof of (18.12.17): 'le O_Y′-Module inversible ℒ′=O_Y(n)|Y′ (II, 2.5.8)'", "the formula is set in the line (page_184_s4.png)", "displayed formula", "formula",
    "Module inversible\n\\[\n  \\mathscr L'=\\sh{O}_Y(n)|Y'\n\\]\n", "Module inversible $\\mathscr L'=\\sh{O}_Y(n)|Y'$ ",
    "Display vs inline only. Independent of the next finding (no overlap).")
add(184, "proof of (18.12.17): '(II, 2.5.8)'", "bold II", "plain II", "convention",
    "(II, 2.5.8)", "(\\textbf{II}, 2.5.8)", "", conv=2)
add(184, "proof of (18.12.17): '(II, 4.4.3)'", "bold II", "plain II", "convention",
    "(II, 4.4.3)", "(\\textbf{II}, 4.4.3)", "", conv=2)
add(184, "end of p. 184: page break 184/185 inside 'n'est autre par définition que ℒ^{⊗n} | (II, 3.7.9, (i))'",
    "p. 185 begins mid-sentence with '(II, 3.7.9, (i)).' (crop c185_top.png)", "blank lines before and after \\oldpage[IV-4]{185}", "marker",
    "par définition que $\\mathscr L^{\\otimes n}$\n\n", "par définition que $\\mathscr L^{\\otimes n}$\n",
    "BOUNDARY FIX (page break with p. 185). The marker is at the right place. This edit removes the blank line before the marker; the blank line after \\oldpage[IV-4]{185} (p. 185 segment) must go too.")

# ------------------------------------------------------------------ verify
src = open(SRC, encoding="utf-8", newline="").read()
assert "\r" not in src
bad = 0
for d in F:
    if not d["fix"]:
        continue
    page = d["page"]
    pg = open(fr"{RUN}\page_{page}.tex", encoding="utf-8", newline="").read().replace("\r\n", "\n")
    o = d["fix"]["old"]
    a = src.index(f"\\oldpage[IV-4]{{{page}}}")
    b = src.index(f"\\oldpage[IV-4]{{{page + 1}}}")
    seg = src[a:b]
    cp, cs, cf = pg.count(o), seg.count(o), src.count(o)
    if cp != 1 or cs != 1:
        bad += 1
        print("NOT UNIQUE IN PAGE", page, cp, cs, repr(o[:80]))
    elif cf != 1:
        print("note: occurs", cf, "times in the whole file:", page, repr(o[:80]))
print("findings", len(F), "bad", bad)

json.dump(F, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
from collections import Counter
c = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    c[(d["page"], k)] += 1
for p in range(180, 185):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
