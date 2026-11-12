"""Build findings_115_119.json for EGA IV-3 pp. 115-119 and check every fix's 'old' against page_NNN.tex.
'<NL>' in the strings below stands for a line break."""
import json
import pathlib

run = pathlib.Path(__file__).resolve().parent.parent
OUT = run / "findings_115_119.json"


def N(s):
    return None if s is None else s.replace("<NL>", "\n")


F = []


def add(page, where, scan, tex, kind, conv, old, new, note="", conf="high"):
    fix = None if old is None else {"old": N(old), "new": N(new)}
    F.append({"page": page, "where": where, "scan": scan, "tex": N(tex), "kind": kind, "convention": conv,
              "confidence": conf, "fix": fix, "note": note})


C7 = "\\setmin pending the convention-7 decision (FIX_POLICY 2.7)."
C7SUB = "Subtraction, not set difference (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision."
WAVY = "Wavy arrow (GLOBAL_ISSUES 33), written \\leadsto as in the earlier page fixes; not convention 3."

# ---------------- page 115 (ega4-10-fr.tex) ----------------
add(115, "(10.10.2), l. 3: 'Considérons en particulier un corps algébriquement clos k; Spm(k)'",
    "'corps algébriquement clos k' italic (enlarged crop)", "roman", "italics", None,
    r"un corps algébriquement clos $k$~;", r"un \emph{corps algébriquement clos $k$}~;")
add(115, "(10.10.2): 'il en est de même de X×_Z Y (1.3.4), donc en vertu de (10.9.6)'",
    "'(1.3.4)': old-style figure 1, light face, full stops between the numbers (enlarged crop); a reference to (1.3.4) of this chapter",
    r"(\textbf I, 3.4)", "number", None,
    r"(\textbf I, 3.4)", r"(1.3.4)",
    "The TeX read the old-style figure 1 as a bold chapter numeral I.")
add(115, "(10.10.3), l. 2: 'entre points fermés de X,'",
    "only 'points fermés' italic; 'de X' roman (enlarged crop)", r"\emph{points fermés de $X$}: 'de' italic",
    "italics", None, r"\emph{points fermés de $X$}", r"\emph{points fermés} de $X$")
add(115, "(10.10.3): 'l'ensemble sous-jacent au produit X'×_k Y' est identique à l'ensemble produit X'×Y''",
    "'est identique à l'ensemble produit' all italic (enlarged crop)", "only 'ensemble produit' italic",
    "italics", None, r"est identique à l'\emph{ensemble produit}", r"\emph{est identique à l'ensemble produit}")
add(115, "(10.10.3): 'la topologie de l'espace sous-jacent à X'×_k Y' n'est pas la topologie produit'",
    "'n'est pas la topologie produit' all italic (enlarged crop)", "only 'topologie produit' italic",
    "italics", None, r"n'est pas la \emph{topologie produit}", r"\emph{n'est pas la topologie produit}")
add(115, "(10.10.3), 2nd paragraph: 'tel que φ(x—λ.1) appartienne'",
    "long dash for the subtraction x—λ.1 (enlarged crop)", r"$\varphi(x-\lambda.1)$", "convention", 7,
    r"$\varphi(x-\lambda.1)$", r"$\varphi(x\setmin\lambda.1)$", C7SUB)
add(115, "(10.10.3), 2nd paragraph: 'puisque x—λ.1 est inversible dans A'",
    "long dash for the subtraction x—λ.1 (enlarged crop)", r"$x-\lambda.1$", "convention", 7,
    r"puisque $x-\lambda.1$", r"puisque $x\setmin\lambda.1$", C7SUB)
add(115, "(10.10.3): 'tout morphisme X'→Y' d'espaces k-annelés est aussi un morphisme'",
    "'espaces k-annelés' italic (enlarged crop)", "roman", "italics", None,
    r"d'espaces $k$-annelés est aussi", r"d'\emph{espaces $k$-annelés} est aussi")
add(115, "(10.10.3): 'un morphisme d'espaces k-annelés en anneaux locaux (I, 1.8.2; cf. Err_II)'",
    "'espaces k-annelés en anneaux locaux' italic (enlarged crop)", "roman", "italics", None,
    r"d'espaces $k$-annelés en anneaux locaux", r"d'\emph{espaces $k$-annelés en anneaux locaux}")
