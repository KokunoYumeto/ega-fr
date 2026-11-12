# Builds findings_202_206.json and checks every fix against the page files.
# Newlines in TeX snippets are written as the placeholder ⏎ (TeX here contains \notin etc.).
import json, sys, os

RUN = r"user\Documents\ega_scan_check_20261101\run_III2"
OUT = os.path.join(RUN, "findings_202_206.json")

def T(s):
    return s.replace("⏎", "\n")

F = []
def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, check_file=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": T(old), "new": T(new)}}
    if corrected is not None:
        d["corrected"] = T(corrected)
    d["note"] = note
    d["_check_file"] = check_file or f"page_{page}.tex"
    F.append(d)

KAPPA_NOTE = ("Residue field k, not kappa: bold italic, bold upright in sub- and superscripts "
              "(GLOBAL_ISSUES items 48, 55; same page-fix form as pp. 194-201).")
TOR_NOTE = ("Heavy hypertor sign (roundhand T, bold italic 'or') of the global hypertor Tor^Y(f, 1_Y; P_•, ...); "
            "page-fix form \\boldsymbol{\\mathscr{T}\\!or} as in ega3-6 for the same expression (GLOBAL_ISSUES items 52, 54).")
RH_NOTE = ("Second, lighter roundhand H of hypercohomology (unlike the ordinary script H of H_i, H_p on p. 204); "
           "page-fix form \\mathcal H as in ega3-6 (GLOBAL_ISSUES items 42, 54).")
LEADSTO_NOTE = "Wavy arrow in the print (\\leadsto), not convention 3; GLOBAL_ISSUES item 33."

# ---------------- page 202 ----------------
add(202, "diagram, left vertical arrow Γ(X, F⊗M) → Hom(Q, M)",
    "≀ (vertical tilde) to the left of the arrow", "\\ar[d]_-{\\sim} (horizontal tilde)",
    "symbol", None, "high",
    r"\ar[r]\ar[d]_-{\sim}", r"\ar[r]\ar[d]_-{\wr}",
    "As the fixes logged for EGA II p. 42 and III p. 141 (\\wr).")
add(202, "diagram, right vertical arrow Γ(X, F'⊗M) → Hom(Q', M)",
    "≀ (vertical tilde) to the LEFT of the arrow", "\\ar[d]^-{\\sim}: horizontal tilde on the right",
    "symbol", None, "high",
    r"\ar[d]^-{\sim}", r"\ar[d]_-{\wr}",
    "Symbol and label side (both ≀ of the diagram stand left of their arrows).")
add(202, "'soit commutatif (0, 8.1.4)'", "bold 0", "plain 0", "convention", 2, "high",
    r"commutatif (0, 8.1.4)", r"commutatif (\textbf{0}, 8.1.4)", "Bold chapter number in the reference.")
add(202, "'le foncteur contravariant N⇝Hom_{O_Y}(N, M)'", "wavy arrow", "\\mapsto", "symbol", None, "high",
    r"$\mathscr N\mapsto\operatorname{Hom}", r"$\mathscr N\leadsto\operatorname{Hom}", LEADSTO_NOTE)
add(202, "Corollaire (7.7.8): 'Sous les hypothèses de (7.7.6) relatives à X, Y et f'",
    "(7.7.6) upright inside the italic statement", "italic (corollary environment)",
    "convention", 6, "high",
    r"hypothèses de (7.7.6) relatives", r"hypothèses de \textup{(7.7.6)} relatives",
    "Reference set in roman figures inside the italic statement.")
add(202, "Corollaire (7.7.8): '(i) F est Y-plat'", "label (i) upright", "italic", "convention", 6, "high",
    r"(i) $\mathscr F$ est", r"\textup{(i)} $\mathscr F$ est", "Roman-numeral label upright in the print (GLOBAL_ISSUES item 16).")
add(202, "Corollaire (7.7.8): 'F est Y-plat : (ii) G est isomorphe'",
    "a colon after 'Y-plat' (checked on a 5x crop: two round dots, no comma tail)", "semicolon",
    "misprint_in_print", None, "high",
    r"$Y$-plat ;", r"$Y$-plat :",
    "The print separates the conditions (i), (ii) with a colon where a semicolon is meant; the TeX silently corrects it. The edit restores the printed colon.",
    corrected=r"$Y$-plat ;")
add(202, "Corollaire (7.7.8): '(ii) G est isomorphe au conoyau'", "label (ii) upright", "italic", "convention", 6, "high",
    r"(ii) $\mathscr G$ est isomorphe", r"\textup{(ii)} $\mathscr G$ est isomorphe",
    "Roman-numeral label upright in the print (GLOBAL_ISSUES item 16).")
add(202, "Corollaire (7.7.8), first display line: 'T(M) = f_*(Hom_{O_Y}(G, F⊗_{O_Y} M))'",
    "script Hom with subscript O_Y (enlarged crop)", "\\mathscr{H}\\!om_{\\mathscr O_X}",
    "misprint_in_print", None, "high",
    r"&=⏎  f_*⏎  \bigl(⏎    \mathscr{H}\!om_{\mathscr O_X}",
    r"&=⏎  f_*⏎  \bigl(⏎    \mathscr{H}\!om_{\mathscr O_Y}",
    "G and F⊗M are O_X-Modules (the next line and the proof have Hom_{O_X}); the TeX silently corrects O_Y to O_X. The edit restores the printed O_Y.",
    corrected=r"\mathscr{H}\!om_{\mathscr O_X}(\mathscr G,\mathscr F\otimes_{\mathscr O_Y}\mathscr M)")
add(202, "Corollaire (7.7.8), end of the first display line", "no comma after T(M)=f_*(...)", "comma",
    "punctuation", None, "high",
    r"\bigr),\\", r"\bigr)\\", "")
