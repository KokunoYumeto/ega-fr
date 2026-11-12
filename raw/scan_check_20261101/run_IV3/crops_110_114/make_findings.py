# Builds findings_110_114.json for EGA IV-3 pp. 110-114 and checks every fix's "old" against page_NNN.tex.
# In the strings below, the character U+00B6 (pilcrow) stands for a line break (LF).
import json
import pathlib
import collections

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
OUT = RUN / "findings_110_114.json"
NL = "\u00b6"


def nl(s):
    return None if s is None else s.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None, nofix=False):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if nofix else dict(old=nl(old), new=nl(new)))
    if kind == "misprint_in_print":
        d["corrected"] = nl(corrected)
    d["note"] = note
    F.append(d)


WAVY = "Wavy arrow (GLOBAL_ISSUES 33), \\leadsto as in the earlier page fixes; not convention 3. Enlarged crop."
REF6 = "Reference printed upright inside the italic statement (enlarged crop)."
CAT = "Category letter bold italic in the print (as on IV-2 p. 220); bold upright C would be the complex numbers."

# ---------------- page 110 ----------------
add(110, "(10.7.2), l. 2: 'Alors S vérifie les conditions 1°, 2° et 3° de (10.6.1) :'",
    "'vérifie les conditions 1°, 2° et 3° de' italic (italic figures); (10.6.1) upright (enlarged crop)",
    "upright (env body is roman)", "italics", None, "high",
    r"Alors $S$ vérifie les conditions $1^\circ$, $2^\circ$ et $3^\circ$ de (10.6.1)",
    r"Alors $S$ \emph{vérifie les conditions $1^\circ$, $2^\circ$ et $3^\circ$ de} (10.6.1)",
    "The print's 1, 2, 3 here are italic figures; the math $1^\\circ$ etc. stay upright (minor). Same treatment as (10.7.1) on p. 109.")
add(110, "(10.7.3), l. 2: 'deux idéaux maximaux m, n de hauteurs respectives n et n+1'",
    "'de hauteurs respectives n et' italic, 'de' and 'et' included; 'n+1' after it (enlarged crop)",
    r"de \emph{hauteurs respectives} $n$ et", "italics", None, "high",
    r"de \emph{hauteurs respectives} $n$ et¶$n+1$",
    r"\emph{de hauteurs respectives $n$ et}¶$n+1$")
add(110, "(10.7.3), l. 7: 'Soit 𝔍 l'idéal 𝔪∩𝔫 = 𝔪𝔫, et R = 1 + 𝔍'",
    "'Soit 𝔍 l'idéal 𝔪∩𝔫=𝔪𝔫' (enlarged crop)",
    r"'Soit $\mathfrak J=\mathfrak m\cap\mathfrak n=\mathfrak m\mathfrak n$': the words 'l'idéal' missing, an '=' added",
    "word", None, "high",
    r"$\mathfrak J=\mathfrak m\cap\mathfrak n=\mathfrak m\mathfrak n$",
    r"$\mathfrak J$ l'idéal $\mathfrak m\cap\mathfrak n=\mathfrak m\mathfrak n$")
add(110, "(10.7.3): 'l'idéal 𝔍' = R^{-1}𝔍 est contenu dans le radical de B''",
    "'radical' italic (enlarged crop)", "upright", "italics", None, "high",
    r"dans le¶radical de $B'$", r"dans le¶\emph{radical} de $B'$")
add(110, "(10.7.3): 'et soit S = X'—Y''", "long dash for the set difference X'—Y'", "$S=X'-Y'$",
    "convention", 7, "high", "$S=X'-Y'$", r"$S=X'\setmin Y'$",
    "\\setmin pending the convention-7 decision (FIX_POLICY 2.7); not defined in EGA_IV3_FR.tex.")
add(110, "(10.7.3), last line: 'a et b sont dans S, donc fermés dans S, et répondent'",
    "only 'fermés' italic, 'dans S' upright (enlarged crop)", r"\emph{fermés dans $S$}", "italics", None, "high",
    r"\emph{fermés dans $S$}", r"\emph{fermés} dans $S$")
