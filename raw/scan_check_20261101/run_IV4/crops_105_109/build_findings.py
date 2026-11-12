import json, os, sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, 'findings_105_109.json')
SRC = os.path.join(os.path.dirname(RUN), 'ega-fr', 'editions', '2026-10-24-r20', 'diplomatic',
                   'packages', 'IV4', 'native', 'ega4')

def page_text(p):
    with open(os.path.join(RUN, 'page_%03d.tex' % p), encoding='utf-8', newline='') as f:
        return f.read().replace('\r\n', '\n')

def src_text(name):
    with open(os.path.join(SRC, name), encoding='utf-8', newline='') as f:
        return f.read()

S17 = src_text('ega4-17-fr.tex')
S18 = src_text('ega4-18-fr.tex')

def T(s):
    """raw LaTeX with the character U+23CE marking a line break"""
    return s.replace('⏎', '\n')

F = []
def add(page, where, scan, tex, kind, fix, note='', convention=None, confidence='high',
        corrected=None, src='17'):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": convention, "confidence": confidence, "fix": fix}
    if kind == 'misprint_in_print':
        d["corrected"] = corrected
    d["note"] = note
    d["_src"] = src
    F.append(d)

def fx(old, new):
    return {"old": T(old), "new": T(new)}

C6 = 'Printed upright inside the italic statement.'
LBL = 'Labels in roman text are italic in the print, parenthesis included (GLOBAL_ISSUES 88).'
REF1 = ('The print has (1.x.y), a reference to EGA IV itself (old-style 1 followed by a full stop, light weight), '
        'not (I, x.y); the bold I of real chapter references looks different (cf. (I, 3.3.14) on p. 106).')
PRE18 = ' This text lies in ega4-18-fr.tex BEFORE its first page marker (\\oldpage[IV-4]{110}).'
OM = 'Italic Omega for the sheaf of differentials (GLOBAL_ISSUES 92).'

# ======================= page 105 =======================
add(105, "Proposition (17.15.15), l. 2: 'et que Ω^1_f soit'",
    "italic (slanted) capital Omega (crop p105_omega1f.png)", "\\Omega (upright)", "font",
    fx(r"et que $\Omega^1_f$ soit", r"et que $\varOmega^1_f$ soit"), OM)
add(105, "Proposition (17.15.15), l. 3: 'soit un Ω_X-Module localement libre'",
    "UPRIGHT capital Omega with subscript X: 'un Ω_X-Module' (crop p105_omegaX.png; the script O of O_{X_s,x} on the same page looks quite different, crop p105_OX.png)",
    "$\\sh{O}_X$-Module (silent correction)", "misprint_in_print",
    fx(r"un $\sh{O}_X$-Module localement libre dans un voisinage de $x$, de rang en $x$",
       r"un $\Omega_X$-Module localement libre dans un voisinage de $x$, de rang en $x$"),
    "The print has Omega_X where the structure sheaf O_X is meant. The fix restores the printed reading and changes only the letter; independent of the varOmega edit of Omega^1_f just before it (no overlap).",
    corrected=r"un $\sh{O}_X$-Module localement libre dans un voisinage de $x$, de rang en $x$")
add(105, "'(5.4.2 et II, 7.4.6)'", "bold II", "plain II", "convention",
    fx(r"(5.4.2 et II, 7.4.6)", r"(5.4.2 et \textbf{II}, 7.4.6)"), "", convention=2)
add(105, "'en vertu des définitions et de (II, 7.4.5)'", "bold II", "plain II", "convention",
    fx(r"(II, 7.4.5)", r"(\textbf{II}, 7.4.5)"), "", convention=2)
add(105, "proof of (17.15.15): 'est lisse sur k(y) au point x'", "bold italic k", "plain k", "convention",
    fx(r"lisse sur $k(y)$ au point $x$", r"lisse sur $\boldsymbol{k}(y)$ au point $x$"), "", convention=1)
add(105, "Proposition (17.16.1): 'un anneau de Cohen-Macaulay;'", "hyphen (crop p105_cohen.png)",
    "Cohen--Macaulay (en dash)", "punctuation",
    fx(r"anneau de Cohen--Macaulay; alors", r"anneau de Cohen-Macaulay; alors"),
    "As the Cohen--Macaulay fixes of ega4-2 (GLOBAL_ISSUES 74).")
add(105, "proof of (17.16.1), first sentence: 'La question étant locale sur X et Y'",
    "'sur X et Y' (page_105_s4.png); (17.16.1) concerns f: X→S and has no Y",
    "'sur $X$ et $Y$': the TeX keeps the printed reading", "misprint_in_print", None,
    "Y for S (the base of f: X→S). Corrected edition only; no erratum found.", confidence='medium',
    corrected=r"La question étant locale sur $X$ et $S$")
add(105, "proof of (17.16.1): 'Soit (t_i)_{1≤i≤m} un système de paramètres'",
    "new paragraph: the line 'La question ... de présentation finie.' ends short and 'Soit (t_i)' starts indented (page_105_s4.png)",
    "one paragraph", "other",
    fx(r"de présentation finie. Soit $(t_i)_{1\leq i\leq m}$", r"de présentation finie.⏎⏎Soit $(t_i)_{1\leq i\leq m}$"),
    "Paragraph break missing in the TeX.")
