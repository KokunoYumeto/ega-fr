"""Build findings_143_147.json, check every fix against the page copies, and simulate the sequential
application (as apply_fixes.py does) on an in-memory copy of the diplomatic ega3-1-fr.tex. Writes only the JSON."""
import json
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
RUN = E / "run_III1"
OUT = RUN / "findings_143_147.json"
DIP = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega3\ega3-1-fr.tex"
MARK = re.compile(r"\\oldpage\[III\]\{(\d+)\}")

F = []


def add(page, where, scan, tex, kind, fix, note, convention=None, confidence="high", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=convention,
             confidence=confidence, fix=fix)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


def conv2(page, where, ref, old=None, new=None, note=None):
    old = old or ref
    new = new or ref.replace("(II,", r"(\textbf{II},").replace("(I,", r"(\textbf{I},").replace(
        r"(0\textsubscript{I},", r"(\textbf{0}\textsubscript{I},").replace("(0,", r"(\textbf{0},")
    numeral = "0" if ref.startswith("(0") else ("II" if "II," in ref else "I")
    add(page, where, f"{ref} with a bold {numeral}", ref, "convention",
        fx(old, new), note or "Bold chapter numeral in the reference.", convention=2)


# ---------------------------------------------------------------- page 143
# (the two-step move of \oldpage[III]{143} is appended at the end of the list)
add(143, "1st paragraph: 'on peut donc déjà supposer que le morphisme f est fini'",
    "'fini' in italics", "upright", "italics",
    fx(r"le morphisme $f$ est fini, donc que", r"le morphisme $f$ est \emph{fini}, donc que"),
    "Enlarged crop.")
conv2(143, "1st paragraph: 'le morphisme f correspondant (II, 1.2.7)'", "(II, 1.2.7)")
conv2(143, "1st paragraph: 'le faisceau Coker u étant cohérent (0_I, 5.3.4 et 5.2.2)'",
      r"(0\textsubscript{I}, 5.3.4 et 5.2.2)")
add(143, "1st paragraph: 'correspond à l'homomorphisme v = u⊗1 : O_Y⊗_{O_Z}k(z)→B⊗_{O_Z}k(z), et l'hypothèse'",
    "formula inline in the text line; k bold italic in both k(z)",
    "displayed with \\[ ... \\]; plain k", "other",
    fx(r"""l'homomorphisme
\[
v=u\otimes1:
\mathcal O_Y\otimes_{\mathcal O_Z}k(z)
\longrightarrow
\mathcal B\otimes_{\mathcal O_Z}k(z),
\]
et l'hypothèse""",
       r"""l'homomorphisme
$v=u\otimes1:
\mathcal O_Y\otimes_{\mathcal O_Z}\boldsymbol{k}(z)
\longrightarrow
\mathcal B\otimes_{\mathcal O_Z}\boldsymbol{k}(z)$,
et l'hypothèse"""),
    "One edit for the inline setting and the two convention-1 findings below. Crop: the subscript of O under ⊗ is "
    "a roman capital Z here (O_Z), as in the TeX.")
for which in ("first", "second"):
    add(143, f"same formula, {which} k(z)", "bold italic k", "k(z)", "convention", None,
        "Covered by the edit of the preceding 'other' finding.", convention=1)
add(143, "1st paragraph: 'l'homomorphisme u_y⊗1 : O_y⊗_{O_z}k(z)→B_y⊗_{O_z}k(z) est surjectif'",
    "formula inline in the text line; k bold italic in both k(z)",
    "displayed with \\[ ... \\]; plain k", "other",
    fx(r"""l'homomorphisme
\[
u_y\otimes1:
\mathcal O_y\otimes_{\mathcal O_z}k(z)
\longrightarrow
\mathcal B_y\otimes_{\mathcal O_z}k(z)
\]
est surjectif.""",
       r"""l'homomorphisme
$u_y\otimes1:
\mathcal O_y\otimes_{\mathcal O_z}\boldsymbol{k}(z)
\longrightarrow
\mathcal B_y\otimes_{\mathcal O_z}\boldsymbol{k}(z)$
est surjectif."""),
    "One edit for the inline setting and the two convention-1 findings below. Crop: lower-case italic z under O "
    "here (O_z), as in the TeX.")
for which in ("first", "second"):
    add(143, f"same formula, {which} k(z)", "bold italic k", "k(z)", "convention", None,
        "Covered by the edit of the preceding 'other' finding.", convention=1)
add(143, "2nd paragraph: '(ii) Le même raisonnement que ci-dessus'",
    "'(ii)' upright (roman)", "\\textit{(ii)} (italic) in the proof", "italics",
    fx(r"\noindent\textit{(ii)} Le même", r"\noindent (ii) Le même"),
    "Enlarged crop. The same \\textit{(i)} opens this part of the proof on p. 142.")
add(143, "Lemme (4.6.7.1): 'et que u⊗1 : N⊗_A k→M⊗_A k (où k est le corps résiduel de A) est injectif'",
    "formula inline in the text line", "displayed with \\[ ... \\]", "other",
    fx(r"""de type fini et que
\[
u\otimes1:N\otimes_Ak\longrightarrow M\otimes_Ak
\]
(où $k$""",
       r"""de type fini et que
$u\otimes1:N\otimes_Ak\longrightarrow M\otimes_Ak$
(où $k$"""),
    "")
add(143, "proof of (4.6.7.1): 'pour tout couple de A-modules de type fini P, Q'",
    "'de type fini' in italics", "upright", "italics",
    fx(r"$A$-modules de type fini $P$, $Q$", r"$A$-modules \emph{de type fini} $P$, $Q$"),
    "Enlarged crop.")
add(143, "proof of (4.6.7.1): 'la topologie définie par cette filtration est donc séparée'",
    "'séparée' in italics", "upright", "italics",
    fx(r"est donc séparée,", r"est donc \emph{séparée},"), "Enlarged crop.")
