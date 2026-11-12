import json, sys

RUN = r"user\Documents\ega_scan_check_20261101\run_III2"
OUT = RUN + r"\findings_152_156.json"

def L(*lines):
    return "\n".join(lines)

F = []
def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

C2 = "Bold chapter numeral in the reference."
C6R = "'(resp.' is upright inside the italic statement."

# ---------------- page 152 ----------------
p = 152
add(p, "Remarque (6.5.12), end: '(cf. (0, 11.5.2.2))'", "(𝟎, 11.5.2.2): bold 0", "(0, 11.5.2.2)",
    "convention", 2, "high", r"(cf. (0, 11.5.2.2))", r"(cf. (\textbf{0}, 11.5.2.2))", C2)
add(p, "Proposition (6.5.13), label (i)", "(i) upright", r"\item[(i)] italic inside the italic proposition",
    "convention", 6, "high", r"\item[(i)]", r"\item[\textup{(i)}]", "Roman-numeral item labels are upright in the print (GLOBAL_ISSUES item 16).")
add(p, "Proposition (6.5.13), label (ii)", "(ii) upright", r"\item[(ii)] italic inside the italic proposition",
    "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]", "As label (i).")
add(p, "(6.5.13): 'Soit P. (resp. Q.) un complexe'", "'(resp.' upright", "italic (proposition body)",
    "convention", 6, "high", r"(resp. $\mathscr Q_\bullet$) un complexe", r"\textup{(resp.} $\mathscr Q_\bullet$) un complexe", C6R)
add(p, "(6.5.13): '(resp. de O_Y-Modules)'", "'(resp.' upright", "italic (proposition body)",
    "convention", 6, "high", r"(resp. de $\mathscr O_Y$-Modules)", r"\textup{(resp.} de $\mathscr O_Y$-Modules)", C6R)
add(p, "(6.5.13): '(resp. H_n(Q.))'", "'(resp.' upright", "italic (proposition body)",
    "convention", 6, "high", L(r"(resp.", r"$\mathscr H_n(\mathscr Q_\bullet)$)"), L(r"\textup{(resp.}", r"$\mathscr H_n(\mathscr Q_\bullet)$)"), C6R)
add(p, "(6.5.13): '(resp. un O_Y-Module) de type fini'", "'(resp.' upright", "italic (proposition body)",
    "convention", 6, "high", L(r"(resp. un", r"$\mathscr O_Y$-Module) de type fini."), L(r"\textup{(resp.} un", r"$\mathscr O_Y$-Module) de type fini."), C6R)
add(p, "Proof of (6.5.13): 'en vertu de (0, 11.1.8)'", "(𝟎, 11.1.8): bold 0", "(0, 11.1.8)",
    "convention", 2, "high", r"en vertu de (0, 11.1.8)", r"en vertu de (\textbf{0}, 11.1.8)", C2)
add(p, "Corollaire (6.5.14): 'des conditions (i), (ii) de'", "'(i), (ii)' upright inside the italic statement", "italic (corollary body)",
    "convention", 6, "high", r"conditions (i), (ii) de", r"conditions \textup{(i), (ii)} de", "")
add(p, "Corollaire (6.5.14): 'de (6.5.13), et'", "'(6.5.13)' upright inside the italic statement", "italic (corollary body)",
    "convention", 6, "high", r"(6.5.13), et", r"\textup{(6.5.13)}, et", "")
add(p, "Corollaire (6.5.14): 'soit F (resp. G) un'", "'(resp.' upright", "italic (corollary body)",
    "convention", 6, "high", r"(resp. $\mathscr G$) un", r"\textup{(resp.} $\mathscr G$) un", C6R)
add(p, "Corollaire (6.5.14): '(resp. un O_Y-Module) quasi-cohérent'", "'(resp.' upright", "italic (corollary body)",
    "convention", 6, "high", L(r"(resp. un", r"$\mathscr O_Y$-Module) quasi-cohérent"), L(r"\textup{(resp.} un", r"$\mathscr O_Y$-Module) quasi-cohérent"), C6R)
add(p, "Proof of (6.5.14) (i): '(I, 1.3.7)'", "(𝐈, 1.3.7): bold I", "(I, 1.3.7)",
    "convention", 2, "high", r"(I, 1.3.7)", r"(\textbf{I}, 1.3.7)", C2)
add(p, "Proof of (6.5.14) (i): 'que l'on a Tor_n^S(F, G)=H_n(L.⊗_S G);'",
    "the formula is set inline in the running text, followed by ';'", r"displayed with \[ ... \] (semicolon inside the display)",
    "other", None, "high",
    L(r"que l'on a", r"\[", r"  \mathscr{T}\!or_n^S(\mathscr F,\mathscr G)", r"  =\mathscr H_n(\mathscr L_\bullet\otimes_S\mathscr G);", r"\]", r"or,"),
    L(r"que l'on a", r"$\mathscr{T}\!or_n^S(\mathscr F,\mathscr G)", r"=\mathscr H_n(\mathscr L_\bullet\otimes_S\mathscr G)$;", r"or,"),
    "Layout: inline in the print.")
add(p, "Proof of (6.5.14) (i): '(I, 9.1.1)'", "(𝐈, 9.1.1): bold I", "(I, 9.1.1)",
    "convention", 2, "high", r"(I, 9.1.1)", r"(\textbf{I}, 9.1.1)", C2)
add(p, "Proof of (6.5.14) (i): 'est cohérent (0_I, 5.3.4)'", "(𝟎_I, 5.3.4): bold 0", r"($0_{\mathrm I}$, 5.3.4)",
    "convention", 2, "high", L(r"cohérent", r"($0_{\mathrm I}$, 5.3.4)"), L(r"cohérent", r"($\mathbf{0}_{\mathrm I}$, 5.3.4)"),
    "Bold 0 (GLOBAL_ISSUES item 35 form).")
add(p, "Proof of (6.5.14) (ii): '(I, 6.3.3)'", "(𝐈, 6.3.3): bold I", "(I, 6.3.3)",
    "convention", 2, "high", r"(I, 6.3.3)", r"(\textbf{I}, 6.3.3)", C2)
add(p, "Proof of (6.5.14) (ii): '(I, 6.3.7)'", "(𝐈, 6.3.7): bold I", "(I, 6.3.7)",
    "convention", 2, "high", r"(I, 6.3.7)", r"(\textbf{I}, 6.3.7)", C2)
add(p, "Proof of (6.5.14) (ii), end: 'la conclusion par (0_I, 5.3.4)'", "(𝟎_I, 5.3.4): bold 0", r"($0_{\mathrm I}$, 5.3.4)",
    "convention", 2, "high", r"par ($0_{\mathrm I}$, 5.3.4)", r"par ($\mathbf{0}_{\mathrm I}$, 5.3.4)", "Bold 0 (GLOBAL_ISSUES item 35 form).")
add(p, "(6.5.15): 'Z=X^(1)×_S X^(2)×_S ... ×_S X^(m)'", "baseline dots", r"\cdots",
    "symbol", None, "high", r"\times_S\cdots\times_S", r"\times_S\ldots\times_S", "Baseline dots in the print (checked on a crop).")
add(p, "end of the page: '... est Tor_•^S(P^(1), ..., P^(m)) :' followed on p. 153 by the display (6.5.15.1)",
    "no paragraph break: the display (6.5.15.1) at the top of p. 153 continues the sentence",
    r"blank line after ':' and before \oldpage[III]{153} (and another after the marker): spurious paragraph before the display",
    "other", None, "medium", L(r"^{(m)})$ :", "", ""), L(r"^{(m)})$ :", ""),
    "Apply together with the p. 153 finding that removes the blank line after \\oldpage[III]{153} (both blank lines must go).")

