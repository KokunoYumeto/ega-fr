import json, io, sys, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
RUN = r'user\Documents\ega_scan_check_20261101\run_IV2'
OUT = os.path.join(RUN, 'findings_195_199.json')
NL = '<NL>'


def F(page, where, scan, tex, kind, old, new, conf='high', conv=None, note=None, corrected=None, nofix=False):
    d = {
        'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind,
        'convention': conv, 'confidence': conf,
        'fix': None if nofix else {'old': old.replace(NL, '\n'), 'new': new.replace(NL, '\n')},
    }
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    return d


UR_NOTE = ("The print sets the subscript of U_R in a bold upright sans-serif R (same face as the bold subscript k of "
           "the tensor products on p. 197), not the bold italic R of the running text; the TeX has \\boldsymbol R "
           "(bold italic). Fix written \\mathbf{R} in line with the edition's \\mathbf{k} for that subscript k "
           "(GLOBAL_ISSUES 48); \\boldsymbol{\\mathsf R} would also give the sans-serif shape. Document-wide: about "
           "20 U_{\\boldsymbol R} in ega4-2-fr.tex.")

f = []

# ---------------- page 195 ----------------
f.append(F(195, "Remarque (7.3.11), condition (R'_I): 'f : X->Y un P-morphisme (pour la propriété P'",
           "'P-morphisme' with 'morphisme' italic (enlarged crop)",
           "no emphasis on 'morphisme'", 'italics',
           r"un $\boldsymbol P$-morphisme (pour la", r"un $\boldsymbol P$-\emph{morphisme} (pour la",
           note="Remark body judged as roman (document-wide remark item)."))
f.append(F(195, "Proposition (7.3.12): '(R_I) et (R_II) (resp. (R'_I) et (R_II))'",
           "'(resp.' upright inside the italic statement", "italic (statement environment)", 'convention',
           r"(resp.<NL>$(\mathrm R'_{\mathrm I})$", r"\textup{(resp.}<NL>$(\mathrm R'_{\mathrm I})$", conv=6))
f.append(F(195, "Proposition (7.3.12): 'tout morphisme régulier (resp. tout P-morphisme)'",
           "'(resp.' upright; 'tout' and 'P-morphisme' italic", "'resp.' italic (statement environment)",
           'convention', r"(resp. tout", r"\textup{(resp.} tout", conv=6))
f.append(F(195, "Proposition (7.3.12): 'U_R(X) désigne l'ensemble des x∈X'",
           "subscript R bold upright sans-serif (5x crop)", "U_{\\boldsymbol R} (bold italic)", 'font',
           r"$U_{\boldsymbol R}(X)$ désigne", r"$U_{\mathbf{R}}(X)$ désigne", conf='medium', note=UR_NOTE))
f.append(F(195, "display (7.3.12.1): U_R(X)=f^{-1}(U_R(Y)) (two occurrences)",
           "both subscripts R bold upright sans-serif (3x crop)", "U_{\\boldsymbol R} twice", 'font',
           r"U_{\boldsymbol R}(X)=f^{-1}(U_{\boldsymbol R}(Y))", r"U_{\mathbf{R}}(X)=f^{-1}(U_{\mathbf{R}}(Y))",
           conf='medium', note="See the U_R finding above (same decision)."))
f.append(F(195, "Remarque (7.3.11): 'Les raisonnements de (6.6.1) et (6.8.3) prouvent que si R'",
           "new indented paragraph after condition (R'_I)",
           "text follows \\end{enumerate} without a blank line (continues the paragraph, no indent)", 'other',
           r"\end{enumerate}<NL>Les raisonnements", r"\end{enumerate}<NL><NL>Les raisonnements", conf='medium',
           note="Paragraph break of the print."))
f.append(F(195, "(7.3.13): 'nous appellerons fibres formelles de A les fibres'",
           "only 'fibres formelles' italic; 'de A' roman (crop)", "\\emph{fibres formelles de $A$}", 'italics',
           r"\emph{fibres formelles de $A$}", r"\emph{fibres formelles} de $A$"))
f.append(F(195, "(7.3.13): 'Spec(Â⊗_A k(p))'", "bold italic k (3x crop)", "plain k", 'convention',
           r"\otimes_A k(\mathfrak p))", r"\otimes_A \boldsymbol{k}(\mathfrak p))", conv=1))
