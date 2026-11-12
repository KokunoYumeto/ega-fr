import json
import os
import sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, 'findings_164_167.json')

F = []


def add(page, where, scan, tex, kind, fix, note, convention=None,
        confidence='high', corrected=None):
    d = {
        'page': page,
        'where': where,
        'scan': scan,
        'tex': tex,
        'kind': kind,
        'convention': convention,
        'confidence': confidence,
        'fix': fix,
    }
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    F.append(d)


# ---------------------------------------------------------------- page 164
P = 164
add(P, "first entry 'S-C-module filtré, ... : 0, 13.6.6', S-C-module filtré",
    "S-C-module filtré: C bold italic",
    r"$S$-$C$-module filtré",
    'font',
    {'old': r"$S$-$C$-module", 'new': r"$S$-$\boldsymbol{C}$-module"},
    "Category letter C bold italic, as in the body (13.6.x); GLOBAL_ISSUES item 33.")
add(P, "first entry, gr(S)-C-module gradué",
    "gr•(S): the letters 'gr' are bold (as heavy as the bold 0 of the reference); the body (0_III p. 77) has a light gr",
    r"$\operatorname{gr}^\bullet(S)$-$C$-module gradué",
    'font',
    {'old': r"filtré, $\operatorname{gr}", 'new': r"filtré, $\mathbf{gr}"},
    "Bold gr only in this index entry (crop at 3x).")
add(P, "first entry, gr(S)-C-module gradué",
    "gr•(S)-C-module gradué: C bold italic",
    r"$C$-module gradué",
    'font',
    {'old': r"$C$-module gradué", 'new': r"$\boldsymbol{C}$-module gradué"},
    "Category letter C bold italic.")
add(P, "first entry, gr(S)-C-module bigradué",
    "gr•(S): 'gr' bold, as in the gradué item before it",
    r"$\operatorname{gr}^{\bullet\bullet}(S)$",
    'font',
    {'old': "\n" + r"$\operatorname{gr}", 'new': "\n" + r"$\mathbf{gr}"},
    "The 'old' is the start of line 5 of page_164.tex (after the line break).")
add(P, "first entry, gr(S)-C-module bigradué",
    "gr•(S)-C-module bigradué: a single bullet, the same as in 'gr•(S)-C-module gradué' (the body, 13.6.5-13.6.6, also writes gr•(S)-C'-module bigradué)",
    r"\operatorname{gr}^{\bullet\bullet}(S)",
    'symbol',
    {'old': r"^{\bullet\bullet}(S)", 'new': r"^\bullet(S)"},
    "Disjoint from the bold-gr fix just before it; both apply.")
add(P, "first entry, gr(S)-C-module bigradué",
    "C bold italic",
    r"$C$-module bigradué",
    'font',
    {'old': r"$C$-module bigradué", 'new': r"$\boldsymbol{C}$-module bigradué"},
    "Category letter C bold italic.")
for word, old in (("C-objet en groupes", r"$C$-objet"),
                  ("C-groupe", r"$C$-groupe"),
                  ("C-anneau", r"$C$-anneau"),
                  ("C-module", r"$C$-module :")):
    add(P, "entry 'C-objet en groupes, C-groupe, C-anneau, C-module : 0, 8.2.3', " + word,
        word + ": C bold italic",
        old,
        'font',
        {'old': old, 'new': old.replace(r"$C$", r"$\boldsymbol{C}$", 1)},
        "Category letter C bold italic.")

# convention 2: bold chapter number in every reference of the index
conv2 = [
    ("S-C-module filtré, ... bigradué", "0, 13.6.6."),
    ("Morphisme de suites spectrales", "0, 11.1.2."),
    ("Nombre géométrique de composantes connexes d'une fibre", "III, 4.3.4."),
    ("C-objet en groupes, ...", "0, 8.2.3."),
    ("Objet des bords, ..., objet des cycles", "cycles :\n0, 11.2.1."),
    ("Objet des images universelles", "0, 13.1.1."),
    ("Objet gradué associé à un système projectif satisfaisant à (ML)", "(ML) : 0, 13.4.2."),
    ("Objet gradué limité inférieurement (supérieurement)", "(supérieurement) : 0, 11.2.1."),
    ("Partie propre (sur Y) d'un préschéma formel", "formel : III, 3.4.1."),
    ("Pleine (sous-catégorie)", "(sous-catégorie) : 0, 8.1.5."),
    ("Pleinement fidèle (foncteur)", "fidèle (foncteur) : 0, 8.1.5."),
    ("Polynôme de Hilbert", "III, 2.5.3."),
    ("Propre (morphisme) de préschémas formels", "formels : III, 3.4.1."),
    ("Représentable (foncteur)", "0, 8.1.8."),
    ("Résolution cohomologique, droite, ...", "0, 11.4.1."),
    ("Résolution de Cartan-Eilenberg droite, injective", "0, 11.4.2."),
    ("Résolution de Cartan-Eilenberg gauche, projective", "0, 11.6.1."),
    ("Rétrocompact (ensemble)", "0, 9.1.1."),
    ("Strict (système projectif)", "projectif) : 0, 13.4.2."),
    ("Suite spectrale dans une catégorie abélienne", "0, 11.1.1."),
    ("Suite spectrale faiblement convergente, ...", "0, 11.1.3."),
    ("Suite spectrale dégénérée", "0, 11.1.6."),
    ("Suite spectrale d'un foncteur relativement à un objet filtré", "0, 13.6.4."),
    ("Suites spectrales d'un bicomplexe", "0, 11.3.2 et 11.3.5."),
    ("Suites spectrales d'hypercohomologie ... complexe", "0, 11.4.3."),
    ("Suites spectrales d'hyperhomologie ... complexe", "0, 11.6.2."),
    ("Suites spectrales d'hyperhomologie ... bicomplexe", "0, 11.7.2."),
    ("Système de coefficients", "0, 11.8.4."),
    ("Unibranche (anneau, point)", "III, 4.3.6."),
    ("Universellement ouvert (morphisme)", "III, 4.3.9."),
]
for entry, old in conv2:
    # bold the chapter number (the first '0, ' or 'III, ' in old that starts the reference)
    if "III, " in old:
        new = old.replace("III, ", r"\textbf{III}, ", 1)
        ch = "III"
    else:
        i = old.index("0, ")
        new = old[:i] + r"\textbf{0}" + old[i + 1:]
        ch = "0"
    ref = old[old.index(ch + ", "):].strip()
    add(P, "entry '" + entry + "'",
        "bold " + ch + " in the reference " + ref,
        ref,
        'convention',
        {'old': old, 'new': new},
        "Bold chapter number in the index reference.",
        convention=2)

