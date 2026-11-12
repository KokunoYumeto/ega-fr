import json
import io

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
SRC = (r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
       r"\diplomatic\packages\IV4\native\ega4\ega4-20-fr.tex")
OUT = RUN + r"\findings_245_249.json"


def F(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None, nofix=False):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if nofix else {"old": old, "new": new},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


B = "\\"  # one backslash
L = []

# ---------------- page 245 ----------------
L.append(F(245, "Proposition (20.4.4): 'est un point normal tel que'",
           "'normal' roman inside the italic statement (crop p245_prop4.png)",
           "italic (statement environment)", "convention", 6, "high",
           r"est un point normal tel que", r"est un point \textup{normal} tel que"))
L.append(F(245, "Proposition (20.4.4): 'contienne un point isolé,'",
           "'isolé' roman inside the italic statement (crop p245_prop4.png)",
           "italic", "convention", 6, "high",
           r"un point isolé,", r"un point \textup{isolé},"))
L.append(F(245, "proof of (20.4.4): '(Err_IV, 30)'",
           "bold 'Err', light roman subscript IV, bold '30' (crop p245_err.png)",
           "subscript IV bold, number 30 light", "font", None, "high",
           r"(\textbf{Err}\textsubscript{\textbf{IV}}, 30)",
           r"(\textbf{Err}\textsubscript{IV}, \textbf{30})",
           "Two weight changes in one reference (subscript light, item number bold)."))
L.append(F(245, "Proposition (20.4.5): 'soient X′ un préschéma réduit,'",
           "'réduit' roman inside the italic statement (crop p245_stmt.png)",
           "italic", "convention", 6, "high",
           r"un préschéma réduit, $f:X'\to X$", r"un préschéma \textup{réduit}, $f:X'\to X$"))
L.append(F(245, "Proposition (20.4.5): 'localement de type fini et universellement ouvert.'",
           "'universellement ouvert' roman (crop p245_dom2.png)",
           "italic", "convention", 6, "high",
           r"et universellement ouvert.", r"et \textup{universellement ouvert}."))
L.append(F(245, "Proposition (20.4.5): 'dom_S(ω∘f) = f^{-1}(dom(ω))'",
           "dom(ω) without a subscript S on the right-hand side (crop p245_dom2.png)",
           r"\operatorname{dom}_S(\omega)", "formula", None, "high",
           r"\operatorname{dom}_S(\omega\circ f)=f^{-1}(\operatorname{dom}_S(\omega))$",
           r"\operatorname{dom}_S(\omega\circ f)=f^{-1}(\operatorname{dom}(\omega))$",
           "The TeX adds the S. The print writes dom without S for S-rational maps elsewhere too "
           "((20.4.12), p. 249: 'X—dom(f)'), so this is recorded as a transcription difference, not as a misprint. "
           "Adjacent to the next finding; no overlap."))
L.append(F(245, "Proposition (20.4.5): '(en d'autres termes, ... au point x′)'",
           "the whole parenthesis roman, upright parentheses (crop p245_dom2.png and page_245_s3.png)",
           "italic (statement environment)", "convention", 6, "high",
           r"(en d'autres termes, si $x'\in X'$ et $x=f(x')$, alors, pour que $\omega$ soit définie au point $x$, il faut et il suffit que $\omega\circ f$ le soit au point $x'$)",
           r"\textup{(en d'autres termes, si $x'\in X'$ et $x=f(x')$, alors, pour que $\omega$ soit définie au point $x$, il faut et il suffit que $\omega\circ f$ le soit au point $x'$)}"))
L.append(F(245, "proof of (20.4.5): 'donc f_(Y)^{-1}(M̄) = (f_(Y)^{-1}(M))‾'",
           "left side f_(Y)^{-1}(M̄), right side with the long bar over f_(Y)^{-1}(M) (crop p245_bar.png)",
           "the two sides swapped", "formula", None, "high",
           r"$\overline{f_{(Y)}^{-1}(M)}=f_{(Y)}^{-1}(\overline{M})$",
           r"$f_{(Y)}^{-1}(\overline{M})=\overline{f_{(Y)}^{-1}(M)}$"))
