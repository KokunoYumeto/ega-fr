"""Build findings_076_079.json for EGA 0_III pp. 76-79 and check every fix's "old" (exactly once in its page_NNN.tex,
LF-normalised), then simulate applying each page's fixes in list order and in reverse order."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding='utf-8')
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0III")
OUT = RUN / "findings_076_079.json"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, fix_null=False):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf)
    d["fix"] = None if fix_null else {"old": old, "new": new}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


MARK76 = r"\oldpage[0\textsubscript{III}]{76}"
MARK77 = r"\oldpage[0\textsubscript{III}]{77}"
MARK80 = r"\oldpage[0\textsubscript{III}]{80}"

# ---------------------------------------------------------------- page 75 (counterpart of the p. 76 marker finding)
add(75, "end of the p. 75 segment, (13.7.2): 'avec les filtrations, ... de complexes.'",
    "printed p. 75 ends with '... un morphisme de complexes X_{k+1} -> X_k compatibles'; 'avec les filtrations, et faisant de X = (X_k)_{k in Z} un systeme projectif de complexes.' is the first line of printed p. 76",
    "this sentence end stands before \\oldpage[0\\textsubscript{III}]{76}",
    "marker", None, "high",
    " avec les\nfiltrations, et faisant de\n" + r"$\mathbf X^\bullet=(X_k^\bullet)_{k\in\mathbb Z}$ un système projectif" + "\nde complexes.",
    "",
    "OUTSIDE MY PAGES (p. 75 segment). First half of a two-part text move; the p. 76 marker finding re-inserts this text "
    "after \\oldpage[0\\textsubscript{III}]{76} (with \\emph{système projectif}, printed italic). Each edit stays in its own "
    "page segment, order does not matter; apply both or neither. Result: '... compatibles' + newline + marker + 'avec les filtrations ...'.")

# ---------------------------------------------------------------- page 76
add(76, "top of p. 76", "p. 76 begins 'avec les filtrations, et faisant de X = (X_k)_{k in Z} un systeme projectif (italic) de complexes. On peut en outre ...'",
    "p. 76 segment begins 'On peut en outre'; the first printed line sits at the end of the p. 75 segment",
    "marker", None, "high",
    MARK76 + "\nOn peut en outre",
    MARK76 + "\navec les\nfiltrations, et faisant de\n" + r"$\mathbf X^\bullet=(X_k^\bullet)_{k\in\mathbb Z}$ un \emph{système projectif}" + "\nde complexes.\nOn peut en outre",
    "Second half of the move begun by the page-75 finding (which deletes this text from the end of the p. 75 segment). "
    "Apply both or neither. The re-inserted text also sets 'système projectif' italic as printed (TeX upright).")

add(76, "(13.7.2), l. 2", "est strict. (strict italic)", "est strict.", "italics", None, "high",
    "est strict. Pour", r"est \emph{strict}. Pour", "")
add(76, "(13.7.2), l. 4", "A_{k+1}/F^{k+1}(A_{k+1}) egale a X_k (egale italic)", "égale à $X_k^\\bullet$ (upright)", "italics", None, "high",
    r"égale à $X_k^\bullet$", r"\emph{égale} à $X_k^\bullet$", "")
add(76, "(13.7.2), l. 6-7", "un isomorphisme (italic, hyphenated iso-morphisme)", "un isomorphisme (upright)", "italics", None, "high",
    "aux quotients un isomorphisme", r"aux quotients un \emph{isomorphisme}", "")
add(76, "(13.7.2), l. 7", "X_{k+1}/F^{k+1}(X_{k+1}) ~-> X_k set inline in the text line ('... un isomorphisme X.../F...(X...) ~-> X_k respectant les filtrations')",
    "displayed with \\[ \\]", "other", None, "high",
    "\\[\n" + r"X_{k+1}^\bullet/\mathrm F^{k+1}(X_{k+1}^\bullet)" + "\n" + r"\xrightarrow{\sim}X_k^\bullet" + "\n\\]",
    r"$X_{k+1}^\bullet/\mathrm F^{k+1}(X_{k+1}^\bullet)" + "\n" + r"\xrightarrow{\sim}X_k^\bullet$",
    "Display in the TeX, inline in the print.")

add(76, "Proposition (13.7.4), first sentence", "'(Shih). — Soit n un entier. Les deux conditions suivantes sont équivalentes :' italic",
    "\\emph{...} around the sentence inside the \\itshape proposition environment: renders upright", "convention", 6, "high",
    r"\emph{(Shih). --- Soit $n$ un entier. Les deux conditions suivantes sont" + "\néquivalentes :}",
    r"(Shih). --- Soit $n$ un entier. Les deux conditions suivantes sont" + "\néquivalentes :",
    "The statement environments are \\itshape (EGA_FR.tex), so a \\emph wrapper sets the whole body upright. Drop the wrapper. "
    "Document-wide pattern: 24 statements of ega3-1-fr.tex (11.8.3 ... 13.7.5) wrap their body in \\emph.")
add(76, "Proposition (13.7.4) a)", "a) (upright label) Pour tout couple ... essentiellement constant. (italic)",
    "\\emph{Pour tout couple ...} renders upright", "convention", 6, "high",
    r"\emph{Pour tout couple $(p,q)$ tel que $p+q=n$, le" + "\n" + r"système projectif $(\mathrm E_r^{pq}(\mathbf A))_{r\geq2}$ est" + "\nessentiellement constant.}",
    r"Pour tout couple $(p,q)$ tel que $p+q=n$, le" + "\n" + r"système projectif $(\mathrm E_r^{pq}(\mathbf A))_{r\geq2}$ est" + "\nessentiellement constant.",
    "The labels a), b) are upright in the print; \\item[\\emph{a)}] already renders upright in the italic environment, keep it.")
add(76, "Proposition (13.7.4) b)", "b) Le système projectif R^nT(A) = (R^nT(A_k))_{k in Z} vérifie (italic) (ML) (upright).",
    "\\emph{Le système projectif ... vérifie (ML).} renders upright", "convention", 6, "high",
    r"\emph{Le système projectif" + "\n" + r"$\mathrm R^n\mathrm T(\mathbf A)=" + "\n" + r"(\mathrm R^n\mathrm T(A_k))_{k\in\mathbb Z}$ vérifie (ML).}",
    r"Le système projectif" + "\n" + r"$\mathrm R^n\mathrm T(\mathbf A)=" + "\n" + r"(\mathrm R^n\mathrm T(A_k))_{k\in\mathbb Z}$ vérifie \textup{(ML)}.",
    "Drop the wrapper; (ML) is upright in the print, hence \\textup.")
add(76, "Proposition (13.7.4), 'En outre ...'", "En outre, lorsque ces conditions sont remplies, on a un isomorphisme canonique (italic)",
    "\\emph{...} renders upright", "convention", 6, "high",
    r"\emph{En outre, lorsque ces conditions sont remplies, on a un" + "\nisomorphisme canonique}",
    r"En outre, lorsque ces conditions sont remplies, on a un" + "\nisomorphisme canonique",
    "")
add(76, "(13.7.4.1)", "pour tout p in Z. (italic)", "\\qquad\\emph{pour tout ...} in the equation of the \\itshape environment: upright", "convention", 6, "high",
    r"\qquad\emph{pour tout $p\in\mathbb Z$.}" + "\n" + r"\end{equation}" + "\n" + r"\end{proposition}",
    r"\qquad\textit{pour tout $p\in\mathbb Z$.}" + "\n" + r"\end{equation}" + "\n" + r"\end{proposition}",
    "")
add(76, "proof of (13.7.4), l. 3", "gr^p(R^n(T(A_k)) — an extra opening parenthesis after R^n (three '(' , two ')')",
    "$\\operatorname{gr}^p(\\mathrm R^n\\mathrm T(A_k))$ (silently corrected)", "misprint_in_print", None, "high",
    r"$\operatorname{gr}^p(\mathrm R^n\mathrm T(A_k))$ est canoniquement",
    r"$\operatorname{gr}^p(\mathrm R^n(\mathrm T(A_k))$ est canoniquement",
    "The TeX silently corrects the print; the fix restores the printed reading.",
    corrected=r"$\operatorname{gr}^p(\mathrm R^n\mathrm T(A_k))$")
add(76, "Corollaire (13.7.5), opening of the statement", "the statement is italic",
    "\\emph{Soit ... canonique} around the whole statement inside the \\itshape corollary environment: renders upright", "convention", 6, "high",
    r"\label{0.13.7.5-fr}" + "\n" + r"\emph{Soit",
    r"\label{0.13.7.5-fr}" + "\n" + "Soit",
    "Opening half of the wrapper removal; the closing brace is removed by the next finding ('On a alors un isomorphisme canonique}'). "
    "APPLY TOGETHER (unbalanced braces otherwise), with the \\textup{(13.3.1)} finding. After the change the inner "
    "\\emph{(i)}, \\emph{(ii)}, \\emph{(iii)} render upright, as printed (they render italic at present).")
add(76, "Corollaire (13.7.5), end of the statement", "On a alors un isomorphisme canonique (italic)",
    "closing brace of the \\emph wrapper", "convention", 6, "high",
    "On a alors un isomorphisme canonique}", "On a alors un isomorphisme canonique",
    "Closing half of the wrapper removal begun by the previous finding; apply together.")
add(76, "Corollaire (13.7.5), l. 1", "Soit 𝔉 = (𝓕_k)_{k in N}: the system letter is an outlined (bold) script F, a different glyph from the script 𝓕_k and from 𝓕 = lim 𝓕_k",
    "$\\mathcal F=(\\mathcal F_k)$: same \\mathcal F as the limit sheaf ('Soit F = (F_k) ... et soit F = lim F_k')", "font", None, "high",
    r"Soit $\mathcal F=(\mathcal F_k)_{k\in\mathbb N}$",
    r"Soit $\boldsymbol{\mathcal F}=(\mathcal F_k)_{k\in\mathbb N}$",
    "Enlarged crops: the projective system (also in E_r^{pq}(.) and E_infty(.) of (13.7.5)/(13.7.5.1) and in R^{n+1}Gamma(.) on p. 77) "
    "is printed with an outlined script F; the sheaf F = lim F_k and H^{n+1}(X, F) use the ordinary script F. Bold script "
    "(\\boldsymbol{\\mathcal F}), like the bold A and X for systems in this section; same occurrences on p. 77.")
add(76, "Corollaire (13.7.5), l. 2", "(13.3.1) upright inside the italic statement",
    "(\\hyperref[0.13.3.1-fr]{13.3.1}) — upright only because of the \\emph wrapper; italic once the wrapper is dropped", "convention", 6, "high",
    r"(\hyperref[0.13.3.1-fr]{13.3.1}) et soit",
    r"\textup{(\hyperref[0.13.3.1-fr]{13.3.1})} et soit",
    "Companion of the (13.7.5) wrapper removal (harmless on its own).")
add(76, "Corollaire (13.7.5), l. 2", "𝓕 = lim 𝓕_k with no index under lim",
    "\\varprojlim_k", "formula", None, "high",
    r"$\mathcal F=\varprojlim_k\mathcal F_k$", r"$\mathcal F=\varprojlim\mathcal F_k$",
    "Enlarged crop: only the arrow under lim, no k.")
add(76, "Corollaire (13.7.5), l. 3", "pour le foncteur G ~> Gamma(X, G): wavy arrow", "\\mathcal G\\mapsto\\Gamma(X,\\mathcal G)", "symbol", None, "high",
    r"$\mathcal G\mapsto\Gamma(X,\mathcal G)$", r"$\mathcal G\leadsto\Gamma(X,\mathcal G)$",
    "Edition point for this file: the print's wavy arrow is \\leadsto.")
add(76, "Corollaire (13.7.5), l. 3", "(E_r^{pq}(𝔉))_{r in Z}: outlined (bold) script F", "(\\mathrm E_r^{pq}(\\mathcal F))", "font", None, "high",
    r"(\mathrm E_r^{pq}(\mathcal F))_{r\in\mathbb Z}", r"(\mathrm E_r^{pq}(\boldsymbol{\mathcal F}))_{r\in\mathbb Z}",
    "See the first bold-script finding of (13.7.5).")
add(76, "(13.7.5.1)", "E_infty^{p,n-p+1}(𝔉): outlined (bold) script F", "\\mathrm E_\\infty^{p,n-p+1}(\\mathcal F)", "font", None, "high",
    r"\mathrm E_\infty^{p,n-p+1}(\mathcal F)", r"\mathrm E_\infty^{p,n-p+1}(\boldsymbol{\mathcal F})",
    "See the first bold-script finding of (13.7.5). H^{n+1}(X, F) on the left keeps the ordinary script F.")
add(76, "(13.7.5.1)", "pour tout p in Z. (italic)", "\\qquad\\emph{pour tout ...} in the \\itshape corollary: upright", "convention", 6, "high",
    r"\qquad\emph{pour tout $p\in\mathbb Z$.}" + "\n" + r"\end{equation}" + "\n" + r"\end{corollary}",
    r"\qquad\textit{pour tout $p\in\mathbb Z$.}" + "\n" + r"\end{equation}" + "\n" + r"\end{corollary}",
    "")

# ---------------------------------------------------------------- page 77
add(77, "top of p. 77 / end of p. 76 (proof of (13.7.5))",
    "p. 76 ends '... que l'on a un isomorphisme'; p. 77 begins 'canonique gr^p(R^{n+1}Gamma(𝔉)) ...'; C and C' bold italic",
    "the p. 77 marker stands before 'Il résulte de (13.7.4) ...' (right after \\begin{proof}); $C$, $C'$ plain", "marker", None, "high",
    MARK77 + "\n" + r"Il résulte de (\hyperref[0.13.7.4-fr]{13.7.4}) appliqué au cas où $C$" + "\n"
    + r"est la catégorie des faisceaux de groupes abéliens sur $X$, $C'$ la" + "\n"
    + r"catégorie des groupes abéliens, et $\mathrm T=\Gamma$, que l'on a un" + "\nisomorphisme canonique",
    r"Il résulte de (\hyperref[0.13.7.4-fr]{13.7.4}) appliqué au cas où $\boldsymbol{C}$" + "\n"
    + r"est la catégorie des faisceaux de groupes abéliens sur $X$, $\boldsymbol{C}'$ la" + "\n"
    + r"catégorie des groupes abéliens, et $\mathrm T=\Gamma$, que l'on a un" + "\nisomorphisme\n" + MARK77 + "\ncanonique",
    "One atomic edit inside the p. 77 segment: the marker moves after 'isomorphisme', so these four lines fall into p. 76 "
    "(where they are printed). It also sets the category letters C, C' bold italic (\\boldsymbol), as printed; no separate "
    "font findings for these two letters.")
add(77, "l. 1", "gr^p(R^{n+1}Gamma(𝔉)) ~-> E_infty^{p,n-p+1}(𝔉): outlined (bold) script F twice", "\\mathcal F twice", "font", None, "high",
    r"$\operatorname{gr}^p(\mathrm R^{n+1}\Gamma(\mathcal F))" + "\n" + r"\xrightarrow{\sim}\mathrm E_\infty^{p,n-p+1}(\mathcal F)$ pour tout",
    r"$\operatorname{gr}^p(\mathrm R^{n+1}\Gamma(\boldsymbol{\mathcal F}))" + "\n" + r"\xrightarrow{\sim}\mathrm E_\infty^{p,n-p+1}(\boldsymbol{\mathcal F})$ pour tout",
    "Projective system of (13.7.5) (see p. 76).")
add(77, "after (13.7.5.1)", "Comme le système projectif R^{n+1}Gamma(𝔉): outlined (bold) script F", "\\Gamma(\\mathcal F)", "font", None, "high",
    r"Comme le système projectif $\mathrm R^{n+1}\Gamma(\mathcal F)$ vérifie",
    r"Comme le système projectif $\mathrm R^{n+1}\Gamma(\boldsymbol{\mathcal F})$ vérifie", "")
add(77, "after (13.7.5.1), l. 2", "gr^p(R^{n+1}Gamma(𝔉)) ~-> lim_k gr^p(H^{n+1}(X, F_k)) (13.4.3): inline in the text line; outlined (bold) script F",
    "displayed with \\[ \\]; \\mathcal F", "other", None, "high",
    "canonique\n\\[\n" + r"\operatorname{gr}^p(\mathrm R^{n+1}\Gamma(\mathcal F))" + "\n" + r"\xrightarrow{\sim}" + "\n"
    + r"\varprojlim_k\operatorname{gr}^p(H^{n+1}(X,\mathcal F_k))" + "\n\\]",
    "canonique\n" + r"$\operatorname{gr}^p(\mathrm R^{n+1}\Gamma(\boldsymbol{\mathcal F}))" + "\n" + r"\xrightarrow{\sim}" + "\n"
    + r"\varprojlim_k\operatorname{gr}^p(H^{n+1}(X,\mathcal F_k))$",
    "Display in the TeX, inline in the print; the same edit sets the bold script F of the projective system.")
add(77, "after (13.7.5.1), l. 3", "lim_k gr^p(H^{n+1}(X, F_k)) ~-> gr^p(lim_k H^{n+1}(X, F_k)) (13.4.5): inline",
    "displayed with \\[ \\]", "other", None, "high",
    "canonique\n\\[\n" + r"\varprojlim_k\operatorname{gr}^p(H^{n+1}(X,\mathcal F_k))" + "\n" + r"\xrightarrow{\sim}" + "\n"
    + r"\operatorname{gr}^p(\varprojlim_k H^{n+1}(X,\mathcal F_k))" + "\n\\]",
    "canonique\n" + r"$\varprojlim_k\operatorname{gr}^p(H^{n+1}(X,\mathcal F_k))" + "\n" + r"\xrightarrow{\sim}" + "\n"
    + r"\operatorname{gr}^p(\varprojlim_k H^{n+1}(X,\mathcal F_k))$",
    "Display in the TeX, inline in the print.")
add(77, "display (13.7.5.1) in the proof of (13.7.5)",
    "the proof's display H^{n+1}(X, F) ~-> lim_k H^{n+1}(X, F_k) is numbered (13.7.5.1), the number of the statement's display on p. 76; 'Tout revient donc à voir que l'isomorphisme (13.7.5.1) est compatible avec les filtrations' refers to the proof's display",
    "\\tag{13.7.5.1} (label 0.13.7.5.1b-fr): keeps the printed number", "misprint_in_print", None, "medium",
    None, None,
    "Duplicate equation number in the print; TeX keeps it. Corrected edition: number the proof's display (13.7.5.2) and cite "
    "(13.7.5.2) in 'Tout revient donc à voir que l'isomorphisme (13.7.5.1) ...'. Link issue in both editions: that citation "
    "hyperrefs 0.13.7.5.1-fr (the statement's display) instead of 0.13.7.5.1b-fr.",
    corrected=r"\tag{13.7.5.2}; Tout revient donc à voir que l'isomorphisme (13.7.5.2)", fix_null=True)
add(77, "diagram in the proof of (13.7.5)",
    "triangle: H^{n+1}(X, F) ~-> lim_k H^{n+1}(X, F_k) on top, H^{n+1}(X, F_{p-1}) centred below, arrows ↘ from the left and ↙ from the right",
    "\\xymatrix with the bottom object under the right one and a vertical arrow \\ar[d] from lim", "formula", None, "high",
    r"H^{n+1}(X,\mathcal F)\ar[r]^{\sim}\ar[dr]" + "\n" + r"&\varprojlim_k H^{n+1}(X,\mathcal F_k)\ar[d]\\" + "\n" + r"&H^{n+1}(X,\mathcal F_{p-1})",
    r"H^{n+1}(X,\mathcal F)\ar[rr]^{\sim}\ar[dr]" + "\n" + r"&&\varprojlim_k H^{n+1}(X,\mathcal F_k)\ar[dl]\\" + "\n" + r"&H^{n+1}(X,\mathcal F_{p-1})&",
    "Arrow direction ↙ vs ↓; the isomorphism arrow keeps its \\sim label.")
add(77, "(13.7.6), l. 3", "soit un S-C-module filtré: C bold italic", "$C$", "font", None, "high",
    r"soit un $S$-$C$-", r"soit un $S$-$\boldsymbol{C}$-",
    "Bold italic category letter C (edition point for this file), \\boldsymbol as on pp. 5-24.")
add(77, "(13.7.6), l. 3", "S-C-module filtré (13.6.6): 'module filtré' italic", "upright", "italics", None, "high",
    "module filtré\n" + r"(\hyperref[0.13.6.6-fr]{13.6.6})", r"\emph{module filtré}" + "\n" + r"(\hyperref[0.13.6.6-fr]{13.6.6})", "")
add(77, "(13.7.6), l. 4", "pour la structure de S-C-module filtré: C bold italic (module filtré upright here)", "$C$", "font", None, "high",
    r"structure de $S$-$C$-module", r"structure de $S$-$\boldsymbol{C}$-module", "")
add(77, "(13.7.6), l. 5", "système projectif de S-C-modules filtrés: C bold italic", "$C$", "font", None, "high",
    r"projectif de $S$-$C$-modules filtrés}", r"projectif de $S$-$\boldsymbol{C}$-modules filtrés}", "")
add(77, "(13.7.6), l. 7", "gr(S)-C'-module bigradué (13.6.5): C' bold italic", "$C'$", "font", None, "high",
    "structures de\n" + r"$\operatorname{gr}^\bullet(S)$-$C'$-", "structures de\n" + r"$\operatorname{gr}^\bullet(S)$-$\boldsymbol{C}'$-", "")
add(77, "(13.7.6), l. 7", "'module bigradué' italic", "upright", "italics", None, "high",
    "module bigradué\n" + r"(\hyperref[0.13.6.5-fr]{13.6.5})", r"\emph{module bigradué}" + "\n" + r"(\hyperref[0.13.6.5-fr]{13.6.5})", "")
add(77, "(13.7.6), l. 8", "gr(S)-C'-modules bigradués pour r fini: C' bold italic", "$C'$", "font", None, "high",
    r"$C'$-modules bigradués pour", r"$\boldsymbol{C}'$-modules bigradués pour", "")
add(77, "(13.7.6), l. 10", "les sous-objets respectifs des précédents obtenu en ne prenant (singular 'obtenu')",
    "obtenus (silently corrected)", "misprint_in_print", None, "high",
    "obtenus en ne prenant", "obtenu en ne prenant",
    "Enlarged crop: 'obtenu' without s; the participle agrees with 'sous-objets'. The fix restores the printed reading.",
    corrected="obtenus")
add(77, "(13.7.6), l. 11", "ce sont des gr(S)-C'-modules gradués: C' bold italic", "$C'$", "font", None, "high",
    "ce sont des\n" + r"$\operatorname{gr}^\bullet(S)$-$C'$-", "ce sont des\n" + r"$\operatorname{gr}^\bullet(S)$-$\boldsymbol{C}'$-", "")
add(77, "(13.7.6), l. 11", "'modules gradués' italic", "upright", "italics", None, "high",
    "modules gradués.\n\nLorsque", r"\emph{modules gradués}." + "\n\nLorsque", "")
add(77, "(13.7.6), 2nd paragraph, l. 2", "un gr(S)-C'-module bigradué: C' bold italic", "$C'$", "font", None, "high",
    r"$C'$-module bigradué, et chaque", r"$\boldsymbol{C}'$-module bigradué, et chaque", "")
add(77, "(13.7.6), 2nd paragraph, l. 2", "un gr(S)-C'-module gradué.: C' bold italic", "$C'$", "font", None, "high",
    r"$C'$-module gradué. En outre", r"$\boldsymbol{C}'$-module gradué. En outre", "")
add(77, "(13.7.6), 2nd paragraph, l. 4", "structure de gr(S)-C'-module gradué de E_infty^{(n)}(A_k): C' bold italic", "$C'$", "font", None, "high",
    r"$C'$-module gradué de", r"$\boldsymbol{C}'$-module gradué de", "")
add(77, "(13.7.6), 2nd paragraph, l. 7", "l'isomorphisme canonique gr(R^nT(A) ~-> lim_k gr(R^nT(A_k)): the closing parenthesis after A is missing",
    "\\operatorname{gr}^\\bullet(\\mathrm R^n\\mathrm T(\\mathbf A)) (silently corrected)", "misprint_in_print", None, "high",
    r"$\operatorname{gr}^\bullet(\mathrm R^n\mathrm T(\mathbf A))" + "\n" + r"\xrightarrow{\sim}",
    r"$\operatorname{gr}^\bullet(\mathrm R^n\mathrm T(\mathbf A)" + "\n" + r"\xrightarrow{\sim}",
    "Enlarged crop: one ')' after the bold A. The fix restores the printed reading.",
    corrected=r"$\operatorname{gr}^\bullet(\mathrm R^n\mathrm T(\mathbf A))")
add(77, "(13.7.6), last line", "structures de gr(S)-C'-module gradué.: C' bold italic", "$C'$", "font", None, "high",
    r"structures de $\operatorname{gr}^\bullet(S)$-$C'$-", r"structures de $\operatorname{gr}^\bullet(S)$-$\boldsymbol{C}'$-", "")
add(77, "(13.7.6), last line", "'module gradué' italic", "upright", "italics", None, "high",
    "module gradué.\n" + r"\end{env}", r"\emph{module gradué}." + "\n" + r"\end{env}", "")
add(77, "Proposition (13.7.7), l. 1", "Supposons que C soit une catégorie abélienne: C bold italic", "$C$", "font", None, "high",
    r"Supposons que $C$ soit", r"Supposons que $\boldsymbol{C}$ soit", "")
add(77, "Proposition (13.7.7), l. 3", "foncteur covariant additif de C dans: C bold italic", "$C$", "font", None, "high",
    r"additif de $C$ dans", r"additif de $\boldsymbol{C}$ dans", "")

# ---------------------------------------------------------------- page 78
add(78, "Proposition (13.7.7), l. 1", "système projectif strict de S-C-modules filtrés: C bold italic", "$C$", "font", None, "high",
    r"strict de $S$-$C$-modules filtrés", r"strict de $S$-$\boldsymbol{C}$-modules filtrés", "")
add(78, "(13.7.7), condition (F_n)", "E_1^{(m)}(A) = (R^mT(gr^p(A)))_{p in Z} set inline in the text line",
    "displayed with \\[ \\] (and \\bigl( \\bigr))", "other", None, "high",
    "gradué\n\\[\n" + r"\mathrm E_1^{(m)}(\mathbf A)=" + "\n" + r"\bigl(\mathrm R^m\mathrm T(\operatorname{gr}^p(\mathbf A))\bigr)_{p\in\mathbb Z}" + "\n\\]",
    "gradué\n" + r"$\mathrm E_1^{(m)}(\mathbf A)=" + "\n" + r"(\mathrm R^m\mathrm T(\operatorname{gr}^p(\mathbf A)))_{p\in\mathbb Z}$",
    "Display in the TeX, inline in the print (ordinary-size parentheses).")
add(78, "(13.7.7), condition (F_n)", "... )_{p in Z} (13.7.3.1) est de type fini: no 'de' before (13.7.3.1); (13.7.3.1) upright",
    "de (\\hyperref[0.13.7.3.1-fr]{13.7.3.1}) est de type fini (italic reference)", "extra", None, "high",
    "\nde " + r"(\hyperref[0.13.7.3.1-fr]{13.7.3.1}) est de type fini",
    "\n" + r"\textup{(\hyperref[0.13.7.3.1-fr]{13.7.3.1})} est de type fini",
    "Enlarged crop: no 'de'. The same edit sets the reference upright inside the italic statement (convention 6).")
add(78, "(13.7.7) (i)", "vérifient (ML).: (ML) upright", "(ML) italic in the \\itshape environment", "convention", 6, "high",
    "vérifient (ML).", r"vérifient \textup{(ML)}.", "")
add(78, "(13.7.7) (ii)", "R'^nT(A) = lim_k R^nT(A_k), set inline in the text line", "displayed with \\[ \\]", "other", None, "high",
    "Si on pose\n\\[\n" + r"\mathrm R'^{\,n}\mathrm T(\mathbf A)=" + "\n" + r"\varprojlim_k\mathrm R^n\mathrm T(A_k)," + "\n\\]",
    "Si on pose\n" + r"$\mathrm R'^{\,n}\mathrm T(\mathbf A)=" + "\n" + r"\varprojlim_k\mathrm R^n\mathrm T(A_k)$,",
    "Display in the TeX, inline in the print.")
add(78, "(13.7.7) (iii)", "F^p(R'^nT(A)) = Ker(R'^nT(A) -> R^nT(A_{p-1})) (p in Z) set inline in the text line", "displayed with \\[ \\]", "other", None, "high",
    "La filtration définie par\n\\[\n" + r"\mathrm F^p(\mathrm R'^{\,n}\mathrm T(\mathbf A))=" + "\n"
    + r"\operatorname{Ker}\bigl(\mathrm R'^{\,n}\mathrm T(\mathbf A)" + "\n" + r"\longrightarrow\mathrm R^n\mathrm T(A_{p-1})\bigr)" + "\n"
    + r"\quad(p\in\mathbb Z)" + "\n\\]",
    "La filtration définie par\n" + r"$\mathrm F^p(\mathrm R'^{\,n}\mathrm T(\mathbf A))=" + "\n"
    + r"\operatorname{Ker}(\mathrm R'^{\,n}\mathrm T(\mathbf A)" + "\n" + r"\to\mathrm R^n\mathrm T(A_{p-1}))$ $(p\in\mathbb Z)$",
    "Display in the TeX, inline in the print.")
add(78, "(13.7.7) (iii), l. 2", "JF^p(R'^nT(A)) ⊂ F^{p+1}(R'^n(T(A)): an extra '(' after R'^n (three '(' , two ')')",
    "\\mathrm F^{p+1}(\\mathrm R'^{\\,n}\\mathrm T(\\mathbf A)) (silently corrected)", "misprint_in_print", None, "high",
    r"\subset\mathrm F^{p+1}(\mathrm R'^{\,n}\mathrm T(\mathbf A))$ pour tout",
    r"\subset\mathrm F^{p+1}(\mathrm R'^{\,n}(\mathrm T(\mathbf A))$ pour tout",
    "Enlarged crop. The fix restores the printed reading.",
    corrected=r"\subset\mathrm F^{p+1}(\mathrm R'^{\,n}\mathrm T(\mathbf A))")
add(78, "(13.7.7) (iv), l. 2", "E_infty^{pq}(A) est donc défini (13.5.7): reference upright", "(13.5.7) italic in the \\itshape environment", "convention", 6, "high",
    r"(\hyperref[0.13.5.7-fr]{13.5.7}) et on a", r"\textup{(\hyperref[0.13.5.7-fr]{13.5.7})} et on a", "")
add(78, "proof of (13.7.7), l. 1", "permettra de noter R^nT(A) par abus de langage (no comma after R^nT(A))",
    "$\\mathrm R^n\\mathrm T(\\mathbf A)$, par abus", "punctuation", None, "high",
    r"permettra de noter $\mathrm R^n\mathrm T(\mathbf A)$, par abus", r"permettra de noter $\mathrm R^n\mathrm T(\mathbf A)$ par abus",
    "Enlarged crop.")
add(78, "proof of (13.7.7), l. 2", "du système projectif R^nT(A), with the bold A of the system (no index k)",
    "$\\mathrm R^n\\mathrm T(A_k)$", "formula", None, "high",
    r"$\mathrm R^n\mathrm T(A_k)$, compte tenu", r"$\mathrm R^n\mathrm T(\mathbf A)$, compte tenu",
    "Enlarged crop: R^nT(A) with bold A, as in (13.7.4) b).")
add(78, "proof of (13.7.7), 2nd paragraph, l. 2", "sous-gr(S)-modules gradués (one word)",
    "'sous-$\\operatorname{gr}^\\bullet(S)$-' at a line end: the line break typesets a space after the hyphen ('...(S)- modules')", "other", None, "high",
    "sous-" + r"$\operatorname{gr}^\bullet(S)$" + "-\nmodules gradués", "sous-" + r"$\operatorname{gr}^\bullet(S)$" + "-%\nmodules gradués",
    "Spurious space inside the compound; '%' keeps the line structure.")
add(78, "proof of (13.7.7), 2nd paragraph, l. 3", "est stationnaire (italic)", "upright", "italics", None, "high",
    "est\nstationnaire pour", "est\n" + r"\emph{stationnaire} pour", "")
add(78, "proof of (13.7.7), 2nd paragraph, l. 3", "la condition b) (italic b))", "b) upright", "italics", None, "high",
    "la condition b) de", r"la condition \emph{b)} de", "")
add(78, "proof of (13.7.7), 2nd paragraph, l. 4", "la condition a) de (13.7.4) (italic a))", "a) upright", "italics", None, "high",
    "la condition\na) de", "la condition\n" + r"\emph{a)} de", "")
add(78, "proof of (13.7.7), 2nd paragraph, l. 6", "isomorphe à E_infty^{(n)}(A) = Z_infty^{(n)}(A)/B_infty^{(n)}(A); set inline in the text line",
    "displayed with \\[ \\]", "other", None, "high",
    "isomorphe à\n\\[\n" + r"\mathrm E_\infty^{(n)}(\mathbf A)=" + "\n" + r"\mathrm Z_\infty^{(n)}(\mathbf A)/\mathrm B_\infty^{(n)}(\mathbf A)~;" + "\n\\]",
    "isomorphe à\n" + r"$\mathrm E_\infty^{(n)}(\mathbf A)=" + "\n" + r"\mathrm Z_\infty^{(n)}(\mathbf A)/\mathrm B_\infty^{(n)}(\mathbf A)$~;",
    "Display in the TeX, inline in the print.")
add(78, "proof of (13.7.7), 2nd paragraph, l. 7", "il est de type fini (italic)", "upright", "italics", None, "high",
    "il est de type fini, et", r"il est de \emph{type fini}, et", "")

# ---------------------------------------------------------------- page 79
add(79, "Lemme (13.7.7.2) c), top of p. 79", "J⊗_S F^{p+1}(M) -> J⊗_S F^p(M) -> F^{p+1}(M) set inline at the start of the second line",
    "displayed with \\[ \\]", "other", None, "high",
    "composé\n\\[\n" + r"\mathfrak J\otimes_S\mathrm F^{p+1}(M)\longrightarrow" + "\n" + r"\mathfrak J\otimes_S\mathrm F^p(M)\longrightarrow\mathrm F^{p+1}(M)" + "\n\\]",
    "composé\n" + r"$\mathfrak J\otimes_S\mathrm F^{p+1}(M)\to" + "\n" + r"\mathfrak J\otimes_S\mathrm F^p(M)\to\mathrm F^{p+1}(M)$",
    "Display in the TeX, inline in the print.")
add(79, "after Lemme (13.7.7.2)", "'Pour la démonstration, voir Bourbaki, Alg. comm., chap. III, § 3, n° 1, prop. 3.' is a roman paragraph after the lemma, with italic 'Alg. comm.'",
    "inside the \\itshape lemma environment: the sentence is italic and \\emph{Alg. comm.} upright", "convention", 6, "high",
    r"\end{enumerate}" + "\n" + r"Pour la démonstration, voir Bourbaki, \emph{Alg. comm.}, chap.~III, \S~3," + "\n"
    + r"n\textsuperscript{o}~1, prop.~3." + "\n" + r"\end{lemma}",
    r"\end{enumerate}" + "\n" + r"\end{lemma}" + "\n" + r"Pour la démonstration, voir Bourbaki, \emph{Alg. comm.}, chap.~III, \S~3," + "\n"
    + r"n\textsuperscript{o}~1, prop.~3.",
    "Close the lemma before the sentence (a new indented paragraph, as printed).")
for lab, num, ctx in (("0.7.6.11-fr", "7.6.11", "), séparée"), ("0.7.6.2-fr", "7.6.2", "). On conclut"),
                      ("0.7.7.8-fr", "7.7.8", ") et"), ("0.7.7.1-fr", "7.7.1", ") que")):
    add(79, "proof of (13.7.8): (0_I, " + num + ")", "(0_I, " + num + ") with bold 0", "0\\textsubscript{I}", "convention", 2, "high",
        r"(\hyperref[" + lab + r"]{0\textsubscript{I}, " + num + "}" + ctx,
        r"(\hyperref[" + lab + r"]{\textbf{0}\textsubscript{I}, " + num + "}" + ctx, "")
add(79, "after '(A suivre.)': printed p. 80", "printed p. 80 (PDF p. 77 of PMIHES_1961__11__5_0.pdf, journal p. 424) is blank; chapter III begins on printed p. 81",
    "no \\oldpage[0\\textsubscript{III}]{80}; the blank page is made by \\clearpage \\thispagestyle{empty} \\null \\clearpage", "marker", None, "high",
    r"\textit{(A suivre.)}" + "\n" + r"\end{flushright}" + "\n\n" + r"\clearpage" + "\n" + r"\thispagestyle{empty}" + "\n" + r"\null" + "\n" + r"\clearpage",
    r"\textit{(A suivre.)}" + "\n" + r"\end{flushright}" + "\n\n" + r"\clearpage" + "\n" + MARK80 + "\n" + r"\thispagestyle{empty}" + "\n" + r"\null" + "\n" + r"\clearpage",
    "Blank printed page: marker on the empty page, as for EGA II pp. 212 and 216 (\\clearpage, \\oldpage, \\thispagestyle{empty}).")

# ---------------------------------------------------------------- checks
def text(page):
    return (RUN / f"page_{page:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")

bad = 0
for i, f in enumerate(F):
    if not f["fix"]:
        continue
    t = text(f["page"])
    n = t.count(f["fix"]["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", i, f["page"], n, repr(f["fix"]["old"])[:120])
print("uniqueness problems:", bad)

# simulate application per page in list order and reverse order
for order in ("forward", "reverse"):
    for page in sorted({f["page"] for f in F}):
        t = text(page)
        fx = [f for f in F if f["page"] == page and f["fix"]]
        if order == "reverse":
            fx = fx[::-1]
        for f in fx:
            n = t.count(f["fix"]["old"])
            if n != 1:
                print(order, "page", page, "count", n, repr(f["fix"]["old"])[:100])
                bad += 1
                continue
            t = t.replace(f["fix"]["old"], f["fix"]["new"])
        (RUN / "crops_076_079" / f"sim_{order}_{page:03d}.tex").write_text(t, encoding="utf-8")
print("simulation problems:", bad)

from collections import Counter
c = Counter()
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    c[(f["page"], k)] += 1
for p in sorted({f["page"] for f in F}):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
if bad == 0:
    json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("written", OUT, len(F))