# ---------------- page 153 ----------------
p = 153
add(p, "top of the page: \\oldpage[III]{153} before the display (6.5.15.1)",
    "the display continues the sentence of p. 152", r"blank line between \oldpage[III]{153} and \[",
    "other", None, "medium", L(r"\oldpage[III]{153}", "", r"\["), L(r"\oldpage[III]{153}", r"\["),
    "Second half of the p. 152 finding (blank line before the marker); apply both.")
add(p, "(6.5.15.1): index of ⊕ 'q_1+q_2+...+q_m=q'", "baseline dots", r"\cdots",
    "symbol", None, "high", r"q_1+q_2+\cdots+q_m=q", r"q_1+q_2+\ldots+q_m=q", "Baseline dots (checked on a crop).")
add(p, "heading 6.6", "'... cas de la base affine.' (final full stop)", "no full stop",
    "punctuation", None, "high", r"cas de la base affine}", r"cas de la base affine.}",
    "The 6.1-6.6 titles of ega3-6-fr.tex lack the full stop that 6.7 onwards have (see final message).")
add(p, "(6.6.1): 'deux S-schémas quasi-compacts'", "'schémas' italic", "upright",
    "italics", None, "high", r"deux $S$-schémas", r"deux $S$-\emph{schémas}", "")
add(p, "(6.6.1): 'limité inférieurement, dont'", "'limité inférieurement' italic", "upright",
    "italics", None, "high", r"limité inférieurement, dont", r"\emph{limité inférieurement}, dont", "")
add(p, "(6.6.1): 'un recouvrement fini U^(i)'", "'fini' italic", "upright",
    "italics", None, "high", r"part un recouvrement fini", r"part un recouvrement \emph{fini}", "")
add(p, "(6.6.1): 'soit X=X^(1)×_S X^(2), qui est'", "inline in the running text", r"displayed with \[ ... \]",
    "other", None, "high", L(r"soit", r"\[", r"  X=X^{(1)}\times_S X^{(2)},", r"\]", r"qui est"),
    L(r"soit", r"$X=X^{(1)}\times_S X^{(2)}$,", r"qui est"), "Layout: inline in the print.")
add(p, "(6.6.1): '(I, 5.5.1 et 6.6.4)'", "(𝐈, 5.5.1 et 6.6.4): bold I", "(I, 5.5.1 et 6.6.4)",
    "convention", 2, "high", r"(I, 5.5.1 et 6.6.4)", r"(\textbf{I}, 5.5.1 et 6.6.4)", C2)
add(p, "(6.6.1): '(-p)-cochaînes alternées C^{-p}(U^(i), P_q^(i)) du recouvrement'", "inline in the running text", r"displayed with \[ ... \]",
    "other", None, "high", L(r"alternées", r"\[", r"  C^{-p}(\mathfrak U^{(i)},\mathscr P_q^{(i)})", r"\]", r"du recouvrement"),
    L(r"alternées", r"$C^{-p}(\mathfrak U^{(i)},\mathscr P_q^{(i)})$", r"du recouvrement"), "Layout: inline in the print.")
add(p, "(6.6.1): 'on a ainsi défini un bicomplexe'", "'bicomplexe' italic", "upright",
    "italics", None, "high", L(r"défini un", r"bicomplexe"), L(r"défini un", r"\emph{bicomplexe}"), "")
add(p, "(6.6.1): 'bicomplexe C^•(U^(i), P_•^(i)) de A-modules'", "inline in the running text", r"displayed with \[ ... \]",
    "other", None, "high", L(r"\[", r"  C^\bullet(\mathfrak U^{(i)},\mathscr P_\bullet^{(i)})", r"\]", r"de $A$-modules"),
    L(r"$C^\bullet(\mathfrak U^{(i)},\mathscr P_\bullet^{(i)})$", r"de $A$-modules"), "Layout: inline in the print.")
add(p, "(6.6.1): 'dont les deux opérateurs de dérivation'", "'deux' italic", "upright",
    "italics", None, "high", r"dont les deux opérateurs", r"dont les \emph{deux} opérateurs", "")
add(p, "(6.6.1): 'Il résulte des définitions (0, 12.1.2)'", "(𝟎, 12.1.2): bold 0, no subscript", r"($0_{\mathrm I}$, 12.1.2)",
    "extra", None, "high", r"($0_{\mathrm I}$, 12.1.2)", r"(\textbf{0}, 12.1.2)",
    "The print has no subscript I (§12 of chapter 0 is in 0_III); the edit also sets the bold 0 of the next finding.")
add(p, "(6.6.1): same reference (0, 12.1.2)", "bold 0", "plain 0", "convention", 2, "high", None, None,
    "Covered by the edit of the preceding finding.")
add(p, "(6.6.1): 'le A-module d'homologie H_n(C^•(U^(i), P_•^(i))) de ce bicomplexe'", "inline in the running text", r"displayed with \[ ... \]",
    "other", None, "high",
    L(r"d'homologie", r"\[", r"  \mathrm H_n\bigl(C^\bullet", r"  (\mathfrak U^{(i)},\mathscr P_\bullet^{(i)})\bigr)", r"\]", r"de ce bicomplexe"),
    L(r"d'homologie", r"$\mathrm H_n\bigl(C^\bullet", r"(\mathfrak U^{(i)},\mathscr P_\bullet^{(i)})\bigr)$", r"de ce bicomplexe"),
    "Layout: inline in the print.")
add(p, "(6.6.1): 'le A-module d'hypercohomologie H^{-n}(U^(i), P^(i)•)'", "'hypercohomologie' italic (first occurrence)", "upright",
    "italics", None, "high", r"que le $A$-module d'hypercohomologie", r"que le $A$-module d'\emph{hypercohomologie}", "")
add(p, "(6.6.1): 'H^{-n}(U^(i), P^(i)•) où P^(i)• est'", "no comma after the formula", r"comma at the end of the display",
    "punctuation", None, "high",
    L(r"\[", r"  \mathbf H^{-n}", r"  (\mathfrak U^{(i)},\mathscr P^{(i)\bullet}),", r"\]", r"où"),
    L(r"$\mathbf H^{-n}", r"(\mathfrak U^{(i)},\mathscr P^{(i)\bullet})$", r"où"),
    "Checked on a crop. The edit also sets the formula inline (next finding).")
add(p, "(6.6.1): same formula H^{-n}(U^(i), P^(i)•)", "inline in the running text", r"displayed with \[ ... \]",
    "other", None, "high", None, None, "Covered by the edit of the preceding finding.")
add(p, "(6.6.2): 'par rapport aux bicomplexes (0, 11.7.4)'", "(𝟎, 11.7.4): bold 0, no subscript", r"($0_{\mathrm I}$, 11.7.4)",
    "extra", None, "high", r"($0_{\mathrm I}$, 11.7.4)", r"(\textbf{0}, 11.7.4)",
    "No subscript I in the print (§11 of chapter 0 is in 0_III); the edit also sets the bold 0.")
add(p, "(6.6.2): same reference (0, 11.7.4)", "bold 0", "plain 0", "convention", 2, "high", None, None,
    "Covered by the edit of the preceding finding.")
add(p, "(6.6.2): 'les cochaînes considérées sont alternées'", "'alternées' italic", "upright",
    "italics", None, "high", L(r"sont", r"alternées"), L(r"sont", r"\emph{alternées}"), "")
