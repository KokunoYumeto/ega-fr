import json
import pathlib

OUT = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3\findings_080_084.json")


def nl(s):
    return None if s is None else s.replace("<NL>", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, fix_null=False):
    d = {"page": page, "where": where, "scan": scan, "tex": nl(tex), "kind": kind, "convention": conv,
         "confidence": conf}
    d["fix"] = None if fix_null else {"old": nl(old), "new": nl(new)}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 79 (outside pp. 80-84)
add(79, "end of page_079.tex, page break 79/80 mid-sentence: '... de X_eta sont géométriquement | irréductibles (resp. géométriquement connexes) ...'",
    "printed p. 79 ends 'sont géométriquement' and p. 80 continues the sentence 'irréductibles (resp. ...' with no paragraph break",
    r"blank line before \oldpage[IV-3]{80} (and another after it): the TeX starts a new paragraph inside the sentence",
    "marker", None, "high",
    r"de $X_\eta$ sont géométriquement<NL><NL>", r"de $X_\eta$ sont géométriquement<NL>",
    "OUTSIDE pp. 80-84: 'old' lies in page_079.tex (end of its segment). Part 1 of 2 with the next finding (p. 80), which removes the blank line after the marker; apply both. The pp. 75-79 checker may report the same edit.")

# ---------------------------------------------------------------- page 80
add(80, "top of p. 80: \\oldpage[IV-3]{80} at a mid-sentence break",
    "p. 80 begins 'irréductibles (resp. géométriquement connexes) et que (X_eta)_red est géométriquement réduit.', continuing the sentence of p. 79",
    r"\oldpage[IV-3]{80} followed by a blank line (paragraph break the print lacks)",
    "marker", None, "high",
    r"\oldpage[IV-3]{80}<NL><NL>irréductibles", r"\oldpage[IV-3]{80}<NL>irréductibles",
    "Part 2 of 2 with the page-79 finding (blank line before the marker). Marker position itself is right.")

add(80, "'Supposons d'abord que eta∈S—E pour une des propriétés (i) à (iv)'",
    "long dash for the set difference S—E", r"$\eta\in S-E$ (minus sign)",
    "convention", 7, "high",
    r"$\eta\in S-E$", r"$\eta\in S\setmin E$",
    "\\setmin pending the convention-7 decision (FIX_POLICY 2.7).")

add(80, "1°, 'on a donc G=F_{(k(eta))}'",
    "subscript k(eta) with a bold UPRIGHT k (enlarged crop p80_Fk_eta.png; the k(s) of p. 81 l. 7, on the line, is bold italic for comparison)",
    r"F_{(\boldsymbol{k}(\eta))} (bold italic k)",
    "font", None, "high",
    r"F_{(\boldsymbol{k}(\eta))}", r"F_{(\mathbf{k}(\eta))}",
    "In subscripts the print's k is bold upright (GLOBAL_ISSUES 48). Not convention 1: the TeX k is already bold, but italic.")

add(80, "'on peut supposer que v=w_eta où w : W→X est une immersion ouverte'",
    "no comma between w_eta and 'où' (enlarged crop p80_vw.png)",
    r"$v=w_\eta$, où (comma added)",
    "punctuation", None, "high",
    r"$v=w_\eta$, où", r"$v=w_\eta$ où",
    "")

add(80, "'tel que F_{(k(s))} soit géométriquement irréductible pour tout s∈U'",
    "subscript k(s) with a bold UPRIGHT k (enlarged crop p80_Fk_s.png)",
    r"F_{(\boldsymbol{k}(s))} (bold italic k)",
    "font", None, "high",
    r"F_{(\boldsymbol{k}(s))}", r"F_{(\mathbf{k}(s))}",
    "As the k(eta) subscript above (GLOBAL_ISSUES 48).")

