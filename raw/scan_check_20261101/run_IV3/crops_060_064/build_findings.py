import json, sys

BASE = 'user/Documents/ega_scan_check_20261101/run_IV3/'
OUT = BASE + 'findings_060_064.json'
NL = '<NL>'

def T(s):
    return None if s is None else s.replace(NL, '\n')

F = []
def add(page, where, scan, tex, kind, conv, conf, old=None, new=None, corrected=None, note=''):
    d = {'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind,
         'convention': conv, 'confidence': conf,
         'fix': None if old is None else {'old': T(old), 'new': T(new)}}
    if kind == 'misprint_in_print':
        d['corrected'] = T(corrected)
    d['note'] = note
    F.append(d)

K1 = ('The TeX has bold upright \\mathbf{k}; outside subscripts the print sets the residue-field k bold italic. '
      'The subscript k of V^n_{k(eta)}, V^n_{k(s)} and of the tensor signs is bold upright in the print and stays \\mathbf{k} (GLOBAL_ISSUES 48).')
Q = ('The property letter Q is bold italic in the print, like the P of convention 10; the TeX has bold upright \\mathbf Q '
     '(6 times on this page, all in 9.3.5-9.3.6).')

# ---------------- outside the batch: end of the p. 59 segment ----------------
add(59, 'end of the p. 59 segment / top of p. 60: "... un recouvrement fini (U_j) de X par des | ouverts affines partout denses"',
    'p. 60 begins mid-sentence ("ouverts affines partout denses"); no paragraph break',
    'blank line between "des" and \\oldpage[IV-3]{60}: a paragraph break mid-sentence',
    'marker', None, 'high', r'de $X$ par<NL>des<NL><NL>', r'de $X$ par<NL>des<NL>',
    note='OUTSIDE pp. 60-64: old lies at the end of page_059.tex (ega4-9-fr.tex, blank line 405). There is no blank line after the p. 60 marker, so this edit completes the repair (GLOBAL_ISSUES 20). The pp. 55-59 batch may file the same edit; apply it once.')

# ---------------- page 60 ----------------
P = 60
add(P, 'l. 4: "et un k(eta)-morphisme fini surjectif h"', 'bold italic k (crop p60_s1_keta.png)', '$\\mathbf{k}(\\eta)$ (bold upright)',
    'convention', 1, 'high', r'$\mathbf{k}(\eta)$-morphisme', r'$\boldsymbol{k}(\eta)$-morphisme', note=K1)
add(P, 'l. 4: "(=Spec(k(eta)[T_1, ..., T_n]))"', 'bold italic k inside Spec(...) (crop p60_s1_keta.png)', '\\operatorname{Spec}(\\mathbf{k}(\\eta)[...]) (bold upright)',
    'convention', 1, 'high', r'\operatorname{Spec}(\mathbf{k}(\eta)[T_1', r'\operatorname{Spec}(\boldsymbol{k}(\eta)[T_1', note=K1)
add(P, 'Proposition (9.3.1): "Soit P(X, k) une propriété"', 'bold italic P', '\\mathbf P',
    'convention', 10, 'high', r'$\mathbf P(X,k)$', r'$\boldsymbol{P}(X,k)$')
add(P, 'Proposition (9.3.1), l. 1: "constructible (resp. ind-constructible) de préschémas"',
    '"(resp." and the closing parenthesis upright, "ind-constructible" italic (crop p60_s2_resp1.png)', 'all italic (proposition environment)',
    'convention', 6, 'high', r'(resp. ind-constructible)<NL>de', r'\textup{(resp.} ind-constructible\textup{)}<NL>de')
add(P, 'Proposition (9.3.1): "Désignons par P\'(f, X, Y, k)"', 'bold italic P', '\\mathbf P\'',
    'convention', 10, 'high', r"$\mathbf P'(f,X,Y,k)$", r"$\boldsymbol{P}'(f,X,Y,k)$")
add(P, 'Proposition (9.3.1): "on ait la propriété P(f^{-1}(y), k(y))"', 'bold italic P', '\\mathbf P',
    'convention', 10, 'high', r'$\mathbf P(f^{-1}(y)', r'$\boldsymbol{P}(f^{-1}(y)')
add(P, 'Proposition (9.3.1): same formula, "k(y)"', 'bold italic k', 'plain k',
    'convention', 1, 'high', r',k(y))$', r',\boldsymbol{k}(y))$')
