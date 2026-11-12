import json, sys
from collections import Counter, OrderedDict

sys.stdout.reconfigure(encoding='utf-8')
RUN = r'user\Documents\ega_scan_check_20261101\run_IV2'
OUT = RUN + r'\findings_065_069.json'

# '¶' stands for a line break in the strings below.
def nl(s):
    return None if s is None else s.replace('¶', '\n')

F = []
def add(page, where, scan, tex, kind, conv, conf, old, new, note='', corrected=None):
    d = OrderedDict()
    d['page'] = page
    d['where'] = where
    d['scan'] = scan
    d['tex'] = tex
    d['kind'] = kind
    d['convention'] = conv
    d['confidence'] = conf
    d['fix'] = None if old is None else {'old': nl(old), 'new': nl(new)}
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    F.append(d)

BK = r'\boldsymbol{k}'
C1 = 'bold italic k(...) printed (residue field)'

# ---------------- page 65 ----------------
add(65, 'top of p. 65: \'désignant le sous-préschéma réduit de X ...\' continues the sentence of p. 64 (proof of (4.5.13.1))',
    'no paragraph break: the first line is flush left and continues the sentence',
    'blank line after \\oldpage[IV-2]{65} (and before it, at the end of page_064.tex): paragraph break',
    'other', None, 'high',
    r'\oldpage[IV-2]{65}¶¶désignant', r'\oldpage[IV-2]{65}¶désignant',
    'Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). Apply together with removing the blank line at the end of page_064.tex (\'$X_0$\\n\\n\' -> \'$X_0$\\n\'), which lies outside pp. 65-69.')
add(65, "proof of (4.5.13.1)(i): '(I, 5.2.2)'", 'bold I', 'plain I', 'convention', 2, 'high',
    '(I, 5.2.2)', r'(\textbf{I}, 5.2.2)')
add(65, 'proof of (4.5.13.1), part (ii)', "'(ii) En considérant un préschéma ayant Y pour espace sous-jacent'",
    "'Pour (ii), en considérant ...' (added 'Pour' and comma)", 'word', None, 'high',
    'Pour (ii), en considérant', '(ii) En considérant',
    "The print starts the paragraph with the label '(ii)'. The opening of this proof on p. 64 reads 'Pour (i), on peut supposer' in the TeX: probably the same rewording (p. 64 segment).")
add(65, "Corollaire (4.5.14): 'tel que k(x) soit'", C1, 'k(x)', 'convention', 1, 'high',
    'que $k(x)$ soit une', r'que $' + BK + r'(x)$ soit une')
add(65, "Corollaire (4.5.14): '(en particulier si x est un point rationnel de X)'",
    "the parenthesis is roman inside the italic statement; only 'point rationnel' is italic (crop)",
    'whole parenthesis italic (corollary environment), no emphasis on point rationnel', 'convention', 6, 'high',
    '(en particulier si $x$ est un point rationnel de¶$X$)',
    r'\textup{(en particulier si $x$ est un \emph{point rationnel} de¶$X$)}',
    "Also restores the printed emphasis on 'point rationnel' (\\emph inside \\textup gives italic).")
add(65, "proof of (4.5.14): 'Y = Spec(k(x))'", C1, 'k(x)', 'convention', 1, 'high',
    r'\operatorname{Spec}(k(x))$', r'\operatorname{Spec}(' + BK + r'(x))$')
add(65, "Proposition (4.5.15): 'dans k(x)'", C1, 'k(x)', 'convention', 1, 'high',
    'dans $k(x)$. On suppose', r'dans $' + BK + r'(x)$. On suppose')
add(65, 'Proposition (4.5.15), label (i)', '(i) upright', '\\item[(i)] italic inside the italic proposition',
    'convention', 6, 'high', r'\item[(i)] $X$ est connexe.', r'\item[\textup{(i)}] $X$ est connexe.',
    'Roman-numeral item labels are upright in the print (GLOBAL_ISSUES item 16).')
