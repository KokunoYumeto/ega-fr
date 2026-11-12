import json
import pathlib
import sys

RUN = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2])

F = []


def add(page, where, scan, tex, kind, conf, old=None, new=None, conv=None, corrected=None, note=""):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


DOTS = "Baseline dots in the print (GLOBAL_ISSUES item 22); checked on an enlarged crop."
INLINE = "The print sets this formula in the running text (GLOBAL_ISSUES item 21)."
REPRISE = ("The print repeats the symbol at the start of the continuation line of the broken display; the TeX breaks "
           "the display at the same place but gives the symbol once. Document-wide question whether such reprises "
           "are reproduced.")
CONV7 = ("Long dash for the subtraction (GLOBAL_ISSUES 23); \\setmin as proposed for convention 7, pending that "
         "decision.")

# ---------------------------------------------------------------- boundary 166/167
add(166, "Boundary p. 166/167: 'et dont les termes E_2 sont respectivement' | display (e) at the top of p. 167",
    "the sentence runs into the display (e) on p. 167; no paragraph break", "blank line before \\oldpage[III]{167}",
    "other", "high",
    "sont respectivement\n\n", "sont respectivement\n",
    note="Spurious paragraph break before a display at a mid-sentence page break (GLOBAL_ISSUES item 20). OUTSIDE "
         "pp. 167-171: the edit lies at the end of p. 166's segment (unique in page_166.tex); not in the pp. 162-166 "
         "findings.")

# ---------------------------------------------------------------- page 167
add(167, "Prop. (6.9.3), display (e), end", "ℋ_{q''}(𝒬'_•)) with no punctuation (crop)",
    "\\Bigr),", "punctuation", "high",
    r"""\mathscr H_{q''}(\mathscr Q'_\bullet)
  \Bigr),""",
    r"""\mathscr H_{q''}(\mathscr Q'_\bullet)
  \Bigr)""")
add(167, "Prop. (6.9.3), display (f): index of ⊕ 'q_1+q_2+...+q_{m+1}=q'", "baseline dots (crop)",
    "q_2+\\cdots+q_{m+1}", "symbol", "high",
    r"""q_2+\cdots+q_{m+1}=q}
  \mathscr{T}\!or_p^{S'}""",
    r"""q_2+\ldots+q_{m+1}=q}
  \mathscr{T}\!or_p^{S'}""", note=DOTS)
add(167, "Prop. (6.9.3), display (f), start of the second line", "'..., 𝔗or_{q_m}^S(f_m, ...' (the line begins with '..., ')",
    "&\\mathfrak{Tor}_{q_m}^S", "missing", "medium",
    r"""\ldots,\\
  &\mathfrak{Tor}_{q_m}^S""",
    r"""\ldots,\\
  &\ldots,\mathfrak{Tor}_{q_m}^S""", note=REPRISE)
add(167, "Prop. (6.9.3), display (f), end", "ℋ_{q_{m+1}}(𝒬'_•)) with no punctuation (crop)",
    "\\Bigr),", "punctuation", "high",
    r"""\mathscr H_{q_{m+1}}(\mathscr Q'_\bullet)
  \Bigr),""",
    r"""\mathscr H_{q_{m+1}}(\mathscr Q'_\bullet)
  \Bigr)""")
add(167, "Prop. (6.9.3), display (f'): index of ⊕ 'q_1+...+q_m=q'", "baseline dots (crop)",
    "q_1+\\cdots+q_m", "symbol", "high",
    r"""\cdots+q_m=q}
  \mathfrak{Tor}_p^{S'}""",
    r"""\ldots+q_m=q}
  \mathfrak{Tor}_p^{S'}""", note=DOTS)
add(167, "Prop. (6.9.3), display (f'), end", "..., 𝒬'_•) with no full stop (crop)",
    "\\Bigr).", "punctuation", "high",
    r"""  \mathscr Q'_\bullet
  \Bigr).""",
    r"""  \mathscr Q'_\bullet
  \Bigr)""")
add(167, "Corollaire (6.9.4): 'des S-schémas quasi-compacts et pour chaque i, soit'",
    "no comma after 'et' (crop)", "quasi-compacts et, pour chaque", "punctuation", "high",
    "quasi-compacts et, pour chaque", "quasi-compacts et pour chaque")
add(167, "Corollaire (6.9.4), displayed abutment Tor_•^S(X^(1), ..., S'; ..., Q̃'_•)",
    "tilde over the Q only, prime and dot outside (crop)", "\\widetilde{Q'_\\bullet}", "convention", "high",
    r"""\widetilde{Q'_\bullet})
\]""",
    r"""\widetilde{Q}'_\bullet)
\]""", conv=8)
add(167, "Corollaire (6.9.4), display (e), end", "H_{q''}(Q'_•)) with no punctuation (crop)",
    "\\Bigr),", "punctuation", "high",
    r"""&H_{q''}(Q'_\bullet)
  \Bigr),""",
    r"""&H_{q''}(Q'_\bullet)
  \Bigr)""")
add(167, "Corollaire (6.9.4), display (f): index of ⊕ 'q_1+q_2+...+q_{m+1}=q'", "baseline dots",
    "q_2+\\cdots+q_{m+1}", "symbol", "high",
    r"""q_2+\cdots+q_{m+1}=q}
  \operatorname{Tor}_p^{A'}""",
    r"""q_2+\ldots+q_{m+1}=q}
  \operatorname{Tor}_p^{A'}""", note=DOTS)
