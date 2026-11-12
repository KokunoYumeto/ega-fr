import json

RUN = 'user/Documents/ega_scan_check_20261101/run_0IV1/'
OUT = RUN + 'findings_216_220.json'


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, nofix=False):
    d = {
        'page': page,
        'where': where,
        'scan': scan,
        'tex': tex,
        'kind': kind,
        'convention': conv,
        'confidence': conf,
        'fix': None if nofix else {'old': old, 'new': new},
    }
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    return d


B2 = 'Bold 0 of the chapter-0 sign printed; TeX plain 0.'
L = []

# ---------------- page 216 ----------------
L += [
    F(216, 'top of the page: ... il suffit évidemment de prouver | que B est un anneau japonais',
      'no paragraph break: the page starts mid-sentence, flush left',
      'blank line after the marker (and one before it, p. 215 segment): paragraph break',
      'other', None, 'high',
      '\\oldpage[0\\textsubscript{IV-1}]{216}\n\nque $B$', '\\oldpage[0\\textsubscript{IV-1}]{216}\nque $B$',
      'GLOBAL_ISSUES 20. Apply together with the p. 215 entry of findings_211_215.json that removes the blank line '
      'before the marker (\'évidemment de prouver\\n\\n\').'),
    F(216, 'proof of (23.1.5), line 4: soit x un élément de m-m^2',
      'm—m² with the long dash (set difference)', r'$\mathfrak m-\mathfrak m^2$',
      'convention', 7, 'high',
      r'$\mathfrak m-\mathfrak m^2$', r'$\mathfrak m\setmin\mathfrak m^2$',
      'Set difference.'),
    F(216, 'proof of (23.1.5): l\'idéal xA est fermé dans A (0_I, 7.3.5)',
      '(0_I, 7.3.5) with bold 0', r'(0\textsubscript{I}, 7.3.5)',
      'convention', 2, 'high',
      r'(0\textsubscript{I}, 7.3.5), donc', r'(\textbf{0}\textsubscript{I}, 7.3.5), donc', B2),
    F(216, 'Proposition (23.1.7), first sentence: le complété Â est réduit',
      'réduit printed roman inside the italic statement', 'réduit (italic, body of the italic environment)',
      'convention', 6, 'high',
      r"$\widehat A$ est réduit, et l'on", r"$\widehat A$ est \textup{réduit}, et l'on",
      'Checked on an enlarged crop: "est" italic, "réduit" upright.'),
    F(216, 'Proposition (23.1.7), label (i)',
      '(i) upright', r'\item[(i)] (italic in the italic environment)',
      'convention', 6, 'high',
      r"\item[(i)] Si l'anneau", r"\item[\textup{(i)}] Si l'anneau",
      'As for the other item labels of italic statements (GLOBAL_ISSUES 16).'),
    F(216, 'Proposition (23.1.7) (i): parenthesis (ce qui aura lieu ... cor. 1 du th. 1))',
      'the whole parenthesis is roman, with séparable and Alg. italic',
      r'parenthesis italic (environment), séparable italic, \emph{Alg.} upright',
      'convention', 6, 'high',
      "réduit (ce qui aura lieu en\n  particulier lorsque $K'$ est une extension séparable de $K$, $R$ étant\n"
      "  composé direct de corps, extensions de $K$ (Bourbaki, \\emph{Alg.},\n"
      "  chap.~VIII, §~7, n\\textsuperscript{o}~3, cor.~1 du th.~1)), alors",
      "réduit \\textup{(ce qui aura lieu en\n  particulier lorsque $K'$ est une extension \\emph{séparable} de $K$, $R$ étant\n"
      "  composé direct de corps, extensions de $K$ (Bourbaki, \\emph{Alg.},\n"
      "  chap.~VIII, §~7, n\\textsuperscript{o}~3, cor.~1 du th.~1))}, alors",
      'One edit: inside \\textup, \\emph gives the printed italic séparable and Alg.; "alors A\' est un A-module de type fini" stays italic.'),
    F(216, 'Proposition (23.1.7), label (ii)',
      '(ii) upright', r'\item[(ii)] (italic in the italic environment)',
      'convention', 6, 'high',
      r'\item[(ii)] Si en particulier', r'\item[\textup{(ii)}] Si en particulier', ''),
    F(216, 'proof of (23.1.7), start: (i) Posons pour simplifier',
      '(i) upright (proof-part label, roman text)', r'\emph{(i)} (italic)',
      'italics', None, 'high',
      r'\emph{(i)} Posons', '(i) Posons',
      'Checked on an enlarged crop; proof-part labels are printed upright (GLOBAL_ISSUES 51).'),
    F(216, 'proof of (23.1.7): Comme A_1 est un A-module plat (0_I, 7.3.5)',
      '(0_I, 7.3.5) with bold 0', r'(0\textsubscript{I}, 7.3.5)',
      'convention', 2, 'high',
      r"plat (0\textsubscript{I}, 7.3.5), $A'_1$", r"plat (\textbf{0}\textsubscript{I}, 7.3.5), $A'_1$", B2),
    F(216, 'proof of (23.1.7): et est évidemment entier sur A_1',
      'entier italic', 'entier roman',
      'italics', None, 'high',
      'évidemment entier', r'évidemment \emph{entier}', 'Checked on an enlarged crop.'),
    F(216, 'proof of (23.1.7): tout élément ≠0 de A est A_1-régulier (0_I, 6.3.4)',
      '(0_I, 6.3.4) with bold 0', r'(0\textsubscript{I}, 6.3.4)',
      'convention', 2, 'high',
      r'(0\textsubscript{I}, 6.3.4)', r'(\textbf{0}\textsubscript{I}, 6.3.4)', B2),
    F(216, 'proof of (23.1.7): où S = A—{0}',
      'A—{0} with the long dash (set difference)', r'$S=A-\{0\}$',
      'convention', 7, 'high',
      r'$S=A-\{0\}$', r'$S=A\setmin\{0\}$', 'Set difference.'),
    F(216, 'proof of (23.1.7): K_1 s\'identifie à un sous-anneau de l\'anneau total des fractions',
      'sous-anneau italic', 'sous-anneau roman',
      'italics', None, 'high',
      "sous-anneau de l'anneau total", r"\emph{sous-anneau} de l'anneau total", 'Checked on an enlarged crop.'),
    F(216, "proof of (23.1.7): K'_1 s'identifie à un sous-anneau de K'⊗_K R",
      'sous-anneau italic', 'sous-anneau roman',
      'italics', None, 'high',
      r"sous-anneau de $K'\otimes_KR$", r"\emph{sous-anneau} de $K'\otimes_KR$",
      'The earlier "sous-anneau de K\'_1" (same proof) is roman in the print, as in the TeX.'),
    F(216, 'proof of (23.1.7): qui par hypothèse est réduit',
      'réduit italic', 'réduit roman',
      'italics', None, 'high',
      'est réduit et est une', r'est \emph{réduit} et est une', 'Checked on an enlarged crop.'),
    F(216, 'proof of (23.1.7): est une R-algèbre finie',
      'finie italic', 'finie roman',
      'italics', None, 'high',
      r'$R$-algèbre finie.', r'$R$-algèbre \emph{finie}.', 'Checked on an enlarged crop.'),
    F(216, 'proof of (23.1.7): corps, extensions finies des L_i',
      'finies italic', 'finies roman',
      'italics', None, 'high',
      'extensions finies des $L_i$', r'extensions \emph{finies} des $L_i$', 'Checked on an enlarged crop.'),
    F(216, 'proof of (23.1.7), end: A-module fidèlement plat (0_I, 7.3.5)',
      '(0_I, 7.3.5) with bold 0', r'(0\textsubscript{I}, 7.3.5)',
      'convention', 2, 'high',
      r'fidèlement plat (0\textsubscript{I}, 7.3.5)', r'fidèlement plat (\textbf{0}\textsubscript{I}, 7.3.5)', B2),
]