add(115, "(10.10.3): '(I, 1.8.2; cf. Err_II)'",
    "'Err' bold, subscript II roman (enlarged crop)", r"$\mathrm{Err}_{\mathrm{II}}$", "font", None,
    r"$\mathrm{Err}_{\mathrm{II}}$", r"$\mathbf{Err}_{\mathrm{II}}$",
    "The edition writes \\mathbf{Err} elsewhere (1,277 times).")
add(115, "(10.10.3): 'donc tout morphisme X'→Y' de k-espaces annelés'",
    "'tout' italic (enlarged crop)", "roman", "italics", None,
    r"donc tout morphisme", r"donc \emph{tout} morphisme")
add(115, "(10.10.3): 'où f : X→Y est un morphisme de k-préschémas.'",
    "'morphisme de k-préschémas' italic (enlarged crop)", "roman", "italics", None,
    r"est un<NL>morphisme de $k$-préschémas.", r"est un<NL>\emph{morphisme de $k$-préschémas}.")
add(115, "(10.10.3), last paragraph: 'une application s̄ : x ⇝ s(x) de U dans k'",
    "wavy arrow (enlarged crop)", r"\mapsto", "symbol", None,
    r"$\overline s:x\mapsto s(x)$", r"$\overline s:x\leadsto s(x)$", WAVY)
add(115, "(10.10.3), last paragraph: 'du faisceau 𝒜(X') des germes d'applications de X' dans k;'",
    "'faisceau 𝒜(X') des germes d'applications de X' dans k' italic (enlarged crop)", "roman", "italics", None,
    r"du faisceau $\mathcal A(X')$<NL>des germes d'applications de $X'$ dans $k$~;",
    r"du \emph{faisceau $\mathcal A(X')$<NL>des germes d'applications de $X'$ dans $k$}~;")
add(115, "(10.10.3), last paragraph: 'comme l'application h_U : s ⇝ s̄'",
    "wavy arrow (enlarged crop)", r"\mapsto", "symbol", None,
    r"$h_U:s\mapsto\overline s$", r"$h_U:s\leadsto\overline s$", WAVY)
add(115, "(10.10.3), last paragraph: 'un homomorphisme de faisceaux d'anneaux h : 𝒪_X' → 𝒜(X')'",
    "'faisceaux d'anneaux' italic (enlarged crop)", "roman", "italics", None,
    r"de faisceaux d'anneaux $h:", r"de \emph{faisceaux d'anneaux} $h:")
add(115, "(10.10.3), end: 'il faut et il suffit par suite que A soit réduit.'",
    "'réduit' italic (enlarged crop)", "roman", "italics", None,
    r"que $A$ soit réduit.", r"que $A$ soit \emph{réduit}.")
add(115, "(10.10.4): 'chacun de ses anneaux locaux 𝒪_x (pour x∈X') est réduit.'",
    "'réduit' italic (enlarged crop; the earlier 'X' est réduit' of the same sentence is roman)", "roman",
    "italics", None, r"$x\in X'$) est réduit.", r"$x\in X'$) est \emph{réduit}.")
add(115, "(10.10.4): 'il faut et il suffit que X' soit réduit. Dans (FAC)'",
    "'réduit' italic (enlarged crop)", "roman", "italics", None,
    r"suffit que $X'$ soit réduit.", r"suffit que $X'$ soit \emph{réduit}.")
add(115, "(10.10.4), end: 'ne considère que des espaces préalgébriques quasi-compacts)'",
    "'quasi-compacts' italic (enlarged crop)", "roman", "italics", None,
    r"préalgébriques quasi-compacts)", r"préalgébriques \emph{quasi-compacts})")

# ---------------- page 116 (ega4-10-fr.tex, then ega4-11-fr.tex before its first marker) ----------------
add(116, "(10.10.5), l. 1: 'sur un corps k quelconque en conservant'",
    "'quelconque' italic (enlarged crop)", "roman", "italics", None,
    r"$k$<NL>quelconque en conservant", r"$k$<NL>\emph{quelconque} en conservant")
add(116, "(10.10.5), l. 3: 'une extension algébriquement close fixe K de k'",
    "'fixe' italic (enlarged crop)", "roman", "italics", None,
    r"close fixe $K$", r"close \emph{fixe} $K$")
add(116, "(10.10.5): 'au sens de Weil). A tout préschéma X'",
    "capital A without accent (enlarged crop)", "À tout", "word", None,
    r"Weil). À tout", r"Weil). A tout",
    "As the page fixes for EGA II pp. 17, 29, 0_III p. 27 and III p. 219.")