add(105, "page break 105/106 inside 'au-dessus de V telles que | les images'",
    "p. 105 ends 'telles que' (no stop); p. 106 continues the sentence ('les images des (g_i)_x', no indent)",
    "blank line before \\oldpage[IV-4]{106} (and another after it): a paragraph break inside the sentence",
    "marker", fx(r"au-dessus de $V$ telles que⏎⏎", r"au-dessus de $V$ telles que⏎"),
    "The marker is at the right place. Part 1 of 2: the first p. 106 finding removes the blank line after \\oldpage[IV-4]{106}; apply both.")

# ======================= page 106 =======================
add(106, "top of page_106.tex: blank line after \\oldpage[IV-4]{106}",
    "p. 106 begins mid-sentence ('les images', no indent)", "blank line between the marker and 'les images'",
    "marker", fx(r"\oldpage[IV-4]{106}⏎⏎les images", r"\oldpage[IV-4]{106}⏎les images"),
    "Part 2 of 2 with the last p. 105 finding; both blank lines must go.")
add(106, "'la suite (t_i) étant par hypothèse régulière (0, 16.5.7)'", "bold 0", "plain 0", "convention",
    fx(r"régulière (0, 16.5.7)", r"régulière (\textbf{0}, 16.5.7)"), "", convention=2)
add(106, "'restriction de f, est plat et de présentation finie.'",
    "'plat' and 'de présentation finie' italic, 'et' roman (crop p106_l5_8.png)", "roman", "italics",
    fx(r"est plat et de présentation finie. D'autre part", r"est \emph{plat} et \emph{de présentation finie}. D'autre part"), "")
add(106, "'l'anneau O_{X'_s,x} est par définition artinien'", "'artinien' italic", "roman", "italics",
    fx(r"par définition artinien", r"par définition \emph{artinien}"), "")
add(106, "'et comme x est fermé dans X'_s'", "'fermé' italic", "roman", "italics",
    fx(r"comme $x$ est fermé dans", r"comme $x$ est \emph{fermé} dans"), "")
add(106, "'on en conclut qu'il est isolé dans X'_s'", "'isolé' italic", "roman", "italics",
    fx(r"qu'il est isolé dans", r"qu'il est \emph{isolé} dans"), "")
add(106, "end of the proof of (17.16.1): 'le morphisme X'→S est quasi-fini.'", "'quasi-fini' italic", "roman", "italics",
    fx(r"grâce à (13.1.4) que le morphisme $X'\to S$ est quasi-fini.", r"grâce à (13.1.4) que le morphisme $X'\to S$ est \emph{quasi-fini}."), "")
add(106, "Corollaire (17.16.2), l. 2-3: 'localement de présentation finie et localement quasi-fini,'",
    "'localement quasi-fini' roman inside the italic statement (crop p106_cor2.png)", "italic", "convention",
    fx(r"fidèlement plat, localement de présentation finie et localement quasi-fini",
       r"fidèlement plat, localement de présentation finie et \textup{localement quasi-fini}"), C6, convention=6)
add(106, "Corollaire (17.16.2): '(autrement dit, tel qu'il existe une S'-section de X'=X×_S S'",
    "parenthetical roman, only 'section' italic (crop p106_cor2.png)", "all italic (corollary environment)", "convention",
    fx(r"(autrement dit, tel qu'il existe une $S'$-section de $X'",
       r"\textup{(autrement dit, tel qu'il existe une} $S'$-section \textup{de} $X'"),
    "Roman parenthetical inside the italic statement; the reference and closing parentheses are the next finding.", convention=6)
add(106, "Corollaire (17.16.2): '(I, 3.3.14))'", "bold upright I, reference and both closing parentheses upright",
    "plain I, italic inside the corollary", "convention",
    fx(r"(I, 3.3.14))", r"\textup{(\textbf{I}, 3.3.14))}"),
    "Convention 2 with convention 6 (upright reference in an italic statement), one edit.", convention=2)
add(106, "Corollaire (17.16.2), last sentence: '(resp. quasi-compact et quasi-séparé)' and '(resp. S' affine et le morphisme g quasi-fini)'",
    "'(resp.' and the closing parentheses roman, the words between italic", "italic", "convention",
    fx(r"(resp. quasi-compact et quasi-séparé), on peut supposer $S'$ affine (resp. $S'$ affine et le morphisme $g$ quasi-fini).",
       r"\textup{(resp.} quasi-compact et quasi-séparé\textup{)}, on peut supposer $S'$ affine \textup{(resp.} $S'$ affine et le morphisme $g$ quasi-fini\textup{)}."),
    "Two occurrences in one edit (the same sentence recurs in (17.16.5)).", convention=6)
add(106, "proof of (17.16.2): 'localement de type fini sur k(s)'", "bold italic k", "plain k", "convention",
    fx(r"localement de type fini sur $k(s)$", r"localement de type fini sur $\boldsymbol{k}(s)$"), "", convention=1)
