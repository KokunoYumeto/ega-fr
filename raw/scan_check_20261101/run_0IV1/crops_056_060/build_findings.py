import json, os

RUN = r'user\Documents\ega_scan_check_20261101\run_0IV1'
OUT = os.path.join(RUN, 'findings_056_060.json')

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {
        'page': page,
        'where': where,
        'scan': scan,
        'tex': tex,
        'kind': kind,
        'convention': conv,
        'confidence': conf,
        'fix': ({'old': old, 'new': new} if old is not None else None),
    }
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    F.append(d)


# ---------------------------------------------------------------- page 56
add(56, '(18.2.5), first diagram (morphism of two extensions of B\'): labels h and g',
    'h and g stand left of their vertical arrows; 1_B\' right',
    '\\ar[d]^h, \\ar[d]^g put the labels right of the arrows',
    'formula', None, 'high',
    "\\ar[d]^h & E'_1\\ar[r]\\ar[d]^g",
    "\\ar[d]_h & E'_1\\ar[r]\\ar[d]_g",
    'Position of the labels only (enlarged crop).')

add(56, '(18.2.5): \'on en déduit un morphisme image réciproque par v\'',
    "'image réciproque' italic, 'par' roman, v italic",
    '\\emph{image réciproque par $v$} ("par" italic)',
    'italics', None, 'high',
    '\\emph{image réciproque par $v$}',
    '\\emph{image réciproque} par $v$',
    'Enlarged crop.')

add(56, '(18.2.5), second diagram (image réciproque par v): labels h and g×_{B\'}1_B',
    'h and g×_{B\'}1_B stand left of their vertical arrows; 1_B right',
    '\\ar[d]^h, \\ar[d]^{g\\times_{B\'}1_B}: labels right of the arrows',
    'formula', None, 'high',
    "\\ar[d]^h & E'_1\\times_{B'}B\\ar[r]\n      \\ar[d]^{g\\times_{B'}1_B}",
    "\\ar[d]_h & E'_1\\times_{B'}B\\ar[r]\n      \\ar[d]_{g\\times_{B'}1_B}",
    'Position of the labels only. Apply before the next finding (bold h), whose old is taken from the text after this edit.')

add(56, '(18.2.5), second diagram: label h of the arrow L\'_1 -> L\'_2',
    'h in bold italic (heavier than the g beside it and than the h of the first diagram; 3x crop)',
    'plain h',
    'misprint_in_print', None, 'medium',
    "\\ar[d]_h & E'_1\\times",
    "\\ar[d]_{\\boldsymbol{h}} & E'_1\\times",
    'Wrong-fount letter (GLOBAL_ISSUES 29): the TeX silently corrects it; the fix reproduces the bold italic h in the diplomatic text. old is taken from the text after the label-side edit listed just before.',
    corrected='h')

add(56, '(18.2.5), second diagram: right vertical arrow B -> B (1_B)',
    'isomorphism sign ≀ left of the arrow, 1_B right',
    '\\ar[d]^{1_B} without the ≀',
    'missing', None, 'high',
    "\\ar[d]^{1_B} & 0\\\\\n    0\\ar[r] & L'_2",
    "\\ar[d]^{1_B}_{\\wr} & 0\\\\\n    0\\ar[r] & L'_2",
    'Enlarged crop. The sign is set as a second label on the printed side (cf. the applied p. 55 fix \\ar[d]_{i\\wr}).')

add(56, '(18.2.5), second diagram, end of the bottom row',
    '... B -> 0 (no full stop)',
    '... B\\ar[r] & 0.',
    'punctuation', None, 'high',
    'B\\ar[r] & 0.',
    'B\\ar[r] & 0',
    'Enlarged crop.')

add(56, '(18.2.5): \'il se factorise à travers l\'image réciproque\'',
    "'factorise' italic, 'à travers' roman",
    '\\emph{factorise à travers}',
    'italics', None, 'high',
    '\\emph{factorise à travers}',
    '\\emph{factorise} à travers',
    'Enlarged crop.')

