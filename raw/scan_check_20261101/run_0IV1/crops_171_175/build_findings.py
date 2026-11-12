import json, os
BASE = r"user\Documents\ega_scan_check_20261101\run_0IV1"
OUT = os.path.join(BASE, "findings_171_175.json")
NL = "<NL>"

def s(x):
    return None if x is None else x.replace(NL, "\n")

def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, fixpage=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": s(old), "new": s(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = s(corrected)
    d["note"] = note
    d["_fixpage"] = fixpage or page
    return d

L = []

# ---------------- page 171 ----------------
L.append(F(171, "top of p. 171, Corollaire (21.7.3): 'Par suite, on a l'inégalité'",
  "'Par suite' opens a new indented paragraph of the statement, after display (21.7.3.1) at the foot of p. 170 (indent checked against the margin lines)",
  r"\end{equation} (end of p. 170) followed by \oldpage{171} and 'Par suite' with no blank line: the paragraph continues",
  "other", None, "high",
  r"\oldpage[0\textsubscript{IV-1}]{171}<NL>Par suite", r"\oldpage[0\textsubscript{IV-1}]{171}<NL><NL>Par suite",
  "Paragraph break after a display (GLOBAL_ISSUES 47 pattern); the blank line goes after the marker, inside the p. 171 segment."))
L.append(F(171, "Corollaire (21.7.3), display (21.7.3.2)",
  "rg_L Ω¹_{L/k} — rg_K Ω¹_{K/k} ⩾ deg. tr_K L, with no full stop; the statement goes on below the display with 'l'égalité étant atteinte ...'",
  r"\geqslant\deg.\operatorname{tr}_K L. (full stop after the formula)",
  "punctuation", None, "high",
  r"\operatorname{tr}_K L.", r"\operatorname{tr}_K L",
  "Checked on a crop. See the next finding (lower-case l'égalité)."))
L.append(F(171, "Corollaire (21.7.3), line after (21.7.3.2)",
  "l'égalité étant atteinte si et seulement si ... (lower-case l: the sentence continues after the display)",
  "L'égalité étant atteinte",
  "word", None, "high",
  "L'égalité étant atteinte", "l'égalité étant atteinte",
  ""))
L.append(F(171, "proof of (21.7.3), second display",
  "rg_L Ω¹_{L/K} — rg_L Υ_{L/K/k} (capital K after the slash in Ω¹_{L/K}; crop)",
  r"\operatorname{rg}_L\Omega^1_{L/k}-\operatorname{rg}_L\Upsilon_{L/K/k}",
  "formula", None, "high",
  r"\Omega^1_{L/k}-\operatorname{rg}_L\Upsilon", r"\Omega^1_{L/K}-\operatorname{rg}_L\Upsilon",
  "The printed L/K is also the correct reading: by the exact sequence just above, rg Ω¹_{L/k} − rg Ω¹_{K/k} = rg Ω¹_{L/K} − rg Υ_{L/K/k}."))
L.append(F(171, "paragraph after the proof of (21.7.3): 'tel que [K : k] soit fini et qui est admissible'",
  "soit *fini* (italic; crop)",
  "soit fini et",
  "italics", None, "high",
  "soit fini et", r"soit \emph{fini} et",
  ""))
L.append(F(171, "Corollaire (21.7.4) b): 'formellement non ramifiée (19.10.2).'",
  "the reference (19.10.2) is upright inside the italic statement (crop)",
  "(19.10.2) italic inside the corollary",
  "convention", 6, "high",
  "ramifiée (19.10.2)", r"ramifiée \textup{(19.10.2)}",
  ""))
L.append(F(171, "Corollaire (21.7.4) c): 'formellement étale (19.10.2).'",
  "the reference (19.10.2) is upright inside the italic statement (crop)",
  "(19.10.2) italic inside the corollary",
  "convention", 6, "high",
  "étale (19.10.2)", r"étale \textup{(19.10.2)}",
  ""))
