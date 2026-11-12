import json, pathlib, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
RUN = pathlib.Path(r'user\Documents\ega_scan_check_20261101\run_IV2')
OUT = RUN / 'findings_115_119.json'

F = []


def add(page, where, scan, tex, kind, fix, conv=None, conf='high', note='', corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf, fix=fix)
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    F.append(d)


def fx(old, new):
    return {'old': old, 'new': new}


BLANK = 'Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20).'

# ---------------- p. 115 ----------------
add(115, "l. 1: 'de la forme (5.10.2, b)) de la condition'",
    "italic 'b)' (letter and its parenthesis), then the roman ')' (enlarged crop)", "upright b)",
    'italics', fx('(5.10.2, b))', r'(5.10.2, \emph{b)})'))
add(115, "Corollaire (5.10.4): 'il faut et il suffit que prof_{Z_x}(F~_x) >= 1 (avec les notations ...)'",
    "the formula is in the running text of the statement ('il faut et il suffit que prof... >= 1 (avec les notations de ...)' on one line)",
    'set as a display \\[ ... \\]', 'other',
    fx('\\[\n\\operatorname{prof}_{Z_x}(\\widetilde{\\mathcal F}_x)\\geq1\n\\]',
       '$\\operatorname{prof}_{Z_x}(\\widetilde{\\mathcal F}_x)\\geq1$'),
    note='Formula displayed where the print has it inline; no connecting word lost.')
add(115, "Corollaire (5.10.4): '(avec les notations de (5.9 6))'",
    "both outer parentheses and the reference upright inside the italic statement; 'avec les notations de' italic (enlarged crop)",
    'whole parenthesis italic (corollary environment)', 'convention',
    fx('(avec les notations de (5.9.6)).', '\\textup{(}avec les notations de \\textup{(5.9.6))}.'),
    conv=6, conf='medium',
    note="Apply before the misprint entry that follows (its 'old' (5.9.6)) occurs once before and after this edit).")
add(115, "Corollaire (5.10.4): '(avec les notations de (5.9 6))'",
    "(5.9 6): no point between 9 and 6, a space instead (3x crop)", "(5.9.6)",
    'misprint_in_print', fx('(5.9.6))', '(5.9 6))'), corrected='(5.9.6)',
    note="The TeX silently corrects; the fix restores the printed reading and changes only the missing point. "
         "Its 'old' occurs once before and after the convention-6 edit above; list order: convention edit first.")
add(115, "Théorème (5.10.5): 'il faut et il suffit que l'on ait prof_Z(F) >= 2.'",
    "the formula ends the statement in the running text ('l'on ait prof_Z(F)>=2.')",
    'set as a display \\[ ... \\]', 'other',
    fx('\\[\n\\operatorname{prof}_Z(\\mathcal F)\\geq2.\n\\]', '$\\operatorname{prof}_Z(\\mathcal F)\\geq2$.'),
    note='Formula displayed where the print has it inline; no connecting word lost.')
add(115, "proof of (5.10.5): 'On peut donc déjà se borner au cas où Z est fermé.'",
    "'fermé' italic (crop)", 'fermé upright', 'italics',
    fx('$Z$ est fermé. La', '$Z$ est \\emph{fermé}. La'))
add(115, "proof of (5.10.5): 'et comme Ass(F) ⊂ X—Z, il y a'",
    'long dash for the set difference X—Z', 'X-Z', 'convention',
    fx('\\subset X-Z$, il y', '\\subset X\\setmin Z$, il y'), conv=7)
add(115, "proof of (5.10.5): 'Ass(F) ⊂ X_f ⊂ X—Z (II, 4.5.4)'",
    'long dash for the set difference X—Z', 'X-Z', 'convention',
    fx('X_f\\subset X-Z$', 'X_f\\subset X\\setmin Z$'), conv=7)
add(115, "proof of (5.10.5): '(II, 4.5.4)'", 'bold II', 'plain II', 'convention',
    fx('(II, 4.5.4)', '(\\textbf{II}, 4.5.4)'), conv=2)