add(56, '(18.2.5), third diagram, first column of arrows: labels w_0 and u_0',
    'w_0 and u_0 left of their vertical arrows; 1_B right',
    '\\ar[d]^{w_0}, \\ar[d]^{u_0}: labels right of the arrows',
    'formula', None, 'high',
    '\\ar[d]^{w_0} & E\\ar[r]^f\\ar[d]^{u_0}',
    '\\ar[d]_{w_0} & E\\ar[r]^f\\ar[d]_{u_0}',
    'Position of the labels only.')

add(56, '(18.2.5), third diagram, second row of vertical arrows: labels i ≀ and p_1',
    'i and the sign ≀ left of the arrow L_0 -> L\'; p_1 left of its arrow; v right',
    '\\ar[d]^i (right) with \\ar@{}[d]|{\\wr} (≀ on the arrow), \\ar[d]^{p_1} (right)',
    'formula', None, 'high',
    '\\ar[d]^i\\ar@{}[d]|{\\wr} & F\\ar[r]^{p_2}\\ar[d]^{p_1}',
    '\\ar[d]_{i\\wr} & F\\ar[r]^{p_2}\\ar[d]_{p_1}',
    'Position of the labels only; same construction as the applied fix of the same row on p. 55 (\\ar[d]_{i\\wr}, \\ar[d]_{p_1}).')

add(56, '(18.2.5), third diagram: label v of the arrow B -> B\'',
    'v in bold italic (heavier than w_0, u_0, i, p_1 of the same diagram; enlarged crop)',
    'plain v',
    'misprint_in_print', None, 'medium',
    '\\ar[d]^v & 0\\\\',
    '\\ar[d]^{\\boldsymbol{v}} & 0\\\\',
    'Wrong-fount letter (GLOBAL_ISSUES 29): the TeX silently corrects it; the fix reproduces the bold italic v in the diplomatic text.',
    corrected='v')

fr_note = ('Fraktur K, not R: 3x crop; the glyph is the same as the \\mathfrak{K} of EGA I p. 184 (run_I_b) and unlike the '
           'Fraktur R of \'radical R(A)\', 0_I p. 12 (run_0I). Same letter as the 23 already fixed on pp. 52-54; '
           'these five are the last \\mathfrak{R} in ega0-18-fr.tex.')

add(56, '(18.2.6), l. 3: \'l\'idéal bilatère K de B, noyau de v\'',
    'Fraktur K', '\\mathfrak{R}', 'symbol', None, 'high',
    'bilatère $\\mathfrak{R}$', 'bilatère $\\mathfrak{K}$', fr_note)

add(56, '(18.2.6): \'homomorphisme de F-bimodules θ : K -> F\'',
    'Fraktur K', '\\mathfrak{R}', 'symbol', None, 'high',
    '$\\theta:\\mathfrak{R}\\to F$', '$\\theta:\\mathfrak{K}\\to F$', 'As above.')

add(56, '(18.2.6), triangle diagram: top vertex',
    'Fraktur K', '\\mathfrak{R}', 'symbol', None, 'high',
    '& \\mathfrak{R}\\ar[ld]', '& \\mathfrak{K}\\ar[ld]', 'As above (3x crop of this vertex).')

add(56, '(18.2.6), triangle diagram: label θ of the diagonal arrow',
    'θ above left of the diagonal arrow (outside the triangle)',
    '\\ar[ld]^\\theta puts θ below right, inside the triangle',
    'formula', None, 'high',
    '\\ar[ld]^\\theta\\ar[d]', '\\ar[ld]_\\theta\\ar[d]',
    'Position of the label only; independent of the Fraktur-K edit on the same line.')

add(56, '(18.2.6): \'une extension E\' de B\'=B/K par L\'',
    'Fraktur K', '\\mathfrak{R}', 'symbol', None, 'high',
    "$B'=B/\\mathfrak{R}$", "$B'=B/\\mathfrak{K}$", 'As above.')