add(202, "Corollaire (7.7.8): 'Alors il existe un O_Y-Module cohérent N' after the display",
    "'Alors' begins a new, indented paragraph", "no blank line after \\end{align*}",
    "other", None, "high",
    r"\end{align*}⏎Alors il existe", r"\end{align*}⏎⏎Alors il existe",
    "Paragraph break as printed (cf. GLOBAL_ISSUES item 47).")
add(202, "proof of (7.7.8): '(0_I, 5.4.2.1)'", "bold 0", "plain 0", "convention", 2, "high",
    r"($0_{\mathrm I}$, 5.4.2.1)", r"($\mathbf{0}_{\mathrm I}$, 5.4.2.1)", "Bold chapter number (form of GLOBAL_ISSUES item 35).")
add(202, "proof of (7.7.8): 'cohérents (0_I, 5.3.5)'", "bold 0", "plain 0", "convention", 2, "high",
    r"($0_{\mathrm I}$, 5.3.5)", r"($\mathbf{0}_{\mathrm I}$, 5.3.5)", "Bold chapter number.")
add(202, "proof of (7.7.8): 'Y-plats (0_I, 5.4.2)'", "bold 0", "plain 0", "convention", 2, "high",
    r"($0_{\mathrm I}$, 5.4.2)", r"($\mathbf{0}_{\mathrm I}$, 5.4.2)", "Bold chapter number.")
add(202, "proof of (7.7.8): 'du foncteur H⇝Hom_{O_X}(H, F⊗_{O_Y} M)'", "wavy arrow", "\\mapsto", "symbol", None, "high",
    r"$\mathscr H\mapsto\mathscr{H}\!om", r"$\mathscr H\leadsto\mathscr{H}\!om", LEADSTO_NOTE)
add(202, "proof of (7.7.8), end of the display '... ⥲ Ker(F_0⊗M → F_1⊗M)'", "no full stop (crop)", "full stop",
    "punctuation", None, "high",
    r"\mathscr M⏎  \bigr).", r"\mathscr M⏎  \bigr)", "")
add(202, "proof of (7.7.8): 'Puisque f_* est exact à gauche' after the display",
    "'Puisque' begins a new, indented paragraph", "no blank line after \\end{align*}",
    "other", None, "high",
    r"\end{align*}⏎Puisque", r"\end{align*}⏎⏎Puisque", "Paragraph break as printed.")

# ---------------- page 203 ----------------
add(203, "Remarques (7.7.9) (i): 'ce qui n'est autre que (0_I, 4.4.3.1)'", "bold 0", "plain 0", "convention", 2, "high",
    r"($0_{\mathrm I}$, 4.4.3.1)", r"($\mathbf{0}_{\mathrm I}$, 4.4.3.1)", "Bold chapter number.")
add(203, "Remarques (7.7.9) (i): 'une suite exacte E'_1→E'_0→G'→0 avec E'_i=E_i⊗_{O_Y}O_X' et de ce que'",
    "both formulas in the running text, joined by 'avec'", "one display, \\qquad\\text{avec}\\qquad",
    "other", None, "high",
    r"suite exacte⏎\[⏎  \mathscr E'_1\longrightarrow⏎  \mathscr E'_0\longrightarrow⏎  \mathscr G'\longrightarrow0⏎  \qquad\text{avec}\qquad⏎  \mathscr E'_i=\mathscr E_i\otimes_{\mathscr O_Y}\mathscr O_{X'}⏎\]⏎",
    r"suite exacte⏎$\mathscr E'_1\longrightarrow\mathscr E'_0\longrightarrow\mathscr G'\longrightarrow0$ avec⏎$\mathscr E'_i=\mathscr E_i\otimes_{\mathscr O_Y}\mathscr O_{X'}$⏎",
    "Layout: the print sets these formulas in the running text; the formulas match.")
add(203, "Remarques (7.7.9) (i): 'et de ce que Ě'_i⊗(F⊗M') = Ě_i⊗(F⊗M) (i=0, 1).' (part 1 of 2)",
    "formula in the running text", "displayed",
    "other", None, "high",
    r"et de ce que⏎\[⏎", r"et de ce que⏎$",
    "Layout: inline in the print. Apply together with part 2 ('\\qquad(i=0,1).' edit); the misprint fix below lies between them.")
add(203, "Remarques (7.7.9) (i): right side 'Ě_i⊗_{O_X}(F⊗_{O_Y} M)'",
    "M without a prime on the right side (enlarged crop)", "M' on both sides",
    "misprint_in_print", None, "high",
    r"\otimes_{\mathscr O_X}⏎  (\mathscr F\otimes_{\mathscr O_Y}\mathscr M')",
    r"\otimes_{\mathscr O_X}⏎  (\mathscr F\otimes_{\mathscr O_Y}\mathscr M)",
    "Both sides concern the O_{Y'}-Module M' (M is not in play here); the TeX silently corrects. The edit restores the printed M.",
    corrected=r"\check{\mathscr E}_i\otimes_{\mathscr O_X}(\mathscr F\otimes_{\mathscr O_Y}\mathscr M')")
add(203, "Remarques (7.7.9) (i): same formula, end (part 2 of 2)",
    "'... (i=0, 1).' in the running text", "\\qquad(i=0,1). inside the display",
    "other", None, "high",
    r"⏎  \qquad(i=0,1).⏎\]⏎", r"$ ($i=0,1$).⏎",
    "Apply together with part 1 ('et de ce que' edit).")
add(203, "Remarques (7.7.9) (ii): 'un O_X-Module inversible Y-ample'", "'ample' italic", "upright",
    "italics", None, "high", r"$Y$-ample", r"$Y$-\emph{ample}",
    "Italic in the print (remark body judged as roman).")
add(203, "Remarques (7.7.9) (ii): 'est un morphisme projectif.'", "'projectif' italic", "upright",
    "italics", None, "high", r"morphisme⏎projectif.", r"morphisme⏎\emph{projectif}.",
    "Italic in the print (remark body judged as roman).")
add(203, "Remarques (7.7.9) (ii): '(II, 5.5.1)'", "bold II", "plain II", "convention", 2, "high",
    r"(II, 5.5.1)", r"(\textbf{II}, 5.5.1)", "Bold chapter number.")