add(106, "proof of (17.16.2): 'est un anneau de Cohen-Macaulay est ouvert'", "hyphen", "Cohen--Macaulay (en dash)", "punctuation",
    fx(r"Cohen--Macaulay est ouvert", r"Cohen-Macaulay est ouvert"), "As the Cohen--Macaulay fixes of ega4-2 (GLOBAL_ISSUES 74).")
add(106, "'les points maximaux de X_s (0, 16.5.1)'", "bold 0", "plain 0", "convention",
    fx(r"(0, 16.5.1)", r"(\textbf{0}, 16.5.1)"), "", convention=2)
add(106, "'il contient par suite un point x_s fermé dans X_s'", "'fermé' italic (crop p106_proof2a.png)", "roman", "italics",
    fx(r"un point $x_s$ fermé dans", r"un point $x_s$ \emph{fermé} dans"), "")
add(106, "'il suffit de prendre la somme des X'(s)'", "'somme' italic (crop p106_proof2b.png)", "roman", "italics",
    fx(r"de prendre la somme des", r"de prendre la \emph{somme} des"), "")
add(106, "'un nombre fini de U(s_j)'", "subscript j (crops p106_s3top.png, p106_sj.png)", "U(s_i)", "symbol",
    fx(r"un nombre fini de $U(s_i)$", r"un nombre fini de $U(s_j)$"), "The print indexes the finite family by j here and in the next three formulas.")
add(106, "'le préschéma S' somme des X'(s_j) répond encore'", "subscript j", "X'(s_i)", "symbol",
    fx(r"somme des $X'(s_i)$ répond", r"somme des $X'(s_j)$ répond"), "")
add(106, "'on peut supposer les immersions ouvertes U(s)→S quasi-compactes'", "U(s), no subscript (crop p106_s3top.png)", "U(s_i)", "symbol",
    fx(r"ouvertes $U(s_i)\to S$", r"ouvertes $U(s)\to S$"), "")
add(106, "'quasi-compactes (1.2.7)'", "(1.2.7) (crop p106_s3top.png)", "(I, 2.7)", "number",
    fx(r"quasi-compactes (I, 2.7)", r"quasi-compactes (1.2.7)"), REF1)
add(106, "'donc de présentation finie (1.6.2), et alors'", "(1.6.2)", "(I, 6.2)", "number",
    fx(r"donc de présentation finie (I, 6.2), et alors", r"donc de présentation finie (1.6.2), et alors"), REF1)
add(106, "'les morphismes X'(s_j)→S sont de présentation finie'", "subscript j", "X'(s_i)", "symbol",
    fx(r"les morphismes $X'(s_i)\to S$", r"les morphismes $X'(s_j)\to S$"), "")
add(106, "'sont de présentation finie (1.6.2) et il en est par suite'", "(1.6.2)", "(I, 6.2)", "number",
    fx(r"sont de présentation finie (I, 6.2) et il en est", r"sont de présentation finie (1.6.2) et il en est"), REF1)
add(106, "Corollaire (17.16.3), label (i)", "label (i) upright (crop p106_cor3.png)",
    "\\item[(i)] comes out italic in the italic corollary", "convention",
    fx(r"\item[(i)] Soit $f:X\to S$ un morphisme lisse. Soient", r"\item[\textup{(i)}] Soit $f:X\to S$ un morphisme lisse. Soient"),
    "Roman-numeral labels in italic statements are upright (GLOBAL_ISSUES 16).", convention=6)
add(106, "Corollaire (17.16.3) (i): 'le corps résiduel k(x)'", "bold italic k", "plain k", "convention",
    fx(r"le corps résiduel $k(x)$", r"le corps résiduel $\boldsymbol{k}(x)$"), "", convention=1)
add(106, "Corollaire (17.16.3) (i): 'soit séparable sur k(s); alors'", "bold italic k", "plain k", "convention",
    fx(r"séparable sur $k(s)$; alors", r"séparable sur $\boldsymbol{k}(s)$; alors"), "", convention=1)
add(106, "Corollaire (17.16.3) (i): 'dans la conclusion de (17.16.1),'", "reference upright", "italic", "convention",
    fx(r"dans la conclusion de (17.16.1),", r"dans la conclusion de \textup{(17.16.1)},"), C6, convention=6)
add(106, "Corollaire (17.16.3), label (ii)", "label (ii) upright", "\\item[(ii)] italic", "convention",
    fx(r"\item[(ii)] Soit $f:X\to S$ un morphisme lisse surjectif", r"\item[\textup{(ii)}] Soit $f:X\to S$ un morphisme lisse surjectif"),
    "GLOBAL_ISSUES 16.", convention=6)
add(106, "Corollaire (17.16.3) (ii): 'dans les conclusions de (17.16.2),'", "reference upright", "italic", "convention",
    fx(r"dans les conclusions de (17.16.2),", r"dans les conclusions de \textup{(17.16.2)},"), C6, convention=6)
add(106, "proof of (17.16.3): 'comme X_s est non vide et lisse sur k(s)'", "bold italic k (crop p106_proof3.png)", "plain k", "convention",
    fx(r"non vide et lisse sur $k(s)$", r"non vide et lisse sur $\boldsymbol{k}(s)$"), "", convention=1)