add(110, "Définition (10.8.1): 'on appelle profondeur rectifiée de F au point x et on note'",
    "the defined term is in the same italic as the statement, no change of face (enlarged crop)",
    r"\emph{...} inside the italic definition environment: typeset upright", "convention", 6, "high",
    r"\emph{profondeur rectifiée de $\mathcal F$¶au point $x$}",
    r"profondeur rectifiée de $\mathcal F$¶au point $x$",
    "FIX_POLICY 2.6: inside an italic environment drop \\emph where the print shows no change of face.")
add(110, "Définition (10.8.1): 'on appelle profondeur rectifiée de F le long de Z et on note'",
    "the defined term is in the same italic as the statement, no change of face (enlarged crop)",
    r"\emph{...} inside the italic definition environment: typeset upright", "convention", 6, "high",
    r"\emph{profondeur rectifiée de $\mathcal F$ le long de $Z$}",
    r"profondeur rectifiée de $\mathcal F$ le long de $Z$")

# ---------------- page 111 ----------------
add(111, "Remarques (10.8.2) (ii), end: 'prof*_x(G) = prof*_x j_*((G)) pour tout x∈Y'",
    "prof*_x j_*( (G)): the parenthesis that should follow prof*_x stands after j_* (enlarged crop)",
    r"\operatorname{prof}^{*}_{x}(j_*(\mathcal G)) (silently corrected)", "misprint_in_print", None, "high",
    r"=\operatorname{prof}^{*}_{x}(j_*(\mathcal G))$",
    r"=\operatorname{prof}^{*}_{x}j_*((\mathcal G))$",
    "Misplaced parenthesis; the line above has prof(j_*(G)_x). The fix restores the printed reading.",
    corrected=r"\operatorname{prof}^{*}_{x}(j_*(\mathcal G))")
add(111, "Corollaire (10.8.4): 'Sous les hypothèses de (10.8.3), la fonction'",
    "(10.8.3) upright inside the italic statement", "italic (corollary environment)", "convention", 6, "high",
    "Sous les hypothèses de (10.8.3), la fonction",
    r"Sous les hypothèses de \textup{(10.8.3)}, la fonction", REF6)
add(111, "Corollaire (10.8.4): 'la fonction x ⇝ prof*_x(F) est semi-continue inférieurement'",
    "wavy arrow ⇝", r"\mapsto", "symbol", None, "high",
    r"$x\mapsto\operatorname{prof}^{*}_{x}(\mathcal F)$ est semi-continue inférieurement.",
    r"$x\leadsto\operatorname{prof}^{*}_{x}(\mathcal F)$ est semi-continue inférieurement.", WAVY)
add(111, "proof of (10.8.4): 'puisque x ⇝ dim.proj(F_x) est semi-continue supérieurement'",
    "wavy arrow ⇝", r"\mapsto", "symbol", None, "high",
    r"$x\mapsto\dim.\operatorname{proj}(\mathcal F_x)$",
    r"$x\leadsto\dim.\operatorname{proj}(\mathcal F_x)$", WAVY)
add(111, "Proposition (10.8.5): 'Alors la fonction x ⇝ prof*_x(F) est semi-continue inférieurement dans X'",
    "wavy arrow ⇝", r"\mapsto", "symbol", None, "high",
    r"$x\mapsto\operatorname{prof}^{*}_{x}(\mathcal F)$ est semi-continue inférieurement¶dans",
    r"$x\leadsto\operatorname{prof}^{*}_{x}(\mathcal F)$ est semi-continue inférieurement¶dans", WAVY)
