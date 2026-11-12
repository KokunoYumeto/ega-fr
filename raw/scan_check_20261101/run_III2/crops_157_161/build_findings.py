import json, pathlib, re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III2")
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega3\ega3-6-fr.tex")
OUT = RUN / "findings_157_161.json"
N = "\n"
BT = r"\boldsymbol{\mathscr{T}\!or}"   # proposed form for the print's bold script Tor (hypertor)
PT = r"\mathscr{T}\!or"                # plain script Tor (as used elsewhere in ega3-6)
F = []


def add(page, where, scan, tex, kind, old, new, conf="high", conv=None, note="", corrected=None):
    x = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=(dict(old=old, new=new) if old is not None else None))
    if kind == "misprint_in_print":
        x["corrected"] = corrected
    x["note"] = note
    F.append(x)


E_NOTE = ("The print sets the spectral functors of modules (X, U or the affine case) with a roman E, "
          "and keeps the script E for the sheaf versions (f_1, f_2; ...) on the same pages.")
BT_NOTE = ("The print has two script Tor: a bold one (heavier script T, bold italic 'or') for the hypertor of "
           "complexes, and the plain script T + italic 'or' for the Tor of Modules / termwise Tor (as bold Tor vs "
           "roman Tor for modules). \\mathfrak{Tor} prints Fraktur. Proposed form " + BT + "; one decision for "
           "the 55 \\mathfrak{Tor} of ega3-6 (see final message).")
RH_NOTE = ("Second, lighter roundhand script H (hypercohomology H^{-n}(f, P.)), unlike the usual script H of the "
           "same pages; same decision as GLOBAL_ISSUES item 42. ega3-6 uses \\mathscr for the usual script, so "
           "\\mathcal is proposed for the roundhand H.")
Z_NOTE = ("The print has a bold 0 without the subscript I (chapter 0, section 11 is in 0_III); "
          "the fix also sets the bold 0 (convention 2).")
PAIR = "Display set inline in the print; part {} of {}: apply together with the other part(s) of this formula."

# ---------------- page 157 ----------------
add(157, "first line, 'les isomorphismes (6.6.7, t))'", "(6.6.7, t))", "(6.6.7, $t$)", "misprint_in_print",
    "isomorphismes (6.6.7, $t$) définissent", "isomorphismes (6.6.7, $t$)) définissent",
    corrected="(6.6.7, $t$)",
    note="The print has a second, unbalanced closing parenthesis; the TeX silently corrects it.")
add(157, "display after 'Nous désignerons par', first member", "roman E: (t)E(X^(1), X^(2); P.^(1), P.^(2))",
    r"{}^{(t)}\mathscr E", "font", r"\[" + N + r"  {}^{(t)}\mathscr E" + N, r"\[" + N + r"  {}^{(t)}E" + N,
    note=E_NOTE)
add(157, "same display, second member", "roman E: (t)E^S(X^(1), X^(2); ...)", r"{}^{(t)}\mathscr E^S", "font",
    r"  {}^{(t)}\mathscr E^S" + N, r"  {}^{(t)}E^S" + N, note=E_NOTE)
add(157, "display after 'nous écrirons'", "Tor.^S(X^(1), X^(2); F^(1), F^(2)) with roman (not bold) Tor",
    r"\mathbf{Tor}", "font",
    r"  \mathbf{Tor}_\bullet^S" + N + r"  (X^{(1)},X^{(2)};\mathscr F^{(1)}",
    r"  \operatorname{Tor}_\bullet^S" + N + r"  (X^{(1)},X^{(2)};\mathscr F^{(1)}",
    note="Bold Tor only for the hypertor of the complexes ('par Tor.^S(X^(1), X^(2); P...)', '(Tor.^S(...))~'); "
         "the Tor of the Modules F^(i) and the Tor_q of the 'conventions générales' are roman.")
add(157, "'conformément aux conventions générales, Tor_q^S(X^(1), X^(2); P.^(1), P.^(2))'",
    "roman Tor_q^S", r"\mathbf{Tor}_q^S", "font",
    r"  \mathbf{Tor}_q^S" + N + r"  (X^{(1)},X^{(2)};\mathscr P_\bullet^{(1)}",
    r"  \operatorname{Tor}_q^S" + N + r"  (X^{(1)},X^{(2)};\mathscr P_\bullet^{(1)}",
    note="Roman Tor (termwise Tor of the 'conventions générales').")
add(157, "'sera donc le bicomplexe des Tor_q^S(X^(1), X^(2); P_h^(1), P_k^(2))'", "roman Tor_q^S",
    r"\mathbf{Tor}_q^S", "font",
    r"  \mathbf{Tor}_q^S" + N + r"  (X^{(1)},X^{(2)};\mathscr P_h^{(1)}",
    r"  \operatorname{Tor}_q^S" + N + r"  (X^{(1)},X^{(2)};\mathscr P_h^{(1)}",
    note="Roman Tor, as in the previous formula.")