add(167, "Corollaire (6.9.4), display (f), start of the second line", "'..., Tor_{q_m}^S(X^(m), ...' (the line begins with '..., ')",
    "&\\mathbf{Tor}_{q_m}^S", "missing", "medium",
    r"""\ldots,\\
  &\mathbf{Tor}_{q_m}^S""",
    r"""\ldots,\\
  &\ldots,\mathbf{Tor}_{q_m}^S""", note=REPRISE)
add(167, "Corollaire (6.9.4), display (f), end", "H_{q_{m+1}}(Q'_•)) with no punctuation (crop)",
    "\\Bigr),", "punctuation", "high",
    r"""  H_{q_{m+1}}(Q'_\bullet)
  \Bigr),""",
    r"""  H_{q_{m+1}}(Q'_\bullet)
  \Bigr)""")
add(167, "Corollaire (6.9.4), display (f'): index of ⊕", "'q_1 + ... q_m = q': no + before q_m, baseline dots (2.5x crop)",
    "q_1+\\cdots+q_m=q", "misprint_in_print", "high",
    r"""\bigoplus_{q_1+\cdots+q_m=q}
  \mathbf{Tor}_p^{S'}""",
    r"""\bigoplus_{q_1+\ldots q_m=q}
  \mathbf{Tor}_p^{S'}""", corrected=r"\bigoplus_{q_1+\ldots+q_m=q}",
    note="The print drops the + before q_m (the same index in (6.9.3) (f') has it). The TeX silently corrects; the fix "
         "restores the printed reading and also sets the baseline dots (\\ldots, GLOBAL_ISSUES 22).")
add(167, "Corollaire (6.9.4), display (f'), last argument Q̃'_•", "tilde over the Q only (crop)",
    "\\widetilde{Q'_\\bullet}", "convention", "high",
    r"""\widetilde{Q'_\bullet}
  \Bigr).""",
    r"""\widetilde{Q}'_\bullet
  \Bigr).""", conv=8)
add(167, "Proof of (6.9.4): 'un recouvrement ouvert affine fini U^(i) de X^(i), et, si u_i : ...'",
    "comma after X^(i) (crop)", "de $X^{(i)}$ et, si", "punctuation", "high",
    r"de $X^{(i)}$ et, si", r"de $X^{(i)}$, et, si")
add(167, "Proof of (6.9.4): '... = u_i^{-1}(U^(i)). En vertu de (6.6.6)'",
    "'En vertu de' starts flush left after a full line: same paragraph", "blank line before 'En vertu de'",
    "other", "high",
    r"""(\mathfrak U^{(i)})$.

En vertu""",
    r"""(\mathfrak U^{(i)})$.
En vertu""", note="No paragraph break in the print.")
add(167, "Proof of (6.9.4): 'En vertu de (6.6.6), Tor_•^S(X^(1), ..., X^(m), S'; P^(1), ..., P^(m), Q̃'_•) s'obtient'",
    "the heavy hypertor glyph of the 𝔗or(f_1, ...) of (6.9.3), not the bold Tor of the statement (crop)",
    "\\mathbf{Tor}_\\bullet^S", "misprint_in_print", "high",
    r"""(6.6.6),
$\mathbf{Tor}_\bullet^S""",
    r"""(6.6.6),
$\mathfrak{Tor}_\bullet^S""", corrected=r"\mathbf{Tor}_\bullet^S",
    note="Wrong symbol in the print: with schemes X^(i) as arguments the module hypertor is bold Tor (as in the "
         "statement's display and in (6.6.6)); the sheaf glyph belongs to the Tor of morphisms. The TeX silently "
         "corrects; the fix restores the printed glyph in the TeX's own form for it (\\mathfrak{Tor}).")
add(167, "Proof of (6.9.4), same formula: Q̃'_•", "tilde over the Q only (crop)", "\\widetilde{Q'_\\bullet}",
    "convention", "high",
    r"\widetilde{Q'_\bullet})$ s'obtient", r"\widetilde{Q}'_\bullet)$ s'obtient", conv=8)
add(167, "Proof of (6.9.4): '(au sens de (0, 11.7.1))'", "bold 0 (crop)", "(0, 11.7.1)", "convention", "high",
    "(au sens de (0, 11.7.1))", r"(au sens de (\textbf{0}, 11.7.1))", conv=2)
add(167, "Proof of (6.9.4): 'le tricomplexe M... = M^(1)... ⊗_A M^(2)... ⊗ ... ⊗_A M^(m)... ⊗_A Q'.'",
    "'M^(2)_••• ⊗ . . . ⊗_A': no subscript A on the ⊗ after M^(2); baseline dots (4x crop)",
    "M^{(2)}\\otimes_A\\cdots\\otimes_A", "formula", "high",
    r"""tricomplexe
\[
  M_{\bullet\bullet\bullet}
  =M_{\bullet\bullet\bullet}^{(1)}\otimes_A
   M_{\bullet\bullet\bullet}^{(2)}\otimes_A\cdots\otimes_A
   M_{\bullet\bullet\bullet}^{(m)}\otimes_A Q'_\bullet
\]
(où""",
    r"""tricomplexe
$M_{\bullet\bullet\bullet}
=M_{\bullet\bullet\bullet}^{(1)}\otimes_A
M_{\bullet\bullet\bullet}^{(2)}\otimes\ldots\otimes_A
M_{\bullet\bullet\bullet}^{(m)}\otimes_A Q'_\bullet$
(où""",
    note="One edit for three differences: the bare ⊗ after M^(2), the baseline dots, and the inline setting (next finding).")
