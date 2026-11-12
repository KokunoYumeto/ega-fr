# Builds findings_040_044.json for run_0III (EGA 0_III pp. 40-44).
# "¶" in the strings below stands for a line break (LF) of the TeX file.
import json, re, sys, random

RUN = r"user\Documents\ega_scan_check_20261101\run_0III"
SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\source\ega3\ega3-1-fr.tex"
OUT = RUN + r"\findings_040_044.json"

def nl(s):
    return None if s is None else s.replace("¶", "\n")

F = []
def add(page, where, scan, tex, kind, old, new, conf="high", conv=None, note="", corrected=None, outside=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": nl(old), "new": nl(new)},
         "note": note}
    if corrected is not None:
        d["corrected"] = corrected
    d["_outside"] = outside
    F.append(d)

# ---------------- page 40 ----------------
add(40, "(11.6.2), line 1", "un *foncteur covariant additif* de C", "un foncteur covariant additif de (upright)", "italics",
    r"soit un foncteur covariant additif de", r"soit un \emph{foncteur covariant additif} de")
add(40, "(11.6.2), line 2", "de l'*hyperhomologie* (l' upright)", r"\emph{l'hyperhomologie}", "italics",
    r"\emph{l'hyperhomologie}", r"l'\emph{hyperhomologie}",
    note="Enlarged crop: the l and the apostrophe are upright.")
add(40, "(11.6.2), line 2", "bold L in L.T(K.)", r"$L_\bullet T(K_\bullet)$", "font",
    r"$L_\bullet T(K_\bullet)$ et des", r"$\mathbf{L}_\bullet T(K_\bullet)$ et des",
    note="The print sets the hyperhomology L bold throughout 11.6-11.7 (plain L only for the derived functors L_pT, L_qT, L_nT).")
add(40, "(11.6.2), line 4", "les termes E^2 des deux suites", r"$E_2$", "formula",
    r"$E_2$ des deux suites", r"$E^2$ des deux suites", note="Superscript 2 (enlarged crop), as in (11.6.2.1)-(11.6.2.2).")
add(40, "(11.6.2.2)", "no comma after the formula", "trailing comma", "punctuation",
    r"{}''E^2_{pq}=L_pT(H_q(K_\bullet)),", r"{}''E^2_{pq}=L_pT(H_q(K_\bullet))")
add(40, "after (11.6.2.2)", "le p^e dérivé de T", "le $p$-ième dérivé gauche de $T$", "extra",
    r"dérivé gauche de", r"dérivé de", note="The print has no 'gauche'.")
add(40, "after (11.6.2.2)", "p^e (superscript e)", "$p$-ième", "word",
    r"$p$-ième", r"$p$\textsuperscript{e}")
add(40, "second paragraph, line 3", "du type AB 5*) de T, 1.5 sur la catégorie C')", "du type (AB~5*) de (T, 1.5) sur la", "punctuation",
    r"du type (AB~5*) de (T, 1.5) sur la", r"du type AB~5*) de T, 1.5 sur la",
    note="The print has no parenthesis before AB and none around T, 1.5 (enlarged crop); 'AB 5*)' is the Tohoku axiom label, cf. 'AB 5) de (T, 1.5)' at ega3-1-fr.tex line 1647. Not a misprint.")
add(40, "second paragraph", "conditions de *régularité*", "régularité upright", "italics",
    r"conditions de régularité des", r"conditions de \emph{régularité} des")
add(40, "second paragraph", "la *seconde* suite spectrale", "seconde upright", "italics",
    r"et la seconde suite spectrale", r"et la \emph{seconde} suite spectrale")
add(40, "second paragraph", "est cette fois *régulière*", "régulière upright", "italics",
    r"est cette fois régulière.", r"est cette fois \emph{régulière}.")
add(40, "second paragraph", "alors les *deux* suites", "deux upright", "italics",
    r"alors les deux suites", r"alors les \emph{deux} suites")
add(40, "second paragraph, end", "sont *birégulières*", "birégulières upright", "italics",
    r"et sont birégulières.", r"et sont \emph{birégulières}.")
add(40, "Proposition (11.6.3) (i)", "statement text italic", r"\emph{...} inside the italic proposition environment (comes out upright)", "convention",
    r"\item[{\rm(i)}] \emph{L'hyperhomologie", r"\item[{\rm(i)}] {L'hyperhomologie", conv=6,
    note="Drops \\emph (FIX_POLICY 6); the brace group is kept so the closing brace stays balanced.")
add(40, "Proposition (11.6.3) (i)", "bold L in L.T(K.)", r"$L_\bullet T(K_\bullet)$", "font",
    r"$L_\bullet T(K_\bullet)$ est un", r"$\mathbf{L}_\bullet T(K_\bullet)$ est un")
add(40, "Proposition (11.6.3) (ii)", "statement text italic", r"\emph{...} inside the italic environment", "convention",
    r"\item[{\rm(ii)}] \emph{Soit", r"\item[{\rm(ii)}] {Soit", conv=6)
add(40, "(11.6.3.1)", "bold L_i", r"L_iT(K_\bullet)", "font",
    r"\tag{11.6.3.1}¶L_iT", r"\tag{11.6.3.1}¶\mathbf{L}_iT")
add(40, "(11.6.3.1)", "isomorphism arrow (tilde over arrow)", r"\simeq", "convention",
    r"\simeq H_i(T(K_\bullet))", r"\xrightarrow{\sim} H_i(T(K_\bullet))", conv=4)
add(40, "Proposition (11.6.3) (iii)", "statement text italic", r"\emph{...} inside the italic environment", "convention",
    r"\item[{\rm(iii)}] \emph{Soit", r"\item[{\rm(iii)}] {Soit", conv=6)
add(40, "(11.6.3.2)", "bold L in L.T(K.)", r"L_\bullet T(K_\bullet)", "font",
    r"\tag{11.6.3.2}¶L_\bullet T", r"\tag{11.6.3.2}¶\mathbf{L}_\bullet T")
add(40, "(11.6.3.2)", "isomorphism arrow (tilde over arrow)", r"\simeq", "convention",
    r"K_\bullet)\simeq H_\bullet", r"K_\bullet)\xrightarrow{\sim} H_\bullet", conv=4)
add(40, "(11.6.3.2)", "no period after the formula", "trailing period", "punctuation",
    r"(T(L_{\bullet\bullet})).", r"(T(L_{\bullet\bullet}))")
