# Builds findings_172_176.json for the EGA III part 2 scan check (pages 172-176).
# Strings use "⏎" for a line break (LF); raw strings keep TeX backslashes literal.
import json
import os

RUN = r"user\Documents\ega_scan_check_20261101\run_III2"
OUT = os.path.join(RUN, "findings_172_176.json")
SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega3"

NL = "\u23ce"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, outside=False):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected.replace(NL, "\n")
    d["note"] = note
    d["_outside"] = outside
    F.append(d)


IT = "Italic in the print; upright in the TeX."
IT_REM = "Italic in the print; upright in the TeX (remark body judged as roman)."
LAY = "Layout: the print sets this formula in the running text; the TeX displays it. The formula itself matches."
OUTS = "OUTSIDE the page's segment: in ega3-7-fr.tex before its first marker \\oldpage[III]{176} (continuation of p. 175). "

# ---------------- page 172 ----------------
add(172, "proof of (6.10.1): 'une résolution de Cartan-Eilenberg projective'",
    "Cartan-Eilenberg with a hyphen (enlarged crop)", "Cartan--Eilenberg (en dash)",
    "punctuation", None, "high",
    r"""Cartan--Eilenberg""", r"""Cartan-Eilenberg""",
    "ega3-6 writes Cartan-Eilenberg with a hyphen elsewhere (pp. 141-145).")
add(172, "proof of (6.10.1): '(au sens de (0, 11.7.1))'", "bold 0", "plain 0",
    "convention", 2, "high",
    r"""(0, 11.7.1)""", r"""(\textbf{0}, 11.7.1)""",
    "Bold chapter number in the reference.")
add(172, "proof of (6.10.1): 'formée de A_i-modules, et en vertu de (6.6.6)'",
    "'modules' italic (enlarged crop)", "upright", "italics", None, "high",
    r"""$A_i$-modules, et en vertu""", r"""$A_i$-\emph{modules}, et en vertu""",
    IT)
add(172, "proof of (6.10.1): 'est canoniquement isomorphe à H•(M•••⊗_A Q'•), où'",
    "roman H (homology of a complex of modules), as upright as the M; formula in the running text (enlarged crop)",
    "\\mathscr H_\\bullet, displayed", "font", None, "high",
    r"""isomorphe à⏎\[⏎  \mathscr H_\bullet⏎  (M_{\bullet\bullet\bullet}\otimes_A Q'_\bullet),⏎\]⏎où""",
    r"""isomorphe à⏎$\mathrm H_\bullet(M_{\bullet\bullet\bullet}\otimes_A Q'_\bullet)$, où""",
    "Roman H, not script: M••• is a complex of A-modules (ega3-6 writes this H as \\mathrm H elsewhere). The fix also sets the formula inline, as printed.")
add(172, "proof of (6.10.1): 'M••• = M(1)•••⊗_A M(2)•••⊗ . . . ⊗_A M(n)•••'",
    "second tensor sign without the subscript A, then baseline dots: '⊗ . . . ⊗_A' (enlarged crop); formula in the running text",
    "\\otimes_A\\cdots\\otimes_A, displayed", "formula", None, "high",
    r"""\[⏎  M_{\bullet\bullet\bullet}⏎  =⏎  M_{\bullet\bullet\bullet}^{(1)}⏎  \otimes_A M_{\bullet\bullet\bullet}^{(2)}⏎  \otimes_A\cdots\otimes_A M_{\bullet\bullet\bullet}^{(n)}⏎\]⏎""",
    r"""$M_{\bullet\bullet\bullet}=M_{\bullet\bullet\bullet}^{(1)}\otimes_A M_{\bullet\bullet\bullet}^{(2)}\otimes\ldots\otimes_A M_{\bullet\bullet\bullet}^{(n)}$⏎""",
    "The first and last ⊗ carry the subscript A, the one before the dots does not. The fix also sets the formula inline, as printed.")
add(172, "proof of (6.10.1): 'et Q'• = Q̃'•'", "tilde over Q only; prime and bullet outside (enlarged crop)",
    "\\widetilde{Q'_\\bullet}", "convention", 8, "high",
    r"""\widetilde{Q'_\bullet}""", r"""\widetilde{Q}'_\bullet""",
    "Tilde over a letter carrying a prime and a subscript.")
add(172, "proof of (6.10.1): 'les anneaux A_i sont des A-modules plats'", "'plats' italic (enlarged crop)",
    "upright", "italics", None, "high",
    r"""sont des $A$-modules plats, les""", r"""sont des $A$-modules \emph{plats}, les""",
    "Italic in the print; upright in the TeX. The second 'plats' of the sentence ('A-modules plats (0_I, 6.2.1)') is roman, as in the TeX.")
add(172, "proof of (6.10.1): '(0_I, 6.2.1)'", "bold 0", "plain 0 ($0_{\\mathrm I}$)",
    "convention", 2, "high",
    r"""($0_{\mathrm I}$, 6.2.1)""", r"""($\mathbf{0}_{\mathrm I}$, 6.2.1)""",
    "Bold chapter number in the reference (form as GLOBAL_ISSUES item 35).")
add(172, "proof of (6.10.1): 'M••• est un tricomplexe de B-modules'", "'modules' italic (enlarged crop)",
    "upright", "italics", None, "high",
    r"""$B$-modules;""", r"""$B$-\emph{modules};""",
    IT)
add(172, "proof of (6.10.1): 'le complexe R• = (M•••)~ de O_Y-Modules'", "in the running text", "displayed",
    "other", None, "high",
    r"""le complexe⏎\[⏎  \mathscr R_\bullet=(M_{\bullet\bullet\bullet})^\sim⏎\]⏎de""",
    r"""le complexe⏎$\mathscr R_\bullet=(M_{\bullet\bullet\bullet})^\sim$ de""",
    LAY + " The ^\\sim after the parenthesis is left for the GLOBAL_ISSUES item 25 pass.")
