import json, sys

BASE = 'user/Documents/ega_scan_check_20261101/run_0IV1'
OUT = BASE + '/findings_131_135.json'
R = '\\mathfrak{R}'
K = '\\mathfrak{K}'
FK = '\U0001D50E'  # Fraktur K


def J(*parts):
    return '\n'.join(parts)


def page_text(p):
    with open(f'{BASE}/page_{p:03d}.tex', encoding='utf-8', newline='') as f:
        return f.read().replace('\r\n', '\n')


F = []


def add(page, where, scan, tex, kind, fix, note='', conv=None, conf='high'):
    F.append({'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind,
              'convention': conv, 'confidence': conf, 'fix': fix, 'note': note})


KNOTE = ('Wrong letter: the print has Fraktur K (' + FK + '), the same glyph as the ' + FK +
         ' of 0_IV pp. 52-54 (GLOBAL_ISSUES item 63); the TeX writes \\mathfrak{R}. All 81 '
         '\\mathfrak{R} on pp. 133-135 are this letter in the print (pp. 133: 27, 134: 17, 135: 37).')


def kfix(page, where, old):
    assert R in old, old
    add(page, where, FK + ' (Fraktur K)', '\\mathfrak{R}', 'symbol',
        {'old': old, 'new': old.replace(R, K)}, KNOTE)


# ---------------------------------------------------------------- page 131
add(131, "proof of (20.5.5): 'p_{B'/A'} s'identifie alors \u00e0 p_{B/A}\u22971_{A'}'",
    "p_{B/A}\u22971_{A'}: identity map with the old-style figure 1 (same glyph as the final 1 of (20.5.5.1))",
    "p_{B/A}\\otimes\\mathrm{I}_{A'} (roman capital letter I)", 'symbol',
    {'old': 'p_{B/A}\\otimes\\mathrm{I}_{A\'}', 'new': 'p_{B/A}\\otimes1_{A\'}'},
    'The print has the figure 1, not a letter: the TeX writes the same printed glyph as 1 in '
    '$\\operatorname{Hom}(\\delta_{C/B/A},1_L)$ (p. 134) and 1_B, 1_{L} in ega0-18. ega0-20-fr.tex writes the '
    'identity \\mathrm{I}_X 12 times (pp. 117-131); only this one is on pp. 131-135.')

add(131, "(20.5.6), last sentence: 'ces homomorphismes ne sont autres (\u2026) que les homomorphismes (20.2.1.2) et (20.2.1.3) respectivement'",
    "'ne sont autres', 'que les homomorphismes' and 'et' italic; the parenthesis, the references and 'respectivement' roman",
    'all upright (no \\emph)', 'italics',
    {'old': J('ces homomorphismes ne sont',
              'autres (\u00e0 une identification canonique pr\u00e8s) que les homomorphismes',
              '\\sref{0.20.2.1.2-fr} et \\sref{0.20.2.1.3-fr} respectivement.'),
     'new': J('ces homomorphismes \\emph{ne sont',
              'autres} (\u00e0 une identification canonique pr\u00e8s) \\emph{que les homomorphismes}',
              '\\sref{0.20.2.1.2-fr} \\emph{et} \\sref{0.20.2.1.3-fr} respectivement.')})

add(131, "Th\u00e9or\u00e8me (20.5.7) (ii): '(pour les topologies discr\u00e8tes (cf. (19.9.1)))'",
    "'(cf. (19.9.1))' roman inside the italic statement",
    "'(cf. \\sref{0.19.9.1-fr})' italic (theorem environment)", 'convention',
    {'old': '(cf. \\sref{0.19.9.1-fr})', 'new': '\\textup{(cf. \\sref{0.19.9.1-fr})}'},
    'Roman words inside an italic statement.', conv=6)

add(131, "proof of (20.5.7) (ii): 'la suite 0\u2192Hom_C(\u2026)\u21920 est exacte; compte tenu de'",
    "'exacte' italic", "'exacte' upright", 'italics',
    {'old': 'est exacte ; compte tenu', 'new': 'est \\emph{exacte} ; compte tenu'})

