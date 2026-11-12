import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
OUT = RUN / "findings_110_114.json"
NL = "<NL>"


def F(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf)
    d["fix"] = None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}
    if kind == "misprint_in_print":
        d["corrected"] = corrected.replace(NL, "\n")
    d["note"] = note
    return d


def C2(page, where, numeral, ref, old=None, new=None, note=""):
    if old is None:
        old = "{" + numeral + ", " + ref + "}"
        new = "{\\textbf{" + numeral + "}, " + ref + "}"
    return F(page, where, f"({numeral}, {ref}) with bold {numeral}",
             f"({numeral}, {ref}) with plain {numeral} in the link text", "convention", 2, "high", old, new, note)


def RESP(page, where, word, old, new, note=""):
    return F(page, where, f"'(resp.' and the closing parenthesis upright, '{word}' italic",
             "the whole parenthesis italic (inside the \\itshape environment)", "convention", 6, "high", old, new, note)


def LAB(page, lab, nxt):
    return F(page, f"Proposition (6.1.5): item label {lab}", f"label {lab} upright",
             f"\\item[{lab}] comes out italic inside the italic proposition environment", "convention", 6, "high",
             f"\\item[{lab}]", f"\\item[\\textup{{{lab}}}]", "GLOBAL_ISSUES item 16 (labels fixed locally as on pp. 150-154 of EGA I).")


def K(page, where, old, new):
    return F(page, where, "bold italic k", "plain $k$", "convention", 1, "high", old, new)


def ITAL(page, where, word, old, new, note=""):
    return F(page, where, f"'{word}' italic", f"'{word}' upright (no \\emph)", "italics", None, "high", old, new, note)


L = []
# ---------------- page 110 ----------------
L.append(F(110, "top of page: 'on a S'=Spec(A[c_1, ..., c_n]) (I, 6.3.3)'",
           "continues the sentence 'Or, si S' est affine et de type fini sur S=Spec(A), on a ...' from p. 109; line not indented, no new paragraph",
           "blank line after \\oldpage[II]{110} (and a blank line before the marker, at the end of the p. 109 segment) starts a new paragraph",
           "other", None, "high", r"\oldpage[II]{110}<NL><NL>on a", r"\oldpage[II]{110}<NL>on a",
           "spurious paragraph break at the page marker (GLOBAL_ISSUES item 20). The blank line before the marker "
           "(end of the p. 109 segment, after 'sur $S=\\operatorname{Spec}(A)$,') must be removed as well; it lies outside this page's segment."))
L.append(C2(110, "first line: 'on a S'=Spec(A[c_1, ..., c_n]) (I, 6.3.3)'", "I", "6.3.3"))
L.append(C2(110, "after the diagram: 'sont des immersions fermées (I, 4.3.1)'", "I", "4.3.1"))
L.append(F(110, "after the diagram: 'et (f_0)_(S') est fermé par hypothèse; il en est donc de même de (f_0)_(S'')'",
           "(f_0)_{(S')} est fermé par hypothèse; il en est donc de même de (f_0)_{(S'')}  (S' first, S'' second; checked on a crop)",
           "TeX silently corrects to (f_0)_{(S'')} ... de même de (f_0)_{(S')}",
           "misprint_in_print", None, "high",
           r"$(f_0)_{(S'')}$ est fermé par hypothèse~;<NL>il en est donc de même de $(f_0)_{(S')}$.",
           r"$(f_0)_{(S')}$ est fermé par hypothèse~;<NL>il en est donc de même de $(f_0)_{(S'')}$.",
           "The hypothesis (second condition of the corollary on p. 109) concerns S''=Spec(A[T_1,...,T_n]); closedness of (f_0)_(S'') "
           "and the closed immersions j, 1_X x j give closedness of (f_0)_(S'). The print swaps S' and S''. Both subscripts in one edit.",
           corrected=r"$(f_0)_{(S'')}$ est fermé par hypothèse~; il en est donc de même de $(f_0)_{(S')}$."))