add(p, "(6.6.2): 'un nombre fini (indépendant de q) de valeurs de p'", "'fini (indépendant de q)' italic", "upright",
    "italics", None, "high", r"nombre fini (indépendant de $q$)", r"nombre \emph{fini (indépendant de $q$)}", "")
add(p, "(6.6.2): 'les deux degrés de chacun des L^(i)'", "'deux' italic", "upright",
    "italics", None, "high", L(r"les", r"deux degrés"), L(r"les", r"\emph{deux} degrés"), "")
add(p, "(6.6.2): 'sont limités inférieurement. Nous'", "'limités inférieurement' italic", "upright",
    "italics", None, "high", L(r"sont limités", r"inférieurement."), L(r"sont \emph{limités", r"inférieurement}."), "")
add(p, "(6.6.2): 'Nous désignerons par Tor_n^A(L^(1), L^(2)) ou ...'", "inline in the running text", r"displayed with \[ ... \]",
    "other", None, "high",
    L(r"\[", r"  \mathbf{Tor}_n^A(L_{\bullet\bullet}^{(1)},L_{\bullet\bullet}^{(2)})", r"\]"),
    r"$\mathbf{Tor}_n^A(L_{\bullet\bullet}^{(1)},L_{\bullet\bullet}^{(2)})$", "Layout: inline in the print.")
add(p, "(6.6.2): '... ou Tor_n^S(U^(1), U^(2); P_•^(1), P_•^(2)) le n-ème module'", "inline in the running text", r"displayed with \[ ... \]",
    "other", None, "high",
    L(r"ou", r"\[", r"  \mathbf{Tor}_n^S", r"  (\mathfrak U^{(1)},\mathfrak U^{(2)};", r"   \mathscr P_\bullet^{(1)},\mathscr P_\bullet^{(2)})", r"\]"),
    L(r"ou", r"$\mathbf{Tor}_n^S", r"(\mathfrak U^{(1)},\mathfrak U^{(2)};", r"\mathscr P_\bullet^{(1)},\mathscr P_\bullet^{(2)})$"),
    "Layout: inline in the print (bold Tor correct here).")
add(p, "(6.6.2): 'le n-ème module d'hyperhomologie'", "n-ème", r"$n$-ième",
    "word", None, "high", r"le $n$-ième module", r"le $n$-ème module", "Checked on a crop; ega3-6 writes -ème elsewhere ((-p)-ème).")
add(p, "(6.6.2): 'on écrit Tor_n^S(U^(1), U^(2); F^(1), F^(2)) leur hypertor'", "script 𝒯or (not bold), inline",
    r"\mathbf{Tor}_n^S, displayed", "font", None, "high",
    L(r"on écrit", r"\[", r"  \mathbf{Tor}_n^S", r"  (\mathfrak U^{(1)},\mathfrak U^{(2)};", r"   \mathscr F^{(1)},\mathscr F^{(2)})", r"\]", r"leur hypertor."),
    L(r"on écrit", r"$\mathscr{T}\!or_n^S", r"(\mathfrak U^{(1)},\mathfrak U^{(2)};", r"\mathscr F^{(1)},\mathscr F^{(2)})$", r"leur hypertor."),
    "Checked on a crop: the print distinguishes the bold hypertor of complexes from this non-bold symbol (here script, roman Tor in (6.6.5)-(6.6.7)). The edit also sets the formula inline (next finding).")
add(p, "(6.6.2): same formula", "inline in the running text", r"displayed with \[ ... \]",
    "other", None, "high", None, None, "Covered by the edit of the preceding finding.")
add(p, "(6.6.2): 'On désignera par Tor_n^S(U^(1), U^(2); P_•^(1), P_•^(2)), suivant'", "script 𝒯or (not bold), inline",
    r"\mathbf{Tor}_n^S, displayed", "font", None, "high",
    L(r"On désignera par", r"\[", r"  \mathbf{Tor}_n^S", r"  (\mathfrak U^{(1)},\mathfrak U^{(2)};", r"   \mathscr P_\bullet^{(1)},\mathscr P_\bullet^{(2)}),", r"\]", r"suivant"),
    L(r"On désignera par", r"$\mathscr{T}\!or_n^S", r"(\mathfrak U^{(1)},\mathfrak U^{(2)};", r"\mathscr P_\bullet^{(1)},\mathscr P_\bullet^{(2)})$,", r"suivant"),
    "The bicomplex of the general conventions (non-bold); checked on a crop. The edit also sets the formula inline (next finding).")
add(p, "(6.6.2): same formula", "inline in the running text", r"displayed with \[ ... \]",
    "other", None, "high", None, None, "Covered by the edit of the preceding finding.")
add(p, "(6.6.2): 'le bicomplexe dont le composant'", "'bicomplexe' italic", "upright",
    "italics", None, "high", r"le bicomplexe dont", r"le \emph{bicomplexe} dont", "")
add(p, "(6.6.2): 'composant d'indices (j, k) est Tor_n^S(U^(1), U^(2); P_j^(1), P_k^(2)).'", "script 𝒯or (not bold), inline",
    r"\mathbf{Tor}_n^S, displayed", "font", None, "high",
    L(r"est", r"\[", r"  \mathbf{Tor}_n^S", r"  (\mathfrak U^{(1)},\mathfrak U^{(2)};", r"   \mathscr P_j^{(1)},\mathscr P_k^{(2)}).", r"\]"),
    L(r"est", r"$\mathscr{T}\!or_n^S", r"(\mathfrak U^{(1)},\mathfrak U^{(2)};", r"\mathscr P_j^{(1)},\mathscr P_k^{(2)})$."),
    "Checked on a crop. The edit also sets the formula inline (next finding).")
add(p, "(6.6.2): same formula", "inline in the running text", r"displayed with \[ ... \]",
    "other", None, "high", None, None, "Covered by the edit of the preceding finding.")

# ---------------- page 154 ----------------
p = 154
E_NOTE = "Roman E for the spectral sequences of A-modules (t)E (the sheaf sequence ''ℰ of 6.5 is script); checked on crops."
add(p, "line 1: '(I, 5.5.6 et 1.3.11)'", "(𝐈, 5.5.6 et 1.3.11): bold I", "(I, 5.5.6 et 1.3.11)",
    "convention", 2, "high", r"(I, 5.5.6 et 1.3.11)", r"(\textbf{I}, 5.5.6 et 1.3.11)", C2)
add(p, "(6.6.2): 'est un bi-∂-foncteur covariant en'", "'bi-∂-foncteur covariant' italic", "upright",
    "italics", None, "high", r"bi-$\partial$-foncteur covariant", r"\emph{bi-$\partial$-foncteur covariant}", "")
add(p, "(6.6.2): 'des A-modules (0, 11.7.3)'", "(𝟎, 11.7.3): bold 0, no subscript", r"($0_{\mathrm I}$, 11.7.3)",
    "extra", None, "high", r"($0_{\mathrm I}$, 11.7.3)", r"(\textbf{0}, 11.7.3)", "No subscript I in the print; the edit also sets the bold 0.")
add(p, "(6.6.2): same reference (0, 11.7.3)", "bold 0", "plain 0", "convention", 2, "high", None, None, "Covered by the edit of the preceding finding.")
add(p, "(6.6.2): 'on sait (0, 11.7.2)'", "(𝟎, 11.7.2): bold 0, no subscript", r"($0_{\mathrm I}$, 11.7.2)",
    "extra", None, "high", r"($0_{\mathrm I}$, 11.7.2)", r"(\textbf{0}, 11.7.2)", "No subscript I in the print; the edit also sets the bold 0.")