add(157, "'et conformément aux conventions générales, Tor_q^S(...) sera donc le bicomplexe des Tor_q^S(...).'",
    "both formulas inline in the running text", "two displays", "other",
    "aux conventions générales," + N + r"\[", "aux conventions générales," + N + "$", note=PAIR.format(1, 3))
add(157, "same sentence", "inline", r"\] ... \[", "other",
    r"\]" + N + "sera donc le bicomplexe des" + N + r"\[", "$" + N + "sera donc le bicomplexe des" + N + "$",
    note=PAIR.format(2, 3))
add(157, "same sentence, end of (6.6.7)", "inline", r"\]", "other",
    r"\mathscr P_k^{(2)})." + N + r"\]" + N + r"\end{env}", r"\mathscr P_k^{(2)})$." + N + r"\end{env}",
    note=PAIR.format(3, 3))
add(157, "(6.6.8): 'est un S-schéma affine'", "S-schéma affine with 'schéma affine' italic",
    r"$S$-schéma \emph{affine}", "italics", r"$S$-schéma \emph{affine}", r"$S$-\emph{schéma affine}")
add(157, "(6.6.8): '(I, 2.2.4)'", "bold I", "(I, 2.2.4)", "convention", "(I, 2.2.4)", r"(\textbf{I}, 2.2.4)",
    conv=2)
add(157, "(6.6.8): 'suites spectrales de (B_1 (x)_A B_2)-modules. Si l'on pose'", "'modules' italic",
    "-modules", "italics", r"$(B_1\otimes_A B_2)$-modules. Si", r"$(B_1\otimes_A B_2)$-\emph{modules}. Si")
add(157, "(6.6.8): '(I, 1.3.4)'", "bold I", "(I, 1.3.4)", "convention", "(I, 1.3.4)", r"(\textbf{I}, 1.3.4)",
    conv=2)
add(157, "(6.6.8): 'les six suites spectrales ((t)E(X^(1), X^(2); ...))~ de O_Y-Modules'", "inline",
    "display", "other", "les six suites spectrales" + N + r"\[", "les six suites spectrales" + N + "$",
    note=PAIR.format(1, 2))
add(157, "same formula, end", "inline", r"\]", "other",
    r"\bigr)^{\sim}" + N + r"\]" + N + r"de $\mathscr O_Y$-Modules",
    r"\bigr)^{\sim}$" + N + r"de $\mathscr O_Y$-Modules", note=PAIR.format(2, 2))
add(157, "same formula", "roman E: ((t)E(X^(1), X^(2); ...))~", r"{}^{(t)}\mathscr E", "font",
    r"  \bigl({}^{(t)}\mathscr E" + N, r"  \bigl({}^{(t)}E" + N, note=E_NOTE)
add(157, "(6.6.8): 'Tor.^S(f_1, f_2; P.^(1), P.^(2)) leur aboutissement commun'", "bold script Tor",
    r"\mathfrak{Tor} (Fraktur)", "font",
    r"$\mathfrak{Tor}_\bullet^S" + N + r"(f_1,f_2;\mathscr P_\bullet^{(1)}",
    "$" + BT + r"_\bullet^S" + N + r"(f_1,f_2;\mathscr P_\bullet^{(1)}", conf="medium", note=BT_NOTE)
add(157, "(6.6.8): 'leur aboutissement commun (Tor.^S(...))~. On le'", "inline", "display", "other",
    "aboutissement commun" + N + r"\[", "aboutissement commun" + N + "$", note=PAIR.format(1, 2))
add(157, "same formula, end", "inline", r"\]", "other",
    r"\bigr)^{\sim}." + N + r"\]" + N + "On le notera", r"\bigr)^{\sim}$." + N + "On le notera",
    note=PAIR.format(2, 2))
add(157, "same formula: '(Tor.^S(X.^(1), X^(2); ...))~'", "X.^(1) (a dot under X^(1))", "X^{(1)}",
    "misprint_in_print",
    r"  \bigl(\mathbf{Tor}_\bullet^S" + N + r"  (X^{(1)},",
    r"  \bigl(\mathbf{Tor}_\bullet^S" + N + r"  (X_\bullet^{(1)},",
    corrected=r"\bigl(\mathbf{Tor}_\bullet^S(X^{(1)},X^{(2)};\mathscr P_\bullet^{(1)},\mathscr P_\bullet^{(2)})\bigr)^{\sim}",
    note="The print puts the dot of the complexes under X^(1), a prescheme; the TeX silently corrects it.")
add(157, "'On le notera Tor.^S(f_1, f_2; F^(1), F^(2))'", "plain script T + italic 'or'",
    r"\mathfrak{Tor} (Fraktur)", "font",
    r"$\mathfrak{Tor}_\bullet^S(f_1,f_2;\mathscr F^{(1)}", "$" + PT + r"_\bullet^S(f_1,f_2;\mathscr F^{(1)}",
    note="Plain script Tor (Tor of Modules), the form ega3-6 writes " + PT + ".")