L.append(F(110, "Définition (6.1.1), first words", "Soient X un S-préschéma, f: X->S son morphisme structural",
           "Soit $X$ un $S$-préschéma", "word", None, "high",
           r"Soit $X$ un $S$-préschéma", r"Soient $X$ un $S$-préschéma", "Checked on a crop."))
for w, old, new in [
    ("entier au-dessus de S", r"\emph{entier au-dessus de $S$}", r"entier au-dessus de $S$"),
    ("morphisme entier", r"\emph{morphisme<NL>entier}", r"morphisme<NL>entier"),
    ("fini au-dessus de S", r"\emph{fini au-dessus de<NL>$S$}", r"fini au-dessus de<NL>$S$"),
    ("morphisme fini", r"\emph{morphisme fini}", r"morphisme fini"),
]:
    L.append(F(110, f"Définition (6.1.1): '{w}'", f"'{w}' in the same italic as the rest of the definition (no change of face)",
               f"\\emph{{{w}}} inside the \\itshape definition environment (comes out upright)", "convention", 6, "high", old, new,
               "Printed italic words left upright by \\emph inside the italic environment; drop the \\emph. Checked on a crop."))
L.append(ITAL(110, "(6.1.2), first sentence: 'il est affine au-dessus de S'", "affine",
              r"il est affine au-dessus", r"il est \emph{affine} au-dessus"))
L.append(ITAL(110, "(6.1.2): 'si et seulement si c'est un O_S-Module de type fini (I, 1.3.9)'", "Module de type fini",
              r"c'est un $\mathcal{O}_S$-Module de<NL>type fini", r"c'est un $\mathcal{O}_S$-\emph{Module de<NL>type fini}",
              "The whole 'Module de type fini' is italic in the print. Checked on a crop."))
L.append(C2(110, "(6.1.2): 'c'est un O_S-Module de type fini (I, 1.3.9)'", "I", "1.3.9"))
L.append(F(110, "(6.1.2): 'que B est une O_S-Algèbre entière et de type fini, car'",
           "'entière' italic, 'et' roman, 'de type fini' italic", "all upright", "italics", None, "high",
           r"-Algèbre entière et de type fini, car", r"-Algèbre \emph{entière} et \emph{de type fini}, car", "Checked on a crop."))
L.append(C2(110, "proof of (6.1.3): 'les O_S-Modules cohérents (I, 1.5.1)'", "I", "1.5.1"))
L.append(F(110, "Proposition (6.1.4), first words", "Soient X un préschéma entier (resp. fini) au-dessus de S, f: X->S le morphisme structural",
           "Soit $X$ un préschéma entier", "word", None, "high",
           r"Soit $X$ un préschéma entier", r"Soient $X$ un préschéma entier", "Checked on a crop."))
L.append(RESP(110, "Proposition (6.1.4): 'entier (resp. fini) au-dessus de S'", "fini",
              r"(resp. fini) au-dessus de $S$, $f:X\to S$", r"\textup{(resp. \emph{fini})} au-dessus de $S$, $f:X\to S$"))
L.append(RESP(110, "Proposition (6.1.4), end: 'une algèbre entière (resp. finie) sur A'", "finie",
              r"(resp. finie) sur $A$.", r"\textup{(resp. \emph{finie})} sur $A$."))

# ---------------- page 111 ----------------
L.append(F(111, "proof of Lemme (6.1.4.1): 'dans M_{g_i}, m/1=(Σ a_ij m_ij)/g_i^p'",
           "the index under Σ is i: m/1=(Σ_i a_{ij} m_{ij})/g_i^p (checked on a crop; same i as under the two later sums)",
           "TeX silently corrects to \\sum_j", "misprint_in_print", None, "high",
           r"(\sum_j a_{ij}m_{ij})", r"(\sum_i a_{ij}m_{ij})",
           "i is fixed ('pour chaque i ... dans M_{g_i}'); the sum runs over j.",
           corrected=r"(\sum_j a_{ij}m_{ij})"))
for lab, nxt in [("(i)", ""), ("(ii)", ""), ("(iii)", ""), ("(iv)", ""), ("(v)", ""), ("(vi)", "")]:
    L.append(LAB(111, lab, nxt))