add(115, "proof of (5.10.5): 'donc prof(F_y) = 1 + prof(F_y/f_yF_y) (0, 16.4.6). La condition'",
    'formula and reference in the running text (the sentence continues on the same line with \'La condition\')',
    'displayed with \\[ ... \\quad(0, 16.4.6). \\]', 'other',
    fx('\\[\n\\operatorname{prof}(\\mathcal F_y)\n=1+\\operatorname{prof}(\\mathcal F_y/f_y\\mathcal F_y)\n\\quad(0, 16.4.6).\n\\]',
       '$\\operatorname{prof}(\\mathcal F_y)\n=1+\\operatorname{prof}(\\mathcal F_y/f_y\\mathcal F_y)$\n(0, 16.4.6).'),
    note='Display vs inline. Apply before the convention-2 edit of (0, 16.4.6) (next entry).')
add(115, "proof of (5.10.5): '(0, 16.4.6)'", 'bold 0', 'plain 0', 'convention',
    fx('(0, 16.4.6).', '(\\textbf{0}, 16.4.6).'), conv=2,
    note="'old' occurs once before and after the inline edit above.")
add(115, "proof of (5.10.5): 'au fait que F/fF est Z-pur, et il suffit de voir'",
    "'pur' italic (enlarged crop; the other Z-pur on the page are roman)", 'upright', 'italics',
    fx('$Z$-pur, et il suffit', '$Z$-\\emph{pur}, et il suffit'))
add(115, "proof of (5.10.5): 'équivaut au fait que F est Z-clos.'",
    "'clos' italic (enlarged crop)", 'upright', 'italics',
    fx('$Z$-clos.', '$Z$-\\emph{clos}.'))
add(115, "proof of (5.10.5): 'Considérons la suite exacte 0 → F →(f) F → F/fF → 0 (l'homothétie ...'",
    'the exact sequence is in the running text, followed on the same line by \'(l\'homothétie de rapport\'',
    'set as a display \\[ ... \\]', 'other',
    fx('\\[\n0\\longrightarrow\\mathcal F\\xrightarrow{f}\\mathcal F\n\\longrightarrow\\mathcal F/f\\mathcal F\\longrightarrow0\n\\]',
       '$0\\to\\mathcal F\\xrightarrow{f}\\mathcal F\n\\to\\mathcal F/f\\mathcal F\\to0$'),
    note='Formula displayed where the print has it inline; no connecting word lost.')
add(115, "proof of (5.10.5): '(l'homothétie de rapport f : F →(f) F étant par hypothèse injective)'",
    'the arrow carries an f above it (3x crop), as in the exact sequence', 'f:\\mathcal F\\to\\mathcal F (bare arrow)', 'formula',
    fx('$f:\\mathcal F\\to\\mathcal F$', '$f:\\mathcal F\\xrightarrow{f}\\mathcal F$'))
add(115, "proof of (5.10.5): 'si on pose W = X—Z'", 'long dash for the set difference', 'X-Z', 'convention',
    fx('$W=X-Z$', '$W=X\\setmin Z$'), conv=7)
add(115, "proof of (5.10.5): '(I, 1.4.1)'", 'bold I', 'plain I', 'convention',
    fx('(I, 1.4.1)', '(\\textbf{I}, 1.4.1)'), conv=2)
add(115, "end of p. 115: '... de la forme f^nt', où t' ∈ Γ(X, F)' continues on p. 116 'pour montrer que ...'",
    'mid-sentence page break', 'blank line before \\oldpage[IV-2]{116}', 'other',
    fx("$t'\\in\\Gamma(X,\\mathcal F)$\n\n", "$t'\\in\\Gamma(X,\\mathcal F)$\n"),
    note=BLANK + " Apply together with the p. 116 entry removing the blank line after \\oldpage[IV-2]{116}.")

# ---------------- p. 116 ----------------
add(116, "top of p. 116: 'pour montrer que l'homomorphisme ...' continues the sentence of p. 115",
    'flush left, no new paragraph', 'blank line after \\oldpage[IV-2]{116}', 'other',
    fx('\\oldpage[IV-2]{116}\n\npour montrer', '\\oldpage[IV-2]{116}\npour montrer'),
    note=BLANK + ' Apply together with the p. 115 entry (blank line before the marker).')