add(40, "after (11.6.3.2)", "'Les démonstrations se font ... au lecteur.' roman (after the statement)", "inside the italic proposition environment", "convention",
    r"Les démonstrations se font comme celles de", r"\upshape Les démonstrations se font comme celles de", conv=6,
    note="Same repair as FIXLOG p. 117 (\\upshape before text that follows a statement inside its environment). Moving \\end{proposition} before this paragraph would also do.")
add(40, "(11.6.4), line 1", "les *multifoncteurs* covariants", "multifoncteurs upright", "italics",
    r"pour les multifoncteurs covariants", r"pour les \emph{multifoncteurs} covariants")
add(40, "(11.6.4), line 3", "de termes E^2 donnés par", r"$E_2$", "formula",
    r"de termes $E_2$ donnés par", r"de termes $E^2$ donnés par", note="Superscript 2 (enlarged crop).")

# ---------------- page 41 ----------------
add(41, "(11.6.4.2)", "''E^2_pq = Σ L_p(H_q'(K.), H_q''(K'.)).  (no T after L_p)", r"L_pT(H_{q'}(K_\bullet),H_{q''}(K'_\bullet))", "misprint_in_print",
    r"\sum_{q'+q''=q}L_pT(H_{q'}", r"\sum_{q'+q''=q}L_p(H_{q'}",
    corrected=r"\sum_{q'+q''=q}L_pT(H_{q'}(K_\bullet),H_{q''}(K'_\bullet))",
    note="The print omits T (enlarged crop); compare (11.6.2.2) L_pT(H_q(K.)). The TeX silently corrects; the fix restores the printed reading.")
add(41, "after (11.6.4.2)", "c'est la *seconde* suite spectrale", "seconde upright", "italics",
    r"c'est la seconde suite spectrale", r"c'est la \emph{seconde} suite spectrale")
add(41, "Proposition (11.6.5) (i)", "statement text italic", r"\emph{...} inside the italic environment", "convention",
    r"\item[{\rm(i)}] \emph{", r"\item[{\rm(i)}] {", conv=6)
add(41, "Proposition (11.6.5) (i)", "bold L in L.T(K., K'.)", r"$L_\bullet T(K_\bullet,K'_\bullet)$", "font",
    r"$L_\bullet T(K_\bullet,K'_\bullet)$ est un bifoncteur", r"$\mathbf{L}_\bullet T(K_\bullet,K'_\bullet)$ est un bifoncteur")
add(41, "Proposition (11.6.5) (ii)", "statement text italic", r"\emph{...} inside the italic environment", "convention",
    r"\item[{\rm(ii)}] \emph{Supposons", r"\item[{\rm(ii)}] {Supposons", conv=6)
add(41, "Proposition (11.6.5) (ii), line 2", "soit une résolutiou de K_i", "résolution", "misprint_in_print",
    r"soit une¶résolution de $K_i$", r"soit une¶résolutiou de $K_i$", corrected="résolution",
    note="Turned n in the print (enlarged crop); the TeX silently corrects.")
add(41, "Proposition (11.6.5) (ii), line 3", "une résolution de K'_i, et enfin que", "no comma after $K'_i$", "punctuation",
    r"$K'_i$ et enfin que", r"$K'_i$, et enfin que")
add(41, "(11.6.5.1)", "bold L", r"L_\bullet T(K_\bullet,K'_\bullet)", "font",
    r"\tag{11.6.5.1}¶L_\bullet T", r"\tag{11.6.5.1}¶\mathbf{L}_\bullet T")
add(41, "(11.6.5.1)", "isomorphism arrow (tilde over arrow)", r"\simeq", "convention",
    r"\simeq H_\bullet(T(L_{\bullet\bullet},L'_{\bullet\bullet}))", r"\xrightarrow{\sim} H_\bullet(T(L_{\bullet\bullet},L'_{\bullet\bullet}))", conv=4)
add(41, "Proposition (11.6.5) (iii)", "statement text italic", r"\emph{...} inside the italic environment", "convention",
    r"\item[{\rm(iii)}] \emph{Supposons en outre", r"\item[{\rm(iii)}] {Supposons en outre", conv=6)
add(41, "Proposition (11.6.5) (iii)", "inline: A ⇝ T(A, L'_hk) et A' ⇝ T(L_ij, A') (squiggly arrows, word 'et')",
    r"display with \longmapsto and ',\qquad' (no 'et')", "formula",
    r"les foncteurs¶\[¶A\longmapsto T(A,L'_{hk}),\qquad¶A'\longmapsto T(L_{ij},A')¶\]",
    r"les foncteurs¶$A\leadsto T(A,L'_{hk})$ et $A'\leadsto T(L_{ij},A')$",
    note="Three differences in one edit: wavy arrow (\\leadsto, as elsewhere in ega3-1-fr.tex), missing word 'et', and display versus the print's inline setting.")
add(41, "(11.6.5.2)", "bold L", r"L_\bullet T(K_\bullet,K'_\bullet)", "font",
    r"\tag{11.6.5.2}¶L_\bullet T", r"\tag{11.6.5.2}¶\mathbf{L}_\bullet T")
add(41, "(11.6.5.2), first arrow", "isomorphism arrow (tilde over arrow)", r"\simeq", "convention",
    r"\simeq H_\bullet(T(L_{\bullet\bullet},K'_\bullet))", r"\xrightarrow{\sim} H_\bullet(T(L_{\bullet\bullet},K'_\bullet))", conv=4)
add(41, "(11.6.5.2), second arrow", "isomorphism arrow (tilde over arrow)", r"\simeq", "convention",
    r"\simeq H_\bullet(T(K_\bullet,L'_{\bullet\bullet}))", r"\xrightarrow{\sim} H_\bullet(T(K_\bullet,L'_{\bullet\bullet}))", conv=4)
add(41, "after (11.6.5.2)", "'Les démonstrations sont analogues ...' roman", "inside the italic proposition environment", "convention",
    r"Les démonstrations sont analogues", r"\upshape Les démonstrations sont analogues", conv=6)
add(41, "(11.7.1), line 3", "*limités inférieurement*", "upright", "italics",
    r"degrés sont limités inférieurement;", r"degrés sont \emph{limités inférieurement};")
add(41, "(11.7.1)", "un *tricomplexe* M...", "tricomplexe upright", "italics",
    r"est un¶tricomplexe $M", r"est un¶\emph{tricomplexe} $M")
add(41, "(11.7.1)", "constituent des *résolutions projectives* de", "upright", "italics",
    r"constituent des résolutions¶projectives de", r"constituent des \emph{résolutions¶projectives} de")