add(P, 'Proposition (9.3.1): "Alors P\' est une propriété"', 'bold italic P', '\\mathbf P\'',
    'convention', 10, 'high', r"Alors $\mathbf P'$ est", r"Alors $\boldsymbol{P}'$ est")
add(P, 'Proposition (9.3.1), last line: "constructible (resp. ind-constructible)."',
    '"(resp." and the closing parenthesis upright, "ind-constructible" italic (crop p60_s2_resp2.png)', 'all italic (proposition environment)',
    'convention', 6, 'high', r'(resp. ind-constructible).', r'\textup{(resp.} ind-constructible\textup{)}.')
add(P, 'proof of (9.3.1): "comme P vérifie la condition"', 'bold italic P', '\\mathbf P',
    'convention', 10, 'high', r'comme $\mathbf P$ vérifie', r'comme $\boldsymbol{P}$ vérifie')
add(P, 'proof of (9.3.1): "il en est de même de P\' en vertu"', 'bold italic P', '\\mathbf P\'',
    'convention', 10, 'high', r"de $\mathbf P'$ en vertu", r"de $\boldsymbol{P}'$ en vertu")
add(P, 'proof of (9.3.1): "transitivité des fibres (I, 3.6.4)"', 'bold I in the reference', '(I, 3.6.4): plain I',
    'convention', 2, 'high', r'(I, 3.6.4)', r'(\textbf{I}, 3.6.4)')
add(P, 'proof of (9.3.1): "le fait que P\' vérifie la condition"', 'bold italic P', '\\mathbf P\'',
    'convention', 10, 'high', r"que $\mathbf P'$ vérifie", r"que $\boldsymbol{P}'$ vérifie")
add(P, 'Proposition (9.3.2): "Désignons par P une des propriétés"', 'bold italic P', '\\mathbf P',
    'convention', 10, 'high', r'par $\mathbf P$ une des', r'par $\boldsymbol{P}$ une des')
add(P, 'Proposition (9.3.2), item label (i)', '"(i)" upright (crop p60_s2_labels.png)', 'enumerate label=(\\roman*) inside the italic proposition: italic',
    'convention', 6, 'high', r'[label=(\roman*)]', r'[label=\textup{(\roman*)}]',
    note='One edit sets all four labels (i)-(iv) upright (GLOBAL_ISSUES 16; same form as the (8.5.8) enumerate in ega4-8-fr.tex).')
for lab in ('(ii)', '(iii)', '(iv)'):
    add(P, 'Proposition (9.3.2), item label ' + lab, '"' + lab + '" upright', 'italic (enumerate label inside the italic proposition)',
        'convention', 6, 'high', note='Included in the label edit of the (i) entry.')
add(P, 'Proposition (9.3.2) (iv): "appartient à Phi (notation de (9.2.6))"', 'the reference (9.2.6) upright inside the italic statement (crop p60_s3_iv_zoom.png)',
    '(9.2.6) italic (proposition environment)', 'convention', 6, 'high', r'de (9.2.6)).', r'de \textup{(9.2.6)}).')
add(P, 'Proposition (9.3.2): "Alors P est constructible."', 'bold italic P', '\\mathbf P',
    'convention', 10, 'high', r'Alors $\mathbf P$ est constructible', r'Alors $\boldsymbol{P}$ est constructible')
add(P, 'proof of (9.3.2): "de ce que f est de type fini (1.5.4, (v)) de la caractérisation des morphismes radiciels"',
    '"(1.5.4, (v)) de la": no comma after "(v))" (crop p60_s3_154v.png)', '"(1.5.4, (v)), de la": the TeX silently corrects',
    'misprint_in_print', None, 'high', r'(1.5.4, (v)), de', r'(1.5.4, (v)) de', corrected=r'(1.5.4, (v)), de',
    note='The sentence lists three things (de ce que f est de type fini ..., de la caractérisation ..., et de celle ...); the print omits the comma after the first. The diplomatic text takes the printed reading.')
add(P, 'proof of (9.3.2): "morphismes radiciels (I, 3.5.8)"', 'bold I in the reference', '(I, 3.5.8): plain I',
    'convention', 2, 'high', r'(I, 3.5.8)', r'(\textbf{I}, 3.5.8)')
add(P, 'proof of (9.3.2): "morphismes quasi-finis (II, 6.2.2)"', 'bold II in the reference', '(II, 6.2.2): plain II',
    'convention', 2, 'high', r'(II, 6.2.2)', r'(\textbf{II}, 6.2.2)')
