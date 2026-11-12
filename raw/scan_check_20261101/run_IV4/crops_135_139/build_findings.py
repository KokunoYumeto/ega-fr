import json, sys
sys.stdout.reconfigure(encoding='utf-8')

RUN = r'user/Documents/ega_scan_check_20261101/run_IV4/'
SRC = r'user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-18-fr.tex'
OUT = RUN + 'findings_135_139.json'


def F(page, where, scan, tex, kind, old, new, note='', convention=None, confidence='high', corrected=None, after=None):
    d = {
        'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind,
        'convention': convention, 'confidence': confidence,
        'fix': None if old is None else {'old': old, 'new': new},
    }
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    d['_after'] = after  # index (within this list) of a fix that must be applied first; stripped before writing
    return d


L = []

# ---------------- page 135 ----------------
L.append(F(135, "first paragraph (proof of 18.5.18), line 1",
    "'que d) implique la condition b) de (18.5.11)': both labels wholly italic",
    "$d)$ ... $b)$ (italic letter, upright parenthesis)", 'italics',
    r"que $d)$ implique la condition $b)$ de (18.5.11) car",
    r"que \emph{d)} implique la condition \emph{b)} de (18.5.11) car",
    "Labels in roman text are italic in the print (GLOBAL_ISSUES 88); two labels, one edit."))
L.append(F(135, "first paragraph, lines 3-4",
    "'et prouvons d). L'hypothèse de d) implique': labels wholly italic",
    "$d)$ twice", 'italics',
    r"et prouvons $d)$. L'hypothèse de $d)$ implique",
    r"et prouvons \emph{d)}. L'hypothèse de \emph{d)} implique",
    "GLOBAL_ISSUES 88; two labels, one edit."))
L.append(F(135, "first paragraph, line 4",
    "'(Err_III, 20)' with bold 'Err'", "(Err$_{\\mathrm{III}}$, 20)", 'font',
    r"(Err$_{\mathrm{III}}$, 20), en vertu de (13.1.4)",
    r"(\textbf{Err}$_{\mathrm{III}}$, 20), en vertu de (13.1.4)",
    "Same form as the earlier page fixes (p. 81: (\\textbf{Err}$_{\\mathrm{III}}$, 20)); roman text, so no \\textup."))
L.append(F(135, "first paragraph, line 4",
    "'la condition c) de (18.5.11)': label wholly italic", "$c)$", 'italics',
    r"la condition $c)$ de (18.5.11), $\sh{O}",
    r"la condition \emph{c)} de (18.5.11), $\sh{O}",
    "GLOBAL_ISSUES 88."))
L.append(F(135, "Proposition (18.5.19), statement",
    "wavy arrow: 'Y ⇝ Y∩X_s'", "Y\\longmapsto Y\\cap X_s", 'symbol',
    r"Y\longmapsto Y\cap X_s", r"Y\leadsto Y\cap X_s",
    "Wavy arrow in the print (GLOBAL_ISSUES 33 pattern)."))
L.append(F(135, "proof of (18.5.19), line 2",
    "'(II, 7.2.1)' with bold II", "(II, 7.2.1)", 'convention',
    r"non vide résulte de (II, 7.2.1)", r"non vide résulte de (\textbf{II}, 7.2.1)", convention=2))
L.append(F(135, "proof of (18.5.19), Stein factorization",
    "'(III, 4.3.3)' with bold III", "(III, 4.3.3)", 'convention',
    r"du morphisme propre $f$ (III, 4.3.3)", r"du morphisme propre $f$ (\textbf{III}, 4.3.3)", convention=2))
L.append(F(135, "proof of (18.5.19), 'il résulterait alors de (18.5.11, c))'",
    "'(18.5.11, c))': italic label c) followed by the closing parenthesis of the reference",
    "'(18.5.11, $c)$ que': one closing parenthesis only (the label's)", 'punctuation',
    r"(18.5.11, $c)$ que $S'$", r"(18.5.11, \emph{c)}) que $S'$",
    "One edit for two differences: the reference's closing parenthesis, missing in the TeX, and the italic label (GLOBAL_ISSUES 88)."))
