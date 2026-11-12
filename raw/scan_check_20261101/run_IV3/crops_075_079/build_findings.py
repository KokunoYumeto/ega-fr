import json, sys

RUN = r"user\Documents\ega_scan_check_20261101\run_IV3"
OUT = RUN + r"\findings_075_079.json"

F = []


def add(page, where, scan, tex, kind, fix, note="", convention=None, confidence="high", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": convention, "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


SETMIN = "\\setmin pending the convention-7 decision (FIX_POLICY 2.7)."
KSUB = ("Bold upright k in the subscript (enlarged crop), bold italic only on the line (GLOBAL_ISSUES 48); "
        "the TeX has bold italic \\boldsymbol{k}.")

# ---------------------------------------------------------------- p. 75
add(75, "case 1 of E', end: 'ce qui prouve dans ce cas que S—E' est un voisinage de η'",
    "S—E' (long dash)", "$S-E'$", "convention",
    fx(r"$S-E'$", r"$S\setmin E'$"), SETMIN, convention=7)

add(75, "case 2 of E', first sentence: 'mais que le morphisme X→P((f_*(L))_η) ne soit pas une immersion'",
    "X→P((f_*(𝓛))_η): X without the subscript η (enlarged crop p75_s2_XP.png)",
    r"$X_\eta\to\mathbf P((f_*(\mathcal L))_\eta)$", "misprint_in_print",
    fx(r"$X_\eta\to\mathbf P", r"$X\to\mathbf P"),
    "The morphism of the generic fibre is meant (cf. X_s→P((f_*(𝓛))_s) two lines below). The TeX silently "
    "corrects the print; the diplomatic text restores the printed X.",
    corrected=r"$X_\eta\to\mathbf P((f_*(\mathcal L))_\eta)$", confidence="high")

add(75, "case 2 of E', end: 'n'est pas une immersion ce qui achève la démonstration dans le cas de E''",
    "no comma after 'immersion' (line end; enlarged crops p75_s2_immersion*.png)",
    "immersion, ce qui achève", "misprint_in_print",
    fx("immersion, ce qui achève", "immersion ce qui achève"),
    "Comma dropped in the print (the parallel sentence above has ', ce qui prouve'). The TeX silently "
    "supplies it; the diplomatic text follows the print.",
    corrected="immersion, ce qui achève", confidence="medium")

add(75, "Corollaire (9.6.4), first words",
    "'Soient f : X→S un morphisme propre ..., 𝓛 un 𝒪_X-Module inversible'",
    "Soit $f:X\\to S$", "word",
    fx(r"Soit $f:X\to S$ un", r"Soient $f:X\to S$ un"), "Enlarged crop p75_s2_propre.png.")

add(75, "Corollaire (9.6.4): 'un morphisme propre de présentation finie'",
    "'propre' upright (roman) inside the italic statement (enlarged crop p75_s2_propre2.png)",
    "propre (italic in the corollary environment)", "convention",
    fx("morphisme propre de", r"morphisme \textup{propre} de"), "", convention=6)

add(75, "proof of (9.6.4): 'vérifiée par la propriété P définie plus haut'",
    "bold italic P (enlarged crop)", r"$\mathbf P$", "convention",
    fx(r"$\mathbf P$ définie", r"$\boldsymbol{P}$ définie"),
    "Property letter. The projective P of P((f_s)_*(𝓛_s)) etc. on this page is bold upright and correct as \\mathbf P.",
    convention=10)

add(75, "heading (9.6.6)",
    "'(9.6.6)' bold, 'Fin de la démonstration de' italic, '(9.6.3).' roman (enlarged crop p75_s3_heading.png)",
    r"\textbf{(9.6.6) Fin de la démonstration de (9.6.3).} (all bold)", "font",
    fx(r"\textbf{(9.6.6) Fin de la démonstration de (9.6.3).}",
       r"\textbf{(9.6.6)} \emph{Fin de la démonstration de} (9.6.3)."),
    "The only heading of this form in the IV-3 files.")

add(75, "(9.6.6), l. 2: 'de point générique η∈S—E'", "S—E (long dash)", r"$\eta\in S-E$", "convention",
    fx(r"$\eta\in S-E$", r"$\eta\in S\setmin E$"), SETMIN, convention=7)

add(75, "(9.6.6): 'relativement au morphisme f_y : X_y→Spec(k(y))'",
    "bold italic k (enlarged crop p75_s3_spec.png)", "k(y)", "convention",
    fx(r"\operatorname{Spec}(k(y))", r"\operatorname{Spec}(\boldsymbol{k}(y))"), "", convention=1)

add(75, "(9.6.6): 'donc F=Y—V est fermé dans Y'", "Y—V (long dash)", "$F=Y-V$", "convention",
    fx("$F=Y-V$", r"$F=Y\setmin V$"), SETMIN, convention=7)

add(75, "(9.6.6): 'pour que s appartienne à S—E, il faut'", "S—E (long dash)", "$S-E$", "convention",
    fx("$S-E$, il faut", r"$S\setmin E$, il faut"), SETMIN, convention=7)

add(75, "Remarques (9.6.7) (i): 'Pour chacune des propriétés P considérées'",
    "bold italic P (enlarged crop p75_s4_P.png)", r"$\mathbf P$", "convention",
    fx(r"$\mathbf P$ considérées", r"$\boldsymbol{P}$ considérées"), "", convention=10)

add(75, "end of page / marker 76: '... induit sur l'ouvert Z∩X_s.' + 'Alors, dans les propositions' (p. 76)",
    "printed p. 76 begins 'Alors,' flush left: the paragraph of Remarque (ii) continues across the page break",
    r"blank line before \oldpage[IV-3]{76} (and after it, p. 76) makes a paragraph break", "marker",
    fx("induit sur l'ouvert $Z\\cap X_s$.\n\n", "induit sur l'ouvert $Z\\cap X_s$.\n"),
    "Apply together with the p. 76 marker fix (blank line after \\oldpage[IV-3]{76}). Marker position itself is right.")

# ---------------------------------------------------------------- p. 76
add(76, "top of page (marker 76)",
    "'Alors, dans les propositions (9.6.1) ...' flush left, continuing the paragraph of p. 75",
    r"\oldpage[IV-3]{76} followed by a blank line", "marker",
    fx("\\oldpage[IV-3]{76}\n\nAlors", "\\oldpage[IV-3]{76}\nAlors"),
    "Apply together with the p. 75 fix removing the blank line before the marker.")

add(76, "subsection heading 9.7",
    "'9.7. Constructibilité ... et de connexité géométrique.' (final full stop; enlarged crop p76_s2_title2.png)",
    r"\subsection{... de connexité géométrique} (no full stop)", "punctuation",
    fx("géométrique et de connexité géométrique}", "géométrique et de connexité géométrique.}"),
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop).")

add(76, "Lemme (9.7.1): 'Si X_η a n composantes irréductibles (resp. n' composantes connexes), il existe'",
    "'resp.' upright inside the italic statement (enlarged crop p76_s2_resp1.png)", "(resp. (italic)", "convention",
    fx("(resp. $n'$ composantes connexes), il", "(\\textup{resp.} $n'$ composantes connexes), il"),
    "Form of the p. 9 fix.", convention=6)

add(76, "Lemme (9.7.1), end: 'au moins n composantes irréductibles (resp. n' composantes connexes).'",
    "'resp.' upright (enlarged crop p76_s2_resp2.png)", "(resp. (italic)", "convention",
    fx("(resp. $n'$ composantes connexes).", "(\\textup{resp.} $n'$ composantes connexes)."), "", convention=6)

add(76, "proof of (9.7.1): '... donc X quasi-compact et quasi-séparé. Soient V_i (1⩽i⩽n) ...'",
    "'Soient V_i' starts a new indented paragraph (enlarged crop p76_s2_indent.png)",
    "one paragraph", "other",
    fx("quasi-séparé. Soient $V_i$", "quasi-séparé.\n\nSoient $V_i$"), "Missing paragraph break.")

# ---------------------------------------------------------------- p. 77
add(77, "Lemme (9.7.4): item labels a), b), c)",
    "labels a), b), c) italic like the statement (enlarged crop p77_s2_labels.png)",
    r"label=\emph{\alph*)}: \emph inside the italic lemma gives upright labels", "convention",
    fx(r"\begin{enumerate}[label=\emph{\alph*)}]", r"\begin{enumerate}[label=\alph*)]"),
    "One edit for the three labels (FIX_POLICY 2.6: drop \\emph where the print shows no change of face).",
    convention=6)

add(77, "after Lemme (9.7.4): 'Nous dirons dans ce cas que F est géométriquement irréductible.'",
    "a separate indented roman paragraph after the statement, with 'géométriquement irréductible' italic "
    "(enlarged crop p77_s2_nous.png)",
    r"inside the lemma environment: sentence italic, \emph words upright", "italics",
    fx("Nous dirons dans ce cas que $F$ est \\emph{géométriquement irréductible}.\n\\end{lemma}",
       "\\end{lemma}\n\nNous dirons dans ce cas que $F$ est \\emph{géométriquement irréductible}."),
    "The \\end{lemma} moves before the sentence; no overlap with the label fix above.")

add(77, "Lemme (9.7.5): 'pour tout x∈D(f), F_(k(x)) soit géométriquement irréductible'",
    "F_(k(x)) with bold upright k (enlarged crop p77_s3_Fkx.png)", r"$F_{(\boldsymbol{k}(x))}$", "font",
    fx(r"$F_{(\boldsymbol{k}(x))}$ soit", r"$F_{(\mathbf{k}(x))}$ soit"), KSUB)

add(77, "proof of (9.7.5): 'T^α=T_1^{α_1}T_2^{α_2} . . . T_n^{α_n}'",
    "baseline dots (enlarged crop p77_s3_Talpha.png)", r"\cdots", "symbol",
    fx(r"\mathrm T_2^{\alpha_2}\cdots", r"\mathrm T_2^{\alpha_2}\ldots"), "")

add(77, "proof of (9.7.5): '|α|=α_1+α_2+ . . . +α_n⩽d'",
    "baseline dots (enlarged crop p77_s3_alpha.png)", r"\cdots", "symbol",
    fx(r"\alpha_2+\cdots+\alpha_n", r"\alpha_2+\ldots+\alpha_n"), "")

add(77, "proof of (9.7.5): 'que les c_α non nuls sont inversibles dans A.'",
    "'dans' italic (enlarged crop p77_s3_dansA.png)", "dans (upright)", "italics",
    fx("inversibles dans $A$.", r"inversibles \emph{dans} $A$."), "")

add(77, "proof of (9.7.5): 'F_(k(x)) est de degré d'",
    "bold upright k in the subscript (enlarged crop p77_s3_Fkx2.png)", r"$F_{(\boldsymbol{k}(x))}$", "font",
    fx(r"$F_{(\boldsymbol{k}(x))}$ est", r"$F_{(\mathbf{k}(x))}$ est"), KSUB)

add(77, "Lemme (9.7.5.1): 'engendré par les polynômes (P_i)_(k(s)) (i∈I)'",
    "bold upright k in the subscript (enlarged crop p77_s4_Pi.png); k(s)[T_1,...,T_m] on the line is bold italic",
    r"$(P_i)_{(\boldsymbol{k}(s))}$", "font",
    fx(r"$(P_i)_{(\boldsymbol{k}(s))}$", r"$(P_i)_{(\mathbf{k}(s))}$"), KSUB)

# ---------------------------------------------------------------- p. 78
add(78, "proof of (9.7.5), l. 4: 'considérons le polynôme de B=A[T'_β, T''_γ]_{|β|⩽p,|γ|⩽q} : P_α(T'_β, T''_γ)=Σ_{β+γ=α}T'_βT''_γ—c_α. Soit Ω'",
    "formula in the running text, followed on the same line by 'Soit Ω une clôture algébrique' (enlarged crop p78_s1_display.png)",
    r"displayed \[ ... \] with \qquad", "other",
    fx("\\[\nB=A[\\mathrm T'_\\beta,\\mathrm T''_\\gamma]_{|\\beta|\\leqslant p,\n  |\\gamma|\\leqslant q}:\n"
       "\\qquad\nP_\\alpha(\\mathrm T'_\\beta,\\mathrm T''_\\gamma)\n"
       "=\\sum_{\\beta+\\gamma=\\alpha}\\mathrm T'_\\beta\\mathrm T''_\\gamma-c_\\alpha.\n\\]",
       "$B=A[\\mathrm T'_\\beta,\\mathrm T''_\\gamma]_{|\\beta|\\leqslant p,\n  |\\gamma|\\leqslant q}:\n"
       "P_\\alpha(\\mathrm T'_\\beta,\\mathrm T''_\\gamma)\n"
       "=\\sum_{\\beta+\\gamma=\\alpha}\\mathrm T'_\\beta\\mathrm T''_\\gamma-c_\\alpha$."),
    "Display set inline as printed (GLOBAL_ISSUES 21). Apply before the convention-7 fix of the same formula "
    "(next finding); that fix's old matches both before and after this edit.")

add(78, "same formula: 'T'_βT''_γ—c_α'", "long dash used for the subtraction (enlarged crop p78_s1_dash.png)",
    r"-c_\alpha", "convention",
    fx(r"\mathrm T''_\gamma-c_\alpha", r"\mathrm T''_\gamma\setmin c_\alpha"),
    "Subtraction (GLOBAL_ISSUES 23). " + SETMIN + " Listed after the inline fix it overlaps.", convention=7)

add(78, "'tels que F_1F_2=F_(Ω) signifie que le système d'équations'",
    "no comma after F_(Ω) (enlarged crop p78_s1_FOmega.png)", r"$F_1F_2=F_{(\Omega)}$, signifie", "punctuation",
    fx(r"$F_1F_2=F_{(\Omega)}$, signifie", r"$F_1F_2=F_{(\Omega)}$ signifie"), "")

add(78, "'dans un voisinage de η, on a V(𝔞_x)=0, et par suite'",
    "V(𝔞_x)=0 with a zero (enlarged crop p78_s2_Vax.png), not Ø", r"$V(\mathfrak a_x)=0$", "misprint_in_print",
    None,
    "The empty set is meant (Lemme (9.7.5.1) gives V(𝔞_s)=Ø; V(𝔞_η)=Ø two lines above). The TeX keeps the "
    "printed 0.",
    corrected=r"$V(\mathfrak a_x)=\varnothing$", confidence="medium")

add(78, "'pour ces valeurs de x, F_(k(x)) n'admet pas de factorisation'",
    "bold upright k in the subscript (enlarged crop p78_s2_Fkx.png)", r"$F_{(\boldsymbol{k}(x))}$", "font",
    fx(r"$F_{(\boldsymbol{k}(x))}$ n'admet", r"$F_{(\mathbf{k}(x))}$ n'admet"), KSUB)

add(78, "'de factorisation F_(k(x))=G_1G_2'",
    "bold upright k in the subscript (enlarged crop p78_s2_Fkx2.png); k(x) at the end of the sentence is bold italic",
    r"$F_{(\boldsymbol{k}(x))}=G_1G_2$", "font",
    fx(r"$F_{(\boldsymbol{k}(x))}=G_1G_2$", r"$F_{(\mathbf{k}(x))}=G_1G_2$"), KSUB)

add(78, "proof of (9.7.6), l. 2: 'où chacun des 𝒢_i est irredondant et Ass(ℱ_η)'",
    "irredondant (no accent; enlarged crop p78_s2_irred1.png)", "irrédondant", "word",
    fx("irrédondant et", "irredondant et"),
    "The other 5 occurrences in ega4-9-fr.tex already read 'irredondant'.")

add(78, "proof of (9.7.6): 'pour i≠j, Z_i—(Z_i∩Z_j) est ouvert dense'", "Z_i—(…) (long dash)",
    r"$Z_i-(Z_i\cap Z_j)$", "convention",
    fx(r"$Z_i-(Z_i\cap Z_j)$", r"$Z_i\setmin(Z_i\cap Z_j)$"), SETMIN, convention=7)

add(78, "proof of (9.7.6): '(Y_i)_s—((Y_i)_s∩(Y_j)_s) est ouvert et dense'", "long dash",
    r"$(Y_i)_s-((Y_i)_s\cap(Y_j)_s)$", "convention",
    fx(r"$(Y_i)_s-((Y_i)_s\cap(Y_j)_s)$", r"$(Y_i)_s\setmin((Y_i)_s\cap(Y_j)_s)$"), SETMIN, convention=7)

add(78, "proof of (9.7.6): 'chacun des (ℱ_i)_s est sans cycle premier associé pour s∈U'",
    "'sans cycle premier associé pour s∈U' (no 'immergé')", "same as the print", "misprint_in_print",
    None,
    "'immergé' is missing: what is to be proved is that (ℱ_i)_s has no embedded associated cycle (the next "
    "sentence uses that Ass((ℱ_i)_s) consists of the maximal points of (Y_i)_s). The TeX keeps the printed reading.",
    corrected=r"sans cycle premier associé immergé pour $s\in U$", confidence="medium")

add(78, "proof of (9.7.6): 'On peut donc supposer que ℱ_η est irredondant'",
    "irredondant (italic, no accent; enlarged crop p78_s3_irred2.png)", r"\emph{irrédondant}", "word",
    fx(r"\emph{irrédondant}", r"\emph{irredondant}"), "")

add(78, "proof of (9.7.6): 'réunion d'un nombre fini d'ouverts affines V_j et si V_j∩Supp(ℱ_η)=Ø'",
    "no comma after V_j (line end; enlarged crop p78_s4_Vj.png)", "$V_j$, et si", "punctuation",
    fx("affines $V_j$, et si", "affines $V_j$ et si"), "")

add(78, "proof of (9.7.6), last line: 'le B_(K)-module M_(K) est irredondant. Soit 𝔮 l'unique'",
    "irredondant (no accent; enlarged crop p78_s4_irred3.png)", "irrédondant", "word",
    fx("irrédondant.", "irredondant."), "")

add(78, "end of page / marker 79: '... Soit 𝔮 l'unique' + 'élément de Ass(M_(K))' (p. 79)",
    "the sentence runs on: printed p. 79 begins 'élément de' flush left",
    r"blank line before \oldpage[IV-3]{79} (and after it, p. 79) breaks the sentence into two paragraphs", "marker",
    fx("Soit $\\mathfrak q$ l'unique\n\n", "Soit $\\mathfrak q$ l'unique\n"),
    "Apply together with the p. 79 marker fix (blank line after \\oldpage[IV-3]{79}).")

# ---------------------------------------------------------------- p. 79
add(79, "top of page (marker 79): 'élément de Ass(M_(K))'",
    "mid-sentence continuation, flush left", r"\oldpage[IV-3]{79} followed by a blank line", "marker",
    fx("\\oldpage[IV-3]{79}\n\nélément de", "\\oldpage[IV-3]{79}\nélément de"),
    "Apply together with the p. 78 fix removing the blank line before the marker.")

add(79, "'pour s assez voisin de η, (M_h)_(k(s)) s'identifie'",
    "bold upright k in the subscript (enlarged crop p79_s1_Mh.png)", r"$(M_h)_{(\boldsymbol{k}(s))}$", "font",
    fx(r"$(M_h)_{(\boldsymbol{k}(s))}$ s'identifie", r"$(M_h)_{(\mathbf{k}(s))}$ s'identifie"), KSUB)

add(79, "'à un sous-B_(k(s))-module de M_(k(s))'", "bold upright k in both subscripts (crop p79_s1_line6.png)",
    r"\boldsymbol{k} twice", "font",
    fx(r"sous-$B_{(\boldsymbol{k}(s))}$-module de $M_{(\boldsymbol{k}(s))}$",
       r"sous-$B_{(\mathbf{k}(s))}$-module de $M_{(\mathbf{k}(s))}$"), KSUB)

add(79, "'et le quotient (M_h)_(k(s))/(M_{h+1})_(k(s))'", "bold upright k in both subscripts (crop p79_s1_line6.png)",
    r"\boldsymbol{k} twice", "font",
    fx(r"$(M_h)_{(\boldsymbol{k}(s))}/(M_{h+1})_{(\boldsymbol{k}(s))}$",
       r"$(M_h)_{(\mathbf{k}(s))}/(M_{h+1})_{(\mathbf{k}(s))}$"), KSUB)

add(79, "'à un sous-B_(k(s))-module ≠0 de'", "bold upright k in the subscript (crop p79_s1_line7.png)",
    r"$B_{(\boldsymbol{k}(s))}$", "font",
    fx(r"sous-$B_{(\boldsymbol{k}(s))}$-module $\neq0$", r"sous-$B_{(\mathbf{k}(s))}$-module $\neq0$"), KSUB)

add(79, "'de B_(k(s))/𝔭_(k(s))=(B/𝔭)_(k(s))'", "bold upright k in the three subscripts (crop p79_s1_line7.png)",
    r"\boldsymbol{k} three times", "font",
    fx("$B_{(\\boldsymbol{k}(s))}/\\mathfrak p_{(\\boldsymbol{k}(s))}\n=(B/\\mathfrak p)_{(\\boldsymbol{k}(s))}$",
       "$B_{(\\mathbf{k}(s))}/\\mathfrak p_{(\\mathbf{k}(s))}\n=(B/\\mathfrak p)_{(\\mathbf{k}(s))}$"), KSUB)

add(79, "'si B est intègre, alors B_(k(s)) n'a pas d'idéaux premiers associés immergés'",
    "bold upright k in the subscript", r"$B_{(\boldsymbol{k}(s))}$", "font",
    fx(r"alors $B_{(\boldsymbol{k}(s))}$", r"alors $B_{(\mathbf{k}(s))}$"), KSUB)

add(79, "'(Bourbaki, Alg. comm., chap. V, § 3, n° 1, cor. 1 du th. 1)'",
    "n with a raised letter o (enlarged crop p79_s2_no.png)", r"n$^\circ$ (degree ring)", "symbol",
    fx(r"\S~3, n$^\circ$~1", r"\S~3, n\textsuperscript{o}~1"),
    "The edition's form is n\\textsuperscript{o} (as on 0_IV pp. 156-164).")

add(79, "'pour s voisin de η, C_(k(s)) n'a pas d'idéaux premiers associés immergés'",
    "bold upright k in the subscript", r"$C_{(\boldsymbol{k}(s))}$", "font",
    fx("$C_{(\\boldsymbol{k}(s))}$\nn'a pas", "$C_{(\\mathbf{k}(s))}$\nn'a pas"), KSUB)

add(79, "'évident puisque C_(k(s))=k(s)[T_1, ..., T_n]'",
    "subscript k bold upright, k(s) on the line bold italic (enlarged crop p79_s2_Cks.png)",
    r"$C_{(\boldsymbol{k}(s))}=\boldsymbol{k}(s)[...]$", "font",
    fx(r"$C_{(\boldsymbol{k}(s))}=", r"$C_{(\mathbf{k}(s))}="), KSUB + " The \\boldsymbol{k}(s) on the line is right.")

add(79, "Théorème (9.7.7): item labels (i)-(iv)",
    "labels (i), (ii), (iii), (iv) upright (enlarged crop p79_s2_labels.png)",
    r"label=(\roman*) inside the italic theorem: italic labels", "convention",
    fx(r"\begin{enumerate}[label=(\roman*)]", r"\begin{enumerate}[label=\textup{(\roman*)}]"),
    "One edit for the four labels (GLOBAL_ISSUES 16).", convention=6)

add(79, "proof of (9.7.7): 'g étant surjectif, on a E=g(E') et S—E=g(S'—E')' (first dash)",
    "S—E (long dash)", "$S-E=g(S'-E')$", "convention",
    fx("$S-E=g(", r"$S\setmin E=g("), SETMIN, convention=7)

add(79, "same formula, second dash: 'g(S'—E')'", "S'—E' (long dash)", "$S-E=g(S'-E')$", "convention",
    fx("S'-E')", r"S'\setmin E')"), SETMIN, convention=7)

add(79, "proof of (9.7.7): '(Bourbaki, Alg. comm., chap. V, § 2, n° 1, cor. 1 de la prop. 1)'",
    "n with a raised letter o", r"n$^\circ$ (degree ring)", "symbol",
    fx(r"\S~2, n$^\circ$~1", r"\S~2, n\textsuperscript{o}~1"),
    "As the § 3 reference above.")

add(79, "proof of (9.7.7): 'si l'on prouve que E' ou S'—E' est un voisinage de η''",
    "S'—E' (long dash)", "$S'-E'$", "convention",
    fx("ou $S'-E'$", r"ou $S'\setmin E'$"), SETMIN, convention=7)

# ---------------------------------------------------------------- check and write
ok = True
for d in F:
    if not d["fix"]:
        continue
    p = d["page"]
    with open(rf"{RUN}\page_{p:03d}.tex", encoding="utf-8", newline="") as f:
        t = f.read().replace("\r\n", "\n")
    n = t.count(d["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE/MISSING", p, n, repr(d["fix"]["old"]))

# overlap check per page (positions in the original text)
by_page = {}
for i, d in enumerate(F):
    if d["fix"]:
        by_page.setdefault(d["page"], []).append(i)
for p, idx in by_page.items():
    with open(rf"{RUN}\page_{p:03d}.tex", encoding="utf-8", newline="") as f:
        t = f.read().replace("\r\n", "\n")
    spans = []
    for i in idx:
        o = F[i]["fix"]["old"]
        s = t.find(o)
        spans.append((s, s + len(o), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            print("OVERLAP page", p, F[a[2]]["where"][:50], "|", F[b[2]]["where"][:50])

with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    json.dump(F, f, ensure_ascii=False, indent=1)
print("written", len(F), "findings; all olds unique:", ok)
from collections import Counter
c = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    c[(d["page"], k)] += 1
for p in range(75, 80):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
