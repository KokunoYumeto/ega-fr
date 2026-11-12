"""Build findings_345_349.json and check every edit against page_NNN.tex and a simulated page-segment apply.
No .tex file is written.  '~N~' inside strings below stands for a newline."""
import json, re, pathlib

RUN = pathlib.Path('user/Documents/ega_scan_check_20261101/run_IVback')
SRC = pathlib.Path('user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-errata-addenda-list3-fr.tex')
CUR = pathlib.Path('user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/current/packages/IV4/native/ega4/ega4-errata-addenda-list3-fr.tex')
OUT = RUN / 'findings_345_349.json'

NL = '~N~'
def s(x):
    return None if x is None else x.replace(NL, '\n')

F = []
def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=(None if old is None else dict(old=s(old), new=s(new))), note=note)
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    F.append(d)

# ---------------------------------------------------------------- heading helpers
def stop_plain(page, label):           # \paragraph{(II, 3.3.2).}
    add(page, f'heading ({label})', f'({label}) followed directly by the text, no full stop',
        f'\\paragraph{{({label}).}}', 'punctuation', None, 'high',
        f'({label}).}}', f'({label})}}',
        'The errata headings carry a full stop the print lacks (GLOBAL_ISSUES 32; EGA II p. 217 fixed the same way).')

def stop_IV(page, num):                # hyperref heading (IV, n)
    add(page, f'heading (IV, {num})', f'(IV, {num}) followed directly by the text, no full stop',
        f'\\paragraph{{(...{{IV, {num}}}).}}', 'punctuation', None, 'high',
        f'{{IV, {num}}}}}).}}', f'{{IV, {num}}}}})}}',
        'The errata headings carry a full stop the print lacks (GLOBAL_ISSUES 32).')

def zero_head(page, sub, num):         # \paragraph{($0_{\mathrm{IV}}$, n).}
    lab = f'0_{sub}, {num}'
    add(page, f'heading ({lab})', f'bold 0 with a light subscript {sub}: (0_{sub}, {num})',
        f'($0_{{\\mathrm{{{sub}}}}}$, {num}) in \\paragraph: math-mode 0 prints in normal weight', 'convention', 2, 'high',
        f'\\paragraph{{($0_{{\\mathrm{{{sub}}}}}$, {num})', f'\\paragraph{{($\\mathbf{{0}}_{{\\mathrm{{{sub}}}}}$, {num})',
        'Math mode ignores the \\paragraph bold (GLOBAL_ISSUES 56; EGA III errata page-fixed with $\\mathbf{0}_{\\mathrm I}$). '
        'Independent of the full-stop fix on the same heading (either order).')
    add(page, f'heading ({lab})', f'({lab}) followed directly by the text, no full stop',
        f'\\paragraph{{({lab}).}}', 'punctuation', None, 'high',
        f'{num}).}}', f'{num})}}',
        'The errata headings carry a full stop the print lacks (GLOBAL_ISSUES 32). Independent of the bold-0 fix on the same heading.')

def err_head(page, n, where_extra=''):
    add(page, f'heading (Err_IV, {n}){where_extra}', f'bold Err with a light roman subscript IV: (Err_IV, {n})',
        f'(Err\\textsubscript{{IV}}, {n}) inside \\paragraph: the subscript IV is bold', 'font', None, 'high',
        f'(Err\\textsubscript{{IV}}, {n})', f'($\\mathbf{{Err}}_{{\\mathrm{{IV}}}}$, {n})',
        'Same form as the EGA III errata headings ($\\mathbf{Err}_{\\mathrm{III}}$, light subscript). '
        'Independent of the full-stop fix on the same heading (either order).')
    add(page, f'heading (Err_IV, {n}){where_extra}', f'(Err_IV, {n}) followed directly by the text, no full stop',
        f'\\paragraph{{(Err\\textsubscript{{IV}}, {n}).}}', 'punctuation', None, 'high',
        f', {n}).}}', f', {n})}}',
        'The errata headings carry a full stop the print lacks (GLOBAL_ISSUES 32). Independent of the subscript fix on the same heading.')

def conv2(page, where, scan, tex, old, new, note=''):
    add(page, where, scan, tex, 'convention', 2, 'high', old, new, note or 'Bold chapter numeral in the print.')

def ital(page, where, scan, tex, old, new, note='', conf='high'):
    add(page, where, scan, tex, 'italics', None, conf, old, new, note or 'Italic in the print, upright in the TeX.')

def degtr(page, where, old, new, extra=''):
    add(page, where, 'deg.tr_k (no full stop after tr)', '\\operatorname{deg.tr.}', 'punctuation', None, 'high', old, new,
        'The print has no full stop after "tr" (as in the main text of EGA IV-2, where ega4-2 was page-fixed to \\operatorname{deg.tr}).' + extra)

# ================================================================ PAGE 345
P = 345
add(P, 'heading A) of the list', 'centred "A) Erreurs typographiques" in text size, "Erreurs typographiques" italic, "A)" upright',
    '\\subsection*{A) Erreurs typographiques} (bold, no italics)', 'italics', None, 'medium',
    '\\subsection*{A) Erreurs typographiques}', '\\begin{center}~N~A) \\emph{Erreurs typographiques}~N~\\end{center}',
    'Same form as the EGA III errata (Liste 2) heading in ega3-7-fr.tex. If headings are left to a document-wide decision, keep at least the italics.')
stop_plain(P, 'II, 3.3.2')
stop_plain(P, 'II, 4.1.1')
add(P, '(II, 4.1.1), first formula', '𝒪-ₚModule: hyphen, then a SUBSCRIPT P, then "Module" (no hyphen before Module)',
    '$\\sh{O}$-$P$-Module (P on the line, extra hyphen)', 'formula', None, 'high',
    '$\\sh{O}$-$P$-', '$\\sh{O}$-${}_P$',
    'The erratum quotes the faulty "𝒪-ₚModule" of EGA II p. 71. Independent of the italics fix on "Module" (either order).')
ital(P, '(II, 4.1.1)', '𝒪-ₚ*Module* par 𝒪ₚ-*Module*', 'Module upright (twice)',
     'Module par~N~$\\sh{O}_P$-Module.', '\\emph{Module} par~N~$\\sh{O}_P$-\\emph{Module}.')
stop_plain(P, 'II, 5.4.5')
stop_plain(P, 'II, 5.4.8')
stop_plain(P, 'II, 6.4.4')
ital(P, '(II, 6.4.4)', 'remplacer *normal* par *intégralement clos*', 'roman',
     'remplacer normal par intégralement clos.', 'remplacer \\emph{normal} par \\emph{intégralement clos}.')