L.append(F(135, "proof of (18.5.19), last sentence",
    "'(III, 4.3.1)' with bold III", "(III, 4.3.1)", 'convention',
    r"surjectif (III, 4.3.1)", r"surjectif (\textbf{III}, 4.3.1)", convention=2))
L.append(F(135, "(18.6.1), second paragraph: 'on a par hypothèse A′ = B_n où B est'",
    "no comma after 'A′=B_n' (crop p135_s3_comma.png); the parallel 'A″=B′_n′, où' has one",
    "$A'=B_{\\mathfrak n}$, où", 'punctuation',
    r"$A'=B_{\mathfrak n}$, où $B$", r"$A'=B_{\mathfrak n}$ où $B$",
    "The TeX adds a comma the print lacks."))
L.append(F(135, "(18.6.1), second paragraph: 'Si l'on pose S = B — n'",
    "long dash for the set difference", "$S=B-\\mathfrak n$", 'convention',
    r"$S=B-\mathfrak n$", r"$S=B\setmin\mathfrak n$",
    "Set difference (convention 7 proper); \\setmin as in the earlier IV-4 fixes.", convention=7))
L.append(F(135, "page break 135/136 ('formellement | étale', mid-sentence)",
    "p. 136 begins mid-sentence with 'étale (pour les topologies discrètes'",
    "blank lines before and after \\oldpage[IV-4]{136}", 'marker',
    "$A''$ est une $A$-algèbre formellement\n\n", "$A''$ est une $A$-algèbre formellement\n",
    "The marker is at the right place. Part 1 of 2: the first p. 136 finding removes the blank line after \\oldpage[IV-4]{136}; apply both (\\oldpage ends with \\ignorespaces, which does not skip a \\par)."))

# ---------------- page 136 ----------------
L.append(F(136, "top of page", "continues the sentence of p. 135 ('formellement | étale')",
    "blank line after \\oldpage[IV-4]{136}", 'marker',
    "\\oldpage[IV-4]{136}\n\nétale (pour", "\\oldpage[IV-4]{136}\nétale (pour",
    "Part 2 of 2 with the last p. 135 finding; both blank lines must go."))
i_conv6_18_6_1 = len(L)
L.append(F(136, "Lemme (18.6.2), statement",
    "'essentiellement étale (18.6.1) et tel que': reference upright", "(18.6.1) in the italic statement", 'convention',
    r"essentiellement étale (18.6.1) et tel que", r"essentiellement étale \textup{(18.6.1)} et tel que",
    "Printed upright inside the italic statement.", convention=6))
i_hens = len(L)
L.append(F(136, "Lemme (18.6.2), statement: 'pour tout anneau local hensé-|lien B'",
    "'hensélien' printed upright (roman) inside the italic statement", "italic 'hensélien'", 'convention',
    r"Alors, pour tout anneau local hensélien $B$", r"Alors, pour tout anneau local \textup{hensélien} $B$",
    "Roman word inside the italic statement. Same spot as the next finding (bold 'lien'): apply THIS one first.", convention=6))
L.append(F(136, "Lemme (18.6.2), statement: second half of 'hensé-|lien' at the start of a line",
    "'lien' in BOLD roman (wrong fount; 'hensé-' at the end of the line above is normal weight): side by side with the 'lien' of 'hensélien' on the same page, median stroke 6 px against 4 px (crops p136_lien_cmp.png, chk_lien_pair.png); the shapes are the wider bold ones",
    "normal weight (silent correction)", 'misprint_in_print',
    r"local \textup{hensélien} $B$", r"local \textup{hensé\textbf{lien}} $B$",
    "Wrong-fount letters recorded as a misprint (GLOBAL_ISSUES 29/97/99); isolated at the start of a line, so not the line-end heaviness of item 100. 'old' is the text AFTER the previous finding (apply that first); the fix changes only the bold 'lien'.",
    corrected=r"local \textup{hensélien} $B$", after=i_hens))
L.append(F(136, "proof of (18.6.2): 'puisque k(x) = k(s)'",
    "bold italic k", "$k(x)=k(s)$", 'convention',
    r"puisque $k(x)=k(s)$", r"puisque $\boldsymbol{k}(x)=\boldsymbol{k}(s)$", convention=1))