add(116, "Théorème (5.10.7): 'C—(C∩Y) est connexe'", 'long dash for the set difference', 'C-(C\\cap Y)', 'convention',
    fx('$C-(C\\cap Y)$', '$C\\setmin(C\\cap Y)$'), conv=7)
add(116, "proof of (5.10.7): 'O_X → i_*(O_X|X—Y)'", 'long dash for the set difference', 'X-Y', 'convention',
    fx('i_*(\\mathcal O_X|X-Y)', 'i_*(\\mathcal O_X|X\\setmin Y)'), conv=7)
add(116, "proof of (5.10.7): '(où i : X—Y → X est l'injection canonique)'", 'long dash for the set difference', 'X-Y', 'convention',
    fx('$i:X-Y\\to X$', '$i:X\\setmin Y\\to X$'), conv=7)
add(116, "proof of (5.10.7): 'Γ(X, O_X) → Γ(X—Y, O_X)'", 'long dash for the set difference', 'X-Y', 'convention',
    fx('\\Gamma(X-Y,\\mathcal O_X)', '\\Gamma(X\\setmin Y,\\mathcal O_X)'), conv=7)
add(116, "proof of (5.10.7): 'le lemme (III, 7.8.6.1)'", 'bold III', 'plain III', 'convention',
    fx('(III, 7.8.6.1)', '(\\textbf{III}, 7.8.6.1)'), conv=2)
add(116, "Corollaire (5.10.8): 'on ait codim(X_{i-1}∩X_i, X) ≤ d—1 (on dit alors ...)'",
    "the formula is in the running text: the line reads 'codim(X_{i-1}∩X_i, X)≤d—1 (on dit alors que X est connexe en codimension ≤d—1).'",
    'set as a display \\[ ... \\]', 'other',
    fx('\\[\n\\operatorname{codim}(X_{i-1}\\cap X_i,X)\\leq d-1\n\\]',
       '$\\operatorname{codim}(X_{i-1}\\cap X_i,X)\\leq d-1$'),
    note='Formula displayed where the print has it inline; no connecting word lost. Apply before the convention-7 entry for d—1 (next).')
add(116, "Corollaire (5.10.8): 'codim(X_{i-1}∩X_i, X) ≤ d—1'", 'long dash for the minus in d—1 (crop)', 'd-1', 'convention',
    fx('X_i,X)\\leq d-1', 'X_i,X)\\leq d\\setmin 1'), conv=7,
    note="Subtraction (GLOBAL_ISSUES 23). 'old' occurs once before and after the inline edit.")
add(116, "Corollaire (5.10.8): '(on dit alors que X est connexe en codimension ≤ d—1)'",
    "'(on dit alors que X est' and the closing parenthesis upright; only 'connexe en codimension' italic (crop)",
    'whole parenthesis italic (corollary environment), no emphasis on the defined term', 'convention',
    fx('(on dit alors que $X$ est connexe en codimension $\\leq d-1$)',
       '\\textup{(on dit alors que $X$ est \\emph{connexe en codimension} $\\leq d-1$)}'),
    conv=6, note='Also restores the printed italics of the defined term (\\emph inside \\textup). Apply before the convention-7 entry for this d—1 (next).')
add(116, "Corollaire (5.10.8): 'connexe en codimension ≤ d—1)'", 'long dash for the minus in d—1 (crop)', 'd-1', 'convention',
    fx('$\\leq d-1$)', '$\\leq d\\setmin 1$)'), conv=7,
    note="Subtraction (GLOBAL_ISSUES 23). 'old' occurs once before and after the convention-6 edit above.")
add(116, "proof of (5.10.8): 'il résulte de (5.10.7) que X—Y est connexe'", 'long dash for the set difference', 'X-Y', 'convention',
    fx('(5.10.7) que $X-Y$', '(5.10.7) que $X\\setmin Y$'), conv=7)
add(116, "proof of (5.10.8): '(0, 14.2.3)'", 'bold 0', 'plain 0', 'convention',
    fx('(0, 14.2.3)', '(\\textbf{0}, 14.2.3)'), conv=2)
add(116, "proof of (5.10.8): '(0, 14.2.5)'", 'bold 0', 'plain 0', 'convention',
    fx('(0, 14.2.5)', '(\\textbf{0}, 14.2.5)'), conv=2)