add(P, 'Proposition (9.3.3): "les hypothèses de (8.8.1) dont nous gardons"', 'the reference (8.8.1) upright inside the italic statement',
    '(8.8.1) italic (proposition environment)', 'convention', 6, 'high', r'de (8.8.1) dont', r'de \textup{(8.8.1)} dont')
add(P, 'Proposition (9.3.3): "Soit P une propriété ind-constructible"', 'bold italic P', '\\mathbf P',
    'convention', 10, 'high', r'Soit $\mathbf P$ une', r'Soit $\boldsymbol{P}$ une')
add(P, 'Proposition (9.3.3): "Pour tout s in S (resp. s_lambda in S_lambda) posons"', '"(resp." and the closing parenthesis upright (crop p60_s3_resp33.png)',
    'italic (proposition environment)', 'convention', 6, 'high',
    r'(resp. $s_\lambda\in S_\lambda$) posons', r'\textup{(resp.} $s_\lambda\in S_\lambda$\textup{)} posons')
add(P, 'Proposition (9.3.3): "X_s=X x_S Spec(k(s))"', 'bold italic k (crop p60_s3_Ys.png)', 'plain k',
    'convention', 1, 'high', r'X\times_S\operatorname{Spec}(k(s))', r'X\times_S\operatorname{Spec}(\boldsymbol{k}(s))')
add(P, 'Proposition (9.3.3): "Y_s=Y x_S (Spec(k(s)))"', 'Y_s=Y x_S(Spec(k(s))): Spec(...) inside an extra pair of parentheses (crop p60_s3_Ys.png); X_s just before has none',
    'Y\\times_S\\operatorname{Spec}(k(s)) (no extra parentheses)', 'formula', None, 'high',
    r'Y\times_S\operatorname{Spec}(k(s))', r'Y\times_S(\operatorname{Spec}(\boldsymbol{k}(s)))',
    note='Redundant but harmless parentheses: a reading of the print, not an error, so the edit applies to both editions. The edit also sets the bold italic k of this k(s) (convention 1, next entry).')
add(P, 'Proposition (9.3.3): same formula, "k(s)"', 'bold italic k', 'plain k', 'convention', 1, 'high',
    note='Included in the formula edit of the previous entry.')
add(P, 'Proposition (9.3.3): "f_s=f x 1 : X_s -> Y_s (resp. X_{lambda,s_lambda}=..."', '"(resp." upright (crop p60_s3_resp33b.png)',
    'italic (proposition environment)', 'convention', 6, 'high',
    r'$f_s=f\times1:X_s\to Y_s$ (resp.', r'$f_s=f\times1:X_s\to Y_s$ \textup{(resp.}',
    note='The closing parenthesis of this "resp." clause is the next-but-two entry.')
add(P, 'Proposition (9.3.3): "X_{lambda,s_lambda}=X_lambda x_{S_lambda} Spec(k(s_lambda))"', 'bold italic k (crop p60_s3_resp33b.png)', 'plain k',
    'convention', 1, 'high', r'X_\lambda\times_{S_\lambda}<NL>\operatorname{Spec}(k(s_\lambda))', r'X_\lambda\times_{S_\lambda}<NL>\operatorname{Spec}(\boldsymbol{k}(s_\lambda))')
add(P, 'Proposition (9.3.3): "Y_{lambda,s_lambda}=Y_lambda x_{S_lambda} Spec(k(s_lambda))"', 'bold italic k', 'plain k',
    'convention', 1, 'high', r'Y_\lambda\times_{S_\lambda}<NL>\operatorname{Spec}(k(s_\lambda))', r'Y_\lambda\times_{S_\lambda}<NL>\operatorname{Spec}(\boldsymbol{k}(s_\lambda))')
add(P, 'Proposition (9.3.3): "-> Y_{lambda,s_lambda}). Alors, afin que"', 'closing parenthesis of the "resp." clause upright (crop p60_s3_close.png)',
    'italic (proposition environment)', 'convention', 6, 'high',
    r'Y_{\lambda,s_\lambda}$). Alors', r'Y_{\lambda,s_\lambda}$\textup{)}. Alors')
add(P, 'Proposition (9.3.3): "on ait la propriété P(f_s), il faut"', 'bold italic P', '\\mathbf P',
    'convention', 10, 'high', r'$\mathbf P(f_s)$, il', r'$\boldsymbol{P}(f_s)$, il')
add(P, 'Proposition (9.3.3): "on ait P(f_{lambda,s_lambda})."', 'bold italic P', '\\mathbf P',
    'convention', 10, 'high', r'on ait $\mathbf P(f_{\lambda,s_\lambda})$', r'on ait $\boldsymbol{P}(f_{\lambda,s_\lambda})$')