add(157, "(6.7.1): 'des morphismes séparés et quasi-compacts'", "'séparés' and 'quasi-compacts' italic, 'et' roman",
    r"\emph{séparés et quasi-compacts}", "italics", r"\emph{séparés et quasi-compacts}",
    r"\emph{séparés} et \emph{quasi-compacts}")
add(157, "(6.7.1): 'limités inférieurement, (i = 1, 2), de définir'", "comma after 'inférieurement'",
    "no comma", "punctuation", "limités inférieurement" + N + "($i=1,2$)", "limités inférieurement," + N + "($i=1,2$)")
add(157, "(6.7.1): 'un O_Y-Module quasi-cohérent Tor_n^S(f_1, f_2; P.^(1), P.^(2))'", "bold script Tor",
    r"\mathfrak{Tor} (Fraktur)", "font", r"$\mathfrak{Tor}_n^S" + N + "(f_1,f_2;", "$" + BT + r"_n^S" + N + "(f_1,f_2;",
    conf="medium", note=BT_NOTE)
add(157, "(6.7.1): 'Supposons d'abord S = Spec(A) affine'", "same paragraph (line not indented)",
    "new paragraph (blank line)", "other",
    r"$Y=Y^{(1)}\times_S Y^{(2)}$)." + N + N + "Supposons", r"$Y=Y^{(1)}\times_S Y^{(2)}$)." + N + "Supposons",
    conf="medium", note="The print runs on: 'Supposons d'abord' starts at the left margin, unindented.")
add(157, "(6.7.1): 'conditions de recollement (0_I, 3.3.1)'", "bold 0 with subscript I", r"$0_{\mathrm I}$",
    "convention", r"($0_{\mathrm I}$, 3.3.1)", r"($\mathbf{0}_{\mathrm I}$, 3.3.1)", conv=2)

# ---------------- page 158 ----------------
add(158, "first line, '(II, 4.3.2.1)'", "bold II", "(II, 4.3.2.1)", "convention", "(II, 4.3.2.1)",
    r"(\textbf{II}, 4.3.2.1)", conv=2)
add(158, "(6.7.1.1), first member", "roman E", r"{}^{(t)}\mathscr E", "font",
    r"  {}^{(t)}\mathscr E" + N + r"  (X'^{(1)}", r"  {}^{(t)}E" + N + r"  (X'^{(1)}", note=E_NOTE)
add(158, "(6.7.1.1), second member", "roman E", r"{}^{(t)}\mathscr E", "font",
    r"\xrightarrow{\sim}" + N + r"  {}^{(t)}\mathscr E" + N, r"\xrightarrow{\sim}" + N + r"  {}^{(t)}E" + N,
    note=E_NOTE)
add(158, "'formé d'ouverts affines (I, 5.5.10)'", "bold I", "(I, 5.5.10)", "convention", "(I, 5.5.10)",
    r"(\textbf{I}, 5.5.10)", conv=2)
add(158, "'on a donc L'..^(1) (x)_A L'..^(2) = (...) (x)_A (...);'", "inline", "display", "other",
    "on a donc" + N + r"\[", "on a donc" + N + "$", note=PAIR.format(1, 2))
add(158, "same formula, end", "inline", r"\]", "other",
    r"\bigr);" + N + r"\]" + N + "comme on a", r"\bigr)$;" + N + "comme on a", note=PAIR.format(2, 2))
add(158, "'à un isomorphisme canonique près, L'..^(1) (x)_A L'..^(2) = (L..^(1) (x)_A L..^(2)) (x)_B B_g.'",
    "inline", "display", "other",
    "à un isomorphisme canonique près," + N + r"\[", "à un isomorphisme canonique près," + N + "$",
    note=PAIR.format(1, 2))
add(158, "same formula, end", "inline", r"\]", "other",
    r"\otimes_B B_g." + N + r"\]" + N + "Si $M", r"\otimes_B B_g$." + N + "Si $M", note=PAIR.format(2, 2))
add(158, "(6.7.2): 'qui est un morphisme séparé et quasi-compact'", "roman", r"\emph{séparé et quasi-compact}",
    "italics", r"\emph{séparé et quasi-compact}", "séparé et quasi-compact")
add(158, "(6.7.2): 'On se ramène aussitôt à la situation suivante'", "same paragraph (line not indented)",
    "new paragraph (blank line)", "other", "recollement." + N + N + "On se ramène",
    "recollement." + N + "On se ramène", conf="medium",
    note="The print runs on after 'recollement.': 'On se ramène' starts at the left margin, unindented.")
add(158, "(6.7.2.1), first member", "roman E", r"{}^{(t)}\mathscr E^S", "font",
    r"  {}^{(t)}\mathscr E^S" + N, r"  {}^{(t)}E^S" + N, note=E_NOTE)