add(56, '(18.2.6): \'de F-bimodules de K dans F\'',
    'Fraktur K', '\\mathfrak{R}', 'symbol', None, 'high',
    'de $\\mathfrak{R}$ dans $F$', 'de $\\mathfrak{K}$ dans $F$', 'As above (3x crop).')

add(56, '(18.2.6): \'donnent deux A-extensions A-équivalentes de B par L\'',
    "'équivalentes' italic (A- roman)",
    '$A$-équivalentes upright',
    'italics', None, 'high',
    '$A$-équivalentes de $B$ par $L$, il faut',
    '$A$-\\emph{équivalentes} de $B$ par $L$, il faut',
    'Enlarged crop.')

add(56, '(18.2.6): \'deux A-extensions A-équivalentes de B par L\'',
    "'de B par L' (no prime on B; enlarged crop)",
    'de $B$ par $L$ (keeps the printed reading)',
    'misprint_in_print', None, 'medium',
    None, None,
    'The extensions determined by θ_1, θ_2 are extensions of B\'=B/K by L (they are compared through F, their common inverse image, in the next lines and in (18.2.5)); the printed B lacks its prime. The TeX keeps the printed reading. For the corrected edition: the B in \'$A$-équivalentes de $B$ par $L$, il faut\'.',
    corrected="de $B'$ par $L$")

add(56, '(18.2.6), last line: \'une A-équivalence u de la A-extension F\'',
    "'équivalence' italic (A- roman)",
    '$A$-équivalence upright',
    'italics', None, 'high',
    'une $A$-équivalence $u$', 'une $A$-\\emph{équivalence} $u$',
    'Enlarged crop.')

# ---------------------------------------------------------------- page 57
add(57, '(18.2.7): \'dans la catégorie des A-bimodules (0_III, 8.1.11)\'',
    'bold 0', '$0_{\\mathrm{III}}$', 'convention', 2, 'high',
    '($0_{\\mathrm{III}}$, 8.1.11)', '($\\mathbf{0}_{\\mathrm{III}}$, 8.1.11)', '')

add(57, '(18.2.7): \'l\'homomorphisme x ⇝ (f(x), —g(x))\'',
    'wavy arrow x ⇝ (...)', '$x\\mapsto(f(x)', 'symbol', None, 'high',
    '$x\\mapsto(f(x)', '$x\\leadsto(f(x)',
    'Wavy arrow, neither a plain arrow nor ↦ (GLOBAL_ISSUES 33).')

add(57, '(18.2.7): \'(f(x), —g(x))\'',
    'long dash as minus sign: —g(x)', '-g(x)', 'convention', 7, 'high',
    ',-g(x))$', ',\\setmin g(x))$',
    'Long dash used for a (unary) minus (GLOBAL_ISSUES 23, 49); \\setmin pending the convention-7 decision.')

add(57, '(18.2.8): \'un homomorphisme de B-bimodules. Soit H\'',
    "'bimodules' italic", '$B$-bimodules upright', 'italics', None, 'high',
    'homomorphisme de $B$-bimodules. Soit', 'homomorphisme de $B$-\\emph{bimodules}. Soit',
    'Enlarged crop.')

add(57, '(18.2.8): \'une structure de A-anneau et définir une A-extension\'',
    "'anneau' and 'extension' italic", 'both upright', 'italics', None, 'high',
    'structure de $A$-anneau et définir une $A$-extension',
    'structure de $A$-\\emph{anneau} et définir une $A$-\\emph{extension}',
    'Enlarged crop.')

add(57, '(18.2.8): \'l\'application θ : z ⇝ (j(z), —w(z))\'',
    'wavy arrow', '\\mapsto', 'symbol', None, 'high',
    '$\\theta:z\\mapsto(j(z)', '$\\theta:z\\leadsto(j(z)',
    'Wavy arrow (GLOBAL_ISSUES 33).')

add(57, '(18.2.8): \'θ : z ⇝ (j(z), —w(z)) de L dans G\'',
    'long dash as minus sign', '-w(z)', 'convention', 7, 'high',
    ',-w(z))$ de $L$', ',\\setmin w(z))$ de $L$',
    'Long dash for a unary minus; \\setmin pending the convention-7 decision.')

