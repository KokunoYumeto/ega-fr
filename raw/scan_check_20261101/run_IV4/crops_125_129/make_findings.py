import json

OUT = r"user\Documents\ega_scan_check_20261101\run_IV4\findings_125_129.json"
F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": (None if old is None else {"old": old, "new": new})}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 125
add(125, "Corollaire (18.4.14), label (i)", "upright (i) inside the italic statement",
    r"\item[(i)] (italic in the corollary)", "convention", 6, "high",
    r"\item[(i)]", r"\item[\textup{(i)}]", "GLOBAL_ISSUES 16.")
add(125, "Corollaire (18.4.14), label (ii)", "upright (ii) inside the italic statement",
    r"\item[(ii)] (italic in the corollary)", "convention", 6, "high",
    r"\item[(ii)]", r"\item[\textup{(ii)}]", "GLOBAL_ISSUES 16.")
add(125, "Corollaire (18.4.14) (ii): '(ce qui équivaut à dire (0_I, 6.3.3) que pour tout idéal maximal 𝔫 de B (nécessairement au-dessus de 𝔪), B_𝔫 est un A-module plat).'",
    "the whole parenthesis is roman inside the italic statement (crop p125_s1_top.png)",
    "italic (inside the corollary)", "convention", 6, "high",
    r"(ce qui équivaut à dire ($0_{\mathrm I}$, 6.3.3) que pour tout idéal maximal $\mathfrak n$ de $B$ (nécessairement au-dessus de $\mathfrak m$), $B_{\mathfrak n}$ est un $A$-module plat).",
    r"\textup{(ce qui équivaut à dire ($0_{\mathrm I}$, 6.3.3) que pour tout idéal maximal $\mathfrak n$ de $B$ (nécessairement au-dessus de $\mathfrak m$), $B_{\mathfrak n}$ est un $A$-module plat).}",
    "Same spot as the next finding (bold 0 of the reference inside this parenthesis): apply THIS one first; its 'old' contains the next one's 'old', which this edit leaves unchanged.")
add(125, "Corollaire (18.4.14) (ii): '(0_I, 6.3.3)'", "bold 0 with subscript I", "plain 0",
    "convention", 2, "high", r"($0_{\mathrm I}$, 6.3.3)", r"($\mathbf{0}_{\mathrm I}$, 6.3.3)",
    "Apply after the previous finding (convention-6 \\textup around the same parenthesis).")
add(125, "proof of (18.4.14): 'Ω¹_{(B⊗_A k)/k} = Ω¹_{B/A}⊗_B k (0, 20.5.5)'", "bare bold 0", "plain 0",
    "convention", 2, "high", "(0, 20.5.5)", r"(\textbf{0}, 20.5.5)")
add(125, "proof of (18.4.14): 'B-module de type fini (0, 20.4.7)'", "bare bold 0", "plain 0",
    "convention", 2, "high", "(0, 20.4.7)", r"(\textbf{0}, 20.4.7)")
add(125, "footnote (1) to the heading 18.5: 'est due à AZUMAYA, celle de hensélisation à NAGATA'",
    "both names in capitals and small capitals (crop p125_fn.png)", "plain 'Azumaya', 'Nagata'",
    "font", None, "high",
    "due à Azumaya, celle de hensélisation à Nagata,",
    r"due à \textsc{Azumaya}, celle de hensélisation à \textsc{Nagata},",
    "Author names in small capitals, written \\textsc as in the bibliography fixes of the other parts.")
add(125, "(18.5.1.1): 'ᵗV_ℰ : X′ ⇝ Γ(X′, ℰ_(X′))', the V",
    "light roman V, not bold (crops p125_eq1.png, p125_V_side.png; the V of the scheme V(Ě) in the same paragraph is bold)",
    r"{}^t\!\mathbf V_{\sh{E}} (bold V)", "font", None, "high",
    r"{}^t\!\mathbf V_{\sh{E}}", r"{}^t\!V_{\sh{E}}",
    "The functor ᵗV is printed with a light roman V in all three places on p. 125 (next findings too); only the representing scheme V(Ě) is bold. Written V like the edition's other roman capitals in formulas (GLOBAL_ISSUES 17).")
add(125, "(18.5.1.1), arrow", "wavy arrow ⇝ (crop p125_eq1.png)", r"\longmapsto", "symbol", None, "high",
    r"X'\longmapsto\Gamma(X',\sh{E}_{(X')})", r"X'\leadsto\Gamma(X',\sh{E}_{(X')})",
    "Wavy arrow in the print (GLOBAL_ISSUES 33 pattern).")