add(167, "Same formula (tricomplexe M...)", "in the running text", "displayed with \\[ \\]", "other", "high",
    note=INLINE + " Covered by the edit of the preceding finding.")
add(167, "Proof of (6.9.4): 'on a (...) M... = M'^(1)... ⊗_A' M'^(2)... ⊗ ... ⊗_A' M'^(m)... ⊗_A' Q'.. Or,'",
    "'M'^(2)_••• ⊗ . . . ⊗_{A'}': no subscript on the ⊗ after M'^(2); baseline dots (crop)",
    "M'^{(2)}\\otimes_{A'}\\cdots\\otimes_{A'}", "formula", "high",
    r"""$A'$-modules)
\[
  M_{\bullet\bullet\bullet}
  =M_{\bullet\bullet\bullet}'^{(1)}\otimes_{A'}
   M_{\bullet\bullet\bullet}'^{(2)}\otimes_{A'}\cdots\otimes_{A'}
   M_{\bullet\bullet\bullet}'^{(m)}\otimes_{A'} Q'_\bullet.
\]
Or,""",
    r"""$A'$-modules)
$M_{\bullet\bullet\bullet}
=M_{\bullet\bullet\bullet}'^{(1)}\otimes_{A'}
M_{\bullet\bullet\bullet}'^{(2)}\otimes\ldots\otimes_{A'}
M_{\bullet\bullet\bullet}'^{(m)}\otimes_{A'} Q'_\bullet$.
Or,""",
    note="One edit for three differences: the bare ⊗ after M'^(2), the baseline dots, and the inline setting (next finding).")
add(167, "Same formula (M... = M'^(1)... ⊗ ...)", "in the running text", "displayed with \\[ \\]", "other", "high",
    note=INLINE + " Covered by the edit of the preceding finding.")
add(167, "Proof of (6.9.4): 'formé de A'-modules projectifs;'", "'projectifs' italic (crop)", "projectifs upright",
    "italics", "high", r"$A'$-modules projectifs;", r"$A'$-modules \emph{projectifs};")
add(167, "Proof of (6.9.4): 'est aussi égal à Tor_•^{A'}(M'^(1)..., ..., M'^(m)..., Q'.); c'est donc'",
    "bold Tor (crop), formula in the running text", "\\operatorname{Tor}_\\bullet^{A'} in a display", "font", "high",
    r"""égal à
\[
  \operatorname{Tor}_\bullet^{A'}
  (M_{\bullet\bullet\bullet}'^{(1)},\ldots,
   M_{\bullet\bullet\bullet}'^{(m)},Q'_\bullet);
\]
c'est donc""",
    r"""égal à
$\mathbf{Tor}_\bullet^{A'}
(M_{\bullet\bullet\bullet}'^{(1)},\ldots,
M_{\bullet\bullet\bullet}'^{(m)},Q'_\bullet)$;
c'est donc""",
    note="One edit for the bold Tor and the inline setting (next finding).")
add(167, "Same formula (Tor_•^{A'}(M'^(1)..., ...))", "in the running text", "displayed with \\[ \\]", "other", "high",
    note=INLINE + " Covered by the edit of the preceding finding.")
add(167, "Last display E^2_pq: index of ⊕ 'q_1+...+q_{m+1}=q'", "baseline dots (crop)", "q_1+\\cdots+q_{m+1}",
    "symbol", "high", r"\bigoplus_{q_1+\cdots+q_{m+1}=q}", r"\bigoplus_{q_1+\ldots+q_{m+1}=q}", note=DOTS)
add(167, "Last display E^2_pq = ⊕ Tor_p^{A'}(H_{q_1}(M^(1)...), ..., H_{q_m}(M'^(m)...), ...)",
    "H_{q_1}(M^(1)_•••) without the prime; H_{q_m}(M'^(m)_•••) has it (crop)", "H_{q_1}(M'^{(1)})",
    "misprint_in_print", "high",
    r"(H_{q_1}(M_{\bullet\bullet\bullet}'^{(1)})", r"(H_{q_1}(M_{\bullet\bullet\bullet}^{(1)})",
    corrected=r"H_{q_1}(M_{\bullet\bullet\bullet}'^{(1)})",
    note="Missing prime in the print (the Tor^{A'} is of the M'^(i)). The TeX silently corrects; the fix restores "
         "the printed reading.")
add(167, "All 𝔗or on pp. 167-171 (first here: (6.9.3) (e) 𝔗or_{q'}^S(f_1, ..., f_m; ...))",
    "heavy roundhand T with bold italic 'or' (the glyph of the hypertor local of (6.4.1.1), p. 146)",
    "\\mathfrak{Tor} (Fraktur)", "font", "high",
    note="Document-wide, no page fix: ega3-6 writes this glyph \\mathfrak{Tor} (55 times), while the p. 146 checker "
         "proposed \\boldsymbol{\\mathscr{T}\\!or} for the same glyph in (6.4.1.1). One macro decision for the heavy "
         "hypertor glyph; on these pages: p. 167 4 (+1 from the misprint fix), p. 168 1, p. 169 13, p. 170 2, "
         "p. 171 1 (+3 from the fixes below).")