# ---------------- page 217 ----------------
L += [
    F(217, 'proof of (23.1.7) (ii), start',
      '(ii) upright (proof-part label)', r'\emph{(ii)} (italic)',
      'italics', None, 'high',
      r"\emph{(ii)} L'hypothèse", "(ii) L'hypothèse",
      'Checked on an enlarged crop (GLOBAL_ISSUES 51).'),
    F(217, 'proof of (23.1.7) (ii): appliquer (i) à toute extension finie',
      'toute italic', 'toute roman',
      'italics', None, 'high',
      'à toute\nextension finie', 'à \\emph{toute}\nextension finie', 'Checked on an enlarged crop.'),
    F(217, 'proof of (23.1.7) (ii): appliquer (i)',
      'the letter i of "(i)" is bold (wrong fount); the parentheses are light',
      '(i) in light roman',
      'misprint_in_print', None, 'high',
      'appliquer (i)', r'appliquer (\textbf{i})',
      'Wrong-fount bold i, clearly heavier than the i of "appliquer" on a 3x crop; the TeX silently corrects it. '
      'Recorded as a misprint (GLOBAL_ISSUES 29: wrong-fount letters are reproduced in the diplomatic text).',
      corrected='appliquer (i)'),
    F(217, 'title of 23.2',
      '23.2. Clôture intégrale d\'un anneau local noethérien intègre.  (final full stop)',
      'title without the full stop',
      'punctuation', None, 'high',
      "\\subsection{Clôture intégrale d'un anneau local noethérien intègre}",
      "\\subsection{Clôture intégrale d'un anneau local noethérien intègre.}",
      'GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop).'),
    F(217, '(23.2.1): ce qui généralise la définition donnée dans (III, 4.3.6)',
      '(III, 4.3.6) with bold III', '(III, 4.3.6)',
      'convention', 2, 'high',
      '(III, 4.3.6)', r'(\textbf{III}, 4.3.6)', 'Bold chapter numeral III.'),
    F(217, 'proof of (23.2.2): Dire que f est injectif signifie donc',
      'injectif italic', 'injectif roman',
      'italics', None, 'high',
      'est injectif signifie', r'est \emph{injectif} signifie', 'Checked on the strip.'),
    F(217, 'proof of (23.2.2): f est radiciel en vertu de (I, 3.5.8)',
      '(I, 3.5.8) with bold I', '(I, 3.5.8)',
      'convention', 2, 'high',
      '(I, 3.5.8)', r'(\textbf{I}, 3.5.8)', 'Bold chapter numeral I.'),
    F(217, 'proof of (23.2.2): f est surjectif et fermé (II, 6.1.10)',
      '(II, 6.1.10) with bold II', '(II, 6.1.10)',
      'convention', 2, 'high',
      '(II, 6.1.10)', r'(\textbf{II}, 6.1.10)', 'Bold chapter numeral II.'),
    F(217, 'Lemme (23.2.3): number of the displayed formula',
      '(23.1.8.1) (in bold) as the number of the formula inside Lemme (23.2.3)',
      r'\tag{23.1.8.1} (keeps the printed number)',
      'misprint_in_print', None, 'medium',
      None, None,
      'The print has no (23.1.8) (section 23.1 ends with (23.1.7), p. 216); the formula of Lemme (23.2.3) should be (23.2.3.1). '
      'The TeX keeps the printed number. No reference to (23.1.8.1) or (23.2.3.1) elsewhere in EGA IV (grep of the four IV packages). '
      'Not in the EGA IV errata (only (0_IV, 23.1.3) is listed for section 23).',
      corrected=r'\tag{23.2.3.1}', nofix=True),
    F(217, 'end of the page: si N est | le nilradical de B (p. 218)',
      'no paragraph break: the sentence continues on p. 218, flush left',
      'blank line before the p. 218 marker (and one after it): paragraph break',
      'other', None, 'high',
      'si $\\mathfrak N$ est\n\n', 'si $\\mathfrak N$ est\n',
      'GLOBAL_ISSUES 20. Apply together with the p. 218 entry that removes the blank line after the marker.'),
]