add(125, "after (18.5.1.1): 'de la catégorie des X-préschémas dans celle des ensembles'",
    "'préschémas' italic, like 'ensembles' (crop p125_s3a.png)", "$X$-préschémas upright", "italics", None, "high",
    r"des $X$-préschémas dans celle des \emph{ensembles}", r"des $X$-\emph{préschémas} dans celle des \emph{ensembles}")
add(125, "'(0_III, 8.1.8)'", "bold 0 with subscript III", "plain 0", "convention", 2, "high",
    r"($0_{\mathrm{III}}$, 8.1.8)", r"($\mathbf{0}_{\mathrm{III}}$, 8.1.8)")
add(125, "'d'où (0_I, 4.4.3.2) une application'", "bold 0 with subscript I", "plain 0", "convention", 2, "high",
    r"($0_{\mathrm I}$, 4.4.3.2)", r"($\mathbf{0}_{\mathrm I}$, 4.4.3.2)")
add(125, "'une application Γ(X′, ℰ_(X′)) → Γ(X′, f_*(ℰ_(X″))) = Γ(X″, ℰ_(X″))'",
    "Γ(X′, f_*(ℰ_(X″))): first argument X′ with ONE prime (crop p125_s3a.png)",
    r"\Gamma(X'',f_*(\sh{E}_{(X'')}))", "formula", None, "high",
    r"\to\Gamma(X'',f_*(\sh{E}_{(X'')}))", r"\to\Gamma(X',f_*(\sh{E}_{(X'')}))",
    "The printed reading is correct (f : X″ → X′, so f_*(ℰ_(X″)) is a sheaf on X′); the TeX's X″ is not what the print says.")
add(125, "'qui achève de définir le foncteur ᵗV.'", "light roman V (crop p125_V_side.png)",
    r"{}^t\!\mathbf V (bold)", "font", None, "high",
    r"achève de définir le foncteur ${}^t\!\mathbf V$", r"achève de définir le foncteur ${}^t\!V$",
    "As (18.5.1.1).")
add(125, "'le X-préschéma V(Ě) (II, 1.7.8) représente'", "bold II", "plain II", "convention", 2, "high",
    r"$\mathbf V(\check{\sh{E}})$ (II, 1.7.8)", r"$\mathbf V(\check{\sh{E}})$ (\textbf{II}, 1.7.8)")
add(125, "'représente le foncteur ᵗV. Il est immédiat'",
    "light roman V, next to the bold V(Ě) of the same line (crops p125_s3b.png, p125_V_side.png)",
    r"{}^t\!\mathbf V (bold)", "font", None, "high",
    r"\emph{représente} le foncteur ${}^t\!\mathbf V$", r"\emph{représente} le foncteur ${}^t\!V$",
    "As (18.5.1.1).")
add(125, "'donc V(Ě) ×_X X′ = V((ℰ_(X′))ˇ)'",
    "V((ℰ_(X′))ˇ): the dual of ℰ_(X′), raised check after the parenthesis (crop p125_VEdual.png)",
    r"\mathbf V((\check{\sh{E}})_{(X')})", "formula", None, "high",
    r"=\mathbf V((\check{\sh{E}})_{(X')})$; compte", r"=\mathbf V((\sh{E}_{(X')})^\vee)$; compte",
    "The TeX substitutes the equal expression (Ě)_(X′) of the preceding equation; restored to the printed reading.")
add(125, "'compte tenu de (I, 3.3.14)'", "bold I, then '3.3.14' (crop p125_s3b.png)", "plain I",
    "convention", 2, "high", "(I, 3.3.14)", r"(\textbf{I}, 3.3.14)",
    "Genuine reference to EGA I (bold I), not one of EGA IV's own (1.x.y).")
add(125, "'une bijection Γ(V(Ě)/X) ⥲ Γ(X, ℰ)'", "isomorphism arrow (tilde over the arrow), crop p125_s3b.png",
    r"\to", "symbol", None, "high",
    r"/X)\to\Gamma(X,\sh{E})$", r"/X)\xrightarrow{\sim}\Gamma(X,\sh{E})$",
    "Not convention 4: the TeX has a plain arrow, not \\simeq.")