conv2(143, "proof of (4.6.7.1): 'P un A-module de type fini (0_I, 7.3.5)'", r"(0\textsubscript{I}, 7.3.5)")
add(143, "proof of (4.6.7.1): 'l'homomorphisme gr(u⊗1_P) : gr.(N⊗_AP)→gr.(M⊗_AP) (où les modules'",
    "formula inline in the text line", "displayed with \\[ ... \\]", "other",
    fx(r"""l'homomorphisme
\[
\operatorname{gr}(u\otimes1_P):
\operatorname{gr}_\bullet(N\otimes_AP)
\longrightarrow
\operatorname{gr}_\bullet(M\otimes_AP)
\]
(où les modules""",
       r"""l'homomorphisme
$\operatorname{gr}(u\otimes1_P):
\operatorname{gr}_\bullet(N\otimes_AP)
\longrightarrow
\operatorname{gr}_\bullet(M\otimes_AP)$
(où les modules"""),
    "")
add(143, "proof of (4.6.7.1): '(Bourbaki, Alg. comm., chap. III, § 2, n° 8, cor. 1 du th. 1)'",
    "n with a raised o (n°)", "no~8 (plain 'no')", "symbol",
    fx(r"no~8", r"n\textsuperscript{o}~8"),
    "Enlarged crop. ega3-1-fr.tex writes n\\textsuperscript{o} elsewhere (13 times); 'no~' only here and in "
    "'no~3' on p. 142.")
add(143, "proof of (4.6.7.1): 'les homomorphismes M⊗_A(m^nP)→m^n(M⊗_AP) sont bijectifs'",
    "formula inline in the text line", "displayed with \\[ ... \\]", "other",
    fx(r"""homomorphismes
\[
M\otimes_A(\mathfrak m^nP)
\longrightarrow
\mathfrak m^n(M\otimes_AP)
\]
sont bijectifs""",
       r"""homomorphismes
$M\otimes_A(\mathfrak m^nP)
\longrightarrow
\mathfrak m^n(M\otimes_AP)$
sont bijectifs"""),
    "The following φ_M formula is displayed in the print too.")

# ---------------------------------------------------------------- page 144
add(144, "proof of (4.6.7.1): 'et comme gr_0(N)⊗_A gr.(P) = gr_0(N)⊗_k gr.(P), gr_0(M)⊗_A gr.(P) = "
         "gr_0(M)⊗_k gr.(P), gr_0(u)⊗1 est aussi injectif'",
    "both equalities inline in the text line", "displayed (\\[ \\begin{split} ... \\])", "other",
    fx(r"""et comme
\[
\begin{split}
\operatorname{gr}_0(N)\otimes_A\operatorname{gr}_\bullet(P)
&=\operatorname{gr}_0(N)\otimes_k\operatorname{gr}_\bullet(P),\\
\operatorname{gr}_0(M)\otimes_A\operatorname{gr}_\bullet(P)
&=\operatorname{gr}_0(M)\otimes_k\operatorname{gr}_\bullet(P),
\end{split}
\]
$\operatorname{gr}_0(u)\otimes1$ est aussi injectif.""",
       r"""et comme
$\operatorname{gr}_0(N)\otimes_A\operatorname{gr}_\bullet(P)
=\operatorname{gr}_0(N)\otimes_k\operatorname{gr}_\bullet(P)$,
$\operatorname{gr}_0(M)\otimes_A\operatorname{gr}_\bullet(P)
=\operatorname{gr}_0(M)\otimes_k\operatorname{gr}_\bullet(P)$,
$\operatorname{gr}_0(u)\otimes1$ est aussi injectif."""),
    "")
add(144, "Proposition (4.6.8): 'ses images réciproques, X^ = X_{/X'}, Y^ = Y_{/Y'}, Z^ = Z_{/Z'} les complétés formels'",
    "the three formulas inline in the text line", "displayed with \\[ ... \\]", "other",
    fx(r"""réciproques,
\[
\widehat X=X_{/X'},\qquad
\widehat Y=Y_{/Y'},\qquad
\widehat Z=Z_{/Z'}
\]
les complétés""",
       r"""réciproques,
$\widehat X=X_{/X'}$, $\widehat Y=Y_{/Y'}$, $\widehat Z=Z_{/Z'}$
les complétés"""),
    "")
add(144, "Proposition (4.6.8): 'Pour que f^ soit un isomorphisme (resp. une immersion fermée)'",
    "'(resp.' upright inside the italic statement", "italic (statement environment)", "convention",
    fx(r"""isomorphisme (resp.
une immersion fermée), il faut""", r"""isomorphisme (\textup{resp.}
une immersion fermée), il faut"""),
    "Enlarged crop.", convention=6)
add(144, "Proposition (4.6.8), end: 'soit un isomorphisme (resp. une immersion fermée).'",
    "'(resp.' upright inside the italic statement", "italic (statement environment)", "convention",
    fx(r"""soit un isomorphisme (resp. une immersion fermée).
\end{proposition}""", r"""soit un isomorphisme (\textup{resp.} une immersion fermée).
\end{proposition}"""),
    "Enlarged crop.", convention=6)
conv2(144, "proof of (4.6.8): 'La suffisance de la condition est immédiate (I, 10.14.7)'", "(I, 10.14.7)")
add(144, "proof of (4.6.8): 'Par hypothèse (I, 10.9.1 et 10.14.2) la fibre'",
    "(I, 10.9.1 et 10.14.2) with a light roman I (wrong fount; every other chapter numeral on pp. 143-147 is bold)",
    "(I, 10.9.1 et 10.14.2) with plain I (printed reading kept)", "misprint_in_print", None,
    "Enlarged crop: the I is a light roman capital, unlike the bold I of (I, 10.14.7) four lines above and the "
    "bold II of (II, 5.4.3) on the next line. The TeX keeps the printed reading; do not bold it in a "
    "convention-2 pass.",
    confidence="medium", corrected=r"(\textbf{I}, 10.9.1 et 10.14.2)")