add(111, "end of page_111.tex / top of p. 112: 'les composantes irréductibles de X sont | ouvertes (I, 6.1.10)'",
    "p. 112 begins 'ouvertes (I, 6.1.10)' flush left: the sentence continues, no paragraph break",
    r"blank line after 'sont', before \oldpage[IV-3]{112}: paragraph break mid-sentence", "marker", None, "high",
    "irréductibles de $X$ sont¶¶", "irréductibles de $X$ sont¶",
    "Mid-sentence page break (GLOBAL_ISSUES 20); the p. 112 marker is in the right place and has no blank line after it, so this one edit suffices.")

# ---------------- page 112 ----------------
add(112, "Corollaire (10.8.6), l. 1: 'Les hypothèses étant celles de (10.8.5), pour tout x∈X'",
    "(10.8.5) upright inside the italic statement", "italic (corollary environment)", "convention", 6, "high",
    "Les hypothèses étant celles de (10.8.5), pour",
    r"Les hypothèses étant celles de \textup{(10.8.5)}, pour", REF6)
add(112, "Corollaire (10.8.6): 'pour tout point x'∈U∩{x}‾, fermé dans U, on ait'",
    "'fermé' italic, 'dans' upright (enlarged crop)", "'dans' italic (corollary environment)", "convention", 6, "high",
    "fermé dans $U$, on ait", r"fermé \textup{dans} $U$, on ait")
add(112, "Corollaire (10.8.6): '(resp. prof*_x(F) ≤ m), il faut et il suffit'",
    "'(resp.' and the closing parenthesis upright (enlarged crop)", "italic (corollary environment)",
    "convention", 6, "high",
    r"(resp.¶$\operatorname{prof}^{*}_{x}(\mathcal F)\leq m$), il faut",
    r"\textup{(resp.}¶$\operatorname{prof}^{*}_{x}(\mathcal F)\leq m$\textup{)}, il faut")
add(112, "Corollaire (10.8.6): 'pour tout x'∈V∩{x}‾, fermé dans V, on ait'",
    "'fermé' italic, 'dans' upright (enlarged crop)", "'dans' italic (corollary environment)", "convention", 6, "high",
    "fermé dans $V$, on ait", r"fermé \textup{dans} $V$, on ait")
add(112, "Corollaire (10.8.6), end: '(resp. prof(F_x') ≤ m).'",
    "'(resp.' and the closing parenthesis upright (enlarged crop)", "italic (corollary environment)",
    "convention", 6, "high",
    r"(resp.¶$\operatorname{prof}(\mathcal F_{x'})\leq m$).",
    r"\textup{(resp.}¶$\operatorname{prof}(\mathcal F_{x'})\leq m$\textup{)}.")
add(112, "proof of (10.8.6): 'de la semi-continuité inférieure de y ⇝ prof*_y(F)'",
    "wavy arrow ⇝", r"\mapsto", "symbol", None, "high",
    r"$y\mapsto\operatorname{prof}^{*}_{y}(\mathcal F)$",
    r"$y\leadsto\operatorname{prof}^{*}_{y}(\mathcal F)$", WAVY)
add(112, "proof of (10.8.6): 'si x'∈U∩{x}‾ est fermé dans U (puisque'",
    "'fermé' italic (enlarged crop)", "upright", "italics", None, "high",
    "est fermé dans $U$ (puisque", r"est \emph{fermé} dans $U$ (puisque")
add(112, "Proposition (10.8.7): 'les conditions 1°, 2° et 3° de (10.6.1). Soient X'",
    "(10.6.1) upright inside the italic statement", "italic (proposition environment)", "convention", 6, "high",
    "de (10.6.1). Soient", r"de \textup{(10.6.1)}. Soient", REF6)
add(112, "Corollaire (10.8.8): 'Les hypothèses sur f et F étant celles de (9.9.1), la fonction'",
    "(9.9.1) upright inside the italic statement", "italic (corollary environment)", "convention", 6, "high",
    "étant celles de (9.9.1), la fonction", r"étant celles de \textup{(9.9.1)}, la fonction", REF6)