L.append(F(245, "proof of (20.4.5): 'et de (I, 5.3.12) que l'ensemble sous-jacent'",
           "(I, 5.3.12) (crop p245_I53.png)",
           "(I, 3.3.12)", "number", None, "high",
           r"\sref[I]{I.3.3.12}", r"\sref[I]{I.5.3.12}",
           "The print is right: EGA I (5.3.12) says that the graph of the base-changed morphism is the inverse image "
           "of the graph, which is the step used here; EGA I (3.3.12) is about monomorphisms."))

# ---------------- page 246 ----------------
L.append(F(246, "l. 2: 'Γ_{ω∘f} → Γ_ω×_X X′ → X′' (arrow label)",
           "label p_(X′) with (X′) as a subscript (crop p246_pX.png)",
           r"p^{(X')} (superscript)", "formula", None, "high",
           r"\xrightarrow{p^{(X')}}X'", r"\xrightarrow{p_{(X')}}X'"))
L.append(F(246, "l. 3: 'p_(X′) est nécessairement radiciel'",
           "p_(X′), subscript (crop p246_pX2.png)",
           r"p^{(X')}", "formula", None, "high",
           r"$p^{(X')}$ est nécessairement", r"$p_{(X')}$ est nécessairement"))
L.append(F(246, "Proposition (20.4.6): 'x∈X—U'",
           "long dash", "minus sign", "convention", 7, "high",
           r"un $S$-morphisme, $x\in X-U$", r"un $S$-morphisme, $x\in X\setmin U$"))
L.append(F(246, "Proposition (20.4.6): 'un point normal de X,'",
           "'normal' roman inside the italic statement (crop p246_normal.png)",
           "italic", "convention", 6, "high",
           r"un point normal de $X$,", r"un point \textup{normal} de $X$,"))
L.append(F(246, "Proposition (20.4.6): 'h′_x : Spec(k(x)) → Y un S-morphisme.'",
           "bold italic k", "plain k", "convention", 1, "high",
           r"\Spec(k(x))\to Y$ un $S$-morphisme.", r"\Spec(\boldsymbol{k}(x))\to Y$ un $S$-morphisme."))
L.append(F(246, "Proposition (20.4.6): 'le morphisme composé Spec(k(x)) → U′ → Y'",
           "bold italic k", "plain k", "convention", 1, "high",
           r"composé $\Spec(k(x))\to U'\xrightarrow{h'}Y$ est",
           r"composé $\Spec(\boldsymbol{k}(x))\to U'\xrightarrow{h'}Y$ est"))
L.append(F(246, "Proposition (20.4.6): condition (P), start",
           "the condition is italic like the statement, its label (P) upright (page_246_s2.png)",
           r"\emph{...} inside the italic proposition: the whole condition comes out upright",
           "convention", 6, "high",
           r"\emph{(P) Pour tout spectre", r"\textup{(P)} Pour tout spectre",
           "Part 1 of 2 (apply both): the second part removes the closing brace of the \\emph."))
L.append(F(246, "Proposition (20.4.6): condition (P), end ('tel que le diagramme')",
           "italic", "closing brace of the \\emph", "convention", 6, "high",
           r"$h'_1:S_1\to Y$ tel que le diagramme}", r"$h'_1:S_1\to Y$ tel que le diagramme",
           "Part 2 of 2 with the previous finding; apply both."))
L.append(F(246, "Proposition (20.4.6), diagram: 'Spec(k(a))'",
           "bold italic k", "plain k", "convention", 1, "high",
           r"\Spec(k(a)) \ar[r]", r"\Spec(\boldsymbol{k}(a)) \ar[r]"))
L.append(F(246, "Proposition (20.4.6), diagram: 'Spec(k(x))'",
           "bold italic k", "plain k", "convention", 1, "high",
           r"\Spec(k(x)) \ar[r]_{h'_x}", r"\Spec(\boldsymbol{k}(x)) \ar[r]_{h'_x}"))
