"""Write findings_140_144.json for the EGA IV-3 scan check (pp. 140-144) and verify every fix."""
import json
import pathlib

here = pathlib.Path(__file__).parent
run = here.parent
OUT = run / "findings_140_144.json"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 139/140 break ----------------
add(139, "end of page_139.tex, before \\oldpage[IV-3]{140}: Remarque (11.3.12), 'Soient A un anneau, ..., M un B-module de présentation finie, J un | idéal de A'",
    "p. 140 begins 'idéal de A, p un idéal premier de B contenant JB.' flush left: the sentence of p. 139 continues (page_139_s4.png, page_140_s1.png)",
    "blank line after '$\\mathfrak J$ un' before the p. 140 marker: a paragraph break mid-sentence",
    "marker", None, "high", "$\\mathfrak J$ un\n\n", "$\\mathfrak J$ un\n",
    "OUTSIDE pp. 140-144 (last line of page_139.tex). Apply together with the next entry (blank line after the marker); both are needed. The pp. 135-139 checker may report the same edit; apply once.")
add(140, "top of p. 140: 'idéal de A, p un idéal premier de B contenant JB'",
    "flush left, continuing the sentence begun at the foot of p. 139",
    "blank line after \\oldpage[IV-3]{140}: paragraph break mid-sentence",
    "marker", None, "high", "\\oldpage[IV-3]{140}\n\nidéal de $A$", "\\oldpage[IV-3]{140}\nidéal de $A$",
    "Apply together with the page-139 entry (blank line before the marker). The marker itself stands in the right place.")

# ---------------- page 140 ----------------
add(140, "Remarque (11.3.12), after the items a), b): 'Lorsque A est noethérien, c'est une conséquence de ...'",
    "'Lorsque' begins a new, indented paragraph", "\\end{enumerate} directly followed by the text: no paragraph indent",
    "other", None, "medium", "\\end{enumerate}\nLorsque", "\\end{enumerate}\n\nLorsque",
    "Paragraph indent only (GLOBAL_ISSUES 80).")
add(140, "Remarque (11.3.12): 'lorsqu'on remplace la condition b) ci-dessus'",
    "'b)' italic (enlarged crop)", "plain b) (remark body judged as roman)",
    "italics", None, "high", "la condition b) ci-dessus", "la condition \\emph{b)} ci-dessus",
    "Remark printed roman; the letters of the conditions are italic, as the item labels a), b) above.")
add(140, "Remarque (11.3.12): 'l'une des conditions c), d) de (0_III, 10.2.1)'",
    "'c)' and 'd)' italic (enlarged crop)", "plain c), d)",
    "italics", None, "high", "conditions c), d) de", "conditions \\emph{c)}, \\emph{d)} de", None)
add(140, "Remarque (11.3.12): 'tel que l'intersection R = ⋂_{n≥0} J^{n+1} ne soit pas réduite à 0'",
    "the formula stands in the running text ('R = ⋂ J^{n+1} ne soit pas réduite à 0 (par exemple ...' on one line)",
    "displayed with \\[ ... \\]",
    "formula", None, "high",
    "l'intersection\n\\[\n\\mathfrak R=\\bigcap_{n\\geq0}\\mathfrak J^{n+1}\n\\]\n",
    "l'intersection $\\mathfrak R=\\bigcap_{n\\geq0}\\mathfrak J^{n+1}$\n",
    "Display vs inline; no connecting word lost. The Fraktur letter is a genuine Fraktur R (compared at 6x with the radical R of p. 106 and the Fraktur K of p. 130), so \\mathfrak R is right here and in 'de R ;' below.")
add(140, "Remarque (11.3.12): 'ne soit pas réduite à 0'",
    "'ne soit pas réduite à' italic (enlarged crop); the 0 upright", "upright (remark body judged as roman)",
    "italics", None, "high", "ne soit pas réduite à $0$", "\\emph{ne soit pas réduite à} $0$", None)
add(140, "Remarque (11.3.12): '(Bourbaki, Alg. comm., chap. II, § 3, n° 2, cor. 2 de la prop. 5)'",
    "n with a raised letter o", "n$^\\circ$ (degree ring)",
    "symbol", None, "medium", "\\S~3, n$^\\circ$~2", "\\S~3, n\\textsuperscript{o}~2",
    "The edition's usual form is n\\textsuperscript{o} (as the pp. 75-79 and 120-124 findings).")
