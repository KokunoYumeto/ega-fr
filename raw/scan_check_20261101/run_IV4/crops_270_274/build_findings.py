"""Build findings_270_274.json and check every fix's "old" against page_NNN.tex and the release source."""
import json
import pathlib
import re

here = pathlib.Path(__file__).resolve().parent
run = here.parent
SRC = run.parent / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4"
OUT = run / "findings_270_274.json"

BFM = ("Lies before the first marker of ega4-21b-fr.tex (the 21.6 heading and (21.6.1) continue p. 270; "
       "apply in the file's before_first_marker region).")
YSANS = ("The print sets the Y of Y(D) as a sans-serif capital (crops p272_YD.png, p272_2165.png, p273_YDU.png), "
         "as from (21.2.12) on (findings_260_264); written \\boldsymbol{\\mathsf{Y}} (heavy sans-serif; coordinator decision, 4 Nov).")
SCRI = ("Script I: the letter sits on the baseline, no descender (crops p272_IdealI.png, p272_IXDD.png); "
        "the letter of I_X(D), as in findings_260_264.")
DOT = "Baseline period in the print (GLOBAL_ISSUES 65), as the IV-4 page fixes write it."
WAVY = "Wavy arrow in the print (GLOBAL_ISSUES 107; coordinator note on ega4-21)."
C7 = "Long dash for the minus sign (GLOBAL_ISSUES 23/49); \\setmin pending the convention-7 decision."

F = []


def add(page, where, scan, tex, kind, fix, note="", convention=None, confidence="high", corrected=None):
    x = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=convention,
             confidence=confidence, fix=fix)
    if kind == "misprint_in_print":
        x["corrected"] = corrected
    x["note"] = note
    F.append(x)


def fx(old, new):
    return {"old": old, "new": new}


# ---------------------------------------------------------------- p. 270 (ega4-21a)
add(270, "Proposition (21.5.8), l. 2: 'g'=g_(X) : Y'→X''",
    "g_(X): subscript (X) without prime (4x crop p270_gX.png)",
    "g_{(X')}: silent correction", "misprint_in_print",
    fx(r"g'=g_{(X')}", r"g'=g_{(X)}"),
    "g' is the base change of g by f: X'→X, i.e. g_(X') (as f'=f_(Y) beside it). The TeX silently corrects; "
    "the fix restores the printed reading. Not in Err_IV (Liste 3).",
    corrected=r"g'=g_{(X')}")
add(270, "Proposition (21.5.8): item labels (i), (ii), (iii)",
    "labels upright (crops p270_ii.png, p270_iii.png)",
    "enumerate labels italic inside the italic proposition", "convention",
    fx("suivantes :\n\\begin{enumerate}[label=(\\roman*)]",
       "suivantes :\n\\begin{enumerate}[label=\\textup{(\\roman*)}]"),
    "GLOBAL_ISSUES 16; same form as the (21.2.3) fix in findings_255_259. One edit covers the three labels.",
    convention=6)
add(270, "Proposition (21.5.8) (iii): 'f vérifie l'hypothèse II) de (21.5.3)'",
    "'II)' upright (crop p270_iii.png)", "italic (statement environment)", "convention",
    fx("l'hypothèse II) de", "l'hypothèse \\textup{II)} de"),
    "GLOBAL_ISSUES 88 (label upright inside an italic statement).", convention=6)
add(270, "Proposition (21.5.8) (iii): 'de Y (resp. Y') domine'",
    "'(resp.' and ')' upright (crop p270_iii.png)", "italic (statement environment)", "convention",
    fx("de $Y$ (resp. $Y'$) domine", "de $Y$ \\textup{(resp.} $Y'$\\textup{)} domine"),
    "GLOBAL_ISSUES 101: parentheses next to 'resp.' are upright.", convention=6)
add(270, "Proposition (21.5.8) (iii): 'de X (resp. X').'",
    "'(resp.' and ')' upright (crop p270_iii.png)", "italic (statement environment)", "convention",
    fx("de $X$ (resp. $X'$).", "de $X$ \\textup{(resp.} $X'$\\textup{)}."),
    "As the previous entry.", convention=6)
add(270, "Proposition (21.5.8): 'Alors, pour tout diviseur D' sur X''",
    "new indented paragraph after item (iii)", "follows \\end{enumerate} without a blank line (no indent)", "other",
    fx("\\end{enumerate}\nAlors, pour tout diviseur", "\\end{enumerate}\n\nAlors, pour tout diviseur"),
    "GLOBAL_ISSUES 80 pattern; inside the proposition environment, so the text stays italic.")
add(270, "proof of (21.5.8): 'dans la catégorie des O_X'-Module inversibles'",
    "O_X' (subscript X') (crop p270_categorie.png)", "O_Y: silent correction", "misprint_in_print",
    fx("catégorie des $\\sh{O}_Y$-", "catégorie des $\\sh{O}_{X'}$-"),
    "Both sides of the isomorphism are invertible O_Y-Modules (g^*(N_{X'/X}(L')) and N_{Y'/Y}(...)). The TeX "
    "silently corrects; the fix restores the printed reading. Independent of the next entry (no overlap). "
    "Not in Err_IV (Liste 3).",
    corrected="catégorie des $\\sh{O}_Y$-")