add(125, "'la bijection Γ(V(Ě_(X′))/X′) ⥲ Γ(X′, ℰ_(X′))', argument of V",
    "V(Ě_(X′)): the subscript (X′) on Ě, no parentheses round Ě (crop p125_VEX.png)",
    r"\mathbf V((\check{\sh{E}})_{(X')})", "formula", None, "high",
    r"\Gamma(\mathbf V((\check{\sh{E}})_{(X')})/X')", r"\Gamma(\mathbf V(\check{\sh{E}}_{(X')})/X')",
    "Independent of the next finding (no shared characters).")
add(125, "same formula, the arrow", "isomorphism arrow (tilde over the arrow), crop p125_VEX.png", r"\to",
    "symbol", None, "high",
    r"\to\Gamma(X',\sh{E}_{(X')})$ est fonctorielle", r"\xrightarrow{\sim}\Gamma(X',\sh{E}_{(X')})$ est fonctorielle")
add(125, "'sur Hom_{O_X}(Ě, O_X) (II, 1.7.8), et la transposition'", "bold II", "plain II",
    "convention", 2, "high", "(II, 1.7.8), et la transposition", r"(\textbf{II}, 1.7.8), et la transposition")
add(125, "'la transposition u ⇝ ᵗu'", "wavy arrow (crop p125_s3c.png)", r"\mapsto", "symbol", None, "high",
    r"u\mapsto{}^t u", r"u\leadsto{}^t u", "Wavy arrow in the print (GLOBAL_ISSUES 33 pattern).")

# ---------------------------------------------------------------- p. 126
add(126, "first sentence: 'conformément à la théorie générale (0_III, 8.1.6)'", "bold 0 with subscript III",
    "plain 0", "convention", 2, "high",
    r"($0_{\mathrm{III}}$, 8.1.6)", r"($\mathbf{0}_{\mathrm{III}}$, 8.1.6)",
    "The next finding (comma) touches the same spot: list order first this, then that (either order works; neither edit changes the other's 'old').")
add(126, "first sentence: 'Notons encore que, conformément à la théorie générale (0_III, 8.1.6) l'automorphisme identique'",
    "no comma after '(0_III, 8.1.6)' (crop p126_comma.png), although the incise opens with a comma after 'que'",
    "'8.1.6), l'automorphisme': the TeX adds the comma (silent correction)", "misprint_in_print", None, "high",
    "8.1.6), l'automorphisme", "8.1.6) l'automorphisme",
    "Missing closing comma of the incise. The fix removes only the comma.",
    corrected="8.1.6), l'automorphisme")
add(126, "'c'est-à-dire (II, 1.4.1)'", "bold II", "plain II", "convention", 2, "high",
    "c'est-à-dire (II, 1.4.1)", r"c'est-à-dire (\textbf{II}, 1.4.1)")
add(126, "'un homomorphisme de S(Ě)-Modules u : S(Ě) → S(Ě)⊗ℰ; pour tout ouvert affine W de X'",
    "the formula is in the running text: it starts a line and 'pour tout ouvert affine W de X, si l'on pose' follows on the same line (crop p126_u.png)",
    r"displayed with \[ ... \]", "other", None, "high",
    "-Modules\n\\[\n  u:\\mathbf S_{\\sh{O}_X}(\\check{\\sh{E}})\\longrightarrow\n  \\mathbf S_{\\sh{O}_X}(\\check{\\sh{E}})\\otimes_{\\sh{O}_X}\\sh{E};\n\\]\npour tout",
    "-Modules $u:\\mathbf S_{\\sh{O}_X}(\\check{\\sh{E}})\\to\\mathbf S_{\\sh{O}_X}(\\check{\\sh{E}})\\otimes_{\\sh{O}_X}\\sh{E}$; pour tout",
    "Display vs inline only; no connecting word lost or added.")
add(126, "'de C-modules tel que u(1) = Σ_{i=1}^n T_i⊗e_i.' and the next paragraph 'Si X′ = Spec(A)'",
    "u(1) = Σ T_i⊗e_i is in the running text after 'tel que' (limits stacked, line set wider; crop p126_u1.png); 'Si X′ = Spec(A)' then begins a new indented paragraph",
    r"displayed with \[ ... \]; no blank line before 'Si', so that line is not indented", "other", None, "high",
    "tel que\n\\[\n  u(1)=\\sum_{i=1}^n T_i\\otimes e_i.\n\\]\nSi $X'=\\Spec(A)$",
    "tel que $u(1)=\\sum_{i=1}^n T_i\\otimes e_i$.\n\nSi $X'=\\Spec(A)$",
    "Inline formula restored, and the paragraph break the print has before 'Si' added.")