add(41, "(11.7.1), last line", "M_{ij,.} est une *résolution projective* de K_ij", "upright", "italics",
    r"est une résolution projective de $K_{ij}$", r"est une \emph{résolution projective} de $K_{ij}$")
add(41, "Proposition (11.7.2)", "reference (11.7.1) upright", "italic (inside the italic environment, outside \\emph)", "convention",
    r"(\hyperref[0.11.7.1-fr]{11.7.1})", r"\textup{(\hyperref[0.11.7.1-fr]{11.7.1})}", conv=6)
add(41, "Proposition (11.7.2)", "statement text italic from l'homologie on (continues on p. 42 to 'les formules')", r"\emph{l'homologie ...} inside the italic environment (upright)", "convention",
    r"\emph{l'homologie", r"{l'homologie", conv=6,
    note="The group closes on p. 42 ('donnés par les formules}'); see the p. 42 \\textup for (11.6.2).")
add(41, "Proposition (11.7.2), last line", "bold L in L.T(K..)", r"$L_\bullet T(K_{\bullet\bullet})$", "font",
    r"$L_\bullet T(K_{\bullet\bullet})$ du complexe", r"$\mathbf{L}_\bullet T(K_{\bullet\bullet})$ du complexe")

# ---------------- page 42 ----------------
add(42, "Proposition (11.7.2), line 1", "reference (11.6.2) upright", "upright only because of the \\emph that the p. 41 fix drops", "convention",
    r"(\hyperref[0.11.6.2-fr]{11.6.2}), et est", r"\textup{(\hyperref[0.11.6.2-fr]{11.6.2})}, et est", conv=6,
    note="Apply with the p. 41 fix '\\emph{l'homologie' -> '{l'homologie'; harmless on its own.")
add(42, "Proposition (11.7.2), line 2", "dont les termes E^2 sont", r"$E_2$", "formula",
    r"dont les termes $E_2$ sont", r"dont les termes $E^2$ sont", note="Superscript 2 (enlarged crop).")
add(42, "display after (11.7.2), (a)", "no punctuation after the formulas", "trailing comma", "punctuation",
    r"=L_pT(H_q(K_{\bullet\bullet})),&", r"=L_pT(H_q(K_{\bullet\bullet}))&",
    note="The six formulas are printed one per line without commas or final period.")
add(42, "display after (11.7.2), (b)", "H_p(**L**^II_q T(K..)), no comma", r"H_p(L_q^{\mathrm{II}}T(K_{\bullet\bullet})),", "font",
    r"=H_p(L_q^{\mathrm{II}}T(K_{\bullet\bullet})),\\", r"=H_p(\mathbf{L}_q^{\mathrm{II}}T(K_{\bullet\bullet}))\\",
    note="Bold L (hyperhomology) and no comma.")
add(42, "display after (11.7.2), (a')", "**L**_pT(H^I_q(K..)), no comma", r"L_pT(H_q^{\mathrm I}(K_{\bullet\bullet})),", "font",
    r"=L_pT(H_q^{\mathrm I}(K_{\bullet\bullet})),&", r"=\mathbf{L}_pT(H_q^{\mathrm I}(K_{\bullet\bullet}))&",
    note="Bold L and no comma.")
add(42, "display after (11.7.2), (b')", "no comma", "trailing comma", "punctuation",
    r"=H_p(L_qT(K_{\bullet\bullet})),\\", r"=H_p(L_qT(K_{\bullet\bullet}))\\")
add(42, "display after (11.7.2), (c)", "**L**_pT(H^II_q(K..)), no comma", r"L_pT(H_q^{\mathrm{II}}(K_{\bullet\bullet})),", "font",
    r"=L_pT(H_q^{\mathrm{II}}(K_{\bullet\bullet})),&", r"=\mathbf{L}_pT(H_q^{\mathrm{II}}(K_{\bullet\bullet}))&",
    note="Bold L and no comma.")
add(42, "display after (11.7.2), (d)", "H_p(**L**^I_q T(K..)), no period", r"H_p(L_q^{\mathrm I}T(K_{\bullet\bullet})).", "font",
    r"=H_p(L_q^{\mathrm I}T(K_{\bullet\bullet})).", r"=H_p(\mathbf{L}_q^{\mathrm I}T(K_{\bullet\bullet}))",
    note="Bold L and no final period.")
add(42, "'On rappelle' paragraph, start", "(On rappelle ...", "no opening parenthesis", "punctuation",
    r"On rappelle que nous utilisons", r"(On rappelle que nous utilisons")
add(42, "'On rappelle' paragraph, end", "... au complexe simple K_{i,.}.)", "no closing parenthesis", "punctuation",
    r"au complexe simple $K_{i,\bullet}$.", r"au complexe simple $K_{i,\bullet}$.)")
add(42, "'On rappelle' paragraph", "bold L in L^II_q T(K..)", "plain L", "font",
    r"exemple $L_q^{\mathrm{II}}T", r"exemple $\mathbf{L}_q^{\mathrm{II}}T")
add(42, "'On rappelle' paragraph", "bold L in (L^II_q T(K_{i,.}))_{i>=0}", "plain L", "font",
    r"$(L_q^{\mathrm{II}}T(K_{i,\bullet}))_{i\geq0}$", r"$(\mathbf{L}_q^{\mathrm{II}}T(K_{i,\bullet}))_{i\geq0}$")
add(42, "'On rappelle' paragraph", "bold L in L^II_q T(K_{i,.}) est l'hyperhomologie", "plain L", "font",
    r"$L_q^{\mathrm{II}}T(K_{i,\bullet})$ est", r"$\mathbf{L}_q^{\mathrm{II}}T(K_{i,\bullet})$ est")
add(42, "proof of (11.7.2), line 1", "inline: de sorte que L_i = ⊕ K_rs, et posons", "display", "other",
    r"de sorte que¶\[¶L_i=\bigoplus_{r+s=i}K_{rs},¶\]¶et posons",
    r"de sorte que $L_i=\bigoplus_{r+s=i}K_{rs}$, et¶posons", note="Display in the TeX, inline in the print.")
add(42, "proof of (11.7.2), line 2", "inline: N_ij = ⊕ M_rsj;", "display", "other",
    r"\[¶N_{ij}=\bigoplus_{r+s=i}M_{rsj};¶\]", r"$N_{ij}=\bigoplus_{r+s=i}M_{rsj}$;",
    note="Display in the TeX, inline in the print.")
add(42, "proof of (11.7.2), line 2", "une *résolution projective* de L_i", "upright", "italics",
    r"une résolution¶projective de $L_i$", r"une \emph{résolution¶projective} de $L_i$")
