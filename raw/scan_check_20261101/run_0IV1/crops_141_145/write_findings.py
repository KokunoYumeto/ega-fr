import json
import os
import sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, 'findings_141_145.json')

SETMIN_NOTE = ("Long dash used for a subtraction (GLOBAL_ISSUES 23); \\setmin as in the other "
               "convention-7 fixes, pending that decision. \\setmin is not defined in the IV1 "
               "preamble EGA_IV1_FR.tex (only in preamble-base.tex).")

FRAK_NOTE = ("Same glyph as the Fraktur K identified on 0_IV pp. 52-54 and 133 (GLOBAL_ISSUES 63); "
             "all 14 Fraktur letters on p. 145 have this shape (crops), none is a Fraktur R.")


def F(page, where, scan, tex, kind, conf, old=None, new=None, conv=None, note='', corrected=None):
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
    return d


findings = [
    # ---------------- page 141 ----------------
    F(141, "(20.6.14.1), end of the display u' : Υ_{C/A/Λ} → Υ_{C/B/Λ}",
      "no punctuation after Υ_{C/B/Λ} (crop)",
      "comma after \\Upsilon_{C/B/\\Lambda}",
      'punctuation', 'high',
      r"\Upsilon_{C/B/\Lambda},\\", r"\Upsilon_{C/B/\Lambda}\\"),
    F(141, "(20.6.14.4), left vertical arrow Ω^1_{A/Λ}⊗_A C → Ω^1_{A/Λ}⊗_A C ('la flèche verticale de gauche est l'identité')",
      "an ordinary downward arrow with the isomorphism sign ≀ to its right (crop)",
      "\\ar@{=}[d]: a double line without arrowhead and without ≀",
      'symbol', 'high',
      "\\xymatrix{\n  \\Omega^1_{A/\\Lambda}\\otimes_A C \\ar[r] \\ar@{=}[d]",
      "\\xymatrix{\n  \\Omega^1_{A/\\Lambda}\\otimes_A C \\ar[r] \\ar[d]^{\\wr}"),
    F(141, "(20.6.14.7), second vertical arrow Ω^1_{A/Λ}⊗_A C → Ω^1_{A/Λ}⊗_A C",
      "an ordinary downward arrow with ≀ to its right (crop)",
      "\\ar@{=}[d]: a double line without arrowhead and without ≀",
      'symbol', 'high',
      "\\ar[d]^{v'} &\n  \\Omega^1_{A/\\Lambda}\\otimes_A C \\ar[r] \\ar@{=}[d]",
      "\\ar[d]^{v'} &\n  \\Omega^1_{A/\\Lambda}\\otimes_A C \\ar[r] \\ar[d]^{\\wr}"),

    # ---------------- page 142 ----------------
    F(142, "(20.6.15), after (20.6.15.1): 'D'autre part, nous désignerons par T_•(C/B/Λ)'",
      "'D'autre part' begins a new indented paragraph (left edge 528 px against the 416 px margin)",
      "no blank line after \\end{equation}: same paragraph, no indent",
      'other', 'high',
      "\\end{equation}\nD'autre part", "\\end{equation}\n\nD'autre part"),
    F(142, "(20.6.15), after (20.6.15.2): 'de sorte que ce complexe est homotope à 0'",
      "*homotope à* italic, 0 upright (crop)",
      "homotope à 0 upright",
      'italics', 'high',
      "homotope à 0", "\\emph{homotope à} 0"),
    F(142, "(20.6.15), after (20.6.15.3): 'En vertu du caractère trivial de T_•, il est clair que l'on a'",
      "new indented paragraph (left edge 530 px against the 418 px margin)",
      "no blank line after \\end{equation}: same paragraph, no indent",
      'other', 'high',
      "\\end{equation}\nEn vertu du caractère", "\\end{equation}\n\nEn vertu du caractère"),
    F(142, "(20.6.16), first line: 'Définissons maintenant une suite exacte de complexes, scindée en chaque degré'",
      "*suite exacte* and *scindée* both italic",
      "only scindée in \\emph",
      'italics', 'high',
      "une suite exacte de complexes", "une \\emph{suite exacte} de complexes"),
    F(142, "(20.6.16), display 'f : Ω^1_{A/Λ}⊗_A C → Ω^1_{B/Λ}⊗_B C' / 'g : Ω^1_{B/Λ}⊗_B C → Ω^1_{C/Λ}'",
      "the two maps one above the other, no punctuation after the first (crop)",
      "the two maps side by side, a comma after the first",
      'punctuation', 'high',
      "\\Omega^1_{B/\\Lambda}\\otimes_B C,\n  \\qquad", "\\Omega^1_{B/\\Lambda}\\otimes_B C\n  \\qquad",
      note="Stacking versus side by side is layout only; the comma is the textual difference."),
    F(142, "(20.6.16): 'p_1(y, z) = z—f(y)'",
      "long dash for the subtraction (bar 40-41 px at 300 dpi; the = bars on the same line 34-35 px)",
      "minus sign",
      'convention', 'high',
      "p_1(y,z)=z-f(y)", "p_1(y,z)=z\\setmin f(y)", conv=7, note=SETMIN_NOTE),
    F(142, "(20.6.16): 'p_0(y, z) = g(z)—y'",
      "long dash for the subtraction (bar 40-41 px; = bars 34-35 px)",
      "minus sign",
      'convention', 'high',
      "p_0(y,z)=g(z)-y", "p_0(y,z)=g(z)\\setmin y", conv=7, note=SETMIN_NOTE),
    F(142, "(20.6.16): 'Im(j_0) = Ker(p_0) est le graphe de g, supplémentaire de K_1(C/A/Λ)⊕{0}'",
      "K_1(C/A/Λ)⊕{0} (subscript 1, crop)",
      "$\\mathrm{K}_1(C/A/\\Lambda)\\oplus\\{0\\}$: keeps the printed reading",
      'misprint_in_print', 'high',
      corrected="supplémentaire de $\\mathrm{K}_0(C/A/\\Lambda)\\oplus\\{0\\}$",
      note=("j_0 lives in degree 0: j_0(x) = (g(x), x) maps K^C_0(B/A/Λ) = Ω^1_{B/Λ}⊗_B C into "
            "K'_0(C/A/Λ) = K_0(C/A/Λ)⊕T_0(C/B/Λ) (20.6.5.1, 20.6.15.3), and the graph of g has the "
            "complement K_0(C/A/Λ)⊕{0} there; K_1(C/A/Λ)⊕{0} lies in K'_1. Compare the degree-1 "
            "statement just before ('supplémentaire de {0}⊕T_1'). No errata entry. For the corrected "
            "edition: in $\\mathrm{K}_1(C/A/\\Lambda)\\oplus\\{0\\}$ (unique on the page) change K_1 to K_0.")),

    # ---------------- page 143 ----------------
    F(143, "proof of (20.6.17): 'par l'homomorphisme canonique s_{B/A/Λ}⊗1_C : Ω^1_{B/Λ}⊗_B C → Ω^1_{B/A}⊗_B C. Notre assertion'",
      "the formula is inline, in the running text, followed by 'Notre assertion' on the same line (crop)",
      "displayed formula \\[ ... \\] with the full stop inside",
      'other', 'high',
      ("canonique\n\\[\n  s_{B/A/\\Lambda}\\otimes1_C:\n"
       "  \\Omega^1_{B/\\Lambda}\\otimes_B C\\to\\Omega^1_{B/A}\\otimes_B C.\n\\]\nNotre assertion"),
      ("canonique\n$s_{B/A/\\Lambda}\\otimes1_C:"
       "\\Omega^1_{B/\\Lambda}\\otimes_B C\\to\\Omega^1_{B/A}\\otimes_B C$. Notre assertion")),
    F(143, "Corollaire (20.6.18) (i), (20.6.18.1): label s' of the arrow Υ_{C/B/Λ} → Υ_{C/B/A}",
      ("s' in bold italic (wrong fount): 141 dark pixels against 91-92 for the light s' of (20.6.17.2) "
       "and (20.6.17.3); the u', v' labels of (20.6.18.1) have the normal weight (crops at 6x)"),
      "plain s' (silent correction)",
      'misprint_in_print', 'high',
      "{s'}\\Upsilon_{C/B/A}\\to0", "{\\boldsymbol{s}'}\\Upsilon_{C/B/A}\\to0",
      corrected="\\xrightarrow{s'}",
      note="Wrong-fount letter reproduced in the diplomatic text, as the earlier bold-italic fixes."),

    # ---------------- page 144 ----------------
    F(144, "Corollaire (20.6.20) (ii), end: '(cf. (21.4.4) et (21.7.5))'",
      "the parenthesis upright (roman 'cf.', 'et') inside the italic statement (crop)",
      "italic (corollary environment)",
      'convention', 'high',
      "(cf.\\ (21.4.4) et\n  (21.7.5))", "\\textup{(cf.\\ (21.4.4) et\n  (21.7.5))}", conv=6),
    F(144, "proof of (20.6.20) (ii): 'il résulte de (20.6.19, (i)) que la suite (20.5.7.2)'",
      "(20.6.19, (i)): one pair of parentheses around number and item (crop)",
      "\\sref{0.20.6.19-fr}, (i) prints '(20.6.19), (i)'",
      'punctuation', 'high',
      "\\sref{0.20.6.19-fr}, (i) que", "(\\ref{0.20.6.19-fr}, (i)) que"),
    F(144, "Remarques (20.6.21) (i), after (20.6.21.1): 'Cet homomorphisme est bijectif lorsque la suite'",
      "new indented paragraph (left edge 520 px against the 407 px margin)",
      "no blank line after \\end{equation}: same paragraph",
      'other', 'high',
      "\\end{equation}\nCet homomorphisme", "\\end{equation}\n\nCet homomorphisme"),
    F(144, "Remarques (20.6.21) (i), 2°: 'Ker(Ω^1_{B/Λ} → Ω^1_{B/A}) (0_I, 6.1.2)'",
      "bold 0 with a light roman subscript I (crop at 4x)",
      "$\\mathbf{0_I}$: the subscript I bold as well",
      'font', 'medium',
      "($\\mathbf{0_I}$, 6.1.2), et la suite", "($\\mathbf{0}_{\\mathrm I}$, 6.1.2), et la suite",
      note="Same form as the earlier convention-2 fixes ($\\mathbf{0}_{\\mathrm I}$)."),
    F(144, "Remarques (20.6.21) (i), 2°: 'est alors exacte en vertu de (0_I, 6.1.2)'",
      "bold 0 with a light roman subscript I (crop at 4x)",
      "$\\mathbf{0_I}$: the subscript I bold as well",
      'font', 'medium',
      "vertu de ($\\mathbf{0_I}$, 6.1.2)", "vertu de ($\\mathbf{0}_{\\mathrm I}$, 6.1.2)"),
    F(144, "Remarques (20.6.21) (ii), after the diagram of rings: 'Alors les définitions de (20.6.16) montrent'",
      "new indented paragraph (left edge 521 px against the 408 px margin)",
      "no blank line after \\]: same paragraph",
      'other', 'high',
      "\\]\nAlors les définitions", "\\]\n\nAlors les définitions"),

    # ---------------- page 145 ----------------
    F(145, "Proposition (20.6.22), line 2: '𝔎 un idéal de B, C l'anneau quotient B/𝔎'",
      "Fraktur K twice", "\\mathfrak{R} twice",
      'symbol', 'high',
      "$\\mathfrak{R}$ un idéal de $B$, $C$ l'anneau quotient $B/\\mathfrak{R}$",
      "$\\mathfrak{K}$ un idéal de $B$, $C$ l'anneau quotient $B/\\mathfrak{K}$", note=FRAK_NOTE),
    F(145, "Proposition (20.6.22): 'E = B/𝔎²'",
      "Fraktur K", "\\mathfrak{R}",
      'symbol', 'high', "$E=B/\\mathfrak{R}^2$", "$E=B/\\mathfrak{K}^2$"),
    F(145, "Proposition (20.6.22): 'de C par 𝔎/𝔎². On a alors'",
      "Fraktur K twice", "\\mathfrak{R} twice",
      'symbol', 'high',
      "par $\\mathfrak{R}/\\mathfrak{R}^2$. On a alors", "par $\\mathfrak{K}/\\mathfrak{K}^2$. On a alors"),
    F(145, "(20.6.22.1): '𝔎/𝔎² →δ_{C/B/A}'",
      "Fraktur K twice", "\\mathfrak{R} twice",
      'symbol', 'high',
      "\\mathfrak{R}/\\mathfrak{R}^2\\xrightarrow{\\delta_{C/B/A}}",
      "\\mathfrak{K}/\\mathfrak{K}^2\\xrightarrow{\\delta_{C/B/A}}"),
    F(145, "proof of (20.6.22): 'Υ_{C/B/Λ} s'identifie canoniquement à 𝔎/𝔎²'",
      "Fraktur K twice", "\\mathfrak{R} twice",
      'symbol', 'high',
      "$\\mathfrak{R}/\\mathfrak{R}^2$. Il suffit", "$\\mathfrak{K}/\\mathfrak{K}^2$. Il suffit"),
    F(145, "proof of (20.6.22), diagram, middle row 'Υ_{C/E/Λ} = Υ_{C/B/Λ} = 𝔎/𝔎²'",
      "Fraktur K twice", "\\mathfrak{R} twice",
      'symbol', 'high',
      "\\Upsilon_{C/B/\\Lambda}=\\mathfrak{R}/\\mathfrak{R}^2",
      "\\Upsilon_{C/B/\\Lambda}=\\mathfrak{K}/\\mathfrak{K}^2"),
    F(145, "proof of (20.6.22), diagram, bottom row '𝔎/𝔎²'",
      "Fraktur K twice", "\\mathfrak{R} twice",
      'symbol', 'high',
      "\\\\\n  \\mathfrak{R}/\\mathfrak{R}^2", "\\\\\n  \\mathfrak{K}/\\mathfrak{K}^2"),
    F(145, "paragraph after (20.6.22): 'et que B/𝔎² soit Λ-triviale'",
      "Fraktur K", "\\mathfrak{R}",
      'symbol', 'high',
      "et que\n$B/\\mathfrak{R}^2$", "et que\n$B/\\mathfrak{K}^2$"),
    F(145, "proof of (20.6.22), diagram, middle row right: 'Ω^1_{B/Λ}⊗_B C = Ω^1_{E/Λ}⊗_E C'",
      "subscripts B/Λ and E/Λ (Λ without crossbar; crop at 4x, against the A of Ω^1_{B/A} in the bottom row)",
      "\\Omega^1_{B/A}\\otimes_B C=\\Omega^1_{E/A}\\otimes_E C",
      'formula', 'high',
      "\\Omega^1_{B/A}\\otimes_B C=\\Omega^1_{E/A}\\otimes_E C",
      "\\Omega^1_{B/\\Lambda}\\otimes_B C=\\Omega^1_{E/\\Lambda}\\otimes_E C",
      note="The print's reading is the mathematically right one: Υ_{C/B/Λ} ⊂ Ω^1_{B/Λ}⊗_B C."),
    F(145, "proof of (20.6.22), diagram, left vertical arrow 𝔎/𝔎² → 𝔎/𝔎² (middle row to bottom row)",
      "isomorphism sign ≀ to the right of the arrow (crop)",
      "label \\ell (ℓ) to the left of the arrow",
      'symbol', 'high',
      "\\ar[d]_{\\ell}", "\\ar[d]^{\\wr}"),
    F(145, "proof of (20.6.22), diagram, bottom row arrow 𝔎/𝔎² → Ω^1_{B/A}⊗_B C",
      "label δ_{C/B/A} below the arrow (crop)",
      "label above the arrow (\\ar[r]^{...})",
      'other', 'high',
      "\\ar[r]^{\\delta_{C/B/A}} &", "\\ar[r]_{\\delta_{C/B/A}} &"),
    F(145, "proof of (20.6.22), diagram, middle row arrow 𝔎/𝔎² → Ω^1_{B/Λ}⊗_B C",
      ("label δ_{C/B/A} (last letter A with its bar, like the A of the bottom label and of (20.6.22.1); "
       "the Λ of Ω^1_{B/Λ} beside it has none; crops at 8x-12x)"),
      "\\ar[r]^-{\\delta_{C/B/A}}: keeps the printed reading",
      'misprint_in_print', 'medium',
      corrected="\\ar[r]^-{\\delta_{C/B/\\Lambda}}",
      note=("The arrow ends in Ω^1_{B/Λ}⊗_B C = Ω^1_{E/Λ}⊗_E C and is the inclusion Υ_{C/B/Λ} → Ω^1_{B/Λ}⊗_B C, "
            "i.e. δ_{C/B/Λ}; δ_{C/B/A} ends in Ω^1_{B/A}⊗_B C (bottom row, which it labels correctly). "
            "No errata entry. Corrected edition: after the Fraktur and Λ fixes of this diagram, change "
            "\\ar[r]^-{\\delta_{C/B/A}} (unique) to \\ar[r]^-{\\delta_{C/B/\\Lambda}}.")),
    F(145, "paragraph after (20.6.22): 'et que B/𝔎² soit Λ-triviale; on observera'",
      "*triviale* italic (crop)",
      "$\\Lambda$-triviale upright",
      'italics', 'high',
      "$\\Lambda$-triviale ;", "$\\Lambda$-\\emph{triviale} ;"),
    F(145, "last diagram of the page (Λ → A → B under Λ' → A' → B'), right vertical arrow B → B'",
      "label f to the right of the upward arrow (crop)",
      "\\ar[u]^f puts f to the left",
      'other', 'high',
      "B \\ar[u]^f", "B \\ar[u]_f"),
]