add(57, '(18.2.8): \'c\'est un homomorphisme de G-bimodules\'',
    "'bimodules' italic", '$G$-bimodules upright', 'italics', None, 'high',
    'homomorphisme de $G$-bimodules ($L$', 'homomorphisme de $G$-\\emph{bimodules} ($L$',
    'The second \'G-bimodule\' of the line is roman, as in the TeX.')

add(57, '(18.2.8): \'au moyen de l\'homomorphisme canonique p : G -> E\'',
    'italic p (the same letter as the label p of G -> E in the diagram below)',
    '\\rho', 'symbol', None, 'high',
    '$\\rho:G\\to E$', '$p:G\\to E$',
    'Enlarged crop: italic p with its serif and descender, not a rho.')

add(57, '(18.2.8): \'on a (j(z), —w(z))(x, z\')\'',
    'long dash as minus sign', '-w(z)', 'convention', 7, 'high',
    "$(j(z),-w(z))(x,z')", "$(j(z),\\setmin w(z))(x,z')",
    'Long dash for a unary minus; \\setmin pending the convention-7 decision.')

add(57, '(18.2.8): \'= (j(z)x, j(z)z\' — w(z)x)\'',
    'long dash as minus sign', "j(z)z'-w(z)", 'convention', 7, 'high',
    "j(z)z'-w(z)", "j(z)z'\\setmin w(z)",
    'Long dash for a subtraction; independent of the next edit (either order).')

add(57, '(18.2.8): right-hand side \'(j(z)x, j(z)z\' — w(z)x)\'',
    "second component ends 'w(z)x' (x acting on L' through its E-bimodule structure)",
    "w(z)f(x)", 'formula', None, 'high',
    'w(z)f(x))$~; or', 'w(z)x)$~; or',
    'Enlarged crop. The printed reading is correct as it stands (E acts on L\' through f).')

add(57, '(18.2.8): \'..., et j(z)x = j(zf(x)) et w(z)x = w(zf(x)); on vérifie de même\'',
    "'et j(z)x=j(zf(x)) et w(z)x=w(zf(x));'",
    "'et $w(z)f(x)=w(zf(x))$ par définition de la structure de $B$-bimodule sur $L'$~;'",
    'formula', None, 'high',
    "et $w(z)f(x)=w(zf(x))$ par définition de la structure de $B$-bimodule\nsur $L'$~;",
    "et $j(z)x=j(zf(x))$ et\n$w(z)x=w(zf(x))$~;",
    'Enlarged crop. The TeX drops the formula j(z)x=j(zf(x)), changes w(z)x to w(z)f(x) and adds the clause \'par définition de la structure de B-bimodule sur L\'\' that the print does not have.')

add(57, '(18.2.8), diagram: position of 0 and L and the label θ',
    "the column 0 -> L -> E -> B -> 0 stands over E: j : L -> E, θ : L -> G (diagonal), θ above left of its arrow",
    "0 and L are in the third column (over G): the TeX's j goes L -> G and θ goes L -> L'; ^\\theta below right",
    'formula', None, 'high',
    "    & & 0\\ar[d] & & \\\\\n    & & L\\ar[ld]^\\theta\\ar[d]^j & & \\\\",
    "    & & & 0\\ar[d] & \\\\\n    & & & L\\ar[ld]_\\theta\\ar[d]^j & \\\\",
    'One edit: moves 0 and L one column to the right (over E) and puts θ on the printed side.')

# ---------------------------------------------------------------- page 58
add(58, '(18.2.8), first diagram: labels 1_L ≀, g, h',
    '1_L left and ≀ right of the arrow L -> L; g and h left of their arrows',
    '\\ar[d]^{1_L} (right) with \\ar@{}[d]|{\\wr} (≀ on the arrow), \\ar[d]^g, \\ar[d]^h (right)',
    'formula', None, 'high',
    '\\ar[d]^{1_L}\\ar@{}[d]|{\\wr}\n      & E_1\\ar[r]\\ar[d]^g & B_1\\ar[r]\\ar[d]^h',
    '\\ar[d]_{1_L}^{\\wr}\n      & E_1\\ar[r]\\ar[d]_g & B_1\\ar[r]\\ar[d]_h',
    'Position of the labels and of the sign ≀ only (cf. the applied p. 55 fix \\ar[d]_{i\\wr}).')