L.append(F(136, "proof of (18.6.2): 'il existe un seul point x′∈X au-dessus de x et de y'",
    "'x′∈X' with no prime on X (crop p136_s3_xX.png)", "$x'\\in X'$ (silent correction)", 'misprint_in_print',
    r"point $x'\in X'$ au-dessus de $x$ et de $y$", r"point $x'\in X$ au-dessus de $x$ et de $y$",
    "x′ is the point of X′ = X×_S Y over x and y (defined in the same sentence). The fix restores the printed X; it changes only the prime.",
    corrected=r"point $x'\in X'$ au-dessus de $x$ et de $y$"))
L.append(F(136, "proof of (18.6.2): 'et que k(x′) = k(y)'",
    "bold italic k", "$k(x')=k(y)$", 'convention',
    r"et que $k(x')=k(y)$. Il faut", r"et que $\boldsymbol{k}(x')=\boldsymbol{k}(y)$. Il faut", convention=1))
L.append(F(136, "proof of (18.6.2): 'le corps k(x′) = k(y)'",
    "bold italic k", "$k(x')=k(y)$", 'convention',
    r"le corps $k(x')=k(y)$", r"le corps $\boldsymbol{k}(x')=\boldsymbol{k}(y)$", convention=1))
L.append(F(136, "proof of (18.6.2): 'Y_0 = Spec(k(y))'",
    "bold italic k", "\\Spec(k(y))", 'convention',
    r"$Y_0=\Spec(k(y))$", r"$Y_0=\Spec(\boldsymbol{k}(y))$", convention=1))
L.append(F(136, "proof of (18.6.2), last line: '(18.5.11, b))'",
    "label b) wholly italic", "$b)$", 'italics',
    r"hensélien et de (18.5.11, $b)$).", r"hensélien et de (18.5.11, \emph{b)}).",
    "GLOBAL_ISSUES 88."))
L.append(F(136, "'Notons que le critère (18.5.11, b)) signifie'",
    "label b) wholly italic", "$b)$", 'italics',
    r"le critère (18.5.11, $b)$) signifie", r"le critère (18.5.11, \emph{b)}) signifie",
    "GLOBAL_ISSUES 88."))
L.append(F(136, "Lemme (18.6.3), item (i)", "label (i) upright", "\\item[(i)] (italic in the statement)", 'convention',
    r"\item[(i)] Il existe au plus", r"\item[\textup{(i)}] Il existe au plus", "GLOBAL_ISSUES 16.", convention=6))
L.append(F(136, "Lemme (18.6.3), item (ii)", "label (ii) upright", "\\item[(ii)] (italic in the statement)", 'convention',
    r"\item[(ii)] Il existe une", r"\item[\textup{(ii)}] Il existe une", "GLOBAL_ISSUES 16.", convention=6))
L.append(F(136, "proof of (18.6.3): 'les hypothèses k(x_1) = k(x_2) = k(s)'",
    "bold italic k", "$k(x_1)=k(x_2)=k(s)$", 'convention',
    r"les hypothèses $k(x_1)=k(x_2)=k(s)$",
    r"les hypothèses $\boldsymbol{k}(x_1)=\boldsymbol{k}(x_2)=\boldsymbol{k}(s)$", convention=1))
L.append(F(136, "proof of (18.6.3): 'et que k(x_3) = k(s)'",
    "bold italic k", "$k(x_3)=k(s)$", 'convention',
    r"et que $k(x_3)=k(s)$", r"et que $\boldsymbol{k}(x_3)=\boldsymbol{k}(s)$",
    "Adjacent to (not overlapping) the next finding.", convention=1))
L.append(F(136, "proof of (18.6.3): '(I, 3.4.9). En outre'",
    "'(I, 3.4.9)' with bold I and a comma (crop p136_s4_I349.png)", "(I, 3.4.9)", 'convention',
    r"(I, 3.4.9). En outre", r"(\textbf{I}, 3.4.9). En outre",
    "Genuine reference to EGA I (bold I), not one of EGA IV's own (1.x.y).", convention=2))
L.append(F(136, "page break 136/137 ('Par ailleurs, | on a vu', mid-sentence)",
    "p. 137 begins mid-sentence with 'on a vu qu'un A-homomorphisme'",
    "blank lines before and after \\oldpage[IV-4]{137}", 'marker',
    "vérifie les conditions de (ii). Par ailleurs,\n\n", "vérifie les conditions de (ii). Par ailleurs,\n",
    "The marker is at the right place. Part 1 of 2: the first p. 137 finding removes the blank line after \\oldpage[IV-4]{137}; apply both."))