add(172, "Remarques (6.10.3) (i): 'est isomorphe à Tor•(R•, Q'•) puisque'",
    "roundhand T + italic 'or', regular weight: the sign of the hypertor of Modules of 6.5 (cf. p. 150), not the bold roman Tor of modules (enlarged crop)",
    "\\mathbf{Tor}_\\bullet", "font", None, "medium",
    r"""\mathbf{Tor}_\bullet(\mathscr R_\bullet,\mathscr Q'_\bullet)""",
    r"""\mathscr{T}\!or_\bullet(\mathscr R_\bullet,\mathscr Q'_\bullet)""",
    "ega3-6 transcribes this sign as \\mathscr{T}\\!or in 6.5 (pp. 149-151); \\mathbf{Tor} is its form for the bold roman Tor of modules (6.3). Part of the document-wide Tor issue (final message).")
add(172, "(6.10.3.1): 'E²_pq = ⊕ Tor^S_p(H_q'(R•), H_q''(Q'•))'",
    "script 𝒯 + italic 'or' (the sheaf Tor of (6.9.8.1)) (enlarged crop)", "\\mathbf{Tor}_p^S", "font", None, "high",
    r"""\mathbf{Tor}_p^S""", r"""\mathscr{T}\!or_p^S""",
    "Same sign as in (6.9.8.1)-(6.9.8.3), which ega3-6 writes \\mathscr{T}\\!or.")
add(172, "Remarques (6.10.3) (ii): 'tel que H•(g) : H•(R'•)→H•(R•) soit un isomorphisme'", "in the running text",
    "displayed", "other", None, "high",
    r"""tel⏎que⏎\[⏎  \mathscr H_\bullet(g):⏎  \mathscr H_\bullet(\mathscr R'_\bullet)⏎  \longrightarrow⏎  \mathscr H_\bullet(\mathscr R_\bullet)⏎\]⏎soit un isomorphisme""",
    r"""tel⏎que $\mathscr H_\bullet(g):\mathscr H_\bullet(\mathscr R'_\bullet)\longrightarrow\mathscr H_\bullet(\mathscr R_\bullet)$⏎soit un isomorphisme""",
    LAY)
add(172, "Remarques (6.10.3) (ii): 'un isomorphisme de ∂-foncteurs en Q'• : H•(R'•⊗_S Q'•) ⥲ H•(R•⊗_S Q'•) tel que'",
    "colon after 'en Q'•'; formula in the running text", "no colon; displayed", "punctuation", None, "high",
    r"""en $\mathscr Q'_\bullet$⏎\[⏎  \mathscr H_\bullet⏎  (\mathscr R'_\bullet\otimes_S\mathscr Q'_\bullet)⏎  \xrightarrow{\sim}⏎  \mathscr H_\bullet⏎  (\mathscr R_\bullet\otimes_S\mathscr Q'_\bullet)⏎\]⏎tel que le diagramme""",
    r"""en $\mathscr Q'_\bullet$ :⏎$\mathscr H_\bullet(\mathscr R'_\bullet\otimes_S\mathscr Q'_\bullet)\xrightarrow{\sim}\mathscr H_\bullet(\mathscr R_\bullet\otimes_S\mathscr Q'_\bullet)$⏎tel que le diagramme""",
    "Missing colon. The fix also sets the formula inline, as printed.")

# ---------------- page 173 ----------------
add(173, "Remarques (6.10.3) (iii): 'formés de A_i-modules libres (comme il'", "'libres' italic", "upright",
    "italics", None, "high",
    r"""$A_i$-modules libres (comme""", r"""$A_i$-modules \emph{libres} (comme""", IT_REM)
add(173, "(iii): '(0, 11.5.2.1) « dualisée »'", "bold 0", "plain 0", "convention", 2, "high",
    r"""(0, 11.5.2.1)""", r"""(\textbf{0}, 11.5.2.1)""", "Bold chapter number in the reference.")
add(173, "(iii): 'les M(i)•••⊗_{A_i}B sont alors formés'", "in the running text", "displayed", "other", None, "high",
    r"""les⏎\[⏎  M_{\bullet\bullet\bullet}^{(i)}\otimes_{A_i}B⏎\]⏎sont alors""",
    r"""les⏎$M_{\bullet\bullet\bullet}^{(i)}\otimes_{A_i}B$⏎sont alors""", LAY)
add(173, "(iii): 'associé à un complexe de B-modules libres. En outre'", "'libres' italic", "upright", "italics", None, "high",
    r"""$B$-modules libres. En outre""", r"""$B$-modules \emph{libres}. En outre""",
    IT_REM + " The earlier 'B-modules libres, et comme' is roman, as in the TeX.")
add(173, "(iii): 'dépend fonctoriellement de chacun'", "'fonctoriellement' italic", "upright", "italics", None, "high",
    r"""dépend fonctoriellement""", r"""dépend \emph{fonctoriellement}""", IT_REM)
add(173, "(iii): 'les classes d'homomorphismes pour la relation d'homotopie'", "'classes d'homomorphismes' italic",
    "upright", "italics", None, "high",
    r"""les classes d'homomorphismes""", r"""les \emph{classes d'homomorphismes}""", IT_REM)
add(173, "(iii): 'le tricomplexe M••• est un foncteur en chacun des P(i)•'", "'foncteur' italic", "upright",
    "italics", None, "high",
    r"""est un foncteur en chacun""", r"""est un \emph{foncteur} en chacun""", IT_REM)
add(173, "(iii): 'suites exactes 0→P'(i)•→P(i)•→P''(i)•→0 de complexes'", "in the running text", "displayed",
    "other", None, "high",
    r"""exactes⏎\[⏎  0\longrightarrow\mathscr P_\bullet^{\prime(i)}⏎  \longrightarrow\mathscr P_\bullet^{(i)}⏎  \longrightarrow\mathscr P_\bullet^{\prime\prime(i)}⏎  \longrightarrow0⏎\]⏎de complexes""",
    r"""exactes $0\longrightarrow\mathscr P_\bullet^{\prime(i)}\longrightarrow\mathscr P_\bullet^{(i)}\longrightarrow\mathscr P_\bullet^{\prime\prime(i)}\longrightarrow0$⏎de complexes""",
    LAY)
