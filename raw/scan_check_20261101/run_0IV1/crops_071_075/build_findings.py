import json, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = r'user/Documents/ega_scan_check_20261101/run_0IV1/'
OUT = RUN + 'findings_071_075.json'
NL = '\u23ce'  # placeholder for a line break in old/new


def L(s):
    return s.replace(NL, '\n')


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note='', corrected=None):
    d = {'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind,
         'convention': conv, 'confidence': conf,
         'fix': None if old is None else {'old': L(old), 'new': L(new)}}
    if corrected is not None:
        d['corrected'] = corrected
    d['note'] = note
    F.append(d)


KNOTE = ('Same glyph as the \\mathfrak K of p. 80 (the neighbourhoods K_{H,mu,n}) and of 0_I (7.7.5) '
         "'J.B c K' (J, K, L for the ideals of A, B, C); the print's Fraktur R (radical R(A), 0_I p. 12) has a different shape "
         '(enlarged crops). Document-wide: ega0-19 writes \\mathfrak R for this letter throughout section 19 (p. 70 too).')
LNOTE = ('Same glyph as the \\mathfrak L of p. 80 ((L_mu)), p. 84 (si L est le noyau) and 0_I (7.7.5) (J.C c L); '
         'Fraktur Q has an O-shaped body (enlarged crops). Document-wide: \\mathfrak Q for this letter also on pp. 14, 84-85.')

# ---------------- page 71 ----------------
add(71, "end of the paragraph continued from p. 70: 'pour tout idéal ouvert K de B'",
    'Fraktur K (enlarged crop)', r'$\mathfrak R$', 'symbol', None, 'high',
    r'ouvert $\mathfrak R$ de $B$', r'ouvert $\mathfrak K$ de $B$', KNOTE)
add(71, "same sentence: 'tel que JB c K'", 'Fraktur K', r'\mathfrak R', 'symbol', None, 'high',
    r'\mathfrak JB\subset\mathfrak R$', r'\mathfrak JB\subset\mathfrak K$', 'As the previous finding.')
add(71, "heading '19.1. Épimorphismes et monomorphismes formels.'", 'title ends with a full stop',
    'no full stop', 'punctuation', None, 'high',
    r'\subsection{Épimorphismes et monomorphismes formels}',
    r'\subsection{Épimorphismes et monomorphismes formels.}', 'GLOBAL_ISSUES 43/58; page-fixed as on p. 20.')
for lab, old, where in [
        ('(i)', r'\item[(i)] Les conditions', 'Proposition (19.1.1), label (i)'),
        ('a)', r'\item[a)]', 'Proposition (19.1.1), label a)'),
        ("a')", r"\item[a$'$)]", "Proposition (19.1.1), label a')"),
        ("a'')", r"\item[a$''$)]", "Proposition (19.1.1), label a'')"),
        ('(ii)', r'\item[(ii)] Les conditions', 'Proposition (19.1.1), label (ii)'),
        ('b)', r'\item[b)]', 'Proposition (19.1.1), label b)'),
        ("b')", r"\item[b$'$)]", "Proposition (19.1.1), label b')"),
        ("b'')", r"\item[b$''$)]", "Proposition (19.1.1), label b'')")]:
    inner = old[old.index('[') + 1:old.index(']')]
    add(71, where, lab + ' upright (enlarged crop)', 'italic (label inside the italic statement)', 'convention', 6, 'high',
        old, old.replace('[' + inner + ']', '[\\textup{' + inner + '}]'), 'GLOBAL_ISSUES 16.')
add(71, "(19.1.1) a): 'u(M) est dense dans N'", "'dense' italic like the rest of the statement (enlarged crop)",
    "\\emph{dense}: upright inside the italic statement", 'convention', 6, 'high',
    r'est \emph{dense} dans $N$.', r'est dense dans $N$.')
add(71, "(19.1.1) a'): 'û(M^) est dense dans N^'", "'dense' italic", '\\emph{dense}: upright', 'convention', 6, 'high',
    r'est \emph{dense} dans $\widehat N$', r'est dense dans $\widehat N$')