add(42, "proof of (11.7.2), line 4", "inline: L.T(L.) ⥲ H.(T(N..));", "display", "other",
    r"isomorphisme fonctoriel¶\[", r"isomorphisme fonctoriel¶$",
    note="Opening half of display -> inline; apply together with the closing edit ';\\n\\]\\ncomme le complexe' (same page).")
add(42, "proof of (11.7.2), line 4", "bold L in L.T(L.)", "plain L", "font",
    "¶" + r"L_\bullet T(L_", "¶" + r"\mathbf{L}_\bullet T(L_")
add(42, "proof of (11.7.2), line 4", "isomorphism arrow (tilde over arrow)", r"\simeq", "convention",
    r"\simeq H_\bullet(T(N_{\bullet\bullet}))", r"\xrightarrow{\sim} H_\bullet(T(N_{\bullet\bullet}))", conv=4)
add(42, "proof of (11.7.2), line 4", "inline (closing)", "display", "other",
    r";¶\]¶comme le complexe", r"$;¶comme le complexe",
    note="Closing half of display -> inline; apply together with 'isomorphisme fonctoriel\\n\\[' -> 'isomorphisme fonctoriel\\n$'.")
add(42, "proof of (11.7.2), 'En outre'", "bold L in L.T(L.)", "plain L", "font",
    r"En outre, $L_\bullet T(L_\bullet)$", r"En outre, $\mathbf{L}_\bullet T(L_\bullet)$")
add(42, "proof of (11.7.2), 'Considérons maintenant'", "inline: U_ij = ⊕ M_irs;", "display", "other",
    r"\[¶U_{ij}=\bigoplus_{r+s=j}M_{irs};¶\]", r"$U_{ij}=\bigoplus_{r+s=j}M_{irs}$;",
    note="Display in the TeX, inline in the print.")
add(42, "proof of (11.7.2), 'donc'", "bold L in L^II_q T(K_{i,.})", "plain L", "font",
    r"=¶L_q^{\mathrm{II}}T", r"=¶\mathbf{L}_q^{\mathrm{II}}T")
add(42, "proof of (11.7.2), 'donc'", "L^II_qT(K_{i,.})), (one closing parenthesis too many)", r"L_q^{\mathrm{II}}T(K_{i,\bullet})", "misprint_in_print",
    r"(K_{i,\bullet})$, et la première", r"(K_{i,\bullet}))$, et la première",
    corrected=r"H_q^{\mathrm{II}}(T(U_{i,\bullet}))=\mathbf{L}_q^{\mathrm{II}}T(K_{i,\bullet})",
    note="Unbalanced parenthesis in the print (enlarged crop); the TeX silently corrects; the fix restores the printed reading.")
add(42, "proof of (11.7.2), 'D'autre part'", "complexe simple K_{.,r}; le calcul", "comma", "punctuation",
    r"$K_{\bullet,r}$, le calcul", r"$K_{\bullet,r}$; le calcul")
add(42, "proof of (11.7.2), (M, XV, 2)", "inline: H^I_q(T(M_{.,rs})) = T(H^I_q(M_{.,rs})),", "display", "other",
    r"montre que¶\[¶H_q^{\mathrm I}(T(M_{\bullet,rs}))¶=T(H_q^{\mathrm I}(M_{\bullet,rs})),¶\]",
    r"montre que¶$H_q^{\mathrm I}(T(M_{\bullet,rs}))=T(H_q^{\mathrm I}(M_{\bullet,rs}))$,",
    note="Display in the TeX, inline in the print.")
add(42, "proof of (11.7.2), d'où", "inline: d'où H^I_q(T(U_{.,j})) = ⊕ T(H^I_q(M_{.,rs}));", "display", "other",
    r"¶d'où¶\[¶H_q^{\mathrm I}(T(U_{\bullet,j}))¶=\bigoplus_{r+s=j}T(H_q^{\mathrm I}(M_{\bullet,rs}));¶\]",
    r"¶d'où $H_q^{\mathrm I}(T(U_{\bullet,j}))=\bigoplus_{r+s=j}T(H_q^{\mathrm I}(M_{\bullet,rs}))$;",
    note="Display in the TeX, inline in the print.")
add(42, "proof of (11.7.2), 'associé au bicomplexe'", "T(H^I_q(M...)). (one closing parenthesis missing)", r"T(H_q^{\mathrm I}(M_{\bullet\bullet\bullet}))", "misprint_in_print",
    r"$T(H_q^{\mathrm I}(M_{\bullet\bullet\bullet}))$. Or,", r"$T(H_q^{\mathrm I}(M_{\bullet\bullet\bullet})$. Or,",
    corrected=r"T(H_q^{\mathrm I}(M_{\bullet\bullet\bullet}))",
    note="Only one closing parenthesis in the print (enlarged crop); the TeX silently corrects; the fix restores the printed reading.")
add(42, "proof of (11.7.2), 'Or, pour tout q'", "une résolution *projective* du complexe", "upright", "italics",
    r"est une résolution projective du", r"est une résolution \emph{projective} du")
add(42, "proof of (11.7.2), last display", "bold L in L_pT(H^I_q(K..))", "plain L", "font",
    r"\bigr)¶=L_pT(H_q^{\mathrm I}", r"\bigr)¶=\mathbf{L}_pT(H_q^{\mathrm I}")
add(42, "'On dit que'", "bold L in L.T(K..)", "plain L", "font",
    r"On dit que $L_\bullet T(K_{\bullet\bullet})$", r"On dit que $\mathbf{L}_\bullet T(K_{\bullet\bullet})$")
add(42, "'On dit que'", "l'*hyperhomologie* (l' upright)", r"\emph{l'hyperhomologie}", "italics",
    r"\emph{l'hyperhomologie} de", r"l'\emph{hyperhomologie} de", note="Enlarged crop: l' upright.")
add(42, "'On dit que'", "relative au *bicomplexe* K..", "bicomplexe upright", "italics",
    r"relative au bicomplexe", r"relative au \emph{bicomplexe}")
add(42, "(11.7.3) heading", "Remarques (11.7.3). — (i) ...", r"env heading '(11.7.3)' followed by '\emph{Remarques}.'", "other",
    r"\begin{env}[11.7.3]¶\label{0.11.7.3-fr}¶\emph{Remarques}.¶",
    r"\begin{remarks}[11.7.3]¶\label{0.11.7.3-fr}¶\upshape¶",
    note="Apply together with the p. 43 edit '\\end{enumerate}\\n\\end{env}' -> '\\end{enumerate}\\n\\end{remarks}'. \\upshape keeps the body roman as printed while the remarks environment is italic (GLOBAL_ISSUES 2). Same env + \\emph{Remarques} pattern 7 times in ega3-1-fr.tex.")