f.append(F(195, "(7.3.13), last line: 'au point générique (0) de Spec(A/p)'",
           "'(0)' upright roman between the italic words 'au point générique' and 'de' (crop)",
           "'(0)' inside \\emph{...} (italic)", 'italics',
           r"générique (0) de", r"générique \textup{(0)} de", conf='medium'))

# ---------------- page 196 ----------------
f.append(F(196, "first paragraph: 'P(f^{-1}(x), k(x)) est vraie'", "bold italic k", "plain k", 'convention',
           r"$\boldsymbol P(f^{-1}(x),k(x))$", r"$\boldsymbol P(f^{-1}(x),\boldsymbol{k}(x))$", conv=1))
f.append(F(196, "first paragraph, end: 'que f est un P-morphisme.'", "'morphisme' italic (crop)",
           "no emphasis", 'italics',
           r"est un $\boldsymbol P$-morphisme.", r"est un $\boldsymbol P$-\emph{morphisme}."))
f.append(F(196, "Proposition (7.3.15), label (i)", "label '(i)' upright, with both parentheses (crop)",
           "\\item[\\emph{i)}] gives 'i)' without the opening parenthesis", 'punctuation',
           r"\item[\emph{i)}] Si $A$", r"\item[\textup{(i)}] Si $A$"))
f.append(F(196, "Proposition (7.3.15), label (ii)", "label '(ii)' upright, with both parentheses (crop)",
           "\\item[\\emph{ii)}] gives 'ii)'", 'punctuation',
           r"\item[\emph{ii)}] Si de plus", r"\item[\textup{(ii)}] Si de plus"))
f.append(F(196, "Proposition (7.3.15) (ii): 'la condition (P_IV) (7.3.6), alors'",
           "reference (7.3.6) upright inside the italic statement", "italic", 'convention',
           r"(7.3.6), alors", r"\textup{(7.3.6)}, alors", conv=6))
f.append(F(196, "Proposition (7.3.16): 'est du premier (resp. du second) type'",
           "'(resp.' upright, 'du second' italic (crop)", "'resp.' italic", 'convention',
           r"premier (resp. du", r"premier \textup{(resp.} du", conv=6))
f.append(F(196, "Proposition (7.3.16): 'définie à partir d'une propriété R (7.3.10).'",
           "reference (7.3.10) upright", "italic", 'convention',
           r"$\boldsymbol R$ (7.3.10).", r"$\boldsymbol R$ \textup{(7.3.10)}.", conv=6))
f.append(F(196, "Proposition (7.3.16), the quoted relation: '« pour toute extension finie k' de k'",
           "'finie' upright (emphasis) among italic words (crop)", "italic", 'convention',
           r"extension finie $k'$", r"extension \textup{finie} $k'$", conv=6))
f.append(F(196, "Proposition (7.3.16): '(ce qui est vérifié pour les exemples (iv') à (vii') de (7.3.8), en vertu de (6.7.7) et (4.6.1))'",
           "the whole parenthesis upright roman (crop)", "italic (statement environment)", 'convention',
           r"(ce qui est vérifié pour les exemples<NL>(iv$'$) à (vii$'$) de (7.3.8), en vertu de (6.7.7) et (4.6.1))",
           r"\textup{(ce qui est vérifié pour les exemples<NL>(iv$'$) à (vii$'$) de (7.3.8), en vertu de (6.7.7) et (4.6.1))}",
           conv=6))
f.append(F(196, "Proposition (7.3.16) b): 'intègre B de A (resp. toute A-algèbre finie intègre B)'",
           "'(resp.' upright", "italic", 'convention',
           r"intègre $B$ de $A$ (resp. toute", r"intègre $B$ de $A$ \textup{(resp.} toute", conv=6))
f.append(F(196, "Proposition (7.3.16): 'Si de plus R satisfait à la condition (R'_I)'",
           "new indented paragraph after item b)",
           "text follows \\end{enumerate} without a blank line (no new paragraph)", 'other',
           r"\end{enumerate}<NL>Si de plus", r"\end{enumerate}<NL><NL>Si de plus", conf='medium',
           note="Paragraph break of the print."))
