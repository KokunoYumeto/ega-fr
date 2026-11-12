import json, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = r'user\Documents\ega_scan_check_20261101\run_III2'
OUT = RUN + r'\findings_207_211.json'


def nl(s):
    return None if s is None else s.replace('¶', '\n')


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": nl(old), "new": nl(new)}}
    if kind == 'misprint_in_print':
        d["corrected"] = nl(corrected)
    d["note"] = note
    F.append(d)


C1 = "Convention 1: bold italic k of the residue field; ega3-7 writes Greek \\kappa (63 times in the file, never \\boldsymbol{k})."
C1S = "Convention 1 in a subscript: the print's k is bold upright here (GLOBAL_ISSUES item 48), hence \\mathbf{k}; ega3-7 writes Greek \\kappa."
C2 = "Bold chapter number in the reference (convention 2)."
C6R = "Reference set upright inside the italic statement (convention 6)."
C7 = "Long dash for the minus sign (convention 7, unary minus as in item 49); FIX_POLICY defers convention 7 to the \\setmin pass."
RT = ("Roman T in the print: the module-level functor T^{O_y}, T_i(k(y)); the TeX itself writes T_p^{\\mathscr O_y} with a roman T "
      "on pp. 202-206, so this is notation, not a misprint.")
RH = "Roundhand (second) script H of hypercohomology, as in (7.7.1.1) on p. 198; ega3-7 writes \\mathscr H. GLOBAL_ISSUES items 42/50: needs the roundhand-H macro, no page fix."

# ---------------------------------------------------------------- p. 207
add(207, "Lemma in the proof of (7.8.6): 'l'ensemble des z où s_z=1 est aussi ouvert (0_I, 5.5.2)'",
    "(𝟎_I, 5.5.2): bold 0", "($0_{\\mathrm I}$, 5.5.2)", "convention", 2, "high",
    r"($0_{\mathrm I}$, 5.5.2)", r"($\mathbf{0}_{\mathrm I}$, 5.5.2)", C2)
add(207, "Proof of (7.8.6): 'et que Γ(X'_i, O_{X'_i}) = k(y) pour tout i'",
    "bold italic k", "\\kappa(y)", "convention", 1, "high",
    r"\mathscr O_{X'_i})=\kappa(y)", r"\mathscr O_{X'_i})=\boldsymbol{k}(y)", C1)
add(207, "Proof of (7.8.6): 'telles que X'_i = X_i ⊗_Y k(y)'",
    "bold italic k", "\\kappa(y)", "convention", 1, "high",
    r"\otimes_Y\kappa(y)", r"\otimes_Y\boldsymbol{k}(y)", C1)
add(207, "Proof of (7.8.6): 'ramené au cas où R = k(y)'",
    "bold italic k", "\\kappa(y)", "convention", 1, "high",
    r"$R=\kappa(y)$", r"$R=\boldsymbol{k}(y)$", C1)
add(207, "Proof of (7.8.6): 'en vertu de (7.7.10, b))'",
    "'b)' italic (letter and its parenthesis); outer ')' roman", "b) upright", "italics", None, "high",
    r"(7.7.10, b))", r"(7.7.10, \emph{b)})", "Italic letter in the reference, as fixed elsewhere with \\emph{b)}.")
add(207, "Proof of (7.8.6): 'l'homomorphisme canonique Γ(X, O_X) → Γ(X_y, O_{X_y}) est surjectif'",
    "formula in the running text", "displayed with \\[ \\]", "other", None, "high",
    r"canonique¶\[¶  \Gamma(X,\mathscr O_X)¶  \longrightarrow¶  \Gamma(X_y,\mathscr O_{X_y})¶\]¶est surjectif",
    r"canonique¶$\Gamma(X,\mathscr O_X)\to\Gamma(X_y,\mathscr O_{X_y})$¶est surjectif",
    "Layout: the print sets this formula inline; the formula itself matches.")
add(207, "Proof of (7.8.6), display 'Γ(Y, O_Y) = A → Γ(X, O_X) → Γ(X_y, O_{X_y}) = k(y)'",
    "bold italic k", "\\kappa(y)", "convention", 1, "high",
    r"=\kappa(y)¶\]", r"=\boldsymbol{k}(y)¶\]", C1)
add(207, "Corollaire (7.8.7): 'Sous les hypothèses de (7.8.6), il existe'",
    "(7.8.6) upright in the italic statement", "italic (corollary environment)", "convention", 6, "high",
    r"[7.8.7]¶Sous les hypothèses de (7.8.6)", r"[7.8.7]¶Sous les hypothèses de \textup{(7.8.6)}", C6R)
add(207, "Corollaire (7.8.7), label (i)",
    "(i) upright", "\\item[(i)] italic in the corollary environment", "convention", 6, "high",
    r"\item[(i)] $f_*", r"\item[\textup{(i)}] $f_*", "Roman-numeral label upright in the print (GLOBAL_ISSUES item 16).")
add(207, "Corollaire (7.8.7), label (ii)",
    "(ii) upright", "\\item[(ii)] italic in the corollary environment", "convention", 6, "high",
    r"\item[(ii)] Pour tout", r"\item[\textup{(ii)}] Pour tout", "Roman-numeral label upright in the print (GLOBAL_ISSUES item 16).")
add(207, "Corollaire (7.8.7) (ii), display '(f_*(O_X))_z ⊗_{O_z} k(z) → Γ(X_z, O_{X_z})'",
    "bold italic k", "\\kappa(z)", "convention", 1, "high",
    r"\otimes_{\mathscr O_z}\kappa(z)", r"\otimes_{\mathscr O_z}\boldsymbol{k}(z)", C1)
add(207, "Corollaire (7.8.8): 'Supposons vérifiées les conditions de (7.8.6)'",
    "(7.8.6) upright in the italic statement", "italic (corollary environment)", "convention", 6, "high",
    r"conditions de (7.8.6) et en outre", r"conditions de \textup{(7.8.6)} et en outre", C6R)
add(207, "Corollaire (7.8.8): 'Γ(X_y, O_{X_y}) = k(y). Alors'",
    "bold italic k", "\\kappa(y)", "convention", 1, "high",
    r"=\kappa(y)$. Alors", r"=\boldsymbol{k}(y)$. Alors", C1)
add(207, "Corollaire (7.8.9): 'Sous les hypothèses de (7.8.6), il existe'",
    "(7.8.6) upright in the italic statement", "italic (corollary environment)", "convention", 6, "high",
    r"[7.8.9]¶Sous les hypothèses de (7.8.6)", r"[7.8.9]¶Sous les hypothèses de \textup{(7.8.6)}", C6R)