stop_plain(P, 'II, 6.4.7')
ital(P, '(II, 6.4.7)', 'remplacer *dimension* par *rang*', 'roman',
     'remplacer dimension par rang.', 'remplacer \\emph{dimension} par \\emph{rang}.')
stop_plain(P, 'II, 6.5.2')
add(P, '(II, 6.5.2), second sentence', '(N_{ℬ/𝒜}ω_{λ_μ}): μ is a sub-subscript of λ',
    '\\omega_{\\lambda\\mu}', 'misprint_in_print', None, 'medium',
    '\\omega_{\\lambda\\mu}', '\\omega_{\\lambda_\\mu}',
    'The TeX silently corrects: the print sets μ below λ (side-by-side crop crops_345_349/p345_omega.png); EGA II (6.5.2) has the double index ω_{λμ}.',
    corrected='\\omega_{\\lambda\\mu}')
zero_head(P, 'III', '8.1.11')
zero_head(P, 'III', '9.1.2')
add(P, '(0_III, 9.1.2)', 'remplacer 𝔉 par X (Fraktur F)', '$\\sh{F}$ (script F)', 'symbol', None, 'high',
    'remplacer $\\sh{F}$ par $X$', 'remplacer $\\mathfrak{F}$ par $X$',
    'The erratum quotes the Fraktur 𝔉 of 0_III (9.1.2) ("rétrocompactes de $\\mathfrak{F}$" in ega3-1-fr.tex); the script 𝓕 of the print looks different (cf. (III, 7.8.5) on this page).')
zero_head(P, 'III', '10.2.1')
stop_plain(P, 'III, 4.4.12')
stop_plain(P, 'III, 5.2.5')
conv2(P, '(III, 5.2.5)', '(**I**, 5.5.4)', '(I, 5.5.4)', 'remplacer (I, 5.5.4)', 'remplacer (\\textbf{I}, 5.5.4)')
conv2(P, '(III, 5.2.5)', '(**II**, 5.5.4)', '(II, 5.5.4)', 'par (II, 5.5.4)', 'par (\\textbf{II}, 5.5.4)')
stop_plain(P, 'III, 7.4.7')
ital(P, '(III, 7.4.7)', 'remplacer : *tout* A-*module* par : *tout* A-*module* M', 'all roman',
     'remplacer : tout $A$-module par : tout~N~$A$-module $M$.',
     'remplacer : \\emph{tout} $A$-\\emph{module} par : \\emph{tout}~N~$A$-\\emph{module} $M$.')
stop_plain(P, 'III, 7.8.5')
stop_plain(P, 'III, 7.8.9')
stop_plain(P, 'III, 7.9.11')
for num in ['16.2.2.2', '17.3.7', '18.1.3', '19.8.7', '19.8.8', '20.5.4', '20.7.8', '21.5.3', '21.7.1', '22.1.1']:
    zero_head(P, 'IV', num)

# ================================================================ PAGE 346
P = 346
for num in ['22.3.3', '22.7.3', '23.1.3']:
    zero_head(P, 'IV', num)
stop_IV(P, '2.1.1')
conv2(P, '(IV, 2.1.1)', '(**III**, 1.4.15.1)', '(III, 1.4.15.1)', 'remplacer (III, 1.4.15.1)', 'remplacer (\\textbf{III}, 1.4.15.1)')
conv2(P, '(IV, 2.1.1)', '(**III**, 1.4.15.5)', '(III, 1.4.15.5)', '(III, 1.4.15.5)', '(\\textbf{III}, 1.4.15.5)')
stop_IV(P, '2.4.3')
add(P, '(IV, 2.4.3)', 'the replacement (X_red ×_{Y_red} Y\'_red)_red. is a centred display', 'set in the line',
    'other', None, 'high',
    'par~N~$(X_{\\mathrm{red}}\\times_{Y_{\\mathrm{red}}}Y\'_{\\mathrm{red}})_{\\mathrm{red}}$.',
    'par~N~\\[~N~(X_{\\mathrm{red}}\\times_{Y_{\\mathrm{red}}}Y\'_{\\mathrm{red}})_{\\mathrm{red}}.~N~\\]',
    'The print centres the second formula on a line of its own, with extra space before the next entry.')
stop_IV(P, '2.6.1')
stop_IV(P, '4.2.1')
degtr(P, '(IV, 4.2.1), first line', '$\\operatorname{deg.tr.}_kE$ par $\\operatorname{deg.tr.}_LE$',
      '$\\operatorname{deg.tr}_kE$ par $\\operatorname{deg.tr}_LE$')
degtr(P, '(IV, 4.2.1), second line', '$\\operatorname{deg.tr.}_kL(', '$\\operatorname{deg.tr}_kL(',
      ' Independent of the bold-t fix on the same formula.')
degtr(P, '(IV, 4.2.1), second line', '$\\operatorname{deg.tr.}_LL(', '$\\operatorname{deg.tr}_LL(',
      ' Independent of the bold-t fix on the same formula.')
add(P, '(IV, 4.2.1)', 'deg.tr_kL(**t**): bold upright t', 'L(t)', 'font', None, 'high',
    'L(t)$ par', 'L(\\mathbf{t})$ par', 'Independent of the deg.tr fix on the same formula.')
add(P, '(IV, 4.2.1)', 'deg.tr_LL(**t**): bold upright t', 'L(t)', 'font', None, 'high',
    'L(t)$;', 'L(\\mathbf{t})$;', 'Independent of the deg.tr fix on the same formula.')
stop_IV(P, '4.4.2')
stop_IV(P, '4.7.3')
ital(P, '(IV, 4.7.3)', 'remplacer *préschéma* par *k-préschéma*', 'roman',
     'remplacer préschéma par $k$-préschéma.', 'remplacer \\emph{préschéma} par $k$-\\emph{préschéma}.')
stop_IV(P, '5.6.1')
add(P, '(IV, 5.6.1)', '**k**(𝔭( : bold italic k', 'k', 'convention', 1, 'high',
    '$k(\\mathfrak p($ par', '$\\boldsymbol{k}(\\mathfrak p($ par', 'Residue field k.')
add(P, '(IV, 5.6.1)', '**k**(𝔭) : bold italic k', 'k', 'convention', 1, 'high',
    '$k(\\mathfrak p)$.', '$\\boldsymbol{k}(\\mathfrak p)$.', 'Residue field k.')