f.append(F(196, "Proposition (7.3.16): 'les propriétés a) et b) sont aussi équivalentes à :'",
           "'a)' and 'b)' upright inside the italic statement (crop)", "italic", 'convention',
           r"les propriétés a) et b) sont aussi", r"les propriétés \textup{a)} et \textup{b)} sont aussi", conv=6))
f.append(F(196, "Proposition (7.3.16) c): 'quotient B de A (resp. toute A-algèbre finie B)'",
           "'(resp.' upright", "italic", 'convention',
           r"quotient $B$ de $A$ (resp. toute", r"quotient $B$ de $A$ \textup{(resp.} toute", conv=6))
f.append(F(196, "Proposition (7.3.16) c): '(avec les notations de (7.3.12))'",
           "'avec les notations de' italic, the reference (7.3.12) upright", "reference italic", 'convention',
           r"notations de (7.3.12))", r"notations de \textup{(7.3.12)})", conv=6))
f.append(F(196, "display (7.3.16.1): U_R(Y')=g^{-1}(U_R(Y)) (two occurrences)",
           "both subscripts R bold upright sans-serif", "U_{\\boldsymbol R} twice", 'font',
           r"U_{\boldsymbol R}(Y')=g^{-1}(U_{\boldsymbol R}(Y))", r"U_{\mathbf{R}}(Y')=g^{-1}(U_{\mathbf{R}}(Y))",
           conf='medium', note="Same decision as the U_R findings on p. 195."))
f.append(F(196, "proof of (7.3.16): 'L'équivalence de a) et b) est immédiate'",
           "'a)' and 'b)' italic in the roman proof (crop)", "upright", 'italics',
           r"L'équivalence de a) et b) est", r"L'équivalence de \emph{a)} et \emph{b)} est"))
f.append(F(196, "proof of (7.3.16): 'l'équivalence de a) et b) résulte du lemme plus général suivant'",
           "'a)' and 'b)' italic (crop)", "upright", 'italics',
           r"l'équivalence de a) et b)<NL>résulte", r"l'équivalence de \emph{a)} et \emph{b)}<NL>résulte"))
f.append(F(196, "page break 196/197 (edit 1 of 2): Lemme (7.3.16.2) '... Afin que pour tout x∈Spec(A), toute | extension finie k de k(x)'",
           "the sentence runs on over the page break (no new paragraph on p. 197)",
           "blank line before \\oldpage[IV-2]{197} (end of the p. 196 segment) breaks the paragraph", 'marker',
           "$, toute<NL><NL>", "$, toute<NL>",
           note="Apply together with edit 2 of 2 (p. 197), which removes the blank line after the marker."))

# ---------------- page 197 ----------------
f.append(F(197, "page break 196/197 (edit 2 of 2): marker before 'extension finie k de k(x)'",
           "p. 197 begins mid-sentence 'extension finie k de k(x) et tout point z'",
           "blank line after \\oldpage[IV-2]{197}", 'marker',
           r"\oldpage[IV-2]{197}<NL><NL>extension", r"\oldpage[IV-2]{197}<NL>extension",
           note="Apply together with edit 1 of 2 (end of the p. 196 segment). The marker itself is in the right place."))
f.append(F(197, "Lemme (7.3.16.2): 'extension finie k de k(x) et tout point z'", "bold italic k", "plain k",
           'convention', r"finie $k$ de $k(x)$ et tout", r"finie $k$ de $\boldsymbol{k}(x)$ et tout", conv=1))
f.append(F(197, "Lemme (7.3.16.2): 'f^{-1}(x)⊗_{k(x)} k = Z'", "subscript k bold upright (sans-serif; 10x crop)",
           "plain k", 'convention', r"\otimes_{k(x)}k=Z", r"\otimes_{\mathbf{k}(x)}k=Z", conv=1,
           note="Bold upright in the subscript (GLOBAL_ISSUES 48)."))
f.append(F(197, "proof of (7.3.16.2): 'au-dessus duquel est ξ, k(ξ) est une extension finie'", "bold italic k",
           "plain k", 'convention', r"$\xi$, $k(\xi)$ est une", r"$\xi$, $\boldsymbol{k}(\xi)$ est une", conv=1))