add(131, "proof of (20.5.7) (ii): 'cette condition \u00e9quivaut \u00e0 Exalcom_{B/A}(C, L)=0 pour tout C-module L'",
    'Exalcom_{B/A}(C, L)=0 set in the running text (start of the last line of the page)',
    'formula displayed with \\[ \\]', 'other',
    {'old': J('\\[', '  \\operatorname{Exalcom}_{B/A}(C,L)=0', '\\]', 'pour tout'),
     'new': '$\\operatorname{Exalcom}_{B/A}(C,L)=0$ pour tout'},
    'Formula displayed where the print has it inline; no connecting words lost.')

# ---------------------------------------------------------------- page 132
add(132, "proof of (20.5.8): 'Hom_C(\u03a9\u00b9_{C/B}, L)=0 pour tout C-module L'",
    "'tout' italic", "'tout' upright", 'italics',
    {'old': '=0$ pour tout $C$-module $L$, donc', 'new': '=0$ pour \\emph{tout} $C$-module $L$, donc'})

add(132, "proof of (20.5.9): 'pour les topologies discr\u00e8tes (19.10.3, (ii))'",
    '(19.10.3, (ii)).', "\\sref{0.19.10.3-fr}, (ii). typesets '(19.10.3), (ii).'", 'punctuation',
    {'old': '\\sref{0.19.10.3-fr}, (ii).', 'new': '(\\ref{0.19.10.3-fr}, (ii)).'},
    "\\sref adds its own parentheses; ega0-20-fr.tex has 8 '\\sref{...}, (i...)' of this kind.")

add(132, "proof of (20.5.10): 'cela r\u00e9sulte de (20.4.13, (i)) et de (20.5.9)'",
    '(20.4.13, (i)) et de', "\\sref{0.20.4.13-fr}, (i) et de typesets '(20.4.13), (i) et de'", 'punctuation',
    {'old': '\\sref{0.20.4.13-fr}, (i) et de', 'new': '(\\ref{0.20.4.13-fr}, (i)) et de'},
    'Same pattern as the previous finding.')

# ---------------------------------------------------------------- page 133
add(133, "(20.5.11): 'Mais en fait, \u03b4_{C/B/A} est un homomorphisme de C-modules'",
    "'modules' italic (C-modules)", "'modules' upright", 'italics',
    {'old': '$C$-modules, car', 'new': '$C$-\\emph{modules}, car'})

add(133, "(20.5.11): 'd(xy)\u2261xdy (mod. " + FK + ".\u03a9\u00b9_{B/A})'",
    "'(mod. " + FK + ".\u03a9\u00b9_{B/A})' with a full stop after 'mod'",
    "\\pmod{\\mathfrak{R}.\\Omega^1_{B/A}} typesets '(mod \u211c.\u03a9\u00b9_{B/A})' without the stop", 'punctuation',
    {'old': '$d(xy)\\equiv xdy\\pmod{\\mathfrak{R}.\\Omega^1_{B/A}}$',
     'new': '$d(xy)\\equiv xdy$ (mod.~$\\mathfrak{K}.\\Omega^1_{B/A}$)'},
    'Includes the Fraktur K letter fix for this occurrence (see the \\mathfrak{R} findings). Same form as the '
    'EGA II p. 20-24 \\pmod fix.')

add(133, "(20.5.12.1): '\u2026 \u2192 \u03a9\u00b9_{C/A} \u2192 0'",
    'no punctuation after the final 0', "'\\longrightarrow 0,' (comma added)", 'punctuation',
    {'old': J('\\Omega^1_{C/A}\\longrightarrow 0,', '\\end{equation}'),
     'new': J('\\Omega^1_{C/A}\\longrightarrow 0', '\\end{equation}')})