add(203, "Remarques (7.7.9) (ii): '(II, 2.7.10)'", "bold II", "plain II", "convention", 2, "high",
    r"(II, 2.7.10)", r"(\textbf{II}, 2.7.10)", "Bold chapter number.")
add(203, "Proposition (7.7.10): title '(critères locaux pour la propriété d'échange)'",
    "lower-case 'critères' (the title stands before the dash: GLOBAL_ISSUES item 11)", "'(Critères' with a capital C",
    "word", None, "high", r"\textnormal{(Critères", r"\textnormal{(critères",
    "Capital letter only; the position of the title is the document-wide item 11.")
add(203, "Proposition (7.7.10): 'Sous les conditions générales de (7.7.5)'", "(7.7.5) upright", "italic",
    "convention", 6, "high", r"générales de (7.7.5),", r"générales de \textup{(7.7.5)},",
    "Reference in roman inside the italic statement.")
add(203, "Proposition (7.7.10): label a)", "upright a)", "italic (\\item[a)] in the italic statement)",
    "convention", 6, "high", r"\item[a)]", r"\item[\textup{a)}]", "Labels a), b), c) of this statement are upright in the print.")
add(203, "Proposition (7.7.10): label b)", "upright b)", "italic", "convention", 6, "high",
    r"\item[b)]", r"\item[\textup{b)}]", "")
add(203, "Proposition (7.7.10) b): 'L'homomorphisme canonique T_p(O_y)→T_p(k(y)) est surjectif.' (part 1 of 2)",
    "formula in the running text", "displayed", "other", None, "high",
    r"L'homomorphisme canonique⏎    \[⏎", r"L'homomorphisme canonique⏎    $",
    "Layout: inline in the print. Apply together with part 2; the k(y) fix lies between them.")
add(203, "Proposition (7.7.10) b): T_p^{O_y}(k(y))", "bold italic k(y)", "\\kappa(y)", "symbol", None, "high",
    r"T_p^{\mathscr O_y}(\mathscr O_y)⏎      \longrightarrow⏎      T_p^{\mathscr O_y}(\kappa(y))",
    r"T_p^{\mathscr O_y}(\mathscr O_y)⏎      \longrightarrow⏎      T_p^{\mathscr O_y}(\boldsymbol{k}(y))",
    KAPPA_NOTE)
add(203, "Proposition (7.7.10) b): end of the formula (part 2 of 2)", "see part 1", "\\] before 'est surjectif.'",
    "other", None, "high",
    r"⏎    \]⏎    est surjectif.⏎⏎", r"$⏎    est surjectif.⏎⏎",
    "Apply together with part 1.")
add(203, "Proposition (7.7.10): label c)", "upright c)", "italic", "convention", 6, "high",
    r"\item[c)]", r"\item[\textup{c)}]", "")
add(203, "Proposition (7.7.10) c): 'l'homomorphisme canonique T_p(O_y/m^{n+1})→T_p(k(y)) est surjectif.' (part 1 of 2)",
    "formula in the running text", "displayed", "other", None, "high",
    r"l'homomorphisme canonique⏎    \[⏎", r"l'homomorphisme canonique⏎    $",
    "Layout: inline in the print. Apply together with part 2; the k(y) fix lies between them.")
add(203, "Proposition (7.7.10) c): T_p^{O_y}(k(y))", "bold italic k(y)", "\\kappa(y)", "symbol", None, "high",
    r"(\mathscr O_y/\mathfrak m_y^{n+1})⏎      \longrightarrow⏎      T_p^{\mathscr O_y}(\kappa(y))",
    r"(\mathscr O_y/\mathfrak m_y^{n+1})⏎      \longrightarrow⏎      T_p^{\mathscr O_y}(\boldsymbol{k}(y))",
    KAPPA_NOTE)
add(203, "Proposition (7.7.10) c): end of the formula (part 2 of 2)", "see part 1", "\\] before 'est surjectif.'",
    "other", None, "high",
    r"⏎    \]⏎    est surjectif.⏎\end{enumerate}", r"$⏎    est surjectif.⏎\end{enumerate}",
    "Apply together with part 1.")
add(203, "Proposition (7.7.10): 'De plus, l'ensemble des y∈Y ...' after the list",
    "'De plus' begins an indented paragraph (its second line starts at the margin)",
    "text directly after \\end{enumerate}: no indentation", "other", None, "medium",
    r"⏎De plus, l'ensemble", r"⏎⏎De plus, l'ensemble", "Paragraph break as printed.")
add(203, "proof of (7.7.10): 'l'équivalence de a), b) et c)'", "a), b), c) italic", "upright",
    "italics", None, "high", r"de a), b) et c) résulte", r"de \emph{a)}, \emph{b)} et \emph{c)} résulte",
    "Statement labels cited in the roman text are italic in the print.")
add(203, "proof of (7.7.10): 'par la condition c) de (7.7.5)'", "c) italic", "upright",
    "italics", None, "high", r"la condition c) de (7.7.5)", r"la condition \emph{c)} de (7.7.5)", "")
add(203, "Corollaire (7.7.11): 'exact à droite (resp. à gauche), alors'",
    "'(resp.' and ')' upright, 'à gauche' italic", "all italic", "convention", 6, "high",
    r"à droite (resp. à gauche), alors", r"à droite \textup{(resp.} à gauche\textup{)}, alors",
    "Roman 'resp.' and parentheses inside the italic statement (enlarged crop).")
add(203, "Corollaire (7.7.11): 'est exact à droite (resp. à gauche). La réciproque'",
    "'(resp.' and ')' upright", "all italic", "convention", 6, "high",
    r"à droite (resp. à gauche). La", r"à droite \textup{(resp.} à gauche\textup{)}. La", "")