add(65, 'Proposition (4.5.15), label (ii)', '(ii) upright', '\\item[(ii)] italic inside the italic proposition',
    'convention', 6, 'high', r"\item[(ii)] $k'$ est", r"\item[\textup{(ii)}] $k'$ est")
add(65, "after (4.5.15): 'si X est localement de type fini sur k.'",
    "'localement de type fini sur k' italic, including 'sur' (crop)", "\\emph{localement de type fini} sur $k$ ('sur' upright)",
    'italics', None, 'high', 'type fini} sur $k$.', 'type fini sur} $k$.')
add(65, "proof of (4.5.15): '(II, 6.1.10)'", 'bold II', 'plain II', 'convention', 2, 'high',
    '(II, 6.1.10)', r'(\textbf{II}, 6.1.10)')
add(65, "proof of (4.5.15): 'Spec(k(x)⊗_k k'')'", C1, 'k(x)', 'convention', 1, 'high',
    r"\operatorname{Spec}(k(x)\otimes_k k'')", r"\operatorname{Spec}(" + BK + r"(x)\otimes_k k'')")
add(65, "proof of (4.5.15): '(I, 3.4.9), c'est-à-dire'", 'bold I', 'plain I', 'convention', 2, 'high',
    "(I, 3.4.9), c'est", r"(\textbf{I}, 3.4.9), c'est")
add(65, "proof of (4.5.15): 'k(x''_α) est une extension primaire'", C1, "k(x''_\\alpha)", 'convention', 1, 'high',
    r"$k(x''_\alpha)$", r"$" + BK + r"(x''_\alpha)$")
add(65, "proof of (4.5.15): 'et de (I, 3.4.9). On peut'", 'bold I', 'plain I', 'convention', 2, 'high',
    '(I, 3.4.9). On peut', r'(\textbf{I}, 3.4.9). On peut')
add(65, 'Corollaire (4.5.16), label (i)', '(i) upright', '\\item[(i)] italic inside the italic corollary',
    'convention', 6, 'high', r'\item[(i)] La famille', r'\item[\textup{(i)}] La famille')
add(65, 'Corollaire (4.5.16), label (ii)', '(ii) upright', '\\item[(ii)] italic inside the italic corollary',
    'convention', 6, 'high', r'\item[(ii)] Pour tout', r'\item[\textup{(ii)}] Pour tout')
add(65, "Corollaire (4.5.16)(ii): 'dans k(x_α)'", C1, 'k(x_\\alpha)', 'convention', 1, 'high',
    r'$k(x_\alpha)$', r'$' + BK + r'(x_\alpha)$')

# ---------------- page 66 ----------------
add(66, "Corollaire (4.5.17): 'dans k(x) soit finie'", C1, 'k(x)', 'convention', 1, 'high',
    'dans $k(x)$ soit finie', r'dans $' + BK + r'(x)$ soit finie')
add(66, "Proposition (4.5.19): 'est contenu dans une seule composante irréductible'",
    "'une seule' roman (emphasis) inside the italic statement (crop)", 'italic like the rest of the statement',
    'convention', 6, 'high', 'dans une seule composante', r'dans \textup{une seule} composante')
add(66, "Proposition (4.5.19): 'de X' qui rencontre Z', alors'",
    "'rencontre' roman (emphasis) inside the italic statement (crop); the second 'qui rencontre Z.' is italic",
    'italic', 'convention', 6, 'high', "qui rencontre $Z'$", r"qui \textup{rencontre} $Z'$")
add(66, "proof of Lemme (4.5.19.1): '(I, 3.4.7)'", 'bold I', 'plain I', 'convention', 2, 'high',
    '(I, 3.4.7)', r'(\textbf{I}, 3.4.7)')
add(66, "proof of (4.5.19): 'on a p_1^{-1}(X'_0)∩φ''^{-1}(s'') = p_2^{-1}(X'_0)∩φ''^{-1}(s'').'",
    'in the running text (same line as \'pour tout s\'\'∈S\'\', on a\')', 'displayed with \\[ ... \\]',
    'other', None, 'high',
    r"on a¶\[¶p_1^{-1}(X'_0)\cap\varphi''^{-1}(s'')¶=p_2^{-1}(X'_0)\cap\varphi''^{-1}(s'').¶\]",
    r"on a¶$p_1^{-1}(X'_0)\cap\varphi''^{-1}(s'')¶=p_2^{-1}(X'_0)\cap\varphi''^{-1}(s'')$.",
    'Layout only (display vs inline); the formula itself matches.')
