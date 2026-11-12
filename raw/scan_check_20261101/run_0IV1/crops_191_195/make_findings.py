import json
import pathlib

RUN = pathlib.Path(r'user/Documents/ega_scan_check_20261101/run_0IV1')
OUT = RUN / 'findings_191_195.json'
NL = '\u00b6'  # placeholder for a line break in old/new strings


def F(page, where, scan, tex, kind, conv, conf, old, new, note='', corrected=None):
    fix = None
    if old is not None:
        fix = {'old': old.replace(NL, '\n'), 'new': new.replace(NL, '\n')}
    d = {'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind, 'convention': conv,
         'confidence': conf, 'fix': fix}
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    return d


L = []
# ---------------------------------------------------------------- page 191
L.append(F(191, "Lemme (22.3.1), parenthesis: 'cf. Bourbaki, Alg. comm., chap. IV, § 2, n° 5, cor. 3 de la prop. 9)'",
           "'cf. Bourbaki, … prop. 9).' roman inside the italic statement, only 'Alg. comm.' italic (crop)",
           "italic (lemma environment), 'Alg. comm.' upright through \\emph", 'convention', 6, 'high',
           r"cf. Bourbaki,¶\emph{Alg. comm.}, chap.~IV, §~2, n\textsuperscript{o}~5, cor.~3 de la¶prop.~9)",
           r"\textup{cf. Bourbaki,¶\emph{Alg. comm.}, chap.~IV, §~2, n\textsuperscript{o}~5, cor.~3 de la¶prop.~9)}",
           "The opening parenthesis and '(qui est donc … noethérien,' are italic in the print."))
L.append(F(191, "Lemme (22.3.1): 'lorsqu'on munit A_0, A et Â des topologies discrètes'",
           "'discrètes' roman inside the italic statement (crop)", "'discrètes' italic", 'convention', 6, 'high',
           r"des topologies discrètes,", r"des topologies \textup{discrètes},"))
L.append(F(191, "Lemme (22.3.1), last words: '(19.9.1)'", "reference upright inside the italic statement",
           "italic", 'convention', 6, 'high', r"à $A_0$ (19.9.1).", r"à $A_0$ \textup{(19.9.1)}."))
L.append(F(191, "Proposition (22.3.2), label (i)", "(i) upright (crop)", "\\item[(i)] italic in the statement",
           'convention', 6, 'high', r"\item[(i)] $p=0$.", r"\item[\textup{(i)}] $p=0$."))
L.append(F(191, "Proposition (22.3.2), label (ii)", "(ii) upright (crop)", "\\item[(ii)] italic in the statement",
           'convention', 6, 'high', r"\item[(ii)] $p>0$", r"\item[\textup{(ii)}] $p>0$"))
L.append(F(191, "Proposition (22.3.2) (ii): 'on ait ⋂_α K_α(K^p) = K^p.'",
           "formula in the running text, at the end of the line 'et que, si K_α désigne … on ait'",
           "displayed with \\[ \\]", 'other', None, 'high',
           r"on ait¶  \[¶    \bigcap_\alpha K_\alpha(K^p)=K^p.¶  \]",
           r"on ait¶  $\bigcap_\alpha K_\alpha(K^p)=K^p$.",
           "Formula displayed where the print has it inline; no connecting words lost. The print sets α under ⋂ also in the text line."))
L.append(F(191, "Proposition (22.3.2): paragraph 'Soient alors B une A-algèbre finie intègre …' after (ii)",
           "'Soient alors' begins an indented paragraph (crop)", "no blank line after \\end{enumerate}: flush-left continuation",
           'other', None, 'medium', r"\end{enumerate}¶Soient alors", r"\end{enumerate}¶¶Soient alors",
           "Paragraph break as printed (indented line), as for text after displays. Does not overlap the display finding above."))