# ---------------- page 137 ----------------
L.append(F(137, "top of page", "continues the sentence of p. 136 ('Par ailleurs, | on a vu')",
    "blank line after \\oldpage[IV-4]{137}", 'marker',
    "\\oldpage[IV-4]{137}\n\non a vu", "\\oldpage[IV-4]{137}\non a vu",
    "Part 2 of 2 with the last p. 136 finding; both blank lines must go."))
L.append(F(137, "proof of (18.6.3), end: 'Comme k(x_3) = k(x_2)'",
    "bold italic k", "$k(x_3)=k(x_2)$", 'convention',
    r"Comme $k(x_3)=k(x_2)$", r"Comme $\boldsymbol{k}(x_3)=\boldsymbol{k}(x_2)$", convention=1))
L.append(F(137, "Définition (18.6.5): 'On appelle hensélisé d'un anneau local A'",
    "'hensélisé' italic like the rest of the italic definition (crop p137_s2_def.png)",
    "\\emph{hensélisé} inside the italic definition environment, which sets it upright", 'italics',
    r"On appelle \emph{hensélisé} d'un anneau local", r"On appelle hensélisé d'un anneau local",
    "No change of face in the print (FIX_POLICY rule 2.6: drop \\emph inside an italic environment where the print shows none)."))
L.append(F(137, "Définition (18.6.5): 'défini dans (18.6.4).'",
    "reference upright", "(18.6.4) in the italic definition", 'convention',
    r"défini dans (18.6.4).", r"défini dans \textup{(18.6.4)}.",
    "Printed upright inside the italic statement.", convention=6))
for lab, ctx in [('i', r"] ${}^h\!A$ est un anneau local hensélien"),
                 ('ii', r"] Pour tout anneau local hensélien $B$, l'application canonique"),
                 ('iii', r"] ${}^h\!A$ est un $A$-module fidèlement plat"),
                 ('iv', r"] Si $\widehat A$ et"),
                 ('v', r"] Pour que ${}^h\!A$ soit noethérien"),
                 ('vi', r"] Si $A$ est hensélien, l'homomorphisme canonique")]:
    L.append(F(137, "Théorème (18.6.6), item (%s)" % lab, "label (%s) upright" % lab,
        "\\item[(%s)] (italic in the statement)" % lab, 'convention',
        r"\item[(" + lab + ")" + ctx, r"\item[\textup{(" + lab + ")}" + ctx, "GLOBAL_ISSUES 16.", convention=6))
L.append(F(137, "Théorème (18.6.6) (iii): 'et l'homomorphisme A/mA → ʰA/m.ʰA des corps résiduels est bijective.'",
    "'est bijective' (crop p137_s4_iii.png)", "'est bijective' (keeps the printed reading)", 'misprint_in_print',
    None, None,
    "Agreement error: the subject is 'l'homomorphisme' (masculine). The TeX keeps the printed reading.",
    corrected=r"des corps résiduels est bijectif."))

# ---------------- page 138 ----------------
L.append(F(138, "first paragraph: 'dans (17.6.1), a) implique c′)'",
    "labels a) and c′) wholly italic", "$a)$ ... $c')$", 'italics',
    r"dans (17.6.1), $a)$ implique $c')$, que", r"dans (17.6.1), \emph{a)} implique \emph{c$'$)}, que",
    "GLOBAL_ISSUES 88; two labels, one edit; prime written c$'$ as in the edition's fixed labels."))
L.append(F(138, "first paragraph: '(0_III, 10.3.1.3)'",
    "bold 0 with subscript III", "($0_{\\mathrm{III}}$, 10.3.1.3)", 'convention',
    r"résultent donc de ($0_{\mathrm{III}}$, 10.3.1.3)", r"résultent donc de ($\mathbf{0}_{\mathrm{III}}$, 10.3.1.3)", convention=2))
