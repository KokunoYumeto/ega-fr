"""Build findings_065_069.json and check every fix.

Checks: (1) each "old" occurs exactly once in its page_NNN.tex (CRLF normalised to LF);
(2) applied in list order to the release segments (as apply_fixes.py does: page N = from the first
\\oldpage[IV-4]{N} to the next marker of another page), each "old" occurs exactly once when its turn comes.
In the strings below, the character "¶" stands for a line break.
"""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\IV4\native\ega4\ega4-17-fr.tex")
OUT = RUN / "findings_065_069.json"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    fix = None if old is None else {"old": old.replace("¶", "\n"), "new": new.replace("¶", "\n")}
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def label(page, where, lab, newlab, note="Hand-set label inside an italic statement: upright in the print "
                                         "(GLOBAL_ISSUES 88; same form as the p. 47 and p. 54 page fixes)."):
    add(page, where, f"label {lab} upright", f"\\item[{lab}] (italic in the italic statement)", "convention", 6,
        "high", f"\\item[{lab}]", f"\\item[\\textup{{{newlab}}}]", note)


K1 = "bold italic k"
B0 = "bold 0, no subscript"
B0I = "bold 0 with subscript I"

# ---------------------------------------------------------------- page 65
add(65, "end of the proof of (17.4.1): 'et par suite (I, 3.4.9) X×_k X est réduit à un seul point'",
    "bold I", "plain I", "convention", 2, "high", r"(I, 3.4.9)", r"(\textbf{I}, 3.4.9)")
add(65, "Remarque (17.4.1.2): 'Alors Ω^1_{X/Y} est encore un O_X-Module de type fini'",
    "italic Omega", "upright \\Omega", "font", None, "high",
    r"Alors $\Omega^1_{X/Y}$ est encore", r"Alors $\varOmega^1_{X/Y}$ est encore",
    "Sheaf of differentials: italic Omega (\\varOmega) in the print (GLOBAL_ISSUES 92).")
add(65, "Remarque (17.4.1.2): 'Δ_f un morphisme localement de présentation finie (1.4.3.1)'",
    "(1.4.3.1) in old-style figures: no bold I, no comma (crop p65_s1_1431.png)", "(I, 4.3.1)", "number", None,
    "high", r"(I, 4.3.1)", r"(1.4.3.1)",
    "Reference to EGA IV (1.4.3.1) misread as (I, 4.3.1) (cf. GLOBAL_ISSUES 78 and 98, p. 53).")
add(65, "Remarque (17.4.1.2): 'à condition de remplacer a) par'",
    "label a) italic, parenthesis included (crop p65_s2_remark_a.png)", "plain 'a)'", "italics", None, "high",
    r"remplacer a) par", r"remplacer \emph{a)} par",
    "Labels in roman text are italic in the print (GLOBAL_ISSUES 88); the remark body is judged as roman.")
add(65, "Remarque (17.4.1.2), last line: 'est un morphisme localement quasi-fini.'",
    "'localement' is set in BOLD italic, 'quasi-fini' in ordinary italic (crop p65_s2_localement_z.png, against "
    "the light italic 'localement' of the remark's first line, p65_s1_localement_ref.png); vertical stroke runs "
    "5 px against 3-4 px for 'morphisme' and 'quasi-fini' on the same line",
    "\\emph{localement quasi-fini}, ordinary weight: silent correction", "misprint_in_print", None, "high",
    r"\emph{localement quasi-fini}", r"\emph{\textbf{localement} quasi-fini}",
    "Wrong-fount word recorded as a misprint (GLOBAL_ISSUES 29; cf. 'est' p. 42, 'rentiel' p. 43); EGA uses no "
    "bold-italic emphasis in running text. With the "
    "remark body set roman (document-wide decision), \\emph gives italic and \\textbf inside it bold italic.",
    corrected=r"\emph{localement quasi-fini}")
label(65, "Corollaire (17.4.2), label a)", "a)", "a)")
label(65, "Corollaire (17.4.2), label b)", "b)", "b)")
label(65, "Corollaire (17.4.2), label b')", "b')", "b$'$)")
label(65, "Corollaire (17.4.2), label c)", "c)", "c)")
add(65, "Corollaire (17.4.2) c): 'On a Ω^1_{X/Y}=0.'", "italic Omega", "upright \\Omega", "font", None, "high",
    r"$\Omega^1_{X/Y}=0$", r"$\varOmega^1_{X/Y}=0$",
    "Sheaf of differentials: italic Omega (\\varOmega) in the print (GLOBAL_ISSUES 92).")
label(65, "Corollaire (17.4.2), label d)", "d)", "d)")
add(65, "Corollaire (17.4.2) d): 'le k(y)-préschéma f^{-1}(y) est non ramifié'", K1, "plain k", "convention", 1,
    "high", r"le $k(y)$-préschéma $f^{-1}(y)$ est non", r"le $\boldsymbol{k}(y)$-préschéma $f^{-1}(y)$ est non")
add(65, "Corollaire (17.4.2) d): 'est non ramifié sur k(y).'", K1, "plain k", "convention", 1, "high",
    r"sur $k(y)$.", r"sur $\boldsymbol{k}(y)$.")
label(65, "Corollaire (17.4.2), label d')", "d')", "d$'$)")
add(65, "Corollaire (17.4.2) d'): 'le k(y)-préschéma f^{-1}(y) est isomorphe'", K1, "plain k", "convention", 1,
    "high", r"le $k(y)$-préschéma $f^{-1}(y)$ est isomorphe",
    r"le $\boldsymbol{k}(y)$-préschéma $f^{-1}(y)$ est isomorphe")