stop_IV(P, '5.6.5')
add(P, '(IV, 5.6.5)', '**k**(ξ)) : bold italic k', 'k', 'convention', 1, 'high',
    '$k(\\xi))$', '$\\boldsymbol{k}(\\xi))$', 'Residue field k.')
stop_IV(P, '5.6.11.1')
stop_IV(P, '5.11.2')
stop_IV(P, '6.1.5')
conv2(P, '(IV, 6.1.5)', '(**0**, 16.3.9.2): bare bold 0, no subscript', '($0$, 16.3.9.2)', '($0$, 16.3.9.2)', '(\\textbf{0}, 16.3.9.2)')
for num in ['6.3.1', '6.7.2', '6.10.1', '6.14.1', '6.15.2']:
    stop_IV(P, num)
add(P, '(IV, 6.15.2)', 't(t—v): long dash for the minus', 't(t-v)', 'convention', 7, 'high',
    '$t(t-v)$ par', '$t(t\\setmin v)$ par', '')
add(P, '(IV, 6.15.2)', 't²(t—v)²: long dash for the minus', 't^2(t-v)^2', 'convention', 7, 'high',
    '$t^2(t-v)^2$', '$t^2(t\\setmin v)^2$', '')
for num in ['6.15.7', '7.5.4', '7.8.4']:
    stop_IV(P, num)
add(P, 'heading (IV, 2e Partie, Bibliographie)', '(**IV**, 2^e Partie, Bibliographie): only IV bold; parentheses and "2e Partie, Bibliographie" roman; no full stop',
    '\\paragraph{(IV, 2\\textsuperscript{e} Partie, Bibliographie).}: all bold, with a full stop', 'font', None, 'high',
    '\\paragraph{(IV, 2\\textsuperscript{e} Partie, Bibliographie).}',
    '(\\textbf{IV}, 2\\textsuperscript{e} Partie, Bibliographie)',
    'One edit for the weight and the extra full stop (as EGA II p. 221: \\paragraph{Insérer après (I, 3.2.8) :} replaced by plain text with \\textbf on the numerals). '
    'The entry stays a new indented paragraph (blank line before it).')
for num in ['8.5.8', '8.10.1', '10.2.1', '10.4.11', '11.2.9', '11.3.4', '11.3.10', '11.7.5', '12.1.1']:
    stop_IV(P, num)
ital(P, '(IV, 12.1.1)', 'ajouter à la fin : *pour* k⩾1', 'pour roman',
     'à la fin : pour $k\\geq1$.', 'à la fin : \\emph{pour} $k\\geq1$.')
stop_IV(P, '14.2.1')

# ================================================================ PAGE 347
P = 347
for num in ['14.3.8', '14.5.7', '14.5.11', '15.4.2', '15.5.2', '15.6.10']:
    stop_IV(P, num)
add(P, 'heading B) of the list', 'centred "B) Modifications de texte" in text size, "Modifications de texte" italic, "B)" upright',
    '\\subsection*{B) Modifications de texte} (bold, no italics)', 'italics', None, 'medium',
    '\\subsection*{B) Modifications de texte}', '\\begin{center}~N~B) \\emph{Modifications de texte}~N~\\end{center}',
    'Same form as the EGA III errata heading B) in ega3-7-fr.tex (the IV print has no footnote here).')
err_head(P, 1)
conv2(P, 'Err_IV 1, first line', 'Dans (**0**_III, 11.1.6)', '($0_{\\mathrm{III}}$, 11.1.6)',
      'Dans ($0_{\\mathrm{III}}$, 11.1.6)', 'Dans ($\\mathbf{0}_{\\mathrm{III}}$, 11.1.6)')
add(P, 'Err_IV 1, "est alors E_r^{p0}"', 'E_r^{p0} (no comma in the exponent; the d_r^{p,0} before it has one)', 'E_r^{p,0}',
    'formula', None, 'high', 'est alors $E_r^{p,0}$', 'est alors $E_r^{p0}$',
    'Crop crops_345_349/p347_Ep0.png. The later E_{r+1}^{p,0}=E_r^{p,0} has the commas and stays.')
add(P, 'Err_IV 1, "l\'image de d_r^{p0}"', 'd_r^{p0} (no comma)', 'd_r^{p,0}', 'formula', None, 'high',
    "l'image de $d_r^{p,0}$", "l'image de $d_r^{p0}$", 'Crop crops_345_349/p347_dp0.png.')
add(P, 'Err_IV 1, "est E^{p+r,-r+1}=0"', 'E^{p+r,—r+1}=0 without the subscript r', 'E_r^{p+r,-r+1}=0',
    'misprint_in_print', None, 'high', '$E_r^{p+r,-r+1}=0$', '$E^{p+r,-r+1}=0$',
    'The TeX silently corrects; every other term of the argument is on page r of the spectral sequence. Crop crops_345_349/p347_err1e.png.',
    corrected='$E_r^{p+r,-r+1}=0$')
err_head(P, 2)
conv2(P, 'Err_IV 2', 'Dans (**III**, 3.4)', '(III, 3.4)', 'Dans (III, 3.4)', 'Dans (\\textbf{III}, 3.4)')

# ================================================================ PAGE 348 segment, Err_IV 3-12 (printed on p. 347)
P = 348
W = ' (printed p. 347; in the page_348 segment until the p. 348 marker moves)'
conv2(P, 'Err_IV 3' + W, 'Dans (**III**, 4.4.9)', '(III, 4.4.9)', 'Dans (III, 4.4.9)', 'Dans (\\textbf{III}, 4.4.9)')
ital(P, 'Err_IV 3' + W, 'remplacer : *finies* par : *finies en tant qu\'ensembles*', 'roman',
     "remplacer : finies par :~N~finies en tant qu'ensembles.",
     "remplacer : \\emph{finies} par :~N~\\emph{finies en tant qu'ensembles}.")
err_head(P, 4, W)
conv2(P, 'Err_IV 4' + W, 'Dans (**III**, 7.8.10)', '(III, 7.8.10)', 'Dans (III, 7.8.10)', 'Dans (\\textbf{III}, 7.8.10)')
err_head(P, 5, W)
conv2(P, 'Err_IV 5' + W, '(**0**_IV, 16.1.4)', '($0_{\\mathrm{IV}}$, 16.1.4)', '($0_{\\mathrm{IV}}$, 16.1.4)', '($\\mathbf{0}_{\\mathrm{IV}}$, 16.1.4)')
ital(P, 'Err_IV 5' + W, "Dire qu'un anneau *intègre* A est caténaire", 'intègre roman',
     "anneau intègre $A$ est", "anneau \\emph{intègre} $A$ est")