# ---------------- page 218 ----------------
L += [
    F(218, 'top of the page: si N est | le nilradical de B',
      'no paragraph break: the page starts mid-sentence, flush left',
      'blank line after the marker: paragraph break',
      'other', None, 'high',
      '\\oldpage[0\\textsubscript{IV-1}]{218}\n\nle nilradical', '\\oldpage[0\\textsubscript{IV-1}]{218}\nle nilradical',
      'GLOBAL_ISSUES 20. Apply together with the p. 217 entry that removes the blank line before the marker.'),
    F(218, 'Proposition (23.2.4), label (i)',
      '(i) upright', r'\item[(i)] (italic in the italic environment)',
      'convention', 6, 'high',
      r'\item[(i)] Il existe', r'\item[\textup{(i)}] Il existe', ''),
    F(218, 'Proposition (23.2.4), label (ii)',
      '(ii) upright', r'\item[(ii)] (italic in the italic environment)',
      'convention', 6, 'high',
      r'\item[(ii)] Si en outre', r'\item[\textup{(ii)}] Si en outre', ''),
    F(218, 'proof of (23.2.4), start: (i) Soit B_1 = B_red',
      '(i) upright (proof-part label)', r'\emph{(i)} (italic)',
      'italics', None, 'high',
      r'\emph{(i)} Soit $B_1', '(i) Soit $B_1', 'Checked on an enlarged crop.'),
    F(218, 'proof of (23.2.4) (i): A est B-régulier (0_I, 6.3.4)',
      '(0_I, 6.3.4) with bold 0', r'(0\textsubscript{I}, 6.3.4)',
      'convention', 2, 'high',
      r'(0\textsubscript{I}, 6.3.4)', r'(\textbf{0}\textsubscript{I}, 6.3.4)', B2),
    F(218, 'proof of (23.2.4) (i): qui sont des B-algèbres finies, donc contenues dans B\'',
      'finies italic', 'finies roman',
      'italics', None, 'high',
      '$B$-algèbres finies, donc', r'$B$-algèbres \emph{finies}, donc', 'Checked on the strip.'),
    F(218, 'proof of (23.2.4), part (ii), start',
      '(ii) upright (proof-part label)', r'\emph{(ii)} (italic)',
      'italics', None, 'high',
      r'\emph{(ii)} Comme', '(ii) Comme', 'Checked on an enlarged crop.'),
    F(218, 'proof of (23.2.4) (ii): il suffit (IV, 2.6.1, (v))',
      '(IV, 2.6.1, (v)) with bold IV', '(IV, 2.6.1, (v))',
      'convention', 2, 'high',
      '(IV, 2.6.1, (v))', r'(\textbf{IV}, 2.6.1, (v))', 'Bold chapter numeral IV.'),
    F(218, 'proof of (23.2.4) (ii): ce qui revient au même (I, 5.1.6)',
      '(I, 5.1.6) with bold I', '(I, 5.1.6)',
      'convention', 2, 'high',
      '(I, 5.1.6)', r'(\textbf{I}, 5.1.6)', 'Bold chapter numeral I.'),
    F(218, 'proof of (23.2.4) (ii): ou, ce qui revient au même (I, 5.1.6) que le morphisme',
      '"au même (I, 5.1.6) que le morphisme": no comma after the reference',
      '"(I, 5.1.6), que": comma added',
      'punctuation', None, 'high',
      '5.1.6), que', '5.1.6) que',
      'Checked on an enlarged crop. Not treated as a misprint: EGA IV has the same construction without the comma elsewhere '
      '("ou, ce qui revient au même (17.9.1) que", ega4-18-fr.tex).'),
    F(218, 'proof of (23.2.4) (ii): donc (IV, 5.13.2)',
      '(IV, 5.13.2) with bold IV', '(IV, 5.13.2)',
      'convention', 2, 'high',
      '(IV, 5.13.2)', r'(\textbf{IV}, 5.13.2)', 'Bold chapter numeral IV.'),
    F(218, 'Corollaire (23.2.5): parenthesis (donc des anneaux noethériens semi-locaux (Bourbaki, ...))',
      'the parenthesis is roman, with Alg. comm. italic',
      r'parenthesis italic (environment), \emph{Alg. comm.} upright',
      'convention', 6, 'high',
      "(donc\ndes anneaux noethériens semi-locaux (Bourbaki, \\emph{Alg. comm.}, chap.~IV,\n"
      "§~2, n\\textsuperscript{o}~5, cor.~3 de la prop.~9))",
      "\\textup{(donc\ndes anneaux noethériens semi-locaux (Bourbaki, \\emph{Alg. comm.}, chap.~IV,\n"
      "§~2, n\\textsuperscript{o}~5, cor.~3 de la prop.~9))}",
      'Checked on an enlarged crop.'),
    F(218, 'Corollaire (23.2.5), end: est radiciel (cf. (23.2.2))',
      '(cf. (23.2.2)) upright', 'italic (environment)',
      'convention', 6, 'high',
      '(cf. (23.2.2))', r'\textup{(cf. (23.2.2))}', 'Checked on an enlarged crop.'),
]