f.append(F(197, "proof of (7.3.16.2): 'extension finie de k(x). Inversement'", "bold italic k", "plain k",
           'convention', r"finie de $k(x)$. Inversement", r"finie de $\boldsymbol{k}(x)$. Inversement", conv=1))
f.append(F(197, "proof of (7.3.16.2): 'et soit k une extension finie de k(x).'", "bold italic k", "plain k",
           'convention', r"soit $k$ une extension finie de $k(x)$.",
           r"soit $k$ une extension finie de $\boldsymbol{k}(x)$.", conv=1))
f.append(F(197, "proof of (7.3.16.2): 'Si l'on pose p = j_x,'",
           "lower-case Fraktur j (j_x, the prime ideal of x; 4x crop)", "\\mathfrak J (capital Fraktur J)", 'symbol',
           r"\mathfrak p=\mathfrak J_x", r"\mathfrak p=\mathfrak j_x",
           note="ega4-2-fr.tex writes \\mathfrak j_x elsewhere (14 times); one more \\mathfrak J_x near source line 15340, before p. 195."))
f.append(F(197, "proof of (7.3.16.2): 'k(x) est le corps des fractions de A/p'", "bold italic k", "plain k",
           'convention', r"$k(x)$ est le corps des", r"$\boldsymbol{k}(x)$ est le corps des", conv=1))
f.append(F(197, "proof of (7.3.16.2): 'une base de k sur k(x) formée'", "bold italic k", "plain k",
           'convention', r"sur $k(x)$ formée", r"sur $\boldsymbol{k}(x)$ formée", conv=1))
f.append(F(197, "proof of (7.3.16.2): 'k est le corps k(ξ) au point générique ξ'", "bold italic k", "plain k",
           'convention', r"corps $k(\xi)$ au point", r"corps $\boldsymbol{k}(\xi)$ au point", conv=1))
f.append(F(197, "proof of (7.3.16.2): 'comme x est l'image de ξ dans Spec(A)'",
           "this x is heavier than the other italic x of the page (strokes about 1.3x, hairline as thick as the main stroke; 9x side-by-side crop), likely a bold italic sort",
           "plain $x$ (silent normalisation if it is a wrong-font sort)", 'misprint_in_print',
           r"comme $x$ est l'image", r"comme $\boldsymbol{x}$ est l'image", conf='low', corrected="$x$",
           note="Wrong-font x (GLOBAL_ISSUES 29 pattern) or heavy inking: the weight gain is smaller than between the page's bold italic k and italic k, hence low confidence. The TeX silently has the normal x."))
f.append(F(197, "proof of (7.3.16.2): 'n'est autre que f^{-1}(x)⊗_{k(x)} k, ce qui achève'",
           "subscript k bold upright (sans-serif)", "plain k", 'convention',
           r"\otimes_{k(x)}k$, ce qui", r"\otimes_{\mathbf{k}(x)}k$, ce qui", conv=1,
           note="Bold upright in the subscript (GLOBAL_ISSUES 48)."))
f.append(F(197, "end of the proof of (7.3.16): heading 'Fin de la démonstration de (7.3.16)'",
           "no heading: the paragraph 'Le fait que a) entraîne c) ...' follows the proof of the lemma directly",
           "\\begin{proof}[Fin de la démonstration de (7.3.16)]: the proof environment takes no optional argument, so the bracket text is typeset",
           'extra', r"\begin{proof}[Fin de la démonstration de (7.3.16)]", r"\begin{proof}",
           note="The only \\begin{proof}[...] in ega4-2-fr.tex. The 'Démonstration. —' heading left by the environment is the document-wide proof-heading item."))
f.append(F(197, "end of the proof of (7.3.16): 'Le fait que a) entraîne c)'", "'a)' and 'c)' italic (crop)",
           "upright", 'italics', r"Le fait que a) entraîne c) est", r"Le fait que \emph{a)} entraîne \emph{c)} est"))
f.append(F(197, "end of the proof of (7.3.16): 'si on spécialise c) au cas où B est intègre'", "'c)' italic",
           "upright", 'italics', r"si on spécialise c) au cas", r"si on spécialise \emph{c)} au cas"))
