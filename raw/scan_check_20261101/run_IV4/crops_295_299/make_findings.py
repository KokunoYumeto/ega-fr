import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-21b-fr.tex"
OUT = os.path.join(RUN, "findings_295_299.json")

NL = "\n"


def L(s):
    """raw LaTeX with <NL> for line breaks"""
    return s.replace("<NL>", NL)


F = []


def add(page, where, scan, tex, kind, fix, note="", convention=None, confidence="high", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": convention, "confidence": confidence,
         "fix": None if fix is None else {"old": L(fix[0]), "new": L(fix[1])}}
    if kind == "misprint_in_print":
        d["corrected"] = L(corrected) if corrected is not None else None
    d["note"] = note
    F.append(d)


# ---------------- page 295 ----------------
add(295, "display after 'et d'autre part, pour i ≥ 2,': '0 = Tor_i^A(M, A) → Tor_i^A(M, A/tA) → Tor_{i-1}^A(M, A) = 0'",
    "no punctuation after the final '= 0' (crop p295_disp1end.png)",
    "comma after '=0'", "punctuation",
    (r"\operatorname{Tor}_{i-1}^A(M,A)=0,<NL>\]", r"\operatorname{Tor}_{i-1}^A(M,A)=0<NL>\]"))

add(295, "l. 9: 'et cette suite s'écrit, d'après ce qui précède' (before the display)",
    "no comma after 'précède' (crop p295_precede.png)",
    "'précède,'", "punctuation",
    (r"d'après ce qui précède,<NL>\[", r"d'après ce qui précède<NL>\["))

add(295, "display '0 → N_t(M') → N_t(M) → N_t(M'') → P_t(M') → P_t(M) → P_t(M'') → 0'",
    "no comma at the end (crop p295_disp3end.png)",
    "comma after the final '\\to0'", "punctuation",
    (r"\to P_t(M'')\to0,<NL>\]", r"\to P_t(M'')\to0<NL>\]"))

add(295, "(iv), last sentence: 'd_t(M) = d_t(A^n) = n.d_t(A) = n.long(A/tA)'",
    "baseline periods after both n (crop p295_ndot.png)",
    "n\\cdot d_t(A)=n\\cdot\\operatorname{long}(A/tA)", "symbol",
    (r"d_t(A^n)=n\cdot d_t(A)=n\cdot\operatorname{long}(A/tA)", r"d_t(A^n)=n.d_t(A)=n.\operatorname{long}(A/tA)"),
    "Baseline period in the print (GLOBAL_ISSUES 65), written as in the IV-4 page fixes (p. 271: n_x.).")

add(295, "heading 'Proposition (21.10.13)' (after 'Ce lemme permet de généraliser (21.10.4) :')",
    "the proposition is numbered (21.10.13), the number of Lemme (21.10.13) on p. 294 (crop p294_lemma.png; page_295_s3.png)",
    "\\begin{proposition}[21.10.13] with \\label{IV.21.10.13bis}: keeps the printed number", "misprint_in_print",
    None,
    "Two statements carry the number (21.10.13) in the print: the lemma (p. 294) and this proposition; (21.10.14) follows. "
    "'(21.10.13, (v))' on p. 296 refers to the lemma; the TeX resolves the reference on p. 302 (\\sref{IV.21.10.13bis}) to the "
    "proposition. Not in the IV-4 errata list. The diplomatic text keeps the printed number (fix null).",
    confidence="high",
    corrected=r"a number distinct from the lemma's, e.g. \begin{proposition}[21.10.13 bis] (editorial choice, not a printed or errata reading)")

# ---------------- page 296 ----------------
add(296, "l. 7: 'on peut appliquer (21.10.13, (v)) à M = A''",
    "'(21.10.13, (v))', the item label inside the reference's parentheses (crop p296_ref13v.png)",
    "\\sref{IV.21.10.13}, (v) prints '(21.10.13), (v)'", "punctuation",
    (r"\sref{IV.21.10.13}, (v)", r"\sref{IV.21.10.13}[(v)]"),
    "\\sref's third argument (GLOBAL_ISSUES 68).")

add(296, "l. 8: 'la longueur de A'/t_yA' en tant que A-module est donc r_{x'}n_y'",
    "'module' italic (crop p296_Amodule.png)",
    "upright", "italics",
    (r"en tant que $A$-module est donc", r"en tant que $A$-\emph{module} est donc"))

