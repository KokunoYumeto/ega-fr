import json, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = r'user\Documents\ega_scan_check_20261101\run_IV3'
OUT = RUN + r'\findings_195_199.json'
N = '\n'

def F(page, where, scan, tex, kind, conv, conf, old, new, note='', corrected=None):
    d = {'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind,
         'convention': conv, 'confidence': conf,
         'fix': None if old is None else {'old': old, 'new': new}}
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    return d

BK = r'\boldsymbol{k}'
L = []

# ---------------- page 195 ----------------
L.append(F(195, "(13.3.1) b), 'un Y-morphisme quasi-fini'",
  "'quasi-fini' set in roman inside the italic statement (enlarged crop p195_quasifini.png)",
  "$Y$-morphisme quasi-fini (italic in the proposition)", 'convention', 6, 'high',
  r"$Y$-morphisme quasi-fini", r"$Y$-morphisme \textup{quasi-fini}",
  "Does not overlap the next two edits."))
L.append(F(195, "(13.3.1) b), 'g : U->Y(x)_Z Z[T_1, ..., T_e] (préschéma ...'",
  "the formula stands in the text line, followed on the same line by '(préschéma que nous noterons aussi ...'",
  "the formula is a centred display \\[ ... \\]", 'formula', None, 'high',
  r"\[" + N + r"    g:U\longrightarrow Y\otimes_{\mathbf Z}\mathbf Z[T_1,\ldots,T_e]" + N + r"  \]",
  r"$g:U\longrightarrow Y\otimes_{\mathbf Z}\mathbf Z[T_1,\ldots,T_e]$",
  "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting word lost."))
L.append(F(195, "(13.3.1) b), parenthesis '(préschéma que nous noterons aussi Y[T_1, ..., T_e] pour abréger)'",
  "the whole parenthesis is roman inside the italic statement; 'tels que l'image ...' resumes in italic",
  "italic (proposition environment)", 'convention', 6, 'high',
  r"(préschéma que nous noterons aussi $Y[T_1,\ldots,T_e]$ pour abréger)",
  r"\textup{(préschéma que nous noterons aussi $Y[T_1,\ldots,T_e]$ pour abréger)}"))
L.append(F(195, "proof of (13.3.1), a') => a''): 'l'ensemble V_lambda des x' in U_lambda tels que dim_{x'}(f_lambda^{-1}(f_lambda(x)))=e'",
  "dim_{x'}(f_lambda^{-1}(f_lambda(x)))=e: the inner argument is x without a prime (enlarged crop p195_dim.png)",
  "\\dim_{x'}(f_\\lambda^{-1}(f_\\lambda(x')))=e: silently corrected", 'misprint_in_print', None, 'high',
  r"f_\lambda(x')))=e", r"f_\lambda(x)))=e",
  "V_lambda is the set of x' where the fibre through x' has dimension e at x'; Chevalley's theorem (13.1.3) gives its openness only for f_lambda(x'). The fix restores the printed reading.",
  corrected=r"f_\lambda(x')))=e"))
L.append(F(195, "Lemme (13.3.1.1): 'X_y=X x_Y Spec(k(y))'",
  "bold italic k", "plain k", 'convention', 1, 'high',
  r"\times_Y\operatorname{Spec}(k(y))", r"\times_Y\operatorname{Spec}(" + BK + "(y))"))
L.append(F(195, "Lemme (13.3.1.1): 'g_y : X_y -> Spec(k(y)[T_1, ..., T_e])'",
  "bold italic k", "plain k", 'convention', 1, 'high',
  r"\operatorname{Spec}(k(y)[T_1,\ldots,T_e])", r"\operatorname{Spec}(" + BK + r"(y)[T_1,\ldots,T_e])"))
L.append(F(195, "'l'anneau B(x)_A k(p) est une'",
  "bold italic k", "plain k", 'convention', 1, 'high',
  r"$B\otimes_Ak(\mathfrak p)$ est une", r"$B\otimes_A" + BK + r"(\mathfrak p)$ est une"))
L.append(F(195, "'une k(p)-algèbre de type fini'",
  "bold italic k", "plain k", 'convention', 1, 'high',
  r"$k(\mathfrak p)$-algèbre de type fini", "$" + BK + r"(\mathfrak p)$-algèbre de type fini"))
