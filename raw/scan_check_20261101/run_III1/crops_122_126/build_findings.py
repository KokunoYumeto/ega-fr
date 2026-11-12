"""Build findings_122_126.json; '@@' in TeX strings stands for a line break (LF)."""
import json

D = 'user/Documents/ega_scan_check_20261101/run_III1/'
OUT = D + 'findings_122_126.json'

HAT = r'^{\widehat{\,}}'

def nl(s):
    return None if s is None else s.replace('@@', '\n')

F = []

def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, misprint=False):
    d = {'page': page, 'where': where, 'scan': scan, 'tex': nl(tex), 'kind': kind,
         'convention': conv, 'confidence': conf,
         'fix': None if old is None else {'old': nl(old), 'new': nl(new)}}
    if misprint:
        d['corrected'] = nl(corrected)
    d['note'] = note
    F.append(d)

def conv2(page, where, old, new, numeral):
    add(page, where, '(%s, ...) with a bold %s' % (numeral, numeral), old, 'convention', 2, 'high',
        old, new, 'Bold %s in the reference to chapter %s.' % (numeral, numeral))

PB = ('Missing paragraph break: the print starts a new, indented paragraph after the display '
      '(left edge measured on the strip); the TeX runs on without a blank line.')

# ---------------- page 121 (outside this run's pages) ----------------
add(121, "end of p. 121 / top of p. 122, (3.4.5): display '... = Γ(𝔜_g, lim R^nf_*(ℱ_k))' | 'et comme le faisceau R^nf_*(ℱ) ...'",
    'p. 122 begins flush left with \u00abet comme\u00bb: the sentence continues after the display',
    r'blank line before \oldpage[III]{122}', 'other', None, 'high',
    r'\varprojlim_kR^nf_*(\mathcal F_k))@@\]@@@@', r'\varprojlim_kR^nf_*(\mathcal F_k))@@\]@@',
    "Spurious paragraph break at a page break inside the sentence (GLOBAL_ISSUES item 20). OUTSIDE pp. 122-126: "
    "the 'old' lies in page 121's segment (end of page_121.tex, checked unique there); findings_117_121.json has no entry for it. "
    "There is no blank line after the marker, so this one edit suffices.")

# ---------------- page 122 ----------------
add(122, "(3.4.5), 1st line: 'associé au préfaisceau 𝔜_g⇝H^n(f^{-1}(𝔜_g), ℱ)'", '𝔜_g ⇝ H^n(...) (wavy arrow)',
    r'$\mathfrak Y_g\mapsto H^n(f^{-1}(\mathfrak Y_g),\mathcal F)$', 'symbol', None, 'high',
    r'$\mathfrak Y_g\mapsto H^n', r'$\mathfrak Y_g\leadsto H^n',
    'Wavy maps-to arrow in the print (\\leadsto), not convention 3; GLOBAL_ISSUES item 33. Enlarged crop.')
conv2(122, "(3.4.5): 'sur les 𝔜_g (0_I, 3.2.1)'", r'(0\textsubscript{I}, 3.2.1)', r'(\textbf{0}\textsubscript{I}, 3.2.1)', '0')
add(122, "(3.4.5): 'l'homomorphisme (3.4.2.2) est bijectif. Prouvons'", "'bijectif' in italics", 'est bijectif. Prouvons',
    'italics', None, 'high', 'est bijectif. Prouvons', r'est \emph{bijectif}. Prouvons', 'Enlarged crop.')
add(122, "after (3.4.5.1): 'Avec les notations précédentes, on a, puisque'", 'new indented paragraph',
    r'\]@@Avec les notations (no blank line)', 'other', None, 'high',
    r'\]@@Avec les notations', r'\]@@@@Avec les notations', PB)
add(122, "after the display Γ(𝔜_g, R^nf_*(ℱ_k)) = ... = (H^n(𝔛, ℱ_k))_g: 'Or, les H^n(𝔛, ℱ_k) forment'", 'new indented paragraph',
    r'\]@@Or, les $H^n (no blank line)', 'other', None, 'high',
    r'\]@@Or, les $H^n', r'\]@@@@Or, les $H^n', PB)
conv2(122, "(3.4.5): 'On en conclut (0, 13.7.8) que l'on a'", '(0, 13.7.8)', r'(\textbf{0}, 13.7.8)', '0')
add(122, "(3.4.5), display: 'lim_k((H^n(𝔛, ℱ_k))_g) = H^n(𝔛, ℱ)⊗_A A_{g} = ...'",
    'lim((H^n(𝔛, ℱ_k))_g): the argument of lim is enclosed in a further pair of parentheses',
    r'\varprojlim_k(H^n(\mathfrak X,\mathcal F_k))_g', 'formula', None, 'high',
    r'\varprojlim_k(H^n(\mathfrak X,\mathcal F_k))_g', r'\varprojlim_k((H^n(\mathfrak X,\mathcal F_k))_g)',
    'Enlarged crop: two opening parentheses after lim and a closing one after the subscript g.')
conv2(122, "(3.4.5): 'compte tenu de (I, 10.10.8) appliqué à A et A_{g}'", '(I, 10.10.8)', r'(\textbf{I}, 10.10.8)', 'I')
add(122, "(3.4.5): 'ceci démontre (3.4.5.1) puisque Γ(𝔜_g, R^nf_*(ℱ)) = lim Γ(𝔜_g, R^nf_*(ℱ_k)).'",
    'the formula is set inline in the running text (flush left, not centred)', r'displayed with \[ ... \]', 'other', None, 'high',
    r'puisque@@\[@@\Gamma(\mathfrak Y_g,R^nf_*(\mathcal F))@@=\varprojlim_k\Gamma(\mathfrak Y_g,R^nf_*(\mathcal F_k)).@@\]@@Comme',
    r'puisque@@$\Gamma(\mathfrak Y_g,R^nf_*(\mathcal F))@@=\varprojlim_k\Gamma(\mathfrak Y_g,R^nf_*(\mathcal F_k))$.@@@@Comme',
    "Layout: the print sets this formula inline (GLOBAL_ISSUES items 21/36). The same edit also inserts the paragraph break "
    "before 'Comme (3.4.2.2)' (next finding).")