add(106, "proof of (17.16.3): 'un point fermé x∈X_s tel que k(x)'", "bold italic k", "plain k", "convention",
    fx(r"fermé $x\in X_s$ tel que $k(x)$", r"fermé $x\in X_s$ tel que $\boldsymbol{k}(x)$"), "", convention=1)
add(106, "proof of (17.16.3): 'soit séparable sur k(s) (17.15.10, (iii))'",
    "'séparable' italic (crop p106_proof3.png)", "roman", "italics",
    fx(r"soit séparable sur $k(s)$ (17.15.10", r"soit \emph{séparable} sur $\boldsymbol{k}(s)$ (17.15.10"),
    "One edit for this finding and the next (convention 1, bold k of k(s)): the bare 'soit séparable sur' is not unique in the file.")
add(106, "proof of (17.16.3): same 'k(s) (17.15.10, (iii))'", "bold italic k", "plain k", "convention", None,
    "Covered by the edit of the preceding finding (italics), which also sets \\boldsymbol{k}.", convention=1)
add(106, "proof of (17.16.3): 'en prenant pour (t_i) un système régulier de paramètres de'",
    "'système régulier de paramètres' italic (crop p106_s4.png)", "roman", "italics",
    fx(r"un système régulier de paramètres de", r"un \emph{système régulier de paramètres} de"), "")
add(106, "proof of (17.16.3): 'un corps isomorphe à k(x)'", "bold italic k", "plain k", "convention",
    fx(r"isomorphe à $k(x)$", r"isomorphe à $\boldsymbol{k}(x)$"), "", convention=1)
add(106, "proof of (17.16.3): 'donc séparable sur k(s) par hypothèse'", "bold italic k", "plain k", "convention",
    fx(r"donc séparable sur $k(s)$ par hypothèse", r"donc séparable sur $\boldsymbol{k}(s)$ par hypothèse"), "", convention=1)
add(106, "proof of (17.16.3), last line: '(17.6.1, c'))'", "c') italic, its parenthesis included (crop p106_cprime.png)",
    "$c'$) with an upright parenthesis", "italics",
    fx(r"(17.6.1, $c'$))", r"(17.6.1, \emph{c$'$)})"), LBL)
add(106, "page break 106/107 inside Proposition (17.16.4): 'une famille finie (S_i)_{i∈I} | de sous-préschémas affines'",
    "p. 106 ends '(S_i)_{i∈I}' (no stop); p. 107 continues the statement",
    "blank line before \\oldpage[IV-4]{107} (and another after it): a paragraph break inside the sentence",
    "marker", fx(r"une famille finie $(S_i)_{i\in I}$⏎⏎", r"une famille finie $(S_i)_{i\in I}$⏎"),
    "The marker is at the right place. Part 1 of 2: the first p. 107 finding removes the blank line after \\oldpage[IV-4]{107}; apply both.")

# ======================= page 107 =======================
add(107, "top of page_107.tex: blank line after \\oldpage[IV-4]{107}",
    "p. 107 begins mid-sentence ('de sous-préschémas affines', no indent)", "blank line between the marker and 'de sous-préschémas'",
    "marker", fx(r"\oldpage[IV-4]{107}⏎⏎de sous-préschémas", r"\oldpage[IV-4]{107}⏎de sous-préschémas"),
    "Part 2 of 2 with the last p. 106 finding; both blank lines must go.")
add(107, "Proposition (17.16.4): 'surjectifs S_i''→S_i'→S_i, où h_i est étale'",
    "the chain with g_i, h_i over the arrows is set in the running text, followed by ', où' (crop p107_stmt_chain.png)",
    "displayed with \\[ ... \\]", "other",
    fx(r"et surjectifs⏎\[⏎  S_i''\xrightarrow{g_i}S_i'\xrightarrow{h_i}S_i,⏎\]⏎où $h_i$",
       r"et surjectifs $S_i''\xrightarrow{g_i}S_i'\xrightarrow{h_i}S_i$, où $h_i$"),
    "Layout only (display vs inline); the formula matches.")
add(107, "Proposition (17.16.4), last line: '(autrement dit une S_i''-section de X_i''=X×_S S_i'').'",
    "parenthetical roman, only 'section' italic (crop p107_stmt_chain.png)", "all italic (proposition environment)", "convention",
    fx(r"(autrement dit une $S_i''$-section de $X_i''=X\times_S S_i''$).",
       r"\textup{(autrement dit une} $S_i''$-section \textup{de} $X_i''=X\times_S S_i''$\textup{)}."),
    C6, convention=6)
add(107, "proof of (17.16.4): 'l'intersection W_i = ∩_{j≤i} U_j est quasi-compacte' (layout, part 1)",
    "the formula is set in the running text (crops p107_Wi.png, p107_Wi_zoom.png)", "displayed with \\[ ... \\]", "other",
    fx(r"l'intersection⏎\[⏎  W_i=", r"l'intersection $W_i="),
    "Layout part 1 of 2 (opens the inline formula); part 2 is two findings below. The misprint fix between them changes only the right-hand side; the three edits do not overlap. The corrected edition applies both layout parts and skips the misprint fix.")