L.append(F(171, "proof of (21.7.4), line 1: 'les conditions b) et d) sont équivalentes'",
  "*b)* and *d)* italic (letter and parenthesis; crop)",
  "b) and d) upright",
  "italics", None, "high",
  "les conditions b) et<NL>d) sont", r"les conditions \emph{b)} et<NL>\emph{d)} sont",
  "Condition letters in this proof are all italic in the print (this and the next three findings)."))
L.append(F(171, "proof of (21.7.4), line 2: 'et que a) entraîne'",
  "*a)* italic (crop)",
  "a) upright",
  "italics", None, "high",
  "et que a) entraîne", r"et que \emph{a)} entraîne",
  ""))
L.append(F(171, "proof of (21.7.4), line 3: 'la conjonction de a) et b) équivaut à c).'",
  "*a)*, *b)*, *c)* italic (crop)",
  "a), b), c) upright",
  "italics", None, "high",
  "la conjonction de a) et b)<NL>équivaut à c).", r"la conjonction de \emph{a)} et \emph{b)}<NL>équivaut à \emph{c)}.",
  ""))
L.append(F(171, "proof of (21.7.4), line 3: 'Tout revient à voir que d) entraîne a).'",
  "*d)* and *a)* italic (crop)",
  "d), a) upright",
  "italics", None, "high",
  "voir que d) entraîne a).", r"voir que \emph{d)} entraîne \emph{a)}.",
  ""))
L.append(F(171, "proof of (21.7.4), line 5: 'que K est algébrique (donc finie) sur k'",
  "(donc finie) (crop)",
  "(donc fini)",
  "word", None, "high",
  "(donc fini)", "(donc finie)",
  "Not a misprint: finie agrees with 'extension'."))
L.append(F(171, "Remarque (21.7.5), line 1: '(0_III, 11.10.2)'",
  "bold 0 in (0_III, 11.10.2) (crop)",
  r"(0$_{\rm III}$, 11.10.2)",
  "convention", 2, "high",
  r"(0$_{\rm III}$", r"(\textbf{0}$_{\rm III}$",
  ""))
L.append(F(171, "Remarque (21.7.5), line 1: '(0_III, 11.10.2) le premier membre'",
  "no comma after (0_III, 11.10.2) (crop)",
  "11.10.2), le premier",
  "punctuation", None, "high",
  "11.10.2), le premier", "11.10.2) le premier",
  ""))
L.append(F(171, "Remarque (21.7.5): 'théorème de Riemann-Roch'",
  "Riemann-Roch with a hyphen, the same short dash as in Euler-Poincaré (crop)",
  "Riemann--Roch (en dash)",
  "punctuation", None, "high",
  "Riemann--Roch", "Riemann-Roch",
  "The only Riemann--Roch in ega0-21; the other EGA files write Riemann-Roch."))
L.append(F(171, "page break inside Lemme (21.8.1): '(a_i)_{1<=i<=n} | une famille finie de vecteurs de V'",
  "printed p. 171 ends with '..., (a_i)_{1<=i<=n}'; p. 172 begins 'une famille finie de vecteurs de V; si la famille (a_i) est libre sur k, ...' (the rest of the lemma)",
  r"\oldpage[0\textsubscript{IV-1}]{172} stands after \end{lemma}, before \begin{proof}: the last two lines of the lemma fall in the p. 171 segment",
  "marker", None, "high",
  r"$(a_i)_{1\leqslant i\leqslant n}$ une famille finie",
  r"$(a_i)_{1\leqslant i\leqslant n}$<NL>\oldpage[0\textsubscript{IV-1}]{172}<NL>une famille finie",
  "Move, part 1 of 2: insert the marker here first; the p. 172 marker finding then removes the old one before \\begin{proof}. Apply both or neither, in this order."))

# ---------------- page 172 ----------------
L.append(F(172, "top of the TeX segment: old place of the p. 172 marker",
  "p. 172 begins with 'une famille finie de vecteurs de V' (end of Lemme (21.8.1)), then the proof 'Soit r le rang ...'",
  r"\oldpage[0\textsubscript{IV-1}]{172} before \begin{proof}",
  "marker", None, "high",
  r"\oldpage[0\textsubscript{IV-1}]{172}<NL>\begin{proof}", r"\begin{proof}",
  "Move, part 2 of 2: remove the old marker after the p. 171 marker finding has inserted the new one. Apply both or neither."))