add(270, "proof of (21.5.8): 'dans la catégorie des O_X'-Module inversibles'",
    "'Module' singular after 'des' (crop p270_categorie.png)", "'Modules': silent correction",
    "misprint_in_print",
    fx("Modules inversibles;", "Module inversibles;"),
    "Missing plural s after 'des ... '. The TeX silently corrects; the fix restores the printed reading.",
    corrected="Modules inversibles;")
add(270, "heading 21.6: 'Cycle 1-codimensionnel associé à un diviseur.'",
    "full stop after the title (page_270_s4.png)", "no full stop", "punctuation",
    fx("\\subsection{Cycle 1-codimensionnel associé à un diviseur}",
       "\\subsection{Cycle 1-codimensionnel associé à un diviseur.}"),
    BFM + " GLOBAL_ISSUES 43/58; same form as the 20.6 title fix in findings_250_254.")
add(270, "(21.6.1): 'Soit X un préschéma localement noethérien,'",
    "'préschéma localement noethérien' italic (crop p270_2161.png)", "roman", "italics",
    fx("Soit $X$ un préschéma localement noethérien,",
       "Soit $X$ un \\emph{préschéma localement noethérien},"),
    BFM)
add(270, "(21.6.1): 'par l'application x ⇝ {x}‾'",
    "wavy arrow (crop p270_2161.png)", "\\mapsto", "symbol",
    fx("l'application $x\\mapsto\\overline{\\{x\\}}$", "l'application $x\\leadsto\\overline{\\{x\\}}$"),
    BFM + " " + WAVY)
add(270, "(21.6.1), printed p. 271 l. 1: '... tels que n_x ≠ 0) soit localement fini.'",
    "'localement fini' italic (crop p271_top.png)", "roman", "italics",
    fx("$n_x\\neq0$) soit localement fini.", "$n_x\\neq0$) soit \\emph{localement fini}."),
    BFM + " Printed on p. 271; apply before the marker insertion below.")
add(270, "(21.6.1), printed p. 271 l. 2: 'est un sous-groupe de Z^X'",
    "'sous-groupe' italic (crop p271_top.png)", "roman", "italics",
    fx("est un sous-groupe", "est un \\emph{sous-groupe}"),
    BFM + " Printed on p. 271.")
add(270, "(21.6.1), printed p. 271 l. 2: 'de Z^X, qui contient le groupe somme directe'",
    "comma after Z^X (crop p271_top.png)", "no comma", "punctuation",
    fx("$\\bb{Z}^X$ qui contient", "$\\bb{Z}^X$, qui contient"),
    BFM + " Printed on p. 271; does not overlap the previous entry.")
add(270, "(21.6.1), printed p. 271 l. 3: 'et lui est égal lorsque X est noethérien.'",
    "'noethérien' italic (crop p271_top.png)", "roman", "italics",
    fx("et lui est égal lorsque $X$ est noethérien.", "et lui est égal lorsque $X$ est \\emph{noethérien}."),
    BFM + " Printed on p. 271.")
add(270, "(21.6.1), printed p. 271 l. 6: 'On considère toujours 𝔷(X) comme ordonné par'",
    "'ordonné' italic (crop p271_top.png)", "roman", "italics",
    fx("comme ordonné par", "comme \\emph{ordonné} par"),
    BFM + " Printed on p. 271.")
add(270, "(21.6.1), printed p. 271 l. 6: 'par l'ordre produit de Z^X, et on notera'",
    "comma after Z^X (crop p271_top.png)", "no comma", "punctuation",
    fx("produit de $\\bb{Z}^X$ et on notera", "produit de $\\bb{Z}^X$, et on notera"),
    BFM + " Printed on p. 271.")
add(270, "page break 270/271 inside (21.6.1): '(ou, ce qui revient | au même, l'ensemble des x∈X'",
    "p. 270 ends with '(ou, ce qui revient'; p. 271 begins 'au même, l'ensemble des x∈X tels que n_x≠0) "
    "soit localement fini.' (page_270_s4.png, page_271_s1.png)",
    "marker 271 stands later, before 'Pour tout cycle' (seven printed lines too late)", "marker",
    fx("(ou, ce qui revient au même, l'ensemble",
       "(ou, ce qui revient\n\\oldpage[IV-4]{271}\nau même, l'ensemble"),
    BFM + " Mid-sentence break: no blank lines. Part 1 of 2: apply together with the last p. 271 entry, which "
    "removes the old marker. Apply the (21.6.1) entries above first (they are written for the region before "
    "the file's first marker).")