add(107, "proof of (17.16.4): right-hand side of 'W_i = ∩_{j≤i} U_j'",
    "W_i = ⋂_{j⩽i} U_j: big intersection sign, index j⩽i beneath, then U_j (6x crop p107_Wi_zoom.png)",
    "U_i\\cap\\left(\\bigcup_{j<i}U_j\\right): silent correction", "misprint_in_print",
    fx(r"U_i\cap\left(\bigcup_{j<i}U_j\right)", r"\bigcap_{j\leq i}U_j"),
    "The argument needs W_i = U_i ∩ (⋃_{j<i} U_j): then V_i = U_i—W_i are pairwise disjoint with union S, and W_i is quasi-compact because S is quasi-separated (1.2.7); the printed ⋂_{j≤i} U_j does not give this. No erratum found. The fix restores the printed reading and changes only the formula; it does not overlap the two layout edits around it.",
    corrected=r"U_i\cap\left(\bigcup_{j<i}U_j\right)")
add(107, "proof of (17.16.4): 'W_i = ... est quasi-compacte' (layout, part 2)",
    "inline formula, as above", "end of the display", "other",
    fx(r"⏎\]⏎est quasi-compacte", r"$ est quasi-compacte"),
    "Layout part 2 of 2 (closes the inline formula opened by the layout part 1 finding); apply both.")
add(107, "'est quasi-compacte (1.2.7) donc il existe'", "(1.2.7) (crop p107_pourtouti.png)", "(I, 2.7)", "number",
    fx(r"(I, 2.7) donc il existe", r"(1.2.7) donc il existe"), REF1)
add(107, "'ayant pour espace sous-jacent U_i—W_i'", "long dash for set difference", "minus sign", "convention",
    fx(r"$U_i-W_i$", r"$U_i\setmin W_i$"), "", convention=7)
add(107, "'de présentation finie sur S (1.6.2). Il est clair'", "(1.6.2) (crop p107_s2a.png)", "(I, 6.2)", "number",
    fx(r"sur $S$ (I, 6.2). Il est clair", r"sur $S$ (1.6.2). Il est clair"), REF1)
add(107, "'sont constructibles dans S (1.8.4)'", "(1.8.4) (crop p107_s2a.png)", "(I, 8.4)", "number",
    fx(r"(I, 8.4)", r"(1.8.4)"), REF1)
add(107, "'par suite (1.9.9) il existe une sous-famille finie'", "(1.9.9) (crop p107_s2a.png)", "(I, 9.9)", "number",
    fx(r"(I, 9.9)", r"(1.9.9)"), REF1)
add(107, "'Soit alors X' le préschéma somme des sous-préschémas induits'", "'somme' italic", "roman", "italics",
    fx(r"le préschéma somme des sous-préschémas induits", r"le préschéma \emph{somme} des sous-préschémas induits"), "")
add(107, "'On peut donc supposer X affine et f de présentation finie'", "'affine' italic", "roman", "italics",
    fx(r"supposer $X$ affine et", r"supposer $X$ \emph{affine} et"), "")
add(107, "'On peut donc supposer de plus S noethérien et f de type fini'", "'noethérien' italic", "roman", "italics",
    fx(r"supposer de plus $S$ noethérien et", r"supposer de plus $S$ \emph{noethérien} et"), "")
add(107, "'raisonnons par récurrence noethérienne (0_I, 2.2.2)'", "bold 0 with subscript I (crop p107_0I.png)", "plain 0", "convention",
    fx(r"($0_{\mathrm I}$, 2.2.2)", r"($\mathbf{0}_{\mathrm I}$, 2.2.2)"), "", convention=2)
add(107, "'ayant pour espace sous-jacent S—(∪_h U_h)'", "long dash for set difference", "minus sign", "convention",
    fx(r"$S-(\bigcup_h U_h)$", r"$S\setmin(\bigcup_h U_h)$"), "", convention=7)
add(107, "'chacun des O_{S,s_h} est un corps k(s_h)'", "'corps' italic (crop p107_s3b.png)", "roman", "italics",
    fx(r"\sh{O}_{S,s_h}$ est un corps", r"\sh{O}_{S,s_h}$ est un \emph{corps}"), "")
add(107, "same: 'k(s_h)'", "bold italic k", "plain k", "convention",
    fx(r"$k(s_h)$. Supposons", r"$\boldsymbol{k}(s_h)$. Supposons"), "", convention=1)
add(107, "'lorsque S est le spectre d'un corps et f est de type fini'", "'spectre d'un corps' italic", "roman", "italics",
    fx(r"est le spectre d'un corps et $f$", r"est le \emph{spectre d'un corps} et $f$"), "")
add(107, "'résulte de la méthode de (8.1.2, a))'", "a) italic, its parenthesis included (crop p107_s3b.png)",
    "$a$) with an upright parenthesis", "italics",
    fx(r"(8.1.2, $a$)) et de (8.8.2", r"(8.1.2, \emph{a)}) et de (8.8.2"), LBL)