f.append(F(197, "end of the proof of (7.3.16): 'O_{Y,y} = k(y)'", "bold italic k", "plain k", 'convention',
           r"=k(y)$", r"=\boldsymbol{k}(y)$", conv=1))
f.append(F(197, "end of the proof of (7.3.16): 'donc y∈U_R(Y)'", "subscript R bold upright sans-serif",
           "U_{\\boldsymbol R}", 'font', r"y\in U_{\boldsymbol R}(Y)$", r"y\in U_{\mathbf{R}}(Y)$", conf='medium',
           note="Same decision as the U_R findings on p. 195."))
f.append(F(197, "end of the proof of (7.3.16): 'appartient à U_R(Y')'", "subscript R bold upright sans-serif",
           "U_{\\boldsymbol R}", 'font', r"appartient à $U_{\boldsymbol R}(Y')$", r"appartient à $U_{\mathbf{R}}(Y')$",
           conf='medium', note="Same decision as the U_R findings on p. 195."))
f.append(F(197, "end of the proof of (7.3.16): 'on obtient l'énoncé b), donc c) entraîne b). C.Q.F.D.'",
           "'b)', 'c)', 'b)' italic (crop)", "upright", 'italics',
           r"l'énoncé b), donc c) entraîne b).", r"l'énoncé \emph{b)}, donc \emph{c)} entraîne \emph{b)}."))
f.append(F(197, "Proposition (7.3.17): 'la propriété du premier (resp. du second) type'",
           "'(resp.' upright, 'du second' italic (crop)", "'resp.' italic", 'convention',
           r"la propriété du premier (resp. du second)", r"la propriété du premier \textup{(resp.} du second)",
           conv=6))
f.append(F(197, "Proposition (7.3.17): 'définie à partir de R (7.3.10). Alors,'", "reference (7.3.10) upright",
           "italic", 'convention', r"$\boldsymbol R$ (7.3.10). Alors", r"$\boldsymbol R$ \textup{(7.3.10)}. Alors",
           conv=6))
f.append(F(197, "Proposition (7.3.18): 'une propriété du premier (resp. du second) type'",
           "'(resp.' upright, 'du second' italic", "'resp.' italic", 'convention',
           r"une propriété du premier (resp. du", r"une propriété du premier \textup{(resp.} du", conv=6))
f.append(F(197, "Proposition (7.3.18), condition (R_III): 'anneau local noethérien complet C'",
           "'complet' upright (emphasis) among italic words (crop)", "italic", 'convention',
           r"noethérien complet<NL>$C$", r"noethérien \textup{complet}<NL>$C$", conv=6))
f.append(F(197, "Proposition (7.3.18), condition (R_III): 'l'ensemble U_R(Z)'", "subscript R bold upright sans-serif",
           "U_{\\boldsymbol R}", 'font', r"U_{\boldsymbol R}(Z)", r"U_{\mathbf{R}}(Z)", conf='medium',
           note="Same decision as the U_R findings on p. 195."))
f.append(F(197, "Proposition (7.3.18), condition (R_III): 'U_R(Z) (7.3.12) est ouvert dans Z'",
           "reference (7.3.12) upright (crop)", "italic", 'convention',
           r"(7.3.12) est ouvert dans $Z$", r"\textup{(7.3.12)} est ouvert dans $Z$", conv=6))
f.append(F(197, "Proposition (7.3.18): 'l'ensemble U_R(X) est ouvert dans X'", "subscript R bold upright sans-serif",
           "U_{\\boldsymbol R}", 'font', r"l'ensemble $U_{\boldsymbol R}(X)$", r"l'ensemble $U_{\mathbf{R}}(X)$",
           conf='medium', note="Same decision as the U_R findings on p. 195."))
f.append(F(197, "proof of (7.3.18): 'U_R(X')=f^{-1}(U_R(X)) (7.3.12)' (two occurrences)",
           "both subscripts R bold upright sans-serif", "U_{\\boldsymbol R} twice", 'font',
           r"U_{\boldsymbol R}(X')=f^{-1}(U_{\boldsymbol R}(X))", r"U_{\mathbf{R}}(X')=f^{-1}(U_{\mathbf{R}}(X))",
           conf='medium', note="Same decision as the U_R findings on p. 195."))