conv2(144, "proof of (4.6.8): 'donc comme f est propre (II, 5.4.3)'", "(II, 5.4.3)")
add(144, "proof of (4.6.8): 'la restriction f^{-1}(U)→U de f soit un morphisme fini (4.4.11)'",
    "'fini' in italics", "upright", "italics",
    fx(r"morphisme fini (\hyperref[III.4.4.11-fr]{4.4.11})", r"morphisme \emph{fini} (\hyperref[III.4.4.11-fr]{4.4.11})"),
    "Enlarged crop.")
add(144, "proof of (4.6.8): 'où B est une A-algèbre finie sur A'", "'finie' in italics", "upright", "italics",
    fx(r"algèbre finie sur $A$", r"algèbre \emph{finie} sur $A$"), "Enlarged crop.")
add(144, "proof of (4.6.8): 'on a alors Y^ = Spf(A^), X^ = Spf(B^), A^ étant'",
    "both formulas inline in the text line", "displayed with \\[ ... \\]", "other",
    fx(r"""on a alors
\[
\widehat Y=\operatorname{Spf}(\widehat A),\qquad
\widehat X=\operatorname{Spf}(\widehat B),
\]
$\widehat A$ étant""",
       r"""on a alors
$\widehat Y=\operatorname{Spf}(\widehat A)$, $\widehat X=\operatorname{Spf}(\widehat B)$,
$\widehat A$ étant"""),
    "")
conv2(144, "proof of (4.6.8): 'est surjectif (resp. bijectif) (I, 10.14.2). Or,'", "(I, 10.14.2)")
conv2(144, "proof of (4.6.8): 'on sait alors (I, 10.8.14)'", "(I, 10.8.14)")

# ---------------------------------------------------------------- page 145
add(145, "Théorème (4.7.1): 'X_y = X⊗_Y k(y) = f^{-1}(y)'", "bold italic k", "k(y)", "convention",
    fx(r"X\otimes_Yk(y)", r"X\otimes_Y\boldsymbol{k}(y)"), "", convention=1)
add(145, "Théorème (4.7.1): 'L_y = g^*(L) = L⊗_{O_Y} k(y)'", "bold italic k", "k(y)", "convention",
    fx(r"\mathcal L\otimes_{\mathcal O_Y}k(y)", r"\mathcal L\otimes_{\mathcal O_Y}\boldsymbol{k}(y)"), "", convention=1)
add(145, "proof of (4.7.1): 'I) Posons'", "'I)' upright (roman)", "\\textit{I)} (italic) in the proof", "italics",
    fx(r"\noindent\textit{I)} Posons", r"\noindent I) Posons"), "Enlarged crop.")
add(145, "proof of (4.7.1): 'Posons Y' = Spec(O_y), X' = X×_Y Y', et soit L' = L⊗_{O_Y}O_y; nous allons'",
    "'et soit' before L' = ...; the formulas inline in the text line",
    "no 'et soit' (three formulas in a display separated by \\qquad)", "missing",
    fx(r"""Posons
\[
Y'=\operatorname{Spec}(\mathcal O_y),\qquad
X'=X\times_YY',\qquad
\mathcal L'=\mathcal L\otimes_{\mathcal O_Y}\mathcal O_y~;
\]
nous allons""",
       r"""Posons
$Y'=\operatorname{Spec}(\mathcal O_y)$, $X'=X\times_YY'$, et soit
$\mathcal L'=\mathcal L\otimes_{\mathcal O_Y}\mathcal O_y$~;
nous allons"""),
    "Enlarged crop. The edit also sets the formulas inline as printed.")
add(145, "proof of (4.7.1): 'prouver que L' est ample pour f' = f_{(Y')}'", "'ample pour' in italics", "upright",
    "italics", fx(r"""$\mathcal L'$ est ample pour
$f'=f_{(Y')}$""", r"""$\mathcal L'$ est \emph{ample pour}
$f'=f_{(Y')}$"""), "Enlarged crop.")
add(145, "diagram: 'Spec(k(y))'", "bold italic k", "k(y)", "convention",
    fx(r"\operatorname{Spec}(k(y))\ar[l]", r"\operatorname{Spec}(\boldsymbol{k}(y))\ar[l]"), "", convention=1)
conv2(145, "proof of (4.7.1): 'Comme f' est propre (II, 5.4.2, (iii)) et O_y noethérien'", "(II, 5.4.2, (iii))",
      old=r"(II, 5.4.2, (iii)) et $\mathcal O_y$", new=r"(\textbf{II}, 5.4.2, (iii)) et $\mathcal O_y$")
conv2(145, "proof of (4.7.1): 'prouver que L est ample pour f (II, 4.6.6)'", "(II, 4.6.6)")
add(145, "proof of (4.7.1): 'Nous allons appliquer le critère (2.6.1, c))'", "letter 'c)' in italics", "upright 'c)'",
    "italics", fx(r"{2.6.1, c)})", r"{2.6.1, \emph{c)}})"),
    "Enlarged crop. Form \\emph{c)} as elsewhere in ega3-1-fr.tex.")
add(145, "proof of (4.7.1): 'H^1(X, F(n)) = 0 pour tout n≥N, avec F(n) = F⊗L^{⊗n}. Notons que'",
    "'avec' before F(n) = ...; the formulas inline in the text line",
    "no 'avec' (\\qquad in a display)", "missing",
    fx(r"""tel que
\[
H^1(X,\mathcal F(n))=0\quad\text{pour tout }n\geq N,
\qquad
\mathcal F(n)=\mathcal F\otimes\mathcal L^{\otimes n}.
\]
Notons que""",
       r"""tel que
$H^1(X,\mathcal F(n))=0$ pour tout $n\geq N$, avec
$\mathcal F(n)=\mathcal F\otimes\mathcal L^{\otimes n}$.
Notons que"""),
    "Enlarged crop. The edit also sets the formulas inline as printed.")
