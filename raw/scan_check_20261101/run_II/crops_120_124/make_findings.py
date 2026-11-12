import json

OUT = r'user/Documents/ega_scan_check_20261101/run_II/findings_120_124.json'


def F(page, where, scan, tex, kind, conv, conf, old, new, note=''):
    d = {
        'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind,
        'convention': conv, 'confidence': conf,
        'fix': None if old is None else {'old': old, 'new': new},
        'note': note,
    }
    return d


L = []

# ---------------- page 120 ----------------
L.append(F(120, "top of page: blank line after \\oldpage[II]{120}",
    "'brique L\u2032 (resp. K\u2032) de L ...' continues the word 'alg\u00e9-|brique' and the sentence of p. 119: no paragraph break",
    "\\oldpage[II]{120} followed by a blank line (the source also has a blank line before the marker)",
    "other", None, "high",
    "\\oldpage[II]{120}\n\n$L'$", "\\oldpage[II]{120}\n$L'$",
    "Apply together with removing the blank line before the marker at the end of the p. 119 segment "
    "('fermeture alg\u00e9brique\\n\\n' -> 'fermeture alg\u00e9brique\\n', ega2-1-fr.tex ll. 10616-10617), which is not in page_120.tex. "
    "The whole word 'alg\u00e9brique' (printed alg\u00e9-|brique) stands before the marker."))

L.append(F(120, "Remarque (6.3.10), l. 2: 'soit de rang fini sur k(\u03be_i)'",
    "'de rang fini' italic, 'de' included",
    "de \\emph{rang fini}",
    "italics", None, "high",
    "soit de \\emph{rang fini} sur", "soit \\emph{de rang fini} sur",
    "Checked on a crop. Remark body judged as roman."))

L.append(F(120, "Remarque (6.3.10), l. 2: 'sur k(\u03be_i)'",
    "bold italic k", "$k(\\xi_i)$",
    "convention", 1, "high",
    "sur $k(\\xi_i)$", "sur $\\boldsymbol{k}(\\xi_i)$"))

L.append(F(120, "Remarque (6.3.10): 'est un C-module de type fini (6.3.4)'",
    "'module de type fini' italic (C- roman)",
    "$C$-module de type fini without emphasis",
    "italics", None, "high",
    "$C$-module de type fini", "$C$-\\emph{module de type fini}",
    "Checked on a crop."))

L.append(F(120, "Remarque (6.3.10): 'alg\u00e8bre de type fini sur un corps ([13], t. I, p. 267, th. 9)'",
    "([13], t. I, p. 267, th. 9): the bracket closes after the number, the locator follows outside it",
    "(\\cite[t.~I, p.~267, th.~9]{I-13}), which prints ([13, t. I, p. 267, th. 9])",
    "punctuation", None, "high",
    "(\\cite[t.~I, p.~267, th.~9]{I-13})", "(\\cite{I-13}, t.~I, p.~267, th.~9)",
    "Same repair as EGA I p. 148 ((\\cite{I-1}, p.~3-11 et 3-12)); the master file uses the standard \\cite. The 'I' of 't. I' is roman (checked on a crop at 4x)."))

L.append(F(120, "Remarque (6.3.10): 'ou sur Z [9, I, p. 93, th. 3], ou sur un anneau local'",
    "[9, I, p. 93, th. 3]: no parentheses and no 't.'",
    "(\\cite[t.~I, p.~93, th.~3]{I-9}), which prints ([9, t. I, p. 93, th. 3])",
    "extra", None, "high",
    "(\\cite[t.~I, p.~93, th.~3]{I-9})", "\\cite[I, p.~93, th.~3]{I-9}",
    "Checked on a crop. The print uses this bracket form only here; the neighbouring citations read ([13], t. I, ...) and ([25], p. 298)."))

L.append(F(120, "Remarque (6.3.10), last sentence: 'lorsque X est un sch\u00e9ma de type fini sur un corps, ou sur Z'",
    "'de type fini' italic, 'sur un corps' roman",
    "de \\emph{type fini sur un corps}",
    "italics", None, "high",
    "sch\u00e9ma de \\emph{type fini sur un corps}", "sch\u00e9ma \\emph{de type fini} sur un corps",
    "Checked on a crop."))