add(112, "Corollaire (10.8.8): 'la fonction x ⇝ prof*_x(F_f(x)) est constructible'",
    "wavy arrow ⇝", r"\mapsto", "symbol", None, "high",
    r"$x\mapsto\operatorname{prof}^{*}_{x}(\mathcal F_{f(x)})$",
    r"$x\leadsto\operatorname{prof}^{*}_{x}(\mathcal F_{f(x)})$", WAVY)
add(112, "proof of (10.8.8): 'localement de type fini sur k(s)'", "bold italic k", "$k(s)$",
    "convention", 1, "high", "type fini sur $k(s)$", r"type fini sur $\boldsymbol{k}(s)$")
add(112, "proof of (10.8.8): 'comme en outre Spec(k(s)) vérifie'", "bold italic k", r"\operatorname{Spec}(k(s))",
    "convention", 1, "high", r"$\operatorname{Spec}(k(s))$", r"$\operatorname{Spec}(\boldsymbol{k}(s))$")
add(112, "proof of (10.8.8): 'on a prof*_x(F_f(x)) = dim_x(Supp(F_f(x))) — coprof((F_f(x))_x) (10.8.7).'",
    "the formula is set inline in the running text", "displayed with \\[ \\]", "other", None, "high",
    r"on a¶\[¶  \operatorname{prof}^{*}_{x}(\mathcal F_{f(x)})¶  =\dim_x(\operatorname{Supp}(\mathcal F_{f(x)}))¶  -\operatorname{coprof}((\mathcal F_{f(x)})_x)¶\]¶(10.8.7).",
    r"on a¶$\operatorname{prof}^{*}_{x}(\mathcal F_{f(x)})¶  =\dim_x(\operatorname{Supp}(\mathcal F_{f(x)}))¶  -\operatorname{coprof}((\mathcal F_{f(x)})_x)$¶(10.8.7).",
    "Layout only (display vs inline, GLOBAL_ISSUES 21); the formula itself matches.")
add(112, "proof of (10.8.8): 'donc les fonctions x ⇝ dim_x(Supp(F_f(x)))'",
    "wavy arrow ⇝", r"\mapsto", "symbol", None, "high",
    r"$x\mapsto\dim_x(\operatorname{Supp}(\mathcal F_{f(x)}))$",
    r"$x\leadsto\dim_x(\operatorname{Supp}(\mathcal F_{f(x)}))$", WAVY)
add(112, "proof of (10.8.8): 'et x ⇝ coprof((F_f(x))_x) sont localement constructibles'",
    "wavy arrow ⇝", r"\mapsto", "symbol", None, "high",
    r"$x\mapsto\operatorname{coprof}((\mathcal F_{f(x)})_x)$",
    r"$x\leadsto\operatorname{coprof}((\mathcal F_{f(x)})_x)$", WAVY)
add(112, "(10.9.1), l. 1: 'Soit X un préschéma de Jacobson, et soit S(X)'",
    "'préschéma de Jacobson' italic (enlarged crop)", "upright", "italics", None, "high",
    "un préschéma de Jacobson, et soit", r"un \emph{préschéma de Jacobson}, et soit")
add(112, "(10.9.1), l. 2: 'le sous-espace des points fermés de X'",
    "'fermés' italic (enlarged crop)", "upright", "italics", None, "high",
    "points fermés de $X$", r"points \emph{fermés} de $X$")
add(112, "(10.9.1), l. 2: 'le faisceau induit sur ce sous-espace par O_X'",
    "'induit' italic (enlarged crop)", "upright", "italics", None, "high",
    "le faisceau induit sur", r"le faisceau \emph{induit} sur")
add(112, "end of page_112.tex / top of p. 113: 'Comme ψ est un quasi- | homéomorphisme'",
    "the compound 'quasi-homéomorphisme' is split by the page break at its hyphen",
    "'quasi-' ends a source line before \\oldpage[IV-3]{113}: the line end typesets a space ('quasi- homéomorphisme')",
    "other", None, "high", "est un quasi-¶", "est un quasi-%¶",
    "The hyphen is part of the word and stays; '%' joins 'quasi-' to 'homéomorphisme' (\\oldpage ends with \\ignorespaces), as on EGA II p. 187.")