add(58, '(18.2.8), second diagram: labels 1_{L\'} ≀, g⊕_L1_{L\'}, h',
    '1_{L\'} left and ≀ right of the first arrow; g⊕_L1_{L\'} and h left of their arrows',
    'labels right of the arrows (^); ≀ on the arrow',
    'formula', None, 'high',
    "\\ar[d]^{1_{L'}}\\ar@{}[d]|{\\wr}\n      & E_1\\oplus_LL'\\ar[r]\\ar[d]^{g\\oplus_L1_{L'}}\n      & B_1\\ar[r]\\ar[d]^h",
    "\\ar[d]_{1_{L'}}^{\\wr}\n      & E_1\\oplus_LL'\\ar[r]\\ar[d]_{g\\oplus_L1_{L'}}\n      & B_1\\ar[r]\\ar[d]_h",
    'Position of the labels and of the sign ≀ only.')

add(58, '(18.2.8), second diagram, end of the bottom row',
    '... B_2 -> 0 (no full stop)', '... B_2\\ar[r] & 0.', 'punctuation', None, 'high',
    'B_2\\ar[r] & 0.', 'B_2\\ar[r] & 0', 'Enlarged crop.')

add(58, '(18.2.8): \'il se factorise à travers la A-extension H\'',
    "'factorise' italic, 'à travers' roman", '\\emph{factorise\\nà travers}', 'italics', None, 'high',
    '\\emph{factorise\nà travers}', '\\emph{factorise}\nà travers', 'Enlarged crop.')

add(58, '(18.2.8), third diagram: label w_0',
    'w_0 left of the arrow L -> L\'_0', '\\ar[d]^{w_0} (right)', 'formula', None, 'high',
    '\\ar[d]^{w_0}', '\\ar[d]_{w_0}', 'Position of the label only.')

add(58, '(18.2.8), third diagram: sign ≀ of the arrow 1_B',
    '≀ left of the arrow B -> B, 1_B right',
    '\\ar@{}[d]|{\\wr} (≀ on the arrow)', 'formula', None, 'high',
    '\\ar[d]^{1_B}\\ar@{}[d]|{\\wr}', '\\ar[d]^{1_B}_{\\wr}',
    'Position of the sign only.')

add(58, '(18.2.8), third diagram: labels j_2 and j_0 ≀',
    'j_2 below the arrow L\'_0 -> H; j_0 and ≀ left of the arrow L\'_0 -> L\'',
    '\\ar[r]^{j_2} (above), \\ar[d]^{j_0} (right) with \\ar@{}[d]|{\\wr}', 'formula', None, 'high',
    '\\ar[r]^{j_2}\\ar[d]^{j_0}\\ar@{}[d]|{\\wr}', '\\ar[r]_{j_2}\\ar[d]_{j_0\\wr}',
    'Position of the labels only (enlarged crop); same construction as the applied p. 55 fix \\ar[d]_{i\\wr}.')

add(58, '(18.2.8), third diagram: label f_0',
    'f_0 below the arrow H -> B', '\\ar[r]^{f_0} (above)', 'formula', None, 'high',
    '\\ar[r]^{f_0}', '\\ar[r]_{f_0}', 'Position of the label only (enlarged crop).')

add(58, 'Proposition (18.2.9): \'rendant commutatif les diagrammes\'',
    "'commutatif' without the plural s (enlarged crop)", "'commutatif' (keeps the printed reading)",
    'misprint_in_print', None, 'medium',
    None, None,
    'Agreement slip in the print (adjective with the plural \'les diagrammes\'); the TeX keeps the printed reading.',
    corrected='rendant commutatifs les diagrammes')