add(122, "'Comme (3.4.2.2) est alors un isomorphisme de 𝒪_𝔜-Modules cohérents'", 'new indented paragraph',
    r'\]@@Comme (no blank line)', 'other', None, 'high', None, None,
    'Missing paragraph break; covered by the edit of the preceding finding.')
conv2(122, "'c'est nécessairement un isomorphisme topologique (I, 10.11.6)'", '(I, 10.11.6)', r'(\textbf{I}, 10.11.6)', 'I')
add(122, "(3.4.5): 'il résulte des relations R^nf_*(ℱ_k) = (H^n(X, ℱ_k))^Δ que le système projectif'",
    'H^n(X, ℱ_k) with a roman X, not Fraktur 𝔛', r'$R^nf_*(\mathcal F_k)=(H^n(\mathfrak X,\mathcal F_k))^\Delta$',
    'misprint_in_print', None, 'high',
    r'=(H^n(\mathfrak X,\mathcal F_k))^\Delta$ que', r'=(H^n(X,\mathcal F_k))^\Delta$ que',
    'Enlarged crop: an upright roman X. No X is defined in (3.4.5) (only 𝔛 and X_k); every other H^n(𝔛, ℱ_k) of the proof has 𝔛. '
    'The TeX silently corrects it; the fix restores the printed reading. No authors\' errata entry for this page.',
    corrected=r'(H^n(\mathfrak X,\mathcal F_k))^\Delta', misprint=True)
conv2(122, "'(R^nf_*(ℱ_k))_{k≥0} vérifie (ML) (I, 10.10.2)'", '(I, 10.10.2)', r'(\textbf{I}, 10.10.2)', 'I')
add(122, "Corollaire (3.4.6): 'Sous les hypothèses de (3.4.4), l'homomorphisme canonique'",
    '(3.4.4) upright inside the italic statement', r'(\hyperref[III.3.4.4-fr]{3.4.4}) inside the italic corollary environment: italic',
    'convention', 6, 'high',
    r'Sous les hypothèses de (\hyperref[III.3.4.4-fr]{3.4.4})',
    r'Sous les hypothèses de \textup{(\hyperref[III.3.4.4-fr]{3.4.4})}', 'Enlarged crop.')
add(122, "(4.1.1): 'f : X→Y un morphisme propre, Y' une partie fermée'", "'propre' in italics", "morphisme propre, $Y'$",
    'italics', None, 'high', "morphisme propre, $Y'$", r"morphisme \emph{propre}, $Y'$", 'Enlarged crop.')
add(122, "(4.1.1): 'les préschémas formels X_{/X'} et Y_{/Y'} complétés de X et Y'", "no comma after Y_{/Y'}", "$Y_{/Y'}$, complétés",
    'punctuation', None, 'high', "$Y_{/Y'}$,", "$Y_{/Y'}$", 'Enlarged crop. Independent of the italics finding for complétés.')
add(122, "(4.1.1): 'Y_{/Y'} complétés de X et Y le long de X' et Y''", "'complétés' in italics", 'complétés de $X$',
    'italics', None, 'high', 'complétés de $X$', r'\emph{complétés} de $X$', 'Enlarged crop.')
conv2(122, "(4.1.1): 'respectivement (I, 10.8.5)'", '(I, 10.8.5)', r'(\textbf{I}, 10.8.5)', 'I')
add(122, "(4.1.1): 'par f^ le prolongement de f à ces complétés'", "'prolongement' in italics", 'le prolongement',
    'italics', None, 'high', 'le prolongement', r'le \emph{prolongement}', '')
conv2(122, "(4.1.1): 'à ces complétés (I, 10.9.1) qui est un morphisme'", '(I, 10.9.1)', r'(\textbf{I}, 10.9.1)', 'I')
add(122, "(4.1.1): 'Pour tout 𝒪_X-Module cohérent ℱ, nous'", "'cohérent' in italics", r'$\mathcal O_X$-Module cohérent $\mathcal F$',
    'italics', None, 'high', r'$\mathcal O_X$-Module cohérent $\mathcal F$', r'$\mathcal O_X$-Module \emph{cohérent} $\mathcal F$', '')
add(122, "end of p. 122 / top of p. 123, (4.1.1): '... ℱ, nous | désignerons par ℱ^ ...'",
    'one sentence across the page break; p. 123 begins flush left', r'blank line before \oldpage[III]{123}', 'other', None, 'high',
    ', nous@@@@', ', nous@@',
    'Spurious paragraph break at a page break inside the sentence (GLOBAL_ISSUES item 20). Apply together with the p. 123 entry '
    'that removes the blank line after the marker.')

# ---------------- page 123 ----------------
add(123, "top of p. 123: '\\oldpage[III]{123}' followed by a blank line", 'p. 123 begins flush left (sentence continues)',
    r'\oldpage[III]{123}@@@@désignerons', 'other', None, 'high',
    r'\oldpage[III]{123}@@@@désignerons', r'\oldpage[III]{123}@@désignerons',
    'Second half of the p. 122 entry (blank line before the marker); apply both.')
add(123, "(4.1.1): 'désignerons par ℱ^ son complété ℱ_{/X'} le long de X''", "'complété' in italics", 'son complété',
    'italics', None, 'high', 'son complété', r'son \emph{complété}', '')
