import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")

RUN = r"user\Documents\ega_scan_check_20261101\run_III2"
OUT = os.path.join(RUN, "findings_162_166.json")
NL = "\n"

def F(page, where, scan, tex, kind, conf, old, new, note, convention=None, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": convention, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d

items = []

# ---------------- page 162 ----------------
items += [
F(162, "Théorème (6.7.8), first line: 'ou tous les Modules'",
  "'ou' printed roman (upright) inside the italic statement",
  "'ou' in the italic theorem environment",
  "convention", "high",
  r"$ ou tous les Modules", r"$ \textup{ou} tous les Modules",
  "Emphasis by roman type inside the italic statement.", convention=6),
F(162, "(6.7.8.1), end of the display",
  "no full stop after the formula; the next line is '(« formule de Künneth »).'",
  "full stop after \\mathscr H^{n_2}(f_2,\\mathscr P_\\bullet^{(2)})",
  "punctuation", "high",
  r"\mathscr H^{n_2}(f_2,\mathscr P_\bullet^{(2)}).", r"\mathscr H^{n_2}(f_2,\mathscr P_\bullet^{(2)})",
  "Extra full stop in the TeX."),
F(162, "Proposition (6.7.9), end of condition 1°",
  "'... de type fini sur S.' (full stop; in the print each condition 1°, 2°, 3° is its own paragraph)",
  "'de type fini sur $S$;'",
  "punctuation", "high",
  r"fini sur $S$; $2^\circ$", r"fini sur $S$. $2^\circ$",
  "Paragraph layout of the conditions is left as is."),
F(162, "Proposition (6.7.9), end of 2° and start of 3°",
  "'... limités inférieurement. 3° Pour tout n∈Z,'",
  "'inférieurement; $3^\\circ$ pour tout'",
  "punctuation", "high",
  r"inférieurement; $3^\circ$ pour tout", r"inférieurement. $3^\circ$ Pour tout",
  "Full stop after 2° and capital P in 'Pour' in the print."),
F(162, "proof of (6.7.9): 'les hypertor locaux Tor_n^S(P^(1), P^(2))'",
  "the curly 'Tor' glyph (the same glyph as the global hypertor in the statement of (6.7.9), which the TeX writes \\mathfrak{Tor})",
  "\\mathscr{T}\\!or_n^S (the TeX's form for the print's other, thin script 'Tor', e.g. the outer Tor_p in (6.8.2) and (a) in (6.7.3) p. 159)",
  "font", "medium",
  r"\mathscr{T}\!or_n^S", r"\mathfrak{Tor}_n^S",
  "Glyph-to-macro mismatch; part of a document-wide pattern (p. 150 'Il est clair que Tor_.^S(P_., Q_.)' prints the curly glyph and has \\mathscr{T}\\!or; p. 159 (b) prints the same local hypertor and has \\mathfrak). Needs one decision; apply this fix only with it."),
F(162, "proof of (6.7.9): '(I, 6.3.4 et 6.3.8)'",
  "bold I", "plain I", "convention", "high",
  r"(I, 6.3.4", r"(\textbf{I}, 6.3.4", "", convention=2),
F(162, "proof of (6.7.9): '(II, 5.4.2)'",
  "bold II", "plain II", "convention", "high",
  r"(II, 5.4.2)", r"(\textbf{II}, 5.4.2)", "", convention=2),
F(162, "proof of (6.7.9), last line: 'on conclut par (0, 11.1.8)'",
  "(0, 11.1.8) with a bold 0 and no subscript",
  "($0_{\\mathrm I}$, 11.1.8)",
  "number", "high",
  r"($0_{\mathrm I}$, 11.1.8)", r"(\textbf{0}, 11.1.8)",
  "The TeX adds the subscript I (11.1.8 is in chapter 0 of EGA III, not 0_I). The fix also applies convention 2 (bold 0)."),
F(162, "(6.7.10): 'v : v_1 x_S v_2 leur produit'",
  "v : v_1×_S v_2 (colon)",
  "$v=v_1\\times_S v_2$",
  "misprint_in_print", "high",
  r"$v=v_1\times_S v_2$", r"$v:v_1\times_S v_2$",
  "The print has a colon for '='; the TeX silently corrects it.",
  corrected=r"$v=v_1\times_S v_2$"),
F(162, "(6.7.10): 'f'_i : X'^(i) -> Y'^(i), de sorte que les diagrammes'",
  "comma after Y'^(i)",
  "no comma",
  "punctuation", "high",
  r"Y'^{(i)}$ de sorte que", r"Y'^{(i)}$, de sorte que",
  "Missing comma in the TeX."),
F(162, "(6.7.10): 'étant séparés et quasi-compacts'",
  "'séparés' and 'quasi-compacts' italic, 'et' roman",
  "\\emph{séparés et quasi-compacts} (et italic too)",
  "italics", "high",
  "\\emph{séparés et" + NL + "quasi-compacts}", "\\emph{séparés} et" + NL + "\\emph{quasi-compacts}",
  ""),
F(162, "(6.7.10): 'nous considérerons comme dans (6.6.1)'",
  "considérerons (future)",
  "considérons",
  "word", "high",
  r"considérons comme dans", r"considérerons comme dans",
  ""),
F(162, "(6.7.10), last line: 'nous considérerons des recouvrements finis U'^(i)'",
  "considérerons (future)",
  "considérons",
  "word", "high",
  r"nous considérons des recouvrements", r"nous considérerons des recouvrements",
  ""),
]

# ---------------- page 163 ----------------
items += [
F(163, "'on définit un homomorphisme de bicomplexes C(u_i^-1(U), u_i^*(P)) -> C(U', u_i^*(P)) d'où, par composition'",
  "formula set inline in the running text",
  "displayed with \\[ ... \\]",
  "other", "high",
  "\\[" + NL + r"  C^\bullet(u_i^{-1}(\mathfrak U^{(i)}),u_i^*(\mathscr P_\bullet^{(i)}))" + NL
  + r"  \longrightarrow" + NL + r"  C^\bullet(\mathfrak U'^{(i)},u_i^*(\mathscr P_\bullet^{(i)}))" + NL + "\\]",
  r"$C^\bullet(u_i^{-1}(\mathfrak U^{(i)}),u_i^*(\mathscr P_\bullet^{(i)}))" + NL
  + r"\to C^\bullet(\mathfrak U'^{(i)},u_i^*(\mathscr P_\bullet^{(i)}))$",
  "Layout: display where the print has an inline formula (cf. GLOBAL_ISSUES 21/36)."),
F(163, "'un homomorphisme de bicomplexes L -> L' = C(U'^(i), u_i^*(P)). En outre'",
  "formula set inline in the running text, followed by a full stop",
  "displayed with \\[ ... \\]",
  "other", "high",
  "\\[" + NL + r"  L_{\bullet\bullet}^{(i)}" + NL + r"  \longrightarrow" + NL
  + r"  L_{\bullet\bullet}^{\prime(i)}" + NL
  + r"  =C^\bullet(\mathfrak U'^{(i)},u_i^*(\mathscr P_\bullet^{(i)}))." + NL + "\\]",
  r"$L_{\bullet\bullet}^{(i)}\to L_{\bullet\bullet}^{\prime(i)}" + NL
  + r"=C^\bullet(\mathfrak U'^{(i)},u_i^*(\mathscr P_\bullet^{(i)}))$.",
  "Layout: display where the print has an inline formula."),
F(163, "'(0_I, 4.4.3.2)'",
  "bold 0 with subscript I", "plain 0", "convention", "high",
  r"($0_{\mathrm I}$, 4.4.3.2)", r"($\mathbf{0}_{\mathrm I}$, 4.4.3.2)", "", convention=2),
F(163, "'V'^(i) un recouvrement affine fini de X'^(i), plus fin que ... et que ..., le diagramme'",
  "plus fin que u_i^{-1}(U'^(i)) et que V^(i)",
  "plus fin que $u_i^{-1}(\\mathfrak V^{(i)})$ et que $\\mathfrak U'^{(i)}$",
  "misprint_in_print", "high",
  r"$u_i^{-1}(\mathfrak V^{(i)})$ et que $\mathfrak U'^{(i)}$",
  r"$u_i^{-1}(\mathfrak U'^{(i)})$ et que $\mathfrak V^{(i)}$",
  "The print interchanges V and U' (u_i^{-1} of a covering of X'^(i) is meaningless; V'^(i) must refine u_i^{-1}(V^(i)) and U'^(i) for the diagram). The TeX silently corrects.",
  corrected=r"$u_i^{-1}(\mathfrak V^{(i)})$ et que $\mathfrak U'^{(i)}$"),
F(163, "'On a donc en fait défini un homomorphisme de A-modules'",
  "'modules' italic (A roman)",
  "'$A$-modules' upright",
  "italics", "high",
  r"$A$-modules", r"$A$-\emph{modules}",
  "Contrasts with the (B_1 ⊗_A B_2)-modules that follow."),
F(163, "(6.7.10.4), end of the display",
  "no full stop after the formula; the text continues 'mais il est clair'",
  "full stop after the formula",
  "punctuation", "high",
  r"u_2^*(\mathscr P_\bullet^{(2)}))." + NL + r"  \tag{6.7.10.4}",
  r"u_2^*(\mathscr P_\bullet^{(2)}))" + NL + r"  \tag{6.7.10.4}",
  "Extra full stop in the TeX."),
F(163, "'compte tenu de (I, 1.6.5)'",
  "bold I", "plain I", "convention", "high",
  r"(I, 1.6.5)", r"(\textbf{I}, 1.6.5)", "", convention=2),
]

# ---------------- page 164 ----------------
items += [
F(164, "first line: 'l'isomorphisme canonique (M ⊗_B B')_g' ⥲ M_g ⊗_{B_g} B'_g' (0_I, 1.5.4)'",
  "formula set inline in the running text",
  "displayed with \\[ ... \\]",
  "other", "high",
  "\\[" + NL + r"  (M\otimes_B B')_{g'}" + NL + r"  \xrightarrow{\sim}" + NL + r"  M_g\otimes_{B_g}B'_{g'}" + NL + "\\]",
  r"$(M\otimes_B B')_{g'}\xrightarrow{\sim}M_g\otimes_{B_g}B'_{g'}$",
  "Layout: display where the print has an inline formula."),
F(164, "first line: '(0_I, 1.5.4)'",
  "bold 0 with subscript I", "plain 0", "convention", "high",
  r"($0_{\mathrm I}$, 1.5.4)", r"($\mathbf{0}_{\mathrm I}$, 1.5.4)", "", convention=2),
F(164, "(6.7.11): 'une famille finie de S-morphismes séparés et quasi-compacts f_i'",
  "'séparés' and 'quasi-compacts' italic, 'et' roman",
  "all upright",
  "italics", "high",
  r"$S$-morphismes séparés et quasi-compacts", r"$S$-morphismes \emph{séparés} et \emph{quasi-compacts}",
  ""),
F(164, "Proposition (6.7.12): 'pour i ∈ I—J, on ait'",
  "long dash I—J", "minus sign I-J", "convention", "high",
  r"pour $i\in I-J$, on ait", r"pour $i\in I\setmin J$, on ait", "", convention=7),
F(164, "proof of (6.7.12): 'Pour i ∈ I—J, on peut prendre'",
  "long dash I—J", "minus sign I-J", "convention", "high",
  r"Pour $i\in I-J$,", r"Pour $i\in I\setmin J$,", "", convention=7),
F(164, "Remarque (6.7.13): '(I, 3.3.5)'",
  "bold I", "plain I", "convention", "high",
  r"(I, 3.3.5)", r"(\textbf{I}, 3.3.5)", "", convention=2),
F(164, "Remarque (6.7.13): 'est Tor_.^S(f_2, f_1 : P^(2), P^(1))'",
  "colon after f_1",
  "semicolon after f_1",
  "misprint_in_print", "high",
  r"(f_2,f_1;", r"(f_2,f_1:",
  "The print has ':' for ';'; the TeX silently corrects it.",
  corrected=r"(f_2,f_1;"),
F(164, "(6.8.1): 'étant supposés limités inférieurement, supposons'",
  "'limités inférieurement' italic",
  "upright",
  "italics", "high",
  r"supposés limités inférieurement", r"supposés \emph{limités inférieurement}",
  ""),
F(164, "(6.8.1): '(et en particulier les P^(i) étant supposés limités inférieurement, supposons'",
  "the parenthesis opened before 'et en particulier' is never closed",
  "the same (kept)",
  "misprint_in_print", "medium",
  None, None,
  "The TeX keeps the printed reading. Correct reading: closing parenthesis after 'inférieurement', as in the same phrase of (6.9.1), p. 166.",
  corrected=r"étant supposés \emph{limités inférieurement}), supposons"),
F(164, "(6.8.1), last display: 'T_.j = Tor_.^S(...)'",
  "the script T of the print's script alphabet (the same family as P, O)",
  "\\mathcal T (the file writes its script letters with \\mathscr)",
  "font", "medium",
  r"\mathcal T_{\bullet j}", r"\mathscr T_{\bullet j}",
  "Only \\mathcal in pp. 160-169 of this run."),
]

# ---------------- page 165 ----------------
items += [
F(165, "Proposition (6.8.2): '(dit « foncteur spectral d'associativité »)'",
  "the parenthesis printed roman inside the italic statement",
  "italic (proposition environment)",
  "convention", "high",
  "(dit « foncteur spectral" + NL + "d'associativité »)",
  "\\textup{(dit « foncteur spectral" + NL + "d'associativité »)}",
  "", convention=6),
F(165, "Proposition (6.8.2): '(ou simplement (e)E(f_1, ..., f_m; P^(1), ..., P^(m)))'",
  "'(ou simplement ...)' set roman on the display line, after the formula",
  "set after the display in the running text, so italic",
  "convention", "high",
  r"\mathscr P_\bullet^{(m)})" + NL + "\\]" + NL + r"(ou simplement ${}^{(e)}\mathscr E(f_1,\ldots,f_m;" + NL
  + r"\mathscr P_\bullet^{(1)},\ldots,\mathscr P_\bullet^{(m)})$) dont",
  r"\mathscr P_\bullet^{(m)})" + NL + r"  \qquad\textup{(ou simplement ${}^{(e)}\mathscr E(f_1,\ldots,f_m;" + NL
  + r"\mathscr P_\bullet^{(1)},\ldots,\mathscr P_\bullet^{(m)})$)}" + NL + "\\]" + NL + "dont",
  "Moves the parenthesis into the display, upright.", convention=6),
F(165, "Proposition (6.8.2), E_2 term: outer 'Tor_q^S(Tor_{q_1}^S(...), Tor_{q_2}^S(...))'",
  "outer Tor with subscript q",
  "\\mathscr{T}\\!or_p^S",
  "misprint_in_print", "high",
  r"\mathscr{T}\!or_p^S\Bigl(", r"\mathscr{T}\!or_q^S\Bigl(",
  "E^2_{pq} needs Tor_p (cf. Tor_p^A in (6.8.3)); the TeX silently corrects.",
  corrected=r"\mathscr{T}\!or_p^S\Bigl("),
F(165, "proof of (6.8.2): 'Z^(1) = Y^(1) x_S Y^(2) x ... x_S Y^(r)'",
  "the second product sign has no subscript S; dots on the baseline",
  "Y^{(2)}\\times_S\\cdots\\times_S Y^{(r)}",
  "misprint_in_print", "medium",
  r"Y^{(2)}\times_S\cdots\times_S Y^{(r)}", r"Y^{(2)}\times\ldots\times_S Y^{(r)}",
  "Missing S under the second product sign; the TeX silently corrects. The fix also writes the print's baseline dots (\\ldots for \\cdots).",
  corrected=r"Y^{(2)}\times_S\ldots\times_S Y^{(r)}"),
F(165, "proof of (6.8.2): 'Z^(2) = Y^(r+1) x_S ... x_S Y^(m)'",
  "baseline dots", "\\cdots", "symbol", "medium",
  r"Y^{(r+1)}\times_S\cdots\times_S Y^{(m)}", r"Y^{(r+1)}\times_S\ldots\times_S Y^{(m)}",
  "Same pattern as GLOBAL_ISSUES 22 (EGA II)."),
F(165, "proof of (6.8.2): 'les Y^(i) sont affines;'",
  "'affines' italic", "upright", "italics", "high",
  r"sont affines;", r"sont \emph{affines};", ""),
F(165, "proof of (6.8.2), last sentence: 'Nous démontrerons donc le' + 'Corollaire (6.8.3). —'",
  "'Nous démontrerons donc le' runs into the heading 'Corollaire (6.8.3). —'",
  "'Nous démontrerons donc le corollaire suivant.'",
  "extra", "high",
  r"démontrerons donc le corollaire suivant.", r"démontrerons donc le",
  "Added words 'corollaire suivant.' in the TeX."),
F(165, "Corollaire (6.8.3), end of the E_2 display",
  "no full stop after the formula",
  "full stop after \\Bigr)",
  "punctuation", "high",
  "\\Bigr)." + NL + "\\end{split}" + NL + "\\]" + NL + "\\end{corollary}",
  "\\Bigr)" + NL + "\\end{split}" + NL + "\\]" + NL + "\\end{corollary}",
  "Extra full stop in the TeX."),
F(165, "proof of (6.8.3): '(au sens de (0, 11.7.1))'",
  "bold 0", "plain 0", "convention", "high",
  r"(au sens de (0, 11.7.1))", r"(au sens de (\textbf{0}, 11.7.1))", "", convention=2),
F(165, "proof of (6.8.3): 'le produit tensoriel M_... = ⊗_{i=1}^m M^(i)_... de ces tricomplexes'",
  "formula set inline in the running text",
  "displayed with \\[ ... \\]",
  "other", "high",
  "\\[" + NL + r"  M_{\bullet\bullet\bullet}" + NL + r"  =\bigotimes_{i=1}^m M_{\bullet\bullet\bullet}^{(i)}" + NL + "\\]",
  r"$M_{\bullet\bullet\bullet}" + NL + r"=\bigotimes_{i=1}^m M_{\bullet\bullet\bullet}^{(i)}$",
  "Layout: display where the print has an inline formula."),
F(165, "proof of (6.8.3): 'sont projectifs'",
  "'projectifs' italic", "upright", "italics", "high",
  r"sont projectifs,", r"sont \emph{projectifs},", ""),
F(165, "proof of (6.8.3): 'que l'on a H_.(M_...) = Tor_.^A(N'_., N''_.); la suite spectrale'",
  "formula set inline in the running text",
  "displayed with \\[ ... \\]",
  "other", "high",
  "\\[" + NL + r"  H_\bullet(M_{\bullet\bullet\bullet})" + NL + r"  =\mathbf{Tor}_\bullet^A(N'_\bullet,N''_\bullet);" + NL + "\\]",
  r"$H_\bullet(M_{\bullet\bullet\bullet})" + NL + r"=\mathbf{Tor}_\bullet^A(N'_\bullet,N''_\bullet)$;",
  "Layout: display where the print has an inline formula."),
F(165, "proof of (6.8.3): 'produits partiels X^(1) x_S x ... x_S X^(r)'",
  "X^(1)×_S × . . . ×_S X^(r) (a second product sign right after x_S; baseline dots)",
  "X^{(1)}\\times_S\\cdots\\times_S X^{(r)}",
  "misprint_in_print", "high",
  r"X^{(1)}\times_S\cdots\times_S X^{(r)}", r"X^{(1)}\times_S\times\ldots\times_S X^{(r)}",
  "Stray product sign in the print; the TeX silently corrects. The fix also writes the baseline dots.",
  corrected=r"X^{(1)}\times_S\ldots\times_S X^{(r)}"),
F(165, "proof of (6.8.3): 'et X^(r+1) x_S x ... x_S X^(m)'",
  "X^(r+1)×_S × . . . ×_S X^(m) (a second product sign right after x_S; baseline dots)",
  "X^{(r+1)}\\times_S\\cdots\\times_S X^{(m)}",
  "misprint_in_print", "high",
  r"X^{(r+1)}\times_S\cdots\times_S X^{(m)}", r"X^{(r+1)}\times_S\times\ldots\times_S X^{(m)}",
  "Stray product sign in the print; the TeX silently corrects. The fix also writes the baseline dots.",
  corrected=r"X^{(r+1)}\times_S\ldots\times_S X^{(m)}"),
]

# ---------------- page 166 ----------------
items += [
F(166, "(6.9.1): 'étant supposés limités inférieurement), considérons'",
  "'limités inférieurement' italic", "upright", "italics", "high",
  "supposés limités" + NL + "inférieurement)", "supposés \\emph{limités" + NL + "inférieurement})", ""),
F(166, "(6.9.1): 'posons Y'^(i = Y^(i)_(S')'",
  "Y'^(i : no closing parenthesis visible in the superscript (the '(' and 'i' are faintly printed)",
  "Y'^{(i)}",
  "misprint_in_print", "low",
  r"$Y'^{(i)}=Y_{(S')}^{(i)}$", r"$Y'^{(i}=Y_{(S')}^{(i)}$",
  "May be an inking defect rather than a dropped sort; check another copy before applying.",
  corrected=r"$Y'^{(i)}=Y_{(S')}^{(i)}$"),
F(166, "(6.9.1): '(I, 5.5.1 et 6.6.4)'",
  "bold I", "plain I", "convention", "high",
  r"(I, 5.5.1 et 6.6.4)", r"(\textbf{I}, 5.5.1 et 6.6.4)", "", convention=2),
F(166, "proof of (6.9.2): '(II, 1.5.5)'",
  "bold II", "plain II", "convention", "high",
  r"(II, 1.5.5)", r"(\textbf{II}, 1.5.5)", "", convention=2),
F(166, "proof of (6.9.2): 'il est clair alors que C(U'^(i), P'^(i)) = C(U^(i), P^(i)) ⊗_A A','",
  "formula set inline in the running text",
  "displayed with \\[ ... \\]",
  "other", "high",
  "\\[" + NL + r"  C^\bullet(\mathfrak U'^{(i)},\mathscr P_\bullet'^{(i)})" + NL
  + r"  =C^\bullet(\mathfrak U^{(i)},\mathscr P_\bullet^{(i)})\otimes_A A'," + NL + "\\]",
  r"$C^\bullet(\mathfrak U'^{(i)},\mathscr P_\bullet'^{(i)})" + NL
  + r"=C^\bullet(\mathfrak U^{(i)},\mathscr P_\bullet^{(i)})\otimes_A A'$,",
  "Layout: display where the print has an inline formula."),
F(166, "proof of (6.9.2): 'au sens de (0, 11.7.1)'",
  "bold 0", "plain 0", "convention", "high",
  r"au sens de (0, 11.7.1), formée", r"au sens de (\textbf{0}, 11.7.1), formée", "", convention=2),
F(166, "proof of (6.9.2), end: 'H_.(⊗(M^(i) ⊗_A A')) = H_.(⊗ M^(i)) ⊗_A A'.'",
  "formula set inline in the running text",
  "displayed with \\[ ... \\] and \\left( \\right)",
  "other", "high",
  "\\[" + NL + r"  H_\bullet\left(" + NL + r"    \bigotimes_{i=1}^m" + NL
  + r"    (M_{\bullet\bullet\bullet}^{(i)}\otimes_A A')" + NL + r"  \right)" + NL
  + r"  =H_\bullet\left(" + NL + r"    \bigotimes_{i=1}^m M_{\bullet\bullet\bullet}^{(i)}" + NL
  + r"  \right)\otimes_A A'." + NL + "\\]",
  r"$H_\bullet(\bigotimes_{i=1}^m(M_{\bullet\bullet\bullet}^{(i)}\otimes_A A'))" + NL
  + r"=H_\bullet(\bigotimes_{i=1}^m M_{\bullet\bullet\bullet}^{(i)})\otimes_A A'$.",
  "Layout: display where the print has an inline formula."),
F(166, "paragraph 'On notera que lorsque I est réduit au seul élément 1' (start)",
  "an unnumbered indented paragraph: no '(6.9.2.2)'",
  "\\begin{env}[6.9.2.2] prints a bold '(6.9.2.2)'",
  "extra", "high",
  "\\begin{env}[6.9.2.2]" + NL + "On notera que", "On notera que",
  "Apply together with the next finding (\\end{env})."),
F(166, "paragraph 'On notera que ...' (end): 'pour n=0 (6.2.1).'",
  "plain paragraph end",
  "\\end{env} of the env opened as (6.9.2.2)",
  "extra", "high",
  "pour $n=0$ (6.2.1)." + NL + "\\end{env}", "pour $n=0$ (6.2.1).",
  "Apply together with the previous finding (\\begin{env}[6.9.2.2])."),
F(166, "'un complexe Q'_. de O_S'-Modules quasi-cohérents limités inférieurement'",
  "'limités inférieurement' italic", "upright", "italics", "high",
  r"quasi-cohérents limités inférieurement, de sorte", r"quasi-cohérents \emph{limités inférieurement}, de sorte", ""),
]

# ---------------- verification ----------------
ok = True
texts = {}
for p in sorted({it["page"] for it in items}):
    with open(os.path.join(RUN, f"page_{p}.tex"), encoding="utf-8", newline="") as fh:
        texts[p] = fh.read().replace("\r\n", "\n")
for i, it in enumerate(items):
    fx = it["fix"]
    if fx is None:
        continue
    n = texts[it["page"]].count(fx["old"])
    if n != 1:
        ok = False
        print(f"BAD count={n} page={it['page']} where={it['where']!r}\n  old={fx['old']!r}")

# overlap check: no two fixes on one page may overlap in the original text
for p, t in texts.items():
    spans = []
    for it in items:
        if it["page"] == p and it["fix"]:
            s = t.find(it["fix"]["old"])
            spans.append((s, s + len(it["fix"]["old"]), it["where"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print("OVERLAP on page", p, ":", a[2], "|", b[2])

counts = {}
for it in items:
    c = counts.setdefault(it["page"], [0, 0, 0])
    if it["kind"] == "convention":
        c[1] += 1
    elif it["kind"] == "misprint_in_print":
        c[2] += 1
    else:
        c[0] += 1
print("counts (normal/convention/misprint):", counts)
print("total", len(items))
if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(items, fh, ensure_ascii=False, indent=1)
    print("written", OUT)
else:
    print("NOT written")
    sys.exit(1)