# ---------------- page 204 ----------------
add(204, "proof of (7.7.11): 'd'après (7.7.5, c) et b))'", "c), b) italic", "upright",
    "italics", None, "high", r"(7.7.5, c) et b))", r"(7.7.5, \emph{c)} et \emph{b)})", "")
add(204, "Remarques (7.7.12) (i): 'est aussi fini, et de façon précise'", "'fini' italic (start of the line)", "upright",
    "italics", None, "high", r"aussi fini, et de façon", r"aussi \emph{fini}, et de façon",
    "Remark body judged as roman.")
add(204, "Remarques (7.7.12) (i): 'tel que C^h(U, P^k⊗M)=0 pour tous les couples (h, k)∉E.'",
    "in the running text", "displayed with \\qquad\\text{...}", "other", None, "high",
    r"tel que⏎\[⏎  C^h(\mathfrak U,\mathscr P^k\otimes_{\mathscr O_Y}\mathscr M)=0⏎  \qquad\text{pour tous les couples }(h,k)\notin E.⏎\]⏎On en conclut",
    r"tel que⏎$C^h(\mathfrak U,\mathscr P^k\otimes_{\mathscr O_Y}\mathscr M)=0$ pour tous les couples $(h,k)\notin E$.⏎On en conclut",
    "Layout: inline in the print; the formula matches.")
add(204, "Remarques (7.7.12) (i): 'et soit L'_•=L̃'_•'", "tilde over L only (L̃'_•)", "\\widetilde{L'_\\bullet}",
    "convention", 8, "high", r"\widetilde{L'_\bullet}", r"\widetilde{L}'_\bullet", "")
add(204, "Remarques (7.7.12) (i): 'Il est clair que H_i(L'⊗M)=H_i(L'⊗M) pour i<i_1-1' (part 1 of 2)",
    "in the running text", "displayed", "other", None, "high",
    r"Il est clair que⏎\[⏎", r"Il est clair que⏎$",
    "Layout: inline in the print. Apply together with part 2; the misprint fix lies between them.")
add(204, "Remarques (7.7.12) (i): right side of 'H_i(L'_•⊗M)=H_i(L'_•⊗M) pour i<i_1-1'",
    "L'_• with a prime on the right side too (enlarged crop)", "L_• (no prime) on the right",
    "misprint_in_print", None, "high",
    r"  =⏎  \mathscr H_i(\mathscr L_\bullet", r"  =⏎  \mathscr H_i(\mathscr L'_\bullet",
    "The comparison is between L'_• and L_• (as in the case i=i_1-1 two lines later); the TeX silently corrects. The edit restores the printed prime.",
    corrected=r"\mathscr H_i(\mathscr L_\bullet\otimes_{\mathscr O_Y}\mathscr M)")
add(204, "Remarques (7.7.12) (i): same formula, end (part 2 of 2)", "see part 1", "\\] before 'pour $i<i_1-1$'",
    "other", None, "high",
    r"⏎\]⏎pour $i<i_1-1$", r"$⏎pour $i<i_1-1$", "Apply together with part 1.")
add(204, "Remarques (7.7.12) (ii), (7.7.12.1): 'T_p(M)=Tor_p^Y(f, 1_Y; P_•, M)'",
    "heavy hypertor sign: roundhand T with bold italic 'or' (crop)", "\\operatorname{Tor} (roman Tor of modules)",
    "font", None, "high", r"\operatorname{Tor}^Y_p", r"\boldsymbol{\mathscr{T}\!or}^Y_p", TOR_NOTE)
add(204, "Remarques (7.7.12) (ii): 'En effet, Tor_n^Y(f, 1_Y; P_•, O_Y) est alors'",
    "heavy hypertor sign (enlarged crop)", "\\operatorname{Tor}", "font", None, "high",
    r"\operatorname{Tor}^Y_n", r"\boldsymbol{\mathscr{T}\!or}^Y_n", TOR_NOTE)
add(204, "Remarques (7.7.12) (ii): 'l'on a T_p(M)=H_p(L_•⊗M), avec L_•=L̃_•, où L_• ...' (part 1 of 2)",
    "in the running text; the word 'avec' joins the two formulas", "displayed, joined by \\qquad; 'avec' missing",
    "missing", None, "high",
    r"l'on a⏎\[⏎  \mathscr T_p(\mathscr M)⏎  =⏎  \mathscr H_p(\mathscr L_\bullet\otimes_{\mathscr O_Y}\mathscr M),⏎  \qquad⏎  \mathscr L_\bullet=",
    r"l'on a⏎$\mathscr T_p(\mathscr M)=\mathscr H_p(\mathscr L_\bullet\otimes_{\mathscr O_Y}\mathscr M)$,⏎avec $\mathscr L_\bullet=",
    "Restores 'avec' and sets the formulas inline (GLOBAL_ISSUES item 51). Apply together with part 2; the tilde fix lies between them.")
add(204, "Remarques (7.7.12) (ii): 'L_•=L̃_•'", "tilde over L only (L̃_•)", "\\widetilde{L_\\bullet}",
    "convention", 8, "high", r"\widetilde{L_\bullet}", r"\widetilde{L}_\bullet", "")
add(204, "Remarques (7.7.12) (ii): end of the same formula (part 2 of 2)", "see part 1", "\\] before 'où'",
    "other", None, "high", r",⏎\]⏎où $L_\bullet$", r"$,⏎où $L_\bullet$", "Apply together with part 1.")
add(204, "heading 7.8", "'7.8. Application aux morphismes propres : II. Critères de platitude cohomologique.' (final full stop)",
    "no full stop", "punctuation", None, "high",
    r"Critères de platitude⏎cohomologique}", r"Critères de platitude⏎cohomologique.}", "As GLOBAL_ISSUES items 43/50.")
add(204, "Définition (7.8.1): 'défini par (7.7.1.1), y un point de Y'", "(7.7.1.1) upright", "italic",
    "convention", 6, "high", r"défini par (7.7.1.1), $y$", r"défini par \textup{(7.7.1.1)}, $y$",
    "Reference in roman inside the italic statement.")