L.append(F(138, "first paragraph: 'fidèlement plat (0_I, 6.5.2)'",
    "bold 0 with subscript I", "($0_{\\mathrm I}$, 6.5.2)", 'convention',
    r"${}^h\!A$ est un $A$-module fidèlement plat ($0_{\mathrm I}$, 6.5.2)", r"${}^h\!A$ est un $A$-module fidèlement plat ($\mathbf{0}_{\mathrm I}$, 6.5.2)", convention=2))
L.append(F(138, "proof of (18.6.6) (i): 'appliquons le critère (18.5.11, b))'",
    "label b) wholly italic", "$b)$", 'italics',
    r"appliquons le critère (18.5.11, $b)$).", r"appliquons le critère (18.5.11, \emph{b)}).",
    "GLOBAL_ISSUES 88."))
L.append(F(138, "proof of (18.6.6) (i): 'qu'il existe un indice λ∈S'",
    "'λ∈S' with a roman S (crop p138_s2_lamS.png; the index set is the Fraktur 𝔖 of (18.6.4), printed Fraktur on p. 137)",
    "$\\lambda\\in\\mathfrak S$ (silent correction)", 'misprint_in_print',
    r"indice $\lambda\in\mathfrak S$, un morphisme", r"indice $\lambda\in S$, un morphisme",
    "Wrong letter (S is the scheme Spec(ʰA) of the same proof). The fix restores the printed roman S.",
    corrected=r"indice $\lambda\in\mathfrak S$, un morphisme"))
L.append(F(138, "proof of (18.6.6) (i): 'S′_0^(λ) = g^{-1}(S_0^(λ))'",
    "'g^{-1}' without the index λ (crop p138_s2_ginv.png)", "g_\\lambda^{-1} (silent correction)", 'misprint_in_print',
    r"=g_\lambda^{-1}(S_0^{(\lambda)})", r"=g^{-1}(S_0^{(\lambda)})",
    "The inverse image is taken under g_λ : S′^(λ) → S^(λ) (g : S′ → S does not see S_0^(λ)). The fix restores the printed g.",
    corrected=r"=g_\lambda^{-1}(S_0^{(\lambda)})"))
i_disp_g = len(L)
L.append(F(138, "proof of (18.6.6) (i): 'tels que S′ = S′^(λ) ×_S^(λ) S, g = g^(λ) × 1 et f_0 = f_0^(λ) × 1. Soient'",
    "in the running text, with 'et' before the last formula and no comma after the second",
    "displayed with \\qquad; the print's 'et' lost and a comma added", 'missing',
    "tels que\n\\[\n  S'=S'^{(\\lambda)}\\times_{S^{(\\lambda)}}S,\\qquad\n  g=g_\\lambda\\times1,\\qquad\n  f_0=f_0^{(\\lambda)}\\times1.\n\\]\nSoient $s$",
    "tels que $S'=S'^{(\\lambda)}\\times_{S^{(\\lambda)}}S$, $g=g_\\lambda\\times1$ et $f_0=f_0^{(\\lambda)}\\times1$. Soient $s$",
    "Formula inline as printed, the connecting 'et' restored. Same spot as the next finding (g^(λ)): apply THIS one first."))
L.append(F(138, "same place: 'g = g^(λ) × 1'",
    "'g = g^(λ)×1' with a superscript (λ) (crop p138_s2_glam.png)", "g=g_\\lambda\\times1 (silent correction)", 'misprint_in_print',
    r"g=g_\lambda\times1", r"g=g^{(\lambda)}\times1",
    "The morphism is named g_λ two lines earlier ('un morphisme étale g_λ : S′^(λ) → S^(λ)'); g^(λ) is not defined. Apply after the previous finding (display made inline): this 'old' occurs exactly once both before and after it, but the previous edit's 'old' contains it. The fix changes only the index.",
    corrected=r"g=g_\lambda\times1", confidence='medium', after=i_disp_g))
L.append(F(138, "proof of (18.6.6) (i): 'on a k(x_λ) = k(s_λ)'",
    "bold italic k", "$k(x_\\lambda)=k(s_\\lambda)$", 'convention',
    r"on a $k(x_\lambda)=k(s_\lambda)$", r"on a $\boldsymbol{k}(x_\lambda)=\boldsymbol{k}(s_\lambda)$", convention=1))
