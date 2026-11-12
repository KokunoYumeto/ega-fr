# Builds findings_035_039.json for EGA IV-3 pp. 35-39 and checks every fix.
# "⏎" in the strings below stands for a line break (LF).
import json

OUT = r"user/Documents/ega_scan_check_20261101/run_IV3/findings_035_039.json"
BASE = r"user/Documents/ega_scan_check_20261101/run_IV3"

def nl(s):
    return None if s is None else s.replace("⏎", "\n")

F = []
def add(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None, nofix=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if nofix else {"old": nl(old), "new": nl(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = nl(corrected)
    d["note"] = note
    F.append(d)

# ---------------- page 35 ----------------
add(35, "proof of (8.9.3), l. 5: 'on peut supposer que f_0 est surjectif'",
    "'surjectif' italic", "upright 'surjectif'", "italics", None, "high",
    r"que $f_0$ est surjectif.", r"que $f_0$ est \emph{surjectif}.")
add(35, "Corollaire (8.9.5), last line: 'le O_{X_i}-Module F_i = F (x)_{O_S} O_{S'_i}'",
    "plain equals sign: F_i = F (x) ... (enlarged crop)", r"\mathcal F_i:=\mathcal F (colon-equals)",
    "formula", None, "high",
    r"\mathcal F_i:=\mathcal F", r"\mathcal F_i=\mathcal F")
add(35, "proof of (8.9.5), l. 2: 'T_j = U_j — U_{h<j}(U_j n U_h)'",
    "long dash for the set difference (enlarged crop)", "minus sign", "convention", 7, "high",
    r"T_j=U_j-\bigcup", r"T_j=U_j\setmin\bigcup",
    "\\setmin pending the convention-7 decision (FIX_POLICY 2.7).")
add(35, "proof of (8.9.5), l. 5: 'sont constructibles dans S'",
    "'constructibles' italic", "upright", "italics", None, "high",
    r"sont constructibles dans $S$", r"sont \emph{constructibles} dans $S$")
add(35, "proof of (8.9.5), l. 5: 'dans S (1.8.1), donc'",
    "(1.8.1): no chapter numeral (enlarged crop)", "(I, 1.8.1)", "extra", None, "high",
    r"(I, 1.8.1)", r"(1.8.1)",
    "Not a misprint: the print cites (IV, 1.8.1) in section 1 of this chapter (EGA I has no 1.8.x on constructible sets); "
    "ega4-8-fr.tex writes (I, 1.x.y) for such references throughout (as reported for pp. 26, 30-31).")
add(35, "proof of (8.9.5), last line: 'est quasi-compacte puisque S est quasi-séparé (1.2.7)'",
    "(1.2.7): no chapter numeral (enlarged crop)", "(I, 1.2.7)", "extra", None, "high",
    r"(I, 1.2.7)", r"(1.2.7)",
    "Not a misprint: (IV, 1.2.7), as on p. 26.")

# ---------------- page 36 ----------------
add(36, "l. 1: 'tation finie (1.6.2, (i))'",
    "(1.6.2, (i)): no chapter numeral (enlarged crop)", "(I, 1.6.2, (i))", "extra", None, "high",
    r"(I, 1.6.2, (i))", r"(1.6.2, (i))",
    "Not a misprint: (IV, 1.6.2, (i)).")
add(36, "l. 3: 'fermé constructible dans S. Soit S = Spec(A)'",
    "'Soit S = Spec(A), et considérons' begins at the left margin: same paragraph",
    "blank line before 'Soit' (paragraph break)", "other", None, "high",
    r"constructible dans $S$.⏎⏎Soit $S=", r"constructible dans $S$.⏎Soit $S=",
    "Removes a paragraph break the print does not have.")
add(36, "l. 8: 'est de présentation finie (1.6.1)'",
    "(1.6.1): no chapter numeral (enlarged crop)", "(I, 1.6.1)", "extra", None, "high",
    r"(I, 1.6.1)", r"(1.6.1)",
    "Not a misprint: (IV, 1.6.1), as on p. 26.")
add(36, "l. 10: 'au cas où T' = S est affine. Alors (8.9.1)'",
    "'Alors (8.9.1)' follows on the same line: same paragraph", "blank line before 'Alors' (paragraph break)",
    "other", None, "high",
    r"est affine.⏎⏎Alors (8.9.1)", r"est affine.⏎Alors (8.9.1)",
    "Removes a paragraph break the print does not have.")
add(36, "end of the proof of (8.9.5): 'F_{λi} = ... soit plat sur S'_{λi}'",
    "'plat' italic", "upright", "italics", None, "high",
    r"soit plat sur $S'_{\lambda i}$", r"soit \emph{plat} sur $S'_{\lambda i}$")
add(36, "heading 8.10",
    "'8.10. Propriétés de permanence des morphismes par passage à la limite projective.' (final full stop)",
    "\\subsection{...} without the full stop", "punctuation", None, "high",
    r"à la limite projective}", r"à la limite projective.}",
    "GLOBAL_ISSUES 43/58.")
add(36, "Proposition (8.10.1), l. 2: '(resp. universellement ouvert), alors'",
    "'(resp.' and the closing parenthesis roman in the italic statement (enlarged crop)",
    "italic (proposition environment)", "convention", 6, "high",
    r"ouvert (resp. universellement ouvert), alors",
    r"ouvert \textup{(resp.} universellement ouvert\textup{)}, alors")
add(36, "Proposition (8.10.1), end: '(resp. universellement ouvert).'",
    "'(resp.' and the closing parenthesis roman (enlarged crop)", "italic", "convention", 6, "high",
    r"(resp. universellement ouvert).⏎\end{proposition}",
    r"\textup{(resp.} universellement ouvert\textup{)}.⏎\end{proposition}")
add(36, "proof of (8.10.1), l. 3: 'pour tout ouvert quasi-compact U de X'",
    "'quasi-compact' italic", "upright", "italics", None, "high",
    r"ouvert quasi-compact $U$ de $X$", r"ouvert \emph{quasi-compact} $U$ de $X$")
add(36, "proof of (8.10.1), last line: '(I, 3.4.8), donc f(U)'",
    "bold I (enlarged crop)", "plain I", "convention", 2, "high",
    r"(I, 3.4.8)", r"(\textbf{I}, 3.4.8)")
add(36, "Corollaire (8.10.2), l. 3: 'X_n = X x_Y Y_n'",
    "the subscript n of X_n is a bold italic n (wrong fount); the other subscript n's of the line are ordinary (enlarged crop; "
    "149 dark px, mean stroke run 6.2 px against 120-126 px and 3.6-4.3 px for the ordinary subscript n's of the page)",
    "$X_n$ (ordinary n): silent correction", "misprint_in_print", None, "high",
    r"$X_n=X\times_YY_n$", r"$X_{\boldsymbol{n}}=X\times_YY_n$",
    "Wrong-fount letter, kept in the diplomatic text (GLOBAL_ISSUES 29). Three more subscripts on this page look a little heavier "
    "but measure within the range of the ordinary n's of pp. 36-37 (up to 136 px): the last Y_n of (8.10.2), T_n in "
    "'Y_n = Y (x) Z[T_1, ..., T_n]', and Y_n in 'fermé de Y_n'; not reported.",
    corrected=r"$X_n=X\times_YY_n$")
add(36, "proof of (8.10.2), l. 4: 'le morphisme f_n^{-1}(U_n) -> U_n'",
    "the subscript n of f_n is a bold italic n (wrong fount); the n's of U_n are ordinary (enlarged crop; 145 dark px, "
    "mean stroke run 6.6 px against 121-128 px and 4.1-4.4 px for the other subscript n's of the line)",
    "$f_n^{-1}$ (ordinary n): silent correction", "misprint_in_print", None, "high",
    r"$f_n^{-1}(U_n)\to U_n$", r"$f_{\boldsymbol{n}}^{-1}(U_n)\to U_n$",
    "Wrong-fount letter, kept in the diplomatic text (GLOBAL_ISSUES 29).",
    corrected=r"$f_n^{-1}(U_n)\to U_n$")
add(36, "proof of (8.10.2), l. 5: 'est affine. En outre'",
    "'affine' italic", "upright", "italics", None, "high",
    r"est⏎affine. En outre", r"est⏎\emph{affine}. En outre")
add(36, "proof of (8.10.2), l. 6: 'est lui aussi affine'",
    "'affine' italic", "upright", "italics", None, "high",
    r"est lui aussi affine,", r"est lui aussi \emph{affine},")
add(36, "proof of (8.10.2), l. 7: 'donc quotient d'une algèbre'",
    "'quotient' italic", "upright", "italics", None, "high",
    r"donc quotient d'une", r"donc \emph{quotient} d'une")
add(36, "proof of (8.10.2), last line: 'A[T_1, ..., T_n]'",
    "the subscript n of T_n is a bold italic n (wrong fount) (enlarged crop; 148 dark px, mean stroke run 5.9 px; "
    "the T_n of 'U_n = U (x) Z[T_1, ..., T_n]' three lines above: 122 px, 4.4 px)",
    "$T_n$ (ordinary n): silent correction", "misprint_in_print", None, "high",
    r"$A[T_1,\ldots,T_n]$", r"$A[T_1,\ldots,T_{\boldsymbol{n}}]$",
    "Wrong-fount letter, kept in the diplomatic text (GLOBAL_ISSUES 29).",
    corrected=r"$A[T_1,\ldots,T_n]$")

# ---------------- page 37 ----------------
add(37, "Proposition (8.10.3), 3°: 'les morphismes u_{λμ} : S_μ -> S_λ soient plats;'",
    "'plats;' roman in the italic statement (enlarged crop)", "italic (proposition environment)",
    "convention", 6, "high",
    r"soient plats~;", r"soient \textup{plats}~;")
add(37, "proof of (8.10.3), l. 2: 'quasi-compact (1.2.4); par suite'",
    "(1.2.4): no chapter numeral", "(I, 1.2.4)", "extra", None, "high",
    r"(I, 1.2.4)", r"(1.2.4)",
    "Not a misprint: (IV, 1.2.4).")
add(37, "proof of (8.10.3), l. 2: 'par suite f_α(X_α) = Z_α est pro-constructible'",
    "no closure bar over f_α(X_α) (the pixel rows above the formula are blank; the bar over f_α(X_α) in 4° of the statement is solid)",
    r"\overline{f_\alpha(X_\alpha)}=Z_\alpha", "formula", None, "high",
    r"\overline{f_\alpha(X_\alpha)}=Z_\alpha", r"f_\alpha(X_\alpha)=Z_\alpha",
    "Not a misprint: Z_α is the image, pro-constructible by (1.9.5, (vii)) because f_α is quasi-compact, and (I, 3.4.8) "
    "concerns images, so Z_λ = f_λ(X_λ) and Z = f(X) follow; the TeX's three closure bars in this proof are additions.")
add(37, "proof of (8.10.3), l. 2-3: 'est pro-constructible (1.9.5, (vii)) dans Y_α'",
    "(1.9.5, (vii)): no chapter numeral (enlarged crop)", "(I, 1.9.5, (vii))", "extra", None, "high",
    r"(I, 1.9.5,⏎(vii)) dans", r"(1.9.5,⏎(vii)) dans",
    "Not a misprint: (IV, 1.9.5, (vii)), the image of a pro-constructible set under a quasi-compact morphism.")
add(37, "proof of (8.10.3), l. 3: 'on a donc Z_λ = f_λ(X_λ)'",
    "no closure bar over f_λ(X_λ) (blank pixel rows above)", r"\overline{f_\lambda(X_\lambda)}", "formula", None, "high",
    r"Z_\lambda=\overline{f_\lambda(X_\lambda)}", r"Z_\lambda=f_\lambda(X_\lambda)",
    "See the finding on Z_α above.")
add(37, "proof of (8.10.3), l. 4: 'et Z = f(X) (I, 3.4.8)'",
    "no closure bar over f(X) (blank pixel rows above)", r"\overline{f(X)}", "formula", None, "high",
    r"Z=\overline{f(X)}", r"Z=f(X)",
    "See the finding on Z_α above.")
add(37, "proof of (8.10.3), l. 4: '(I, 3.4.8) et Z_λ'",
    "bold I (enlarged crop)", "plain I", "convention", 2, "high",
    r"(I, 3.4.8)", r"(\textbf{I}, 3.4.8)")
add(37, "proof of (8.10.3), l. 4: '(I, 3.4.8) et Z_λ est pro-constructible'",
    "no comma after the reference (enlarged crop)", "'(I, 3.4.8), et'", "punctuation", None, "high",
    r", et $Z_\lambda$ est", r" et $Z_\lambda$ est")
add(37, "proof of (8.10.3), l. 4: 'pro-constructible dans Y_λ (1.9.5, (vi))'",
    "(1.9.5, (vi)): no chapter numeral, item (vi) (enlarged crop)", "(I, 1.9.5, (vii))", "number", None, "high",
    r"(I, 1.9.5, (vii)). Il suffit", r"(1.9.5, (vi)). Il suffit",
    "Not a misprint: (IV, 1.9.5, (vi)) is the statement on inverse images, which gives Z_λ = w_{αλ}^{-1}(Z_α) "
    "pro-constructible; the TeX repeats the (vii) of the earlier reference and adds 'I, '.")
add(37, "proof of (8.10.4), l. 5-6: 'par hypothèse (1.2.3, (iii))'",
    "(1.2.3, (iii)): no chapter numeral (enlarged crop)", "(I, 1.2.3, (iii))", "extra", None, "high",
    r"(I, 1.2.3, (iii))", r"(1.2.3, (iii))",
    "Not a misprint: (IV, 1.2.3, (iii)), as on p. 31.")
add(37, "proof of (8.10.4), l. 7: 'il résulte de (I, 5.3.4 et 3.4.8)'",
    "bold I (enlarged crop)", "plain I", "convention", 2, "high",
    r"(I, 5.3.4 et 3.4.8)", r"(\textbf{I}, 5.3.4 et 3.4.8)")
add(37, "proof of (8.10.4), l. 9: 'D'autre part Δ_λ est constructible dans X'_λ'",
    "'constructible' italic", "upright", "italics", None, "high",
    r"est⏎constructible dans $X'_\lambda$~:", r"est⏎\emph{constructible} dans $X'_\lambda$~:")
add(37, "proof of (8.10.4), l. 11: 'de type fini (1.4.3 et 1.5.4, (iii))'",
    "(1.4.3 et 1.5.4, (iii)) (enlarged crop)", "(I, 4.3 et I, 5.4, (iii))", "number", None, "high",
    r"(I, 4.3 et I, 5.4, (iii))", r"(1.4.3 et 1.5.4, (iii))",
    "The old-style 1 of 1.4.3 and 1.5.4 was read as the numeral I; the print cites (IV, 1.4.3) and (IV, 1.5.4, (iii)).")
labels37 = [("(i)", r"\item[(i)] un", r"\item[\textup{(i)}] un"),
            ("(i bis)", r"\item[(i \emph{bis})]", r"\item[\textup{(i \emph{bis})}]"),
            ("(ii)", r"\item[(ii)]", r"\item[\textup{(ii)}]"),
            ("(iii)", r"\item[(iii)]", r"\item[\textup{(iii)}]"),
            ("(iv)", r"\item[(iv)]", r"\item[\textup{(iv)}]"),
            ("(v)", r"\item[(v)]", r"\item[\textup{(v)}]"),
            ("(vi)", r"\item[(vi)]", r"\item[\textup{(vi)}]")]
for lab, old, new in labels37:
    add(37, "Théorème (8.10.5), label " + lab,
        "label upright" + (" ('bis' italic)" if "bis" in lab else ""),
        "\\item label comes out italic in the italic theorem", "convention", 6, "high", old, new,
        "Roman-numeral labels in italic statements are upright in the print (GLOBAL_ISSUES 16).")

# ---------------- page 38 ----------------
labels38a = ["(vii)", "(viii)", "(ix)", "(x)", "(xi)", "(xii)"]
for lab in labels38a:
    add(38, "Théorème (8.10.5), label " + lab, "label upright",
        "\\item label comes out italic in the italic theorem", "convention", 6, "high",
        r"\item[" + lab + "]", r"\item[\textup{" + lab + "}]",
        "GLOBAL_ISSUES 16.")
add(38, "Théorème (8.10.5), after item (xii): 'Alors, si P désigne ...'",
    "'Alors' begins an indented paragraph after the list", "text follows \\end{enumerate} without a blank line (no indent)",
    "other", None, "high",
    r"\end{enumerate}⏎Alors, si", r"\end{enumerate}⏎⏎Alors, si",
    "Paragraph break after the list, as printed (cf. GLOBAL_ISSUES 47 for displays).")
add(38, "Théorème (8.10.5): 'si P désigne une des propriétés précédentes'",
    "bold italic P (enlarged crop)", r"\mathbf P", "convention", 10, "high",
    r"si $\mathbf P$ désigne", r"si $\boldsymbol{P}$ désigne")
add(38, "Théorème (8.10.5): 'possède la propriété P, il faut'",
    "bold italic P", r"\mathbf P", "convention", 10, "high",
    r"la propriété $\mathbf P$, il faut", r"la propriété $\boldsymbol{P}$, il faut")
add(38, "Théorème (8.10.5): 'f_λ possède la propriété P (auquel cas'",
    "bold italic P", r"\mathbf P", "convention", 10, "high",
    r"la propriété $\mathbf P$⏎(auquel", r"la propriété $\boldsymbol{P}$⏎(auquel")
add(38, "Théorème (8.10.5): 'lorsque P est la propriété d'être'",
    "bold italic P", r"\mathbf P", "convention", 10, "high",
    r"lorsque $\mathbf P$ est", r"lorsque $\boldsymbol{P}$ est")
for lab in ["(xiii)", "(xiv)"]:
    add(38, "Théorème (8.10.5), label " + lab, "label upright",
        "\\item label comes out italic in the italic theorem", "convention", 6, "high",
        r"\item[" + lab + "]", r"\item[\textup{" + lab + "}]",
        "GLOBAL_ISSUES 16.")
add(38, "proof of (8.10.5), l. 1: 'Le cas où P est l'une des propriétés'",
    "bold italic P (enlarged crop)", r"\mathbf P", "convention", 10, "high",
    r"Le cas où $\mathbf P$ est", r"Le cas où $\boldsymbol{P}$ est")
add(38, "proof of (8.10.5), l. 3: 'compte tenu de (I, 5.4.1 et 5.3.4)'",
    "bold I", "plain I", "convention", 2, "high",
    r"(I, 5.4.1 et 5.3.4)", r"(\textbf{I}, 5.4.1 et 5.3.4)")
add(38, "proof of (8.10.5), l. 4: 'en utilisant (I, 5.3.8)'",
    "bold I", "plain I", "convention", 2, "high",
    r"(I, 5.3.8)", r"(\textbf{I}, 5.3.8)")
add(38, "proof of (8.10.5), 2nd paragraph, l. 2: 'des conditions sur les fibres f^{-1}(y)'",
    "'fibres' italic", "upright", "italics", None, "high",
    r"sur les fibres $f^{-1}(y)$", r"sur les \emph{fibres} $f^{-1}(y)$")
add(38, "proof of (8.10.5), 2nd paragraph, l. 3: 'par changement de base (I, 3.6.4)'",
    "bold I", "plain I", "convention", 2, "high",
    r"(I, 3.6.4)", r"(\textbf{I}, 3.6.4)")
add(38, "proof of (8.10.5), 2nd paragraph, l. 4: 'radicielles (I, 3.5.8)'",
    "bold I", "plain I", "convention", 2, "high",
    r"(I, 3.5.8)", r"(\textbf{I}, 3.5.8)")
add(38, "proof of (8.10.5), 2nd paragraph, l. 5: 'finies (II, 6.2.2 et 6.2.3 et I, 6.4.4,'",
    "bold II (two strokes; enlarged crop)", "(III, 6.2.2", "number", None, "high",
    r"(III, 6.2.2", r"(\textbf{II}, 6.2.2",
    "EGA II 6.2 treats quasi-finite morphisms. One edit for the wrong numeral and the bold of convention 2.")
add(38, "proof of (8.10.5), 2nd paragraph, l. 5: 'et I, 6.4.4,'",
    "bold I", "plain I", "convention", 2, "high",
    r"et I, 6.4.4", r"et \textbf{I}, 6.4.4")
add(38, "proof of (8.10.5), 2nd paragraph, l. 6: 'de type fini par (1.5.4, (v))'",
    "(1.5.4, (v)) (enlarged crop)", "(I, 5.4, (v))", "number", None, "high",
    r"(I, 5.4,⏎(v))", r"(1.5.4,⏎(v))",
    "The old-style 1 of 1.5.4 was read as the numeral I; the print cites (IV, 1.5.4, (v)).")
add(38, "proof of (8.10.5), 2nd paragraph, l. 5-6: '(II, 6.2.2 et 6.2.3 et I, 6.4.4, compte tenu de ... par (1.5.4, (v)).'",
    "the parenthesis opened before II is never closed: the sentence ends '(v)).' with two closing parentheses (enlarged crop)",
    "the TeX keeps the two closing parentheses", "misprint_in_print", None, "medium",
    None, None,
    "Missing closing parenthesis in the print, kept in the diplomatic text; the corrected edition needs a third ')' after "
    "'(v))' (after the number fix above).",
    corrected=r"(1.5.4,⏎(v)))", nofix=True)
add(38, "proof of (8.10.5), 3rd paragraph, l. 2: 'toutes les propriétés P envisagées'",
    "bold italic P (enlarged crop)", r"\mathbf P", "convention", 10, "high",
    r"les propriétés $\mathbf P$⏎envisagées", r"les propriétés $\boldsymbol{P}$⏎envisagées")
add(38, "proof of (8.10.5), 3rd paragraph, l. 7: 'S_0 = Spec(A_0) est affine (donc quasi-séparé)'",
    "'affine' italic", "upright", "italics", None, "high",
    r"est affine (donc quasi-séparé)", r"est \emph{affine} (donc quasi-séparé)")
add(38, "proof of (8.10.5): 'Cas (ii), (iii), (iv) :'",
    "only 'Cas' italic; the labels (ii), (iii), (iv) upright (enlarged crop)", "\\emph{Cas (ii), (iii), (iv)}",
    "italics", None, "high",
    r"\emph{Cas (ii), (iii), (iv)}", r"\emph{Cas} (ii), (iii), (iv)")

# ---------------- page 39 ----------------
add(39, "proof of (8.10.5): 'Cas (vi) et (vii) :'",
    "'Cas' and 'et' italic, the labels upright (enlarged crop)", "\\emph{Cas (vi) et (vii)}", "italics", None, "high",
    r"\emph{Cas (vi) et (vii)}", r"\emph{Cas} (vi) \emph{et} (vii)")
add(39, "proof of (8.10.5), case (vi): 'Z = f(X) (I, 3.4.8). Comme'",
    "bold I (enlarged crop)", "plain I", "convention", 2, "high",
    r"(I, 3.4.8)", r"(\textbf{I}, 3.4.8)")
add(39, "proof of (8.10.5), case (vii): '(I, 5.3.4 et 3.3.11)'",
    "bold I (enlarged crop)", "plain I", "convention", 2, "high",
    r"(I, 5.3.4 et 3.3.11)", r"(\textbf{I}, 5.3.4 et 3.3.11)")
add(39, "proof of (8.10.5): 'Cas (viii) et (ix) :'",
    "'Cas' and 'et' italic, the labels upright (enlarged crop)", "\\emph{Cas (viii) et (ix)}", "italics", None, "high",
    r"\emph{Cas (viii) et (ix)}", r"\emph{Cas} (viii) \emph{et} (ix)")
add(39, "proof of (8.10.5), cases (viii)-(ix): 'S quasi-compact (II, 5.1.9)'",
    "bold II (enlarged crop)", "plain II", "convention", 2, "high",
    r"(II, 5.1.9)", r"(\textbf{II}, 5.1.9)")
add(39, "proof of (8.10.5): 'Cas (x) :'",
    "only 'Cas' italic (enlarged crop)", "\\emph{Cas (x)}", "italics", None, "high",
    r"\emph{Cas (x)}", r"\emph{Cas} (x)")
add(39, "proof of (8.10.5), case (x), l. 3: 'un A_λ-module de présentation finie B_λ'",
    "'module' italic (enlarged crop)", "upright", "italics", None, "high",
    r"un $A_\lambda$-module⏎de", r"un $A_\lambda$-\emph{module}⏎de")
add(39, "proof of (8.10.5), case (x), l. 3: 'tels que le A-module B soit isomorphe'",
    "'module' italic (enlarged crop)", "upright", "italics", None, "high",
    r"le $A$-module $B$", r"le $A$-\emph{module} $B$")

# ---------------- checks ----------------
pages = {}
for p in sorted({f["page"] for f in F}):
    with open(f"{BASE}/page_{p:03d}.tex", encoding="utf-8", newline="") as fh:
        pages[p] = fh.read().replace("\r\n", "\n")
bad = 0
for f in F:
    if f["fix"] is None:
        continue
    c = pages[f["page"]].count(f["fix"]["old"])
    if c != 1:
        bad += 1
        print("COUNT", c, f["page"], repr(f["fix"]["old"]))
# apply all fixes per page in order, to check they are compatible
for p, txt in pages.items():
    t = txt
    for f in F:
        if f["page"] != p or f["fix"] is None:
            continue
        if t.count(f["fix"]["old"]) != 1:
            bad += 1
            print("SEQ", p, repr(f["fix"]["old"]))
        t = t.replace(f["fix"]["old"], f["fix"]["new"], 1)
print("findings", len(F), "problems", bad)
from collections import Counter
cnt = Counter()
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    cnt[(f["page"], k)] += 1
for p in sorted({f["page"] for f in F}):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print("written", OUT)