add(116, "(10.10.5): 'des germes d'applications de X' dans K)'",
    "'dans' italic (enlarged crop)", "roman", "italics", None,
    r"de $X'$ dans $K$)", r"de $X'$ \emph{dans} $K$)")
add(116, "page break 116/117: '(11.3.1) un résultat souvent utilisé | par la suite, impliquant que'",
    "the sentence runs on: p. 117 begins 'par la suite' flush left, no paragraph break",
    "blank line after 'souvent utilisé', before \\oldpage[IV-3]{117} (a paragraph break)", "marker", None,
    r"souvent utilisé<NL><NL>", r"souvent utilisé<NL>",
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). The blank line is the last line of "
    "ega4-11-fr.tex's text before its first marker (appended to page 116); after the p. 117 marker there is no "
    "blank line.")

# ---------------- page 117 (ega4-11-fr.tex) ----------------
add(117, "(11.1.1.1): 'Alors il existe g∈B—q tel que,'",
    "long dash for the set difference B—q (enlarged crop)", r"$g\in B-\mathfrak q$", "convention", 7,
    r"$g\in B-\mathfrak q$ tel que,", r"$g\in B\setmin\mathfrak q$ tel que,", C7)
add(117, "(11.1.1.1), end: '(il revient d'ailleurs au même (0_I, 6.3.1) de dire que M_q' est un A-module plat).'",
    "the parenthesis is roman, only 'module plat' italic (enlarged crop)",
    "inside the \\emph that wraps the whole statement: all italic", "convention", 6,
    r"dans $A$ (il revient d'ailleurs au même<NL>($\mathbf 0_{\mathrm I}$, 6.3.1) de dire que $M_{\mathfrak q'}$ est un<NL>$A$-module plat).}",
    r"dans $A$} (il revient d'ailleurs au même<NL>($\mathbf 0_{\mathrm I}$, 6.3.1) de dire que $M_{\mathfrak q'}$ est un<NL>$A$-\emph{module plat}).",
    "Closes the \\emph after 'dans A' and italicizes 'module plat' only.")
add(117, "proof of (11.1.1): 'B_q' étant plat sur B, on a M_q'/pM_q' = (M/pM)_q' et'",
    "formula in the running text (enlarged crop)", "displayed \\[...\\]", "formula", None,
    r"\[<NL>  M_{\mathfrak q'}/\mathfrak pM_{\mathfrak q'}<NL>  =(M/\mathfrak pM)_{\mathfrak q'}<NL>\]",
    r"$M_{\mathfrak q'}/\mathfrak pM_{\mathfrak q'}<NL>  =(M/\mathfrak pM)_{\mathfrak q'}$",
    "The connecting words 'on a' and 'et' are kept.")
add(117, "proof of (11.1.1): 'et Tor_1^A(M_q', A/p) = (Tor_1^A(M, A/p))_q' (en définissant le Tor'",
    "formula in the running text (enlarged crop)", "displayed \\[...\\]", "formula", None,
    r"\[<NL>  \operatorname{Tor}_1^A(M_{\mathfrak q'},A/\mathfrak p)<NL>  =(\operatorname{Tor}_1^A(M,A/\mathfrak p))_{\mathfrak q'}<NL>\]",
    r"$\operatorname{Tor}_1^A(M_{\mathfrak q'},A/\mathfrak p)<NL>  =(\operatorname{Tor}_1^A(M,A/\mathfrak p))_{\mathfrak q'}$")
add(117, "proof of (11.1.1): 'B_q' est plat sur B_g, donc (M/pM)_q' = ((M/pM)_g)_{q'B_g} et'",
    "formula in the running text (enlarged crop)", "displayed \\[...\\]", "formula", None,
    r"\[<NL>  (M/\mathfrak pM)_{\mathfrak q'}<NL>  =((M/\mathfrak pM)_g)_{\mathfrak q'B_g}<NL>\]",
    r"$(M/\mathfrak pM)_{\mathfrak q'}<NL>  =((M/\mathfrak pM)_g)_{\mathfrak q'B_g}$")
add(117, "proof of (11.1.1): 'et (Tor_1^A(M, A/p))_q' = ((Tor_1^A(M, A/p))_g)_{q'B_g}, où dans ces formules'",
    "formula in the running text, comma after it (enlarged crop)", "displayed \\[...\\] with the comma inside",
    "formula", None,
    r"\[<NL>  (\operatorname{Tor}_1^A(M,A/\mathfrak p))_{\mathfrak q'}<NL>  =((\operatorname{Tor}_1^A(M,A/\mathfrak p))_g)_{\mathfrak q'B_g},<NL>\]",
    r"$(\operatorname{Tor}_1^A(M,A/\mathfrak p))_{\mathfrak q'}<NL>  =((\operatorname{Tor}_1^A(M,A/\mathfrak p))_g)_{\mathfrak q'B_g}$,")