L.append(F(138, "proof of (18.6.6) (ii): 'il suffit de noter que l'on a Hom.loc(ʰA, B) ≅ lim← Hom.loc(A_λ, B) et que'",
    "in the running text; isomorphism sign ≅ (tilde over two bars, crop p138_s2_cong.png); lim with the arrow and no index",
    "displayed; '=' ; \\varprojlim_\\lambda", 'formula',
    "noter que l'on a\n\\[\n  \\Hom.\\operatorname{loc}({}^h\\!A,B)=\\varprojlim_\\lambda\\Hom.\\operatorname{loc}(A_\\lambda,B)\n\\]\net que par (18.6.2)",
    "noter que l'on a $\\Hom.\\operatorname{loc}({}^h\\!A,B)\\cong\\varprojlim\\Hom.\\operatorname{loc}(A_\\lambda,B)$ et que par (18.6.2)",
    "One edit for three differences: the sign ≅ for '=', no index under lim (GLOBAL_ISSUES 30), and the inline setting (no connecting word lost or added)."))
L.append(F(138, "proof of (18.6.6) (iv): 'et (m.ʰA)^n = m^n.ʰA = lim→ m_λ^n. On en conclut'",
    "in the running text; lim with the arrow and no index", "displayed; \\varinjlim_\\lambda", 'formula',
    "et\n\\[\n  (\\mathfrak m.{}^h\\!A)^n=\\mathfrak m^n.{}^h\\!A=\\varinjlim_\\lambda\\mathfrak m_\\lambda^n.\n\\]\nOn en conclut",
    "et $(\\mathfrak m.{}^h\\!A)^n=\\mathfrak m^n.{}^h\\!A=\\varinjlim\\mathfrak m_\\lambda^n$. On en conclut",
    "Inline as printed and no index under lim (GLOBAL_ISSUES 30); no connecting word lost or added."))
L.append(F(138, "proof of (18.6.6) (iv): 'que ʰA/(m.ʰA)^n = lim→ (A_λ/m_λ^n), et par suite'",
    "in the running text; lim with the arrow and no index", "displayed; \\varinjlim_\\lambda", 'formula',
    "que\n\\[\n  {}^h\\!A/(\\mathfrak m.{}^h\\!A)^n=\\varinjlim_\\lambda(A_\\lambda/\\mathfrak m_\\lambda^n),\n\\]\net par suite",
    "que ${}^h\\!A/(\\mathfrak m.{}^h\\!A)^n=\\varinjlim(A_\\lambda/\\mathfrak m_\\lambda^n)$, et par suite",
    "Inline as printed and no index under lim (GLOBAL_ISSUES 30); no connecting word lost or added."))
L.append(F(138, "(18.6.7), line 1: 'un anneau semi-local'",
    "'semi-local' italic", "roman", 'italics',
    r"un anneau semi-local, $\mathfrak m_i$", r"un anneau \emph{semi-local}, $\mathfrak m_i$"))
L.append(F(138, "(18.6.7), line 2: 'l'anneau produit'",
    "'produit' italic", "roman", 'italics',
    r"${}^h\!A$ l'anneau produit", r"${}^h\!A$ l'anneau \emph{produit}",
    "Adjacent to (not overlapping) the next finding."))
L.append(F(138, "(18.6.7), line 2: '∏_i ʰ(A_m_i)'",
    "product sign with the index i only (no i=1, no r)", "\\prod_{i=1}^r", 'formula',
    r"\prod_{i=1}^r{}^h(A_{\mathfrak m_i})", r"\prod_i{}^h(A_{\mathfrak m_i})",
    "The TeX adds the bounds '=1' and 'r'."))
L.append(F(138, "page break 138/139 ('que r.ʰA | est le radical', mid-sentence)",
    "p. 139 begins mid-sentence with 'est le radical de ʰA'",
    "blank lines before and after \\oldpage[IV-4]{139}", 'marker',
    "il résulte de ce qui précède que $\\mathfrak r.{}^h\\!A$\n\n", "il résulte de ce qui précède que $\\mathfrak r.{}^h\\!A$\n",
    "The marker is at the right place. Part 1 of 2: the first p. 139 finding removes the blank line after \\oldpage[IV-4]{139}; apply both."))