add(80, "end of p. 80: '... enfin, on peut supposer aussi que | pour s∈U, w_s : W_s→X_s ...' (break 80/81 mid-sentence)",
    "p. 80 ends 'enfin, on peut supposer aussi que'; p. 81 continues 'pour s∈U, w_s ...' in the same sentence",
    r"blank line before \oldpage[IV-3]{81} (and another after it): paragraph break inside the sentence",
    "marker", None, "high",
    r"supposer aussi que<NL><NL>", r"supposer aussi que<NL>",
    "Part 1 of 2 with the first p. 81 finding (blank line after the marker); apply both.")

# ---------------------------------------------------------------- page 81
add(81, "top of p. 81: \\oldpage[IV-3]{81} at a mid-sentence break",
    "p. 81 begins 'pour s∈U, w_s : W_s→X_s est une immersion ouverte (9.6.1, (x))', continuing the sentence of p. 80",
    r"\oldpage[IV-3]{81} followed by a blank line",
    "marker", None, "high",
    r"\oldpage[IV-3]{81}<NL><NL>pour", r"\oldpage[IV-3]{81}<NL>pour",
    "Part 2 of 2 with the last p. 80 finding; apply both. Marker position itself is right.")

add(81, "3°, 'il existe (en vertu de (5.10.8.1) appliqué à 𝔉={∅})'",
    "Fraktur F (letter with the middle cross-stroke), enlarged crop p81_frak.png; (5.10.8.1) names its antifilter 𝔉 (ega4-2-fr.tex: \\mathfrak F)",
    r"$\mathfrak T=\{\varnothing\}$ (Fraktur T)",
    "symbol", None, "high",
    r"$\mathfrak T=\{\varnothing\}$", r"$\mathfrak F=\{\varnothing\}$",
    "Wrong Fraktur letter.")

add(81, "3°, 'une application surjective j→ν(j) d'un intervalle [1, m]'",
    "plain arrow j→ν(j) (enlarged crop p81_arrow.png)", r"$j\mapsto\nu(j)$",
    "convention", 3, "high",
    r"$j\mapsto\nu(j)$", r"$j\to\nu(j)$",
    "")

add(81, "3°, 'telle que Z_{ν(j)}∩Z_{ν(j+1)}≠∅ pour 1≤j≤m'",
    "pour 1⩽j⩽m (enlarged crop p81_zcap.png)",
    r"$Z_{\nu(j)}\cap Z_{\nu(j+1)}\neq\varnothing$ pour $1\leqslant j\leqslant m$ (keeps the printed reading)",
    "misprint_in_print", None, "medium", None, None,
    "Slip of the print: ν is defined on [1, m], so ν(j+1) does not exist for j=m; the condition is for 1⩽j⩽m−1 (consecutive pairs of the chain). Same slip in the second occurrence below. The TeX keeps the printed reading (right for the diplomatic edition).",
    corrected=r"$1\leqslant j\leqslant m-1$", fix_null=True)

add(81, "3°, 'on a (X_{ν(j)})_s∩(X_{ν(j+1)})_s≠∅ (9.5.1) pour 1≤j≤m'",
    "pour 1⩽j⩽m",
    r"(9.5.1) pour<NL>$1\leqslant j\leqslant m$~; (keeps the printed reading)",
    "misprint_in_print", None, "medium", None, None,
    "Same slip as above: j+1 must stay in [1, m]; correct reading 1⩽j⩽m−1. The TeX keeps the printed reading.",
    corrected=r"$1\leqslant j\leqslant m-1$", fix_null=True)

# ---------------------------------------------------------------- page 82
add(82, "Proposition (9.7.8), l. 2: 'Soit n (resp. n') le nombre géométrique'",
    "'(resp.' and the closing parenthesis roman inside the italic statement (enlarged crop p82_prop_b.png)",
    "(resp. $n'$) italic (proposition environment)",
    "convention", 6, "high",
    r"Soit $n$ (resp. $n'$) le", r"Soit $n$ \textup{(resp. $n'$)} le",
    "")

