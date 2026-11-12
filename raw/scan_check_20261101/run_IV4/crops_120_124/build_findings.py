"""Build findings_120_124.json and check every fix 'old' against the page files and the current source."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions"
                   r"\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex")
OUT = RUN / "findings_120_124.json"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


N = "\n"
G16 = "GLOBAL_ISSUES 16."
REF_I = "Genuine EGA I reference (bold I)."
BOLDP = "Bold italic P in the print (crop p123_s2_P.png)."

# ---------------------------------------------------------------- p. 120
add(120, "top of p. 120: page break 119/120 inside '... autrement dit la A-algèbre B est | isomorphe à A[T]/F.A[T]'",
    "p. 120 begins mid-sentence with 'isomorphe à' at the left margin, no indent",
    r"blank line after \oldpage[IV-4]{120}: a paragraph break inside the sentence",
    "marker", None, "high",
    r"\oldpage[IV-4]{120}" + N + N + "isomorphe à",
    r"\oldpage[IV-4]{120}" + N + "isomorphe à",
    r"The marker is at the right place. The blank line before it is already removed; this removes the one after it (\oldpage ends with \ignorespaces, which does not skip a \par).")

add(120, "Théorème (18.4.6), label '(i)'",
    "upright (i) inside the italic statement (crop p120_s1_i.png)",
    r"\item[(i)] (italic in the theorem)",
    "convention", 6, "high",
    r"\item[(i)] Soient $f:X\to Y$ un morphisme localement de type fini, $x$ un point de $X$, $y=f(x)$",
    r"\item[\textup{(i)}] Soient $f:X\to Y$ un morphisme localement de type fini, $x$ un point de $X$, $y=f(x)$",
    G16)

add(120, "Théorème (18.4.6) (i): 'formellement étale (resp. formellement non ramifiée), il faut'",
    "'(resp.' and ')' upright, 'formellement non ramifiée' italic (crop p120_s1_resp1.png)",
    "all italic",
    "convention", 6, "high",
    r"formellement étale (resp. formellement non ramifiée), il faut",
    r"formellement étale \textup{(resp.} formellement non ramifiée\textup{)}, il faut",
    "As in Proposition (18.4.5), p. 119.")

add(120, "Théorème (18.4.6) (i): '(resp. d'une algèbre quotient B de A[T]/F.A[T])'",
    "'(resp.' and ')' upright, 'd'une algèbre quotient' and 'de' italic (crops p120_s1_resp2.png, p120_s1_resp2b.png)",
    "all italic",
    "convention", 6, "high",
    r"(resp. d'une algèbre quotient $B$ de $A[T]/F.A[T]$)",
    r"\textup{(resp.} d'une algèbre quotient $B$ de $A[T]/F.A[T]$\textup{)}")

add(120, "Théorème (18.4.6), label '(ii)'",
    "upright (ii) (crop p120_s2_ii.png)",
    r"\item[(ii)] (italic)",
    "convention", 6, "high",
    r"\item[(ii)] Supposons en outre que $f$ soit localement de présentation finie",
    r"\item[\textup{(ii)}] Supposons en outre que $f$ soit localement de présentation finie",
    G16)

add(120, "proof of (18.4.6): 'les idéaux maximaux de l'anneau semi-local C autres que r'",
    "'autres que': both words italic (crop p120_s2_autres2.png)",
    r"\emph{autres} que: only 'autres' italic",
    "italics", None, "high",
    r"\emph{autres} que $\mathfrak r$",
    r"\emph{autres que} $\mathfrak r$")

add(120, "proof of (18.4.6), second paragraph: 'Pour traiter le cas où O_{X,y} est une A-algèbre'",
    "O with subscript 'X, y' (crop p120_s3_Oxy.png)",
    r"$\sh{O}_{X,x}$ (silent correction)",
    "misprint_in_print", None, "high",
    r"Pour traiter le cas où $\sh{O}_{X,x}$",
    r"Pour traiter le cas où $\sh{O}_{X,y}$",
    "The local ring of X at the point x is meant (y is a point of Y). The fix restores the printed y. No erratum in Liste 3.",
    r"\sh{O}_{X,x}")

add(120, "same sentence: '... est une A-algèbre formellement ramifiée, il suffira de prouver'",
    "'formellement ramifiée' (no 'non')",
    "'formellement ramifiée' (the printed reading is kept)",
    "misprint_in_print", None, "high",
    None, None,
    "The case treated is the formally unramified one (the 'resp.' case of (18.4.6, (i)); the sentence goes on 'B_n sera alors formellement non ramifié sur A'). The TeX keeps the printed reading. No erratum in Liste 3.",
    "formellement non ramifiée")

add(120, "same paragraph: 'il suffira de prouver que B_n est isomorphe à C_r ;'",
    "'isomorphe à' italic (crop p120_s3_isom2.png)",
    "upright",
    "italics", None, "high",
    r"est isomorphe à $C_{\mathfrak r}$; en effet",
    r"est \emph{isomorphe à} $C_{\mathfrak r}$; en effet")

add(120, "proof of Lemme (18.4.6.1): 'Posons R = B—n,'",
    "long dash (set difference)",
    "minus sign",
    "convention", 7, "high",
    r"$R=B-\mathfrak n$",
    r"$R=B\setmin\mathfrak n$",
    r"Set difference (convention 7 proper); \setmin as in the earlier IV-4 fixes.")

add(120, "same sentence: 'S = C—r,'",
    "long dash (set difference)",
    "minus sign",
    "convention", 7, "high",
    r"$S=C-\mathfrak r$",
    r"$S=C\setmin\mathfrak r$",
    r"Set difference (convention 7 proper); \setmin as in the earlier IV-4 fixes.")

add(120, "same sentence: 'l'homomorphisme canonique B_r → C_r peut s'écrire comme le composé'",
    "B with the subscript Fraktur r (crop p120_s3_Br.png; the B_n just before is p120_s3_Bn.png)",
    r"$B_{\mathfrak n}$ (silent correction)",
    "misprint_in_print", None, "high",
    r"$B_{\mathfrak n}\to C_{\mathfrak r}$ peut",
    r"$B_{\mathfrak r}\to C_{\mathfrak r}$ peut",
    "The canonical homomorphism B_n → C_r of the lemma is meant (the composite R^{-1}B → R^{-1}C → S^{-1}C). The fix restores the printed r.",
    r"B_{\mathfrak n}\to C_{\mathfrak r}")

add(120, "page break 120/121 inside 'l'image réciproque de p dans | R^{-1}B = B_n est l'unique idéal maximal'",
    "p. 120 ends 'de p dans'; p. 121 continues the sentence at the left margin, no indent",
    r"blank line before \oldpage[IV-4]{121} (and another after it): a paragraph break inside the sentence",
    "marker", None, "high",
    r"l'image réciproque de $\mathfrak p$ dans" + N + N,
    r"l'image réciproque de $\mathfrak p$ dans" + N,
    r"The marker is at the right place. Part 1 of 2: the first p. 121 finding removes the blank line after \oldpage[IV-4]{121}; apply both.")

# ---------------------------------------------------------------- p. 121
add(121, "top of p. 121: 'R^{-1}B = B_n est l'unique idéal maximal'",
    "continuation of the sentence, no indent",
    r"blank line after \oldpage[IV-4]{121}",
    "marker", None, "high",
    r"\oldpage[IV-4]{121}" + N + N + r"$R^{-1}B",
    r"\oldpage[IV-4]{121}" + N + r"$R^{-1}B",
    "Part 2 of 2 with the last p. 120 finding; both blank lines must go.")

add(121, "'l'homomorphisme g : R^{-1}B → R^{-1}C est injectif (0_I, 1.3.2)'",
    "bold 0 with subscript I",
    "plain 0",
    "convention", 2, "high",
    r"injectif ($0_{\mathrm I}$, 1.3.2)",
    r"injectif ($\mathbf{0}_{\mathrm I}$, 1.3.2)")

add(121, "'il suffit de prouver que l'homomorphisme R^{-1}B/mR^{-1}B → R^{-1}C/mR^{-1}C est surjectif.'",
    "the formula is set in the line: it starts a text line and 'est surjectif. Mais en vertu de la première partie de' follows on the same line",
    r"displayed with \[ ... \]",
    "other", None, "high",
    "l'homomorphisme" + N + r"\[" + N + r"  R^{-1}B/\mathfrak mR^{-1}B\longrightarrow R^{-1}C/\mathfrak mR^{-1}C" + N + r"\]" + N + "est surjectif.",
    r"l'homomorphisme $R^{-1}B/\mathfrak mR^{-1}B\to R^{-1}C/\mathfrak mR^{-1}C$ est surjectif.",
    "Display vs inline only; no connecting word lost or added.")

add(121, "'on peut supposer que X est un voisinage de n dans Spec(B) (1.7.2).'",
    "'(1.7.2)': light old-style 1 followed by a full stop (crop p121_s2_172.png)",
    "(I, 7.2)",
    "number", None, "high",
    r"dans $\Spec(B)$ (I, 7.2).",
    r"dans $\Spec(B)$ (1.7.2).",
    "EGA IV's own (1.7.2) (it improves (I, 6.5.1, (ii)), which is cited beside it at the foot of the page), misread as an EGA I reference; compare the bold I with a comma in '(I, 6.5.1, (ii))' (crop p121_s4_refs.png). GLOBAL_ISSUES 78 pattern.")

add(121, "'Posons B' = Spec(A[T]/F.A[T]) et soit n' l'image réciproque de n dans B''",
    "B' = Spec(A[T]/F.A[T])",
    r"$B'=\Spec(A[T]/F.A[T])$ (the printed reading is kept)",
    "misprint_in_print", None, "medium",
    None, None,
    "B' is used as a ring in what follows (Spec(B') → Spec(A), the image of F'(T) in B', B'_{n'}), so B' = A[T]/F.A[T] is meant: an authors' slip. The TeX keeps it. No erratum in Liste 3.",
    r"B'=A[T]/F.A[T]")

add(121, "'cela ne peut avoir lieu que si cet homomorphisme est bijectif (0, 19.10.3, (i))'",
    "bare bold 0",
    "plain 0",
    "convention", 2, "high",
    r"\emph{bijectif} (0, 19.10.3, (i))",
    r"\emph{bijectif} (\textbf{0}, 19.10.3, (i))")

add(121, "proof of (18.4.7): 'S'il en est ainsi, on peut appliquer (18.4.6, (i)) ;'",
    "(18.4.6, (i)) (crop p121_s3_1846i.png)",
    "(18.4.6, (ii))",
    "number", None, "high",
    r"on peut appliquer (18.4.6, (ii));",
    r"on peut appliquer (18.4.6, (i));",
    "The TeX changes the printed (i) to (ii). The print is right: the formally unramified case is part (i) of (18.4.6). Same change on p. 122.")

add(121, "'le morphisme h : X' → Y correspondant à l'homomorphisme canonique R → R[T]/G.R[T] est étale au point x, donc'",
    "x without a prime (crop p121_s4_x.png); the comma follows the x directly",
    "$x'$ (silent correction)",
    "misprint_in_print", None, "high",
    r"est étale au point $x'$, donc",
    r"est étale au point $x$, donc",
    "h : X' → Y is étale at the point x' of X' (by (18.4.2); the next clause restricts X' to a neighbourhood of x'). The fix restores the printed x.",
    "x'")

add(121, "'D'autre part, en vertu de (I, 6.5.1, (ii)) et de (1.7.2)'",
    "bold I",
    "plain I",
    "convention", 2, "high",
    r"en vertu de (I, 6.5.1, (ii))",
    r"en vertu de (\textbf{I}, 6.5.1, (ii))",
    REF_I + " Adjacent to (not overlapping) the next finding.")

add(121, "same sentence: '... et de (1.7.2), il résulte du fait que'",
    "'(1.7.2)': light old-style 1 followed by a full stop (crop p121_s4_refs.png)",
    "(I, 7.2)",
    "number", None, "high",
    r"et de (I, 7.2), il résulte",
    r"et de (1.7.2), il résulte",
    "EGA IV's own (1.7.2), which deals with (I, 6.5.1, (ii)), as earlier on this page.")

add(121, "page break 121/122 inside 'que cet homomorphisme correspond à un mor-|phisme j : U → X''",
    "p. 121 ends with the hyphenated 'mor-'; p. 122 begins 'phisme j : U → X'' at the left margin",
    r"blank line before \oldpage[IV-4]{122} (and another after it): a paragraph break inside the sentence",
    "marker", None, "high",
    "correspond à un morphisme" + N + N,
    "correspond à un morphisme" + N,
    r"The marker stands after the whole word 'morphisme' (the print breaks inside the word). Part 1 of 2: the first p. 122 finding removes the blank line after \oldpage[IV-4]{122}; apply both.")

# ---------------------------------------------------------------- p. 122
add(122, "top of p. 122: '(mor)phisme j : U → X' d'un voisinage ouvert'",
    "continuation of the sentence, no indent",
    r"blank line after \oldpage[IV-4]{122}",
    "marker", None, "high",
    r"\oldpage[IV-4]{122}" + N + N + r"$j:U\to X'$",
    r"\oldpage[IV-4]{122}" + N + r"$j:U\to X'$",
    "Part 2 of 2 with the last p. 121 finding; both blank lines must go.")

add(122, "'d'un voisinage ouvert U de x dans X' ; restreignant au besoin U'",
    "X' with a prime (crop p122_s1_dansX2.png)",
    "$X$ (silent correction)",
    "misprint_in_print", None, "high",
    r"de $x$ dans $X$; restreignant",
    r"de $x$ dans $X'$; restreignant",
    "U is an open neighbourhood of the point x of X (f|U follows). The fix restores the printed X'.",
    "X")

add(122, "'en appliquant (I, 6.5.1, (i)), supposer que h∘j = f|U'",
    "bold I",
    "plain I",
    "convention", 2, "high",
    r"en appliquant (I, 6.5.1, (i))",
    r"en appliquant (\textbf{I}, 6.5.1, (i))",
    REF_I)

add(122, "'donc j est de type fini (I, 6.3.4, (v))'",
    "bold I",
    "plain I",
    "convention", 2, "high",
    r"de type fini (I, 6.3.4, (v))",
    r"de type fini (\textbf{I}, 6.3.4, (v))",
    REF_I)

add(122, "'l'homomorphisme φ est surjectif par (18.4.6, (i))'",
    "(18.4.6, (i)) (crop p122_s1_refs.png)",
    "(18.4.6, (ii))",
    "number", None, "high",
    r"surjectif par (18.4.6, (ii))",
    r"surjectif par (18.4.6, (i))",
    "As on p. 121: the TeX changes the printed (i) to (ii); the print is right (B is a quotient of A[T]/F.A[T] by (18.4.6, (i))).")

add(122, "'donc il résulte de (I, 6.5.4, (i)) qu'on peut'",
    "bold I",
    "plain I",
    "convention", 2, "high",
    r"il résulte de (I, 6.5.4, (i))",
    r"il résulte de (\textbf{I}, 6.5.4, (i))",
    REF_I)

add(122, "Corollaire (18.4.8): 'Pour que f soit non ramifié (resp. étale), il faut'",
    "'(resp.' and ')' upright, 'étale' italic (crop p122_s1_resp_etale.png)",
    "all italic",
    "convention", 6, "high",
    r"non ramifié (resp. étale), il faut et il suffit qu'il existe une famille",
    r"non ramifié \textup{(resp.} étale\textup{)}, il faut et il suffit qu'il existe une famille")

add(122, "Corollaire (18.4.8): 'soit une immersion fermée (resp. ouverte).'",
    "'(resp.' and ')' upright, 'ouverte' italic (crop p122_s2_resp_ouverte.png)",
    "all italic",
    "convention", 6, "high",
    r"fermée (resp. ouverte). On peut",
    r"fermée \textup{(resp.} ouverte\textup{)}. On peut")

add(122, "proof of (18.4.8), last paragraph: 'en chaque point de g'(U_α), donc dans X tout entier puisque les g'(U_α) recouvrent X'",
    "g' without the index α, twice",
    r"$g'(U_\alpha)$ twice (the printed reading is kept)",
    "misprint_in_print", None, "medium",
    None, None,
    "The projections are g'_α (statement of (18.4.8)); the index is dropped twice. The TeX keeps the printed reading.",
    r"g'_\alpha(U_\alpha)")

add(122, "Proposition (18.4.9), label 'a)'",
    "upright a) inside the italic statement (crop p122_s3_ab_list.png)",
    r"\item[a)] (italic)",
    "convention", 6, "high",
    r"\item[a)] $h$ est étale au point $y$ et $g$ est plat",
    r"\item[\textup{a)}] $h$ est étale au point $y$ et $g$ est plat",
    "GLOBAL_ISSUES 88 (hand-set labels in italic statements, same as item 16).")

add(122, "Proposition (18.4.9), label 'b)'",
    "upright b) (crop p122_s3_ab_list.png)",
    r"\item[b)] (italic)",
    "convention", 6, "high",
    r"\item[b)] $h$ est non ramifié au point $y$ et $f$ est plat",
    r"\item[\textup{b)}] $h$ est non ramifié au point $y$ et $f$ est plat",
    "GLOBAL_ISSUES 88.")

add(122, "'Comme f = h∘g, a) entraîne que f est plat'",
    "label a) wholly italic, parenthesis included (crop p122_s3_ab_run.png)",
    "$a)$: italic letter, upright parenthesis",
    "italics", None, "high",
    r"Comme $f=h\circ g$, $a)$ entraîne",
    r"Comme $f=h\circ g$, \emph{a)} entraîne",
    "Labels in roman text are italic in the print (GLOBAL_ISSUES 88).")

add(122, "'donc a) implique b).'",
    "labels a) and b) wholly italic (crop p122_s3_ab_run.png)",
    "$a)$, $b)$: italic letters, upright parentheses",
    "italics", None, "high",
    r"donc $a)$ implique $b)$.",
    r"donc \emph{a)} implique \emph{b)}.",
    "GLOBAL_ISSUES 88; two labels, one edit.")

add(122, "'Pour prouver que b) entraîne a), on peut d'abord supposer'",
    "labels b) and a) wholly italic (crop p122_s3_ba_run.png)",
    "$b)$, $a)$: italic letters, upright parentheses",
    "italics", None, "high",
    r"Pour prouver que $b)$ entraîne $a)$, on peut d'abord",
    r"Pour prouver que \emph{b)} entraîne \emph{a)}, on peut d'abord",
    "GLOBAL_ISSUES 88; two labels, one edit.")

add(122, "page break 122/123 inside 'au cas où h est une immersion fermée | de présentation finie, f étant supposé plat'",
    "p. 122 ends 'immersion fermée' (no stop); p. 123 continues the sentence at the left margin, no indent",
    r"blank line before \oldpage[IV-4]{123} (and another after it): a paragraph break inside the sentence",
    "marker", None, "high",
    r"une \emph{immersion fermée}" + N + N,
    r"une \emph{immersion fermée}" + N,
    r"The marker is at the right place. Part 1 of 2: the first p. 123 finding removes the blank line after \oldpage[IV-4]{123}; apply both.")

# ---------------------------------------------------------------- p. 123
add(123, "top of p. 123: 'de présentation finie, f étant supposé plat au point x.'",
    "continuation of the sentence, no indent (roman 'de présentation finie', as in the TeX)",
    r"blank line after \oldpage[IV-4]{123}",
    "marker", None, "high",
    r"\oldpage[IV-4]{123}" + N + N + "de présentation finie",
    r"\oldpage[IV-4]{123}" + N + "de présentation finie",
    "Part 2 of 2 with the last p. 122 finding; both blank lines must go.")

add(123, "'l'homomorphisme O_{S,s} → O_{X,x} est injectif (0_I, 6.5.1)'",
    "bold 0 with subscript I",
    "plain 0",
    "convention", 2, "high",
    r"injectif ($0_{\mathrm I}$, 6.5.1);",
    r"injectif ($\mathbf{0}_{\mathrm I}$, 6.5.1);")

add(123, "'tel que J|U = 0 (0_I, 5.2.2)'",
    "bold 0 with subscript I",
    "plain 0",
    "convention", 2, "high",
    r"$\mathscr J|U=0$ ($0_{\mathrm I}$, 5.2.2)",
    r"$\mathscr J|U=0$ ($\mathbf{0}_{\mathrm I}$, 5.2.2)")

add(123, "Proposition (18.4.10): 'Désignons par P(f, x) une propriété'",
    "bold italic P (crop p123_s1_P.png)",
    r"\mathbf P",
    "convention", 10, "high",
    r"Désignons par $\mathbf P(f,x)$",
    r"Désignons par $\boldsymbol{P}(f,x)$")

add(123, "(18.4.10) 1°: 'tout isomorphisme local h : Y → Z, P(f, x) est équivalente'",
    "bold italic P",
    r"\mathbf P",
    "convention", 10, "high",
    r"$h:Y\to Z$, $\mathbf P(f,x)$",
    r"$h:Y\to Z$, $\boldsymbol{P}(f,x)$",
    BOLDP)

add(123, "(18.4.10) 1°: 'est équivalente à P(h∘f, x) pour x ∈ X'",
    "bold italic P",
    r"\mathbf P",
    "convention", 10, "high",
    r"$\mathbf P(h\circ f,x)$",
    r"$\boldsymbol{P}(h\circ f,x)$",
    BOLDP)

add(123, "(18.4.10) 2°: 'les propriétés P(f, x) et P(f', x')' (first P)",
    "bold italic P",
    r"\mathbf P",
    "convention", 10, "high",
    r"au-dessus de $x$, les propriétés $\mathbf P(f,x)$",
    r"au-dessus de $x$, les propriétés $\boldsymbol{P}(f,x)$",
    BOLDP)

add(123, "(18.4.10) 2°: '... et P(f', x') sont équivalentes' (second P)",
    "bold italic P",
    r"\mathbf P",
    "convention", 10, "high",
    r"$\mathbf P(f',x')$ sont équivalentes",
    r"$\boldsymbol{P}(f',x')$ sont équivalentes",
    BOLDP)

add(123, "(18.4.10): 'Alors les propriétés P(f, x) et P(g, x)' (first P)",
    "bold italic P",
    r"\mathbf P",
    "convention", 10, "high",
    r"Alors les propriétés $\mathbf P(f,x)$",
    r"Alors les propriétés $\boldsymbol{P}(f,x)$",
    BOLDP)

add(123, "(18.4.10): '... et P(g, x) sont équivalentes.' (second P)",
    "bold italic P",
    r"\mathbf P",
    "convention", 10, "high",
    r"$\mathbf P(g,x)$ sont équivalentes.",
    r"$\boldsymbol{P}(g,x)$ sont équivalentes.",
    BOLDP)

add(123, "(18.4.10) 2°: 'sont équivalentes (« invariance par changement de base étale »).'",
    "the whole parenthesis is roman (crop p123_s2_invariance.png)",
    "italic (inside the proposition)",
    "convention", 6, "high",
    r"(« invariance par changement de base étale »)",
    r"\textup{(« invariance par changement de base étale »)}")

add(123, "(18.4.10): 'Soient alors S un préschéma, ...' after the conditions 1°, 2°",
    "'Soient alors' begins an indented new paragraph (same indent as 1°, 2°)",
    r"text follows \end{enumerate} without a blank line, so it is set without an indent",
    "other", None, "high",
    r"\end{enumerate}" + N + r"Soient alors $S$",
    r"\end{enumerate}" + N + N + r"Soient alors $S$",
    "GLOBAL_ISSUES 80/99 pattern. The proposition's italic shape continues across the paragraph break (the environment group is still open).")

add(123, "proof of (18.4.10): 'P(f', x') (resp. P(g', x'))' (first P)",
    "bold italic P (crop p123_s2_P.png)",
    r"\mathbf P",
    "convention", 10, "high",
    r"$\mathbf P(f',x')$ (resp.",
    r"$\boldsymbol{P}(f',x')$ (resp.")

add(123, "proof of (18.4.10): '(resp. P(g', x'))' (second P)",
    "bold italic P (crop p123_s2_P.png)",
    r"\mathbf P",
    "convention", 10, "high",
    r"$\mathbf P(g',x')$)",
    r"$\boldsymbol{P}(g',x')$)")

add(123, "proof of (18.4.10): 'est alors par hypothèse équivalente à P(f, x)'",
    "bold italic P",
    r"\mathbf P",
    "convention", 10, "high",
    r"équivalente à $\mathbf P(f,x)$",
    r"équivalente à $\boldsymbol{P}(f,x)$",
    BOLDP)

add(123, "proof of (18.4.10): '(resp. P(g, x)). On peut donc'",
    "bold italic P",
    r"\mathbf P",
    "convention", 10, "high",
    r"(resp. $\mathbf P(g,x)$)",
    r"(resp. $\boldsymbol{P}(g,x)$)",
    BOLDP)

add(123, "proof of (18.4.10): 'Comme l'hypothèse entraîne que P(g, x) est alors équivalente'",
    "bold italic P",
    r"\mathbf P",
    "convention", 10, "high",
    r"que $\mathbf P(g,x)$ est alors",
    r"que $\boldsymbol{P}(g,x)$ est alors",
    BOLDP)

add(123, "proof of (18.4.10): '... équivalente à P(h∘g, x), on en déduit la conclusion'",
    "bold italic P",
    r"\mathbf P",
    "convention", 10, "high",
    r"$\mathbf P(h\circ g,x)$",
    r"$\boldsymbol{P}(h\circ g,x)$",
    BOLDP)

add(123, "heading of (18.4.11)",
    "'Exemples (18.4.11). — On peut prendre ...' (italic 'Exemples', number after it, roman body)",
    r"\begin{env}[18.4.11] ... \emph{Exemples.} --- gives '(18.4.11) Exemples. —'",
    "other", None, "high",
    r"\begin{env}[18.4.11]" + N + r"\label{IV.18.4.11}" + N + r"\emph{Exemples.} --- On peut",
    r"\begin{examples}[18.4.11]" + N + r"\label{IV.18.4.11}" + N + "On peut",
    r"Use the preamble's plural examples environment ('Exemples (…). —', roman body), as the print shows. Part 1 of 2 with the next-but-one finding (\end{env} -> \end{examples}); apply both.")

add(123, "(18.4.11): 'On peut prendre pour propriété P(f, x) l'une quelconque'",
    "bold italic P (crop p123_s3_P.png)",
    r"\mathbf P",
    "convention", 10, "high",
    r"pour propriété $\mathbf P(f,x)$",
    r"pour propriété $\boldsymbol{P}(f,x)$")

add(123, "end of (18.4.11)",
    "-",
    r"\end{env}",
    "other", None, "high",
    r"étale au point $x$ (17.7.4)." + N + r"\end{enumerate}" + N + r"\end{env}",
    r"étale au point $x$ (17.7.4)." + N + r"\end{enumerate}" + N + r"\end{examples}",
    r"Part 2 of 2 with the heading finding (\begin{env}[18.4.11] -> \begin{examples}[18.4.11]); apply both.")

# ---------------------------------------------------------------- p. 124
add(124, "Corollaire (18.4.12), label '(i)'",
    "upright (i)",
    r"\item[(i)] (italic)",
    "convention", 6, "high",
    r"\item[(i)] Soient $f:X\to Y$ un morphisme localement de type fini, $x$ un point de $X$. Si",
    r"\item[\textup{(i)}] Soient $f:X\to Y$ un morphisme localement de type fini, $x$ un point de $X$. Si",
    G16)

add(124, "Corollaire (18.4.12) (i): 'h un morphisme étale (18.4.7), l'homomorphisme'",
    "upright (18.4.7) (crop p124_s1_18_4_7.png)",
    "italic",
    "convention", 6, "high",
    r"un morphisme étale (18.4.7), l'homomorphisme",
    r"un morphisme étale \textup{(18.4.7)}, l'homomorphisme",
    "Printed upright inside the italic statement.")

add(124, "Corollaire (18.4.12) (i): '(en particulier O_{X,x} est une O_{Y,f(x)}-algèbre essentiellement étale (18.6.1))'",
    "the parenthesis is roman except 'essentiellement étale', which is italic (crops p124_s1_enpart.png, p124_s1_essent.png)",
    r"the parenthesis italic, \emph{essentiellement étale} upright (inside the corollary)",
    "convention", 6, "high",
    r"(en particulier $\sh{O}_{X,x}$ est une $\sh{O}_{Y,f(x)}$-algèbre \emph{essentiellement étale} (18.6.1))",
    r"\textup{(en particulier $\sh{O}_{X,x}$ est une $\sh{O}_{Y,f(x)}$-algèbre \emph{essentiellement étale} (18.6.1))}",
    r"Inside \textup the \emph gives italic, as printed.")

add(124, "Corollaire (18.4.12), label '(ii)'",
    "upright (ii)",
    r"\item[(ii)] (italic)",
    "convention", 6, "high",
    r"\item[(ii)] Pour qu'un morphisme $f:X\to Y$ soit étale",
    r"\item[\textup{(ii)}] Pour qu'un morphisme $f:X\to Y$ soit étale",
    G16)

add(124, "proof of (18.4.12) (i): 'ou seulement plat (0_I, 6.5.1 et 6.6.2)'",
    "bold 0 with subscript I",
    "plain 0",
    "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.5.1 et 6.6.2)",
    r"($\mathbf{0}_{\mathrm I}$, 6.5.1 et 6.6.2)")

add(124, "proof of (18.4.13): 'puisque A' est réduit (I, 1.2.7)'",
    "bold I (crop p124_s4_I127.png)",
    "plain I",
    "convention", 2, "high",
    r"réduit (I, 1.2.7)",
    r"réduit (\textbf{I}, 1.2.7)",
    REF_I)

# ---------------------------------------------------------------- checks
src = SRC.read_bytes().decode("utf-8")
assert "\r" not in src
pages = {}
for n in range(120, 125):
    pages[n] = (RUN / f"page_{n:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")

bad = 0
for i, d in enumerate(F):
    if d["fix"] is None:
        continue
    old, new = d["fix"]["old"], d["fix"]["new"]
    cp = pages[d["page"]].count(old)
    cs = src.count(old)
    if cp != 1 or cs != 1 or old == new:
        bad += 1
        print(f"#{i} p{d['page']}: page count {cp}, source count {cs}: {old[:80]!r}")

# overlaps between fixes on the same page (by source position)
spans = []
for i, d in enumerate(F):
    if d["fix"] is None:
        continue
    pos = src.find(d["fix"]["old"])
    spans.append((pos, pos + len(d["fix"]["old"]), i))
spans.sort()
for a, b in zip(spans, spans[1:]):
    if b[0] < a[1]:
        print("OVERLAP:", a, b)

# simulate applying all fixes to the source (in order) to make sure each still applies
sim = src
for i, d in enumerate(F):
    if d["fix"] is None:
        continue
    if sim.count(d["fix"]["old"]) != 1:
        print(f"apply problem #{i}: count {sim.count(d['fix']['old'])}")
        bad += 1
        continue
    sim = sim.replace(d["fix"]["old"], d["fix"]["new"], 1)

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("findings:", len(F), "problems:", bad)
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0, 0])
    if d["kind"] == "convention":
        c[1] += 1
    elif d["kind"] == "misprint_in_print":
        c[2] += 1
    else:
        c[0] += 1
print(counts)

# preview of the simulated segment for pp. 120-124
a = sim.index(r"\oldpage[IV-4]{120}")
b = sim.index(r"\oldpage[IV-4]{125}")
(RUN / "crops_120_124" / "applied_preview.txt").write_text(sim[a - 200:b + 40], encoding="utf-8")