add(173, "Scholie (6.10.4): 'formé de O_Y-Modules S-plats entraîne'", "'plats' italic (enlarged crop)",
    "upright (the scholium body is roman)", "italics", None, "high",
    r"""$S$-plats entraîne""", r"""$S$-\emph{plats} entraîne""", IT)
add(173, "Scholie (6.10.4): 'entraîne aisément que H•(R•⊗_S Q'•) est un foncteur'", "in the running text",
    "displayed", "other", None, "high",
    r"""aisément que⏎\[⏎  \mathscr H_\bullet⏎  (\mathscr R_\bullet\otimes_S\mathscr Q'_\bullet)⏎\]⏎est un""",
    r"""aisément que $\mathscr H_\bullet(\mathscr R_\bullet\otimes_S\mathscr Q'_\bullet)$⏎est un""", LAY)
add(173, "Scholie (6.10.4): 'un foncteur homologique en Q'•'", "'homologique' italic (enlarged crop)", "upright",
    "italics", None, "high",
    r"""foncteur homologique en""", r"""foncteur \emph{homologique} en""", IT)
add(173, "Scholie (6.10.4), display: 'X = X_1 ×_S X_2 × . . . ×_S X_n'",
    "X_1, X_2, X_n with subscripts; second × without S; baseline dots (enlarged crop)",
    "X=X^{(1)}\\times_SX^{(2)}\\times_S\\cdots\\times_SX^{(n)}", "misprint_in_print", None, "high",
    r"""X=X^{(1)}\times_SX^{(2)}\times_S\cdots\times_SX^{(n)}""",
    r"""X=X_1\times_SX_2\times\ldots\times_SX_n""",
    "Misprint: the factors are the X^{(i)} of (6.10.1) (f_i : X^{(i)}→Y^{(i)}); the print has X_1, X_2, X_n. The TeX silently corrects it; the fix restores the printed reading. The bare × before the dots and the baseline dots are the printed reading, not part of the misprint (kept in 'corrected').",
    corrected=r"""X=X^{(1)}\times_SX^{(2)}\times\ldots\times_SX^{(n)}""")
add(173, "Scholie (6.10.4), display: 'f = f_1 ×_S f_2 ×_S . . . ×_S f_n'", "baseline dots (enlarged crop)", "\\cdots",
    "symbol", None, "high",
    r"""f=f_1\times_Sf_2\times_S\cdots\times_Sf_n""", r"""f=f_1\times_Sf_2\times_S\ldots\times_Sf_n""",
    "Baseline dots, as GLOBAL_ISSUES item 22 notes for EGA II.")
add(173, "Scholie (6.10.4), display: 'P• = P(1)•⊗_S P(2)•⊗ . . . ⊗_S P(n)•'",
    "second ⊗ without the subscript S, then baseline dots (enlarged crop)", "\\otimes_S\\cdots\\otimes_S",
    "formula", None, "high",
    r"""\otimes_S\cdots\otimes_S\mathscr P_\bullet^{(n)}""", r"""\otimes\ldots\otimes_S\mathscr P_\bullet^{(n)}""",
    "As printed: the ⊗ before the dots has no subscript.")
add(173, "Scholie (6.10.4): 'f' = f ×_S 1_S'; les problèmes de changement de base'",
    "semicolon after the display, then lower-case 'les'", "full stop, then 'Les'", "punctuation", None, "high",
    r"""f'=f\times_S1_{S'}.⏎\]⏎Les problèmes""", r"""f'=f\times_S1_{S'};⏎\]⏎les problèmes""",
    "The sentence continues after the display.")
add(173, "Scholie (6.10.4): 'l'hypercohomologie H•_{f'}(P•⊗_S N') en tant que foncteur'", "in the running text",
    "displayed", "other", None, "high",
    r"""l'hypercohomologie⏎\[⏎  \mathscr H^\bullet_{f'}⏎  (\mathscr P_\bullet\otimes_S\mathscr N')⏎\]⏎en tant que""",
    r"""l'hypercohomologie $\mathscr H^\bullet_{f'}(\mathscr P_\bullet\otimes_S\mathscr N')$⏎en tant que""",
    LAY + " The letter H is the roundhand hypercohomology H (document-wide, final message).")
add(173, "Scholie (6.10.4): 'l'hypercohomologie H•_f(P•⊗_S N) comme foncteur'", "in the running text", "displayed",
    "other", None, "high",
    r"""l'hypercohomologie⏎\[⏎  \mathscr H^\bullet_f⏎  (\mathscr P_\bullet\otimes_S\mathscr N)⏎\]⏎comme""",
    r"""l'hypercohomologie $\mathscr H^\bullet_f(\mathscr P_\bullet\otimes_S\mathscr N)$⏎comme""", LAY)
add(173, "Scholie (6.10.4): 'sont S-plats, il résulte de ce qui précède'", "'plats' italic (enlarged crop)", "upright",
    "italics", None, "high",
    r"""$S$-plats, il résulte""", r"""$S$-\emph{plats}, il résulte""", IT)
add(173, "Scholie (6.10.4): 'un foncteur cohomologique en N'", "'cohomologique' italic (enlarged crop)", "upright",
    "italics", None, "high",
    r"""foncteur cohomologique en""", r"""foncteur \emph{cohomologique} en""", IT)
add(173, "Scholie (6.10.4): 'aborder l'étude de H•_f(P•⊗_S N) par les méthodes'", "in the running text",
    "displayed", "other", None, "high",
    r"""l'étude de⏎\[⏎  \mathscr H^\bullet_f⏎  (\mathscr P_\bullet\otimes_S\mathscr N)⏎\]⏎par""",
    r"""l'étude de $\mathscr H^\bullet_f(\mathscr P_\bullet\otimes_S\mathscr N)$⏎par""", LAY)
add(173, "Scholie (6.10.4): 'formé de O_X-Modules Y-plats. On a dans ce cas le'", "'plats' italic (enlarged crop)",
    "upright", "italics", None, "high",
    r"""$Y$-plats. On a""", r"""$Y$-\emph{plats}. On a""", IT)
