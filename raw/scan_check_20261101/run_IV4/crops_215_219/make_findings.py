import json, sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
BASE = r'user\Documents\ega_scan_check_20261101\run_IV4'
OUT = BASE + r'\findings_215_219.json'

def N(s):
    return None if s is None else s.replace('¶', '\n')

F = []
def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, after=None):
    e = {'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind,
         'convention': conv, 'confidence': conf,
         'fix': None if old is None else {'old': N(old), 'new': N(new)}}
    if kind == 'misprint_in_print':
        e['corrected'] = N(corrected)
    e['note'] = note
    e['_after'] = after
    F.append(e)
    return len(F) - 1

K63 = ('Wrong letter (GLOBAL_ISSUES 63): Fraktur K in the print (crossbar and descending leg, no closed bowl; '
       'the same glyph as the Fraktur K of p. 197, crop p197_frakK_a.png), written \\mathfrak R in the TeX.')

# ---------------------------------------------------------------- page 215
add(215, "l. 1: 'par récurrence sur m'", "'récurrence sur m' italic", "'récurrence sur' upright", 'italics', None, 'high',
    r'par récurrence sur $m$, supposant', r'par \emph{récurrence sur} $m$, supposant', '')
add(215, "(*_d): R∩(𝔎^mN+𝔏^{m+1}N)⊂(R∩𝔎^dN∩𝔏^mN)+𝔏^{m+1}N", "Fraktur K twice (enlarged crop)", "\\mathfrak R twice", 'symbol', None, 'high',
    r'R\cap(\mathfrak R^mN+\mathfrak L^{m+1}N)\subset(R\cap\mathfrak R^dN\cap\mathfrak L^mN)+\mathfrak L^{m+1}N.',
    r'R\cap(\mathfrak K^mN+\mathfrak L^{m+1}N)\subset(R\cap\mathfrak K^dN\cap\mathfrak L^mN)+\mathfrak L^{m+1}N.',
    K63 + ' Of the 136 \\mathfrak R on pp. 215-219, 134 are this K (one edit per formula below); the two gr^d subscripts of p. 217 are Fraktur L (separate findings).')
add(215, "l. 5: 'par récurrence sur d'", "'récurrence sur d' italic", "upright", 'italics', None, 'high',
    r'par récurrence sur $d$;', r'par \emph{récurrence sur} $d$;', '')
add(215, "(*_{d+1})", "Fraktur K twice", "\\mathfrak R twice", 'symbol', None, 'high',
    r'R\cap(\mathfrak R^mN+\mathfrak L^{m+1}N)\subset(R\cap\mathfrak R^{d+1}N\cap\mathfrak L^mN)+\mathfrak L^{m+1}N.',
    r'R\cap(\mathfrak K^mN+\mathfrak L^{m+1}N)\subset(R\cap\mathfrak K^{d+1}N\cap\mathfrak L^mN)+\mathfrak L^{m+1}N.',
    'Wrong letter (GLOBAL_ISSUES 63), as in (*_d).')
add(215, "(**_{d+1,h}), first part", "Fraktur K three times", "\\mathfrak R three times", 'symbol', None, 'high',
    r'R\cap(\mathfrak R^mN+\mathfrak L^{m+1}N)\subset(R\cap(\mathfrak R^{d+1}N+\mathfrak R^d\mathfrak L^hN)',
    r'R\cap(\mathfrak K^mN+\mathfrak L^{m+1}N)\subset(R\cap(\mathfrak K^{d+1}N+\mathfrak K^d\mathfrak L^hN)',
    'Wrong letter (GLOBAL_ISSUES 63).')
add(215, "end of (**_{d+1,h})", "no full stop after ...+𝔏^{m+1}N (enlarged crop); (*_d) and (*_{d+1}) have one", "full stop", 'punctuation', None, 'high',
    r'N.¶  \tag{$**_{d+1,h}$}', r'N¶  \tag{$**_{d+1,h}$}', '')
add(215, "l. after (**): 'par récurrence sur h'", "'récurrence' (end of line) and 'sur h' italic", "upright", 'italics', None, 'high',
    r'par récurrence sur $h$ que', r'par \emph{récurrence sur} $h$ que', '')
add(215, "same sentence: 'pour tout h≥0'", "'tout' italic", "upright", 'italics', None, 'high',
    r'est vraie pour tout $h\geq0$. Mais', r'est vraie pour \emph{tout} $h\geq0$. Mais', '')
add(215, "Lemme (19.7.1.7): 'tel que E∩(F+𝔏^hN)⊂(E∩F)+𝔏^kN.'", "the formula is in the running text (third line of the lemma, flush left)", "displayed with \\[ \\]", 'other', None, 'high',
    r'tel que¶\[¶  E\cap(F+\mathfrak L^hN)\subset(E\cap F)+\mathfrak L^kN.¶\]¶\end{lemma}',
    r'tel que $E\cap(F+\mathfrak L^hN)\subset(E\cap F)+\mathfrak L^kN$.¶\end{lemma}',
    'Layout: display where the print sets the formula inline; no words change.')
add(215, "proof of (19.7.1.7): '(0_I, 7.3.2)'", "bold 0 with subscript I", "plain 0", 'convention', 2, 'high',
    r'($0_{\mathrm I}$, 7.3.2)', r'($\mathbf{0}_{\mathrm I}$, 7.3.2)', '')
add(215, "proof of (19.7.1.7): 'x_1—y_1∈𝔏^hN_1'", "long dash", "minus sign", 'convention', 7, 'high',
    r'$x_1-y_1\in', r'$x_1\setmin y_1\in', 'GLOBAL_ISSUES 23 (long dash used for subtraction); \\setmin pending the convention-7 decision.')