add(65, "Corollaire (17.4.2) d'): 'extension finie et séparable de k(y).'", K1, "plain k", "convention", 1, "high",
    r"séparable de $k(y)$.", r"séparable de $\boldsymbol{k}(y)$.")
label(65, "Corollaire (17.4.2), label e)", "e)", "e)")
add(65, "Corollaire (17.4.3): 'alors f est localement quasi-fini (Err_III, 20).'",
    "bold upright 'Err' with a light roman subscript III; parentheses and 20 upright (crop p65_s3_err.png)",
    "(Err$_{\\mathrm{III}}$, 20): normal-weight Err, the whole reference italic in the italic statement",
    "font", None, "high",
    r"(Err$_{\mathrm{III}}$, 20)", r"\textup{(\textbf{Err}$_{\mathrm{III}}$, 20)}",
    "Same forms as the earlier page fixes (\\textup{$\\mathbf{Err}_{\\mathrm{III}}$, 10)} in ega4-16 p. 14; "
    "(\\textbf{Err}$_{\\rm III}$, 30) in IV-2 p. 160); the \\textup covers the upright reference (convention 6).")
add(65, "Proposition (17.4.4): 'Soient Y un préschéma localement noethérien'",
    "'localement noethérien' roman inside the italic statement (crop p65_s3_noeth.png)",
    "italic (no change of face)", "convention", 6, "high",
    r"préschéma localement noethérien", r"préschéma \textup{localement noethérien}",
    "Not a wrong fount: the authors' emphasis of the hypothesis added to (17.4.1), set roman in the italic "
    "statement; the same in (17.5.3) p. 68, and italic in the roman Remarque (17.5.4) p. 69.")
add(65, "Proposition (17.4.4): 'Alors les conditions équivalentes a) à e)'", "label a) upright (crop p65_s3_ae.png)",
    "plain a) (italic in the italic statement)", "convention", 6, "high",
    r"équivalentes a)", r"équivalentes \textup{a)}", "GLOBAL_ISSUES 88 (labels upright inside italic statements).")
add(65, "Proposition (17.4.4): 'à e) du théorème'", "label e) upright", "plain e) (italic)", "convention", 6, "high",
    r"e) du théorème", r"\textup{e)} du théorème", "GLOBAL_ISSUES 88.")
add(65, "Proposition (17.4.4): 'du théorème (17.4.1) sont aussi équivalentes'", "upright (17.4.1)",
    "italic in the italic statement", "convention", 6, "high",
    r"(17.4.1) sont aussi", r"\textup{(17.4.1)} sont aussi")
label(65, "Proposition (17.4.4), label f)", "f)", "f)")
add(65, "Proposition (17.4.4) f): '(ce qui entraîne que B^ est une A^-algèbre finie)'",
    "the parenthesis is roman, with 'finie' italic (crop p65_s3_f.png)",
    "all italic in the italic statement", "convention", 6, "high",
    r"(ce qui entraîne que $\widehat{B}$ est une $\widehat{A}$-algèbre finie)",
    r"\textup{(ce qui entraîne que $\widehat{B}$ est une $\widehat{A}$-algèbre \emph{finie})}")
label(65, "Proposition (17.4.4), label f')", "f')", "f$'$)")
add(65, "Proposition (17.4.4): 'Si de plus k(x)=k(y), ou si k est séparablement clos'",
    K1 + " (both; the k of 'si k est séparablement clos' is light)", "plain k", "convention", 1, "high",
    r"Si de plus $k(x)=k(y)$, ou si", r"Si de plus $\boldsymbol{k}(x)=\boldsymbol{k}(y)$, ou si",
    "Two occurrences in one formula.")
label(65, "Proposition (17.4.4), label f'')", "f'')", "f$''$)")
add(65, "proof of (17.4.4): 'par le même raisonnement que dans (0, 19.3.6)'", B0, "plain 0", "convention", 2,
    "high", r"(0, 19.3.6)", r"(\textbf{0}, 19.3.6)")
add(65, "page break 65/66 inside the sentence 'entraîne que Ω^1_{B/A} | est un B-module'",
    "the sentence runs on to p. 66 ('est un B-module de type fini')",
    "blank line before \\oldpage[IV-4]{66}: a paragraph break inside the sentence", "marker", None, "high",
    "entraîne que $\\Omega^1_{B/A}$¶¶", "entraîne que $\\Omega^1_{B/A}$¶",
    "GLOBAL_ISSUES 20. The blank line is the end of this page's segment, just before the p. 66 marker.")

# ---------------------------------------------------------------- page 66
add(66, "proof of (17.4.4): 'l'idéal maximal de B) (0_I, 7.3.5); il revient'", B0I, "plain 0", "convention", 2,
    "high", r"de $B$) ($0_{\mathrm I}$, 7.3.5)", r"de $B$) ($\mathbf{0}_{\mathrm I}$, 7.3.5)")
add(66, "proof of (17.4.4): 'donc (0, 20.7.4), il revient au même'", B0, "plain 0", "convention", 2, "high",
    r"(0, 20.7.4)", r"(\textbf{0}, 20.7.4)")
add(66, "proof of (17.4.4): 'Ceci prouve l'équivalence des conditions e) et f').'",
    "labels e) and f') italic (crop p66_s1_ef.png)", "plain labels", "italics", None, "high",
    r"conditions e) et f').", r"conditions \emph{e)} et \emph{f')}.", "GLOBAL_ISSUES 88.")