err_head(P, 6, W)
conv2(P, 'Err_IV 6' + W, '(**0**_IV, 16.1.9)', '($0_{\\mathrm{IV}}$, 16.1.9)', '($0_{\\mathrm{IV}}$, 16.1.9)', '($\\mathbf{0}_{\\mathrm{IV}}$, 16.1.9)')
err_head(P, 7, W)
conv2(P, 'Err_IV 7' + W, '(**0**_IV, 16.5.12)', '($0_{\\mathrm{IV}}$, 16.5.12)', '($0_{\\mathrm{IV}}$, 16.5.12)', '($\\mathbf{0}_{\\mathrm{IV}}$, 16.5.12)')
err_head(P, 8, W)
conv2(P, 'Err_IV 8' + W, '(**0**_IV, 19.3.12)', '($0_{\\mathrm{IV}}$, 19.3.12)', '($0_{\\mathrm{IV}}$, 19.3.12)', '($\\mathbf{0}_{\\mathrm{IV}}$, 19.3.12)')
err_head(P, 9, W)
conv2(P, 'Err_IV 9' + W, '(**0**_IV, 19.8.3)', '($0_{\\mathrm{IV}}$, 19.8.3)', '($0_{\\mathrm{IV}}$, 19.8.3)', '($\\mathbf{0}_{\\mathrm{IV}}$, 19.8.3)')
ital(P, 'Err_IV 9' + W, 'remplacer *homomorphisme* par *homomorphisme local*', 'roman',
     'remplacer homomorphisme par homomorphisme local;', 'remplacer \\emph{homomorphisme} par \\emph{homomorphisme local};')
conv2(P, 'Err_IV 9' + W, '(**0**_IV, 19.8.4)', '($0_{\\mathrm{IV}}$, 19.8.4)', '($0_{\\mathrm{IV}}$, 19.8.4)', '($\\mathbf{0}_{\\mathrm{IV}}$, 19.8.4)')
err_head(P, 10, W)
conv2(P, 'Err_IV 10' + W, '(**0**_IV, 20.1.2)', '($0_{\\mathrm{IV}}$, 20.1.2)', '($0_{\\mathrm{IV}}$, 20.1.2)', '($\\mathbf{0}_{\\mathrm{IV}}$, 20.1.2)')
add(P, 'Err_IV 10' + W, 'aD par bD: roman D (the derivation D of (20.1.2))', 'italic $aD$, $bD$', 'font', None, 'medium',
    '$aD$ par $bD$', '$a\\mathrm{D}$ par $b\\mathrm{D}$',
    'Rule for EGA IV-4: derivations D are roman (\\mathrm{D}); the print shows an upright D like its other capitals. Drop if the coordinator leaves this D to the upright-capitals decision (GLOBAL_ISSUES 17).')
ital(P, 'Err_IV 10' + W, 'remplacer A-*module* par B-*module*', 'module roman',
     'remplacer $A$-module par $B$-module.', 'remplacer $A$-\\emph{module} par $B$-\\emph{module}.')
err_head(P, 11, W)
conv2(P, 'Err_IV 11' + W, '(**0**_IV, 20.2.1)', '($0_{\\mathrm{IV}}$, 20.2.1)', '($0_{\\mathrm{IV}}$, 20.2.1)', '($\\mathbf{0}_{\\mathrm{IV}}$, 20.2.1)')
ital(P, 'Err_IV 11' + W, 'remplacer A-*modules* par B-*modules*', 'modules roman',
     '$A$-modules par $B$-modules.', '$A$-\\emph{modules} par $B$-\\emph{modules}.')
add(P, 'Err_IV 11' + W, '"Ligne 21 et 22" (singular)', '"Lignes 21 et 22"', 'misprint_in_print', None, 'medium',
    'Lignes 21 et 22', 'Ligne 21 et 22',
    'The TeX silently corrects; elsewhere the list writes "Lignes 7, 8 et 9", "lignes 6 et 8", "Lignes 1 à 3". Crop crops_345_349/p347_ligne2122.png.',
    corrected='Lignes 21 et 22')
err_head(P, 12, W)
conv2(P, 'Err_IV 12' + W, '(**0**_IV, 20.4.6.1)', '($0_{\\mathrm{IV}}$, 20.4.6.1)', '($0_{\\mathrm{IV}}$, 20.4.6.1)', '($\\mathbf{0}_{\\mathrm{IV}}$, 20.4.6.1)')
add(P, 'Err_IV 12' + W, 'p₂—p₁: long dash', 'p_2-p_1', 'convention', 7, 'high', '$p_2-p_1$ par', '$p_2\\setmin p_1$ par', '')
add(P, 'Err_IV 12' + W, 'p₁—p₂: long dash', 'p_1-p_2', 'convention', 7, 'high', 'par $p_1-p_2$;', 'par $p_1\\setmin p_2$;', '')
add(P, 'Err_IV 12' + W, 'x⊗1—1⊗x: long dash', 'x\\otimes1-1\\otimes x', 'convention', 7, 'high',
    '$x\\otimes1-1\\otimes x$', '$x\\otimes1\\setmin 1\\otimes x$', '')
add(P, 'Err_IV 12' + W, '1⊗x—x⊗1: long dash', '1\\otimes x-x\\otimes1', 'convention', 7, 'high',
    '$1\\otimes x-x\\otimes1$', '$1\\otimes x\\setmin x\\otimes1$', '')
add(347, 'Err_IV 12, first half (printed p. 347; text in the page_348 segment)',
    '"remplacer p₂—p₁ par p₁—p₂"', 'the same (kept)', 'misprint_in_print', None, 'high', None, None,
    'Error of the print, kept in the diplomatic text (fix null): (0_IV, 20.4.6.1) prints d_{B/A}=p_1-p_2 (ega0-20-fr.tex line 782), so the erratum must replace p_1-p_2 by p_2-p_1, as its second half and Err_IV 13 confirm (GLOBAL_ISSUES 67).',
    corrected='remplacer $p_1\\setmin p_2$ par $p_2\\setmin p_1$')