L.append(F(195, "'prouve qu'il y a dans B(x)_A k(p) une suite finie'",
  "bold italic k", "plain k", 'convention', 1, 'high',
  r"dans $B\otimes_Ak(\mathfrak p)$ une", r"dans $B\otimes_A" + BK + r"(\mathfrak p)$ une"))
L.append(F(195, "'algébriquement indépendants sur k(p)'",
  "bold italic k", "plain k", 'convention', 1, 'high',
  "sur" + N + r"$k(\mathfrak p)$ et", "sur" + N + "$" + BK + r"(\mathfrak p)$ et"))
L.append(F(195, "'si l'on pose C'=k(p)[t_1, ..., t_r]'",
  "bold italic k", "plain k", 'convention', 1, 'high',
  r"$C'=k(\mathfrak p)", "$C'=" + BK + r"(\mathfrak p)"))
L.append(F(195, "'B(x)_A k(p) soit une C'-algèbre finie'",
  "bold italic k", "plain k", 'convention', 1, 'high',
  r"$B\otimes_Ak(\mathfrak p)$ soit une", r"$B\otimes_A" + BK + r"(\mathfrak p)$ soit une"))
L.append(F(195, "'on a donc dim(B(x)_A k(p))=dim(C')'",
  "bold italic k", "plain k", 'convention', 1, 'high',
  r"\dim(B\otimes_Ak(\mathfrak p))", r"\dim(B\otimes_A" + BK + r"(\mathfrak p))"))
L.append(F(195, "'Comme B(x)_A k(p)=(B/pB)(x)_{A/p} k(p)'",
  "both k bold italic (on the line, not in a subscript)", "plain k twice", 'convention', 1, 'high',
  r"$B\otimes_Ak(\mathfrak p)=(B/\mathfrak pB)\otimes_{A/\mathfrak p}k(\mathfrak p)$",
  r"$B\otimes_A" + BK + r"(\mathfrak p)=(B/\mathfrak pB)\otimes_{A/\mathfrak p}" + BK + r"(\mathfrak p)$",
  "Two occurrences, one edit."))
L.append(F(195, "end of page_195.tex: page break 195/196 mid-sentence '... par un élément ≠0 | convenable de A/p, ...'",
  "p. 196 begins 'convenable de A/p, supposer que ...' flush left, continuing the sentence of p. 195",
  "blank line before \\oldpage[IV-3]{196}: a paragraph break inside the sentence", 'marker', None, 'high',
  r"élément $\neq0$" + N + N, r"élément $\neq0$" + N,
  "Marker position itself is right; only the blank line before it goes (GLOBAL_ISSUES 20)."))

# ---------------- page 196 ----------------
L.append(F(196, "'l'image canonique dans B(x)_A k(p) d'un élément s_i'",
  "bold italic k", "plain k", 'convention', 1, 'high',
  r"$B\otimes_Ak(\mathfrak p)$ d'un", r"$B\otimes_A" + BK + r"(\mathfrak p)$ d'un"))
L.append(F(196, "'et l'on déduit par suite de g un k(y_alpha)-morphisme quasi-fini'",
  "bold italic k", "plain k", 'convention', 1, 'high',
  r"$k(y_\alpha)$-morphisme quasi-fini", "$" + BK + r"(y_\alpha)$-morphisme quasi-fini",
  "Does not overlap the next edit."))
L.append(F(196, "'un k(y_alpha)-morphisme quasi-fini h : U∩f^{-1}(y_alpha)->p^{-1}(y_alpha). Or ...'",
  "the formula stands in the text line, followed on the same line by 'Or p^{-1}(y_alpha)=...'",
  "centred display \\[ h:... . \\]", 'formula', None, 'high',
  r"\[" + N + r"  h:U\cap f^{-1}(y_\alpha)\longrightarrow p^{-1}(y_\alpha)." + N + r"\]",
  r"$h:U\cap f^{-1}(y_\alpha)\longrightarrow p^{-1}(y_\alpha)$.",
  "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting word lost."))