add(207, "Corollaire (7.8.9), first line: '(7.8.6), il existe un voisinage ouvert U de y,'",
    "the comma after (7.8.6) and 'il' in bold (bold italic 'il'; 2.5x crop beside the normal 'existe' and the normal comma after 'y')",
    "normal weight", "misprint_in_print", None, "high",
    r", il existe un voisinage ouvert $U$ de $y$, un", r"\textbf{, il} existe un voisinage ouvert $U$ de $y$, un",
    "Wrong-fount sorts. The TeX silently corrects; the fix reproduces the bold (\\textbf inside the italic statement gives bold italic).",
    corrected=r", il existe un voisinage ouvert $U$ de $y$, un")
add(207, "Corollaire (7.8.9): 'un isomorphisme de foncteurs en le O_U-Module quasi-cohérent M :'",
    "bold upright roman M (side-by-side crop with the normal roman A and U); the formula (7.8.9.1) has script M",
    "$\\mathscr M$", "misprint_in_print", None, "high",
    r"quasi-cohérent¶$\mathscr M$ :", r"quasi-cohérent¶$\mathbf M$ :",
    "Wrong-fount letter for script M. The TeX silently corrects; the fix restores the printed bold M.",
    corrected=r"quasi-cohérent¶$\mathscr M$ :")
add(207, "Proof of (7.8.9): 'l'équivalence de (7.7.5, a))'",
    "'a)' italic; outer ')' roman", "a) upright", "italics", None, "high",
    r"(7.7.5, a))", r"(7.7.5, \emph{a)})", "Italic letter in the reference.")
add(207, "Proof of (7.8.9): 'et (7.7.5, b'))'",
    "'b')' italic; outer ')' roman", "b$'$) upright", "italics", None, "high",
    r"(7.7.5, b$'$))", r"(7.7.5, \emph{b$'$)})", "Italic letter in the reference.")
add(207, "Remarques (7.8.10) (i), display 'X → Y' → Y' (Stein factorisation)",
    "no full stop after Y (3x crop); the sentence continues on p. 208 with 'avec Y' = ...'",
    "'& Y .' (full stop)", "punctuation", None, "high",
    r"\ar[r]^{g} & Y .", r"\ar[r]^{g} & Y", "Extra full stop in the TeX.")
add(207, "Boundary p. 207/208: blank line after the Stein display, before \\oldpage[III]{208}",
    "p. 208 begins 'avec Y' = Spec(f_*(O_X)) ; ...' flush left, continuing the sentence",
    "blank line after \\] (new paragraph)", "other", None, "high",
    r"}¶\]¶¶", r"}¶\]¶", "Spurious paragraph break at the page boundary (GLOBAL_ISSUES item 20).")

# ---------------------------------------------------------------- p. 208
add(208, "Remarques (7.8.10) (i): 'algèbre séparable sur k(y) (II, 1.5.1)'",
    "bold italic k", "\\kappa(y)", "convention", 1, "high",
    r"sur¶$\kappa(y)$", r"sur¶$\boldsymbol{k}(y)$", C1)
add(208, "Remarques (7.8.10) (i): '(II, 1.5.1)'",
    "bold II", "(II, 1.5.1)", "convention", 2, "high",
    r"(II, 1.5.1)", r"(\textbf{II}, 1.5.1)", C2)
add(208, "Remarques (7.8.10) (i): 'algèbre séparable sur k(z)'",
    "bold italic k", "\\kappa(z)", "convention", 1, "high",
    r"sur $\kappa(z)$", r"sur $\boldsymbol{k}(z)$", C1)
add(208, "Heading 7.9: '... et du polynôme de Hilbert.'",
    "the title ends with a full stop", "no full stop", "punctuation", None, "high",
    r"et du polynôme de Hilbert}", r"et du polynôme de Hilbert.}", "Printed final full stop (GLOBAL_ISSUES items 43/52).")
add(208, "(7.9.1.1), second member 'rang_p(M_p)'",
    "the subscript p of this rang looks bold Fraktur (8x stack: about 1.24x the ink of the first subscript, 1.12x that of M_p)",
    "\\mathfrak p", "misprint_in_print", None, "low",
    r"=\operatorname{rang}_{\mathfrak p}(M_{\mathfrak p})", r"=\operatorname{rang}_{\boldsymbol{\mathfrak p}}(M_{\mathfrak p})",
    "Possible wrong-fount sort; low confidence (ink gain, not a clear bold). Apply only after a look at the print.",
    corrected=r"=\operatorname{rang}_{\mathfrak p}(M_{\mathfrak p})")
add(208, "(7.9.1.1), third member: subscript k(p) of rang",
    "bold upright k (8x crop)", "\\kappa(\\mathfrak p)", "convention", 1, "high",
    r"=\operatorname{rang}_{\kappa(\mathfrak p)}¶  \bigl(M", r"=\operatorname{rang}_{\mathbf{k}(\mathfrak p)}¶  \bigl(M", C1S)
add(208, "(7.9.1.1), third member: 'M ⊗_A k(p)'",
    "bold italic k", "\\kappa(\\mathfrak p)", "convention", 1, "high",
    r"\otimes_A\kappa(\mathfrak p)\bigr).", r"\otimes_A\boldsymbol{k}(\mathfrak p)\bigr).", C1)
add(208, "(7.9.2.1), left member: '(—1)^i'",
    "long dash", "(-1)^i", "convention", 7, "high",
    r"on a¶\[¶  \sum_i(-1)^i", r"on a¶\[¶  \sum_i(\setmin 1)^i", C7)
add(208, "(7.9.2.1), left member: subscript k(p) of rang and 'T_i(k(p))'",
    "subscript k bold upright; k of T_i(k(p)) bold italic", "\\kappa(\\mathfrak p) twice", "convention", 1, "high",
    r"_{\kappa(\mathfrak p)}¶  T_i\bigl(\kappa(\mathfrak p)\bigr)¶  =",
    r"_{\mathbf{k}(\mathfrak p)}¶  T_i\bigl(\boldsymbol{k}(\mathfrak p)\bigr)¶  =",
    C1S + " This fix also covers the following finding (the k of T_i(k(p))): the two are only unique together.")
add(208, "(7.9.2.1), left member: 'T_i(k(p))'",
    "bold italic k", "\\kappa(\\mathfrak p)", "convention", 1, "high",
    None, None, C1 + " Included in the fix of the preceding finding.")
add(208, "(7.9.2.1), right member: '(—1)^i'",
    "long dash", "(-1)^i", "convention", 7, "high",
    r"\sum_i(-1)^i\operatorname{rang}_{\mathfrak p}", r"\sum_i(\setmin 1)^i\operatorname{rang}_{\mathfrak p}", C7)