add(126, "(18.5.2): 'Rappelons (II, 1.7.8)'", "bold II", "plain II", "convention", 2, "high",
    "Rappelons (II, 1.7.8)", r"Rappelons (\textbf{II}, 1.7.8)")
add(126, "(18.5.2): 'tels que J soit contenu dans le noyau de v'",
    "'contenu dans le noyau de' italic, the 'de' included (crop p126_noyau.png)",
    r"\emph{contenu dans le noyau} de $v$: 'de' upright", "italics", None, "high",
    r"\emph{contenu dans le noyau} de $v$", r"\emph{contenu dans le noyau de} $v$")
add(126, "(18.5.2), displayed functor 'X′ ⇝ Al(X′, ℰ_(X′), J⊗O_X′)'", "wavy arrow", r"\longmapsto",
    "symbol", None, "high", r"X'\longmapsto\operatorname{Al}", r"X'\leadsto\operatorname{Al}",
    "Wavy arrow in the print (GLOBAL_ISSUES 33 pattern).")
add(126, "(18.5.2): 'l'ensemble Al(...) s'identifie alors à la partie de A^n formée des points'",
    "the exponent n is BOLD italic (wrong fount), mid-line: side by side with the light n of 'l'ensemble A^n,' two lines above and of O^n_{X′} (crops p126_n_side.png, p126_n_side2.png; mean stroke width 5.2 px against 3.8 px for both)",
    "normal n (silent correction)", "misprint_in_print", None, "high",
    r"à la partie de $A^n$ formée", r"à la partie de $A^{\boldsymbol{n}}$ formée",
    "Wrong-fount letter recorded as a misprint (GLOBAL_ISSUES 29/99, like the exponent n on p. 38). The heavy subscript n of 'T_n];' at the end of the line above is line-end heaviness (item 100), not reported.",
    corrected=r"à la partie de $A^n$ formée")
add(126, "Lemme (18.5.3): 'un morphisme fini et localement libre (18.2.7).'",
    "(18.2.7) upright inside the italic statement (crop p126_lemme.png)", "italic", "convention", 6, "high",
    "localement libre (18.2.7). Considérons", r"localement libre \textup{(18.2.7)}. Considérons")
add(126, "(18.5.3.1): 'S′ ⇝ Of(X×_S S′)'", "wavy arrow (crop p126_lemme2.png)", r"\longmapsto", "symbol", None,
    "high", r"S'\longmapsto\operatorname{Of}(X\times_S S')", r"S'\leadsto\operatorname{Of}(X\times_S S')",
    "Wavy arrow in the print (GLOBAL_ISSUES 33 pattern).")

# ---------------------------------------------------------------- p. 127
add(127, "proof of (18.5.3): 'quasi-cohérentes (II, 1.2.7 et 1.3.1)'", "bold II", "plain II",
    "convention", 2, "high", "(II, 1.2.7 et 1.3.1)", r"(\textbf{II}, 1.2.7 et 1.3.1)")
add(127, "'Il suffit donc de prouver le lemme pour le foncteur S′ ⇝ Id(ℬ′).'", "wavy arrow",
    r"\longmapsto", "symbol", None, "high",
    r"S'\longmapsto\operatorname{Id}(\mathscr B')", r"S'\leadsto\operatorname{Id}(\mathscr B')",
    "Wavy arrow in the print (GLOBAL_ISSUES 33 pattern).")
add(127, "'un Idéal de type fini J de S_{O_S}(ℬ)' (end of the first line of the paragraph 'Pour cela')",
    "S_{O_S}(ℬ) WITHOUT the check accent (crop p127_SB.png, no trace of an accent); later in the same paragraph the same Ideal is 'l'Idéal J de S_{O_S}(ℬ̌)', with the check",
    r"\mathbf S_{\sh{O}_S}(\check{\mathscr B}) (silent correction)", "misprint_in_print", None, "medium",
    r"(\check{\mathscr B})$ tel que", r"(\mathscr B)$ tel que",
    "J is an Ideal of S(ℬ̌) (V(ℬ̌) = Spec S(ℬ̌), 18.5.2). The check missing here is printed instead on ℬ′ in the next line (next finding). Medium only because a dropped accent sort cannot be ruled out.",
    corrected=r"(\check{\mathscr B})$ tel que")