add(117, "Lemme (11.1.1.2): 'Sous les conditions de (11.1.1.1), il existe'",
    "'(11.1.1.1)' upright in the italic statement (enlarged crop)", "italic (lemma environment)",
    "convention", 6, r"conditions de (11.1.1.1), il existe", r"conditions de \textup{(11.1.1.1)}, il existe")
add(117, "Lemme (11.1.1.2): 'il existe g∈B—q tel que :'",
    "long dash for the set difference B—q", r"$g\in B-\mathfrak q$", "convention", 7,
    r"$g\in B-\mathfrak q$ tel que~:", r"$g\in B\setmin\mathfrak q$ tel que~:", C7)
add(117, "Lemme (11.1.1.2), label (i)",
    "label (i) upright (enlarged crop)", "enumerate label=(\\roman*) inside the italic lemma environment: italic",
    "convention", 6, r"\begin{enumerate}[label=(\roman*)]", r"\begin{enumerate}[label=\textup{(\roman*)}]",
    "One edit of the label option covers (i) and (ii) (next entry). GLOBAL_ISSUES 16.")
add(117, "Lemme (11.1.1.2), label (ii)",
    "label (ii) upright", "italic (same enumerate)", "convention", 6, None, None,
    "Included in the previous edit (label=\\textup{(\\roman*)}).")

# ---------------- page 118 (ega4-11-fr.tex) ----------------
add(118, "proof of (11.1.1.2), l. 3: 'il existe un h∈A—p tel que'",
    "long dash for the set difference A—p (enlarged crop)", r"$h\in A-\mathfrak p$", "convention", 7,
    r"un $h\in A-\mathfrak p$ tel que", r"un $h\in A\setmin\mathfrak p$ tel que", C7)
add(118, "proof of (11.1.1.2): 'donc (0_I, 5.2.2) il existe g∈B—q tel que'",
    "long dash for the set difference B—q (enlarged crop)", r"$g\in B-\mathfrak q$", "convention", 7,
    r"$g\in B-\mathfrak q$ tel que", r"$g\in B\setmin\mathfrak q$ tel que", C7)
add(118, "proof of (11.1.1.2), end: 'et hg∈B—q puisque'",
    "long dash for the set difference B—q (enlarged crop)", r"$hg\in B-\mathfrak q$", "convention", 7,
    r"$hg\in B-\mathfrak q$", r"$hg\in B\setmin\mathfrak q$", C7)
add(118, "proof of (11.1.1.2), end: 'puisque h∈A—p. C.Q.F.D.'",
    "long dash for the set difference A—p (enlarged crop)", r"$h\in A-\mathfrak p$", "convention", 7,
    r"$h\in A-\mathfrak p$. C.Q.F.D.", r"$h\in A\setmin\mathfrak p$. C.Q.F.D.", C7)
add(118, "Corollaire (11.1.2): 'l'homomorphisme u_x⊗1 : ℱ'_x⊗_{𝒪_y} k(y) → ℱ_x⊗_{𝒪_y} k(y) soit injectif' (edit 1 of 2: opening)",
    "formula in the running text of the statement (enlarged crop)", "displayed \\[...\\]", "formula", None,
    r"l'homomorphisme<NL>\[<NL>  u_x\otimes1:", r"l'homomorphisme<NL>$u_x\otimes1:",
    "Apply together with the next edit (closing). The two convention-1 edits for k(y) do not overlap these two.")
add(118, "Corollaire (11.1.2) (edit 2 of 2: closing)",
    "formula in the running text of the statement", "displayed \\[...\\]", "formula", None,
    r"<NL>\]<NL>soit injectif", r"$<NL>soit injectif",
    "Apply together with the previous edit.")
add(118, "Corollaire (11.1.2): 'ℱ'_x⊗_{𝒪_y} k(y)'",
    "bold italic k (enlarged crop)", "k(y)", "convention", 1,
    r"\mathcal F'_x\otimes_{\mathcal O_y}k(y)", r"\mathcal F'_x\otimes_{\mathcal O_y}\boldsymbol{k}(y)")