add(66, "proof of (17.4.4): 'on a k=A/m=A^/mA^, donc B^⊗_A^ k=B^/mB^=B^⊗_B(B/mB), et par suite'",
    "both formulas in the running text, joined by the roman word 'donc' (page_066_s1.png)",
    "the two formulas are displayed, joined by \\qquad; 'donc' is missing", "missing", None, "high",
    "on a¶\\[¶k=A/\\mathfrak m=\\widehat A/\\mathfrak m\\widehat A,¶\\qquad¶"
    "\\widehat B\\otimes_{\\widehat A}k=\\widehat B/\\mathfrak m\\widehat B¶=\\widehat B\\otimes_B(B/\\mathfrak m B),¶\\]",
    "on a $k=A/\\mathfrak m=\\widehat A/\\mathfrak m\\widehat A$, donc "
    "$\\widehat B\\otimes_{\\widehat A}k=\\widehat B/\\mathfrak m\\widehat B=\\widehat B\\otimes_B(B/\\mathfrak m B)$,",
    "Formula displayed where the print sets it inline, with the connecting word lost (GLOBAL_ISSUES 21, 51). "
    "The line 'et par suite (...)' after \\] is left untouched (the next fix edits it).")
add(66, "proof of (17.4.4): 'et par suite (0_I, 7.3.5) B^/mB^ est le complété'", B0I, "plain 0", "convention", 2,
    "high", r"et par suite ($0_{\mathrm I}$, 7.3.5)", r"et par suite ($\mathbf{0}_{\mathrm I}$, 7.3.5)")
add(66, "proof of (17.4.4): 'ceci prouve l'équivalence de d'') et de f).'",
    "labels d'') and f) italic (crop p66_s1_dfk.png)", "plain labels", "italics", None, "high",
    r"l'équivalence de d'') et de f).", r"l'équivalence de \emph{d'')} et de \emph{f)}.", "GLOBAL_ISSUES 88.")
add(66, "proof of (17.4.4): 'Enfin, lorsque k(x)=k(y) ou lorsque k est séparablement clos'",
    K1 + " (both; the k of 'lorsque k est séparablement clos' is light)", "plain k", "convention", 1, "high",
    r"lorsque $k(x)=k(y)$ ou", r"lorsque $\boldsymbol{k}(x)=\boldsymbol{k}(y)$ ou", "Two occurrences in one formula.")
add(66, "proof of (17.4.4): 'la condition f) entraîne que l'homomorphisme'", "label f) italic", "plain f)",
    "italics", None, "high", r"la condition f) entraîne", r"la condition \emph{f)} entraîne", "GLOBAL_ISSUES 88.")
add(66, "proof of (17.4.4): 'la condition f) implique d'autre part'", "label f) italic", "plain f)",
    "italics", None, "high", r"la condition f) implique", r"la condition \emph{f)} implique", "GLOBAL_ISSUES 88.")
add(66, "proof of (17.4.4): 'quasi-finie (0_I, 7.4.4)'", B0I, "plain 0", "convention", 2, "high",
    r"($0_{\mathrm I}$, 7.4.4)", r"($\mathbf{0}_{\mathrm I}$, 7.4.4)")
add(66, "proof of (17.4.4): 'idéal de définition de B^ (0_I, 7.4.1)'", B0I, "plain 0", "convention", 2, "high",
    r"($0_{\mathrm I}$, 7.4.1)", r"($\mathbf{0}_{\mathrm I}$, 7.4.1)")
add(66, "proof of (17.4.4): 'Donc f) entraîne alors f''), et la réciproque'", "labels f) and f'') italic",
    "plain labels", "italics", None, "high",
    r"Donc f) entraîne alors f''),", r"Donc \emph{f)} entraîne alors \emph{f'')},", "GLOBAL_ISSUES 88.")
add(66, "(17.4.5): 'l'image réciproque par (f, g)_S de la diagonale Δ_{Y|S}'",
    "'diago-nale' italic (crop p66_s2_env1745.png)", "plain 'diagonale'", "italics", None, "high",
    r"de la diagonale $\Delta_{Y|S}$", r"de la \emph{diagonale} $\Delta_{Y|S}$")
add(66, "(17.4.5): 'qui est fermé lorsque Y est un S-schéma (I, 5.4.1)'",
    "'schéma' italic after the roman S- (crop p66_s2_env1745.png)", "plain 'schéma'", "italics", None, "high",
    r"lorsque $Y$ est un $S$-schéma", r"lorsque $Y$ est un $S$-\emph{schéma}")
add(66, "(17.4.5): 'S-schéma (I, 5.4.1).'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 5.4.1).", r"(\textbf{I}, 5.4.1).")
add(66, "Proposition (17.4.6): 'Soient h : Y→S un morphisme non ramifié, et soient'",
    "'non ramifié,' masculine, no final e (crop p66_s2_prop1746.png)", "'non ramifiée'", "word", None, "high",
    r"non ramifiée, et soient", r"non ramifié, et soient", "The TeX adds an e the print does not have.")
add(66, "Proposition (17.4.6): 'si de plus Y est un S-schéma (I, 5.4.1), C est'",
    "bold I; the reference upright inside the italic statement", "plain I, italic reference", "convention", 2,
    "high", r"(I, 5.4.1), $C$", r"\textup{(\textbf{I}, 5.4.1)}, $C$",
    "Same form as the earlier page fixes (\\textup{(\\textbf{II}, 1.7.4 et 2.1.2)}, p. 20).")
add(66, "proof of (17.4.6): 'induit sur un ouvert de X (I, 4.4.1)'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 4.4.1)", r"(\textbf{I}, 4.4.1)")
add(66, "Corollaire (17.4.7): 'Sous les hypothèses de (17.4.6), soit x'", "upright (17.4.6)",
    "italic in the italic statement", "convention", 6, "high",
    r"hypothèses de (17.4.6), soit", r"hypothèses de \textup{(17.4.6)}, soit")
add(66, "Corollaire (17.4.7): 'Spec(k(x)) → X →f Y'", K1, "plain k", "convention", 1, "high",
    r"$\Spec(k(x))\to X\xrightarrow{f}Y$", r"$\Spec(\boldsymbol{k}(x))\to X\xrightarrow{f}Y$")