add(42, "Remarques (11.7.3) (i)", "bold L in L.T(K..)", "plain L", "font",
    r"$L_\bullet T(K_{\bullet\bullet})$ est un", r"$\mathbf{L}_\bullet T(K_{\bullet\bullet})$ est un")
add(42, "Remarques (11.7.3) (i)", "un *foncteur homologique*", "upright", "italics",
    r"foncteur homologique dans la", r"\emph{foncteur homologique} dans la")

# ---------------- page 43 ----------------
add(43, "Remarques (11.7.3) (ii)", "une *résolution* de K_rs", "upright", "italics",
    r"soit une résolution de $K_{rs}$", r"soit une \emph{résolution} de $K_{rs}$")
add(43, "Remarques (11.7.3) (ii)", "inline: L.T(K..) ⥲ H.(T(M...));", "display", "other",
    r"un isomorphisme¶\[", r"un isomorphisme¶$",
    note="Opening half of display -> inline; apply together with the closing edit ';\\n\\]\\nen effet' (same page).")
add(43, "Remarques (11.7.3) (ii)", "bold L in L.T(K..)", "plain L", "font",
    "¶" + r"L_\bullet T(K_{\bullet\bullet})", "¶" + r"\mathbf{L}_\bullet T(K_{\bullet\bullet})")
add(43, "Remarques (11.7.3) (ii)", "isomorphism arrow (tilde over arrow)", r"\simeq", "convention",
    r"\simeq H_\bullet(T(M_{\bullet\bullet\bullet}))", r"\xrightarrow{\sim} H_\bullet(T(M_{\bullet\bullet\bullet}))", conv=4)
add(43, "Remarques (11.7.3) (ii)", "inline (closing)", "display", "other",
    r";¶\]¶en effet", r"$;¶en effet",
    note="Closing half of display -> inline; apply together with 'un isomorphisme\\n\\[' -> 'un isomorphisme\\n$'.")
add(43, "Remarques (11.7.3) (iii)", "bold L in L.T(L., L'.)", "plain L", "font",
    r"$L_\bullet T(L_\bullet,L'_\bullet)$", r"$\mathbf{L}_\bullet T(L_\bullet,L'_\bullet)$")
add(43, "end of Remarques (11.7.3)", "end of the remarks", r"\end{env}", "other",
    r"\end{enumerate}¶\end{env}", r"\end{enumerate}¶\end{remarks}",
    note="Apply together with the p. 42 heading edit (\\begin{env}[11.7.3] ... -> \\begin{remarks}[11.7.3]).")
add(43, "(11.8.1)", "étant de *degré* h", "degré upright", "italics",
    r"étant de degré $h$", r"étant de \emph{degré} $h$")
add(43, "(11.8.1), differential", "inline: d(α_0, ..., α_h) = Σ (−1)^j (α_0, ..., α̂_j, ..., α_h). with the hat over α only",
    r"display; \widehat{\alpha_j}", "other",
    r"définie par¶\[¶d(\alpha_0,\ldots,\alpha_h)=¶\sum_{j=0}^{h}(-1)^j¶(\alpha_0,\ldots,\widehat{\alpha_j},\ldots,\alpha_h).¶\]",
    r"définie par¶$d(\alpha_0,\ldots,\alpha_h)=\sum_{j=0}^{h}(-1)^j(\alpha_0,\ldots,\widehat{\alpha}_j,\ldots,\alpha_h)$.",
    note="Inline in the print; the hat covers alpha only (\\widehat{\\alpha}_j), cf. convention 8. The print's minus is the long dash (GLOBAL_ISSUES 23), left as is.")
add(43, "(11.8.1)", "π(σ) — ε_π.σ (dot before σ)", r"\pi(\sigma)-\varepsilon_\pi\sigma", "formula",
    r"\pi(\sigma)-\varepsilon_\pi\sigma", r"\pi(\sigma)-\varepsilon_\pi.\sigma",
    note="Baseline dot in the print (enlarged crop). The long-dash minus is GLOBAL_ISSUES 23.")
add(43, "(11.8.1)", "inline: π(σ) = (α_π(0), ..., α_π(h))", "display", "other",
    r"\[¶\pi(\sigma)=(\alpha_{\pi(0)},\ldots,\alpha_{\pi(h)})¶\]", r"$\pi(\sigma)=(\alpha_{\pi(0)},\ldots,\alpha_{\pi(h)})$",
    note="Display in the TeX, inline in the print.")
add(43, "(11.8.1)", "dits chaînes *dégénérées* (chaînes upright)", r"\emph{chaînes dégénérées}", "italics",
    r"\emph{chaînes¶dégénérées}", r"chaînes¶\emph{dégénérées}")
add(43, "(11.8.1)", "inline: p : C.(A) → L.(A).", "display", "other",
    r"\[¶p:\mathrm C_\bullet(A)\longrightarrow\mathrm L_\bullet(A).¶\]", r"$p:\mathrm C_\bullet(A)\longrightarrow\mathrm L_\bullet(A)$.",
    note="Display in the TeX, inline in the print.")
add(43, "(11.8.1)", "inline: j : L.(A) → C.(A)", "display", "other",
    r"\[¶j:\mathrm L_\bullet(A)\longrightarrow\mathrm C_\bullet(A)¶\]", r"$j:\mathrm L_\bullet(A)\longrightarrow\mathrm C_\bullet(A)$",
    note="Display in the TeX, inline in the print.")
add(43, "(11.8.1)", "rangés *dans l'ordre croissant*", "upright", "italics",
    r"rangés dans l'ordre croissant dans", r"rangés \emph{dans l'ordre croissant} dans")
add(43, "(11.8.1), end", "l'*identité* de L.(A)", "upright", "italics",
    r"est l'identité de", r"est l'\emph{identité} de")
add(43, "(11.8.2)", "inline: d(σ, τ) = ... si Card |σ| = h + 1. ending the paragraph; 'Les homomorphismes naturels' starts a new paragraph",
    "display; no paragraph break before 'Les homomorphismes naturels'", "other",
    r"\[¶d(\sigma,\tau)=(d'\sigma,\tau)+(-1)^{h+1}(\sigma,d''\tau)¶\quad\text{si }\operatorname{Card}|\sigma|=h+1.¶\]¶Les homomorphismes naturels",
    r"$d(\sigma,\tau)=(d'\sigma,\tau)+(-1)^{h+1}(\sigma,d''\tau)$ si $\operatorname{Card}|\sigma|=h+1$.¶¶Les homomorphismes naturels",
    note="Inline in the print, and the next paragraph is indented.")