add(118, "Corollaire (11.1.2): '→ ℱ_x⊗_{𝒪_y} k(y)'",
    "bold italic k (enlarged crop)", "k(y)", "convention", 1,
    r"\mathcal F_x\otimes_{\mathcal O_y}k(y)", r"\mathcal F_x\otimes_{\mathcal O_y}\boldsymbol{k}(y)")
add(118, "Corollaire (11.1.3): 'non diviseur de zéro dans 𝒪_x⊗_{𝒪_f(x)} k(f(x))'",
    "bold italic k (enlarged crop)", "k(f(x))", "convention", 1,
    r"\mathcal O_x\otimes_{\mathcal O_{f(x)}}k(f(x))", r"\mathcal O_x\otimes_{\mathcal O_{f(x)}}\boldsymbol{k}(f(x))")
add(118, "Corollaire (11.1.4): 'soit (ℱ_x⊗_{𝒪_f(x)} k(f(x)))-régulière'",
    "bold italic k (enlarged crop)", "k(f(x))", "convention", 1,
    r"\mathcal F_x\otimes_{\mathcal O_{f(x)}}k(f(x))", r"\mathcal F_x\otimes_{\mathcal O_{f(x)}}\boldsymbol{k}(f(x))")
add(118, "footnote (1), l. 2: 'il suffit de voir que b) entraîne a).'",
    "'b)' and 'a)' italic (enlarged crop)", "upright", "italics", None,
    r"voir que b) entraîne a).", r"voir que \emph{b)} entraîne \emph{a)}.")

# ---------------- page 119 (ega4-11-fr.tex) ----------------
add(119, "page break 118/119 (edit 1 of 2: insert the marker): '... que U est aussi l'ensemble des x∈X | tels que la suite (g_i)_x'",
    "printed p. 118 ends with the line 'Comme ℱ est f-plat, il résulte de (0, 15.1.16) que U est aussi l'ensemble des x∈X' "
    "(page_118_s3.png, just above the footnote rule); p. 119 begins 'tels que la suite (g_i)_x soit ℱ_x-régulière'",
    "\\oldpage[IV-3]{119} stands before 'Comme' (one printed line too early)", "marker", None,
    r"aussi l'ensemble des $x\in X$ tels", r"aussi l'ensemble des $x\in X$<NL>\oldpage[IV-3]{119}<NL>tels",
    "Inserts the marker mid-sentence on its own line, without blank lines. Apply together with the next edit, "
    "which removes the misplaced marker.")
add(119, "page break 118/119 (edit 2 of 2: remove the misplaced marker)",
    "see the previous entry", "\\oldpage[IV-3]{119} and a blank line before 'Comme'", "marker", None,
    r"\oldpage[IV-3]{119}<NL><NL>Comme", r"Comme",
    "Apply together with the previous edit. The blank line after \\end{corollary} at the end of the p. 118 segment "
    "stays, so 'Comme' still opens a paragraph, as printed; 'Comme ... l'ensemble des x∈X' then belongs to p. 118 "
    "and matches the print there.")
add(119, "first line: 'tels que la suite (g_i)_x soit ℱ_x-régulière'",
    "(g_i)_x with one pair of parentheses (enlarged crop)", r"$((g_i)_x)$", "formula", None,
    r"$((g_i)_x)$ soit", r"$(g_i)_x$ soit",
    "Not a misprint: (g_i)_x denotes the sequence; the outer parentheses are the TeX's.")
add(119, "Corollaire (11.1.5): '(i.e. tels que ℱ⊗_Y Spec(𝒪_{Y,y}) soit plat relativement au morphisme X×_Y Spec(𝒪_{Y,y})→Z)'",
    "'(i.e.' and the closing parenthesis upright, the rest italic (enlarged crops)", "all italic (corollary environment)",
    "convention", 6,
    r"(i.e. tels que<NL>$\mathcal F\otimes_Y\operatorname{Spec}(\mathcal O_{Y,y})$ soit plat<NL>relativement au morphisme<NL>$X\times_Y\operatorname{Spec}(\mathcal O_{Y,y})\to Z$) est ouvert",
    r"\textup{(i.e.} tels que<NL>$\mathcal F\otimes_Y\operatorname{Spec}(\mathcal O_{Y,y})$ soit plat<NL>relativement au morphisme<NL>$X\times_Y\operatorname{Spec}(\mathcal O_{Y,y})\to Z$\textup{)} est ouvert",
    "As the IV-2 p. 58 page fix.")