# ---------------------------------------------------------------- page 59
add(59, 'proof of (18.2.9): \'l\'application (x, s) ⇝ (v(x), w(s))\'',
    'wavy arrow', '\\mapsto', 'symbol', None, 'high',
    '$(x,s)\\mapsto(v(x),w(s))$', '$(x,s)\\leadsto(v(x),w(s))$', 'Wavy arrow (GLOBAL_ISSUES 33).')

add(59, 'Proposition (18.2.10): \'(autrement dit, l\'ensemble des A-homomorphismes inverses à droite de l\'augmentation E -> B)\'',
    'the parenthesis is roman inside the italic statement',
    'italic (inside the proposition environment)',
    'convention', 6, 'high',
    "(autrement dit, l'ensemble des\n$A$-homomorphismes inverses à droite de l'augmentation $E\\to B$)",
    "\\textup{(autrement dit, l'ensemble des\n$A$-homomorphismes inverses à droite de l'augmentation $E\\to B$)}",
    'Enlarged crop.')

add(59, 'Proposition (18.2.10): \'g\' : (x, s) ⇝ g(x)+s\'',
    'wavy arrow', '\\mapsto', 'symbol', None, 'high',
    "$g':(x,s)\\mapsto g(x)+s$", "$g':(x,s)\\leadsto g(x)+s$", 'Wavy arrow (GLOBAL_ISSUES 33).')

add(59, 'Proposition (18.2.10): \'le B-homomorphisme x ⇝ g\'(x, 0)\'',
    'wavy arrow', '\\mapsto', 'symbol', None, 'high',
    "$x\\mapsto g'(x,0)$", "$x\\leadsto g'(x,0)$", 'Wavy arrow (GLOBAL_ISSUES 33).')

add(59, 'heading 18.3',
    "'18.3. Le groupe des classes de A-extensions.' (final full stop)",
    '\\subsection{Le groupe des classes de $A$-extensions} (no full stop)',
    'punctuation', None, 'high',
    '\\subsection{Le groupe des classes de $A$-extensions}',
    '\\subsection{Le groupe des classes de $A$-extensions.}',
    'GLOBAL_ISSUES 43/57 (subsection titles lack the printed full stop).')

add(59, '(18.3.1): \'et l\'on peut écrire c_{x+y}=c_x+c_y+φ(x, y), c_{xy}=c_xc_y+ψ(x, y), où\'',
    'the two formulas are set inline in the running text',
    'displayed with \\[ ... \\qquad ... \\]',
    'other', None, 'high',
    "et l'on peut écrire\n\\[\n  c_{x+y}=c_x+c_y+\\varphi(x,y),\\qquad\n  c_{xy}=c_xc_y+\\psi(x,y),\n\\]\noù $\\varphi(x,y)$",
    "et l'on peut écrire\n$c_{x+y}=c_x+c_y+\\varphi(x,y)$,\n$c_{xy}=c_xc_y+\\psi(x,y)$, où $\\varphi(x,y)$",
    'Layout only (display vs inline, GLOBAL_ISSUES 21); the formulas themselves match.')

add(59, '(18.3.2): \'la classe de la A-extension E⊕_LL\' déduite de w, en vertu de (18.2.8)\'',
    "'déduite de w,'", "'déduite de $E$ par $w$,'", 'extra', None, 'high',
    'déduite de $E$\npar $w$', 'déduite de\n$w$',
    "Enlarged crop: the print has no 'E par'.")

add(59, '(18.3.2): after (18.3.2.1), \'En effet, on sait qu\'il existe\'',
    "'En effet' begins an indented new paragraph",
    'no blank line after \\end{equation}',
    'other', None, 'high',
    '\\end{equation}\nEn effet, on sait', '\\end{equation}\n\nEn effet, on sait',
    'Paragraph break missing in the TeX.')

add(59, '(18.3.2): \'(cf. par exemple (I, 3.3.9))\'',
    'bold I', '$\\mathrm{I}$', 'convention', 2, 'high',
    '($\\mathrm{I}$, 3.3.9)', '(\\textbf{I}, 3.3.9)', '')