add(140, "Remarque (11.3.12): 'Cependant, J^k M/J^{k+n} M est isomorphe à A/J^n quels que soient k et n positifs'",
    "words 'est isomorphe à' in the running text, the two quotients inline (enlarged crop)",
    "displayed \\[ \\mathfrak J^kM/\\mathfrak J^{k+n}M\\simeq A/\\mathfrak J^n \\]: the words 'est isomorphe à' replaced by \\simeq",
    "word", None, "high",
    "Cependant,\n\\[\n\\mathfrak J^kM/\\mathfrak J^{k+n}M\\simeq A/\\mathfrak J^n\n\\]\nquels",
    "Cependant, $\\mathfrak J^kM/\\mathfrak J^{k+n}M$ est isomorphe à $A/\\mathfrak J^n$\nquels",
    "Restores the printed words and the inline setting.")
add(140, "Remarque (11.3.12): 'donc M vérifie bien les conditions c) et d) de (0_III, 10.2.1)'",
    "'c)' and 'd)' italic (enlarged crops)", "plain c), d)",
    "italics", None, "high", "conditions c)\net d) de", "conditions \\emph{c)}\net \\emph{d)} de", None)
add(140, "Proposition (11.3.13)(i): 'Si X est réduit (resp. normal) au point x'",
    "'(resp.' and ')' roman, 'normal' italic (enlarged crop)", "(resp. normal) all italic in the proposition environment",
    "convention", 6, "high", "Si $X$ est réduit (resp. normal) au point $x$",
    "Si $X$ est réduit \\textup{(resp. \\emph{normal})} au point $x$",
    "Inside \\textup, \\emph gives the printed italic 'normal'.")
add(140, "Proposition (11.3.13)(i): 'alors Y est réduit (resp. normal) au point y'",
    "'(resp.' and ')' roman, 'normal' italic", "all italic",
    "convention", 6, "high", "est réduit\n(resp. normal) au point $y$.",
    "est réduit\n\\textup{(resp. \\emph{normal})} au point $y$.", None)
add(140, "Proposition (11.3.13)(ii): 'si Y est réduit (resp. normal) au point y'",
    "'(resp.' and ')' roman, 'normal' italic", "all italic",
    "convention", 6, "high", "$Y$ est réduit (resp. normal) au point $y$ et",
    "$Y$ est réduit \\textup{(resp. \\emph{normal})} au point $y$ et", None)
add(140, "Proposition (11.3.13)(ii): 'si le morphisme f est réduit (resp. normal) au point x'",
    "'(resp.' and ')' roman, 'normal' italic (enlarged crop)", "all italic",
    "convention", 6, "high", "le morphisme $f$\nest réduit (resp. normal) au point",
    "le morphisme $f$\nest réduit \\textup{(resp. \\emph{normal})} au point", None)
add(140, "Proposition (11.3.13)(ii): 'au point x (6.8.1), X est'",
    "the reference (6.8.1) upright inside the italic statement (enlarged crop)", "(6.8.1) italic in the proposition environment",
    "convention", 6, "high", "(6.8.1),", "\\textup{(6.8.1)},", None)
add(140, "Proposition (11.3.13)(ii): 'X est réduit (resp. normal) au point x'",
    "'(resp.' and ')' roman, 'normal' italic", "all italic",
    "convention", 6, "high", "$X$ est réduit (resp. normal)\nau point",
    "$X$ est réduit \\textup{(resp. \\emph{normal})}\nau point", None)
add(140, "proof of (11.3.13): 'On peut alors (8.9.1) écrire B = B_0⊗_{A_0} A, où A_0 est une sous-Z-algèbre'",
    "the formula is in the running text", "displayed with \\[ ... \\] (comma inside the display)",
    "formula", None, "high", "écrire\n\\[\nB=B_0\\otimes_{A_0}A,\n\\]\noù", "écrire $B=B_0\\otimes_{A_0}A$,\noù",
    "Display vs inline; no connecting word lost.")
add(140, "proof of (11.3.13): 'et B_0 une A-algèbre de type fini'",
    "'B_0 une A-algèbre de type fini': plain A, no subscript 0 (enlarged crop)",
    "'$B_0$ une $A_0$-algèbre': the TeX silently corrects the printed reading",
    "misprint_in_print", None, "high", "$B_0$ une\n$A_0$-algèbre de type fini.", "$B_0$ une\n$A$-algèbre de type fini.",
    "Misprint A for A_0: B = B_0⊗_{A_0} A and X_α = Spec(B_0⊗_{A_0} A'_α) need B_0 to be an A_0-algebra. The diplomatic TeX must keep the printed A; the corrected edition keeps A_0.",
    corrected="$A_0$-algèbre")
add(140, "proof of (11.3.13), 1°: 'que A'_α est réduit (puisqu'il en est ainsi de C_α) on déduit de (3.3.5)'",
    "no comma after the parenthesis (enlarged crop; the line ends with ')' and the next begins 'on déduit')",
    "'de $C_\\alpha$), on déduit': comma added",
    "punctuation", None, "high", "de $C_\\alpha$), on déduit", "de $C_\\alpha$) on déduit", None)