# ---------------- page 139 ----------------
L.append(F(139, "top of page", "continues the sentence of p. 138 ('r.ʰA | est le radical')",
    "blank line after \\oldpage[IV-4]{139}", 'marker',
    "\\oldpage[IV-4]{139}\n\nest le radical", "\\oldpage[IV-4]{139}\nest le radical",
    "Part 2 of 2 with the last p. 138 finding; both blank lines must go."))
L.append(F(139, "(18.6.7), second paragraph: 'deux anneaux semi-locaux de radicaux respectifs'",
    "'semi-locaux' italic (crop p139_s1_semi.png)", "roman", 'italics',
    r"deux anneaux semi-locaux de radicaux", r"deux anneaux \emph{semi-locaux} de radicaux"))
L.append(F(139, "(18.6.7), second paragraph: 'd'appeler homomorphisme semi-local de A dans B'",
    "'homomorphisme' roman, only 'semi-local' italic", "\\emph{homomorphisme semi-local}", 'italics',
    r"d'appeler \emph{homomorphisme semi-local} de", r"d'appeler homomorphisme \emph{semi-local} de"))
L.append(F(139, "(18.6.7): 'identifier cet ensemble à ∏_j(∪_i Hom.loc(A_m_i, B_j)) dans le cas considéré'",
    "in the running text", "displayed", 'other',
    "identifier cet ensemble à\n\\[\n  \\prod_j\\left(\\bigcup_i\\Hom.\\operatorname{loc}(A_{\\mathfrak m_i},B_j)\\right)\n\\]\ndans le cas considéré",
    "identifier cet ensemble à $\\prod_j(\\bigcup_i\\Hom.\\operatorname{loc}(A_{\\mathfrak m_i},B_j))$ dans le cas considéré",
    "Display vs inline only; no connecting word lost or added."))
L.append(F(139, "proof of (18.6.8): 'et de (I, 3.4.9), on conclut'",
    "'(I, 3.4.9)' with bold I and a comma", "(I, 3.4.9)", 'convention',
    r"et de (I, 3.4.9), on conclut", r"et de (\textbf{I}, 3.4.9), on conclut",
    "Genuine reference to EGA I (bold I), not one of EGA IV's own (1.x.y).", convention=2))
L.append(F(139, "proof of (18.6.8): 'tels que les composés A → B →φ C, A → ʰA →ψ C soient égaux'",
    "in the running text", "displayed with \\qquad", 'other',
    "tels que les composés\n\\[\n  A\\longrightarrow B\\xrightarrow{\\varphi}C,\\qquad\n  A\\longrightarrow{}^h\\!A\\xrightarrow{\\psi}C\n\\]\nsoient égaux",
    "tels que les composés $A\\to B\\xrightarrow{\\varphi}C$, $A\\to{}^h\\!A\\xrightarrow{\\psi}C$ soient égaux",
    "Display vs inline only; no connecting word lost or added."))
L.append(F(139, "proof of (18.6.8): 'donc l'application Hom.sloc(B⊗_A(ʰA), C) → Hom.sloc(B, C) est bijective'",
    "in the running text", "displayed", 'other',
    "donc l'application\n\\[\n  \\Hom.\\operatorname{sloc}(B\\otimes_A({}^h\\!A),C)\\longrightarrow\\Hom.\\operatorname{sloc}(B,C)\n\\]\nest bijective",
    "donc l'application $\\Hom.\\operatorname{sloc}(B\\otimes_A({}^h\\!A),C)\\to\\Hom.\\operatorname{sloc}(B,C)$ est bijective",
    "Display vs inline only; no connecting word lost or added."))
L.append(F(139, "Théorème (18.6.9), item (i): '(i) Pour que ʰA soit réduit (resp. normal)'",
    "label (i) upright; '(resp.' and ')' upright, 'normal' italic (crop p139_s4_resp.png)",
    "\\item[(i)] and '(resp. normal)' all italic", 'convention',
    r"\item[(i)] Pour que ${}^h\!A$ soit réduit (resp. normal), il faut",
    r"\item[\textup{(i)}] Pour que ${}^h\!A$ soit réduit \textup{(resp.} normal\textup{)}, il faut",
    "Two convention-6 items in one edit: the label (GLOBAL_ISSUES 16) and the upright '(resp. ...)' (as in Proposition (18.4.5), p. 119). The 'old' includes 'h' context because Théorème (18.8.12) repeats the line with ʰˢA.",
    convention=6))