add(133, "Th\u00e9or\u00e8me (20.5.12) (iv) 'Il y a correspondance biunivoque canonique \u2026 E\u2192C.'",
    'printed p. 133 ends with (iii) c) \u2026 par ' + FK + '/' + FK + '\u00b2.; item (iv) is the first text of printed p. 134',
    'item (iv) stands before \\oldpage[0\\textsubscript{IV-1}]{134} (the marker stands after \\begin{proof})', 'marker',
    {'old': '  \\item[\\rm(iv)] Il y a correspondance',
     'new': J('\\oldpage[0\\textsubscript{IV-1}]{134}', '  \\item[\\rm(iv)] Il y a correspondance')},
    'Marker move, part 1 of 2: insert the p. 134 marker before (iv); the p. 134 marker finding removes the old '
    'marker after \\begin{proof}. Apply both (order does not matter).')

for where, old in [
    ("(20.5.11): '" + FK + " un id\u00e9al de B'", '$\\mathfrak{R}$ un id\u00e9al de $B$,'),
    ("(20.5.11): 'la A-alg\u00e8bre quotient B/" + FK + "'", 'quotient $B/\\mathfrak{R}$, et consid\u00e9rons'),
    ("(20.5.11.1): '\u03b4 : " + FK + " \u2192 B'", '\\delta:\\mathfrak{R}\\longrightarrow'),
    ("(20.5.11): '\u03b4(" + FK + "\u00b2) \u2282 " + FK + ".\u03a9\u00b9_{B/A}'", '$\\delta(\\mathfrak{R}^2)\\subset\\mathfrak{R}.\\Omega^1_{B/A}$'),
    ("(20.5.11.2): '\u03b4_{C/B/A} : " + FK + "/" + FK + "\u00b2 \u2192'", '\\delta_{C/B/A}:\\mathfrak{R}/\\mathfrak{R}^2\\longrightarrow'),
    ("(20.5.11.2): '\u03a9\u00b9_{B/A}/(" + FK + ".\u03a9\u00b9_{B/A})'", '\\Omega^1_{B/A}/(\\mathfrak{R}.\\Omega^1_{B/A}).'),
    ("(20.5.11): 'y\u2208" + FK + "'", '$y\\in\\mathfrak{R}$'),
    ("(20.5.11): 'ydx\u2208" + FK + ".\u03a9\u00b9_{B/A}'", '$ydx\\in\\mathfrak{R}.\\Omega^1_{B/A}$'),
    ("(20.5.11): 'comme " + FK + " annule les deux membres'", '$\\mathfrak{R}$ annule'),
    ("(20.5.11), second paragraph: '" + FK + "\u2032 un id\u00e9al de B\u2032'", "$\\mathfrak{R}'$ un id\u00e9al de $B'$"),
    ("(20.5.11): 'u(" + FK + ") \u2282 " + FK + "\u2032 et C\u2032=B\u2032/" + FK + "\u2032'", "$u(\\mathfrak{R})\\subset\\mathfrak{R}'$ et $C'=B'/\\mathfrak{R}'$"),
    ("diagram (20.5.11.3), top left '" + FK + "/" + FK + "\u00b2'", '\\mathfrak{R}/\\mathfrak{R}^2 \\ar[r]^-{\\delta_{C/B/A}}'),
    ("diagram (20.5.11.3), bottom left '" + FK + "\u2032/" + FK + "\u2032\u00b2'", "\\mathfrak{R}'/\\mathfrak{R}'^2"),
    ("Th\u00e9or\u00e8me (20.5.12): 'quotient B/" + FK + "'", '$B/\\mathfrak{R}$, $u:B\\to C$'),
    ("(20.5.12.1): '" + FK + "/" + FK + "\u00b2 \u2192'", J('\\mathfrak{R}/\\mathfrak{R}^2', '  \\xrightarrow{\\delta_{C/B/A}}')),
    ("(20.5.12) (ii): 'E=B/" + FK + "\u00b2'", 'pose $E=B/\\mathfrak{R}^2$,'),
    ("(20.5.12) (iii) c): 'La A-alg\u00e8bre E=B/" + FK + "\u00b2'", '$E=B/\\mathfrak{R}^2$ est une extension'),
    ("(20.5.12) (iii) c): 'par " + FK + "/" + FK + "\u00b2'", 'par $\\mathfrak{R}/\\mathfrak{R}^2$.'),
]:
    kfix(133, where, old)

