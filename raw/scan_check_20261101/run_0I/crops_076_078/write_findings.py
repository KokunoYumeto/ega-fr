import json, os, sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, 'findings_076_078.json')

F = []

def add(page, where, scan, tex, kind, conv, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf, "fix": fix}
    if kind == 'misprint_in_print':
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

# ---------------- page 76 ----------------
add(76, "(7.7.2), 2nd sentence: 'On en conclut que (M⊗_A N)^ est le séparé complété du A-module ...'",
    "'est le' roman, italics begin with 'séparé complété'",
    r"est \emph{le séparé complété du",
    "italics", None, "high",
    {"old": r"est \emph{le séparé complété du", "new": r"est le \emph{séparé complété du"},
    "Checked on an enlarged crop: 'le' is upright.")

add(76, "(7.7.3): 'il est immédiat que u⊗v est continu pour les topologies produits tensoriels sur M⊗N et M'⊗N' respectivement'",
    "M⊗N et M'⊗N' (no subscript A under ⊗)",
    r"$M\otimes_A N$ et $M'\otimes_A N'$",
    "formula", None, "high",
    {"old": r"$M\otimes_A N$ et $M'\otimes_A N'$", "new": r"$M\otimes N$ et $M'\otimes N'$"},
    "Checked on an enlarged crop. The print drops the subscript here and in the next formula (⊗ is over A throughout, so not a misprint); the TeX adds it.")

add(76, "(7.7.3): 'on en déduit un homomorphisme continu (M⊗N)^→(M'⊗N')^'",
    "(M⊗N)^→(M'⊗N')^ (no subscript A under ⊗)",
    r"$(M\otimes_A N)^\wedge\to(M'\otimes_A N')^\wedge$",
    "formula", None, "high",
    {"old": r"$(M\otimes_A N)^\wedge\to(M'\otimes_A N')^\wedge$", "new": r"$(M\otimes N)^\wedge\to(M'\otimes N')^\wedge$"},
    "Checked on an enlarged crop. The following (M⊗_A N)^ in 'est donc un bifoncteur' does have the subscript, as in the TeX.")

add(76, "(7.7.6), 1st line: 'Les homomorphismes de A-algèbres b→b⊗1, c→1⊗c'",
    "plain arrow b→b⊗1 (checked on a crop)",
    r"$b\mapsto b\otimes 1$",
    "convention", 3, "high",
    {"old": r"$b\mapsto b\otimes 1$", "new": r"$b\to b\otimes 1$"},
    None)

add(76, "(7.7.6), 1st line: 'Les homomorphismes de A-algèbres b→b⊗1, c→1⊗c'",
    "plain arrow c→1⊗c (checked on a crop)",
    r"$c\mapsto 1\otimes c$",
    "convention", 3, "high",
    {"old": r"$c\mapsto 1\otimes c$", "new": r"$c\to 1\otimes c$"},
    None)

add(76, "(7.7.6): 'possèdent en outre la propriété universelle suivante ; pour toute ...'",
    "'propriété univer-selle' italic, 'suivante' roman",
    r"\emph{propriété universelle suivante}",
    "italics", None, "high",
    {"old": r"\emph{propriété universelle suivante}", "new": r"\emph{propriété universelle} suivante"},
    "Checked on an enlarged crop (top of the last strip). Independent of the next finding.")

add(76, "(7.7.6): 'la propriété universelle suivante ; pour toute A-algèbre ...'",
    "semicolon: 'suivante ; pour toute'",
    r"suivante}~: pour toute",
    "punctuation", None, "high",
    {"old": "~: pour toute", "new": "~; pour toute"},
    "Checked on an enlarged crop: a semicolon, not a colon. Not a misprint (the print uses ';' freely before an explanation).")