# ================================================================ PAGE 348 (printed p. 348)
P = 348
conv2(P, 'Err_IV 13', '(**0**_IV, 20.4.8)', '($0_{\\mathrm{IV}}$, 20.4.8)', '($0_{\\mathrm{IV}}$, 20.4.8)', '($\\mathbf{0}_{\\mathrm{IV}}$, 20.4.8)')
add(P, 'Err_IV 13', 'p₂=p₁—d_{B/A}: long dash', 'p_1-d_{B/A}', 'convention', 7, 'high', '$p_2=p_1-d_{B/A}$', '$p_2=p_1\\setmin d_{B/A}$', '')
add(P, 'Err_IV 13', 'p₁=p₂—d_{B/A}: long dash', 'p_2-d_{B/A}', 'convention', 7, 'high', '$p_1=p_2-d_{B/A}$', '$p_1=p_2\\setmin d_{B/A}$', '')
err_head(P, 14)
conv2(P, 'Err_IV 14', '(**0**_IV, 20.4.13)', '($0_{\\mathrm{IV}}$, 20.4.13)', '($0_{\\mathrm{IV}}$, 20.4.13)', '($\\mathbf{0}_{\\mathrm{IV}}$, 20.4.13)')
ital(P, 'Err_IV 14, (iv)', 'une extension *séparable* de celui de A', 'roman',
     'extension séparable de celui', 'extension \\emph{séparable} de celui')
ital(P, 'Err_IV 14, (iv)', 'est un *module de torsion*', 'roman',
     'est un module de torsion.', 'est un \\emph{module de torsion}.')
err_head(P, 15)
conv2(P, 'Err_IV 15', '(**0**_IV, 22.2.7)', '($0_{\\mathrm{IV}}$, 22.2.7)', '($0_{\\mathrm{IV}}$, 22.2.7)', '($\\mathbf{0}_{\\mathrm{IV}}$, 22.2.7)')
err_head(P, 16)
ital(P, 'Err_IV 16, last sentence', '« *de présentation finie* » par « *localement de présentation finie* »', 'roman',
     'remplacer « de présentation finie » par~N~« localement de présentation finie »',
     'remplacer « \\emph{de présentation finie} » par~N~« \\emph{localement de présentation finie} »')
err_head(P, 17)
conv2(P, 'Err_IV 17', 'Dans (**IV**, 3.1.10)', '(IV, 3.1.10)', 'Dans (IV, 3.1.10)', 'Dans (\\textbf{IV}, 3.1.10)')
add(P, 'Remarque (3.1.10.2), displays (3.1.10.3)-(3.1.10.4)',
    'display (3.1.10.3) Ass(f_*(𝓕))⊂f(X) (no comma); text line "et, si X est localement noethérien,"; display (3.1.10.4) Ass(f_*(𝓕))⊂f(Ass(𝓕)).',
    'one align: "f(X)," then "\\quad\\text{si $X$ est localement noethérien}." inside the second display; "et," lost',
    'word', None, 'high',
    'Alors on a~N~\\begin{align}~N~ \\operatorname{Ass}(f_*(\\sh{F}))&\\subset f(X),~N~ \\label{IV.3.1.10.3}\\tag{3.1.10.3}\\\\~N~ \\operatorname{Ass}(f_*(\\sh{F}))&\\subset f(\\operatorname{Ass}(\\sh{F}))~N~ \\quad\\text{si $X$ est localement noethérien}.~N~ \\label{IV.3.1.10.4}\\tag{3.1.10.4}~N~\\end{align}',
    'Alors on a~N~\\begin{equation}~N~ \\operatorname{Ass}(f_*(\\sh{F}))\\subset f(X)~N~ \\label{IV.3.1.10.3}\\tag{3.1.10.3}~N~\\end{equation}~N~et, si $X$ est localement noethérien,~N~\\begin{equation}~N~ \\operatorname{Ass}(f_*(\\sh{F}))\\subset f(\\operatorname{Ass}(\\sh{F})).~N~ \\label{IV.3.1.10.4}\\tag{3.1.10.4}~N~\\end{equation}',
    'Restores the printed wording (the TeX rewrote it) and drops the comma after f(X).')
add(P, 'Remarque (3.1.10.2), "où f\': ..."', "f' : X×_Y Spec(𝒪_{Y,y})→Spec(𝒪_{Y,y}) set in the line", 'displayed', 'other', None, 'high',
    "où~N~\\[~N~ f':X\\times_Y\\operatorname{Spec}(\\sh{O}_{Y,y})~N~ \\longrightarrow\\operatorname{Spec}(\\sh{O}_{Y,y})~N~\\]~N~est déduit",
    "où~N~$f':X\\times_Y\\operatorname{Spec}(\\sh{O}_{Y,y})\\to\\operatorname{Spec}(\\sh{O}_{Y,y})$~N~est déduit", '')
conv2(P, 'Remarque (3.1.10.2)', 'compte tenu de (**I**, 3.6.5)', '(I, 3.6.5)', '(I, 3.6.5)', '(\\textbf{I}, 3.6.5)')
add(P, 'Remarque (3.1.10.2), "de la définition de Ass(𝓕)"', 'Ass(𝓕) (no prime)', "Ass(\\sh{F}') (prime added)", 'symbol', None, 'high',
    "$\\operatorname{Ass}(\\sh{F}')$.", '$\\operatorname{Ass}(\\sh{F})$.', 'Independent of the paragraph-break fix after it.')
add(P, 'Remarque (3.1.10.2), "Par définition"', '"Par définition, il y a" continues the same paragraph (same line)', 'blank line: new paragraph',
    'other', None, 'high', '~N~~N~Par définition, il y a un élément', '~N~Par définition, il y a un élément', '')
add(P, 'Remarque (3.1.10.2), "et par suite (0_I, 1.7.4),"', 'et par suite (0_I, 1.7.4), le support de s (ensemble des x∈X tels que s_x≠0) est contenu dans',
    'et il résulte de (0_I, 1.7.4) que le support de s est contenu dans', 'word', None, 'high',
    'et il résulte de~N~', 'et par suite~N~', 'Rewording in the TeX; goes with the next finding (independent edits).')
add(P, 'Remarque (3.1.10.2), "le support de s (...)"', 'le support de s (ensemble des x∈X tels que s_x≠0) est contenu',
    'que le support de s est contenu (parenthesis missing)', 'missing', None, 'high',
    '1.7.4) que le support de $s$ est contenu', '1.7.4), le support de $s$ (ensemble des $x\\in X$ tels que $s_x\\neq0$) est contenu',
    'Independent of the bold-0 fix on ($0_{\\mathrm I}$, 1.7.4) just before it.')