add(127, "'tel que Id(ℬ′) soit de la forme Al(S′, ℬ̌′, J⊗_{O_S}O_S′) (18.5.2)'",
    "a check accent over ℬ′ (crop p127_Al.png)", r"\mathscr B' without the check (silent correction)",
    "misprint_in_print", None, "high",
    r"\operatorname{Al}(S',\mathscr B',", r"\operatorname{Al}(S',\check{\mathscr B}',",
    "By (18.5.2) the second argument is ℰ_(S′) with ℰ = ℬ, i.e. ℬ′ (the idempotents lie in Γ(S′, ℬ′)); the check belongs on the ℬ of the preceding line (previous finding).",
    corrected=r"\operatorname{Al}(S',\mathscr B',")
add(127, "'son image réciproque ℬ_(V(ℬ̌)) est une O_{V(ℬ̌)}-Algèbre'",
    "subscript V(ℬ̌) of O without the outer parentheses (ℬ_(V(ℬ̌)) just before has them); crop p127_OV.png",
    r"\sh{O}_{(\mathbf V(\check{\mathscr B}))}", "formula", None, "high",
    r"\sh{O}_{(\mathbf V(\check{\mathscr B}))}$-Algèbre", r"\sh{O}_{\mathbf V(\check{\mathscr B})}$-Algèbre")
add(127, "'tel que u^(2)(1) = Σ_k(Σ_{i,j} c_ijk T_iT_j)⊗e_k, où (c_ijk) est la table de multiplication'",
    "in the running text: starts a line, 'où (c_ijk) est la table de multiplication de l'algèbre Γ(W, ℬ)' follows on the same line; ordinary-size parentheses (crop p127_u2.png)",
    r"displayed with \[ ... \] and \Bigl( \Bigr)", "other", None, "high",
    "tel que\n\\[\n  u^{(2)}(1)=\\sum_k\\Bigl(\\sum_{i,j}c_{ijk}T_iT_j\\Bigr)\\otimes e_k,\n\\]\noù",
    "tel que $u^{(2)}(1)=\\sum_k(\\sum_{i,j}c_{ijk}T_iT_j)\\otimes e_k$, où",
    "Display vs inline only; no connecting word lost or added.")
add(127, "'le noyau de l'homomorphisme u—u^(2)'", "long dash for the minus (crop p127_umin.png)", "u-u^{(2)}",
    "convention", 7, "high", "u-u^{(2)}", r"u\setmin u^{(2)}", "Subtraction (GLOBAL_ISSUES 23).")
add(127, "'P_k(T_1, ..., T_n) = T_k—Σ_{i,j} c_ijk T_iT_j'", "long dash for the minus (crop p127_s3a.png)",
    "T_k-\\sum", "convention", 7, "high", r"=T_k-\sum_{i,j}", r"=T_k\setmin\sum_{i,j}",
    "Subtraction (GLOBAL_ISSUES 23).")
add(127, "'annule tous les polynômes P_k (1 ≤ i ≤ n)'", "'(1⩽i⩽n)' with i (crop p127_Pk.png)",
    r"($1\leq i\leq n$): keeps the printed reading", "misprint_in_print", None, "high",
    None, None,
    "The range belongs to the index k of the polynomials P_k (i is the summation index of Σ_i t_i e_i).",
    corrected=r"($1\leq k\leq n$)")
add(127, "Proposition (18.5.4), label a)", "upright a) (crop p127_a.png)", r"\item[a)] (italic)",
    "convention", 6, "high", r"\item[a)]", r"\item[\textup{a)}]", "GLOBAL_ISSUES 16/88.")
add(127, "Proposition (18.5.4) a): 'Pour tout morphisme fini g : S′ → S'",
    "'fini' roman inside the italic statement (crop p127_a.png)", "italic", "convention", 6, "high",
    r"morphisme fini $g:S'\to S$, l'application canonique",
    r"morphisme \textup{fini} $g:S'\to S$, l'application canonique")