add(71, "(19.1.1) a''): '... est surjectif.'", "'surjectif' italic", '\\emph{surjectif}: upright', 'convention', 6, 'high',
    r'\emph{surjectif}', 'surjectif')
add(71, "(19.1.1) b'): 'û est un isomorphisme du Â-module'", "'isomorphisme' italic", '\\emph{isomorphisme}: upright',
    'convention', 6, 'high', r'est un \emph{isomorphisme} du', 'est un isomorphisme du',
    'Only the occurrence in b\'); the \\emph{isomorphisme} of (19.1.2) is correct (roman paragraph).')
add(71, "(19.1.1) b'): '(qui est nécessairement fermé)'", "'fermé' italic", '\\emph{fermé}: upright', 'convention', 6, 'high',
    r'\emph{fermé}', 'fermé')
add(71, "after (19.1.1): 'Cela résulte immédiatement de la définition des séparés complétés, et du fait que N/W_lambda est discret.'",
    'roman sentence in a new indented paragraph after the statement',
    'inside the proposition environment (italic, run on after the list)', 'other', None, 'high',
    r'\end{enumerate}⏎Cela résulte immédiatement de la définition des séparés complétés, et du fait⏎que $N/W_\lambda$ est discret.⏎\end{proposition}',
    r'\end{enumerate}⏎\end{proposition}⏎⏎Cela résulte immédiatement de la définition des séparés complétés, et du fait⏎que $N/W_\lambda$ est discret.',
    'One edit: moves \\end{proposition} to the end of the printed statement and adds the paragraph break (as GLOBAL_ISSUES 58, (16.4.5)).')
add(71, "(19.1.2): 'on dit que u est un épimorphisme formel'", "'un épimorphisme formel' italic, 'un' included (enlarged crop)",
    "'un' upright", 'italics', None, 'high',
    r'est un \emph{épimorphisme formel}', r'est \emph{un épimorphisme formel}')
add(71, "(19.1.2): '(resp. un monomorphisme formel)'", "'un monomorphisme formel' italic, 'un' included",
    "'un' upright", 'italics', None, 'high',
    r'(resp. un⏎\emph{monomorphisme formel})', r'(resp. \emph{un⏎monomorphisme formel})')
for lab, old in [('(i)', r'\item[(i)] Pour que'), ('(ii)', r'\item[(ii)] Pour que'), ('(iii)', r'\item[(iii)]')]:
    inner = old[old.index('[') + 1:old.index(']')]
    add(71, 'Proposition (19.1.3), label ' + lab, lab + ' upright', 'italic', 'convention', 6, 'high',
        old, old.replace('[' + inner + ']', '[\\textup{' + inner + '}]'), 'GLOBAL_ISSUES 16.')
add(71, "end of p. 71, (19.1.3) (iii): '... l'homomorphisme canonique M/V_mu -> M/V_lambda / se factorise en' (p. 72)",
    'the sentence runs on over the page break; p. 72 begins flush left with \'se factorise en\'',
    'blank lines before and after \\oldpage{72} (paragraph break, \\noindent)', 'other', None, 'high',
    r"et que l'homomorphisme canonique⏎  $M/V_\mu\to M/V_\lambda$⏎⏎", r"et que l'homomorphisme canonique⏎  $M/V_\mu\to M/V_\lambda$⏎",
    'GLOBAL_ISSUES 20. Apply together with the p. 72 finding that removes the blank line after the marker (both must go).')

# ---------------- page 72 ----------------
add(72, "top of p. 72: 'se factorise en' (continues (19.1.3) (iii))", 'flush left, same paragraph',
    'blank line after the marker and \\noindent', 'other', None, 'high',
    r'\oldpage[0\textsubscript{IV-1}]{72}⏎⏎  \noindent se factorise en', r'\oldpage[0\textsubscript{IV-1}]{72}⏎  se factorise en',
    'Apply together with the p. 71 finding that removes the blank line before the marker.')