L.append(F(172, "proof of (21.8.1), line 1: 'le rang de la famille (a_i)_{1<=i<=n} sur K'",
  "*sur* italic (crop)",
  "sur $K$ upright",
  "italics", None, "high",
  "sur $K$, et<NL>raisonnons", r"\emph{sur} $K$, et<NL>raisonnons",
  ""))
L.append(F(172, "proof of (21.8.1), line 7: 'la famille (a_i)_{1<=i<=r+1} est libre sur k_β'",
  "*libre sur* italic (crop)",
  "libre sur upright",
  "italics", None, "high",
  r"est libre sur $k_\beta$~; en effet", r"est \emph{libre sur} $k_\beta$~; en effet",
  ""))
L.append(F(172, "Lemme (21.8.2): the paragraph 'En effet, dire que la famille (x_i) est p-libre ...'",
  "the statement ends with '... soit p-libre sur k_α.'; 'En effet, dire que ...' is a new roman paragraph (the proof)",
  r"the paragraph stands inside \begin{lemma}...\end{lemma}, so it is set italic",
  "italics", None, "high",
  r"$p$-libre sur $k_\alpha$.<NL><NL>En effet, dire",
  r"$p$-libre sur $k_\alpha$.<NL>\end{lemma}<NL><NL>\begin{proof}<NL>En effet, dire",
  "Part 1 of 2: close the lemma before the proof paragraph; the next finding turns the old \\end{lemma} into \\end{proof}. Apply both or neither. The only such case in ega0-21."))
L.append(F(172, "end of the proof of (21.8.2): '... et k_0(K^p) de K.'",
  "roman proof paragraph",
  r"\end{lemma} after the proof paragraph",
  "italics", None, "high",
  r"de $K$.<NL>\end{lemma}", r"de $K$.<NL>\end{proof}",
  "Part 2 of 2 of the previous finding. Apply both or neither."))
L.append(F(172, "proof of (21.8.2): 'la famille finie des monômes ∏_{i=0}^n x_i^{m(i)}'",
  "lower limit i = 0 under the product (crop)",
  r"\prod_{i=0}^n x_i^{m(i)} (the printed reading is kept)",
  "misprint_in_print", None, "high",
  None, None,
  "The family is (x_i)_{1<=i<=n}; there is no x_0, so the product runs from i=1. The TeX keeps the printed i=0.",
  corrected=r"\prod_{i=1}^n x_i^{m(i)}"))
L.append(F(172, "Théorème (21.8.3) b): 'telle que Υ_{L/K/k_0} soit un L-espace vectoriel de rang fini'",
  "Υ_{L/K/k_0} (subscript k_0; crop)",
  r"\Upsilon_{L/K/k_\alpha}",
  "formula", None, "high",
  r"$\Upsilon_{L/K/k_\alpha}$ soit un", r"$\Upsilon_{L/K/k_0}$ soit un",
  "k_α is not yet chosen at this point of the statement ('il existe α ∈ I' follows)."))
L.append(F(172, "Théorème (21.8.3) b): 'en vertu de (21.7.2))'",
  "the reference (21.7.2) and the closing parenthesis of '(ce qui a lieu ...)' are upright inside the italic statement (crop)",
  "(21.7.2)) italic inside the theorem",
  "convention", 6, "high",
  "vertu de (21.7.2))", r"vertu de \textup{(21.7.2))}",
  ""))
L.append(F(172, "Théorème (21.8.3) b): '(ce qui a lieu en particulier ...'",
  "the opening parenthesis is upright, the words after it italic (crop)",
  "( italic inside the theorem",
  "convention", 6, "medium",
  "(ce qui a lieu", r"\textup{(}ce qui a lieu",
  "Only the face of the parenthesis differs; it matches the upright closing parenthesis of the previous finding."))