add(107, "'il existe dans X un point fermé x (0_I, 2.1.3)'", "bold 0 with subscript I (crop p107_s4.png)", "plain 0", "convention",
    fx(r"($0_{\mathrm I}$, 2.1.3)", r"($\mathbf{0}_{\mathrm I}$, 2.1.3)"), "", convention=2)
add(107, "'donc k(x) est une extension finie de k'", "bold italic k", "plain k", "convention",
    fx(r"donc $k(x)$ est une extension finie de $k$", r"donc $\boldsymbol{k}(x)$ est une extension \emph{finie} de $k$"),
    "One edit for this finding and the next (italics 'finie'): the shorter contexts are not unique in the file.", convention=1)
add(107, "same sentence: 'une extension finie de k (I, 6.4.2)'", "'finie' italic (crop p107_s4.png)", "roman", "italics", None,
    "Covered by the edit of the preceding finding (convention 1), which also sets \\emph{finie}.")
add(107, "'(I, 6.4.2)'", "bold I", "plain I", "convention",
    fx(r"(I, 6.4.2). Il y a", r"(\textbf{I}, 6.4.2). Il y a"), "", convention=2)
add(107, "'telle que k''=k(x) soit extension finie radicielle'", "bold italic k", "plain k", "convention",
    fx(r"$k''=k(x)$", r"$k''=\boldsymbol{k}(x)$"), "", convention=1)

# ======================= page 108 =======================
add(108, "Corollaire (17.16.5), l. 2-3: 'localement de présentation finie et localement quasi-fini,'",
    "'localement quasi-fini' roman inside the italic statement (crop p108_cor5.png)", "italic", "convention",
    fx(r"surjectif, localement de présentation finie et localement quasi-fini",
       r"surjectif, localement de présentation finie et \textup{localement quasi-fini}"), C6, convention=6)
add(108, "Corollaire (17.16.5): '(autrement dit tel qu'il existe une S'-section de X'=X×_S S').'",
    "parenthetical roman, only 'section' italic (crop p108_cor5.png)", "all italic (corollary environment)", "convention",
    fx(r"(autrement dit tel qu'il existe une $S'$-section de $X'=X\times_S S'$).",
       r"\textup{(autrement dit tel qu'il existe une} $S'$-section \textup{de} $X'=X\times_S S'$\textup{)}."),
    C6, convention=6)
add(108, "Corollaire (17.16.5), last sentence: '(resp. quasi-compact et quasi-séparé)' and '(resp. S' affine et le morphisme g de présentation finie et quasi-fini)'",
    "'(resp.' and the closing parentheses roman, the words between italic", "italic", "convention",
    fx(r"(resp. quasi-compact et quasi-séparé), on peut supposer $S'$ affine (resp. $S'$ affine et le morphisme $g$ de présentation finie et quasi-fini).",
       r"\textup{(resp.} quasi-compact et quasi-séparé\textup{)}, on peut supposer $S'$ affine \textup{(resp.} $S'$ affine et le morphisme $g$ de présentation finie et quasi-fini\textup{)}."),
    "Two occurrences in one edit.", convention=6)
add(108, "proof of (17.16.5): 'les immersions S_α→S sont de présentation finie (1.6.2)'", "(1.6.2) (crop p108_s2mid.png)", "(I, 6.2)", "number",
    fx(r"les immersions $S_\alpha\to S$ sont de présentation finie (I, 6.2)", r"les immersions $S_\alpha\to S$ sont de présentation finie (1.6.2)"), REF1)
add(108, "'en prenant S' égal à la somme des S_i''", "'somme' italic (crop p108_s2mid.png)", "roman", "italics",
    fx(r"égal à la somme des", r"égal à la \emph{somme} des"), "")
add(108, "Proposition (17.16.6), l. 3: 'soit un préschéma propre sur k(s)'", "bold italic k", "plain k", "convention",
    fx(r"soit un préschéma propre sur $k(s)$", r"soit un préschéma propre sur $\boldsymbol{k}(s)$"), "", convention=1)
add(108, "Proposition (17.16.6): 'le morphisme X_i=X×_S S_i→S_i soit propre et plat.'",
    "'propre' and 'plat' roman, 'soit' and 'et' italic (crop p108_prop6b.png)", "italic", "convention",
    fx(r"soit propre et plat.", r"soit \textup{propre} et \textup{plat}."), C6, convention=6)
add(108, "Proposition (17.16.6): 'X_s est fini sur k(s), on peut prendre'", "bold italic k", "plain k", "convention",
    fx(r"est fini sur $k(s)$, on peut prendre", r"est fini sur $\boldsymbol{k}(s)$, on peut prendre"), "", convention=1)
add(108, "Proposition (17.16.6), last line: 'localement libres (18.2.7)'", "reference upright (crop p108_prop6b.png)", "italic", "convention",
    fx(r"localement libres (18.2.7)", r"localement libres \textup{(18.2.7)}"), C6, convention=6)