# ---------------------------------------------------------------- page 165
P = 165
add(P, "contents table, above the page numbers (before the Chapitre 0 line)",
    "column head 'Pages' (small capitals, a short rule under it) at the top right, above the page numbers",
    "(nothing)",
    'missing',
    {'old': "\\begin{flushleft}\n\\textsc{Chapitre 0.}",
     'new': "\\begin{flushleft}\n\\hfill\\textsc{Pages}\n\n\\textsc{Chapitre 0.}"},
    "As in the EGA II contents (findings 212-217). The short rule under 'Pages' is layout.")
add(P, "contents entry 'Chapitre 0. — Préliminaires (suite) ... 5'",
    "'Préliminaires' bold; '(suite)' light italic (italic parentheses)",
    r"\textbf{Préliminaires (suite)}",
    'italics',
    {'old': r"\textbf{Préliminaires (suite)}", 'new': r"\textbf{Préliminaires} \textit{(suite)}"},
    "")

# ---------------------------------------------------------------- page 166
P = 166
add(P, "top of the contents table (repeated column head), before § 13",
    "'Pages' (small capitals, short rule under it) above the page numbers, as on p. 165",
    "(nothing)",
    'missing',
    {'old': "\\S~13. Limites", 'new': "\\hfill\\textsc{Pages}\n\n\\S~13. Limites"},
    "")

# ---------------------------------------------------------------- page 167
P = 167
add(P, "top of the contents table (repeated column head), before § 5",
    "'Pages' (small capitals, short rule under it) above the page numbers, as on pp. 165-166",
    "(nothing)",
    'missing',
    {'old': "\\S~5. Un théorème", 'new': "\\hfill\\textsc{Pages}\n\n\\S~5. Un théorème"},
    "")
add(P, "contents entry 5.4",
    "Application : comparaison des morphismes de schémas usuels et de morphismes de schémas formels. Schémas formels algébrisables",
    "comparaison de morphismes",
    'word',
    {'old': "comparaison de morphismes", 'new': "comparaison des morphismes"},
    "The contents line has 'des'; the section heading itself (p. 156) has 'de morphismes', which the body TeX matches. Change only the contents line.")
add(P, "contents entry 'Bibliographie (suite) ... 161'",
    "Bibliographie in small capitals, '(suite)' in italic (italic parentheses)",
    r"\textsc{Bibliographie (suite)}",
    'italics',
    {'old': r"\textsc{Bibliographie (suite)}", 'new': r"\textsc{Bibliographie} \textit{(suite)}"},
    "Same as the EGA II contents entry 'Bibliographie (suite)'.")

# ---------------------------------------------------------------- checks
ok = True
by_page = {}
for f in F:
    by_page.setdefault(f['page'], []).append(f)
for page, fs in by_page.items():
    src = open(os.path.join(RUN, 'page_%03d.tex' % page), 'rb').read().decode('utf-8')
    src = src.replace('\r\n', '\n')
    spans = []
    for f in fs:
        if f['fix'] is None:
            continue
        old = f['fix']['old']
        n = src.count(old)
        if n != 1:
            ok = False
            print('NOT UNIQUE', page, n, repr(old))
            continue
        i = src.index(old)
        spans.append((i, i + len(old), old))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            ok = False
            print('OVERLAP', page, repr(a[2]), repr(b[2]))
    # apply all fixes to a copy to make sure they compose
    s = src
    for f in fs:
        if f['fix'] is None:
            continue
        if s.count(f['fix']['old']) != 1:
            ok = False
            print('AFTER-APPLY NOT UNIQUE', page, repr(f['fix']['old']))
            continue
        s = s.replace(f['fix']['old'], f['fix']['new'], 1)
    print(page, 'findings', len(fs))

if not ok:
    sys.exit(1)
with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write('\n')
from collections import Counter
c = Counter((f['page'], 'convention' if f['kind'] == 'convention' else
             'misprint' if f['kind'] == 'misprint_in_print' else 'normal') for f in F)
print(sorted(c.items()))
print('written', OUT, len(F))