add(204, "page break p. 204/205: 'On dit que P_• est' / 'homologiquement plat sur Y au point y ...'",
    "p. 205 continues the sentence flush left", "blank line before \\oldpage[III]{205}: spurious paragraph break",
    "other", None, "high", r"On dit que $\mathscr P_\bullet$ est⏎⏎", r"On dit que $\mathscr P_\bullet$ est⏎",
    "No blank line follows the marker on p. 205, so this edit alone removes the break.")

# ---------------- page 205 ----------------
add(205, "Définition (7.8.1), first defined term and '(ou' (part 1 of 2)",
    "'homologiquement plat sur Y au point y, en dimension p' and 'cohomologiquement plat ...' italic like the rest of the definition; only '(ou' upright",
    "both terms in \\emph (upright inside the italic environment); '(ou' italic",
    "convention", 6, "high",
    r"\emph{homologiquement plat sur $Y$ au point $y$, en dimension $p$} (ou⏎\emph{cohomologiquement plat sur $Y$ au point",
    r"homologiquement plat sur $Y$ au point $y$, en dimension $p$ \textup{(ou}⏎cohomologiquement plat sur $Y$ au point",
    "Drops the \\emph (no change of face in the print) and sets '(ou' upright. Apply together with part 2 (closing brace '}) s'il⏎existe').")
add(205, "Définition (7.8.1): 'en dimension —p) s'il existe'", "long dash for the minus", "minus sign",
    "convention", 7, "medium", r"$y$, en dimension $-p$", r"$y$, en dimension $\setmin p$",
    "Unary minus printed as the long dash (GLOBAL_ISSUES item 23/49); \\setmin as for O(—n), pending the convention-7 decision.")
add(205, "Définition (7.8.1), first pair, closing brace (part 2 of 2)", "see part 1", "'}' of the \\emph",
    "convention", 6, "high", r"}) s'il⏎existe", r") s'il⏎existe", "Apply together with part 1.")
add(205, "Définition (7.8.1), second pair 'homologiquement plat en dimension p sur Y (ou cohomologiquement plat ...)' (part 1 of 2)",
    "terms italic like the rest; '(ou' upright", "terms in \\emph (upright); '(ou' italic",
    "convention", 6, "high",
    r"\emph{homologiquement plat en dimension $p$ sur $Y$} (ou⏎\emph{cohomologiquement plat en dimension",
    r"homologiquement plat en dimension $p$ sur $Y$ \textup{(ou}⏎cohomologiquement plat en dimension",
    "As the first pair. Apply together with part 2 ('}) s'il est').")
add(205, "Définition (7.8.1): 'en dimension —p sur Y)'", "long dash for the minus", "minus sign",
    "convention", 7, "medium", r"$-p$ sur $Y$", r"$\setmin p$ sur $Y$", "As above.")
add(205, "Définition (7.8.1), second pair, closing brace (part 2 of 2)", "see part 1", "'}' of the \\emph",
    "convention", 6, "high", r"}) s'il est", r") s'il est", "Apply together with part 1.")
add(205, "Définition (7.8.1), paragraph 'Lorsque P_• est homologiquement plat sur Y ...'",
    "the whole paragraph is roman, with 'toute dimension p', 'homologiquement plat sur', 'cohomologiquement plat sur' italic",
    "italic (definition environment); its three \\emph come out upright",
    "convention", 6, "high",
    r"⏎⏎Lorsque $\mathscr P_\bullet$", r"⏎⏎\upshape Lorsque $\mathscr P_\bullet$",
    "\\upshape holds to \\end{definition}, so the existing \\emph then give italic. Alternative: close the definition before this paragraph.")
add(205, "(7.8.2): 'est locale sur Y'", "only 'locale' italic", "\\emph{locale sur $Y$}",
    "italics", None, "high", r"\emph{locale sur⏎$Y$}", r"\emph{locale} sur⏎$Y$", "")
add(205, "(7.8.2): '(I, 9.4.2)'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 9.4.2)", r"(\textbf{I}, 9.4.2)", "Bold chapter number.")
add(205, "Proposition (7.8.3): 'étant celles de (7.8.1)'", "(7.8.1) upright", "italic", "convention", 6, "high",
    r"celles de (7.8.1),", r"celles de \textup{(7.8.1)},", "")
add(205, "Proposition (7.8.3): label a)", "upright", "italic", "convention", 6, "high",
    r"\item[a)] $\mathscr P_\bullet$ est homologiquement plat sur $Y$ au",
    r"\item[\textup{a)}] $\mathscr P_\bullet$ est homologiquement plat sur $Y$ au", "")
add(205, "Proposition (7.8.3): label b)", "upright", "italic", "convention", 6, "high",
    r"\item[b)] Il existe", r"\item[\textup{b)}] Il existe", "")
add(205, "Proposition (7.8.3): label c)", "upright", "italic", "convention", 6, "high",
    r"\item[c)] Il existe un voisinage", r"\item[\textup{c)}] Il existe un voisinage", "")
add(205, "Proposition (7.8.3): label d)", "upright", "italic", "convention", 6, "high",
    r"\item[d)] Il existe", r"\item[\textup{d)}] Il existe", "")
add(205, "Proposition (7.8.3) d): 'tel que T_{p+1}^U est exact à droite et T_{p-1}^U exact à gauche'",
    "'est' (enlarged crop)", "'soit'", "word", None, "high",
    r"soit exact à droite et", r"est exact à droite et", "")
add(205, "Proposition (7.8.4): 'le foncteur défini par (7.7.1.1). Pour tout'", "(7.7.1.1) upright", "italic",
    "convention", 6, "high", r"défini par (7.7.1.1).⏎Pour", r"défini par \textup{(7.7.1.1)}.⏎Pour", "")
add(205, "Proposition (7.8.4): label a)", "upright", "italic", "convention", 6, "high",
    r"\item[a)] $\mathscr P_\bullet$ est homologiquement plat sur $Y$ en",
    r"\item[\textup{a)}] $\mathscr P_\bullet$ est homologiquement plat sur $Y$ en", "")