add(p, "(6.6.2): same reference (0, 11.7.2)", "bold 0", "plain 0", "convention", 2, "high", None, None, "Covered by the edit of the preceding finding.")
add(p, "(6.6.2): 'six foncteurs spectraux biréguliers'", "'biréguliers' italic", "upright",
    "italics", None, "high", r"spectraux biréguliers,", r"spectraux \emph{biréguliers},", "")
add(p, "(6.6.2): 'la notation (t)E^S(U^(1), U^(2); P_•^(1), P_•^(2))'", "roman E, inline", r"\mathscr E, displayed",
    "font", None, "high",
    L(r"\[", r"  {}^{(t)}\mathscr E^S", r"  (\mathfrak U^{(1)},\mathfrak U^{(2)};", r"   \mathscr P_\bullet^{(1)},\mathscr P_\bullet^{(2)})", r"\]"),
    L(r"${}^{(t)}E^S", r"(\mathfrak U^{(1)},\mathfrak U^{(2)};", r"\mathscr P_\bullet^{(1)},\mathscr P_\bullet^{(2)})$"),
    E_NOTE + " The edit also sets the formula inline (next finding).")
add(p, "(6.6.2): same formula", "inline in the running text", r"displayed with \[ ... \]",
    "other", None, "high", None, None, "Covered by the edit of the preceding finding.")
add(p, "(6.6.2): 'ou (t)E(U^(1), U^(2); P_•^(1), P_•^(2)), où t'", "roman E, inline", r"\mathscr E, displayed",
    "font", None, "high",
    L(r"\[", r"  {}^{(t)}\mathscr E", r"  (\mathfrak U^{(1)},\mathfrak U^{(2)};", r"   \mathscr P_\bullet^{(1)},\mathscr P_\bullet^{(2)}),", r"\]"),
    L(r"${}^{(t)}E", r"(\mathfrak U^{(1)},\mathfrak U^{(2)};", r"\mathscr P_\bullet^{(1)},\mathscr P_\bullet^{(2)})$,"),
    E_NOTE + " The edit also sets the formula inline (next finding).")
add(p, "(6.6.2): same formula", "inline in the running text", r"displayed with \[ ... \]",
    "other", None, "high", None, None, "Covered by the edit of the preceding finding.")
add(p, "(6.6.2) display, line (a): (a)E^2_pq", "roman E", r"\mathscr E", "font", None, "high",
    L(r"{}^{(a)}\mathscr E_{pq}^2", r"  &="), L(r"{}^{(a)}E_{pq}^2", r"  &="), E_NOTE)
add(p, "(6.6.2) display, line (a): '⊕ Tor_p^A(H_{q_1}(L^(1)), H_{q_2}(L^(2)))'", "Tor not bold (roman)", r"\mathbf{Tor}_p^A",
    "font", None, "high", L(r"\mathbf{Tor}_p^A", r"    \bigl(\mathrm H_{q_1}(L"), L(r"\operatorname{Tor}_p^A", r"    \bigl(\mathrm H_{q_1}(L"),
    "Checked on a crop: lines (a) and (b') have the ordinary Tor, lines (b), (a'), (c), (d) the bold hypertor.")
add(p, "(6.6.2) display, end of line (a)", "no comma", "comma before \\\\",
    "punctuation", None, "high", r"\mathrm H_{q_2}(L_{\bullet\bullet}^{(2)})\bigr),\\", r"\mathrm H_{q_2}(L_{\bullet\bullet}^{(2)})\bigr)\\",
    "Only line (d) ends with a comma in the print (crop).")
add(p, "(6.6.2) display, line (b): (b)E^2_pq", "roman E", r"\mathscr E", "font", None, "high",
    r"{}^{(b)}\mathscr E_{pq}^2", r"{}^{(b)}E_{pq}^2", E_NOTE)
add(p, "(6.6.2) display, end of line (b)", "no comma", "comma before \\\\",
    "punctuation", None, "high", L(r"{A,\mathrm{II}}", r"    (L_{\bullet\bullet}^{(1)},L_{\bullet\bullet}^{(2)})\bigr),\\"),
    L(r"{A,\mathrm{II}}", r"    (L_{\bullet\bullet}^{(1)},L_{\bullet\bullet}^{(2)})\bigr)\\"), "")
add(p, "(6.6.2) display, line (a'): (a')E^2_pq", "roman E", r"\mathscr E", "font", None, "high",
    L(r"{}^{(a')}\mathscr E_{pq}^2", r"  &="), L(r"{}^{(a')}E_{pq}^2", r"  &="), E_NOTE)
add(p, "(6.6.2) display, end of line (a')", "no comma", "comma before \\\\",
    "punctuation", None, "high", r"\mathrm H_{q_2}^{\mathrm I}(L_{\bullet\bullet}^{(2)})\bigr),\\", r"\mathrm H_{q_2}^{\mathrm I}(L_{\bullet\bullet}^{(2)})\bigr)\\", "")
add(p, "(6.6.2) display, line (b'): (b')E^2_pq", "roman E", r"\mathscr E", "font", None, "high",
    r"{}^{(b')}\mathscr E_{pq}^2", r"{}^{(b')}E_{pq}^2", E_NOTE)
add(p, "(6.6.2) display, line (b'): 'H_p(Tor_q^A(L^(1), L^(2)))'", "Tor not bold (roman), no comma at the end of the line", r"\mathbf{Tor}_q^A ... \bigr),\\",
    "font", None, "high",
    L(r"\mathbf{Tor}_q^A", r"    (L_{\bullet\bullet}^{(1)},L_{\bullet\bullet}^{(2)})\bigr),\\"),
    L(r"\operatorname{Tor}_q^A", r"    (L_{\bullet\bullet}^{(1)},L_{\bullet\bullet}^{(2)})\bigr)\\"),
    "Checked on a crop. The edit also removes the comma (next finding).")
add(p, "(6.6.2) display, end of line (b')", "no comma", "comma before \\\\", "punctuation", None, "high", None, None,
    "Covered by the edit of the preceding finding.")
add(p, "(6.6.2) display, line (c): (c)E^2_pq", "roman E", r"\mathscr E", "font", None, "high",
    r"{}^{(c)}\mathscr E_{pq}^2", r"{}^{(c)}E_{pq}^2", E_NOTE)
add(p, "(6.6.2) display, end of line (c)", "no comma", "comma before \\\\",
    "punctuation", None, "high", r"\mathrm H_{q_2}^{\mathrm{II}}(L_{\bullet\bullet}^{(2)})\bigr),\\", r"\mathrm H_{q_2}^{\mathrm{II}}(L_{\bullet\bullet}^{(2)})\bigr)\\", "")
add(p, "(6.6.2) display, line (d): (d)E^2_pq", "roman E", r"\mathscr E", "font", None, "high",
    r"{}^{(d)}\mathscr E_{pq}^2", r"{}^{(d)}E_{pq}^2", E_NOTE)
add(p, "(6.6.3), display (a)E^2_pq = ⊕ Tor_p^A(H^{-q_1}(X^(1), P_•^(1)), H^{-q_2}(X^(2), P_•^(2)))", "Tor not bold (roman); the H are bold",
    r"\mathbf{Tor}_p^A", "font", None, "high",
    L(r"{}^{(a)}\mathscr E_{pq}^2", r"  =\bigoplus_{q_1+q_2=q}", r"   \mathbf{Tor}_p^A"),
    L(r"{}^{(a)}E_{pq}^2", r"  =\bigoplus_{q_1+q_2=q}", r"   \operatorname{Tor}_p^A"),
    "Checked on a crop. The TeX's (a) and (a') displays of (6.6.3) are identical; the print has ordinary Tor with bold H in (a), bold Tor with plain H in (a'). The edit also sets the roman E (next finding).")