conv2(145, "proof of (4.7.1): 'de O_X (I, 4.4.5), et g l'injection canonique'", "(I, 4.4.5)")
add(145, "proof of (4.7.1): 'X_y est donc un sous-préschéma fermé de X défini par l'Idéal cohérent'",
    "'par' set in bold (wrong fount)", "roman 'par' (silently corrected)", "misprint_in_print",
    fx(r"défini par l'Idéal cohérent", r"défini \textbf{par} l'Idéal cohérent"),
    "Crop at 3x and ink count: the 'a' of 'par' has about 38% more ink than the 'a' of 'l'Idéal' beside it; the X "
    "before 'défini' has normal weight. Typographical slip; medium only on whether a wrong fount is reproduced.",
    confidence="medium", corrected="défini par l'Idéal cohérent")
add(145, "proof of (4.7.1): 'Considérons alors la k(y)-algèbre graduée'", "bold italic k", "k(y)", "convention",
    fx(r"la $k(y)$-algèbre graduée", r"la $\boldsymbol{k}(y)$-algèbre graduée"), "", convention=1)
add(145, "proof of (4.7.1): 'S = gr(O_y) = ⊕_{j≥0} m^j/m^{j+1}, qui est de type fini'",
    "formula inline in the text line", "displayed with \\[ ... \\]", "other",
    fx(r"""graduée
\[
S=\operatorname{gr}(\mathcal O_y)
=\bigoplus_{j\geq0}\mathfrak m^j/\mathfrak m^{j+1},
\]
qui est""",
       r"""graduée
$S=\operatorname{gr}(\mathcal O_y)
=\bigoplus_{j\geq0}\mathfrak m^j/\mathfrak m^{j+1}$,
qui est"""),
    "")
add(145, "proof of (4.7.1): 'Posons d'autre part, M_j = m^jF/m^{j+1}F et M = ⊕_{j≥0} M_j = gr(F); comme'",
    "'et' between the two formulas; the formulas inline in the text line",
    "comma and \\qquad instead of 'et' (display)", "missing",
    fx(r"""Posons d'autre part
\[
\mathcal M_j=\mathfrak m^j\mathcal F/\mathfrak m^{j+1}\mathcal F,
\qquad
\mathcal M=\bigoplus_{j\geq0}\mathcal M_j
=\operatorname{gr}(\mathcal F)~;
\]
comme""",
       r"""Posons d'autre part,
$\mathcal M_j=\mathfrak m^j\mathcal F/\mathfrak m^{j+1}\mathcal F$ et
$\mathcal M=\bigoplus_{j\geq0}\mathcal M_j
=\operatorname{gr}(\mathcal F)$~;
comme"""),
    "Enlarged crop. One edit for 'et', the comma after 'part' (next finding) and the inline setting.")
add(145, "same place: 'Posons d'autre part,'", "comma after 'part'", "no comma", "punctuation", None,
    "Covered by the edit of the preceding finding.")
conv2(145, "proof of (4.7.1): 'M est un S-Module quasi-cohérent de type fini (0, 10.1.1)'", "(0, 10.1.1)")
add(145, "proof of (4.7.1): 'si l'on pose M'_j = g^*(M_j), M' = g^*(M) = ⊕_{j≥0} M'_j est un S_y-Module gradué'",
    "'... = ⊕ M'_j est un S_y-Module': no comma and no second M' before 'est un'; formulas inline",
    "', \\] $\\mathcal M'$ est un' (comma and an added M')", "extra",
    fx(r"""si l'on pose
\[
\mathcal M'_j=g^*(\mathcal M_j),\qquad
\mathcal M'=g^*(\mathcal M)=\bigoplus_{j\geq0}\mathcal M'_j,
\]
$\mathcal M'$ est un""",
       r"""si l'on pose
$\mathcal M'_j=g^*(\mathcal M_j)$, $\mathcal M'=g^*(\mathcal M)=\bigoplus_{j\geq0}\mathcal M'_j$
est un"""),
    "Enlarged crop: the printed sentence runs '... = ⊕_{j≥0} M'_j est un S_y-Module gradué'. The edit also sets "
    "the formulas inline as printed.")
add(145, "proof of (4.7.1): 'on a M'_j(n) = g^*((M_j(n))). Cela étant'",
    "g^*((M_j(n))): doubled parentheses around M_j(n)", "g^*(\\mathcal M_j(n)) (silently corrected)",
    "misprint_in_print",
    fx(r"$\mathcal M'_j(n)=g^*(\mathcal M_j(n))$", r"$\mathcal M'_j(n)=g^*((\mathcal M_j(n)))$"),
    "Enlarged crop: two opening and three closing parentheses after g^*. The fix restores the printed reading.",
    corrected=r"\mathcal M'_j(n)=g^*(\mathcal M_j(n))")
conv2(145, "proof of (4.7.1): 'f_y est propre (II, 5.4.2, (iii)) et L_y est ample'", "(II, 5.4.2, (iii))",
      old=r"(II, 5.4.2, (iii)) et $\mathcal L_y$", new=r"(\textbf{II}, 5.4.2, (iii)) et $\mathcal L_y$")
add(145, "proof of (4.7.1): 'donc f_y est projectif'", "'projectif' in italics", "upright", "italics",
    fx(r"donc $f_y$ est projectif", r"donc $f_y$ est \emph{projectif}"), "Enlarged crop.")
conv2(145, "proof of (4.7.1): '(II, 5.5.4 et 4.6.11)'", "(II, 5.5.4 et 4.6.11)")
add(145, "proof of (4.7.1): 'appliquer à Spec(k(y)), f_y, S_y, L_y et M''", "bold italic k", "k(y)", "convention",
    fx(r"$\operatorname{Spec}(k(y))$, $f_y$", r"$\operatorname{Spec}(\boldsymbol{k}(y))$, $f_y$"), "", convention=1)