add(116, 'Lemme (5.10.8.1), label a)', 'a) upright (crop)', '\\item[a)] italic inside the italic lemma', 'convention',
    fx('\\item[a)]', '\\item[\\textup{a)}]'), conv=6)
add(116, "Lemme (5.10.8.1) a): 'Pour tout Y∈F, X—Y est connexe.'", 'long dash for the set difference', 'X-Y', 'convention',
    fx('\\mathfrak F$, $X-Y$ est connexe', '\\mathfrak F$, $X\\setmin Y$ est connexe'), conv=7)
add(116, 'Lemme (5.10.8.1), label b)', 'b) upright (crop)', '\\item[b)] italic inside the italic lemma', 'convention',
    fx('\\item[b)]', '\\item[\\textup{b)}]'), conv=6)
add(116, "proof of (5.10.8.1): 'Supposons b) vérifiée'", "'b)' italic, letter and parenthesis (crop)", 'upright b)', 'italics',
    fx('Supposons b) vérifiée', 'Supposons \\emph{b)} vérifiée'))
add(116, "proof of (5.10.8.1): 'prouvons que U = X—Y est connexe'", 'long dash for the set difference', 'X-Y', 'convention',
    fx('$U=X-Y$', '$U=X\\setmin Y$'), conv=7)
add(116, "proof of (5.10.8.1), last line: '(0_I, 2.1.6);'", 'bold 0 with subscript I', 'plain 0', 'convention',
    fx('(0$_\\mathrm I$, 2.1.6);', '(\\textbf{0}$_\\mathrm I$, 2.1.6);'), conv=2)
add(116, "end of p. 116: '... X''∩U = U'' (0_I, 2.1.6);' continues on p. 117 'formons pour ces deux composantes ...'",
    'mid-sentence page break', 'blank line before \\oldpage[IV-2]{117}', 'other',
    fx('2.1.6);\n\n', '2.1.6);\n'),
    note=BLANK + " Apply together with the p. 117 entry removing the blank line after \\oldpage[IV-2]{117}. 'old' occurs once before and after the convention-2 edit above.")

# ---------------- p. 117 ----------------
add(117, "top of p. 117: 'formons pour ces deux composantes ...' continues the sentence of p. 116",
    'flush left, no new paragraph', 'blank line after \\oldpage[IV-2]{117}', 'other',
    fx('\\oldpage[IV-2]{117}\n\nformons', '\\oldpage[IV-2]{117}\nformons'),
    note=BLANK + ' Apply together with the p. 116 entry (blank line before the marker).')
add(117, "l. 1: 'une suite (X_i) ayant la propriété énoncée'",
    'the subscript i is a bold italic i (wrong-font sort): 5x side-by-side crop with X_i in l. 2 shows a much thicker stem and dot; the X is normal',
    'plain i (silent correction)', 'misprint_in_print',
    fx('$(X_i)$ ayant', '$(X_{\\boldsymbol{i}})$ ayant'), conf='medium', corrected='$(X_i)$',
    note='Wrong-font sort (GLOBAL_ISSUES 29: wrong-font letters are reproduced in the diplomatic text); the TeX silently normalises it.')
add(117, "l. 1: 'la propriété énoncée dans b)'", "'b)' italic (crop)", 'upright b)', 'italics',
    fx('dans b) et posons', 'dans \\emph{b)} et posons'))
add(117, "l. 3: 'composante irréductible de U (0_I, 2.1.6) et de plus'", 'bold 0', 'plain 0', 'convention',
    fx('(0$_\\mathrm I$, 2.1.6) et de plus', '(\\textbf{0}$_\\mathrm I$, 2.1.6) et de plus'), conv=2)
add(117, "2nd paragraph: 'Montrons maintenant que a) entraîne b).'", "'a)' and 'b)' italic", 'upright', 'italics',
    fx('que a) entraîne b).', 'que \\emph{a)} entraîne \\emph{b)}.'))
add(117, "2nd paragraph: 'couples de composantes irréductibles distinctes de X'", "'distinctes' italic", 'upright', 'italics',
    fx('irréductibles distinctes de $X$ telles', 'irréductibles \\emph{distinctes} de $X$ telles'))