add(296, "l. 10: 'la longueur de A'/t_yA' en tant que A'-module est donc'",
    "'module' italic (crop p296_Aprimemodule.png)",
    "upright", "italics",
    (r"en tant que $A'$-module est donc", r"en tant que $A'$-\emph{module} est donc"))

add(296, "(21.10.14), l. 2: 'un morphisme ayant les deux propriétés suivantes :'",
    "only 'deux' is italic; 'propriétés' is roman (crop p296_deux.png)",
    "\\emph{deux propriétés}", "italics",
    (r"\emph{deux propriétés} suivantes", r"\emph{deux} propriétés suivantes"))

add(296, "(21.10.14) a): 'f est fini;'",
    "'fini' italic (crop p296_afini.png)",
    "upright", "italics",
    (r"\item $f$ est fini;", r"\item $f$ est \emph{fini};"))

add(296, "(21.10.14), after the items a), b): 'Pour tout x ∈ X^(1), les points x' ∈ f^{-1}(x) appartiennent'",
    "new paragraph, indented like the item labels (page_296_s2.png)",
    "the text follows \\end{enumerate} without a blank line, so it is set without the indent", "other",
    (r"\end{enumerate}<NL>Pour tout $x\in X^{(1)}$, les points", r"\end{enumerate}<NL><NL>Pour tout $x\in X^{(1)}$, les points"),
    "GLOBAL_ISSUES 80/99 pattern.")

add(296, "display 'Z' = Σ_{x'∈X'^(1)} n_{x'}.{x'}‾'",
    "baseline period after n_{x'} (crop p296_Zdisp.png)",
    "\\cdot", "symbol",
    (r"n_{x'}\cdot\overline{\{x'\}}", r"n_{x'}.\overline{\{x'\}}"),
    "Baseline period in the print (GLOBAL_ISSUES 65), as the IV-4 page fixes write it.")

add(296, "display 'n_x = Σ_{x'∈f^{-1}(x)} n_{x'}.[k(x') : k(x)]'",
    "baseline period after n_{x'}; no comma at the end (crops p296_nxdisp.png, p296_nxdisp2.png)",
    "\\cdot and a final comma", "symbol",
    (r"n_{x'}\cdot[\boldsymbol{k}(x'): \boldsymbol{k}(x)],<NL>", r"n_{x'}.[\boldsymbol{k}(x'): \boldsymbol{k}(x)]<NL>"),
    "Baseline period in the print (GLOBAL_ISSUES 65); the same edit drops the comma the print lacks.")

add(296, "display (21.10.14.1): 'f_*(Z') = Σ_{x∈X^(1)} n_x.{x}‾'",
    "baseline period after n_x (crop p296_fZdisp2.png)",
    "\\cdot", "symbol",
    (r"f_*(Z')=\sum_{x\in X^{(1)}}n_x\cdot\overline{\{x\}}", r"f_*(Z')=\sum_{x\in X^{(1)}}n_x.\overline{\{x\}}"),
    "Baseline period in the print (GLOBAL_ISSUES 65).")

add(296, "display (21.10.14.2): '(f_U)_*(Z'|f^{-1}(U)) = f_*(Z')|U'",
    "no comma at the end (crop p296_disp142b.png)",
    "comma after 'f_*(Z')|U'", "punctuation",
    (r"=f_*(Z')|U,<NL>", r"=f_*(Z')|U<NL>"))

add(296, "end of the page: printed p. 296 ends with 'ψ_*(Z^1_{X'}) → Z^1_X.'; Proposition (21.10.15) begins p. 297",
    "page_296_s4.png ends with the display ψ_*(...) → Z^1_X.; page_297_s1.png begins with 'Proposition (21.10.15). — Soient X, X', X''...'",
    "\\oldpage[IV-4]{297} stands after \\begin{proposition}[21.10.15]\\label{IV.21.10.15}, so the heading falls in the p. 296 segment", "marker",
    (r"\end{env}<NL><NL>\begin{proposition}[21.10.15]", r"\end{env}<NL><NL>\oldpage[IV-4]{297}<NL>\begin{proposition}[21.10.15]"),
    "Marker move, part 1 of 2: inserts the marker before (21.10.15) (as at (20.2.2), (20.3.13)). Apply together with the first p. 297 entry, "
    "which removes the old marker; either order works, and each 'old' stays unique after the other is applied.")