add(145, "proof of (4.7.1): 'H^q(X_y, M'_j(n)) = 0 pour tout q>0 et tout j; par suite'",
    "'et tout' in italics (the 'pour tout' before it is roman)", "upright", "italics",
    fx(r"pour tout $q>0$ et tout $j$~; par suite", r"pour tout $q>0$ \emph{et tout} $j$~; par suite"),
    "Enlarged crop. In the next line 'pour tout q>0 et tout j (G, II, 4.9.1)' is roman throughout, as in the TeX.")
add(145, "proof of (4.7.1): 'Posons alors F(n)_j = F(n)/m^{j+1}F(n), de sorte que'",
    "formula inline in the text line", "displayed with \\[ ... \\]", "other",
    fx(r"""Posons alors
\[
\mathcal F(n)_j=\mathcal F(n)/\mathfrak m^{j+1}\mathcal F(n),
\]
de sorte que""",
       r"""Posons alors
$\mathcal F(n)_j=\mathcal F(n)/\mathfrak m^{j+1}\mathcal F(n)$,
de sorte que"""),
    "")

# ---------------------------------------------------------------- page 146
add(146, "page start: marker \\oldpage[III]{146}",
    "printed p. 145 ends with 'II) Revenons aux notations du début de la démonstration, et remarquons qu'on'; "
    "p. 146 begins 'peut toujours supposer Y = Spec(A) affine'",
    "\\oldpage[III]{146} stands before 'II) Revenons'", "marker",
    fx(r"""\oldpage[III]{146}

\noindent\textit{II)} Revenons aux notations du début de la démonstration,
et remarquons qu'on peut toujours""",
       r"""\noindent II) Revenons aux notations du début de la démonstration,
et remarquons qu'on
\oldpage[III]{146}
peut toujours"""),
    "The blank line before 'II)' (end of the p. 145 segment) stays: 'II) Revenons' begins an indented paragraph. "
    "The edit also sets 'II)' upright (next finding).")
add(146, "same place (printed on p. 145): 'II) Revenons'", "'II)' upright (roman)", "\\textit{II)} (italic)",
    "italics", None, "Covered by the edit of the preceding marker finding.")
add(146, "1st paragraph: 'soit très ample pour f' (II, 4.6.11)'",
    "(II, 4.6.11): the first I bold, the second a light roman I (wrong fount)", "(II, 4.6.11)",
    "misprint_in_print", fx(r"(II, 4.6.11)", r"(\textbf{I}I, 4.6.11)"),
    "Crop at 5x and ink count: the second I is 12 px wide with 184 dark pixels, the first (bold) I 17 px with 349; "
    "thin serifs, as the light I of (I, 10.9.1 ...) on p. 144. The edit also applies convention 2 to the first I. "
    "If a damaged bold I is assumed instead, use (\\textbf{II}, 4.6.11).",
    confidence="medium", corrected=r"(\textbf{II}, 4.6.11)")
add(146, "1st paragraph: 'le cas où L' est très ample pour f''", "'très ample' in italics", "upright", "italics",
    fx(r"$\mathcal L'$ est très ample pour $f'$, et à prouver",
       r"$\mathcal L'$ est \emph{très ample} pour $f'$, et à prouver"),
    "Enlarged crop. The other two 'très ample' on the page are roman, as in the TeX.")
add(146, "1st paragraph: 'il existe alors une Y'-immersion fermée j : X'→P = P^r_{Y'}'", "'fermée' in italics",
    "upright", "italics", fx(r"une $Y'$-immersion fermée", r"une $Y'$-immersion \emph{fermée}"),
    "Enlarged crop. The P of P^r_{Y'} is bold upright here, matching \\mathbf P.")
conv2(146, "1st paragraph: 'isomorphe à j^*(O_P(1)) (II, 5.5.4, (ii))'", "(II, 5.5.4, (ii))")
add(146, "1st paragraph: 'un O_{X'}-homomorphisme surjectif u : O_{X'}^{r+1}→L' (II, 4.2.3)'",
    "'surjectif' in italics; the formula inline in the text line", "upright 'surjectif'; formula displayed",
    "italics",
    fx(r"""homomorphisme
surjectif
\[
u:\mathcal O_{X'}^{r+1}\longrightarrow\mathcal L'
\]
""",
       r"""homomorphisme
\emph{surjectif}
$u:\mathcal O_{X'}^{r+1}\longrightarrow\mathcal L'$
"""),
    "Enlarged crop. The edit also sets the formula inline as printed.")
conv2(146, "1st paragraph: '→L' (II, 4.2.3). Ce dernier'", "(II, 4.2.3)",
      old=r"(II, 4.2.3). Ce dernier", new=r"(\textbf{II}, 4.2.3). Ce dernier")
conv2(146, "1st paragraph: 'Ce dernier correspond (0_I, 5.1.1)'", r"(0\textsubscript{I}, 5.1.1)")
add(146, "1st paragraph: 'on a f'_*(L') = f_*(L)⊗_{O_Y}O_{Y'} (0_I, 5.4.10), Y est affine'",
    "formula inline in the text line", "displayed with \\[ ... \\]", "other",
    fx(r"""on a
\[
f'_*(\mathcal L')=f_*(\mathcal L)\otimes_{\mathcal O_Y}\mathcal O_{Y'}
\]
""",
       r"""on a
$f'_*(\mathcal L')=f_*(\mathcal L)\otimes_{\mathcal O_Y}\mathcal O_{Y'}$
"""),
    "")