conv2(123, "(4.1.1): 'le long de X' (I, 10.8.4)'", '(I, 10.8.4)', r'(\textbf{I}, 10.8.4)', 'I')
conv2(123, "(4.1.1): 'cohérent (I, 10.8.8).'", 'cohérent (I, 10.8.8).', r'cohérent (\textbf{I}, 10.8.8).', 'I')
conv2(123, "(4.1.2): 'Supp(𝒪_Y/𝒥) = Y' (I, 5.2.1)'", '(I, 5.2.1)', r'(\textbf{I}, 5.2.1)', 'I')
conv2(123, "(4.1.2): 'on sait (I, 4.4.5) que'", '(I, 4.4.5)', r'(\textbf{I}, 4.4.5)', 'I')
add(123, "(4.1.2): 'on sait (I, 4.4.5) que 𝒦 = f^*(𝒥)𝒪_X est un Idéal cohérent de 𝒪_X tel que'",
    'the formula is set inline in the running text', r'displayed with \[ ... \]', 'other', None, 'high',
    r'que@@\[@@\mathcal K=f^*(\mathcal J)\mathcal O_X@@\]@@est un Idéal',
    r'que@@$\mathcal K=f^*(\mathcal J)\mathcal O_X$@@est un Idéal',
    'Layout: the print sets this formula inline (GLOBAL_ISSUES items 21/36); Supp(𝒪_X/𝒦) = X\' below is displayed in the print too.')
add(123, "(4.1.2), after the display ℱ_k = ℱ⊗(𝒪_Y/𝒥^{k+1}) = ℱ/𝒦^{k+1}ℱ: 'Les 𝒪_Y-Modules R^nf_*(ℱ) et'", 'new indented paragraph',
    r'\]@@Les $\mathcal O_Y$-Modules (no blank line)', 'other', None, 'high',
    r'\]@@Les $\mathcal O_Y$-Modules', r'\]@@@@Les $\mathcal O_Y$-Modules', PB)
add(123, "(4.1.2): 'sont cohérents pour tout n (3.2.1)'", "'cohérents' in italics", 'sont cohérents pour tout',
    'italics', None, 'high', 'sont cohérents pour tout', r'sont \emph{cohérents} pour tout', '')
add(123, "(4.1.2), after (4.1.2.1): 'En outre, comme ℱ_k est un 𝒪_X/𝒦^{k+1}-Module'", 'new indented paragraph',
    r'\]@@En outre, comme (no blank line)', 'other', None, 'high',
    r'\]@@En outre, comme', r'\]@@@@En outre, comme', PB)
conv2(123, "(4.1.2): 'est un 𝒪_Y/𝒥^{k+1}-Module (0, 12.2.1)'", '(0, 12.2.1)', r'(\textbf{0}, 12.2.1)', '0')
add(123, "(4.1.2), after (4.1.2.2): 'Les deux membres de (4.1.2.2) forment deux systèmes projectifs'", 'new indented paragraph',
    r'\]@@Les deux membres (no blank line)', 'other', None, 'high',
    r'\]@@Les deux membres', r'\]@@@@Les deux membres', PB)
add(123, "(4.1.2): 'n'est autre que le complété (R^nf_*(ℱ))_{/Y'}'", "'complété' in italics", 'que le complété',
    'italics', None, 'high', 'que le complété', r'que le \emph{complété}', '')
add(123, "(4.1.2): 'que nous noterons (R^nf_*(ℱ))^. En outre'",
    '(R^nf_*(ℱ))^: parentheses, then a raised circumflex after the closing parenthesis', r'$\widehat{R^nf_*(\mathcal F)}$ (wide hat over the expression)',
    'formula', None, 'high',
    r'$\widehat{R^nf_*(\mathcal F)}$. En outre', r'$(R^nf_*(\mathcal F))' + HAT + r'$. En outre',
    'Enlarged crop. Hat after the parenthesis, the analogue of convention 5 for the tilde; same form as the EGA II p. 194 fixes '
    '(^{\\widehat{\\,}}, GLOBAL_ISSUES item 31, \\superhat).')
add(123, "(4.1.2): 'd'où par passage à la limite un homomorphisme canonique'", "'homomorphisme canonique' in italics",
    'limite un homomorphisme canonique', 'italics', None, 'high',
    'limite un homomorphisme canonique', r'limite un \emph{homomorphisme canonique}', '')
add(123, "(4.1.2.3): 'φ_n : (R^nf_*(ℱ))^ → lim R^nf_*(ℱ_k).'", '(R^nf_*(ℱ))^ with the hat after the parenthesis',
    r'\varphi_n:\widehat{R^nf_*(\mathcal F)}', 'formula', None, 'high',
    r'\varphi_n:\widehat{R^nf_*(\mathcal F)}', r'\varphi_n:(R^nf_*(\mathcal F))' + HAT,
    'Enlarged crop; as for (R^nf_*(ℱ))^ two lines above.')
add(123, "(4.1.2), after (4.1.2.3): 'D'ailleurs (4.1.2.2) est un homomorphisme'", 'new indented paragraph',
    r"\]@@D'ailleurs (no blank line)", 'other', None, 'high',
    r"\]@@D'ailleurs", r"\]@@@@D'ailleurs", PB)
conv2(123, "(4.1.2): 'et par suite (I, 10.8.3) peut être considéré'", '(I, 10.8.3)', r'(\textbf{I}, 10.8.3)', 'I')
conv2(123, "(4.1.2): 'pseudo-discrets (0_I, 3.8.1)'", r'(0\textsubscript{I}, 3.8.1)', r'(\textbf{0}\textsubscript{I}, 3.8.1)', '0')
add(123, "(4.1.2), last sentence: 'φ_n est par suite un homomorphisme continu de 𝒪_Y-Modules topologiques'", "'continu' in italics",
    'suite un@@homomorphisme continu', 'italics', None, 'high',
    'suite un@@homomorphisme continu', r'suite un@@homomorphisme \emph{continu}', 'Enlarged crop.')