L.append(F(191, "Proposition (22.3.2), last words: '(19.6.5)'", "reference upright inside the italic statement",
           "italic", 'convention', 6, 'high', r"sur $L$ (19.6.5).", r"sur $L$ \textup{(19.6.5)}."))
L.append(F(191, "proof of (22.3.2), case I): 'B̂ = Â⊗_A B (Bourbaki, Alg. comm., chap. IV, § 2, n° 5, cor. de la prop. 9 et chap. III, § 3, n° 4, th. 1)'",
           "'cor. de la prop. 9' without a corollary number (crop)", "'cor. de la prop.~9' (printed reading kept)",
           'misprint_in_print', None, 'low', None, None,
           "TeX keeps the printed reading. The same two Bourbaki results are cited for the same kind of identity (completion of a finite algebra = tensor product) in (22.3.1) and its proof as 'cor. 3 de la prop. 9'; a corollary number seems to have dropped out here. Low: the reading is not checked against Bourbaki.",
           corrected=r"cor.~3 de la prop.~9"))
L.append(F(191, "end of p. 191 / top of p. 192: 'en un de ses idéaux premiers.'",
           "printed p. 191 ends with the display Â_p⊗_A L = (Â_p⊗_A K)⊗_K L; p. 192 begins 'en un de ses idéaux premiers. Pour montrer que cet anneau local …' as one paragraph",
           "'en un de ses idéaux premiers.' stands before \\oldpage{192}; blank lines around the marker start a new paragraph at 'Pour montrer'",
           'marker', None, 'high', r"\]¶en un de ses idéaux premiers.¶¶", r"\]¶",
           "Move, part 1 of 2: removes the words (and the blank line) from the end of the p. 191 segment; part 2 is the LAST p. 192 finding, which puts them after \\oldpage{192} on the line of 'Pour montrer'. Apply both or neither (part 1 alone loses the words, part 2 alone duplicates them); either order works and the p. 192 marker never moves."))

# ---------------------------------------------------------------- page 192
L.append(F(192, "proof of (22.3.2), case I): 'est une K-algèbre formellement lisse (19.3.5, (iii) et (iv))'",
           "'algèbre formellement lisse' italic (crop)", "upright", 'italics', None, 'high',
           r"$K$-algèbre formellement lisse (19.3.5", r"$K$-\emph{algèbre formellement lisse} (19.3.5"))
L.append(F(192, "proof of (22.3.2): 'de vérifier la condition b) de (22.2.8)'", "'b)' italic (crop)", "'b)' upright",
           'italics', None, 'high', r"vérifier la condition b) de", r"vérifier la condition \emph{b)} de"))
L.append(F(192, "proof of (22.3.2): 'par suite Â⊗_{A_α}K_α = Â⊗_A(A⊗_{A_α}K_α) est une …'",
           "formula in the running text, at the end of the line 'vement à A_α (pour les topologies discrètes); par suite'",
           "displayed with \\[ \\]", 'other', None, 'high',
           r"par suite¶\[¶  \widehat A\otimes_{A_\alpha}K_\alpha¶  =\widehat A\otimes_A(A\otimes_{A_\alpha}K_\alpha)¶\]¶est une",
           r"par suite¶$\widehat A\otimes_{A_\alpha}K_\alpha=\widehat A\otimes_A(A\otimes_{A_\alpha}K_\alpha)$¶est une",
           "Formula displayed where the print has it inline; no connecting words lost."))
L.append(F(192, "proof of (22.3.2): 'comme A est une A_α-algèbre finie, on a'", "'finie' italic (crop)", "upright",
           'italics', None, 'high', r"$A_\alpha$-algèbre finie, on a", r"$A_\alpha$-algèbre \emph{finie}, on a"))
L.append(F(192, "proof of (22.3.2): 'Â_p est une K-algèbre formellement lisse relativement à K_α, pour la topologie discrète'",
           "'relativement à' italic (crop)", "upright", 'italics', None, 'high',
           r"relativement à $K_\alpha$, pour la topologie", r"\emph{relativement à} $K_\alpha$, pour la topologie"))