L.append(F(196, "'Or p^{-1}(y_alpha)=Spec(k(y_alpha)[T_1, ..., T_e])'",
  "bold italic k", "plain k", 'convention', 1, 'high',
  r"\operatorname{Spec}(k(y_\alpha)[T_1,\ldots,T_e])", r"\operatorname{Spec}(" + BK + r"(y_\alpha)[T_1,\ldots,T_e])"))
L.append(F(196, "'se factorisant en {x_lambda}bar -> Z'_lambda -> p^{-1}(y_alpha) en vertu de (I, 5.2.2))'",
  "the formula stands at the start of a text line followed by 'en vertu de (I, 5.2.2)); on aboutit ...'",
  "centred display", 'formula', None, 'high',
  r"\[" + N + r"  \overline{\{x_\lambda\}}\longrightarrow Z'_\lambda" + N + r"  \longrightarrow p^{-1}(y_\alpha)" + N + r"\]",
  r"$\overline{\{x_\lambda\}}\longrightarrow Z'_\lambda" + N + r"  \longrightarrow p^{-1}(y_\alpha)$",
  "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting word lost."))
L.append(F(196, "'le k(y_alpha)-morphisme h : U∩f^{-1}(y_alpha)->p^{-1}(y_alpha) déduit de g'",
  "bold italic k", "plain k", 'convention', 1, 'high',
  r"le $k(y_\alpha)$-morphisme", "le $" + BK + r"(y_\alpha)$-morphisme"))
L.append(F(196, "'est un k(f(x'))-morphisme quasi-fini'",
  "bold italic k", "plain k", 'convention', 1, 'high',
  r"$k(f(x'))$-morphisme", "$" + BK + r"(f(x'))$-morphisme"))
L.append(F(196, "Définition (13.3.2), first sentence: 'On dit que f est équidimensionnel au point x (ou que X est équidimensionnel sur Y au point x)'",
  "the defined terms 'équidimensionnel au point' and 'équidimensionnel sur Y au point' are roman inside the italic definition; 'x', '(ou que X est' and 'x)' italic (enlarged crop p196_def_a.png)",
  "all italic (definition environment)", 'convention', 6, 'high',
  r"est équidimensionnel au point $x$ (ou que $X$" + N + r"est équidimensionnel sur $Y$ au point $x$)",
  r"est \textup{équidimensionnel au point} $x$ (ou que $X$" + N + r"est \textup{équidimensionnel sur $Y$ au point} $x$)",
  "The parentheses here are italic in the print, as the TeX gives them."))
L.append(F(196, "Définition (13.3.2): 'les conditions équivalentes de (13.3.1) sont vérifiées'",
  "reference upright", "italic (inside the definition)", 'convention', 6, 'high',
  r"(13.3.1) sont vérifiées", r"\textup{(13.3.1)} sont vérifiées"))
L.append(F(196, "Définition (13.3.2), second sentence: 'On dit que f est équidimensionnel (ou que X est équidimensionnel sur Y) si ...'",
  "'équidimensionnel' and 'équidimensionnel sur Y)' roman (closing parenthesis upright too); 'ou que X est' italic (enlarged crop p196_def_b.png)",
  "all italic", 'convention', 6, 'high',
  r"est équidimensionnel (ou que $X$ est" + N + r"équidimensionnel sur $Y$) si",
  r"est \textup{équidimensionnel} (ou que $X$ est" + N + r"\textup{équidimensionnel sur $Y$)} si",
  "The opening parenthesis before 'ou que' also looks upright in the print; left as is (parentheses: GLOBAL_ISSUES 26)."))
L.append(F(196, "end of page_196.tex: the word 'équidimensionnel' broken across pp. 196/197 ('équidimen- | sionnel')",
  "one word, hyphenated at the page end",
  "'équidimen-' + newline + \\oldpage[IV-3]{197} + newline + 'sionnel': typesets 'équidimen- sionnel' (hyphen and a space inside the word)",
  'marker', None, 'high',
  "équidimen-" + N, "équidimen%" + N,
  "The marker stays mid-word, joined with % as elsewhere in IV-3 (ega4-9 p. 93, ega4-10 p. 100); \\oldpage ends with \\ignorespaces, so the newline after it adds no space. The only such split in IV-3."))