add(59, 'last line \'..., d\'où\' and the page break to p. 60 (sentence continues \'la relation (18.3.2.1)\')',
    'no paragraph break: p. 60 begins at the left margin',
    'blank line before \\oldpage[0\\textsubscript{IV-1}]{60} (and another after it)',
    'other', None, 'high',
    '$A$-extensions, d\'où\n\n', '$A$-extensions, d\'où\n',
    'Spurious paragraph break mid-sentence; the blank line is the last line of the p. 59 segment. Apply together with the p. 60 finding that removes the blank line after the marker (both blank lines must go).')

# ---------------------------------------------------------------- page 60
add(60, 'top of the page: \'la relation (18.3.2.1).\' continues the sentence of p. 59',
    'no indentation (continuation of the paragraph)',
    'blank line after \\oldpage[0\\textsubscript{IV-1}]{60}',
    'other', None, 'high',
    '\\oldpage[0\\textsubscript{IV-1}]{60}\n\nla relation', '\\oldpage[0\\textsubscript{IV-1}]{60}\nla relation',
    'Spurious paragraph break; apply together with the p. 59 finding that removes the blank line before the marker.')

add(60, '(18.3.2): \'Si C_B désigne la catégorie des B-bimodules\'',
    'bold italic C', '\\mathbf C (bold upright)', 'font', None, 'high',
    'Si $\\mathbf C_B$ désigne', 'Si $\\boldsymbol{C}_B$ désigne',
    'Enlarged crop; category letter bold italic as in 0_III section 8 (\\boldsymbol, as in the earlier fixes).')

add(60, '(18.3.2): \'un foncteur covariant T : C_B -> Ens\'',
    'bold italic C and bold italic Ens', '\\mathbf C, \\mathbf{Ens} (bold upright)', 'font', None, 'high',
    '$T:\\mathbf C_B\\to\\mathbf{Ens}$', '$T:\\boldsymbol{C}_B\\to\\boldsymbol{\\mathit{Ens}}$',
    'Enlarged crop; \\boldsymbol{\\mathit{Ens}} as in the 0_III fixes.')

add(60, '(18.3.4): \'s : L×L -> L de B-bimodules\'',
    "'bimodules' italic", '$B$-bimodules upright', 'italics', None, 'high',
    '$s:L\\times L\\to L$ de $B$-bimodules', '$s:L\\times L\\to L$ de $B$-\\emph{bimodules}',
    'Enlarged crop.')

add(60, '(18.3.5): \'Désignons par K la catégorie\'',
    'bold italic K', '\\mathbf K (bold upright)', 'font', None, 'high',
    'Désignons par $\\mathbf K$ la', 'Désignons par $\\boldsymbol{K}$ la',
    'Enlarged crop; category letter K bold italic as in GLOBAL_ISSUES 18.')

add(60, '(18.3.5), diagram: label v of the arrow B\' -> B',
    'v right of the upward arrow (u left of its arrow, w right of the downward arrow)',
    "B'\\ar[u]^v puts v left of the arrow",
    'formula', None, 'high',
    "B'\\ar[u]^v", "B'\\ar[u]_v",
    'Position of the label only; the u and w labels are on the printed sides.')

add(60, 'last line \'w(v(b\')z)=b\'w(z) et\' and the page break to p. 61 (sentence continues \'w(zv(b\'))=w(z)b\' quels que soient\')',
    'no paragraph break: p. 61 begins at the left margin (checked on the p. 61 scan)',
    'blank line before \\oldpage[0\\textsubscript{IV-1}]{61} (and another after it)',
    'other', None, 'high',
    "$w(v(b')z)=b'w(z)$ et\n\n", "$w(v(b')z)=b'w(z)$ et\n",
    'Spurious paragraph break mid-sentence; the blank line is the last line of the p. 60 segment. The blank line after the p. 61 marker is already gone from the current ega0-18-fr.tex, so this edit completes the repair.')

json.dump(F, open(OUT, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print('wrote', len(F), 'findings to', OUT)