# ---------------- page 113 ----------------
add(113, "(10.9.1): 'et F ⇝ j*_X(F) une équivalence de la catégorie'",
    "wavy arrow ⇝", r"\mapsto", "symbol", None, "high",
    r"$\mathcal F\mapsto j_X^*(\mathcal F)$", r"$\mathcal F\leadsto j_X^*(\mathcal F)$", WAVY)
add(113, "(10.9.2): 'on obtient ainsi un morphisme d'espaces annelés S(f) = (S(ρ), S(λ)) : (S(X), O_S(X)) → (S(Y), O_S(Y)) tel que le diagramme'",
    "the formula is set inline in the running text", "displayed with \\[ \\]", "other", None, "high",
    r"annelés¶\[¶  S(f)=(S(\rho),S(\lambda)):(S(X),\mathcal O_{S(X)})\longrightarrow¶  (S(Y),\mathcal O_{S(Y)})¶\]¶tel que",
    r"annelés¶$S(f)=(S(\rho),S(\lambda)):(S(X),\mathcal O_{S(X)})\longrightarrow¶  (S(Y),\mathcal O_{S(Y)})$¶tel que",
    "Layout only (display vs inline, GLOBAL_ISSUES 21); the formula itself matches.")
add(113, "(10.9.2): 'un foncteur covariant S : C → C''", "bold italic C, C' (enlarged crop)",
    r"$S:\mathbf C\to\mathbf C'$ (bold upright)", "font", None, "high",
    r"$S:\mathbf C\to\mathbf C'$", r"$S:\boldsymbol{C}\to\boldsymbol{C}'$", CAT)
add(113, "(10.9.2): 'où C' est la catégorie des espaces annelés en anneaux locaux'", "bold italic C'",
    r"$\mathbf C'$", "font", None, "high",
    r"où $\mathbf C'$ est la catégorie", r"où $\boldsymbol{C}'$ est la catégorie", CAT)
add(113, "(10.9.2): 'et C la catégorie dont les objets sont'", "bold italic C",
    r"$\mathbf C$", "font", None, "high",
    r"et $\mathbf C$ la catégorie", r"et $\boldsymbol{C}$ la catégorie", CAT)
add(113, "(10.9.3), l. 1: 'la sous-catégorie C'' de C''", "bold italic C'', C'",
    r"$\mathbf C''$, $\mathbf C'$", "font", None, "high",
    r"sous-catégorie $\mathbf C''$ de $\mathbf C'$", r"sous-catégorie $\boldsymbol{C}''$ de $\boldsymbol{C}'$", CAT)
add(113, "(10.9.3): '2° du faisceau d'anneaux O_S(X) tel que Γ(D^m(h), O_S(X)) = A_f'",
    "A_f: subscript italic f (enlarged crop)", "$A_h$ (silently corrected)", "misprint_in_print", None, "high",
    r"\mathcal O_{S(X)})=A_h$", r"\mathcal O_{S(X)})=A_f$",
    "The basic open set is D^m(h) = D(h)∩S(X), so the ring of sections is A_h; the print has the usual letter f of A_f. The fix restores the printed reading.",
    corrected=r"\Gamma(D^m(h),\mathcal O_{S(X)})=A_h")
add(113, "(10.9.3), 3rd paragraph: 'faisant de A une B-algèbre de type fini, f = (aφ, φ~)'",
    "'de type fini' italic (enlarged crop)", "upright", "italics", None, "high",
    r"$B$-algèbre de¶type fini, $f=", r"$B$-algèbre \emph{de¶type fini}, $f=")
add(113, "(10.9.3): 'c'est-à-dire (Err_II, 1.8.2) que pour tout'",
    "'Err' bold, subscript II light (enlarged crop)", r"$\mathrm{Err}_{\mathrm{II}}$ (roman Err)", "font", None, "high",
    r"$\mathrm{Err}_{\mathrm{II}}$", r"$\mathbf{Err}_{\mathrm{II}}$",
    "Like convention 2 for chapter numbers; ega4-8-fr.tex already writes $\\mathbf{Err}_{\\mathrm{III}}$.")