# ---------------- page 297 ----------------
add(297, "top of the page: old position of \\oldpage[IV-4]{297}",
    "p. 297 begins with 'Proposition (21.10.15). —' (page_297_s1.png)",
    "marker after \\begin{proposition}[21.10.15]\\label{IV.21.10.15}", "marker",
    (r"\oldpage[IV-4]{297}<NL>Soient $X$, $X'$, $X''$", r"Soient $X$, $X'$, $X''$"),
    "Marker move, part 2 of 2: removes the old marker. Apply together with the last p. 296 entry.")

add(297, "Proposition (21.10.15), end: 'on a (f∘g)_*(Z'') = f_*(g_*(Z'')).'",
    "the formula is set in the line (last line of the statement, flush with the left margin) (crop p297_fg.png)",
    "displayed", "formula",
    (r"on a<NL>\[<NL>  (f\circ g)_*(Z'')=f_*(g_*(Z'')).<NL>\]", r"on a $(f\circ g)_*(Z'')=f_*(g_*(Z''))$."),
    "Formula displayed in the TeX where the print sets it in the line.")

add(297, "Proposition (21.10.16), l. 4: 'les projections canoniques. Alors, f_1 vérifie les conditions a) et b)'",
    "comma after 'Alors' (crop p297_alors.png)",
    "no comma", "punctuation",
    (r"Alors $f_1$ vérifie", r"Alors, $f_1$ vérifie"))

add(297, "Proposition (21.10.16), l. 5: 'et pour tout 1-cycle codimensionnel Z' sur X''",
    "'1-cycle codimensionnel' (crop p297_1cycle.png)",
    "'$1$-cycle codimensionnel' (keeps the printed reading)", "misprint_in_print",
    None,
    "Word order: the text everywhere else (27 times in ega4-21b, e.g. (21.10.14), (21.10.15)) has 'cycle 1-codimensionnel'; "
    "'1-cycle codimensionnel' occurs only here. The TeX keeps the printed reading (fix null).",
    confidence="medium",
    corrected=r"et pour tout cycle $1$-codimensionnel $Z'$ sur $X'$")

add(297, "display after 'Comme on a': '[k(x'_1) : k(x')].[k(x') : k(x)] = [k(x'_1) : k(x_1)].[k(x_1) : k(x)]'",
    "baseline periods between the brackets, and no comma at the end (crop p297_degdisp.png)",
    "\\cdot twice and a final comma", "symbol",
    (r"[\boldsymbol{k}(x'_1):\boldsymbol{k}(x')]\cdot[\boldsymbol{k}(x'):\boldsymbol{k}(x)]<NL>  =[\boldsymbol{k}(x'_1):\boldsymbol{k}(x_1)]\cdot[\boldsymbol{k}(x_1):\boldsymbol{k}(x)],<NL>",
     r"[\boldsymbol{k}(x'_1):\boldsymbol{k}(x')].[\boldsymbol{k}(x'):\boldsymbol{k}(x)]<NL>  =[\boldsymbol{k}(x'_1):\boldsymbol{k}(x_1)].[\boldsymbol{k}(x_1):\boldsymbol{k}(x)]<NL>"),
    "Baseline periods (GLOBAL_ISSUES 65); the same edit drops the comma the print lacks.")

add(297, "display after 's'écrit aussi': '... long_{A'}(A'_1/m_{x'}A'_1) = long_{A_1}(A'_1/m_{x'}A'_1)'",
    "no comma at the end (crop p297_fracdisp.png)",
    "comma at the end", "punctuation",
    (r"=\operatorname{long}_{A_1}(A'_1/\mathfrak{m}_{x'}A'_1),<NL>\]", r"=\operatorname{long}_{A_1}(A'_1/\mathfrak{m}_{x'}A'_1)<NL>\]"))

add(297, "l. after the fraction display: 'On a donc A'_1/m_{x'}A'_1 = (A'/m_{x'})⊗_A A_1'",
    "'(A'/m_{x'})' (crop p297_ondonc.png)",
    "(A'/\\mathfrak{m}_{x'}A')", "formula",
    (r"=(A'/\mathfrak{m}_{x'}A')\otimes_AA_1", r"=(A'/\mathfrak{m}_{x'})\otimes_AA_1"),
    "The TeX rewrites the printed notation (A' is local, A'/m_{x'} = A'/m_{x'}A'); not a misprint. Same in the next display.")