add(66, "Corollaire (17.4.7): 'Spec(k(x)) → X →g Y'", K1, "plain k", "convention", 1, "high",
    r"$\Spec(k(x))\to X\xrightarrow{g}Y$", r"$\Spec(\boldsymbol{k}(x))\to X\xrightarrow{g}Y$")
add(66, "proof of (17.4.7): 'Cela résulte de (17.4.6) et de (I, 5.3.17).'", "bold I", "plain I", "convention", 2,
    "high", r"(I, 5.3.17)", r"(\textbf{I}, 5.3.17)")
add(66, "Corollaire (17.4.8): 'Sous les hypothèses de (17.4.6), supposons'", "upright (17.4.6)",
    "italic in the italic statement", "convention", 6, "high",
    r"hypothèses de (17.4.6), supposons", r"hypothèses de \textup{(17.4.6)}, supposons")
add(66, "Corollaire (17.4.8): 'soit X_s le k(s)-préschéma φ^{-1}(s)'", K1, "plain k", "convention", 1, "high",
    r"le $k(s)$-préschéma", r"le $\boldsymbol{k}(s)$-préschéma")
add(66, "proof of (17.4.8): 'donc φ(X—C) est à la'", "long dash (set difference)", "minus sign", "convention", 7,
    "high", r"$\varphi(X-C)$", r"$\varphi(X\setmin C)$")
add(66, "page break 66/67 inside 'φ(X—C) est à la | fois ouvert et fermé dans S'",
    "the sentence runs on to p. 67 ('fois ouvert et fermé')",
    "blank line before \\oldpage[IV-4]{67}: a paragraph break inside the sentence", "marker", None, "high",
    "est à la¶¶", "est à la¶", "GLOBAL_ISSUES 20. Independent of the convention-7 edit on the same line.")

# ---------------------------------------------------------------- page 67
add(67, "Proposition (17.4.9): 'et l'application g ⇝ g(Y) est une bijection'",
    "wavy arrow (crop p67_s1_leadsto2.png)", "\\mapsto", "symbol", None, "high",
    r"$g\mapsto g(Y)$", r"$g\leadsto g(Y)$")
add(67, "Proposition (17.4.9): '(nécessairement ouvertes dans X)'",
    "the parenthesis is roman, with 'ouvertes' italic (crop p67_s1_leadsto.png)", "all italic", "convention", 6,
    "high", r"(nécessairement ouvertes dans $X$)", r"\textup{(nécessairement \emph{ouvertes} dans $X$)}")
add(67, "proof of (17.4.9): 'Il résulte en effet de (17.4.1, b''))'", "label b'') italic (crop p67_s2_b2.png)",
    "plain b'')", "italics", None, "high", r"(17.4.1, b''))", r"(17.4.1, \emph{b'')})")
add(67, "proof of (17.4.9): 'une immersion fermée (I, 5.4.7)'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 5.4.7)", r"(\textbf{I}, 5.4.7)")
add(67, "heading 17.5: 'Caractérisations des morphismes lisses.'", "full stop after the title (crop p67_s2_title.png)",
    "no full stop", "punctuation", None, "high",
    r"\subsection{Caractérisations des morphismes lisses}", r"\subsection{Caractérisations des morphismes lisses.}",
    "GLOBAL_ISSUES 43/58; same form as the earlier subsection-title page fixes (17.2 on p. 59).")
label(67, "Théorème (17.5.1), label a)", "a)", "a)")
label(67, "Théorème (17.5.1), label b)", "b)", "b)")
add(67, "Théorème (17.5.1) b): 'et le k(y)-préschéma f^{-1}(y)'", K1, "plain k", "convention", 1, "high",
    r"et le $k(y)$-préschéma", r"et le $\boldsymbol{k}(y)$-préschéma")
add(67, "Théorème (17.5.1) b): 'est lisse sur k(y) au point x.'", K1, "plain k", "convention", 1, "high",
    r"lisse sur $k(y)$ au point $x$.", r"lisse sur $\boldsymbol{k}(y)$ au point $x$.")
label(67, "Théorème (17.5.1), label b')", "b')", "b$'$)")
add(67, "Théorème (17.5.1) b'): 'f est régulier au point x (6.8.1).'", "upright (6.8.1)",
    "italic in the italic statement", "convention", 6, "high", r"(6.8.1).", r"\textup{(6.8.1)}.")
label(67, "Théorème (17.5.1), label c)", "c)", "c)")
add(67, "proof of (17.5.1): 'et J un idéal de B de type fini.'", "'de type fini' italic (crop p67_s3_J.png)",
    "plain", "italics", None, "high", r"de $B$ de type fini.", r"de $B$ \emph{de type fini}.")
add(67, "proof of (17.5.1): 'L'équivalence de a) et c) résulte alors'", "labels a), c) italic", "plain labels",
    "italics", None, "high", r"L'équivalence de a) et c) résulte",
    r"L'équivalence de \emph{a)} et \emph{c)} résulte", "GLOBAL_ISSUES 88.")
add(67, "proof of (17.5.1): 'de l'équivalence de a) et c) dans (0, 22.6.4)'", "labels a), c) italic",
    "plain labels", "italics", None, "high", r"l'équivalence de a) et c) dans",
    r"l'équivalence de \emph{a)} et \emph{c)} dans", "GLOBAL_ISSUES 88.")
add(67, "proof of (17.5.1): 'dans (0, 22.6.4). D'autre part'", B0, "plain 0", "convention", 2, "high",
    r"(0, 22.6.4). D'autre", r"(\textbf{0}, 22.6.4). D'autre")