# ---------------------------------------------------------------- p. 271 (ega4-21b)
add(271, "display after 'on écrira par abus de langage,': 'Z = Σ n_x.{x}‾'",
    "baseline period (4x crop p271_dot.png)", "\\cdot", "symbol",
    fx("\\[\n  Z=\\sum_{x\\in X}n_x\\cdot", "\\[\n  Z=\\sum_{x\\in X}n_x."), DOT)
add(271, "same display: final punctuation",
    "semicolon (crop p271_dot.png); the sentence goes on with 'on appelle'", "full stop", "punctuation",
    fx("\\overline{\\{x\\}}.\n\\]", "\\overline{\\{x\\}};\n\\]"),
    "Does not overlap the previous entry.")
add(271, "after the display: 'on appelle multiplicité de Z au point x'",
    "lowercase 'on' (crop p271_mult.png)", "'On'", "word",
    fx("On appelle \\emph{multiplicité", "on appelle \\emph{multiplicité"),
    "Follows from the printed semicolon.")
add(271, "(21.6.1): 'c'est une partie fermée de X'",
    "'fermée' italic (crop p271_mult.png)", "roman", "italics",
    fx("c'est une partie fermée de $X$", "c'est une partie \\emph{fermée} de $X$"))
add(271, "(21.6.2): 'est un cycle p-codimensionnel si son support'",
    "no comma after 'p-codimensionnel' (line end, crop p271_pcodim.png)", "comma", "punctuation",
    fx("$p$-codimensionnel}, si son support", "$p$-codimensionnel} si son support"))
add(271, "(21.6.2): 'si son support est purement de codimension p'",
    "'purement' italic (crop p271_purement.png)", "roman", "italics",
    fx("support est purement de", "support est \\emph{purement} de"))
add(271, "(21.6.2): 'ou, ce qui revient au même (5.1.2.1), dim(O_X,x) = p'",
    "(5.1.2.1) (crop p271_5121.png)", "\\sref{IV.5.1.2} prints (5.1.2)", "number",
    fx("au même \\sref{IV.5.1.2}, $\\dim", "au même \\sref{IV.5.1.2.1}, $\\dim"),
    "(5.1.2.1) is the formula dim(O_X,x)=codim of EGA IV_2; the label is outside this package, so \\sref "
    "prints the number with the unavailable-link fallback, as for IV.5.1.2.")
add(271, "(21.6.2), end: 'on considère 𝔷(X) comme gradué par les Z^p(X) pour p∈N'",
    "roman capital Z, not the Fraktur 𝔷 (4x crop p271_Zp.png)", "\\mathfrak{Z}^p(X): silent correction",
    "misprint_in_print",
    fx("par les $\\mathfrak{Z}^p(X)$ pour", "par les $Z^p(X)$ pour"),
    "Wrong letter in the print: the graded pieces are the groups 𝔷^p(X) of the same sentence. The TeX "
    "silently corrects; the fix restores the printed reading (formula capital written $Z$ as elsewhere).",
    corrected="par les $\\mathfrak{Z}^p(X)$ pour")
add(271, "(21.6.3), l. 1: 'Soient Z = Σ n_x.{x}‾ un cycle sur X'",
    "baseline period (crop p271_2163.png)", "\\cdot", "symbol",
    fx("Soient $Z=\\sum_{x\\in X}n_x\\cdot", "Soient $Z=\\sum_{x\\in X}n_x."), DOT)
add(271, "(21.6.3): 'le cycle Σ_{x∈U} n_x.(U∩{x}‾) sur U'",
    "baseline period (crop p271_2163.png)", "\\cdot", "symbol",
    fx("\\sum_{x\\in U}n_x\\cdot(U\\cap", "\\sum_{x\\in U}n_x.(U\\cap"), DOT)
add(271, "(21.6.3): 'Il est clair que Z ⇝ Z|U est un homomorphisme'",
    "wavy arrow (crop p271_arrows.png)", "\\mapsto", "symbol",
    fx("$Z\\mapsto Z|U$", "$Z\\leadsto Z|U$"), WAVY)
add(271, "(21.6.3): 'l'application U ⇝ 𝔷(U)'",
    "wavy arrow (crop p271_arrows.png)", "\\mapsto", "symbol",
    fx("$U\\mapsto\\mathfrak{Z}(U)$", "$U\\leadsto\\mathfrak{Z}(U)$"), WAVY)
add(271, "(21.6.3): '(resp. U ⇝ 𝔷^p(U))'",
    "wavy arrow (page_271_s4.png)", "\\mapsto", "symbol",
    fx("$U\\mapsto\\mathfrak{Z}^p(U)$", "$U\\leadsto\\mathfrak{Z}^p(U)$"), WAVY)
add(271, "top of p. 271: old position of the page marker",
    "printed p. 271 begins 'au même, l'ensemble des x∈X' inside (21.6.1); 'Pour tout cycle' is the 8th line",
    "\\oldpage[IV-4]{271} with blank lines before 'Pour tout cycle'", "marker",
    fx("\\oldpage[IV-4]{271}\n\nPour tout cycle", "Pour tout cycle"),
    "Part 2 of 2: apply together with the p. 270 entry that inserts the marker after '(ou, ce qui revient' "
    "(that one lies before the first marker of ega4-21b). Listed last for this page: the other p. 271 "
    "entries need the old marker to locate their segment. The blank line before the old marker stays, so "
    "'Pour tout cycle' remains a new paragraph, as printed.")