add(297, "last display, first line: 'long_A(A'/m_{x'})long_{A_1}(A_1/mA_1)'",
    "'long_A(A'/m_{x'})' (crop p297_longdisp.png)",
    "\\operatorname{long}_{A}(A'/\\mathfrak{m}_{x'}A')", "formula",
    (r"\operatorname{long}_{A}(A'/\mathfrak{m}_{x'}A')", r"\operatorname{long}_{A}(A'/\mathfrak{m}_{x'})"),
    "As in the entry above. Apply before the next (misprint) entry; the two edits are adjacent and do not overlap.")

add(297, "last display, first line: 'long_{A_1}(A_1/mA_1)'",
    "bare m without the subscript x (crops p297_mA1.png; the definition three lines above reads λ_{x_1} = long(A_1/m_xA_1), crop p297_lambdax1.png)",
    "\\mathfrak{m}_xA_1 (silent correction)", "misprint_in_print",
    (r"\operatorname{long}_{A_1}(A_1/\mathfrak{m}_xA_1)", r"\operatorname{long}_{A_1}(A_1/\mathfrak{m}A_1)"),
    "The factor is λ_{x_1} = long(A_1/m_xA_1) (the display ends with λ_{x_1}); the print drops the subscript x. The TeX silently supplies it: "
    "restore the printed reading. List after the formula entry above (adjacent, no overlap).",
    confidence="medium",
    corrected=r"\operatorname{long}_{A_1}(A_1/\mathfrak{m}_xA_1)")

add(297, "last display, second line: '= [k(x') : k(x)].λ_{x_1}'",
    "baseline period before λ_{x_1}; no comma at the end (crop p297_longdisp.png)",
    "\\cdot and a final comma", "symbol",
    (r"\boldsymbol{k}(x)]\cdot\lambda_{x_1},<NL>", r"\boldsymbol{k}(x)].\lambda_{x_1}<NL>"),
    "Baseline period (GLOBAL_ISSUES 65); the same edit drops the comma the print lacks.")

# ---------------- page 298 ----------------
add(298, "l. 1: 'A-algèbre qui est un A-module libre de rang fini'",
    "'libre' italic (crop p298_libre.png)",
    "upright", "italics",
    (r"qui est un $A$-module libre de rang fini", r"qui est un $A$-module \emph{libre} de rang fini"))

add(298, "l. 6: 'où x'_i (1≤i≤r) sont les points de X' au-dessus de x'",
    "no article before x'_i (crop p298_ouxi.png)",
    "'où les $x'_i$'", "extra",
    (r"où les $x'_i$ $(1\leq i\leq r)$ sont", r"où $x'_i$ $(1\leq i\leq r)$ sont"),
    "Word added by the TeX.")

add(298, "l. 8: 'comme le produit long_{A'_i}(A'_i/t'_iA'_i).[k(x'_i) : k(x)]'",
    "baseline period (crop p298_proddot.png)",
    "\\cdot", "symbol",
    (r"(A'_i/t'_iA'_i)\cdot[\boldsymbol{k}(x'_i):\boldsymbol{k}(x)]", r"(A'_i/t'_iA'_i).[\boldsymbol{k}(x'_i):\boldsymbol{k}(x)]"),
    "Baseline period in the print (GLOBAL_ISSUES 65).")

add(298, "after (21.10.17.2): 'Cette relation découle du lemme plus général suivant :'",
    "colon at the end (crop p298_suivant.png)",
    "full stop", "punctuation",
    (r"du lemme plus général suivant.", r"du lemme plus général suivant:"))

add(298, "proof of (21.10.17.3), case I): 'I) A est un anneau de valuation discrète.'",
    "'est un anneau de valuation discrète' italic (crop p298_I.png)",
    "upright", "italics",
    (r"I) $A$ est un anneau de valuation discrète.", r"I) $A$ \emph{est un anneau de valuation discrète}."))

add(298, "case I), l. 4: 'donc a pour longueur m = Σ_{i=1}^n m_i, et det(u) est produit'",
    "comma after m_i (crop p298_summi.png)",
    "no comma", "punctuation",
    (r"$m=\sum_{i=1}^nm_i$ et", r"$m=\sum_{i=1}^nm_i$, et"))

add(298, "case I), l. 4: 'est produit d'un élément inversible et de t^m'",
    "t^m (crop p298_tm.png)",
    "\\pi^m (silent correction)", "misprint_in_print",
    (r"et de $\pi^m$, d'où", r"et de $t^m$, d'où"),
    "π is the uniformizer of A and det(u) is a unit times π^m (π^{m_i} are the invariant factors); the print has t. "
    "The TeX silently corrects it: restore the printed reading.",
    confidence="high",
    corrected=r"et de $\pi^m$, d'où")