# ---------------- page 173 ----------------
L.append(F(173, "proof of (21.8.3), line 3: 'est par hypothèse de rang fini'",
  "rang *fini* (italic; crop)",
  "fini upright",
  "italics", None, "high",
  "de rang<NL>fini, il revient", r"de rang<NL>\emph{fini}, il revient",
  ""))
L.append(F(173, "proof of (21.8.3), line 4: 'que l'un des N_α est 0'",
  "est 0 (the figure zero; crop)",
  "est nul",
  "word", None, "high",
  "est nul ou", "est $0$ ou",
  ""))
L.append(F(173, "proof of (21.8.3), line 4: 'ou que leur intersection est 0'",
  "*intersection* italic (crop)",
  "intersection upright",
  "italics", None, "high",
  "leur<NL>intersection est", r"leur<NL>\emph{intersection} est",
  ""))
L.append(F(173, "proof of (21.8.3), line 4: 'leur intersection est 0. Mais'",
  "est 0 (the figure zero; crop)",
  "est nulle",
  "word", None, "high",
  "est nulle. Mais", "est $0$. Mais",
  ""))
L.append(F(173, "commutative diagram, bottom right",
  "lim← Ω¹_{K/k_α} ⊗_K L, without parentheses (crop)",
  r"\varprojlim(\Omega^1_{K/k_\alpha}\otimes_KL)",
  "formula", None, "high",
  r"\varprojlim(\Omega^1_{K/k_\alpha}\otimes_KL)", r"\varprojlim\Omega^1_{K/k_\alpha}\otimes_KL",
  ""))
L.append(F(173, "after the diagram: 'il suffit donc de montrer que c) entraîne que l'application canonique'",
  "... de montrer que *c)* entraîne que l'application canonique",
  "... de montrer que l'application canonique ('c) entraîne que' missing)",
  "missing", None, "high",
  "de montrer que l'application canonique", r"de montrer que $c)$ entraîne que l'application canonique",
  ""))
L.append(F(173, "display (21.8.3.2)",
  "lim← with no index under the arrow: lim←(Ω¹_{K/k_α} ⊗_K V) (crop)",
  r"\varprojlim_{\alpha}(\Omega^1_{K/k_\alpha}\otimes_KV)",
  "formula", None, "high",
  r"\varprojlim_{\alpha}(\Omega^1_{K/k_\alpha}\otimes_KV)", r"\varprojlim(\Omega^1_{K/k_\alpha}\otimes_KV)",
  "Index the print lacks (GLOBAL_ISSUES 30 pattern); the lim of (21.8.3.1) and the inline lims on this page do have the α."))
L.append(F(173, "after (21.8.3.2): 'est injective pour tout espace vectoriel V sur K'",
  "*espace vectoriel* italic (crop)",
  "espace vectoriel upright",
  "italics", None, "high",
  "pour tout espace vectoriel $V$ sur", r"pour tout \emph{espace vectoriel} $V$ sur",
  ""))
L.append(F(173, "after (21.8.3.2): 'W⊗_K V = W^n pour tout espace vectoriel sur K'",
  "'pour tout espace vectoriel sur K': no W after 'vectoriel' (crop)",
  "pour tout espace vectoriel $W$ sur $K$ (silent correction)",
  "misprint_in_print", None, "medium",
  "espace vectoriel $W$ sur $K$", "espace vectoriel sur $K$",
  "The printed reading is certain; classing the missing W (the space named in the formula just before) as a misprint is a judgement. If it is not taken as a misprint, the same fix applies as an ordinary 'extra' finding.",
  corrected="pour tout espace vectoriel $W$ sur $K$"))
L.append(F(173, "'pour tout élément z du premier membre de (21.8.3.2) il existe'",
  "no comma after (21.8.3.2) (crop)",
  "(21.8.3.2), il existe",
  "punctuation", None, "high",
  "(21.8.3.2), il existe", "(21.8.3.2) il existe",
  ""))