add(43, "(11.8.2)", "inline: p : C.(A)⊗C.(B) → L.(A)⊗L.(B),", "display", "other",
    r"\[¶p:\mathrm C_\bullet(A)\otimes\mathrm C_\bullet(B)¶\longrightarrow\mathrm L_\bullet(A)\otimes\mathrm L_\bullet(B),¶\]",
    r"$p:\mathrm C_\bullet(A)\otimes\mathrm C_\bullet(B)\longrightarrow\mathrm L_\bullet(A)\otimes\mathrm L_\bullet(B)$,",
    note="Display in the TeX, inline in the print.")
add(43, "(11.8.2)", "(C.(A)⊗C.(B))/(C.(A)⊗D.(B) + D.(A)⊗C.(B)). inline with a slash", r"display \frac{...}{...}", "formula",
    r"\[¶\frac{\mathrm C_\bullet(A)\otimes\mathrm C_\bullet(B)}¶{\mathrm C_\bullet(A)\otimes\mathrm D_\bullet(B)¶+\mathrm D_\bullet(A)\otimes\mathrm C_\bullet(B)}.¶\]",
    r"$(\mathrm C_\bullet(A)\otimes\mathrm C_\bullet(B))/(\mathrm C_\bullet(A)\otimes\mathrm D_\bullet(B)+\mathrm D_\bullet(A)\otimes\mathrm C_\bullet(B))$.",
    note="The print writes the quotient inline with a slash and parentheses.")
add(43, "(11.8.2), end", "inline: j : L.(A)⊗L.(B) → C.(A)⊗C.(B)", "display", "other",
    r"\[¶j:\mathrm L_\bullet(A)\otimes\mathrm L_\bullet(B)¶\longrightarrow\mathrm C_\bullet(A)\otimes\mathrm C_\bullet(B)¶\]",
    r"$j:\mathrm L_\bullet(A)\otimes\mathrm L_\bullet(B)\longrightarrow\mathrm C_\bullet(A)\otimes\mathrm C_\bullet(B)$",
    note="Display in the TeX, inline in the print.")

# ---------------- page 44 ----------------
add(44, "Proposition (11.8.3)", "statement italic", r"\emph{...} inside the italic environment", "convention",
    r"\emph{Il existe une homotopie", r"{Il existe une homotopie", conv=6)
add(44, "Proposition (11.8.3)", "inline: h : C.(A)⊗C.(B) → C.(A)⊗C.(B),", "display", "other",
    r"\[¶h:\mathrm C_\bullet(A)\otimes\mathrm C_\bullet(B)¶\longrightarrow\mathrm C_\bullet(A)\otimes\mathrm C_\bullet(B),¶\]",
    r"$h:\mathrm C_\bullet(A)\otimes\mathrm C_\bullet(B)\longrightarrow\mathrm C_\bullet(A)\otimes\mathrm C_\bullet(B)$,",
    note="Display in the TeX, inline in the print.")
add(44, "proof of (11.8.3)", "inline: ω = f(σ, τ) − (σ, τ) − h(d(σ, τ));", "display", "other",
    r"\[¶\omega=f(\sigma,\tau)-(\sigma,\tau)-h(d(\sigma,\tau));¶\]", r"$\omega=f(\sigma,\tau)-(\sigma,\tau)-h(d(\sigma,\tau))$;",
    note="Display in the TeX, inline in the print.")
add(44, "proof of (11.8.3)", "inline: ω ∈ C.(|σ|)⊗C.(|τ|).", "display", "other",
    r"\[¶\omega\in\mathrm C_\bullet(|\sigma|)\otimes\mathrm C_\bullet(|\tau|).¶\]", r"$\omega\in\mathrm C_\bullet(|\sigma|)\otimes\mathrm C_\bullet(|\tau|)$.",
    note="Display in the TeX, inline in the print.")
add(44, "proof of (11.8.3)", "inline: H_q(C.(A)⊗C.(B)) = 0 pour q > 0,", r"display '=0\quad(q>0),'", "word",
    r"\[¶H_q(\mathrm C_\bullet(A)\otimes\mathrm C_\bullet(B))=0\quad(q>0),¶\]",
    r"$H_q(\mathrm C_\bullet(A)\otimes\mathrm C_\bullet(B))=0$ pour $q>0$,",
    note="The print has the words 'pour q>0' and sets the formula inline.")
add(44, "proof of (11.8.3)", "un élément ω' de C.(|σ|)⊗C.(|τ|) (word 'de')", r"display '\omega'\in ...'", "word",
    r"\[¶\omega'\in\mathrm C_\bullet(|\sigma|)\otimes\mathrm C_\bullet(|\tau|)¶\]",
    r"$\omega'$ de $\mathrm C_\bullet(|\sigma|)\otimes\mathrm C_\bullet(|\tau|)$",
    note="The print has the word 'de', not the sign of membership, and sets it inline (enlarged crop).")
add(44, "(11.8.4)", "système de coefficients 𝒮 (script S)", r"$\Gamma$", "formula",
    r"coefficients} $\Gamma$ sur", r"coefficients} $\mathscr S$ sur",
    note="The print names the system script S and its groups Gamma_{sigma,tau}; the TeX uses Gamma for both. The script S continues in C^.(A,B;S), L^.(A,B;S) on this page (all occurrences below) and the TeX's A,B;\\Gamma occurs 15 more times on pp. 45 ff.")
add(44, "(11.8.4)", "inline: Γ_{σ,τ} → Γ_{σ',τ'}, pour (σ, τ) ≤ (σ', τ'),", r"display with '\quad\text{pour }'", "other",
    r"\[¶\Gamma_{\sigma,\tau}\longrightarrow\Gamma_{\sigma',\tau'}¶\quad\text{pour }(\sigma,\tau)\leq(\sigma',\tau'),¶\]",
    r"$\Gamma_{\sigma,\tau}\longrightarrow\Gamma_{\sigma',\tau'}$, pour $(\sigma,\tau)\leq(\sigma',\tau')$,",
    note="Inline in the print, with a comma after Gamma_{sigma',tau'} (printed at subscript height).")
add(44, "(11.8.4)", "un *système inductif*", "upright", "italics",
    r"formant un système inductif", r"formant un \emph{système inductif}")