add(173, "Théorème (6.10.5): 'O_X-Modules cohérents, plats sur Y, limité inférieurement'",
    "'plats' roman inside the italic statement (enlarged crop)", "italic (theorem body)", "convention", 6, "high",
    r"""cohérents, plats sur $Y$""", r"""cohérents, \textup{plats} sur $Y$""", "")
add(173, "Théorème (6.10.5): 'des O_Y-Modules de la forme O_Y^{mi}'",
    "exponent 'mi': the i is on the line of the m, same size, not a subscript (crop at 8x)",
    "\\mathscr O_Y^{m_i}", "misprint_in_print", None, "high",
    r"""\mathscr O_Y^{m_i}""", r"""\mathscr O_Y^{mi}""",
    "Misprint: the exponent is m_i (the rank of the term L_i). The TeX silently corrects it; the fix restores the printed reading.",
    corrected=r"""\mathscr O_Y^{m_i}""")
add(173, "Théorème (6.10.5), last display of the page: '... L'• = u*(L•)'",
    "no comma after u*(L•); p. 174 continues '(qui est un complexe ...'", "comma after u^*(\\mathscr L_\\bullet)",
    "punctuation", None, "high",
    r"""u^*(\mathscr L_\bullet),⏎\]""", r"""u^*(\mathscr L_\bullet)⏎\]""",
    "Extra comma in the TeX (enlarged crop).")

# ---------------- page 174 ----------------
add(174, "Théorème (6.10.5): '(qui est un complexe de O_{Y'}-modules localement libres de type fini)'",
    "lower-case 'modules' after O_{Y'} (enlarged crop)", "'Modules'", "misprint_in_print", None, "high",
    r"""$\mathscr O_{Y'}$-Modules localement""", r"""$\mathscr O_{Y'}$-modules localement""",
    "Misprint: sheaves of modules are O_Y-Modules with a capital M everywhere else. The TeX silently corrects it; the fix restores the printed reading.",
    corrected=r"""$\mathscr O_{Y'}$-Modules localement""")
add(174, "proof of (6.10.5): 'quasi-cohérents et Y-libres (6.10.3, (ii))'", "'(6.10.3, (ii))' (enlarged crop)",
    "'(6.10.3, (iii))'", "misprint_in_print", None, "high",
    r"""(6.10.3, (iii))""", r"""(6.10.3, (ii))""",
    "Misprint: the freeness of R• comes from (6.10.3, (iii)); (ii) is the quasi-isomorphism remark, cited correctly twice later on the page. The TeX silently corrects it; the fix restores the printed reading.",
    corrected=r"""(6.10.3, (iii))""")
add(174, "proof of (6.10.5): 'ne sont pas nécessairement des O_Y-Modules de type fini'", "'de type fini' italic",
    "upright", "italics", None, "high",
    r"""Modules de type fini. Mais""", r"""Modules \emph{de type fini}. Mais""", IT)
add(174, "proof of (6.10.5): 'formé de O_Y-Modules cohérents (6.2.5)'", "'cohérents' italic", "upright",
    "italics", None, "high",
    r"""Modules cohérents (6.2.5)""", r"""Modules \emph{cohérents} (6.2.5)""", IT)
add(174, "proof of (6.10.5): 'On sait alors (0, 11.9.2)'", "bold 0", "plain 0", "convention", 2, "high",
    r"""(0, 11.9.2)""", r"""(\textbf{0}, 11.9.2)""", "Bold chapter number in the reference.")
add(174, "proof of (6.10.5): 'à des A-modules libres de type fini, et un homomorphisme'", "'de type fini' italic",
    "upright", "italics", None, "high",
    r"""libres de type fini, et un""", r"""libres \emph{de type fini}, et un""", IT)
add(174, "proof of (6.10.5): 'et un homomorphisme L•→R•, tels que'", "in the running text", "displayed",
    "other", None, "high",
    r"""homomorphisme⏎\[⏎  \mathscr L_\bullet\longrightarrow\mathscr R_\bullet,⏎\]⏎tels que""",
    r"""homomorphisme $\mathscr L_\bullet\longrightarrow\mathscr R_\bullet$,⏎tels que""", LAY)
add(174, "proof of (6.10.5): 'pour l'homologie, H•(L•)→H•(R•) soit bijectif'",
    "comma after 'l'homologie'; formula in the running text (enlarged crop)", "no comma; displayed",
    "punctuation", None, "high",
    r"""pour l'homologie⏎\[⏎  \mathscr H_\bullet(\mathscr L_\bullet)⏎  \longrightarrow⏎  \mathscr H_\bullet(\mathscr R_\bullet)⏎\]⏎soit bijectif""",
    r"""pour l'homologie,⏎$\mathscr H_\bullet(\mathscr L_\bullet)\longrightarrow\mathscr H_\bullet(\mathscr R_\bullet)$⏎soit bijectif""",
    "Missing comma. The fix also sets the formula inline, as printed.")
add(174, "proof of (6.10.5): 'lorsque Y' est affine'", "'affine' italic", "upright", "italics", None, "high",
    r"""est affine;""", r"""est \emph{affine};""", IT)
add(174, "Remarque (6.10.6): 'on a alors H_n(L•) = H^{-n}(f, F) = R^{-n}f_*(F) (6.2.1), on voit'",
    "roman R; formula in the running text (enlarged crop)", "plain R (math italic); displayed with \\qquad(6.2.1)",
    "font", None, "high",
    r"""Comme on a alors⏎\[⏎  \mathscr H_n(\mathscr L_\bullet)⏎  =⏎  \mathscr H^{-n}(f,\mathscr F)⏎  =⏎  R^{-n}f_*(\mathscr F)⏎  \qquad(6.2.1),⏎\]⏎on voit""",
    r"""Comme on a alors⏎$\mathscr H_n(\mathscr L_\bullet)=\mathscr H^{-n}(f,\mathscr F)=\mathrm R^{-n}f_*(\mathscr F)$ (6.2.1),⏎on voit""",
    "Upright R as ega3-6 writes R^n f_* elsewhere (\\mathrm R). The fix also sets the formula inline, as printed.")
add(174, "Remarque (6.10.6): 'qu'on peut alors supposer que L• n'a que des termes de degrés ≤0'",
    "'n'a que des termes de degrés' italic", "upright", "italics", None, "high",
    r"""n'a que des termes de degrés""", r"""\emph{n'a que des termes de degrés}""", IT_REM)