add(205, "Proposition (7.8.4): label b)", "upright", "italic", "convention", 6, "high",
    r"\item[b)] Le foncteur", r"\item[\textup{b)}] Le foncteur", "")
add(205, "Proposition (7.8.4): label c)", "upright", "italic", "convention", 6, "high",
    r"\item[c)] Il existe un entier", r"\item[\textup{c)}] Il existe un entier", "")
add(205, "Proposition (7.8.4): label d)", "upright", "italic", "convention", 6, "high",
    r"\item[d)] Il y a", r"\item[\textup{d)}] Il y a", "")
add(205, "(7.8.4.1): 'long T_p^{O_y}(k(y))'", "bold italic k(y)", "\\kappa(y)", "symbol", None, "high",
    r"\operatorname{long}T_p^{\mathscr O_y}(\kappa(y))", r"\operatorname{long}T_p^{\mathscr O_y}(\boldsymbol{k}(y))", KAPPA_NOTE)
add(205, "(7.8.4.1): product '... (k(y)) . long ...'", "a full stop on the baseline (crop)", "\\cdot (centred)",
    "symbol", None, "medium", r"\cdot", r".", "As the baseline product dots fixed elsewhere (e.g. III p. 177, a.v).")
add(205, "(7.8.4.1): last factor 'long O_y/m_y^{n+1}'", "no parentheses", "\\operatorname{long}(\\mathscr O_y/...)",
    "formula", None, "high",
    r"\operatorname{long}(\mathscr O_y/\mathfrak m_y^{n+1})", r"\operatorname{long}\mathscr O_y/\mathfrak m_y^{n+1}", "")
add(205, "(7.8.4) d): '(H^{-p}(f, P^•))|U soit isomorphe'", "roundhand H (enlarged crop)", "\\mathscr H",
    "font", None, "high",
    r"$(\mathscr H^{-p}(f,\mathscr P^\bullet))|U$ soit", r"$(\mathcal H^{-p}(f,\mathscr P^\bullet))|U$ soit", RH_NOTE)
add(205, "(7.8.4.2), left side: '(H^{-p}(f, P^•))|U)⊗_{O_Y|U} M'",
    "two opening and three closing parentheses (enlarged crop)", "((\\mathscr H^{-p}(f,\\mathscr P^\\bullet))|U): balanced",
    "misprint_in_print", None, "high", r"\[⏎      ((", r"\[⏎      (",
    "Unbalanced parentheses in the print; the TeX silently adds the missing one. The edit restores the printed reading "
    "(it removes the first of the two opening parentheses).",
    corrected=r"((\mathscr H^{-p}(f,\mathscr P^\bullet))|U)\otimes_{\mathscr O_Y|U}\mathscr M")
add(205, "(7.8.4.2), left side: H^{-p}(f, P^•)", "roundhand H (enlarged crop)", "\\mathscr H", "font", None, "high",
    r"\mathscr H^{-p}(f,\mathscr P^\bullet))|U)⏎      \otimes", r"\mathcal H^{-p}(f,\mathscr P^\bullet))|U)⏎      \otimes", RH_NOTE)
add(205, "(7.8.4.2), right side: H^{-p}(f, (P^•|U)⊗M)", "roundhand H (enlarged crop)", "\\mathscr H", "font", None, "high",
    r"\mathscr H^{-p}⏎      \bigl(", r"\mathcal H^{-p}⏎      \bigl(", RH_NOTE)
add(205, "Proposition (7.8.4): 'Lorsque ces conditions sont vérifiées ...' after the list",
    "indented new paragraph", "text directly after \\end{enumerate}: no indentation", "other", None, "medium",
    r"\end{enumerate}⏎Lorsque ces conditions", r"\end{enumerate}⏎⏎Lorsque ces conditions", "Paragraph break as printed.")
add(205, "Proposition (7.8.4): label e)", "upright", "italic", "convention", 6, "high",
    r"\item[e)]", r"\item[\textup{e)}]", "")
add(205, "Proposition (7.8.4) e): 'la fonction z⇝d_p(z)'", "wavy arrow", "\\mapsto", "symbol", None, "high",
    r"$z\mapsto d_p(z)$", r"$z\leadsto d_p(z)$", LEADSTO_NOTE)
add(205, "Proposition (7.8.4) e): '(définie dans (7.7.5.1))'", "the parenthesis is upright", "italic",
    "convention", 6, "high", r"(définie dans (7.7.5.1))", r"\textup{(définie dans (7.7.5.1))}", "")
add(205, "Proposition (7.8.4): 'De plus, si Y est réduit ...' after the list",
    "indented new paragraph", "text directly after \\end{enumerate}: no indentation", "other", None, "medium",
    r"\end{enumerate}⏎De plus, si", r"\end{enumerate}⏎⏎De plus, si", "Paragraph break as printed.")
add(205, "Proposition (7.8.4): 'si Y est réduit au point y'", "'réduit' upright (enlarged crop)", "italic",
    "convention", 6, "high", r"est réduit au point", r"est \textup{réduit} au point", "")
add(205, "Proposition (7.8.4): '(0_I, 4.1.4)'", "bold 0; the reference upright", "plain 0, italic",
    "convention", 2, "high", r"($0_{\mathrm I}$, 4.1.4)", r"\textup{($\mathbf{0}_{\mathrm I}$, 4.1.4)}",
    "One edit for convention 2 and the upright reference inside the italic statement (convention 6), as logged for (0_I, 4.4.3).")

# ---------------- page 206 ----------------
add(206, "proof of (7.8.4): 'la condition b) équivaut'", "b) italic", "upright", "italics", None, "high",
    r"la condition b) équivaut", r"la condition \emph{b)} équivaut", "")