# ---------------------------------------------------------------- page 168
add(168, "'On a d'ailleurs H_{q_i}(M'^(i)...) = H_{q_i}(M^(i)... ⊗_A A') = Tor^S_{q_i}(X^(i), S'; P^(i), O_S') en vertu'",
    "in the running text", "displayed with \\[ \\]", "other", "high",
    r"""On a d'ailleurs
\[
  H_{q_i}(M_{\bullet\bullet\bullet}'^{(i)})
  =H_{q_i}(M_{\bullet\bullet\bullet}^{(i)}\otimes_A A')
  =\mathbf{Tor}_{q_i}^S
  (X^{(i)},S';\mathscr P_\bullet^{(i)},\mathscr O_{S'})
\]
en vertu""",
    r"""On a d'ailleurs
$H_{q_i}(M_{\bullet\bullet\bullet}'^{(i)})
=H_{q_i}(M_{\bullet\bullet\bullet}^{(i)}\otimes_A A')
=\mathbf{Tor}_{q_i}^S
(X^{(i)},S';\mathscr P_\bullet^{(i)},\mathscr O_{S'})$
en vertu""", note=INLINE)
add(168, "'sont des A'-modules projectifs, la théorie'", "'projectifs' italic (crop)", "upright", "italics", "high",
    r"$A'$-modules projectifs, la", r"$A'$-modules \emph{projectifs}, la")
add(168, "'l'homologie du bicomplexe M'^(1)... ⊗_A' M'^(2)... ⊗ ... ⊗_A' M'^(m)... ⊗_A' Q'. est canoniquement'",
    "'M'^(2)_••• ⊗ . . . ⊗_{A'}': no subscript on the ⊗ after M'^(2); baseline dots (crop)",
    "M'^{(2)}\\otimes_{A'}\\cdots\\otimes_{A'}", "formula", "high",
    r"""du bicomplexe
\[
  M_{\bullet\bullet\bullet}'^{(1)}\otimes_{A'}
  M_{\bullet\bullet\bullet}'^{(2)}\otimes_{A'}\cdots\otimes_{A'}
  M_{\bullet\bullet\bullet}'^{(m)}\otimes_{A'} Q'_\bullet
\]
est canoniquement""",
    r"""du bicomplexe
$M_{\bullet\bullet\bullet}'^{(1)}\otimes_{A'}
M_{\bullet\bullet\bullet}'^{(2)}\otimes\ldots\otimes_{A'}
M_{\bullet\bullet\bullet}'^{(m)}\otimes_{A'} Q'_\bullet$
est canoniquement""",
    note="One edit for three differences: the bare ⊗ after M'^(2), the baseline dots, and the inline setting (next finding).")
add(168, "Same formula (the bicomplex)", "in the running text", "displayed with \\[ \\]", "other", "high",
    note=INLINE + " Covered by the edit of the preceding finding.")
add(168, "'isomorphe à son hyperhomologie (0, 11.6.5)'", "'hyperhomologie' italic (crop)", "upright", "italics", "high",
    "son hyperhomologie", r"son \emph{hyperhomologie}")
add(168, "'(0, 11.6.5)'", "bold 0 (crop)", "(0, 11.6.5)", "convention", "high",
    "(0, 11.6.5)", r"(\textbf{0}, 11.6.5)", conv=2)
add(168, "First display E^2_pq = ⊕ Tor_p^{A'}(H^II_{q_1}(M'^(1)...), ..., H^II_{q_{m+1}}(Q'.))",
    "bold Tor (crop)", "\\operatorname{Tor}_p^{A'}", "font", "high",
    r"""\bigoplus_{q_1+\cdots+q_{m+1}=q}
  \operatorname{Tor}_p^{A'}""",
    r"""\bigoplus_{q_1+\ldots+q_{m+1}=q}
  \mathbf{Tor}_p^{A'}""",
    note="One edit for the bold Tor and the baseline dots of the index (next finding).")
add(168, "Same display: index 'q_1+...+q_{m+1}=q'", "baseline dots", "\\cdots", "symbol", "high",
    note=DOTS + " Covered by the edit of the preceding finding.")
add(168, "'Or, comme le second degré de Q'. se réduit à 0'", "new indented paragraph after the display (crop)",
    "no blank line after \\]", "other", "high",
    "\\]\nOr, comme", "\\]\n\nOr, comme", note="Paragraph break after the display, as printed.")
add(168, "Second display E^2_pq = ⊕_{q_1+...+q_m=q} Tor_p^{A'}(..., Q'.)", "bold Tor (crop)",
    "\\operatorname{Tor}_p^{A'}", "font", "high",
    r"""\bigoplus_{q_1+\cdots+q_m=q}
  \operatorname{Tor}_p^{A'}""",
    r"""\bigoplus_{q_1+\ldots+q_m=q}
  \mathbf{Tor}_p^{A'}""",
    note="One edit for the bold Tor and the baseline dots of the index (next finding).")
add(168, "Same display: index 'q_1+...+q_m=q'", "baseline dots", "\\cdots", "symbol", "high",
    note=DOTS + " Covered by the edit of the preceding finding.")