add(298, "case II), l. 1: 'II) A est un anneau complet intègre (de dimension 1).'",
    "'est un anneau complet intègre (de dimension' italic, parentheses included; the figure 1 roman (crops p298_II.png, p298_paren_dedim.png against the upright parentheses of p298_paren_0.png)",
    "upright", "italics",
    (r"II) $A$ est un anneau complet intègre (de dimension $1$).", r"II) $A$ \emph{est un anneau complet intègre (de dimension $1$)}."),
    "Independent of the next entry (same line, no overlap).")

add(298, "case II), l. 1: 'On sait alors (0, 19.8.8, (ii)) qu'il y a'",
    "'(0, 19.8.8, (ii))', bold 0, the item inside the parentheses (crop p298_paren_0.png)",
    "'$(\\mathbf{0},19.8.8)$, (ii)' prints '(0, 19.8.8), (ii)'", "punctuation",
    (r"$(\mathbf{0},19.8.8)$, (ii)", r"\sref[0]{0.19.8.8}[(ii)]"),
    "\\sref[0]{...}[(ii)] prints '(0, 19.8.8, (ii))' with the bold 0, as \\sref[0]{0.16.5.1} elsewhere in ega4-21b.")

add(298, "case II), l. 4: 'il est libre (Bourbaki, Alg. comm., chap. VI'",
    "'libre' italic (crop p298_libre2.png)",
    "upright", "italics",
    (r"il est libre (Bourbaki", r"il est \emph{libre} (Bourbaki"))

add(298, "after (21.10.17.5): 'Mais on a (Bourbaki, Alg., chap. VIII, § 12, n° 2, prop. 7)'",
    "new indented paragraph after the display (crop p298_mais.png)",
    "no blank line after \\], so the line is set without the indent", "other",
    (r"\]<NL>Mais on a (Bourbaki", r"\]<NL><NL>Mais on a (Bourbaki"),
    "GLOBAL_ISSUES 47 pattern (paragraph break after a display).")

add(298, "l. 3 from the end: 'l'homothétie x ⇝ (det u)x du B-module libre A'",
    "wavy arrow (crop p298_wavy.png)",
    "\\mapsto", "symbol",
    (r"$x\mapsto(\det u)x$", r"$x\leadsto(\det u)x$"),
    "GLOBAL_ISSUES 109 (ega4-21 \\mapsto for the print's wavy arrows).")

# ---------------- page 299 ----------------
add(299, "case III), l. 1: 'III) A est un anneau complet.'",
    "'est un anneau complet' italic (crop p299_III.png)",
    "upright", "italics",
    (r"III) $A$ est un anneau complet.", r"III) $A$ \emph{est un anneau complet}."))

add(299, "l. 6: 'tel que Ker v et Coker v soient de longueur finie, on posera'",
    "'longueur finie' italic (crop p299_dans.png)",
    "upright", "italics",
    (r"soient de longueur finie, on posera", r"soient de \emph{longueur finie}, on posera"))

add(299, "display 'χ(N, v) = long_R(Ker(v)) — long_R(Coker(v)).'",
    "long dash for the subtraction (crop p299_chidef.png)",
    "minus sign", "convention",
    (r"(\operatorname{Ker}(v))-\operatorname{long}_R", r"(\operatorname{Ker}(v))\setmin\operatorname{long}_R"),
    "Long dash used for subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.",
    convention=7)

add(299, "after the χ display: 'On notera que l'hypothèse sur v revient à dire que le complexe'",
    "new indented paragraph after the display (crop p299_onnotera.png)",
    "no blank line after \\], so the line is set without the indent", "other",
    (r"\]<NL>On notera que l'hypothèse", r"\]<NL><NL>On notera que l'hypothèse"),
    "GLOBAL_ISSUES 47 pattern (paragraph break after a display).")

add(299, "display 'K^0 : 0 → N →^v N → 0'",
    "superscript lining 0 on K (crop p299_K0.png)",
    "K^0 (keeps the printed reading)", "misprint_in_print",
    None,
    "The complex 0 → N → N → 0 is meant (degrees 0 and 1); (0_III, 11.10), which the next line cites, writes complexes M^• and "
    "χ(M^•) = χ(H^•(M^•)) (11.10.2). The raised bullet is printed as 0 here and in the next entry. The TeX keeps the printed reading (fix null).",
    confidence="medium",
    corrected=r"K^\bullet:0\to N\xrightarrow{v}N\to0")

