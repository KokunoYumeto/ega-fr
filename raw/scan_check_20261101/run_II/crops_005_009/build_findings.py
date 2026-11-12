"""Build findings_005_009.json for EGA II pp. 5-9 and check every fix's 'old'.

Run: python -I build_findings.py
"""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
RUN = 'user/Documents/ega_scan_check_20261101/run_II'
OUT = RUN + '/findings_005_009.json'
NL = '\n'

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
        'fix': None if old is None else {'old': old, 'new': new},
    }
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    F.append(d)


def bold_ref(page, where, printed, old, new, note=''):
    letter = '0' if '{0,' in old else 'I'
    add(page, where, printed + ' with bold ' + letter,
        printed + ' with plain ' + letter + ' in the link text', 'convention', 2, 'high', old, new, note)


# ---------------- page 5 ----------------
bold_ref(5, "(1.1.1): 'On sait (0, 4.2.4) que l'image directe'", '(0, 4.2.4)',
         r'{0, 4.2.4}', r'{\textbf{0}, 4.2.4}',
         'This line is in ega2-1-fr.tex before its first page marker (the part of page_005.tex after '
         "'% (continued in ega2-1-fr.tex ...)'), i.e. outside the page-5 segment of front-fr.tex.")

# ---------------- page 6 ----------------
bold_ref(6, "(1.1.2): 'on en déduit (0, 4.2.2) un homomorphisme'", '(0, 4.2.2)',
         r'{0, 4.2.2}', r'{\textbf{0}, 4.2.2}')
add(6, "(1.1.2): 'de 𝒪_S-Algèbres g_*(θ) : g_*(𝒪_Y)→g_*(h_*(𝒪_X))=f_*(𝒪_X), autrement dit'",
    'the formula is set inline in the running text, followed by a comma and \'autrement dit\' on the same line',
    r'displayed with \[ ... \]', 'other', None, 'high',
    r'\[' + NL + r'  g_*(\theta):g_*(\mathcal{O}_Y)\to' + NL
    + r'  g_*(h_*(\mathcal{O}_X))=f_*(\mathcal{O}_X),' + NL + r'\]',
    r'$g_*(\theta):g_*(\mathcal{O}_Y)\to g_*(h_*(\mathcal{O}_X))=f_*(\mathcal{O}_X)$,',
    'Layout only (display vs inline); the formula itself matches.')
bold_ref(6, "(1.1.2), second paragraph: 'c'est-à-dire (0, 4.4.1) un homomorphisme'", '(0, 4.4.1)',
         r'{0, 4.4.1}', r'{\textbf{0}, 4.4.1}')
add(6, "(1.1.2), second paragraph: 'Alors g_*(u) : g_*(𝒢)→g_*(h_*(ℱ))=f_*(ℱ) est un homomorphisme'",
    "the formula is set inline in the running text ('Alors' ends the line, the formula and 'est un homomorphisme' follow on the next line)",
    r'displayed with \[ ... \]', 'other', None, 'high',
    r'\[' + NL + r'  g_*(u):g_*(\mathcal{G})\to g_*(h_*(\mathcal{F}))=f_*(\mathcal{F})' + NL + r'\]',
    r'$g_*(u):g_*(\mathcal{G})\to g_*(h_*(\mathcal{F}))=f_*(\mathcal{F})$',
    'Layout only (display vs inline); the formula itself matches.')
add(6, "Définition (1.2.1): 'On dit que X est affine au-dessus de S s'il existe'",
    "'affine au-dessus de S' in the same italic as the rest of the statement (no change of face)",
    r'\emph{affine au-dessus de $S$} inside the \itshape definition environment (comes out upright)',
    'convention', 6, 'high',
    r'\emph{affine au-dessus de $S$}', r'affine au-dessus de $S$',
    'Printed italic words left upright by \\emph inside the italic environment; drop the \\emph. Checked on a crop.')