add(168, "'En outre, on a ...' after the second display", "new indented paragraph (crop)",
    "no blank line after \\]", "other", "high",
    r"""),Q'_\bullet).
\]
""",
    r"""),Q'_\bullet).
\]

""", note="Paragraph break after the display, as printed.")
add(168, "'En outre, on a H^II_{q_i}(M'^(i)...) = H^II_{q_i}(M^(i)... ⊗_A A') = Tor^A_{q_i}(L^(i).., A') en vertu de (6.3.4)'",
    "in the running text", "displayed with \\[ \\]", "other", "high",
    r"""on a
\[
  H_{q_i}^{\mathrm{II}}(M_{\bullet\bullet\bullet}'^{(i)})
  =H_{q_i}^{\mathrm{II}}(M_{\bullet\bullet\bullet}^{(i)}\otimes_A A')
  =\operatorname{Tor}_{q_i}^A(L_{\bullet\bullet}^{(i)},A')
\]
en vertu de (6.3.4)""",
    r"""on a
$H_{q_i}^{\mathrm{II}}(M_{\bullet\bullet\bullet}'^{(i)})
=H_{q_i}^{\mathrm{II}}(M_{\bullet\bullet\bullet}^{(i)}\otimes_A A')
=\operatorname{Tor}_{q_i}^A(L_{\bullet\bullet}^{(i)},A')$
en vertu de (6.3.4)""", note=INLINE + " The Tor here is roman in the print, as in the TeX.")
add(168, "'V' est affine dans X'^(i), et il résulte de (6.4.1.1)'", "comma after X'^(i) (crop)",
    "$X'^{(i)}$ et il", "punctuation", "high",
    r"$X'^{(i)}$ et il résulte", r"$X'^{(i)}$, et il résulte")
add(168, "Display C^•(U'^(i), Tor^S_{q_i}(P^(i), O_S')), end", "no comma (crop)", "\\bigr),", "punctuation", "high",
    r"""\mathscr O_{S'})\bigr),
\]""",
    r"""\mathscr O_{S'})\bigr)
\]""")
add(168, "Remarque (6.9.5): 'qui leur sont respectivement homotopes'", "'homotopes' italic in the roman remark (crop)",
    "no \\emph", "italics", "high", "respectivement homotopes", r"respectivement \emph{homotopes}")
add(168, "Remarque (6.9.5): '(f)E(f_1, ..., f_m; P..., Q'.) ⥲ (f)E(f_1, ..., f_m : R^(1)., ..., R^(m)., T'.);'",
    "colon after f_m in the second E (crop)", "f_m;", "misprint_in_print", "high",
    r"""spectrales
\[
\begin{split}
  {}^{(f)}\mathscr E
  (f_1,\ldots,f_m;
   \mathscr P_\bullet^{(1)},\ldots,\mathscr P_\bullet^{(m)},
   \mathscr Q'_\bullet)
  \xrightarrow{\sim}\;&
  {}^{(f)}\mathscr E
  (f_1,\ldots,f_m;\\
  &\mathscr R_\bullet^{(1)},\ldots,\mathscr R_\bullet^{(m)},
   \mathscr T'_\bullet);
\end{split}
\]
la démonstration""",
    r"""spectrales
${}^{(f)}\mathscr E
(f_1,\ldots,f_m;
\mathscr P_\bullet^{(1)},\ldots,\mathscr P_\bullet^{(m)},
\mathscr Q'_\bullet)
\xrightarrow{\sim}
{}^{(f)}\mathscr E
(f_1,\ldots,f_m:
\mathscr R_\bullet^{(1)},\ldots,\mathscr R_\bullet^{(m)},
\mathscr T'_\bullet)$;
la démonstration""", corrected=r"(f_1,\ldots,f_m;\mathscr R_\bullet^{(1)},",
    note="Colon for semicolon in the print. The TeX silently corrects. One edit restores the colon and sets the "
         "formula inline (next finding); for the corrected edition apply the same edit with ';' for ':'.")
add(168, "Same formula (isomorphism of spectral sequences)", "in the running text", "displayed (split)", "other", "high",
    note=INLINE + " Covered by the edit of the preceding finding.")
add(168, "Corollaire (6.9.6): 'Sous les conditions de (6.9.1), supposons que :'",
    "(6.9.1) upright inside the italic statement (crop)", "italic", "convention", "high",
    "Sous les conditions de (6.9.1), supposons que", r"Sous les conditions de \textup{(6.9.1)}, supposons que", conv=6)

# ---------------------------------------------------------------- page 169
add(169, "(6.9.6.1), second line: '... ⊗_S ℋ_{n''}(𝒬'.).'", "⊗ with subscript S only (crop); (6.9.6.5) has ⊗_{𝒪_S}",
    "\\otimes_{\\mathscr O_S}", "formula", "high",
    r"\otimes_{\mathscr O_S}\mathscr H_{n''}(\mathscr Q'_\bullet).", r"\otimes_S\mathscr H_{n''}(\mathscr Q'_\bullet).",
    note="Printed reading; ⊗_S is also EGA's external tensor product notation, so not recorded as a misprint.")