L.append(F(192, "proof of (22.3.2): 'Mais cela est précisément la condition b) de (22.2.8)'", "'b)' italic (crop)",
           "'b)' upright", 'italics', None, 'high', r"précisément la condition b) de",
           r"précisément la condition \emph{b)} de"))
L.append(F(192, "proof of (22.3.2), case II): 'S = A—𝔰'", "long dash for the set difference", "minus sign",
           'convention', 7, 'high', r"$S=A-\mathfrak s$", r"$S=A\setmin\mathfrak s$"))
L.append(F(192, "proof of (22.3.2), case II): 'où cette fois, S^{-1}𝔫 contient'", "comma after 'cette fois' (crop)",
           "no comma", 'punctuation', None, 'high', r"où cette fois¶$S^{-1}", r"où cette fois,¶$S^{-1}"))
L.append(F(192, "proof of (22.3.2), case II): 'S_α = A_α—𝔰_α'", "long dash for the set difference", "minus sign",
           'convention', 7, 'high', r"$S_\alpha=A_\alpha-\mathfrak s_\alpha$", r"$S_\alpha=A_\alpha\setmin\mathfrak s_\alpha$"))
L.append(F(192, "Théorème (22.3.3): 'Soient A un anneau local noethérien complet'",
           "'complet' roman inside the italic statement (crop)", "italic", 'convention', 6, 'high',
           r"noethérien complet, $\mathfrak p$", r"noethérien \textup{complet}, $\mathfrak p$"))
L.append(F(192, "Théorème (22.3.3): 'Alors l'anneau localisé B̂_𝔭 de B̂ est une B_𝔯-algèbre …'",
           "B̂ with subscript Fraktur 𝔭 (side-by-side crop with the 𝔭 of A_𝔭 and the 𝔮 of B̂_𝔮 in the proof)",
           "\\widehat B_\\mathfrak q (silent correction)", 'misprint_in_print', None, 'high',
           r"localisé $\widehat B_\mathfrak q$ de", r"localisé $\widehat B_\mathfrak p$ de",
           "The statement localizes B̂ at its prime 𝔮 (𝔭 is a prime of A); the proof works with B̂_𝔮 throughout. The diplomatic text restores the printed 𝔭.",
           corrected=r"\widehat B_\mathfrak q"))
L.append(F(192, "proof of (22.3.3): 'il suffit de prouver que B̂_𝔮⊗_{B_𝔯}k = B̂_𝔮/𝔯B̂_𝔮 est une k-algèbre …'",
           "formula in the running text ('… il suffit de prouver que B̂_𝔮⊗_{B_𝔯}k = B̂_𝔮/𝔯B̂_𝔮 est une k-algèbre formellement' on one line)",
           "displayed with \\[ \\]", 'other', None, 'high',
           r"il suffit de prouver que¶\[¶  \widehat B_\mathfrak q\otimes_{B_\mathfrak r}k¶  =\widehat B_\mathfrak q/\mathfrak r\widehat B_\mathfrak q¶\]¶est une $k$-algèbre",
           r"il suffit de prouver que¶$\widehat B_\mathfrak q\otimes_{B_\mathfrak r}k=\widehat B_\mathfrak q/\mathfrak r\widehat B_\mathfrak q$¶est une $k$-algèbre",
           "Formula displayed where the print has it inline; no connecting words lost."))
L.append(F(192, "proof of (22.3.3): 'B/𝔯 = A'_{𝔭'}, où 𝔭' = 𝔭/𝔫'", "A'_{𝔭'}: A with a prime (crop at 4x)",
           "A_{\\mathfrak p'} (prime on A missing)", 'formula', None, 'high',
           r"$B/\mathfrak r=A_{\mathfrak p'}$", r"$B/\mathfrak r=A'_{\mathfrak p'}$",
           "A' = A/𝔫 (defined a few lines above); B/𝔯 = (A/𝔫)_{𝔭/𝔫}."))
