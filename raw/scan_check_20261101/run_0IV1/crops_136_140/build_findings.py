"""Build findings_136_140.json; check every fix's 'old' is unique in its page_NNN.tex (LF) and that the
fixes of each page apply in the listed order. NL stands for a line break inside raw strings."""
import json, sys

BASE = r"user\Documents\ega_scan_check_20261101\run_0IV1"
SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\ega0-20-fr.tex"
OUT = BASE + r"\findings_136_140.json"


def L(s):
    return s.replace("NL", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf,
         "fix": None if old is None else {"old": L(old), "new": L(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- p. 136 ----------------
add(136, "Définition (20.6.1): 'on appelle module d'imperfection de la B-algèbre C relativement à A'",
    "only 'module d'imperfection' is upright; 'de la', '-algèbre', 'relativement à' are italic like the rest of the statement (enlarged crop)",
    r"\emph{module d'imperfection de la $B$-algèbre $C$ relativement à $A$}: the whole phrase comes out upright",
    "convention", 6, "high",
    r"\emph{module d'imperfection de la $B$-algèbre $C$ relativement àNL$A$}",
    r"\emph{module d'imperfection} de la $B$-algèbre $C$ relativement àNL$A$",
    "Printed italic words left upright: the \\emph runs past the defined term.")

add(136, "after Définition (20.6.1): 'On a donc par définition (cf. (20.5.7)) la suite exacte' and display (20.6.1.1)",
    "the statement ends at '... → Ω^1_{C/A}.'; 'On a donc par définition ...' is a new indented roman paragraph",
    "the sentence and (20.6.1.1) stand inside the italic definition environment, run on without a paragraph break",
    "other", None, "high",
    r"\to\Omega^1_{C/A}$.NLOn a donc par définition (cf. (20.5.7)) la suite exacteNL\begin{equation}NL\tag{20.6.1.1}NL\label{0.20.6.1.1-fr}NL  0\longrightarrow\Upsilon_{C/B/A}\longrightarrowNL  \Omega^1_{B/A}\otimes_B C\xrightarrow{v_{C/B/A}}NL  \Omega^1_{C/A}\xrightarrow{u_{C/B/A}}\Omega^1_{C/B}NL  \longrightarrow0.NL\end{equation}NL\end{definition}",
    r"\to\Omega^1_{C/A}$.NL\end{definition}NLNLOn a donc par définition (cf. (20.5.7)) la suite exacteNL\begin{equation}NL\tag{20.6.1.1}NL\label{0.20.6.1.1-fr}NL  0\longrightarrow\Upsilon_{C/B/A}\longrightarrowNL  \Omega^1_{B/A}\otimes_B C\xrightarrow{v_{C/B/A}}NL  \Omega^1_{C/A}\xrightarrow{u_{C/B/A}}\Omega^1_{C/B}NL  \longrightarrow0.NL\end{equation}",
    "One edit: moves \\end{definition} to the end of the printed statement and adds the paragraph break (GLOBAL_ISSUES 58, as for (16.4.5), (16.4.9)); the display itself is unchanged.")

add(136, "heading '20.6. Modules d'imperfection et homomorphismes caractéristiques.'",
    "title ends with a full stop", "no full stop", "punctuation", None, "high",
    r"\subsection{Modules d'imperfection et homomorphismes caractéristiques}",
    r"\subsection{Modules d'imperfection et homomorphismes caractéristiques.}",
    "GLOBAL_ISSUES 43/58; page-fixed as on pp. 20, 71.")

add(136, "Proposition (20.6.2): '(et en particulier si C est une B-algèbre formellement lisse)'",
    "'(et en particulier si C est une B-algèbre' upright, 'formellement lisse' italic (enlarged crop)",
    "the whole parenthesis italic (statement environment)",
    "convention", 6, "high",
    r"(et enNLparticulier si $C$ est une $B$-algèbre formellement lisse)",
    r"\textup{(et enNLparticulier si $C$ est une $B$-algèbre \emph{formellement lisse})}",
    "Roman words inside the italic statement, with the italic emphasis inside them.")

add(136, "Proposition (20.6.3): '(autrement dit, l'homomorphisme canonique ... est injectif ou encore (20.4.8), toute dérivation de k dans K se prolonge en une dérivation de K dans lui-même)'",
    "the parenthesis is upright except 'injectif' and 'se prolonge', which are italic (enlarged crop)",
    "the whole parenthesis italic (statement environment)",
    "convention", 6, "high",
    r"(autrement dit, l'homomorphisme canoniqueNL$\Omega^1_k\otimes_k K\to\Omega^1_K$ est injectif ou encore (20.4.8),NLtoute dérivation de $k$ dans $K$ se prolonge en une dérivation de $K$NLdans lui-même)",
    r"\textup{(autrement dit, l'homomorphisme canoniqueNL$\Omega^1_k\otimes_k K\to\Omega^1_K$ est \emph{injectif} ou encore (20.4.8),NLtoute dérivation de $k$ dans $K$ \emph{se prolonge} en une dérivation de $K$NLdans lui-même)}",
    "")

add(136, "proof of (20.6.3): 'ou une k-algèbre formellement lisse (19.6.1)'",
    "'formellement lisse' italic ('k-algèbre' upright; enlarged crop)", "upright", "italics", None, "high",
    r"$k$-algèbre formellement lisse (19.6.1)",
    r"$k$-algèbre \emph{formellement lisse} (19.6.1)", "")

add(136, "proof of (20.6.3): 'donc une P-algèbre formellement lisse'",
    "'algèbre formellement lisse' italic (enlarged crop)", "upright", "italics", None, "high",
    r"$P$-algèbreNLformellement lisse,",
    r"$P$-\emph{algèbreNLformellement lisse},", "")

add(136, "proof of (20.6.3): 'de dire que K est une k-algèbre formellement lisse ou une ...'",
    "'k-algèbre formellement lisse' italic (enlarged crop)", "upright", "italics", None, "high",
    r"$k$-algèbre formellement lisse ou une",
    r"$k$-\emph{algèbre formellement lisse} ou une", "")

add(136, "proof of (20.6.3): '... ou une k-algèbre formellement lisse relativement à P. Enfin'",
    "'k-algèbre formellement lisse relativement à' italic, 'P.' upright (enlarged crop)", "upright", "italics", None, "high",
    r"$k$-algèbre formellement lisseNLrelativement à $P$.",
    r"$k$-\emph{algèbre formellement lisseNLrelativement à} $P$.",
    "The next sentence 'Enfin, dire que K est une k-algèbre formellement lisse relativement à P' is upright in the print, as in the TeX.")

add(136, "page break 136/137: (20.6.4.1) ... 'd'homomorphismes d'anneaux commutatifs.'",
    "p. 137 begins flush left with 'd'homomorphismes d'anneaux commutatifs.', continuing the sentence 'Considérons un diagramme commutatif (20.6.4.1)'",
    "blank line between \\end{equation} and \\oldpage[0\\textsubscript{IV-1}]{137}: paragraph break",
    "other", None, "high",
    r"C \ar[u]^hNL}NL\end{equation}NLNL",
    r"C \ar[u]^hNL}NL\end{equation}NL",
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). The blank line is the last line of the p. 136 segment, before the p. 137 marker.")

# ---------------- p. 137 ----------------
add(137, "(20.6.4.3), bottom row, label under the arrow Ω^1_{B'/A'}⊗_{B'}C' → Ω^1_{C'/A'}",
    "v'_{C'/B'/A'} (prime on v; enlarged crop)", "v_{C'/B'/A'}", "formula", None, "high",
    r"\ar[r]_{v_{C'/B'/A'}}", r"\ar[r]_{v'_{C'/B'/A'}}",
    "The print names the maps of the primed row after u', v' of (20.6.4.1); the top row has v_{C/B/A}, u_{C/B/A} as in the TeX.")

add(137, "(20.6.4.3), bottom row, label under the arrow Ω^1_{C'/A'} → Ω^1_{C'/B'}",
    "u'_{C'/B'/A'} (prime on u; enlarged crop)", "u_{C'/B'/A'}", "formula", None, "high",
    r"\ar[r]_{u_{C'/B'/A'}}", r"\ar[r]_{u'_{C'/B'/A'}}", "As the previous finding.")

add(137, "(20.6.4): 'équivaut d'ailleurs à celle d'un C'-homomorphisme'",
    "'homomorphisme' italic (enlarged crop)", "upright", "italics", None, "high",
    r"$C'$-homomorphisme", r"$C'$-\emph{homomorphisme}", "")

add(137, "(20.6.5.1), first line 'K_0(C/B/A) = Ω^1_{C/A}'",
    "no comma at the end of the line (enlarged crop)", "comma after \\Omega^1_{C/A}", "punctuation", None, "high",
    r"&=\Omega^1_{C/A},\\", r"&=\Omega^1_{C/A}\\", "")

add(137, "(20.6.5.1), second line 'K_1(C/B/A) = Ω^1_{B/A}⊗_B C'",
    "no comma at the end (enlarged crop)", "comma after C", "punctuation", None, "high",
    r"&=\Omega^1_{B/A}\otimes_B C,", r"&=\Omega^1_{B/A}\otimes_B C", "")

add(137, "Proposition (20.6.6): 'Sous les hypothèses de (20.6.1), pour tout C-module L'",
    "reference (20.6.1) upright inside the italic statement (enlarged crop)", "italic (statement environment)",
    "convention", 6, "high",
    r"de (20.6.1), pour tout", r"de \textup{(20.6.1)}, pour tout", "")

add(137, "(20.6.6.1): 'H^0(K.(C/B/A), L) ⥲ Dér_B(C, L)'",
    "isomorphism arrow (tilde above the arrow; enlarged crop)", "\\simeq", "convention", 4, "high",
    r"&\simeq\operatorname{D\acute{e}r}_B", r"&\xrightarrow{\sim}\operatorname{D\acute{e}r}_B", "")

add(137, "(20.6.6.1), end of the line",
    "no comma after Dér_B(C, L) (enlarged crop)", "comma before \\\\", "punctuation", None, "high",
    r"(C,L),\\", r"(C,L)\\", "")

add(137, "(20.6.6.2): 'H^1(K.(C/B/A), L) ⥲ Exalcom_{B/A}(C, L).'",
    "isomorphism arrow (tilde above the arrow; enlarged crop)", "\\simeq", "convention", 4, "high",
    r"&\simeqNL  \operatorname{Exalcom}", r"&\xrightarrow{\sim}NL  \operatorname{Exalcom}", "")

add(137, "proof of (20.6.6), display: '... → 0 → Dér_A(C, L) → Dér_A(B, L) → 0 → ...', left end",
    "baseline dots (enlarged crop)", "\\cdots", "symbol", None, "high",
    r"  \cdots\longrightarrow0", r"  \ldots\longrightarrow0", "")

add(137, "same display, right end",
    "baseline dots (enlarged crop)", "\\cdots", "symbol", None, "high",
    r"0\longrightarrow\cdots", r"0\longrightarrow\ldots", "")

# ---------------- p. 138 ----------------
add(138, "(20.6.7), first display: 'α : H^i(K., L) → Hom_C(H_i(K.), L)'",
    "α without index (enlarged crop); the next display has α_1", "\\alpha_i", "formula", None, "high",
    r"\alpha_i:", r"\alpha:",
    "Not recorded as a misprint: an unindexed α for the family of maps of (M, IV, 6) is not an error; the second display specialises it as α_1.")

add(138, "(20.6.7): 'on obtient donc un C-homomorphisme canonique'",
    "'homomorphisme canonique' italic (enlarged crop)", "upright", "italics", None, "high",
    r"un $C$-homomorphisme canonique", r"un $C$-\emph{homomorphisme canonique}", "")

add(138, "Définition (20.6.8): 'qui est A-triviale (18.3.7), on appelle'",
    "reference (18.3.7) upright inside the italic statement (enlarged crop)", "italic (definition environment)",
    "convention", 6, "high",
    r"(18.3.7), on appelle", r"\textup{(18.3.7)}, on appelle", "")

add(138, "Définition (20.6.8): 'on appelle homo-|morphisme caractéristique de E' (across the p. 138/139 break)",
    "'homo-' (end of p. 138) and 'morphisme caractéristique de' (top of p. 139) italic like the rest of the statement: no change of face (enlarged crops at 3x)",
    "\\emph{homomorphisme caractéristique de $E$}: upright inside the italic definition",
    "convention", 6, "high",
    r"\emph{homomorphisme caractéristique de $E$}", r"homomorphisme caractéristique de $E$",
    "Printed italic words left upright. Apply before the marker edit that follows (its 'old' lies inside this one).")

add(138, "page break 138/139 inside Définition (20.6.8): '... on appelle homo-' | 'morphisme caractéristique de E, et on note χ_E, ...'",
    "p. 138 ends with 'on appelle homo-'; p. 139 begins 'morphisme caractéristique de E, et on note χ_E, le C-homomorphisme Υ_{C/B/A} → L, image de la classe de E par l'homomorphisme canonique (20.6.7.1).'",
    "the whole definition stands before \\oldpage[0\\textsubscript{IV-1}]{139}, which comes after \\end{definition}",
    "marker", None, "high",
    r"homomorphisme caractéristique",
    r"homo%NL\oldpage[0\textsubscript{IV-1}]{139}NLmorphisme caractéristique",
    "Move, part 1 of 2: inserts the marker at the printed word break (as homomor%|phismes, EGA III p. 126). Apply after the \\emph finding above, and together with part 2 (p. 139), which deletes the old marker.")

add(138, "Définition (20.6.8), end (printed p. 139): 'par l'homomorphisme canonique (20.6.7.1).'",
    "reference (20.6.7.1) upright inside the italic statement (enlarged crop of p. 139)", "italic (definition environment)",
    "convention", 6, "high",
    r"canonique (20.6.7.1).", r"canonique \textup{(20.6.7.1)}.",
    "Printed on p. 139; the TeX is in the p. 138 segment until the marker moves.")

# ---------------- p. 139 ----------------
add(139, "top of page_139.tex: \\oldpage[0\\textsubscript{IV-1}]{139} before 'On peut définir'",
    "p. 139 begins inside Définition (20.6.8) ('morphisme caractéristique de E, ...')",
    "\\oldpage[0\\textsubscript{IV-1}]{139} after \\end{definition}", "marker", None, "high",
    r"\oldpage[0\textsubscript{IV-1}]{139}NLOn peut définir", r"On peut définir",
    "Move, part 2 of 2: deletes the old marker; apply only together with part 1 (p. 138). The blank line after \\end{definition} stays: 'On peut définir' is a new indented paragraph in the print.")

add(139, "Proposition (20.6.9): 'qui est A-triviale (18.3.7); alors le diagramme'",
    "reference (18.3.7) upright inside the italic statement", "italic (proposition environment)",
    "convention", 6, "high",
    r"(18.3.7); alors", r"\textup{(18.3.7)}; alors", "")

add(139, "(20.6.9.1): label χ_E of the left vertical arrow",
    "χ_E to the LEFT of the arrow (enlarged crop)", "\\ar[d]^{\\chi_E}: label on the right", "other", None, "high",
    r"\ar[d]^{\chi_E}", r"\ar[d]_{\chi_E}",
    "Label side as printed (cf. GLOBAL_ISSUES 30; p. 63 fix \\ar[d]^w -> \\ar[d]_w). The middle label q_{E/B/A}⊗1_C is on the right, as in the TeX.")

add(139, "(20.6.9.1): label of the right vertical arrow Ω^1_{C/A} → Ω^1_{C/A}",
    "'≀ 1' beside the arrow, on the right: isomorphism sign and the label 1 (enlarged crop)", "label '1' only",
    "symbol", None, "high",
    r"\Omega^1_{C/A} \ar[d]^{1}", r"\Omega^1_{C/A} \ar[d]^{\wr 1}",
    "The isomorphism sign is missing; set beside the arrow as in the print (cf. GLOBAL_ISSUES 64).")

add(139, "proof of (20.6.9): 'est donc contenue dans le noyau L de p_{C/B/A}. D'autre part'",
    "p_{C/B/A} (enlarged crop)", "p_{C/E/A}", "misprint_in_print", None, "high",
    r"$p_{C/E/A}$. D'autre", r"$p_{C/B/A}$. D'autre",
    "Misprint: the map whose kernel is L is p_{C/E/A} of the bottom row of (20.6.9.1) (B plays no role in it). The TeX silently corrects it; the fix restores the printed reading.",
    corrected=r"p_{C/E/A}")

add(139, "proof of (20.6.9): 'on a q_{E/B/A}(d_{B/A}(b)) = d_{E/A}(q(b)) = d_{E/A}(h(v(b))) + d_{E/A}(j(f(d_{B/A}(b)))) pour b∈B'",
    "the formula is inline, in the running line (enlarged crop)", "displayed with \\[ ... \\]", "other", None, "high",
    r"on aNL\[NL  q_{E/B/A}(d_{B/A}(b))=d_{E/A}(q(b))NL  =d_{E/A}(h(v(b)))+d_{E/A}(j(f(d_{B/A}(b))))NL\]NLpour $b\in B$.",
    r"on aNL$q_{E/B/A}(d_{B/A}(b))=d_{E/A}(q(b))=d_{E/A}(h(v(b)))+d_{E/A}(j(f(d_{B/A}(b))))$NLpour $b\in B$.",
    "Layout only (display vs inline, GLOBAL_ISSUES 21); the formula and the connecting words match.")

add(139, "proof of (20.6.9): 'Dans la première somme, on a ...' after the first display",
    "new indented paragraph", "no blank line after \\]", "other", None, "high",
    r"\]NLDans la première somme", r"\]NLNLDans la première somme",
    "Paragraph break as printed (GLOBAL_ISSUES 47).")

add(139, "proof of (20.6.9), last display: '... = δ_{C/E/A}(f(z))'",
    "no comma at the end of the display (enlarged crop)", "comma after (f(z))", "punctuation", None, "high",
    r"=\delta_{C/E/A}(f(z)),", r"=\delta_{C/E/A}(f(z))", "")

add(139, "after the proof of (20.6.9): 'permettrait encore de définir χ_E comme'",
    "'définir' italic (enlarged crop)", "upright", "italics", None, "high",
    r"de définir $\chi_E$", r"de \emph{définir} $\chi_E$", "")

FRAK_NOTE = ("Fraktur K misread as R: the glyph is the 𝔎 of p. 71 and pp. 80-85 (looped top-left stroke), unlike the "
             "Fraktur R of the radical ℜ(A), 0_I p. 12 (compared on enlarged crops). GLOBAL_ISSUES 63.")
add(139, "Corollaire (20.6.10): 'Si K est un idéal de B'", "Fraktur K", "\\mathfrak{R}", "symbol", None, "high",
    r"Si $\mathfrak{R}$ est", r"Si $\mathfrak{K}$ est", FRAK_NOTE)
add(139, "Corollaire (20.6.10): 'C = B/K'", "Fraktur K", "\\mathfrak{R}", "symbol", None, "high",
    r"$C=B/\mathfrak{R}$", r"$C=B/\mathfrak{K}$", FRAK_NOTE)
add(139, "Corollaire (20.6.10): 'E = B/K^2'", "Fraktur K", "\\mathfrak{R}", "symbol", None, "high",
    r"$E=B/\mathfrak{R}^2$", r"$E=B/\mathfrak{K}^2$", FRAK_NOTE)
add(139, "Corollaire (20.6.10): 'de C par K/K^2'", "Fraktur K (twice)", "\\mathfrak{R} (twice)", "symbol", None, "high",
    r"par $\mathfrak{R}/\mathfrak{R}^2$", r"par $\mathfrak{K}/\mathfrak{K}^2$", FRAK_NOTE)
add(139, "Corollaire (20.6.10): 'χ_E : Υ_{C/B/A} → K/K^2 est bijectif'", "Fraktur K (twice)", "\\mathfrak{R} (twice)",
    "symbol", None, "high",
    r"\to\mathfrak{R}/\mathfrak{R}^2$", r"\to\mathfrak{K}/\mathfrak{K}^2$", FRAK_NOTE)

add(139, "Corollaire (20.6.10): 'une B-extension A-triviale (18.3.7) de C'",
    "reference (18.3.7) upright inside the italic statement (enlarged crop)", "italic (corollary environment)",
    "convention", 6, "high",
    r"(18.3.7) de $C$", r"\textup{(18.3.7)} de $C$", "")

# ---------------- p. 140 ----------------
add(140, "Théorème (20.6.11): 'Alors l'homomorphisme canonique (20.6.7.1)' after the list (i), (ii)",
    "new indented paragraph", "no blank line after \\end{enumerate}: the line starts flush left", "other", None, "high",
    r"\end{enumerate}NLAlors l'homomorphisme", r"\end{enumerate}NLNLAlors l'homomorphisme",
    "Paragraph break as printed (as the earlier \\end{enumerate} fixes, e.g. EGA II pp. 84, 189).")

add(140, "Théorème (20.6.11): 'Alors l'homomorphisme canonique (20.6.7.1)'",
    "reference (20.6.7.1) upright inside the italic statement (enlarged crop)", "italic (theorem environment)",
    "convention", 6, "high",
    r"canonique (20.6.7.1)NL\[", r"canonique \textup{(20.6.7.1)}NL\[", "")

add(140, "Théorème (20.6.11), last paragraph: 'l'homomorphisme canonique (20.6.7.1) est bijectif'",
    "reference (20.6.7.1) upright inside the italic statement (enlarged crop)", "italic (theorem environment)",
    "convention", 6, "high",
    r"canonique (20.6.7.1) est", r"canonique \textup{(20.6.7.1)} est", "")

add(140, "Corollaire (20.6.12): 'En outre, cet homomorphisme est bijectif ...' after (20.6.12.1)",
    "new indented paragraph", "no blank line after \\end{equation}", "other", None, "high",
    r"\end{equation}NLEn outre", r"\end{equation}NLNLEn outre",
    "Paragraph break as printed (GLOBAL_ISSUES 47).")

add(140, "Corollaire (20.6.12): 'si l'une des conditions (i), (ii) de (20.6.11)'",
    "(i) and (ii) upright inside the italic statement (enlarged crop)", "italic (corollary environment)",
    "convention", 6, "high",
    r"conditions (i),NL(ii)", r"conditions \textup{(i)},NL\textup{(ii)}", "")

add(140, "Corollaire (20.6.12): 'de (20.6.11) est vérifiée'",
    "reference (20.6.11) upright inside the italic statement (enlarged crop)", "italic (corollary environment)",
    "convention", 6, "high",
    r"(20.6.11) est vérifiée", r"\textup{(20.6.11)} est vérifiée", "")

add(140, "Corollaire (20.6.13): 'l'homomorphisme (20.6.12.1) est bijectif'",
    "reference (20.6.12.1) upright inside the italic statement", "italic (corollary environment)",
    "convention", 6, "high",
    r"(20.6.12.1) est bijectif", r"\textup{(20.6.12.1)} est bijectif", "")

add(140, "(20.6.14): 'soient des Λ-algèbres'",
    "'algèbres' italic", "upright", "italics", None, "high",
    r"$\Lambda$-algèbres et", r"$\Lambda$-\emph{algèbres} et", "")

add(140, "(20.6.14): 'u, v des Λ-homomorphismes'",
    "'homomorphismes' italic", "upright", "italics", None, "high",
    r"$\Lambda$-homomorphismes, ce", r"$\Lambda$-\emph{homomorphismes}, ce", "")

# ---------------- checks ----------------
pages = {}
for p in (136, 137, 138, 139, 140):
    with open(rf"{BASE}\page_{p:03d}.tex", encoding="utf-8") as fh:
        pages[p] = fh.read().replace("\r\n", "\n")
with open(SRC, encoding="utf-8") as fh:
    src = fh.read().replace("\r\n", "\n")

ok = True
for i, d in enumerate(F):
    fx = d["fix"]
    if fx is None:
        continue
    n = pages[d["page"]].count(fx["old"])
    ns = src.count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", i, d["page"], n, repr(fx["old"][:80]))
    if ns != 1:
        print("source count", ns, i, d["page"], repr(fx["old"][:60]))

# sequential application per page
work = dict(pages)
for i, d in enumerate(F):
    fx = d["fix"]
    if fx is None:
        continue
    t = work[d["page"]]
    if t.count(fx["old"]) != 1:
        ok = False
        print("SEQ FAIL", i, d["page"], repr(fx["old"][:80]))
        continue
    work[d["page"]] = t.replace(fx["old"], fx["new"], 1)

from collections import Counter
c = Counter()
for d in F:
    cat = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    c[(d["page"], cat)] += 1
for p in (136, 137, 138, 139, 140):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("ok" if ok else "PROBLEMS", len(F))

if "--write" in sys.argv and ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
    print("written", OUT)
if "--show" in sys.argv:
    for p in (138, 139):
        print("=====", p)
        print(work[p][:1200] if p == 139 else work[p][-900:])