f.append(F(197, "proof of (7.3.18): 'par hypothèse U_R(X') est ouvert dans X''", "subscript R bold upright sans-serif",
           "U_{\\boldsymbol R}", 'font', r"hypothèse<NL>$U_{\boldsymbol R}(X')$", r"hypothèse<NL>$U_{\mathbf{R}}(X')$",
           conf='medium', note="Same decision as the U_R findings on p. 195."))
f.append(F(197, "Remarques (7.3.19), label (i)", "label '(i)' upright, with both parentheses",
           "\\item[\\emph{i)}] gives 'i)' (and italic if the remark body is roman)", 'punctuation',
           r"\item[\emph{i)}] La propriété", r"\item[\textup{(i)}] La propriété"))
f.append(F(197, "Remarques (7.3.19) (i): 'du théorème de Cohen (0, 19.8.8)'", "bold 0", "plain 0", 'convention',
           r"(0, 19.8.8)", r"(\textbf{0}, 19.8.8)", conv=2))

# ---------------- page 198 ----------------
f.append(F(198, "Remarques (7.3.19), label (ii)", "label '(ii)' upright, with both parentheses",
           "\\item[\\emph{ii)}] gives 'ii)'", 'punctuation',
           r"\item[\emph{ii)}] Nous avons", r"\item[\textup{(ii)}] Nous avons"))
f.append(F(198, "(7.3.19) (ii): 'lorsque A est un anneau quotient d'un anneau de Cohen-Macaulay'",
           "'anneau' roman, 'quotient d'un anneau de Cohen-Macaulay' italic (crop)",
           "\\emph{anneau quotient d'un anneau de Cohen--Macaulay}", 'italics',
           r"un \emph{anneau quotient d'un anneau de", r"un anneau \emph{quotient d'un anneau de"))
f.append(F(198, "(7.3.19) (ii): 'Cohen-Macaulay, les fibres formelles'", "hyphen (crop)", "en dash (--)",
           'punctuation', r"Cohen--Macaulay}, les", r"Cohen-Macaulay}, les",
           note="ega4-2-fr.tex has 43 'Cohen--Macaulay' against 58 'Cohen-Macaulay'; the print uses a hyphen."))
f.append(F(198, "(7.3.19) (ii): 'schémas de Cohen-Macaulay (6.3.8)'", "hyphen", "en dash (--)", 'punctuation',
           r"Cohen--Macaulay} (6.3.8)", r"Cohen-Macaulay} (6.3.8)"))
f.append(F(198, "Remarques (7.3.19), label (iii)", "label '(iii)' upright, with both parentheses",
           "\\item[\\emph{iii)}] gives 'iii)'", 'punctuation',
           r"\item[\emph{iii)}] Le cas", r"\item[\textup{(iii)}] Le cas"))
f.append(F(198, "Remarques (7.3.19), label (iv)", "label '(iv)' upright, with both parentheses",
           "\\item[\\emph{iv)}] gives 'iv)'", 'punctuation',
           r"\item[\emph{iv)}] Soit", r"\item[\textup{(iv)}] Soit"))
f.append(F(198, "(7.3.19) (iv): 'des points maximaux b_i (1⩽i⩽r)'",
           "the subscript i is a bold italic sort (heavy stem and dot; 5x side-by-side crop with the thin i of b_i two lines below and of K_i)",
           "plain subscript i (silent normalisation)", 'misprint_in_print',
           r"$b_i$ $(1\leqslant i\leqslant r)$", r"$b_{\boldsymbol{i}}$ $(1\leqslant i\leqslant r)$", conf='medium',
           corrected="$b_i$", note="Wrong-font subscript (GLOBAL_ISSUES 29 pattern); the TeX silently has the normal i."))
f.append(F(198, "(7.3.19) (iv): 'aux points maximaux b_ij au-dessus de b_i'",
           "the subscript ij is in a bold italic sort (stems about twice the hairline of L_ij one line above; 8x crop)",
           "plain subscript ij (silent normalisation)", 'misprint_in_print',
           r"$b_{ij}$ au-dessus", r"$b_{\boldsymbol{ij}}$ au-dessus", conf='medium', corrected="$b_{ij}$",
           note="Wrong-font subscript (GLOBAL_ISSUES 29 pattern); the TeX silently has the normal ij."))