L.append(F(192, "Corollaire (22.3.4): 'Soient A un anneau local noethérien complet et intègre'",
           "'complet' roman, 'et intègre' italic (crop)", "italic", 'convention', 6, 'high',
           r"noethérien complet et intègre", r"noethérien \textup{complet} et intègre"))
L.append(F(192, "end of p. 192: '… Alors, pour tout idéal premier 𝔮' | p. 193 'du complété B̂, …'",
           "the statement of (22.3.4) runs on to p. 193 ('du complété' flush left): no paragraph break",
           "blank line at the end of the p. 192 segment (and another after \\oldpage{193})", 'other', None, 'high',
           r"pour tout idéal premier $\mathfrak q$¶¶", r"pour tout idéal premier $\mathfrak q$¶",
           "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the first p. 193 finding."))
L.append(F(192, "top of p. 192: 'en un de ses idéaux premiers. Pour montrer que cet anneau local …'",
           "p. 192 begins with 'en un de ses idéaux premiers.' and 'Pour montrer' follows on the same line (no new paragraph)",
           "the words stand before the marker (p. 191 segment); blank line after \\oldpage{192}", 'marker', None, 'high',
           r"\oldpage[0\textsubscript{IV-1}]{192}¶¶Pour montrer",
           r"\oldpage[0\textsubscript{IV-1}]{192}¶en un de ses idéaux premiers. Pour montrer",
           "Move, part 2 of 2 (see the last p. 191 finding): puts the words after the marker and removes the paragraph break. Apply both or neither."))

# ---------------------------------------------------------------- page 193
L.append(F(193, "top of p. 193: 'du complété B̂, tel que 𝔮∩B = 0, …' (statement of (22.3.4) continued)",
           "flush left, continuing the sentence of p. 192", "blank line after \\oldpage{193}: new paragraph",
           'other', None, 'high', r"\oldpage[0\textsubscript{IV-1}]{193}¶¶du complété",
           r"\oldpage[0\textsubscript{IV-1}]{193}¶du complété",
           "Apply together with the last-but-one p. 192 finding (blank line before the marker)."))
L.append(F(193, "proof of (22.3.4): 'et est tel que A soit une A_0-algèbre finie.'", "'finie' italic (crop)",
           "upright", 'italics', None, 'high', r"$A_0$-algèbre finie. Or", r"$A_0$-algèbre \emph{finie}. Or"))
L.append(F(193, "proof of (22.3.4): 'l'anneau A_0 est régulier (17.3.8)'", "'régulier' italic (crop)", "upright",
           'italics', None, 'high', r"est régulier (17.3.8)", r"est \emph{régulier} (17.3.8)"))
L.append(F(193, "Proposition (22.4.1): 'un polynôme unitaire de A[T_i], de degré d_i'",
           "comma after A[T_i] (crop)", "no comma", 'punctuation', None, 'high',
           r"de $A[T_i]$ de degré", r"de $A[T_i]$, de degré"))
L.append(F(193, "Proposition (22.4.1), label (i)", "(i) upright", "\\item[(i)] italic in the statement",
           'convention', 6, 'high', r"\item[(i)] Si l'on pose", r"\item[\textup{(i)}] Si l'on pose"))
L.append(F(193, "Proposition (22.4.1), label (ii)", "(ii) upright", "\\item[(ii)] italic in the statement",
           'convention', 6, 'high', r"\item[(ii)] Pour que", r"\item[\textup{(ii)}] Pour que"))
L.append(F(193, "proof of (22.4.1): 'M_ν = t_1^{ν_1}t_2^{ν_2} … t_r^{ν_r}'", "baseline dots (crop)", "\\cdots",
           'symbol', None, 'high', r"t_2^{\nu_2}\cdots t_r^{\nu_r}", r"t_2^{\nu_2}\ldots t_r^{\nu_r}"))