# ---------------- page 197 ----------------
L.append(F(197, "Proposition (13.3.3): 'le morphisme déduit de f (I, 5.2.2)'",
  "reference upright (bold upright I, roman figures) (enlarged crop p197_ref_I522.png)",
  "(\\textbf{I}, 5.2.2) inside the italic proposition: bold italic I, italic figures", 'convention', 6, 'high',
  r"(\textbf{I}, 5.2.2)", r"\textup{(\textbf{I}, 5.2.2)}"))
L.append(F(197, "Corollaire (13.3.4): 'Avec les notations de (13.3.3), posons'",
  "reference upright (enlarged crop p197_ref_1333.png)", "italic", 'convention', 6, 'high',
  r"(13.3.3), posons", r"\textup{(13.3.3)}, posons"))
L.append(F(197, "(13.3.4.1): '+e—deg.tr'",
  "long dash for the subtraction (enlarged crop p197_disp1.png)", "minus sign", 'convention', 7, 'high',
  "+e" + N + r"  -\deg", "+e" + N + r"  \setmin\deg",
  "Subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision (FIX_POLICY 2.7)."))
L.append(F(197, "(13.3.4.1): 'deg.tr_{k(y)} k(x)'",
  "subscript k(y) with a bold upright k; k(x) with a bold italic k", "plain k twice", 'convention', 1, 'high',
  r"_{k(y)}k(x)" + N, r"_{\mathbf{k}(y)}" + BK + "(x)" + N,
  "Two occurrences, one edit; bold upright in the subscript (GLOBAL_ISSUES 48)."))
L.append(F(197, "Corollaire (13.3.5): 'Avec les notations de (13.3.4), supposons'",
  "reference upright (enlarged crop p197_ref_1334.png)", "italic", 'convention', 6, 'high',
  r"(13.3.4), supposons", r"\textup{(13.3.4)}, supposons"))
L.append(F(197, "proof of (13.3.5): 'Inversement, si O_{X,x} est équidimensionnel, tous les nombres O_{Y_j,y} sont égaux par (13.3.4.1)'",
  "'tous les nombres O_{Y_j,y} sont égaux': 'dim' missing", "keeps the printed reading", 'misprint_in_print', None, 'medium',
  None, None,
  "The numbers compared are the dimensions dim(O_{Y_j,y}) (cf. 'les nombres dim(O_{Y'_i,y})' three lines above and (13.3.4.1)).",
  corrected=r"tous les nombres $\dim(\mathcal O_{Y_j,y})$ sont égaux"))
L.append(F(197, "(13.3.6.1): 'dim(O_x (x)_{O_y} k(y))'",
  "bold italic k (on the line)", "plain k", 'convention', 1, 'high',
  r"\otimes_{\mathcal O_y}k(y)", r"\otimes_{\mathcal O_y}" + BK + "(y)"))
L.append(F(197, "Proposition (13.3.6), after (13.3.6.1): '(cf. (13.2.7.1)) f est équidimensionnel'",
  "'(cf. (13.2.7.1))' upright (enlarged crop p197_cf.png)", "italic", 'convention', 6, 'high',
  r"(cf. (13.2.7.1)) $f$", r"\textup{(cf. (13.2.7.1))} $f$"))
L.append(F(197, "last display of the page: '+dim_x(X_j∩f^{-1}(y))—deg.tr'",
  "long dash for the subtraction (enlarged crop p197_disp2.png)", "minus sign", 'convention', 7, 'high',
  r"(y))-\deg", r"(y))\setmin\deg",
  "Subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision."))
L.append(F(197, "last display of the page: 'deg.tr_{k(y)} k(x).'",
  "subscript k bold upright; k(x) bold italic", "plain k twice", 'convention', 1, 'high',
  r"_{k(y)}k(x).", r"_{\mathbf{k}(y)}" + BK + "(x).",
  "Two occurrences, one edit (GLOBAL_ISSUES 48)."))