add(158, "(6.7.2.1), second member", "roman E", r"{}^{(t)}\mathscr E^{S'}", "font",
    r"{}^{(t)}\mathscr E^{S'}", r"{}^{(t)}E^{S'}", note=E_NOTE)
add(158, "'Or, avec les notations de (6.6.2)'", "new paragraph (indented)", "no paragraph break", "other",
    r"\]" + N + "Or, avec les notations", r"\]" + N + N + "Or, avec les notations", conf="medium",
    note="The print indents 'Or, avec' (new paragraph after the display (6.7.2.1)).")
add(158, "Théorème (6.7.3): 'Il existe un bi-d-foncteur Tor.^S(f_1, f_2; P.^(1), P.^(2))'",
    "bold script Tor", r"\mathfrak{Tor} (Fraktur)", "font",
    r"$\mathfrak{Tor}_\bullet^S" + N + "(f_1,f_2;", "$" + BT + r"_\bullet^S" + N + "(f_1,f_2;",
    conf="medium", note=BT_NOTE)
add(158, "Théorème (6.7.3), display 'Tor.^S(f_1, f_2; ...)|V = (Tor.^S(...))~' (printed on p. 159; it lies in "
         "the p. 158 segment because the 159 marker is misplaced)", "bold script Tor",
    r"\mathfrak{Tor} (Fraktur)", "font",
    r"\mathfrak{Tor}_\bullet^S" + N + "  (f_1,f_2;", BT + r"_\bullet^S" + N + "  (f_1,f_2;",
    conf="medium", note=BT_NOTE)

# ---------------- page 159 (all before the marker move) ----------------
add(159, "E_2 display, row (a), first H", "roundhand script H", r"\mathscr H^{-q_1}", "font",
    PT + r"_p^S" + N + r"    \bigl(\mathscr H^{-q_1}", PT + r"_p^S" + N + r"    \bigl(\mathcal H^{-q_1}",
    conf="medium", note=RH_NOTE + " Row (a') has the usual script H.")
add(159, "E_2 display, row (a), second H", "roundhand script H", r"\mathscr H^{-q_2}", "font",
    r"\mathscr H^{-q_2}(f_2,\mathscr P_\bullet^{(2)})\bigr),\\" + N + r"  {}^{(b)}",
    r"\mathcal H^{-q_2}(f_2,\mathscr P_\bullet^{(2)})\bigr),\\" + N + r"  {}^{(b)}", conf="medium", note=RH_NOTE)
add(159, "E_2 display, row (b): 'H^{-p}(f_1 x_S f_2, Tor_q^S(P.^(1), P.^(2)))'", "bold script Tor",
    r"\mathfrak{Tor} (Fraktur)", "font",
    r"\mathfrak{Tor}_q^S" + N + r"    (\mathscr P_\bullet^{(1)}", BT + r"_q^S" + N + r"    (\mathscr P_\bullet^{(1)}",
    conf="medium", note=BT_NOTE + " Row (b') has the plain Tor.")
add(159, "E_2 display, row (a')", "bold script Tor", r"\mathfrak{Tor} (Fraktur)", "font",
    r"\mathfrak{Tor}_p^S" + N + r"    \bigl(\mathscr H^{-q_1}", BT + r"_p^S" + N + r"    \bigl(\mathscr H^{-q_1}",
    conf="medium", note=BT_NOTE + " Row (a) has the plain Tor.")
add(159, "E_2 display, row (b'): 'H^{-p}(f_1 x_S f_2, ...)'", "roundhand script H", r"\mathscr H^{-p}", "font",
    r"\mathscr H^{-p}\bigl(f_1\times_S f_2," + N + "    " + PT + "_q^S",
    r"\mathcal H^{-p}\bigl(f_1\times_S f_2," + N + "    " + PT + "_q^S", conf="medium",
    note=RH_NOTE + " Row (b) has the usual script H.")
add(159, "E_2 display, row (c): 'Tor_p^S(f_1, f_2; H_{q_1}(P.^(1)), H_{q_2}(P.^(2)))'",
    "plain script T + italic 'or'", r"\mathfrak{Tor} (Fraktur)", "font",
    r"\mathfrak{Tor}_p^S" + N + r"    \bigl(f_1,f_2;", PT + r"_p^S" + N + r"    \bigl(f_1,f_2;",
    note="Plain script Tor (the TeX's \\mathfrak{Tor} stands for the bold one elsewhere).")
add(159, "E_2 display, row (d): 'H_p(Tor_q^S(f_1, f_2; P.^(1), P.^(2)))'", "plain script T + italic 'or'",
    r"\mathfrak{Tor} (Fraktur)", "font", r"\mathscr H_p\bigl(\mathfrak{Tor}_q^S", r"\mathscr H_p\bigl(" + PT + "_q^S",
    note="Plain script Tor.")