add(140, "end of page_140.tex / top of p. 141: 'f'_α soit normal au point x'_α ((6.7.8) et (11.2.6)); | comme X'_α et Y'_α sont noethériens'",
    "p. 141 begins 'comme X'_α et Y'_α sont noethériens' flush left: the sentence continues",
    "blank line after 'et (11.2.6))~;', before \\oldpage[IV-3]{141}: paragraph break mid-sentence",
    "marker", None, "high", "et (11.2.6))~;\n\n", "et (11.2.6))~;\n",
    "Apply together with the page-141 entry (blank line after the marker); the marker is in the right place.")

# ---------------- page 141 ----------------
add(141, "top of p. 141: 'comme X'_α et Y'_α sont noethériens'",
    "continuation of the sentence of p. 140, flush left", "blank line after \\oldpage[IV-3]{141}",
    "marker", None, "high", "\\oldpage[IV-3]{141}\n\ncomme", "\\oldpage[IV-3]{141}\ncomme",
    "With the page-140 entry (blank line before the marker).")
add(141, "proof of (11.3.13): 'appliqué aux préschémas Spec(O_{X_0,x_0}⊗_{A_0} A''_α), que X est normal au point x'",
    "the formula is in the running text", "displayed with \\[ ... \\]",
    "formula", None, "high",
    "aux préschémas\n\\[\n\\operatorname{Spec}(\\mathcal O_{X_0,x_0}\\otimes_{A_0}A''_\\alpha),\n\\]\nque $X$",
    "aux préschémas\n$\\operatorname{Spec}(\\mathcal O_{X_0,x_0}\\otimes_{A_0}A''_\\alpha)$,\nque $X$",
    "Display vs inline; no connecting word lost.")
add(141, "Corollaire (11.3.14): 'géométriquement unibranche au point y (6.15.1) et'",
    "(6.15.1) upright inside the italic statement", "(6.15.1) italic in the corollary environment",
    "convention", 6, "high", "au point $y$ (6.15.1)", "au point $y$ \\textup{(6.15.1)}", None)
add(141, "Corollaire (11.3.14): 'normal au point x (6.8.1), alors'",
    "(6.8.1) upright inside the italic statement", "(6.8.1) italic",
    "convention", 6, "high", "au point $x$ (6.8.1)", "au point $x$ \\textup{(6.8.1)}", None)
add(141, "Proposition (11.3.15), l. 2: 'M un B-module de présentation finie'",
    "the M is a bold roman M (wrong fount): 637 dark px against 489-522 for the other ten M's of the page (one at a line end 588), same size 43x33 px; hairlines 3-4 px against 2 (side-by-side crop Ms_compare.png)",
    "$M$ (light roman): silent correction",
    "misprint_in_print", None, "medium", "finie, $M$ un\n$B$-module", "finie, $\\mathbf{M}$ un\n$B$-module",
    "Wrong-fount letter (GLOBAL_ISSUES 29), reproduced in the diplomatic text as on 0_IV p. 31. Possibly only a heavier sort; the measurement makes it an outlier on the page.",
    corrected="$M$")
add(141, "Proposition (11.3.15): 'qui est un A-module plat. Alors'",
    "'plat' set roman (emphasis inside the italic statement; enlarged crop)", "plat italic like the rest of the statement",
    "italics", None, "high", "$A$-module plat. Alors il existe", "$A$-module \\emph{plat}. Alors il existe",
    "Inside the italic proposition, \\emph gives the printed upright 'plat'.")
add(141, "Proposition (11.3.15): 'pour 0≤i<n, M_{f_{i+1}}/(Σ_{j=1}^i f_j M_{f_{i+1}}) soit un ...'",
    "the formula is in the running text, normal-size parentheses", "displayed with \\[ ... \\] and \\Big delimiters",
    "formula", None, "high",
    "pour $0\\leq i<n$,\n\\[\nM_{f_{i+1}}\\Big/\\Big(\\sum_{j=1}^{i}f_jM_{f_{i+1}}\\Big)\n\\]\nsoit un",
    "pour $0\\leq i<n$,\n$M_{f_{i+1}}/(\\sum_{j=1}^{i}f_jM_{f_{i+1}})$\nsoit un",
    "Display vs inline; the \\Big sizes dropped with the display.")
add(141, "Proposition (11.3.15): 'soit un (A_{f_{i+1}}/(Σ_{j=1}^i f_j A_{f_{i+1}}))-module libre'",
    "outer parentheses around the whole ring before '-module' (enlarged crop: '(A_{f_{i+1}}/(Σ ...))-module')",
    "$A_{f_{i+1}}\\big/(\\sum ...)$-module: the outer parentheses are missing",
    "formula", None, "high",
    "$A_{f_{i+1}}\\big/(\\sum_{j=1}^{i}f_jA_{f_{i+1}})$-module",
    "$(A_{f_{i+1}}\\big/(\\sum_{j=1}^{i}f_jA_{f_{i+1}}))$-module", None)