L.append(F(173, "proof of b') ⇒ a): 'que l'on a rg Υ_{L/K/k_0} ⩽ rg Υ_{L/K} ⩽ 1'",
  "rg Υ_{L/K/k_0} ⩽ rg Υ_{L/K} ⩽ 1 (crop)",
  r"$\operatorname{rg}\Upsilon_{L/K}\leqslant1$ (first term missing)",
  "missing", None, "high",
  r"$\operatorname{rg}\Upsilon_{L/K}\leqslant1$",
  r"$\operatorname{rg}\Upsilon_{L/K/k_0}\leqslant\operatorname{rg}\Upsilon_{L/K}\leqslant1$",
  ""))
L.append(F(173, "proof of b') ⇒ a): 'Si Υ_{L/K/k_0} = 0'",
  "Υ_{L/K/k_0} (crop)",
  r"\Upsilon_{L/K/k_\alpha}=0",
  "formula", None, "high",
  r"$\Upsilon_{L/K/k_\alpha}=0$", r"$\Upsilon_{L/K/k_0}=0$",
  "The printed argument is about Υ_{L/K/k_0} throughout (its basis d_{K/k_0}(a)⊗1, mapped to d_{K/k_α}(a)⊗1); the TeX has k_α in four places (this and three findings below)."))
L.append(F(173, "proof of b') ⇒ a): 'Si Υ_{L/K/k_0}=0 il n'y a rien à démontrer'",
  "no comma before 'il n'y a' (crop)",
  "=0$, il n'y a rien",
  "punctuation", None, "high",
  ", il n'y a rien", " il n'y a rien",
  ""))
L.append(F(173, "proof of b') ⇒ a): 'Sinon, Υ_{L/K/k_0} s'identifie canoniquement à Υ_{L/K}'",
  "Υ_{L/K/k_0} (crop)",
  r"\Upsilon_{L/K/k_\alpha}",
  "formula", None, "high",
  r"Sinon, $\Upsilon_{L/K/k_\alpha}$", r"Sinon, $\Upsilon_{L/K/k_0}$",
  ""))
L.append(F(173, "proof of b') ⇒ a): 'à Υ_{L/K} et si l'on pose a = x^p'",
  "no comma after 'et' (crop)",
  "et, si l'on pose",
  "punctuation", None, "high",
  "et, si l'on pose", "et si l'on pose",
  ""))
L.append(F(173, "proof of b') ⇒ a): 'formée du seul élément d_K a ⊗ 1 (21.4.7)'",
  "d_K a⊗1, no parentheses around a (crop)",
  r"d_K(a)\otimes1",
  "formula", None, "high",
  r"$d_K(a)\otimes1$", r"$d_Ka\otimes1$",
  ""))
L.append(F(173, "proof of b') ⇒ a): 'Υ_{L/K/k_0} a donc une base'",
  "Υ_{L/K/k_0} (crop)",
  r"\Upsilon_{L/K/k_\alpha}",
  "formula", None, "high",
  r"$\Upsilon_{L/K/k_\alpha}$ a donc", r"$\Upsilon_{L/K/k_0}$ a donc",
  ""))
L.append(F(173, "proof of b') ⇒ a): 'formée du seul élément d_{K/k_0}(a)⊗1'",
  "d_{K/k_0}(a)⊗1 (crop)",
  r"d_{K/k_\alpha}(a)\otimes1",
  "formula", None, "high",
  r"$d_{K/k_\alpha}(a)\otimes1$", r"$d_{K/k_0}(a)\otimes1$",
  ""))
L.append(F(173, "proof of a) ⇒ c): 'forment une famille p-libre sur k_α'",
  "*sur* italic (crop)",
  "sur upright",
  "italics", None, "high",
  r"$p$-libre sur $k_\alpha$, et l'existence", r"$p$-libre \emph{sur} $k_\alpha$, et l'existence",
  ""))