add(159, "after the E_2 display: 'On dit que ... suites spectrales de Künneth.' and 'On notera que ... sans intérêt.'",
    "roman text (only 'suites spectrales de Künneth' italic): the statement ends with the E_2 display",
    r"both paragraphs inside \begin{theorem}...\end{theorem} (italic, with \emph upright)", "italics",
    r"\]" + N + r"On dit que les suites spectrales $(a)$ et $(b)$ sont les \emph{suites" + N
    + r"spectrales de Künneth}." + N + N
    + r"On notera que les suites spectrales $(a)$ et $(a')$ (resp. $(b)$ et $(b')$)" + N
    + r"sont identiques lorsque $\mathscr P_\bullet^{(1)}$ et" + N
    + r"$\mathscr P_\bullet^{(2)}$ se réduisent à leurs termes de degré 0; dans ce cas," + N
    + r"les suites $(c)$ et $(d)$ sont dégénérées et sont donc sans intérêt." + N + r"\end{theorem}",
    r"\]" + N + r"\end{theorem}" + N + r"\noindent On dit que les suites spectrales $(a)$ et $(b)$ sont les \emph{suites" + N
    + r"spectrales de Künneth}." + N + N
    + r"On notera que les suites spectrales $(a)$ et $(a')$ (resp. $(b)$ et $(b')$)" + N
    + r"sont identiques lorsque $\mathscr P_\bullet^{(1)}$ et" + N
    + r"$\mathscr P_\bullet^{(2)}$ se réduisent à leurs termes de degré 0; dans ce cas," + N
    + r"les suites $(c)$ et $(d)$ sont dégénérées et sont donc sans intérêt.",
    note="\\end{theorem} moved up to the end of the E_2 display (one edit). 'On dit que' is not indented in the print.")
add(159, "Remarque (6.7.4): 'f : X -> Y quasi-compact et séparé'", "'quasi-compact' and 'séparé' italic, 'et' roman",
    r"\emph{quasi-compact et séparé}", "italics", r"\emph{quasi-compact et séparé}",
    r"\emph{quasi-compact} et \emph{séparé}", note="Judged with the remark body roman, as printed.")
add(159, "(6.7.4.1), first member", "bold script Tor", r"\mathfrak{Tor} (Fraktur)", "font",
    r"\mathfrak{Tor}_n^Y", BT + r"_n^Y", conf="medium", note=BT_NOTE)
add(159, "(6.7.4.1), second member 'H^{-n}(f, P.)'", "roundhand script H", r"\mathscr H^{-n}", "font",
    r"\mathscr H^{-n}(f,\mathscr P_\bullet)" + N, r"\mathcal H^{-n}(f,\mathscr P_\bullet)" + N, conf="medium",
    note=RH_NOTE)
add(159, "'En effet, les méthodes de recollement de (6.7.2)'", "new paragraph (indented)", "no paragraph break",
    "other", r"\]" + N + "En effet, les méthodes", r"\]" + N + N + "En effet, les méthodes", conf="medium",
    note="The print indents 'En effet' after (6.7.4.1).")
add(159, "'à l'aide d'un même recouvrement fini U de Y par des ouverts affines'", "de Y", "de $X$",
    "misprint_in_print", r"recouvrement fini $\mathfrak U$ de $X$", r"recouvrement fini $\mathfrak U$ de $Y$",
    corrected=r"recouvrement fini $\mathfrak U$ de $X$",
    note="Both members are computed with a finite affine covering of X (the covering of Y is 'formé de Y "
         "lui-même'); the print's Y is a misprint, silently corrected in the TeX.")
add(159, "'la conclusion résulte de (0, 11.7.5)'", "(0, 11.7.5): bold 0, no subscript", r"($0_{\mathrm I}$, 11.7.5)",
    "extra", r"($0_{\mathrm I}$, 11.7.5)", r"(\textbf{0}, 11.7.5)", note=Z_NOTE)
add(159, "'un isomorphisme avec H^{-n}(f, P. (x)_{O_Y} F)'", "roundhand script H", r"\mathscr H^{-n}", "font",
    r"$\mathscr H^{-n}(f,\mathscr P_\bullet\otimes", r"$\mathcal H^{-n}(f,\mathscr P_\bullet\otimes", conf="medium",
    note=RH_NOTE)
add(159, "(6.7.4.2), first member", "bold script Tor", r"\mathfrak{Tor} (Fraktur)", "font",
    r"\mathfrak{Tor}_\bullet^S" + N + r"  (1_{X^{(1)}}", BT + r"_\bullet^S" + N + r"  (1_{X^{(1)}}", conf="medium",
    note=BT_NOTE)
add(159, "(6.7.4.2), second member 'Tor.^S(P.^(1), P.^(2))'", "bold script Tor (same glyph as the first member)",
    PT + " (plain)", "font", PT + r"_\bullet^S", BT + r"_\bullet^S", conf="medium",
    note="The local hypertor is printed with the bold script Tor. " + BT_NOTE)