add(299, "l. after the K^0 display: 'et que χ(N, v) = χ(H^0(K^0)) (0_III, 11.10)'",
    "χ(H^0(K^0)), lining 0s (crop p299_chiH.png)",
    "\\chi(H^0(K^0)) (keeps the printed reading)", "misprint_in_print",
    None,
    "χ(N, v) = long Ker v − long Coker v is the Euler–Poincaré characteristic of the cohomology complex H^•(K^•) of (0_III, 11.10.2); "
    "χ of the single module H^0 is not defined there. Same misprint as the entry above. The TeX keeps the printed reading (fix null).",
    confidence="medium",
    corrected=r"$\chi(N,v)=\chi(H^\bullet(K^\bullet))$")

add(299, "commutative diagram before (21.10.17.6): labels v', v of the left and middle vertical arrows",
    "v' and v stand LEFT of their arrows, v'' right of its arrow (crop p299_diag.png)",
    "\\ar[d]^{v'} and \\ar[d]^v put them on the right", "other",
    (r"\ar[d]^{v'} & N \ar[r]^s \ar[d]^v &", r"\ar[d]_{v'} & N \ar[r]^s \ar[d]_v &"),
    "In xymatrix ^ puts the label of a downward arrow on its right, _ on its left (cf. GLOBAL_ISSUES 30); \\ar[d]^{v''} is right.")

add(299, "l. after (21.10.17.6): 'Enfin, si N est un R-module de longueur finie, on a χ(N, v) = 0.'",
    "'longueur finie' italic (crop p299_enfin.png)",
    "upright", "italics",
    (r"$R$-module de longueur finie, on a", r"$R$-module de \emph{longueur finie}, on a"))

add(299, "'Avec ces notations, on a le lemme suivant :'",
    "colon at the end (crop p299_enfin.png)",
    "full stop", "punctuation",
    (r"on a le lemme suivant.", r"on a le lemme suivant:"))

add(299, "display (21.10.17.8): 'χ(M, u) = Σ_{i=1}^n long(A_{p_i}).χ(M_i, u_i).'",
    "baseline period before χ (crop p299_sum8.png)",
    "\\cdot", "symbol",
    (r"\operatorname{long}(A_{\mathfrak{p}_i})\cdot\chi(M_i,u_i)", r"\operatorname{long}(A_{\mathfrak{p}_i}).\chi(M_i,u_i)"),
    "Baseline period in the print (GLOBAL_ISSUES 65).")

add(299, "proof of (21.10.17.7), l. 4: 'où M'' est de longueur finie : en effet'",
    "'longueur finie' italic (crop p299_finie.png)",
    "upright", "italics",
    (r"où $M''$ est de longueur finie:", r"où $M''$ est de \emph{longueur finie}:"))

add(299, "proof of (21.10.17.7), l. 5: 'car (q_i)_{p_i} = 0 et (q_i)_{p_j} = A_{p_j} pour j ≠ i'",
    "(q_i)_{p_j} = A_{p_j} (crop p299_qi.png)",
    "(\\mathfrak{q}_j)_{\\mathfrak{p}_i}=A_{\\mathfrak{p}_i}", "formula",
    (r"$(\mathfrak{q}_j)_{\mathfrak{p}_i}=A_{\mathfrak{p}_i}$", r"$(\mathfrak{q}_i)_{\mathfrak{p}_j}=A_{\mathfrak{p}_j}$"),
    "The TeX swaps the printed indices (both forms are correct for j ≠ i); restore the print's (GLOBAL_ISSUES 102/104 pattern).")


# ---------------- checks ----------------
src = open(SRC, encoding="utf-8", newline="").read()
pages = {}
for n in range(295, 300):
    # page files have CRLF; compare with LF as in the release files
    pages[n] = open(os.path.join(RUN, "page_%03d.tex" % n), encoding="utf-8", newline="").read().replace("\r\n", "\n")

bad = 0
for i, d in enumerate(F):
    if d["fix"] is None:
        continue
    old = d["fix"]["old"]
    cp = pages[d["page"]].count(old)
    cs = src.count(old)
    if cp != 1 or cs != 1:
        bad += 1
        print("NOT UNIQUE", i, d["page"], d["where"][:60], "page:", cp, "src:", cs)
print("findings:", len(F), "bad:", bad)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print("written", OUT)