add(208, "Proof of (7.9.2): 'T_i(k(p)) = H_i(P. ⊗_A k(p))', first k",
    "bold italic k", "\\kappa(\\mathfrak p)", "convention", 1, "high",
    r"$T_i(\kappa(\mathfrak p))=", r"$T_i(\boldsymbol{k}(\mathfrak p))=", C1)
add(208, "Proof of (7.9.2): 'T_i(k(p)) = H_i(P. ⊗_A k(p))', second k",
    "bold italic k", "\\kappa(\\mathfrak p)", "convention", 1, "high",
    r"\otimes_A\kappa(\mathfrak p))$", r"\otimes_A\boldsymbol{k}(\mathfrak p))$", C1)
add(208, "Proof of (7.9.2): 'la formule (7.9.1.2) n'est autre que'",
    "(7.9.1.2)", "(7.9.1.2) (keeps the printed reading)", "misprint_in_print", None, "high",
    None, None,
    "Wrong formula number: the formula proved is (7.9.2.1); no (7.9.1.2) exists. The TeX keeps the printed reading.",
    corrected=r"(7.9.2.1)")
add(208, "Proof of (7.9.2): 'par passage à l'homologie (0, 11.10.2)'",
    "(𝟎, 11.10.2): bold 0 with no subscript (crop)", "($0_{\\mathrm I}$, 11.10.2)", "extra", None, "high",
    r"($0_{\mathrm I}$, 11.10.2)", r"(\textbf{0}, 11.10.2)",
    "The TeX adds a subscript I; the print's (0, 11.10.2) is EGA III's form for chapter 0 §11 (0_I has no §11). The fix also sets the bold 0 (convention 2, next finding).")
add(208, "Proof of (7.9.2): same reference (0, 11.10.2)",
    "bold 0", "plain 0", "convention", 2, "high",
    None, None, C2 + " Included in the fix of the preceding finding.")
add(208, "Corollaire (7.9.3): 'p ⇝ Σ ...'",
    "wavy arrow (crop)", "\\longmapsto", "symbol", None, "high",
    r"\mathfrak p\longmapsto", r"\mathfrak p\leadsto", "Wavy arrow (\\leadsto), not convention 3; GLOBAL_ISSUES item 33.")
add(208, "Corollaire (7.9.3): '(—1)^i'",
    "long dash", "(-1)^i", "convention", 7, "high",
    None, None,
    C7 + " No unique 'old' disjoint from the neighbouring fixes: it is the (-1) of the line after '\\mathfrak p\\longmapsto' in (7.9.3); give it to the global pass.")
add(208, "Corollaire (7.9.3): subscript k(p) of rang and 'T_i(k(p))'",
    "subscript k bold upright; k of T_i(k(p)) bold italic", "\\kappa(\\mathfrak p) twice", "convention", 1, "high",
    r"_{\kappa(\mathfrak p)}¶  T_i\bigl(\kappa(\mathfrak p)\bigr)¶\]",
    r"_{\mathbf{k}(\mathfrak p)}¶  T_i\bigl(\boldsymbol{k}(\mathfrak p)\bigr)¶\]",
    C1S + " This fix also covers the following finding (the k of T_i(k(p))).")
add(208, "Corollaire (7.9.3): 'T_i(k(p))'",
    "bold italic k", "\\kappa(\\mathfrak p)", "convention", 1, "high",
    None, None, C1 + " Included in the fix of the preceding finding.")
add(208, "Théorème (7.9.4): 'Si l'on pose T.(M) = H^.(f, P^. ⊗_{O_Y} M) (cf. (7.7.1.1)) la fonction', opening",
    "formula in the running text, on the line of the statement", "displayed with \\[ \\]", "other", None, "high",
    r"Si l'on pose¶\[¶  \mathscr T_\bullet(\mathscr M)", r"Si l'on pose¶$\mathscr T_\bullet(\mathscr M)",
    "Layout: the print sets the formula inline. Opening half; apply together with the next finding (closing half).")
add(208, "Théorème (7.9.4): same formula, closing, with '(cf. (7.7.1.1))'",
    "formula inline; '(cf. (7.7.1.1))' upright in the italic statement", "end of the display; \\text{(cf. ...)} italic",
    "other", None, "high",
    r"\mathscr M\bigr)¶  \qquad\text{(cf. (7.7.1.1))}¶\]¶", r"\mathscr M\bigr)$ \textup{(cf. (7.7.1.1))}¶",
    "Closing half of the inline conversion; apply together with the preceding finding. Also sets the convention-6 \\textup.")
add(208, "Théorème (7.9.4): '(cf. (7.7.1.1))'",
    "upright in the italic statement", "italic (\\text inside the theorem environment)", "convention", 6, "high",
    None, None, C6R + " Included in the fix of the preceding finding.")
add(208, "Théorème (7.9.4): 'T.(M) = H^.(f, P^. ⊗_{O_Y} M)'",
    "H with superscript bullet only, no minus (4x crop); (7.7.1.1) on p. 198 prints H^{-n}",
    "\\mathscr H^{-\\bullet}", "misprint_in_print", None, "medium",
    r"=\mathscr H^{-\bullet}", r"=\mathscr H^{\bullet}",
    "The print drops the minus of (7.7.1.1), which it cites. The TeX silently corrects; the fix restores the printed reading. Disjoint from the two display halves.",
    corrected=r"=\mathscr H^{-\bullet}")
add(208, "Théorème (7.9.4): H^.(f, ...)",
    "roundhand hypercohomology H", "\\mathscr H", "font", None, "high", None, None, RH)
add(208, "Boundary p. 208/209: blank line after 'la fonction', before \\oldpage[III]{209}",
    "p. 209 begins with the display (7.9.4.1); the sentence continues", "blank line before the marker and the display",
    "other", None, "high",
    r"la fonction¶¶", r"la fonction¶", "Spurious paragraph break before the display (GLOBAL_ISSUES item 20).")

# ---------------------------------------------------------------- p. 209
add(209, "(7.9.4.1): 'y ⇝ Σ ...'",
    "wavy arrow (3x crop)", "\\longmapsto", "symbol", None, "high",
    r"y\longmapsto", r"y\leadsto", "Wavy arrow (\\leadsto), not convention 3; GLOBAL_ISSUES item 33.")
add(209, "(7.9.4.1): '(—1)^i'",
    "long dash", "(-1)^i", "convention", 7, "high",
    r"\sum_i(-1)^i\operatorname{rang}", r"\sum_i(\setmin 1)^i\operatorname{rang}", C7)