add(67, "proof of (17.5.1): 'f^{-1}(y) → Spec(k(y))'", K1, "plain k", "convention", 1, "high",
    r"\to\Spec(k(y))$", r"\to\Spec(\boldsymbol{k}(y))$")
add(67, "proof of (17.5.1): 'l'équivalence de b) et b') résulte'", "labels b), b') italic", "plain labels",
    "italics", None, "high", r"l'équivalence de b) et b') résulte",
    r"l'équivalence de \emph{b)} et \emph{b')} résulte", "GLOBAL_ISSUES 88.")
add(67, "proof of (17.5.1): 'de l'équivalence de a) et b) dans (6.8.6)'", "labels a), b) italic", "plain labels",
    "italics", None, "high", r"l'équivalence de a) et b) dans", r"l'équivalence de \emph{a)} et \emph{b)} dans",
    "GLOBAL_ISSUES 88.")
add(67, "proof of (17.5.1): 'Reste donc à démontrer l'équivalence de a) et b).'", "labels a), b) italic",
    "plain labels", "italics", None, "high", r"démontrer l'équivalence de a) et b).",
    r"démontrer l'équivalence de \emph{a)} et \emph{b)}.", "GLOBAL_ISSUES 88.")
add(67, "proof of (17.5.1): 'Montrons d'abord que a) entraîne b);'", "labels a), b) italic", "plain labels",
    "italics", None, "high", r"que a) entraîne b);", r"que \emph{a)} entraîne \emph{b)};", "GLOBAL_ISSUES 88.")
add(67, "proof of (17.5.1): 'notons p l'idéal premier j_x dans C'",
    "Fraktur j: dot, stem descending below the baseline nearly as far as the p of 'premier' (crop p67_s3_jx_z.png)",
    "\\mathfrak i (Fraktur i)", "symbol", None, "high", r"$\mathfrak i_x$", r"$\mathfrak j_x$",
    "Wrong letter: EGA's j_x (the prime ideal of x), written \\mathfrak{j}_x in the EGA I files.")
add(67, "proof of (17.5.1): 'r l'idéal premier j_y dans A'", "Fraktur j (crop p67_s3_jy_z.png)",
    "\\mathfrak i (Fraktur i)", "symbol", None, "high", r"$\mathfrak i_y$", r"$\mathfrak j_y$",
    "As j_x above.")
add(67, "proof of (17.5.1): 'L'hypothèse a) entraîne d'abord'", "label a) italic", "plain a)", "italics", None,
    "high", r"L'hypothèse a) entraîne", r"L'hypothèse \emph{a)} entraîne", "GLOBAL_ISSUES 88.")
add(67, "proof of (17.5.1): 'est lisse sur k(y) au point x par (17.3.3)'", K1, "plain k", "convention", 1,
    "high", r"lisse sur $k(y)$ au point $x$ par", r"lisse sur $\boldsymbol{k}(y)$ au point $x$ par")
add(67, "proof of (17.5.1): 'le critère jacobien (0, 22.6.4), joint à'", B0, "plain 0", "convention", 2, "high",
    r"(0, 22.6.4), joint", r"(\textbf{0}, 22.6.4), joint")
add(67, "proof of (17.5.1): 'joint à (0, 19.1.12), entraîne'", B0, "plain 0", "convention", 2, "high",
    r"(0, 19.1.12),", r"(\textbf{0}, 19.1.12),")

# ---------------------------------------------------------------- page 68
add(68, "proof of (17.5.1): 'le spectre de l'anneau régulier k(y)[T_1, ..., T_n]'", "'régulier' italic",
    "plain", "italics", None, "high", r"de l'anneau régulier", r"de l'anneau \emph{régulier}")
add(68, "proof of (17.5.1): 'l'anneau régulier k(y)[T_1, ..., T_n]'", K1, "plain k", "convention", 1, "high",
    r"$k(y)[T_1", r"$\boldsymbol{k}(y)[T_1")
add(68, "proof of (17.5.1): 'k(y)[T_1, ..., T_n] (0, 17.3.7), donc'", B0, "plain 0", "convention", 2, "high",
    r"(0, 17.3.7)", r"(\textbf{0}, 17.3.7)")
add(68, "proof of (17.5.1): 'On conclut donc de (0, 17.1.7) que (v_i)'", B0, "plain 0", "convention", 2, "high",
    r"(0, 17.1.7)", r"(\textbf{0}, 17.1.7)")
add(68, "proof of (17.5.1): 'Prouvons enfin que b) implique a).'", "labels b), a) italic", "plain labels",
    "italics", None, "high", r"que b) implique a).", r"que \emph{b)} implique \emph{a)}.", "GLOBAL_ISSUES 88.")
add(68, "proof of (17.5.1): 'est injectif (0_I, 6.1.2)'", B0I, "plain 0", "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.1.2)", r"($\mathbf{0}_{\mathrm I}$, 6.1.2)")
add(68, "proof of (17.5.1): 'le critère jacobien (0, 22.6.4); joint à'", B0, "plain 0", "convention", 2, "high",
    r"(0, 22.6.4); joint", r"(\textbf{0}, 22.6.4); joint")
add(68, "proof of (17.5.1): 'joint à (0, 19.1.12), ce dernier prouve'", B0, "plain 0", "convention", 2, "high",
    r"(0, 19.1.12), ce dernier", r"(\textbf{0}, 19.1.12), ce dernier")
add(68, "proof of (17.5.1): 'en vertu de l'hypothèse b), l'existence'", "label b) italic (crop p68_s2_envertu_z.png)",
    "plain b)", "italics", None, "high", r"b), l'existence", r"\emph{b)}, l'existence",
    "Listed before the misprint fix of the same line; the two edits do not overlap.")