add(66, "proof of (4.5.19): 'T = Spec(k(s''))'", C1, "k(s'')", 'convention', 1, 'high',
    r"\operatorname{Spec}(k(s''))", r"\operatorname{Spec}(" + BK + r"(s''))")
add(66, 'diagram (4.5.19.2), bottom row', "'S ← S' ⇇ S'' ← T' with no full stop after T (crop)",
    "'T\\ar[l].' prints a full stop after T", 'punctuation', None, 'high',
    r'T\ar[l].', r'T\ar[l]')
add(66, "end of p. 66: display 'w = p∘p_1∘v = p∘p_2∘v.'; p. 67 continues 'Or, il existe un corps K'",
    'p. 67 begins flush left: the paragraph continues after the display',
    'blank line after \\] (before \\oldpage[IV-2]{67}): paragraph break', 'other', None, 'high',
    r'p_2\circ v.¶\]¶¶', r'p_2\circ v.¶\]¶',
    'Spurious paragraph break (GLOBAL_ISSUES item 20). Apply together with the p. 67 top entry (blank line after the marker).')

# ---------------- page 67 ----------------
add(67, "top of p. 67: 'Or, il existe un corps K, ...' continues the paragraph after the display that ends p. 66",
    'flush left, no paragraph indent', 'blank line after \\oldpage[IV-2]{67}', 'other', None, 'high',
    r'\oldpage[IV-2]{67}¶¶Or, il existe', r'\oldpage[IV-2]{67}¶Or, il existe',
    'Apply together with the p. 66 end entry (blank line before the marker).')
add(67, "proof of (4.5.19): 'extension commune de k' et de k(s'')'", C1, "k(s'')", 'convention', 1, 'high',
    "$k(s'')$", r"$" + BK + r"(s'')$")
add(67, "end of p. 67: Proposition (4.5.21) continues on p. 68 with 'En particulier les composantes irréductibles ...'",
    "p. 68 begins flush left: same paragraph of the statement",
    'blank line before \\oldpage[IV-2]{68}: paragraph break inside the statement', 'other', None, 'high',
    'homéomorphisme universel.¶¶', 'homéomorphisme universel.¶',
    'Spurious paragraph break (GLOBAL_ISSUES item 20). Apply together with the p. 68 top entry.')

# ---------------- page 68 ----------------
add(68, "top of p. 68: 'En particulier les composantes irréductibles ...' (end of Proposition (4.5.21))",
    'flush left, continues the statement begun on p. 67', 'blank line after \\oldpage[IV-2]{68}', 'other', None, 'high',
    r'\oldpage[IV-2]{68}¶¶En particulier', r'\oldpage[IV-2]{68}¶En particulier',
    'Apply together with the p. 67 end entry.')
add(68, "Proposition (4.5.21): '(resp. connexes)'", "'(resp.' and ')' upright, 'connexes' italic (crop)",
    'all italic (proposition environment)', 'convention', 6, 'high',
    '(resp. connexes)', r'\textup{(resp.} connexes\textup{)}')
add(68, "Proposition (4.5.21): '(resp. géométriquement connexes)'", "'(resp.' and ')' upright (crop)",
    'all italic (proposition environment)', 'convention', 6, 'high',
    '(resp. géométriquement connexes)', r'\textup{(resp.} géométriquement connexes\textup{)}')
add(68, "heading 4.6", "'4.6. Préschémas algébriques géométriquement réduits.' (final full stop)", 'no full stop',
    'punctuation', None, 'high',
    r'\subsection{Préschémas algébriques géométriquement réduits}',
    r'\subsection{Préschémas algébriques géométriquement réduits.}',
    'None of the 58 \\subsection titles in ega4-2-fr.tex has the printed final full stop (GLOBAL_ISSUES item 43).')