add(123, "(4.1.2), last sentence: '... homomorphisme continu de 𝒪_Y-Modules topologiques.'",
    '𝒪_Y without the hat (the line above has 𝒪_Ŷ-Modules topologiques pseudo-discrets)',
    r'$\mathcal O_{\widehat Y}$-Modules topologiques.', 'misprint_in_print', None, 'high',
    r'$\mathcal O_{\widehat Y}$-Modules topologiques.', r'$\mathcal O_Y$-Modules topologiques.',
    'Enlarged crop. φ_n is a homomorphism of 𝒪_Ŷ-Modules on Ŷ (its source and target are the limits of the pseudo-discrete '
    '𝒪_Ŷ-Modules of the preceding sentence). The TeX silently corrects it; the fix restores the printed reading. '
    'Disjoint from the italics edit for continu.',
    corrected=r'$\mathcal O_{\widehat Y}$-Modules topologiques.', misprint=True)
conv2(123, "(4.1.3): 'défini dans (I, 10.8.7), de sorte que'", '(I, 10.8.7)', r'(\textbf{I}, 10.8.7)', 'I')
conv2(123, "(4.1.3): '𝒪_X^ → 𝒪_X/𝒦^{k+1} (I, 10.5.2)'", '(I, 10.5.2)', r'(\textbf{I}, 10.5.2)', 'I')
conv2(123, "(4.1.3): 'ℱ^ = i^*(ℱ) (I, 10.8.8) à un isomorphisme canonique près'", '(I, 10.8.8) à un', r'(\textbf{I}, 10.8.8) à un', 'I')
add(123, "end of p. 123 / top of p. 124: (4.1.3.2) | 'à un isomorphisme canonique près, puisque'",
    'p. 124 begins flush left: the sentence continues after the display', r'blank line before \oldpage[III]{124}', 'other', None, 'high',
    r'\label{III.4.1.3.2-fr}@@\]@@@@', r'\label{III.4.1.3.2-fr}@@\]@@',
    'Spurious paragraph break at the page break (GLOBAL_ISSUES item 20). Apply together with the p. 124 entry that removes the '
    'blank line after the marker.')

# ---------------- page 124 ----------------
add(124, "top of p. 124: '\\oldpage[III]{124}' followed by a blank line", 'p. 124 begins flush left (sentence continues)',
    r'\oldpage[III]{124}@@@@à un', 'other', None, 'high',
    r'\oldpage[III]{124}@@@@à un', r'\oldpage[III]{124}@@à un',
    'Second half of the p. 123 entry (blank line before the marker); apply both.')
conv2(124, "(4.1.3): 'H^n(X_k, h_k^*(ℱ^)) (0, 12.1.3.5) s'écrit donc aussi'", '(0, 12.1.3.5)', r'(\textbf{0}, 12.1.3.5)', '0')
add(124, "(4.1.3), after (4.1.3.4): 'Remplaçant X par un ouvert de la forme f^{-1}(V)'", 'new indented paragraph',
    r'\]@@Remplaçant (no blank line)', 'other', None, 'high',
    r'\]@@Remplaçant', r'\]@@@@Remplaçant', PB)
add(124, "(4.1.3): 'donc définissent finalement un homomorphisme canonique de faisceaux'", "'homomorphisme canonique' in italics",
    'un homomorphisme@@canonique de faisceaux', 'italics', None, 'high',
    'un homomorphisme@@canonique de faisceaux', r'un \emph{homomorphisme@@canonique} de faisceaux', '')
conv2(124, "(4.1.4): 'le morphisme canonique d'espaces annelés (I, 10.8.7);'", '(I, 10.8.7)', r'(\textbf{I}, 10.8.7)', 'I')
add(124, "(4.1.4): 'on a j^*(R^nf_*(ℱ)) = R^nf_*(ℱ))^ à un isomorphisme canonique près'",
    'R^nf_*(ℱ))^: the opening parenthesis is missing; hat after the closing parenthesis',
    r'$j^*(R^nf_*(\mathcal F))=\widehat{R^nf_*(\mathcal F)}$', 'misprint_in_print', None, 'high',
    r'$j^*(R^nf_*(\mathcal F))=\widehat{R^nf_*(\mathcal F)}$', r'$j^*(R^nf_*(\mathcal F))=R^nf_*(\mathcal F))' + HAT + '$',
    'Enlarged crop: unbalanced parentheses in the print (the display (4.1.4.1) below has (R^nf_*(ℱ))^). The TeX silently corrects '
    'it (and writes a wide hat); the fix restores the printed reading with the hat after the parenthesis.',
    corrected=r'$j^*(R^nf_*(\mathcal F))=(R^nf_*(\mathcal F))' + HAT + '$', misprint=True)
conv2(124, "(4.1.4): 'à un isomorphisme canonique près (I, 10.8.8)'", '(I, 10.8.8)', r'(\textbf{I}, 10.8.8)', 'I')
add(124, "(4.1.4.1): 'ρ_n : (R^nf_*(ℱ))^ = j^*(R^nf_*(ℱ)) → ...'", '(R^nf_*(ℱ))^ with the hat after the parenthesis',
    r'\rho_n:\widehat{R^nf_*(\mathcal F)}=', 'formula', None, 'high',
    r'\rho_n:\widehat{R^nf_*(\mathcal F)}=', r'\rho_n:(R^nf_*(\mathcal F))' + HAT + '=', 'Enlarged crop.')