# ---------------------------------------------------------------- page 134
add(134, 'top of p. 134: Th\u00e9or\u00e8me (20.5.12) (iv)',
    'printed p. 134 begins with (iv) Il y a correspondance biunivoque canonique \u2026 E\u2192C., then (i) Comme u est surjectif',
    'the marker stands after \\begin{proof}, so (iv) is in the p. 133 segment', 'marker',
    {'old': J('\\oldpage[0\\textsubscript{IV-1}]{134}', '(i) Comme'), 'new': '(i) Comme'},
    'Marker move, part 2 of 2: remove the marker here; the p. 133 marker finding inserts it before \\item[\\rm(iv)]. '
    'Apply both (order does not matter).')

add(134, "(20.5.12.2): '\u2026 \u2192 Exalcom_A(B, L)'",
    'no punctuation after Exalcom_A(B, L) (the display is broken over two lines in the print)',
    "'\\operatorname{Exalcom}_A(B,L),' (comma added)", 'punctuation',
    {'old': J('\\operatorname{Exalcom}_A(B,L),', '\\end{equation}'),
     'new': J('\\operatorname{Exalcom}_A(B,L)', '\\end{equation}')})

add(134, "(20.5.12.4): '\u2026 \u2192 \u03a9\u00b9_{E/A} \u2192 0'",
    'no punctuation after the final 0', "'\\longrightarrow 0,' (comma added)", 'punctuation',
    {'old': J('\\Omega^1_{E/A}\\longrightarrow 0,', '\\end{equation}'),
     'new': J('\\Omega^1_{E/A}\\longrightarrow 0', '\\end{equation}')})

add(134, "proof (ii), display after (20.5.12.4): '" + FK + "\u00b2/" + FK + "\u2074\u2297_E C \u2192(\u03b4\u2032) \u03a9\u00b9_{B/A}\u2297_B C \u2192 \u2026'",
    "first arrow labelled \u03b4\u2032 (the map \u03b4\u2032 is used in the next sentence: 'l'image \u03b4\u2032(\u03b6\u22971)')",
    'plain \\longrightarrow without label', 'missing',
    {'old': '\\mathfrak{R}^2/\\mathfrak{R}^4\\otimes_E C\\longrightarrow',
     'new': "\\mathfrak{K}^2/\\mathfrak{K}^4\\otimes_E C\\xrightarrow{\\delta'}"},
    'Includes the Fraktur K letter fix for the two \\mathfrak{R} of this line.')

add(134, "proof (ii): paragraph 'Or, si x, y sont deux \u00e9l\u00e9ments de " + FK + "'",
    "'Or, si x, y' begins an indented paragraph after the display", 'no blank line after \\]', 'other',
    {'old': J('\\]', 'Or, si'), 'new': J('\\]', '', 'Or, si')},
    'Paragraph break as printed (indented line).')

add(134, "proof (iii): 'est exacte et scind\u00e9e, et il revient au m\u00eame'",
    "'exacte' and 'scind\u00e9e' italic, 'et' between them roman",
    '\\emph{exacte et scind\u00e9e} (italic et)', 'italics',
    {'old': 'est \\emph{exacte et scind\u00e9e}, et il revient',
     'new': 'est \\emph{exacte} et \\emph{scind\u00e9e}, et il revient'})

add(134, "proof (iii): 'l'\u00e9quivalence des conditions a) et b) (cf. (18.3.6.2))'",
    "'a)' and 'b)' italic", "'a)' and 'b)' upright", 'italics',
    {'old': 'a) et b) (cf. (18.3.6.2)).', 'new': '\\emph{a)} et \\emph{b)} (cf. (18.3.6.2)).'})

add(134, "proof (iii): 'Le fait que b) entra\u00eene c) provient'",
    "'b)' and 'c)' italic", "'b)' and 'c)' upright", 'italics',
    {'old': 'Le fait que b) entra\u00eene c) provient', 'new': 'Le fait que \\emph{b)} entra\u00eene \\emph{c)} provient'})