add(p, "(6.6.3), display (a): (a)E^2_pq", "roman E", r"\mathscr E", "font", None, "high", None, None,
    "Covered by the edit of the preceding finding.")
add(p, "(6.6.3): 'le module de cohomologie H^{-n}(U^(i), P_k^(i))'", "'cohomologie' italic", "upright",
    "italics", None, "high", r"le module de cohomologie", r"le module de \emph{cohomologie}", "")
add(p, "(6.6.3): 'H^{-n}(U^(i), P_k^(i)); on sait (1.4.1)'", "plain H (not bold)", r"\mathbf H^{-n}",
    "font", None, "high", r"$\mathbf H^{-n}(\mathfrak U^{(i)},\mathscr P_k^{(i)})$", r"$\mathrm H^{-n}(\mathfrak U^{(i)},\mathscr P_k^{(i)})$",
    "Cohomology of the single sheaf P_k: plain H in the print (crop).")
add(p, "(6.6.3): 'canoniquement isomorphe à H^{-n}(X^(i), P_k^(i)); donc'", "plain H (not bold)", r"\mathbf H^{-n}",
    "font", None, "high", r"$\mathbf H^{-n}(X^{(i)},\mathscr P_k^{(i)})$", r"$\mathrm H^{-n}(X^{(i)},\mathscr P_k^{(i)})$", "Checked on a crop.")
add(p, "(6.6.3), display (a')E^2_pq = ⊕ Tor_p^A(H^{-q_1}(X^(1), P_•^(1)), H^{-q_2}(X^(2), P_•^(2)))", "both H plain (not bold); Tor bold",
    r"\mathbf H^{-q_1}, \mathbf H^{-q_2}", "font", None, "high",
    L(r"{}^{(a')}\mathscr E_{pq}^2", r"  =\bigoplus_{q_1+q_2=q}", r"   \mathbf{Tor}_p^A",
      r"   \bigl(\mathbf H^{-q_1}(X^{(1)},\mathscr P_\bullet^{(1)}),", r"         \mathbf H^{-q_2}(X^{(2)},\mathscr P_\bullet^{(2)})\bigr)."),
    L(r"{}^{(a')}E_{pq}^2", r"  =\bigoplus_{q_1+q_2=q}", r"   \mathbf{Tor}_p^A",
      r"   \bigl(\mathrm H^{-q_1}(X^{(1)},\mathscr P_\bullet^{(1)}),", r"         \mathrm H^{-q_2}(X^{(2)},\mathscr P_\bullet^{(2)})\bigr)."),
    "Checked on a crop. The edit also sets the roman E (next finding).")
add(p, "(6.6.3), display (a'): (a')E^2_pq", "roman E", r"\mathscr E", "font", None, "high", None, None,
    "Covered by the edit of the preceding finding.")
add(p, "(6.6.4): 'somme directe des A-modules Tor_q^A(Γ(U_σ^(1), P_•^(1)), Γ(U_τ^(2), P_•^(2))), où σ'", "inline in the running text",
    r"displayed with \[ ... \]", "other", None, "high",
    L(r"des $A$-modules", r"\[", r"  \mathbf{Tor}_q^A", r"  \bigl(\Gamma(U_\sigma^{(1)},\mathscr P_\bullet^{(1)}),", r"        \Gamma(U_\tau^{(2)},\mathscr P_\bullet^{(2)})\bigr),", r"\]"),
    L(r"des $A$-modules", r"$\mathbf{Tor}_q^A", r"\bigl(\Gamma(U_\sigma^{(1)},\mathscr P_\bullet^{(1)}),", r"\Gamma(U_\tau^{(2)},\mathscr P_\bullet^{(2)})\bigr)$,"),
    "Layout: inline in the print.")

# ---------------- page 155 ----------------
p = 155
add(p, "line 1: 'On voit donc que (b)E^2_pq est le'", "roman E", r"\mathscr E", "font", None, "high",
    r"${}^{(b)}\mathscr E_{pq}^2$ est le", r"${}^{(b)}E_{pq}^2$ est le", E_NOTE)
add(p, "line 2: 'du complexe L^•(Φ^(1), Φ^(2); S) des cochaînes'", "inline in the running text", r"displayed with \[ ... \]",
    "other", None, "high", L(r"\[", r"  L^\bullet(\Phi^{(1)},\Phi^{(2)};\mathscr S)", r"\]"), r"$L^\bullet(\Phi^{(1)},\Phi^{(2)};\mathscr S)$",
    "Layout: inline in the print.")
add(p, "line 2: 'des cochaînes bi-alternées sur'", "'bi-alternées' italic", "upright",
    "italics", None, "high", r"des cochaînes bi-alternées", r"des cochaînes \emph{bi-alternées}", "")
add(p, "line 2: 'à valeurs dans le système de coefficients'", "'système de coefficients' italic", "upright",
    "italics", None, "high", L(r"dans le", r"système de coefficients"), L(r"dans le", r"\emph{système de coefficients}"), "")
add(p, "after the display of S: '(0, 11.8.4)'", "(𝟎, 11.8.4): bold 0, no subscript", r"($0_{\mathrm I}$, 11.8.4)",
    "extra", None, "high", r"($0_{\mathrm I}$, 11.8.4)", r"(\textbf{0}, 11.8.4)", "No subscript I in the print; the edit also sets the bold 0.")
add(p, "same reference (0, 11.8.4)", "bold 0", "plain 0", "convention", 2, "high", None, None, "Covered by the edit of the preceding finding.")
add(p, "'On sait alors (0, 11.8.5 et 11.8.6)'", "(𝟎, 11.8.5 et 11.8.6): bold 0, no subscript", r"($0_{\mathrm I}$, 11.8.5 et 11.8.6)",
    "extra", None, "high", r"($0_{\mathrm I}$, 11.8.5 et 11.8.6)", r"(\textbf{0}, 11.8.5 et 11.8.6)", "No subscript I in the print; the edit also sets the bold 0.")
add(p, "same reference (0, 11.8.5 et 11.8.6)", "bold 0", "plain 0", "convention", 2, "high", None, None, "Covered by the edit of the preceding finding.")
add(p, "'de toutes les cochaînes sur Φ^(1)'", "'toutes' italic", "upright",
    "italics", None, "high", r"de toutes les cochaînes", r"de \emph{toutes} les cochaînes", "")
add(p, "display λ(σ, τ)∈Γ(U_σ^(1)×_S U_τ^(2), Tor_q^S(P_•^(1), P_•^(2)))", "no comma after the display", "comma at the end of the display",
    "punctuation", None, "high",
    L(r"(\mathscr P_\bullet^{(1)},\mathscr P_\bullet^{(2)})\bigr),", r"\]", r"où $\sigma"),
    L(r"(\mathscr P_\bullet^{(1)},\mathscr P_\bullet^{(2)})\bigr)", r"\]", r"où $\sigma"), "Checked on a crop.")
add(p, "'des suites ayant même nombre d'éléments. Mais'", "'même nombre d'éléments' italic", "upright",
    "italics", None, "high", r"ayant même nombre d'éléments.", r"ayant \emph{même nombre d'éléments}.", "")