add(169, "(6.9.6.1), start of the second line", "'⥲ ⊕_{n'+n''=n} ...' (the line begins with the arrow again)",
    "&\\qquad \\bigoplus", "missing", "medium",
    r"""\xrightarrow{\sim}\\
  &\qquad
  \bigoplus_{n'+n''=n}""",
    r"""\xrightarrow{\sim}\\
  &\qquad\xrightarrow{\sim}
  \bigoplus_{n'+n''=n}""", note=REPRISE)
add(169, "Proof of (6.9.6): 'les complexes Tor^S_{q_i}(P^(i)., O_S') sont nuls pour q ≠ 0 (6.5.8)'",
    "q ≠ 0, without the index i (crop)", "q_i\\ne0", "misprint_in_print", "high",
    r"pour $q_i\ne0$ (6.5.8)", r"pour $q\ne0$ (6.5.8)", corrected=r"$q_i\ne0$",
    note="The index of the Tor is q_i. The TeX silently corrects; the fix restores the printed reading.")
add(169, "(6.9.6.4), end of the first line", "'... → (f')ℰ^2_{n0} =' (the second line begins with '=' again)",
    "{}^{(f')}\\mathscr E_{n0}^2\\\\", "missing", "medium",
    r"{}^{(f')}\mathscr E_{n0}^2\\", r"{}^{(f')}\mathscr E_{n0}^2=\\", note=REPRISE)
add(169, "'est bijectif (0, 11.1.6). L'hypothèse de platitude'", "bold 0 (crop)", "(0, 11.1.6)", "convention", "high",
    "(0, 11.1.6). L'hypothèse", r"(\textbf{0}, 11.1.6). L'hypothèse", conv=2)
add(169, "(6.9.6.5), end of the first line", "'... → (e)ℰ^2_{0n} =' (the second line begins with '=' again)",
    "{}^{(e)}\\mathscr E_{0n}^2\\\\", "missing", "medium",
    r"{}^{(e)}\mathscr E_{0n}^2\\", r"{}^{(e)}\mathscr E_{0n}^2=\\", note=REPRISE)
add(169, "'est bijectif (0, 11.1.6); d'où, en combinant'", "bold 0", "(0, 11.1.6)", "convention", "high",
    "(0, 11.1.6); d'où", r"(\textbf{0}, 11.1.6); d'où", conv=2)
add(169, "Corollaire (6.9.7): 'Sous les conditions de (6.9.1), supposons S et S' affines'",
    "(6.9.1) upright inside the italic statement (crop)", "italic", "convention", "high",
    "Sous les conditions de (6.9.1), supposons", r"Sous les conditions de \textup{(6.9.1)}, supposons", conv=6)
add(169, "Corollaire (6.9.7): 'des isomorphismes canoniques (6.9.6.3) pour n ≤ n_0'",
    "(6.9.6.3) upright inside the italic statement (crop)", "italic", "convention", "high",
    "(6.9.6.3) pour $n", r"\textup{(6.9.6.3)} pour $n", conv=6)
add(169, "Corollaire (6.9.7): conditions 1°, 2°, 3°", "run in the statement's paragraph ('suivantes : 1° ...; 2° ...; 3° ...')",
    "enumerate list", "other", "medium",
    r"""suivantes :
\begin{enumerate}
  \item[$1^\circ$] $\mathscr P_k^{(i)}=0$ pour $k<d_i$;
  \item[$2^\circ$] $\mathscr P_k^{(i)}$ est plat sur $S$ pour $k<n_0+N$;
  \item[$3^\circ$]
  $\mathfrak{Tor}_q^S(f_1,\ldots,f_m;
  \mathscr P_\bullet^{(1)},\ldots,\mathscr P_\bullet^{(m)})$ est plat sur
  $S$ pour $q<n_0+N$.
\end{enumerate}""",
    r"""suivantes :
$1^\circ$ $\mathscr P_k^{(i)}=0$ pour $k<d_i$;
$2^\circ$ $\mathscr P_k^{(i)}$ est plat sur $S$ pour $k<n_0+N$;
$3^\circ$
$\mathfrak{Tor}_q^S(f_1,\ldots,f_m;
\mathscr P_\bullet^{(1)},\ldots,\mathscr P_\bullet^{(m)})$ est plat sur
$S$ pour $q<n_0+N$.""",
    note="Layout: the print runs the three conditions in (3° does not start an indented line); words and formulas agree. "
         "In (6.9.6), p. 168, the print does set 1° and 2° as separate paragraphs.")
add(169, "(6.9.7.1), end", "no full stop: the sentence continues on p. 170 ('calculons (6.9.7.1) par la méthode ...')",
    "\\Bigr).", "punctuation", "high", r"\Bigr).", r"\Bigr)")
add(169, "Boundary p. 169/170: after (6.9.7.1), before \\oldpage[III]{170}",
    "p. 170 begins 'par la méthode de (6.6.2)' flush left, mid-sentence", "blank line before the marker", "other", "high",
    r"""\label{III.6.9.7.1.fr}
\]

""",
    r"""\label{III.6.9.7.1.fr}
\]
""", note="Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). The edit lies in p. 169's "
           "segment (end of page_169.tex); there is no blank line after \\oldpage[III]{170}.")

# ---------------------------------------------------------------- page 170
add(170, "'sont nuls pour j < —N_i'", "long dash (crop)", "$j<-N_i$", "convention", "medium",
    r"$j<-N_i$", r"$j<\setmin N_i$", conv=7, note=CONV7)