add(76, "(7.7.6): 'il existe un A-homomorphisme continu et un seul w : (B⊗_A C)^→D et un seul tel que u=w∘ρ et v=w∘σ'",
    "'et un seul' printed twice: '... continu et un seul w : (B⊗_A C)^→D et un seul tel que ...'",
    r"$A$-homomorphisme continu et un seul $w:(B\otimes_A C)^\wedge\to D$ et un seul tel que",
    "misprint_in_print", None, "medium",
    None,
    "The TeX keeps the printed reading (checked on a crop; the doubled phrase is certainly printed). The second 'et un seul' duplicates the first; medium only because the duplication is a slip of wording rather than of type.",
    corrected=r"il existe un $A$-homomorphisme continu et un seul $w:(B\otimes_A C)^\wedge\to D$ tel que $u=w\circ\rho$ et $v=w\circ\sigma$")

add(76, "(7.7.6), last line of the page: 'et tout revient à prouver que w_0 est continu, car il donnera alors un'",
    "'continu' in italics",
    r"$w_0$ est continu,",
    "italics", None, "high",
    {"old": r"$w_0$ est continu,", "new": r"$w_0$ est \emph{continu},"},
    "Checked on an enlarged crop.")

# ---------------- page 77 ----------------
add(77, "end of (7.7.6): 'l'image par w_0 de Im(𝔎⊗C)+Im(B⊗𝔏) est encore contenue dans 𝔐'",
    "Im(𝔎⊗C)+Im(B⊗𝔏) (no subscript A under either ⊗)",
    r"$\Im(\mathfrak K\otimes_A C)+\Im(B\otimes_A\mathfrak L)$ est encore",
    "formula", None, "high",
    {"old": r"$\Im(\mathfrak K\otimes_A C)+\Im(B\otimes_A\mathfrak L)$ est encore", "new": r"$\Im(\mathfrak K\otimes C)+\Im(B\otimes\mathfrak L)$ est encore"},
    "Checked on an enlarged crop. Same abbreviation as on p. 76 (7.7.3); not a misprint.")

add(77, "Proposition (7.7.7): 'et si 𝔎 (resp. 𝔏) est un idéal de définition'",
    "'(resp. 𝔏)' roman inside the italic statement (parentheses and 'resp.' upright)",
    "(resp.\n$\\mathfrak L$) inside the proposition environment",
    "convention", 6, "high",
    {"old": "(resp.\n$\\mathfrak L$)", "new": "\\textup{(resp.\n$\\mathfrak L$)}"},
    "Enlarged crop. Form of the fix as in the p. 23 precedent.")

add(77, "Proposition (7.7.7): 'est un idéal de définition de B (resp. C), l'adhérence'",
    "'(resp. C)' roman inside the italic statement",
    r"(resp. $C$) inside the proposition environment",
    "convention", 6, "high",
    {"old": r"(resp. $C$)", "new": r"\textup{(resp. $C$)}"},
    "Enlarged crop.")

add(77, "Proposition (7.7.7): 'de l'image canonique de 𝔋=Im(𝔎⊗C)+Im(B⊗𝔏) est un idéal de définition'",
    "𝔋 = Im(𝔎⊗C) + Im(B⊗𝔏) (no subscript A)",
    r"$\mathfrak H=\Im(\mathfrak K\otimes_A C)+\Im(B\otimes_A\mathfrak L)$",
    "formula", None, "high",
    {"old": r"$\mathfrak H=\Im(\mathfrak K\otimes_A C)+\Im(B\otimes_A\mathfrak L)$", "new": r"$\mathfrak H=\Im(\mathfrak K\otimes C)+\Im(B\otimes\mathfrak L)$"},
    "Checked on an enlarged crop. The (B⊗_A C)^ earlier in the statement has the subscript, as in the TeX.")

add(77, "proof of (7.7.7), displayed inclusion",
    "𝔋^{2n} ⊂ Im(𝔎^n⊗C) + Im(B⊗𝔏^n) (no subscript A)",
    r"\Im(\mathfrak K^n\otimes_A C)+\Im(B\otimes_A\mathfrak L^n).",
    "formula", None, "high",
    {"old": r"\Im(\mathfrak K^n\otimes_A C)+\Im(B\otimes_A\mathfrak L^n)", "new": r"\Im(\mathfrak K^n\otimes C)+\Im(B\otimes\mathfrak L^n)"},
    "Checked on an enlarged crop. Can be applied before or after the next finding (period).")