add(72, "proof of (19.1.4): 'si l'on a une factorisation M/J_mu M -> N/J_mu N -> M/J_lambda M, l'image de'",
    'the factorisation is inline, in the running line', 'displayed formula', 'other', None, 'high',
    r"une factorisation⏎\[⏎  M/\mathfrak J_\mu M\xrightarrow{u_\mu}⏎  N/\mathfrak J_\mu N\xrightarrow{v}M/\mathfrak J_\lambda M,⏎\]⏎l'image de",
    r"une factorisation⏎$M/\mathfrak J_\mu M\xrightarrow{u_\mu}N/\mathfrak J_\mu N\xrightarrow{v}M/\mathfrak J_\lambda M$,⏎l'image de",
    'Layout: inline in the print, displayed in the TeX (GLOBAL_ISSUES 21).')
for lab, old in [('a)', r'\item[a)] Pour tout'), ('b)', r'\item[b)] Pour tout')]:
    inner = old[old.index('[') + 1:old.index(']')]
    add(72, 'Proposition (19.1.5), label ' + lab, lab + ' upright (enlarged crop)', 'italic', 'convention', 6, 'high',
        old, old.replace('[' + inner + ']', '[\\textup{' + inner + '}]'))
add(72, "(19.1.5) a): 'Pour tout A-module topologique discret E'", "'discret' upright (enlarged crop)",
    'italic (statement environment)', 'convention', 6, 'high',
    r'topologique discret $E$', r'topologique \textup{discret} $E$')
add(72, "(19.1.5) b), display 'M/V'' -> N/W'' -> M/V''", 'no comma after the display (enlarged crop)',
    "comma: M/V',", 'punctuation', None, 'high',
    r"\xrightarrow{h}M/V',⏎", r"\xrightarrow{h}M/V'⏎")
add(72, "proof of (19.1.5): 'Pour voir que a) entraîne b), il suffit d'appliquer a) à'", 'a), b), a) italic',
    'upright', 'italics', None, 'high',
    r"Pour voir que a) entraîne b), il suffit d'appliquer a) à",
    r"Pour voir que \emph{a)} entraîne \emph{b)}, il suffit d'appliquer \emph{a)} à")
add(72, "proof of (19.1.5): 'pour montrer que b) entraîne a), on peut'", 'b), a) italic', 'upright', 'italics', None, 'high',
    r'pour montrer que b) entraîne a), on peut', r'pour montrer que \emph{b)} entraîne \emph{a)}, on peut')
add(72, "proof of (19.1.5): 'et en appliquant b), on obtient'", 'b) italic', 'upright', 'italics', None, 'high',
    r'appliquant b),', r'appliquant \emph{b)},')
add(72, "end of p. 72: '... on obtient / le A-homomorphisme continu w cherché' (p. 73)",
    'the sentence runs on over the page break; p. 73 begins flush left', 'blank lines before and after \\oldpage{73}',
    'other', None, 'high', 'on obtient⏎⏎', 'on obtient⏎',
    'GLOBAL_ISSUES 20. Apply together with the p. 73 finding that removes the blank line after the marker.')

# ---------------- page 73 ----------------
add(73, "top of p. 73: 'le A-homomorphisme continu w cherché'", 'flush left, same paragraph', 'blank line after the marker',
    'other', None, 'high',
    r'\oldpage[0\textsubscript{IV-1}]{73}⏎⏎le $A$-homomorphisme', r'\oldpage[0\textsubscript{IV-1}]{73}⏎le $A$-homomorphisme',
    'Apply together with the p. 72 finding that removes the blank line before the marker.')
add(73, "after the proof of (19.1.5): 'comme la condition b) de (19.1.5)'", 'b) italic', 'upright', 'italics', None, 'high',
    r'comme la condition b) de', r'comme la condition \emph{b)} de')
add(73, "same sentence: 'u est alors un monomorphisme formel.'", "'monomorphisme formel' italic", 'upright', 'italics', None, 'high',
    r'un monomorphisme⏎formel.', r'un \emph{monomorphisme⏎formel}.')