bold_ref(6, "Exemple (1.2.2): '(I, 4.2.3 et 4.2.4)'", '(I, 4.2.3 et 4.2.4)',
         r'{I, 4.2.3}', r'{\textbf{I}, 4.2.3}')

# ---------------- page 7 ----------------
bold_ref(7, "Remarque (1.2.3), end: 'est affine au-dessus de S (I, 5.5.10)'", '(I, 5.5.10)',
         r'{I, 5.5.10}', r'{\textbf{I}, 5.5.10}')
add(7, "Proposition (1.2.4): '(autrement dit, est un S-schéma).'",
    "the parenthesis is upright: '(autrement dit, est un S-' roman, 'schéma' italic, ')' roman",
    'the whole parenthesis italic (inside the \\itshape proposition environment)',
    'convention', 6, 'high',
    r'(autrement dit, est un $S$-schéma)',
    r'\textup{(autrement dit, est un $S$-\emph{schéma})}',
    'Checked on a crop. Inside \\textup the \\emph gives the printed italic schéma.')
bold_ref(7, "proof of (1.2.4): 'Cela résulte aussitôt de (I, 5.5.5)'", '(I, 5.5.5)',
         r'{I, 5.5.5}', r'{\textbf{I}, 5.5.5}')
bold_ref(7, "proof of (1.2.4): 'et (I, 5.5.8).'", '(I, 5.5.8)',
         r'{I, 5.5.8}', r'{\textbf{I}, 5.5.8}')
bold_ref(7, "proof of (1.2.5): 'f^{-1}(U)=D(φ(g)) (I, 1.2.2.2)'", '(I, 1.2.2.2)',
         r'{I, 1.2.2.2}', r'{\textbf{I}, 1.2.2.2}')
bold_ref(7, "proof of (1.2.6): 'cela résulte de (I, 9.2.2, a))'", '(I, 9.2.2, a))',
         r'\hyperref[I.9.2.2-fr]{I, 9.2.2', r'\hyperref[I.9.2.2-fr]{\textbf{I}, 9.2.2',
         "Independent of the italic 'a)' finding at the same reference (either order works).")
add(7, "proof of (1.2.6): 'cela résulte de (I, 9.2.2, a))'",
    "'a)' italic (the a and its closing parenthesis); the outer ')' roman",
    'a) upright', 'italics', None, 'high',
    r'9.2.2, a)}', r'9.2.2, \emph{a)}}',
    'Checked on a 4x crop. Independent of the bold-I finding at the same reference (either order works).')
add(7, "Proposition (1.2.7): 'l'application h→𝒜(h) de l'ensemble'",
    'plain arrow h→𝒜(h)', r'h\mapsto\mathcal{A}(h)', 'convention', 3, 'high',
    r'$h\mapsto\mathcal{A}(h)$', r'$h\to\mathcal{A}(h)$', 'Checked on a crop: no bar at the tail.')
add(7, "Proposition (1.2.7): 'Hom(𝒜(X), 𝒜(Y)) (1.1.2) est bijective'",
    'the reference (1.1.2) upright', 'italic (inside the \\itshape proposition environment)',
    'convention', 6, 'high',
    r'(\hyperref[II.1.1.2-fr]{1.1.2})', r'\textup{(\hyperref[II.1.1.2-fr]{1.1.2})}',
    'Checked on a crop.')
add(7, "proof of (1.2.7): 'ω définit un homomorphisme ω_U=Γ(U, ω) : Γ(f^{-1}(U), 𝒪_X)→Γ(g^{-1}(U), 𝒪_Y) de Γ(U, 𝒪_S)-algèbres'",
    'the formula is set inline in the running text, followed on the same line by \'de Γ(U, 𝒪_S)-algèbres. En particulier,\'',
    r'displayed with \[ ... \]', 'other', None, 'high',
    r'\[' + NL + r'  \omega_U=\Gamma(U,\omega):' + NL + r'  \Gamma(f^{-1}(U),\mathcal{O}_X)\to' + NL
    + r'  \Gamma(g^{-1}(U),\mathcal{O}_Y)' + NL + r'\]',
    r'$\omega_U=\Gamma(U,\omega):\Gamma(f^{-1}(U),\mathcal{O}_X)\to\Gamma(g^{-1}(U),\mathcal{O}_Y)$',
    'Layout only (display vs inline); the formula itself matches.')