add(174, "Remarque (6.10.6): '(donc en nombre fini)'", "'fini' italic", "upright", "italics", None, "high",
    r"""nombre fini)""", r"""nombre \emph{fini})""", IT_REM)
add(174, "Remarque (6.10.6): 'que les L_i sont localement libres de type fini'", "'localement libres' italic",
    "upright", "italics", None, "high",
    r"""sont localement libres de type fini.""", r"""sont \emph{localement libres} de type fini.""", IT_REM)

# ---------------- page 175 ----------------
add(175, "Remarque (6.10.6): 'tels qu'il y ait un isomorphisme H•(f, F⊗_Y Q•) ⥲ H•(L•⊗_Y Q•) fonctoriel en Q•'",
    "in the running text", "displayed", "other", None, "high",
    r"""isomorphisme⏎\[⏎  \mathscr H^\bullet⏎  (f,\mathscr F\otimes_Y\mathscr Q_\bullet)⏎  \xrightarrow{\sim}⏎  \mathscr H_\bullet⏎  (\mathscr L_\bullet\otimes_Y\mathscr Q_\bullet)⏎\]⏎fonctoriel""",
    r"""isomorphisme $\mathscr H^\bullet(f,\mathscr F\otimes_Y\mathscr Q_\bullet)\xrightarrow{\sim}\mathscr H_\bullet(\mathscr L_\bullet\otimes_Y\mathscr Q_\bullet)$⏎fonctoriel""",
    LAY)
add(175, "heading 7.1", "'7.1. Foncteurs de A-modules.' (final full stop)", "no full stop", "punctuation", None, "high",
    r"""\subsection{Foncteurs de $A$-modules}""", r"""\subsection{Foncteurs de $A$-modules.}""",
    OUTS + "Same pattern as GLOBAL_ISSUES item 43 and the 6.1 heading (p. 137).", outside=True)
add(175, "(7.1.1): 'nous noterons Ab_A la catégorie'", "Ab bold italic (enlarged crop)", "\\mathbf{Ab} (bold upright)",
    "font", None, "high",
    r"""noterons⏎$\mathbf{Ab}_A$ la""", r"""noterons⏎$\boldsymbol{Ab}_A$ la""",
    OUTS + "Category name printed bold italic (document-wide candidate, final message).", outside=True)
add(175, "(7.1.1): 'la catégorie des A-modules à gauche'", "'modules à gauche' italic (enlarged crop)", "upright",
    "italics", None, "high",
    r"""$A$-modules à gauche, et nous""", r"""$A$-\emph{modules à gauche}, et nous""", OUTS + IT, outside=True)
add(175, "(7.1.1): 'nous noterons simplement Ab la catégorie des Z-modules'", "Ab bold italic", "\\mathbf{Ab}",
    "font", None, "high",
    r"""simplement $\mathbf{Ab}$ la""", r"""simplement $\boldsymbol{Ab}$ la""", OUTS + "Bold italic Ab.", outside=True)
add(175, "(7.1.1): 'Soit T : Ab_A→Ab un foncteur covariant additif'", "Ab bold italic; formula in the running text",
    "\\mathbf{Ab}; displayed", "font", None, "high",
    r"""Soit⏎\[⏎  T:\mathbf{Ab}_A\longrightarrow\mathbf{Ab}⏎\]⏎un""",
    r"""Soit $T:\boldsymbol{Ab}_A\longrightarrow\boldsymbol{Ab}$⏎un""",
    OUTS + "Bold italic Ab. The fix also sets the formula inline, as printed.", outside=True)
add(175, "(7.1.1): 'un foncteur covariant additif, et soit M'", "'foncteur covariant additif' italic (enlarged crop)",
    "upright", "italics", None, "high",
    r"""foncteur covariant additif, et soit""", r"""\emph{foncteur covariant additif}, et soit""",
    OUTS + IT, outside=True)
add(175, "(7.1.1): 'un (A, A)-bimodule'", "'bimodule' italic (enlarged crop)", "upright", "italics", None, "high",
    r"""$(A,A)$-bimodule;""", r"""$(A,A)$-\emph{bimodule};""", OUTS + IT, outside=True)
add(175, "(7.1.1): 'd'une structure de A-module à droite. En effet'", "'module à droite' italic (enlarged crop)",
    "upright", "italics", None, "high",
    r"""structure de $A$-module à droite""", r"""structure de $A$-\emph{module à droite}""", OUTS + IT, outside=True)
add(175, "(7.1.1): 'l'endomorphisme x→xa'", "plain arrow (enlarged crop)", "\\mapsto", "convention", 3, "high",
    r"""$x\mapsto xa$""", r"""$x\to xa$""", OUTS + "Plain arrow printed.", outside=True)
add(175, "(7.1.1): 'du A-module à gauche M'", "'à gauche' italic, 'module' roman (enlarged crop)", "upright",
    "italics", None, "high",
    r"""$A$-module à gauche $M$""", r"""$A$-module \emph{à gauche} $M$""", OUTS + IT, outside=True)
add(175, "(7.1.1): 'un endomorphisme du Z-module T(M)'", "'module' italic (enlarged crop)", "upright",
    "italics", None, "high",
    r"""$\mathbf Z$-module $T(M)$""", r"""$\mathbf Z$-\emph{module} $T(M)$""", OUTS + IT, outside=True)
add(175, "(7.1.1), display: 'T(h_ab) = T(h_b∘h_a) = T(h_b)∘T(h_a)   et   T(h_{a+b}) = ...'",
    "no comma before 'et' (enlarged crop)", "comma after T(h_b)\\circ T(h_a)", "punctuation", None, "high",
    r"""T(h_b)\circ T(h_a),⏎  \qquad\text{et}""", r"""T(h_b)\circ T(h_a)⏎  \qquad\text{et}""",
    OUTS + "Extra comma in the TeX.", outside=True)