add(68, "proof of (17.5.1): 'ce dernier prouve, en vertu de l'hypothèse b), l'existence'",
    "'en vertu de l'hypothèse' is set in BOLD roman; 'prouve,' before it and 'l'existence de' after it are of "
    "normal weight (crops p68_s2_envertu.png, p68_s2_envertu_z.png; ink per column 11.5 against 9.4 and 10.0, "
    "vertical stroke runs 4 px against 3 px)",
    "normal weight: silent correction", "misprint_in_print", None, "high",
    r"prouve, en vertu de l'hypothèse", r"prouve, \textbf{en vertu de l'hypothèse}",
    "Wrong-fount words recorded as a misprint (GLOBAL_ISSUES 29; cf. p. 42 'est', p. 43 'rentiel'). Apply after "
    "the italics fix of b) on the same line (no overlap).", corrected=r"prouve, en vertu de l'hypothèse")
add(68, "proof of (17.5.1): 'r polynômes v_i∈k(y)[T_1, ..., T_n]'", K1, "plain k", "convention", 1, "high",
    r"$v_i\in k(y)[T_1", r"$v_i\in\boldsymbol{k}(y)[T_1")
add(68, "end of the proof of (17.5.1): 'Le critère jacobien (0, 22.6.4) joint à'", B0, "plain 0", "convention", 2,
    "high", r"(0, 22.6.4) joint", r"(\textbf{0}, 22.6.4) joint")
add(68, "end of the proof of (17.5.1): 'joint à (0, 19.1.12), prouve alors'", B0, "plain 0", "convention", 2,
    "high", r"(0, 19.1.12), prouve", r"(\textbf{0}, 19.1.12), prouve")
add(68, "Corollaire (17.5.2): 'Pour que f soit lisse (au sens de (17.3.1)), il faut'",
    "outer parentheses and (17.3.1) upright, 'au sens de' italic (crop p68_s3_cor1752.png)",
    "all italic in the italic statement", "convention", 6, "high",
    r"(au sens de (17.3.1))", r"\textup{(}au sens de \textup{(17.3.1))}")
add(68, "Corollaire (17.5.2): 'que f soit régulier (6.8.1), autrement dit'", "upright (6.8.1)",
    "italic in the italic statement", "convention", 6, "high",
    r"régulier (6.8.1), autrement", r"régulier \textup{(6.8.1)}, autrement")
add(68, "Corollaire (17.5.2): 'f^{-1}(y) soit un k(y)-préschéma géométriquement régulier'", K1, "plain k",
    "convention", 1, "high", r"soit un $k(y)$-préschéma", r"soit un $\boldsymbol{k}(y)$-préschéma")
add(68, "Corollaire (17.5.2): 'géométriquement régulier (6.7.6).'", "upright (6.7.6)",
    "italic in the italic statement", "convention", 6, "high", r"(6.7.6).", r"\textup{(6.7.6)}.")
add(68, "after (17.5.2): 'On a ainsi établi l'équivalence des deux définitions'", "'l'équivalence' italic",
    "plain", "italics", None, "high", r"établi l'équivalence", r"établi \emph{l'équivalence}")
add(68, "Proposition (17.5.3): 'Soient Y un préschéma localement noethérien'",
    "'localement noethérien' roman inside the italic statement (page_068_s4.png)", "italic (no change of face)",
    "convention", 6, "high", r"préschéma localement noethérien", r"préschéma \textup{localement noethérien}",
    "The authors' emphasis of the hypothesis added to (17.5.1), as in (17.4.4) p. 65.")
add(68, "Proposition (17.5.3): 'Alors les conditions équivalentes a) à c) de (17.5.1)'",
    "label a) upright (crop p68_s4_1753.png)", "plain a) (italic)", "convention", 6, "high",
    r"équivalentes a)", r"équivalentes \textup{a)}", "GLOBAL_ISSUES 88.")
add(68, "Proposition (17.5.3): 'à c) de (17.5.1)'", "label c) upright", "plain c) (italic)", "convention", 6,
    "high", r"c) de", r"\textup{c)} de", "GLOBAL_ISSUES 88.")
add(68, "Proposition (17.5.3): 'de (17.5.1) sont aussi équivalentes'", "upright (17.5.1)",
    "italic in the italic statement", "convention", 6, "high",
    r"(17.5.1) sont aussi", r"\textup{(17.5.1)} sont aussi")
P69 = (" Printed at the top of p. 69; the text stands in the p. 68 segment until the marker fix below moves "
       "the page boundary: apply this fix before it.")
label(68, "Proposition (17.5.3), label d) (printed p. 69)", "d)", "d)",
      "GLOBAL_ISSUES 88." + P69)
label(68, "Proposition (17.5.3), label d') (printed p. 69)", "d')", "d$'$)", "GLOBAL_ISSUES 88." + P69)
add(68, "Proposition (17.5.3): 'Si de plus k(x)=k(y), ces conditions équivalent aussi à' (printed p. 69)",
    K1 + " (both)", "plain k", "convention", 1, "high",
    r"Si de plus $k(x)=k(y)$, ces", r"Si de plus $\boldsymbol{k}(x)=\boldsymbol{k}(y)$, ces",
    "Two occurrences in one formula." + P69)