add(206, "proof of (7.8.4): 'L'équivalence de a) et b) résulte alors'", "a), b) italic", "upright",
    "italics", None, "high", r"L'équivalence de a) et b)⏎résulte", r"L'équivalence de \emph{a)} et \emph{b)}⏎résulte", "")
add(206, "proof of (7.8.4): 'T_p^{O_y}(k(y)) sont des'", "bold italic k(y)", "\\kappa(y)", "symbol", None, "high",
    r"$T_p^{\mathscr O_y}(\kappa(y))$ sont des", r"$T_p^{\mathscr O_y}(\boldsymbol{k}(y))$ sont des", KAPPA_NOTE)
add(206, "proof of (7.8.4): 'l'équivalence de b) et c) résulte encore'", "b), c) italic", "upright",
    "italics", None, "high", r"l'équivalence de b) et c) résulte", r"l'équivalence de \emph{b)} et \emph{c)} résulte", "")
add(206, "proof of (7.8.4): 'Le fait que a) entraîne e)'", "a), e) italic", "upright", "italics", None, "high",
    r"Le fait que a) entraîne e),", r"Le fait que \emph{a)} entraîne \emph{e)},", "")
add(206, "proof of (7.8.4): 'Enfin, a) entraîne que (7.8.4.2)'", "a) italic", "upright", "italics", None, "high",
    r"Enfin, a) entraîne", r"Enfin, \emph{a)} entraîne", "")
add(206, "proof of (7.8.4): 'd'autre part, a) entraîne que'", "a) italic", "upright", "italics", None, "high",
    r"part, a) entraîne", r"part, \emph{a)} entraîne", "")
add(206, "proof of (7.8.4): 'plat (7.3.3, f))'", "f) italic", "upright", "italics", None, "high",
    r"(7.3.3, f))", r"(7.3.3, \emph{f)})", "")
add(206, "proof of (7.8.4): 'donc libre (0, 10.1.3)'", "bold 0 WITHOUT the subscript I (enlarged crop)", "$0_{\\mathrm I}$",
    "extra", None, "high", r"($0_{\mathrm I}$, 10.1.3)", r"(\textbf{0}, 10.1.3)",
    "Chapter 0 §10 (flat modules) is 0_III, cited as (0, ...) in EGA III; 0_I has no §10. The edit also writes the bold 0 (convention 2).")
add(206, "proof of (7.8.4): 'voisinage de y (0_I, 5.2.7)'", "bold 0", "plain 0", "convention", 2, "high",
    r"($0_{\mathrm I}$, 5.2.7)", r"($\mathbf{0}_{\mathrm I}$, 5.2.7)", "Bold chapter number.")
add(206, "proof of (7.8.4): 'il est clair que d) entraîne a)'", "d), a) italic", "upright", "italics", None, "high",
    r"que d) entraîne a) par", r"que \emph{d)} entraîne \emph{a)} par", "")
add(206, "Proposition (7.8.5): 'Sous les hypothèses de (7.8.4)'", "(7.8.4) upright", "italic", "convention", 6, "high",
    r"hypothèses de (7.8.4), les", r"hypothèses de \textup{(7.8.4)}, les", "")
add(206, "Proposition (7.8.5): label a)", "upright", "italic", "convention", 6, "high",
    r"\item[a)]", r"\item[\textup{a)}]", "")
add(206, "Proposition (7.8.5): label b)", "upright", "italic", "convention", 6, "high",
    r"\item[b)]", r"\item[\textup{b)}]", "")
add(206, "Proposition (7.8.5): label c)", "upright", "italic", "convention", 6, "high",
    r"\item[c)]", r"\item[\textup{c)}]", "")
add(206, "Proposition (7.8.5) c): 'Pour i⩾—p'", "long dash for the minus", "minus sign", "convention", 7, "medium",
    r"$i\geq-p$", r"$i\geq\setmin p$", "Unary minus printed as the long dash (GLOBAL_ISSUES item 23/49); pending the convention-7 decision.")
add(206, "proof of (7.8.5): 'L'équivalence de a) et b) est triviale'", "a), b) italic", "upright",
    "italics", None, "high", r"L'équivalence de a) et b) est triviale", r"L'équivalence de \emph{a)} et \emph{b)} est triviale", "")
add(206, "proof of (7.8.5): 'et a) entraîne c) en vertu de (7.8.4)'", "a), c) italic", "upright",
    "italics", None, "high", r"et a) entraîne c) en vertu", r"et \emph{a)} entraîne \emph{c)} en vertu", "")
add(206, "proof of (7.8.5): 'supposons c) vérifiée'", "c) italic", "upright", "italics", None, "high",
    r"supposons c) vérifiée", r"supposons \emph{c)} vérifiée", "")
add(206, "proof of (7.8.5): 'qu'on a L_i=0 pour i⩽i_0 (7.7.4)'", "i⩽i_0 (enlarged crop; as in 'T_i=0 pour i⩽i_0' next)",
    "i<i_0", "formula", None, "high",
    r"$\mathscr L_i=0$ pour $i<i_0$", r"$\mathscr L_i=0$ pour $i\leq i_0$",
    "Transcription error, not a misprint: with L_i=0 for i⩽i_0 the conclusion 'donc aussi T_i=0 pour i⩽i_0' follows.")
add(206, "paragraph after (7.8.5): 'réduit à un seul O_X-Module'", "'un seul' italic", "only 'seul' in \\emph",
    "italics", None, "high", r"à un \emph{seul}", r"à \emph{un seul}", "")
add(206, "same sentence: 'cohérent F plat sur Y'", "roman capital F (enlarged crop)", "script F",
    "misprint_in_print", None, "high", r"$\mathscr F$ \emph{plat}", r"$F$ \emph{plat}",
    "Wrong-font letter in the print (the sheaf is script F, as in the formula that follows); the TeX silently corrects. Roman capitals are italic in the TeX (GLOBAL_ISSUES item 17).",
    corrected=r"$\mathscr F$")