# ---------------------------------------------------------------- p. 272 (ega4-21b)
add(272, "l. 1: 'de monoïdes U ⇝ 𝔷^+(U)'",
    "wavy arrow (crop p272_arrows.png)", "\\mapsto", "symbol",
    fx("$U\\mapsto\\mathfrak{Z}^+(U)$", "$U\\leadsto\\mathfrak{Z}^+(U)$"), WAVY)
add(272, "l. 1: '(resp. U ⇝ 𝔷^{p+}(U))'",
    "wavy arrow (crop p272_arrows.png)", "\\mapsto", "symbol",
    fx("$U\\mapsto\\mathfrak{Z}^{p+}(U)$", "$U\\leadsto\\mathfrak{Z}^{p+}(U)$"), WAVY)
add(272, "'en posant Z' = Σ_{x∈U} mult_x(Z).{x}‾'",
    "baseline period (4x crop p272_dot.png)", "\\cdot", "symbol",
    fx("\\operatorname{mult}_x(Z)\\cdot\\overline{\\{x\\}}", "\\operatorname{mult}_x(Z).\\overline{\\{x\\}}"), DOT)
add(272, "(21.6.4): 'du faisceau de monoïdes 𝒮(O_X) = O_X ∩ M_X^*'",
    "'𝒮(O_X)=' before O_X ∩ M_X^* (crop p272_2164.png)", "'𝒮(O_X)=' missing", "missing",
    fx("du faisceau de monoïdes $\\sh{O}_X\\cap\\sh{M}_X^*$",
       "du faisceau de monoïdes $\\sh{S}(\\sh{O}_X)=\\sh{O}_X\\cap\\sh{M}_X^*$"),
    "The notation 𝒮(O_X) is used in the same sentence ('sa restriction 𝒮(O_X) → 𝒵^1_X').")
add(272, "(21.6.4): 'sa restriction 𝒮(O_X) → 𝒵^1_X, qui est un homomorphisme'",
    "comma after 𝒵^1_X (crop p272_2164.png)", "no comma", "punctuation",
    fx("\\to\\mathscr{Z}_X^1$ qui est", "\\to\\mathscr{Z}_X^1$, qui est"))
add(272, "(21.6.4): 'qui est un homomorphisme de faisceau de monoïdes soumis'",
    "'faisceau' singular (crop p272_2164.png)", "'faisceaux'", "word",
    fx("un homomorphisme de faisceaux de \\emph{monoïdes}", "un homomorphisme de faisceau de \\emph{monoïdes}"),
    "The print has the singular in both places of this paragraph (also the next entry); the TeX changed both. "
    "Not recorded as a misprint (repeated, and 'homomorphisme de faisceau de monoïdes' is a possible usage).")
add(272, "(21.6.4): 'il suffit de définir un homomorphisme de faisceau de monoïdes'",
    "'faisceau de monoïdes' italic, 'faisceau' singular (crop p272_2164.png)", "\\emph{faisceaux de monoïdes}",
    "word",
    fx("\\emph{faisceaux de monoïdes}", "\\emph{faisceau de monoïdes}"))
add(272, "display (21.6.4.2): 'c : 𝒟iv^+_X → 𝒵^1_X.'",
    "target 𝒵^1_X without + (4x crop p272_21642.png)", "\\mathscr{Z}_X^{1+}", "formula",
    fx("c:\\sh{D}iv_X^+\\to\\mathscr{Z}_X^{1+}.", "c:\\sh{D}iv_X^+\\to\\mathscr{Z}_X^1."),
    "Not a misprint: a homomorphism of sheaves of monoids into 𝒵^1_X is what the sentence needs (the print "
    "also has 'sa restriction 𝒮(O_X) → 𝒵^1_X' and, p. 273, 'cyc : Div^+(U) → 𝔷^1(U)'); the TeX rewrote it.")
add(272, "(21.6.5): 'le sous-préschéma fermé Y(D) de X'",
    "sans-serif Y (3x crop p272_YD.png)", "$Y(D)$", "font",
    fx("fermé $Y(D)$ de $X$", "fermé $\\boldsymbol{\\mathsf{Y}}(D)$ de $X$"), YSANS)
add(272, "(21.6.5): 'défini par l'Idéal I_X(D) ⊂ O_X'",
    "script I (4x crop p272_IdealI.png)", "\\sh{J}", "symbol",
    fx("l'Idéal $\\sh{J}_X(D)\\subset", "l'Idéal $\\sh{I}_X(D)\\subset"), SCRI)