add(134, "proof (iii): 'Inversement, c) entra\u00eene b), car toute B-extension de C'",
    "'c)', 'b)' and 'extension' (of B-extension) italic", 'all upright', 'italics',
    {'old': J('Inversement, c)', 'entra\u00eene b), car toute $B$-extension de'),
     'new': J('Inversement, \\emph{c)}', 'entra\u00eene \\emph{b)}, car toute $B$-\\emph{extension} de')})

add(134, "proof (iii): '(consid\u00e9r\u00e9 comme B-extension)'",
    "'extension' italic", "'extension' upright", 'italics',
    {'old': '(consid\u00e9r\u00e9 comme $B$-extension)', 'new': '(consid\u00e9r\u00e9 comme $B$-\\emph{extension})'})

add(134, "end of p. 134: 'par l'homomorphisme' / top of p. 135 'w_* : Exan_B(\u2026)'",
    "the sentence runs on: printed p. 135 begins 'w_* : Exan_B(C, " + FK + "/" + FK + "\u00b2) \u2192 \u2026' at the left margin, no paragraph break",
    'blank line between \u2018par l\u2019homomorphisme\u2019 and \\oldpage[0\\textsubscript{IV-1}]{135}', 'other',
    {'old': "par l'homomorphisme\n\n", 'new': "par l'homomorphisme\n"},
    'Paragraph break the print does not have (page break mid-sentence, GLOBAL_ISSUES item 20).')

for where, old in [
    ("proof (i): 'Hom_C(" + FK + "/" + FK + "\u00b2, L); on d\u00e9duit donc'", '$\\operatorname{Hom}_C(\\mathfrak{R}/\\mathfrak{R}^2,L)$'),
    ("(20.5.12.3): 'Hom_C(" + FK + "/" + FK + "\u00b2, L)'", '\\xrightarrow{\\varphi}\\operatorname{Hom}_C(\\mathfrak{R}/\\mathfrak{R}^2,L)'),
    ("proof (ii): '\u00e0 l'id\u00e9al " + FK + "\u00b2'", "l'id\u00e9al $\\mathfrak{R}^2$"),
    ("(20.5.12.4): '" + FK + "\u00b2/" + FK + "\u2074 \u2192'", '\\mathfrak{R}^2/\\mathfrak{R}^4\\longrightarrow'),
    ("proof (ii): 'deux \u00e9l\u00e9ments de " + FK + "'", '\u00e9l\u00e9ments de $\\mathfrak{R}$'),
    ("proof (ii): 'la classe de xy mod. " + FK + "\u2074'", 'mod. $\\mathfrak{R}^4$'),
    ("(20.5.12.5): '0 \u2192 " + FK + "/" + FK + "\u00b2'", '0\\longrightarrow\\mathfrak{R}/\\mathfrak{R}^2'),
    ("proof (iii): 'la A-extension E de C par " + FK + "/" + FK + "\u00b2 est A-triviale'", '$\\mathfrak{R}/\\mathfrak{R}^2$ est $A$-triviale'),
    ("proof (iii): 'E\u2295_{" + FK + "/" + FK + "\u00b2}L'", '$E\\oplus_{\\mathfrak{R}/\\mathfrak{R}^2}L$'),
]:
    kfix(134, where, old)

# ---------------------------------------------------------------- page 135
add(135, "proof (iii), cont.: 'Le fait que c) entra\u00eene b) r\u00e9sulte alors'",
    "'c)' and 'b)' italic", "'c)' and 'b)' upright", 'italics',
    {'old': 'Le fait que c) entra\u00eene b) r\u00e9sulte', 'new': 'Le fait que \\emph{c)} entra\u00eene \\emph{b)} r\u00e9sulte'})

add(135, "diagram (18.3.6.5) as used in the proof, bottom right 'Exan_A(C, L)'",
    'no full stop after Exan_A(C, L)', "'\\operatorname{Exan}_A(C,L).' (full stop added)", 'punctuation',
    {'old': J('\\operatorname{Exan}_A(C,L).', '}'), 'new': J('\\operatorname{Exan}_A(C,L)', '}')})