add(P, 'proof of (9.3.3): "tels que la propriété P(f_s) (resp."', 'bold italic P', '\\mathbf P',
    'convention', 10, 'high', r'$\mathbf P(f_s)$ (resp.', r'$\boldsymbol{P}(f_s)$ (resp.')
add(P, 'proof of (9.3.3): "P(f_{lambda,s_lambda})) soit vraie"', 'bold italic P', '\\mathbf P',
    'convention', 10, 'high', r'$\mathbf P(f_{\lambda,s_\lambda})$) soit', r'$\boldsymbol{P}(f_{\lambda,s_\lambda})$) soit')

# ---------------- page 61 ----------------
P = 61
add(P, 'l. 1: "à des propriétés P du type considéré"', 'bold italic P', '\\mathbf P',
    'convention', 10, 'high', r'propriétés $\mathbf P$ du type', r'propriétés $\boldsymbol{P}$ du type')
add(P, 'Proposition (9.3.5): "Soit P(X, Y, k) la propriété"', 'bold italic P', '\\mathbf P',
    'convention', 10, 'high', r'$\mathbf P(X,Y,k)$', r'$\boldsymbol{P}(X,Y,k)$')
add(P, 'Proposition (9.3.5): "vérifiant Q(g) »"', 'bold italic Q (crop p61_s1_ou.png)', '\\mathbf Q (bold upright)',
    'font', None, 'high', r'vérifiant $\mathbf Q(g)$', r'vérifiant $\boldsymbol{Q}(g)$', note=Q)
add(P, 'Proposition (9.3.5): "vérifiant Q(g) », ou Q est une des propriétés"', '"ou" without the grave accent (crop p61_s1_ou.png)',
    '"où": the TeX silently corrects', 'misprint_in_print', None, 'high', r'~», où', r'~», ou', corrected=r'~», où',
    note='Relative "où" printed as "ou". The diplomatic text takes the printed reading.')
add(P, 'Proposition (9.3.5): "ou Q est une des propriétés"', 'bold italic Q', '\\mathbf Q (bold upright)',
    'font', None, 'high', r'$\mathbf Q$ est une des', r'$\boldsymbol{Q}$ est une des', note=Q)
add(P, 'Proposition (9.3.5): "une des propriétés (i) à (xiv) de (8.10.5)": (i)', '"(i)" upright inside the italic statement; "à", "de" italic (crop p61_s1_ou.png)',
    'italic (proposition environment)', 'convention', 6, 'high',
    r'(i) à (xiv) de (8.10.5)', r'\textup{(i)} à \textup{(xiv)} de \textup{(8.10.5)}',
    note='One edit for the three upright references (i), (xiv), (8.10.5).')
add(P, 'Proposition (9.3.5): same place, (xiv)', '"(xiv)" upright', 'italic', 'convention', 6, 'high',
    note='Included in the edit of the previous entry.')
add(P, 'Proposition (9.3.5): same place, (8.10.5)', '"(8.10.5)" upright', 'italic', 'convention', 6, 'high',
    note='Included in the edit of the (i) entry.')
add(P, 'Proposition (9.3.5): "Alors P est une propriété ind-constructible"', 'bold italic P', '\\mathbf P',
    'convention', 10, 'high', r'Alors $\mathbf P$', r'Alors $\boldsymbol{P}$')
add(P, 'proof of (9.3.5): "La définition de P montre"', 'bold italic P', '\\mathbf P',
    'convention', 10, 'high', r'définition de $\mathbf P$', r'définition de $\boldsymbol{P}$')
add(P, 'proof of (9.3.5): "la propriété Q(g) est stable"', 'bold italic Q', '\\mathbf Q (bold upright)',
    'font', None, 'high', r'$\mathbf Q(g)$ est stable', r'$\boldsymbol{Q}(g)$ est stable', note=Q)
add(P, 'proof of (9.3.5): "si K=k(eta), corps des fractions de A"', 'bold italic k', '\\mathbf{k} (bold upright)',
    'convention', 1, 'high', r'$K=\mathbf{k}(\eta)$', r'$K=\boldsymbol{k}(\eta)$', note=K1)
add(P, 'proof of (9.3.5): "une extension finie K\' de K"', '"finie" italic (crop p61_s2_finie.png)', 'upright',
    'italics', None, 'high', r"extension finie $K'$", r"extension \emph{finie} $K'$")
