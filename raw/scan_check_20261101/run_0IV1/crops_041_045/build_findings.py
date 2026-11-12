import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

RUN = r'user\Documents\ega_scan_check_20261101\run_0IV1'
OUT = RUN + r'\findings_041_045.json'
SRC = r'user\Documents\ega_scan_check_20261101\ega-fr\source\ega4\ega0-17-fr.tex'
NL = '\n'

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note='', corrected=None):
    d = {'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind,
         'convention': conv, 'confidence': conf,
         'fix': None if old is None else {'old': old, 'new': new}}
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    F.append(d)


AB_NOTE = ('References to the conditions a), b) in running text are italic in the print; '
           'the list labels are upright, as in the TeX.')

# ---------------- page 41 ----------------
add(41, "proof of (17.1.5), end: 'la condition a) de (17.1.1) est donc la même pour A et Â'",
    "'a)' in italics (crop)", "la condition a) de (roman)", 'italics', None, 'high',
    "la condition a) de", r"la condition \emph{a)} de", AB_NOTE)

add(41, "Définition (17.1.6): 'on appelle système régulier de paramètres de A un système de paramètres pour A'",
    "the defined term is italic like the rest of the definition: no change of face (crop)",
    r"\emph{système régulier de paramètres de $A$}: \emph inside the italic definition environment sets it upright",
    'convention', 6, 'high',
    r"\emph{système régulier de paramètres de $A$}", r"système régulier de paramètres de $A$")

add(41, "Définition (17.1.6): 'un système de paramètres pour A (16.3.5) qui engendre m'",
    "'(16.3.5)' upright (roman figures and parentheses) inside the italic statement (crop)",
    "(16.3.5) italic (definition environment)", 'convention', 6, 'high',
    r"pour $A$ (16.3.5) qui", r"pour $A$ \textup{(16.3.5)} qui")

add(41, "after (17.1.6): 'L'existence d'un tel système équivaut au fait que A est régulier (17.1.1)'",
    "'régulier' in italics (crop)", "régulier (roman)", 'italics', None, 'high',
    r"$A$ est régulier (17.1.1)", r"$A$ est \emph{régulier} (17.1.1)")

add(41, "same paragraph: 'en vertu de (17.1.1, a)) et de (15.1.9)'",
    "'a)' in italics, the closing parenthesis of the reference roman (crop)", "(17.1.1, a)) roman",
    'italics', None, 'high',
    "(17.1.1, a))", r"(17.1.1, \emph{a)})")

add(41, "same paragraph: '(x_i) est une suite A-régulière maximale (d'où la terminologie)'",
    "'régulière' in italics (crop)", "$A$-régulière (roman)", 'italics', None, 'high',
    "$A$-régulière" + NL + "maximale", r"$A$-\emph{régulière}" + NL + "maximale",
    "The 'A-régulière' of the next paragraph ('On prendra garde ...') is roman in the print, as in the TeX.")

add(41, "Proposition (17.1.7): 'J l'idéal x_1A + ... + x_rA'",
    "baseline dots (crop)", r"x_1A+\cdots+x_rA (centred dots)", 'symbol', None, 'high',
    r"x_1A+\cdots+x_rA", r"x_1A+\ldots+x_rA",
    r"GLOBAL_ISSUES item 22 (\cdots for the print's baseline dots).")

add(41, "Proposition (17.1.7) a'): 'les classes x̄_i des x_i mod. m² sont linéairement indépendantes sur k'",
    "'mod.' upright inside the italic statement (crop)", "mod. italic (proposition environment)",
    'convention', 6, 'high',
    r"mod. $\mathfrak{m}^2$ sont", r"\textup{mod.} $\mathfrak{m}^2$ sont")

add(41, "proof of (17.1.7): 'L'équivalence de a) et a') est immédiate'",
    "'a)' and 'a')' in italics (crop)", "a), a') roman", 'italics', None, 'high',
    "L'équivalence de a)" + NL + "et a') est", r"L'équivalence de \emph{a)}" + NL + r"et \emph{a')} est")