add(113, "(10.9.3), end: 'θ♯_x est un homomorphisme local. Réciproquement :'",
    "'local' italic (enlarged crop)", "upright", "italics", None, "high",
    "est un homomorphisme local.", r"est un homomorphisme \emph{local}.")

# ---------------- page 114 ----------------
add(114, "(10.9.5), l. 3: 'où A est un anneau de Jacobson. Nous dirons'",
    "'anneau de Jacobson' italic (enlarged crop)", "upright", "italics", None, "high",
    "est un anneau de Jacobson. Nous dirons", r"est un \emph{anneau de Jacobson}. Nous dirons")
add(114, "(10.9.5): '1° f est un morphisme d'espaces annelés en anneaux locaux;'",
    "'espaces annelés en anneaux locaux' italic (enlarged crop)", "upright", "italics", None, "high",
    "un morphisme d'espaces annelés en anneaux locaux~;", r"un morphisme d'\emph{espaces annelés en anneaux locaux}~;")
add(114, "(10.9.5): 'une Γ(V, O_Y)-algèbre de type fini.'",
    "'algèbre de type fini' italic (enlarged crop)", "upright", "italics", None, "high",
    r"$\Gamma(V,\mathcal O_Y)$-algèbre de type fini.", r"$\Gamma(V,\mathcal O_Y)$-\emph{algèbre de type fini}.")
add(114, "(10.9.5), 2nd paragraph: 'la catégorie C''_0 ainsi définie'", "bold italic C",
    r"$\mathbf C''_0$", "font", None, "high",
    r"la catégorie $\mathbf C''_0$ ainsi", r"la catégorie $\boldsymbol{C}''_0$ ainsi", CAT)
add(114, "(10.9.5): 'de C' qui contient C'';'", "bold italic C', C''",
    r"$\mathbf C'$, $\mathbf C''$", "font", None, "high",
    r"de $\mathbf C'$ qui contient $\mathbf C''$~;", r"de $\boldsymbol{C}'$ qui contient $\boldsymbol{C}''$~;", CAT)
add(114, "(10.9.5): 'de montrer que C'' = C''_0, autrement dit :'", "bold italic C'', C''_0",
    r"$\mathbf C''=\mathbf C''_0$", "font", None, "high",
    r"$\mathbf C''=\mathbf C''_0$, autrement", r"$\boldsymbol{C}''=\boldsymbol{C}''_0$, autrement", CAT)
add(114, "Proposition (10.9.6): 'Le foncteur X ⇝ S(X) de C dans C''_0'",
    "wavy arrow ⇝", r"\mapsto", "symbol", None, "high",
    r"Le foncteur $X\mapsto S(X)$", r"Le foncteur $X\leadsto S(X)$", WAVY)
add(114, "Proposition (10.9.6): 'de C dans C''_0 est une équivalence de catégories'", "bold italic C, C''_0",
    r"$\mathbf C$, $\mathbf C''_0$", "font", None, "high",
    r"$\mathbf C$ dans $\mathbf C''_0$", r"$\boldsymbol{C}$ dans $\boldsymbol{C}''_0$", CAT)
add(114, "proof of (10.9.6), 1°: 'le foncteur X ⇝ S(X) est pleinement fidèle'",
    "wavy arrow ⇝", r"\mapsto", "symbol", None, "high",
    r"le foncteur $X\mapsto S(X)$ est", r"le foncteur $X\leadsto S(X)$ est", WAVY)
add(114, "proof of (10.9.6), 1°: 'pour X, Y dans C, l'application canonique'", "bold italic C",
    r"$\mathbf C$", "font", None, "high",
    r"dans $\mathbf C$,¶l'application", r"dans $\boldsymbol{C}$,¶l'application", CAT)