label(68, "Proposition (17.5.3), label d'') (printed p. 69)", "d'')", "d$''$)", "GLOBAL_ISSUES 88." + P69)
add(68, "page break 68/69: printed p. 68 ends with '... équivalentes à chacune des suivantes :'",
    "p. 69 begins with item d) of (17.5.3) ('d) B est une A-algèbre formellement lisse ...'), page_069_s1.png",
    "\\oldpage[IV-4]{69} stands after \\end{proposition}, before 'L'équivalence de la condition c)': items d), d') "
    "and d''), and 'Si de plus k(x)=k(y), ces conditions équivalent aussi à', fall before the marker",
    "marker", None, "high",
    "chacune des suivantes:¶\\begin{enumerate}", "chacune des suivantes:¶\\oldpage[IV-4]{69}¶\\begin{enumerate}",
    "Part 1 of 2: inserts the marker where printed p. 69 begins (as \\oldpage[IV-4]{60} before \\begin{enumerate}); "
    "the p. 69 finding deletes the old marker. Apply both or neither, this one first, after the four (17.5.3) "
    "fixes above.")

# ---------------------------------------------------------------- page 69
add(69, "top of page_069.tex: old \\oldpage[IV-4]{69} before 'L'équivalence de la condition c)'",
    "printed p. 69 begins with item d) of (17.5.3)",
    "the marker stands after \\end{proposition}", "marker", None, "high",
    "\\oldpage[IV-4]{69}¶L'équivalence", "L'équivalence",
    "Part 2 of 2: apply only after the p. 68 marker finding has inserted the new \\oldpage[IV-4]{69} before "
    "\\begin{enumerate} of (17.5.3). The blank line after \\end{proposition} stays: 'L'équivalence' opens an "
    "indented paragraph in the print.")
add(69, "proof of (17.5.3): 'L'équivalence de la condition c) de (17.5.1) et de d) résulte'",
    "labels c), d) italic", "plain labels", "italics", None, "high",
    r"la condition c) de (17.5.1) et de d) résulte", r"la condition \emph{c)} de (17.5.1) et de \emph{d)} résulte",
    "GLOBAL_ISSUES 88.")
add(69, "proof of (17.5.3): 'de l'équivalence de a) et d) dans le critère jacobien'", "labels a), d) italic",
    "plain labels", "italics", None, "high", r"l'équivalence de a) et d) dans",
    r"l'équivalence de \emph{a)} et \emph{d)} dans", "GLOBAL_ISSUES 88.")
add(69, "proof of (17.5.3): 'critère jacobien (0, 22.6.4), et'", B0, "plain 0", "convention", 2, "high",
    r"(0, 22.6.4), et", r"(\textbf{0}, 22.6.4), et")
add(69, "proof of (17.5.3): 'l'équivalence de d) et d') résulte de (0, 19.3.6)'", "labels d), d') italic",
    "plain labels", "italics", None, "high", r"l'équivalence de d) et d') résulte",
    r"l'équivalence de \emph{d)} et \emph{d')} résulte", "GLOBAL_ISSUES 88.")
add(69, "proof of (17.5.3): 'résulte de (0, 19.3.6). D'autre part'", B0, "plain 0", "convention", 2, "high",
    r"(0, 19.3.6)", r"(\textbf{0}, 19.3.6)")
add(69, "proof of (17.5.3): 'D'autre part, d'') implique d') sans hypothèse'", "labels d''), d') italic",
    "plain labels", "italics", None, "high", r"part, d'') implique d') sans",
    r"part, \emph{d'')} implique \emph{d')} sans", "GLOBAL_ISSUES 88.")
add(69, "proof of (17.5.3): 'sur les corps résiduels (0, 19.3.4)'", B0, "plain 0", "convention", 2, "high",
    r"(0, 19.3.4)", r"(\textbf{0}, 19.3.4)")
add(69, "proof of (17.5.3): 'l'hypothèse d') entraîne que B^/mB^'", "label d') italic", "plain d')", "italics",
    None, "high", r"l'hypothèse d') entraîne", r"l'hypothèse \emph{d')} entraîne", "GLOBAL_ISSUES 88.")
add(69, "proof of (17.5.3): 'est une k(y)-algèbre locale noethérienne complète'", K1, "plain k", "convention", 1,
    "high", r"est une $k(y)$-algèbre", r"est une $\boldsymbol{k}(y)$-algèbre")
add(69, "proof of (17.5.3): 'pour sa topologie adique (0, 19.3.5)'", B0, "plain 0", "convention", 2, "high",
    r"(0, 19.3.5)", r"(\textbf{0}, 19.3.5)")
add(69, "proof of (17.5.3): 'l'hypothèse k(y)=k(x) entraîne donc'", K1 + " (both)", "plain k", "convention", 1,
    "high", r"l'hypothèse $k(y)=k(x)$", r"l'hypothèse $\boldsymbol{k}(y)=\boldsymbol{k}(x)$",
    "Two occurrences in one formula.")
add(69, "proof of (17.5.3): 'est k(y)-isomorphe'", K1, "plain k", "convention", 1, "high",
    r"est $k(y)$-isomorphe", r"est $\boldsymbol{k}(y)$-isomorphe")
add(69, "proof of (17.5.3): 'algèbre de séries formelles k(y)[[T_1, ..., T_n]]'", K1, "plain k", "convention", 1,
    "high", r"formelles $k(y)[[T_1", r"formelles $\boldsymbol{k}(y)[[T_1")
add(69, "proof of (17.5.3): 'k(y)[[T_1, ..., T_n]] (0, 19.6.4). Comme'", B0, "plain 0", "convention", 2, "high",
    r"(0, 19.6.4)", r"(\textbf{0}, 19.6.4)")
add(69, "proof of (17.5.3): 'on conclut de (0, 19.7.1.5) que cette algèbre'", B0, "plain 0", "convention", 2,
    "high", r"(0, 19.7.1.5)", r"(\textbf{0}, 19.7.1.5)")
add(69, "proof of (17.5.3): 'Donc d') entraîne d'') sous l'hypothèse additionnelle'", "labels d'), d'') italic",
    "plain labels", "italics", None, "high", r"Donc d') entraîne d'') sous",
    r"Donc \emph{d')} entraîne \emph{d'')} sous", "GLOBAL_ISSUES 88.")