add(73, "after (19.1.6): 'avec les notations de (19.1.5, a))'", 'a) italic', 'upright', 'italics', None, 'high',
    r'(19.1.5, a))', r'(19.1.5, \emph{a)})')
add(73, "Corollaire (19.1.7): '(autrement dit, soit un isomorphisme de M/J_lambda M sur un facteur direct de N/J_lambda N)'",
    'the parenthetical is roman', 'italic (statement environment)', 'convention', 6, 'high',
    r'(autrement dit, soit⏎un isomorphisme de $M/\mathfrak J_\lambda M$ sur un facteur direct de⏎$N/\mathfrak J_\lambda N$)',
    r'\textup{(autrement dit, soit⏎un isomorphisme de $M/\mathfrak J_\lambda M$ sur un facteur direct de⏎$N/\mathfrak J_\lambda N$)}')
add(73, "proof of (19.1.7): 'pour V' = J_lambda M dans la condition b) de (19.1.5)'", 'b) italic', 'upright', 'italics', None, 'high',
    r'dans la condition b) de', r'dans la condition \emph{b)} de')
add(73, "proof of (19.1.7): 'en vertu de (19.1.5, b))'", 'b) italic', 'upright', 'italics', None, 'high',
    r'(19.1.5, b))', r'(19.1.5, \emph{b)})')
add(73, "proof of (19.1.7): 'se factorise en M/J_mu M -> N/J_mu N -> M/J_lambda M; mais comme'",
    'inline, in the running line', 'displayed formula', 'other', None, 'high',
    r'se factorise en⏎\[⏎  M/\mathfrak J_\mu M\xrightarrow{u_\mu}N/\mathfrak J_\mu N⏎  \xrightarrow{h}M/\mathfrak J_\lambda M~;⏎\]⏎mais comme⏎',
    r'se factorise en⏎$M/\mathfrak J_\mu M\xrightarrow{u_\mu}N/\mathfrak J_\mu N\xrightarrow{h}M/\mathfrak J_\lambda M$~; mais comme⏎',
    'Layout: inline in the print (GLOBAL_ISSUES 21).')
add(73, "proof of (19.1.7): 'h(J_lambda(N/J_mu N)) = J_lambda h(N/J_mu N) c J_lambda(M/J_lambda M) = 0'",
    'h(J_l(N/J_mN)) = J_l h(N/J_mN) c J_l(M/J_lM) = 0', 'the middle term = J_lambda h(N/J_mu N) is missing',
    'missing', None, 'high',
    r'h(\mathfrak J_\lambda(N/\mathfrak J_\mu N))⏎\subset',
    r'h(\mathfrak J_\lambda(N/\mathfrak J_\mu N))=\mathfrak J_\lambda h(N/\mathfrak J_\mu N)⏎\subset')
add(73, "proof of (19.1.7): 'h se factorise canoniquement en N/J_mu N -> N/J_lambda N -> M/J_lambda M, et il est immédiat'",
    'inline, in the running line', 'displayed formula', 'other', None, 'high',
    r'canoniquement en⏎\[⏎  N/\mathfrak J_\mu N\longrightarrow N/\mathfrak J_\lambda N⏎  \xrightarrow{s}M/\mathfrak J_\lambda M,⏎\]⏎et il est',
    r'canoniquement en⏎$N/\mathfrak J_\mu N\longrightarrow N/\mathfrak J_\lambda N\xrightarrow{s}M/\mathfrak J_\lambda M$, et il est',
    'Layout: inline in the print (GLOBAL_ISSUES 21).')
add(73, "Proposition (19.1.8): '(et u est alors un isomorphisme topologique de M sur un facteur direct topologique de N)'",
    'the parenthetical is roman', 'italic (statement environment)', 'convention', 6, 'high',
    r'(et⏎$u$ est alors un isomorphisme topologique de $M$ sur un facteur direct⏎topologique de $N$)',
    r'\textup{(et⏎$u$ est alors un isomorphisme topologique de $M$ sur un facteur direct⏎topologique de $N$)}')