conv2(146, "1st paragraph: '(0_I, 5.4.10), Y est affine'", r"(0\textsubscript{I}, 5.4.10)")
conv2(146, "1st paragraph: '(on rappelle que l'espace Y' est contenu dans V, cf. I, 2.4.2)'", "cf. I, 2.4.2",
      old="cf. I,\n2.4.2)", new="cf. \\textbf{I},\n2.4.2)")
add(146, "1st paragraph: 'un homomorphisme v : (O_X|f^{-1}(V))^{r+1}→L|f^{-1}(V) qui, par hypothèse'",
    "formula inline in the text line", "displayed with \\[ ... \\]", "other",
    fx(r"""un homomorphisme
\[
v:\bigl(\mathcal O_X|f^{-1}(V)\bigr)^{r+1}
\longrightarrow\mathcal L|f^{-1}(V)
\]
qui, par hypothèse""",
       r"""un homomorphisme
$v:\bigl(\mathcal O_X|f^{-1}(V)\bigr)^{r+1}
\longrightarrow\mathcal L|f^{-1}(V)$
qui, par hypothèse"""),
    "")
conv2(146, "1st paragraph: 'Coker (v) est cohérent (0_I, 5.3.4)'", r"(0\textsubscript{I}, 5.3.4)")
conv2(146, "1st paragraph: 'son support est fermé (0_I, 5.2.2)'", r"(0\textsubscript{I}, 5.2.2)")
add(146, "1st paragraph: 'la restriction de v à W soit un homomorphisme surjectif.'", "'surjectif' in italics",
    "upright", "italics",
    fx(r"soit un homomorphisme surjectif. Puisque", r"soit un homomorphisme \emph{surjectif}. Puisque"),
    "Enlarged crop.")
conv2(146, "end of the proof of (4.7.1): 'la conclusion résulte alors de (II, 4.2.3).'", "(II, 4.2.3)",
      old="(II, 4.2.3).\n\\end{proof}", new="(\\textbf{II}, 4.2.3).\n\\end{proof}")
add(146, "Proposition (4.8.1) a): 'le morphisme f_0 : (X, O_X/J)→(Y, O_Y/K) déduit de f est fini'",
    "formula inline in the text line", "displayed with \\[ ... \\]", "other",
    fx(r"""le morphisme
  \[
  f_0:(\mathfrak X,\mathcal O_{\mathfrak X}/\mathcal J)
  \longrightarrow
  (\mathfrak Y,\mathcal O_{\mathfrak Y}/\mathcal K)
  \]
  déduit de $f$ est fini.""",
       r"""le morphisme
  $f_0:(\mathfrak X,\mathcal O_{\mathfrak X}/\mathcal J)
  \longrightarrow
  (\mathfrak Y,\mathcal O_{\mathfrak Y}/\mathcal K)$
  déduit de $f$ est fini."""),
    "")
conv2(146, "Proposition (4.8.1) a): 'f est un morphisme adique (I, 10.12.1)'", "(I, 10.12.1)",
      new=r"\textup{(\textbf{I}, 10.12.1)}",
      note="One edit for this finding and the next (convention 6): bold numeral and the upright reference together.")
add(146, "same reference '(I, 10.12.1)'", "the reference is upright inside the italic statement",
    "italic (statement environment)", "convention", None,
    "Covered by the edit of the preceding finding (convention 2), which adds the \\textup.", convention=6)
add(146, "proof of (4.8.1): 'Il est immédiat que a) entraîne b)'", "letters 'a)' and 'b)' in italics",
    "upright", "italics",
    fx(r"Il est immédiat que a) entraîne b) en vertu", r"Il est immédiat que \emph{a)} entraîne \emph{b)} en vertu"),
    "Enlarged crop. Form \\emph{a)} as elsewhere in ega3-1-fr.tex.")
conv2(146, "proof of (4.8.1): 'en vertu de (I, 10.12.3)'", "(I, 10.12.3)")
add(146, "proof of (4.8.1): 'Pour voir que b) entraîne c)'", "letters 'b)' and 'c)' in italics", "upright",
    "italics", fx(r"""Pour voir que b)
entraîne c), on peut""", r"""Pour voir que \emph{b)}
entraîne \emph{c)}, on peut"""), "Enlarged crop.")
conv2(146, "proof of (4.8.1): 'B/R-module de type fini (II, 6.1.3)'", "(II, 6.1.3)")
conv2(146, "proof of (4.8.1): 'En vertu de (I, 5.1.9)'", "(I, 5.1.9)")
add(146, "proof of (4.8.1): 'l'hypothèse b) entraîne'", "letter 'b)' in italics", "upright", "italics",
    fx(r"""l'hypothèse b)
entraîne""", r"""l'hypothèse \emph{b)}
entraîne"""), "Enlarged crop.")
add(146, "proof of (4.8.1): 'où A = lim_{←, n} A_n'", "lim with the arrow and the index n below it",
    "\\varprojlim A_n (no index)", "formula", fx(r"\varprojlim A_n", r"\varprojlim_n A_n"), "Enlarged crop.")
conv2(146, "proof of (4.8.1): 'on conclut en vertu de (0_I, 7.2.9)'", r"(0\textsubscript{I}, 7.2.9)")
add(146, "last line: 'Enfin, pour prouver que c)'", "letter 'c)' in italics; the sentence runs on to p. 147",
    "upright 'c)', followed by a blank line before \\oldpage[III]{147} (paragraph break)", "italics",
    fx(r"""Enfin, pour prouver que c)

""", r"""Enfin, pour prouver que \emph{c)}
"""),
    "Enlarged crop. The edit also removes the blank line before \\oldpage[III]{147}; the p. 147 'other' finding "
    "removes the one after it. Apply both.")

# ---------------------------------------------------------------- page 147
add(147, "page start: '\\oldpage[III]{147}' followed by a blank line",
    "'entraîne a), on peut ...' continues the sentence of p. 146 ('pour prouver que c)')",
    "blank line after the marker (paragraph break)", "other",
    fx(r"""\oldpage[III]{147}

entraîne""", r"""\oldpage[III]{147}
entraîne"""),
    "Goes with the p. 146 edit that removes the blank line before the marker. Apply both.")