add(114, "proof of (10.9.6), 1°, display: 'Hom_C(X, Y) → Hom_{C_0'}(S(X), S(Y))'",
    "second subscript C_0' with a single prime set after the 0 (enlarged crop); both subscript C's are bold upright",
    r"\operatorname{Hom}_{\mathbf C''_0} (silently corrected)", "misprint_in_print", None, "high",
    r"\operatorname{Hom}_{\mathbf C''_0}(S(X),S(Y))", r"\operatorname{Hom}_{\mathbf C_0{}'}(S(X),S(Y))",
    "The category is C''_0 (text before and after). The bold upright subscript C matches \\mathbf C; only the primes are changed.",
    corrected=r"\operatorname{Hom}_{\mathbf C''_0}(S(X),S(Y))")
add(114, "proof of (10.9.6), 1°: 'induisent la même section au-dessus de S(X)'",
    "'même' italic (enlarged crop)", "upright", "italics", None, "high",
    "induisent la¶même section", r"induisent la¶\emph{même} section")
add(114, "proof of (10.9.6), 1°: '(pour la catégorie C''_0)'", "bold italic C''_0",
    r"$\mathbf C''_0$", "font", None, "high",
    r"(pour la catégorie $\mathbf C''_0$)", r"(pour la catégorie $\boldsymbol{C}''_0$)", CAT)
add(114, "proof of (10.9.6), 1°: 'il existe un recouvrement ouvert ultra-affine (U') (resp. (V'_μ))'",
    "(U' ): no index λ under the prime, a blank where it would stand (enhanced crop shows no trace)",
    r"$(U'_\lambda)$ (silently corrected)", "misprint_in_print", None, "medium",
    r"ultra-affine $(U'_\lambda)$ (resp.", r"ultra-affine $(U')$ (resp.",
    "Same omission two lines lower (next entry), while h_λ : U'_λ → V'_μ has the index: a missing inferior, not faint type. Medium only as to typesetting slip versus a dropped sort.",
    corrected=r"$(U'_\lambda)$")
add(114, "proof of (10.9.6), 1°: 'On peut supposer que U' = U_λ∩S(X) et V'_μ = V_μ∩S(Y)'",
    "U' without the index λ, a blank before '=' (enhanced crop shows no trace)",
    r"$U'_\lambda=U_\lambda\cap S(X)$ (silently corrected)", "misprint_in_print", None, "medium",
    r"$U'_\lambda=U_\lambda\cap S(X)$", r"$U'=U_\lambda\cap S(X)$",
    "As the previous entry.",
    corrected=r"$U'_\lambda=U_\lambda\cap S(X)$")
add(114, "proof of (10.9.6), 1°: 'des ouverts affines uniquement déterminés dans X et Y'",
    "'uniquement déterminés' italic (enlarged crop)", "upright", "italics", None, "high",
    "affines uniquement déterminés dans", r"affines \emph{uniquement déterminés} dans")

# ---------------- checks ----------------
pages = {}
for p in range(110, 115):
    pages[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
bad = 0
for x in F:
    fx = x["fix"]
    if fx is None:
        continue
    n = pages[x["page"]].count(fx["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", x["page"], n, repr(fx["old"][:80]))
    if fx["old"] == fx["new"]:
        bad += 1
        print("NO CHANGE", x["page"], repr(fx["old"][:80]))
# overlapping olds on the same page
for p in pages:
    spans = []
    for x in F:
        if x["page"] == p and x["fix"]:
            i = pages[p].find(x["fix"]["old"])
            spans.append((i, i + len(x["fix"]["old"]), x["where"][:60]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            print("OVERLAP", p, a, b)
cnt = collections.defaultdict(lambda: [0, 0, 0])
for x in F:
    k = 1 if x["kind"] == "convention" else (2 if x["kind"] == "misprint_in_print" else 0)
    cnt[x["page"]][k] += 1
print({p: tuple(v) for p, v in sorted(cnt.items())}, "total", len(F), "bad", bad)
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("written", OUT)