f.append(F(198, "(7.3.19) (iv): 'un anneau de Cohen-Macaulay, on voit que'", "hyphen (at the line end)",
           "en dash (--)", 'punctuation', r"Cohen--Macaulay, on voit", r"Cohen-Macaulay, on voit"))
f.append(F(198, "(7.3.19) (iv) d): 'Â est réduit et L_ij est une extension séparable de K_i'",
           "the subscript ij is a bold italic sort, as in b_ij (8x crop; the L_ij of 'corps résiduels L_ij' and K_i have the thin sort)",
           "plain subscript ij (silent normalisation)", 'misprint_in_print',
           r"$L_{ij}$ est une extension", r"$L_{\boldsymbol{ij}}$ est une extension", conf='medium',
           corrected="$L_{ij}$", note="Wrong-font subscript (GLOBAL_ISSUES 29 pattern); the TeX silently has the normal ij."))
f.append(F(198, "(7.3.19) (iv): 'En particulier, si A est un anneau de valuation discrète'",
           "new indented paragraph after item d)",
           "text follows \\end{enumerate} without a blank line (no new paragraph)", 'other',
           r"\end{enumerate}<NL>En particulier", r"\end{enumerate}<NL><NL>En particulier", conf='medium',
           note="Paragraph break of the print."))
f.append(F(198, "(7.3.19) (iv): 'soit une extension séparable de K.'", "'extension séparable de' italic, K roman (crop)",
           "'de' outside \\emph", 'italics',
           r"\emph{extension séparable}<NL>de $K$", r"\emph{extension séparable<NL>de} $K$"))
f.append(F(198, "(7.3.19) (iv), end: 'lorsque K est de caractéristique 0.'",
           "'de caractéristique' italic, '0' roman (crop)", "'de' roman, '0' inside \\emph", 'italics',
           r"est de \emph{caractéristique<NL>0}", r"est \emph{de caractéristique}<NL>0"))
f.append(F(198, "heading 7.4", "'7.4. Permanence des propriétés des fibres formelles.' (final full stop)",
           "\\subsection{...} without the full stop", 'punctuation',
           r"\subsection{Permanence des propriétés des fibres formelles}",
           r"\subsection{Permanence des propriétés des fibres formelles.}",
           note="GLOBAL_ISSUES 43/58 pattern, as the other IV-2 subsection page fixes."))
f.append(F(198, "(7.4.1): 'pour toute générisation z' de z dans Z'", "'générisation' italic (crop)", "no emphasis",
           'italics', r"pour toute générisation", r"pour toute \emph{générisation}"))
f.append(F(198, "(7.4.1): 'Q(O_z, k) entraîne Q(O_z', k)'", "'entraîne' italic (crop)", "no emphasis", 'italics',
           r"O_z,k)$ entraîne", r"O_z,k)$ \emph{entraîne}"))

# ---------------- page 199 ----------------
f.append(F(199, "proof of (7.4.2): 'φ̂ : Â→Â''", "hat over A only, prime outside the hat (4x crop)",
           "\\widehat{A'} (hat over A')", 'formula',
           r"\to\widehat{A'}$", r"\to\widehat{A}'$", note="Same pattern as convention 8, with a hat."))
f.append(F(199, "diagram of the proof of (7.4.2), top right node 'Spec(Â')'", "hat over A only, prime outside (3x crop)",
           "\\widehat{A'}", 'formula',
           r"{$\operatorname{Spec}(\widehat{A'})$}", r"{$\operatorname{Spec}(\widehat{A}')$}",
           note="Same pattern as convention 8, with a hat."))
f.append(F(199, "proof of (7.4.2): 'donc fidèlement plat (0_I, 6.6.2)'", "bold 0", "plain 0", 'convention',
           r"(0$_{\mathrm I}$, 6.6.2)", r"(\textbf{0}$_{\mathrm I}$, 6.6.2)", conv=2))
f.append(F(199, "Corollaire (7.4.3) (ii): 'la condition (P_IV) (7.3.6). Soient'",
           "reference (7.3.6) upright inside the italic statement", "italic", 'convention',
           r"(7.3.6). Soient", r"\textup{(7.3.6)}. Soient", conv=6))