add(108, "proof of (17.16.6): 'au cas où S est affine et où f est plat'", "'affine' and 'plat' italic", "roman", "italics",
    fx(r"où $S$ est affine et où $f$ est plat,", r"où $S$ est \emph{affine} et où $f$ est \emph{plat},"), "")
add(108, "'chaque fibre (X_0)_{s_0} est encore propre sur k(s_0)'", "bold italic k", "plain k", "convention",
    fx(r"propre sur $k(s_0)$", r"propre sur $\boldsymbol{k}(s_0)$"), "", convention=1)
add(108, "'application du procédé de (8.1.2, a))'", "a) italic, its parenthesis included", "$a$) with an upright parenthesis", "italics",
    fx(r"procédé de (8.1.2, $a$))", r"procédé de (8.1.2, \emph{a)})"), LBL)
add(108, "'le cas où X_s est supposé fini sur k(s) pour tout s∈S'", "bold italic k", "plain k", "convention",
    fx(r"fini sur $k(s)$ pour tout", r"fini sur $\boldsymbol{k}(s)$ pour tout"), "", convention=1)
add(108, "'A est une k-algèbre finie (I, 6.4.4)'", "bold I", "plain I", "convention",
    fx(r"(I, 6.4.4)", r"(\textbf{I}, 6.4.4)"), "", convention=2)
add(108, "page break 108/109 inside 'puisque A_j est un anneau artinien et une | k-algèbre'",
    "p. 108 ends 'et une' (no stop); p. 109 continues the sentence ('k-algèbre, il contient', no indent)",
    "blank line before \\oldpage[IV-4]{109} (and another after it): a paragraph break inside the sentence",
    "marker", fx(r"anneau artinien et une⏎⏎", r"anneau artinien et une⏎"),
    "The marker is at the right place. Part 1 of 2: the first p. 109 finding removes the blank line after \\oldpage[IV-4]{109}; apply both.")

# ======================= page 109 =======================
add(109, "top of page_109.tex: blank line after \\oldpage[IV-4]{109}",
    "p. 109 begins mid-sentence ('k-algèbre, il contient', no indent)", "blank line between the marker and '$k$-algèbre'",
    "marker", fx(r"\oldpage[IV-4]{109}⏎⏎$k$-algèbre", r"\oldpage[IV-4]{109}⏎$k$-algèbre"),
    "Part 2 of 2 with the last p. 108 finding; both blank lines must go.")
add(109, "'au corps résiduel de A_j (0, 19.6.2)'", "bold 0", "plain 0", "convention",
    fx(r"(0, 19.6.2)", r"(\textbf{0}, 19.6.2)"), "", convention=2)
add(109, "'deux homomorphismes K'_j→A_j→k(A_j)'", "bold italic k", "plain k", "convention",
    fx(r"A_j\to k(A_j)", r"A_j\to\boldsymbol{k}(A_j)"), "", convention=1)
add(109, "Proposition (18.1.1), l. 2: 'un S_0-préschéma lisse (resp. étale) sur S_0'",
    "'(resp.' and ')' roman, 'étale' italic (crop p109_prop1811.png)", "italic", "convention",
    fx(r"lisse (resp. étale) sur $S_0$, $x_0$ un point", r"lisse \textup{(resp.} étale\textup{)} sur $S_0$, $x_0$ un point"),
    C6 + PRE18, convention=6, src='18')
add(109, "Proposition (18.1.1), l. 3: 'un S-préschéma U lisse (resp. étale) sur S'",
    "'(resp.' and ')' roman, 'étale' italic", "italic", "convention",
    fx(r"$U$ lisse (resp. étale) sur $S$ et un", r"$U$ lisse \textup{(resp.} étale\textup{)} sur $S$ et un"),
    C6 + PRE18, convention=6, src='18')
add(109, "Proposition (18.1.1), end: 'un S_0-isomorphisme U×_S S_0 ⥲ U_0.'",
    "the isomorphism is set in the running text at the end of the statement's last line (crop p109_prop1811.png)",
    "displayed with \\[ ... \\]", "other",
    fx(r"isomorphisme⏎\[⏎  U\times_S S_0\xrightarrow{\sim}U_0.⏎\]⏎\end{proposition}",
       r"isomorphisme $U\times_S S_0\xrightarrow{\sim}U_0$.⏎\end{proposition}"),
    "Layout only (display vs inline); the formula matches." + PRE18, src='18')
add(109, "proof of (18.1.1): 'il est a fortiori non ramifié sur S_0'", "'a fortiori' italic", "roman", "italics",
    fx(r"il est a fortiori non ramifié", r"il est \emph{a fortiori} non ramifié"), PRE18.strip(), src='18')
add(109, "'non ramifié sur S au point x_0 (17.4.1, d))'", "d) italic, its parenthesis included", "$d$) with an upright parenthesis", "italics",
    fx(r"au point $x_0$ (17.4.1, $d$))", r"au point $x_0$ (17.4.1, \emph{d)})"), LBL + PRE18, src='18')
add(109, "'Le critère jacobien (0, 22.6.4)'", "bold 0", "plain 0", "convention",
    fx(r"jacobien (0, 22.6.4)", r"jacobien (\textbf{0}, 22.6.4)"), PRE18.strip(), convention=2, src='18')