add(P, 'proof of (9.3.5): "vérifiant Q(g\')"', 'bold italic Q', '\\mathbf Q (bold upright)',
    'font', None, 'high', r"$\mathbf Q(g')$", r"$\boldsymbol{Q}(g')$", note=Q)
add(P, 'proof of (9.3.5): "d\'une A-algèbre intègre finie A\'"', '"finie" italic (crop p61_s2_finie.png)', 'upright',
    'italics', None, 'high', r"intègre finie $A'$", r"intègre \emph{finie} $A'$")
add(P, 'proof of (9.3.5): "ayant la propriété Q. Mais"', 'bold italic Q', '\\mathbf Q (bold upright)',
    'font', None, 'high', r'propriété $\mathbf Q$. Mais', r'propriété $\boldsymbol{Q}$. Mais', note=Q)
add(P, 'proof of (9.3.5): "X\'_{s\'}=X_s (x)_{k(s)} k(s\')"', 'bold italic k in k(s\'); the subscript k(s) bold upright (crop p61_s2_ks.png)',
    '\\mathbf{k}(s\') (bold upright)', 'convention', 1, 'high',
    r"X_s\otimes_{\mathbf{k}(s)}\mathbf{k}(s')", r"X_s\otimes_{\mathbf{k}(s)}\boldsymbol{k}(s')", note=K1)
add(P, 'proof of (9.3.5): "Y\'_{s\'}=Y_s (x)_{k(s)} k(s\')"', 'bold italic k in k(s\'); the subscript k(s) bold upright', '\\mathbf{k}(s\') (bold upright)',
    'convention', 1, 'high', r"Y_s\otimes_{\mathbf{k}(s)}\mathbf{k}(s')", r"Y_s\otimes_{\mathbf{k}(s)}\boldsymbol{k}(s')", note=K1)
add(P, 'proof of (9.3.5): "la propriété P(X_s, Y_s, k(s))"', 'bold italic P', '\\mathbf P',
    'convention', 10, 'high', r'$\mathbf P(X_s,', r'$\boldsymbol{P}(X_s,')
add(P, 'proof of (9.3.5): same formula, "k(s)"', 'bold italic k (crop p61_s2_ks.png)', '\\mathbf{k} (bold upright)',
    'convention', 1, 'high', r'Y_s,\mathbf{k}(s))', r'Y_s,\boldsymbol{k}(s))', note=K1)
add(P, 'proof of (9.3.5): "la propriété P(X_s, Y_s, k(s)), est vraie pour tout s in U"', 'a comma after the closing parenthesis, before "est vraie" (crop p61_s2_ks.png)',
    'no comma: the TeX silently corrects', 'misprint_in_print', None, 'high',
    r'$ est vraie pour tout', r'$, est vraie pour tout', corrected=r'$ est vraie pour tout',
    note='A comma between subject and verb. The edit does not overlap the P and k edits of the same formula. The diplomatic text takes the printed comma.')
add(P, 'Exemple (9.3.6): "Prenons par exemple pour Q la propriété"', 'bold italic Q', '\\mathbf Q (bold upright)',
    'font', None, 'high', r'pour $\mathbf Q$ la', r'pour $\boldsymbol{Q}$ la', note=Q)
add(P, 'Exemple (9.3.6): "X_s et Y_s soient géométriquement isomorphes (9.1.4)"', '"géométriquement isomorphes" italic', 'upright (env body is roman)',
    'italics', None, 'high', r'soient<NL>géométriquement isomorphes (9.1.4)', r'soient<NL>\emph{géométriquement isomorphes} (9.1.4)',
    note='The second "géométriquement isomorphes" at the end of the example is roman in the print, as in the TeX.')
add(P, 'paragraph after (9.3.6): "des isomorphismes de préschémas qui sont des homomorphismes pour les lois"', '"homomorphismes" italic', 'upright',
    'italics', None, 'high', r'qui sont des homomorphismes', r'qui sont des \emph{homomorphismes}')

# ---------------- page 62 ----------------
P = 62
add(P, 'Notations (9.4.1): "X_s=f^{-1}(s)=X x_S Spec(k(s))"', 'bold italic k (crop p62_s1_ks.png)', '\\mathbf{k} (bold upright)',
    'convention', 1, 'high', r'\operatorname{Spec}(\mathbf{k}(s))', r'\operatorname{Spec}(\boldsymbol{k}(s))', note=K1)