add(141, "after (11.3.15): 'puis, par récurrence, Z_{i+1} = D(f_{i+1}) ∩ V(f_1A + ... + f_iA), les Z_i forment'",
    "the formula is in the running text", "displayed with \\[ ... \\]",
    "formula", None, "high",
    "récurrence,\n\\[\nZ_{i+1}=D(f_{i+1})\\cap V(f_1A+\\cdots+f_iA),\n\\]\nles",
    "récurrence, $Z_{i+1}=D(f_{i+1})\\cap V(f_1A+\\cdots+f_iA)$,\nles",
    "Display vs inline. Apply before the next entry (the \\cdots edit), whose old string lies inside this one.")
add(141, "same formula: 'f_1A + ... + f_iA'",
    "baseline dots (enlarged crop)", "\\cdots",
    "symbol", None, "high", "\\cdots", "\\ldots",
    "\\cdots where the print has baseline dots. Apply after the previous entry; '\\cdots' occurs once on the page before and after it.")
add(141, "proof of (11.3.15): 'un B_0-module de type fini M_0, plat sur A_0'",
    "'plat' italic (enlarged crop)", "upright",
    "italics", None, "high", "$M_0$, plat sur", "$M_0$, \\emph{plat} sur", None)
add(141, "proof of (11.3.15): 'puisque M_{f_{i+1}}/(Σ f_j M_{f_{i+1}}) = ((M_0)_{f_{i+1}}/(Σ f_j (M_0)_{f_{i+1}}))⊗_{A_0} A (Bourbaki, ...'",
    "the formula is in the running text, normal-size parentheses", "displayed with \\[ ... \\], \\Big and \\left/\\right delimiters",
    "formula", None, "high",
    "puisque\n\\[\nM_{f_{i+1}}\\Big/\\Big(\\sum_{j=1}^{i}f_jM_{f_{i+1}}\\Big)\n=\\left((M_0)_{f_{i+1}}\\Big/\\Big(\\sum_{j=1}^{i}f_j(M_0)_{f_{i+1}}\\Big)\\right)\n\\otimes_{A_0}A\n\\]\n(Bourbaki",
    "puisque\n$M_{f_{i+1}}/(\\sum_{j=1}^{i}f_jM_{f_{i+1}})\n=((M_0)_{f_{i+1}}/(\\sum_{j=1}^{i}f_j(M_0)_{f_{i+1}}))\n\\otimes_{A_0}A$\n(Bourbaki",
    "Display vs inline; no connecting word lost.")
add(141, "proof of (11.3.15): '(Bourbaki, Alg. comm., chap. II, § 2, n° 7, prop. 18)'",
    "n with a raised letter o", "n$^\\circ$ (degree ring)",
    "symbol", None, "medium", "\\S~2, n$^\\circ$~7", "\\S~2, n\\textsuperscript{o}~7",
    "The edition's usual form is n\\textsuperscript{o}.")
add(141, "proof of (11.3.15): 'et P un C-module plat, alors il résulte de'",
    "'plat' italic (enlarged crop)", "upright",
    "italics", None, "high", "$C$-module plat, alors", "$C$-module \\emph{plat}, alors", None)
add(141, "end of page_141.tex / top of p. 142: 'que pour que P soit un C-module libre, | il faut et il suffit que'",
    "p. 142 begins 'il faut et il suffit que' flush left: the sentence continues",
    "blank line after 'un $C$-module libre,', before \\oldpage[IV-3]{142}: paragraph break mid-sentence",
    "marker", None, "high", "un $C$-module libre,\n\n", "un $C$-module libre,\n",
    "Apply together with the page-142 entry; the marker is in the right place.")

# ---------------- page 142 ----------------
add(142, "top of p. 142: 'il faut et il suffit que P⊗_C(C/N) soit un (C/N)-module libre'",
    "continuation of the sentence of p. 141, flush left", "blank line after \\oldpage[IV-3]{142}",
    "marker", None, "high", "\\oldpage[IV-3]{142}\n\nil faut", "\\oldpage[IV-3]{142}\nil faut",
    "With the page-141 entry (blank line before the marker).")
add(142, "proof of (11.3.15), after the items 1°-3°: 'Comme A est noethérien, la suite croissante (J_i) est stationnaire'",
    "'Comme' begins a new, indented paragraph", "\\end{enumerate} directly followed by the text: no paragraph indent",
    "other", None, "medium", "\\end{enumerate}\nComme $A$", "\\end{enumerate}\n\nComme $A$",
    "Paragraph indent only (GLOBAL_ISSUES 80).")