add(272, "(21.6.5): 'En chacun des points maximaux x de Y(D)'",
    "sans-serif Y (crop p272_2165.png)", "$Y(D)$", "font",
    fx("maximaux $x$ de $Y(D)$", "maximaux $x$ de $\\boldsymbol{\\mathsf{Y}}(D)$"), YSANS)
add(272, "(21.6.5): 'et O_{Y(D),x} est un anneau artinien'",
    "sans-serif Y in the subscript (crop p272_2165.png)", "$\\sh{O}_{Y(D),x}$", "font",
    fx("et $\\sh{O}_{Y(D),x}$ est un anneau", "et $\\sh{O}_{\\boldsymbol{\\mathsf{Y}}(D),x}$ est un anneau"), YSANS)
add(272, "(21.6.5): 'qui n'est pas point maximal de Y(D)'",
    "sans-serif Y (crop p272_2165.png)", "$Y(D)$", "font",
    fx("point maximal de $Y(D)$", "point maximal de $\\boldsymbol{\\mathsf{Y}}(D)$"), YSANS)
add(272, "(21.6.5): 'on a nécessairement x ∉ Y(D)'",
    "sans-serif Y (crop p272_2165.png)", "$Y(D)$", "font",
    fx("$x\\notin Y(D)$", "$x\\notin\\boldsymbol{\\mathsf{Y}}(D)$"), YSANS)
add(272, "(21.6.5): 'donc O_{Y(D),x} = 0'",
    "sans-serif Y in the subscript (crop p272_2165.png)", "$\\sh{O}_{Y(D),x}=0$", "font",
    fx("$\\sh{O}_{Y(D),x}=0$", "$\\sh{O}_{\\boldsymbol{\\mathsf{Y}}(D),x}=0$"), YSANS)
add(272, "display (21.6.5.1): 'long(O_{Y(D),x})'",
    "sans-serif Y in the subscript (crop p272_cyc.png)", "$\\sh{O}_{Y(D),x}$", "font",
    fx("\\sum_{x\\in X^{(1)}}\\operatorname{long}(\\sh{O}_{Y(D),x})",
       "\\sum_{x\\in X^{(1)}}\\operatorname{long}(\\sh{O}_{\\boldsymbol{\\mathsf{Y}}(D),x})"),
    YSANS + " Does not overlap the next entry.")
add(272, "display (21.6.5.1): 'long(O_{Y(D),x}).{x}‾'",
    "baseline period (crop p272_cyc.png)", "\\cdot", "symbol",
    fx("\\cdot\\overline{\\{x\\}}\n  \\tag{21.6.5.1}", ".\\overline{\\{x\\}}\n  \\tag{21.6.5.1}"), DOT)
add(272, "Proposition (21.6.6): 'L'application D ⇝ cyc(D)'",
    "wavy arrow (crop p272_2166.png)", "\\mapsto", "symbol",
    fx("L'application $D\\mapsto\\operatorname{cyc}(D)$", "L'application $D\\leadsto\\operatorname{cyc}(D)$"), WAVY)
add(272, "Proposition (21.6.6): 'du monoïde Div^+(X) dans 𝔷^1(X).'",
    "𝔷^1(X) without + (3x crop p272_2166b.png)", "\\mathfrak{Z}^{1+}(X)", "formula",
    fx("$\\operatorname{Div}^+(X)$ dans $\\mathfrak{Z}^{1+}(X)$", "$\\operatorname{Div}^+(X)$ dans $\\mathfrak{Z}^1(X)$"),
    "Not a misprint (a monoid homomorphism into the group 𝔷^1(X), as in (21.6.4.2) and on p. 273); the TeX "
    "rewrote it.")
add(272, "proof of (21.6.6): 'pour deux diviseurs positifs D, D''",
    "'positifs' italic (page_272_s3.png)", "roman", "italics",
    fx("deux diviseurs positifs $D$", "deux diviseurs \\emph{positifs} $D$"))
add(272, "proof of (21.6.6): 'Or, on a (21.2.5) I_X(D+D') = I_X(D) I_X(D')'",
    "script I three times (3x crop p272_IXDD.png)", "\\sh{J} three times", "symbol",
    fx("$\\sh{J}_X(D+D')=\\sh{J}_X(D)\\sh{J}_X(D')$", "$\\sh{I}_X(D+D')=\\sh{I}_X(D)\\sh{I}_X(D')$"),
    SCRI + " One edit for the three letters of the formula.")
add(272, "after the proof, printed p. 273 l. 2: display 'Y(D|U) = Y(D) ∩ U,' (left side)",
    "sans-serif Y (3x crop p273_YDU.png)", "$Y(D|U)$", "font",
    fx("Y(D|U)", "\\boldsymbol{\\mathsf{Y}}(D|U)"),
    YSANS + " Printed on p. 273; apply before the marker insertion below (it is in p. 272's segment until then).")