add(69, "proof of (17.5.3): 'sous l'hypothèse additionnelle k(x)=k(y).'", K1 + " (both)", "plain k",
    "convention", 1, "high", r"additionnelle $k(x)=k(y)$", r"additionnelle $\boldsymbol{k}(x)=\boldsymbol{k}(y)$",
    "Two occurrences in one formula.")
add(69, "Remarque (17.5.4): 'Supposons que Y soit un préschéma localement noethérien, et'",
    "'localement noethérien' italic (crop p69_s2_rem1754.png)", "plain", "italics", None, "high",
    r"préschéma localement noethérien, et", r"préschéma \emph{localement noethérien}, et",
    "The remark body is judged as roman.")
add(69, "Remarque (17.5.4): 'Le critère (17.5.3, d)), joint à'", "label d) italic", "plain d)", "italics", None,
    "high", r"(17.5.3, d))", r"(17.5.3, \emph{d)})")
add(69, "Remarque (17.5.4): 'joint à (0, 22.1.4) montre que'", B0, "plain 0", "convention", 2, "high",
    r"(0, 22.1.4)", r"(\textbf{0}, 22.1.4)")
add(69, "Remarque (17.5.4): 'en se restreignant au cas où'", "'restreignant' italic", "plain", "italics", None,
    "high", r"en se restreignant", r"en se \emph{restreignant}")
add(69, "Remarque (17.5.4): 'est le spectre d'un anneau local artinien.'",
    "'spectre d'un anneau local artinien' italic", "plain", "italics", None, "high",
    r"le spectre d'un anneau local artinien.", r"le \emph{spectre d'un anneau local artinien}.")
add(69, "Proposition (17.5.5): 'Supposons que Y soit réduit au point y.'",
    "'réduit' roman inside the italic statement (crop p69_s2_reduit.png)", "italic (no change of face)",
    "convention", 6, "high", r"soit réduit au point", r"soit \textup{réduit} au point",
    "The authors' emphasis of the added hypothesis ('localement noethérien' is italic in this statement).")
add(69, "Proposition (17.5.5): 'f^{-1}(y) soit un k(y)-préschéma géométriquement régulier au point x.'", K1,
    "plain k", "convention", 1, "high",
    "soit un $k(y)$-préschéma géométriquement régulier au point $x$.¶\\end{proposition}",
    "soit un $\\boldsymbol{k}(y)$-préschéma géométriquement régulier au point $x$.¶\\end{proposition}")
add(69, "proof of (17.5.5): 'tout revient à voir que, si f^{-1}(y) est un k(y)-préschéma'", K1, "plain k",
    "convention", 1, "high", r"si $f^{-1}(y)$ est un $k(y)$-préschéma",
    r"si $f^{-1}(y)$ est un $\boldsymbol{k}(y)$-préschéma")
add(69, "proof of (17.5.5): 'et que f^{-1}(y) est un k(y)-préschéma géométriquement régulier au point x entraîne'",
    K1, "plain k", "convention", 1, "high", r"et que $f^{-1}(y)$ est un $k(y)$-préschéma",
    r"et que $f^{-1}(y)$ est un $\boldsymbol{k}(y)$-préschéma")
add(69, "Corollaire (17.5.6): 'On suppose que Y soit réduit et géométriquement unibranche (6.15.1) au point y.'",
    "'réduit' and 'géométriquement unibranche (6.15.1)' roman, 'et' and 'au point y' italic (page_069_s3.png)",
    "all italic in the italic statement", "convention", 6, "high",
    r"soit réduit et géométriquement unibranche (6.15.1) au point",
    r"soit \textup{réduit} et \textup{géométriquement unibranche (6.15.1)} au point",
    "The authors' emphasis of the added hypotheses, as 'réduit' in (17.5.5); (6.15.1) upright.")
add(69, "Corollaire (17.5.6): 'f^{-1}(y) soit un k(y)-préschéma géométriquement régulier au point x.'", K1,
    "plain k", "convention", 1, "high",
    "soit un $k(y)$-préschéma géométriquement régulier au point $x$.¶\\end{corollary}",
    "soit un $\\boldsymbol{k}(y)$-préschéma géométriquement régulier au point $x$.¶\\end{corollary}")
add(69, "page break 69/70 inside 'que f vérifie | en ce point toutes les propriétés'",
    "the sentence runs on to p. 70 ('en ce point toutes les propriétés définies dans (6.8.1)')",
    "blank line before \\oldpage[IV-4]{70}: a paragraph break inside the sentence", "marker", None, "high",
    "que $f$ vérifie¶¶", "que $f$ vérifie¶", "GLOBAL_ISSUES 20.")

# ---------------------------------------------------------------- checks
pages = {}
for p in range(65, 70):
    pages[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
bad = 0
for x in F:
    if x["fix"]:
        n = pages[x["page"]].count(x["fix"]["old"])
        if n != 1:
            bad += 1
            print("NOT UNIQUE in page file:", x["page"], n, repr(x["fix"]["old"][:80]))

# sequential application on the release file, as apply_fixes.py does
t = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")


def locate(text, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(text)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(text)
    return None, None


for x in F:
    if not x["fix"]:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    n = seg.count(x["fix"]["old"])
    if n != 1:
        bad += 1
        print("SEQUENTIAL FAIL:", x["page"], n, repr(x["fix"]["old"][:80]))
        continue
    t = t[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + t[e:]
(RUN / "crops_065_069" / "simulated_ega4-17.txt").write_text(t, encoding="utf-8", newline="")
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
cnt = {}
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print("findings", len(F), "problems", bad)
for p in sorted(cnt):
    print(p, cnt[p])