L.append(F(111, "Proposition (6.1.5) (i): '(et a fortiori entière)'", "'a fortiori' upright; '(et' and 'entière)' italic",
           "'a fortiori' italic (inside the \\itshape environment)", "convention", 6, "high",
           r"(et a fortiori entière)", r"(et \textup{a fortiori} entière)", "Checked on a crop."))
L.append(RESP(111, "(6.1.5) (ii): 'deux morphismes finis (resp. entiers)'", "entiers",
              r"morphismes finis (resp. entiers)", r"morphismes finis \textup{(resp. \emph{entiers})}"))
L.append(RESP(111, "(6.1.5) (ii): 'est fini (resp. entier).'", "entier",
              r"est fini<NL>(resp. entier).", r"est fini<NL>\textup{(resp. \emph{entier})}."))
L.append(RESP(111, "(6.1.5) (iii): 'S-morphisme fini (resp. entier)'", "entier",
              r"$S$-morphisme fini (resp. entier)", r"$S$-morphisme fini \textup{(resp. \emph{entier})}"))
L.append(F(111, "(6.1.5) (iii): 'Si f: X->Y est un S-morphisme fini (resp. entier) f_(S'): X_(S')->Y_(S') est fini'",
           "no comma after '(resp. entier)' before f_(S') (checked on a crop)",
           "TeX silently adds the comma: '(resp. entier),'", "misprint_in_print", None, "high",
           r",<NL>$f_{(S')}", r"<NL>$f_{(S')}",
           "The comma closing the conditional clause is missing in the print. Independent of the '(resp. entier)' convention-6 edit just before it.",
           corrected=r"(resp. entier), $f_{(S')}:X_{(S')}\to Y_{(S')}$"))
L.append(RESP(111, "(6.1.5) (iii): 'est fini (resp. entier) pour toute extension'", "entier",
              r"(resp. entier) pour toute", r"\textup{(resp. \emph{entier})} pour toute"))
L.append(RESP(111, "(6.1.5) (iv): 'S-morphismes finis (resp. entiers), il en est'", "entiers",
              r"(resp. entiers), il en est", r"\textup{(resp. \emph{entiers})}, il en est"))
L.append(F(111, "(6.1.5) (iv): 'il en est de même de f x_S g : ...'",
           "f\\times_S g : X\\times_S Y \\to X'\\times_S Y' (checked on a crop)",
           "TeX silently corrects to X\\times_S X'\\to Y\\times_S Y'", "misprint_in_print", None, "high",
           r"X\times_S X'\to Y\times_S Y'", r"X\times_S Y\to X'\times_S Y'",
           "f: X->Y and g: X'->Y' give f x_S g : X x_S X' -> Y x_S Y'; the print has Y and X' interchanged.",
           corrected=r"X\times_S X'\to Y\times_S Y'"))
L.append(RESP(111, "(6.1.5) (v): 'g∘f soit fini (resp. entier) et g séparé'", "entier",
              r"soit fini (resp. entier) et", r"soit fini \textup{(resp. \emph{entier})} et"))
L.append(RESP(111, "(6.1.5) (v), end: 'alors f est fini (resp. entier).'", "entier",
              r"alors $f$ est fini (resp. entier).", r"alors $f$ est fini \textup{(resp. \emph{entier})}."))
L.append(RESP(111, "(6.1.5) (vi): 'un morphisme fini (resp. entier), il en est de même'", "entier",
              r"morphisme fini (resp. entier), il", r"morphisme fini \textup{(resp. \emph{entier})}, il"))

# ---------------- page 112 ----------------
L.append(C2(112, "first line: 'En vertu de (I, 5.5.12)'", "I", "5.5.12"))
L.append(C2(112, "proof of (6.1.5) (iii): 'X_(S') s'identifie à X x_Y Y_(S') (I, 3.3.11)'", "I", "3.3.11"))
L.append(RESP(112, "Corollaire (6.1.6): 'préschéma entier (resp. fini) au-dessus de S, alors'", "fini",
              r"(resp. fini) au-dessus de $S$, alors", r"\textup{(resp. \emph{fini})} au-dessus de $S$, alors"))