add(124, "diagram (4.1.4.2), top left: '(R^nf_*(ℱ))^'", '(R^nf_*(ℱ))^ with the hat after the parenthesis',
    r'\widehat{R^nf_*(\mathcal F)}\ar[rr]', 'formula', None, 'high',
    r'\widehat{R^nf_*(\mathcal F)}\ar[rr]', r'(R^nf_*(\mathcal F))' + HAT + r'\ar[rr]', 'Enlarged crop.')
add(124, "(4.1.4), after (4.1.4.2): 'est commutatif. Il suffit évidemment'", "'commutatif' in italics (the second 'est commutatif.' after (4.1.4.3) is roman)",
    'est commutatif. Il suffit', 'italics', None, 'high',
    'est commutatif. Il suffit', r'est \emph{commutatif}. Il suffit', '')
add(124, "diagram (4.1.4.2), right label 'ψ_n'", 'the n of ψ_n looks bold italic',
    r'\ar[dl]^{\psi_n}', 'misprint_in_print', None, 'low',
    r'\ar[dl]^{\psi_n}', r'\ar[dl]^{\psi_{\boldsymbol{n}}}',
    'Wrong-font n? On a 5x crop the n is much heavier than the n of φ_n in the same diagram (ink about 45% more), but the ψ and '
    'the arrow of this label are also heavier than in (4.1.4.3), so it may be over-inking of the whole label. Apply only if '
    'wrong-font letters are reproduced and the coordinator accepts this reading; otherwise drop.',
    corrected=r'\ar[dl]^{\psi_n}', misprint=True)
add(124, "diagram (4.1.4.3), top left: '(H^n(X, ℱ))^'", '(H^n(X, ℱ))^ with the hat after the parenthesis',
    r'\widehat{H^n(X,\mathcal F)}\ar[rr]', 'formula', None, 'high',
    r'\widehat{H^n(X,\mathcal F)}\ar[rr]', r'(H^n(X,\mathcal F))' + HAT + r'\ar[rr]', 'Enlarged crop.')
add(124, "end of p. 124 / top of p. 125: 'donnent aussitôt le diagramme commutatif' | diagram",
    'the sentence runs into the display at the top of p. 125; no paragraph break', r'blank line before \oldpage[III]{125} (and after it)',
    'other', None, 'medium',
    'aussitôt le diagramme commutatif@@@@', 'aussitôt le diagramme commutatif@@',
    'A blank line before a display makes an empty paragraph line the print does not have (GLOBAL_ISSUES item 20). '
    'Apply together with the p. 125 entry that removes the blank line after the marker.')

# ---------------- page 125 ----------------
add(125, "top of p. 125: '\\oldpage[III]{125}' followed by a blank line and the display", 'no paragraph break before the diagram',
    r'\oldpage[III]{125}@@@@\[', 'other', None, 'medium',
    r'\oldpage[III]{125}@@@@\[', r'\oldpage[III]{125}@@\[',
    'Second half of the p. 124 entry; apply both.')
add(125, "diagram ending (4.1.4): right arrow from H^n(X^, ℱ^) to H^n(X, ℱ_k) = H^n(X_k, i_k^*(ℱ))",
    'two slanting arrows (↘ and ↙) converge on the bottom entry, centred below', r'\ar[d]: the right arrow is vertical',
    'formula', None, 'high',
    r'H^n(X,\mathcal F)\ar[r]\ar[dr]&@@H^n(\widehat X,\widehat{\mathcal F})@@=H^n(\widehat X,i^*(\mathcal F))\ar[d]\\@@&H^n(X,\mathcal F_k)=H^n(X_k,i_k^*(\mathcal F))@@}',
    r'H^n(X,\mathcal F)\ar[rr]\ar[dr]&&@@H^n(\widehat X,\widehat{\mathcal F})@@=H^n(\widehat X,i^*(\mathcal F))\ar[dl]\\@@&H^n(X,\mathcal F_k)=H^n(X_k,i_k^*(\mathcal F))&@@}',
    'Enlarged crop: the arrow under H^n(X^, ℱ^) is ↙, as in the triangles (4.1.4.2)-(4.1.4.3); three columns as in those diagrams.')
add(125, "Théorème (4.1.5): 'du diagramme (4.1.4.2) sont des isomorphismes topologiques'", '(4.1.4.2) upright inside the italic statement',
    r'(\hyperref[III.4.1.4.2-fr]{4.1.4.2}) inside the italic theorem environment: italic', 'convention', 6, 'high',
    r'diagramme@@(\hyperref[III.4.1.4.2-fr]{4.1.4.2}) sont', r'diagramme@@\textup{(\hyperref[III.4.1.4.2-fr]{4.1.4.2})} sont', '')
add(125, "Théorème (4.1.5): 'R^nf^_*(ℱ^) est un 𝒪_X^-Module cohérent'", '𝒪_X^ (hat on X)',
    r'$\mathcal O_{\widehat X}$-Module cohérent et les homomorphismes', 'misprint_in_print', None, 'high', None, None,
    'The TeX keeps the printed reading. R^nf^_*(ℱ^) is a sheaf on Ŷ (f^ : X^ → Ŷ), so the correct reading is 𝒪_Ŷ-Module. '
    'Enlarged crop: the subscript is X^. No authors\' errata entry found.',
    corrected=r'$\mathcal O_{\widehat Y}$-Module cohérent', misprint=True)
add(125, "proof of (4.1.5): 'il en résultera que (R^nf_*(ℱ))^ est cohérent'", '(R^nf_*(ℱ))^ with the hat after the parenthesis',
    r'$\widehat{R^nf_*(\mathcal F)}$ est cohérent', 'formula', None, 'high',
    r'$\widehat{R^nf_*(\mathcal F)}$ est cohérent', r'$(R^nf_*(\mathcal F))' + HAT + r'$ est cohérent', '')