conv2(P, 'Remarque (3.1.10.2)', '(**0**_I, 1.7.4)', '($0_{\\mathrm I}$, 1.7.4)', '($0_{\\mathrm I}$, 1.7.4)', '($\\mathbf{0}_{\\mathrm I}$, 1.7.4)')
add(P, 'Remarque (3.1.10.2), end', 'mais Ass(𝒪_Xs)⊂Supp(𝒪_Xs)⊂f⁻¹(y) et d\'autre part Ass(𝒪_Xs)⊂Ass(𝓕) (3.1.7), set in the line',
    'one display joining the two inclusions with a comma and \\qquad; "et d\'autre part" missing', 'missing', None, 'high',
    'mais~N~\\[~N~ \\operatorname{Ass}(\\sh{O}_Xs)\\subset~N~ \\operatorname{Supp}(\\sh{O}_Xs)\\subset f^{-1}(y),\\qquad~N~ \\operatorname{Ass}(\\sh{O}_Xs)\\subset\\operatorname{Ass}(\\sh{F})~N~\\]~N~',
    "mais~N~$\\operatorname{Ass}(\\sh{O}_Xs)\\subset\\operatorname{Supp}(\\sh{O}_Xs)\\subset f^{-1}(y)$ et d'autre part~N~$\\operatorname{Ass}(\\sh{O}_Xs)\\subset\\operatorname{Ass}(\\sh{F})$~N~", '')

# ================================================================ PAGE 349
P = 349
add(P, '(3.1.10.5), heading', 'bold "(3.1.10.5)" then the roman text; no "Remarque", no dash', '\\begin{remark}[3.1.10.5] prints "Remarque (3.1.10.5). ---" (italic body)',
    'extra', None, 'high', '\\begin{remark}[3.1.10.5]', '\\begin{env}[3.1.10.5]',
    'Apply together with the next finding (\\end{remark} -> \\end{env}); env (EGA_IV4_FR.tex) prints a bold number and a roman body.')
add(P, '(3.1.10.5), end', '(end of the numbered paragraph)', '\\end{remark}', 'extra', None, 'high',
    '$\\operatorname{Ass}(\\sh{F})\\neq\\varnothing$.~N~\\end{remark}', '$\\operatorname{Ass}(\\sh{F})\\neq\\varnothing$.~N~\\end{env}',
    'Apply together with the previous finding.')
add(P, '(3.1.10.5), "nécessairement ..."', 'nécessairement f(Ass(𝓕))⊂Ass(f_*(𝓕)) : on le voit en prenant (in the line)',
    'displayed formula ending with a full stop, then "On le voit"', 'other', None, 'high',
    'nécessairement~N~\\[~N~ f(\\operatorname{Ass}(\\sh{F}))\\subset~N~ \\operatorname{Ass}(f_*(\\sh{F})).~N~\\]~N~On le voit',
    'nécessairement~N~$f(\\operatorname{Ass}(\\sh{F}))\\subset\\operatorname{Ass}(f_*(\\sh{F}))$ :~N~on le voit', '')
add(P, '(3.1.10.5)', '𝒪_X(—1): long dash', '(-1)', 'convention', 7, 'high', '\\sh{O}_X(-1)', '\\sh{O}_X(\\setmin 1)', '')
add(P, '(3.1.10.5), "alors F=𝒪_X(—1)"', 'roman F (regular weight: stem 6 px like other roman capitals, bold P 9 px) where the script 𝓕 is meant',
    '\\sh{F}', 'misprint_in_print', None, 'high', '$\\sh{F}=', '$F=',
    'The TeX silently corrects. The edit touches only "\\sh{F}" and is independent of the convention-7 edit on (-1). Crop crops_345_349/p349_F_zoom.png.',
    corrected='$\\sh{F}=')
conv2(P, '(3.1.10.5)', '(**III**, 2.1.13)', '(III, 2.1.13)', '(III, 2.1.13)', '(\\textbf{III}, 2.1.13)')
err_head(P, 18)
conv2(P, 'Err_IV 18', 'Après (**IV**, 3.2.8)', '(IV, 3.2.8)', 'Après (IV, 3.2.8)', 'Après (\\textbf{IV}, 3.2.8)')
add(P, 'Remarque (3.2.9), first line', 'Spec(**k**(s))→X', 'k(s)', 'convention', 1, 'high',
    '\\operatorname{Spec}(k(s))\\to X$', '\\operatorname{Spec}(\\boldsymbol{k}(s))\\to X$', 'Residue field k.')
add(P, 'Remarque (3.2.9)', 'Pour tout **k**(s)-module', 'k(s)', 'convention', 1, 'high',
    'Pour tout $k(s)$-module', 'Pour tout $\\boldsymbol{k}(s)$-module', 'Residue field k.')
add(P, 'Remarque (3.2.9)', 'Module sur Spec(**k**(s))', 'k(s)', 'convention', 1, 'high',
    'Module sur $\\operatorname{Spec}(k(s))$', 'Module sur $\\operatorname{Spec}(\\boldsymbol{k}(s))$', 'Residue field k.')
ital(P, 'Remarque (3.2.9)', 'est *irredondant*', 'roman', 'est irredondant.', 'est \\emph{irredondant}.')
ital(P, 'Remarque (3.2.9), second paragraph', 'une partie *discrète*', 'roman', 'une partie discrète', 'une partie \\emph{discrète}')
add(P, 'Remarque (3.2.9), "posons 𝓕(s)=i_s^*(𝓕) qui"', 'no comma after i_s^*(𝓕) (end of line, then "qui est un")', 'comma added', 'punctuation', None, 'high',
    'i_s^*(\\sh{F})$, qui', 'i_s^*(\\sh{F})$ qui', 'The stray raised dot before "posons" in the scan is a printing speck, not reported.')
add(P, 'Remarque (3.2.9)', 'qui est un **k**(s)-module', 'k(s)', 'convention', 1, 'high',
    'un $k(s)$-module;', 'un $\\boldsymbol{k}(s)$-module;', 'Residue field k.')
