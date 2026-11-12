# -*- coding: utf-8 -*-
"""Build and validate findings_116_120.json (checker helper; reads page TeX only)."""
import json
import os
import sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, "findings_116_120.json")
N = "\n"

GLY = "Fraktur L (the same glyph is written \\mathfrak L in ega0-19-fr.tex, p. 82; 8x crop)"
WAVY = "Wavy arrow, neither a plain arrow nor a maps-to arrow (GLOBAL_ISSUES 33)."
ONE = ("Identity map 1_E written with the old-style figure 1 (x-height, looks like a small-capital I); "
       "ega0-18-fr.tex writes such identities 1_B. The TeX's roman capital I is a misreading.")
REF6 = "Reference number and its parentheses upright in the print (as the earlier page fixes, e.g. pp. 16, 27, 36)."


def F(page, where, scan, tex, kind, old, new, conv=None, conf="high", note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []

# ---------------- page 116 ----------------
L += [
    F(116, "Exemples (19.10.3), (i): 'l'homomorphisme composé A->B->E doit être l'homomorphisme structural'",
      "label rho over the first arrow: A ->(rho) B ->(v) E (3x crop)",
      "$A\\xrightarrow{j}B\\xrightarrow{v}E$: label j (the notation of (ii))", "formula",
      r"$A\xrightarrow{j}B\xrightarrow{v}E$ doit", r"$A\xrightarrow{\rho}B\xrightarrow{v}E$ doit",
      note="In (i) the structural homomorphism is called rho; j is introduced only in (ii). The second composite, in (ii), has j in the print too."),
    F(116, "(19.10.3) (iii): 'pour qu'une extension de type fini K d'un corps k'",
      "'de type fini' all italic, 'de' included (crop)", "de \\emph{type fini}", "italics",
      r"de \emph{type fini}", r"\emph{de type fini}"),
    F(116, "Remarque (19.10.4): 'le noyau de p : E->C est de carré nul'",
      "'de carré nul' italic, 'de' included (crop)", "est de \\emph{carré nul}", "italics",
      r"est de" + N + r"\emph{carré nul}", r"est" + N + r"\emph{de carré nul}",
      note="Emphasis judged as if the remark body were roman."),
    F(116, "Remarque (19.10.4): '(sans quoi ...) et en remplaçant C par u(B)'",
      "'et en remplaçant': no comma after 'et' (crop)", "et, en remplaçant", "punctuation",
      "et, en remplaçant", "et en remplaçant"),
    F(116, "Remarque (19.10.4), end: 'supposer u et p surjectifs.'",
      "'surjectifs' italic (crop)", "surjectifs without \\emph", "italics",
      r"$p$ surjectifs.", r"$p$ \emph{surjectifs}.",
      note="Emphasis judged as if the remark body were roman."),
    F(116, "§ 20 introduction: 'avec la notion d'algèbre formellement lisse'",
      "'formellement lisse' italic (crop)", "formellement lisse (no \\emph)", "italics",
      "d'algèbre formellement lisse,", r"d'algèbre \emph{formellement lisse},",
      note="In the page-116 continuation: ega0-20-fr.tex, before its first page marker (outside the page-116 segment)."),
    F(116, "heading 20.1 'Dérivations et extensions d'algèbres' (end of page_116.tex)",
      "p. 116 ends with the § 20 introduction ('... faite au § 7 du chapitre IV.'); the heading 20.1 is the first line of p. 117",
      "\\subsection{Dérivations et extensions d'algèbres} and its \\label stand before \\oldpage[0\\textsubscript{IV-1}]{117} (ega0-20-fr.tex lines 16-19)",
      "marker",
      r"\subsection{Dérivations et", r"\oldpage[0\textsubscript{IV-1}]{117}" + N + r"\subsection{Dérivations et",
      note="In ega0-20-fr.tex before its first page marker (outside the page-116 segment). Move, part 1 of 2: inserts the p. 117 marker before the heading; the page-117 marker finding removes the old marker. Apply both or neither."),
    F(116, "heading 20.1 (printed at the top of p. 117)",
      "'20.1. Dérivations et extensions d'algèbres.' with a final full stop",
      "\\subsection{Dérivations et extensions d'algèbres}", "punctuation",
      "extensions d'algèbres}", "extensions d'algèbres.}",
      note="In ega0-20-fr.tex before its first page marker (outside the page-116 segment). GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop)."),
]

# ---------------- page 117 ----------------
L += [
    F(117, "top of p. 117: page marker",
      "p. 117 begins with the heading '20.1. Dérivations et extensions d'algèbres.'",
      "\\oldpage[0\\textsubscript{IV-1}]{117} stands after the 20.1 heading, just before \\begin{proposition}[20.1.1]",
      "marker",
      r"\oldpage[0\textsubscript{IV-1}]{117}" + N + r"\begin{proposition}[20.1.1]", r"\begin{proposition}[20.1.1]",
      note="Move, part 2 of 2: removes the old marker; apply only together with the page-116 marker finding, which inserts it before \\subsection{Dérivations et extensions d'algèbres}."),
    F(117, "Proposition (20.1.1), line 1: 'Soient A un anneau (non nécessairement commutatif)'",
      "the parenthetical is roman inside the italic statement (crop)",
      "(non nécessairement commutatif) italic (itshape environment)", "convention",
      "(non nécessairement commutatif)", r"\textup{(non nécessairement commutatif)}", conv=6),
    F(117, "Proposition (20.1.1), line 2: 'dont le noyau L est de carré nul' (Fraktur)",
      GLY, "$\\mathfrak{Q}$ (Fraktur Q)", "symbol",
      r"noyau $\mathfrak{Q}$" + N + "est de carré nul", r"noyau $\mathfrak{L}$" + N + "est de carré nul"),
    F(117, "Proposition (20.1.1): 'où D : B->L (Fraktur) est une application'",
      GLY, "$D:B\\to\\mathfrak{Q}$", "symbol",
      r"$D:B\to\mathfrak{Q}$", r"$D:B\to\mathfrak{L}$"),
    F(117, "proof of (20.1.1), line 1: 'D(f)=v(f)—v_0(f)'",
      "long dash for the subtraction (crop)", "v(f)-v_0(f)", "convention",
      "v(f)-v_0(f)", r"v(f)\setmin v_0(f)", conv=7,
      note="Subtraction, not set difference (GLOBAL_ISSUES 23)."),
    F(117, "proof of (20.1.1): 'appartient à L (Fraktur)'",
      GLY, "$\\mathfrak{Q}$", "symbol",
      r"appartient à $\mathfrak{Q}$", r"appartient à $\mathfrak{L}$"),
    F(117, "proof of (20.1.1): 'L (Fraktur) étant de carré nul'",
      GLY, "$\\mathfrak{Q}$", "symbol",
      r"$\mathfrak{Q}$ étant de carré nul", r"$\mathfrak{L}$ étant de carré nul"),
    F(117, "proof of (20.1.1), after the display: 'si D est nulle dans rho(A)'",
      "'nulle dans' italic (crop)", "nulle dans (no \\emph)", "italics",
      r"est nulle dans $\rho(A)$", r"est \emph{nulle dans} $\rho(A)$"),
    F(117, "Définition (20.1.2): 'on appelle A-dérivation de B dans L une application'",
      "'A-dérivation de B dans L' italic like the rest of the statement (crop)",
      "\\emph{$A$-dérivation de $B$ dans $L$}: upright inside the itshape definition", "convention",
      r"\emph{$A$-dérivation de $B$ dans $L$}", r"$A$-dérivation de $B$ dans $L$", conv=6,
      note="Printed italic words left upright."),
    F(117, "Définition (20.1.2): 'vérifiant les conditions (i) et (ii) de (20.1.1)': (i)",
      "(i) upright (crop)", "(i) italic inside the definition", "convention",
      "vérifiant" + N + "les conditions (i)", "vérifiant" + N + r"les conditions \textup{(i)}", conv=6),
    F(117, "Définition (20.1.2): '... (i) et (ii) de (20.1.1)': (ii)",
      "(ii) upright (crop)", "(ii) italic inside the definition", "convention",
      "et (ii) de", r"et \textup{(ii)} de", conv=6),
    F(117, "Définition (20.1.2): '... de (20.1.1).': the reference",
      "(20.1.1) upright (crop)", "\\sref{0.20.1.1-fr} italic inside the definition", "convention",
      r"\sref{0.20.1.1-fr}." + N + r"\end{definition}", r"\textup{\sref{0.20.1.1-fr}}." + N + r"\end{definition}",
      conv=6, note=REF6),
    F(117, "after (20.1.2): 'Il résulte de (20.1.1.1) que le noyau d'une A-dérivation'",
      "(20.1.1.1) (crop)", "\\sref{0.20.1.1-fr}, which prints (20.1.1)", "number",
      r"Il résulte de \sref{0.20.1.1-fr} que", r"Il résulte de \sref{0.20.1.1.1-fr} que"),
    F(117, "same sentence: 'est un sous-A-anneau de B'",
      "'sous-' and 'anneau' italic (crop)", "sous-$A$-anneau (no \\emph)", "italics",
      r"est un sous-$A$-anneau de $B$.", r"est un \emph{sous-}$A$-\emph{anneau} de $B$."),
    F(117, "'On appelle parfois dérivation de B dans L une Z-dérivation, c'est-à-dire'",
      "'dérivation' after the bold Z italic (crop)", "$\\mathbf{Z}$-dérivation (no \\emph)", "italics",
      r"$\mathbf{Z}$-dérivation, c'est-à-dire", r"$\mathbf{Z}$-\emph{dérivation}, c'est-à-dire"),
    F(117, "'toute Z-dérivation de B est une P-dérivation :'",
      "'dérivation' of 'P-dérivation' italic; the preceding 'Z-dérivation' is roman (crop)",
      "$P$-dérivation (no \\emph)", "italics",
      "$P$-dérivation :", r"$P$-\emph{dérivation} :"),
    F(117, "'il en est de même de D—D''",
      "long dash for the subtraction (crop)", "$D-D'$", "convention",
      "$D-D'$", r"$D\setmin D'$", conv=7,
      note="Subtraction, not set difference (GLOBAL_ISSUES 23)."),
    F(117, "last sentence: 'et L un B-module, alors, pour toute'",
      "'module' italic (crop)", "$B$-module (no \\emph)", "italics",
      "$L$ un $B$-module, alors", r"$L$ un $B$-\emph{module}, alors"),
]

# ---------------- page 118 ----------------
L += [
    F(118, "Corollaire (20.1.3), line 2: 'dont le premier a un noyau L (Fraktur) de carré nul'",
      GLY, "$\\mathfrak{Q}$", "symbol",
      r"noyau $\mathfrak{Q}$ de carré nul", r"noyau $\mathfrak{L}$ de carré nul"),
    F(118, "Corollaire (20.1.3), end: 'pour le groupe Dér_A(B, L (Fraktur))'",
      GLY, "\\operatorname{D\\acute{e}r}_A(B,\\mathfrak{Q})", "symbol",
      r"(B,\mathfrak{Q})", r"(B,\mathfrak{L})"),
    F(118, "Corollaire (20.1.4): 'associe l'application x ~> x+D(p(x))'",
      "wavy arrow (crop)", "$x\\mapsto x+D(p(x))$", "symbol",
      r"$x\mapsto x+D(p(x))$", r"$x\leadsto x+D(p(x))$", note=WAVY),
    F(118, "proof of (20.1.4), line 1: 'pour B=E, v_0=1_E :'",
      "1_E with the old-style figure 1 (3x crop)", "$v_0=\\mathrm{I}_E$ (roman capital I)", "symbol",
      r"$v_0=\mathrm{I}_E$ :", r"$v_0=1_E$ :", note=ONE),
    F(118, "proof of (20.1.4), line 2: 'des applications v=1_E+D''",
      "1_E with the old-style figure 1 (3x crop)", "$v=\\mathrm{I}_E+D'$", "symbol",
      r"$v=\mathrm{I}_E+D'$", r"$v=1_E+D'$", note=ONE),
    F(118, "Corollaire (20.1.5): 'associe l'application alpha : x ~> (u(x), D(x))'",
      "wavy arrow (crop)", "$\\alpha:x\\mapsto(u(x),D(x))$", "symbol",
      r"$\alpha:x\mapsto(u(x),D(x))$", r"$\alpha:x\leadsto(u(x),D(x))$", note=WAVY),
    F(118, "Corollaire (20.1.5): 'v : B->D_C(L) (cf. 18.2.3) tels que'",
      "'(cf. 18.2.3)' roman inside the italic statement (crop)", "(cf. 18.2.3) italic", "convention",
      "(cf. 18.2.3)", r"\textup{(cf. 18.2.3)}", conv=6),
    F(118, "Corollaire (20.1.6), 1°: 'la A-équivalence (x, y) ~> (x, y+D(x))'",
      "wavy arrow (crop)", "$(x,y)\\mapsto(x,y+D(x))$", "symbol",
      r"$(x,y)\mapsto(x,y+D(x))$", r"$(x,y)\leadsto(x,y+D(x))$", note=WAVY),
    F(118, "Corollaire (20.1.6), 2°: 'le A-homomorphisme x ~> (x, D(x))'",
      "wavy arrow (crop)", "$x\\mapsto(x,D(x))$", "symbol",
      r"$x\mapsto(x,D(x))$", r"$x\leadsto(x,D(x))$", note=WAVY),
    F(118, "Corollaire (20.1.7), line 1: 'C un A-anneau, L un A-bimodule, E une A-extension triviale de C par L'",
      "'L un A-bimodule' (crop)", "$L$ un $A$-bimodule: keeps the printed reading", "misprint_in_print",
      None, None, conf="medium", corrected=r"$L$ un $C$-bimodule",
      note="An A-extension (here the trivial one D_C(L)) of C by L requires L to be a C-bimodule, as in (20.1.4) ('L un C-bimodule, E une A-extension de C par L'). Not in the Err_IV list."),
    F(118, "Corollaire (20.1.7): 'l'ensemble des applications x ~> x—w(p(x))': the arrow",
      "wavy arrow (crop)", "$x\\mapsto x-w(p(x))$", "symbol",
      r"applications $x\mapsto x", r"applications $x\leadsto x", note=WAVY),
    F(118, "Corollaire (20.1.7): 'x—w(p(x))': the dash",
      "long dash for the subtraction (crop)", "x-w(p(x))", "convention",
      "-w(p(x))$", r"\setmin w(p(x))$", conv=7,
      note="Subtraction (GLOBAL_ISSUES 23). Does not overlap the arrow fix above."),
    F(118, "proof of (20.1.7), line 1: 'pour B=E, v_0=1_E;'",
      "1_E with the old-style figure 1 (crop)", "$v_0=\\mathrm{I}_E$", "symbol",
      r"$v_0=\mathrm{I}_E$ ;", r"$v_0=1_E$ ;", note=ONE),
    F(118, "proof of (20.1.7), line 1: 'si v=1_E—D': the identity",
      "1_E with the old-style figure 1 (crop)", "$v=\\mathrm{I}_E-D$", "symbol",
      r"si $v=\mathrm{I}_E", r"si $v=1_E", note=ONE),
    F(118, "proof of (20.1.7), line 1: 'si v=1_E—D': the dash",
      "long dash for the subtraction (crop)", "-D", "convention",
      "-D$, la condition", r"\setmin D$, la condition", conv=7,
      note="Subtraction (GLOBAL_ISSUES 23). Does not overlap the identity fix above."),
    F(118, "proof of (20.1.7): 'équivaut à p o w=1_C'",
      "1_C with the old-style figure 1", "$p\\circ w=\\mathrm{I}_C$", "symbol",
      r"$p\circ w=\mathrm{I}_C$", r"$p\circ w=1_C$", note=ONE),
    F(118, "heading 20.2 'Propriétés fonctorielles des dérivations' (end of page_118.tex)",
      "p. 118 ends with the proof of (20.1.7); the heading 20.2 is the first line of p. 119",
      "\\subsection{Propriétés fonctorielles des dérivations} and its \\label stand before \\oldpage[0\\textsubscript{IV-1}]{119}",
      "marker",
      r"\end{proof}" + N + N + r"\subsection{Propriétés",
      r"\end{proof}" + N + N + r"\oldpage[0\textsubscript{IV-1}]{119}" + N + r"\subsection{Propriétés",
      note="Move, part 1 of 2: inserts the p. 119 marker before the heading; the page-119 marker finding removes the old marker. Apply both or neither."),
    F(118, "heading 20.2 (printed at the top of p. 119)",
      "'20.2. Propriétés fonctorielles des dérivations.' with a final full stop",
      "\\subsection{Propriétés fonctorielles des dérivations}", "punctuation",
      "fonctorielles des dérivations}", "fonctorielles des dérivations.}",
      note="GLOBAL_ISSUES 43/58."),
]

# ---------------- page 119 ----------------
L += [
    F(119, "top of p. 119: page marker",
      "p. 119 begins with the heading '20.2. Propriétés fonctorielles des dérivations.'",
      "\\oldpage[0\\textsubscript{IV-1}]{119} stands after the 20.2 heading, just before \\begin{env}[20.2.1]",
      "marker",
      r"\oldpage[0\textsubscript{IV-1}]{119}" + N + r"\begin{env}[20.2.1]", r"\begin{env}[20.2.1]",
      note="Move, part 2 of 2: removes the old marker; apply only together with the page-118 marker finding, which inserts it before \\subsection{Propriétés fonctorielles des dérivations}."),
    F(119, "(20.2.1), line 3: 'l'application D ~> w o D'",
      "wavy arrow (crop)", "$D\\mapsto w\\circ D$", "symbol",
      r"$D\mapsto w\circ D$", r"$D\leadsto w\circ D$", note=WAVY),
    F(119, "(20.2.1): '(20.2.1.1) est un homomorphisme de A-modules.'",
      "'modules' italic (crop)", "$A$-modules (no \\emph)", "italics",
      r"\sref{0.20.2.1.1-fr} est un" + N + r"homomorphisme de $A$-modules.",
      r"\sref{0.20.2.1.1-fr} est un" + N + r"homomorphisme de $A$-\emph{modules}.",
      note="The same phrase after (20.2.1.2) is roman in the print and needs no change."),
    F(119, "(20.2.1), second paragraph: 'alors l'application D ~> D o v'",
      "wavy arrow (crop)", "$D\\mapsto D\\circ v$", "symbol",
      r"$D\mapsto D\circ v$", r"$D\leadsto D\circ v$", note=WAVY),
    F(119, "(20.2.1), third paragraph: 'et L un B-module (20.2.1.3) est un di-homomorphisme'",
      "no comma between 'B-module' and '(20.2.1.3)' (crop)", "$L$ un $B$-module, \\sref{0.20.2.1.3-fr}", "punctuation",
      r"$L$ un $B$-module, \sref{0.20.2.1.3-fr}", r"$L$ un $B$-module \sref{0.20.2.1.3-fr}"),
    F(119, "left diagram, bottom arrow Dér_A(B, L') -> Dér_A(B', L')",
      "label v^0 below the arrow (crop)", "\\ar[r]^{v^0} (label above)", "formula",
      r"(B,L') \ar[r]^{v^0}", r"(B,L') \ar[r]_{v^0}",
      note="The top arrows have their labels above, as in the TeX."),
    F(119, "right diagram, bottom arrow Dér_A(B, L') -> Dér_A'(B, L')",
      "label u^0 below the arrow (crop)", "\\ar[r]^{u^0} (label above)", "formula",
      r"(B,L') \ar[r]^{u^0}", r"(B,L') \ar[r]_{u^0}"),
    F(119, "last line: 'pour tout homomorphisme w : L->L' de B-bimodules.'",
      "'bimodules' italic (crop)", "$B$-bimodules (no \\emph)", "italics",
      r"de $B$-bimodules." + N + r"\end{env}", r"de $B$-\emph{bimodules}." + N + r"\end{env}"),
]

# ---------------- page 120 ----------------
L += [
    F(120, "Théorème (20.2.2), display (20.2.2.1), start of the second line",
      "the second line begins with an arrow labelled with the partial sign, repeating the one at the end of the first line (crop)",
      "&\\to\\operatorname{Exan}_B(C,L) (unlabelled arrow)", "formula",
      r"&\to\operatorname{Exan}_B(C,L)", r"&\xrightarrow{\partial}\operatorname{Exan}_B(C,L)"),
    F(120, "Théorème (20.2.2): 'les homomorphismes (20.2.1.3) et (20.2.1.2)': (20.2.1.3)",
      "(20.2.1.3) upright (crop)", "(20.2.1.3) italic inside the theorem", "convention",
      "homomorphismes (20.2.1.3)", r"homomorphismes \textup{(20.2.1.3)}", conv=6, note=REF6),
    F(120, "Théorème (20.2.2): '... et (20.2.1.2) respectivement': (20.2.1.2)",
      "(20.2.1.2) upright (crop)", "(20.2.1.2) italic", "convention",
      "et (20.2.1.2)" + N + "respectivement", r"et \textup{(20.2.1.2)}" + N + "respectivement", conv=6),
    F(120, "Théorème (20.2.2): 'définis dans (18.3.4.1) et (18.3.3.1)': (18.3.4.1)",
      "(18.3.4.1) upright (crop)", "(18.3.4.1) italic", "convention",
      "dans (18.3.4.1)", r"dans \textup{(18.3.4.1)}", conv=6),
    F(120, "Théorème (20.2.2): '... et (18.3.3.1) respectivement': (18.3.3.1)",
      "(18.3.3.1) upright (crop)", "(18.3.3.1) italic", "convention",
      "(18.3.3.1) respectivement, et", r"\textup{(18.3.3.1)} respectivement, et", conv=6),
    F(120, "Théorème (20.2.2): 'par le A-homomorphisme alpha : x ~> (v(x), D(x))'",
      "wavy arrow (crop)", "$\\alpha:x\\mapsto(v(x),D(x))$", "symbol",
      "par le" + N + r"$A$-homomorphisme $\alpha:x\mapsto", "par le" + N + r"$A$-homomorphisme $\alpha:x\leadsto",
      note=WAVY),
    F(120, "Théorème (20.2.2): '(cf. (20.1.5))'",
      "'(cf. (20.1.5))' roman inside the italic statement (crop)", "(cf. \\sref{0.20.1.5-fr}) italic", "convention",
      "(cf." + N + r"\sref{0.20.1.5-fr})", r"\textup{(cf." + N + r"\sref{0.20.1.5-fr})}", conv=6),
    F(120, "Théorème (20.2.2): 'En outre, la suite exacte (20.2.2.1) est fonctorielle'",
      "(20.2.2.1) upright (crop)", "\\sref{0.20.2.2.1-fr} italic", "convention",
      r"suite exacte \sref{0.20.2.2.1-fr}", r"suite exacte \textup{\sref{0.20.2.2.1-fr}}", conv=6, note=REF6),
    F(120, "Théorème (20.2.2): '(pour les homomorphismes définis dans (20.2.1.1) et (18.3.1.1) respectivement)': (20.2.1.1)",
      "(20.2.1.1) upright; the surrounding words and the outer parentheses italic (crop)", "(20.2.1.1) italic", "convention",
      "dans (20.2.1.1)", r"dans \textup{(20.2.1.1)}", conv=6),
    F(120, "Théorème (20.2.2), same parenthesis: (18.3.1.1)",
      "(18.3.1.1) upright (crop)", "(18.3.1.1) italic", "convention",
      "(18.3.1.1) respectivement)", r"\textup{(18.3.1.1)} respectivement)", conv=6),
    F(120, "proof of (20.2.2), line 2: 'le A-homomorphisme alpha : x ~> (v(x), D(x)) définit bien'",
      "wavy arrow (crop)", "$\\alpha:x\\mapsto(v(x),D(x))$", "symbol",
      r"le $A$-homomorphisme" + N + r"$\alpha:x\mapsto", r"le $A$-homomorphisme" + N + r"$\alpha:x\leadsto",
      note=WAVY),
    F(120, "proof, 3): 'la B-extension définie par alpha : x ~> (v(x), D(x))'",
      "wavy arrow (crop)", "$\\alpha:x\\mapsto(v(x),D(x))$", "symbol",
      "définie par" + N + r"$\alpha:x\mapsto", "définie par" + N + r"$\alpha:x\leadsto", note=WAVY),
    F(120, "proof, 3): 'un B-homomorphisme z ~> (z, w(z))'",
      "wavy arrow (crop)", "$z\\mapsto(z,w(z))$", "symbol",
      r"$z\mapsto(z,w(z))$", r"$z\leadsto(z,w(z))$", note=WAVY),
    F(120, "proof, 3): 'est de la forme z ~> (z, D'(z))'",
      "wavy arrow (crop)", "$z\\mapsto(z,D'(z))$", "symbol",
      r"$z\mapsto(z,D'(z))$", r"$z\leadsto(z,D'(z))$", note=WAVY),
    F(120, "proof, 4): 'définie par l'homomorphisme t ~> (u(t), 0)'",
      "wavy arrow (crop)", "$t\\mapsto(u(t),0)$", "symbol",
      r"$t\mapsto(u(t),0)$", r"$t\leadsto(u(t),0)$", note=WAVY),
    F(120, "proof, 4): 'définie par un homomorphisme alpha : x ~> (v(x), D(x)), où D est une'",
      "wavy arrow (crop)", "$\\alpha:x\\mapsto(v(x),D(x))$", "symbol",
      r"un homomorphisme $\alpha:x\mapsto", r"un homomorphisme $\alpha:x\leadsto", note=WAVY),
    F(120, "proof, 4): 'où D est une Z-dérivation de B dans L (20.1.5)'",
      "'dérivation' italic after the bold Z (crop)", "$\\mathbf{Z}$-dérivation (no \\emph)", "italics",
      r"$\mathbf{Z}$-dérivation de $B$ dans $L$ \sref{0.20.1.5-fr}",
      r"$\mathbf{Z}$-\emph{dérivation} de $B$ dans $L$ \sref{0.20.1.5-fr}",
      note="The 'Z-dérivation' in the first line of the proof is roman in the print and needs no change."),
    F(120, "proof, 4): 'donc que D est une A-dérivation ou encore'",
      "'dérivation' italic (crop)", "$A$-dérivation (no \\emph)", "italics",
      "est une $A$-dérivation ou encore", r"est une $A$-\emph{dérivation} ou encore"),
]

# ---------------- validation ----------------
ok = True
pages = {}
for p in sorted({d["page"] for d in L}):
    with open(os.path.join(RUN, f"page_{p:03d}.tex"), encoding="utf-8", newline="") as fh:
        pages[p] = fh.read().replace("\r\n", "\n")
    if "\r" in pages[p]:
        print("WARNING: stray CR in page", p)
for i, d in enumerate(L):
    fx = d["fix"]
    if fx is None:
        continue
    n = pages[d["page"]].count(fx["old"])
    if n != 1:
        ok = False
        print("BAD", d["page"], i, n, repr(fx["old"]))
# overlap check: spans of olds on the same page must not overlap
for p in pages:
    spans = []
    for d in L:
        if d["page"] == p and d["fix"]:
            s = pages[p].find(d["fix"]["old"])
            spans.append((s, s + len(d["fix"]["old"]), d["where"][:50]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP", p, a, b)

counts = {}
for d in L:
    c = counts.setdefault(d["page"], [0, 0, 0])
    if d["kind"] == "misprint_in_print":
        c[2] += 1
    elif d["kind"] == "convention":
        c[1] += 1
    else:
        c[0] += 1
print("counts (normal/convention/misprint):", counts)
if not ok:
    sys.exit(1)
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(L, fh, ensure_ascii=False, indent=1)
print("wrote", OUT, len(L))