bold_ref(7, "proof of (1.2.7): 'puisque X est affine (I, 2.2.4)'", '(I, 2.2.4)',
         r'{I, 2.2.4}', r'{\textbf{I}, 2.2.4}')
add(7, "proof of (1.2.7): 'On peut se borner au cas où U=D(λ), avec λ∈S ; alors'",
    'λ∈S', r'\lambda\in S (same as the print)', 'misprint_in_print', None, 'high',
    None, None,
    'The TeX keeps the printed reading. λ must be an element of A: S=Spec(A), D(λ) is a basic open set and '
    'μ=ρ(λ) with ρ : A→B on the same line. Checked on a crop. Not in the EGA III list of errata to EGA II.',
    corrected=r'\lambda\in A')
bold_ref(7, "proof of (1.2.7): 'des anneaux de fractions (0, 1.2.4).'", '(0, 1.2.4)',
         r'{0, 1.2.4}', r'{\textbf{0}, 1.2.4}')

# ---------------- page 8 ----------------
bold_ref(8, "proof of (1.3.1): 'X_U est un S-préschéma (I, 1.6.1)'", '(I, 1.6.1)',
         r'{I, 1.6.1}', r'{\textbf{I}, 1.6.1}')
bold_ref(8, "proof of (1.3.1): 'à ℬ|U (I, 1.3.7, 1.3.13 et 1.6.3)'", '(I, 1.3.7, 1.3.13 et 1.6.3)',
         r'{I, 1.3.7}', r'{\textbf{I}, 1.3.7}')
bold_ref(8, "proof of (1.3.1): 'θ_{U,V}=φ_U^{-1}∘φ_V (I, 2.3.1)'", '(I, 2.3.1)',
         r'{I, 2.3.1}', r'{\textbf{I}, 2.3.1}')
add(8, "after the proof of (1.3.1): 'ou est le spectre de ℬ, et on le note Spec(ℬ)'",
    "only 'spectre' italic; 'de' upright",
    r'\emph{spectre de $\mathcal{B}$} (de italic)', 'italics', None, 'high',
    r'\emph{spectre de' + NL + r'$\mathcal{B}$}', r'\emph{spectre} de' + NL + r'$\mathcal{B}$',
    'Checked on a crop. The preceding \\emph{associé à la 𝒪_S-Algèbre ℬ} matches the print.')

# ---------------- page 9 ----------------
bold_ref(9, "Exemple (1.3.3): 'a été dédoublé (I, 5.5.11) ;'", '(I, 5.5.11)',
         r'{I, 5.5.11})~;', r'{\textbf{I}, 5.5.11})~;')
bold_ref(9, "Exemple (1.3.3): 'avec les notations de (I, 5.5.11),'", '(I, 5.5.11)',
         r'{I, 5.5.11}),', r'{\textbf{I}, 5.5.11}),')
add(9, "Exemple (1.3.3): '(loc. cit.), donc on a un exemple'",
    "'(loc. cit.)' italic including both parentheses",
    r'(\emph{loc. cit.}) with upright parentheses', 'italics', None, 'medium',
    r'(\emph{loc. cit.})', r'\emph{(loc. cit.)}',
    'Checked on a crop: both parentheses are slanted, unlike the upright parentheses elsewhere on the page.')
add(9, "Corollaire (1.3.7), end: 'soit de type fini (I, 9.6.2).'",
    'the reference (I, 9.6.2) upright', 'italic (inside the \\itshape corollary environment)',
    'convention', 6, 'high',
    r'fini' + NL + r'(\hyperref[I.9.6.2-fr]', r'fini' + NL + r'\upshape(\hyperref[I.9.6.2-fr]',
    'Checked on a crop. The reference ends the statement, so the \\upshape switch (closed by \\end{corollary}) '
    'covers exactly the reference and the final period. Kept clear of the bold-I edit inside the braces, so both '
    'edits apply in either order.')