add(P, 'Notations (9.4.1): "le O_{X_s}-Module F (x)_{O_S} k(s)"', 'bold italic k (crop p62_s1_ks.png)', '\\mathbf{k} (bold upright)',
    'convention', 1, 'high', r'\otimes_{\mathcal O_S}\mathbf{k}(s)', r'\otimes_{\mathcal O_S}\boldsymbol{k}(s)', note=K1)
add(P, 'proof of (9.4.2): "il s\'agit ici de la relation P(X, F, G, H, u, v, k)"', 'bold italic P', '\\mathbf P',
    'convention', 10, 'high', r'$\mathbf P(X,\mathcal F', r'$\boldsymbol{P}(X,\mathcal F')
add(P, 'proof of (9.4.2): "en vertu de (8.5.8, (i)) appliqué suivant la méthode générale"', '(8.5.8, (i)) (crop p62_s3_858.png)', '(8.5.8, (ii))',
    'number', None, 'high', r'(8.5.8, (ii))', r'(8.5.8, (i))',
    note='Transcription error, not a misprint: (8.5.8) (i) is the exactness criterion for a sequence F->G->H (ega4-8-fr.tex), which is what is used here; (ii) is about injectivity. The fix applies to both editions.')
add(P, 'proof of (9.4.2): "dans le cas particulier où la suite 0 -> F -u-> G -v-> H -> 0 est exacte"',
    'the formula is in the running text (start of a line, followed by "est exacte. Or, il y a alors") (crop p62_s3_seq.png)', 'set as a display \\[ ... \\]',
    'other', None, 'high', r'\[<NL>0\to\mathcal F\xrightarrow{u}\mathcal G\xrightarrow{v}\mathcal H\to0<NL>\]',
    r'$0\to\mathcal F\xrightarrow{u}\mathcal G\xrightarrow{v}\mathcal H\to0$',
    note='Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting words lost.')

# ---------------- page 63 ----------------
P = 63
add(P, 'proof of (9.4.3): "de degrés -1, 0, +1 : M -u-> N -v-> P et à i=0"', 'the formula is in the running text (start of the second line, followed by "et à i=0;")',
    'set as a display \\[ ... \\]', 'other', None, 'high',
    r'\[<NL>\mathcal M\xrightarrow{u}\mathcal N\xrightarrow{v}\mathcal P<NL>\]',
    r'$\mathcal M\xrightarrow{u}\mathcal N\xrightarrow{v}\mathcal P$',
    note='Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting words lost.')
add(P, 'proof of (9.4.3): "appliqué à la suite exacte 0 -> Im(u) -> Ker(v) -> Ker(v)/Im(u) -> 0, compte tenu"',
    'the formula is in the running text (same line as "suite exacte" and "compte tenu de ce que")', 'set as a display \\[ ... \\] with the comma inside',
    'other', None, 'high',
    r'\[<NL>0\to\operatorname{Im}(u)\to\operatorname{Ker}(v)\to<NL>\operatorname{Ker}(v)/\operatorname{Im}(u)\to0,<NL>\]',
    r'$0\to\operatorname{Im}(u)\to\operatorname{Ker}(v)\to<NL>\operatorname{Ker}(v)/\operatorname{Im}(u)\to0$,',
    note='Formula displayed where the print has it inline (GLOBAL_ISSUES 21). The next sequence, 0 -> (Im u)_eta -> ..., is displayed in the print too and stays.')
add(P, 'proof of (9.4.3): "compte tenu de ce que O_eta=k(eta)"', 'bold italic k', 'plain k',
    'convention', 1, 'high', r'$\mathcal O_\eta=k(\eta)$', r'$\mathcal O_\eta=\boldsymbol{k}(\eta)$')
add(P, 'proof of (9.4.4): "il faut établir que la propriété P considérée dans (9.4.2)"', 'bold italic P', '\\mathbf P',
    'convention', 10, 'high', r'$\mathbf P$ considérée', r'$\boldsymbol{P}$ considérée')
add(P, 'proof of (9.4.4): "Supposons donc S intègre noethérien, de point générique"', '"noethérien" italic (crop p63_s2_noeth.png)', 'upright',
    'italics', None, 'high', r'intègre<NL>noethérien, de point', r'intègre<NL>\emph{noethérien}, de point')
add(P, 'proof of (9.4.4): "prouvons que E ou S-E est un voisinage de eta"', 'long dash for set difference', '$S-E$',
    'convention', 7, 'high', r'ou $S-E$ est', r'ou $S\setmin E$ est')