add(206, "Proposition (7.8.6): 'la fibre f^{-1}(y)=X⊗_Y k(y)'", "bold italic k(y)", "\\kappa(y)", "symbol", None, "high",
    r"X\otimes_Y\kappa(y)", r"X\otimes_Y\boldsymbol{k}(y)", KAPPA_NOTE)
add(206, "Proposition (7.8.6): 'soit une k(y)-algèbre séparable'", "bold italic k(y)", "\\kappa(y)", "symbol", None, "high",
    r"une $\kappa(y)$-algèbre", r"une $\boldsymbol{k}(y)$-algèbre", KAPPA_NOTE)
add(206, "Proposition (7.8.6): '(Bourbaki, Alg., chap. VIII, § 7, n° 5)'", "roman, with 'Alg.' italic",
    "italic, 'Alg.' upright", "convention", 6, "high",
    r"(Bourbaki, \emph{Alg.}, chap. VIII, § 7, n\textsuperscript{o} 5)",
    r"\textup{(Bourbaki, \emph{Alg.}, chap. VIII, § 7, n\textsuperscript{o} 5)}",
    "As the logged fix for '(Bourbaki, Alg., chap. VIII, § 8, prop. 2)'.")
add(206, "Proposition (7.8.6): 'de degré fini de k(y).'", "bold italic k(y)", "\\kappa(y)", "symbol", None, "high",
    r"degré fini de $\kappa(y)$.", r"degré fini de $\boldsymbol{k}(y)$.", KAPPA_NOTE)
add(206, "proof of (7.8.6): 'en vertu de (7.7.10 c))'", "no comma after 7.7.10 (enlarged crop)", "comma",
    "punctuation", None, "high", r"(7.7.10, ", r"(7.7.10 ", "")
add(206, "proof of (7.8.6): '(7.7.10 c))'", "c) italic", "upright", "italics", None, "high",
    r"c)), on est même", r"\emph{c)}), on est même", "")
add(206, "proof of (7.8.6): 'une extension finie de k(y)'", "bold italic k(y)", "\\kappa(y)", "symbol", None, "high",
    r"finie de $\kappa(y)$ qui", r"finie de $\boldsymbol{k}(y)$ qui", KAPPA_NOTE)
add(206, "proof of (7.8.6): 'R⊗_{k(y)} k''", "subscript k bold UPRIGHT (GLOBAL_ISSUES item 48)", "\\kappa(y)",
    "symbol", None, "high", r"R\otimes_{\kappa(y)}k'", r"R\otimes_{\mathbf{k}(y)}k'", KAPPA_NOTE)
add(206, "proof of (7.8.6): 'isomorphe à k' (0, 10.3.2)'", "bold 0 WITHOUT the subscript I (enlarged crop)", "$0_{\\mathrm I}$",
    "extra", None, "high", r"($0_{\mathrm I}$,⏎10.3.2)", r"(\textbf{0},⏎10.3.2)",
    "As (0, 10.1.3) above: 0_III §10, cited (0, ...) in EGA III. The edit also writes the bold 0 (convention 2).")
add(206, "proof of (7.8.6): 'm corps isomorphes à k(y)'", "bold italic k(y)", "\\kappa(y)", "symbol", None, "high",
    r"isomorphes à $\kappa(y)$. Notons", r"isomorphes à $\boldsymbol{k}(y)$. Notons", KAPPA_NOTE)
add(206, "page break p. 206/207: Lemme (7.8.6.1) 'pour que Z soit connexe,' / 'il faut et il suffit ...'",
    "p. 207 continues the sentence flush left", "blank line before \\oldpage[III]{207}: spurious paragraph break",
    "other", None, "high", r"soit connexe,⏎⏎", r"soit connexe,⏎",
    "No blank line follows the marker on p. 207, so this edit alone removes the break.")
add(206, "proof of (7.8.4): 'a) entraîne que (H^{-p}(f, P^•))_y est un O_y-module plat'", "roundhand H (enlarged crop)",
    "\\mathscr H", "font", None, "high",
    r"$(\mathscr H^{-p}(f,\mathscr P^\bullet))_y$", r"$(\mathcal H^{-p}(f,\mathscr P^\bullet))_y$", RH_NOTE)
add(206, "proof of (7.8.4): 'puisque H^{-p}(f, P^•) est un O_Y-Module cohérent'", "roundhand H", "\\mathscr H",
    "font", None, "high",
    r"puisque $\mathscr H^{-p}(f,\mathscr P^\bullet)$", r"puisque $\mathcal H^{-p}(f,\mathscr P^\bullet)$", RH_NOTE)
add(206, "Proposition (7.8.5) c): 'les O_Y-Modules H^i(f, P^•) sont localement libres'", "roundhand H (enlarged crop)",
    "\\mathscr H", "font", None, "high",
    r"$\mathscr H^i(f,\mathscr P^\bullet)$", r"$\mathcal H^i(f,\mathscr P^\bullet)$", RH_NOTE)

# ---------------- checks ----------------
def load(name):
    with open(os.path.join(RUN, name), encoding="utf-8") as fh:
        return fh.read().replace("\r\n", "\n")

ok = True
texts = {}
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    fn = d["_check_file"]
    if fn not in texts:
        texts[fn] = load(fn)
    n = texts[fn].count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", n, d["page"], repr(fx["old"][:80]))

# sequential application per file, in list order
work = {fn: load(fn) for fn in texts}
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    fn = d["_check_file"]
    n = work[fn].count(fx["old"])
    if n != 1:
        ok = False
        print("SEQ FAIL", n, d["page"], repr(fx["old"][:80]))
        continue
    work[fn] = work[fn].replace(fx["old"], fx["new"], 1)

for d in F:
    del d["_check_file"]

if not ok:
    sys.exit(1)
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)

# counts
from collections import Counter
c = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    c[(d["page"], k)] += 1
for p in range(202, 207):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("total", len(F))
# dump the patched page texts for a brace sanity check
for fn, s in work.items():
    with open(os.path.join(RUN, "crops_202_206", "patched_" + fn), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(s)