L.append(RESP(112, "Corollaire (6.1.6): 'f^{-1}(U) est entier (resp. fini) au-dessus de U'", "fini",
              r"(resp. fini) au-dessus de $U$", r"\textup{(resp. \emph{fini})} au-dessus de $U$"))
L.append(K(112, "Corollaire (6.1.7): 'schéma algébrique fini sur k(y)'",
           r"algébrique fini sur $k(y)$", r"algébrique fini sur $\boldsymbol{k}(y)$"))
L.append(F(112, "Corollaire (6.1.7): 'et a fortiori son espace sous-jacent'", "'a fortiori' upright inside the italic statement",
           "'a fortiori' italic (inside the \\itshape corollary environment)", "convention", 6, "high",
           r"a fortiori son", r"\textup{a fortiori} son", "Checked on a crop."))
L.append(K(112, "proof of (6.1.7): 'en tant que k(y)-préschéma'", r"que $k(y)$-préschéma", r"que $\boldsymbol{k}(y)$-préschéma"))
L.append(K(112, "proof of (6.1.7): 'identifié à X x_Y Spec(k(y))'",
           r"$X\times_Y\operatorname{Spec}(k(y))$", r"$X\times_Y\operatorname{Spec}(\boldsymbol{k}(y))$"))
L.append(C2(112, "proof of (6.1.7): '(I, 3.6.1)'", "I", "3.6.1"))
L.append(K(112, "proof of (6.1.7): 'fini au-dessus de Spec(k(y))'",
           r"de $\operatorname{Spec}(k(y))$", r"de $\operatorname{Spec}(\boldsymbol{k}(y))$"))
L.append(K(112, "proof of (6.1.7): 'algèbre de rang fini sur k(y)'", r"rang fini sur $k(y)$", r"rang fini sur $\boldsymbol{k}(y)$"))
L.append(C2(112, "proof of (6.1.7): 'résulte alors de (I, 6.4.4)'", "I", "6.4.4"))
L.append(F(112, "Corollaire (6.1.8): 'f: X->S un morphisme dominant.'", "'dominant' upright (roman) inside the italic statement",
           "'dominant' italic (inside the \\itshape corollary environment)", "convention", 6, "high",
           r"morphisme dominant.", r"morphisme \textup{dominant}.", "Checked on a crop."))
L.append(RESP(112, "Corollaire (6.1.8): 'Si f est entier (resp. fini), le corps'", "fini",
              r"(resp. fini), le corps", r"\textup{(resp. \emph{fini})}, le corps"))
L.append(RESP(112, "Corollaire (6.1.8): '(resp. algébrique de degré fini)'", "algébrique de degré fini",
              r"(resp. algébrique de degré fini)", r"\textup{(resp. \emph{algébrique de degré fini})}"))
L.append(K(112, "proof of (6.1.8): 'le k(s)-préschéma f^{-1}(s)'", r"le $k(s)$-préschéma", r"le $\boldsymbol{k}(s)$-préschéma"))
L.append(K(112, "proof of (6.1.8): 'au-dessus de Spec(k(s))'",
           r"$\operatorname{Spec}(k(s))$", r"$\operatorname{Spec}(\boldsymbol{k}(s))$"))
L.append(K(112, "proof of (6.1.8): 'étant égal à k(x)'", r"égal à $k(x)$", r"égal à $\boldsymbol{k}(x)$"))
L.append(C2(112, "proof of (6.1.8): 'égal à k(x) (I, 3.6.5)'", "I", "3.6.5"))
L.append(K(112, "proof of (6.1.8): 'entière (resp. finie) sur k(s) (6.1.4)'", r"sur $k(s)$", r"sur $\boldsymbol{k}(s)$"))
L.append(ITAL(112, "proof of (6.1.10): 'il suffit de montrer que f est fermé.'", "fermé",
              r"est<NL>fermé. Soit", r"est<NL>\emph{fermé}. Soit", "Checked on a crop."))