add(82, "Proposition (9.7.8), l. 3: 'irréductibles (resp. connexes) de X_eta (4.5.2).'",
    "'(resp.' and ')' roman, 'connexes' italic; the reference (4.5.2) upright (enlarged crop p82_prop_c.png)",
    "(resp. connexes) and (4.5.2) all italic",
    "convention", 6, "high",
    r"(resp. connexes) de $X_\eta$ (4.5.2)", r"\textup{(resp.} connexes\textup{)} de $X_\eta$ \textup{(4.5.2)}",
    "Two roman spots on one line, one edit.")

add(82, "Proposition (9.7.8), l. 5: 'irréductibles (resp. connexes) de X_s'",
    "'(resp.' and ')' roman, 'connexes' italic (enlarged crop p82_prop_d.png)",
    "(resp. connexes) all italic",
    "convention", 6, "high",
    r"(resp. connexes) de $X_s$", r"\textup{(resp.} connexes\textup{)} de $X_s$",
    "")

add(82, "Proposition (9.7.8), last line: 'soit égal à n (resp. n').'",
    "'(resp.' and the closing parenthesis roman (enlarged crop p82_prop_c.png)",
    "(resp. $n'$) italic",
    "convention", 6, "high",
    r"(resp. $n'$).<NL>\end{proposition}", r"\textup{(resp. $n'$)}.<NL>\end{proposition}",
    "")

add(82, "proof of (9.7.8): 'soient géométriquement irréductibles (resp. géométriquement connexes)'",
    "only 'géométriquement' italic in both places; 'connexes' roman (enlarged crop p82_geom.png)",
    r"(resp. \emph{géométriquement connexes}) (both words italic)",
    "italics", None, "high",
    r"(resp. \emph{géométriquement connexes})", r"(resp. \emph{géométriquement} connexes)",
    "")

add(82, "Corollaire (9.7.9), l. 2: 'soit n(s) (resp. n'(s)) le nombre'",
    "'(resp.' and the last closing parenthesis roman inside the italic statement (enlarged crop p82_cor_a.png)",
    "(resp. $n'(s)$) italic",
    "convention", 6, "high",
    r"$n(s)$ (resp. $n'(s)$) le", r"$n(s)$ \textup{(resp. $n'(s)$)} le",
    "")

add(82, "Corollaire (9.7.9), l. 3: '(resp. connexes) de f^{-1}(s) (4.5.2).'",
    "'(resp.' and ')' roman, 'connexes' italic; (4.5.2) upright (enlarged crops p82_cor_a/b.png)",
    "(resp. connexes) and (4.5.2) all italic",
    "convention", 6, "high",
    r"(resp. connexes) de $f^{-1}(s)$ (4.5.2)", r"\textup{(resp.} connexes\textup{)} de $f^{-1}(s)$ \textup{(4.5.2)}",
    "Two roman spots on one line, one edit.")

add(82, "Corollaire (9.7.9): 'Alors la fonction s⇝n(s)'",
    "wavy arrow s⇝n(s) (enlarged crop p82_cor_a.png)", r"$s\mapsto n(s)$",
    "symbol", None, "high",
    r"$s\mapsto n(s)$", r"$s\leadsto n(s)$",
    "The print has the wavy maps-to arrow (as \\leadsto; amssymb is loaded); not convention 3.")

add(82, "Corollaire (9.7.9): '(resp. s⇝n'(s)) est localement constructible'",
    "'(resp.' and the last closing parenthesis roman inside the italic statement (enlarged crop p82_cor_b.png)",
    r"(resp. $s\mapsto n'(s)$) italic",
    "convention", 6, "high",
    r"(resp. $s\mapsto n'(s)$)", r"\textup{(resp. $s\mapsto n'(s)$)}",
    "Apply BEFORE the next finding (wavy arrow), whose 'old' lies inside this one and survives this edit.")