L.append(F(193, "proof of (22.4.1): '0 ≤ ν_i ≤ d_i—1'", "long dash for the minus sign (crop at 4x)", "minus sign",
           'convention', 7, 'high', r"\nu_i\leqslant d_i-1$", r"\nu_i\leqslant d_i\setmin 1$"))
L.append(F(193, "proof of (22.4.1): 'forment une base du A-module A''", "'base' italic (crop)", "upright",
           'italics', None, 'high', r"forment une base du", r"forment une \emph{base} du"))
L.append(F(193, "Proposition (22.4.3): 'les notations étant celles de (22.4.1)'",
           "reference upright inside the italic statement", "italic", 'convention', 6, 'high',
           r"(22.4.1), supposons¶que les $F_i$", r"\textup{(22.4.1)}, supposons¶que les $F_i$"))
L.append(F(193, "display (22.4.3.1): 'F_i(T_i) = T_i^{d_i} + Σ c_{ik}T_i^{d_i-k}'",
           "no punctuation after the display (crop)", "comma added after T_i^{d_i-k}", 'punctuation', None, 'high',
           r"c_{ik}T_i^{d_i-k},¶", r"c_{ik}T_i^{d_i-k}¶"))
L.append(F(193, "Proposition (22.4.3), label (i)", "(i) upright", "\\item[(i)] italic in the statement",
           'convention', 6, 'high', r"\item[(i)] $A'$ est un anneau local, et son corps",
           r"\item[\textup{(i)}] $A'$ est un anneau local, et son corps"))

# ---------------------------------------------------------------- page 194
L.append(F(194, "Proposition (22.4.3), label (ii)", "(ii) upright", "\\item[(ii)] italic in the statement",
           'convention', 6, 'high', r"\item[(ii)] Le noyau", r"\item[\textup{(ii)}] Le noyau"))
L.append(F(194, "display (22.4.3.2): 'rg_{K'}(V') = rg_K(V) + r—r''",
           "long dash for the minus sign (crop at 4x: longer than the bar of +)", "minus sign", 'convention', 7,
           'high', r"(V)+r-r'", r"(V)+r\setmin r'"))
L.append(F(194, "display (22.4.3.2)", "no punctuation after r' ('où r' = …' follows)", "comma added after r'",
           'punctuation', None, 'high', r",¶    \tag{22.4.3.2}", r"¶    \tag{22.4.3.2}"))
L.append(F(194, "proof of (22.4.3) (ii), display '𝔪' = 𝔪A' + Σ_{i=1}^r t_iA''",
           "no punctuation after t_iA' (crop)", "comma added", 'punctuation', None, 'high',
           r"t_iA',¶\]", r"t_iA'¶\]"))
L.append(F(194, "proof of (22.4.3) (ii): paragraph 'Soient 𝔠_1 = …'",
           "'Soient' begins an indented paragraph after the display ξ_i (1≤i≤r), …", "no blank line after \\]",
           'other', None, 'high', r"\]¶Soient", r"\]¶¶Soient", "Paragraph break as printed."))
L.append(F(194, "proof of (22.4.3) (ii): 'Soient 𝔠_1 = Σ_{i,j}T_iT_jA[T_1, …, T_r], 𝔠_2 = 𝔠_1 + Σ_i 𝔪T_iA[T_1, …, T_r], de sorte que'",
           "both formulas in the running text, on the line of 'Soient … de sorte que'",
           "displayed with \\[ \\] (joined by \\qquad)", 'other', None, 'high',
           r"\[¶  \mathfrak c_1=\sum_{i,j}T_iT_jA[T_1,\ldots,T_r],\qquad¶  \mathfrak c_2=\mathfrak c_1+\sum_i\mathfrak mT_iA[T_1,\ldots,T_r],¶\]¶de sorte que",
           r"$\mathfrak c_1=\sum_{i,j}T_iT_jA[T_1,\ldots,T_r]$,¶$\mathfrak c_2=\mathfrak c_1+\sum_i\mathfrak mT_iA[T_1,\ldots,T_r]$, de sorte que",
           "Formulas displayed where the print has them inline; no connecting words lost (the commas are printed). Does not overlap the previous finding."))