add(117, "2nd paragraph: 'donc U = X—Y est connexe'", 'long dash for the set difference', 'X-Y', 'convention',
    fx('$U=X-Y$', '$U=X\\setmin Y$'), conv=7)
add(117, "2nd paragraph: 'distinctes de U (0_I, 2.1.6). Or la réunion'", 'bold 0', 'plain 0', 'convention',
    fx('(0$_\\mathrm I$, 2.1.6). Or', '(\\textbf{0}$_\\mathrm I$, 2.1.6). Or'), conv=2)
add(117, "2nd paragraph: 'et U_n = W est un ensemble'",
    "the subscript n is a bold italic n (wrong-font sort): 5x crop beside 'U_n = U''' four lines below (stems about twice as thick; the two U are equally inked)",
    'plain n (silent correction)', 'misprint_in_print',
    fx('$U_n=W$', '$U_{\\boldsymbol{n}}=W$'), conf='medium', corrected='$U_n=W$',
    note='Wrong-font sort (GLOBAL_ISSUES 29); the TeX silently normalises it.')
add(117, "2nd paragraph: 'est un ensemble ouvert et fermé dans U'", "'ouvert et fermé' italic", 'upright', 'italics',
    fx('ensemble ouvert et fermé dans', 'ensemble \\emph{ouvert et fermé} dans'))
add(117, "2nd paragraph: 'telle que X_i∩U = U_i (0_I, 2.1.6); comme'", 'bold 0', 'plain 0', 'convention',
    fx('(0$_\\mathrm I$, 2.1.6); comme', '(\\textbf{0}$_\\mathrm I$, 2.1.6); comme'), conv=2)
add(117, "'lorsque X est un préschéma de Cohen-Macaulay et d ≥ 2'",
    "'préschéma de Cohen-Macaulay et' italic, 'et' included (crop)", 'upright', 'italics',
    fx('un préschéma de Cohen-Macaulay et $d', 'un \\emph{préschéma de Cohen-Macaulay et} $d'))
add(117, 'Proposition (5.10.10), label (i)', '(i) upright', '\\item[(i)] italic inside the italic proposition', 'convention',
    fx('\\item[(i)]', '\\item[\\textup{(i)}]'), conv=6, note='GLOBAL_ISSUES 16.')
add(117, 'Proposition (5.10.10), label (ii)', '(ii) upright', '\\item[(ii)] italic inside the italic proposition', 'convention',
    fx('\\item[(ii)]', '\\item[\\textup{(ii)}]'), conv=6, note='GLOBAL_ISSUES 16.')
add(117, "Proposition (5.10.10) (ii): 'x∈Ass(F)∩(X—Z)'", 'long dash for the set difference', 'X-Z', 'convention',
    fx('\\cap(X-Z)$', '\\cap(X\\setmin Z)$'), conv=7)
add(117, "Proposition (5.10.10) (ii): 'on a codim(Z∩{x}^-, {x}^-) ≥ 2.'",
    'the formula ends item (ii) in the running text, on the same line as \'Pour tout point x ...\'',
    'set as a display \\[ ... \\]', 'other',
    fx('\\[\n\\operatorname{codim}(Z\\cap\\overline{\\{x\\}},\\overline{\\{x\\}})\\geq2.\n\\]',
       '$\\operatorname{codim}(Z\\cap\\overline{\\{x\\}},\\overline{\\{x\\}})\\geq2$.'),
    note='Formula displayed where the print has it inline; no connecting word lost.')
add(117, 'Proposition (5.10.10), label (iii)', '(iii) upright', '\\item[(iii)] italic inside the italic proposition', 'convention',
    fx('\\item[(iii)]', '\\item[\\textup{(iii)}]'), conv=6, note='GLOBAL_ISSUES 16.')
add(117, "Proposition (5.10.10) (iii): '(notations de (5.9.6))'",
    'the whole parenthesis upright (roman) inside the italic statement', 'italic (proposition environment)', 'convention',
    fx('(notations de\n(5.9.6))', '\\textup{(notations de\n(5.9.6))}'), conv=6)