conv2(125, "proof of (4.1.5): 'est cohérent (I, 10.8.8)'", '(I, 10.8.8)', r'(\textbf{I}, 10.8.8)', 'I')
conv2(125, "proof of (4.1.5): 'est alors automatique (I, 10.11.6)'", '(I, 10.11.6)', r'(\textbf{I}, 10.11.6)', 'I')
add(125, "heading of (4.1.6): 'Remarques (4.1.6). — (i) Si on pose'", "'Remarques (4.1.6). —' (the plural remarks heading)",
    r"\begin{env}[4.1.6] ... \emph{Remarques.} (prints '(4.1.6) Remarques.')", 'other', None, 'high',
    r'\begin{env}[4.1.6]@@\label{III.4.1.6-fr}@@\emph{Remarques.}@@',
    r'\begin{remarks}[4.1.6]@@\label{III.4.1.6-fr}@@\upshape@@',
    "Same treatment as the 0_III p. 42 precedent (env with \\emph{Remarques} -> remarks + \\upshape, body roman as printed). "
    "Apply together with the next entry (\\end{env} -> \\end{remarks}); both edits are on p. 125.")
add(125, "end of (4.1.6): 'Nous commencerons par établir la forme affine de (4.1.5) :'", 'end of the same environment',
    r'\end{env}', 'other', None, 'high',
    r'(\hyperref[III.4.1.5-fr]{4.1.5})~:@@\end{env}', r'(\hyperref[III.4.1.5-fr]{4.1.5})~:@@\end{remarks}',
    'Second half of the preceding entry; apply both or neither.')
add(125, "Remarques (4.1.6) (i): 'Si on pose ℱ_k = ℱ^/𝒦^{k+1}ℱ^, il est immédiat que ℱ_k = i_*(ℱ^_k)'",
    'the first ℱ_k has no hat', r'$\widehat{\mathcal F}_k=', 'misprint_in_print', None, 'high',
    r'$\widehat{\mathcal F}_k=@@', r'$\mathcal F_k=@@',
    'Enlarged crop: no hat on the defined symbol; ℱ_k is already ℱ/𝒦^{k+1}ℱ (4.1.2) and ℱ^_k is used undefined in i_*(ℱ^_k). '
    'The TeX silently corrects it; the fix restores the printed reading.',
    corrected=r'$\widehat{\mathcal F}_k=', misprint=True)
conv2(125, "Remarques (4.1.6) (i): 'suites spectrales (0, 13.7)'", '(0, 13.7)', r'(\textbf{0}, 13.7)', '0')
add(125, "Remarques (4.1.6) (ii): 'exprime entre autres que la formation des R^nf_* commute à la complétion'",
    "'la formation des' and 'commute à la complétion' in italics (R^nf_* between them)",
    'que la formation des@@$R^nf_*$ commute à la complétion et', 'italics', None, 'high',
    'que la formation des@@$R^nf_*$ commute à la complétion et',
    r'que \emph{la formation des}@@$R^nf_*$ \emph{commute à la complétion} et', '')
add(125, "Remarques (4.1.6) (ii): 'pourra s'appeler le premier théorème de comparaison'", "'premier théorème de comparaison' in italics",
    'le premier théorème de@@comparaison de', 'italics', None, 'high',
    'le premier théorème de@@comparaison de', r'le \emph{premier théorème de@@comparaison} de', '')
add(125, "after (4.1.6) (ii): 'Nous commencerons par établir la forme affine de (4.1.5) :'", 'new indented paragraph',
    r'\end{enumerate}@@Nous commencerons (no blank line: not indented)', 'other', None, 'high',
    r'\end{enumerate}@@Nous commencerons', r'\end{enumerate}@@@@Nous commencerons',
    'Missing paragraph break: the line is indented in the print; text directly after \\end{enumerate} is not.')
add(125, "Corollaire (4.1.7): 'Les hypothèses étant celles de (4.1.5), supposons en outre'", '(4.1.5) upright inside the italic statement',
    r'(\hyperref[III.4.1.5-fr]{4.1.5}) inside the italic corollary environment: italic', 'convention', 6, 'high',
    r'celles de (\hyperref[III.4.1.5-fr]{4.1.5}), supposons', r'celles de \textup{(\hyperref[III.4.1.5-fr]{4.1.5})}, supposons', 'Enlarged crop.')
add(125, "(4.1.7.1): 'φ_n : (H^n(X, ℱ))^ → lim H^n(X, ℱ_k)'", '(H^n(X, ℱ))^ with the hat after the parenthesis',
    r'\varphi_n:\widehat{H^n(X,\mathcal F)}', 'formula', None, 'high',
    r'\varphi_n:\widehat{H^n(X,\mathcal F)}', r'\varphi_n:(H^n(X,\mathcal F))' + HAT, 'Enlarged crop.')
add(125, "Corollaire (4.1.7): 'vérifie pour tout n la condition (ML), et'", '(ML) upright inside the italic statement',
    'condition (ML), et (italic in the corollary environment)', 'convention', 6, 'high',
    'condition (ML), et', r'condition \textup{(ML)}, et', 'Enlarged crop.')