for lab in 'abcde':
    add(68, 'Proposition (4.6.1), label %s)' % lab, '%s) upright (crop)' % lab,
        '\\item[%s)] italic inside the italic proposition' % lab, 'convention', 6, 'high',
        r'\item[%s)]' % lab, r'\item[\textup{%s)}]' % lab)
add(68, "Proposition (4.6.1) e): 'X est réduit,'", "'réduit' (crop)", "'réduite'", 'word', None, 'high',
    '$X$ est réduite, et', '$X$ est réduit, et',
    'X is a préschéma (masculine); transcription error, not a misprint.')
add(68, "Proposition (4.6.1) e): 'k(x_α) est une extension séparable'", C1, 'k(x_\\alpha)', 'convention', 1, 'high',
    r'$k(x_\alpha)$ est une extension', r'$' + BK + r'(x_\alpha)$ est une extension')
add(68, "proof of (4.6.1): 'a) ⇒ b) ⇒ c)'", 'the labels a), b), c) italic (crop)', 'upright', 'italics', None, 'high',
    r'a) $\Rightarrow$ b) $\Rightarrow$ c)', r'\emph{a)} $\Rightarrow$ \emph{b)} $\Rightarrow$ \emph{c)}')
add(68, "proof of (4.6.1): 'que c) implique d).'", 'c), d) italic (crop)', 'upright', 'italics', None, 'high',
    'que c) implique¶d).', r'que \emph{c)} implique¶\emph{d)}.')
add(68, "proof of (4.6.1): 'Montrons que d) implique e).'", 'd), e) italic (crop)', 'upright', 'italics', None, 'high',
    'que d) implique e).', r'que \emph{d)} implique \emph{e)}.')
add(68, "proof of (4.6.1): 'pour prouver que k(x_α) est séparable'", C1, 'k(x_\\alpha)', 'convention', 1, 'high',
    r'prouver que $k(x_\alpha)$ est séparable', r'prouver que $' + BK + r'(x_\alpha)$ est séparable')
add(68, "proof of (4.6.1): 'montrer que k(x_α)⊗_k k''", C1, 'k(x_\\alpha)', 'convention', 1, 'high',
    r"montrer que $k(x_\alpha)\otimes_k k'$", r"montrer que $" + BK + r"(x_\alpha)\otimes_k k'$")
add(68, "proof of (4.6.1): '(I, 5.1.4)'", 'bold I', 'plain I', 'convention', 2, 'high',
    '(I, 5.1.4)', r'(\textbf{I}, 5.1.4)')
add(68, "proof of (4.6.1): 'k(x_α)⊗_k k' est un anneau de fractions'", C1, 'k(x_\\alpha)', 'convention', 1, 'high',
    r"$k(x_\alpha)\otimes_k k'$ est un anneau de", r"$" + BK + r"(x_\alpha)\otimes_k k'$ est un anneau de")
add(68, "proof of (4.6.1): '(0_I, 1.2.8)'", 'bold 0 with subscript I', '$(0_{\\mathrm I},1.2.8)$ (plain 0)',
    'convention', 2, 'high', r'(0_{\mathrm I},1.2.8)', r'(\mathbf{0}_{\mathrm I},1.2.8)')
add(68, "proof of (4.6.1): 'pour prouver que e) entraîne a),'", 'e), a) italic', 'upright', 'italics', None, 'high',
    'que e) entraîne a),', r'que \emph{e)} entraîne \emph{a)},')
add(68, "proof of (4.6.1): 'Les k(x_α) sont les corps'", C1, 'k(x_\\alpha)', 'convention', 1, 'high',
    r'Les $k(x_\alpha)$ sont', r'Les $' + BK + r'(x_\alpha)$ sont')
add(68, "proof of (4.6.1): 'donc dans ∏_α k(x_α);'", C1, 'k(x_\\alpha)', 'convention', 1, 'high',
    r'$\prod_\alpha k(x_\alpha)$~;', r'$\prod_\alpha ' + BK + r'(x_\alpha)$~;')