add(175, "(7.1.1): 'l'application (a, y)→T(h_a)(y) est une loi externe'",
    "plain arrow; formula in the running text (enlarged crop)", "\\longmapsto; displayed", "convention", 3, "high",
    r"""l'application⏎\[⏎  (a,y)\longmapsto T(h_a)(y)⏎\]⏎est""", r"""l'application $(a,y)\to T(h_a)(y)$⏎est""",
    OUTS + "Plain arrow printed. The fix also sets the formula inline, as printed.", outside=True)
add(175, "(7.1.1): 'En particulier, T(A_s) est un A-module à droite.'", "'module à droite' italic", "upright",
    "italics", None, "high",
    r"""$T(A_s)$ est un $A$-module à droite.""", r"""$T(A_s)$ est un $A$-\emph{module à droite}.""",
    OUTS + IT + " ('une loi externe de A-module à droite' just before is roman, as in the TeX.)", outside=True)
add(175, "(7.1.2): 'Lorsque A est un anneau commutatif'", "'commutatif' italic (enlarged crop)", "upright",
    "italics", None, "high",
    r"""anneau commutatif, il""", r"""anneau \emph{commutatif}, il""", OUTS + IT, outside=True)
add(175, "(7.1.2): 'pour tout a∈A, u∘h_{a,M} = h_{a,N}∘u, d'où T(u)∘T(h_{a,M}) = T(h_{a,N})∘T(u), ce qui prouve'",
    "both formulas in the running text", "two displays", "other", None, "high",
    r"""$a\in A$,⏎\[⏎  u\circ h_{a,M}=h_{a,N}\circ u,⏎\]⏎d'où⏎\[⏎  T(u)\circ T(h_{a,M})⏎  =⏎  T(h_{a,N})\circ T(u),⏎\]⏎ce qui""",
    r"""$a\in A$, $u\circ h_{a,M}=h_{a,N}\circ u$,⏎d'où $T(u)\circ T(h_{a,M})=T(h_{a,N})\circ T(u)$,⏎ce qui""",
    OUTS + LAY, outside=True)
add(175, "(7.1.2): 'est un homomorphisme de A-modules; on voit donc'", "'modules' italic (enlarged crop)", "upright",
    "italics", None, "high",
    r"""$A$-modules; on⏎voit""", r"""$A$-\emph{modules}; on⏎voit""",
    OUTS + IT + " (The earlier 'homomorphisme de A-modules, on a' is roman, as in the TeX.)", outside=True)
add(175, "(7.1.2): 'de la catégorie Ab_A dans elle-même'", "Ab bold italic", "\\mathbf{Ab}", "font", None, "high",
    r"""catégorie $\mathbf{Ab}_A$ dans elle-même""", r"""catégorie $\boldsymbol{Ab}_A$ dans elle-même""",
    OUTS + "Bold italic Ab.", outside=True)
add(175, "(7.1.2): 'une équivalence canonique'", "'équivalence' italic (enlarged crop)", "upright", "italics", None,
    "high", r"""une équivalence canonique""", r"""une \emph{équivalence} canonique""", OUTS + IT, outside=True)
add(175, "(7.1.2): 'foncteurs covariants additifs Ab_A→Ab'", "Ab bold italic", "\\mathbf{Ab}", "font", None, "high",
    r"""additifs $\mathbf{Ab}_A\to\mathbf{Ab}$""", r"""additifs $\boldsymbol{Ab}_A\to\boldsymbol{Ab}$""",
    OUTS + "Bold italic Ab.", outside=True)
add(175, "(7.1.2): 'foncteurs covariants A-linéaires'", "'linéaires' italic (enlarged crop)", "upright", "italics",
    None, "high", r"""covariants $A$-linéaires""", r"""covariants $A$-\emph{linéaires}""", OUTS + IT, outside=True)
add(175, "(7.1.2): 'T : Ab_A→Ab_A, c'est-à-dire tels que T(h_{a,M}) = h_{a,T(M)} pour tout a∈A.'",
    "Ab bold italic; both formulas in the running text", "\\mathbf{Ab}; two displays ('pour tout' as \\text)",
    "font", None, "high",
    r"""\[⏎  T:\mathbf{Ab}_A\longrightarrow\mathbf{Ab}_A,⏎\]⏎c'est-à-dire tels que⏎\[⏎  T(h_{a,M})=h_{a,T(M)}⏎  \qquad\text{pour tout }a\in A.⏎\]⏎""",
    r"""$T:\boldsymbol{Ab}_A\longrightarrow\boldsymbol{Ab}_A$,⏎c'est-à-dire tels que⏎$T(h_{a,M})=h_{a,T(M)}$ pour tout $a\in A$.⏎""",
    OUTS + "Bold italic Ab. The fix also sets both formulas inline, as printed.", outside=True)
add(175, "(7.1.2): 'le foncteur d'inclusion I : Ab_A→Ab, faisant correspondre'",
    "Ab bold italic; formula in the running text", "\\mathbf{Ab}; displayed", "font", None, "high",
    r"""inclusion⏎\[⏎  I:\mathbf{Ab}_A\longrightarrow\mathbf{Ab},⏎\]⏎faisant""",
    r"""inclusion $I:\boldsymbol{Ab}_A\longrightarrow\boldsymbol{Ab}$,⏎faisant""",
    OUTS + "Bold italic Ab. The fix also sets the formula inline, as printed.", outside=True)
add(175, "(7.1.3): 'soit B une A-algèbre (non nécessairement commutative)'", "'algèbre' italic (enlarged crop)",
    "upright", "italics", None, "high",
    r"""$A$-algèbre (non""", r"""$A$-\emph{algèbre} (non""", OUTS + IT, outside=True)

# ---------------- page 176 ----------------
add(176, "(7.1.3): 'un foncteur covariant additif ρ_* : M⇝M_[ρ] de la catégorie'",
    "wavy arrow; formula in the running text (enlarged crop)", "\\longmapsto; displayed", "symbol", None, "high",
    r"""additif⏎\[⏎  \rho_*:M\longmapsto M_{[\rho]}⏎\]⏎de la catégorie""",
    r"""additif $\rho_*:M\leadsto M_{[\rho]}$⏎de la catégorie""",
    "Wavy arrow in the print (\\leadsto), not convention 3; GLOBAL_ISSUES item 33. The fix also sets the formula inline, as printed.")