L.append(F(112, "end of page: '... il existe un sous-préschéma de X ayant' / p. 113 'pour espace sous-jacent Z'",
           "the sentence runs on to p. 113 without a paragraph break",
           "blank line at the end of the segment, before \\oldpage[II]{113}, ends the paragraph",
           "other", None, "high", r"de $X$<NL>ayant<NL><NL>", r"de $X$<NL>ayant<NL>",
           "spurious paragraph break at the page marker (GLOBAL_ISSUES item 20); apply together with the p. 113 top-of-page fix."))

# ---------------- page 113 ----------------
L.append(F(113, "top of page: 'pour espace sous-jacent Z (I, 5.2.1)'",
           "continues the sentence 'il existe un sous-préschéma de X ayant' from p. 112; line not indented, no new paragraph",
           "blank line after \\oldpage[II]{113} starts a new paragraph", "other", None, "high",
           r"\oldpage[II]{113}<NL><NL>pour espace", r"\oldpage[II]{113}<NL>pour espace",
           "spurious paragraph break at the page marker (GLOBAL_ISSUES item 20); apply together with the p. 112 end-of-page fix (blank line before the marker)."))
L.append(C2(113, "first line: 'pour espace sous-jacent Z (I, 5.2.1)'", "I", "5.2.1",
            r"$Z$ (\hyperref[I.5.2.1-fr]{I, 5.2.1})", r"$Z$ (\hyperref[I.5.2.1-fr]{\textbf{I}, 5.2.1})"))
L.append(ITAL(113, "proof of (6.1.10): 'à prouver que f(X) est fermé dans Y'", "fermé",
              r"est fermé dans $Y$", r"est \emph{fermé} dans $Y$", "Checked on a crop."))
L.append(F(113, "proof of (6.1.10): 'En vertu de (6.1.5, (vi)), on peut supposer X et Y réduits'",
           "(6.1.5, (vi)) (checked on a crop)", "(6.1.5, (vii)) in the link text", "number", None, "high",
           r"{6.1.5, (vii)}", r"{6.1.5, (vi)}",
           "(6.1.5) has only (i)-(vi); (vi) is the statement on f_red used here."))
L.append(ITAL(113, "proof of (6.1.10): 'on peut supposer X et Y réduits;'", "réduits",
              r"$Y$ réduits~;", r"$Y$ \emph{réduits}~;", "Checked on a crop."))
L.append(C2(113, "proof of (6.1.10): 'sous-jacent \\overline{f(X)} (I, 5.2.1)'", "I", "5.2.1",
            r"$\overline{f(X)}$ (\hyperref[I.5.2.1-fr]{I, 5.2.1})", r"$\overline{f(X)}$ (\hyperref[I.5.2.1-fr]{\textbf{I}, 5.2.1})"))
L.append(F(113, "proof of (6.1.10): 'on sait que f se factorise en X->T-j->Y'",
           "X \\to T \\xrightarrow{j} Y: the first arrow carries no label (checked on a crop); the text then says 'que g est un morphisme entier'",
           "TeX silently adds the label g: X\\xrightarrow{g}T\\xrightarrow{j}Y", "misprint_in_print", None, "high",
           r"$X\xrightarrow{g}T\xrightarrow{j}Y$", r"$X\to T\xrightarrow{j}Y$",
           "g is used two lines later but never introduced in the print.",
           corrected=r"$X\xrightarrow{g}T\xrightarrow{j}Y$"))
L.append(C2(113, "proof of (6.1.10): 'le morphisme d'injection (I, 5.2.2)'", "I", "5.2.2"))
L.append(C2(113, "proof of (6.1.10): 'comme j est séparé (I, 5.5.1, (i))'", "I", "5.5.1, (i)"))
L.append(ITAL(113, "proof of (6.1.10): 'On peut donc supposer que f(X) est dense dans Y.'", "dense",
              r"dense dans $Y$. Enfin", r"\emph{dense} dans $Y$. Enfin",
              "Only this 'dense'; the later 'l'hypothèse que f(X) est dense dans Y' is roman. Checked on a crop."))