add(170, "'pour tous les degrés < r + Σ_{j≠i} d_j — Σ_{i=1}^m N_i, donc'", "in the running text (crop)",
    "displayed with \\[ \\]", "other", "high",
    r"""degrés
\[
  <r+\sum_{j\ne i}d_j-\sum_{i=1}^m N_i,
\]
donc""",
    r"""degrés
$<r+\sum_{j\ne i}d_j-\sum_{i=1}^m N_i$,
donc""", note=INLINE + " Keeps the minus sign: the long dash is the next finding (apply this edit first).")
add(170, "Same formula: 'd_j — Σ N_i'", "long dash (crop)", "d_j-\\sum", "convention", "medium",
    r"d_j-\sum_{i=1}^m N_i", r"d_j\setmin\sum_{i=1}^m N_i", conv=7,
    note=CONV7 + " Its old text lies inside the preceding edit's old text; it still matches once after that edit.")
add(170, "'donc (6.9.7.1) est nul pour p < r — N, en désignant'", "long dash (crop)", "$p<r-N$", "convention", "medium",
    r"pour $p<r-N$, en", r"pour $p<r\setmin N$, en", conv=7, note=CONV7)
add(170, "'le plus grand des nombres Σ_{i=1}^m N_i — Σ_{j≠i} d_j. On en conclut'", "in the running text (crop)",
    "displayed with \\[ \\]", "other", "high",
    r"""nombres
\[
  \sum_{i=1}^m N_i-\sum_{j\ne i}d_j.
\]
On en""",
    r"""nombres
$\sum_{i=1}^m N_i-\sum_{j\ne i}d_j$.
On en""", note=INLINE + " Keeps the minus sign: the long dash is the next finding (apply this edit first).")
add(170, "Same formula: 'N_i — Σ d_j'", "long dash (crop)", "N_i-\\sum", "convention", "medium",
    r"N_i-\sum_{j\ne i}d_j", r"N_i\setmin\sum_{j\ne i}d_j", conv=7,
    note=CONV7 + " Its old text lies inside the preceding edit's old text; it still matches once after that edit.")
add(170, "'pour q ≠ 0 et p < r — N; comme d'autre part'", "long dash (crop)", "$p<r-N$", "convention", "medium",
    r"$p<r-N$; comme", r"$p<r\setmin N$; comme", conv=7, note=CONV7)
add(170, "'est bijectif pour n < r — N (M, XV, 5.6)'", "long dash (crop)", "$n<r-N$", "convention", "medium",
    r"$n<r-N$", r"$n<r\setmin N$", conv=7, note=CONV7)
add(170, "'En second lieu, si Tor^S_q(f_1, ..., f_m; P^(1)., ..., P^(m).) est plat sur S'", "in the running text",
    "displayed with \\[ \\]", "other", "high",
    r"""si
\[
  \mathfrak{Tor}_q^S
  (f_1,\ldots,f_m;
   \mathscr P_\bullet^{(1)},\ldots,\mathscr P_\bullet^{(m)})
\]
est plat""",
    r"""si
$\mathfrak{Tor}_q^S
(f_1,\ldots,f_m;
\mathscr P_\bullet^{(1)},\ldots,\mathscr P_\bullet^{(m)})$
est plat""", note=INLINE)
add(170, "Prop. (6.9.8): between (6.9.8.1) and (6.9.8.2)", "the two displays follow each other with no word between them (crop)",
    "'et' between the displays", "extra", "high",
    "\\]\net\n\\[", "\\]\n\\[")
add(170, "Proof of (6.9.8): 'pour tout O_Y-Module quasi-cohérent et Y-plat F'", "'plat' italic (crop)", "upright",
    "italics", "high", r"$Y$-plat $\mathscr F$", r"$Y$-\emph{plat} $\mathscr F$")
add(170, "Proof of (6.9.8): 'formé de O_X-Modules Y-plats)'", "'plats' italic (crop)", "upright", "italics", "high",
    r"$Y$-plats)", r"$Y$-\emph{plats})")
add(170, "Corollaire (6.9.9): 'Sous les conditions de (6.9.8), supposons'", "(6.9.8) upright inside the italic statement",
    "italic", "convention", "high",
    "Sous les conditions de (6.9.8), supposons", r"Sous les conditions de \textup{(6.9.8)}, supposons", conv=6)
add(170, "Hypercohomology ℋ on pp. 170-171 (first here: (6.9.8.1) ℋ^{-q}(f, 𝒫.))",
    "the second, lighter roundhand H of hypercohomology (crop), unlike the homology ℋ_q, ℋ_• (pp. 167-169, (6.10.1.1))",
    "\\mathscr H for both", "font", "high",
    note="Document-wide (GLOBAL_ISSUES item 42), no page fix. On these pages: (6.9.8.1)-(6.9.8.4), ℋ^•(f, 𝒫.⊗_Y ℱ), "
         "Cor. (6.9.9) ℋ^n(f, 𝒫.), (6.9.9.1), (6.9.9.2), Cor. (6.9.10) and (6.9.10.1).")