add(127, "Proposition (18.5.4) a), display (18.5.4.1) and '(cf. (18.5.3))'",
    "'(cf. (18.5.3))' stands on the display line, at the right margin, upright; 'est bijective.' follows on the next line (crop p127_s4a.png)",
    r"'(cf. (18.5.3)) est bijective.' after \end{equation}, italic (in the statement)", "other", None, "high",
    "\\operatorname{Of}(S'\\times_S S_0)\n    \\tag{18.5.4.1}\\label{IV.18.5.4.1}\n  \\end{equation}\n  (cf. (18.5.3)) est bijective.",
    "\\operatorname{Of}(S'\\times_S S_0)\\qquad\\textup{(cf. (18.5.3))}\n    \\tag{18.5.4.1}\\label{IV.18.5.4.1}\n  \\end{equation}\n  est bijective.",
    "Moves the reference into the display, as printed, and sets it upright (the upright setting is a convention-6 item, done in the same edit because the text moves). Unlike (17.13.2) b′), p. 90, where the print sets '(cf. (16.5.12))' after the display.")
add(127, "Proposition (18.5.4), label a′)", "upright a′) (crop p127_ap.png)", r"\item[a')] (italic)",
    "convention", 6, "high", r"\item[a')]", r"\item[\textup{a$'$)}]",
    "Prime written a$'$ as in the edition's fixed labels (GLOBAL_ISSUES 88).")
add(127, "Proposition (18.5.4) a′): 'Pour tout morphisme fini et localement libre g : S′ → S'",
    "'fini et localement libre' roman inside the italic statement (crop p127_ap.png)", "italic",
    "convention", 6, "high", r"morphisme fini et localement libre $g:S'\to S$",
    r"morphisme \textup{fini et localement libre} $g:S'\to S$")
add(127, "Proposition (18.5.4) a′): 'l'application (18.5.4.1) est bijective'",
    "(18.5.4.1) upright inside the italic statement", "italic", "convention", 6, "high",
    "l'application (18.5.4.1) est bijective.", r"l'application \textup{(18.5.4.1)} est bijective.")

# ---------------------------------------------------------------- p. 128
add(128, "Proposition (18.5.4), label b)", "upright b) (crop p128_s1a.png)", r"\item[b)] (italic)",
    "convention", 6, "high", r"\item[b)]", r"\item[\textup{b)}]", "GLOBAL_ISSUES 16/88.")
add(128, "Proposition (18.5.4) b): 'Pour tout morphisme étale et séparé g : S′ → S'",
    "'étale et séparé' roman inside the italic statement (crop p128_s1a.png)", "italic", "convention", 6,
    "high", r"morphisme étale et séparé $g:S'\to S$", r"morphisme \textup{étale et séparé} $g:S'\to S$")
add(128, "Proposition (18.5.4), last sentence: 'La condition b) entraîne a′); ...'",
    "a new indented paragraph after 'est bijective.' (crop p128_s1a.png)",
    r"'La condition' follows \end{enumerate} without a blank line: no indent", "other", None, "high",
    "\\end{enumerate}\nLa condition", "\\end{enumerate}\n\nLa condition",
    "GLOBAL_ISSUES 80 pattern. Independent of the next finding (no overlap).")
add(128, "Proposition (18.5.4): 'La condition b) entraîne a′); si de plus S est quasi-compact et quasi-séparé, la condition a) entraîne b).'",
    "the four labels upright inside the italic statement (crop p128_s1a.png)",
    "$b)$, $a')$, $a)$, $b)$: italic letters", "convention", 6, "high",
    r"$b)$ entraîne $a')$; si de plus $S$ est quasi-compact et quasi-séparé, la condition $a)$ entraîne $b)$.",
    r"\textup{b)} entraîne \textup{a$'$)}; si de plus $S$ est quasi-compact et quasi-séparé, la condition \textup{a)} entraîne \textup{b)}.",
    "GLOBAL_ISSUES 88.")
add(128, "'Prouvons d'abord que b) entraîne a′). Supposons donc b) vérifiée'",
    "labels wholly italic in roman text (crop p128_s1b.png)", "$b)$, $a')$, $b)$: italic letter, upright parenthesis",
    "italics", None, "high",
    r"Prouvons d'abord que $b)$ entraîne $a')$. Supposons donc $b)$ vérifiée",
    r"Prouvons d'abord que \emph{b)} entraîne \emph{a$'$)}. Supposons donc \emph{b)} vérifiée",
    "GLOBAL_ISSUES 88.")
add(128, "commutative diagram, left vertical arrow Γ(P/S) → Of(S′)",
    "vertical tilde ≀ to the right of the arrow (crop p128_diag.png)", r"\ar[d]^{\sim} (horizontal tilde)",
    "symbol", None, "high", r"\Gamma(P/S)\ar[r]\ar[d]^{\sim}", r"\Gamma(P/S)\ar[r]\ar[d]^{\wr}")