add(125, "(4.1.7.2): 'ψ_n : H^n(X^, ℱ^) → lim_k H^n(X, ℱ_k)', index k under lim", 'the k under lim is bold italic',
    r'\varprojlim_kH^n(X,\mathcal F_k)', 'misprint_in_print', None, 'medium',
    r'\varprojlim_kH^n(X,\mathcal F_k)@@\tag{4.1.7.2}', r'\varprojlim_{\boldsymbol{k}}H^n(X,\mathcal F_k)@@\tag{4.1.7.2}',
    'Wrong-font k: on a crop it is clearly heavier and slightly larger than the k under lim in (4.1.7.1) (measured ink about 75% '
    'more). The TeX silently has the normal k. Apply only if wrong-font letters are reproduced.',
    corrected=r'\varprojlim_kH^n(X,\mathcal F_k)', misprint=True)
add(125, "end of p. 125: after (4.1.7.2), 'est un isomorphisme. Enfin, la filtration ...'",
    'the statement continues flush left after the display (this line is printed on p. 125)',
    r'blank line before \oldpage[III]{126}', 'other', None, 'high',
    r'\label{III.4.1.7.2-fr}@@\]@@@@', r'\label{III.4.1.7.2-fr}@@\]@@',
    'Spurious paragraph break (GLOBAL_ISSUES item 20). Apply together with the p. 126 marker entry, which moves the marker and '
    'removes the blank line after it. Disjoint from the bold-k edit just before it.')

# ---------------- page 126 ----------------
add(126, "page break 125/126: '... définie par les noyaux des homomor- | phismes canoniques H^n(X, ℱ)→H^n(X, ℱ_k)'",
    "printed p. 126 begins with 'phismes canoniques'; the line 'est un isomorphisme. Enfin, la filtration sur H^n(X, ℱ), définie "
    "par les noyaux des homomor-' is the last line of p. 125",
    r"\oldpage[III]{126} stands before 'est un isomorphisme. Enfin'", 'marker', None, 'high',
    r'\oldpage[III]{126}@@@@est un isomorphisme. Enfin, la filtration sur $H^n(X,\mathcal F)$, définie@@par les noyaux des homomorphismes canoniques',
    r'est un isomorphisme. Enfin, la filtration sur $H^n(X,\mathcal F)$, définie@@par les noyaux des homomor%@@\oldpage[III]{126}@@phismes canoniques',
    'One atomic edit (moves the marker into homomor|phismes, as for canoni%|quement on EGA II p. 37, and drops the blank line after it). '
    'Apply together with the p. 125 entry that removes the blank line before the old marker position.')
add(126, "Corollaire (4.1.7), continued: 'est 𝔍-bonne (0, 13.7.7) et φ_n est un isomorphisme topologique'",
    '(𝟎, 13.7.7): bold 0', '(0, 13.7.7)', 'convention', 2, 'high',
    '(0, 13.7.7)', r'\textup{(\textbf{0}, 13.7.7)}',
    'One edit for this finding and the next (convention 6): bold numeral and the upright reference together.')
add(126, "Corollaire (4.1.7), continued: same reference '(0, 13.7.7)'", 'the reference is upright inside the italic statement',
    '(0, 13.7.7) inside the italic corollary environment: italic', 'convention', 6, 'high', None, None,
    'Covered by the edit of the preceding finding (convention 2), which adds the \\textup.')
add(126, "end of Corollaire (4.1.7): 'isomorphisme topologique (¹).'", 'footnote mark before the full stop',
    r'topologique.\footnote{...}', 'punctuation', None, 'high',
    r'topologique.@@\footnote{La démonstration qui suit, plus simple que la démonstration@@initiale, et le complément relatif à la filtration de@@$H^n(X,\mathcal F)$, nous ont été communiqués par J.-P. Serre.}@@\end{corollary}',
    r'topologique\footnote{La démonstration qui suit, plus simple que la démonstration@@initiale, et le complément relatif à la filtration de@@$H^n(X,\mathcal F)$, nous ont été communiqués par J.-P. Serre.}.@@\end{corollary}',
    'One edit: moves the full stop after the footnote mark, as in the 0_I p. 54 precedent. The footnote text itself matches the print.')
add(126, "proof of (4.1.7): between (4.1.7.3) and (4.1.7.4)", "no 'et': (4.1.7.4) follows (4.1.7.3) directly as the next display line",
    r'\]@@et@@\[', 'extra', None, 'high',
    r'\]@@et@@\[@@\mathrm R_k=\operatorname{Ker}', r'\]@@\[@@\mathrm R_k=\operatorname{Ker}',
    'The two numbered formulas stand on consecutive lines with nothing between them (strip p. 126 s1).')
add(126, "proof of (4.1.7), after (4.1.7.4): 'La suite exacte de cohomologie'", 'new indented paragraph',
    r'\]@@La suite exacte de cohomologie (no blank line)', 'other', None, 'high',
    r'\]@@La suite exacte de cohomologie', r'\]@@@@La suite exacte de cohomologie', PB)
add(126, "proof of (4.1.7): 'montre que l'on a aussi R_k = Im(H^n(X, 𝔍^{k+1}ℱ)→H^n(X, ℱ)); nous poserons'",
    'the formula is set inline in the running text', r'displayed with \[ ... \] (with \bigl( \bigr))', 'other', None, 'high',
    r"montre que l'on a aussi@@\[@@\mathrm R_k=\operatorname{Im}\bigl(@@H^n(X,\mathfrak J^{k+1}\mathcal F)\longrightarrow H^n(X,\mathcal F)@@\bigr)~;@@\]@@nous poserons",
    r"montre que l'on a aussi@@$\mathrm R_k=\operatorname{Im}(@@H^n(X,\mathfrak J^{k+1}\mathcal F)\longrightarrow H^n(X,\mathcal F)@@)$~;@@nous poserons",
    'Layout: the print sets this formula inline (GLOBAL_ISSUES items 21/36), with ordinary-size parentheses.')