# ---------------- page 174 ----------------
L.append(F(174, "Corollaire (21.8.5), end: 'on a ∩_{α∈I} k_α(L^p) = k_0(L^p).'",
  "the formula is in the running text, on the line 'on a ...' (not displayed)",
  "displayed with \\[ ... \\]",
  "other", None, "high",
  r"on a<NL>\[<NL>  \bigcap_{\alpha\in I}k_\alpha(L^p)=k_0(L^p).<NL>\]",
  r"on a $\bigcap_{\alpha\in I}k_\alpha(L^p)=k_0(L^p)$.",
  "Display where the print has the formula inline (GLOBAL_ISSUES 21 pattern); no connecting words lost."))
L.append(F(174, "proof of (21.8.6): 'les x_λ d'indice λ ∈ J—H'",
  "long dash for the set difference J—H (crop)",
  r"\lambda\in J-H",
  "convention", 7, "high",
  r"$\lambda\in J-H$", r"$\lambda\in J\setmin H$",
  "\\setmin is not defined for IV1 yet (FIX_POLICY 2.7: convention 7 waits for the global pass)."))
L.append(F(174, "Remarques (21.8.7) (i): 'si L est une extension de type fini de K'",
  "*de type fini* italic, including 'de' (crop)",
  r"extension de \emph{type fini} ('de' upright)",
  "italics", None, "high",
  r"une extension de<NL>  \emph{type fini} de $K$", r"une extension<NL>  \emph{de type fini} de $K$",
  "Judged as if the remark body were roman (document-wide remark item)."))
L.append(F(174, "Remarques (21.8.7) (i), last line: 'isomorphe à un sous-espace de Υ_{L/L_0/k}'",
  "Υ_{L/L_0/k}: plain k, no subscript 0 (enlarged crop)",
  r"\Upsilon_{L/L_0/k_0} (silent correction)",
  "misprint_in_print", None, "high",
  r"$\Upsilon_{L/L_0/k_0}$", r"$\Upsilon_{L/L_0/k}$",
  "Only k_0 is defined in the remark; the exact sequence of (21.8.5) embeds Υ_{L/K/k_0} in Υ_{L/L_0/k_0}. The diplomatic text restores the printed k.",
  corrected=r"$\Upsilon_{L/L_0/k_0}$"))

# ---------------- page 175 ----------------
L.append(F(175, "Remarques (21.8.7) (ii): 'soit x un élément de K—K^p'",
  "long dash for the set difference K—K^p (crop)",
  "K-K^p",
  "convention", 7, "high",
  "$K-K^p$", r"$K\setmin K^p$",
  "\\setmin is not defined for IV1 yet (FIX_POLICY 2.7: convention 7 waits for the global pass)."))
L.append(F(175, "Remarques (21.8.7) (ii): 'une suite croissante d'extensions finies M_n de K'",
  "'d'extensions finies M_n de K' (no exponent p on K; crop)",
  "d'extensions finies $M_n$ de $K$ (the printed reading is kept)",
  "misprint_in_print", None, "medium",
  None, None,
  "M_n = K^p(a_1x, ..., a_nx) with a_i, x in K, so K^p ⊂ M_n ⊂ K: the M_n are finite extensions of K^p (M_n(x) 'est de degré fini sur K^p', and L = M^{1/p} is the extension of K). Printed reading certain; the error class (dropped exponent or slip) is a judgement.",
  corrected=r"d'extensions finies $M_n$ de $K^p$"))
L.append(F(175, "proof of (21.8.8): 'telle que [k : k_α] soit fini pour tout α'",
  "soit *fini* (italic; crop)",
  "fini upright",
  "italics", None, "high",
  r"soit fini pour tout $\alpha$", r"soit \emph{fini} pour tout $\alpha$",
  ""))
L.append(F(175, "proof of (21.8.8): 'A est un A_α-module libre de type fini'",
  "*libre de type fini* italic (crop)",
  "libre de type fini upright",
  "italics", None, "high",
  "libre de type fini~; tout revient", r"\emph{libre de type fini}~; tout revient",
  ""))