L.append(F(246, "Proposition (20.4.6): 'soit commutatif.' after the diagram",
           "italic", r"\emph inside the italic proposition: upright", "convention", 6, "high",
           r"\emph{soit commutatif.}", r"soit commutatif."))
L.append(F(246, "Proposition (20.4.6): paragraph 'De plus, si cette condition est vérifiée, ...'",
           "a new indented paragraph (page_246_s3.png)",
           r"text follows \end{quote} without a blank line, so it is set without the indent",
           "other", None, "high",
           "\\end{quote}\nDe plus, si", "\\end{quote}\n\nDe plus, si",
           "Same pattern as text after \\end{enumerate} (GLOBAL_ISSUES 80)."))
L.append(F(246, "proof of (20.4.6): 'supposer X = S irréductible.'",
           "'irréductible' italic (crop p246_irred.png)", "roman", "italics", None, "high",
           r"supposer $X=S$ irréductible.", r"supposer $X=S$ \emph{irréductible}."))
L.append(F(246, "proof of (20.4.6): 'X-sections de X×_S Y (I, 3.3.15)'",
           "(I, 3.3.15)", "(I, 3.3.15) (kept)", "misprint_in_print", None, "medium",
           None, None,
           "The TeX keeps the printed reading. The correspondence between S-morphisms X→Y and X-sections of X×_S Y "
           "is EGA I (3.3.14) (graph morphism, Hom_S(S′, X) ≅ Hom_S′(S′, X_(S′))), which p. 249 cites for the same "
           "reduction; EGA I (3.3.15) treats the X-sections of X⊗Z[T]. No erratum in Liste 3.",
           corrected=r"\sref[I]{I.3.3.14}", nofix=True))

# ---------------- page 247 ----------------
L.append(F(247, "l. 6: 'supposer Y affine, donc séparé sur X'",
           "'séparé' italic (crop p247_separe.png)", "roman", "italics", None, "high",
           r"\emph{affine}, donc séparé sur $X$", r"\emph{affine}, donc \emph{séparé} sur $X$"))
L.append(F(247, "'qu'un seul X-morphisme Spec(k(x)) → Y'",
           "bold italic k", "plain k", "convention", 1, "high",
           r"seul $X$-morphisme $\Spec(k(x))\to Y$", r"seul $X$-morphisme $\Spec(\boldsymbol{k}(x))\to Y$"))
L.append(F(247, "'du composé de h′ et de Spec(k(x)) → U′.'",
           "bold italic k", "plain k", "convention", 1, "high",
           r"et de $\Spec(k(x))\to U'$.", r"et de $\Spec(\boldsymbol{k}(x))\to U'$."))
L.append(F(247, "Corollaire (20.4.7): 'une partie de X—U'",
           "long dash", "minus sign", "convention", 7, "high",
           r"une partie de $X-U$ telle", r"une partie de $X\setmin U$ telle"))
L.append(F(247, "Corollaire (20.4.7): 'X soit normal en tout point de E'",
           "'normal' roman inside the italic statement (page_247_s2.png)", "italic", "convention", 6, "high",
           r"soit normal en tout point de $E$", r"soit \textup{normal} en tout point de $E$"))
L.append(F(247, "Corollaire (20.4.7): 'soit h′_x : Spec(k(x)) → Y un S-morphisme'",
           "bold italic k", "plain k", "convention", 1, "high",
           r"soit $h'_x:\Spec(k(x))\to Y$ un $S$-morphisme, tel",
           r"soit $h'_x:\Spec(\boldsymbol{k}(x))\to Y$ un $S$-morphisme, tel"))
L.append(F(247, "Corollaire (20.4.7): 'la condition (P) de (20.4.6)'",
           "(P) upright, with upright parentheses (crop p247_P.png)", "italic", "convention", 6, "high",
           r"la condition~(P) de", r"la condition~\textup{(P)} de"))
L.append(F(247, "Corollaire (20.4.7): 'd'un nombre fini d'ouverts'",
           "'fini' roman (crop p247_par.png)", "italic", "convention", 6, "high",
           r"nombre fini d'ouverts $V_i$", r"nombre \textup{fini} d'ouverts $V_i$"))