add(272, "after the proof, printed p. 273 l. 2: display 'Y(D|U) = Y(D) ∩ U,' (right side)",
    "sans-serif Y (3x crop p273_YDU.png)", "$Y(D)\\cap U$", "font",
    fx("=Y(D)\\cap U", "=\\boldsymbol{\\mathsf{Y}}(D)\\cap U"),
    YSANS + " Printed on p. 273; apply before the marker insertion below.")
add(272, "page break 272/273: 'd'où aussitôt la proposition.' | 'Il résulte aussitôt des définitions'",
    "p. 272 ends with the proof of (21.6.6); p. 273 begins with the indented paragraph 'Il résulte aussitôt "
    "des définitions que pour tout ouvert U⊂X, on a' and the display Y(D|U) = Y(D)∩U (page_273_s1.png)",
    "marker 273 stands after that display, before 'donc cyc(D|U)'", "marker",
    fx("\\end{proof}\n\nIl résulte aussitôt des définitions",
       "\\end{proof}\n\n\\oldpage[IV-4]{273}\n\nIl résulte aussitôt des définitions"),
    "Part 1 of 2 (apply together with the first p. 273 entry, which removes the old marker). New paragraph "
    "at the top of the page: blank lines kept on both sides, as at marker 271. Listed last for p. 272.")

# ---------------------------------------------------------------- p. 273 (ega4-21b)
add(273, "top of p. 273: old position of the page marker",
    "printed p. 273 begins with 'Il résulte aussitôt des définitions' (two lines and a display above "
    "'donc cyc(D|U)')", "\\oldpage[IV-4]{273} before 'donc cyc(D|U)'", "marker",
    fx("\\oldpage[IV-4]{273}\ndonc $\\operatorname{cyc}(D|U)", "donc $\\operatorname{cyc}(D|U)"),
    "Part 2 of 2: apply together with the last p. 272 entry (new marker before 'Il résulte').")
add(273, "l. 4: 'un homomorphisme de faisceaux de monoïdes (21.6.4.3)'",
    "(21.6.4.3) (4x crop p273_21643.png)", "\\sref{IV.21.6.4.2}: silent correction", "misprint_in_print",
    fx("monoïdes \\sref{IV.21.6.4.2}", "monoïdes \\sref{IV.21.6.4.3}"),
    "There is no (21.6.4.3); the homomorphism of sheaves of monoids is (21.6.4.2). The TeX silently "
    "corrects; the fix restores the printed number (link target as printed, as in the EGA II/III "
    "precedents). Not in Err_IV (Liste 3).",
    corrected="monoïdes \\sref{IV.21.6.4.2}")
add(273, "'(21.6.6.2) Supp(cyc(D)) = Supp(D) lorsque D ≥ 0;'",
    "(21.6.6.2) is the bold number of the display, at the left of the formula line; the sentence runs on "
    "('... pour tout diviseur D et [display] on a déjà vu ...', page_273_s1.png)",
    "\\begin{env}[21.6.6.2]: number set as a heading on its own line, and 'on a déjà vu' starts a new "
    "indented paragraph", "other",
    fx("\\begin{env}[21.6.6.2]\n\\label{IV.21.6.6.2}\n\\[\n"
       "  \\Supp(\\operatorname{cyc}(D))=\\Supp(D)\\quad\\text{lorsque}\\quad D\\geq0;\n\\]\n\\end{env}",
       "\\begin{equation}\n"
       "  \\Supp(\\operatorname{cyc}(D))=\\Supp(D)\\quad\\text{lorsque}\\quad D\\geq0;\n"
       "  \\tag{21.6.6.2}\\label{IV.21.6.6.2}\n\\end{equation}"),
    "GLOBAL_ISSUES 64 pattern (equation number set as an env heading); same form as (19.5.5.5) in "
    "findings_205_209. The label keeps its name and carries the tag.")
add(273, "(21.6.7): 'que nous noterons encore D ⇝ cyc(D)'",
    "wavy arrow (crop p273_arrows.png)", "\\mapsto", "symbol",
    fx("noterons encore $D\\mapsto\\operatorname{cyc}(D)$", "noterons encore $D\\leadsto\\operatorname{cyc}(D)$"), WAVY)
add(273, "(21.6.7): 'égal comme on l'a vu à long(O_{Y(D),x})'",
    "sans-serif Y in the subscript (3x crop p273_longY.png)", "$\\sh{O}_{Y(D),x}$", "font",
    fx("\\operatorname{long}(\\sh{O}_{Y(D),x})$ lorsque", "\\operatorname{long}(\\sh{O}_{\\boldsymbol{\\mathsf{Y}}(D),x})$ lorsque"),
    YSANS)
add(273, "display (21.6.7.1): 'mult_x(D).{x}‾,'",
    "baseline period (crop p273_7671.png)", "\\cdot", "symbol",
    fx("\\operatorname{mult}_x(D)\\cdot\\overline{\\{x\\}},", "\\operatorname{mult}_x(D).\\overline{\\{x\\}},"), DOT)