# ---------------- page 219 ----------------
L += [
    F(219, 'proof of (23.2.5): B est un A-module fidèlement plat (0_I, 7.3.5)',
      '(0_I, 7.3.5) with bold 0', r'(0\textsubscript{I}, 7.3.5)',
      'convention', 2, 'high',
      r'(0\textsubscript{I}, 7.3.5)', r'(\textbf{0}\textsubscript{I}, 7.3.5)', B2),
    F(219, 'Corollaire (23.2.6): Sous les hypothèses de (23.2.5)',
      '(23.2.5) upright', 'italic (environment)',
      'convention', 6, 'high',
      'hypothèses de (23.2.5),', r'hypothèses de \textup{(23.2.5)},', 'Checked on an enlarged crop.'),
    F(219, 'proof of (23.2.6): le nombre des idéaux maximaux de C_λ est constant',
      'constant italic', 'constant roman',
      'italics', None, 'high',
      'est constant pour', r'est \emph{constant} pour', 'Checked on an enlarged crop.'),
    F(219, 'proof of (23.2.6): les corps C_λ/m_λ et C_α/m_α sont canoniquement isomorphes',
      'C_λ/m_λ et C_α/m_α (λ first)', 'C_α/m_α et C_λ/m_λ (order reversed)',
      'formula', None, 'high',
      "les corps $C_\\alpha/\\mathfrak m_\\alpha$ et\n$C_\\lambda/\\mathfrak m_\\lambda$ sont",
      "les corps $C_\\lambda/\\mathfrak m_\\lambda$ et\n$C_\\alpha/\\mathfrak m_\\alpha$ sont",
      'Checked on an enlarged crop.'),
    F(219, 'proof of (23.2.6), end: (0_III, 10.3.1.3)',
      '(0_III, ...) with bold 0', r'(0\textsubscript{III}, ...)',
      'convention', 2, 'high',
      r'(0\textsubscript{III},', r'(\textbf{0}\textsubscript{III},', B2),
    F(219, 'proof of (23.2.6), end: (0_III, 10.3.1.3)',
      '10.3.1.3', '10.3.1.1.3',
      'number', None, 'high',
      '10.3.1.1.3', '10.3.1.3',
      'Checked on an enlarged crop. (0_III, 10.3.1.3) is the lemma on inductive limits of local rings (ega3-1-fr.tex, label 0.10.3.1.3-fr); 10.3.1.1.3 does not exist.'),
    F(219, 'Proposition (23.2.7): anneau de Krull (Bourbaki, Alg. comm., chap. VII, § 1) semi-local',
      'the parenthesis is roman, with Alg. comm. italic',
      r'parenthesis italic (environment), \emph{Alg. comm.} upright',
      'convention', 6, 'high',
      r'(Bourbaki, \emph{Alg. comm.}, chap.~VII, §~1)', r'\textup{(Bourbaki, \emph{Alg. comm.}, chap.~VII, §~1)}',
      'Checked on the strip.'),
    F(219, 'proof of (23.2.7.1): par platitude (0_I, 6.3.4)',
      '(0_I, 6.3.4) with bold 0', r'(0\textsubscript{I}, 6.3.4)',
      'convention', 2, 'high',
      r'(0\textsubscript{I}, 6.3.4)', r'(\textbf{0}\textsubscript{I}, 6.3.4)', B2),
    F(219, "end of the page: dont l'anneau total des | fractions R (p. 220)",
      'no paragraph break: the sentence continues on p. 220, flush left',
      'blank line before the p. 220 marker (and one after it): paragraph break',
      'other', None, 'high',
      "dont l'anneau total des\n\n", "dont l'anneau total des\n",
      'GLOBAL_ISSUES 20. Apply together with the p. 220 entry that removes the blank line after the marker.'),
]