add(68, "proof of (4.6.1): 'une sous-algèbre de (∏_α k(x_α))⊗_k(∏_β L_β), et ce produit'",
    'in the running text, with a bold italic k(x_α)', 'displayed with \\[ ... \\]; plain k(x_\\alpha)',
    'other', None, 'high',
    r'\[¶\left(\prod_\alpha k(x_\alpha)\right)\otimes_k¶\left(\prod_\beta L_\beta\right),¶\]',
    r'$\left(\prod_\alpha ' + BK + r'(x_\alpha)\right)\otimes_k¶\left(\prod_\beta L_\beta\right)$,',
    'Display vs inline; the same edit sets the bold k of this formula (convention 1, no separate finding).')
add(68, "proof of (4.6.1): 'une sous-algèbre de ∏_{α,β}(k(x_α)⊗_k L_β) (Bourbaki, ...'",
    'in the running text, with a bold italic k(x_α)', 'displayed with \\[ ... \\]; plain k(x_\\alpha)',
    'other', None, 'high',
    r'\[¶\prod_{\alpha,\beta}\bigl(k(x_\alpha)\otimes_k L_\beta\bigr)¶\]',
    r'$\prod_{\alpha,\beta}\bigl(' + BK + r'(x_\alpha)\otimes_k L_\beta\bigr)$',
    'Display vs inline; the same edit sets the bold k of this formula (convention 1, no separate finding).')
add(68, "proof of (4.6.1): 'les k(x_α)⊗_k L_β sont réduits'", C1, 'k(x_\\alpha)', 'convention', 1, 'high',
    r'$k(x_\alpha)\otimes_k L_\beta$ sont', r'$' + BK + r'(x_\alpha)\otimes_k L_\beta$ sont')
add(68, "Définition (4.6.2): 'les conditions équivalentes a) à e) de la proposition (4.6.1) sont remplies'",
    "a), e) and (4.6.1) upright, 'à' and 'de la proposition' italic (crop)", 'all italic (definition environment)',
    'convention', 6, 'high',
    'a) à e) de la proposition (4.6.1) sont', r'\textup{a)} à \textup{e)} de la proposition \textup{(4.6.1)} sont')
add(68, "Définition (4.6.2): '... ou universellement réduit) sur k.'", "'sur' roman like the defined terms (crop)",
    "'sur' italic (outside the \\emph)", 'convention', 6, 'high',
    'réduit}) sur $k$', r'réduit}) \textup{sur} $k$')
add(68, "Définition (4.6.2): 'est géométriquement intègre sur k si,'", "'géométriquement intègre sur' roman; 'k si,' italic (crop)",
    "\\emph{géométriquement intègre} sur $k$ ('sur' italic)", 'convention', 6, 'high',
    r'\emph{géométriquement intègre} sur $k$', r'\emph{géométriquement intègre sur} $k$')
add(68, "Définition (4.6.2): '(en vertu de (4.6.1))'", "the reference (4.6.1) upright, 'en vertu de' italic (crop)",
    'all italic', 'convention', 6, 'high',
    '(en vertu de (4.6.1))', r'(en vertu de \textup{(4.6.1)})')
add(68, "end of p. 68: '... Bourbaki, Alg., chap. VIII,' continues on p. 69 '§ 7, n° 5, déf. 1, ...'",
    'p. 69 begins flush left inside the sentence', 'blank line before \\oldpage[IV-2]{69}', 'other', None, 'high',
    'chap.~VIII,¶¶', 'chap.~VIII,¶',
    'Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). Apply together with the p. 69 top entry.')

# ---------------- page 69 ----------------
add(69, "top of p. 69: '§ 7, n° 5, déf. 1, lorsque A est de rang fini ...'", 'flush left, continues the sentence of p. 68',
    'blank line after \\oldpage[IV-2]{69}', 'other', None, 'high',
    r'\oldpage[IV-2]{69}¶¶\S~7', r'\oldpage[IV-2]{69}¶\S~7',
    'Apply together with the p. 68 end entry.')