add(117, "Proposition (5.10.10) (iii): 'on a X—U ⊂ Z'", 'long dash for the set difference', 'X-U', 'convention',
    fx('$X-U\\subset Z$', '$X\\setmin U\\subset Z$'), conv=7)

# ---------------- p. 118 ----------------
add(118, "proof of (5.10.10): 'Soit x∈Ass(F)∩(X—Z)'", 'long dash for the set difference', 'X-Z', 'convention',
    fx('\\cap(X-Z)$', '\\cap(X\\setmin Z)$'), conv=7)
add(118, "proof of (5.10.10): 'les restrictions de F et F' à X—Z sont'", 'long dash for the set difference', 'X-Z', 'convention',
    fx('$X-Z$ sont', '$X\\setmin Z$ sont'), conv=7)
add(118, "proof of (5.10.10): 'en vertu de (i) et de (0, 16.4.6.2)'", 'bold 0', 'plain 0', 'convention',
    fx('(0, 16.4.6.2)', '(\\textbf{0}, 16.4.6.2)'), conv=2)
add(118, "proof of (5.10.10): '2 ≤ prof(F'_y) ≤ dim(O_y/p) = codim({y}^-, {x}^-), d'où (ii).'",
    "formula in the running text, followed on the same line by 'd'où (ii). Enfin, pour prouver (iii), notons'",
    'set as a display \\[ ... \\]', 'other',
    fx('\\[\n2\\leq\\operatorname{prof}(\\mathcal F\'_y)\n\\leq\\dim(\\mathcal O_y/\\mathfrak p)\n=\\operatorname{codim}(\\overline{\\{y\\}},\\overline{\\{x\\}}),\n\\]',
       '$2\\leq\\operatorname{prof}(\\mathcal F\'_y)\n\\leq\\dim(\\mathcal O_y/\\mathfrak p)\n=\\operatorname{codim}(\\overline{\\{y\\}},\\overline{\\{x\\}})$,'),
    note='Formula displayed where the print has it inline; no connecting word lost.')
add(118, "proof of (5.10.10): 'en vertu de l'hypothèse (0_I, 5.3.4)'", 'bold 0', 'plain 0', 'convention',
    fx('(0$_\\mathrm I$,\n5.3.4)', '(\\textbf{0}$_\\mathrm I$,\n5.3.4)'), conv=2)
add(118, "proof of (5.10.10): 'un support fermé (0_I, 5.2.2)'", 'bold 0', 'plain 0', 'convention',
    fx('(0$_\\mathrm I$, 5.2.2)', '(\\textbf{0}$_\\mathrm I$, 5.2.2)'), conv=2)
add(118, "proof of (5.10.10): 'enfin l'inclusion X—U ⊂ Z'", 'long dash for the set difference', 'X-U', 'convention',
    fx('inclusion $X-U\\subset Z$', 'inclusion $X\\setmin U\\subset Z$'), conv=7)
add(118, "(5.10.11): 'X' = Spec(H^0_{X/Z}(O_X)) (II, 1.3.1)'", 'bold II', 'plain II', 'convention',
    fx('(II, 1.3.1)', '(\\textbf{II}, 1.3.1)'), conv=2)
add(118, "(5.10.11): 'est appelé la Z-clôture de X'", "'clôture' italic (crop)", 'upright', 'italics',
    fx('la $Z$-clôture de', 'la $Z$-\\emph{clôture} de'))
add(118, "(5.10.11): 'le morphisme structural (II, 1.4.3)'", 'bold II', 'plain II', 'convention',
    fx('(II, 1.4.3)', '(\\textbf{II}, 1.4.3)'), conv=2)
add(118, "Proposition (5.10.12): 'Les notations étant celles de (5.10.11) :'",
    'the reference upright inside the italic statement (crop)', 'italic (proposition environment)', 'convention',
    fx('celles de (5.10.11):', 'celles de \\textup{(5.10.11)}:'), conv=6)
add(118, 'Proposition (5.10.12), label (i)', '(i) upright (crop)', '\\item[(i)] italic inside the italic proposition', 'convention',
    fx('\\item[(i)]', '\\item[\\textup{(i)}]'), conv=6, note='GLOBAL_ISSUES 16.')