add(P, 'proof of (9.4.4), 1°: "un voisinage U de eta dans S tel que, pour s in S, Ker(w_s)=N_s"', 'pour s in S (crop p63_s3_SinS.png)',
    '"tel que, pour $s\\in S$," (the TeX keeps the printed reading)', 'misprint_in_print', None, 'medium',
    corrected=r'tel que, pour $s\in U$,',
    note='The relation holds on the neighbourhood U just found ("en restreignant S" then shrinks S to it), so the reading is s in U. Diplomatic TeX already right; in the corrected edition replace "tel que, pour $s\\in S$," (once on the page) by the corrected reading.')
add(P, 'proof of (9.4.4), 1°: "l\'exactitude à droite du foncteur F ~> F_s"', 'wavy arrow (crop p63_s3_Ms.png)', '\\mapsto',
    'symbol', None, 'high', r'\mathcal F\mapsto\mathcal F_s', r'\mathcal F\leadsto\mathcal F_s',
    note='Wavy arrow, as elsewhere in IV-3 (GLOBAL_ISSUES 33).')
MNOTE = ('Wrong font in the print: roman M for the script M just defined by "posons M=Coker(j)" (script there). '
         'The edition writes the print\'s upright capitals as plain math letters, so the diplomatic text takes $M$. The TeX silently corrects.')
add(P, 'proof of (9.4.4), 1°: "entraîne que M_s=Coker(j_s) pour tout s in S"', 'roman (upright) M, not script (crop p63_s3_Ms.png)',
    '\\mathcal M_s: the TeX silently corrects', 'misprint_in_print', None, 'high',
    r'$\mathcal M_s=\operatorname{Coker}(j_s)$', r'$M_s=\operatorname{Coker}(j_s)$', corrected=r'$\mathcal M_s=\operatorname{Coker}(j_s)$', note=MNOTE)
add(P, 'proof of (9.4.4), 1°: "signifie que M_eta =/= 0"', 'roman M (crop p63_s3_Meta.png)', '\\mathcal M_\\eta: the TeX silently corrects',
    'misprint_in_print', None, 'high', r'$\mathcal M_\eta\neq0$', r'$M_\eta\neq0$', corrected=r'$\mathcal M_\eta\neq0$', note=MNOTE)
add(P, 'proof of (9.4.4), 1°: "comme M est cohérent (0_I, 5.3.4)"', 'roman M (crop p63_s3_Meta.png)', '\\mathcal M: the TeX silently corrects',
    'misprint_in_print', None, 'high', r'comme $\mathcal M$ est', r'comme $M$ est', corrected=r'comme $\mathcal M$ est', note=MNOTE)
add(P, 'proof of (9.4.4), 1°: "tel que M_s =/= 0 pour s in U"', 'roman M (crop p63_s3_Meta.png)', '\\mathcal M_s: the TeX silently corrects',
    'misprint_in_print', None, 'high', r'$\mathcal M_s\neq0$', r'$M_s\neq0$', corrected=r'$\mathcal M_s\neq0$', note=MNOTE)
add(P, 'proof of (9.4.4), 1°: "et a fortiori S-E est un voisinage de eta"', 'long dash for set difference', '$S-E$',
    'convention', 7, 'high', r'fortiori} $S-E$', r'fortiori} $S\setmin E$')
add(P, 'proof of (9.4.4), 2°: "et H^0(L) est cohérent (0_I, 5.3.4 et 5.3.3)"', 'H^0(L) without the raised bullet (crop p63_s4_H0L.png)',
    '\\mathcal H^0(\\mathcal L) (the TeX keeps the printed reading)', 'misprint_in_print', None, 'medium',
    corrected=r'\mathcal H^0(\mathcal L^\bullet)',
    note='Everywhere else in the passage the complex is L^.; the bullet is missing here. Diplomatic TeX already right; in the corrected edition replace "$\\mathcal H^0(\\mathcal L)$ est cohérent" (once on the page).')
add(P, 'proof of (9.4.4), 2°: "on voit de nouveau que S-E est un voisinage"', 'long dash for set difference', '$S-E$',
    'convention', 7, 'high', r'nouveau que $S-E$', r'nouveau que $S\setmin E$')

# ---------------- page 64 ----------------
P = 64
add(P, 'Corollaire (9.4.5): "soit injectif (resp. surjectif, bijectif, nul)"', '"resp." upright inside the italic statement (crop p64_s1_resp.png)',
    '\\textnormal{(}resp. ...: "resp." italic', 'convention', 6, 'high', r'\textnormal{(}resp. surjectif', r'\textnormal{(resp.} surjectif')