add(69, "Corollaire (4.6.3): '(resp. géométriquement intègre) sur k'", "'(resp.' and ')' upright", 'all italic',
    'convention', 6, 'high',
    'réduit¶(resp. géométriquement intègre)', r'réduit¶\textup{(resp.} géométriquement intègre\textup{)}')
add(69, "Corollaire (4.6.3): '(resp. séparable et primaire)'", "'(resp.' and ')' upright", 'all italic',
    'convention', 6, 'high',
    '(resp.¶séparable et primaire)', r'\textup{(resp.}¶séparable et primaire\textup{)}')
add(69, "proof of (4.6.4): 'l'équivalence de a) et e) dans (4.6.1)'", 'a), e) italic', 'upright', 'italics', None, 'high',
    'de a) et e) dans', r'de \emph{a)} et \emph{e)} dans')
add(69, 'Proposition (4.6.5), label (i)', '(i) upright', '\\item[(i)] italic inside the italic proposition',
    'convention', 6, 'high', r'\item[(i)]', r'\item[\textup{(i)}]')
add(69, "Proposition (4.6.5)(i): 'géométriquement réduit (resp. géométriquement intègre) sur k, il faut'",
    "'(resp.' and ')' upright", 'all italic', 'convention', 6, 'high',
    'réduit (resp. géométriquement intègre) sur $k$', r'réduit \textup{(resp.} géométriquement intègre\textup{)} sur $k$')
add(69, "Proposition (4.6.5)(i): '(resp. géométriquement intègre) sur K.'", "'(resp.' and ')' upright", 'all italic',
    'convention', 6, 'high',
    '(resp. géométriquement¶intègre)', r'\textup{(resp.} géométriquement¶intègre\textup{)}')
add(69, 'Proposition (4.6.5), label (ii)', '(ii) upright', '\\item[(ii)] italic inside the italic proposition',
    'convention', 6, 'high', r'\item[(ii)]', r'\item[\textup{(ii)}]')
add(69, "Proposition (4.6.5)(ii): '(resp. géométriquement intègres)'", "'(resp.' and ')' upright", 'all italic',
    'convention', 6, 'high',
    '(resp. géométriquement intègres)', r'\textup{(resp.} géométriquement intègres\textup{)}')
add(69, "proof of (4.6.5): 'la partie de l'assertion de (ii) concernant la séparabilité'", "'de l'assertion de (ii)' (crop)",
    "'de l'assertion (ii)' (word 'de' missing)", 'missing', None, 'high',
    "l'assertion (ii) concernant", "l'assertion de (ii) concernant")
add(69, "proof of (4.6.5): 'on a (X×_k Y)⊗_k Ω = X×_k(Y⊗_k Ω); comme'", 'in the running text',
    'displayed with \\[ ... \\]', 'other', None, 'high',
    r'on a¶\[¶(X\times_k Y)\otimes_k\Omega=X\times_k(Y\otimes_k\Omega)~;¶\]',
    r'on a¶$(X\times_k Y)\otimes_k\Omega=X\times_k(Y\otimes_k\Omega)$~;',
    'Layout only (display vs inline); the formula itself matches.')
add(69, "proof of (4.6.5): '(4.6.1, a))'", "'a)' italic", 'upright', 'italics', None, 'high',
    '(4.6.1, a))', r'(4.6.1, \emph{a)})')
add(69, "proof of (4.6.6): 's'identifie à (U_i⊗_k k_i)_red⊗_{k_i} k' en vertu de'", 'in the running text',
    'displayed with \\[ ... \\]', 'other', None, 'high',
    r"s'identifie à¶\[¶(U_i\otimes_k k_i)_{\mathrm{red}}\otimes_{k_i}k'¶\]",
    r"s'identifie à¶$(U_i\otimes_k k_i)_{\mathrm{red}}\otimes_{k_i}k'$",
    'Layout only (display vs inline); the formula itself matches.')
add(69, "proof of (4.6.6): 'en vertu de (I, 5.1.8), donc'", 'bold I', 'plain I', 'convention', 2, 'high',
    'de (I, 5.1.8), donc', r'de (\textbf{I}, 5.1.8), donc')