L.append(F(194, "Proposition (22.4.4): 'les notations étant celles de (22.4.1)'",
           "reference upright inside the italic statement", "italic", 'convention', 6, 'high',
           r"(22.4.1), supposons¶que $K$ soit", r"\textup{(22.4.1)}, supposons¶que $K$ soit"))
L.append(F(194, "Proposition (22.4.4): '(donc p.1∈𝔪 dans A)'", "p.1 with a baseline period (crop at 600 dpi)",
           "p\\cdot1", 'symbol', None, 'high', r"$p\cdot1\in\mathfrak m$", r"$p.1\in\mathfrak m$",
           "GLOBAL_ISSUES 65."))
L.append(F(194, "display (22.4.4.1): '… c_{ik}T_i^{p-k}—f_i'",
           "long dash before f_i (81 px at 600 dpi against 69 px for the bars of =); the minus signs in p-1 and p-k are short",
           "minus sign", 'convention', 7, 'high', r"c_{ik}T_i^{p-k}-f", r"c_{ik}T_i^{p-k}\setmin f"))
L.append(F(194, "display (22.4.4.1): subscript i of the final f_i",
           "bold italic i (wrong fount): at 600 dpi 347 px, stroke 14 px, against 198-286 px and 6-9 px for the other subscript i's of the display and of 'c_{ik}∈A et f_i∈A' (side-by-side crop)",
           "plain f_i (silent correction)", 'misprint_in_print', None, 'medium',
           r"_i¶  \tag{22.4.4.1}", r"_{\boldsymbol{i}}¶  \tag{22.4.4.1}",
           "Wrong-fount letter (GLOBAL_ISSUES 29), reproduced in the diplomatic text. Does not overlap the convention-7 finding just above (that one ends at 'f').",
           corrected=r"f_i"))
L.append(F(194, "Proposition (22.4.4): 'pour tout i et tout k tel que 1 ≤ k ≤ p—1'",
           "long dash for the minus sign (83 px at 600 dpi)", "minus sign", 'convention', 7, 'high',
           r"k\leqslant p-1$", r"k\leqslant p\setmin 1$"))
L.append(F(194, "Proposition (22.4.4): 'en outre si a_i est la classe de f_i mod. 𝔪'",
           "subscript i of a_i bold italic (wrong fount): 337 px, stroke 13 px at 600 dpi, like the f_i of (22.4.4.1); the i of f_i in the same line is normal",
           "plain a_i (silent correction)", 'misprint_in_print', None, 'medium',
           r"si $a_i$ est la classe", r"si $a_{\boldsymbol{i}}$ est la classe",
           "Wrong-fount letter (GLOBAL_ISSUES 29), reproduced in the diplomatic text.", corrected=r"$a_i$"))
L.append(F(194, "Proposition (22.4.4): 'la classe de f_i mod. 𝔪'", "'mod.' upright inside the italic statement",
           "italic", 'convention', 6, 'high', r"mod.~$\mathfrak m$, on suppose",
           r"\textup{mod.}~$\mathfrak m$, on suppose"))
L.append(F(194, "Proposition (22.4.4): '(« absolument p-libre »)'",
           "parentheses, guillemets, 'absolument' and 'libre' roman inside the italic statement (600-dpi crop)",
           "italic", 'convention', 6, 'high', r"(«~absolument $p$-libre~»)",
           r"\textup{(«~absolument $p$-libre~»)}"))
L.append(F(194, "Proposition (22.4.4), label (i)", "(i) upright", "\\item[(i)] italic in the statement",
           'convention', 6, 'high', r"\item[(i)] $A'$ est un anneau local, d'idéal",
           r"\item[\textup{(i)}] $A'$ est un anneau local, d'idéal"))