ital(P, 'Remarque (3.2.9)', 'de longueur *finie*. On a donc', 'roman', 'de longueur~N~finie. On a donc', 'de longueur~N~\\emph{finie}. On a donc')
ital(P, 'Remarque (3.2.9)', 'de 𝒪_X-Modules *cohérents* (puisque', 'roman', 'Modules cohérents (puisque', 'Modules \\emph{cohérents} (puisque')
ital(P, 'Remarque (3.2.9)', 'un homomorphisme *injectif*', 'roman', 'homomorphisme injectif', 'homomorphisme \\emph{injectif}')
add(P, 'Remarque (3.2.9), after the display of v', 'display v : 𝒢 → ⊕(i_s)_*(G(s)) without a full stop, then "et si 𝒢^(s) est l\'image"',
    'full stop in the display, then "Si"', 'word', None, 'high',
    '(i_s)_*(G(s)).~N~\\]~N~Si $\\sh{G}^{(s)}$', '(i_s)_*(G(s))~N~\\]~N~et si $\\sh{G}^{(s)}$', '')
ital(P, 'Remarque (3.2.9)', 'une décomposition *irredondante*, qui est *réduite*', 'roman',
     'décomposition irredondante, qui est~N~réduite lorsque', 'décomposition \\emph{irredondante}, qui est~N~\\emph{réduite} lorsque')
ital(P, 'Remarque (3.2.9)', 'obtenu une *bijection*', 'roman', 'obtenu une bijection', 'obtenu une \\emph{bijection}')
add(P, 'Remarque (3.2.9), the bijection', 'wavy arrow (G(s)_{s∈S}) ⇝ 𝒢', '\\leftrightarrow', 'symbol', None, 'high',
    '\\leftrightarrow\\sh{G}', '\\leadsto\\sh{G}', 'Independent of the misprint edit on the same formula.')
add(P, 'Remarque (3.2.9), the bijection', '(G(s)_{s∈S}): the closing parenthesis after the index', '(G(s))_{s\\in S}', 'misprint_in_print', None, 'medium',
    '~N~$(G(s))_{s\\in S}', '~N~$(G(s)_{s\\in S})',
    'The TeX silently corrects; three lines later the print has the usual (G(s))_{s∈S}. The edit touches only the parenthesis (old is the occurrence that starts a line) and is independent of the arrow edit.',
    corrected='(G(s))_{s\\in S}')
err_head(P, 19)
conv2(P, 'Err_IV 19', 'Dans (**IV**, 4.2.1)', '(IV, 4.2.1)', 'Dans (IV, 4.2.1), avant', 'Dans (\\textbf{IV}, 4.2.1), avant')
add(P, 'display (4.2.1.5)', 'dim(K⊗_kL)=inf(deg.tr_kK, deg.tr_kL) (no full stops after tr, none at the end)',
    '\\operatorname{deg.tr.} twice and a final full stop', 'punctuation', None, 'high',
    '\\inf(\\operatorname{deg.tr.}_kK,\\operatorname{deg.tr.}_kL).', '\\inf(\\operatorname{deg.tr}_kK,\\operatorname{deg.tr}_kL)',
    'deg.tr as in ega4-2 (page-fixed by the IV-2 checkers).')
ital(P, 'Remarque (4.2.1.4)', 'des *cardinaux* quelconques', 'roman', 'des cardinaux quelconques', 'des \\emph{cardinaux} quelconques')
conv2(P, 'Remarque (4.2.1.4)', '(**0**, 16.1.1): bare bold 0', '($0$, 16.1.1)', '($0$, 16.1.1)', '(\\textbf{0}, 16.1.1)')
degtr(P, 'Remarque (4.2.1.4), "Supposons ..."', 'que~N~$\\operatorname{deg.tr.}_kK\\leq\\operatorname{deg.tr.}_kL$ et en premier',
      'que~N~$\\operatorname{deg.tr}_kK\\leq\\operatorname{deg.tr}_kL$ et en premier')
degtr(P, 'Remarque (4.2.1.4), "deg.tr_kK=n<+∞"', '$\\operatorname{deg.tr.}_kK=n<+\\infty$', '$\\operatorname{deg.tr}_kK=n<+\\infty$')
conv2(P, 'Remarque (4.2.1.4)', '(**0**, 16.1.5): bare bold 0', '($0$, 16.1.5)', '($0$, 16.1.5)', '(\\textbf{0}, 16.1.5)')

# ---------------------------------------------------------------- tail of Remarque (4.2.1.4), printed p. 350
T = ' (printed p. 350: text after the true page break, in the page_349 segment until the p. 350 marker moves)'
add(P, 'Remarque (4.2.1.4)' + T, 'k[T₁, …, Tₙ]⊗_kL=L[T₁, …, Tₙ], qui est de dimension n (in the line)', 'displayed', 'other', None, 'high',
    'de~N~\\[~N~ k[T_1,\\ldots,T_n]\\otimes_kL=L[T_1,\\ldots,T_n],~N~\\]~N~qui est de dimension',
    'de~N~$k[T_1,\\ldots,T_n]\\otimes_kL=L[T_1,\\ldots,T_n]$,~N~qui est de dimension',
    'The p. 350 checker may report the same; apply before the p. 350 marker edits below.')
conv2(P, 'Remarque (4.2.1.4)' + T, '(**0**, 16.1.3.1): bare bold 0', '($0$, 16.1.3.1)', '($0$, 16.1.3.1)', '(\\textbf{0}, 16.1.3.1)')
conv2(P, 'Remarque (4.2.1.4)' + T, 'ou encore (**I**, 1.7.4)', '(I, 1.7.4)', 'encore (I, 1.7.4)', 'encore (\\textbf{I}, 1.7.4)')
ital(P, 'Remarque (4.2.1.4)' + T, 'un L-*homomorphisme* u', 'roman', 'existe un $L$-homomorphisme', 'existe un $L$-\\emph{homomorphisme}')
ital(P, 'Remarque (4.2.1.4)' + T, "d'un *k-homomorphisme* v", 'roman', '$k$-homomorphisme $v', '$k$-\\emph{homomorphisme} $v')
degtr(P, 'Remarque (4.2.1.4)' + T, "l'hypothèse~N~$\\operatorname{deg.tr.}_kK\\leq\\operatorname{deg.tr.}_kL$.",
      "l'hypothèse~N~$\\operatorname{deg.tr}_kK\\leq\\operatorname{deg.tr}_kL$.", ' Independent of the paragraph-break fix after it.')
add(P, 'Remarque (4.2.1.4)' + T, '"deg.tr_kL. Si deg.tr_kK⩽..." in the same paragraph (same line)', 'blank line: new paragraph', 'other', None, 'high',
    '_kL$.~N~~N~Si $', '_kL$.~N~Si $', 'Independent of the deg.tr fixes on both sides.')