add(209, "(7.9.4.1): subscript k(y) of rang",
    "bold upright k", "\\kappa(y)", "convention", 1, "high",
    r"_{\kappa(y)}", r"_{\mathbf{k}(y)}", C1S)
add(209, "(7.9.4.1): 'T_i(k(y))'",
    "roman T_i (3x crop)", "\\mathscr T_i", "font", None, "high",
    r"\mathscr T_i\bigl", r"T_i\bigl", RT)
add(209, "(7.9.4.1): 'T_i(k(y))', the k",
    "bold italic k", "\\kappa(y)", "convention", 1, "high",
    r"(\kappa(y)\bigr)", r"(\boldsymbol{k}(y)\bigr)", C1)
add(209, "Proof of (7.9.4): 'qu'on a T_p(M) = H_p(L. ⊗_{O_Y} M), où L. = L~.,'",
    "formula in the running text, with 'où' before L. = L~.", "displayed, '\\qquad' instead of 'où'", "missing", None, "high",
    r"qu'on a¶\[¶  \mathscr T_p(\mathscr M)¶  =\mathscr H_p(\mathscr L_\bullet\otimes_{\mathscr O_Y}\mathscr M),¶  \qquad \mathscr L_\bullet=\widetilde{L_\bullet},¶\]¶",
    r"qu'on a¶$\mathscr T_p(\mathscr M)=\mathscr H_p(\mathscr L_\bullet\otimes_{\mathscr O_Y}\mathscr M)$, où¶$\mathscr L_\bullet=\widetilde{L}_\bullet$,¶",
    "The word 'où' is missing (item 51 pattern). The fix also sets the formula inline, as printed, and applies convention 8 (next finding).")
add(209, "Proof of (7.9.4): 'L. = L~.'",
    "tilde over L only", "\\widetilde{L_\\bullet}", "convention", 8, "high",
    None, None, "Convention 8. Included in the fix of the preceding finding.")
add(209, "(7.9.5): 'la caractéristique d'Euler-Poincaré de P.'",
    "only 'caractéristique d'Euler-Poincaré' italic; 'de' roman (crop)", "\\emph covers 'de $\\mathscr P_\\bullet$'",
    "italics", None, "high",
    r"\emph{caractéristique d'Euler-Poincaré de $\mathscr P_\bullet$}",
    r"\emph{caractéristique d'Euler-Poincaré} de $\mathscr P_\bullet$", "Emphasis too wide in the TeX.")
add(209, "(7.9.5): 'par EP(f, P.) ou EP(Y, P.), ou simplement EP(P.) s'il ne peut'",
    "formulas in the running text", "displayed with \\quad\\text{ou}\\quad", "other", None, "high",
    r"par¶\[¶  \operatorname{EP}(f,\mathscr P_\bullet)¶  \quad\text{ou}\quad¶  \operatorname{EP}(Y,\mathscr P_\bullet),¶  \quad\text{ou simplement}\quad¶  \operatorname{EP}(\mathscr P_\bullet)¶\]¶",
    r"par $\operatorname{EP}(f,\mathscr P_\bullet)$ ou $\operatorname{EP}(Y,\mathscr P_\bullet)$, ou simplement¶$\operatorname{EP}(\mathscr P_\bullet)$¶",
    "Layout: the print sets these inline; words and formulas match.")
add(209, "(7.9.5): 'on notera aussi EP(f, P.; y) ou EP(Y, P.; y) ou EP(P.; y) le second membre'",
    "formulas in the running text", "displayed with \\quad\\text{ou}\\quad", "other", None, "high",
    r"aussi¶\[¶  \operatorname{EP}(f,\mathscr P_\bullet;y)¶  \quad\text{ou}\quad¶  \operatorname{EP}(Y,\mathscr P_\bullet;y)¶  \quad\text{ou}\quad¶  \operatorname{EP}(\mathscr P_\bullet;y)¶\]¶",
    r"aussi $\operatorname{EP}(f,\mathscr P_\bullet;y)$ ou $\operatorname{EP}(Y,\mathscr P_\bullet;y)$ ou¶$\operatorname{EP}(\mathscr P_\bullet;y)$¶",
    "Layout: the print sets these inline; words and formulas match.")
add(209, "(7.9.6), exact sequence, start",
    "the sequence starts with an arrow '→ T_i(P'., k(y))', no dots (crop)", "\\cdots\\longrightarrow", "extra", None, "high",
    r"\cdots\longrightarrow", r"\longrightarrow", "Extra leading dots in the TeX.")
add(209, "(7.9.6), exact sequence: 'T_i(P'., k(y))'",
    "bold italic k", "\\kappa(y)", "convention", 1, "high",
    r"\mathscr T_i(\mathscr P'_\bullet,\kappa(y))", r"\mathscr T_i(\mathscr P'_\bullet,\boldsymbol{k}(y))", C1)
add(209, "(7.9.6), exact sequence: 'T_{i+2d}(P., k(y))'",
    "bold italic k", "\\kappa(y)", "convention", 1, "high",
    r"\mathscr T_{i+2d}(\mathscr P_\bullet,\kappa(y))", r"\mathscr T_{i+2d}(\mathscr P_\bullet,\boldsymbol{k}(y))", C1)
add(209, "(7.9.6), exact sequence: 'T_{i+2d+2d'}(P''., k(y))'",
    "bold italic k", "\\kappa(y)", "convention", 1, "high",
    r"(\mathscr P''_\bullet,\kappa(y))", r"(\mathscr P''_\bullet,\boldsymbol{k}(y))", C1)
add(209, "(7.9.6), exact sequence: 'T_{i-1}(P'., k(y))'",
    "bold italic k", "\\kappa(y)", "convention", 1, "high",
    r"\mathscr T_{i-1}(\mathscr P'_\bullet,\kappa(y))", r"\mathscr T_{i-1}(\mathscr P'_\bullet,\boldsymbol{k}(y))", C1)
add(209, "(7.9.6), exact sequence, end '→ ...'",
    "baseline dots", "\\cdots", "symbol", None, "high",
    r"\longrightarrow\cdots", r"\longrightarrow\ldots", "Baseline dots (GLOBAL_ISSUES item 22), as \\ldots elsewhere.")
add(209, "(7.9.6): 'est nulle (0, 11.10.1), il vient aussitôt'",
    "(𝟎, 11.10.1): bold 0 with no subscript (crop)", "($0_{\\mathrm I}$, 11.10.1)", "extra", None, "high",
    r"($0_{\mathrm I}$,¶11.10.1)", r"(\textbf{0},¶11.10.1)",
    "The TeX adds a subscript I (0_I has no §11). The fix also sets the bold 0 (convention 2, next finding).")