L.append(C2(113, "proof of (6.1.10): 'en outre A est réduit (I, 5.1.4)'", "I", "5.1.4"))
L.append(F(113, "proof of (6.1.10): 'A est réduit (I, 5.1.4) et l'hypothèse que'",
           "no comma after (I, 5.1.4) (checked on a crop)", "'), et l'hypothèse'", "punctuation", None, "high",
           r"), et l'hypothèse", r") et l'hypothèse", "Independent of the convention-2 edit of the same reference."))
L.append(ITAL(113, "proof of (6.1.10): 'l'homomorphisme φ: A->B correspondant à f est injectif (I, 1.2.7)'", "injectif",
              r"est<NL>injectif", r"est<NL>\emph{injectif}", "Checked on a crop."))
L.append(C2(113, "proof of (6.1.10): 'est injectif (I, 1.2.7)'", "I", "1.2.7"))
L.append(F(113, "proof of (6.1.10), end: 'le premier théorème de Cohen-Seidenberg ([13], t. I, p. 257, th. 3)'",
           "([13], t. I, p. 257, th. 3): the bracket closes after the number, the locator follows outside it",
           "(\\cite[t.~I, p.~257, th.~3]{I-13}), which prints '([13, t. I, p. 257, th. 3])'", "punctuation", None, "high",
           r"(\cite[t.~I, p.~257, th.~3]{I-13})", r"(\cite{I-13}, t.~I, p.~257, th.~3)",
           "Same treatment as the \\cite with optional argument on EGA I p. 148."))
L.append(ITAL(113, "proof of (6.1.11): 'O_X est un O_X-Module très ample relativement à f'", "très ample",
              r"Module très ample", r"Module \emph{très ample}", "Checked on a crop."))
L.append(ITAL(113, "proof of (6.1.11): 'f_*(O_X) est un O_Y-Module quasi-cohérent de type fini (6.1.2)'", "de type fini",
              r"Module quasi-cohérent de type fini", r"Module quasi-cohérent \emph{de type fini}", "Checked on a crop."))
L.append(F(113, "proof of (6.1.11), end: 'dans les conditions d'applications du critère (5.5.4, (i))'",
           "(5.5.4, (i)) (checked on a crop)", "(5.5.4, (ii)) in the link text", "number", None, "high",
           r"{5.5.4, (ii)}", r"{5.5.4, (i)}",
           "(5.5.4, (i)) is the criterion used here (f propre, L très ample relativement à f, f_*(L) de type fini => f projectif)."))
L.append(C2(113, "proof of Lemme (6.1.12.1): 'au moins un point fermé z'_i (0, 2.1.3)'", "0", "2.1.3"))
L.append(C2(113, "proof of Lemme (6.1.12.1): 'ayant Z pour espace sous-jacent (I, 5.2.1)'", "I", "5.2.1",
            r"sous-jacent (\hyperref[I.5.2.1-fr]{I, 5.2.1})", r"sous-jacent (\hyperref[I.5.2.1-fr]{\textbf{I}, 5.2.1})"))
L.append(F(113, "end of page: 'les s_i sont des éléments' / p. 114 'de M⊗_A(A/J)'",
           "the sentence runs on to p. 114 without a paragraph break",
           "blank line at the end of the segment, before \\oldpage[II]{114}, ends the paragraph",
           "other", None, "high", r"sont des éléments<NL><NL>", r"sont des éléments<NL>",
           "spurious paragraph break at the page marker (GLOBAL_ISSUES item 20); apply together with the p. 114 top-of-page fix."))

# ---------------- page 114 ----------------
L.append(F(114, "top of page: 'de M⊗_A(A/J) et sont donc images de r éléments'",
           "continues the sentence 'les s_i sont des éléments' from p. 113; line not indented, no new paragraph",
           "blank line after \\oldpage[II]{114} starts a new paragraph", "other", None, "high",
           r"\oldpage[II]{114}<NL><NL>de $M", r"\oldpage[II]{114}<NL>de $M",
           "spurious paragraph break at the page marker (GLOBAL_ISSUES item 20); apply together with the p. 113 end-of-page fix (blank line before the marker)."))