add(77, "proof of (7.7.7), end of the displayed inclusion",
    "no period after the display",
    "\\mathfrak L^n).\n\\]",
    "punctuation", None, "high",
    {"old": "\\mathfrak L^n).\n\\]", "new": "\\mathfrak L^n)\n\\]"},
    "Checked on an enlarged crop: nothing follows the closing parenthesis; the next line is Proposition (7.7.8).")

add(77, "(7.8.1), 1st line: 'Soient A un anneau 𝔍-adique noethérien, M et N deux A-modules'",
    "'𝔍-adique noethérien' in italics",
    r"anneau $\mathfrak J$-adique noethérien, $M$",
    "italics", None, "high",
    {"old": r"anneau $\mathfrak J$-adique noethérien, $M$", "new": r"anneau \emph{$\mathfrak J$-adique noethérien}, $M$"},
    "Checked on an enlarged crop.")

# ---------------- page 78 ----------------
add(78, "paragraph after the proof of (7.8.2): 'Si on suppose seulement que A est un anneau 𝔍-préadique noethérien, M et N deux'",
    "'𝔍-préadique noethérien' in italics",
    "anneau $\\mathfrak J$-préadique\nnoethérien,",
    "italics", None, "high",
    {"old": "anneau $\\mathfrak J$-préadique\nnoethérien,", "new": "anneau \\emph{$\\mathfrak J$-préadique\nnoethérien},"},
    "Checked on an enlarged crop.")

add(78, "Proposition (7.8.3): 'Sous les hypothèses de (7.8.2), l'ensemble des homomorphismes'",
    "reference (7.8.2) upright inside the italic statement",
    r"(7.8.2) inside the proposition environment",
    "convention", 6, "high",
    {"old": r"hypothèses de (7.8.2),", "new": r"hypothèses de \textup{(7.8.2)},"},
    "Enlarged crop: parentheses and old-style figures upright. Form of the fix as in the p. 24 precedent.")

add(78, "Proposition (7.8.3): 'l'ensemble des homomorphismes injectifs (resp. surjectifs, bijectifs) de M dans N'",
    "'(resp.' roman; 'surjectifs, bijectifs)' italic, closing parenthesis italic",
    r"(resp. surjectifs, bijectifs) inside the proposition environment",
    "convention", 6, "high",
    {"old": r"(resp. surjectifs", "new": r"\textup{(resp.} surjectifs"},
    "Enlarged crop.")

add(78, "proof of (7.8.3): 'par le lemme d'Artin-Rees (7.3.2.1)'",
    "Artin-Rees with a hyphen",
    r"d'Artin--Rees",
    "punctuation", None, "high",
    {"old": r"d'Artin--Rees", "new": r"d'Artin-Rees"},
    "Checked on an enlarged crop: a short hyphen. The lemma's own heading in ega0-1-fr.tex (namedlemma 7.3.2.1) already has 'Artin-Rees'.")

# ---------------- write and check ----------------
with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write('\n')

ok = True
counts = {}
for d in F:
    p = d['page']
    c = counts.setdefault(p, [0, 0, 0])
    if d['kind'] == 'convention':
        c[1] += 1
    elif d['kind'] == 'misprint_in_print':
        c[2] += 1
    else:
        c[0] += 1
    if d['fix'] is None:
        continue
    tex = open(os.path.join(RUN, 'page_%03d.tex' % p), encoding='utf-8', newline='').read()
    if '\r' in tex:
        print('WARNING: CR in page', p)
    n = tex.count(d['fix']['old'])
    if n != 1:
        ok = False
        print('NOT UNIQUE/ABSENT', p, n, repr(d['fix']['old']))
print('written', len(F), 'findings; uniqueness ok' if ok else 'uniqueness FAILED')
for p in sorted(counts):
    print(p, '%d/%d/%d' % tuple(counts[p]))

# reload check
json.load(open(OUT, encoding='utf-8'))