L.append(F(247, "Corollaire (20.4.7): 'qui sont séparés sur X'",
           "italic like the rest of the statement (crop p247_par.png)",
           r"\emph{séparés} inside the italic corollary: upright", "convention", 6, "high",
           r"qui sont \emph{séparés} sur $X$", r"qui sont séparés sur $X$",
           "Adjacent to the next finding; no overlap."))
L.append(F(247, "Corollaire (20.4.7): '(condition automatiquement vérifiée si Y est séparé sur S, ou si X est quasi-compact et Y de type fini sur S)'",
           "the parenthesis roman with 'séparé', 'quasi-compact' and 'de type fini' italic (crops p247_par.png, p247_dtf.png)",
           "italic, with séparé, quasi-compact, type fini upright and 'de' outside the emphasis",
           "convention", 6, "high",
           r"(condition automatiquement vérifiée si $Y$ est \emph{séparé} sur $S$, ou si $X$ est \emph{quasi-compact} et $Y$ de \emph{type fini} sur $S$)",
           r"\textup{(condition automatiquement vérifiée si $Y$ est \emph{séparé} sur $S$, ou si $X$ est \emph{quasi-compact} et $Y$ \emph{de type fini} sur $S$)}",
           "Two parts in one edit: the roman parenthesis, and 'de' italic together with 'type fini'."))
L.append(F(247, "Corollaire (20.4.7), display: 'Spec(k(x)) → U′ → Y'",
           "bold italic k", "plain k", "convention", 1, "high",
           "\\Spec(k(x))\\to U'\\xrightarrow{h'}Y\n\\]", "\\Spec(\\boldsymbol{k}(x))\\to U'\\xrightarrow{h'}Y\n\\]"))

# ---------------- page 248 ----------------
L.append(F(248, "Remarque (20.4.8): 'Lorsque E = X—U'",
           "long dash", "minus sign", "convention", 7, "high",
           r"Lorsque $E=X-U$", r"Lorsque $E=X\setmin U$"))
L.append(F(248, "Remarque (20.4.8): 'le composé Spec(k(x)) → T → Y'",
           "bold italic k", "plain k", "convention", 1, "high",
           r"le composé $\Spec(k(x))\to T", r"le composé $\Spec(\boldsymbol{k}(x))\to T"))
L.append(F(248, "Remarque (20.4.8): 'pour tout x∈T—(U∩T)'",
           "long dash", "minus sign", "convention", 7, "high",
           r"$x\in T-(U\cap T)$", r"$x\in T\setmin(U\cap T)$"))
L.append(F(248, "Remarque (20.4.8): 'les restrictions d'un S-morphisme h′ : X → Y (partout défini)'",
           "'morphisme' italic in the roman remark (crop p248_Smorph.png)",
           "no emphasis", "italics", None, "medium",
           r"d'un $S$-morphisme $h':X\to Y$ (partout défini)",
           r"d'un $S$-\emph{morphisme} $h':X\to Y$ (partout défini)",
           "Judged with the remark body roman (document-wide remark-font item). Emphasis or a compositor's slip; "
           "either way the diplomatic text reproduces it."))
L.append(F(248, "Remarque (20.4.8): 'de la forme Spec(k(x)) → Z → Y'",
           "bold italic k", "plain k", "convention", 1, "high",
           r"la forme $\Spec(k(x))\to Z", r"la forme $\Spec(\boldsymbol{k}(x))\to Z"))
L.append(F(248, "Remarque (20.4.8): 'ayant X—U pour espace sous-jacent'",
           "long dash", "minus sign", "convention", 7, "high",
           r"ayant $X-U$ pour espace", r"ayant $X\setmin U$ pour espace"))
L.append(F(248, "Corollaire (20.4.9): 'T = S—U'",
           "long dash", "minus sign", "convention", 7, "high",
           r"$T=S-U$", r"$T=S\setmin U$"))
L.append(F(248, "Corollaire (20.4.9): 'Supposons X normal en tous les points de Z.'",
           "'normal' roman inside the italic statement (crop p248_necess.png)", "italic", "convention", 6, "high",
           r"Supposons $X$ normal en tous", r"Supposons $X$ \textup{normal} en tous"))