add(118, "Proposition (5.10.12) (i): '(ce qui a lieu pour tout x∈X—Z)'", 'long dash for the set difference', 'X-Z', 'convention',
    fx('$x\\in X-Z$)', '$x\\in X\\setmin Z$)'), conv=7)
add(118, 'Proposition (5.10.12), label (ii)', '(ii) upright', '\\item[(ii)] italic inside the italic proposition', 'convention',
    fx('\\item[(ii)]', '\\item[\\textup{(ii)}]'), conv=6, note='GLOBAL_ISSUES 16.')
add(118, 'Proposition (5.10.12), label (iii)', '(iii) upright', '\\item[(iii)] italic inside the italic proposition', 'convention',
    fx('\\item[(iii)]', '\\item[\\textup{(iii)}]'), conv=6, note='GLOBAL_ISSUES 16.')
add(118, "Proposition (5.10.12) (iii): 'tel que X—U ⊂ Z'", 'long dash for the set difference', 'X-U', 'convention',
    fx('tel que $X-U\\subset Z$', 'tel que $X\\setmin U\\subset Z$'), conv=7)
add(118, "proof of (5.10.12): 'un ouvert V de X contenant Z—X, et son image réciproque'",
    'long dash for the set difference', 'Z-X', 'convention',
    fx('contenant $Z-X$', 'contenant $Z\\setmin X$'), conv=7,
    note='The order Z—X is a misprint (next entry); this edit keeps it.')
add(118, "proof of (5.10.12): 'un ouvert V de X contenant Z—X'",
    "Z—X (crop): an open V containing the empty set Z—X", "$Z-X$ (printed reading kept)", 'misprint_in_print',
    None, conf='high', corrected='contenant $X\\setmin Z$',
    note='The TeX keeps the printed reading. The open sets V are those containing X—Z: the proof continues on p. 119 '
         "'V_α parcourt la famille filtrante des ouverts contenant X—Z', and H^0_{X/Z} is the limit over such V (5.9.1). "
         'Correct reading X—Z (with the convention-7 macro; $X-Z$ with the present minus sign). Not in the authors\' errata list 3 (EGA IV part 4).')
add(118, "proof of (5.10.12): 'contenant Z—X, et son image réciproque'", 'comma after Z—X (crop)', 'no comma', 'punctuation',
    fx('$ et son image', '$, et son image'))
add(118, "end of p. 118: '... si i : V → X et i' : V' → X' sont les injections' continues on p. 119 'canoniques, ...'",
    'mid-sentence page break', 'blank line before \\oldpage[IV-2]{119}', 'other',
    fx('sont les injections\n\n', 'sont les injections\n'),
    note=BLANK + ' Apply together with the p. 119 entry removing the blank line after \\oldpage[IV-2]{119}.')

# ---------------- p. 119 ----------------
add(119, "top of p. 119: 'canoniques, l'homomorphisme canonique ...' continues the sentence of p. 118",
    'flush left, no new paragraph', 'blank line after \\oldpage[IV-2]{119}', 'other',
    fx('\\oldpage[IV-2]{119}\n\ncanoniques,', '\\oldpage[IV-2]{119}\ncanoniques,'),
    note=BLANK + ' Apply together with the p. 118 entry (blank line before the marker).')
add(119, "l. 2: 'soit l'homomorphisme canonique ρ_{X/Z} : H^0_{X/Z}(F) → i_*(H^0_{X/Z}(F)|V) (II, 1.4.2), compte'",
    'formula in the running text (line 2 of the page)', 'set as a display \\[ ... \\]', 'other',
    fx('\\[\n\\rho_{X/Z}:\\mathcal H^0_{X/Z}(\\mathcal F)\n\\longrightarrow i_*(\\mathcal H^0_{X/Z}(\\mathcal F)|V)\n\\]',
       '$\\rho_{X/Z}:\\mathcal H^0_{X/Z}(\\mathcal F)\n\\to i_*(\\mathcal H^0_{X/Z}(\\mathcal F)|V)$'),
    note='Formula displayed where the print has it inline; no connecting word lost.')