def page_text(p):
    with open(os.path.join(RUN, 'page_%03d.tex' % p), 'rb') as fh:
        return fh.read().decode('utf-8').replace('\r\n', '\n')


ok = True
for f in findings:
    if f['fix'] is None:
        continue
    t = page_text(f['page'])
    n = t.count(f['fix']['old'])
    if n != 1:
        ok = False
        print('NOT UNIQUE/ABSENT', f['page'], n, repr(f['fix']['old']))
    # the new text must not reintroduce the old text elsewhere
    t2 = t.replace(f['fix']['old'], f['fix']['new'])
    if t2 == t:
        ok = False
        print('NO CHANGE', f['page'], repr(f['fix']['old']))

# all fixes of one page applied in sequence must still apply (independence check)
for p in sorted(set(f['page'] for f in findings)):
    t = page_text(p)
    fx = [f for f in findings if f['page'] == p and f['fix'] is not None]
    for order in (fx, list(reversed(fx))):
        s = t
        for f in order:
            if s.count(f['fix']['old']) != 1:
                ok = False
                print('SEQUENTIAL FAIL', p, repr(f['fix']['old']))
            s = s.replace(f['fix']['old'], f['fix']['new'], 1)

if not ok:
    sys.exit(1)

with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write('\n')

from collections import Counter
c = Counter()
for f in findings:
    k = 'misprint' if f['kind'] == 'misprint_in_print' else ('convention' if f['kind'] == 'convention' else 'normal')
    c[(f['page'], k)] += 1
for p in sorted(set(f['page'] for f in findings)):
    print(p, c[(p, 'normal')], c[(p, 'convention')], c[(p, 'misprint')])
print('written', OUT, len(findings))