L.append(F(248, "Corollaire (20.4.9): condition 'Pour tout spectre S_1 ...', start",
           "italic like the statement (page_248_s3.png)",
           r"\emph{...} inside the italic corollary: the condition comes out upright", "convention", 6, "high",
           r"\emph{Pour tout spectre $S_1$", r"Pour tout spectre $S_1$",
           "Part 1 of 2 (apply both): the second part removes the closing brace of the \\emph."))
L.append(F(248, "Corollaire (20.4.9): condition, end ('et est tel que le diagramme')",
           "italic", "closing brace of the \\emph", "convention", 6, "high",
           r"et est tel que le diagramme}", r"et est tel que le diagramme",
           "Part 2 of 2 with the previous finding; apply both."))
L.append(F(248, "Corollaire (20.4.9), diagram: 'Spec(k(z_1))'",
           "bold italic k", "plain k", "convention", 1, "high",
           r"\Spec(k(z_1))", r"\Spec(\boldsymbol{k}(z_1))"))
L.append(F(248, "Corollaire (20.4.9): 'soit commutatif pour tout z_1∈Z_(S_1).'",
           "italic", r"\emph inside the italic corollary: upright", "convention", 6, "high",
           r"\emph{soit commutatif pour tout $z_1\in Z_{(S_1)}$.}",
           r"soit commutatif pour tout $z_1\in Z_{(S_1)}$.",
           "Adjacent to the next finding (no overlap); the next one ends the corollary right after this sentence."))
L.append(F(248, "end of Corollaire (20.4.9): 'L'hypothèse que f est plat entraîne en effet ...'",
           "the statement ends with '... pour tout z_1∈Z_(S_1).'; the justification 'L'hypothèse que f est plat ...' is roman (page_248_s3.png)",
           r"\end{corollary} stands after the justification, so it is set italic",
           "other", None, "high",
           "\n\nL'hypothèse que $f$ est plat entraîne en effet que $f^{-1}(U)$ est dense dans $X$ \\sref{IV.2.3.10}, et il suffit alors d'appliquer \\sref{IV.20.4.8}.\n\\end{corollary}",
           "\n\\end{corollary}\n\nL'hypothèse que $f$ est plat entraîne en effet que $f^{-1}(U)$ est dense dans $X$ \\sref{IV.2.3.10}, et il suffit alors d'appliquer \\sref{IV.20.4.8}.",
           "Moves \\end{corollary} before the roman justification in one edit (same repair as (17.13.6), p. 93, and (19.7.3)-(19.7.5))."))
L.append(F(248, "Corollaire (20.4.10): 'x∈X—U'",
           "long dash", "minus sign", "convention", 7, "high",
           r"correspondante, $x\in X-U$", r"correspondante, $x\in X\setmin U$"))
L.append(F(248, "Corollaire (20.4.10): 'un point normal de X.'",
           "'normal' roman inside the italic statement (page_248_s4.png)", "italic", "convention", 6, "high",
           r"un point normal de $X$.", r"un point \textup{normal} de $X$."))

# ---------------- page 249 ----------------
L.append(F(249, "end of the statement of (20.4.10): '... ω∘u soit partout définie.'",
           "the statement ends at '... soit partout définie.'; the justification 'En effet, par hypothèse ...' is roman (page_249_s1.png)",
           r"the justification stays inside the italic corollary (\end{corollary} after 'd'où la conclusion.')",
           "other", None, "high",
           "soit partout définie.\n\nEn effet", "soit partout définie.\n\\end{corollary}\n\nEn effet",
           "Part 1 of 2 (apply both): ends the corollary after its statement; part 2 removes the old \\end{corollary}. "
           "The \\emph{non vide} fix below assumes the move."))
L.append(F(249, "proof of (20.4.10): 'est non vide dans Γ_ω'",
           "'non vide' italic in the roman text (page_249_s1.png)", "no emphasis", "italics", None, "high",
           r"est non vide dans", r"est \emph{non vide} dans",
           "Assumes the \\end{corollary} move (the findings before and after this one); inside the italic corollary \\emph would print upright."))