# ---------------- page 74 ----------------
add(74, 'proof of (19.1.8), first diagram, top row: P_n', 'P_n with a heavy bold italic subscript n (M_n, N_n normal; enlarged crop)',
    'P_n (ordinary subscript; silently corrected)', 'misprint_in_print', None, 'high',
    r'& P_n\ar[r] & 0', r'& P_{\boldsymbol{n}}\ar[r] & 0',
    'Wrong-fount letter (GLOBAL_ISSUES 29: kept in the diplomatic text).', corrected='P_n')
add(74, "proof of (19.1.8): 'g o s_{n+1} — s'_n o h'", 'long dash for the subtraction', '-', 'convention', 7, 'high',
    r"s_{n+1}-s'_n\circ h", r"s_{n+1}\setmin s'_n\circ h", 'GLOBAL_ISSUES 23; \\setmin pending the convention-7 decision.')
add(74, 'proof of (19.1.8), second diagram, top left: P_n', 'P_n with a heavy bold italic subscript n (N_n, s\'_n normal; enlarged crop)',
    'P_n (silently corrected)', 'misprint_in_print', None, 'high',
    r"P_n\ar[r]^{s'_n}", r"P_{\boldsymbol{n}}\ar[r]^{s'_n}", 'Wrong-fount letter, as in the first diagram.', corrected='P_n')
add(74, 'proof of (19.1.8), second diagram: label g of the right vertical arrow', 'g to the right of the arrow',
    '\\ar[u]^g sets it to the left', 'other', None, 'high',
    r'N_{n+1}\ar[u]^g⏎', r'N_{n+1}\ar[u]_g⏎', 'h (left arrow) is on the left in print and TeX.')
add(74, "proof of (19.1.8): 'dans u_n(M_n) = u_{n+1}(M_{n+1})/J_n u_{n+1}(M_{n+1}); comme'",
    'inline, in the running line', 'displayed formula', 'other', None, 'high',
    r'dans⏎\[⏎  u_n(M_n)=u_{n+1}(M_{n+1})/⏎  \mathfrak J_nu_{n+1}(M_{n+1})~;⏎\]⏎comme',
    r'dans⏎$u_n(M_n)=u_{n+1}(M_{n+1})/\mathfrak J_nu_{n+1}(M_{n+1})$~;⏎comme',
    'Layout: inline in the print (GLOBAL_ISSUES 21).')
add(74, "proof of (19.1.8), display 'P_{n+1} -> u_{n+1}(M_{n+1}) -> u_{n+1}(M_{n+1})/J_n u_{n+1}(M_{n+1})'",
    'no comma after the display (enlarged crop)', 'trailing comma', 'punctuation', None, 'high',
    r'\mathfrak J_nu_{n+1}(M_{n+1}),⏎', r'\mathfrak J_nu_{n+1}(M_{n+1})⏎')
add(74, "proof of (19.1.8): 's'_{n+1} = s_{n+1} — t_{n+1}'", 'long dash for the subtraction', '-', 'convention', 7, 'high',
    r's_{n+1}-t_{n+1}', r's_{n+1}\setmin t_{n+1}', 'GLOBAL_ISSUES 23; \\setmin pending the convention-7 decision.')
add(74, 'proof of (19.1.8), third diagram: label f of the right vertical arrow', 'f to the right of the arrow',
    '\\ar[u]^f sets it to the left', 'other', None, 'high',
    r'M_{n+1}\ar[u]^f⏎', r'M_{n+1}\ar[u]_f⏎', 'g (left arrow) is on the left in print and TeX.')
add(74, "Proposition (19.1.9): 'un anneau topologique préadmissible (0_I, 7.1.2)'", "'préadmissible (0_I, 7.1.2)' upright",
    'italic (statement environment)', 'convention', 6, 'high',
    r'préadmissible ($\mathbf{0}_{\mathrm I}$,⏎7.1.2)', r'\textup{préadmissible ($\mathbf{0}_{\mathrm I}$,⏎7.1.2)}')