add(159, "'En effet, on se ramène encore, par (6.7.1) et (6.7.2)'", "new paragraph (indented)",
    "no paragraph break", "other", r"\]" + N + "En effet, on se ramène", r"\]" + N + N + "En effet, on se ramène",
    conf="medium", note="The print indents 'En effet' after (6.7.4.2).")

# ---------------- page 160 ----------------
add(160, "proof of (6.7.5): 'par hypothèse (0, 11.1.5)'", "(0, 11.1.5): bold 0, no subscript",
    r"($0_{\mathrm I}$, 11.1.5)", "extra", r"hypothèse ($0_{\mathrm I}$, 11.1.5)", r"hypothèse (\textbf{0}, 11.1.5)",
    note=Z_NOTE)
add(160, "'Ceci montre déjà que Tor.^S(f_1, f_2; P...) -> Tor.^S(f_1, f_2; Q...) est un isomorphisme'", "inline",
    "display", "other", "Ceci montre déjà que" + N + r"\[", "Ceci montre déjà que" + N + "$", note=PAIR.format(1, 2))
add(160, "same formula, end", "inline", r"\]", "other", r"\]" + N + "est un isomorphisme. Appliquant",
    "$" + N + "est un isomorphisme. Appliquant", note=PAIR.format(2, 2))
add(160, "same formula, first Tor", "bold script Tor", r"\mathfrak{Tor} (Fraktur)", "font",
    r"\mathfrak{Tor}_\bullet^S" + N + r"  (f_1,f_2;\mathscr P", BT + r"_\bullet^S" + N + r"  (f_1,f_2;\mathscr P",
    conf="medium", note=BT_NOTE)
add(160, "same formula, second Tor", "bold script Tor", r"\mathfrak{Tor} (Fraktur)", "font",
    r"\mathfrak{Tor}_\bullet^S" + N + r"  (f_1,f_2;\mathscr Q", BT + r"_\bullet^S" + N + r"  (f_1,f_2;\mathscr Q",
    conf="medium", note=BT_NOTE)
add(160, "'les homomorphismes H^{-n}(f_1, P.^(1)) -> H^{-n}(f_1, Q.^(1)) et Tor_n^S(...) -> Tor_n^S(...) déduits de u'",
    "inline, 'et' in the running text", "display", "other",
    "d'abord que les homomorphismes" + N + r"\[", "d'abord que les homomorphismes" + N + "$", note=PAIR.format(1, 3))
add(160, "same sentence, 'et'", "inline", r"\quad\text{et}\quad", "other",
    r"  \quad\text{et}\quad" + N, "  $ et $" + N, note=PAIR.format(2, 3))
add(160, "same sentence, end", "inline", r"\]", "other",
    r"\]" + N + "déduits de $u$ sont des isomorphismes. L'assertion",
    "$" + N + "déduits de $u$ sont des isomorphismes. L'assertion", note=PAIR.format(3, 3))
add(160, "same sentence, 'H^{-n}(f_1, P.^(1))'", "roundhand script H", r"\mathscr H^{-n}", "font",
    r"\mathscr H^{-n}(f_1,\mathscr P_\bullet^{(1)})", r"\mathcal H^{-n}(f_1,\mathscr P_\bullet^{(1)})",
    conf="medium", note=RH_NOTE)
add(160, "same sentence, 'H^{-n}(f_1, Q.^(1))'", "roundhand script H", r"\mathscr H^{-n}", "font",
    r"\mathscr H^{-n}(f_1,\mathscr Q_\bullet^{(1)})", r"\mathcal H^{-n}(f_1,\mathscr Q_\bullet^{(1)})",
    conf="medium", note=RH_NOTE)
add(160, "same sentence, 'Tor_n^S(P.^(1), P.^(2))'", "bold script Tor", PT + " (plain)", "font",
    PT + r"_n^S" + N + r"  (\mathscr P", BT + r"_n^S" + N + r"  (\mathscr P", conf="medium",
    note="Local hypertor, printed with the bold script Tor. " + BT_NOTE)
add(160, "same sentence, 'Tor_n^S(Q.^(1), P.^(2))'", "bold script Tor", PT + " (plain)", "font",
    PT + r"_n^S" + N + r"  (\mathscr Q", BT + r"_n^S" + N + r"  (\mathscr Q", conf="medium",
    note="As the previous one. " + BT_NOTE)
add(160, "'bijectifs pour les termes E_2 (0, 11.1.5)'", "(0, 11.1.5): bold 0, no subscript",
    r"($0_{\mathrm I}$, 11.1.5)", "extra", r"$E_2$" + N + r"($0_{\mathrm I}$, 11.1.5)",
    r"$E_2$" + N + r"(\textbf{0}, 11.1.5)", note=Z_NOTE)
add(160, "'on en déduit des isomorphismes canoniques (t)E(f_1, f_2; P...) -> (t)E(f_1, f_2; Q...) pour les six'",
    "inline", "display", "other", "on en déduit des isomorphismes canoniques" + N + r"\[",
    "on en déduit des isomorphismes canoniques" + N + "$", note=PAIR.format(1, 2))