add(142, "Proposition (11.3.16): 'soit un morphisme de type fini (resp. de présentation finie). Alors'",
    "'(resp.' and ')' roman, 'de présentation finie' italic (enlarged crop)", "all italic in the proposition environment",
    "convention", 6, "high", "fini (resp. de présentation finie). Alors",
    "fini \\textup{(resp. \\emph{de présentation finie})}. Alors", None)
add(142, "Proposition (11.3.16): 'Alors g est un morphisme de type fini (resp. de présentation finie).'",
    "'(resp.' and ')' roman, 'de présentation finie' italic", "all italic",
    "convention", 6, "high", "(resp. de présentation finie).\n\\end{proposition}",
    "\\textup{(resp. \\emph{de présentation finie})}.\n\\end{proposition}", None)
add(142, "end of the proof of (11.3.16): 'et on est donc ramené à prouver le' (followed by 'Corollaire (11.3.17). —')",
    "the line ends with 'ramené à prouver le'; the sentence runs into the heading 'Corollaire (11.3.17)' (enlarged crop)",
    "'ramené à prouver le corollaire suivant.': the words 'corollaire suivant.' are added",
    "extra", None, "high", "ramené à prouver le\ncorollaire suivant.\n", "ramené à prouver le\n",
    "The printed sentence ends with 'le' and continues as the corollary heading.")
add(142, "Corollaire (11.3.17): 'si C est une A-algèbre de type fini (resp. de présentation finie), B est'",
    "'(resp.' and ')' roman, 'de présentation finie' italic (enlarged crop)", "all italic in the corollary environment",
    "convention", 6, "high", "(resp. de présentation finie), $B$ est",
    "\\textup{(resp. \\emph{de présentation finie})}, $B$ est", None)
add(142, "Corollaire (11.3.17): 'B est une A-algèbre de type fini (resp. de présentation finie).'",
    "'(resp.' and ')' roman, 'de présentation finie' italic", "all italic",
    "convention", 6, "high", "(resp. de présentation finie).\n\\end{corollary}",
    "\\textup{(resp. \\emph{de présentation finie})}.\n\\end{corollary}", None)
add(142, "end of page_142.tex / top of p. 143: 'il existe λ tel que l'application C_λ→C | soit bijective'",
    "p. 143 begins 'soit bijective' flush left: the sentence continues",
    "blank line after '$C_\\lambda\\to C$', before \\oldpage[IV-3]{143}: paragraph break mid-sentence",
    "marker", None, "high", "$C_\\lambda\\to C$\n\n", "$C_\\lambda\\to C$\n",
    "Apply together with the page-143 entry; the marker is in the right place.")

# ---------------- page 143 ----------------
add(143, "top of p. 143: 'soit bijective, puisque C est une B-algèbre de type fini'",
    "continuation of the sentence of p. 142, flush left", "blank line after \\oldpage[IV-3]{143}",
    "marker", None, "high", "\\oldpage[IV-3]{143}\n\nsoit bijective", "\\oldpage[IV-3]{143}\nsoit bijective",
    "With the page-142 entry (blank line before the marker).")
J_NOTE = "The print has a plain Fraktur J, no tilde, in all 23 places of this proof (enlarged crops); the TeX writes \\widetilde{\\mathfrak J} throughout."
add(143, "proof of (11.3.17): 'on a B = A[T_1, ..., T_n]/J pour un idéal J'",
    "the formula is in the running text; plain Fraktur J without tilde (enlarged crop)",
    "displayed \\[ B=A[T_1,\\ldots,T_n]/\\widetilde{\\mathfrak J} \\]",
    "formula", None, "high", "on a\n\\[\nB=A[T_1,\\ldots,T_n]/\\widetilde{\\mathfrak J}\n\\]\npour",
    "on a\n$B=A[T_1,\\ldots,T_n]/\\mathfrak J$\npour",
    "Display vs inline and the added tilde. " + J_NOTE)
add(143, "same proof: 'pour un idéal J; soit (J_λ) la famille filtrante'",
    "plain Fraktur J, no tilde (enlarged crop)", "\\widetilde{\\mathfrak J} twice",
    "formula", None, "high", "idéal $\\widetilde{\\mathfrak J}$~; soit\n$(\\widetilde{\\mathfrak J}_\\lambda)$",
    "idéal $\\mathfrak J$~; soit\n$(\\mathfrak J_\\lambda)$", "Tilde added by the TeX.")
add(143, "same proof: 'contenus dans J, de sorte que J = lim J_λ'",
    "plain Fraktur J, no tilde (enlarged crop)", "\\widetilde{\\mathfrak J} three times",
    "formula", None, "high",
    "dans $\\widetilde{\\mathfrak J}$, de sorte\nque $\\widetilde{\\mathfrak J}=\\varinjlim\\widetilde{\\mathfrak J}_\\lambda$",
    "dans $\\mathfrak J$, de sorte\nque $\\mathfrak J=\\varinjlim\\mathfrak J_\\lambda$", "Tilde added by the TeX.")