add(74, "Proposition (19.1.9): 'L un idéal de définition de A'", 'Fraktur L (enlarged crop)', r'$\mathfrak Q$', 'symbol', None, 'high',
    r'$\mathfrak Q$ un idéal de définition', r'$\mathfrak L$ un idéal de définition', LNOTE)
add(74, "Proposition (19.1.9): '(cf. (19.2.3))'", 'upright', 'italic (statement environment)', 'convention', 6, 'high',
    r'(cf. (19.2.3))', r'\textup{(cf. (19.2.3))}')
add(74, "end of p. 74: (19.1.9) ends p. 74 with 'Alors les conditions suivantes sont équivalentes :'; 'a) u est formellement inversible à gauche.' opens p. 75",
    'a) is the first line of p. 75', '\\item[a)] stands before \\oldpage{75}', 'marker', None, 'high',
    r'suivantes sont équivalentes~:⏎\begin{enumerate}⏎', r'suivantes sont équivalentes~:⏎\begin{enumerate}⏎  \oldpage[0\textsubscript{IV-1}]{75}⏎',
    'Apply together with the p. 75 marker finding, which removes the old marker. Net edit in ega0-19-fr.tex (ll. 466-470): the marker moves from after \\item[a)] to before it (marginpar in vertical mode before the first \\item, no text).')
add(74, 'Proposition (19.1.9), label a) (printed at the top of p. 75; the TeX line is in the p. 74 segment)', 'a) upright (enlarged crop)',
    'italic', 'convention', 6, 'high', r'\item[a)] $u$ est', r'\item[\textup{a)}] $u$ est')

# ---------------- page 75 ----------------
add(75, 'top of p. 75', "page begins with 'a) u est formellement inversible à gauche.'", "marker followed by '\\item[b)]'",
    'marker', None, 'high', r'\oldpage[0\textsubscript{IV-1}]{75}⏎⏎  ', '',
    'Removes the old marker; apply only together with the p. 74 marker finding, which re-inserts it before \\item[a)].')
add(75, 'Proposition (19.1.9), label b)', 'b) upright', 'italic', 'convention', 6, 'high',
    r"\item[b)] L'homomorphisme", r"\item[\textup{b)}] L'homomorphisme")
add(75, "(19.1.9) b): 'u_0 : M/LM -> N/LN'", 'Fraktur L twice (enlarged crop)', r'\mathfrak Q twice', 'symbol', None, 'high',
    r'$u_0:M/\mathfrak QM\to N/\mathfrak QN$', r'$u_0:M/\mathfrak LM\to N/\mathfrak LN$', LNOTE)
add(75, "proof of (19.1.9): 'que la condition a) équivaut'", 'a) italic', 'upright', 'italics', None, 'high',
    r'que la condition a) équivaut', r'que la condition \emph{a)} équivaut')
add(75, "proof of (19.1.9): 'comme L est un idéal ouvert'", 'Fraktur L', r'$\mathfrak Q$', 'symbol', None, 'high',
    r'comme $\mathfrak Q$ est un idéal', r'comme $\mathfrak L$ est un idéal', 'As the u_0 finding.')
add(75, "proof of (19.1.9): 'Pour montrer inversement que b) entraîne a)'", 'b), a) italic', 'upright', 'italics', None, 'high',
    r'inversement que b) entraîne a),', r'inversement que \emph{b)} entraîne \emph{a)},')
add(75, "proof of (19.1.9): 'L/J_lambda est par hypothèse un idéal nilpotent'", 'Fraktur L', r'\mathfrak Q', 'symbol', None, 'high',
    r'$\mathfrak Q/\mathfrak J_\lambda$', r'$\mathfrak L/\mathfrak J_\lambda$', 'As the u_0 finding.')