add(p, "'Mais on a alors U_σ^(1)×_S U_τ^(2)=(U_{α_0}^(1)×_S U_{β_0}^(2))∩...∩(U_{α_h}^(1)×_S U_{β_h}^(2)) (I, 3.2.7). Si'",
    "inline in the running text, the reference in the text", r"displayed with \[ ... \], reference as \qquad\text{(I, 3.2.7)}",
    "other", None, "high",
    L(r"Mais on a alors", r"\[", r"  U_\sigma^{(1)}\times_S U_\tau^{(2)}",
      r"  =(U_{\alpha_0}^{(1)}\times_S U_{\beta_0}^{(2)})\cap\cdots\cap",
      r"    (U_{\alpha_h}^{(1)}\times_S U_{\beta_h}^{(2)})", r"  \qquad\text{(I, 3.2.7)}.", r"\]"),
    L(r"Mais on a alors", r"$U_\sigma^{(1)}\times_S U_\tau^{(2)}",
      r"=(U_{\alpha_0}^{(1)}\times_S U_{\beta_0}^{(2)})\cap\ldots\cap",
      r"(U_{\alpha_h}^{(1)}\times_S U_{\beta_h}^{(2)})$", r"(\textbf{I}, 3.2.7)."),
    "Layout: inline in the print. The edit also covers the next two findings (baseline dots, bold I).")
add(p, "same formula: '∩...∩'", "baseline dots", r"\cdots", "symbol", None, "high", None, None,
    "Covered by the edit of the preceding finding (checked on a crop).")
add(p, "same place: '(I, 3.2.7)'", "(𝐈, 3.2.7): bold I", r"\text{(I, 3.2.7)}", "convention", 2, "high", None, None,
    "Covered by the edit of the preceding finding.")
add(p, "'compte tenu de ce que X^(1)×_S X^(2) est un schéma'", "'schéma' italic", "upright",
    "italics", None, "high", r"est un schéma, que", r"est un \emph{schéma}, que", "")
add(p, "display (b)E^2_pq = H^{-p}(X^(1)×_S X^(2), Tor_q^S(P_•^(1), P_•^(2)).", "roman E", r"\mathscr E", "font", None, "high",
    L(r"{}^{(b)}\mathscr E_{pq}^2", r"  =\mathbf H^{-p}"), L(r"{}^{(b)}E_{pq}^2", r"  =\mathbf H^{-p}"), E_NOTE)
add(p, "same display, end: '..., Tor_q^S(P_•^(1), P_•^(2)).'",
    "only one closing parenthesis: 'H^{-p}(X^(1)×_S X^(2), Tor_q^S(P_•^(1), P_•^(2)).' (checked on a crop)",
    r"balanced: \mathbf H^{-p}\bigl( ... (\mathscr P_\bullet^{(1)},\mathscr P_\bullet^{(2)})\bigr).",
    "misprint_in_print", None, "high",
    L(r"\bigl(X^{(1)}\times_S X^{(2)},", r"    \mathscr{T}\!or_q^S", r"    (\mathscr P_\bullet^{(1)},\mathscr P_\bullet^{(2)})\bigr).", r"\]", "", r"En second"),
    L(r"(X^{(1)}\times_S X^{(2)},", r"    \mathscr{T}\!or_q^S", r"    (\mathscr P_\bullet^{(1)},\mathscr P_\bullet^{(2)}).", r"\]", "", r"En second"),
    "The TeX silently corrects the missing parenthesis; the edit restores the printed reading.",
    corrected=r"\mathbf H^{-p}\bigl(X^{(1)}\times_S X^{(2)},\mathscr{T}\!or_q^S(\mathscr P_\bullet^{(1)},\mathscr P_\bullet^{(2)})\bigr).")
add(p, "'En second lieu, Tor_q^A(L^(1), L^(2)) est un bicomplexe'", "Tor not bold (roman)", r"\mathbf{Tor}_q^A",
    "font", None, "high", r"$\mathbf{Tor}_q^A(L_{\bullet\bullet}^{(1)},L_{\bullet\bullet}^{(2)})$ est un",
    r"$\operatorname{Tor}_q^A(L_{\bullet\bullet}^{(1)},L_{\bullet\bullet}^{(2)})$ est un",
    "The bicomplex of ordinary Tor of (b'); checked on a crop.")
add(p, "display Tor_q^A(C^{-h_1}(U^(1), P_{k_1}^(1)), C^{-h_2}(U^(2), P_{k_2}^(2)))", "Tor not bold (roman)", r"\mathbf{Tor}_q^A",
    "font", None, "high", L(r"\mathbf{Tor}_q^A", r"  \bigl(C^{-h_1}"), L(r"\operatorname{Tor}_q^A", r"  \bigl(C^{-h_1}"), "Checked on a crop.")
add(p, "display Γ(U_σ^(1)×_S U_τ^(2), Tor_q^S(P_{k_1}^(1), P_{k_2}^(2)))", "no comma after the display", "comma at the end of the display",
    "punctuation", None, "high", L(r"(\mathscr P_{k_1}^{(1)},\mathscr P_{k_2}^{(2)})\bigr),", r"\]"),
    L(r"(\mathscr P_{k_1}^{(1)},\mathscr P_{k_2}^{(2)})\bigr)", r"\]"), "Checked on a crop.")
add(p, "'Le terme (b')E^2_pq que nous calculons'", "roman E", r"\mathscr E", "font", None, "high",
    r"${}^{(b')}\mathscr E_{pq}^2$ que", r"${}^{(b')}E_{pq}^2$ que", E_NOTE)
add(p, "'le complexe de cochaînes bi-alternées sur Φ^(1)'", "'bi-alternées' italic", "upright",
    "italics", None, "high", r"de cochaînes bi-alternées", r"de cochaînes \emph{bi-alternées}", "")
add(p, "display S_k : (σ, τ) ⇝ Γ(U_σ^(1)×U_τ^(2), ⊕ Tor_q^S(P_{-k_1}^(1), P_{-k_2}^(2)))",
    "'U_σ^(1)×U_τ^(2)': no subscript S on × (checked on a crop; ×_S in every parallel formula)", r"\times_S",
    "misprint_in_print", None, "high",
    L(r"\leadsto", r"  \Gamma\left(U_\sigma^{(1)}\times_S U_\tau^{(2)},"),
    L(r"\leadsto", r"  \Gamma\left(U_\sigma^{(1)}\times U_\tau^{(2)},"),
    "The TeX silently corrects; the edit restores the printed reading.",
    corrected=r"\Gamma\left(U_\sigma^{(1)}\times_S U_\tau^{(2)},")
add(p, "same display S_k, end", "no comma after the display", "comma at the end of the display",
    "punctuation", None, "high",
    L(r"(\mathscr P_{-k_1}^{(1)},\mathscr P_{-k_2}^{(2)})\right),", r"\]", r"ces"),
    L(r"(\mathscr P_{-k_1}^{(1)},\mathscr P_{-k_2}^{(2)})\right)", r"\]", r"ces"), "Checked on a crop.")
add(p, "'formant un complexe S^• où la différentielle'", "'complexe' italic", "upright",
    "italics", None, "high", r"formant un complexe", r"formant un \emph{complexe}", "")
add(p, "'de celle du complexe simple associée au bicomplexe'", "associée", "associé",
    "misprint_in_print", None, "medium", r"celle du complexe simple associé", r"celle du complexe simple associée",
    "Checked on a crop. Probably a slip (the phrase is 'le complexe simple associé au bicomplexe' elsewhere, e.g. on p. 155 below); the TeX silently corrects.",
    corrected="associé")