L.append(C2(114, "end of the proof of (6.1.12.1): 'O_Y^r|V_j -> E|V_j (0, 5.5.4)'", "0", "5.5.4"))
L.append(F(114, "Proposition (6.1.13): 'rationnelle partout définie (I, 7.2.1); alors'",
           "(I, 7.2.1) with bold I; the reference is upright inside the italic statement",
           "(\\hyperref[I.7.2.1-fr]{I, 7.2.1}) (plain I, italic in the proposition environment)", "convention", 2, "high",
           r"(\hyperref[I.7.2.1-fr]{I, 7.2.1})", r"\textup{(\hyperref[I.7.2.1-fr]{\textbf{I}, 7.2.1})}",
           "Bold I in the print; the reference is also upright inside the italic statement (convention 6), so the fix sets both. No separate convention-6 entry."))
L.append(ITAL(114, "after (6.1.13): 'lorsqu'on suppose en outre que Y est localement noethérien'", "localement noethérien",
              r"est localement noethérien,", r"est \emph{localement noethérien},", "Checked on a crop."))
L.append(C2(114, "after (6.1.13): 'Y est localement intègre (I, 6.1.13)'", "I", "6.1.13"))
L.append(ITAL(114, "proof of (6.1.13): 'dans la classe de g∘f un morphisme h: Y->X'", "morphisme",
              r"un morphisme $h:Y\to X$", r"un \emph{morphisme} $h:Y\to X$", "Checked on a crop."))
L.append(ITAL(114, "proof of (6.1.13): 'le morphisme g'=g_(Y): Y'->Y est entier (6.1.5, (iii))'", "entier",
              r":Y'\to Y$ est entier", r":Y'\to Y$ est \emph{entier}", "Checked on a crop."))
L.append(C2(114, "proof of (6.1.13): 'Y-sections rationnelles de Y' (I, 7.1.2)'", "I", "7.1.2"))
L.append(F(114, "Corollaire (6.1.14): 'g: X'->X un morphisme entier,'", "'entier' upright (roman) inside the italic statement",
           "'entier' italic (inside the \\itshape corollary environment)", "convention", 6, "high",
           r"morphisme<NL>entier, $f$", r"morphisme<NL>\textup{entier}, $f$", "Checked on a crop."))
L.append(C2(114, "proof of (6.1.14): 'un ouvert U de X dans X' (I, 7.2.2)'", "I", "7.2.2"))
L.append(C2(114, "proof of (6.1.14): 'immersion fermée de U dans g^{-1}(U) (I, 5.4.6)'", "I", "5.4.6"))
L.append(C2(114, "proof of (6.1.14): 'associé à f (I, 4.2.1)'", "I", "4.2.1"))
L.append(C2(114, "proof of (6.1.14): 'l'adhérence Z̄ de Z dans X' (I, 5.2.1)'", "I", "5.2.1"))
L.append(C2(114, "proof of (6.1.14): 'induit sur un ouvert de X_1 (I, 5.2.3)'", "I", "5.2.3"))
L.append(F(114, "Corollaire (6.1.15): 'g: X'->X un morphisme entier.'", "'entier' upright (roman) inside the italic statement",
           "'entier' italic (inside the \\itshape corollary environment)", "convention", 6, "high",
           r"un morphisme entier. S'il", r"un morphisme \textup{entier}. S'il", "Checked on a crop."))
L.append(C2(114, "proof of (6.1.15): 'en vertu de (I, 8.2.1.1)'", "I", "8.2.1.1"))

# ---------------- checks ----------------
ok = True
pages = {}
for p in (110, 111, 112, 113, 114):
    t = (RUN / f"page_{p}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    pages[p] = t
sim = dict(pages)
for x in L:
    if x["fix"] is None:
        continue
    p, old, new = x["page"], x["fix"]["old"], x["fix"]["new"]
    n0 = pages[p].count(old)
    n1 = sim[p].count(old)
    if n0 != 1 or n1 != 1:
        ok = False
        print("NOT UNIQUE", p, n0, n1, repr(old))
    else:
        sim[p] = sim[p].replace(old, new)
json.dump(L, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
from collections import Counter
c = Counter()
for x in L:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    c[(x["page"], k)] += 1
for p in (110, 111, 112, 113, 114):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("all unique" if ok else "PROBLEMS", len(L))