add(109, "'joint à (0, 19.1.12)'", "bold 0", "plain 0", "convention",
    fx(r"joint à (0, 19.1.12)", r"joint à (\textbf{0}, 19.1.12)"), PRE18.strip(), convention=2, src='18')
add(109, "display (18.1.1.1): 'det(∂u_i/∂T_{j_h}) ∉ q_0'",
    "the derivative is written with a solidus, ∂u_i/∂T_{j_h}, in plain parentheses (crop p109_det.png)",
    "\\det\\left(\\frac{\\partial u_i}{\\partial T_{j_h}}\\right): built-up fraction", "formula",
    fx(r"\det\left(\frac{\partial u_i}{\partial T_{j_h}}\right)\notin\mathfrak q_0.",
       r"\det(\partial u_i/\partial T_{j_h})\notin\mathfrak q_0."),
    "The blot on the subscript h is an inking defect, not reported." + PRE18, src='18')
add(109, "after (18.1.1.1): 'Comme (B_0)_{q_0} est un anneau local'",
    "'Comme' starts at the left margin without indent: the paragraph continues after the display (page_109_s4.png)",
    "blank line after \\end{equation}: a new indented paragraph", "extra",
    fx(r"\end{equation}⏎⏎Comme $(B_0)_{\mathfrak q_0}$", r"\end{equation}⏎Comme $(B_0)_{\mathfrak q_0}$"),
    "Paragraph break the print does not have." + PRE18, src='18')
add(109, "'que les u_i engendrent J_0 (0_I, 5.2.2)'", "bold 0 with subscript I", "plain 0", "convention",
    fx(r"engendrent $\mathfrak J_0$ ($0_{\mathrm I}$, 5.2.2)", r"engendrent $\mathfrak J_0$ ($\mathbf{0}_{\mathrm I}$, 5.2.2)"),
    PRE18.strip(), convention=2, src='18')
add(109, "page break 109/110 inside 'B_0 est donc un anneau quotient | de B'",
    "p. 109 ends 'anneau quotient' (no stop); the sentence continues on p. 110",
    "blank line before \\oldpage[IV-4]{110} (and another after it): a paragraph break inside the sentence",
    "marker", fx(r"$B_0$ est donc un anneau quotient⏎⏎", r"$B_0$ est donc un anneau quotient⏎"),
    "The marker is at the right place. The blank line AFTER \\oldpage[IV-4]{110} (before 'de $B$', in the p. 110 segment) must go too; it lies in the p. 110 batch and is not reported here." + PRE18, src='18')

# ----------------------- checks -----------------------
ok = True
for d in F:
    if d['fix'] is None:
        continue
    old = d['fix']['old']
    pc = page_text(d['page']).count(old)
    s = S17 if d['_src'] == '17' else S18
    sc = s.count(old)
    if pc != 1 or sc != 1:
        ok = False
        print('COUNT PROBLEM p%d page=%d src=%d: %r' % (d['page'], pc, sc, old))

# overlap check per source file (positions in the current source)
for name, s in (('17', S17), ('18', S18)):
    spans = []
    for d in F:
        if d['fix'] is None or d['_src'] != name:
            continue
        old = d['fix']['old']
        i = s.find(old)
        if i >= 0:
            spans.append((i, i + len(old), d['page'], old[:40]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print('OVERLAP', a, b)

# apply all fixes to copies (in memory) and to a preview of the corrected edition (misprint fixes skipped)
def apply(s, which, skip_misprints=False):
    for d in F:
        if d['fix'] is None or d['_src'] != which:
            continue
        if skip_misprints and d['kind'] == 'misprint_in_print':
            continue
        assert s.count(d['fix']['old']) == 1, d['fix']['old']
        s = s.replace(d['fix']['old'], d['fix']['new'], 1)
    return s

prev17 = apply(S17, '17'); prev18 = apply(S18, '18')
cor17 = apply(S17, '17', True); cor18 = apply(S18, '18', True)
i = prev17.find('\\oldpage[IV-4]{105}')
j = prev18.find('\\oldpage[IV-4]{110}')
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'applied_preview.txt'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(prev17[i - 200:] + '\n% ---- ega4-18 ----\n' + prev18[:j + 40])
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'corrected_preview.txt'), 'w', encoding='utf-8', newline='\n') as f:
    k = cor17.find('\\oldpage[IV-4]{105}')
    f.write(cor17[k - 200:] + '\n% ---- ega4-18 ----\n' + cor18[:cor18.find('\\oldpage[IV-4]{110}') + 40])

out = []
for d in F:
    e = dict(d); e.pop('_src')
    out.append(e)
with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

from collections import Counter
cnt = Counter()
for d in F:
    k = 'misprint' if d['kind'] == 'misprint_in_print' else ('convention' if d['kind'] == 'convention' else 'normal')
    cnt[(d['page'], k)] += 1
for p in range(105, 110):
    print(p, cnt[(p, 'normal')], cnt[(p, 'convention')], cnt[(p, 'misprint')])
print('OK' if ok else 'PROBLEMS', len(F))