add(44, "(11.8.4)", "un *complexe de cochaînes*", "upright", "italics",
    r"un complexe de cochaînes", r"un \emph{complexe de cochaînes}")
add(44, "(11.8.4)", "C^.(A, B; 𝒮)", r"\mathrm C^\bullet(A,B;\Gamma)", "formula",
    r"$\mathrm C^\bullet(A,B;\Gamma)$ comme l'ensemble", r"$\mathrm C^\bullet(A,B;\mathscr S)$ comme l'ensemble")
add(44, "(11.8.4)", "inline: si d(σ, τ) = Σ_i ±(σ_i, τ_i),", "display", "other",
    r"\[¶d(\sigma,\tau)=\sum_i\pm(\sigma_i,\tau_i),¶\]", r"$d(\sigma,\tau)=\sum_i\pm(\sigma_i,\tau_i)$,",
    note="Display in the TeX, inline in the print (the next formula, d lambda, is displayed in both).")
add(44, "(11.8.4), 'Nous dirons'", "λ ∈ C^.(A, B; 𝒮)", r"\Gamma", "formula",
    r"$\lambda\in\mathrm C^\bullet(A,B;\Gamma)$ est", r"$\lambda\in\mathrm C^\bullet(A,B;\mathscr S)$ est")
add(44, "(11.8.4), 'Nous dirons'", "inline: λ(π(σ), τ) = ε_π λ(σ, τ) et λ(σ, π'(τ)) = ε_π' λ(σ, τ)", r"display joined by ',\qquad' (no 'et')", "missing",
    r"\[¶\lambda(\pi(\sigma),\tau)=\varepsilon_\pi\lambda(\sigma,\tau),¶\qquad¶\lambda(\sigma,\pi'(\tau))=\varepsilon_{\pi'}\lambda(\sigma,\tau)¶\]",
    r"$\lambda(\pi(\sigma),\tau)=\varepsilon_\pi\lambda(\sigma,\tau)$ et¶$\lambda(\sigma,\pi'(\tau))=\varepsilon_{\pi'}\lambda(\sigma,\tau)$",
    note="Missing word 'et'; inline in the print.")
add(44, "(11.8.4), end", "un *sous-complexe*", "upright", "italics",
    r"engendrent un sous-complexe", r"engendrent un \emph{sous-complexe}")
add(44, "(11.8.4), end", "L^.(A, B; 𝒮) de C^.(A, B; 𝒮)", r"\Gamma twice", "formula",
    r"$\mathrm L^\bullet(A,B;\Gamma)$ de $\mathrm C^\bullet(A,B;\Gamma)$.", r"$\mathrm L^\bullet(A,B;\mathscr S)$ de $\mathrm C^\bullet(A,B;\mathscr S)$.",
    note="Two occurrences.")
add(44, "Proposition (11.8.5)", "statement italic", r"\emph{...} inside the italic environment", "convention",
    r"\emph{L'injection canonique", r"{L'injection canonique", conv=6)
add(44, "Proposition (11.8.5)", "inline: L^.(A, B; 𝒮) → C^.(A, B; 𝒮)", r"display; \Gamma twice", "formula",
    r"\[¶\mathrm L^\bullet(A,B;\Gamma)\longrightarrow¶\mathrm C^\bullet(A,B;\Gamma)¶\]",
    r"$\mathrm L^\bullet(A,B;\mathscr S)\longrightarrow\mathrm C^\bullet(A,B;\mathscr S)$",
    note="Script S for Gamma (two occurrences) and inline as printed.")
add(44, "proof of (11.8.5)", "^tp : λ → λ∘p (transpose t, inline)", r"display, {}'p", "formula",
    r"les applications¶\[¶{}'p:", r"les applications¶${}^tp:",
    note="Left superscript t (transpose) in the print, prime in the TeX (enlarged crop). Also opens the inline formula: apply together with the edits ',\\qquad\\n{}'j:' and '\\n\\]\\nsont définies dans' (same page).")
add(44, "proof of (11.8.5)", "plain arrow λ → λ∘p", r"\longmapsto", "convention",
    r"\lambda\longmapsto\lambda\circ p", r"\lambda\to\lambda\circ p", conv=3)
add(44, "proof of (11.8.5)", "... λ∘p et ^tj : λ → λ∘j (word 'et', transpose t)", r"',\qquad' and {}'j", "missing",
    r",\qquad¶{}'j:", r"$ et¶${}^tj:",
    note="Missing word 'et' between the two maps, which the print sets inline; transpose t for the prime. Apply together with the edits on 'les applications\\n\\[\\n{}'p:' and '\\n\\]\\nsont définies dans'.")
add(44, "proof of (11.8.5)", "plain arrow λ → λ∘j", r"\longmapsto", "convention",
    r"\lambda\longmapsto\lambda\circ j", r"\lambda\to\lambda\circ j", conv=3)
add(44, "proof of (11.8.5)", "inline (closing)", "display", "other",
    "¶" + r"\]¶sont définies dans", "$¶sont définies dans",
    note="Closing half of display -> inline; apply together with the two edits above ('les applications ...' and ',\\qquad ...').")
add(44, "proof of (11.8.5)", "L^.(A, B; 𝒮) et C^.(A, B; 𝒮)", r"\Gamma twice", "formula",
    r"$\mathrm L^\bullet(A,B;\Gamma)$ et¶$\mathrm C^\bullet(A,B;\Gamma)$ respectivement",
    r"$\mathrm L^\bullet(A,B;\mathscr S)$ et¶$\mathrm C^\bullet(A,B;\mathscr S)$ respectivement", note="Two occurrences.")
add(44, "proof of (11.8.5)", "^tj∘^tp", r"\mathop{}'j\circ{}'p", "formula",
    r"$\mathop{}'j\circ{}'p$", r"${}^tj\circ{}^tp$", note="Transpose t, not prime (two occurrences).")
add(44, "proof of (11.8.5)", "^tp∘^tj", r"\mathop{}'p\circ{}'j", "formula",
    r"$\mathop{}'p\circ{}'j$", r"${}^tp\circ{}^tj$", note="Transpose t, not prime (two occurrences).")
add(44, "proof of (11.8.5)", "^th", r"\mathop{}'h", "formula",
    r"$\mathop{}'h:", r"${}^th:", note="Transpose t, not prime.")
add(44, "proof of (11.8.5)", "plain arrow λ → λ∘h", r"\mapsto", "convention",
    r"\lambda\mapsto\lambda\circ h", r"\lambda\to\lambda\circ h", conv=3)