add(215, "'F=𝔎^{d+1}N'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'$F=\mathfrak R^{d+1}N$', r'$F=\mathfrak K^{d+1}N$', 'Wrong letter (GLOBAL_ISSUES 63).')
add(215, "'que (**_{d+1,h}) est vérifiée.'", "'est vérifiée' italic", "upright", 'italics', None, 'high',
    r'$(**_{d+1,h})$ est vérifiée.', r'$(**_{d+1,h})$ \emph{est vérifiée}.', '')
add(215, "(19.7.1.8) 'Démonstration de (**_{d+1,h+1}) : Premier cas : h≤m—d.'", "'Démonstration de' and 'Premier cas' italic", "upright (env body is roman)", 'italics', None, 'high',
    r'Démonstration de $(**_{d+1,h+1})$: Premier cas:', r'\emph{Démonstration de} $(**_{d+1,h+1})$: \emph{Premier cas}:', '')
add(215, "(19.7.1.8): 'h≤m—d'", "long dash", "minus sign", 'convention', 7, 'high',
    r'$h\leq m-d$.¶\end{env}', r'$h\leq m\setmin d$.¶\end{env}', 'GLOBAL_ISSUES 23.')
add(215, "(19.7.1.9)", "Fraktur K twice", "\\mathfrak R twice", 'symbol', None, 'high',
    r'g\in R\cap(\mathfrak R^{d+1}N+\mathfrak R^d\mathfrak L^hN)\cap\mathfrak L^mN',
    r'g\in R\cap(\mathfrak K^{d+1}N+\mathfrak K^d\mathfrak L^hN)\cap\mathfrak L^mN', 'Wrong letter (GLOBAL_ISSUES 63).')
add(215, "'g_1∈R∩(𝔎^mN+𝔏^{m+1}N)'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'$g_1\in R\cap(\mathfrak R^mN+\mathfrak L^{m+1}N)$', r'$g_1\in R\cap(\mathfrak K^mN+\mathfrak L^{m+1}N)$', 'Wrong letter (GLOBAL_ISSUES 63).')
add(215, "(19.7.1.10)", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'g\in\mathfrak R^mN+\mathfrak L^{m+1}N.', r'g\in\mathfrak K^mN+\mathfrak L^{m+1}N.', 'Wrong letter (GLOBAL_ISSUES 63).')
add(215, "'à un élément g_2∈R∩(𝔎^{d+1}N+𝔎^d𝔏^{h+1}N), car'", "the formula is a centred display ending with a comma; 'car cela entraînera' starts the next line flush left", "inline", 'other', None, 'high',
    r'à un élément $g_2\in R\cap(\mathfrak R^{d+1}N+\mathfrak R^d\mathfrak L^{h+1}N)$, car cela entraînera',
    r'à un élément¶\[¶  g_2\in R\cap(\mathfrak K^{d+1}N+\mathfrak K^d\mathfrak L^{h+1}N),¶\]¶car cela entraînera',
    'Display where the TeX has the formula inline; no words differ. The edit also writes the two Fraktur K of this formula (GLOBAL_ISSUES 63).')
add(215, "'g_2—g∈𝔏^{m+1}N'", "long dash", "minus sign", 'convention', 7, 'high',
    r'$g_2-g\in', r'$g_2\setmin g\in', 'GLOBAL_ISSUES 23.')
add(215, "'Dans le cas h≤m—d que nous considérons'", "long dash", "minus sign", 'convention', 7, 'high',
    r'$h\leq m-d$ que', r'$h\leq m\setmin d$ que', 'GLOBAL_ISSUES 23. The minus signs in exponents (𝔏^{m-d+1}) are short minus signs in the print, as in the TeX.')
add(215, "(19.7.1.11)", "Fraktur K four times", "\\mathfrak R four times", 'symbol', None, 'high',
    r'(\mathfrak R^mN+\mathfrak L^{m+1}N)\cap\mathfrak R^dN\subset\mathfrak L^{m-d+1}\mathfrak R^dN+\mathfrak R',
    r'(\mathfrak K^mN+\mathfrak L^{m+1}N)\cap\mathfrak K^dN\subset\mathfrak L^{m-d+1}\mathfrak K^dN+\mathfrak K',
    "Wrong letter (GLOBAL_ISSUES 63). The 'old' stops at the last \\mathfrak R (before '^{d+1}N.'), so it does not overlap the next edit.")
i215p = add(215, "end of (19.7.1.11), last line of p. 215", "no full stop: the sentence goes on at the top of p. 216 ('car les relations ...'); enlarged crop", "full stop; blank line before \\oldpage[IV-4]{216}", 'punctuation', None, 'high',
    r'^{d+1}N.¶\]¶\end{env}¶¶', r'^{d+1}N¶\]¶\end{env}¶',
    'Removes the full stop and also the blank line at the end of the p. 215 segment (part 1 of 2 of the 215/216 boundary fix, see the next finding). Applies after the Fraktur edit above (no overlap).')
add(215, "page break 215/216", "p. 216 continues the sentence of (19.7.1.11) ('car les relations ...', flush left)", "blank lines before and after \\oldpage[IV-4]{216}", 'marker', None, 'medium', None, None,
    'BOUNDARY FIX 215/216: the marker is at the right place; the blank line before it is removed by the preceding punctuation edit (part 1), the one after it by the first p. 216 finding (part 2). The output does not change (\\end{env} already ends the paragraph); the source then follows the mid-sentence rule.')

# ---------------------------------------------------------------- page 216
add(216, "top of p. 216 (page break 215/216)", "'car les relations ...' continues the sentence of (19.7.1.11)", "blank line after \\oldpage[IV-4]{216}", 'marker', None, 'medium',
    r'\oldpage[IV-4]{216}¶¶car les relations', r'\oldpage[IV-4]{216}¶car les relations',
    'BOUNDARY FIX (page break 215/216), part 2 of 2 with the last p. 215 punctuation edit (which removes the blank line before the marker). Output unchanged (\\end{env} already ends the paragraph).')
add(216, "l. 2: 'comme h≤m—d'", "long dash", "minus sign", 'convention', 7, 'high',
    r'$h\leq m-d$, on a', r'$h\leq m\setmin d$, on a', 'GLOBAL_ISSUES 23.')
add(216, "l. 3: '𝔎^mN⊂𝔎^dN'", "Fraktur K twice", "\\mathfrak R twice", 'symbol', None, 'high',
    r'$\mathfrak R^mN\subset\mathfrak R^dN$', r'$\mathfrak K^mN\subset\mathfrak K^dN$', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "(19.7.1.12)", "Fraktur K twice", "\\mathfrak R twice", 'symbol', None, 'high',
    r'\mathfrak L^{m+1}N\cap\mathfrak R^dN\subset\mathfrak L^{m-d+1}\mathfrak R^dN',
    r'\mathfrak L^{m+1}N\cap\mathfrak K^dN\subset\mathfrak L^{m-d+1}\mathfrak K^dN', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "(19.7.1.13)", "Fraktur K twice", "\\mathfrak R twice", 'symbol', None, 'high',
    r'\mathfrak L^{m+1}\cap\mathfrak R^d\subset\mathfrak L^{m-d+1}\mathfrak R^d.',
    r'\mathfrak L^{m+1}\cap\mathfrak K^d\subset\mathfrak L^{m-d+1}\mathfrak K^d.', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "(19.7.1.14)", "Fraktur K three times", "\\mathfrak R three times", 'symbol', None, 'high',
    r'\mathfrak L^{m+1}\cap\mathfrak R^d\subset\mathfrak L^{m-d+1}\mathfrak R^d+\mathfrak R^{d+1}.',
    r'\mathfrak L^{m+1}\cap\mathfrak K^d\subset\mathfrak L^{m-d+1}\mathfrak K^d+\mathfrak K^{d+1}.', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "'comme 𝔎⊂𝔏, donc 𝔏^{m-d+1}𝔎^d⊂𝔏^{m+1}'", "Fraktur K twice", "\\mathfrak R twice", 'symbol', None, 'high',
    r'$\mathfrak R\subset\mathfrak L$, donc $\mathfrak L^{m-d+1}\mathfrak R^d\subset',
    r'$\mathfrak K\subset\mathfrak L$, donc $\mathfrak L^{m-d+1}\mathfrak K^d\subset', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "display after 'entraînera'", "Fraktur K three times", "\\mathfrak R three times", 'symbol', None, 'high',
    r'\mathfrak L^{m+1}\cap\mathfrak R^d\subset\mathfrak L^{m-d+1}\mathfrak R^d+\mathfrak L^{m+1}\cap\mathfrak R^{d+1}',
    r'\mathfrak L^{m+1}\cap\mathfrak K^d\subset\mathfrak L^{m-d+1}\mathfrak K^d+\mathfrak L^{m+1}\cap\mathfrak K^{d+1}', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "'et par récurrence sur d<m, on en conclura'", "d<m (strict; enlarged crop)", "d\\leq m", 'formula', None, 'high',
    r'par récurrence sur $d\leq m$, on', r'par récurrence sur $d<m$, on',
    'The printed d<m matches (19.7.1.14), stated just before for d<m; not a misprint.')
add(216, "display after 'on en conclura'", "Fraktur K three times", "\\mathfrak R three times", 'symbol', None, 'high',
    r'\mathfrak L^{m+1}\cap\mathfrak R^d\subset\mathfrak L^{m-d+1}\mathfrak R^d+\mathfrak R^{m+1}¶\]',
    r'\mathfrak L^{m+1}\cap\mathfrak K^d\subset\mathfrak L^{m-d+1}\mathfrak K^d+\mathfrak K^{m+1}¶\]', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "'puisque 𝔎^{m+1}⊂𝔏^{m-d+1}𝔎^d'", "Fraktur K twice", "\\mathfrak R twice", 'symbol', None, 'high',
    r'$\mathfrak R^{m+1}\subset\mathfrak L^{m-d+1}\mathfrak R^d$', r'$\mathfrak K^{m+1}\subset\mathfrak L^{m-d+1}\mathfrak K^d$', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "'Comme 𝔏=𝔍+𝔎'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'$\mathfrak L=\mathfrak J+\mathfrak R$', r'$\mathfrak L=\mathfrak J+\mathfrak K$', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "(19.7.1.15), first line", "Fraktur K four times; '+ . . . +' with baseline dots (4x crop: dots at the baseline, below the bar of +)", "\\mathfrak R; \\cdots", 'symbol', None, 'high',
    r'\label{IV.19.7.1.15}¶\[¶\begin{aligned}¶  &(\mathfrak J^{m+1}+\mathfrak J^m\mathfrak R+\cdots+\mathfrak J\mathfrak R^m+\mathfrak R^{m+1})\cap\mathfrak R^d',
    r'\label{IV.19.7.1.15}¶\[¶\begin{aligned}¶  &(\mathfrak J^{m+1}+\mathfrak J^m\mathfrak K+\ldots+\mathfrak J\mathfrak K^m+\mathfrak K^{m+1})\cap\mathfrak K^d',
    'Wrong letter (GLOBAL_ISSUES 63) and baseline dots (\\cdots -> \\ldots, as on p. 172). The label is in the old only to make it unique ((19.7.1.17) has the same first line).')
add(216, "(19.7.1.15), end of the first line", "the print repeats ⊂ at the end of the first line and at the start of the second", "⊂ only at the start of the second line", 'missing', None, 'medium',
    r'\\¶  &\quad\subset\mathfrak J^{m-d+1}', r'\subset\\¶  &\quad\subset\mathfrak J^{m-d+1}',
    'The print repeats the relation sign at the break of the display; the TeX breaks at the same place but gives the sign once. Same document-wide question as run_III2 p. 169 (whether such reprises are reproduced).')
add(216, "(19.7.1.15), second and third lines", "Fraktur K seven times; baseline dots", "\\mathfrak R; \\cdots", 'symbol', None, 'high',
    r'\mathfrak R^d+\mathfrak J^{m-d}\mathfrak R^{d+1}+\cdots+\mathfrak J\mathfrak R^m+\mathfrak R^{m+1}+\mathfrak R^{d+1}\\¶  &\quad=\mathfrak J^{m-d+1}\mathfrak R^d+\mathfrak R^{d+1}.',
    r'\mathfrak K^d+\mathfrak J^{m-d}\mathfrak K^{d+1}+\ldots+\mathfrak J\mathfrak K^m+\mathfrak K^{m+1}+\mathfrak K^{d+1}\\¶  &\quad=\mathfrak J^{m-d+1}\mathfrak K^d+\mathfrak K^{d+1}.',
    'Wrong letter (GLOBAL_ISSUES 63) and baseline dots.')
add(216, "(19.7.1.16)", "Fraktur K three times", "\\mathfrak R three times", 'symbol', None, 'high',
    r'\mathfrak R^a\mathfrak J^b\cap\mathfrak R^{a+1}\subset\mathfrak R^{a+1}\mathfrak J^{b-1}',
    r'\mathfrak K^a\mathfrak J^b\cap\mathfrak K^{a+1}\subset\mathfrak K^{a+1}\mathfrak J^{b-1}', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "(19.7.1.17), first line", "Fraktur K four times; baseline dots", "\\mathfrak R; \\cdots", 'symbol', None, 'high',
    r'\label{IV.19.7.1.17}¶\[¶\begin{aligned}¶  &(\mathfrak J^{m+1}+\mathfrak J^m\mathfrak R+\cdots+\mathfrak J\mathfrak R^m+\mathfrak R^{m+1})\cap\mathfrak R^d',
    r'\label{IV.19.7.1.17}¶\[¶\begin{aligned}¶  &(\mathfrak J^{m+1}+\mathfrak J^m\mathfrak K+\ldots+\mathfrak J\mathfrak K^m+\mathfrak K^{m+1})\cap\mathfrak K^d',
    'Wrong letter (GLOBAL_ISSUES 63) and baseline dots.')
add(216, "(19.7.1.17), end of the first line", "⊂ repeated at the end of the first line", "⊂ only at the start of the second line", 'missing', None, 'medium',
    r'\\¶  &\quad\subset(\mathfrak J^{m+1-q}', r'\subset\\¶  &\quad\subset(\mathfrak J^{m+1-q}',
    'As for (19.7.1.15): reprise of the relation sign at the break of the display (document-wide question).')
add(216, "(19.7.1.17), second line", "Fraktur K four times; baseline dots", "\\mathfrak R; \\cdots", 'symbol', None, 'high',
    r'\mathfrak R^q+\mathfrak J^{m-q}\mathfrak R^{q+1}+\cdots+\mathfrak R^{m+1})\cap\mathfrak R^d¶\end{aligned}',
    r'\mathfrak K^q+\mathfrak J^{m-q}\mathfrak K^{q+1}+\ldots+\mathfrak K^{m+1})\cap\mathfrak K^d¶\end{aligned}',
    'Wrong letter (GLOBAL_ISSUES 63) and baseline dots.')
add(216, "'y∈𝔍^{m+1-q}𝔎^q'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'$y\in\mathfrak J^{m+1-q}\mathfrak R^q$', r'$y\in\mathfrak J^{m+1-q}\mathfrak K^q$', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "'z∈𝔍^{m-q}𝔎^{q+1}+...+𝔎^{m+1}'", "Fraktur K twice; baseline dots", "\\mathfrak R; \\cdots", 'symbol', None, 'high',
    r'$z\in\mathfrak J^{m-q}\mathfrak R^{q+1}+\cdots+\mathfrak R^{m+1}$;', r'$z\in\mathfrak J^{m-q}\mathfrak K^{q+1}+\ldots+\mathfrak K^{m+1}$;',
    'Wrong letter (GLOBAL_ISSUES 63) and baseline dots.')
add(216, "'comme y+z∈𝔎^d⊂𝔎^{q+1}'", "Fraktur K twice", "\\mathfrak R twice", 'symbol', None, 'high',
    r'$y+z\in\mathfrak R^d\subset\mathfrak R^{q+1}$', r'$y+z\in\mathfrak K^d\subset\mathfrak K^{q+1}$', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "'on en déduit y∈𝔎^{q+1}'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'$y\in\mathfrak R^{q+1}$', r'$y\in\mathfrak K^{q+1}$', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "'puisque z∈𝔎^{q+1}'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'$z\in\mathfrak R^{q+1}$;', r'$z\in\mathfrak K^{q+1}$;', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "'on a y∈𝔍^{m-q}𝔎^{q+1}'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'$y\in\mathfrak J^{m-q}\mathfrak R^{q+1}$', r'$y\in\mathfrak J^{m-q}\mathfrak K^{q+1}$', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "display 'y+z∈... , et y+z∈𝔎^d'", "Fraktur K three times; baseline dots", "\\mathfrak R; \\cdots", 'symbol', None, 'high',
    r'y+z\in\mathfrak J^{m-q}\mathfrak R^{q+1}+\cdots+\mathfrak R^{m+1},\qquad\text{et}\qquad y+z\in\mathfrak R^d',
    r'y+z\in\mathfrak J^{m-q}\mathfrak K^{q+1}+\ldots+\mathfrak K^{m+1},\qquad\text{et}\qquad y+z\in\mathfrak K^d',
    'Wrong letter (GLOBAL_ISSUES 63) and baseline dots.')
add(216, "'s'écrit a_1f_1+...+a_nf_n'", "baseline dots", "\\cdots", 'symbol', None, 'high',
    r'$a_1f_1+\cdots+a_nf_n$, où', r'$a_1f_1+\ldots+a_nf_n$, où', '')
add(216, "'appartiennent à 𝔎^a𝔍^{b-1}'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'$\mathfrak R^a\mathfrak J^{b-1}$;', r'$\mathfrak K^a\mathfrak J^{b-1}$;', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "'(𝔎^a/𝔎^{a+1})-régulière'", "Fraktur K twice", "\\mathfrak R twice", 'symbol', None, 'high',
    r'$(\mathfrak R^a/\mathfrak R^{a+1})$-régulière', r'$(\mathfrak K^a/\mathfrak K^{a+1})$-régulière', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "'(𝔎^a/𝔎^{a+1})-quasi-régulière'", "Fraktur K twice", "\\mathfrak R twice", 'symbol', None, 'high',
    r'$(\mathfrak R^a/\mathfrak R^{a+1})$-quasi-régulière', r'$(\mathfrak K^a/\mathfrak K^{a+1})$-quasi-régulière', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "'(0, 15.1.9)'", "bold 0 (no subscript)", "plain 0", 'convention', 2, 'high',
    r'($0$, 15.1.9)', r'(\textbf{0}, 15.1.9)', '')
add(216, "'(0, 15.1.7)'", "bold 0 (no subscript)", "plain 0", 'convention', 2, 'high',
    r'($0$, 15.1.7)', r'(\textbf{0}, 15.1.7)', '')
add(216, "'la relation a_1f_1+...+a_nf_n∈𝔎^{a+1}'", "baseline dots; Fraktur K", "\\cdots; \\mathfrak R", 'symbol', None, 'high',
    r'$a_1f_1+\cdots+a_nf_n\in\mathfrak R^{a+1}$', r'$a_1f_1+\ldots+a_nf_n\in\mathfrak K^{a+1}$', 'Baseline dots and wrong letter (GLOBAL_ISSUES 63).')
add(216, "'où les a_i∈𝔎^a'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'$a_i\in\mathfrak R^a$,', r'$a_i\in\mathfrak K^a$,', 'Wrong letter (GLOBAL_ISSUES 63). The heavier subscript i of several a_i is small-type weight (most subscript i of pp. 216-219 look so), not reported.')
add(216, "'nécessairement a_i∈𝔎^{a+1}'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'$a_i\in\mathfrak R^{a+1}$, donc', r'$a_i\in\mathfrak K^{a+1}$, donc', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "'donc a_i∈𝔎^a𝔍^{b-1}∩𝔎^{a+1}'", "Fraktur K twice", "\\mathfrak R twice", 'symbol', None, 'high',
    r'$a_i\in\mathfrak R^a\mathfrak J^{b-1}\cap\mathfrak R^{a+1}$', r'$a_i\in\mathfrak K^a\mathfrak J^{b-1}\cap\mathfrak K^{a+1}$', 'Wrong letter (GLOBAL_ISSUES 63).')
add(216, "last line of p. 216: 'il suffit de raisonner par' | p. 217 'récurrence sur b'", "page break mid-sentence; p. 217 begins flush left", "blank line before \\oldpage[IV-4]{217}", 'marker', None, 'high',
    r'raisonner par¶¶', r'raisonner par¶',
    'The marker is at the right place. Part 1 of 2: the first p. 217 finding removes the blank line after \\oldpage[IV-4]{217}; apply both (\\oldpage ends with \\ignorespaces, which does not skip a \\par).')

# ---------------------------------------------------------------- page 217
add(217, "top of p. 217: 'récurrence sur b'", "continues the sentence of p. 216", "blank line after \\oldpage[IV-4]{217}", 'marker', None, 'high',
    r'\oldpage[IV-4]{217}¶¶récurrence', r'\oldpage[IV-4]{217}¶récurrence',
    'Part 2 of 2 with the last p. 216 finding; both blank lines must go.')
add(217, "l. 2: 'pour h≤m—d.'", "long dash", "minus sign", 'convention', 7, 'high',
    r'$h\leq m-d$.', r'$h\leq m\setmin d$.', 'GLOBAL_ISSUES 23.')
add(217, "(19.7.1.18) 'Démonstration de (**_{d+1,h+1}); Deuxième cas : h>m—d.'", "'Démonstration de' and 'Deuxième cas' italic", "upright (env body is roman)", 'italics', None, 'high',
    r'Démonstration de $(**_{d+1,h+1})$; Deuxième cas:', r'\emph{Démonstration de} $(**_{d+1,h+1})$; \emph{Deuxième cas}:', '')
add(217, "(19.7.1.18): 'h>m—d'", "long dash", "minus sign", 'convention', 7, 'high',
    r'$h>m-d$.', r'$h>m\setmin d$.', 'GLOBAL_ISSUES 23.')
add(217, "'pour tout h≥0, on a'", "'tout' italic", "upright", 'italics', None, 'high',
    r'pour tout $h\geq0$, on a', r'pour \emph{tout} $h\geq0$, on a', '')
i19 = add(217, "(19.7.1.19): '⊂𝔏^h(R∩𝔎^dN)'", "Fraktur L: 𝔏^h(R∩𝔎^dN), the same glyph as the 𝔏^{h+1} that follows (4x crop)", "\\mathfrak J^h(R\\cap\\mathfrak R^dN)", 'symbol', None, 'high',
    r'R\cap(\mathfrak R^{d+1}N+\mathfrak R^d\mathfrak L^hN)\subset\mathfrak J^h(R\cap\mathfrak R^dN)+\mathfrak L^{h+1}\mathfrak R^dN+\mathfrak R^{d+1}N.',
    r'R\cap(\mathfrak K^{d+1}N+\mathfrak K^d\mathfrak L^hN)\subset\mathfrak L^h(R\cap\mathfrak K^dN)+\mathfrak L^{h+1}\mathfrak K^dN+\mathfrak K^{d+1}N.',
    "Wrong letter: the print has 𝔏^h, also in 't∈𝔏^h(R∩𝔎^dN)' on p. 218 (the TeX has \\mathfrak J^h in both). Not a misprint: the proof ends 'et comme 𝔍⊂𝔏, cela prouve (19.7.1.19)', and p. 218 uses t∈𝔏^h(...) with h≥m-d+1 to get t∈𝔏^{m+1}N. The edit also writes the five Fraktur K of (19.7.1.19) (GLOBAL_ISSUES 63).")
add(217, "'𝔎^{d+1}N+𝔎^d𝔏^hN=𝔎^{d+1}N+𝔎^d𝔍^hN'", "Fraktur K four times", "\\mathfrak R four times", 'symbol', None, 'high',
    r'$\mathfrak R^{d+1}N+\mathfrak R^d\mathfrak L^hN=\mathfrak R^{d+1}N+\mathfrak R^d\mathfrak J^hN$',
    r'$\mathfrak K^{d+1}N+\mathfrak K^d\mathfrak L^hN=\mathfrak K^{d+1}N+\mathfrak K^d\mathfrak J^hN$', 'Wrong letter (GLOBAL_ISSUES 63).')
add(217, "'puisque 𝔏=𝔎+𝔍'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'$\mathfrak L=\mathfrak R+\mathfrak J$', r'$\mathfrak L=\mathfrak K+\mathfrak J$', 'Wrong letter (GLOBAL_ISSUES 63).')
add(217, "'gr^h_𝔍(gr^d_𝔎(N))'", "Fraktur K subscript (5x crop)", "\\mathfrak R", 'symbol', None, 'high',
    r'\operatorname{gr}_{\mathfrak J}^h(\operatorname{gr}_{\mathfrak R}^d(N))', r'\operatorname{gr}_{\mathfrak J}^h(\operatorname{gr}_{\mathfrak K}^d(N))', 'Wrong letter (GLOBAL_ISSUES 63).')
add(217, "'𝔭=𝔯/𝔎∈Ass_{A/𝔎}(A/𝔏)'", "Fraktur K twice (2x crop)", "\\mathfrak R twice", 'symbol', None, 'high',
    r'\mathfrak r/\mathfrak R\in\operatorname{Ass}_{A/\mathfrak R}(A/\mathfrak L)', r'\mathfrak r/\mathfrak K\in\operatorname{Ass}_{A/\mathfrak K}(A/\mathfrak L)', 'Wrong letter (GLOBAL_ISSUES 63).')
add(217, "'z appartient à R∩(𝔎^dN+𝔏^{d+1}N)'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'$R\cap(\mathfrak R^dN+\mathfrak L^{d+1}N)$', r'$R\cap(\mathfrak K^dN+\mathfrak L^{d+1}N)$', 'Wrong letter (GLOBAL_ISSUES 63).')
add(217, "'(R_𝔯∩𝔎_𝔯^dN_𝔯)+𝔏_𝔯^{d+1}N_𝔯'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'(R_{\mathfrak r}\cap\mathfrak R_{\mathfrak r}^dN_{\mathfrak r})', r'(R_{\mathfrak r}\cap\mathfrak K_{\mathfrak r}^dN_{\mathfrak r})', 'Wrong letter (GLOBAL_ISSUES 63).')
add(217, "'l'image z̄/1 de z̄ dans gr^•_{𝔏_𝔯}(N_𝔯)'", "gr with a raised bullet (4x crop)", "^{h+d}", 'symbol', None, 'high',
    r'\operatorname{gr}_{\mathfrak L_{\mathfrak r}}^{h+d}(N_{\mathfrak r})', r'\operatorname{gr}_{\mathfrak L_{\mathfrak r}}^\bullet(N_{\mathfrak r})',
    "The TeX writes ^{h+d} for the print's raised bullet at 9 places of this paragraph: here, in the three displays of the next three findings (their edits include it) and in 'gr^•_𝔏(N)→gr^•_𝔏(M)'. The print has h+d only in the sentence before (19.7.1.20) and in (19.7.1.20).")
add(217, "'appartient à gr^•_{𝔏_𝔯}(R_𝔯, N_𝔯)=(gr^•_𝔏(R, N))_𝔯=(gr^•_𝔏(R, N))_𝔮, où 𝔮=𝔯/𝔏'", "in the running text, with raised bullets", "displayed, with ^{h+d}", 'other', None, 'high',
    r'appartient à¶\[¶  \operatorname{gr}_{\mathfrak L_{\mathfrak r}}^{h+d}(R_{\mathfrak r},N_{\mathfrak r})¶  =(\operatorname{gr}_{\mathfrak L}^{h+d}(R,N))_{\mathfrak r}¶  =(\operatorname{gr}_{\mathfrak L}^{h+d}(R,N))_{\mathfrak q},¶\]¶où',
    r'appartient à $\operatorname{gr}_{\mathfrak L_{\mathfrak r}}^\bullet(R_{\mathfrak r},N_{\mathfrak r})=(\operatorname{gr}_{\mathfrak L}^\bullet(R,N))_{\mathfrak r}=(\operatorname{gr}_{\mathfrak L}^\bullet(R,N))_{\mathfrak q}$, où',
    'Layout (display where the print sets the formula inline) and the three bullets (TeX ^{h+d}, see the previous finding).')
add(217, "'l'application canonique (gr^•_𝔏(N))_𝔮→(gr^•_𝔏(M))_𝔮 est nulle'", "in the running text, with raised bullets", "displayed, with ^{h+d}", 'other', None, 'high',
    r"l'application canonique¶\[¶  (\operatorname{gr}_{\mathfrak L}^{h+d}(N))_{\mathfrak q}\longrightarrow(\operatorname{gr}_{\mathfrak L}^{h+d}(M))_{\mathfrak q}¶\]¶est nulle",
    r"l'application canonique $(\operatorname{gr}_{\mathfrak L}^\bullet(N))_{\mathfrak q}\longrightarrow(\operatorname{gr}_{\mathfrak L}^\bullet(M))_{\mathfrak q}$ est nulle",
    'Layout and two bullets (TeX ^{h+d}).')
add(217, "'que Ass_{A/𝔏}(gr^•_𝔏(M))⊂Ass_{A/𝔏}(A/𝔏), on en déduit'", "in the running text, with a raised bullet", "displayed, with ^{h+d}", 'other', None, 'high',
    r'que¶\[¶  \operatorname{Ass}_{A/\mathfrak L}(\operatorname{gr}_{\mathfrak L}^{h+d}(M))\subset\operatorname{Ass}_{A/\mathfrak L}(A/\mathfrak L),¶\]¶on en déduit',
    r'que $\operatorname{Ass}_{A/\mathfrak L}(\operatorname{gr}_{\mathfrak L}^\bullet(M))\subset\operatorname{Ass}_{A/\mathfrak L}(A/\mathfrak L)$, on en déduit',
    'Layout and one bullet (TeX ^{h+d}).')
add(217, "'l'application canonique gr^•_𝔏(N)→gr^•_𝔏(M) est nulle'", "raised bullets", "^{h+d} twice", 'symbol', None, 'high',
    r'$\operatorname{gr}_{\mathfrak L}^{h+d}(N)\to\operatorname{gr}_{\mathfrak L}^{h+d}(M)$', r'$\operatorname{gr}_{\mathfrak L}^\bullet(N)\to\operatorname{gr}_{\mathfrak L}^\bullet(M)$', '')
add(217, "(19.7.1.21): 'z≡Σ c_𝐩𝐟^𝐩 mod. 𝔎^{d+1}N'", "'mod.' with a full stop, no parentheses; Fraktur K", "\\pmod{\\mathfrak R^{d+1}N} (prints '(mod ...)')", 'formula', None, 'high',
    r'\pmod{\mathfrak R^{d+1}N}', r'\ \mathrm{mod.}\,\mathfrak K^{d+1}N',
    "\\pmod adds parentheses and drops the print's full stop after 'mod' (as in run_III1 p. 98). The edit also writes the Fraktur K (GLOBAL_ISSUES 63).")
add(217, "'𝐟^𝐩=f_1^{p_1}f_2^{p_2}...f_n^{p_n}'", "baseline dots", "\\cdots", 'symbol', None, 'high',
    r'f_2^{p_2}\cdots f_n^{p_n}', r'f_2^{p_2}\ldots f_n^{p_n}', '')
add(217, "'|𝐩|=p_1+...+p_n'", "baseline dots", "\\cdots", 'symbol', None, 'high',
    r'p_1+\cdots+p_n', r'p_1+\ldots+p_n', '')
add(217, "'où c_𝐩∈𝔎^dN'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'$c_{\mathbf p}\in\mathfrak R^dN$.', r'$c_{\mathbf p}\in\mathfrak K^dN$.', 'Wrong letter (GLOBAL_ISSUES 63).')
i_gr = add(217, "'ψ_N identifie gr^•_𝔏(N) à (gr_𝔎(N)⊗_{A/𝔎}(A/𝔏))[T_1, ..., T_n]'", "gr^•_𝔏(N) with a raised bullet; Fraktur K twice", "^* for the bullet; \\mathfrak R twice", 'symbol', None, 'high',
    r'identifie $\operatorname{gr}_{\mathfrak L}^*(N)$ à $(\operatorname{gr}_{\mathfrak R}^*(N)\otimes_{A/\mathfrak R}(A/\mathfrak L))',
    r'identifie $\operatorname{gr}_{\mathfrak L}^\bullet(N)$ à $(\operatorname{gr}_{\mathfrak K}^\bullet(N)\otimes_{A/\mathfrak K}(A/\mathfrak L))',
    'Raised bullet (gr^\\bullet, not ^*) and wrong letter (GLOBAL_ISSUES 63). Apply BEFORE the next finding (misprint), whose old is taken from the text after this edit; the corrected edition keeps gr_K^\\bullet(N) from this edit.')
add(217, "same formula: '(gr_𝔎(N)⊗...'", "gr_𝔎(N) without the raised bullet (6x crop: nothing above the subscript; gr^•_𝔏(N) just before has it)", "^* (the TeX gives the bullet)", 'misprint_in_print', None, 'medium',
    r'à $(\operatorname{gr}_{\mathfrak K}^\bullet(N)', r'à $(\operatorname{gr}_{\mathfrak K}(N)',
    'The bullet is omitted in the print (the identification is with (gr^•_𝔎(N)⊗(A/𝔏))[T], as in (19.7.1) b)); the TeX silently supplies it. ORDER: apply after the previous finding; this old exists only after that edit. Medium: an omitted sort, not a defect of inking (no trace on the crop).',
    corrected=r'à $(\operatorname{gr}_{\mathfrak K}^\bullet(N)', after=i_gr)
add(217, "'les c_𝐩 sont déterminés mod.'", "'déterminés' italic", "upright", 'italics', None, 'high',
    r'sont déterminés', r'sont \emph{déterminés}', '')
add(217, "'mod. 𝔎^d𝔏N, et si'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'mod. $\mathfrak R^d\mathfrak LN$, et si', r'mod. $\mathfrak K^d\mathfrak LN$, et si', 'Wrong letter (GLOBAL_ISSUES 63).')
add(217, "'classe de c_𝐩 mod. 𝔎^d𝔏N, on a'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'mod. $\mathfrak R^d\mathfrak LN$, on a', r'mod. $\mathfrak K^d\mathfrak LN$, on a', 'Wrong letter (GLOBAL_ISSUES 63).')
add(217, "(19.7.1.22): 'z̄=Σ c̄_𝐩𝐓^𝐩.'", "bold T (enlarged crop)", "italic T", 'font', None, 'high',
    r'\bar c_{\mathbf p}T^{\mathbf p}.', r'\bar c_{\mathbf p}\mathbf T^{\mathbf p}.', 'The multi-index power is printed with a bold T (the T_1, ..., T_n of the text are light).')
add(217, "'(c̄_𝐩 étant ... identifié par ψ_N à un élément de gr^d_𝔏(N))'", "Fraktur L subscript (8x crop: same glyph as the 𝔏 of gr^•_𝔏)", "\\mathfrak R", 'symbol', None, 'high',
    r'élément de $\operatorname{gr}_{\mathfrak R}^d(N)$)', r'élément de $\operatorname{gr}_{\mathfrak L}^d(N)$)',
    "Wrong letter: L, not K. ψ_N carries the degree-0 part (gr_𝔎(N)⊗(A/𝔏)) into gr_𝔏(N), so c̄_𝐩 is identified with an element of gr^d_𝔏(N); the print is right.")
add(217, "(19.7.1.23): 'c̄_𝐩∈gr^d_𝔏(R, N).'", "Fraktur L subscript (8x crop)", "\\mathfrak R", 'symbol', None, 'high',
    r'\bar c_{\mathbf p}\in\operatorname{gr}_{\mathfrak R}^d(R,N).', r'\bar c_{\mathbf p}\in\operatorname{gr}_{\mathfrak L}^d(R,N).',
    'Wrong letter: L, not K (by (19.7.1.3) the coefficients of z̄∈gr_𝔏(R,N) lie in Q∩P, Q=gr_𝔏(R,N)); the print is right.')
add(217, "'c_𝐩∈(R∩𝔎^dN)+𝔎^d𝔏N'", "Fraktur K twice", "\\mathfrak R twice", 'symbol', None, 'high',
    r'$c_{\mathbf p}\in(R\cap\mathfrak R^dN)+\mathfrak R^d\mathfrak LN$', r'$c_{\mathbf p}\in(R\cap\mathfrak K^dN)+\mathfrak K^d\mathfrak LN$', 'Wrong letter (GLOBAL_ISSUES 63).')
add(217, "display 'z∈𝔍^h(R∩𝔎^dN)+𝔍^h𝔎^d𝔏N+𝔎^{d+1}N'", "Fraktur K three times (𝔍^h is right here)", "\\mathfrak R three times", 'symbol', None, 'high',
    r'z\in\mathfrak J^h(R\cap\mathfrak R^dN)+\mathfrak J^h\mathfrak R^d\mathfrak LN+\mathfrak R^{d+1}N',
    r'z\in\mathfrak J^h(R\cap\mathfrak K^dN)+\mathfrak J^h\mathfrak K^d\mathfrak LN+\mathfrak K^{d+1}N', 'Wrong letter (GLOBAL_ISSUES 63).')

# ---------------------------------------------------------------- page 218
add(218, "'avec t∈𝔏^h(R∩𝔎^dN)'", "Fraktur L^h (3x crop), Fraktur K", "\\mathfrak J^h; \\mathfrak R", 'symbol', None, 'high',
    r'$t\in\mathfrak J^h(R\cap\mathfrak R^dN)$', r'$t\in\mathfrak L^h(R\cap\mathfrak K^dN)$',
    'Wrong letter, as in (19.7.1.19) on p. 217 (𝔏^h, not 𝔍^h); the edit also writes the Fraktur K.')
add(218, "'g_2∈𝔎^{d+1}N+𝔎^d𝔏^hN'", "Fraktur K twice", "\\mathfrak R twice", 'symbol', None, 'high',
    r'$g_2\in\mathfrak R^{d+1}N+\mathfrak R^d\mathfrak L^hN$', r'$g_2\in\mathfrak K^{d+1}N+\mathfrak K^d\mathfrak L^hN$', 'Wrong letter (GLOBAL_ISSUES 63).')
add(218, "'g_2∈𝔎^{d+1}N+𝔎^d𝔏^hN'", "𝔏^h (6x crop)", "\\mathfrak L^h (kept)", 'misprint_in_print', None, 'medium', None, None,
    'The TeX keeps the printed reading. (19.7.1.19) gives g_2∈𝔏^{h+1}𝔎^dN+𝔎^{d+1}N, and the conditions at the start of (19.7.1.8) that g_2 must meet (to prove (**_{d+1,h+1})) are g_2∈R∩(𝔎^{d+1}N+𝔎^d𝔏^{h+1}N); with 𝔏^h the conclusion does not follow. No erratum found in Liste 3.',
    corrected=r'$g_2\in\mathfrak K^{d+1}N+\mathfrak K^d\mathfrak L^{h+1}N$')
add(218, "'l'hypothèse h≥m—d+1'", "long dash", "minus sign", 'convention', 7, 'high',
    r'$h\geq m-d+1$', r'$h\geq m\setmin d+1$', 'GLOBAL_ISSUES 23.')
add(218, "Remarques (19.7.2) (i): 'gr^•_𝔎(A) est un (A/𝔎)-module plat'", "raised bullet; Fraktur K twice", "^*; \\mathfrak R", 'symbol', None, 'high',
    r'que $\operatorname{gr}_{\mathfrak R}^*(A)$ est un $(A/\mathfrak R)$-module \emph{plat}', r'que $\operatorname{gr}_{\mathfrak K}^\bullet(A)$ est un $(A/\mathfrak K)$-module \emph{plat}',
    'Raised bullet (gr^\\bullet) and wrong letter (GLOBAL_ISSUES 63).')
add(218, "(19.7.2) (i): 'la suite f est (A/𝔎)-régulière'", "light italic f (3x crop), not the bold 𝐟 of the sequence elsewhere", "\\mathbf f", 'misprint_in_print', None, 'high',
    r'suite $\mathbf f$', r'suite $f$',
    'Wrong-fount letter in the print (light italic f for the bold sequence 𝐟 of (19.7.1)); the TeX silently corrects it. The fix restores the printed reading (GLOBAL_ISSUES 29 practice).',
    corrected=r'suite $\mathbf f$')
add(218, "(19.7.2) (i): '(A/𝔎)-régulière entraîne'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'$(A/\mathfrak R)$-régulière entraîne', r'$(A/\mathfrak K)$-régulière entraîne', 'Wrong letter (GLOBAL_ISSUES 63).')
add(218, "(19.7.2) (i): 'aussi gr^•_𝔎(A)-régulière'", "raised bullet; Fraktur K", "^*; \\mathfrak R", 'symbol', None, 'high',
    r'aussi $\operatorname{gr}_{\mathfrak R}^*(A)$-régulière', r'aussi $\operatorname{gr}_{\mathfrak K}^\bullet(A)$-régulière', 'Raised bullet and wrong letter (GLOBAL_ISSUES 63).')
add(218, "(19.7.2) (i): '(0, 15.1.14)'", "bold 0", "plain 0", 'convention', 2, 'high',
    r'($0$, 15.1.14)', r'(\textbf{0}, 15.1.14)', '')
add(218, "(19.7.2) (i): 'lorsque A et A/𝔎 sont des anneaux réguliers'", "'et' and 'sont des anneaux réguliers' italic; Fraktur K", "upright; \\mathfrak R", 'italics', None, 'high',
    r'lorsque $A$ et $A/\mathfrak R$ sont des anneaux réguliers', r'lorsque $A$ \emph{et} $A/\mathfrak K$ \emph{sont des anneaux réguliers}',
    'Emphasis judged as in a roman remark body (remark-font decision is document-wide). The edit also writes the Fraktur K (GLOBAL_ISSUES 63).')
add(218, "(19.7.2) (i): '(0, 17.3.6)'", "bold 0", "plain 0", 'convention', 2, 'high',
    r'($0$, 17.3.6)', r'(\textbf{0}, 17.3.6)', '')
add(218, "(19.7.2) (i): 'en effet, 𝔎 est alors'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'en effet, $\mathfrak R$ est alors', r'en effet, $\mathfrak K$ est alors', 'Wrong letter (GLOBAL_ISSUES 63).')
add(218, "(19.7.2) (i): 'contenant 𝔎'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'contenant $\mathfrak R$ et utilisant', r'contenant $\mathfrak K$ et utilisant', 'Wrong letter (GLOBAL_ISSUES 63).')
add(218, "(19.7.2) (i): '(0, 15.1.7)'", "bold 0", "plain 0", 'convention', 2, 'high',
    r'($0$, 15.1.7)', r'(\textbf{0}, 15.1.7)', '')
add(218, "(19.7.2) (i): 'gr^•_𝔎(A) est un (A/𝔎)-module projectif'", "raised bullet; Fraktur K twice", "^*; \\mathfrak R", 'symbol', None, 'high',
    r'voit que $\operatorname{gr}_{\mathfrak R}^*(A)$ est un $(A/\mathfrak R)$-module \emph{projectif}', r'voit que $\operatorname{gr}_{\mathfrak K}^\bullet(A)$ est un $(A/\mathfrak K)$-module \emph{projectif}',
    'Raised bullet and wrong letter (GLOBAL_ISSUES 63).')
add(218, "(19.7.2) (ii): 'que M est un B-module de type fini'", "'module' italic (2x crop)", "upright", 'italics', None, 'high',
    r'$B$-module de type fini.', r'$B$-\emph{module} de type fini.', 'Emphasis judged as in a roman remark body.')
add(218, "Corollaire (19.7.3): '𝔎 un idéal de A tel que l'anneau A/𝔎'", "Fraktur K twice", "\\mathfrak R twice", 'symbol', None, 'high',
    r"$\mathfrak R$ un idéal de $A$ tel que l'anneau $A/\mathfrak R$ soit", r"$\mathfrak K$ un idéal de $A$ tel que l'anneau $A/\mathfrak K$ soit", 'Wrong letter (GLOBAL_ISSUES 63).')
add(218, "(19.7.3): label 'a)'", "upright a) (3x crop)", "\\item[a)] in the italic statement", 'convention', 6, 'high',
    r'\item[a)]', r'\item[\textup{a)}]', 'Hand-set label inside an italic statement printed upright (GLOBAL_ISSUES 88).')
add(218, "(19.7.3) a): 'gr^•_𝔎(M) est un (A/𝔎)-module plat.'", "raised bullet; Fraktur K twice", "^*; \\mathfrak R", 'symbol', None, 'high',
    r'$\operatorname{gr}_{\mathfrak R}^*(M)$ est un $(A/\mathfrak R)$-module plat.', r'$\operatorname{gr}_{\mathfrak K}^\bullet(M)$ est un $(A/\mathfrak K)$-module plat.',
    'Raised bullet and wrong letter (GLOBAL_ISSUES 63).')
add(218, "(19.7.3): label 'b)'", "upright b)", "\\item[b)] in the italic statement", 'convention', 6, 'high',
    r'\item[b)]', r'\item[\textup{b)}]', 'GLOBAL_ISSUES 88.')
add(218, "(19.7.3) b): 'gr^•_𝔪(M) et gr^•_𝔎(M)⊗_{A/𝔎}(A/𝔪)'", "raised bullets; Fraktur K twice (3x crop)", "^*; \\mathfrak R", 'symbol', None, 'high',
    r'$\operatorname{gr}_{\mathfrak m}^*(M)$ et $\operatorname{gr}_{\mathfrak R}^*(M)\otimes_{A/\mathfrak R}(A/\mathfrak m)$', r'$\operatorname{gr}_{\mathfrak m}^\bullet(M)$ et $\operatorname{gr}_{\mathfrak K}^\bullet(M)\otimes_{A/\mathfrak K}(A/\mathfrak m)$',
    'Raised bullets and wrong letter (GLOBAL_ISSUES 63).')
add(218, "(19.7.3.1): 'Q(T)=P(T)(1—T)^n.'", "long dash", "minus sign", 'convention', 7, 'high',
    r'Q(T)=P(T)(1-T)^n.', r'Q(T)=P(T)(1\setmin T)^n.', 'GLOBAL_ISSUES 23.')
add(218, "end of the statement of (19.7.3), after (19.7.3.1)", "the proof 'Soit 𝐟=(f_1, ..., f_n) ...' is roman", "the proof stays inside the italic corollary environment (\\end{corollary} after 'soit bijectif.')", 'other', None, 'high',
    r'\tag{19.7.3.1}\label{IV.19.7.3.1}¶\end{equation}¶', r'\tag{19.7.3.1}\label{IV.19.7.3.1}¶\end{equation}¶\end{corollary}¶',
    "Part 1 of 2 (apply both): ends the corollary after its statement; part 2 (later p. 218 finding) removes the old \\end{corollary} after 'soit bijectif.'. The \\emph{a)}/\\emph{b)} fix in this proof assumes the move. Same repair as for (17.13.6), p. 93.")
add(218, "proof of (19.7.3): 'A/𝔎 forment'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'dans $A/\mathfrak R$ forment', r'dans $A/\mathfrak K$ forment', 'Wrong letter (GLOBAL_ISSUES 63).')
add(218, "proof of (19.7.3): 'paramètres de A/𝔎'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'paramètres de $A/\mathfrak R$', r'paramètres de $A/\mathfrak K$', 'Wrong letter (GLOBAL_ISSUES 63).')
add(218, "proof of (19.7.3): '(0, 17.1.6)'", "bold 0", "plain 0", 'convention', 2, 'high',
    r'($0$, 17.1.6)', r'(\textbf{0}, 17.1.6)', '')
add(218, "proof of (19.7.3): 'une suite (A/𝔎)-régulière;'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'$(A/\mathfrak R)$-régulière;', r'$(A/\mathfrak K)$-régulière;', 'Wrong letter (GLOBAL_ISSUES 63).')
add(218, "proof of (19.7.3): '𝔍+𝔎=𝔪'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'$\mathfrak J+\mathfrak R=\mathfrak m$', r'$\mathfrak J+\mathfrak K=\mathfrak m$', 'Wrong letter (GLOBAL_ISSUES 63).')
add(218, "proof of (19.7.3): 'gr^•_𝔪(M) est un (A/𝔪)-module plat'", "raised bullet", "^*", 'symbol', None, 'high',
    r'$\operatorname{gr}_{\mathfrak m}^*(M)$ est un $(A/\mathfrak m)$-module plat', r'$\operatorname{gr}_{\mathfrak m}^\bullet(M)$ est un $(A/\mathfrak m)$-module plat', '')
add(218, "proof of (19.7.3): 'l'équivalence de a) et b) dans (19.7.1)'", "a) and b) wholly italic in roman text", "$a)$ $b)$ (italic letter, upright parenthesis)", 'italics', None, 'high',
    r"l'équivalence de $a)$ et $b)$", r"l'équivalence de \emph{a)} et \emph{b)}",
    'GLOBAL_ISSUES 88. Assumes the \\end{corollary} move of (19.7.3) (otherwise \\emph prints upright inside the italic environment).')
add(218, "proof of (19.7.3): '(gr^•_𝔎(M)⊗_{A/𝔎}(A/𝔪))[T_1, ..., T_n]'", "raised bullet; Fraktur K twice (2.5x crop)", "^*; \\mathfrak R", 'symbol', None, 'high',
    r'$(\operatorname{gr}_{\mathfrak R}^*(M)\otimes_{A/\mathfrak R}(A/\mathfrak m))[T_1,\ldots,T_n]$', r'$(\operatorname{gr}_{\mathfrak K}^\bullet(M)\otimes_{A/\mathfrak K}(A/\mathfrak m))[T_1,\ldots,T_n]$',
    'Raised bullet and wrong letter (GLOBAL_ISSUES 63).')
i_sum = add(218, "proof of (19.7.3): 'égal à Σ_{r=0}^h (r+n—1 n—1) rg(gr^{h-r}_𝔎(M)⊗_{A/𝔎}(A/𝔪)). Comme (1—T)^{-n}=Σ_{r=0}^∞ (r+n—1 n—1)T^r, cela prouve'", "both formulas in the running text (with limits above and below Σ); Fraktur K; long dashes", "two displays", 'other', None, 'high',
    r'égal à¶\[¶  \sum_{r=0}^h\binom{r+n-1}{n-1}\operatorname{rg}(\operatorname{gr}_{\mathfrak R}^{h-r}(M)\otimes_{A/\mathfrak R}(A/\mathfrak m)).¶\]¶Comme¶\[¶  (1-T)^{-n}=\sum_{r=0}^{\infty}\binom{r+n-1}{n-1}T^r,¶\]¶cela prouve',
    r'égal à $\sum_{r=0}^h\binom{r+n\setmin 1}{n\setmin 1}\operatorname{rg}(\operatorname{gr}_{\mathfrak K}^{h-r}(M)\otimes_{A/\mathfrak K}(A/\mathfrak m))$. Comme $(1\setmin T)^{-n}=\sum_{r=0}^{\infty}\binom{r+n\setmin 1}{n\setmin 1}T^r$, cela prouve',
    'Layout (displays where the print sets the formulas inline). The edit also writes the two Fraktur K (GLOBAL_ISSUES 63) and the five long dashes (convention 7, next two findings); the exponent -n has a short minus in the print.')
add(218, "first binomial: '(r+n—1 n—1)'", "long dashes (two)", "minus signs", 'convention', 7, 'high', None, None,
    'Covered by the edit of the preceding finding (inline formulas), which writes \\setmin. GLOBAL_ISSUES 23.')
add(218, "'(1—T)^{-n}' and the second binomial '(r+n—1 n—1)'", "long dashes (three)", "minus signs", 'convention', 7, 'high', None, None,
    'Covered by the edit of the inline-formula finding above, which writes \\setmin. GLOBAL_ISSUES 23.')
add(218, "end of the proof of (19.7.3)", "", "old \\end{corollary}", 'other', None, 'high',
    r'pour que $\psi_M$ soit bijectif.¶\end{corollary}', r'pour que $\psi_M$ soit bijectif.',
    'Part 2 of 2 with the earlier p. 218 finding that inserts \\end{corollary} after (19.7.3.1); apply both.')
add(218, "Corollaire (19.7.4): 'normalement plat (6.10.1) le long de Y'", "reference upright", "italic (inside the statement)", 'convention', 6, 'high',
    r'normalement plat (6.10.1) le long', r'normalement plat \textup{(6.10.1)} le long', 'Reference printed upright inside the italic statement.')
add(218, "(19.7.4): '(indépendante de x∈Y)'", "roman, with upright parentheses (2x crop)", "italic", 'convention', 6, 'high',
    r'(indépendante de $x\in Y$)', r'\textup{(indépendante de $x\in Y$)}', '')
add(218, "(19.7.4): 'gr^•_{𝔪_x}(𝓕_x)'", "raised bullet", "^*", 'symbol', None, 'high',
    r'\operatorname{gr}_{\mathfrak m_x}^*(\sh F_x)', r'\operatorname{gr}_{\mathfrak m_x}^\bullet(\sh F_x)', '')
add(218, "(19.7.4.1): 'R(T)(1—T)^{-n}'", "long dash (the exponent's minus is short)", "minus sign", 'convention', 7, 'high',
    r'R(T)(1-T)^{-n}\qquad', r'R(T)(1\setmin T)^{-n}\qquad', 'GLOBAL_ISSUES 23.')
add(218, "end of the statement of (19.7.4), after (19.7.4.1) (last line of p. 218)", "the proof 'Soit 𝒥 l'Idéal ...' at the top of p. 219 is roman", "the proof stays inside the italic corollary environment (\\end{corollary} on p. 219)", 'other', None, 'high',
    r'\tag{19.7.4.1}\label{IV.19.7.4.1}¶\end{equation}¶', r'\tag{19.7.4.1}\label{IV.19.7.4.1}¶\end{equation}¶\end{corollary}¶',
    "Part 1 of 2 (apply both): part 2 is the p. 219 finding that removes the old \\end{corollary} after 'de $x\\in Y$.'. The blank lines around \\oldpage[IV-4]{219} stay (the proof begins a new indented paragraph).")

# ---------------------------------------------------------------- page 219
add(219, "proof of (19.7.4): 'gr^•_𝒥(𝓕)'", "raised bullet", "^*", 'symbol', None, 'high',
    r'\operatorname{gr}_{\sh J}^*(\sh F)', r'\operatorname{gr}_{\sh J}^\bullet(\sh F)', '')
add(219, "'𝔎=𝒥_x'", "Fraktur K", "\\mathfrak R", 'symbol', None, 'high',
    r'$\mathfrak R=\sh J_x$', r'$\mathfrak K=\sh J_x$', 'Wrong letter (GLOBAL_ISSUES 63).')
add(219, "'l'hypothèse a) étant remplie'", "a) wholly italic in roman text", "$a)$", 'italics', None, 'high',
    r"l'hypothèse $a)$ étant", r"l'hypothèse \emph{a)} étant", 'GLOBAL_ISSUES 88. Assumes the \\end{corollary} move of (19.7.4) (p. 218 part 1, p. 219 part 2).')
add(219, "'R_x(T)(1—T)^{-n}'", "long dash", "minus sign", 'convention', 7, 'high',
    r'$R_x(T)(1-T)^{-n}$', r'$R_x(T)(1\setmin T)^{-n}$', 'GLOBAL_ISSUES 23.')
add(219, "'gr^•_{𝒥_x}(𝓕_x)'", "raised bullet", "^*", 'symbol', None, 'high',
    r'\operatorname{gr}_{\sh J_x}^*(\sh F_x)', r'\operatorname{gr}_{\sh J_x}^\bullet(\sh F_x)', '')
add(219, "'⊗_{𝒪_{Y,x}} k(x)'", "bold italic k", "plain k", 'convention', 1, 'high',
    r'}k(x)$', r'}\boldsymbol{k}(x)$', '')
add(219, "'la série de Poincaré R_x(T) est indépendante de x∈Y'", "'indépendante' italic", "no emphasis (the text is italic only because it sits inside the corollary environment)", 'italics', None, 'high',
    r'est indépendante', r'est \emph{indépendante}', 'Assumes the \\end{corollary} move of (19.7.4).')
add(219, "end of the proof of (19.7.4)", "", "old \\end{corollary}", 'other', None, 'high',
    r'de $x\in Y$.¶\end{corollary}', r'de $x\in Y$.',
    'Part 2 of 2 with the last p. 218 finding (\\end{corollary} after (19.7.4.1)); apply both. That part lies in the p. 218 segment.')
add(219, "Corollaire (19.7.5) (i): label '(i)'", "upright", "\\item[(i)] in the italic statement", 'convention', 6, 'high',
    r'\item[(i)] Si $\sh F$', r'\item[\textup{(i)}] Si $\sh F$', 'GLOBAL_ISSUES 16.')
add(219, "(19.7.5) (i): '(cf. (11.3.4) pour la définition de la platitude normale en un point)'", "roman, upright parentheses", "italic", 'convention', 6, 'high',
    r'(cf. (11.3.4) pour la définition de la platitude normale en un point)', r'\textup{(cf. (11.3.4) pour la définition de la platitude normale en un point)}', '')
add(219, "(19.7.5): label '(ii)'", "upright", "\\item[(ii)] in the italic statement", 'convention', 6, 'high',
    r'\item[(ii)] Supposons en outre', r'\item[\textup{(ii)}] Supposons en outre', 'GLOBAL_ISSUES 16.')
add(219, "(19.7.5) (ii): '(ce qui aura lieu en particulier si X est régulier aux points de Z)'", "roman, with 'régulier' italic", "italic", 'convention', 6, 'high',
    r'(ce qui aura lieu en particulier si $X$ est régulier aux points de $Z$)', r'\textup{(ce qui aura lieu en particulier si $X$ est \emph{régulier} aux points de $Z$)}', '')
add(219, "(19.7.5) (ii): 's'il existe un point z∈Z'", "'un' roman (emphasis), 'point' italic (2x crop)", "italic", 'convention', 6, 'high',
    r"s'il existe un point", r"s'il existe \textup{un} point", '')
add(219, "end of the statement of (19.7.5)", "the proof 'Soient 𝒦 et ℒ⊃𝒦 ...' and its (i), (ii) are roman", "the proof stays inside the italic corollary environment", 'other', None, 'high',
    r'aux points de $Z$.¶\end{enumerate}¶¶Soient', r'aux points de $Z$.¶\end{enumerate}¶\end{corollary}¶¶Soient',
    'Part 1 of 2 (apply both): ends the corollary after its statement; part 2 removes the old \\end{corollary} at the end of the proof. The \\emph{a)}, \\emph{b)}, \\emph{d)} fixes in this proof assume the move.')
add(219, "proof of (19.7.5): 'une suite (f_i) ... qui est 𝒦_z-régulière'", "𝒦_z-régulière (2x crop)", "kept", 'misprint_in_print', None, 'low', None, None,
    "The TeX keeps the printed reading. The proof applies (19.7.1) with A=𝒪_{X,z}, 𝔎=𝒦_z, whose hypothesis is that the sequence is (A/𝔎)-regular; the regular immersion Z→Y at z (19.1.1) gives that too. 𝒦_z-regularity is another condition. Low: a reading of the mathematics (authors' slip), not of the type; no erratum found.",
    corrected=r'$(\sh O_{X,z}/\sh K_z)$-régulière')
add(219, "proof (i): 'gr^•_{𝒦_z}(𝓕_z) est un 𝒪_{Y,z}-module plat'", "raised bullet", "^*", 'symbol', None, 'high',
    r'signifie que $\operatorname{gr}_{\sh K_z}^*(\sh F_z)$', r'signifie que $\operatorname{gr}_{\sh K_z}^\bullet(\sh F_z)$', '')
add(219, "proof (i): 'gr^•_{ℒ_z}(𝓕_z)'", "raised bullet", "^*", 'symbol', None, 'high',
    r'\operatorname{gr}_{\sh L_z}^*(\sh F_z)', r'\operatorname{gr}_{\sh L_z}^\bullet(\sh F_z)', '')
add(219, "proof (i): 'a) entraîne b).'", "a), b) wholly italic", "$a)$ $b)$", 'italics', None, 'high',
    r'$a)$ entraîne $b)$.', r'\emph{a)} entraîne \emph{b)}.', 'GLOBAL_ISSUES 88. Assumes the \\end{corollary} move of (19.7.5).')
add(219, "proof (ii): 'gr^•_{𝒦_z}(𝓕_z)-régulière'", "raised bullet", "^*", 'symbol', None, 'high',
    r'est $\operatorname{gr}_{\sh K_z}^*(\sh F_z)$-régulière', r'est $\operatorname{gr}_{\sh K_z}^\bullet(\sh F_z)$-régulière', '')
add(219, "proof (ii): 'et si gr^•_{𝒦_z}(𝓕_z) est 𝒪_{Y,z}-plat'", "raised bullet", "^*", 'symbol', None, 'high',
    r'et si $\operatorname{gr}_{\sh K_z}^*(\sh F_z)$ est', r'et si $\operatorname{gr}_{\sh K_z}^\bullet(\sh F_z)$ est', '')
add(219, "proof (ii): 'gr^•_{𝒦_ζ}(𝓕_ζ)'", "raised bullet", "^*", 'symbol', None, 'high',
    r'\operatorname{gr}_{\sh K_\zeta}^*', r'\operatorname{gr}_{\sh K_\zeta}^\bullet', '')
add(219, "proof (ii): '(0_I, 6.3.1)'", "bold 0 with subscript I", "plain 0", 'convention', 2, 'high',
    r'($0_{\mathrm I}$, 6.3.1)', r'($\mathbf{0}_{\mathrm I}$, 6.3.1)', '')
add(219, "proof (ii): 'gr^•_{ℒ_{z'}}(𝓕_{z'})'", "raised bullet", "^*", 'symbol', None, 'high',
    r"\operatorname{gr}_{\sh L_{z'}}^*", r"\operatorname{gr}_{\sh L_{z'}}^\bullet", '')
add(219, "proof (ii): 'gr^•_{𝒦_{z'}}(𝓕_{z'})'", "raised bullet", "^*", 'symbol', None, 'high',
    r"\operatorname{gr}_{\sh K_{z'}}^*", r"\operatorname{gr}_{\sh K_{z'}}^\bullet", '')
add(219, "proof (ii): 'l'équivalence de a) et d)'", "a), d) wholly italic", "$a)$ $d)$", 'italics', None, 'high',
    r"l'équivalence de $a)$ et $d)$", r"l'équivalence de \emph{a)} et \emph{d)}", 'GLOBAL_ISSUES 88. Assumes the \\end{corollary} move of (19.7.5).')
add(219, "end of the proof of (19.7.5)", "", "old \\end{corollary}", 'other', None, 'high',
    r'dans (19.7.1).¶\end{enumerate}¶\end{corollary}', r'dans (19.7.1).¶\end{enumerate}',
    'Part 2 of 2 with the p. 219 finding that inserts \\end{corollary} after the statement of (19.7.5); apply both.')
add(219, "Proposition (19.8.1): 'en outre que l'une des deux hypothèses'", "'l'une' roman (emphasis; 1.5x crop)", "italic", 'convention', 6, 'high',
    r"que l'une des deux", r"que \textup{l'une} des deux", '')

# ---------------------------------------------------------------- checks
pages = {}
for n in [215, 216, 217, 218, 219]:
    pages[n] = open(rf'{BASE}\page_{n}.tex', encoding='utf-8').read().replace('\r\n', '\n')
cur = dict(pages)
ok = True
for i, e in enumerate(F):
    fx = e['fix']
    if not fx:
        continue
    old, new = fx['old'], fx['new']
    p = e['page']
    c_orig = pages[p].count(old)
    c_cur = cur[p].count(old)
    if e['_after'] is None:
        if c_orig != 1:
            print('NOT UNIQUE IN ORIGINAL', i, p, c_orig, repr(old)[:120]); ok = False
    if c_cur != 1:
        print('NOT UNIQUE AT APPLY TIME', i, p, c_cur, repr(old)[:120]); ok = False
    cur[p] = cur[p].replace(old, new, 1)
# span overlap check (entries without _after, against the original text)
for p in pages:
    spans = []
    for i, e in enumerate(F):
        if e['page'] != p or not e['fix'] or e['_after'] is not None:
            continue
        s = pages[p].find(e['fix']['old'])
        spans.append((s, s + len(e['fix']['old']), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            print('OVERLAP', p, a, b)
for p in cur:
    for pat in [r'\mathfrak R', r'\cdots', r'^*(', r'^{h+d}(N_', r'\pmod']:
        if pat in cur[p]:
            print('LEFT', p, pat, cur[p].count(pat))
print('entries', len(F), 'ok' if ok else 'PROBLEMS')
for e in F:
    e.pop('_after')
json.dump(F, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for p in cur:
    open(rf'{BASE}\crops_215_219\after_{p}.tex', 'w', encoding='utf-8').write(cur[p])
from collections import Counter
cnt = Counter()
for e in F:
    k = 'misprint' if e['kind'] == 'misprint_in_print' else ('convention' if e['kind'] == 'convention' else 'normal')
    cnt[(e['page'], k)] += 1
for p in sorted(pages):
    print(p, cnt[(p, 'normal')], cnt[(p, 'convention')], cnt[(p, 'misprint')])