add(119, "l. 2: '(II, 1.4.2)'", 'bold II', 'plain II', 'convention',
    fx('(II, 1.4.2)', '(\\textbf{II}, 1.4.2)'), conv=2)
add(119, "l. 4: 'Comme X'—Z' est intersection'", 'long dash for the set difference', "X'-Z'", 'convention',
    fx("$X'-Z'$", "$X'\\setmin Z'$"), conv=7)
add(119, "l. 5: 'la famille filtrante des ouverts contenant X—Z'", 'long dash for the set difference', 'X-Z', 'convention',
    fx('contenant $X-Z$', 'contenant $X\\setmin Z$'), conv=7)
add(119, 'Proposition (5.10.14), label (i)', '(i) upright', '\\item[(i)] italic inside the italic proposition', 'convention',
    fx('\\item[(i)] Pour que', '\\item[\\textup{(i)}] Pour que'), conv=6, note='GLOBAL_ISSUES 16.')
add(119, 'Proposition (5.10.14), label (ii)', '(ii) upright', '\\item[(ii)] italic inside the italic proposition', 'convention',
    fx('\\item[(ii)]', '\\item[\\textup{(ii)}]'), conv=6, note='GLOBAL_ISSUES 16.')
add(119, "proof of (5.10.14) (i): 'on a dim(F_x) = 0 (3.1.4) autrement dit (5.1.12.1) dim(O_x) = 0'",
    'no comma after (3.1.4): the line ends with the parenthesis at the right margin, the next begins with \'autrement dit\' (3x crop)',
    "'(3.1.4), autrement dit' (comma supplied)", 'misprint_in_print',
    fx('(3.1.4), autrement', '(3.1.4) autrement'), conf='medium', corrected='(3.1.4), autrement dit',
    note="The TeX silently supplies the comma that sets off 'autrement dit'; the fix restores the printed reading. "
         "The reading is certain; 'medium' refers to calling the omission a misprint.")
add(119, "proof of (5.10.14) (ii): 'pour tout x∈X, la relation dim(F_x) ≥ 2 entraîne prof(F_x) ≥ 2'",
    'dim(F_x) with the script F (crop), like prof(F_x) after it', 'dim(\\mathcal O_x)', 'formula',
    fx('la relation $\\dim(\\mathcal O_x)\\geq2$ entraîne', 'la relation $\\dim(\\mathcal F_x)\\geq2$ entraîne'),
    note='Not a misprint: Supp(F) = X gives dim(F_x) = dim(O_x), and the print writes dim(F_x)=1 (ou, ce qui revient au même, dim(O_x)=1) a few lines below. The other dim(O_x) on the page are printed with O.')
add(119, 'Corollaire (5.10.15), label (i)', '(i) upright', '\\item[(i)] italic inside the italic corollary', 'convention',
    fx("\\item[(i)] $\\mathcal F'$", "\\item[\\textup{(i)}] $\\mathcal F'$"), conv=6, note='GLOBAL_ISSUES 16.')

json.dump(F, open(OUT, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)

# ---- verification: apply the fixes in list order to LF copies of the page files ----
ok = True
for page in sorted({x['page'] for x in F}):
    t = (RUN / ('page_%03d.tex' % page)).read_text(encoding='utf-8').replace('\r\n', '\n')
    orig = t
    for x in [y for y in F if y['page'] == page]:
        fix = x['fix']
        if not fix:
            continue
        n_now, n_orig = t.count(fix['old']), orig.count(fix['old'])
        if n_now != 1:
            ok = False
            print('FAIL p.%d: old occurs %d times at its turn: %r' % (page, n_now, fix['old'][:60]))
            continue
        if n_orig != 1:
            print('note p.%d: old occurs %d times in the original page file: %r' % (page, n_orig, fix['old'][:60]))
        t = t.replace(fix['old'], fix['new'])
print('all fixes apply in order' if ok else 'SOME FIXES FAIL')
cnt = {}
for x in F:
    k = 'misprint' if x['kind'] == 'misprint_in_print' else 'convention' if x['kind'] == 'convention' else 'normal'
    cnt.setdefault(x['page'], {'normal': 0, 'convention': 0, 'misprint': 0})[k] += 1
for p in sorted(cnt):
    print(p, cnt[p])
print('total', len(F))