add(209, "(7.9.6): same reference (0, 11.10.1)",
    "bold 0", "plain 0", "convention", 2, "high",
    None, None, C2 + " Included in the fix of the preceding finding.")
add(209, "(7.9.6), diagram of complexes: vertical arrows",
    "four vertical arrows between consecutive rows, under each of the four objects (crop)",
    "\\ar[d] only in the first three object columns: the fourth column (0 / P_2 / P_2 / 0) has none", "missing", None, "high",
    r"\xymatrix@C=2.4em{¶  \cdots \ar[r] & 0 \ar[r]\ar[d] & 0 \ar[r]\ar[d]¶    & 0 \ar[r]\ar[d] & 0 \ar[r] & \cdots \\¶  \cdots \ar[r] & 0 \ar[r]\ar[d] & 0 \ar[r]\ar[d]¶    & \mathscr P_1 \ar[r]\ar[d] & \mathscr P_2 \ar[r] & \cdots \\¶  \cdots \ar[r] & 0 \ar[r]\ar[d] & \mathscr P_0 \ar[r]\ar[d]¶    & \mathscr P_1 \ar[r]\ar[d] & \mathscr P_2 \ar[r] & \cdots \\¶  \cdots \ar[r] & 0 \ar[r]\ar[d] & \mathscr P_0 \ar[r]\ar[d]¶    & 0 \ar[r]\ar[d] & 0 \ar[r] & \cdots \\¶  \cdots \ar[r] & 0 \ar[r] & 0 \ar[r]¶    & 0 \ar[r] & 0 \ar[r] & \cdots¶}",
    r"\xymatrix@C=2.4em{¶  \ldots \ar[r] & 0 \ar[r]\ar[d] & 0 \ar[r]\ar[d]¶    & 0 \ar[r]\ar[d] & 0 \ar[r]\ar[d] & \ldots \\¶  \ldots \ar[r] & 0 \ar[r]\ar[d] & 0 \ar[r]\ar[d]¶    & \mathscr P_1 \ar[r]\ar[d] & \mathscr P_2 \ar[r]\ar[d] & \ldots \\¶  \ldots \ar[r] & 0 \ar[r]\ar[d] & \mathscr P_0 \ar[r]\ar[d]¶    & \mathscr P_1 \ar[r]\ar[d] & \mathscr P_2 \ar[r]\ar[d] & \ldots \\¶  \ldots \ar[r] & 0 \ar[r]\ar[d] & \mathscr P_0 \ar[r]\ar[d]¶    & 0 \ar[r]\ar[d] & 0 \ar[r]\ar[d] & \ldots \\¶  \ldots \ar[r] & 0 \ar[r] & 0 \ar[r]¶    & 0 \ar[r] & 0 \ar[r] & \ldots¶}",
    "Four vertical arrows are missing (fourth column, all four gaps). The fix also changes the row-end dots to baseline dots (next finding); rows and objects otherwise match.")
add(209, "(7.9.6), diagram of complexes: dots at both ends of the five rows",
    "baseline dots", "\\cdots (10 times)", "symbol", None, "high",
    None, None, "Baseline dots (GLOBAL_ISSUES item 22). Included in the fix of the preceding finding.")
add(209, "(7.9.6.2): '(—1)^i'",
    "long dash", "(-1)^i", "convention", 7, "high",
    r"(-1)^i\operatorname{EP}", r"(\setmin 1)^i\operatorname{EP}", C7)
add(209, "(7.9.6.2): 'Σ(—1)^i EP(P_i; y)'",
    "Σ with no index (taller crop)", "\\sum_i", "extra", None, "high",
    r"=\sum_i", r"=\sum", "No summation index in the print here (it does have one in (7.9.4.1) and (7.9.12.2)).")
add(209, "(7.9.6.2), end of the formula",
    "no full stop; the sentence continues on p. 210 with 'où, pour tout ...'", "full stop after the formula",
    "punctuation", None, "high",
    r"(\mathscr P_i;y).¶", r"(\mathscr P_i;y)¶", "Extra full stop in the TeX.")
add(209, "Boundary p. 209/210: blank line after the display (7.9.6.2), before \\oldpage[III]{210}",
    "p. 210 begins 'où, pour tout O_X-Module ...' flush left, continuing the sentence", "blank line after \\]",
    "other", None, "high",
    r"\label{III.7.9.6.2.fr}¶\]¶¶", r"\label{III.7.9.6.2.fr}¶\]¶", "Spurious paragraph break at the page boundary (GLOBAL_ISSUES item 20).")

# ---------------------------------------------------------------- p. 210
add(210, "Proposition (7.9.7): 'Sous les hypothèses de (7.9.4), soient'",
    "(7.9.4) upright in the italic statement", "italic (proposition environment)", "convention", 6, "high",
    r"Sous les hypothèses de (7.9.4), soient", r"Sous les hypothèses de \textup{(7.9.4)}, soient", C6R)
add(210, "Proposition (7.9.7): 'un morphisme, X' = X ×_Y Y', f' = f_(Y') : X' → Y','",
    "formulas in the running text", "displayed with \\qquad", "other", None, "high",
    r"un morphisme,¶\[¶  X'=X\times_Y Y',¶  \qquad f'=f_{(Y')}:X'\longrightarrow Y',¶\]¶",
    r"un morphisme, $X'=X\times_Y Y'$, $f'=f_{(Y')}:X'\to Y'$,¶", "Layout: the print sets these inline.")
add(210, "Proposition (7.9.7): 'P'. le complexe fini P. ⊗_{O_Y} O_{Y'} de O_{X'}-Modules'",
    "formula in the running text", "displayed", "other", None, "high",
    r"le complexe fini¶\[¶  \mathscr P_\bullet\otimes_{\mathscr O_Y}\mathscr O_{Y'}¶\]¶",
    r"le complexe fini¶$\mathscr P_\bullet\otimes_{\mathscr O_Y}\mathscr O_{Y'}$¶", "Layout: the print sets this inline.")
add(210, "Proof of (7.9.7): 'en vertu de (0_I, 6.2.1)'",
    "bold 0", "($0_{\\mathrm I}$, 6.2.1)", "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.2.1)", r"($\mathbf{0}_{\mathrm I}$, 6.2.1)", C2)