degtr(P, 'Remarque (4.2.1.4)' + T, 'Si $\\operatorname{deg.tr.}_kK\\leq\\operatorname{deg.tr.}_kL$ et si ces',
      'Si $\\operatorname{deg.tr}_kK\\leq\\operatorname{deg.tr}_kL$ et si ces')
add(P, 'Remarque (4.2.1.4)' + T, 'Spec(L[**t**]): bold upright t', 'L[(t_\\alpha)_{\\alpha\\in I}] (rewritten)', 'formula', None, 'high',
    '\\operatorname{Spec}(L[(t_\\alpha)_{\\alpha\\in I}])', '\\operatorname{Spec}(L[\\mathbf{t}])', 'The TeX rewrote the print\'s L[t].')
add(P, 'Remarque (4.2.1.4)' + T, 'de L[**t**] dans L', 'L[(t_\\alpha)_{\\alpha\\in I}]', 'formula', None, 'high',
    'de $L[(t_\\alpha)_{\\alpha\\in I}]$ dans', 'de $L[\\mathbf{t}]$ dans', '')
add(P, 'Remarque (4.2.1.4)' + T, '(t_α—a_α)_{α∈I}: long dash', 't_\\alpha-a_\\alpha', 'convention', 7, 'high',
    '(t_\\alpha-a_\\alpha)', '(t_\\alpha\\setmin a_\\alpha)', '')
add(P, 'Remarque (4.2.1.4)' + T, "l'anneau local de L[**t**] correspondant", 'L[(t_\\alpha)_{\\alpha\\in I}]', 'formula', None, 'high',
    '$L[(t_\\alpha)_{\\alpha\\in I}]$ correspondant', '$L[\\mathbf{t}]$ correspondant', '')

# ================================================================ MARKERS (apply last, in this order)
add(348, 'marker \\oldpage[IV]{348}, part 1 of 2', 'printed p. 348 begins with (Err_IV, 13)', 'marker before (Err_IV, 3), so Err_IV 3-12 (printed p. 347) sit in the p. 348 segment',
    'marker', None, 'high', '\\paragraph{(Err\\textsubscript{IV}, 13).}',
    '\\oldpage[IV]{348}~N~\\paragraph{($\\mathbf{Err}_{\\mathrm{IV}}$, 13)}',
    'Inserts the marker before Err_IV 13; the same edit carries the heading fixes of Err_IV 13 (light subscript IV, no full stop), which have no separate entry. '
    'Apply with part 2, AFTER all page-348 content edits above (they address Err_IV 3-12 in the current p. 348 segment). GLOBAL_ISSUES 67.')
add(348, 'marker \\oldpage[IV]{348}, part 2 of 2', 'Err_IV 3-12 are on printed p. 347', 'old marker before (Err_IV, 3)',
    'marker', None, 'high', '\\oldpage[IV]{348}~N~\\paragraph{(Err\\textsubscript{IV}, 3).}',
    '\\paragraph{($\\mathbf{Err}_{\\mathrm{IV}}$, 3)}',
    'Deletes the old marker; the same edit carries the heading fixes of Err_IV 3 (no separate entry). Apply with part 1 (either order between the two parts), after the content edits. '
    'The blank line before Err_IV 3 stays: a new entry begins there.')
add(349, 'marker \\oldpage[IV]{350}, part 1 of 2', 'printed p. 349 ends "... est un anneau de fractions de"; p. 350 begins "k[T₁, …, Tₙ]⊗_kL=..."',
    'marker after the end of Remarque (4.2.1.4), before (Err_IV, 20)', 'marker', None, 'high',
    'anneau de fractions~N~de~N~', 'anneau de fractions~N~de~N~\\oldpage[IV]{350}~N~',
    'Mid-sentence break: no blank lines around the marker. Apply after every page-349 edit above (the tail edits address text in the current p. 349 segment). '
    'Boundary with the p. 350 checker, who may report the same move.')
add(350, 'marker \\oldpage[IV]{350}, part 2 of 2', '(Err_IV, 20) is not at the top of p. 350', 'old marker before \\paragraph{(Err\\textsubscript{IV}, 20).}',
    'marker', None, 'high', '\\oldpage[IV]{350}~N~\\paragraph{', '\\paragraph{',
    'Deletes the old marker (it lies in the p. 350 segment; old also matches after a heading fix there). Apply together with part 1. Boundary with the p. 350 checker.')

# ================================================================ checks
def lf(p):
    return p.read_text(encoding='utf-8').replace('\r\n', '\n')

pages = {n: lf(RUN / f'page_{n}.tex') for n in (345, 346, 347, 348, 349, 350)}
ok = True
for i, x in enumerate(F):
    if not x['fix']:
        continue
    c = pages[x['page']].count(x['fix']['old'])
    if c != 1:
        ok = False
        print(f'#{i} page {x["page"]}: old occurs {c} times in page_{x["page"]}.tex: {x["fix"]["old"][:70]!r}')

marker = re.compile(r'\\oldpage\[IV\]\{(\d+)\}')
def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, st) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return st, (cuts[j][1] if j < len(cuts) else len(t))
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None

def simulate(t, skip_misprints, label):
    good = True
    for i, x in enumerate(F):
        if not x['fix'] or (skip_misprints and x['kind'] == 'misprint_in_print'):
            continue
        st, en = locate(t, x['page'])
        seg = t[st:en]
        c = seg.count(x['fix']['old'])
        if c != 1:
            good = False
            print(f'[{label}] #{i} page {x["page"]}: old occurs {c} times in segment: {x["fix"]["old"][:70]!r}')
            continue
        t = t[:st] + seg.replace(x['fix']['old'], x['fix']['new']) + t[en:]
    return good, t

g1, t_dip = simulate(lf(SRC), False, 'diplomatic')
g2, t_cur = simulate(lf(CUR), True, 'corrected')
ok = ok and g1 and g2
# segments after the moves
for n in (347, 348, 349, 350):
    st, en = locate(t_dip, n)
    seg = t_dip[st:en]
    print(n, 'starts:', seg[:90].replace('\n', ' | '))
    print('   ends:', seg[-90:].replace('\n', ' | '))
print('remaining deg.tr. in pp. 345-350 segment:', t_dip[:locate(t_dip, 351)[0]].count('deg.tr.'))
print('findings:', len(F), 'checks ok' if ok else 'CHECK FAILURES')
json.dump(F, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
(RUN / 'crops_345_349' / 'simulated_after_fixes_345_350.txt').write_text(t_dip[locate(t_dip, 345)[0]:locate(t_dip, 351)[0]], encoding='utf-8')