L.append(F(197, "end of page_197.tex: page break 197/198 after the display; p. 198 begins 'Or, comme O_y est supposé équidimensionnel ...'",
  "'Or, comme' starts flush left (not indented, unlike 'Inversement,' further down): the paragraph continues after the display",
  "blank line after \\] before \\oldpage[IV-3]{198}: new indented paragraph", 'marker', None, 'high',
  r"\]" + N + N, r"\]" + N,
  "Marker position itself is right. 'old' is the only \\] followed by a blank line on the page (GLOBAL_ISSUES 20/47)."))

# ---------------- page 198 ----------------
L.append(F(198, "(13.3.6.2): 'dim(O_{X,x})—dim(O_{Y,y})'",
  "long dash for the subtraction", "minus sign", 'convention', 7, 'high',
  r"-\dim(\mathcal O_{Y,y})+\deg", r"\setmin\dim(\mathcal O_{Y,y})+\deg",
  "Subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision."))
L.append(F(198, "(13.3.6.2): 'deg.tr_{k(y)} k(x).'",
  "subscript k bold upright; k(x) bold italic", "plain k twice", 'convention', 1, 'high',
  r"_{k(y)}k(x).", r"_{\mathbf{k}(y)}" + BK + "(x).",
  "Two occurrences, one edit (GLOBAL_ISSUES 48)."))
L.append(F(198, "display after 'que l'on a la relation': '+e—deg.tr'",
  "long dash for the subtraction", "minus sign", 'convention', 7, 'high',
  "+e" + N + r"  -\deg", "+e" + N + r"  \setmin\deg",
  "Subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision."))
L.append(F(198, "display after 'que l'on a la relation': 'deg.tr_{k(y)} k(x)'",
  "subscript k bold upright; k(x) bold italic", "plain k twice", 'convention', 1, 'high',
  r"_{k(y)}k(x)" + N, r"_{\mathbf{k}(y)}" + BK + "(x)" + N,
  "Two occurrences, one edit (GLOBAL_ISSUES 48)."))
L.append(F(198, "(13.3.7.1): 'x ~> codim_x(Z∩f^{-1}(f(x)), f^{-1}(f(x)))'",
  "wavy arrow (enlarged crop p198_leadsto.png)", "\\longmapsto", 'symbol', None, 'high',
  r"x\longmapsto\operatorname{codim}_x", r"x\leadsto\operatorname{codim}_x",
  "Wavy arrow (GLOBAL_ISSUES 33), written \\leadsto as in the earlier page fixes; not convention 3."))
L.append(F(198, "proof of (13.3.7), display: '=dim_x(f^{-1}(f(x)))—dim_x(Z∩f^{-1}(f(x))).'",
  "long dash for the subtraction (enlarged crop p198_codim.png)", "minus sign", 'convention', 7, 'high',
  r"-\dim_x(Z\cap f^{-1}(f(x))).", r"\setmin\dim_x(Z\cap f^{-1}(f(x))).",
  "Subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision."))
L.append(F(198, "proof of (13.3.7): 'le second est fonction semi-continue supérieurement de x en vertu de (13.3.3)'",
  "'(13.3.3)' (enlarged crop p198_ref1333.png)", "keeps the printed '(13.3.3)'", 'misprint_in_print', None, 'medium',
  None, None,
  "Wrong reference in the print: the upper semicontinuity of x -> dim_x(Z∩f^{-1}(f(x))) is Chevalley's theorem (13.1.3) (applied to the restriction of f to Z), cited for the same purpose on p. 195; (13.3.3) is the criterion for equidimensionality by components. Not in the authors' errata (Err_IV 35 covers these pages only for 'localement équidimensionnel').",
  corrected="(13.1.3)"))
L.append(F(198, "Proposition (13.3.8): 'g : Y'->Y un morphisme plat'",
  "'plat' roman inside the italic statement (enlarged crop p198_plat.png)", "italic", 'convention', 6, 'high',
  r"$g:Y'\to Y$ un morphisme plat", r"$g:Y'\to Y$ un morphisme \textup{plat}"))
L.append(F(198, "Remarque (13.3.9): 'n'est pas stable par changement de base quelconque'",
  "the whole phrase 'n'est pas stable par changement de base quelconque' italic in the roman remark (enlarged crop p198_remark.png)",
  "only 'pas' emphasised", 'italics', None, 'high',
  r"n'est \emph{pas}" + N + "stable par changement de base quelconque",
  r"\emph{n'est pas" + N + "stable par changement de base quelconque}",
  "Inside the remark environment (italic in the TeX); judged as a roman body, as the print sets remarks."))