L.append(F(139, "Théorème (18.6.9), item (ii)", "label (ii) upright", "\\item[(ii)] (italic in the statement)", 'convention',
    r"\item[(ii)] Supposons $A$ noethérien. Alors, pour tout idéal premier $\mathfrak p$ de $A$, l'anneau $({}^h\!A)",
    r"\item[\textup{(ii)}] Supposons $A$ noethérien. Alors, pour tout idéal premier $\mathfrak p$ de $A$, l'anneau $({}^h\!A)",
    "GLOBAL_ISSUES 16. Long 'old' because Théorème (18.8.12) repeats the line with ʰˢA.", convention=6))
L.append(F(139, "Théorème (18.6.9) (ii): 'séparables de k(p)'",
    "bold italic k", "$k(\\mathfrak p)$", 'convention',
    r"\mathfrak p.({}^h\!A)_{\mathfrak p}$ est composé direct d'un nombre fini d'extensions algébriques séparables de $k(\mathfrak p)$",
    r"\mathfrak p.({}^h\!A)_{\mathfrak p}$ est composé direct d'un nombre fini d'extensions algébriques séparables de $\boldsymbol{k}(\mathfrak p)$",
    "Long 'old' because Théorème (18.8.12) repeats the sentence with ʰˢA. Adjacent to (not overlapping) the previous and next findings.", convention=1))
L.append(F(139, "Théorème (18.6.9) (ii): '(ce qui entraîne que les fibres ... sont géométriquement régulières)'",
    "the parenthesis set roman, only 'géométriquement régulières' italic (crop p139_s4_cequi.png)",
    "all italic, with 'géométriquement régulières' upright through \\emph", 'convention',
    r"(ce qui entraîne que les fibres du morphisme canonique $\Spec({}^h\!A)\to\Spec(A)$ sont \emph{géométriquement régulières})",
    r"\textup{(ce qui entraîne que les fibres du morphisme canonique $\Spec({}^h\!A)\to\Spec(A)$ sont \emph{géométriquement régulières})}",
    "Inside \\textup the \\emph gives italic, as printed.", convention=6))

# ---------------- checks ----------------
src = open(SRC, encoding='utf-8', newline='').read()
pages = {}
for p in range(135, 140):
    pages[p] = open(RUN + 'page_%03d.tex' % p, encoding='utf-8', newline='').read().replace('\r\n', '\n')

ok = True
applied_page = dict(pages)
applied_src = src
for i, f in enumerate(L):
    fx = f['fix']
    if fx is None:
        continue
    p = f['page']
    old = fx['old']
    if f['_after'] is None:
        cp, cs = pages[p].count(old), src.count(old)
        tag = 'orig'
    else:
        # apply the prerequisite fix first, then count
        pre = L[f['_after']]['fix']
        tp = pages[p].replace(pre['old'], pre['new'], 1)
        ts = src.replace(pre['old'], pre['new'], 1)
        cp, cs = tp.count(old), ts.count(old)
        tag = 'after#%d' % f['_after']
    if cp != 1 or cs != 1:
        ok = False
        print('NOT UNIQUE', i, p, tag, cp, cs, repr(old)[:120])
print('all unique:', ok, 'n =', len(L))

# apply all fixes in order to a copy of the source to check there are no conflicts
t = src
for i, f in enumerate(L):
    fx = f['fix']
    if fx is None:
        continue
    c = t.count(fx['old'])
    if c != 1:
        print('SEQUENTIAL CONFLICT', i, f['page'], c, repr(fx['old'])[:100])
    t = t.replace(fx['old'], fx['new'], 1)
print('sequential application done')

out = []
for f in L:
    g = dict(f)
    del g['_after']
    out.append(g)
with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for f in out:
    k = 'misprint' if f['kind'] == 'misprint_in_print' else ('convention' if f['kind'] == 'convention' else 'normal')
    cnt[(f['page'], k)] += 1
for p in range(135, 140):
    print(p, cnt[(p, 'normal')], cnt[(p, 'convention')], cnt[(p, 'misprint')])