add(160, "same formula, end", "inline", r"\]", "other", r"\]" + N + "pour les six suites spectrales.",
    "$" + N + "pour les six suites spectrales.", note=PAIR.format(2, 2))
add(160, "'un homotopisme de bicomplexes C.(U^(1), P.^(1)) -> C.(U^(1), Q.^(1)), et la proposition'", "inline",
    "display", "other", "un homotopisme de bicomplexes" + N + r"\[", "un homotopisme de bicomplexes" + N + "$",
    note=PAIR.format(1, 2))
add(160, "same formula, end", "inline", r"\]", "other",
    r"\mathscr Q_\bullet^{(1)})," + N + r"\]" + N + "et la proposition",
    r"\mathscr Q_\bullet^{(1)})$," + N + "et la proposition", note=PAIR.format(2, 2))
add(160, "'de l'hyperhomologie (0, 11.3.2)'", "(0, 11.3.2): bold 0, no subscript", r"($0_{\mathrm I}$, 11.3.2)",
    "extra", r"($0_{\mathrm I}$, 11.3.2)", r"(\textbf{0}, 11.3.2)", note=Z_NOTE)
add(160, "(6.7.6.1), first member", "bold script Tor", r"\mathfrak{Tor} (Fraktur)", "font",
    r"\mathfrak{Tor}_n^S", BT + r"_n^S", conf="medium", note=BT_NOTE)
add(160, "(6.7.6.1), second member 'H^{-n}(f_1 x_S f_2, P.^(1) (x)_S P.^(2))'", "roundhand script H",
    r"\mathscr H^{-n}", "font", r"\mathscr H^{-n}\bigl(f_1\times_S f_2,", r"\mathcal H^{-n}\bigl(f_1\times_S f_2,",
    conf="medium", note=RH_NOTE)
add(160, "proof of (6.7.6): 'au sens de (0, 11.7.1)'", "(0, 11.7.1): bold 0, no subscript",
    r"($0_{\mathrm I}$, 11.7.1)", "extra", r"($0_{\mathrm I}$, 11.7.1)", r"(\textbf{0}, 11.7.1)", note=Z_NOTE)
add(160, "'en vertu de l'hypothèse (1.4.15.1)'", "(1.4.15.1): plain 1, period", "(I, 4.15.1)", "number",
    "l'hypothèse (I, 4.15.1)", "l'hypothèse (1.4.15.1)",
    note="The print reads (1.4.15.1): no bold chapter numeral and a period, not a comma, after the first 1.")
add(160, "'on déduit alors de (0, 11.7.5)'", "(0, 11.7.5): bold 0, no subscript", r"($0_{\mathrm I}$, 11.7.5)",
    "extra", r"($0_{\mathrm I}$, 11.7.5)", r"(\textbf{0}, 11.7.5)", note=Z_NOTE)
add(160, "'On a d'autre part un homomorphisme naturel de bicomplexes'", "new paragraph (indented)",
    "no paragraph break", "other", r"\]" + N + "On a d'autre part", r"\]" + N + N + "On a d'autre part",
    conf="medium", note="The print indents 'On a d'autre part' after (6.7.6.2).")

# ---------------- page 161 ----------------
for ref, ctx in (("11.8.5", "'C.(Phi^(1), Phi^(2); S_k) (0, 11.8.5)'"), ("11.8.6", "'P.(Phi^(1), Phi^(2); S_k) (0, 11.8.6)'"),
                 ("11.8.7", "'cochaînes alternées (0, 11.8.7)'")):
    add(161, ctx, "(0, " + ref + "): bold 0, no subscript", r"($0_{\mathrm I}$, " + ref + ")", "extra",
        r"($0_{\mathrm I}$, " + ref + ")", r"(\textbf{0}, " + ref + ")", note=Z_NOTE)
add(161, "'Il faut ensuite prouver que l'isomorphisme ainsi défini'", "new paragraph (indented)",
    "no paragraph break", "other", r"\]" + N + "Il faut ensuite", r"\]" + N + N + "Il faut ensuite", conf="medium",
    note="The print indents 'Il faut ensuite' after (6.7.6.3).")
add(161, "Proposition (6.7.7): 'H^{-n}(f_1, P.^(1)) ou tous les Modules'", "'ou' roman in the italic statement",
    "ou (italic)", "convention", r"$ ou tous les Modules", r"$ \textup{ou} tous les Modules", conv=6)
add(161, "Proposition (6.7.7): 'tous les Modules H^{-n}(f_1, P.^(1))'", "roundhand script H", r"\mathscr H^{-n}",
    "font", r"\mathscr H^{-n}(f_1,", r"\mathcal H^{-n}(f_1,", conf="medium", note=RH_NOTE)
add(161, "Proposition (6.7.7): 'tous les Modules H^{-n}(f_2, P.^(2))'", "roundhand script H", r"\mathscr H^{-n}",
    "font", r"\mathscr H^{-n}(f_2,", r"\mathcal H^{-n}(f_2,", conf="medium", note=RH_NOTE)