add(P, 'Proposition (9.4.7): "L\'ensemble E (resp. E\')"', '"resp." upright (crop p64_s2_resp.png)', '\\textnormal{(}resp. $E\'$: "resp." italic',
    'convention', 6, 'high', r"\textnormal{(}resp. $E'$", r"\textnormal{(resp.} $E'$")
add(P, 'Proposition (9.4.7): "localement libre (resp. localement libre de rang n)"', '"resp." upright (crop p64_s2_resp.png)', '"resp." italic',
    'convention', 6, 'high', r'\textnormal{(}resp.<NL>localement', r'\textnormal{(resp.}<NL>localement')
add(P, 'proof of (9.4.7), 1°: "appliqué suivant la méthode générale de (8.1.2, a)) qu\'il existe"',
    'no comma after "a))" (end of line; next line begins "qu\'il existe") (crop p64_s3_a.png)', '"a)}), qu\'il": the TeX silently corrects',
    'misprint_in_print', None, 'high', r'générale de (8.1.2, \emph{a)}), qu' + "'" + 'il', r'générale de (8.1.2, \emph{a)}) qu' + "'" + 'il',
    corrected=r'générale de (8.1.2, \emph{a)}), qu' + "'" + 'il',
    note='The incise opened by the comma after (8.5.5) is not closed in the print; the same construction later on this page and on p. 63 has the comma. The diplomatic text takes the printed reading.')
add(P, 'proof of (9.4.7), 3°: "eta in S-E"', 'long dash for set difference', '$\\eta\\in S-E$',
    'convention', 7, 'high', r'\eta\in S-E', r'\eta\in S\setmin E')
add(P, 'proof of (9.4.7), 3°: "équivaut à dire qu\'il n\'est pas plat sur O_{X_eta}"', '"n\'est pas plat sur" all italic (crop p64_s3_plat.png)',
    '\\emph{n\'est pas plat} sur: "sur" upright', 'italics', None, 'high', r"\emph{n'est pas plat} sur", r"\emph{n'est pas plat sur}")
add(P, 'proof of (9.4.7), 3°: "Le fait que S-E est un voisinage de eta"', 'long dash for set difference', '$S-E$',
    'convention', 7, 'high', r'fait que $S-E$', r'fait que $S\setmin E$')
add(P, 'proof of (9.4.7.1): "Bourbaki, Alg. comm., chap. Ier, § 2, n° 3, Remarque 1"', '"Remarque" italic, "1" roman (crop p64_s4_rem.png)', 'Remarque~1 upright',
    'italics', None, 'high', r'Remarque~1', r'\emph{Remarque}~1')

# ---------------- validation ----------------
texts = {}
def page_text(p):
    if p not in texts:
        texts[p] = open(BASE + 'page_%03d.tex' % p, encoding='utf-8').read().replace('\r\n', '\n')
    return texts[p]

ok = True
for x in F:
    fx = x['fix']
    if fx is None:
        continue
    n = page_text(x['page']).count(fx['old'])
    if n != 1:
        ok = False
        print('NOT UNIQUE', x['page'], n, repr(fx['old']))
# sequential application per page, in listed order (diplomatic edition: all fixes)
cur = {p: page_text(p) for p in texts}
for x in F:
    fx = x['fix']
    if fx is None:
        continue
    t = cur[x['page']]
    n = t.count(fx['old'])
    if n != 1:
        ok = False
        print('SEQ FAIL', x['page'], n, repr(fx['old']))
        continue
    cur[x['page']] = t.replace(fx['old'], fx['new'], 1)
# corrected edition: skip misprint fixes
cur2 = {p: page_text(p) for p in texts}
for x in F:
    fx = x['fix']
    if fx is None or x['kind'] == 'misprint_in_print':
        continue
    t = cur2[x['page']]
    if t.count(fx['old']) != 1:
        ok = False
        print('SEQ2 FAIL', x['page'], repr(fx['old']))
        continue
    cur2[x['page']] = t.replace(fx['old'], fx['new'], 1)
for x in F:
    if x['kind'] == 'misprint_in_print' and not x.get('corrected'):
        ok = False
        print('MISSING corrected', x['page'], x['where'])

from collections import Counter
c = Counter()
for x in F:
    k = 'misprint' if x['kind'] == 'misprint_in_print' else ('convention' if x['kind'] == 'convention' else 'normal')
    c[(x['page'], k)] += 1
for p in sorted(set(x['page'] for x in F)):
    print(p, c[(p, 'normal')], c[(p, 'convention')], c[(p, 'misprint')])
print('total', len(F), 'ok', ok)
if ok:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    print('written', OUT)