add(41, "proof of (17.1.7): 'Pour voir que a) entraîne b), remarquons'",
    "'a)' and 'b)' in italics (crop)", "a), b) roman", 'italics', None, 'high',
    "Pour voir que a) entraîne b),", r"Pour voir que \emph{a)} entraîne \emph{b)},")

add(41, "proof of (17.1.7), after (17.1.7.1): 'l'hypothèse a) entraîne que rg_k((m²+J)/m²) = r'",
    "'a)' in italics (crop)", "a) roman", 'italics', None, 'high',
    "l'hypothèse a) entraîne", r"l'hypothèse \emph{a)} entraîne")

add(41, "proof of (17.1.7): 'ce qui prouve b) en vertu de (17.1.1, b))'",
    "both 'b)' in italics, the closing parenthesis of the reference roman (crop)", "b) roman (twice)",
    'italics', None, 'high',
    "ce qui prouve b) en vertu de (17.1.1, b))", r"ce qui prouve \emph{b)} en vertu de (17.1.1, \emph{b)})")

add(41, "proof of (17.1.7), second paragraph: 'Inversement, pour prouver que b) entraîne a), notons'",
    "'b)' and 'a)' in italics (crop)", "b), a) roman", 'italics', None, 'high',
    "pour prouver que b) entraîne a),", r"pour prouver que \emph{b)} entraîne \emph{a)},")

# ---------------- page 42 ----------------
add(42, "proof of (17.1.8): 'qu'un élément de m non diviseur de 0 fait partie d'un système de paramètres'",
    "'non diviseur de o': the figure 0 (old style), not the word (crop); statement a) above prints the word 'zéro'",
    "non diviseur de zéro", 'word', None, 'high',
    "de zéro fait", r"de $0$ fait")

add(42, "proof of (17.1.9): 'On a déjà vu (17.1.7) que b) entraîne a).'",
    "'b)' and 'a)' in italics (crop)", "b), a) roman", 'italics', None, 'high',
    "que b) entraîne a).", r"que \emph{b)} entraîne \emph{a)}.")

add(42, "proof of (17.1.9): 'Posons J' = x_1A + ... + x_rA'",
    "baseline dots (crop)", r"x_1A+\cdots+x_rA (centred dots)", 'symbol', None, 'high',
    r"x_1A+\cdots+x_rA", r"x_1A+\ldots+x_rA")

add(42, "heading 17.2: 'Rappels sur la dimension projective et la dimension injective des modules.'",
    "the title ends with a full stop (crop)", r"\subsection{... des modules} without the full stop",
    'punctuation', None, 'high',
    "injective des" + NL + "modules}", "injective des" + NL + "modules.}",
    r"No \subsection title in ega0-14-fr.tex to ega0-19b-fr.tex has the final full stop (as GLOBAL_ISSUES item 43 for ega3-1).")

add(42, "(17.2.1): 'Il revient au même (loc. cit.) de dire'",
    "'(loc. cit.)' italic, both parentheses slanted (crop)", r"(\emph{loc. cit.}) with upright parentheses",
    'italics', None, 'high',
    r"(\emph{loc. cit.})", r"\emph{(loc. cit.)}",
    "Same form as the fixes for EGA II p. 9 and EGA III p. 182.")

add(42, "(17.2.1), display '0 → R → P_{n-1} → ... → P_0 → M → 0'",
    "baseline dots between the arrows (4x crop: on the baseline of P_0, below the arrow shafts)",
    r"\cdots", 'symbol', None, 'high',
    r"P_{n-1}\longrightarrow\cdots", r"P_{n-1}\longrightarrow\ldots")

add(42, "(17.2.1): '(resp. 0 → M → Q_0 → ... → Q_{n-1} → C → 0)'",
    "baseline dots between the arrows (4x crop)", r"\cdots", 'symbol', None, 'high',
    r"Q_0\longrightarrow\cdots", r"Q_0\longrightarrow\ldots")