add(143, "same proof: 'avec B_λ = A[T_1, ..., T_n]/J_λ'",
    "plain Fraktur J, no tilde", "\\widetilde{\\mathfrak J}_\\lambda",
    "formula", None, "high", "/\\widetilde{\\mathfrak J}_\\lambda$. Appliquant", "/\\mathfrak J_\\lambda$. Appliquant",
    "Tilde added by the TeX.")
add(143, "same proof: 'pour λ≥α de sorte que C_λ = ...'",
    "no comma after 'λ≥α' (enlarged crop)", "'$\\lambda\\geq\\alpha$, de sorte que': comma added",
    "punctuation", None, "high", "$\\lambda\\geq\\alpha$, de sorte que", "$\\lambda\\geq\\alpha$ de sorte que", None)
add(143, "same proof: 'de sorte que C_λ = C_α/(C_α⊗_{B_α}(J_λ/J_α)) par platitude'",
    "the formula is in the running text (end of the line), normal-size parentheses, no tilde",
    "displayed with \\[ ... \\], \\big delimiters, \\widetilde{\\mathfrak J} twice",
    "formula", None, "high",
    "\\[\nC_\\lambda=C_\\alpha/\\big(C_\\alpha\\otimes_{B_\\alpha}\n(\\widetilde{\\mathfrak J}_\\lambda/\\widetilde{\\mathfrak J}_\\alpha)\\big)\n\\]\npar platitude",
    "$C_\\lambda=C_\\alpha/(C_\\alpha\\otimes_{B_\\alpha}\n(\\mathfrak J_\\lambda/\\mathfrak J_\\alpha))$\npar platitude",
    "Display vs inline and the added tildes.")
add(143, "same proof: 'et de même C = C_α/(C_α⊗_{B_α}(J/J_α)). Comme par hypothèse'",
    "the formula is in the running text, no tilde", "displayed with \\[ ... \\], \\widetilde{\\mathfrak J} twice",
    "formula", None, "high",
    "et de même\n\\[\nC=C_\\alpha/\\big(C_\\alpha\\otimes_{B_\\alpha}\n(\\widetilde{\\mathfrak J}/\\widetilde{\\mathfrak J}_\\alpha)\\big).\n\\]\nComme",
    "et de même\n$C=C_\\alpha/(C_\\alpha\\otimes_{B_\\alpha}\n(\\mathfrak J/\\mathfrak J_\\alpha))$.\nComme",
    "Display vs inline and the added tildes.")
add(143, "same proof: 'C_α⊗_{B_α}(J/J_α) est un idéal de type fini de C_α (1.4.4)'",
    "no tilde", "\\widetilde{\\mathfrak J} twice",
    "formula", None, "high", "(\\widetilde{\\mathfrak J}/\\widetilde{\\mathfrak J}_\\alpha)$ est un idéal",
    "(\\mathfrak J/\\mathfrak J_\\alpha)$ est un idéal", "Tilde added by the TeX.")
add(143, "same proof: 'et les C_α⊗_{B_α}(J_λ/J_α) s'identifient'",
    "no tilde", "\\widetilde{\\mathfrak J} twice",
    "formula", None, "high", "(\\widetilde{\\mathfrak J}_\\lambda/\\widetilde{\\mathfrak J}_\\alpha)$\ns'identifient",
    "(\\mathfrak J_\\lambda/\\mathfrak J_\\alpha)$\ns'identifient", "Tilde added by the TeX.")
add(143, "same proof: 'dont C_α⊗_{B_α}(J/J_α) est la réunion'",
    "no tilde", "\\widetilde{\\mathfrak J} twice",
    "formula", None, "high", "(\\widetilde{\\mathfrak J}/\\widetilde{\\mathfrak J}_\\alpha)$ est la réunion",
    "(\\mathfrak J/\\mathfrak J_\\alpha)$ est la réunion", "Tilde added by the TeX.")
add(143, "same proof: 'un λ≥α tel que C_α⊗_{B_α}(J/J_α) = C_α⊗_{B_α}(J_λ/J_α), d'où'",
    "the equation is in the running text, no tilde (enlarged crop)", "displayed with \\[ ... \\], \\widetilde{\\mathfrak J} four times",
    "formula", None, "high",
    "tel que\n\\[\nC_\\alpha\\otimes_{B_\\alpha}\n(\\widetilde{\\mathfrak J}/\\widetilde{\\mathfrak J}_\\alpha)\n=C_\\alpha\\otimes_{B_\\alpha}\n(\\widetilde{\\mathfrak J}_\\lambda/\\widetilde{\\mathfrak J}_\\alpha),\n\\]\n",
    "tel que\n$C_\\alpha\\otimes_{B_\\alpha}\n(\\mathfrak J/\\mathfrak J_\\alpha)\n=C_\\alpha\\otimes_{B_\\alpha}\n(\\mathfrak J_\\lambda/\\mathfrak J_\\alpha)$,\n",
    "Display vs inline and the added tildes.")