add(69, "proof of (4.6.6): 'de la forme y_i = Σ_j x_ij⊗ξ_ij où x_ij∈A, ξ_ij∈Ω.'",
    "in the running text, joined by the word 'où'", "displayed; ',\\qquad' in place of 'où'", 'missing', None, 'high',
    r'de la forme¶\[¶y_i=\sum_j x_{ij}\otimes\xi_{ij},¶\qquad x_{ij}\in A,\quad \xi_{ij}\in\Omega.¶\]',
    r'de la forme¶$y_i=\sum_j x_{ij}\otimes\xi_{ij}$ où $x_{ij}\in A$, $\xi_{ij}\in\Omega$.',
    "Restores the printed connecting word 'où' and the inline setting.")
add(69, "proof of (4.6.6): 'Comme (A⊗_k Ω)/𝔑' = ((A⊗_k K)/𝔑)⊗_K Ω, on voit que'", 'in the running text',
    'displayed with \\[ ... \\]', 'other', None, 'high',
    r"Comme¶\[¶(A\otimes_k\Omega)/\mathfrak N'¶=\bigl((A\otimes_k K)/\mathfrak N\bigr)\otimes_K\Omega,¶\]",
    r"Comme¶$(A\otimes_k\Omega)/\mathfrak N'¶=\bigl((A\otimes_k K)/\mathfrak N\bigr)\otimes_K\Omega$,",
    'Layout only (display vs inline); the formula itself matches (Fraktur N checked on a crop).')
add(69, "proof of (4.6.6): 'on voit par (I, 5.1.8) que'", 'bold I', 'plain I', 'convention', 2, 'high',
    'par (I, 5.1.8) que', r'par (\textbf{I}, 5.1.8) que')
add(69, "end of p. 69: '... prop. 14). En vertu' continues on p. 70 'de (I, 5.1.8), ...'",
    'mid-sentence page break', 'blank line before \\oldpage[IV-2]{70}', 'other', None, 'high',
    'prop.~14). En vertu¶¶', 'prop.~14). En vertu¶',
    "Spurious paragraph break (GLOBAL_ISSUES item 20). Apply together with removing the blank line after \\oldpage[IV-2]{70} in page_070.tex ('\\oldpage[IV-2]{70}\\n\\nde (I, 5.1.8)'), outside pp. 65-69.")

# ---------------- checks ----------------
ok = True
pages = {}
for p in range(65, 70):
    raw = open(RUN + r'\page_%03d.tex' % p, 'rb').read().decode('utf-8')
    pages[p] = raw.replace('\r\n', '\n')

for d in F:
    if d['fix'] is None:
        continue
    n = pages[d['page']].count(d['fix']['old'])
    if n != 1:
        ok = False
        print('NOT UNIQUE (%d) p.%d: %r' % (n, d['page'], d['fix']['old']))

# simulate sequential application per page
for p in range(65, 70):
    t = pages[p]
    for d in F:
        if d['page'] != p or d['fix'] is None:
            continue
        o, nw = d['fix']['old'], d['fix']['new']
        c = t.count(o)
        if c != 1:
            ok = False
            print('SEQUENTIAL FAIL p.%d (count %d): %r' % (p, c, o))
            continue
        t = t.replace(o, nw)
    pages[p] = t

cnt = Counter()
for d in F:
    k = 'misprint' if d['kind'] == 'misprint_in_print' else ('convention' if d['kind'] == 'convention' else 'normal')
    cnt[(d['page'], k)] += 1
for p in range(65, 70):
    print('p. %d: %d normal / %d convention / %d misprint' % (p, cnt[(p, 'normal')], cnt[(p, 'convention')], cnt[(p, 'misprint')]))
print('total', len(F), 'ok' if ok else 'PROBLEMS')

if ok:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
    print('written', OUT)
    # dump the fully patched pages for inspection
    for p in range(65, 70):
        with open(RUN + r'\crops_065_069\patched_%03d.tex' % p, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(pages[p])