L.append(F(249, "end of the proof of (20.4.10)",
           "", r"old \end{corollary}", "other", None, "high",
           "d'où la conclusion.\n\\end{corollary}", "d'où la conclusion.",
           "Part 2 of 2 with the first p. 249 finding; apply both."))
L.append(F(249, "Proposition (20.4.11): 'Z = X—U.'",
           "long dash", "minus sign", "convention", 7, "high",
           r"$Z=X-U$.", r"$Z=X\setmin U$."))
L.append(F(249, "proof of (20.4.11): 'se factorisera en X → Y → Y′ : en effet'",
           "colon after Y′ (crop p249_colon.png)", "semicolon", "punctuation", None, "high",
           r"Y\to Y'$ ; en effet", r"Y\to Y'$ : en effet"))
L.append(F(249, "Corollaire (20.4.12): '(par exemple un S-préschéma localement noethérien et normal (5.8.6))'",
           "the parenthesis roman, 'normal' italic (crop p249_cor12.png)",
           "italic; 'normal' not emphasized", "convention", 6, "high",
           r"(par exemple un $S$-préschéma localement noethérien et normal \sref{IV.5.8.6})",
           r"\textup{(par exemple un $S$-préschéma localement noethérien et \emph{normal} \sref{IV.5.8.6})}"))
L.append(F(249, "Corollaire (20.4.12): 'X—dom(f)'",
           "long dash", "minus sign", "convention", 7, "high",
           r"$X-\operatorname{dom}(f)$", r"$X\setmin\operatorname{dom}(f)$"))
L.append(F(249, "proof of (20.4.12): 'tout S-morphisme de X—Z dans Y'",
           "long dash", "minus sign", "convention", 7, "high",
           r"de $X-Z$ dans", r"de $X\setmin Z$ dans"))
L.append(F(249, "heading 20.5: 'Pseudo-morphismes relatifs.'",
           "final full stop (page_249_s3.png)", "no full stop", "punctuation", None, "high",
           r"\subsection{Pseudo-morphismes relatifs}", r"\subsection{Pseudo-morphismes relatifs.}",
           "GLOBAL_ISSUES 43/58."))

# ---------------- checks ----------------
src = io.open(SRC, encoding="utf-8", newline="").read()
pages = {}
for p in (245, 246, 247, 248, 249):
    pages[p] = io.open(RUN + r"\page_%d.tex" % p, encoding="utf-8", newline="").read().replace("\r\n", "\n")
assert "\r\n" not in src
bad = 0
for i, d in enumerate(L):
    fx = d["fix"]
    if fx is None:
        continue
    o = fx["old"]
    cp = pages[d["page"]].count(o)
    cs = src.count(o)
    if cp != 1 or cs != 1:
        bad += 1
        print("NOT UNIQUE", i, d["page"], cp, cs, repr(o)[:120])
    if fx["old"] == fx["new"]:
        print("NO CHANGE", i)
print("findings:", len(L), "bad:", bad)

# simulate applying all fixes to the source in list order
s = src
for d in L:
    fx = d["fix"]
    if fx is None:
        continue
    assert s.count(fx["old"]) == 1, ("after earlier fixes, not unique", fx["old"][:80])
    s = s.replace(fx["old"], fx["new"], 1)
# brace balance in the touched region
a = s.index(r"\oldpage[IV-4]{245}")
b = s.index(r"\oldpage[IV-4]{250}")
seg = s[a:b]
print("braces", seg.count("{"), seg.count("}"))
print("begin/end corollary", seg.count(r"\begin{corollary}"), seg.count(r"\end{corollary}"))
io.open(RUN + r"\crops_245_249\simulated_245_249.txt", "w", encoding="utf-8", newline="").write(seg)

from collections import Counter
c = Counter()
for d in L:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    c[(d["page"], k)] += 1
for p in (245, 246, 247, 248, 249):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])

io.open(OUT, "w", encoding="utf-8", newline="\n").write(json.dumps(L, ensure_ascii=False, indent=1) + "\n")
print("written", OUT)