add(143, "same proof: 'd'où J = J_λ par fidèle platitude'",
    "no tilde (enlarged crop)", "\\widetilde{\\mathfrak J} twice",
    "formula", None, "high", "d'où $\\widetilde{\\mathfrak J}=\\widetilde{\\mathfrak J}_\\lambda$",
    "d'où $\\mathfrak J=\\mathfrak J_\\lambda$", "Tilde added by the TeX. After this entry no \\widetilde is left on p. 143.")
add(143, "heading 11.4", "'11.4. Descente de la platitude par des morphismes quelconques : cas d'un préschéma de base artinien.' with a final full stop",
    "\\subsection{... de base artinien} (no full stop)",
    "punctuation", None, "high", "cas d'un préschéma de base artinien}", "cas d'un préschéma de base artinien.}",
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop).")
add(143, "Lemme (11.4.1.1): 'muni d'une filtration finie (J_n)_{0≤n≤N+1} avec J_0 = A'",
    "no comma before 'avec' (enlarged crop)", "'$(\\mathfrak J_n)_{0\\leq n\\leq N+1}$, avec': comma added",
    "punctuation", None, "high", "_{0\\leq n\\leq N+1}$, avec", "_{0\\leq n\\leq N+1}$ avec", None)
add(143, "end of page_143.tex / top of p. 144: 'puisqu'il n'y a rien à démontrer pour N = 0. | Les conditions sur M entraînent'",
    "p. 144 begins 'Les conditions sur M' flush left (no indent): the paragraph continues; the last line of p. 143 is a full justified line",
    "blank lines around \\oldpage[IV-3]{144}: a paragraph break the print does not have",
    "marker", None, "high", "pour $N=0$.\n\n", "pour $N=0$.\n",
    "Apply together with the page-144 entry; the marker is in the right place.")

# ---------------- page 144 ----------------
add(144, "top of p. 144: 'Les conditions sur M entraînent, en vertu de l'hypothèse de récurrence'",
    "flush left: continuation of the paragraph of p. 143", "blank line after \\oldpage[IV-3]{144}",
    "marker", None, "high", "\\oldpage[IV-3]{144}\n\nLes conditions", "\\oldpage[IV-3]{144}\nLes conditions",
    "With the page-143 entry (blank line before the marker).")
add(144, "proof of (11.4.1.1): 'si N≥1, et (M/J_1M)⊗(J_N/J_{N+1}) = (M/J_NM)⊗(J_N/J_{N+1}) = (M/J_NM)⊗J_N; donc'",
    "the equalities are in the running text, followed by '; donc l'homomorphisme' on the same line",
    "displayed with \\[ ... \\] (the ';' inside the display)",
    "formula", None, "high",
    "et\n\\[\n(M/\\mathfrak J_1M)\\otimes(\\mathfrak J_N/\\mathfrak J_{N+1})\n=(M/\\mathfrak J_NM)\\otimes(\\mathfrak J_N/\\mathfrak J_{N+1})\n=(M/\\mathfrak J_NM)\\otimes\\mathfrak J_N\\,;\n\\]\ndonc",
    "et\n$(M/\\mathfrak J_1M)\\otimes(\\mathfrak J_N/\\mathfrak J_{N+1})\n=(M/\\mathfrak J_NM)\\otimes(\\mathfrak J_N/\\mathfrak J_{N+1})\n=(M/\\mathfrak J_NM)\\otimes\\mathfrak J_N$~;\ndonc",
    "Display vs inline; no connecting word lost.")
add(144, "proof of (11.4.1.1): 'on en conclut bien que M est un A-module plat'",
    "the M is a bold roman M (wrong fount): 679 dark px against 489-568 for the other 34 M's of the page, same size 42x33 px; hairlines 4 px against 2 (side-by-side crop Ms_compare.png)",
    "$M$ (light roman): silent correction",
    "misprint_in_print", None, "medium", "bien que $M$ est", "bien que $\\mathbf{M}$ est",
    "Wrong-fount letter (GLOBAL_ISSUES 29), reproduced in the diplomatic text; plain M in the corrected edition.",
    corrected="$M$")
add(144, "proof of (11.4.1): 'intersection des images réciproques u_λ^{-1}(J^n B_λ) : il est immédiat'",
    "colon (enlarged crop)", "semicolon '~;'",
    "punctuation", None, "high", "(\\mathfrak J^nB_\\lambda)$~; il est", "(\\mathfrak J^nB_\\lambda)$~: il est", None)