add(119, "proof of (11.1.5): 'est égal à Y—f(X—V)' (first dash)",
    "long dash for the set difference (enlarged crop)", r"$Y-f(X-V)$", "convention", 7,
    r"égal à $Y-f", r"égal à $Y\setmin f", C7)
add(119, "proof of (11.1.5): 'est égal à Y—f(X—V)' (second dash)",
    "long dash for the set difference (enlarged crop)", r"$Y-f(X-V)$", "convention", 7,
    r"(X-V)$, donc", r"(X\setmin V)$, donc", C7)
add(119, "proof of (11.1.5), end: 'les points intérieurs à W, d'où la conclusion.'",
    "'intérieurs' italic (enlarged crop)", "roman", "italics", None,
    r"les points intérieurs à $W$", r"les points \emph{intérieurs} à $W$")
add(119, "(11.2.1): 'on considère une résolution gauche de M par des A-modules libres'",
    "'libres' italic (enlarged crop); the later 'A'-modules libres' before (11.2.1.4) is roman", "roman",
    "italics", None, r"$A$-modules libres", r"$A$-modules \emph{libres}")
add(119, "(11.2.1.2): '... → L_{i+1} → L_i → ... → L_0 → M → 0'",
    "baseline dots, twice (enlarged crop)", "\\cdots twice", "symbol", None,
    r"\cdots\longrightarrow L_{i+1}\xrightarrow{f_i}L_i\longrightarrow\cdots",
    r"\ldots\longrightarrow L_{i+1}\xrightarrow{f_i}L_i\longrightarrow\ldots",
    "\\cdots where the print has baseline dots.")
add(119, "(11.2.1.3): '... → L'_{i+1} → L'_i → ... → L'_0 → M' → 0'",
    "baseline dots, twice", "\\cdots twice", "symbol", None,
    r"\cdots\longrightarrow L'_{i+1}\xrightarrow{f'_i}L'_i\longrightarrow\cdots",
    r"\ldots\longrightarrow L'_{i+1}\xrightarrow{f'_i}L'_i\longrightarrow\ldots",
    "\\cdots where the print has baseline dots.")
add(119, "(11.2.1.4): '... → L''_{i+1} → L''_i → ... → L''_0 → M' → 0'",
    "baseline dots, twice (enlarged crop)", "\\cdots twice", "symbol", None,
    r"\cdots\longrightarrow L''_{i+1}\xrightarrow{f''_i}L''_i\longrightarrow\cdots",
    r"\ldots\longrightarrow L''_{i+1}\xrightarrow{f''_i}L''_i\longrightarrow\ldots",
    "\\cdots where the print has baseline dots.")
add(119, "(11.2.1.4), end of the display",
    "no full stop after 'M' → 0' (enlarged crop); p. 120 begins a new sentence", "M'\\longrightarrow0.", "punctuation",
    None, r"M'\longrightarrow0.", r"M'\longrightarrow0")

# ---------------- checks ----------------
pages = {n: (run / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for n in range(115, 120)}
bad = 0
for i, x in enumerate(F):
    if x["fix"] is None:
        continue
    t = pages[x["page"]]
    c = t.count(x["fix"]["old"])
    if c != 1:
        bad += 1
        print("NOT UNIQUE", i, x["page"], c, repr(x["fix"]["old"][:80]))
# overlaps between fixes on the same page
for n, t in pages.items():
    spans = []
    for i, x in enumerate(F):
        if x["page"] == n and x["fix"]:
            s = t.find(x["fix"]["old"])
            spans.append((s, s + len(x["fix"]["old"]), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            bad += 1
            print("OVERLAP on page", n, a, b)
# apply all fixes in sequence to check they still apply and the result is sane
for n, t in pages.items():
    u = t
    for x in F:
        if x["page"] == n and x["fix"]:
            assert u.count(x["fix"]["old"]) == 1, (n, x["where"])
            u = u.replace(x["fix"]["old"], x["fix"]["new"])
    for a, b in [("{", "}")]:
        if u.count(a) - u.count(b) != t.count(a) - t.count(b):
            print("BRACE BALANCE CHANGED on page", n, t.count(a) - t.count(b), u.count(a) - u.count(b))
            bad += 1
    if u.count("$") % 2:
        print("ODD NUMBER OF $ on page", n)
        bad += 1
    (run / "crops_115_119" / f"after_{n:03d}.txt").write_text(u, encoding="utf-8")
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for n in range(115, 120):
    print(n, cnt[(n, "normal")], cnt[(n, "convention")], cnt[(n, "misprint")])
print("findings", len(F), "problems", bad, "->", OUT)