L.append(F(120, "(6.4.1.1): 'P(u, T)=det(T.I\u2014(u\u2297\u0031))'",
    "T.I with a baseline dot",
    "T\\cdot I (centred dot)",
    "symbol", None, "high",
    "T\\cdot I-(u\\otimes1)", "T.I-(u\\otimes1)",
    "Checked on a crop at 2.5x; as the earlier fixes f\\cdot m -> f.m and a_i\\mathbin{\\cdot}(t_i|V) -> a_i.(t_i|V)."))

L.append(F(120, "(6.4.1), after (6.4.1.2): 'on dit que les \u03c3_i(u) sont les fonctions sym\u00e9triques \u00e9l\u00e9mentaires de u'",
    "'fonctions sym\u00e9triques \u00e9l\u00e9mentaires' italic, 'de' roman",
    "\\emph{fonctions sym\u00e9triques \u00e9l\u00e9mentaires de $u$}",
    "italics", None, "high",
    "\\emph{fonctions sym\u00e9triques \u00e9l\u00e9mentaires de $u$}", "\\emph{fonctions sym\u00e9triques \u00e9l\u00e9mentaires} de $u$",
    "Checked on a crop. In (6.4.2), p. 121, the print does set 'de u' italic; the TeX is right there."))

L.append(F(120, "end of p. 120: display (6.4.1.3); the sentence continues on p. 121 with 'ce qui s'\u00e9crit aussi'",
    "p. 121 begins 'ce qui s'\u00e9crit aussi' flush left: same paragraph",
    "blank line after \\] at the end of the page segment (before \\oldpage[II]{121})",
    "other", None, "high",
    "\\tag{6.4.1.3}\n\\]\n\n", "\\tag{6.4.1.3}\n\\]\n",
    "Apply together with the p. 121 finding that removes the blank line after \\oldpage[II]{121}."))

# ---------------- page 121 ----------------
L.append(F(121, "top of page: blank line after \\oldpage[II]{121}",
    "'ce qui s'\u00e9crit aussi' continues the sentence of p. 120 after display (6.4.1.3); no indent",
    "\\oldpage[II]{121} followed by a blank line",
    "other", None, "high",
    "\\oldpage[II]{121}\n\nce qui", "\\oldpage[II]{121}\nce qui",
    "Apply together with the p. 120 end-of-page finding (blank line after \\] of (6.4.1.3))."))

L.append(F(121, "(6.4.1.4): '(det u).1_E=uQ(u)', the dot",
    "baseline dot after (det u)",
    "(\\det u)\\cdot (centred dot)",
    "symbol", None, "high",
    "(\\det u)\\cdot", "(\\det u).",
    "Checked on a crop. Independent of the next finding (non-overlapping strings)."))

L.append(F(121, "(6.4.1.4): '(det u).1_E=uQ(u)', the identity",
    "1_E: the old-style figure 1 (x-height, upright) with subscript E, as in det(1_\u2130)=1_\U0001D49C of (6.4.8.2)",
    "I_E (capital letter I)",
    "symbol", None, "high",
    "I_E=uQ(u)", "1_E=uQ(u)",
    "Checked on a crop: the glyph is the small old-style 1, not the full-height italic I of T.I in (6.4.1.1)."))

L.append(F(121, "after (6.4.1.4): '(1_E automorphisme identique de E), avec'",
    "1_E (old-style figure 1)",
    "$I_E$",
    "symbol", None, "high",
    "($I_E$ automorphisme", "($1_E$ automorphisme",
    "Same glyph as in (6.4.1.4)."))

L.append(F(121, "(6.4.2), end of the first paragraph: 'l'homomorphisme canonique x\u2192x\u22971'",
    "plain arrow \u2192", "x\\mapsto x\\otimes1",
    "convention", 3, "high",
    "$x\\mapsto x\\otimes1$", "$x\\to x\\otimes1$"))

L.append(F(121, "after Proposition (6.4.3): 'Rempla\u00e7ant u par T.I\u2014u\u22971 et A par A[T]'",
    "T.I with a baseline dot",
    "T\\cdot I (centred dot)",
    "symbol", None, "high",
    "$T\\cdot I-u\\otimes1$", "$T.I-u\\otimes1$",
    "Checked on a crop."))

L.append(F(121, "after Proposition (6.4.3): 'Mais alors l'application u\u2192det u est un homomorphisme'",
    "plain arrow \u2192", "u\\mapsto\\det u",
    "convention", 3, "high",
    "$u\\mapsto\\det u$", "$u\\to\\det u$"))