add(147, "proof of (4.8.1): 'entraîne a), on peut se borner'", "letter 'a)' in italics", "upright", "italics",
    fx(r"entraîne a), on peut se borner", r"entraîne \emph{a)}, on peut se borner"), "Enlarged crop.")
add(147, "proof of (4.8.1): 'on peut se borner encore au cas Y = Spf(B), X = Spf(A)'",
    "'au cas' followed directly by the formula (no 'où')", "'au cas où'", "extra",
    fx(r"""au cas où
$\mathfrak Y=\operatorname{Spf}(B)$""", r"""au cas
$\mathfrak Y=\operatorname{Spf}(B)$"""),
    "Enlarged crop.")
conv2(147, "proof of (4.8.1): 'il résulte de (I, 10.10.9)'", "(I, 10.10.9)")
add(147, "proof of (4.8.1): 'que les conditions de a) sont satisfaites'", "letter 'a)' in italics", "upright",
    "italics", fx(r"de a) sont satisfaites", r"de \emph{a)} sont satisfaites"), "Enlarged crop.")
add(147, "Définition (4.8.2): 'les propriétés équivalentes a), b), c) de (4.8.1)'",
    "'a), b), c)' upright inside the italic statement", "italic (definition environment)", "convention",
    fx(r"équivalentes a), b), c) de", r"équivalentes \textup{a), b), c)} de"), "Enlarged crop.", convention=6)
add(147, "Définition (4.8.2): 'de (4.8.1) sont vérifiées'", "the reference (4.8.1) upright",
    "italic (definition environment)", "convention",
    fx(r"(\hyperref[III.4.8.1-fr]{4.8.1}) sont vérifiées", r"\textup{(\hyperref[III.4.8.1-fr]{4.8.1})} sont vérifiées"),
    "Enlarged crop.", convention=6)
for old, new, w in (
        (r"est \emph{fini}, ou que", r"est fini, ou que", "'le morphisme f est fini'"),
        ("\\emph{$\\mathfrak Y$-préschéma\nformel fini}", "$\\mathfrak Y$-préschéma\nformel fini",
         "'X est un Y-préschéma formel fini'"),
        (r"\emph{fini au-dessus de $\mathfrak Y$}", r"fini au-dessus de $\mathfrak Y$",
         "'un préschéma formel fini au-dessus de Y'")):
    add(147, f"Définition (4.8.2): {w}", "italic like the rest of the definition (no change of face)",
        "\\emph inside the italic definition environment: upright", "convention", fx(old, new),
        "Enlarged crop. FIX_POLICY 2.6: drop \\emph where the print shows no change of face.", convention=6)
for lab, after in (("i", "Une immersion"), ("ii", "Le composé"), ("iii", "Soient"), ("iv", "Soient"),
                   ("v", "Soient")):
    add(147, f"Proposition (4.8.3): item label '({lab})'", f"'({lab})' upright", f"\\item[({lab})] inside the italic "
        "statement: italic", "convention",
        fx(f"\\item[({lab})] {after}", f"\\item[\\textup{{({lab})}}] {after}"),
        "Item label printed upright (GLOBAL_ISSUES 16).", convention=6)
add(147, "Proposition (4.8.3) (iv): 'f : X→X', g : Y→Y' deux S-morphismes finis'",
    "'S-morphismes' with a roman capital S (the Fraktur S of 'S-préschémas' and '×_S' is meant)",
    "$\\mathfrak S$-morphismes (silently corrected)", "misprint_in_print",
    fx(r"$\mathfrak S$-morphismes finis", r"$S$-morphismes finis"),
    "Enlarged crop: a plain serif S, unlike the Fraktur S two lines above and in f×_S g. The fix restores the "
    "printed reading ($S$ as for the edition's other upright capitals).",
    corrected=r"$\mathfrak S$-morphismes finis")
conv2(147, "proof of (4.8.3): 'préschémas usuels (II, 6.1.5)'", "(II, 6.1.5)")
add(147, "proof of (4.8.3): 'à l'aide du critère a) de (4.8.1)'", "letter 'a)' in italics", "upright", "italics",
    fx(r"du critère a) de", r"du critère \emph{a)} de"), "Enlarged crop.")
conv2(147, "proof of (4.8.3): 'sur le modèle de (I, 10.13.5)'", "(I, 10.13.5)")
conv2(147, "Corollaire (4.8.4): 'Sous les hypothèses de (I, 10.9.9)'", "(I, 10.9.9)",
      new=r"\textup{(\textbf{I}, 10.9.9)}",
      note="One edit for this finding and the next (convention 6): bold numeral and the upright reference together.")
add(147, "same reference '(I, 10.9.9)'", "the reference is upright inside the italic statement",
    "italic (corollary environment)", "convention", None,
    "Covered by the edit of the preceding finding (convention 2), which adds the \\textup.", convention=6)
add(147, "proof of (4.8.6): 'morphismes f_n : X_n→Y_n; montrons'",
    "the subscript n of f_n and of Y_n bold italic (wrong fount); the n of X_n normal",
    "plain n in all three (silently corrected)", "misprint_in_print",
    fx(r"$f_n:X_n\to Y_n$", r"$f_{\boldsymbol{n}}:X_n\to Y_{\boldsymbol{n}}$"),
    "Crop at 4x and ink count: the two heavy n are 16 px wide with about 32% more ink than the 13 px n of X_n "
    "(wider and heavier: a bold sort, not inking). The other n on the page are normal.",
    confidence="medium", corrected=r"f_n:X_n\to Y_n")
