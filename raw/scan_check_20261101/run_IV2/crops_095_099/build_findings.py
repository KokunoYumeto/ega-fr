# Builds findings_095_099.json and checks every fix's "old" (sequentially and pairwise).
import json, os, sys, itertools

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, 'findings_095_099.json')
NL = '¶'   # newline token used below

def T(s):
    return None if s is None else s.replace(NL, '\n')

F = []
def add(page, where, scan, tex, kind, conv, conf, old, new, note='', corrected=None, dep=None):
    d = {'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind,
         'convention': conv, 'confidence': conf,
         'fix': None if old is None else {'old': T(old), 'new': T(new)}}
    if kind == 'misprint_in_print':
        d['corrected'] = T(corrected)
    d['note'] = note
    d['_dep'] = dep   # index of the edit this one's old depends on (removed before writing)
    F.append(d)
    return len(F) - 1

COV = 'Covered by the edit of the finding just before (one edit for the whole expression).'

# ---------------------------------------------------------------- page 95
add(95, "after Proposition (5.5.2): 'lorsque l'on suppose que f est un morphisme de type fini.'",
    "'de type fini' italic", "upright", 'convention', 6, 'high',
    r"est un morphisme de type fini.", r"est un morphisme \emph{de type fini}.",
    "Printed italic words left upright.")
add(95, "proof of (5.5.3): 'la partie multiplicative S = A—{0}'",
    "long dash for the set difference A—{0} (enlarged crop)", r"$S=A-\{0\}$", 'convention', 7, 'high',
    r"$S=A-\{0\}$", r"$S=A\setmin\{0\}$",
    "\\setmin pending the convention-7 decision (FIX_POLICY 2.7).")
add(95, "proof of (5.5.3): 'de l'anneau intègre A'",
    "'intègre' italic", "upright", 'convention', 6, 'high',
    r"de l'anneau intègre¶$A$;", r"de l'anneau \emph{intègre}¶$A$;", "")
add(95, "proof of (5.5.3): 'En outre, on a, d'après (5.5.1.2),'",
    "(5.5.1.2) (enlarged crop)", "(5.5.1.2): keeps the printed reading", 'misprint_in_print', None, 'high',
    None, None,
    "The TeX keeps the printed reading. No formula (5.5.1.2) exists: (5.5.1) on p. 94 has only (5.5.1.1), and the inequality used here is (5.5.1.1) for A_p -> B_q (B_q (x) k = B_q/pB_q).",
    corrected="(5.5.1.1)")
add(95, "proof of (5.5.3): 'dim(B_q) ≤ dim(A_p) + dim(B_q/pB_q), et si k est le corps des fractions'",
    "formula in the running text, comma after it", r"displayed with \[ ... \] (comma inside the display)", 'other', None, 'high',
    r"\[¶\dim(B_{\mathfrak q})\leq\dim(A_{\mathfrak p})¶+\dim(B_{\mathfrak q}/\mathfrak pB_{\mathfrak q}),¶\]¶et si $k$",
    r"$\dim(B_{\mathfrak q})\leq\dim(A_{\mathfrak p})¶+\dim(B_{\mathfrak q}/\mathfrak pB_{\mathfrak q})$, et si $k$",
    "Display vs inline; the formula itself matches.")
add(95, "proof of (5.5.3): 'si p = p_0 ⊃ p_1 ⊃ ... ⊃ p_m est une chaîne'",
    "baseline dots (enlarged crop)", r"\cdots", 'symbol', None, 'high',
    r"\supset\cdots", r"\supset\ldots", "")
add(95, "after (5.5.4): 'des exemples d'anneaux locaux non noethériens A'",
    "'non noethériens' italic", "upright", 'convention', 6, 'high',
    r"locaux non noethériens", r"locaux \emph{non noethériens}", "")
add(95, "after (5.5.5): 'Cela résulte de (5.5.4) et de (0, 14.1.7).'",
    "bold 0", "plain 0", 'convention', 2, 'high',
    r"(0, 14.1.7)", r"(\textbf{0}, 14.1.7)", "")
add(95, "Corollaire (5.5.6): 'Sous les hypothèses de (5.5.3), soit'",
    "(5.5.3) upright inside the italic statement (enlarged crop)", "italic (corollary environment)", 'convention', 6, 'high',
    r"hypothèses de (5.5.3),", r"hypothèses de \textup{(5.5.3)},", "")
add(95, "(5.5.6.1): 'deg.tr_k k''",
    "'deg.tr' with no point after tr (enlarged crop)", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"\operatorname{deg.tr.}_k", r"\operatorname{deg.tr}_k", "Same correction as on pp. 52-54.")
add(95, "(5.5.6.1): end of the display",
    "no full stop after k' (enlarged crop)", "k'.", 'punctuation', None, 'high',
    r"k'.¶\tag{5.5.6.1}", r"k'¶\tag{5.5.6.1}", "")

# ---------------------------------------------------------------- page 96
add(96, "Lemme (5.5.7), label (i)", "(i) upright (enlarged crop)", r"\item[(i)] italic inside the italic lemma",
    'convention', 6, 'high', r"\item[(i)] Pour tout", r"\item[\textup{(i)}] Pour tout",
    "Roman-numeral labels upright in the print (GLOBAL_ISSUES 16).")
add(96, "Lemme (5.5.7), label (ii)", "(ii) upright (enlarged crop)", r"\item[(ii)] italic inside the italic lemma",
    'convention', 6, 'high', r"\item[(ii)] Supposons", r"\item[\textup{(ii)}] Supposons", "")