L.append(F(121, "after Proposition (6.4.3): '(si E admet un syst\u00e8me de n g\u00e9n\u00e9rateurs), donc les \u00e9l\u00e9ments det u'",
    "comma after the closing parenthesis",
    "semicolon (~;)",
    "punctuation", None, "high",
    "g\u00e9n\u00e9rateurs)~; donc", "g\u00e9n\u00e9rateurs), donc",
    "Checked on a crop."))

# ---------------- page 122 ----------------
L.append(F(122, "Corollaire (6.4.4): 'Sous les hypoth\u00e8ses de (6.4.3), si on suppose en outre'",
    "reference (6.4.3) upright inside the italic statement",
    "(\\hyperref[II.6.4.3-fr]{6.4.3}) italic in the corollary environment",
    "convention", 6, "high",
    "hypoth\u00e8ses de (\\hyperref[II.6.4.3-fr]{6.4.3})", "hypoth\u00e8ses de \\textup{(\\hyperref[II.6.4.3-fr]{6.4.3})}",
    "Checked on a crop."))

L.append(F(122, "after Proposition (6.4.5): 'est \u00e9videmment inverse de det u dans A\u2032'",
    "'dans' italic",
    "dans (roman, no emphasis)",
    "italics", None, "high",
    "inverse de $\\det u$ dans $A'$", "inverse de $\\det u$ \\emph{dans} $A'$",
    "Checked on a crop."))

L.append(F(122, "Lemme (6.4.5.1): 'tel que A\u2032 soit entier sur A'",
    "'entier' roman inside the italic statement",
    "entier (italic in the lemma environment)",
    "convention", 6, "high",
    "soit entier sur $A$", "soit \\textup{entier} sur $A$",
    "Checked on a crop."))

L.append(F(122, "after Lemme (6.4.5.1): 'premier th. de Cohen-Seidenberg ([13], t. I, p. 257, th. 3)'",
    "([13], t. I, p. 257, th. 3)",
    "(\\cite[t.~I, p.~257, th.~3]{I-13}), which prints ([13, t. I, p. 257, th. 3])",
    "punctuation", None, "high",
    "(\\cite[t.~I, p.~257, th.~3]{I-13})", "(\\cite{I-13}, t.~I, p.~257, th.~3)",
    "As on p. 120."))

L.append(F(122, "Remarque (6.4.7): 'Soit E un A-module de type fini, et supposons que E\u2297_A K soit'",
    "'supposons' italic, 'que' roman",
    "\\emph{supposons que}",
    "italics", None, "high",
    "\\emph{supposons que}", "\\emph{supposons} que",
    "Checked on a crop. Remark body judged as roman."))

L.append(F(122, "Remarque (6.4.7): 'soit un K-module libre de rang n'",
    "'libre' italic",
    "libre (no emphasis)",
    "italics", None, "high",
    "$K$-module libre de rang $n$", "$K$-module \\emph{libre} de rang $n$",
    "Checked on a crop."))

L.append(F(122, "after Lemme (6.4.7.1): 'une A-alg\u00e8bre qui est un A-module de type fini ([13], t. I, p. 255, th. 1)'",
    "([13], t. I, p. 255, th. 1)",
    "(\\cite[t.~I, p.~255, th.~1]{I-13}), which prints ([13, t. I, p. 255, th. 1])",
    "punctuation", None, "high",
    "(\\cite[t.~I, p.~255, th.~1]{I-13})", "(\\cite{I-13}, t.~I, p.~255, th.~1)",
    "As on p. 120. Independent of the end-of-page finding (non-overlapping strings)."))

L.append(F(122, "end of p. 122: 'On peut donc' continues on p. 123 with 'remplacer A par A[T]'",
    "no paragraph break: the sentence runs on to p. 123",
    "blank line at the end of the page segment (before \\oldpage[II]{123})",
    "other", None, "high",
    "On peut donc\n\n", "On peut donc\n",
    "Apply together with the p. 123 finding that removes the blank line after \\oldpage[II]{123}."))

# ---------------- page 123 ----------------
L.append(F(123, "top of page: blank line after \\oldpage[II]{123}",
    "'remplacer A par A[T] ...' continues the sentence 'On peut donc' of p. 122; flush left",
    "\\oldpage[II]{123} followed by a blank line",
    "other", None, "high",
    "\\oldpage[II]{123}\n\nremplacer", "\\oldpage[II]{123}\nremplacer",
    "Apply together with the p. 122 end-of-page finding."))