bold_ref(9, "Corollaire (1.3.7), end: 'soit de type fini (I, 9.6.2).'", '(I, 9.6.2)',
         r'{I, 9.6.2}).' + NL + r'\end{corollary}', r'{\textbf{I}, 9.6.2}).' + NL + r'\end{corollary}',
         'Independent of the \\upshape edit for the same reference.')
bold_ref(9, "proof of (1.3.7): 'Par définition (I, 9.6.2), on est ramené'", '(I, 9.6.2)',
         r'{I, 9.6.2}), on', r'{\textbf{I}, 9.6.2}), on')
bold_ref(9, "proof of (1.3.7): 'le corollaire résulte de (I, 9.6.2) et (I, 6.3.3)'", '(I, 9.6.2)',
         r'{I, 9.6.2}) et', r'{\textbf{I}, 9.6.2}) et')
bold_ref(9, "proof of (1.3.7): 'et (I, 6.3.3).'", '(I, 6.3.3)',
         r'{I, 6.3.3}', r'{\textbf{I}, 6.3.3}')
add(9, "proof of (1.3.7): 'comme Γ(U, B̃)=B, le corollaire résulte de'",
    'Γ(U, B̃)=B', r'\Gamma(U,\widetilde{B})=B (same as the print)', 'misprint_in_print', None, 'low',
    None, None,
    'The TeX keeps the printed reading. U is not defined in this proof: S=Spec(A) is affine and Γ(S, B̃)=B. '
    'The U may echo the notation of (I, 9.6.2) (an affine open U with Γ(U, ℬ)=B), so this may be an intended '
    'shorthand for U=S rather than a misprint; low confidence. Checked on a crop.',
    corrected=r'\Gamma(S,\widetilde{B})=B')
add(9, "Corollaire (1.3.8): 'pour que X soit réduit, il faut et il suffit'",
    "comma after 'réduit'", "no comma ('soit réduit il faut')", 'punctuation', None, 'high',
    r'soit réduit il', r'soit réduit, il', 'Checked on a crop.')
add(9, "Corollaire (1.3.8), end: 'soit réduite (0, 4.1.4).'",
    'the reference (0, 4.1.4) upright', 'italic (inside the \\itshape corollary environment)',
    'convention', 6, 'high',
    r'réduite' + NL + r'(\hyperref[0.4.1.4-fr]', r'réduite' + NL + r'\upshape(\hyperref[0.4.1.4-fr]',
    'Checked on a crop. Same form as for (1.3.7): the \\upshape switch runs to \\end{corollary}; independent of '
    'the bold-0 edit inside the braces.')
bold_ref(9, "Corollaire (1.3.8), end: 'soit réduite (0, 4.1.4).'", '(0, 4.1.4)',
         r'{0, 4.1.4}', r'{\textbf{0}, 4.1.4}',
         'Independent of the \\upshape edit for the same reference.')
bold_ref(9, "proof of (1.3.8): 'le corollaire résulte de (I, 5.1.1)'", '(I, 5.1.1)',
         r'{I, 5.1.1}', r'{\textbf{I}, 5.1.1}')
bold_ref(9, "proof of (1.3.8): 'et (I, 5.1.4).'", '(I, 5.1.4)',
         r'{I, 5.1.4}', r'{\textbf{I}, 5.1.4}')
add(9, "Proposition (1.4.1): 'ℱ (resp. 𝒢) un 𝒪_X-Module'",
    "'(resp. 𝒢)' upright", 'italic (inside the \\itshape proposition environment)',
    'convention', 6, 'high',
    r'(resp. $\mathcal{G}$)', r'\textup{(resp. $\mathcal{G}$)}', 'Checked on a crop.')
