import json

OUT = r"user\Documents\ega_scan_check_20261101\run_0IV1\findings_126_130.json"


def N(s):
    return None if s is None else s.replace("⏎", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, nofix=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if nofix else {"old": N(old), "new": N(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = N(corrected)
    d["note"] = note
    F.append(d)


W33 = "Wavy arrow, not a maps-to arrow (GLOBAL_ISSUES 33)."
C7 = "Long dash used for a subtraction (GLOBAL_ISSUES 23); \\setmin as in the earlier 0_IV fixes, pending the convention-7 decision."

# ---------------- p. 126 ----------------
add(126, "proof of (20.4.8) (i), line 2: 'l'application z ⇝ (ε(z), z—p₁(ε(z)))'",
    "z ⇝ (ε(z), …: wavy arrow (crop)", r"$z\mapsto(\varepsilon(z),…", "symbol", None, "high",
    r"$z\mapsto(", r"$z\leadsto(", W33)
add(126, "same formula: 'z—p₁(ε(z))'",
    "long dash for the minus sign (crop: longer than the bar of + in p₁(b)+x)", r"z-p_1(\varepsilon(z))",
    "convention", 7, "high", r",z-p_1(", r",z\setmin p_1(", C7)
add(126, "proof of (20.4.8) (i), line 2: 'l'isomorphisme réciproque l'application (b, x) ⇝ p₁(b)+x'",
    "(b, x) ⇝ p₁(b)+x: wavy arrow (crop)", r"$(b,x)\mapsto p_1(b)+x$", "symbol", None, "high",
    r"$(b,x)\mapsto p_1(b)+x$", r"$(b,x)\leadsto p_1(b)+x$", W33)
add(126, "proof of (20.4.8), line 14: 'Comme on a p₂=p₁—d_{B/A} par définition'",
    "long dash for the minus sign (crop)", r"$p_2=p_1-d_{B/A}$", "convention", 7, "high",
    r"$p_2=p_1-d_{B/A}$", r"$p_2=p_1\setmin d_{B/A}$", C7)
add(126, "proof of (20.4.8), line 14 of p. 126: 'Comme on a p₂=p₁—d_{B/A} par définition'",
    "p₂=p₁—d_{B/A}", r"$p_2=p_1\setmin d_{B/A}$ (printed reading kept)", "misprint_in_print", None, "high",
    None, None,
    "Authors' errata Err_IV 13 (EGA IV part 4, Errata et addenda liste 3, B) Modifications de texte): 'Dans (0_IV, 20.4.8), "
    "ligne 14 de la p. 126, remplacer p_2=p_1-d_{B/A} par p_1=p_2-d_{B/A}.' An authors' correction (sign convention "
    "d_{B/A}=p_2-p_1, see the p. 125 finding on Err_IV 12), not a typesetting slip. The TeX keeps the printed reading; "
    "the corrected edition (r20 current) still has p_2=p_1-d_{B/A}. 'tex' is the text after the convention-7 fix just above; "
    "apply that first.",
    corrected=r"$p_1=p_2\setmin d_{B/A}$", nofix=True)
add(126, "proof of (20.4.8): 'homomorphisme continu de A-algèbres j : b ⇝ (b, 0)'",
    "j : b ⇝ (b, 0): wavy arrow (crop)", r"$j:b\mapsto(b,0)$", "symbol", None, "high",
    r"$j:b\mapsto(b,0)$", r"$j:b\leadsto(b,0)$", W33)
add(126, "proof of (20.4.8): '(𝟎_I, 7.7.6)'",
    "bold 0 with a light roman subscript I (crop)", r"$\mathbf{0_I}$ (subscript I bold too)", "font", None, "high",
    r"($\mathbf{0_I}$, 7.7.6)", r"($\mathbf{0}_{\mathrm I}$, 7.7.6)",
    "Same form as the earlier 0_IV fixes ($\\mathbf{0}_{\\mathrm I}$).")
add(126, "proof of (20.4.8), second diagram: label w of the diagonal arrow B⊗_A B → D_B(L)",
    "w set to the left of the short diagonal arrow, i.e. on its lower-left side (crop)",
    r"\ar[dr]^w (label on the upper-right side)", "formula", None, "medium",
    r"\ar[dr]^w", r"\ar[dr]_w",
    "Label side only. The other labels of both diagrams (u, p_2, v, j_1, j_2, j, u) are on the printed sides.")
add(126, "proof of (20.4.8): 'w(b⊗1—1⊗b)'",
    "long dash for the minus sign (crop)", r"b\otimes1-1\otimes b", "convention", 7, "high",
    r"b\otimes1-1\otimes b", r"b\otimes1\setmin 1\otimes b", C7)
add(126, "same formula: '=j(b)—u(b)∈L'",
    "long dash for the minus sign (crop)", r"j(b)-u(b)", "convention", 7, "high",
    r"j(b)-u(b)", r"j(b)\setmin u(b)", C7)
add(126, "Théorème (20.4.9): 'est formellement projectif.'",
    "'formellement projectif' italic like the rest of the statement (no change of face)",
    r"\emph{formellement projectif} (upright inside the itshape theorem)", "convention", 6, "high",
    r"\emph{formellement projectif}", r"formellement projectif", "Printed italic words left upright.")
add(126, "proof of (20.4.9): 'formellement lisse (19.3.5, (iii))'",
    "(19.3.5, (iii))", r"\sref{0.19.3.5-fr}, (iii), which prints (19.3.5), (iii)", "punctuation", None, "high",
    r"\sref{0.19.3.5-fr}, (iii)", r"(\ref{0.19.3.5-fr}, (iii))",
    "\\sref{X} expands to (\\ref{X}); same fix as on pp. 132 and 146.")
add(126, "proof of (20.4.9): 'formellement lisse (19.3.5, (ii)); comme B'",
    "(19.3.5, (ii))", r"\sref{0.19.3.5-fr}, (ii), which prints (19.3.5), (ii)", "punctuation", None, "high",
    r"\sref{0.19.3.5-fr}, (ii) ;", r"(\ref{0.19.3.5-fr}, (ii)) ;",
    "As the previous finding.")

# ---------------- p. 127 ----------------
add(127, "Corollaire (20.4.10): 'pour tout idéal ouvert 𝔎 de B, Ω¹_{B/A}⊗_B(B/𝔎)=Ω¹_{B/A}/𝔎.Ω¹_{B/A} est un (B/𝔎)-module'",
    "Fraktur K 𝔎, four times (crop: same glyph as the 𝔎 of 0_IV p. 52)", r"\mathfrak{R} (four times)",
    "symbol", None, "high",
    r"ouvert $\mathfrak{R}$ de $B$,⏎$\Omega^1_{B/A}\otimes_B(B/\mathfrak{R})⏎=\Omega^1_{B/A}/\mathfrak{R}.\Omega^1_{B/A}$ est un⏎$(B/\mathfrak{R})$-module",
    r"ouvert $\mathfrak{K}$ de $B$,⏎$\Omega^1_{B/A}\otimes_B(B/\mathfrak{K})⏎=\Omega^1_{B/A}/\mathfrak{K}.\Omega^1_{B/A}$ est un⏎$(B/\mathfrak{K})$-module",
    "Wrong letter (GLOBAL_ISSUES 63); the four occurrences in one edit.")
add(127, "proof of (20.4.11): 'comme B/𝔟 est un anneau artinien'",
    "'artinien' italic (crop)", "artinien upright", "italics", None, "high",
    r"un anneau artinien, tout", r"un anneau \emph{artinien}, tout", "")
add(127, "proof of (20.4.11): '(𝟎_III, 10.1.3)'",
    "bold 0 with a light roman subscript III (crop)", r"$\mathbf{0_{III}}$ (subscript bold too)", "font", None, "high",
    r"($\mathbf{0_{III}}$, 10.1.3)", r"($\mathbf{0}_{\mathrm{III}}$, 10.1.3)",
    "Same form as the earlier 0_IV fixes.")
add(127, "Exemples (20.4.13) (i): 'Ω¹_{B/A} est un B-module libre, dont'",
    "'libre' italic (crop)", "libre upright", "italics", None, "high",
    r"$B$-module libre, dont", r"$B$-module \emph{libre}, dont", "")
add(127, "Exemples (20.4.13) (i): 'dont les dX_α forment une base.'",
    "'base' italic (crop)", "base upright", "italics", None, "high",
    r"forment une⏎  base. En effet", r"forment une⏎  \emph{base}. En effet", "")
add(127, "Exemples (20.4.13) (ii): 'l'homomorphisme canonique x ⇝ d_{B/A}x de L dans Ω¹_{B/A}'",
    "x ⇝ d_{B/A}x: wavy arrow (crop)", r"$x\mapsto d_{B/A}x$", "symbol", None, "high",
    r"$x\mapsto d_{B/A}x$", r"$x\leadsto d_{B/A}x$", W33)
add(127, "Exemples (20.4.13) (ii): 'il est immédiat que les B-dérivations de B=D_A(L) dans un B-module M'",
    "les B-dérivations (crop)", r"les $B$-dérivations (printed reading kept)", "misprint_in_print", None, "medium",
    None, None,
    "B-linear derivations of B are zero, and the conclusion by (20.4.8, (ii)) concerns A-derivations, so the intended word is "
    "A-dérivations (not in the IV part 4 errata). Even so corrected, (ii) is false in general: an A-derivation "
    "(b,x)⇝u(x) must also satisfy (0,x).u(x')+(0,x').u(x)=0 in M, and x⇝d_{B/A}x is not surjective: for A a field of "
    "characteristic ≠ 2 and L=A², B=A[ε₁,ε₂]/(ε₁,ε₂)², Ω¹_{B/A} has dimension 3 (basis dε₁, dε₂, ε₂dε₁) and L dimension 2.",
    corrected=r"les $A$-dérivations de $B=D_A(L)$", nofix=True)
add(127, "Exemples (20.4.13) (ii): 'les applications de la forme (b, x) ⇝ u(x)'",
    "(b, x) ⇝ u(x): wavy arrow (crop)", r"$(b,x)\mapsto u(x)$", "symbol", None, "high",
    r"$(b,x)\mapsto u(x)$", r"$(b,x)\leadsto u(x)$", W33)
add(127, "Exemples (20.4.13) (ii): 'on conclut donc par (20.4.8, (ii)).'",
    "(20.4.8, (ii)).", r"\sref{0.20.4.8-fr}, (ii)., which prints (20.4.8), (ii).", "punctuation", None, "high",
    r"\sref{0.20.4.8-fr}, (ii).", r"(\ref{0.20.4.8-fr}, (ii)).",
    "\\sref{X} expands to (\\ref{X}); same fix as on pp. 132 and 146.")
add(127, "Exemples (20.4.13) (iv): 'soit une extension séparable de celui de A'",
    "'séparable' italic (crop)", "séparable upright", "italics", None, "high",
    r"extension séparable de celui", r"extension \emph{séparable} de celui", "")
add(127, "Exemples (20.4.13) (iv), lines 6 to 11 from the bottom of p. 127 (the whole item)",
    "(iv) Soient A, B deux anneaux intègres tels que A⊂B, que A soit intégralement clos, B entier sur A, … le polynôme "
    "minimal de x … est un polynôme f(T) appartenant à A[T]; … de la relation f(x)=0 que f'(x)d_{B/A}x=0, d'où notre "
    "assertion en vertu de (20.4.7).",
    "printed text kept", "misprint_in_print", None, "high", None, None,
    "Authors' errata Err_IV 14 (EGA IV part 4, liste 3, B) Modifications de texte): 'Dans (0_IV, 20.4.13), remplacer les "
    "lignes 6 à 11 du bas de la p. 127 par le texte suivant'; lines 6-11 from the bottom are exactly item (iv). "
    "'corrected' is that text as transcribed in ega4-errata-addenda-list3-fr.tex ('af[T]' there; probably af(T) in the "
    "print of the errata). An authors' correction, not a typesetting slip; the TeX and the corrected edition (r20 current) "
    "keep the printed (iv). The \\emph{séparable} fix above concerns the printed text.",
    corrected=r"\item[\rm(iv)] Soient $A$, $B$ deux anneaux intègres tels que $A\subset B$, $B$ étant entier sur $A$, et que le corps des fractions de $B$ soit une extension séparable de celui de $A$. Alors le $B$-module $\Omega^1_{B/A}$ est un module de torsion. En effet, pour tout $x\in B$, soit $f$ le polynôme minimal de $x$ par rapport au corps des fractions $K$ de $A$ ; il existe $a\in A$ non nul tel que $af[T]\in A[T]$ ; comme $x$ est séparable sur $K$, on a $f'(x)\neq0$, et d'autre part de la relation $af(x)=0$ on déduit $af'(x)d_{B/A}x=0$, d'où notre assertion en vertu de \sref{0.20.4.7-fr}.",
    nofix=True)
add(127, "heading 20.5 (printed at the top of p. 128): 'Propriétés fonctorielles fondamentales de Ω¹_{B/A}.'",
    "the title ends with a full stop", "no full stop in the \\subsection title", "punctuation", None, "high",
    r"{Omega1(B/A)}}⏎\label{subsection:0.20.5-fr}", r"{Omega1(B/A)}.}⏎\label{subsection:0.20.5-fr}",
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop). Apply before the next finding: after the marker "
    "move this line belongs to the p. 128 segment.")
add(127, "page break 127/128: heading 20.5",
    "p. 127 ends with Remarques (20.4.14) ('… d'ordre n ».'); the heading '20.5. Propriétés fonctorielles fondamentales "
    "de Ω¹_{B/A}.' opens p. 128",
    "\\subsection{…} and its \\label stand before \\oldpage[0\\textsubscript{IV-1}]{128}", "marker", None, "high",
    r"\end{remarks}⏎⏎\subsection{Propriétés fonctorielles fondamentales de",
    r"\end{remarks}⏎⏎\oldpage[0\textsubscript{IV-1}]{128}⏎⏎\subsection{Propriétés fonctorielles fondamentales de",
    "Marker move, part 1 of 2: insert the p. 128 marker before the heading; the p. 128 marker finding removes the old "
    "marker. Apply after the full-stop fix above.")

# ---------------- p. 128 ----------------
add(128, "top of p. 128: heading 20.5 and (20.5.1)",
    "p. 128 begins with the heading 20.5, then (20.5.1)",
    "\\oldpage[0\\textsubscript{IV-1}]{128} stands after the heading, before \\begin{env}[20.5.1]", "marker", None, "high",
    r"\oldpage[0\textsubscript{IV-1}]{128}⏎\begin{env}[20.5.1]", r"\begin{env}[20.5.1]",
    "Marker move, part 2 of 2: removes the old marker; apply together with the p. 127 marker finding.")
add(128, "diagram (20.5.2.1): bottom arrow B → C",
    "label u below the arrow (crop)", r"\ar[r]^u (label above)", "formula", None, "high",
    r"B \ar[r]^u & C⏎}", r"B \ar[r]_u & C⏎}", "Label side.")
add(128, "diagram after (20.5.2.2) (P¹_{B/A} → P¹_{C/A} over B → C): bottom arrow",
    "label u below the arrow (crop)", r"\ar[r]^u (label above)", "formula", None, "high",
    r"\ar[u]^{p_1} \ar[r]^u & C", r"\ar[u]^{p_1} \ar[r]_u & C", "Label side.")

# ---------------- p. 129 ----------------
add(129, "diagram (20.5.2.5), printed at the bottom of p. 128: bottom arrow B → C",
    "label u below the arrow (crop)", r"\ar[r]^u (label above)", "formula", None, "high",
    r"B \ar[u]^{p_2} \ar[r]^u & C \ar[u]_{p_2}", r"B \ar[u]^{p_2} \ar[r]_u & C \ar[u]_{p_2}",
    "Label side. Apply before the two marker findings below (afterwards this line lies in the p. 128 segment).")
add(129, "page break 128/129: after the diagram (20.5.2.5)",
    "p. 128 ends with 'En outre, comme le diagramme' and the diagram (20.5.2.5); p. 129 begins 'est aussi commutatif, "
    "on en déduit que le diagramme'",
    "\\oldpage[0\\textsubscript{IV-1}]{129} stands before 'En outre, comme le diagramme'", "marker", None, "high",
    r"\label{0.20.5.2.5-fr}⏎\]⏎est aussi commutatif",
    r"\label{0.20.5.2.5-fr}⏎\]⏎\oldpage[0\textsubscript{IV-1}]{129}⏎est aussi commutatif",
    "Marker move, part 1 of 2: insert the marker here first; the next finding removes the old one (with the old marker "
    "removed first, p. 129 cannot be located).")
add(129, "old place of the p. 129 marker: before 'En outre, comme le diagramme'",
    "'En outre, comme le diagramme' and (20.5.2.5) are printed on p. 128",
    "\\oldpage[0\\textsubscript{IV-1}]{129} before them", "marker", None, "high",
    r"\oldpage[0\textsubscript{IV-1}]{129}⏎En outre, comme le diagramme", r"En outre, comme le diagramme",
    "Marker move, part 2 of 2: remove the old marker after the insertion above.")
add(129, "diagram (20.5.2.6): label of the top arrow Ω¹_{B/A} → Ω¹_{C/A}",
    "u' (one prime; crop)", r"\ar[r]^{u''} (silently corrected)", "misprint_in_print", None, "high",
    r"\ar[r]^{u''}", r"\ar[r]^{u'}",
    "The arrow is u'', the restriction of u' to Ω¹_{B/A} (20.5.2.3); compare v_{C/B/A} in (20.5.3.5). Not in the IV part 4 "
    "errata. The diplomatic text keeps the printed u'.",
    corrected=r"\ar[r]^{u''}")
add(129, "diagram (20.5.2.6): bottom arrow B → C",
    "label u below the arrow (crop)", r"\ar[r]^u (label above)", "formula", None, "high",
    r"\ar[u]^{d_{B/A}} \ar[r]^u & C", r"\ar[u]^{d_{B/A}} \ar[r]_u & C", "Label side.")
add(129, "(20.5.2.7): '(u_{C/B/A}⊗1_D)'",
    "1_D: the identity, figure one (old-style 1; crop)", r"\mathrm{I}_D (capital I)", "symbol", None, "high",
    r"\otimes\mathrm{I}_D)", r"\otimes1_D)",
    "Identity 1_X as elsewhere in EGA (lining 1 in the labels 1_C, 1_{B'} on pp. 129-130; same fix as 1_{A'} on p. 131).")
add(129, "diagram (20.5.3.1): bottom arrow C → C",
    "label 1_C (figure one) below the arrow (crop)", r"\ar[r]^{\mathrm{I}_C} (capital I, label above)", "formula", None, "high",
    r"C \ar[r]^{\mathrm{I}_C} & C⏎}", r"C \ar[r]_{1_C} & C⏎}",
    "Two differences in one edit: the identity 1_C written \\mathrm{I}_C, and the label side.")
add(129, "diagram after (20.5.3.2) (P¹_{C/A} → P¹_{C/B} over C → C): bottom arrow",
    "label 1_C below the arrow (crop)", r"\ar[r]^{\mathrm{I}_C} (capital I, label above)", "formula", None, "high",
    r"\ar[u]^{p_1} \ar[r]^{\mathrm{I}_C}", r"\ar[u]^{p_1} \ar[r]_{1_C}",
    "Two differences in one edit: 1_C for \\mathrm{I}_C, and the label side.")
add(129, "end of (20.5.3): 'qui est un homomorphisme de C-modules.'",
    "'homomorphisme de C-modules' italic (C roman)", "upright", "italics", None, "high",
    r"qui est un homomorphisme de $C$-modules.", r"qui est un \emph{homomorphisme de $C$-modules}.",
    "Same form as \\emph{homomorphisme de $C$-modules} before (20.5.2.4).")

# ---------------- p. 130 ----------------
add(130, "diagram (20.5.3.4): bottom arrow C → C",
    "label 1_C below the arrow (crop)", r"\ar[r]^{\mathrm{I}_C} (capital I, label above)", "formula", None, "high",
    r"C \ar[u]^{p_2} \ar[r]^{\mathrm{I}_C}", r"C \ar[u]^{p_2} \ar[r]_{1_C}",
    "Two differences in one edit: 1_C for \\mathrm{I}_C, and the label side.")
add(130, "diagram (20.5.3.5): bottom arrow C → C",
    "label 1_C below the arrow", r"\ar[r]^{\mathrm{I}_C} (capital I, label above)", "formula", None, "high",
    r"\ar[u]^{d_{C/A}} \ar[r]^{\mathrm{I}_C}", r"\ar[u]^{d_{C/A}} \ar[r]_{1_C}",
    "Two differences in one edit: 1_C for \\mathrm{I}_C, and the label side.")
add(130, "diagram in (20.5.4): bottom arrow A → A'",
    "label u below the arrow (crop)", r"\ar[r]^u (label above)", "formula", None, "high",
    r"A \ar[u]^f \ar[r]^u & A'", r"A \ar[u]^f \ar[r]_u & A'", "Label side.")
add(130, "(20.5.4): 'par composition, un homomorphisme de B'-modules'",
    "'modules' italic, B' roman; 'un homomorphisme de' upright (crop)", "upright", "italics", None, "high",
    r"un homomorphisme de $B'$-modules", r"un homomorphisme de \emph{$B'$-modules}", "")
add(130, "diagram (20.5.4.2): bottom arrow B' → B'",
    "label 1_{B'} below the arrow (crop)", r"\ar[r]^{\mathrm{I}_{B'}} (capital I, label above)", "formula", None, "high",
    r"\ar[r]^{\mathrm{I}_{B'}}", r"\ar[r]_{1_{B'}}",
    "Two differences in one edit: 1_{B'} for \\mathrm{I}_{B'}, and the label side.")
add(130, "(20.5.4.3), line 5 from the bottom of p. 130: 'Ω¹_{B/A} → Ω_{B'/A'}.'",
    "Ω_{B'/A'} without the superscript 1 (crop)", r"\Omega^1_{B'/A'} (silently corrected)", "misprint_in_print", None, "high",
    r"\to\Omega^1_{B'/A'}.", r"\to\Omega_{B'/A'}.",
    "Authors' errata (EGA IV part 4, liste 3, A) Erreurs typographiques): '(0_IV, 20.5.4). Ligne 5 du bas de la p. 130, "
    "remplacer Ω_{B'/A'} par Ω¹_{B'/A'}.' The diplomatic text keeps the printed reading.",
    corrected=r"\to\Omega^1_{B'/A'}.")
add(130, "Proposition (20.5.5): 'l'homomorphisme canonique (20.5.4.1)'",
    "reference upright inside the italic statement (crop)", "\\sref italic inside the proposition environment",
    "convention", 6, "high",
    r"canonique \sref{0.20.5.4.1-fr}", r"canonique \textup{\sref{0.20.5.4.1-fr}}", "")
add(130, "Proposition (20.5.5): 'l'homomorphisme canonique (20.5.4.1).' before the display (20.5.5.1)",
    "a full stop after (20.5.4.1), although the sentence goes on with (20.5.5.1) and 'est bijectif.' (crop)",
    "no full stop (silently corrected)", "misprint_in_print", None, "high",
    r"}⏎\begin{equation}⏎\tag{20.5.5.1}", r"}.⏎\begin{equation}⏎\tag{20.5.5.1}",
    "Stray full stop inside the statement; not in the IV part 4 errata. The edit adds only the stop and does not "
    "overlap the convention-6 edit above.",
    corrected=r"l'homomorphisme canonique \sref{0.20.5.4.1-fr}" + "⏎" + r"\begin{equation}")

json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(F), "findings written")