# ---------------------------------------------------------------- page 171
add(171, "After (6.9.9.2): 'C'est le cas particulier m = 1 de (6.9.6). Plus particulièrement :'",
    "roman (crop): comment after the statement, not part of it", "inside the corollary environment: italic",
    "convention", "high",
    "C'est le cas particulier $m=1$ de (6.9.6). Plus particulièrement :",
    r"\textup{C'est le cas particulier $m=1$ de (6.9.6). Plus particulièrement :}", conv=6,
    note="Alternatively end the corollary environment before this sentence (the print continues flush left, no indent).")
add(171, "Corollaire (6.9.10): 'les fibres X ⊗_S k(s), ...'", "bold italic k (crop)", "k(s)", "convention", "high",
    r"$X\otimes_S k(s)$", r"$X\otimes_S \boldsymbol{k}(s)$", conv=1)
add(171, "Corollaire (6.9.10): '..., Y ⊗_S k(s)'", "bold italic k (crop)", "k(s)", "convention", "high",
    r"$Y\otimes_S k(s)$", r"$Y\otimes_S \boldsymbol{k}(s)$", conv=1)
add(171, "Corollaire (6.9.10): 'le complexe P. ⊗_{O_S} k(s) de O_{X_s}-Modules'", "bold italic k (crop)", "k(s)",
    "convention", "high", r"\otimes_{\mathscr O_S}k(s)$ de", r"\otimes_{\mathscr O_S}\boldsymbol{k}(s)$ de", conv=1)
add(171, "(6.9.10.1): '... ⊗_{O_S} k(s).'", "bold italic k (crop)", "k(s)", "convention", "high",
    r"\otimes_{\mathscr O_S}k(s).", r"\otimes_{\mathscr O_S}\boldsymbol{k}(s).", conv=1)
add(171, "'la formation des foncteurs dérivés R^n f_*(F)'", "upright roman R (crop)", "$R^nf_*$ (italic R)", "font",
    "medium", r"$R^nf_*(\mathscr F)$", r"$\mathrm R^nf_*(\mathscr F)$",
    note="ega3-6 elsewhere writes \\mathrm R^n f_*; see also GLOBAL_ISSUES item 17.")
add(171, "Prop. (6.10.1): 'une famille finie de S-schémas affines, plats sur S'", "'plats' roman inside the italic statement (crop)",
    "italic", "convention", "high", "affines, plats\nsur", "affines, \\textup{plats}\nsur", conv=6)
add(171, "Prop. (6.10.1): 'de O_Y-Modules quasi-cohérents et plats sur S'", "'plats' roman inside the italic statement (crop)",
    "italic", "convention", "high", "et plats sur\n$S$, ayant", "et \\textup{plats} sur\n$S$, ayant", conv=6)
add(171, "(6.10.1.1), left side", "heavy hypertor glyph 𝔗or^S_•(f_1, ..., f_n, 1_S'; ...) (crop), as for the Tor of morphisms",
    "\\mathbf{Tor}_\\bullet^S (bold Tor of modules)", "symbol", "high",
    r"""\mathbf{Tor}_\bullet^S
  (f_1""",
    r"""\mathfrak{Tor}_\bullet^S
  (f_1""", note="The TeX's form for this glyph is \\mathfrak{Tor} (see the document-wide entry on p. 167).")
add(171, "(6.10.1.2), top left entry", "heavy hypertor glyph 𝔗or (crop)", "\\mathbf{Tor}_\\bullet^S", "symbol", "high",
    r"""\mathbf{Tor}_\bullet^S
    (f_1,\ldots,f_n,1_{S'};""",
    r"""\mathfrak{Tor}_\bullet^S
    (f_1,\ldots,f_n,1_{S'};""")
add(171, "(6.10.1.2), bottom left entry", "heavy hypertor glyph 𝔗or (crop)", "\\mathbf{Tor}_\\bullet^S", "symbol", "high",
    r"""\mathbf{Tor}_\bullet^S
    (f_1,\ldots,f_n,1_{S''};""",
    r"""\mathfrak{Tor}_\bullet^S
    (f_1,\ldots,f_n,1_{S''};""")
add(171, "Prop. (6.10.1): 'définis dans (6.7.10)) est commutatif'", "(6.7.10) upright inside the italic statement (crop)",
    "italic", "convention", "high", "définis dans (6.7.10))", r"définis dans \textup{(6.7.10)})", conv=6)

# ---------------------------------------------------------------- checks
ok = True
pages = {}
for p in sorted({d["page"] for d in F}):
    pages[p] = (RUN / f"page_{p}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
for d in F:
    if d["fix"]:
        n = pages[d["page"]].count(d["fix"]["old"])
        if n != 1:
            ok = False
            print("NOT UNIQUE", d["page"], n, repr(d["fix"]["old"][:80]))
# sequential application in list order
for p, text in pages.items():
    t = text
    for d in F:
        if d["page"] != p or not d["fix"]:
            continue
        n = t.count(d["fix"]["old"])
        if n != 1:
            ok = False
            print("SEQUENTIAL FAIL", p, n, repr(d["fix"]["old"][:80]))
            continue
        t = t.replace(d["fix"]["old"], d["fix"]["new"], 1)
from collections import Counter
cnt = Counter()
for d in F:
    k = "convention" if d["kind"] == "convention" else ("misprint" if d["kind"] == "misprint_in_print" else "normal")
    cnt[(d["page"], k)] += 1
for p in sorted(pages):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("total", len(F), "checks ok" if ok else "CHECKS FAILED")
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("written", OUT)