add(273, "(21.6.7): 'et en vertu du fait que D ⇝ cyc(D) est un homomorphisme'",
    "wavy arrow (page_273_s2.png)", "\\mapsto", "symbol",
    fx("du fait que $D\\mapsto\\operatorname{cyc}(D)$", "du fait que $D\\leadsto\\operatorname{cyc}(D)$"), WAVY)
add(273, "display (21.6.7.2): 'mult_x(—D)'",
    "long dash (crop p273_21672.png)", "minus sign", "convention",
    fx("\\operatorname{mult}_x(-D)", "\\operatorname{mult}_x(\\setmin D)"), C7, convention=7)
add(273, "display (21.6.7.2): '= —mult_x(D)'",
    "long dash (crop p273_21672.png)", "minus sign", "convention",
    fx("=-\\operatorname{mult}_x(D)", "=\\setmin\\operatorname{mult}_x(D)"), C7 + " Does not overlap the previous entry.",
    convention=7)
add(273, "(21.6.7): 'est l'ordre de f au point x∈X^(1)'",
    "'l'' roman, italics begin with 'ordre' (4x crop p273_lordre.png)", "\\emph{l'ordre de $f$ au point}",
    "italics",
    fx("\\emph{l'ordre de $f$ au point}", "l'\\emph{ordre de $f$ au point}"))
add(273, "(21.6.7): '(élément régulier de cet anneau local par hypothèse)'",
    "'régulier' italic (crop p273_ordre.png)", "roman", "italics",
    fx("(élément régulier de cet anneau", "(élément \\emph{régulier} de cet anneau"))
add(273, "display (21.6.7.5): 'o_x(f^{-1}) = —o_x(f)'",
    "long dash (crop p273_21675.png)", "minus sign", "convention",
    fx("=-o_x(f)", "=\\setmin o_x(f)"), C7, convention=7)
add(273, "display Z^+(f): '(o_x(f))^+.{x}‾'",
    "baseline period (crop p273_Zpm.png)", "\\cdot", "symbol",
    fx("(o_x(f))^+\\cdot\\overline{\\{x\\}}", "(o_x(f))^+.\\overline{\\{x\\}}"), DOT)
add(273, "display Z^-(f): '(o_x(f))^-.{x}‾'",
    "baseline period (crop p273_Zpm.png)", "\\cdot", "symbol",
    fx("(o_x(f))^-\\cdot\\overline{\\{x\\}}", "(o_x(f))^-.\\overline{\\{x\\}}"), DOT)
add(273, "(21.6.7): 'cyc(div(f)) = Z^+(f) — Z^-(f)'",
    "long dash (crop p273_ZpZm.png)", "minus sign", "convention",
    fx("Z^+(f)-Z^-(f)", "Z^+(f)\\setmin Z^-(f)"), C7, convention=7)
add(273, "(21.6.7): '(ou linéairement équivalents à 0)'",
    "the figure 0, upright; 'linéairement équivalents à' italic (4x crop p273_lineq2.png)",
    "\\emph{linéairement équivalents à zéro}", "word",
    fx("\\emph{linéairement équivalents à zéro}", "\\emph{linéairement équivalents à} $0$"))

# ---------------------------------------------------------------- p. 274 (ega4-21b)
add(274, "(21.6.7): 'Si Z = Σ_{x∈X^(1)} n_x.{x}‾,'",
    "baseline period (3x crop p274_Zdot.png)", "\\cdot", "symbol",
    fx("Si $Z=\\sum_{x\\in X^{(1)}}n_x\\cdot", "Si $Z=\\sum_{x\\in X^{(1)}}n_x."), DOT)
add(274, "(21.6.7): 'si l'on pose T_y = Spec(O_X,x)'",
    "O_X,x: subscript x (4x crop p274_Spec.png)", "O_{X,y}: silent correction", "misprint_in_print",
    fx("\\Spec(\\sh{O}_{X,y})", "\\Spec(\\sh{O}_{X,x})"),
    "T_y is the spectrum of the local ring at y (x is the summation index of the next formula). The TeX "
    "silently corrects; the fix restores the printed reading. Not in Err_IV (Liste 3).",
    corrected="\\Spec(\\sh{O}_{X,y})")
add(274, "(21.6.7): 'On déduit ... un homomorphisme canonique Div(X)/Div.princ(X) → ...'",
    "'canonique' after 'un homomorphisme' (crop p274_cano.png)", "'canonique' missing", "missing",
    fx("un homomorphisme $\\operatorname{Div}(X)/", "un homomorphisme canonique $\\operatorname{Div}(X)/"))
add(274, "(21.6.8): 'où A est un anneau noethérien intègre et intégralement clos'",
    "'anneau' italic too (crop p274_2168.png)", "\\emph starts at 'noethérien'", "italics",
    fx("un anneau \\emph{noethérien intègre et intégralement clos}",
       "un \\emph{anneau noethérien intègre et intégralement clos}"))
add(274, "(21.6.8): 'aux éléments ≠ 0 du corps des fractions K de A'",
    "'≠ 0' (crop p274_arrows.png)", "'non nuls'", "word",
    fx("aux éléments non nuls du corps", "aux éléments $\\neq0$ du corps"), "Rewording by the TeX.")