add(75, "proof of (19.1.9), last sentence: 'Notre assertion résultera de la proposition suivante :'", 'colon (enlarged crop)',
    'full stop', 'punctuation', None, 'high', r'la proposition suivante.', r'la proposition suivante~:')
add(75, "Proposition (19.1.10): 'on suppose vérifiée l'une des conditions suivantes'", "'l'une' upright (enlarged crop)",
    'italic (statement environment)', 'convention', 6, 'high', r"vérifiée l'une des", r"vérifiée \textup{l'une} des")
add(75, 'Proposition (19.1.10), label (i)', '(i) upright', 'italic', 'convention', 6, 'high',
    r'\item[(i)] $\mathfrak J$ est nilpotent', r'\item[\textup{(i)}] $\mathfrak J$ est nilpotent', 'GLOBAL_ISSUES 16.')
add(75, 'Proposition (19.1.10), label (ii)', '(ii) upright', 'italic', 'convention', 6, 'high',
    r'\item[(ii)] $\mathfrak J$ est contenu', r'\item[\textup{(ii)}] $\mathfrak J$ est contenu', 'GLOBAL_ISSUES 16.')
add(75, "Proposition (19.1.10), after (ii): 'Alors, pour que u soit inversible à gauche'", 'new indented paragraph',
    'no blank line after \\end{enumerate}: continues the paragraph unindented', 'other', None, 'medium',
    r'\end{enumerate}⏎Alors, pour que', r'\end{enumerate}⏎⏎Alors, pour que')
add(75, "proof of (19.1.10): 'déduit par passage aux quotients soit l'identité'", "'identité' italic", 'upright', 'italics', None, 'high',
    r"soit l'identité", r"soit l'\emph{identité}")
add(75, "proof of (19.1.10) (i): 'gr^0(w) = w_0 est l'identité'", "'identité' italic", 'upright', 'italics', None, 'high',
    r"est l'identité", r"est l'\emph{identité}")
add(75, "proof of (19.1.10) (ii): 'lorsque A est un anneau local'", "'local' italic", 'upright', 'italics', None, 'high',
    r'un anneau local.', r'un anneau \emph{local}.')
add(75, "proof of (19.1.10) (ii): 'J est l'idéal maximal J_0 de A'", "'maximal' italic", 'upright', 'italics', None, 'high',
    r"l'idéal maximal⏎$\mathfrak J_0$", r"l'idéal \emph{maximal}⏎$\mathfrak J_0$")

# ---------------- checks ----------------
bad = 0
for f in F:
    fx = f['fix']
    if fx is None:
        continue
    txt = open(RUN + 'page_%03d.tex' % f['page'], encoding='utf-8').read().replace('\r\n', '\n')
    n = txt.count(fx['old'])
    if n != 1:
        bad += 1
        print('NOT UNIQUE', n, f['page'], repr(fx['old']))
    if fx['old'] == fx['new']:
        bad += 1
        print('NO-OP', f['page'], repr(fx['old']))
# overlapping edits on the same page
from collections import defaultdict
spans = defaultdict(list)
for i, f in enumerate(F):
    fx = f['fix']
    if fx is None:
        continue
    txt = open(RUN + 'page_%03d.tex' % f['page'], encoding='utf-8').read().replace('\r\n', '\n')
    s = txt.find(fx['old'])
    spans[f['page']].append((s, s + len(fx['old']), i))
for p, lst in spans.items():
    lst.sort()
    for a, b in zip(lst, lst[1:]):
        if b[0] < a[1]:
            bad += 1
            print('OVERLAP p.', p, F[a[2]]['where'][:60], '|', F[b[2]]['where'][:60])
json.dump(F, open(OUT, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
from collections import Counter
c = Counter((f['page'], 'misprint' if f['kind'] == 'misprint_in_print' else ('convention' if f['kind'] == 'convention' else 'normal')) for f in F)
for p in range(71, 76):
    print(p, c[(p, 'normal')], c[(p, 'convention')], c[(p, 'misprint')])
print('total', len(F), 'problems', bad)