add(9, "Proposition (1.4.1): '(resp. un 𝒪_Y-Module) quasi-cohérent'",
    "'(resp.' and ')' upright, 'un' and 'Module' italic",
    'all italic (inside the \\itshape proposition environment)',
    'convention', 6, 'high',
    r'(resp. un' + NL + r'$\mathcal{O}_Y$-Module)',
    r'\textup{(resp.} un' + NL + r'$\mathcal{O}_Y$-Module\textup{)}', 'Checked on a crop.')
add(9, "Proposition (1.4.1): 'l'application (h, u)→(𝒜(h), 𝒜(u))'",
    'plain arrow (h, u)→(𝒜(h), 𝒜(u))', r'(h,u)\mapsto(\mathcal{A}(h),\mathcal{A}(u))',
    'convention', 3, 'high',
    r'$(h,u)\mapsto(', r'$(h,u)\to(', 'Checked on a crop: no bar at the tail.')
add(9, "Proposition (1.4.1), end: '(1.1.2 et 1.1.3) est bijective'",
    "the reference '(1.1.2 et 1.1.3)' upright", 'italic (inside the \\itshape proposition environment)',
    'convention', 6, 'high',
    r'(\hyperref[II.1.1.2-fr]{1.1.2} et' + NL + r'\hyperref[II.1.1.3-fr]{1.1.3})',
    r'\textup{(\hyperref[II.1.1.2-fr]{1.1.2} et' + NL + r'\hyperref[II.1.1.3-fr]{1.1.3})}',
    'Checked on a crop.')
bold_ref(9, "proof of (1.4.1): 'en utilisant (I, 2.2.5)'", '(I, 2.2.5)',
         r'{I, 2.2.5}', r'{\textbf{I}, 2.2.5}')
bold_ref(9, "proof of (1.4.1): 'et (I, 2.2.4), et les détails'", '(I, 2.2.4)',
         r'{I, 2.2.4}', r'{\textbf{I}, 2.2.4}')
add(9, "Corollaire (1.4.2): 'en outre des hypothèses de (1.4.1), on suppose'",
    'the reference (1.4.1) upright', 'italic (inside the \\itshape corollary environment)',
    'convention', 6, 'high',
    r'(\hyperref[II.1.4.1-fr]{1.4.1})', r'\textup{(\hyperref[II.1.4.1-fr]{1.4.1})}',
    'Checked on a crop.')

# ---------------- checks ----------------
ok = True
texts = {}
for p in sorted({f['page'] for f in F}):
    raw = open(f'{RUN}/page_{p:03d}.tex', encoding='utf-8', newline='').read()
    texts[p] = raw.replace('\r\n', '\n')
for f in F:
    if f['fix'] is None:
        if f['kind'] != 'misprint_in_print':
            print('fix None on non-misprint', f['page'], f['where']); ok = False
        continue
    n = texts[f['page']].count(f['fix']['old'])
    if n != 1:
        ok = False
        print('COUNT', n, 'page', f['page'], repr(f['fix']['old']))
# simulate applying all fixes per page, in order and in reverse order
for p, t in texts.items():
    for order in (1, -1):
        s = t
        fixes = [f['fix'] for f in F if f['page'] == p and f['fix']][::order]
        for fx in fixes:
            if s.count(fx['old']) != 1:
                ok = False
                print('ORDER', order, 'page', p, 'old not unique after earlier edits:', repr(fx['old']))
            s = s.replace(fx['old'], fx['new'], 1)
print('all checks passed' if ok else 'CHECK FAILURES')

json.dump(F, open(OUT, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
counts = {}
for f in F:
    c = counts.setdefault(f['page'], [0, 0, 0])
    if f['kind'] == 'convention':
        c[1] += 1
    elif f['kind'] == 'misprint_in_print':
        c[2] += 1
    else:
        c[0] += 1
print(len(F), 'findings written to', OUT)
for p in sorted(counts):
    print(p, '%d/%d/%d' % tuple(counts[p]))