add(161, "(6.7.7.1), first member", "bold script Tor", r"\mathfrak{Tor} (Fraktur)", "font",
    r"\mathfrak{Tor}_n^S", BT + r"_n^S", conf="medium", note=BT_NOTE)
add(161, "(6.7.7.1), 'H^{-q_1}(f_1, P.^(1))'", "roundhand script H", r"\mathscr H^{-q_1}", "font",
    r"\mathscr H^{-q_1}(f_1,", r"\mathcal H^{-q_1}(f_1,", conf="medium", note=RH_NOTE)
add(161, "(6.7.7.1), 'H^{-q_2}(f_2, P.^(2))'", "roundhand script H", r"\mathscr H^{-q_2}", "font",
    r"\mathscr H^{-q_2}(f_2,", r"\mathcal H^{-q_2}(f_2,", conf="medium", note=RH_NOTE)
add(161, "proof of (6.7.7): 'résulte aussitôt de (0, 11.1.6)'", "(0, 11.1.6): bold 0, no subscript",
    r"($0_{\mathrm I}$, 11.1.6)", "extra", r"($0_{\mathrm I}$, 11.1.6)", r"(\textbf{0}, 11.1.6)", note=Z_NOTE)
add(161, "Théorème (6.7.8), 2°: 'le complexe P.^(1) ou le complexe P.^(2)'", "'ou' roman in the italic statement",
    "ou (italic)", "convention", r"$\mathscr P_\bullet^{(1)}$ ou le complexe",
    r"$\mathscr P_\bullet^{(1)}$ \textup{ou} le complexe", conv=6)

# ---------------- marker move: delete first, then insert (order matters for apply_fixes.py) ----------------
add(159, "\\oldpage[III]{159} before 'Ce bifoncteur'", "printed p. 159 begins at 'à valeurs dans la catégorie' "
    "(Théorème (6.7.3)); 'Ce bifoncteur' starts an indented paragraph", "marker before 'Ce bifoncteur', no "
    "paragraph break", "marker", r"\oldpage[III]{159}" + N + "Ce bifoncteur", N + "Ce bifoncteur",
    note="Part 1 of the marker move: apply after all other p. 158-159 fixes and before part 2 (p. 158). "
         "The blank line restores the printed paragraph break before 'Ce bifoncteur'.")
add(158, "Théorème (6.7.3): '... bi-d-foncteur Tor.^S(f_1, f_2; P.^(1), P.^(2)) | à valeurs dans'",
    "printed p. 158 ends after 'Tor.^S(f_1, f_2; P.^(1), P.^(2))'", "marker after the display ending '...)~.'",
    "marker", r"\mathscr P_\bullet^{(2)})$" + N + "à valeurs", r"\mathscr P_\bullet^{(2)})$" + N + r"\oldpage[III]{159}" + N + "à valeurs",
    note="Part 2 of the marker move: apply after part 1 (p. 159).")

# ---------------- checks ----------------
pages = {p: (RUN / f"page_{p}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for p in range(157, 162)}
bad = 0
for i, x in enumerate(F):
    o = x["fix"]["old"]
    c = pages[x["page"]].count(o)
    if c != 1:
        bad += 1
        print("NOT UNIQUE in page file:", i, x["page"], c, repr(o[:80]))
print("uniqueness problems:", bad)

# replay as apply_fixes.py does (page segment = marker to next marker), in list order, on a copy of ega3-6
t = REL.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[III\]\{(\d+)\}")


def locate(text, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(text)]
    for k, (n, s) in enumerate(cuts):
        if n == page:
            return s, cuts[k + 1][1] if k + 1 < len(cuts) else len(text)
    return None, None


fails = 0
for i, x in enumerate(F):
    s, e = locate(t, x["page"])
    seg = t[s:e]
    o, nw = x["fix"]["old"], x["fix"]["new"]
    if seg.count(o) != 1:
        fails += 1
        print("REPLAY FAIL:", i, x["page"], seg.count(o), repr(o[:80]))
        continue
    t = t[:s] + seg.replace(o, nw) + t[e:]
print("replay failures:", fails)

# sanity of the result for pp. 157-161
s, _ = locate(t, 157)
_, e = locate(t, 161)
seg = t[s:e]
print("markers 157-161 now:", [m.group(1) for m in marker.finditer(seg)] + ["161"])
print("dollars even:", seg.replace("\\$", "").count("$") % 2 == 0, " \\[ vs \\]:", seg.count("\\["), seg.count("\\]"))
print("theorem begin/end:", seg.count("\\begin{theorem}"), seg.count("\\end{theorem}"))
(RUN / "crops_157_161" / "replayed_157_161.tex").write_text(seg, encoding="utf-8", newline="")

json.dump(F, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for p in range(157, 162):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("total findings:", len(F))