add(176, "(7.1.3): 'la catégorie Ab_B des B-modules à gauche dans la catégorie Ab_A des A-modules'",
    "Ab bold italic (twice)", "\\mathbf{Ab}", "font", None, "high",
    r"""$\mathbf{Ab}_B$ des $B$-modules à gauche dans la catégorie⏎$\mathbf{Ab}_A$ des""",
    r"""$\boldsymbol{Ab}_B$ des $B$-modules à gauche dans la catégorie⏎$\boldsymbol{Ab}_A$ des""",
    "Bold italic Ab.")
add(176, "(7.1.3): 'un foncteur T_(B) : Ab_B →(ρ_*) Ab_A →(T) Ab, évidemment covariant'",
    "Ab bold italic; formula in the running text", "\\mathbf{Ab}; displayed", "font", None, "high",
    r"""foncteur⏎\[⏎  T_{(B)}:⏎  \mathbf{Ab}_B⏎  \xrightarrow{\rho_*}⏎  \mathbf{Ab}_A⏎  \xrightarrow{T}⏎  \mathbf{Ab},⏎\]⏎évidemment""",
    r"""foncteur $T_{(B)}:\boldsymbol{Ab}_B\xrightarrow{\rho_*}\boldsymbol{Ab}_A\xrightarrow{T}\boldsymbol{Ab}$,⏎évidemment""",
    "Bold italic Ab. The fix also sets the formula inline, as printed.")
add(176, "(7.1.3): 'par extension des scalaires de A à B'", "'extension des scalaires' italic", "upright",
    "italics", None, "high",
    r"""par extension des scalaires""", r"""par \emph{extension des scalaires}""", IT)
add(176, "(7.1.3): 'un foncteur de Ab_B dans elle-même (7.1.2)'", "Ab bold italic", "\\mathbf{Ab}", "font", None,
    "high", r"""$\mathbf{Ab}_B$ dans elle-même""", r"""$\boldsymbol{Ab}_B$ dans elle-même""", "Bold italic Ab.")
add(176, "(7.1.3): 'on voit aussitôt que T_(C) = (T_(B))_(C); il est immédiat'", "in the running text", "displayed",
    "other", None, "high",
    r"""aussitôt que⏎\[⏎  T_{(C)}=(T_{(B)})_{(C)};⏎\]⏎il est""",
    r"""aussitôt que $T_{(C)}=(T_{(B)})_{(C)}$;⏎il est""", LAY)
add(176, "(7.1.3): 'est fonctorielle et additive en T'", "'fonctorielle' and 'additive' italic", "upright",
    "italics", None, "high",
    r"""est fonctorielle et additive en""", r"""est \emph{fonctorielle} et \emph{additive} en""", IT)
add(176, "(7.1.4): 'et soit T un foncteur covariant additif A-linéaire Ab_A→Ab_A, commutant aux limites inductives.'",
    "word order 'soit T un foncteur covariant additif A-linéaire Ab_A→Ab_A, commutant ...'; Ab bold italic; 'commutant aux limites inductives' italic (enlarged crop)",
    "'soit T:Ab_A→Ab_A un foncteur covariant additif A-linéaire, commutant ...' (formula moved, all upright, \\mathbf{Ab})",
    "word", None, "high",
    r"""soit⏎$T:\mathbf{Ab}_A\to\mathbf{Ab}_A$ un foncteur covariant additif⏎$A$-linéaire, commutant aux limites inductives.""",
    r"""soit⏎$T$ un foncteur covariant additif⏎$A$-linéaire $\boldsymbol{Ab}_A\to\boldsymbol{Ab}_A$, \emph{commutant aux limites inductives}.""",
    "The TeX moves the formula next to T; the fix restores the printed order and also sets the bold italic Ab and the italic phrase.")
add(176, "(7.1.4): after the display (7.1.4.1): 'Supposons en effet d'abord'",
    "new indented paragraph after the display", "no blank line after \\]", "other", None, "high",
    r"""\tag{7.1.4.1}\label{III.7.1.4.1.fr}⏎\]⏎Supposons""",
    r"""\tag{7.1.4.1}\label{III.7.1.4.1.fr}⏎\]⏎⏎Supposons""",
    "Missing paragraph break after a display (GLOBAL_ISSUES item 47 pattern).")
add(176, "(7.1.4): 'On sait alors que M_f = lim→ M_n, où'", "in the running text", "displayed", "other", None, "high",
    r"""que⏎\[⏎  M_f=\varinjlim M_n,⏎\]⏎où""", r"""que $M_f=\varinjlim M_n$,⏎où""", LAY)
add(176, "(7.1.4): 'avec φ_nm : z⇝f^{n-m}z (0_I, 1.6.1);'",
    "wavy arrow; bold 0; formula in the running text (enlarged crop)",
    "\\longmapsto; plain 0; displayed with \\qquad", "symbol", None, "high",
    r"""avec⏎\[⏎  \varphi_{nm}:z\longmapsto f^{\,n-m}z⏎  \qquad(0_{\mathrm I}, 1.6.1);⏎\]⏎d'où""",
    r"""avec $\varphi_{nm}:z\leadsto f^{\,n-m}z$ ($\mathbf{0}_{\mathrm I}$, 1.6.1);⏎d'où""",
    "Wavy arrow in the print (\\leadsto), not convention 3; GLOBAL_ISSUES item 33. The same fix sets the bold 0 of the reference (convention 2) and the formula inline, as printed.")
add(176, "(7.1.4): 'pour f∈S (0_I, 1.4.5)'", "bold 0", "plain 0 ($0_{\\mathrm I}$)", "convention", 2, "high",
    r"""($0_{\mathrm I}$, 1.4.5)""", r"""($\mathbf{0}_{\mathrm I}$, 1.4.5)""",
    "Bold chapter number in the reference (form as GLOBAL_ISSUES item 35).")
add(176, "(7.1.4): 'un isomorphisme de S^{-1}A-modules'", "'modules' italic (enlarged crop)", "upright",
    "italics", None, "high",
    r"""$S^{-1}A$-modules, et""", r"""$S^{-1}A$-\emph{modules}, et""", IT)