add(135, "proof (iv): 'tels que le compos\u00e9 " + FK + "/" + FK + "\u00b2 \u2192(d_{E/A}) \u03a9\u00b9_{E/A} \u2192(h) " + FK + "/" + FK + "\u00b2 soit l'identit\u00e9'",
    "the composite is set in the running text ('tels que le compos\u00e9 \u2026 soit l'identit\u00e9. Par tensori-')",
    'formula displayed with \\[ \\]', 'other',
    {'old': J('\\[', '  \\mathfrak{R}/\\mathfrak{R}^2\\xrightarrow{d_{E/A}}',
              '  \\Omega^1_{E/A}\\xrightarrow{h}\\mathfrak{R}/\\mathfrak{R}^2', '\\]', ''),
     'new': J('$\\mathfrak{K}/\\mathfrak{K}^2\\xrightarrow{d_{E/A}}\\Omega^1_{E/A}\\xrightarrow{h}\\mathfrak{K}/\\mathfrak{K}^2$', '')},
    'Formula displayed where the print has it inline; no connecting words lost. Includes the Fraktur K letter fix '
    'for the four \\mathfrak{R} of this formula.')

add(135, "proof (iv): 'h \u21dd h\u22971 est un isomorphisme de l'ensemble'",
    'wavy arrow (\u21dd / \\leadsto)', '\\mapsto', 'symbol',
    {'old': '$h\\mapsto h\\otimes1$', 'new': '$h\\leadsto h\\otimes1$'},
    'Not convention 3: the print has the wavy arrow (cf. GLOBAL_ISSUES item 33).')

add(135, "Exemple (20.5.13): paragraph 'On en conclut que \u03a9\u00b9_{C/A} est isomorphe'",
    "'On en conclut' begins an indented paragraph after the display of dP_\u03bb", 'no blank line after \\]', 'other',
    {'old': J('\\]', 'On en conclut'), 'new': J('\\]', '', 'On en conclut')},
    'Paragraph break as printed (indented line).')

for where, old in [
    ("top line: 'w_* : Exan_B(C, " + FK + "/" + FK + "\u00b2) \u2192 Exan_B(C, L)'", '$w_*:\\operatorname{Exan}_B(C,\\mathfrak{R}/\\mathfrak{R}^2)'),
    ("'un B-homomorphisme w : " + FK + "/" + FK + "\u00b2\u2192L'", '$w:\\mathfrak{R}/\\mathfrak{R}^2\\to L$'),
    ("diagram, top left 'Exan_B(C, " + FK + "/" + FK + "\u00b2)'", J('\\operatorname{Exan}_B(C,\\mathfrak{R}/\\mathfrak{R}^2)', '    \\ar[r]^{w_*}')),
    ("diagram, bottom left 'Exan_A(C, " + FK + "/" + FK + "\u00b2)'", '\\operatorname{Exan}_A(C,\\mathfrak{R}/\\mathfrak{R}^2)'),
    ("proof (iv): 'D\u2208D\u00e9r_A(E, " + FK + "/" + FK + "\u00b2)'", '$D\\in\\operatorname{D\\acute{e}r}_A(E,\\mathfrak{R}/\\mathfrak{R}^2)$'),
    ("proof (iv): 'D(x)=x dans " + FK + "/" + FK + "\u00b2'", '$\\mathfrak{R}/\\mathfrak{R}^2$, donc aussi'),
    ("proof (iv): 'h : \u03a9\u00b9_{E/A} \u2192 " + FK + "/" + FK + "\u00b2'", '$h:\\Omega^1_{E/A}\\to\\mathfrak{R}/\\mathfrak{R}^2$'),
    ("proof (iv): '(puisque " + FK + "/" + FK + "\u00b2 est un C-module) que le compos\u00e9'", '$\\mathfrak{R}/\\mathfrak{R}^2$ est un $C$-module) que'),
    ("proof (iv), display: '" + FK + "/" + FK + "\u00b2 \u2192(\u03b4_{C/E/A})'", '\\mathfrak{R}/\\mathfrak{R}^2\\xrightarrow{\\delta_{C/E/A}}'),
    ("proof (iv), display: '\u2192(h\u22971) " + FK + "/" + FK + "\u00b2'", J('\\xrightarrow{h\\otimes1}', '  \\mathfrak{R}/\\mathfrak{R}^2')),
    ("proof (iv): 'or, puisque " + FK + "/" + FK + "\u00b2 est un C-module'", 'puisque $\\mathfrak{R}/\\mathfrak{R}^2$ est un'),
    ("proof (iv): 'Hom_E(\u03a9\u00b9_{E/A}, " + FK + "/" + FK + "\u00b2)'", '$\\operatorname{Hom}_E(\\Omega^1_{E/A},\\mathfrak{R}/\\mathfrak{R}^2)$'),
    ("proof (iv): 'Hom_C(\u03a9\u00b9_{E/A}\u2297_E C, " + FK + "/" + FK + "\u00b2)'", '$\\operatorname{Hom}_C(\\Omega^1_{E/A}\\otimes_E C,\\mathfrak{R}/\\mathfrak{R}^2)$'),
    ("Exemple (20.5.13): '" + FK + " un id\u00e9al de B'", '$\\mathfrak{R}$ un id\u00e9al de $B$, $(P_\\lambda)$'),
    ("Exemple (20.5.13): 'g\u00e9n\u00e9rateurs de " + FK + " et C=B/" + FK + "'", '$\\mathfrak{R}$ et $C=B/\\mathfrak{R}$'),
    ("Exemple (20.5.13): 'l'image de " + FK + "/" + FK + "\u00b2 par \u03b4_{C/B/A}'", '$\\mathfrak{R}/\\mathfrak{R}^2$ par $\\delta_{C/B/A}$'),
    ("(20.5.14.1): '0 \u2192 " + FK + "/" + FK + "\u00b2'", '0\\longrightarrow\\mathfrak{R}/\\mathfrak{R}^2'),
]:
    kfix(135, where, old)