# ---------------------------------------------------------------- page 195
L.append(F(195, "Proposition (22.4.4), label (ii)", "(ii) upright", "\\item[(ii)] italic in the statement",
           'convention', 6, 'high', r"\item[(ii)] Les éléments", r"\item[\textup{(ii)}] Les éléments"))
L.append(F(195, "Proposition (22.4.4) (ii): 'de l'homomorphisme canonique Ω^1_A⊗_A K' → Ω^1_{A'}⊗_{A'} K'.'",
           "formula in the running text (second line of (ii))", "displayed with \\[ \\]", 'other', None, 'high',
           r"canonique¶  \[¶    \Omega^1_A\otimes_AK'\longrightarrow¶    \Omega^1_{A'}\otimes_{A'}K'.¶  \]",
           r"canonique¶  $\Omega^1_A\otimes_AK'\longrightarrow\Omega^1_{A'}\otimes_{A'}K'$.",
           "Formula displayed where the print has it inline; no connecting words lost."))
L.append(F(195, "proof of (22.4.4) (i): 'les polynômes T^p—a_i'", "long dash for the minus sign (crop)",
           "minus sign", 'convention', 7, 'high', r"-a_i$~;", r"\setmin a_i$~;"))
L.append(F(195, "proof of (22.4.4) (i): 'l'idéal engendré par les polynômes T^p—a_i'",
           "T^p without the subscript i (600-dpi crop)", "T_i^p (silent correction)", 'misprint_in_print', None,
           'high', r"polynômes $T_i^p", r"polynômes $T^p",
           "Does not overlap the convention-7 finding just above.", corrected=r"T_i^p"))
L.append(F(195, "proof of (22.4.4) (i): 'l'hypothèse faite sur les a_i entraîne que est anneau quotient est un corps'",
           "'que est | anneau quotient' (600-dpi crop): 'est' for 'cet'", "'cet' (silent correction)",
           'misprint_in_print', None, 'high', r"que¶cet anneau quotient", r"que¶est anneau quotient",
           "", corrected=r"cet"))
L.append(F(195, "Lemme (22.4.4.2): '(ce qui équivaut à dire que p.1∈𝔍 dans A)'",
           "p.1 with a baseline period (600-dpi crop)", "p\\cdot1", 'symbol', None, 'high',
           r"que $p\cdot1\in\mathfrak J$", r"que $p.1\in\mathfrak J$", "GLOBAL_ISSUES 65."))
L.append(F(195, "Lemme (22.4.4.2): 'Soit π l'image canonique de p.1 dans 𝔍/𝔍²'",
           "p.1 with a baseline period (600-dpi crop)", "p\\cdot1", 'symbol', None, 'high',
           r"de $p\cdot1$ dans", r"de $p.1$ dans", "GLOBAL_ISSUES 65."))
L.append(F(195, "display (22.4.4.3): '0 → (𝔍/𝔍²)/C.π → …'", "C.π with a baseline period (600 dpi: the dot sits on the baseline of C and π)",
           "C\\cdot\\pi", 'symbol', None, 'high', r"/C\cdot\pi", r"/C.\pi",
           "Same printed period as in p.1 (GLOBAL_ISSUES 65)."))
L.append(F(195, "proof of Lemme (22.4.4.2)", "a new indented paragraph 'Posons en effet …' without any heading",
           "\\begin{proof}[Démonstration du lemme] typesets the bracket text", 'extra', None, 'high',
           r"\begin{proof}[Démonstration du lemme]", r"\begin{proof}",
           "GLOBAL_ISSUES 58 (as on pp. 34, 81, 85). The 'Démonstration. —' that the environment still prints is the document-wide item."))