add(82, "Corollaire (9.7.9): '(resp. s⇝n'(s))'",
    "wavy arrow s⇝n'(s) (enlarged crop p82_cor_b.png)", r"$s\mapsto n'(s)$",
    "symbol", None, "high",
    r"s\mapsto n'(s)", r"s\leadsto n'(s)",
    "Apply AFTER the previous convention-6 finding (its 'old' contains this text). Wavy maps-to arrow, as \\leadsto.")

add(82, "Remarque (9.7.11), l. 1: 'Soit Z une partie localement constructible de X'",
    "'localement constructible' italic in the roman remark",
    "no emphasis (plain words in the remark environment)",
    "italics", None, "high",
    r"une partie localement constructible de", r"une partie \emph{localement constructible} de",
    "Judged with the remark body roman (document-wide remark-font item).")

add(82, "Remarque (9.7.11), l. 2: 'Z∩X_s soit ouvert dans X_s'",
    "'ouvert' italic in the roman remark", "no emphasis",
    "italics", None, "high",
    r"soit ouvert dans", r"soit \emph{ouvert} dans",
    "As the previous finding.")

add(82, "end of p. 82: '... désignons par Z_s le sous-préschéma de X_s induit | sur l'ouvert Z∩X_s.' (break 82/83 inside Remarque (9.7.11))",
    "p. 82 ends 'induit'; p. 83 continues 'sur l'ouvert Z∩X_s.' in the same sentence",
    r"blank line before \oldpage[IV-3]{83} (and another after it): paragraph break inside the sentence",
    "marker", None, "high",
    r"de $X_s$ induit<NL><NL>", r"de $X_s$ induit<NL>",
    "Part 1 of 2 with the first p. 83 finding; apply both.")

# ---------------------------------------------------------------- page 83
add(83, "top of p. 83: \\oldpage[IV-3]{83} at a mid-sentence break",
    "p. 83 begins 'sur l'ouvert Z∩X_s. Alors, dans le théorème (9.7.7) ...', continuing the sentence of p. 82",
    r"\oldpage[IV-3]{83} followed by a blank line",
    "marker", None, "high",
    r"\oldpage[IV-3]{83}<NL><NL>sur l'ouvert", r"\oldpage[IV-3]{83}<NL>sur l'ouvert",
    "Part 2 of 2 with the last p. 82 finding; apply both. Marker position itself is right.")

add(83, "Proposition (9.7.12), l. 2: 'une S-section de X (I, 2.5.5).'",
    "reference (I, 2.5.5) upright (bold upright I) inside the italic statement (enlarged crop p83_prop.png)",
    r"(\textbf{I}, 2.5.5) italic (proposition environment)",
    "convention", 6, "high",
    r"(\textbf{I}, 2.5.5)", r"\textup{(\textbf{I}, 2.5.5)}",
    "")

add(83, "proof of (9.7.12): 'En d'autres termes, g est une S-section de X^0'",
    "'section de' italic in the roman proof (enlarged crop p83_section.png)",
    r"$S$-section de $X^0$ (upright)",
    "italics", None, "high",
    r"est une $S$-section de $X^0$", r"est une $S$-\emph{section de} $X^0$",
    "")

add(83, "subsection heading 9.8",
    "'9.8. Décomposition primaire au voisinage d'une fibre générique.' (final full stop)",
    r"\subsection{... générique} (no full stop)",
    "punctuation", None, "high",
    r"\subsection{Décomposition primaire au voisinage d'une fibre générique}",
    r"\subsection{Décomposition primaire au voisinage d'une fibre générique.}",
    "GLOBAL_ISSUES 43/58: subsection titles lack the printed full stop.")

add(83, "proof of (9.8.1): 'dans ce cas E ou S—E est un voisinage de eta'",
    "long dash for the set difference S—E", r"$S-E$ (minus sign)",
    "convention", 7, "high",
    r"$S-E$ est un voisinage", r"$S\setmin E$ est un voisinage",
    "\\setmin pending the convention-7 decision (FIX_POLICY 2.7).")