add(176, "(7.1.4): after the display (7.1.4.2): 'Lorsque S = A—p'", "new indented paragraph after the display",
    "no blank line after \\]", "other", None, "high",
    r"""\tag{7.1.4.2}\label{III.7.1.4.2.fr}⏎\]⏎Lorsque""",
    r"""\tag{7.1.4.2}\label{III.7.1.4.2.fr}⏎\]⏎⏎Lorsque""",
    "Missing paragraph break after a display (GLOBAL_ISSUES item 47 pattern).")
add(176, "(7.1.4): 'Lorsque S = A—p est le complémentaire'", "long dash for the set difference (enlarged crop)",
    "minus sign", "convention", 7, "high",
    r"""$S=A-\mathfrak p$""", r"""$S=A\setmin\mathfrak p$""", "Long dash for set difference.")
add(176, "Proposition (7.1.5): 'si T_m est exact à gauche (resp. exact à droite, exact) pour tout'",
    "'(resp.' upright (enlarged crop)", "italic (proposition body)", "convention", 6, "high",
    r"""(resp. exact à droite, exact) pour""", r"""\textup{(resp.} exact à droite, exact) pour""", "")
add(176, "Proposition (7.1.5): 'T est exact à gauche (resp. exact à droite, exact).'",
    "'(resp.' upright (enlarged crop)", "italic (proposition body)", "convention", 6, "high",
    r"""(resp. exact à droite, exact).""", r"""\textup{(resp.} exact à droite, exact).""", "")
add(176, "proof of (7.1.5): '(Bourbaki, Alg. comm., chap. II, § 3, n° 3, th. 1)'",
    "n with a raised o (n°) (enlarged crop)", "no~3 (plain 'no')", "symbol", None, "high",
    r"""no~3""", r"""n\textsuperscript{o}~3""", "As fixed for ega3-1 (n\\textsuperscript{o}).")
add(176, "heading 7.2", "'7.2. Caractérisations du foncteur produit tensoriel.' (final full stop)", "no full stop",
    "punctuation", None, "high",
    r"""\subsection{Caractérisations du foncteur produit tensoriel}""",
    r"""\subsection{Caractérisations du foncteur produit tensoriel.}""",
    "Same pattern as GLOBAL_ISSUES item 43.")
add(176, "(7.2.1): 'la donnée d'un Z-homomorphisme v : N⊗_A M→P équivaut'", "in the running text", "displayed",
    "other", None, "high",
    r"""homomorphisme⏎\[⏎  v:N\otimes_A M\longrightarrow P⏎\]⏎équivaut""",
    r"""homomorphisme $v:N\otimes_A M\longrightarrow P$⏎équivaut""", LAY)
add(176, "(7.2.1): 'application Z-bilinéaire u : N×M→P telle que u(ta, x) = u(t, ax) pour a∈A, t∈N, x∈M, les deux'",
    "both formulas in the running text", "two displays ('pour' as \\text)", "other", None, "high",
    r"""bilinéaire⏎\[⏎  u:N\times M\longrightarrow P⏎\]⏎telle que⏎\[⏎  u(ta,x)=u(t,ax)⏎  \qquad\text{pour }a\in A,\ t\in N,\ x\in M,⏎\]⏎les deux""",
    r"""bilinéaire $u:N\times M\longrightarrow P$⏎telle que $u(ta,x)=u(t,ax)$ pour $a\in A$, $t\in N$, $x\in M$,⏎les deux""",
    LAY)


# ---------------- checks ----------------
def load(p):
    with open(os.path.join(RUN, "page_%d.tex" % p), "rb") as fh:
        return fh.read().decode("utf-8").replace("\r\n", "\n")


ok = True
pages = sorted({f["page"] for f in F})
for p in pages:
    text = load(p)
    fs = [f for f in F if f["page"] == p and f["fix"]]
    for f in fs:
        n = text.count(f["fix"]["old"])
        if n != 1:
            ok = False
            print("NOT UNIQUE/ABSENT p%d (%d): %r" % (p, n, f["fix"]["old"][:80]))
    for order in (fs, list(reversed(fs))):
        t = text
        for f in order:
            n = t.count(f["fix"]["old"])
            if n != 1:
                ok = False
                print("SEQUENTIAL PROBLEM p%d (%d): %r" % (p, n, f["fix"]["old"][:80]))
            t = t.replace(f["fix"]["old"], f["fix"]["new"], 1)

# segment check in the LF source files
src6 = open(os.path.join(SRC, "ega3-6-fr.tex"), encoding="utf-8").read()
src7 = open(os.path.join(SRC, "ega3-7-fr.tex"), encoding="utf-8").read()


def seg(src, a, b):
    i = src.index(a)
    j = src.index(b) if b and b in src else len(src)
    return src[i:j]


segs = {
    172: seg(src6, r"\oldpage[III]{172}", r"\oldpage[III]{173}"),
    173: seg(src6, r"\oldpage[III]{173}", r"\oldpage[III]{174}"),
    174: seg(src6, r"\oldpage[III]{174}", r"\oldpage[III]{175}"),
    175: seg(src6, r"\oldpage[III]{175}", None),
    176: seg(src7, r"\oldpage[III]{176}", r"\oldpage[III]{177}"),
}
pre7 = src7[: src7.index(r"\oldpage[III]{176}")]
for f in F:
    if not f["fix"]:
        continue
    o = f["fix"]["old"]
    s = pre7 if f["_outside"] else segs[f["page"]]
    if s.count(o) != 1:
        ok = False
        print("SOURCE SEGMENT p%d (%d): %r" % (f["page"], s.count(o), o[:80]))

for f in F:
    del f["_outside"]

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

# counts
for p in pages:
    fs = [f for f in F if f["page"] == p]
    conv = sum(1 for f in fs if f["kind"] == "convention")
    mis = sum(1 for f in fs if f["kind"] == "misprint_in_print")
    print(p, "normal", len(fs) - conv - mis, "convention", conv, "misprint", mis)
print("ALL CHECKS OK" if ok else "CHECKS FAILED")