add(p, "'associée au bicomplexe Tor_q^S(P^(1)•, P^(2)•). On sait'", "bullets as superscripts: P^(1)•, P^(2)• (cohomological indexing)",
    r"\mathscr P_\bullet^{(1)}, \mathscr P_\bullet^{(2)} (subscript bullets)", "formula", None, "high",
    r"(\mathscr P_\bullet^{(1)},\mathscr P_\bullet^{(2)})$. On sait", r"(\mathscr P^{(1)\bullet},\mathscr P^{(2)\bullet})$. On sait",
    "Checked on a crop; same notation as P^(i)• in (6.6.1).")
add(p, "'du bicomplexe C^•(Φ^(1), Φ^(2); S^•) (0, 11.8.9)'", "(𝟎, 11.8.9): bold 0, no subscript", r"($0_{\mathrm I}$, 11.8.9)",
    "extra", None, "high", r"($0_{\mathrm I}$, 11.8.9)", r"(\textbf{0}, 11.8.9)", "No subscript I in the print; the edit also sets the bold 0.")
add(p, "same reference (0, 11.8.9)", "bold 0", "plain 0", "convention", 2, "high", None, None, "Covered by the edit of the preceding finding.")
add(p, "display λ(σ, τ)∈Γ(U_σ^(1)×_S U_τ^(2), ⊕ Tor_q^S(P_{-k_1}^(1), P_{-k_2}^(2)))", "no comma after the display", "comma at the end of the display",
    "punctuation", None, "high",
    L(r"(\mathscr P_{-k_1}^{(1)},\mathscr P_{-k_2}^{(2)})\right),", r"\]", r"$\sigma"),
    L(r"(\mathscr P_{-k_1}^{(1)},\mathscr P_{-k_2}^{(2)})\right)", r"\]", r"$\sigma"), "Checked on a crop.")
add(p, "'étant des suites ayant même nombre d'éléments (0, 11.8.10)'", "'même nombre d'éléments' italic", "upright",
    "italics", None, "high", L(r"ayant même nombre", r"d'éléments"), L(r"ayant \emph{même nombre", r"d'éléments}"), "")
add(p, "same sentence: '(0, 11.8.10)'", "(𝟎, 11.8.10): bold 0, no subscript", r"($0_{\mathrm I}$, 11.8.10)",
    "extra", None, "high", r"($0_{\mathrm I}$, 11.8.10)", r"(\textbf{0}, 11.8.10)", "No subscript I in the print; the edit also sets the bold 0.")
add(p, "same reference (0, 11.8.10)", "bold 0", "plain 0", "convention", 2, "high", None, None, "Covered by the edit of the preceding finding.")
add(p, "'On voit alors comme ci-dessus que (b')E^2_pq est le'", "roman E", r"\mathscr E", "font", None, "high",
    r"${}^{(b')}\mathscr E_{pq}^2$ est le", r"${}^{(b')}E_{pq}^2$ est le", E_NOTE)
add(p, "'associé au bicomplexe Tor_q^S(P^(1)•, P^(2)•) de O_Z-Modules'", "bullets as superscripts: P^(1)•, P^(2)•",
    r"\mathscr P_\bullet^{(1)}, \mathscr P_\bullet^{(2)}", "formula", None, "high",
    r"(\mathscr P_\bullet^{(1)},\mathscr P_\bullet^{(2)})$ de", r"(\mathscr P^{(1)\bullet},\mathscr P^{(2)\bullet})$ de", "Checked on a crop.")
add(p, "last display: (b')E^2_pq = H^{-p}(...)", "roman E", r"\mathscr E", "font", None, "high",
    L(r"{}^{(b')}\mathscr E_{pq}^2", ""), L(r"{}^{(b')}E_{pq}^2", ""), E_NOTE)

# ---------------- page 156 ----------------
p = 156
T667 = "The print writes (6.6.7, t)) with two closing parentheses, in the label and in every reference on this page (crops)."
add(p, "(6.6.5), display (c)E^2_pq", "roman E", r"\mathscr E", "font", None, "high",
    r"{}^{(c)}\mathscr E_{pq}^2", r"{}^{(c)}E_{pq}^2", E_NOTE)
add(p, "(6.6.5), display (c): '⊕ Tor_p^S(U^(1), U^(2); H_{q_1}(P_•^(1)), H_{q_2}(P_•^(2)))'", "roman Tor (not bold)", r"\mathbf{Tor}_p^S",
    "font", None, "high", r"\mathbf{Tor}_p^S", r"\operatorname{Tor}_p^S",
    "Hypertor of two Modules relative to two coverings (6.6.2): non-bold, here roman Tor (script 𝒯or in (6.6.2)); checked on a crop.")
add(p, "(6.6.5): 'est le A-module Tor_q^S(U^(1), U^(2); P_h^(1), P_k^(2)). On a donc'", "roman Tor (not bold)", r"\mathbf{Tor}_q^S",
    "font", None, "high", L(r"$\mathbf{Tor}_q^S", r"(\mathfrak U^{(1)}"), L(r"$\operatorname{Tor}_q^S", r"(\mathfrak U^{(1)}"), "Checked on a crop.")
add(p, "(6.6.5), display (d)E^2_pq", "roman E", r"\mathscr E", "font", None, "high",
    r"{}^{(d)}\mathscr E_{pq}^2", r"{}^{(d)}E_{pq}^2", E_NOTE)
add(p, "(6.6.5), display (d): 'H_p(Tor_q^S(U^(1), U^(2); P_•^(1), P_•^(2)))'", "roman Tor (not bold)", r"\mathbf{Tor}_q^S",
    "font", None, "high", L(r"\mathrm H_p\bigl(", r"    \mathbf{Tor}_q^S"), L(r"\mathrm H_p\bigl(", r"    \operatorname{Tor}_q^S"), "Checked on a crop.")
add(p, "(6.6.6): 'des foncteurs de bicomplexes (0, 11.7.3)'", "(𝟎, 11.7.3): bold 0, no subscript", r"($0_{\mathrm I}$, 11.7.3)",
    "extra", None, "high", r"($0_{\mathrm I}$, 11.7.3)", r"(\textbf{0}, 11.7.3)", "No subscript I in the print; the edit also sets the bold 0.")
add(p, "same reference (0, 11.7.3)", "bold 0", "plain 0", "convention", 2, "high", None, None, "Covered by the edit of the preceding finding.")
add(p, "(6.6.6): 'résolution plate de Cartan-Eilenberg M^(i)_••• de L^(i)_••'", "M with three bullets (tricomplex)", r"M_{\bullet\bullet}^{(i)} (two bullets)",
    "formula", None, "high", r"Cartan-Eilenberg $M_{\bullet\bullet}^{(i)}$", r"Cartan-Eilenberg $M_{\bullet\bullet\bullet}^{(i)}$",
    "Checked on a crop; every M of (6.6.6) has three bullets, L two.")
add(p, "(6.6.6.1): H_•(M^(1)_•••⊗_A M^(2)_•••)", "three bullets on both M", r"two bullets",
    "formula", None, "high", r"(M_{\bullet\bullet}^{(1)}\otimes_A M_{\bullet\bullet}^{(2)})", r"(M_{\bullet\bullet\bullet}^{(1)}\otimes_A M_{\bullet\bullet\bullet}^{(2)})", "")
add(p, "(6.6.6.1): H_•(M^(1)_•••⊗_A L^(2)_••)", "three bullets on M", r"two bullets",
    "formula", None, "high", r"(M_{\bullet\bullet}^{(1)}\otimes_A L_{\bullet\bullet}^{(2)})", r"(M_{\bullet\bullet\bullet}^{(1)}\otimes_A L_{\bullet\bullet}^{(2)})", "")