L.append(F(195, "display (22.4.4.4): 'V_0 = V/K.p = …'", "K.p with a baseline period (600 dpi: the dot sits on the baseline of K)",
           "K\\cdot p", 'symbol', None, 'high', r"V_0=V/K\cdot p", r"V_0=V/K.p",
           "Same printed period as in p.1 (GLOBAL_ISSUES 65)."))
L.append(F(195, "display (22.4.4.4): 'V'_0 = V'/K'.p = …'", "K'.p with a baseline period (600 dpi: the dot sits on the baseline of K')",
           "K'\\cdot p", 'symbol', None, 'high', r"V_0'=V'/K'\cdot p", r"V_0'=V'/K'.p",
           "Same printed period as in p.1 (GLOBAL_ISSUES 65)."))
L.append(F(195, "after (22.4.4.4): paragraph 'Appliquant la suite exacte (22.4.4.3) …'",
           "'Appliquant' begins an indented paragraph after the display", "no blank line after \\end{equation}",
           'other', None, 'high', r"\end{equation}¶Appliquant", r"\end{equation}¶¶Appliquant",
           "Paragraph break as printed."))
L.append(F(195, "after (22.4.4.5): paragraph 'Considérons alors le diagramme (22.4.4.6) …'",
           "'Considérons' begins an indented paragraph after the display", "no blank line after \\end{equation}",
           'other', None, 'high', r"\end{equation}¶Considérons", r"\end{equation}¶¶Considérons",
           "Paragraph break as printed."))
L.append(F(195, "last sentence: 'la ligne supérieure du diagramme (22.4.4.6) est exacte; les colonnes extrêmes'",
           "'exacte' italic (600-dpi crop)", "upright", 'italics', None, 'high',
           r"(22.4.4.6) est¶exacte", r"(22.4.4.6) est¶\emph{exacte}"))
L.append(F(195, "last sentence: 'est exacte; les colonnes extrêmes du diagramme'",
           "semicolon after 'exacte' (600-dpi crop)", "comma", 'punctuation', None, 'high',
           r", les colonnes", r"~; les colonnes",
           "Does not overlap the italics finding just above."))
L.append(F(195, "end of p. 195: '… les colonnes extrêmes du diagramme' | p. 196 begins with the display (22.4.4.6)",
           "the sentence runs on into the display at the top of p. 196 ('sont donc formées' follows it): no paragraph break",
           "blank line at the end of the p. 195 segment (and another after \\oldpage{196})", 'other', None, 'high',
           r"extrêmes du diagramme¶¶", r"extrêmes du diagramme¶",
           "GLOBAL_ISSUES 20. Pairs with the p. 196 finding of findings_196_200.json (removes the blank line after \\oldpage{196}); apply both."))

# ---------------------------------------------------------------- checks
pages = {}
for p in range(191, 196):
    pages[p] = (RUN / ('page_%d.tex' % p)).read_text(encoding='utf-8').replace('\r\n', '\n')
bad = 0
for x in L:
    if x['fix'] is None:
        continue
    t = pages[x['page']]
    n = t.count(x['fix']['old'])
    if n != 1:
        bad += 1
        print('NOT UNIQUE/NOT FOUND', x['page'], n, repr(x['fix']['old'][:80]))
# overlap check within a page
for p in range(191, 196):
    spans = []
    for x in L:
        if x['page'] == p and x['fix'] is not None:
            i = pages[p].find(x['fix']['old'])
            spans.append((i, i + len(x['fix']['old']), x['where'][:50]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            print('OVERLAP', p, a, b)
OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1), encoding='utf-8')
from collections import Counter
c = Counter()
for x in L:
    k = 'misprint' if x['kind'] == 'misprint_in_print' else ('convention' if x['kind'] == 'convention' else 'normal')
    c[(x['page'], k)] += 1
for p in range(191, 196):
    print(p, c[(p, 'normal')], c[(p, 'convention')], c[(p, 'misprint')])
print('total', len(L), 'bad', bad)