# ---------------------------------------------------------------- checks
ok = True
texts = {p: page_text(p) for p in (131, 132, 133, 134, 135)}
spans = {}
for i, f in enumerate(F):
    fx = f['fix']
    t = texts[f['page']]
    c = t.count(fx['old'])
    if c != 1:
        ok = False
        print('NOT UNIQUE', i, f['page'], c, json.dumps(fx['old'], ensure_ascii=True))
        continue
    a = t.find(fx['old'])
    spans.setdefault(f['page'], []).append((a, a + len(fx['old']), i))
for p, L in spans.items():
    L.sort()
    for (a1, b1, i1), (a2, b2, i2) in zip(L, L[1:]):
        if a2 < b1:
            ok = False
            print('OVERLAP', p, i1, i2)
# every \mathfrak{R} covered
for p, t in texts.items():
    total = t.count(R)
    covered = sum(F[i]['fix']['old'].count(R) for (_, _, i) in spans.get(p, []))
    print('page', p, 'mathfrak R in page:', total, 'covered by fixes:', covered)
    if total != covered:
        ok = False
# simulate application (sequential) to be sure each fix still applies after the earlier ones
for p, t in texts.items():
    s = t
    for f in F:
        if f['page'] != p:
            continue
        if s.count(f['fix']['old']) != 1:
            ok = False
            print('SEQ FAIL', p, json.dumps(f['fix']['old'], ensure_ascii=True))
        s = s.replace(f['fix']['old'], f['fix']['new'])
    print('page', p, 'mathfrak R left after all fixes:', s.count(R))

from collections import Counter
cnt = Counter()
for f in F:
    key = 'misprint' if f['kind'] == 'misprint_in_print' else ('convention' if f['kind'] == 'convention' else 'normal')
    cnt[(f['page'], key)] += 1
for p in (131, 132, 133, 134, 135):
    print(p, cnt[(p, 'normal')], cnt[(p, 'convention')], cnt[(p, 'misprint')])
print('total findings', len(F), 'ok', ok)
if ok and '--write' in sys.argv:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(F, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('written', OUT)