add(128, "commutative diagram, right vertical arrow Γ(P_0/S_0) → Of(S′_0)",
    "vertical tilde ≀ to the right of the arrow (crop p128_diag.png)", r"\ar[d]^{\sim} (horizontal tilde)",
    "symbol", None, "high", r"\Gamma(P_0/S_0)\ar[d]^{\sim}", r"\Gamma(P_0/S_0)\ar[d]^{\wr}")
add(128, "'Comme l'hypothèse b), appliquée au morphisme P → S'", "label wholly italic in roman text (page_128_s2)",
    "$b)$", "italics", None, "high", r"Comme l'hypothèse $b)$, appliquée", r"Comme l'hypothèse \emph{b)}, appliquée",
    "GLOBAL_ISSUES 88.")
add(128, "'Avant de prouver que a) entraîne b) lorsque S est quasi-compact'", "labels wholly italic in roman text (page_128_s2)",
    "$a)$, $b)$", "italics", None, "high",
    r"Avant de prouver que $a)$ entraîne $b)$ lorsque", r"Avant de prouver que \emph{a)} entraîne \emph{b)} lorsque",
    "GLOBAL_ISSUES 88.")
add(128, "Lemme (18.5.4.3): 'vérifient la condition a) de (18.5.4), alors'",
    "label a) and (18.5.4) upright inside the italic statement (crop p128_s3a.png)", "italic",
    "convention", 6, "high", r"la condition $a)$ de (18.5.4), alors",
    r"la condition \textup{a)} de \textup{(18.5.4)}, alors", "GLOBAL_ISSUES 88.")
add(128, "Lemme (18.5.4.3): 'pour tout morphisme fini g : S′ → S'",
    "'fini' roman inside the italic statement (crop p128_s3a.png)", "italic", "convention", 6, "high",
    r"pour tout morphisme fini $g:S'\to S$, $S'$ est l'unique",
    r"pour tout morphisme \textup{fini} $g:S'\to S$, $S'$ est l'unique")
add(128, "proof of (18.5.4.3): 'la condition a) appliquée au morphisme h'", "label wholly italic in roman text (crop p128_s3a.png)",
    "$a)$", "italics", None, "high", r"la condition $a)$ appliquée au morphisme",
    r"la condition \emph{a)} appliquée au morphisme", "GLOBAL_ISSUES 88.")
add(128, "'prouvons d'abord que, sous l'hypothèse a), l'application (18.5.4.2) est injective'",
    "label wholly italic in roman text (crop p128_s3b.png)", "$a)$", "italics", None, "high",
    r"sous l'hypothèse $a)$, l'application (18.5.4.2) est \emph{injective}",
    r"sous l'hypothèse \emph{a)}, l'application (18.5.4.2) est \emph{injective}", "GLOBAL_ISSUES 88.")

# ---------------------------------------------------------------- p. 129
add(129, "'Reste à montrer que sous l'hypothèse a), l'application (18.5.4.2) est surjective' (printed at the bottom of p. 128)",
    "label wholly italic in roman text (crop p128_s4a.png)", "$a)$", "italics", None, "high",
    r"sous l'hypothèse $a)$, l'application (18.5.4.2) est \emph{surjective}",
    r"sous l'hypothèse \emph{a)}, l'application (18.5.4.2) est \emph{surjective}",
    "Printed on p. 128 but in the p. 129 segment of the TeX until the marker move below: apply this fix BEFORE the next two findings (after them the text lies in the p. 128 segment).")
add(129, "page break 128/129: where p. 129 begins",
    "the paragraph 'Reste à montrer que sous l'hypothèse a), ... u_0(S_0) étant quasi-compact dans S′, peut être recouvert par un nombre fini d'ouverts' is the last paragraph of p. 128 (page_128_s4, crop p128_s4a.png); p. 129 begins mid-sentence with 'affines V_i tels que la restriction g|V_i' at the left margin (page_129_s1)",
    r"\oldpage[IV-4]{129} stands before 'Reste à montrer' (three printed lines too early)", "marker", None, "high",
    "\\oldpage[IV-4]{129}\n\nReste à montrer", "Reste à montrer",
    "Marker move, part 1 of 2: removes the marker and the blank line after it (the blank line before it stays: it is the printed paragraph break before 'Reste'). Part 2 (next finding) re-inserts it before 'affines'. Apply both.")