f.append(F(199, "proof of (7.4.3), label (i)", "'(i)' upright in the roman proof (crop)",
           "\\item[\\emph{(i)}] italic", 'italics',
           r"\item[\emph{(i)}] Comme par hypothèse", r"\item[(i)] Comme par hypothèse"))
f.append(F(199, "proof of (7.4.3) (i): 'en vertu de (7.3.2, b)), pour tout'", "'b)' italic (crop)", "upright",
           'italics', r"(7.3.2, b)), pour tout", r"(7.3.2, \emph{b)}), pour tout"))
f.append(F(199, "proof of (7.4.3), label (ii)", "'(ii)' upright in the roman proof", "\\item[\\emph{(ii)}] italic",
           'italics', r"\item[\emph{(ii)}] En vertu de (7.4.2)", r"\item[(ii)] En vertu de (7.4.2)"))
f.append(F(199, "proof of (7.4.3) (ii), end: 'la conclusion résulte de (7.3.2, b)).'", "'b)' italic (crop)",
           "upright", 'italics', r"de (7.3.2, b)).", r"de (7.3.2, \emph{b)})."))
f.append(F(199, "Théorème (7.4.4): 'Les hypothèses sur P étant celles de (7.4.1), soit A'",
           "reference (7.4.1) upright inside the italic statement", "italic", 'convention',
           r"celles de (7.4.1), soit", r"celles de \textup{(7.4.1)}, soit", conv=6))
f.append(F(199, "proof of (7.4.4), label (i)", "'(i)' upright in the roman proof", "\\item[\\emph{(i)}] italic",
           'italics', r"\item[\emph{(i)}] Appliquant", r"\item[(i)] Appliquant"))
f.append(F(199, "proof of (7.4.4) (i): 'Appliquant (7.4.3, (i)), tout revient à voir'",
           "'(7.4.3, (i))' (2x crop)", "'(7.4.3, (ii))'", 'number',
           r"(7.4.3, (ii)), tout revient", r"(7.4.3, (i)), tout revient",
           note="Transcription error, not a misprint: the print's (7.4.3, (i)) is the statement used (A_p is a P-ring when the A'_{p'} have geometrically regular formal fibres)."))
f.append(F(199, "proof of (7.4.4) (i): 'démontré dans (0, 22.3.3 et 22.5.8)'", "bold 0", "plain 0", 'convention',
           r"(0, 22.3.3 et 22.5.8)", r"(\textbf{0}, 22.3.3 et 22.5.8)", conv=2))

# ---------------- checks ----------------
CRLF = chr(13) + chr(10)
LF = chr(10)
ok = True
for i, x in enumerate(f):
    if x['fix'] is None:
        continue
    p = os.path.join(RUN, 'page_%03d.tex' % x['page'])
    t = open(p, encoding='utf-8', newline='').read().replace(CRLF, LF)
    c = t.count(x['fix']['old'])
    if c != 1:
        ok = False
        print('COUNT', c, 'page', x['page'], repr(x['fix']['old']))
    if x['fix']['old'] == x['fix']['new']:
        ok = False
        print('NOOP', x['page'], x['fix']['old'])
print('all unique' if ok else 'PROBLEMS')

# overlap check per page: fixes whose old strings overlap in the page text
for pg in sorted(set(x['page'] for x in f)):
    t = open(os.path.join(RUN, 'page_%03d.tex' % pg), encoding='utf-8', newline='').read().replace(CRLF, LF)
    spans = []
    for x in f:
        if x['page'] != pg or x['fix'] is None:
            continue
        s = t.find(x['fix']['old'])
        spans.append((s, s + len(x['fix']['old']), x['where'][:50]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            print('OVERLAP p', pg, a[2], '|', b[2])

json.dump(f, open(OUT, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in f:
    k = 'convention' if x['kind'] == 'convention' else ('misprint' if x['kind'] == 'misprint_in_print' else 'normal')
    cnt[(x['page'], k)] += 1
for pg in range(195, 200):
    print(pg, cnt[(pg, 'normal')], cnt[(pg, 'convention')], cnt[(pg, 'misprint')])
print('total', len(f))