# ---------------- page 43 ----------------
add(43, "Remarques (17.2.2) (iii): '(Bourbaki, Alg. comm., chap. II, § 3, n° 2, cor. 2 de la prop. 5)'",
    "n° (n with a superior o) (crop)", "no~2", 'symbol', None, 'high',
    "no~2", r"n\textsuperscript{o}~2",
    "Same form as the fixes for EGA III pp. 142, 143, 176.")

add(43, "Lemme (17.2.3): 'pour tout A-module monogène N, on ait Ext^{n+1}_A(N, M) = 0'",
    "'monogène' upright inside the italic statement (crop)", "monogène italic (lemma environment)",
    'convention', 6, 'high',
    r"monogène $N$, on ait $\operatorname{Ext}^{n+1}_A(N,M)",
    r"\textup{monogène} $N$, on ait $\operatorname{Ext}^{n+1}_A(N,M)",
    r"The print's emphasis inside an italic statement; \emph{monogène} gives the same output.")

add(43, "Lemme (17.2.4): 'pour tout A-module monogène N, on ait Ext^{n+1}_A(M, N) = 0'",
    "'monogène' upright inside the italic statement (crop)", "monogène italic (lemma environment)",
    'convention', 6, 'high',
    r"monogène $N$, on ait $\operatorname{Ext}^{n+1}_A(M,N)",
    r"\textup{monogène} $N$, on ait $\operatorname{Ext}^{n+1}_A(M,N)")

add(43, "Corollaire (17.2.5): 'et si M est de type fini'",
    "'de type fini' italic like the rest of the statement: no change of face (crop)",
    r"\emph{de type fini}: \emph inside the italic corollary environment sets it upright",
    'convention', 6, 'high',
    r"$M$ est \emph{de type fini}", r"$M$ est de type fini")

add(43, "proof of (17.2.5): 'par platitude, en considérant une résolution libre de M'",
    "'une résolution libre de M'", "une résolution libre de $M$: keeps the printed reading",
    'misprint_in_print', None, 'medium', None, None,
    "The formula S^{-1}Ext^i_A(N, M) = Ext^i_{S^{-1}A}(S^{-1}N, S^{-1}M) comes from a resolution of the first "
    "argument N (of finite type over the noetherian A) by free modules of finite type, the case i = 0 "
    "(Bourbaki, prop. 19, which needs N of finite presentation) and the flatness of S^{-1}A; a free resolution "
    "of M does not compute Ext^i_A(N, M). For the corrected edition only.",
    corrected=r"une résolution libre de $N$")

add(43, "proof of (17.2.5): '(Bourbaki, Alg. comm., chap. II, § 2, n° 7, prop. 19)'",
    "n° (n with a superior o) (crop)", "no~7", 'symbol', None, 'high',
    "no~7", r"n\textsuperscript{o}~7")

# ---------------- page 44 ----------------
add(44, "end of the proof of (17.2.5): 'de Bourbaki, Alg. comm., chap. II, § 3, n° 3, th. 1'",
    "n° (n with a superior o) (crop)", "no~3", 'symbol', None, 'high',
    "no~3", r"n\textsuperscript{o}~3")

add(44, "proof of (17.2.6): 'appliquée au foncteur covariant M ⇝ k⊗_A M'",
    "wavy arrow ⇝ (3x crop)", r"\mapsto", 'symbol', None, 'high',
    r"$M\mapsto k\otimes_A M$", r"$M\leadsto k\otimes_A M$",
    r"Not convention 3 (the printed arrow is not plain); \leadsto as in the EGA III ch. 0 fixes (GLOBAL_ISSUES item 33).")

add(44, "proof of (17.2.6): '(Bourbaki, Alg. comm., chap. II, § 3, n° 2, cor. 2 de la prop. 5)'",
    "n° (n with a superior o) (crop)", "no~2", 'symbol', None, 'high',
    "no~2", r"n\textsuperscript{o}~2")

add(44, "Corollaire (17.2.7): 'Sous les hypothèses de (17.2.6), soit x un élément M-régulier'",
    "'(17.2.6)' upright inside the italic statement (crop)", "(17.2.6) italic (corollary environment)",
    'convention', 6, 'high',
    "de (17.2.6), soit", r"de \textup{(17.2.6)}, soit")