add(83, "end of p. 83: '... alors, en vertu de (8.5.2, (i) et (ii)) | et (8.5.8), appliqués ...' (break 83/84 mid-sentence)",
    "p. 83 ends 'en vertu de (8.5.2, (i) et (ii))'; p. 84 continues 'et (8.5.8), appliqués suivant la méthode ...' in the same sentence",
    r"blank line before \oldpage[IV-3]{84} (and another after it): paragraph break inside the sentence",
    "marker", None, "high",
    r"et (ii))<NL><NL>", r"et (ii))<NL>",
    "Part 1 of 2 with the first p. 84 finding; apply both.")

# ---------------------------------------------------------------- page 84
add(84, "top of p. 84: \\oldpage[IV-3]{84} at a mid-sentence break",
    "p. 84 begins 'et (8.5.8), appliqués suivant la méthode de (8.1.2, a)), il existe ...', continuing the sentence of p. 83",
    r"\oldpage[IV-3]{84} followed by a blank line",
    "marker", None, "high",
    r"\oldpage[IV-3]{84}<NL><NL>et (8.5.8)", r"\oldpage[IV-3]{84}<NL>et (8.5.8)",
    "Part 2 of 2 with the last p. 83 finding; apply both. Marker position itself is right.")

add(84, "'comme Z—Z' est dense dans Z et Z'≠∅'",
    "long dash for the set difference Z—Z'", r"$Z-Z'$ (minus sign)",
    "convention", 7, "high",
    r"$Z-Z'$", r"$Z\setmin Z'$",
    "\\setmin pending the convention-7 decision (FIX_POLICY 2.7).")

add(84, "'pour s∈U, Y_s—Y'_s soit dense dans Y_s'",
    "long dash for the set difference Y_s—Y'_s", r"$Y_s-Y'_s$ (minus sign)",
    "convention", 7, "high",
    r"$Y_s-Y'_s$", r"$Y_s\setmin Y'_s$",
    "\\setmin pending the convention-7 decision (FIX_POLICY 2.7).")

add(84, "Proposition (9.8.3), l. 1: 'Sous les conditions de (9.8.2), pour tout s∈S'",
    "reference (9.8.2) upright inside the italic statement (enlarged crop p84_prop_b.png)",
    "(9.8.2) italic (proposition environment)",
    "convention", 6, "high",
    r"conditions de (9.8.2), pour", r"conditions de \textup{(9.8.2)}, pour",
    "")

add(84, "Proposition (9.8.3), l. 2: 'désignons par x_{isα} (α∈J_{s,i}) les points maximaux'",
    "both parentheses of (α∈J_{s,i}) upright; the parenthesis '(pour i∈I et, pour chaque i, α∈J_{s,i})' on the next line is italic (enlarged crops p84_alpha_open2.png, p84_jsi2.png, p84_pour_open.png)",
    r"($\alpha\in J_{s,i}$): text parentheses, italic in the proposition environment",
    "convention", 6, "medium",
    r"($\alpha\in J_{s,i}$) les points", r"\textup{(}$\alpha\in J_{s,i}$\textup{)} les points",
    "Parentheses around a formula printed upright inside an italic statement (GLOBAL_ISSUES 26).")

add(84, "proof of (9.8.3): labels of the list (i), (ii), (iii)",
    "labels (i), (ii), (iii) upright roman (enlarged crop p84_labels.png)",
    r"\begin{enumerate}[label=\emph{(\roman*)}] sets the labels italic in the roman proof",
    "italics", None, "high",
    r"\begin{enumerate}[label=\emph{(\roman*)}]", r"\begin{enumerate}[label=(\roman*)]",
    "GLOBAL_ISSUES 76 (item labels in proofs printed upright). The list continues on p. 85 with another \\begin{enumerate}[label=\\emph{(\\roman*)}] and \\item[(iv)] (not checked here).")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(F), "findings written")