L.append(F(123, "Remarque (6.4.7), proof of (6.4.7.1): 'et de ce que v\u2192det v est un homomorphisme'",
    "plain arrow \u2192", "v\\mapsto\\det v",
    "convention", 3, "high",
    "$v\\mapsto\\det v$", "$v\\to\\det v$"))

L.append(F(123, "(6.4.8): 'que nous noterons det u et appellerons le d\u00e9terminant de u'",
    "'d\u00e9terminant' italic, 'de u' roman",
    "\\emph{d\u00e9terminant de $u$}",
    "italics", None, "high",
    "\\emph{d\u00e9terminant de $u$}", "\\emph{d\u00e9terminant} de $u$",
    "Checked on a crop."))

L.append(F(123, "(6.4.8): '(ce qui sera le cas (0, 5.4.1) pour X connexe)'",
    "bold 0", "{0, 5.4.1}",
    "convention", 2, "high",
    "{0, 5.4.1}", "{\\textbf{0}, 5.4.1}"))

L.append(F(123, "(6.4.8.3): 'det(s.u)=s^n det u'",
    "baseline dot",
    "s\\cdot u (centred dot)",
    "symbol", None, "high",
    "\\det(s\\cdot u)", "\\det(s.u)",
    "Checked on a crop at 2.5x."))

# ---------------- page 124 ----------------
L.append(F(124, "(6.4.8), second paragraph: 'si ce dernier est de rang constant) (0, 5.4.5)'",
    "bold 0", "{0, 5.4.5}",
    "convention", 2, "high",
    "{0, 5.4.5}", "{\\textbf{0}, 5.4.5}"))

L.append(F(124, "(6.4.8), after the display: '(0, 4.4.6). On a des r\u00e9sultats analogues'",
    "bold 0", "{0, 4.4.6}",
    "convention", 2, "high",
    "{0, 4.4.6}", "{\\textbf{0}, 4.4.6}"))

L.append(F(124, "(6.4.9): 'un faisceau de corps localement simple (I, 7.3.4)'",
    "bold I", "{I, 7.3.4}",
    "convention", 2, "high",
    "{I, 7.3.4}", "{\\textbf{I}, 7.3.4}"))

L.append(F(124, "(6.4.9): 'un R(X)-Module localement libre (I, 7.3.6)'",
    "bold I", "{I, 7.3.6}",
    "convention", 2, "high",
    "{I, 7.3.6}", "{\\textbf{I}, 7.3.6}"))

L.append(F(124, "(6.4.9): 'que l'on appelle encore d\u00e9terminant de u'",
    "'d\u00e9terminant' italic, 'de u' roman",
    "\\emph{d\u00e9terminant de $u$}",
    "italics", None, "high",
    "\\emph{d\u00e9terminant de $u$}", "\\emph{d\u00e9terminant} de $u$",
    "Checked on a crop."))

L.append(F(124, "(6.4.9): 'de l'homomorphisme u\u2192det u, appliqu\u00e9 aux modules de sections'",
    "plain arrow \u2192", "u\\mapsto\\det u",
    "convention", 3, "high",
    "$u\\mapsto\\det u$", "$u\\to\\det u$"))

L.append(F(124, "(6.4.9), last paragraph: 'f^*(R(Y))\u2192R(X) (I, 7.3.8 (1))'",
    "bold I", "{I, 7.3.8}",
    "convention", 2, "high",
    "{I, 7.3.8}", "{\\textbf{I}, 7.3.8}"))

L.append(F(124, "last line: 'Si v est un endo-' (word continued as 'morphisme' on p. 125)",
    "'endomorphisme' hyphenated across the page break; word and sentence continue on p. 125",
    "endo-\\n\\n\\oldpage[II]{125}\\n\\nmorphisme: the hyphen is typeset and the blank lines make a paragraph break inside the word",
    "other", None, "high",
    "endo-\n\n", "endo%\n",
    "As canoni-/quement at pp. 36-37. Apply together with the p. 125 fix '\\oldpage[II]{125}\\n\\nmorphisme' -> "
    "'\\oldpage[II]{125}\\nmorphisme' (not in this batch); \\oldpage ends with \\ignorespaces, so the result typesets 'endomorphisme'."))

with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(L, f, ensure_ascii=False, indent=1)
    f.write('\n')
print(len(L), 'findings written')