add(129, "page break 128/129 (re-insertion of the marker)", "p. 129 begins with 'affines V_i' in mid-sentence",
    "no marker before 'affines'", "marker", None, "high",
    "un nombre fini d'ouverts affines $V_i$", "un nombre fini d'ouverts\n\\oldpage[IV-4]{129}\naffines $V_i$",
    "Marker move, part 2 of 2 with the previous finding; no blank lines (mid-sentence break). Apply both or neither.")
add(129, "'u_0 est une immersion fermée de S_0 dans S″_0 (I, 5.4.6)'", "bold I, then '5.4.6' (crop p129_s2a.png)",
    "plain I", "convention", 2, "high", "(I, 5.4.6)", r"(\textbf{I}, 5.4.6)",
    "Genuine reference to EGA I (bold I), not one of EGA IV's own (1.x.y).")
add(129, "'En vertu de l'hypothèse a), il existe'", "label wholly italic in roman text (crop p129_s2a.png)", "$a)$",
    "italics", None, "high", r"En vertu de l'hypothèse $a)$, il existe", r"En vertu de l'hypothèse \emph{a)}, il existe",
    "GLOBAL_ISSUES 88.")
add(129, "'Mais comme f|X est étale et fini, s ⇝ n(s) est continue'", "wavy arrow (crop p129_s2b.png)", r"\mapsto",
    "symbol", None, "high", r"s\mapsto n(s)", r"s\leadsto n(s)", "Wavy arrow in the print (GLOBAL_ISSUES 33 pattern).")
add(129, "'et comme X∩S′_0 = X_0, on a n(s) = 1 dans S_0'", "S′_0 with ONE prime (crop p129_Sp0.png)",
    r"X\cap S''_0=X_0", "formula", None, "high",
    r"et comme $X\cap S''_0=X_0$, on a", r"et comme $X\cap S'_0=X_0$, on a",
    "Not a misprint: X ⊂ S′ has just been shown, so X∩S′_0 = X∩S″_0 = X_0; the TeX repeats the earlier X∩S″_0 = X_0 instead of the printed reading.")
add(129, "Remarque (18.5.4.4): 'dans la condition b), on suppose'", "label wholly italic in the roman remark (page_129_s3)",
    "$b)$", "italics", None, "high", r"dans la condition $b)$, on suppose", r"dans la condition \emph{b)}, on suppose",
    "Judged as if the remark body were roman (document-wide remark item); GLOBAL_ISSUES 88.")
add(129, "Définition (18.5.5): 's'ils vérifient la condition a) de (18.5.4).'",
    "label a) and (18.5.4) upright inside the italic statement (crop p129_s3b.png)", "italic",
    "convention", 6, "high", r"s'ils vérifient la condition $a)$ de (18.5.4).",
    r"s'ils vérifient la condition \textup{a)} de \textup{(18.5.4)}.", "GLOBAL_ISSUES 88.")
add(129, "'Compte tenu de (I, 5.1.8)'", "bold I, then '5.1.8' (crop p129_s3b.png)", "plain I", "convention", 2, "high",
    "(I, 5.1.8)", r"(\textbf{I}, 5.1.8)", "Genuine reference to EGA I (bold I).")
add(129, "Proposition (18.5.6), label (i)", "upright (i) (crop p129_s3b.png)", r"\item[(i)] (italic)",
    "convention", 6, "high", r"\item[(i)]", r"\item[\textup{(i)}]", "GLOBAL_ISSUES 16.")
add(129, "Proposition (18.5.6), label (ii)", "upright (ii) (page_129_s4)", r"\item[(ii)] (italic)",
    "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]", "GLOBAL_ISSUES 16.")
add(129, "page break 129/130 inside 'il faut et il suffit que chacune | de ses restrictions g^(α)'",
    "p. 129 ends with 'que chacune' (no stop); p. 130 begins 'de ses restrictions' at the left margin (checked on page_130_s1)",
    r"blank line before \oldpage[IV-4]{130} (and another after it): a paragraph break inside the sentence",
    "marker", None, "high",
    "il faut et il suffit que chacune\n\n", "il faut et il suffit que chacune\n",
    "BOUNDARY FIX (page break with p. 130). The marker is at the right place; both blank lines around it must go (\\oldpage ends with \\ignorespaces, which does not skip a \\par). This removes the one before it; the one after \\oldpage[IV-4]{130} (before 'de ses restrictions') lies in the p. 130 segment (batch 130-134) and is not reported here.")

json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(F), "findings written")