add(210, "Proof of (7.9.7): 'et (1.4.14.5), la question étant locale'",
    "(1.4.14.5): old-style figure 1 (x-height, like the 1 of 6.2.1) and a full stop, not a bold I and a comma (4x crop); p. 212 prints the same (1.4.14.5)",
    "(I, 4.14.5)", "misprint_in_print", None, "medium",
    r"(I, 4.14.5)", r"(1.4.14.5)",
    "The printed reference is defective: EGA III has no (1.4.14.5) ((1.4.14) has no sub-items) and EGA I (1960) has no 4.14.5. The TeX's (I, 4.14.5) is a conjectural correction; 'corrected' repeats it but the intended target is unverified. Treat p. 212 (TeX line 3777) the same way.",
    corrected=r"(I, 4.14.5)")
add(210, "Proof of (7.9.7): 'on sait que f' est propre (II, 5.4.2)'",
    "bold II", "(II, 5.4.2)", "convention", 2, "high",
    r"(II, 5.4.2)", r"(\textbf{II}, 5.4.2)", C2)
add(210, "Proposition (7.9.8): 'hypothèses de (7.9.4) et en outre'",
    "(7.9.4) upright in the italic statement", "italic (proposition environment)", "convention", 6, "high",
    r"hypothèses de (7.9.4) et en outre", r"hypothèses de \textup{(7.9.4)} et en outre", C6R)
add(210, "Proposition (7.9.8): 'tel que T_i(k(y)) = 0 pour i ≠ i_0 et tout y ∈ Y.'",
    "formula in the running text; roman T_i; bold italic k", "displayed; \\mathscr T_i; \\kappa(y)", "other", None, "high",
    r"tel que¶\[¶  \mathscr T_i(\kappa(y))=0¶  \qquad\text{pour $i\ne i_0$ et tout $y\in Y$.}¶\]¶",
    r"tel que $T_i(\boldsymbol{k}(y))=0$ pour $i\ne i_0$ et tout $y\in Y$.¶",
    "Layout: the print sets this inline. The fix also sets the roman T and the bold k (next two findings).")
add(210, "Proposition (7.9.8): 'T_i(k(y)) = 0'",
    "roman T_i", "\\mathscr T_i", "font", None, "high", None, None, RT + " Included in the fix of the preceding finding.")
add(210, "Proposition (7.9.8): 'T_i(k(y)) = 0', the k",
    "bold italic k", "\\kappa(y)", "convention", 1, "high", None, None, C1 + " Included in the fix of the display finding above.")
add(210, "Proposition (7.9.8): 'Alors T_{i_0}(O_Y) = H^{-i_0}(f, P.) est un O_Y-Module'",
    "formula in the running text", "displayed", "other", None, "high",
    r"Alors¶\[¶  \mathscr T_{i_0}(\mathscr O_Y)¶  =\mathscr H^{-i_0}(f,\mathscr P_\bullet)¶\]¶",
    r"Alors $\mathscr T_{i_0}(\mathscr O_Y)=\mathscr H^{-i_0}(f,\mathscr P_\bullet)$¶", "Layout: the print sets this inline.")
add(210, "Proposition (7.9.8): H^{-i_0}(f, P.)",
    "roundhand hypercohomology H", "\\mathscr H", "font", None, "high", None, None, RH)
add(210, "Proposition (7.9.8): '(—1)^{i_0} EP(f, P.; y)'",
    "long dash", "(-1)^{i_0}", "convention", 7, "high",
    r"$(-1)^{i_0}\operatorname{EP}(f,\mathscr P_\bullet;y)$", r"$(\setmin 1)^{i_0}\operatorname{EP}(f,\mathscr P_\bullet;y)$", C7)
add(210, "Proof of (7.9.8): 'vérifiées par les T_j^{O_y}'",
    "roman T", "\\mathscr T_j^{\\mathscr O_y}", "font", None, "high",
    r"$\mathscr T_j^{\mathscr O_y}$", r"$T_j^{\mathscr O_y}$", RT)
add(210, "Proof of (7.9.8): 'entraîne que T_i^{O_y} est nul'",
    "roman T", "\\mathscr T_i^{\\mathscr O_y}", "font", None, "high",
    r"$\mathscr T_i^{\mathscr O_y}$", r"$T_i^{\mathscr O_y}$", RT)
add(210, "Proof of (7.9.8): 'H^{-i_0}(f, P.) est localement libre'",
    "roundhand hypercohomology H", "\\mathscr H", "font", None, "high", None, None, RH)
add(210, "Proof of (7.9.8), display 'rang_{k(y)} T_{i_0}(k(y)) = EP(f, P.; y)'",
    "roman T_{i_0}; subscript k bold upright; k of T_{i_0}(k(y)) bold italic", "\\mathscr T_{i_0}; \\kappa(y) twice",
    "font", None, "high",
    r"\operatorname{rang}_{\kappa(y)}¶  \mathscr T_{i_0}(\kappa(y))",
    r"\operatorname{rang}_{\mathbf{k}(y)}¶  T_{i_0}(\boldsymbol{k}(y))",
    RT + " The fix also sets the two k (next two findings).")
add(210, "Proof of (7.9.8), display: subscript k(y) of rang",
    "bold upright k", "\\kappa(y)", "convention", 1, "high", None, None, C1S + " Included in the fix of the preceding finding.")
add(210, "Proof of (7.9.8), display: 'T_{i_0}(k(y))', the k",
    "bold italic k", "\\kappa(y)", "convention", 1, "high", None, None, C1 + " Included in the fix of the display finding above.")
add(210, "Proof of (7.9.8), display 'rang_{k(y)} T_{i_0}(k(y)) = EP(f, P.; y)'",
    "no sign factor", "no sign factor (keeps the printed reading)", "misprint_in_print", None, "medium",
    None, None,
    "Since EP(f, P.; y) = Σ(-1)^i rang T_i(k(y)) and T_i(k(y)) = 0 for i ≠ i_0, the rank equals (-1)^{i_0} EP(f, P.; y), as the statement says; the display omits the sign. The TeX keeps the printed reading.",
    corrected=r"=(-1)^{i_0}\operatorname{EP}(f,\mathscr P_\bullet;y)")
add(210, "Proof of (7.9.8): 'puisque T_i(k(y)) = 0 pour i ≠ i_0'",
    "roman T_i", "\\mathscr T_i", "font", None, "high",
    r"puisque $\mathscr T_i(", r"puisque $T_i(", RT)
add(210, "Proof of (7.9.8): 'puisque T_i(k(y)) = 0', the k",
    "bold italic k", "\\kappa(y)", "convention", 1, "high",
    r"\kappa(y))=0$ pour $i\ne i_0$.", r"\boldsymbol{k}(y))=0$ pour $i\ne i_0$.", C1)