add(p, "(6.6.6.1): H_•(L^(1)_••⊗_A M^(2)_•••)", "three bullets on M", r"two bullets",
    "formula", None, "high", r"(L_{\bullet\bullet}^{(1)}\otimes_A M_{\bullet\bullet}^{(2)})", r"(L_{\bullet\bullet}^{(1)}\otimes_A M_{\bullet\bullet\bullet}^{(2)})", "")
add(p, "(6.6.7, t)) display, left: (t)E(U^(1), U^(2); ...)", "roman E", r"\mathscr E", "font", None, "high",
    L(r"{}^{(t)}\mathscr E", r"  (\mathfrak U^{(1)}"), L(r"{}^{(t)}E", r"  (\mathfrak U^{(1)}"), E_NOTE)
add(p, "(6.6.7, t)) display, right: (t)E(V^(1), V^(2); ...)", "roman E", r"\mathscr E", "font", None, "high",
    L(r"{}^{(t)}\mathscr E", r"  (\mathfrak V^{(1)}"), L(r"{}^{(t)}E", r"  (\mathfrak V^{(1)}"), E_NOTE)
add(p, "(6.6.7), equation label", "(6.6.7, t))", r"\tag{6.6.7, $t$} gives (6.6.7, t)",
    "punctuation", None, "high", r"\tag{6.6.7, $t$}", r"\tag{6.6.7, $t$)}", T667)
add(p, "(6.6.7): 'des homomorphismes (6.6.7, t)) canoniquement définis'", "(6.6.7, t))", "(6.6.7, $t$)",
    "punctuation", None, "high", r"homomorphismes (6.6.7, $t$) canoniquement", r"homomorphismes (6.6.7, $t$)) canoniquement", T667)
add(p, "(6.6.7): 'dans les aboutissements (0, 11.3.2)'", "(𝟎, 11.3.2): bold 0, no subscript", r"($0_{\mathrm I}$, 11.3.2)",
    "extra", None, "high", r"($0_{\mathrm I}$, 11.3.2)", r"(\textbf{0}, 11.3.2)", "No subscript I in the print; the edit also sets the bold 0.")
add(p, "same reference (0, 11.3.2)", "bold 0", "plain 0", "convention", 2, "high", None, None, "Covered by the edit of the preceding finding.")
add(p, "(6.6.7): 'l'homomorphisme (6.6.7, t)) est un isomorphisme sur les termes E_2'", "(6.6.7, t))", "(6.6.7, $t$)",
    "punctuation", None, "high", r"l'homomorphisme (6.6.7, $t$)", r"l'homomorphisme (6.6.7, $t$))", T667)
add(p, "(6.6.7): 'on voit que (6.6.7, t)) est un isomorphisme pour ces trois'", "(6.6.7, t))", "(6.6.7, $t$)",
    "punctuation", None, "high", r"(6.6.7, $t$) est un isomorphisme pour", r"(6.6.7, $t$)) est un isomorphisme pour", T667)
add(p, "(6.6.7): 'des suites spectrales (a), (b), (a'), (b'), ... pour ces trois foncteurs spectraux'",
    "'ces trois foncteurs spectraux' after four spectral sequences (a), (b), (a'), (b')", "ces trois (as printed)",
    "misprint_in_print", None, "medium", None, None,
    "The TeX keeps the printed reading. Four sequences are listed and their E_2 terms were computed in (6.6.3)-(6.6.4); 'trois' is presumably a slip for 'quatre'.",
    corrected="ces quatre foncteurs spectraux")
add(p, "(6.6.7): 'pour leur aboutissement commun (0, 11.1.5)'", "(𝟎, 11.1.5): bold 0, no subscript", r"($0_{\mathrm I}$, 11.1.5)",
    "extra", None, "high", r"($0_{\mathrm I}$, 11.1.5)", r"(\textbf{0}, 11.1.5)", "No subscript I in the print; the edit also sets the bold 0.")
add(p, "same reference (0, 11.1.5)", "bold 0", "plain 0", "convention", 2, "high", None, None, "Covered by the edit of the preceding finding.")
add(p, "(6.6.7), display, left: Tor_•^S(U^(1), U^(2); F^(1), F^(2))", "roman Tor (not bold)", r"\mathbf{Tor}_\bullet^S",
    "font", None, "high",
    L(r"\mathbf{Tor}_\bullet^S", r"  (\mathfrak U^{(1)},\mathfrak U^{(2)};", r"   \mathscr F"),
    L(r"\operatorname{Tor}_\bullet^S", r"  (\mathfrak U^{(1)},\mathfrak U^{(2)};", r"   \mathscr F"), "Checked on a crop.")
add(p, "(6.6.7), display, right: Tor_•^S(V^(1), V^(2); F^(1), F^(2))", "roman Tor (not bold)", r"\mathbf{Tor}_\bullet^S",
    "font", None, "high", L(r"\mathbf{Tor}_\bullet^S", r"  (\mathfrak V^{(1)}"), L(r"\operatorname{Tor}_\bullet^S", r"  (\mathfrak V^{(1)}"), "Checked on a crop.")
add(p, "(6.6.7): 'on voit que (6.6.7, t)) est aussi un isomorphisme des termes E_2'", "(6.6.7, t))", "(6.6.7, $t$)",
    "punctuation", None, "high", L(r"(6.6.7, $t$) est aussi un", r"isomorphisme des"), L(r"(6.6.7, $t$)) est aussi un", r"isomorphisme des"), T667)
add(p, "(6.6.7), last sentence: 'que (6.6.7, t)) est aussi un isomorphisme de suites spectrales'", "(6.6.7, t))", "(6.6.7, $t$)",
    "punctuation", None, "high", r"(6.6.7, $t$) est aussi un isomorphisme de suites", r"(6.6.7, $t$)) est aussi un isomorphisme de suites", T667)

# ---------------- verification ----------------
texts = {}
for pg in (152, 153, 154, 155, 156):
    raw = open(RUN + r"\page_%d.tex" % pg, "rb").read().decode("utf-8")
    texts[pg] = raw.replace("\r\n", "\n")

ok = True
applied = dict(texts)
for i, f in enumerate(F):
    fx = f["fix"]
    if fx is None:
        continue
    t = texts[f["page"]]
    n = t.count(fx["old"])
    if n != 1:
        ok = False
        print("COUNT", n, "finding", i, f["page"], f["where"], repr(fx["old"])[:160])
    if fx["old"] == fx["new"]:
        ok = False
        print("SAME", i)
# sequential application check (overlaps)
for pg in texts:
    t = texts[pg]
    for i, f in enumerate(F):
        if f["page"] != pg or f["fix"] is None:
            continue
        o, nw = f["fix"]["old"], f["fix"]["new"]
        if t.count(o) != 1:
            ok = False
            print("SEQ-FAIL", i, pg, f["where"], repr(o)[:120])
        else:
            t = t.replace(o, nw)
    applied[pg] = t

if not ok:
    sys.exit(1)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
c = Counter()
for f in F:
    cat = "convention" if f["kind"] == "convention" else ("misprint" if f["kind"] == "misprint_in_print" else "normal")
    c[(f["page"], cat)] += 1
for pg in (152, 153, 154, 155, 156):
    print(pg, c[(pg, "normal")], c[(pg, "convention")], c[(pg, "misprint")])
print("total", len(F))
# dump applied pages for inspection
for pg, t in applied.items():
    open(RUN + r"\crops_152_156\applied_%d.tex" % pg, "w", encoding="utf-8", newline="\n").write(t)