# ---------------- page 220 ----------------
L += [
    F(220, "top of the page: dont l'anneau total des | fractions R",
      'no paragraph break: the page starts mid-sentence, flush left',
      'blank line after the marker: paragraph break',
      'other', None, 'high',
      '\\oldpage[0\\textsubscript{IV-1}]{220}\n\nfractions $R$', '\\oldpage[0\\textsubscript{IV-1}]{220}\nfractions $R$',
      'GLOBAL_ISSUES 20. Apply together with the p. 219 entry that removes the blank line before the marker.'),
    F(220, 'proof of (23.2.7): un anneau local noethérien intègre et complet',
      'intègre and complet italic, "et" roman', r'\emph{intègre et complet} ("et" italic too)',
      'italics', None, 'high',
      r'\emph{intègre et complet}', r'\emph{intègre} et \emph{complet}', 'Checked on an enlarged crop.'),
    F(220, 'proof of (23.2.7): ... un anneau de Krull. Pour prouver la dernière assertion',
      '"Pour prouver" continues the paragraph (flush left, no indent)',
      'blank line: new paragraph',
      'other', None, 'high',
      'anneau de Krull.\n\nPour prouver', 'anneau de Krull.\nPour prouver',
      'Line start compared with the indented paragraphs below (Remarques, (ii)).'),
    F(220, "proof of (23.2.7): l'application p' ⇝ p'∩C",
      "wavy arrow p'⇝p'∩C", r'\mapsto',
      'symbol', None, 'high',
      r"\mathfrak p'\mapsto\mathfrak p'\cap C", r"\mathfrak p'\leadsto\mathfrak p'\cap C",
      'Checked on a 3x crop (GLOBAL_ISSUES 33).'),
    F(220, "proof of (23.2.7): est une bijection de l'ensemble",
      'bijection italic', 'bijection roman',
      'italics', None, 'high',
      'est une bijection de', r'est une \emph{bijection} de', 'Checked on an enlarged crop.'),
    F(220, "Remarques (23.2.8) (ii): dans une extension finie K' de K",
      'finie italic', 'finie roman (judged as if the remark body were roman)',
      'italics', None, 'high',
      "extension finie $K'$", r"extension \emph{finie} $K'$", 'Checked on an enlarged crop.'),
    F(220, 'Remarques (23.2.8) (ii): donc des anneaux de Krull par (23.1.13)',
      '(23.1.13)', '(23.1.13) (keeps the printed reading)',
      'misprint_in_print', None, 'medium',
      None, None,
      'No (23.1.13) exists (section 23.1 ends with (23.1.7)); the integral closures of the local noetherian domains B_{m_i} are Krull rings by '
      "Mori's theorem (23.2.7). Same old-numbering trace as the tag (23.1.8.1) on p. 217. Not in the EGA IV errata.",
      corrected='(23.2.7)', nofix=True),
    F(220, "proof of (23.2.9): on a A' = ∩_m A'_m",
      'index m under the intersection sign', r'\bigcap without index',
      'formula', None, 'high',
      r"$A'=\bigcap A'_{\mathfrak m}$", r"$A'=\bigcap_{\mathfrak m}A'_{\mathfrak m}$",
      'Checked on an enlarged crop.'),
]


def rd(n):
    with open(RUN + f'page_{n}.tex', encoding='utf-8', newline='') as fh:
        return fh.read().replace('\r\n', '\n')


ok = True
texts = {n: rd(n) for n in range(216, 221)}
applied = dict(texts)
for i, d in enumerate(L):
    fx = d['fix']
    if fx is None:
        continue
    c = texts[d['page']].count(fx['old'])
    c2 = applied[d['page']].count(fx['old'])
    if c != 1 or c2 != 1:
        ok = False
        print('NOT UNIQUE', i, d['page'], c, c2, repr(fx['old'])[:80])
    else:
        applied[d['page']] = applied[d['page']].replace(fx['old'], fx['new'], 1)
print('all unique:', ok)

with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(L, fh, ensure_ascii=False, indent=1)

from collections import Counter
cnt = Counter()
for d in L:
    k = 'misprint' if d['kind'] == 'misprint_in_print' else ('convention' if d['kind'] == 'convention' else 'normal')
    cnt[(d['page'], k)] += 1
for n in range(216, 221):
    print(n, cnt[(n, 'normal')], cnt[(n, 'convention')], cnt[(n, 'misprint')])
print('total', len(L))