add(274, "(21.6.8): 'l'application f ⇝ cyc(div(f)) de M(X)'",
    "wavy arrow (crop p274_arrows.png)", "\\mapsto", "symbol",
    fx("$f\\mapsto\\operatorname{cyc}(\\operatorname{div}(f))$", "$f\\leadsto\\operatorname{cyc}(\\operatorname{div}(f))$"),
    WAVY)
add(274, "(21.6.8): 'l'application notée f ⇝ div(f) dans Bourbaki'",
    "wavy arrow (crop p274_arrows.png)", "\\mapsto", "symbol",
    fx("notée $f\\mapsto\\operatorname{div}(f)$", "notée $f\\leadsto\\operatorname{div}(f)$"), WAVY)
add(274, "(21.6.8): 'au groupe des classes de diviseurs de A au sens de Bourbaki'",
    "'de' before A italic (crop p274_classes.png)", "\\emph ends before 'de'", "italics",
    fx("\\emph{groupe des classes de diviseurs} de $A$", "\\emph{groupe des classes de diviseurs de} $A$"))
add(274, "Théorème (21.6.9): 'Soit X un préschéma localement noethérien normal.'",
    "'normal.' upright inside the italic statement (crop p274_thm.png)", "italic (statement environment)",
    "convention",
    fx("localement noethérien normal.", "localement noethérien \\textup{normal}."), "", convention=6)
add(274, "Théorème (21.6.9): item labels (i), (ii)",
    "labels upright (page_274_s3.png)", "enumerate labels italic inside the italic theorem", "convention",
    fx("\\begin{enumerate}[label=(\\roman*)]\n  \\item L'homomorphisme canonique",
       "\\begin{enumerate}[label=\\textup{(\\roman*)}]\n  \\item L'homomorphisme canonique"),
    "GLOBAL_ISSUES 16. Only the theorem's list; the proof's list (roman text) is right. Labels a), b), c) "
    "already come out upright (\\emph inside the italic statement), as printed.", convention=6)
add(274, "Théorème (21.6.9): '(On dit alors que X est un préschéma localement factoriel.)'",
    "roman sentence with 'localement factoriel' italic (page_274_s3.png)",
    "inverted: sentence italic (statement environment), 'localement factoriel' upright", "convention",
    fx("(On dit alors que $X$ est un préschéma \\emph{localement factoriel}.)",
       "\\textup{(On dit alors que $X$ est un préschéma \\emph{localement factoriel}.)}"),
    "Inside \\textup the \\emph gives italic, as printed.", convention=6)
add(274, "proof of (21.6.9) (i): 'Div^+(X) ∩ (—Div^+(X)) = 0'",
    "long dash (crop p274_minus.png)", "minus sign", "convention",
    fx("\\cap(-\\operatorname{Div}^+(X))", "\\cap(\\setmin\\operatorname{Div}^+(X))"), C7, convention=7)
add(274, "proof of (21.6.9) (i): '𝔷^{1+}(X) ∩ (—𝔷^{1+}(X)) = 0'",
    "long dash (crop p274_minus.png)", "minus sign", "convention",
    fx("\\cap(-\\mathfrak{Z}^{1+}(X))", "\\cap(\\setmin\\mathfrak{Z}^{1+}(X))"), C7, convention=7)

# ---------------------------------------------------------------- checks
pages = {n: (run / f"page_{n}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for n in range(270, 275)}
bad = 0
for x in F:
    f = x["fix"]
    if not f:
        continue
    c = pages[x["page"]].count(f["old"])
    if c != 1:
        bad += 1
        print("NOT UNIQUE ON PAGE", x["page"], c, repr(f["old"][:70]))

# source regions (current release text): page segment, or the region before ega4-21b's first marker
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
files = {n: (SRC / n).read_text(encoding="utf-8") for n in ("ega4-21a-fr.tex", "ega4-21b-fr.tex")}


def segment(page):
    for t in files.values():
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for i, (n, s) in enumerate(cuts):
            if n == page:
                return t[s:(cuts[i + 1][1] if i + 1 < len(cuts) else len(t))]
    return ""


t21b = files["ega4-21b-fr.tex"]
bfm = t21b[:marker.search(t21b).start()]
for x in F:
    f = x["fix"]
    if not f:
        continue
    in_seg = segment(x["page"]).count(f["old"])
    in_bfm = bfm.count(f["old"])
    where = "segment" if in_seg == 1 else ("before_first_marker(21b)" if in_bfm == 1 else "NOT FOUND")
    if where == "NOT FOUND" or (in_seg + in_bfm) != 1:
        bad += 1
    if where != "segment":
        print(x["page"], where, repr(f["old"][:60]))

json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for n in range(270, 275):
    print(n, cnt[(n, "normal")], cnt[(n, "convention")], cnt[(n, "misprint")])
print("entries", len(F), "problems", bad)