add(147, "proof of (4.8.6): 'montrons que les f_n sont des morphismes finis et f_*(O_X) est isomorphe'",
    "'et f_*(O_X) est isomorphe' (no 'que' after 'et')", "'et que'", "extra",
    fx(r"""morphismes finis
et que $f_*(\mathcal O_{\mathfrak X})$""", r"""morphismes finis
et $f_*(\mathcal O_{\mathfrak X})$"""),
    "Enlarged crop.")
conv2(147, "proof of (4.8.6): 'ce qui établira notre assertion (I, 10.10.5)'", "(I, 10.10.5)")
add(147, "proof of (4.8.7): 'et posons Y_n = (Y, O_Y/K^{n+1}) et A_n = A/K^{n+1}A; il est clair'",
    "'et' between the two formulas; the formulas inline in the text line",
    "no 'et' (comma and \\qquad in a display)", "missing",
    fx(r"""et posons
\[
Y_n=(\mathfrak Y,\mathcal O_{\mathfrak Y}/\mathcal K^{n+1}),\qquad
\mathcal A_n=\mathcal A/\mathcal K^{n+1}\mathcal A~;
\]
il est clair""",
       r"""et posons
$Y_n=(\mathfrak Y,\mathcal O_{\mathfrak Y}/\mathcal K^{n+1})$ et
$\mathcal A_n=\mathcal A/\mathcal K^{n+1}\mathcal A$~;
il est clair"""),
    "Enlarged crop. The edit also sets the formulas inline as printed.")
add(147, "last line: 'et définit donc un' (the sentence continues on p. 148 'Y_n-préschéma fini')",
    "no paragraph break at the page turn", "blank line before \\oldpage[III]{148} (paragraph break)", "other",
    fx(r"""définit donc un

""", r"""définit donc un
"""),
    "The blank line after \\oldpage[III]{148} is already gone in the diplomatic release file.")

# ---------------------------------------------------------------- move of \oldpage[III]{143} (keep last)
add(143, "page start: marker \\oldpage[III]{143} (step 1 of 2)",
    "printed p. 143 begins 'suppose f_z fini, l'existence pour tout y∈h^{-1}(z) d'un voisinage V_y tel que "
    "f^{-1}(V_y)→V_y soit fini résulte de (4.4.11). Pour traiter le cas où ...', one running paragraph "
    "(p. 142 ends '(II, 5.4.3); si on')",
    "\\oldpage[III]{143} stands before 'Pour traiter le cas', between two blank lines (a paragraph break)",
    "marker",
    fx(r"""\oldpage[III]{143}

Pour traiter le cas""", r"""Pour traiter le cas"""),
    "Step 1 of the move of \\oldpage[III]{143}: remove it here, after all other p. 143 edits (they are located "
    "by this marker), then apply step 2 (next finding, p. 142 segment), which re-inserts it before 'suppose'.")
add(142, "end of the p. 142 segment: 'si on suppose f_z fini, ... résulte de (4.4.11).' (step 2 of 2, printed on "
         "p. 143)",
    "'suppose' is the first word of printed p. 143; 'résulte de (4.4.11). Pour traiter le cas' runs on in one line",
    "the text 'suppose ... (4.4.11).' stands before \\oldpage[III]{143}, followed by a blank line",
    "marker",
    fx(r"""si on suppose $f_z$ fini, l'existence pour tout
$y\in h^{-1}(z)$ d'un voisinage $V_y$ tel que $f^{-1}(V_y)\to V_y$ soit fini
résulte de (\hyperref[III.4.4.11-fr]{4.4.11}).

""", r"""si on
\oldpage[III]{143}
suppose $f_z$ fini, l'existence pour tout
$y\in h^{-1}(z)$ d'un voisinage $V_y$ tel que $f^{-1}(V_y)\to V_y$ soit fini
résulte de (\hyperref[III.4.4.11-fr]{4.4.11}).
"""),
    "Step 2 of the move of \\oldpage[III]{143}, after step 1: lies in the p. 142 segment (no page file in this "
    "run). Puts the marker before 'suppose' and removes the blank line, so 'Pour traiter le cas' continues the "
    "paragraph as printed. The moved text matches the first two lines of the p. 143 scan.")

# ---------------------------------------------------------------- checks
pages = {n: (RUN / f"page_{n}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for n in range(143, 148)}
dip = DIP.read_text(encoding="utf-8")
problems = []
for i, x in enumerate(F):
    if x["fix"] is None:
        continue
    old = x["fix"]["old"]
    if x["page"] not in pages:
        problems.append((i, x["page"], x["kind"], "no page file (outside this run's pages)", old[:60]))
        continue
    c = pages[x["page"]].count(old)
    if c != 1:
        problems.append((i, x["page"], x["kind"], "count in page file = %d" % c, old[:60]))


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in MARK.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            return s, cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
    return None, None


sim = dip
applied, manual = 0, []
for i, x in enumerate(F):
    if x["fix"] is None:
        continue
    s, e = locate(sim, x["page"])
    seg = sim[s:e]
    if seg.count(x["fix"]["old"]) != 1:
        manual.append((i, x["page"], x["kind"], seg.count(x["fix"]["old"])))
        continue
    sim = sim[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + sim[e:]
    applied += 1
# the hand-applied marker edit (p. 143) on the whole file
for i, p, k, c in manual:
    old = F[i]["fix"]["old"]
    print("manual:", i, p, k, "segment count", c, "| whole-file count", sim.count(old))
    if sim.count(old) == 1:
        sim = sim.replace(old, F[i]["fix"]["new"])
print("simulated: applied", applied, "manual", len(manual))
print("page-file problems:", problems)
print("markers after simulation:", [(int(m.group(1)), sim[m.start() - 12:m.start()].replace("\n", "|"),
                                     sim[m.end():m.end() + 14].replace("\n", "|"))
                                    for m in MARK.finditer(sim) if 142 <= int(m.group(1)) <= 148])
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
counts = {}
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else "convention" if x["kind"] == "convention" else "normal"
    counts.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print("counts:", counts, "total", len(F))