add(44, "proof of (11.8.5)", "est *définie* dans", "upright", "italics",
    r"$ est définie dans", r"$ est \emph{définie} dans")
add(44, "proof of (11.8.5)", "C^.(A, B; 𝒮)", r"\Gamma", "formula",
    r"$\mathrm C^\bullet(A,B;\Gamma)$ et on peut donc", r"$\mathrm C^\bullet(A,B;\mathscr S)$ et on peut donc")

# ---------------- category letters (generated) ----------------
pages = {}
for p in range(40, 45):
    with open(RUN + r"\page_%03d.tex" % p, encoding="utf-8", newline="") as fh:
        pages[p] = fh.read().replace("\r\n", "\n")  # page extracts are CRLF; release files are LF
assert all("\r" not in t for t in pages.values()), "CR found"
with open(SRC, encoding="utf-8", newline="") as fh:
    srctext = fh.read()

def spans_of(p):
    out = []
    for d in F:
        if d["page"] != p or d["fix"] is None or d["_outside"]:
            continue
        o = d["fix"]["old"]
        i = pages[p].find(o)
        assert i >= 0, (p, o)
        out.append((i, i + len(o)))
    return out

CAT = re.compile(r"\$[^$]*\\mathcal\s*[CK][^$]*\$")
def conv_cat(s):
    return re.sub(r"\\mathcal\s*([CK])", r"\\boldsymbol{\1}", s)

for p in range(40, 45):
    t = pages[p]
    taken = spans_of(p)
    manual = list(taken)
    catspans = []
    for m in CAT.finditer(t):
        a, b = m.start(), m.end()
        if any(x <= a and b <= y for x, y in catspans):
            continue  # already converted inside a neighbouring category edit
        if any(a < y and x < b for x, y in manual):
            sys.exit("category letter inside a manual fix on p.%d at %d" % (p, a))
        # grow the context word by word until unique, keeping $...$ groups whole,
        # without touching manual fixes or earlier category edits
        def free(x, y):
            return not any(x < yy and xx < y for xx, yy in taken)
        def good(L, R):
            o = t[L:R]
            return t.count(o) == 1 and (R - L) >= (b - a) + 8 and o.count("$") % 2 == 0
        L, R = a, b
        for step in range(40):
            if good(L, R):
                break
            r2 = R
            while r2 < len(t) and t[r2] in " \n":
                r2 += 1
            while r2 < len(t) and t[r2] not in " \n":
                r2 += 1
            if t[b:r2].count("$") % 2 == 1:
                j = t.find("$", r2)
                if j >= 0:
                    r2 = j + 1
            if r2 > R and free(L, r2) and r2 - b < 120:
                R = r2
                continue
            l2 = L
            while l2 > 0 and t[l2 - 1] in " \n":
                l2 -= 1
            while l2 > 0 and t[l2 - 1] not in " \n":
                l2 -= 1
            if t[l2:a].count("$") % 2 == 1:
                j = t.rfind("$", 0, l2)
                if j >= 0:
                    l2 = j
            if l2 < L and free(l2, R) and a - l2 < 120:
                L = l2
                continue
            break
        old = t[L:R]
        unique_ok = t.count(old) == 1 and old.count("$") % 2 == 0
        if not unique_ok or not free(L, R):
            sys.exit("could not place category fix on p.%d: %r" % (p, old))
        taken.append((L, R))
        catspans.append((L, R))
        letters = re.findall(r"\\mathcal\s*([CK])('*)", old)
        lab = ", ".join(c + pr for c, pr in letters)
        F.append({"page": p, "where": "category letter(s) " + lab + " in '" + old.replace("\n", " ") + "'",
                  "scan": "bold italic " + lab, "tex": r"\mathcal " + lab, "kind": "font",
                  "convention": None, "confidence": "high",
                  "fix": {"old": old, "new": conv_cat(old)},
                  "note": "Category letters are printed bold italic (enlarged crops pp. 41, 44); \\mathcal gives calligraphic letters. \\boldsymbol as for the category K in ega0-1-fr.tex.",
                  "_outside": False})

# ---------------- checks ----------------
ok = True
for d in F:
    if d["fix"] is None:
        continue
    o = d["fix"]["old"]
    if d["_outside"]:
        n = srctext.count(o)
        if n != 1:
            print("OUTSIDE fix not unique in source:", d["page"], repr(o), n); ok = False
        continue
    n = pages[d["page"]].count(o)
    if n != 1:
        print("NOT UNIQUE/ABSENT:", d["page"], n, repr(o)); ok = False
# overlaps and order-independence
for p in range(40, 45):
    fx = [d["fix"] for d in F if d["page"] == p and d["fix"] and not d["_outside"]]
    sp = sorted((pages[p].find(f["old"]), pages[p].find(f["old"]) + len(f["old"]), f["old"]) for f in fx)
    for (a1, b1, o1), (a2, b2, o2) in zip(sp, sp[1:]):
        if a2 < b1:
            print("OVERLAP p.%d:" % p, repr(o1), repr(o2)); ok = False
    for trial in range(30):
        order = fx[:]
        random.Random(trial).shuffle(order)
        t = pages[p]
        for f in order:
            if t.count(f["old"]) != 1:
                print("ORDER PROBLEM p.%d:" % p, repr(f["old"])); ok = False; break
            t = t.replace(f["old"], f["new"], 1)
    # brace / math balance before and after applying all
    t = pages[p]
    for f in fx:
        t = t.replace(f["old"], f["new"], 1)
    def stats(s):
        b = re.sub(r"\\[{}$]", "", s)
        return (b.count("{") - b.count("}"), b.count("$") % 2, s.count("\\[") - s.count("\\]"),
                s.count("\\begin{") - s.count("\\end{"))
    print("p.%d before %s after %s  ({-}, $ parity, \\[-\\], begin-end)" % (p, stats(pages[p]), stats(t)))
    with open(RUN + r"\crops_040_044\page_%03d_fixed.tex" % p, "w", encoding="utf-8", newline="") as fh:
        fh.write(t)

out = []
for d in F:
    e = {k: v for k, v in d.items() if k != "_outside"}
    if "corrected" not in e and e["kind"] == "misprint_in_print":
        print("misprint without corrected:", e["where"]); ok = False
    out.append(e)
out.sort(key=lambda e: e["page"])
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
from collections import Counter
c = Counter((e["page"], "convention" if e["kind"] == "convention" else ("misprint" if e["kind"] == "misprint_in_print" else "normal")) for e in out)
for p in range(40, 45):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("total", len(out), "OK" if ok else "PROBLEMS")