add(210, "Corollaire (7.9.9): 'H^i(f^{-1}(y), F ⊗_{O_Y} k(y)) = 0 pour tout i ≠ i_0 et tout y ∈ Y.'",
    "formula in the running text; bold italic k", "displayed; \\kappa(y)", "other", None, "high",
    r"tel que¶\[¶  H^i\bigl(f^{-1}(y),¶  \mathscr F\otimes_{\mathscr O_Y}\kappa(y)\bigr)=0¶  \qquad\text{pour tout $i\ne i_0$ et tout $y\in Y$.}¶\]¶",
    r"tel que¶$H^i\bigl(f^{-1}(y),\mathscr F\otimes_{\mathscr O_Y}\boldsymbol{k}(y)\bigr)=0$ pour tout $i\ne i_0$ et tout $y\in Y$.¶",
    "Layout: the print sets this inline. The fix also sets the bold k (next finding).")
add(210, "Corollaire (7.9.9): 'F ⊗_{O_Y} k(y)'",
    "bold italic k", "\\kappa(y)", "convention", 1, "high", None, None, C1 + " Included in the fix of the preceding finding.")
add(210, "Corollaire (7.9.9): '(—1)^{i_0} EP(f, F; y)'",
    "long dash", "(-1)^{i_0}", "convention", 7, "high",
    r"$(-1)^{i_0}\operatorname{EP}(f,\mathscr F;y)$", r"$(\setmin 1)^{i_0}\operatorname{EP}(f,\mathscr F;y)$", C7)
add(210, "Corollaire (7.9.10): 'Sous les conditions préliminaires de (7.9.9)'",
    "(7.9.9) upright in the italic statement", "italic (corollary environment)", "convention", 6, "high",
    r"préliminaires de (7.9.9)", r"préliminaires de \textup{(7.9.9)}", C6R)
add(210, "Lemme (7.9.10.1): 'Sous les hypothèses de (7.9.10)'",
    "(7.9.10) upright in the italic statement", "italic (lemma environment)", "convention", 6, "high",
    r"hypothèses de (7.9.10)", r"hypothèses de \textup{(7.9.10)}", C6R)
add(210, "Lemme (7.9.10.1): 'on a H^i(f^{-1}(y), F ⊗_{O_Y} k(y)) = 0 pour tout i > 0'",
    "formula in the running text, on the heading line; bold italic k", "displayed; \\kappa(y)", "other", None, "high",
    r"on a¶\[¶  H^i\bigl(f^{-1}(y),¶  \mathscr F\otimes_{\mathscr O_Y}\kappa(y)\bigr)=0¶\]¶",
    r"on a $H^i\bigl(f^{-1}(y),\mathscr F\otimes_{\mathscr O_Y}\boldsymbol{k}(y)\bigr)=0$¶",
    "Layout: the print sets this inline. The fix also sets the bold k (next finding).")
add(210, "Lemme (7.9.10.1): 'F ⊗_{O_Y} k(y)'",
    "bold italic k", "\\kappa(y)", "convention", 1, "high", None, None, C1 + " Included in the fix of the preceding finding.")
add(210, "Proof of (7.9.10.1): 'l'équivalence de (7.7.5, a))'",
    "'a)' italic; outer ')' roman", "a) upright", "italics", None, "high",
    r"(7.7.5, a))", r"(7.7.5, \emph{a)})", "Italic letter in the reference.")
add(210, "Proof of (7.9.10.1): 'et (7.7.5, d))'",
    "'d)' italic; outer ')' roman", "d) upright", "italics", None, "high",
    r"(7.7.5, d))", r"(7.7.5, \emph{d)})", "Italic letter in the reference.")

# ---------------------------------------------------------------- p. 211
add(211, "Proposition (7.9.11): 'Les hypothèses étant celles de (7.9.4)'",
    "(7.9.4) upright in the italic statement", "italic (proposition environment)", "convention", 6, "high",
    r"celles de (7.9.4), soit", r"celles de \textup{(7.9.4)}, soit", C6R)
add(211, "(7.9.11.1): 'n ⇝ EP(f, P.(n); y)'",
    "wavy arrow", "\\longmapsto", "symbol", None, "high",
    r"n\longmapsto\operatorname{EP}", r"n\leadsto\operatorname{EP}", "Wavy arrow (\\leadsto), not convention 3; GLOBAL_ISSUES item 33.")
add(211, "Proposition (7.9.11): 'pour tous les points d'une même composante connexe'",
    "'d'une' in bold italic (crop beside the normal italic words of the line)", "normal italic", "misprint_in_print", None, "high",
    r"points d'une même", r"points \textbf{d'une} même",
    "Wrong-fount word. The TeX silently corrects; the fix reproduces the bold (bold italic in the statement).",
    corrected=r"points d'une même")
add(211, "Proof of (7.9.11): 'complexe de O_X-Modules Y-plats.'",
    "'plats' italic", "upright", "italics", None, "high",
    r"$Y$-plats. En vertu", r"$Y$-\emph{plats}. En vertu", "Printed emphasis missing in the TeX.")
add(211, "Proof of (7.9.11): 'on peut se borner au cas où P. est réduit'",
    "'au' and 'où' in bold, 'cas' normal (3x crop)", "normal weight", "misprint_in_print", None, "high",
    r"se borner au cas¶où $\mathscr P_\bullet$", r"se borner \textbf{au} cas¶\textbf{où} $\mathscr P_\bullet$",
    "Wrong-fount words. The TeX silently corrects; the fix reproduces the bold.",
    corrected=r"se borner au cas¶où $\mathscr P_\bullet$")
add(211, "Proof of (7.9.11): 'f projectif (II, 5.5.3)'",
    "bold II", "(II, 5.5.3)", "convention", 2, "high",
    r"projectif (II, 5.5.3) ; posons", r"projectif (\textbf{II}, 5.5.3) ; posons", C2)
add(211, "Proof of (7.9.11): 'L_y = L ⊗_{O_Y} k(y)'",
    "bold italic k", "\\kappa(y)", "convention", 1, "high",
    r"\mathscr L\otimes_{\mathscr O_Y}\kappa(y)$", r"\mathscr L\otimes_{\mathscr O_Y}\boldsymbol{k}(y)$", C1)
add(211, "Proof of (7.9.11): 'très ample (II, 4.4.10)'",
    "bold II", "(II, 4.4.10)", "convention", 2, "high",
    r"(II, 4.4.10)", r"(\textbf{II}, 4.4.10)", C2)