L.append(F(198, "end of page_198.tex: page break 198/199 mid-sentence '(Y' étant | considérée comme sous-préschéma fermé réduit de Y)'",
  "p. 199 begins 'considérée comme ...' flush left, continuing the sentence",
  "blank line before \\oldpage[IV-3]{199}: a paragraph break inside the sentence", 'marker', None, 'high',
  r"($Y'$ étant" + N + N, r"($Y'$ étant" + N,
  "Marker position itself is right (GLOBAL_ISSUES 20)."))

# ---------------- page 199 ----------------
L.append(F(199, "Remarque (13.3.9), first example: 'le morphisme f' : X'->Y' n'est pas dominant'",
  "'n'est pas dominant' italic, 'n'est' included (enlarged crop p199_nestpas.png)", "n'est \\emph{pas dominant}", 'italics', None, 'high',
  r"n'est \emph{pas dominant}", r"\emph{n'est pas dominant}",
  "Remark body judged as roman."))
L.append(F(199, "Remarque (13.3.9), second example: '(et a fortiori équidimensionnel par (13.3.1, b)))'",
  "three closing parentheses after b: the label's, the reference's and the one opened at '(et a fortiori' (enlarged crop p199_b_paren.png)",
  "'(13.3.1, $b$))': one closing parenthesis missing, so '(et a fortiori ...' is never closed", 'missing', None, 'high',
  r"(13.3.1, $b$)", r"(13.3.1, $b$))",
  "Independent of the next edit (comma), which starts at the following parenthesis; either order works."))
L.append(F(199, "Remarque (13.3.9), second example: '... par (13.3.1, b))) g : Y'->Y fini et dominant'",
  "no comma between 'b)))' and 'g : Y'->Y' (enlarged crop p199_b_paren.png)",
  "'), $g:Y'\\to Y$': comma added (silent correction)", 'misprint_in_print', None, 'medium',
  r"), $g", r") $g",
  "The list 'X et Y ... intègres, f fini et birationnel (...), g fini et dominant' needs the comma; the fix restores the printed reading and changes only the comma.",
  corrected=r"), $g"))
L.append(F(199, "Remarque (13.3.9): 'g : Y'->Y fini et dominant.'",
  "'fini' and 'dominant' italic, 'et' roman (as in 'f fini et birationnel' a line above)", "\\emph{fini et dominant} (et italic too)", 'italics', None, 'high',
  r"\emph{fini et dominant}", r"\emph{fini} et \emph{dominant}",
  "Remark body judged as roman."))

# ---------------- checks ----------------
pages = {}
for p in sorted({x['page'] for x in L}):
    t = open(RUN + r'\page_%03d.tex' % p, encoding='utf-8', newline='').read()
    pages[p] = t.replace('\r\n', '\n')
bad = 0
spans = {}
for i, x in enumerate(L):
    f = x['fix']
    if f is None:
        continue
    t = pages[x['page']]
    c = t.count(f['old'])
    if c != 1:
        bad += 1
        print('COUNT', c, 'page', x['page'], repr(f['old']))
        continue
    s = t.index(f['old'])
    spans.setdefault(x['page'], []).append((s, s + len(f['old']), i))
    if f['old'] == f['new']:
        bad += 1
        print('NOOP', x['page'], repr(f['old']))
for p, sp in spans.items():
    sp.sort()
    for a, b in zip(sp, sp[1:]):
        if a[1] > b[0]:
            bad += 1
            print('OVERLAP page', p, L[a[2]]['where'][:60], '|', L[b[2]]['where'][:60])
# counts
for p in sorted(pages):
    rows = [x for x in L if x['page'] == p]
    conv = sum(1 for x in rows if x['kind'] == 'convention')
    mis = sum(1 for x in rows if x['kind'] == 'misprint_in_print')
    print('p.%d: %d/%d/%d' % (p, len(rows) - conv - mis, conv, mis))
print('problems:', bad, 'findings:', len(L))
if bad == 0:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(L, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    print('written', OUT)