add(126, "proof of (4.1.7), after (4.1.7.5): 'On a donc la suite exacte'", 'new indented paragraph',
    r'\]@@On a donc la suite exacte (no blank line)', 'other', None, 'high',
    r'\]@@On a donc la suite exacte', r'\]@@@@On a donc la suite exacte', PB)
add(126, "(4.1.7.7): 'la multiplication par x dans 𝔍^kℱ'", 'this x is bold italic (the x of \u00abSoit x un élément\u00bb on the same line is not)',
    r'multiplication par@@$x$ dans', 'misprint_in_print', None, 'medium',
    r'multiplication par@@$x$ dans', r'multiplication par@@$\boldsymbol{x}$ dans',
    'Wrong-font x: side-by-side crops at 6x, same size, clearly heavier strokes (measured ink about 25% more). The TeX silently has '
    'the normal x. Apply only if wrong-font letters are reproduced.',
    corrected=r'multiplication par@@$x$ dans', misprint=True)
add(126, "(4.1.7.7), after (4.1.7.8): 'Si on désigne par S la A-algèbre graduée'", 'new indented paragraph',
    r'\]@@Si on désigne (no blank line)', 'other', None, 'high',
    r'\]@@Si on désigne', r'\]@@@@Si on désigne', PB)
add(126, "(4.1.7.7): 'une structure de module gradué de type fini sur l'anneau gradué S'", "'module gradué de type fini' in italics",
    'structure de module gradué de type fini sur', 'italics', None, 'high',
    'structure de module gradué de type fini sur', r'structure de \emph{module gradué de type fini} sur', '')
add(126, "(4.1.7.7): 'qui est noethérien (II, 2.1.5)'", "'noethérien' in italics", 'qui est noethérien',
    'italics', None, 'high', 'qui est noethérien', r'qui est \emph{noethérien}', '')
add(126, "(4.1.7.7): 'qui est noethérien (II, 2.1.5)'", '(𝐈𝐈, 2.1.5): bold II', '(II, 2.1.5)', 'convention', 2, 'high',
    '(II, 2.1.5)', r'(\textbf{II}, 2.1.5)', 'Bold II in the reference to chapter II.')
add(126, "(4.1.7.10): '𝔍^mR_k ⊂ R_{k+m},'", 'the k of the subscript k+m is bold italic (the k of R_k on the same line is not)',
    r'\mathrm R_{k+m},', 'misprint_in_print', None, 'medium',
    r'\mathrm R_{k+m},@@\tag{4.1.7.10}', r'\mathrm R_{\boldsymbol{k}+m},@@\tag{4.1.7.10}',
    'Wrong-font k: crops at 4x and 7x, same size as the k of R_k, clearly heavier (measured ink about 30% more). The m may be heavy '
    'too but cannot be told from the normal small m. The TeX silently has the normal k. Apply only if wrong-font letters are reproduced.',
    corrected=r'\mathrm R_{k+m}', misprint=True)
add(126, "proof of (4.1.7.9): 'l'application μ_{x,0}. | Pour tout x∈𝔍^m, le diagramme'", "'Pour tout x∈𝔍^m' begins a new indented paragraph",
    r'$\mu_{x,0}$. Pour tout (same paragraph)', 'other', None, 'high',
    r'$\mu_{x,0}$. Pour tout', r'$\mu_{x,0}$.@@@@Pour tout',
    'Missing paragraph break: the line is indented in the print (measured on the strip).')
add(126, "proof of (4.1.7.9): the diagram 𝔍^{k+1}ℱ →x 𝔍^{k+m+1}ℱ over ℱ →x ℱ",
    'this diagram has no number; (4.1.7.11) is the number of the next diagram (the cohomology square on p. 127)',
    r'\tag{4.1.7.11}\label{III.4.1.7.11-fr} on this diagram', 'extra', None, 'high',
    r'\mathcal F\ar[r]_x&\mathcal F@@}@@\tag{4.1.7.11}\label{III.4.1.7.11-fr}@@\]@@@@',
    r'\mathcal F\ar[r]_x&\mathcal F@@}@@\]@@',
    'Strips s3/s4 (80 px overlap): no number beside this diagram; p. 127 prints (4.1.7.11) beside the square with μ_{x,m}, μ_{x,0}, '
    'which (4.1.7.12) uses \u00aboù on remplace n par n+1\u00bb. The same edit removes the blank line before \\oldpage[III]{127} (next finding). '
    'Apply together with the page-127 entry of findings_127_131.json (kind missing) that puts \\tag{4.1.7.11}\\label{III.4.1.7.11-fr} '
    'on the cohomology diagram, so the label used by \\hyperref in (4.1.7.12) exists exactly once; and with the p. 127 entry below '
    '(blank line after the marker).')
add(126, "end of p. 126 / top of p. 127: diagram | '(où les flèches horizontales sont la multiplication par x, ...) est commutatif'",
    'p. 127 begins flush left: the sentence continues after the diagram', r'blank line before \oldpage[III]{127}', 'other', None, 'high',
    None, None, 'Spurious paragraph break (GLOBAL_ISSUES item 20); covered by the edit of the preceding finding.')

# ---------------- page 127 (outside this run's pages) ----------------
add(127, "top of p. 127: '\\oldpage[III]{127}' followed by a blank line", 'p. 127 begins flush left (sentence continues)',
    r'\oldpage[III]{127}@@@@(où', 'other', None, 'high',
    r'\oldpage[III]{127}@@@@(où', r'\oldpage[III]{127}@@(où',
    "OUTSIDE pp. 122-126: 'old' lies in page_127.tex (checked unique there). Second half of the p. 126 entry that removes the blank "
    'line before the marker; findings_127_131.json has no entry for it (checked).')

json.dump(F, open(OUT, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print(len(F), 'findings written')