add(44, "Proposition (17.2.8) c'): 'tel que M soit de type fini (ou seulement monogène), on a'",
    "'(ou seulement' and the closing parenthesis upright, 'monogène' italic (4x crop)",
    "the whole parenthesis italic (proposition environment)", 'convention', 6, 'high',
    "type fini (ou seulement monogène), on a",
    r"type fini \textup{(ou seulement} monogène\textup{)}, on a")

# ---------------- page 45 ----------------
add(45, "Corollaire (17.2.10): 'où m parcourt le spectre de A (ou l'ensemble des idéaux maximaux de A).'",
    "both parentheses upright, the words between them italic (5x crop); the parentheses of the same phrase in (17.2.5), p. 43, are italic",
    "italic parentheses (corollary environment)", 'convention', 6, 'medium',
    "de $A$ (ou l'ensemble des idéaux" + NL + "maximaux de $A$).",
    r"de $A$ \textup{(}ou l'ensemble des idéaux" + NL + r"maximaux de $A$\textup{)}.")

add(45, "proof of (17.2.13): 'Comme B est un A-module fidèlement plat (0_I, 6.6.2)'",
    "bold 0 (crop)", r"$0_{\rm I}$", 'convention', 2, 'high',
    r"plat ($0_{\rm I}$, 6.6.2)", r"plat ($\mathbf{0}_{\rm I}$, 6.6.2)")

add(45, "proof of (17.2.13): 'il revient au même (0_I, 6.4.1) de montrer'",
    "bold 0 (crop)", r"$0_{\rm I}$", 'convention', 2, 'high',
    r"($0_{\rm I}$, 6.4.1)", r"($\mathbf{0}_{\rm I}$, 6.4.1)")

add(45, "proof of (17.2.13): 'si L_• = (L_j) est une résolution droite de M par des A-modules libres' and 'est une résolution droite du B-module M⊗_A B'",
    "'résolution droite' twice", "résolution droite (twice): keeps the printed reading",
    'misprint_in_print', None, 'low', None, None,
    "A resolution ... → L_1 → L_0 → M → 0 by free modules is a 'résolution gauche' in the terminology of "
    "(17.2.1) ('résolution projective gauche (resp. ... injective droite)') and (17.2.2, (iii)). Probably the "
    "authors' slip, repeated in the second clause; low confidence because it is a slip of terminology, not of "
    "typesetting. For the corrected edition only, if accepted.",
    corrected=r"résolution gauche (both places)")

# ---------------- checks ----------------
src = open(SRC, encoding='utf-8', newline='').read()
marks = {int(m.group(1)): m.start() for m in re.finditer(r'\\oldpage\[0\\textsubscript\{IV-1\}\]\{(\d+)\}', src)}
ok = True
for d in F:
    fx = d['fix']
    if fx is None:
        continue
    p = d['page']
    page_txt = open(rf'{RUN}\page_{p:03d}.tex', encoding='utf-8', newline='').read().replace('\r\n', '\n')
    n_page = page_txt.count(fx['old'])
    seg = src[marks[p]:marks.get(p + 1, len(src))]
    n_seg = seg.count(fx['old'])
    n_file = src.count(fx['old'])
    flag = '' if (n_page == 1 and n_seg == 1) else '  <-- CHECK'
    if flag:
        ok = False
    print(p, repr(fx['old'])[:60], 'page', n_page, 'segment', n_seg, 'file', n_file, flag)

json.dump(F, open(OUT, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
from collections import Counter
c = Counter()
for d in F:
    k = 'misprint' if d['kind'] == 'misprint_in_print' else ('convention' if d['kind'] == 'convention' else 'normal')
    c[(d['page'], k)] += 1
for p in range(41, 46):
    print(p, c[(p, 'normal')], c[(p, 'convention')], c[(p, 'misprint')])
print('ALL OK' if ok else 'PROBLEMS', len(F))