add(144, "proof of (11.4.1): display 'gr^0_J(N_λ) = N_λ/JN_λ = (M/JM)⊗_A B_λ = (M/J_1M)⊗_A(B_λ/JB_λ)'",
    "no comma after the display (enlarged crop); the next line is 'car ce dernier produit tensoriel'",
    "comma at the end of the display", "punctuation", None, "high",
    "(B_\\lambda/\\mathfrak JB_\\lambda),\n\\]\ncar", "(B_\\lambda/\\mathfrak JB_\\lambda)\n\\]\ncar", None)
add(144, "proof of (11.4.1): display '(M⊗_A B_λ)/(Im(M⊗_A JB_λ) + Im(J_1M⊗_A B_λ))'",
    "no comma after the display (enlarged crop)", "comma at the end of the display",
    "punctuation", None, "high", "B_\\lambda)\\big),\n\\]\net l'on a", "B_\\lambda)\\big)\n\\]\net l'on a", None)
add(144, "proof of (11.4.1): 'et l'on a Im(J_1M⊗_A B) = Im(M⊗_A J_1B_λ) ⊂ Im(M⊗_A JB_λ)'",
    "'Im(J_1M⊗_A B)': B without the subscript λ (enlarged crop)",
    "'\\operatorname{Im}(\\mathfrak J_1M\\otimes_A B_\\lambda)': the TeX silently corrects the printed reading",
    "misprint_in_print", None, "high",
    "\\operatorname{Im}(\\mathfrak J_1M\\otimes_A B_\\lambda)\n=", "\\operatorname{Im}(\\mathfrak J_1M\\otimes_A B)\n=",
    "Misprint B for B_λ (only B_λ occurs in this proof; cf. the display just above). The diplomatic TeX keeps the printed B; the corrected edition keeps B_λ.",
    corrected="\\operatorname{Im}(\\mathfrak J_1M\\otimes_A B_\\lambda)")
add(144, "proof of (11.4.1): display '(M/J_1M)⊗_A(B_λ/JB_λ) = (M/J_1M)⊗_{A/J_1}(B_λ/JB_λ)'",
    "no comma after the display (enlarged crop); next line 'si bien que finalement on a'",
    "comma at the end of the display", "punctuation", None, "high",
    "(B_\\lambda/\\mathfrak JB_\\lambda),\n\\]\nsi bien", "(B_\\lambda/\\mathfrak JB_\\lambda)\n\\]\nsi bien", None)
add(144, "proof of (11.4.1): last display '1⊗gr(u_λ) : M_0⊗_{A_0} gr(A) → M_0⊗_{A_0} gr_J(B_λ)'",
    "no comma after the display (enlarged crop)", "comma at the end of the display",
    "punctuation", None, "high", "\\operatorname{gr}_{\\mathfrak J}(B_\\lambda),\n\\]", "\\operatorname{gr}_{\\mathfrak J}(B_\\lambda)\n\\]",
    "Independent of the next entry (both orders work).")
add(144, "end of page_144.tex / top of p. 145: display '1⊗gr(u_λ) : ...' then 'et comme M_0 est par hypothèse un A_0-module plat'",
    "p. 145 begins 'et comme M_0 est' flush left: the sentence continues after the display (page_145_s1.png)",
    "blank line after the display, before \\oldpage[IV-3]{145}: paragraph break mid-sentence",
    "marker", None, "high", "\\]\n\n", "\\]\n",
    "Apply together with the page-145 entry (blank line after the marker); the marker is in the right place.")
add(145, "top of p. 145: 'et comme M_0 est par hypothèse un A_0-module plat'",
    "continuation of the sentence of p. 144, flush left (page_145_s1.png)", "blank line after \\oldpage[IV-3]{145}",
    "marker", None, "high", "\\oldpage[IV-3]{145}\n\net comme", "\\oldpage[IV-3]{145}\net comme",
    "OUTSIDE pp. 140-144 (page_145.tex). Apply together with the previous entry. The pp. 145-149 checker may report the same edit; apply once.")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------- verification ----------------
def load(p):
    return (run / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")

texts = {}
bad = 0
for i, f in enumerate(F):
    if not f["fix"]:
        continue
    p = f["page"]
    texts.setdefault(p, load(p))
    n = texts[p].count(f["fix"]["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE in original", p, i, n, repr(f["fix"]["old"][:60]))
# sequential application per page, in list order
cur = {p: load(p) for p in texts}
for i, f in enumerate(F):
    if not f["fix"]:
        continue
    p = f["page"]
    n = cur[p].count(f["fix"]["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE at application", p, i, n, repr(f["fix"]["old"][:60]))
    else:
        cur[p] = cur[p].replace(f["fix"]["old"], f["fix"]["new"])
print("widetilde left on 143:", cur[143].count("\\widetilde"))
from collections import Counter
c = Counter()
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    c[(f["page"], k)] += 1
for p in sorted({f["page"] for f in F}):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("entries", len(F), "problems", bad)