L.append(F(175, "proof of (21.8.8), after display (21.8.8.1): 'Comme ∩_α k_α = k^p, cela va résulter ...'",
  "'Comme' opens a new indented paragraph after the display (indent checked against the margin lines)",
  "\\end{equation} followed directly by 'Comme' (no blank line: the paragraph continues)",
  "other", None, "high",
  r"\end{equation}<NL>Comme", r"\end{equation}<NL><NL>Comme",
  "Paragraph break after a display (GLOBAL_ISSUES 47 pattern)."))
L.append(F(175, "end of the proof of (21.8.8): 'cela va résulter des deux lemmes suivants :'",
  "ends with a colon (crop)",
  "ends with a full stop",
  "punctuation", None, "high",
  "deux lemmes suivants.", "deux lemmes suivants~:",
  ""))
L.append(F(175, "page break inside the proof of (21.8.8.3): '... g ∈ k_γ[[T_1, ..., T_r]] tel | que gf ∈ ...'",
  "p. 175 ends with 'Il suffit de prouver qu'un élément f≠0 du premier membre de (21.8.8.4) appartient au second membre. Soient γ un indice, g∈k_γ[[T_1, ..., T_r]] tel'; p. 176 begins 'que gf∈k_γ[[T_1, ..., T_r]]' (crop of p. 176)",
  r"page_175.tex ends at \begin{proof}; \oldpage[0\textsubscript{IV-1}]{176} stands before 'Il suffit de prouver', so these two lines fall in the p. 176 segment",
  "marker", None, "high",
  r"\oldpage[0\textsubscript{IV-1}]{176}<NL>Il suffit de prouver qu'un élément $f\ne0$ du premier membre de (21.8.8.4)<NL>appartient au second membre. Soient $\gamma$ un indice,<NL>$g\in k_\gamma[[T_1,\ldots,T_r]]$ tel que<NL>",
  r"Il suffit de prouver qu'un élément $f\ne0$ du premier membre de (21.8.8.4)<NL>appartient au second membre. Soient $\gamma$ un indice,<NL>$g\in k_\gamma[[T_1,\ldots,T_r]]$ tel<NL>\oldpage[0\textsubscript{IV-1}]{176}<NL>que<NL>",
  "The 'old' text is in page_176.tex (the p. 176 segment), not in page_175.tex: one edit that moves the marker down three lines. The p. 176 checker may report the same move; apply only one of the two.",
  fixpage=176))

# ---------------- verify and write ----------------
texts = {}
def page_text(p):
    if p not in texts:
        b = open(os.path.join(BASE, "page_%03d.tex" % p), "rb").read().decode("utf-8")
        texts[p] = b.replace("\r\n", "\n")
    return texts[p]

ok = True
for d in L:
    if d["fix"] is None:
        continue
    t = page_text(d["_fixpage"])
    n = t.count(d["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE/NOT FOUND", d["page"], d["_fixpage"], n, repr(d["fix"]["old"]))
# overlapping fixes on the same page: apply sequentially and check each old still occurs once
for p in sorted(set(d["_fixpage"] for d in L)):
    t = page_text(p)
    for d in L:
        if d["fix"] is None or d["_fixpage"] != p:
            continue
        if d["kind"] == "misprint_in_print":
            continue
        n = t.count(d["fix"]["old"])
        if n != 1:
            ok = False
            print("SEQUENTIAL PROBLEM", p, n, repr(d["fix"]["old"]))
        else:
            t = t.replace(d["fix"]["old"], d["fix"]["new"])
    # misprint fixes after the others
    for d in L:
        if d["fix"] is None or d["_fixpage"] != p or d["kind"] != "misprint_in_print":
            continue
        n = t.count(d["fix"]["old"])
        if n != 1:
            ok = False
            print("SEQUENTIAL PROBLEM (misprint)", p, n, repr(d["fix"]["old"]))
        else:
            t = t.replace(d["fix"]["old"], d["fix"]["new"])

out = []
for d in L:
    d = dict(d)
    d.pop("_fixpage")
    out.append(d)
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
    f.write("\n")

from collections import Counter
cnt = Counter()
for d in out:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for p in range(171, 176):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("total", len(out), "ok" if ok else "PROBLEMS")