add(211, "Proof of (7.9.11): 'P.(n), T_i(k(y)) = H^{-i}(X_y, F_y ⊗ L_y^{⊗n}) (où F_y = F ⊗_{O_y} k(y)) ; d'où'",
    "formula in the running text; roman T_i; subscript O_y (lowercase y); bold italic k twice",
    "displayed; \\mathscr T_i; \\otimes_{\\mathscr O_Y}; \\kappa(y) twice", "other", None, "high",
    r"$\mathscr P_\bullet(n)$,¶\[¶  \mathscr T_i(\kappa(y))¶  =H^{-i}(X_y,\mathscr F_y\otimes\mathscr L_y^{\otimes n})¶  \qquad¶  \bigl(\text{où }\mathscr F_y=\mathscr F\otimes_{\mathscr O_Y}\kappa(y)\bigr) ;¶\]¶",
    r"$\mathscr P_\bullet(n)$, $T_i(\boldsymbol{k}(y))=H^{-i}(X_y,\mathscr F_y\otimes\mathscr L_y^{\otimes n})$¶(où $\mathscr F_y=\mathscr F\otimes_{\mathscr O_y}\boldsymbol{k}(y)$) ;¶",
    "Layout: the print sets this inline. The fix also covers the next four findings (roman T, O_y, two bold k).")
add(211, "Proof of (7.9.11): 'T_i(k(y)) = H^{-i}(...)'",
    "roman T_i", "\\mathscr T_i", "font", None, "high", None, None, RT + " Included in the fix of the preceding finding.")
add(211, "Proof of (7.9.11): '(où F_y = F ⊗_{O_y} k(y))'",
    "subscript O_y with lowercase y (4x side-by-side crop with the O_Y of 'L ⊗_{O_Y} k(y)' two lines up)",
    "\\otimes_{\\mathscr O_Y}", "formula", None, "high", None, None, "Included in the fix of the display finding above.")
add(211, "Proof of (7.9.11): 'T_i(k(y))', the k",
    "bold italic k", "\\kappa(y)", "convention", 1, "high", None, None, C1 + " Included in the fix of the display finding above.")
add(211, "Proof of (7.9.11): 'F ⊗_{O_y} k(y)', the k",
    "bold italic k", "\\kappa(y)", "convention", 1, "high", None, None, C1 + " Included in the fix of the display finding above.")
add(211, "Proof of (7.9.11): 'la caractéristique d'Euler-Poincaré χ_{k(y)}(F_y(n))'",
    "bold upright k in the subscript", "\\kappa(y)", "convention", 1, "high",
    r"$\chi_{\kappa(y)}(", r"$\chi_{\mathbf{k}(y)}(", C1S)
add(211, "'Nous désignerons par PH(f, P.; y) ...': start of (7.9.12)",
    "this paragraph has no number; the bold number (7.9.12) heads the paragraph 'Avec les notations de (7.9.6) et (7.9.11), on a'",
    "\\begin{env}[7.9.12] before 'Nous désignerons'", "number", None, "high",
    r"\begin{env}[7.9.12]¶\label{III.7.9.12.fr}¶Nous désignerons", r"Nous désignerons",
    "Paragraph number on the wrong paragraph. Apply together with the next finding, which reopens the environment at 'Avec les notations'.")
add(211, "(7.9.12): 'Avec les notations de (7.9.6) et (7.9.11), on a'",
    "'(7.9.12)' printed here", "second paragraph inside the env", "number", None, "high",
    r"donné.¶¶Avec les notations", r"donné.¶¶\begin{env}[7.9.12]¶\label{III.7.9.12.fr}¶Avec les notations",
    "Apply together with the preceding finding (the env's \\end stays after (7.9.12.3)).")
add(211, "'... le polynôme de Hilbert en y relatif à P., f et L'",
    "only 'polynôme de Hilbert' italic; 'en y relatif à P., f et L' roman", "\\emph covers the whole phrase",
    "italics", None, "high",
    r"\emph{polynôme de Hilbert en $y$¶relatif à $\mathscr P_\bullet$, $f$ et $\mathscr L$}",
    r"\emph{polynôme de Hilbert} en $y$¶relatif à $\mathscr P_\bullet$, $f$ et $\mathscr L$", "Emphasis too wide in the TeX.")
add(211, "'(ou simplement le polynôme de Hilbert en y de P., ou de f, ...'",
    "'de' before f italic", "upright", "italics", None, "high",
    r"}, ou de $f$, s'il", r"}, ou \emph{de} $f$, s'il", "Printed emphasis missing in the TeX.")
add(211, "(7.9.12.2): '(—1)^i'",
    "long dash", "(-1)^i", "convention", 7, "high",
    r"\sum_i(-1)^i\operatorname{PH}", r"\sum_i(\setmin 1)^i\operatorname{PH}", C7)
add(211, "Proof of (7.9.13): 'Comme le morphisme f est projectif (II, 5.5.3)'",
    "bold II", "(II, 5.5.3)", "convention", 2, "high",
    r"(II, 5.5.3), il existe", r"(\textbf{II}, 5.5.3), il existe", C2)
add(211, "Boundary p. 211/212: blank line after 'pour n ≥ n_0', before \\oldpage[III]{212}",
    "p. 212 begins 'on ait R^if_*(F(n)) = 0 ...' flush left, continuing the sentence", "blank line before the marker",
    "other", None, "high",
    r"$n\geq n_0$¶¶", r"$n\geq n_0$¶", "Spurious paragraph break at the page boundary (GLOBAL_ISSUES item 20).")

# ---------------------------------------------------------------- checks
ok = True
pages = sorted(set(f['page'] for f in F))
for p in pages:
    txt = open(rf'{RUN}\page_{p}.tex', encoding='utf-8').read().replace('\r\n', '\n')
    spans = []
    for f in F:
        if f['page'] != p or f['fix'] is None:
            continue
        old = f['fix']['old']
        n = txt.count(old)
        if n != 1:
            ok = False
            print(f'COUNT {n} on p.{p}: {old!r}')
            continue
        i = txt.index(old)
        spans.append((i, i + len(old), f['where'][:60]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print(f'OVERLAP p.{p}: [{a[2]}] and [{b[2]}]')
for f in F:
    if f['kind'] == 'misprint_in_print' and 'corrected' not in f:
        ok = False
        print('no corrected:', f['where'])
    if f['kind'] == 'convention' and not f['convention']:
        ok = False
        print('no conv number:', f['where'])

for p in pages:
    fs = [f for f in F if f['page'] == p]
    c = sum(f['kind'] == 'convention' for f in fs)
    m = sum(f['kind'] == 'misprint_in_print' for f in fs)
    print(f'p.{p}: {len(fs) - c - m}/{c}/{m}  (total {len(fs)})')
print('checks ok' if ok else 'CHECKS FAILED')
if ok:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
    print('written', OUT, len(F))