add(96, "(5.5.7.1), left side: 'deg.tr_A B'", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"on a¶\begin{equation}¶\dim(A)+\operatorname{deg.tr.}_A B", r"on a¶\begin{equation}¶\dim(A)+\operatorname{deg.tr}_A B", "")
add(96, "(5.5.7.1), right side: 'deg.tr_k k''", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"\operatorname{deg.tr.}_k k'¶\tag{5.5.7.1}", r"\operatorname{deg.tr}_k k'¶\tag{5.5.7.1}", "")
add(96, "Lemme (5.5.7) (i): 'et par deg.tr_A B le degré de transcendance'", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"$\operatorname{deg.tr.}_A B$ le degré", r"$\operatorname{deg.tr}_A B$ le degré", "")
add(96, "Lemme (5.5.7) (ii): 'alors les deux membres de (5.5.7.1) sont égaux'",
    "(5.5.7.1) upright inside the italic statement (enlarged crop)", "italic (lemma environment)", 'convention', 6, 'high',
    r"les deux membres de (5.5.7.1) sont égaux", r"les deux membres de \textup{(5.5.7.1)} sont égaux", "")
add(96, "proof of (5.5.7) (i): 'on a deg.tr_A B = 1'", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"$\operatorname{deg.tr.}_A B=1$", r"$\operatorname{deg.tr}_A B=1$", "")
add(96, "proof of (5.5.7) (i): 'la formule (0, 16.1.4.1), appliquée'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"(0, 16.1.4.1)", r"(\textbf{0}, 16.1.4.1)", "")
add(96, "(5.5.7.3): 'dim(A) + 1 — deg.tr_k k''", "long dash for the subtraction (enlarged crop)", "1-", 'convention', 7, 'high',
    r"=\dim(A)+1-", r"=\dim(A)+1\setmin",
    "Subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision. Does not overlap the next edit.")
add(96, "(5.5.7.3): 'deg.tr_k k''", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"\operatorname{deg.tr.}_k k'¶\tag{5.5.7.3}", r"\operatorname{deg.tr}_k k'¶\tag{5.5.7.3}", "")
add(96, "proof of (5.5.7) (i): 'on a alors deg.tr_A B = 0'", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"$\operatorname{deg.tr.}_A B=0$", r"$\operatorname{deg.tr}_A B=0$", "")
add(96, "proof of (5.5.7) (ii): 'Si (A[T]_n) est caténaire'",
    "(A[T]_n): the subscript n inside the parenthesis (enlarged crop)", r"$(A[T])_{\mathfrak n}$ (silently corrected)",
    'misprint_in_print', None, 'high',
    r"Si $(A[T])_{\mathfrak n}$ est caténaire", r"Si $(A[T]_{\mathfrak n})$ est caténaire",
    "Silent correction: the diplomatic text gets the printed (A[T]_n); everywhere else the print writes (A[T])_n.",
    corrected=r"Si $(A[T])_{\mathfrak n}$ est caténaire")
add(96, "proof of (5.5.7) (ii): 'sont égaux (0, 16.1.4), donc aussi'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"(0, 16.1.4), donc aussi", r"(\textbf{0}, 16.1.4), donc aussi", "")
add(96, "(5.5.8.1), left side: 'deg.tr_A B'", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"l'inégalité¶\begin{equation}¶\dim(A)+\operatorname{deg.tr.}_A B", r"l'inégalité¶\begin{equation}¶\dim(A)+\operatorname{deg.tr}_A B", "")
add(96, "(5.5.8.1), right side: 'deg.tr_k k'.'", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"\operatorname{deg.tr.}_k k'.¶\tag{5.5.8.1}", r"\operatorname{deg.tr}_k k'.¶\tag{5.5.8.1}", "")
add(96, "Théorème (5.5.8), after (5.5.8.1): 'En outre les deux membres sont égaux si'",
    "new indented paragraph after the display", r"no blank line after \end{equation}", 'other', None, 'high',
    r"\end{equation}¶En outre les deux membres", r"\end{equation}¶¶En outre les deux membres",
    "Missing paragraph break after a display.")
add(96, "proof of (5.5.8): 'si on pose S = C—r'", "long dash for the set difference (enlarged crop)", r"$S=C-\mathfrak r$",
    'convention', 7, 'high', r"$S=C-\mathfrak r$", r"$S=C\setmin\mathfrak r$", "")

# ---------------------------------------------------------------- page 97
add(97, "(5.5.8.2), left side: 'deg.tr_C B'", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"+\operatorname{deg.tr.}_C B", r"+\operatorname{deg.tr}_C B", "")
add(97, "(5.5.8.2), right side: 'deg.tr_{k_1} k'.'", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"+\operatorname{deg.tr.}_{k_1}k'.", r"+\operatorname{deg.tr}_{k_1}k'.", "")
add(97, "after (5.5.8.2): 'D'autre part l'hypothèse de récurrence donne'",
    "new indented paragraph after the display", r"no blank line after \end{equation}", 'other', None, 'high',
    r"\end{equation}¶D'autre part l'hypothèse", r"\end{equation}¶¶D'autre part l'hypothèse",
    "Missing paragraph break after a display.")
add(97, "(5.5.8.3), left side: 'deg.tr_A C'", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"+\operatorname{deg.tr.}_A C", r"+\operatorname{deg.tr}_A C", "")
add(97, "(5.5.8.3), right side: 'deg.tr_k k_1'", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"+\operatorname{deg.tr.}_k k_1", r"+\operatorname{deg.tr}_k k_1", "")
add(97, "proof of (5.5.8): 'C_r[T] = S'^{-1}C[T] où S' = C—r'", "long dash for the set difference (enlarged crop)", r"$S'=C-\mathfrak r$",
    'convention', 7, 'high', r"$S'=C-\mathfrak r$", r"$S'=C\setmin\mathfrak r$", "")
add(97, "end of the proof of (5.5.8): 'il en est de même de (C[T])_{n'} (0, 16.1.4).'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"$(C[T])_{\mathfrak n'}$ (0, 16.1.4).", r"$(C[T])_{\mathfrak n'}$ (\textbf{0}, 16.1.4).", "")
add(97, "heading 5.6", "'5.6. Formule des dimensions et anneaux universellement caténaires.' with a final full stop",
    "no full stop", 'punctuation', None, 'high',
    r"\subsection{Formule des dimensions et anneaux universellement caténaires}",
    r"\subsection{Formule des dimensions et anneaux universellement caténaires.}", "GLOBAL_ISSUES 43/58.")
add(97, "Proposition (5.6.1), label a)", "a) upright (enlarged crop)", r"\item[a)] italic inside the italic proposition",
    'convention', 6, 'high', r"\item[a)]", r"\item[\textup{a)}]", "")
add(97, "Proposition (5.6.1), label b)", "b) upright (enlarged crop)", r"\item[b)] italic inside the italic proposition",
    'convention', 6, 'high', r"\item[b)]", r"\item[\textup{b)}]", "")
add(97, "Proposition (5.6.1), label c)", "c) upright (enlarged crop)", r"\item[c)] italic inside the italic proposition",
    'convention', 6, 'high', r"\item[c)]", r"\item[\textup{c)}]", "")
add(97, "Proposition (5.6.1) c): 'essentiellement de type fini (1.3.8) B''", "(1.3.8) upright inside the italic statement (enlarged crop)",
    "italic (proposition environment)", 'convention', 6, 'high',
    r"de type fini (1.3.8) $B'$", r"de type fini \textup{(1.3.8)} $B'$", "")
add(97, "(5.6.1.1), left side: 'deg.tr_{A'}(B')'", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"\dim(A')+\operatorname{deg.tr.}_{A'}(B')", r"\dim(A')+\operatorname{deg.tr}_{A'}(B')", "")
add(97, "(5.6.1.1), right side: 'deg.tr_k k'.'", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"=\dim(B')+\operatorname{deg.tr.}_k k'.", r"=\dim(B')+\operatorname{deg.tr}_k k'.", "")
add(97, "after (5.6.1): 'Le fait que b) entraîne c)', the b)", "b) italic in the roman text (enlarged crop)", "upright",
    'convention', 6, 'high', r"Le fait que b)", r"Le fait que \emph{b)}", "")
add(97, "after (5.6.1): 'Le fait que b) entraîne c) résulte de (5.5.8)', the c)", "c) italic (enlarged crop)", "upright",
    'convention', 6, 'high', r"c) résulte de (5.5.8)", r"\emph{c)} résulte de (5.5.8)", "")
add(97, "'donc deg.tr_{A'}(B') = deg.tr_{A'}(B'')', first deg.tr", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"$\operatorname{deg.tr.}_{A'}(B')", r"$\operatorname{deg.tr}_{A'}(B')", "")
add(97, "'donc deg.tr_{A'}(B') = deg.tr_{A'}(B'')', second deg.tr", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"\operatorname{deg.tr.}_{A'}(B'')", r"\operatorname{deg.tr}_{A'}(B'')", "")
add(97, "'il suffit de montrer que (sous l'hypothèse b)) toute'", "b) italic (enlarged crop)", "upright",
    'convention', 6, 'high', r"(sous l'hypothèse b))", r"(sous l'hypothèse \emph{b)})", "")
add(97, "'Or l'hypothèse b) entraîne que toute A-algèbre'", "b) italic", "upright",
    'convention', 6, 'high', r"Or l'hypothèse b)", r"Or l'hypothèse \emph{b)}", "")
add(97, "'essentiellement de type fini est caténaire (0, 16.1.4), et A_1'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"est caténaire (0, 16.1.4), et", r"est caténaire (\textbf{0}, 16.1.4), et", "")
add(97, "'Il est trivial que b) entraîne a)', the b)", "b) italic", "upright",
    'convention', 6, 'high', r"trivial que b)", r"trivial que \emph{b)}", "")
add(97, "'Il est trivial que b) entraîne a);', the a)", "a) italic", "upright",
    'convention', 6, 'high', r"entraîne a);", r"entraîne \emph{a)};", "")
add(97, "'inversement, a) entraîne b),', the a)", "a) italic", "upright",
    'convention', 6, 'high', r"inversement, a)", r"inversement, \emph{a)}", "")
add(97, "'inversement, a) entraîne b), toute A-algèbre', the b)", "b) italic", "upright",
    'convention', 6, 'high', r"entraîne b), toute", r"entraîne \emph{b)}, toute", "")
add(97, "'quotient d'une algèbre de polynômes (0, 16.1.4).'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"polynômes¶(0, 16.1.4).", r"polynômes¶(\textbf{0}, 16.1.4).", "")
add(97, "'Reste à prouver que c) entraîne b).', the c)", "c) italic", "upright",
    'convention', 6, 'high', r"prouver que c)", r"prouver que \emph{c)}", "")
add(97, "'Reste à prouver que c) entraîne b).', the b)", "b) italic", "upright",
    'convention', 6, 'high', r"entraîne b). Comme", r"entraîne \emph{b)}. Comme", "")
add(97, "printed p. 98, l. 3 (TeX before the p. 98 marker): 'q' ⊂ q, on a (0, 16.1.4.2)'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"on a (0, 16.1.4.2)", r"on a (\textbf{0}, 16.1.4.2)",
    "Printed on p. 98; the old text lies in the p. 97 segment until the p. 98 marker is moved: apply before the marker move (end of this file).")

# ---------------------------------------------------------------- page 98
add(98, "'la formule (5.6.1.1) appliquée à A' et à B' = B_q, s'écrit'", "comma after B' = B_q (enlarged crop)", "no comma",
    'punctuation', None, 'high', r"$B'=B_{\mathfrak q}$ s'écrit", r"$B'=B_{\mathfrak q}$, s'écrit", "")
add(98, "(5.6.1.3), left side: 'deg.tr_{A_p/n}(B_q)'", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"+\operatorname{deg.tr.}_{A_{\mathfrak p}/\mathfrak n}", r"+\operatorname{deg.tr}_{A_{\mathfrak p}/\mathfrak n}", "")
add(98, "(5.6.1.3), right side: 'deg.tr_{k(p)} k(q).'", "no point after tr (enlarged crop)", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"+\operatorname{deg.tr.}_{k(\mathfrak p)}k(\mathfrak q).", r"+\operatorname{deg.tr}_{\mathbf{k}(\mathfrak p)}\boldsymbol{k}(\mathfrak q).",
    "One edit for this finding and the next two (bold k in the subscript and in k(q)).")
add(98, "(5.6.1.3): subscript k(p) of deg.tr", "bold upright k at subscript size (enlarged crop)", "plain k",
    'convention', 1, 'high', None, None, COV + " \\mathbf{k}: bold upright in subscripts (GLOBAL_ISSUES 48).")
add(98, "(5.6.1.3): k(q)", "bold italic k", "plain k", 'convention', 1, 'high', None, None, COV)
add(98, "(5.6.1.4), left side: 'deg.tr_{A_{p'}/nA_{p'}}(B_{q'})'", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"+\operatorname{deg.tr.}_{A_{\mathfrak p'}/\mathfrak nA_{\mathfrak p'}}", r"+\operatorname{deg.tr}_{A_{\mathfrak p'}/\mathfrak nA_{\mathfrak p'}}", "")
add(98, "(5.6.1.4), right side: 'deg.tr_{k(p')} k(q').'", "no point after tr (enlarged crop)", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"+\operatorname{deg.tr.}_{k(\mathfrak p')}k(\mathfrak q').", r"+\operatorname{deg.tr}_{\mathbf{k}(\mathfrak p')}\boldsymbol{k}(\mathfrak q').",
    "One edit for this finding and the next two (bold k in the subscript and in k(q')).")
add(98, "(5.6.1.4): subscript k(p') of deg.tr", "bold upright k at subscript size (enlarged crop)", "plain k",
    'convention', 1, 'high', None, None, COV)
add(98, "(5.6.1.4): k(q')", "bold italic k (enlarged crop)", "plain k", 'convention', 1, 'high', None, None, COV)
add(98, "(5.6.1.5), left side: 'deg.tr_{A_p/p'A_p}(B_q/q'B_q)'", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"+\operatorname{deg.tr.}_{A_{\mathfrak p}/\mathfrak p'A_{\mathfrak p}}", r"+\operatorname{deg.tr}_{A_{\mathfrak p}/\mathfrak p'A_{\mathfrak p}}", "")
i_form = add(98, "(5.6.1.5), right side: subscript of deg.tr",
    "subscript printed k(p( : bold k, '(', Fraktur p, a second '(' and no prime (enlarged 5x crop)",
    r"_{k(\mathfrak p')}: a prime that is neither in the print nor in the correct reading k(p)",
    'formula', None, 'high',
    r"+\operatorname{deg.tr.}_{k(\mathfrak p')}k(\mathfrak q).", r"+\operatorname{deg.tr}_{\mathbf{k}(\mathfrak p)}\boldsymbol{k}(\mathfrak q).",
    "(5.6.1.5) is (5.6.1.1) for A' = A_p/p'A_p, whose residue field is k(p) (not k(p')); with k(p) the sum of (5.6.1.4) and (5.6.1.5) gives (5.6.1.2) via (5.6.1.3). One edit for this finding and the next three (no point after tr, bold upright subscript k, bold italic k(q)); it gives the correct k(p) in both editions. Apply before the misprint entry that follows them.")
add(98, "(5.6.1.5), right side: 'deg.tr'", "no point after tr", r"\operatorname{deg.tr.}", 'punctuation', None, 'high', None, None,
    "Covered by the formula edit for the (5.6.1.5) subscript.")
add(98, "(5.6.1.5): subscript k of deg.tr", "bold upright k at subscript size", "plain k", 'convention', 1, 'high', None, None,
    "Covered by the formula edit for the (5.6.1.5) subscript.")
add(98, "(5.6.1.5): k(q)", "bold italic k", "plain k", 'convention', 1, 'high', None, None,
    "Covered by the formula edit for the (5.6.1.5) subscript.")
add(98, "(5.6.1.5), right side: subscript printed k(p(", "'(' printed for the closing parenthesis: k(p( (enlarged 5x crop)",
    r"after the formula edit: \mathbf{k}(\mathfrak p)", 'misprint_in_print', None, 'high',
    r"\mathbf{k}(\mathfrak p)}\boldsymbol{k}(\mathfrak q).¶\tag{5.6.1.5}", r"\mathbf{k}(\mathfrak p(}\boldsymbol{k}(\mathfrak q).¶\tag{5.6.1.5}",
    "Diplomatic text only: restores the printed '(' after the formula edit above (its old is the text after that edit). The corrected edition keeps k(p) from the formula edit.",
    corrected=r"\mathbf{k}(\mathfrak p)}\boldsymbol{k}(\mathfrak q).", dep=i_form)
add(98, "'notons que k(p') (resp. k(q')) est le corps des fractions', k(p')", "bold italic k", "plain k", 'convention', 1, 'high',
    r"$k(\mathfrak p')$ (resp.", r"$\boldsymbol{k}(\mathfrak p')$ (resp.", "")
add(98, "'notons que k(p') (resp. k(q')) est le corps des fractions', k(q')", "bold italic k", "plain k", 'convention', 1, 'high',
    r"$k(\mathfrak q')$) est", r"$\boldsymbol{k}(\mathfrak q')$) est", "")
add(98, "'puisque A est supposé caténaire, on a (0, 16.1.4.2)'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"caténaire, on a (0, 16.1.4.2)", r"caténaire, on a (\textbf{0}, 16.1.4.2)", "")
add(98, "unnumbered display 'dim(A_p/p'A_p) + dim(A_{p'}/nA_{p'}) = dim(A_p/n)'", "no full stop after the display (enlarged crop)",
    "full stop", 'punctuation', None, 'high',
    r"=\dim(A_{\mathfrak p}/\mathfrak n).¶\]", r"=\dim(A_{\mathfrak p}/\mathfrak n)¶\]", "")
add(98, "after the unnumbered display: 'Tenant compte de ces remarques'", "new indented paragraph after the display",
    r"no blank line after \]", 'other', None, 'high',
    r"\]¶Tenant compte", r"\]¶¶Tenant compte", "Missing paragraph break after a display.")
add(98, "Définition (5.6.2): 'A est universellement caténaire s'il'", "'universellement caténaire' italic like the rest of the definition (enlarged crop)",
    r"\emph{universellement caténaire} inside the italic definition (comes out upright)", 'convention', 6, 'high',
    r"est \emph{universellement caténaire} s'il", r"est universellement caténaire s'il", "")
add(98, "Définition (5.6.2): 'les conditions équivalentes a), b), c) de (5.6.1)', the labels", "a), b), c) upright (enlarged crop)",
    "italic (definition environment)", 'convention', 6, 'high',
    r"équivalentes a), b), c)", r"équivalentes \textup{a), b), c)}", "")
add(98, "Définition (5.6.2): '... de (5.6.1).', the reference", "(5.6.1) upright (enlarged crop)",
    "italic (definition environment)", 'convention', 6, 'high',
    r"de (5.6.1).¶\end{definition}", r"de \textup{(5.6.1)}.¶\end{definition}", "")
add(98, "Remarques (5.6.3) (i): 'comme il résulte aussitôt de (5.6.1, a))'", "a) italic", "upright (remark body judged as roman)",
    'convention', 6, 'high', r"aussitôt de (5.6.1, a))", r"aussitôt de (5.6.1, \emph{a)})", "")
add(98, "Remarques (5.6.3) (i): 'cela résulte de (5.6.1, c)), si l'on remarque'", "c) italic", "upright (remark body judged as roman)",
    'convention', 6, 'high', r"(5.6.1, c)), si l'on", r"(5.6.1, \emph{c)}), si l'on", "")
add(98, "Remarques (5.6.3) (i): 'en posant S = A—p'", "long dash for the set difference (enlarged crop)", r"$S=A-\mathfrak p$",
    'convention', 7, 'high', r"$S=A-\mathfrak p$", r"$S=A\setmin\mathfrak p$", "")
add(98, "Remarques (5.6.3) (iii): 'Le critère (5.6.1, c)) ne fait intervenir'", "c) italic", "upright (remark body judged as roman)",
    'convention', 6, 'high', r"Le critère (5.6.1, c))", r"Le critère (5.6.1, \emph{c)})", "")
add(98, "Remarques (5.6.3) (iii): 'donc des anneaux quotients intègres de A'", "'anneaux quotients intègres' italic", "upright",
    'convention', 6, 'high', r"donc des anneaux quotients¶intègres de $A$", r"donc des \emph{anneaux quotients¶intègres} de $A$", "")
add(98, "page break 98/99 in Remarques (5.6.3) (iii): 'On en conclut que si | p_i (1 ≤ i ≤ n) sont'",
    "one sentence running over the page break (p. 99 begins flush left with 'p_i')",
    r"blank lines before and after \oldpage[IV-2]{99} (paragraph break mid-sentence)", 'other', None, 'high',
    r"On en conclut que si¶¶", r"On en conclut que si¶",
    "Removes the blank line before the p. 99 marker; apply together with the p. 99 entry that removes the blank line after it (GLOBAL_ISSUES 20). The marker itself is at the right place.")

# ---------------------------------------------------------------- page 99
add(99, "page break 98/99: '\\oldpage[IV-2]{99}' then 'p_i (1 ≤ i ≤ n) sont les idéaux premiers minimaux'",
    "continuation of the sentence 'On en conclut que si', flush left",
    r"blank line after \oldpage[IV-2]{99} (paragraph break mid-sentence)", 'other', None, 'high',
    r"\oldpage[IV-2]{99}¶¶$\mathfrak p_i$", r"\oldpage[IV-2]{99}¶$\mathfrak p_i$",
    "Apply together with the last p. 98 entry (blank line before the marker).")
add(99, "Remarques (5.6.3) (iv): 'Le critère (5.6.1, b)) et la remarque (i)'", "b) italic", "upright (remark body judged as roman)",
    'convention', 6, 'high', r"Le critère (5.6.1, b))", r"Le critère (5.6.1, \emph{b)})", "")
add(99, "Remarques (5.6.3) (iv): 'de toute A-algèbre essentiellement de type fini (1.3.8)'",
    "'algèbre essentiellement de type fini' italic ('A-' upright)", "upright", 'convention', 6, 'high',
    r"$A$-algèbre essentiellement de type fini (1.3.8)", r"$A$-\emph{algèbre essentiellement de type fini} (1.3.8)", "")
add(99, "after (5.6.4): 'est régulier (0, 17.3.7)'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"(0, 17.3.7)", r"(\textbf{0}, 17.3.7)", "")
add(99, "after (5.6.4): 'donc caténaire (0, 16.5.12)'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"(0, 16.5.12)", r"(\textbf{0}, 16.5.12)", "")
add(99, "after (5.6.4): 'et l'on conclut par (5.6.1, a)).'", "a) italic", "upright", 'convention', 6, 'high',
    r"conclut par (5.6.1, a))", r"conclut par (5.6.1, \emph{a)})", "")
add(99, "'il résulte du théorème de Cohen (0, 19.8.8)'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"(0, 19.8.8)", r"(\textbf{0}, 19.8.8)", "")
add(99, "'que tout anneau local noethérien complet est universellement caténaire'", "'anneau local noethérien complet' italic", "upright",
    'convention', 6, 'high', r"que tout anneau¶local noethérien complet est", r"que tout \emph{anneau¶local noethérien complet} est", "")
add(99, "'tout préschéma localement de type fini sur un corps est universellement caténaire'", "'localement de type fini sur un corps' italic", "upright",
    'convention', 6, 'high', r"préschéma localement de type fini sur un corps est", r"préschéma \emph{localement de type fini sur un corps} est", "")
add(99, "Proposition (5.6.5): 'Soit ξ (resp. η) le point générique'", "'(resp. η)' upright (enlarged crop)", "italic (proposition environment)",
    'convention', 6, 'high', r"$\xi$ (resp. $\eta$)", r"$\xi$ \textup{(resp. $\eta$)}", "")
add(99, "Proposition (5.6.5): 'de X (resp. Y), et soit'", "'(resp. Y)' upright (enlarged crop)", "italic (proposition environment)",
    'convention', 6, 'high', r"de $X$ (resp. $Y$)", r"de $X$ \textup{(resp. $Y$)}", "")
add(99, "Proposition (5.6.5): 'e = dim(f^{-1}(η)) = ...'", "dim(f^{-1}(η)): no subscript on dim (enlarged crop)", r"\dim_\eta(f^{-1}(\eta))",
    'formula', None, 'high', r"\dim_\eta(f^{-1}(\eta))", r"\dim(f^{-1}(\eta))", "The TeX adds a subscript eta that the print does not have.")
add(99, "Proposition (5.6.5): '= deg.tr_{k(η)} k(ξ))'", "no point after tr (enlarged crop)", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"=\operatorname{deg.tr.}_{k(\eta)}k(\xi))$", r"=\operatorname{deg.tr}_{\mathbf{k}(\eta)}\boldsymbol{k}(\xi))$",
    "One edit for this finding and the next two (bold k in the subscript and in k(ξ)); it keeps the printed double parenthesis (misprint entry below).")
add(99, "Proposition (5.6.5): subscript k(η) of deg.tr", "bold upright k at subscript size (enlarged crop)", "plain k",
    'convention', 1, 'high', None, None, COV)
add(99, "Proposition (5.6.5): k(ξ)", "bold italic k (enlarged crop)", "plain k", 'convention', 1, 'high', None, None, COV)
add(99, "Proposition (5.6.5): 'e = dim(f^{-1}(η)) = deg.tr_{k(η)} k(ξ))', closing parentheses", "k(ξ)) with an unmatched second ')' (enlarged crop)",
    r"k(\xi))$: keeps the printed reading", 'misprint_in_print', None, 'high', None, None,
    "The TeX keeps the printed reading (one ')' too many).",
    corrected=r"=\operatorname{deg.tr}_{\mathbf{k}(\eta)}\boldsymbol{k}(\xi)$")
add(99, "Proposition (5.6.5): '(« dimension de la fibre générique », cf. (0_I, 2.1.8) et (4.1.1))'",
    "the whole parenthesis upright inside the italic statement; bold 0 in (0_I, 2.1.8) (enlarged crop)",
    "italic (proposition environment); plain 0", 'convention', 6, 'high',
    r"(« dimension de la fibre générique », cf. $(0_{\mathrm I},2.1.8)$ et¶(4.1.1)).",
    r"\textup{(« dimension de la fibre générique », cf. $(\mathbf{0}_{\mathrm I},2.1.8)$ et¶(4.1.1))}.",
    "One edit for this finding and the next (convention 2: bold 0, as on pp. 5-9).")
add(99, "Proposition (5.6.5): '(0_I, 2.1.8)'", "bold 0", "plain 0", 'convention', 2, 'high', None, None, COV)
add(99, "(5.6.5.1): 'deg.tr_{k(y)} k(x)'", "no point after tr (enlarged crop)", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"\geq\operatorname{deg.tr.}_{k(y)}k(x)", r"\geq\operatorname{deg.tr}_{\mathbf{k}(y)}\boldsymbol{k}(x)",
    "One edit for this finding and the next two (bold k in the subscript and in k(x)).")
add(99, "(5.6.5.1): subscript k(y) of deg.tr", "bold upright k at subscript size (enlarged crop)", "plain k",
    'convention', 1, 'high', None, None, COV)
add(99, "(5.6.5.1): k(x)", "bold italic k (enlarged crop)", "plain k", 'convention', 1, 'high', None, None, COV)
add(99, "(5.6.5.2): 'O_x ⊗_{O_y} k(y)'", "bold italic k (enlarged crop)", "plain k", 'convention', 1, 'high',
    r"+\dim(\mathcal O_x\otimes_{\mathcal O_y}k(y)", r"+\dim(\mathcal O_x\otimes_{\mathcal O_y}\boldsymbol{k}(y)", "")
add(99, "(5.6.5.2): '... — δ(x)'", "long dash for the subtraction (enlarged crop)", r")-\delta(x)", 'convention', 7, 'high',
    r")-\delta(x)", r")\setmin\delta(x)", "Subtraction (GLOBAL_ISSUES 23).")
add(99, "Proposition (5.6.5): 'en posant δ(x) = dim_x(f^{-1}(y)) — e.'", "long dash for the subtraction (enlarged crop)", "-e",
    'convention', 7, 'high', r"(f^{-1}(y))-e$", r"(f^{-1}(y))\setmin e$", "Subtraction (GLOBAL_ISSUES 23).")
add(99, "Proposition (5.6.5): 'les deux membres de (5.6.5.1) (resp. (5.6.5.2)) sont égaux'",
    "'(5.6.5.1) (resp. (5.6.5.2))' upright inside the italic statement (enlarged crop)", "italic (proposition environment)",
    'convention', 6, 'high', r"(5.6.5.1) (resp. (5.6.5.2))", r"\textup{(5.6.5.1) (resp. (5.6.5.2))}", "")
add(99, "proof of (5.6.5): 'de O_y et de O_x à k(η) et k(ξ)', k(η)", "bold italic k (enlarged crop)", "plain k",
    'convention', 1, 'high', r"$k(\eta)$", r"$\boldsymbol{k}(\eta)$", "")
add(99, "proof of (5.6.5): 'à k(η) et k(ξ) (I, 8.2.7)', k(ξ)", "bold italic k (enlarged crop)", "plain k",
    'convention', 1, 'high', r"$k(\xi)$", r"$\boldsymbol{k}(\xi)$", "")
add(99, "proof of (5.6.5): '(I, 8.2.7)'", "bold I", "plain I", 'convention', 2, 'high',
    r"(I, 8.2.7)", r"(\textbf{I}, 8.2.7)", "")
add(99, "proof of (5.6.5): 'en un idéal premier q (I, 3.6.5)'", "bold I", "plain I", 'convention', 2, 'high',
    r"(I, 3.6.5)", r"(\textbf{I}, 3.6.5)", "")
add(99, "proof of (5.6.5): 'En outre, O_x ⊗_{O_y} k(y) = O_x/m_y O_x'", "bold italic k", "plain k", 'convention', 1, 'high',
    r"\otimes_{\mathcal O_y}k(y)=", r"\otimes_{\mathcal O_y}\boldsymbol{k}(y)=", "")
add(99, "proof of (5.6.5): 'au point x (I, 3.6.1)'", "bold I", "plain I", 'convention', 2, 'high',
    r"(I, 3.6.1)", r"(\textbf{I}, 3.6.1)", "")
add(99, "proof of (5.6.5): 'un préschéma de type fini sur k(y)'", "bold italic k", "plain k", 'convention', 1, 'high',
    r"sur $k(y)$", r"sur $\boldsymbol{k}(y)$", "")
add(99, "display before 'l'inégalité (5.6.5.2)': 'dim(O_x ⊗_{O_y} k(y))'", "bold italic k (enlarged crop)", "plain k",
    'convention', 1, 'high', r"\dim(\mathcal O_x\otimes_{\mathcal O_y}k(y))¶=", r"\dim(\mathcal O_x\otimes_{\mathcal O_y}\boldsymbol{k}(y))¶=", "")
add(99, "same display: 'dim_x(f^{-1}(y)) — deg.tr'", "long dash for the subtraction (enlarged crop)", "-", 'convention', 7, 'high',
    r"(f^{-1}(y))-\operatorname", r"(f^{-1}(y))\setmin\operatorname", "Subtraction (GLOBAL_ISSUES 23).")
add(99, "same display: 'deg.tr_{k(y)} k(x) ;'", "no point after tr (enlarged crop)", r"\operatorname{deg.tr.}", 'punctuation', None, 'high',
    r"{deg.tr.}_{k(y)}k(x);", r"{deg.tr}_{\mathbf{k}(y)}\boldsymbol{k}(x);",
    "One edit for this finding and the next two (bold k in the subscript and in k(x)).")
add(99, "same display: subscript k(y) of deg.tr", "bold upright k at subscript size (enlarged crop)", "plain k",
    'convention', 1, 'high', None, None, COV)
add(99, "same display: k(x)", "bold italic k (enlarged crop)", "plain k", 'convention', 1, 'high', None, None, COV)

# ---------------------------------------------------------------- marker moves (apply after all other fixes of pp. 96-98)
add(97, "page break 96/97: the p. 97 marker (step 1 of 3: remove the misplaced marker)",
    "printed p. 96 ends '... en outre les corps des fractions'; printed p. 97 begins 'de B' et C_r sont ceux de B et C respectivement.'",
    r"\oldpage[IV-2]{97} stands before the display (5.5.8.2), two printed lines too late", 'marker', None, 'high',
    r"\oldpage[IV-2]{97}¶¶\begin{equation}", r"\begin{equation}",
    "Apply after every other fix of pp. 96-97, together with the next two edits (p. 96 segment).")
add(96, "page break 96/97: the p. 97 marker (step 2 of 3: insert)",
    "printed p. 97 begins with 'de B' et C_r sont ceux de B et C'", "no marker here", 'marker', None, 'high',
    r"corps des fractions de $B'$ et $C_{\mathfrak r}$", r"corps des fractions¶\oldpage[IV-2]{97}¶de $B'$ et $C_{\mathfrak r}$",
    "Inserts the marker mid-sentence on its own line (no blank lines).")
add(96, "page break 96/97: the p. 97 marker (step 3 of 3: blank line before (5.5.8.2))",
    "'on a donc, d'après (5.5.7.1)' runs on into the display (5.5.8.2) without a paragraph break",
    r"blank line after '(5.5.7.1)' (it stood before the old marker)", 'marker', None, 'high',
    r"donc, d'après (5.5.7.1)¶¶", r"donc, d'après (5.5.7.1)¶",
    "Without it a blank line would remain before \\begin{equation} after step 1.")
add(98, "page break 97/98: the p. 98 marker (step 1 of 2: remove the misplaced marker)",
    "printed p. 97 ends 'Comme tout quotient par un idéal premier'; printed p. 98 begins 'd'une A-algèbre de type fini est une A-algèbre intègre'",
    r"\oldpage[IV-2]{98} stands before 'Soient p, p'' (after (5.6.1.2)), four printed lines too late", 'marker', None, 'high',
    r"\oldpage[IV-2]{98}¶¶Soient $\mathfrak p$", r"Soient $\mathfrak p$",
    "Apply after every other fix of pp. 97-98, together with the next edit. The blank line after (5.6.1.2) remains, so 'Soient' still opens a paragraph, as printed.")
add(97, "page break 97/98: the p. 98 marker (step 2 of 2: insert)",
    "printed p. 98 begins 'd'une A-algèbre de type fini'", "no marker here", 'marker', None, 'high',
    r"par un idéal premier¶d'une $A$-algèbre", r"par un idéal premier¶\oldpage[IV-2]{98}¶d'une $A$-algèbre",
    "Inserts the marker mid-sentence on its own line (no blank lines).")

# ---------------------------------------------------------------- checks
def load(n):
    with open(os.path.join(RUN, 'page_%03d.tex' % n), encoding='utf-8', newline='') as fh:
        return fh.read().replace('\r\n', '\n')

pages = sorted({d['page'] for d in F})
texts = {n: load(n) for n in pages}
ok = True
# 1) sequential application in listed order
cur = dict(texts)
for i, d in enumerate(F):
    fx = d['fix']
    if not fx:
        continue
    c = cur[d['page']].count(fx['old'])
    if c != 1:
        ok = False
        print('SEQ FAIL', i, d['page'], d['where'], 'count', c)
    else:
        cur[d['page']] = cur[d['page']].replace(fx['old'], fx['new'], 1)
# 2) each old unique in the original text (except declared dependants)
for i, d in enumerate(F):
    fx = d['fix']
    if not fx:
        continue
    c = texts[d['page']].count(fx['old'])
    if d['_dep'] is None and c != 1:
        ok = False
        print('ORIG FAIL', i, d['page'], d['where'], 'count', c)
    if d['_dep'] is not None:
        print('dependent edit', i, 'on', d['_dep'], 'orig count', c)
# 3) pairwise: applying any single other independent edit first keeps each old unique
indep = [i for i, d in enumerate(F) if d['fix'] and d['_dep'] is None]
for i in indep:
    for j in indep:
        if i == j or F[i]['page'] != F[j]['page']:
            continue
        t = texts[F[j]['page']].replace(F[j]['fix']['old'], F[j]['fix']['new'], 1)
        c = t.count(F[i]['fix']['old'])
        if c != 1:
            ok = False
            print('PAIR FAIL', i, 'after', j, F[i]['where'], '|', F[j]['where'], 'count', c)
# 4) misprint fixes change only the misprinted characters (report diff size)
for i, d in enumerate(F):
    if d['kind'] == 'misprint_in_print' and d['fix']:
        o, n = d['fix']['old'], d['fix']['new']
        print('misprint edit', i, len(o), len(n))
print('ALL OK' if ok else 'PROBLEMS')
out = []
for d in F:
    e = {k: v for k, v in d.items() if k != '_dep'}
    out.append(e)
with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for d in F:
    k = 'misprint' if d['kind'] == 'misprint_in_print' else ('convention' if d['kind'] == 'convention' else 'normal')
    cnt[(d['page'], k)] += 1
for p in pages:
    print(p, cnt[(p, 'normal')], cnt[(p, 'convention')], cnt[(p, 'misprint')])
print('total', len(F))
