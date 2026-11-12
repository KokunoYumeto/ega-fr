import json
import os
import sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, 'findings_187_191.json')
NL = '<NL>'


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {
        'page': page,
        'where': where,
        'scan': scan,
        'tex': tex,
        'kind': kind,
        'convention': conv,
        'confidence': conf,
    }
    if old is None:
        d['fix'] = None
    else:
        d['fix'] = {'old': old.replace(NL, '\n'), 'new': new.replace(NL, '\n')}
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    return d


L = []

# ---------------------------------------------------------------- page 187
L.append(F(187, "proof of (7.4.2): 'Si Z_{p+1}(P.)=Ker(P_{p+1}->P_p), on a'",
           "formula in the running text", "displayed", 'other', None, 'high',
           r"\[<NL>  Z_{p+1}(P_\bullet)=\operatorname{Ker}(P_{p+1}\longrightarrow P_p),<NL>\]",
           r"$Z_{p+1}(P_\bullet)=\operatorname{Ker}(P_{p+1}\longrightarrow P_p)$,",
           "Layout: the print sets this formula inline (GLOBAL_ISSUES 21/36); the formula itself matches."))
L.append(F(187, "proof of (7.4.2), display: 'P'_p=Z'_p(P.) et P'_{p+1}=Z_{p+1}(P.);'",
           "'P'_p=Z'_p(P.)   et   P'_{p+1}=Z_{p+1}(P.);' (no comma after Z'_p(P.))",
           "'P'_p=Z'_p(P_\\bullet),\\qquad P'_{p+1}=...' (comma, no 'et')", 'missing', None, 'high',
           r"P'_p=Z'_p(P_\bullet),<NL>  \qquad<NL>  P'_{p+1}",
           r"P'_p=Z'_p(P_\bullet)<NL>  \qquad\text{et}\qquad<NL>  P'_{p+1}",
           "The word 'et' between the last two equalities is missing in the TeX, which has a comma instead."))
L.append(F(187, "proof of (7.4.2): 'Z'_i(P.⊗M)=..., Z_i(P.⊗M)=Z_i(P.)⊗M et B_i(P.⊗M)=B_i(P.)⊗M'",
           "one display line, with 'et' inside the display", "two displays with 'et' in the running text between them",
           'other', None, 'high',
           r"Z_i(P_\bullet)\otimes M<NL>\]<NL>et<NL>\[<NL>  B_i(P_\bullet\otimes M)",
           r"Z_i(P_\bullet)\otimes M<NL>  \quad\text{et}\quad<NL>  B_i(P_\bullet\otimes M)",
           "Layout only: the print has the three equalities in a single display."))
L.append(F(187, "proof of (7.4.2): 'des isomorphismes fonctoriels H_i(P.⊗M) ⥲ H_i(P'.⊗M) pour tout i'",
           "formula in the running text", "displayed", 'other', None, 'high',
           r"\[<NL>  H_i(P_\bullet\otimes M)\xrightarrow{\sim}H_i(P'_\bullet\otimes M)<NL>\]",
           r"$H_i(P_\bullet\otimes M)\xrightarrow{\sim}H_i(P'_\bullet\otimes M)$",
           "Layout: the print sets this formula inline (GLOBAL_ISSUES 21/36); arrow and formula match."))
L.append(F(187, "proof of (7.4.2): 'Z_{p+1}(P.) est plat (0_I, 6.1.2)'",
           "bold 0", "plain 0", 'convention', 2, 'high',
           r"est plat ($0_{\mathrm I}$, 6.1.2)", r"est plat ($\mathbf{0}_{\mathrm I}$, 6.1.2)",
           "Bold chapter number (form of GLOBAL_ISSUES 35)."))
L.append(F(187, "after (7.4.2): 'impliquent aussi que B_p(P.) est plat, car'",
           "'plat' italic", "upright", 'italics', None, 'high',
           r"$B_p(P_\bullet)$ est plat, car", r"$B_p(P_\bullet)$ est \emph{plat}, car",
           "Italic in the print; upright in the TeX."))
L.append(F(187, "after (7.4.2): 'une suite exacte 0->B_p(P.)->P_p->Z'_p(P.)->0, dans laquelle'",
           "formula in the running text", "displayed", 'other', None, 'high',
           r"\[<NL>  0\longrightarrow B_p(P_\bullet)\longrightarrow P_p<NL>  \longrightarrow Z'_p(P_\bullet)\longrightarrow0,<NL>\]",
           r"$0\longrightarrow B_p(P_\bullet)\longrightarrow P_p<NL>\longrightarrow Z'_p(P_\bullet)\longrightarrow0$,",
           "Layout: the print sets this formula inline (GLOBAL_ISSUES 21/36)."))
L.append(F(187, "after (7.4.2): 'sont plats (0_I, 6.1.2)'",
           "bold 0", "plain 0", 'convention', 2, 'high',
           r"sont plats ($0_{\mathrm I}$, 6.1.2)", r"sont plats ($\mathbf{0}_{\mathrm I}$, 6.1.2)",
           "Bold chapter number."))
L.append(F(187, "Corollaire (7.4.3): '(autrement dit un produit d'anneaux de Dedekind (0_IV, 17.1.3 et 17.3.7), par exemple un anneau principal)'",
           "the parenthesis is roman inside the italic statement, with 'produit d'anneaux de Dedekind' and 'principal' italic",
           "all italic (statement environment)", 'convention', 6, 'high',
           r"(autrement dit un produit d'anneaux de Dedekind<NL>($0_{\mathrm{IV}}$, 17.1.3 et 17.3.7), par exemple un anneau principal)",
           r"\textup{(autrement dit un \emph{produit d'anneaux de Dedekind}<NL>($\mathbf{0}_{\mathrm{IV}}$, 17.1.3 et 17.3.7), par exemple un anneau \emph{principal})}",
           "Enlarged crop. The same edit sets the bold 0 of (0_IV, ...) (next finding, convention 2)."))
L.append(F(187, "Corollaire (7.4.3): '(0_IV, 17.1.3 et 17.3.7)'",
           "bold 0", "plain 0", 'convention', 2, 'high',
           None, None,
           "Covered by the edit of the preceding finding (convention 6), which writes $\\mathbf{0}_{\\mathrm{IV}}$."))
L.append(F(187, "proof of (7.4.3): 'il revient au même de dire que M est plat ou'",
           "'plat' italic", "upright", 'italics', None, 'high',
           r"$M$ est plat ou", r"$M$ est \emph{plat} ou",
           "Italic in the print; upright in the TeX."))
L.append(F(187, "proof of (7.4.3): 'ou qu'il est sans torsion'",
           "'sans torsion' italic", "upright", 'italics', None, 'high',
           r"est sans torsion", r"est \emph{sans torsion}",
           "Italic in the print; upright in the TeX."))
L.append(F(187, "proof of (7.4.3): '(0_I, 6.3.3 et 6.3.4)'",
           "bold 0", "plain 0", 'convention', 2, 'high',
           r"($0_{\mathrm I}$, 6.3.3", r"($\mathbf{0}_{\mathrm I}$, 6.3.3",
           "Bold chapter number."))
L.append(F(187, "proof of (7.4.3): 'B_{p-1}(P.) est un A-module plat, en tant que'",
           "'plat' italic", "upright", 'italics', None, 'high',
           r"est un $A$-module plat, en tant", r"est un $A$-module \emph{plat}, en tant",
           "Italic in the print; upright in the TeX."))
L.append(F(187, "proof of (7.4.3), end: '(0_I, 6.1.2)'",
           "bold 0", "plain 0", 'convention', 2, 'high',
           r"plat<NL>($0_{\mathrm I}$, 6.1.2)", r"plat<NL>($\mathbf{0}_{\mathrm I}$, 6.1.2)",
           "Bold chapter number."))
L.append(F(187, "Proposition (7.4.4): 'un complexe de A-modules plats : on suppose'",
           "colon 'plats :' (enlarged crop)", "semicolon 'plats;'", 'punctuation', None, 'high',
           r"$A$-modules plats;", r"$A$-modules plats :",
           ""))
L.append(F(187, "Proposition (7.4.4): 'défini par (7.4.1.1)'",
           "reference upright (roman figures) in the italic statement", "italic", 'convention', 6, 'high',
           r"par (7.4.1.1).", r"par \textup{(7.4.1.1)}.",
           "Enlarged crop."))
L.append(F(187, "Proposition (7.4.4): 'tels que (T_p)_y (7.1.4) soit exact'",
           "reference upright", "italic", 'convention', 6, 'high',
           r"$(T_p)_y$ (7.1.4)", r"$(T_p)_y$ \textup{(7.1.4)}",
           "Enlarged crop."))
L.append(F(187, "Proposition (7.4.4): '(resp. exact à gauche, exact)'",
           "'(resp.' and the parentheses roman, 'exact à gauche, exact' italic", "all italic", 'convention', 6, 'high',
           r"(resp. exact à gauche, exact)", r"\textup{(resp. \emph{exact à gauche, exact})}",
           "Enlarged crop; same form as the earlier (resp. ...) fixes."))

# ---------------------------------------------------------------- page 188
L.append(F(188, "proof of (7.4.4): 'à T.(M) (0, 11.9.3)'",
           "bold 0", "plain 0", 'convention', 2, 'high',
           r"(0, 11.9.3)", r"(\textbf{0}, 11.9.3)",
           "Bold chapter number."))
L.append(F(188, "proof of (7.4.4): '(cf. (7.4.2, a))). Cela étant'",
           "three closing parentheses after a (enlarged crop)", "'(cf. (7.4.2, $a)$).': one parenthesis short",
           'punctuation', None, 'high',
           r"(cf. (7.4.2, $a)$).", r"(cf. (7.4.2, $a)$)).",
           "The parenthesis closing '(cf.' is missing in the TeX."))
L.append(F(188, "proof of (7.4.4): 'comme le foncteur M⇝M_x est exact'",
           "wavy arrow (enlarged crop)", "\\mapsto", 'symbol', None, 'high',
           r"$M\mapsto M_x$", r"$M\leadsto M_x$",
           "Wavy arrow in the print (\\leadsto), not convention 3 (GLOBAL_ISSUES 33)."))
L.append(F(188, "proof of (7.4.4): 'on a (Z'_p(P.))_x=Z'_p((P.)_x), et'",
           "formula in the running text", "displayed", 'other', None, 'high',
           r"\[<NL>  (Z'_p(P_\bullet))_x=Z'_p((P_\bullet)_x),<NL>\]",
           r"$(Z'_p(P_\bullet))_x=Z'_p((P_\bullet)_x)$,",
           "Layout: the print sets this formula inline (GLOBAL_ISSUES 21/36)."))
L.append(F(188, "proof of (7.4.4): 'donc libre puisqu'il est de type fini'",
           "'libre' italic", "upright", 'italics', None, 'high',
           r"donc libre<NL>puisqu'il", r"donc \emph{libre}<NL>puisqu'il",
           "Italic in the print; upright in the TeX."))
L.append(F(188, "Corollaire (7.4.5): 'Sous les hypothèses de (7.4.4)'",
           "reference upright", "italic", 'convention', 6, 'high',
           r"Sous les hypothèses de (7.4.4), supposons", r"Sous les hypothèses de \textup{(7.4.4)}, supposons",
           "Enlarged crop."))
L.append(F(188, "proof of (7.4.5): 'pour le point générique x'",
           "'générique' italic", "upright", 'italics', None, 'high',
           r"point générique", r"point \emph{générique}",
           "Italic in the print; upright in the TeX."))
L.append(F(188, "proof of (7.4.5): 'tout foncteur additif sur Ab_{A_x}'",
           "Ab bold italic (enlarged crop)", "\\mathbf{Ab} (bold upright)", 'font', None, 'high',
           r"$\mathbf{Ab}_{A_x}$", r"$\boldsymbol{Ab}_{A_x}$",
           "In the running text the print's Ab is bold italic (also pp. 190, 191); inside the italic statements (7.5.2) and (7.5.4) it is bold upright, as the TeX."))
L.append(F(188, "Proposition (7.4.6): 'Sous les hypothèses générales de (7.4.4)'",
           "reference upright", "italic", 'convention', 6, 'high',
           r"générales de (7.4.4), les conditions", r"générales de \textup{(7.4.4)}, les conditions",
           "Enlarged crop."))
L.append(F(188, "Proposition (7.4.6): '... et c) de (7.4.2) sont aussi équivalentes à :'",
           "'de (7.4.2)' upright at the start of the second line (the 'de' of the first line is italic)", "italic",
           'convention', 6, 'high',
           r"$c)$ de<NL>(7.4.2) sont aussi", r"$c)$ \textup{de<NL>(7.4.2)} sont aussi",
           "Enlarged crop. The upright 'de' is probably a compositor's slip; the diplomatic text follows the print."))
L.append(F(188, "proof of (7.4.6): 'foncteur représentable (0, 8.1.5)'",
           "bold 0", "plain 0", 'convention', 2, 'high',
           r"(0, 8.1.5)", r"(\textbf{0}, 8.1.5)",
           "Bold chapter number."))
L.append(F(188, "proof of (7.4.6): '(puisque A est noethérien) projectifs de type fini'",
           "'projectifs' italic", "upright", 'italics', None, 'high',
           r"noethérien) projectifs", r"noethérien) \emph{projectifs}",
           "Italic in the print; upright in the TeX."))
L.append(F(188, "proof of (7.4.6): 'Le dual P̌_i de P_i'",
           "'dual' italic", "upright", 'italics', None, 'high',
           r"Le dual $\check P_i$", r"Le \emph{dual} $\check P_i$",
           "Italic in the print (the second 'dual', 'au dual de P̌_i', is upright as in the TeX)."))
L.append(F(188, "proof of (7.4.6): 'l'homomorphisme canonique P_i⊗_A M->Hom_A(P̌_i, M) est bijectif'",
           "formula in the running text", "displayed", 'other', None, 'high',
           r"\[<NL>  P_i\otimes_A M\longrightarrow\operatorname{Hom}_A(\check P_i,M)<NL>\]",
           r"$P_i\otimes_A M\longrightarrow\operatorname{Hom}_A(\check P_i,M)$",
           "Layout: the print sets this formula inline (GLOBAL_ISSUES 21/36)."))
L.append(F(188, "proof of (7.4.6): 'la suite exacte 0->Q'->P_p->P_{p-1},'",
           "formula in the running text", "displayed", 'other', None, 'high',
           r"\[<NL>  0\longrightarrow Q'\xrightarrow{w}P_p\xrightarrow{d_p}P_{p-1},<NL>\]",
           r"$0\longrightarrow Q'\xrightarrow{w}P_p\xrightarrow{d_p}P_{p-1}$,",
           "Layout: the print sets this formula inline (GLOBAL_ISSUES 21/36)."))
L.append(F(188, "proof of (7.4.6): 'par transposition, la suite exacte P̌_{p-1}->P̌_p->Q̌'->0.'",
           "formula in the running text", "displayed", 'other', None, 'high',
           r"\[<NL>  \check P_{p-1}\xrightarrow{{}^t d_p}\check P_p<NL>  \xrightarrow{{}^t w}\check Q'\longrightarrow0.<NL>\]",
           r"$\check P_{p-1}\xrightarrow{{}^t d_p}\check P_p<NL>\xrightarrow{{}^t w}\check Q'\longrightarrow0$.",
           "Layout: the print sets this formula inline (GLOBAL_ISSUES 21/36)."))
L.append(F(188, "proof of (7.4.6): 'Nous allons voir que Q=Q̌'=Coker(^t d_p) répond'",
           "formula in the running text", "displayed", 'other', None, 'high',
           r"\[<NL>  Q=\check Q'=\operatorname{Coker}({}^t d_p)<NL>\]",
           r"$Q=\check Q'=\operatorname{Coker}({}^t d_p)$",
           "Layout: the print sets this formula inline (GLOBAL_ISSUES 21/36)."))
L.append(F(188, "proof of (7.4.6), last display: '0 -> Hom(Q, M) -> Hom(P̌_p, M) -> Hom(P̌_{p-1}, M)'",
           "Hom without subscript A, three times (enlarged crop)", "\\operatorname{Hom}_A three times",
           'formula', None, 'high',
           r"0\longrightarrow\operatorname{Hom}_A(Q,M)<NL>  \longrightarrow\operatorname{Hom}_A(\check P_p,M)<NL>  \xrightarrow{v'}\operatorname{Hom}_A(\check P_{p-1},M)",
           r"0\longrightarrow\operatorname{Hom}(Q,M)<NL>  \longrightarrow\operatorname{Hom}(\check P_p,M)<NL>  \xrightarrow{v'}\operatorname{Hom}(\check P_{p-1},M)",
           "The (7.4.6.1) display and Hom_A(P̌_i, M) earlier on the page do have the subscript A in the print; this display does not."))

# ---------------------------------------------------------------- page 189
L.append(F(189, "proof of (7.4.6): 'l'isomorphisme fonctoriel T_p(M) ⥲ Hom_A(Q, M) cherché'",
           "formula in the running text", "displayed", 'other', None, 'high',
           r"\[<NL>  T_p(M)\xrightarrow{\sim}\operatorname{Hom}_A(Q,M)<NL>\]",
           r"$T_p(M)\xrightarrow{\sim}\operatorname{Hom}_A(Q,M)$",
           "Layout: the print sets this formula inline (GLOBAL_ISSUES 21/36)."))
L.append(F(189, "Proposition (7.4.7): 'les conditions générales de (7.4.4). Alors'",
           "reference upright", "italic", 'convention', 6, 'high',
           r"générales de (7.4.4). Alors", r"générales de \textup{(7.4.4)}. Alors",
           "Enlarged crop."))
L.append(F(189, "Proposition (7.4.7): label (i)",
           "'(i)' upright", "\\item[(i)] italic in the statement", 'convention', 6, 'high',
           r"\item[(i)] Les", r"\item[\textup{(i)}] Les",
           "GLOBAL_ISSUES 16 (roman-numeral labels upright in the print)."))
L.append(F(189, "Proposition (7.4.7): label (ii)",
           "'(ii)' upright", "\\item[(ii)] italic in the statement", 'convention', 6, 'high',
           r"\item[(ii)] Pour tout idéal", r"\item[\textup{(ii)}] Pour tout idéal",
           "GLOBAL_ISSUES 16."))
L.append(F(189, "(7.4.7.1): '(T_i(M))^ -> lim T_i(M⊗_A(A/m^{n+1}))'",
           "circumflex after the closing parenthesis: (T_i(M))^", "\\widehat{T_i(M)}", 'formula', None, 'high',
           r"\widehat{T_i(M)}", r"(T_i(M))^{\widehat{\,}}",
           "Circumflex analogue of convention 5 (GLOBAL_ISSUES 31/47); same form as the ega3-1 fixes."))
L.append(F(189, "Lemme (7.4.7.2): 'Pour tout A-module de type fini, posons K(M)=...'",
           "'Pour tout A-module de type fini' (no M; enlarged crop)", "same as the print",
           'misprint_in_print', None, 'high',
           None, None,
           "The TeX keeps the printed reading. The variable M used in K(M), C(M) is never introduced.",
           corrected=r"Pour tout $A$-module $M$ de type fini"))
L.append(F(189, "Lemme (7.4.7.2): 'posons K(M)=Ker(u⊗1_M), C(M)=Coker(u⊗1_M); alors'",
           "formulas in the running text", "displayed", 'other', None, 'high',
           r"\[<NL>  K(M)=\operatorname{Ker}(u\otimes1_M),<NL>  \qquad<NL>  C(M)=\operatorname{Coker}(u\otimes1_M);<NL>\]",
           r"$K(M)=\operatorname{Ker}(u\otimes1_M)$,<NL>$C(M)=\operatorname{Coker}(u\otimes1_M)$;",
           "Layout: the print sets these formulas inline (GLOBAL_ISSUES 21/36)."))
L.append(F(189, "(7.4.7.3), first formula: '(K(M))^ -> lim K(M_n)'",
           "(K(M))^", "\\widehat{K(M)}", 'formula', None, 'high',
           r"\widehat{K(M)}\longrightarrow\varprojlim_n K(M_n)",
           r"(K(M))^{\widehat{\,}}\longrightarrow\varprojlim_n K(M_n)",
           "Circumflex analogue of convention 5. The lim has the index n here, as in the TeX."))
L.append(F(189, "(7.4.7.3), second formula: '(C(M))^ -> lim C(M_n)'",
           "(C(M))^", "\\widehat{C(M)}", 'formula', None, 'high',
           r"\widehat{C(M)}\longrightarrow\varprojlim_n C(M_n)",
           r"(C(M))^{\widehat{\,}}\longrightarrow\varprojlim_n C(M_n)",
           "Circumflex analogue of convention 5."))
L.append(F(189, "proof of (7.4.7.2): 'le foncteur M⇝M̂ est exact'",
           "wavy arrow", "\\mapsto", 'symbol', None, 'high',
           r"$M\mapsto\widehat M$", r"$M\leadsto\widehat M$",
           "Wavy arrow in the print (\\leadsto), not convention 3 (GLOBAL_ISSUES 33)."))
L.append(F(189, "proof of (7.4.7.2): 'est exact dans la catégorie'",
           "'exact' italic", "upright", 'italics', None, 'high',
           r"est exact dans la catégorie", r"est \emph{exact} dans la catégorie",
           "Italic in the print; upright in the TeX."))
L.append(F(189, "proof of (7.4.7.2): '(0_I, 7.3.3)'",
           "bold 0", "plain 0", 'convention', 2, 'high',
           r"($0_{\mathrm I}$, 7.3.3)", r"($\mathbf{0}_{\mathrm I}$, 7.3.3)",
           "Bold chapter number."))
L.append(F(189, "proof of (7.4.7.2): '(K(M))^ et (C(M))^ sont respectivement'",
           "(K(M))^ and (C(M))^", "\\widehat{K(M)}, \\widehat{C(M)}", 'formula', None, 'high',
           r"$\widehat{K(M)}$ et $\widehat{C(M)}$ sont", r"$(K(M))^{\widehat{\,}}$ et $(C(M))^{\widehat{\,}}$ sont",
           "Circumflex analogue of convention 5 (two in one edit)."))
L.append(F(189, "proof of (7.4.7.2): 'le noyau et le conoyau de (u⊗1)^ : (E⊗M)^ -> (F⊗M)^.'",
           "inline formula with circumflexes after the parentheses", "displayed, with wide hats over (u⊗1), (E⊗M), (F⊗M)",
           'formula', None, 'high',
           r"\[<NL>  \widehat{(u\otimes1)}:<NL>  \widehat{(E\otimes M)}\longrightarrow\widehat{(F\otimes M)}.<NL>\]",
           r"$(u\otimes1)^{\widehat{\,}}:(E\otimes M)^{\widehat{\,}}\longrightarrow(F\otimes M)^{\widehat{\,}}$.",
           "Circumflex analogue of convention 5 (three hats); the fix also sets the formula inline, as printed."))
L.append(F(189, "proof of (7.4.7.2): 'montre donc que (K(M))^=lim K(M_n)'",
           "(K(M))^; lim without the index n (enlarged crop)", "\\widehat{K(M)}=\\varprojlim_n", 'formula', None, 'high',
           r"$\widehat{K(M)}=\varprojlim_n K(M_n)$", r"$(K(M))^{\widehat{\,}}=\varprojlim K(M_n)$",
           "Two differences in one formula: circumflex after the parenthesis, and no index under the inline lim (cf. GLOBAL_ISSUES 30)."))
L.append(F(189, "proof of (7.4.7.2): 'donc (C(M))^=lim C(M_n) par définition'",
           "(C(M))^; lim without the index n (enlarged crop)", "\\widehat{C(M)}=\\varprojlim_n", 'formula', None, 'high',
           r"$\widehat{C(M)}=\varprojlim_n C(M_n)$", r"$(C(M))^{\widehat{\,}}=\varprojlim C(M_n)$",
           "Two differences in one formula, as in the preceding finding."))
L.append(F(189, "Remarque (7.4.8): 'mais à un complexe de tels Modules'",
           "'complexe' italic in the roman remark", "no emphasis (remark body italic in the TeX)", 'italics', None, 'high',
           r"à un complexe de tels", r"à un \emph{complexe} de tels",
           "Judged as if the remark body were roman (document-wide remark item)."))

# ---------------------------------------------------------------- page 190
L.append(F(190, "heading 7.5",
           "'7.5. Cas des anneaux locaux noethériens.' (final full stop)", "no full stop", 'punctuation', None, 'high',
           r"\subsection{Cas des anneaux locaux noethériens}", r"\subsection{Cas des anneaux locaux noethériens.}",
           "Same pattern as GLOBAL_ISSUES 43; no \\subsection title in ega3-7-fr.tex has the full stop."))
L.append(F(190, "(7.5.1): 'isomorphe à lim(M⊗_A(A/m^{n+1}))=lim(M/m^{n+1}M).'",
           "inline; neither lim has the index n (enlarged crop)", "displayed; \\varprojlim_n twice", 'formula', None, 'high',
           r"\[<NL>  \varprojlim_n\bigl(M\otimes_A(A/\mathfrak m^{n+1})\bigr)<NL>  =<NL>  \varprojlim_n\bigl(M/\mathfrak m^{n+1}M\bigr).<NL>\]",
           r"$\varprojlim\bigl(M\otimes_A(A/\mathfrak m^{n+1})\bigr)=\varprojlim\bigl(M/\mathfrak m^{n+1}M\bigr)$.",
           "No index under the inline lims (cf. GLOBAL_ISSUES 30); the fix also sets the formula inline, as printed."))
L.append(F(190, "(7.5.1): 'additif de Ab_A dans Ab;'",
           "Ab bold italic, twice (enlarged crop)", "\\mathbf{Ab} (bold upright)", 'font', None, 'high',
           r"de $\mathbf{Ab}_A$ dans $\mathbf{Ab}$;", r"de $\boldsymbol{Ab}_A$ dans $\boldsymbol{Ab}$;",
           "Bold italic in the running text; the italic statement (7.5.2) has bold upright Ab, as the TeX."))
L.append(F(190, "(7.5.1.1): '(T(M))^ -> lim T(M_n)'",
           "(T(M))^", "\\widehat{T(M)}", 'formula', None, 'high',
           r"\widehat{T(M)}<NL>  \longrightarrow<NL>  \varprojlim_n T(M_n)",
           r"(T(M))^{\widehat{\,}}<NL>  \longrightarrow<NL>  \varprojlim_n T(M_n)",
           "Circumflex analogue of convention 5. The displayed lim has the index n, as in the TeX."))
L.append(F(190, "(7.5.1): 'où l'on a posé M_n=M⊗_A(A/m^{n+1}), A_n=A/m^{n+1}.'",
           "formulas in the running text", "displayed", 'other', None, 'high',
           r"\[<NL>  M_n=M\otimes_A(A/\mathfrak m^{n+1}),<NL>  \qquad<NL>  A_n=A/\mathfrak m^{n+1}.<NL>\]",
           r"$M_n=M\otimes_A(A/\mathfrak m^{n+1})$, $A_n=A/\mathfrak m^{n+1}$.",
           "Layout: the print sets these formulas inline (GLOBAL_ISSUES 21/36)."))
L.append(F(190, "Proposition (7.5.2): 'l'homomorphisme canonique (7.5.1.1) est un isomorphisme'",
           "reference upright", "italic", 'convention', 6, 'high',
           r"(7.5.1.1) est un isomorphisme", r"\textup{(7.5.1.1)} est un isomorphisme",
           ""))
L.append(F(190, "Proposition (7.5.2) b): 'le foncteur N⇝T(N)'",
           "wavy arrow (enlarged crop)", "\\mapsto", 'symbol', None, 'high',
           r"$N\mapsto T(N)$", r"$N\leadsto T(N)$",
           "Wavy arrow in the print (\\leadsto), not convention 3."))
L.append(F(190, "Proposition (7.5.2) b): '(ce qui revient à dire que T est exact à droite dans la catégorie des A-modules de longueur finie)'",
           "parenthesis roman, 'de longueur finie' italic (enlarged crop)", "all italic", 'convention', 6, 'high',
           r"(ce qui revient à dire que $T$<NL>    est exact à droite dans la catégorie des $A$-modules de longueur finie)",
           r"\textup{(ce qui revient à dire que $T$<NL>    est exact à droite dans la catégorie des $A$-modules \emph{de longueur finie})}",
           ""))
L.append(F(190, "Proposition (7.5.2) c): 'L'homomorphisme canonique T(ε) : T(A)->T(k) est surjectif.'",
           "formula in the running text", "displayed", 'other', None, 'high',
           r"\[<NL>      T(\varepsilon):T(A)\longrightarrow T(k)<NL>    \]",
           r"$T(\varepsilon):T(A)\longrightarrow T(k)$",
           "Layout: the print sets this formula inline (GLOBAL_ISSUES 21/36)."))
L.append(F(190, "Proposition (7.5.2) d): 'l'homomorphisme canonique T(A_n)->T(k) est surjectif.'",
           "formula in the running text", "displayed", 'other', None, 'high',
           r"\[<NL>      T(A_n)\longrightarrow T(k)<NL>    \]",
           r"$T(A_n)\longrightarrow T(k)$",
           "Layout: the print sets this formula inline (GLOBAL_ISSUES 21/36)."))
L.append(F(190, "proof of (7.5.2): 'Il est clair que a) entraîne b). Montrons que b) entraîne a),'",
           "the labels a), b) italic", "upright", 'italics', None, 'high',
           r"Il est clair que a) entraîne b). Montrons que b) entraîne a),",
           r"Il est clair que \emph{a)} entraîne \emph{b)}. Montrons que \emph{b)} entraîne \emph{a)},",
           "Four labels in one edit; form \\emph{a)} as in the earlier fixes."))
L.append(F(190, "proof of (7.5.2): 'il suffit de montrer que (T(u))^ : (T(M))^ -> (T(N))^ est surjectif'",
           "inline formula with circumflexes after the parentheses", "displayed, wide hats", 'formula', None, 'high',
           r"\[<NL>  \widehat{T(u)}:<NL>  \widehat{T(M)}<NL>  \longrightarrow<NL>  \widehat{T(N)}<NL>\]",
           r"$(T(u))^{\widehat{\,}}:(T(M))^{\widehat{\,}}\longrightarrow(T(N))^{\widehat{\,}}$",
           "Circumflex analogue of convention 5 (three hats); the fix also sets the formula inline, as printed."))
L.append(F(190, "proof of (7.5.2): '(0_I, 7.3.5 et 0_I, 6.4.1)', first 0",
           "bold 0", "plain 0", 'convention', 2, 'high',
           r"($0_{\mathrm I}$, 7.3.5 et", r"($\mathbf{0}_{\mathrm I}$, 7.3.5 et",
           "Bold chapter number."))
L.append(F(190, "proof of (7.5.2): '(0_I, 7.3.5 et 0_I, 6.4.1)', second 0",
           "bold 0", "plain 0", 'convention', 2, 'high',
           r"$0_{\mathrm I}$, 6.4.1)", r"$\mathbf{0}_{\mathrm I}$, 6.4.1)",
           "Bold chapter number."))
L.append(F(190, "proof of (7.5.2): '(T(M))^ et (T(N))^ sont respectivement'",
           "(T(M))^ and (T(N))^", "wide hats", 'formula', None, 'high',
           r"$\widehat{T(M)}$ et $\widehat{T(N)}$ sont respectivement",
           r"$(T(M))^{\widehat{\,}}$ et $(T(N))^{\widehat{\,}}$ sont respectivement",
           "Circumflex analogue of convention 5 (two in one edit)."))
L.append(F(190, "proof of (7.5.2): 'lim T(M_n) et lim T(N_n)'",
           "inline lims without the index n (enlarged crop)", "\\varprojlim_n twice", 'formula', None, 'high',
           r"$\varprojlim_n T(M_n)$<NL>et $\varprojlim_n T(N_n)$",
           r"$\varprojlim T(M_n)$<NL>et $\varprojlim T(N_n)$",
           "Cf. GLOBAL_ISSUES 30."))
L.append(F(190, "proof of (7.5.2): 'donc (T(u))^ est limite du système projectif'",
           "(T(u))^", "\\widehat{T(u)}", 'formula', None, 'high',
           r"donc $\widehat{T(u)}$ est limite", r"donc $(T(u))^{\widehat{\,}}$ est limite",
           "Circumflex analogue of convention 5."))
L.append(F(190, "proof of (7.5.2): 'd'homomorphismes T(u⊗1_{A_n}) : T(M_n)->T(N_n).'",
           "formula in the running text", "displayed", 'other', None, 'high',
           r"\[<NL>  T(u\otimes1_{A_n}):T(M_n)\longrightarrow T(N_n).<NL>\]",
           r"$T(u\otimes1_{A_n}):T(M_n)\longrightarrow T(N_n)$.",
           "Layout: the print sets this formula inline (GLOBAL_ISSUES 21/36)."))
L.append(F(190, "proof of (7.5.2): 'Or, b) signifie'",
           "label b) italic", "upright", 'italics', None, 'high',
           r"Or, b) signifie", r"Or, \emph{b)} signifie",
           ""))
L.append(F(190, "proof of (7.5.2): 'ces homomorphismes sont surjectifs;'",
           "'surjectifs' italic", "upright", 'italics', None, 'high',
           r"sont surjectifs;", r"sont \emph{surjectifs};",
           "Italic in the print; upright in the TeX."))
L.append(F(190, "proof of (7.5.2): 'A_n est un anneau artinien par hypothèse'",
           "'artinien' italic", "upright", 'italics', None, 'high',
           r"anneau artinien par", r"anneau \emph{artinien} par",
           "Italic in the print; upright in the TeX."))
L.append(F(190, "proof of (7.5.2): 'on en conclut que (T(u))^ est surjectif'",
           "(T(u))^", "\\widehat{T(u)}", 'formula', None, 'high',
           r"conclut que $\widehat{T(u)}$", r"conclut que $(T(u))^{\widehat{\,}}$",
           "Circumflex analogue of convention 5."))
L.append(F(190, "proof of (7.5.2): '(0, 13.1.2 et 13.2.2)'",
           "bold 0 without subscript (enlarged crop)", "$0_{\\mathrm I}$, 13.1.2", 'extra', None, 'high',
           r"($0_{\mathrm I}$, 13.1.2 et", r"(\textbf{0}, 13.1.2 et",
           "The TeX adds the subscript I; 13.1.2 and 13.2.2 are in chapter 0 of EGA III (Mittag-Leffler), not in 0_I, so the print's '(0, ...)' is right. The edit also sets the bold 0 (next finding)."))
L.append(F(190, "proof of (7.5.2): '(0, 13.1.2 et 13.2.2)', bold 0",
           "bold 0", "plain 0", 'convention', 2, 'high',
           None, None,
           "Covered by the edit of the preceding finding, which writes \\textbf{0}."))
L.append(F(190, "proof of (7.5.2): 'Il est clair que a) entraîne c)'",
           "labels italic", "upright", 'italics', None, 'high',
           r"Il est clair que a) entraîne c)", r"Il est clair que \emph{a)} entraîne \emph{c)}",
           ""))
L.append(F(190, "proof of (7.5.2): 'se factorise en T(A)->T(A_n)->T(k), c) implique d)'",
           "formula in the running text", "displayed", 'other', None, 'high',
           r"\[<NL>  T(A)\longrightarrow T(A_n)\longrightarrow T(k),<NL>\]",
           r"$T(A)\longrightarrow T(A_n)\longrightarrow T(k)$,",
           "Layout: the print sets this formula inline (GLOBAL_ISSUES 21/36)."))
L.append(F(190, "proof of (7.5.2): 'c) implique d);'",
           "labels italic", "upright", 'italics', None, 'high',
           r"c) implique d);", r"\emph{c)} implique \emph{d)};",
           ""))
L.append(F(190, "proof of (7.5.2): 'que b) et d) sont équivalentes'",
           "labels italic", "upright", 'italics', None, 'high',
           r"que b) et d) sont", r"que \emph{b)} et \emph{d)} sont",
           ""))
L.append(F(190, "proof of (7.5.2): 'semi-exact dans Ab_{A_n}'",
           "Ab bold italic (enlarged crop)", "\\mathbf{Ab}", 'font', None, 'high',
           r"$\mathbf{Ab}_{A_n}$", r"$\boldsymbol{Ab}_{A_n}$",
           "Bold italic in the running text."))
L.append(F(190, "Corollaire (7.5.3): 'Sous les hypothèses générales de (7.5.2)'",
           "reference upright", "italic", 'convention', 6, 'high',
           r"générales de (7.5.2), si", r"générales de \textup{(7.5.2)}, si",
           ""))

# ---------------------------------------------------------------- page 191
L.append(F(191, "proof of (7.5.3): '(T(M))^ est isomorphe à'",
           "(T(M))^", "\\widehat{T(M)}", 'formula', None, 'high',
           r"$\widehat{T(M)}$ est isomorphe", r"$(T(M))^{\widehat{\,}}$ est isomorphe",
           "Circumflex analogue of convention 5."))
L.append(F(191, "proof of (7.5.3): 'isomorphe à lim T(M_n), et comme'",
           "inline lim without the index n (enlarged crop)", "\\varprojlim_n", 'formula', None, 'high',
           r"$\varprojlim_n T(M_n)$, et comme", r"$\varprojlim T(M_n)$, et comme",
           "Cf. GLOBAL_ISSUES 30."))
L.append(F(191, "proof of (7.5.3): 'on a (T(M))^=0;'",
           "(T(M))^", "\\widehat{T(M)}", 'formula', None, 'high',
           r"$\widehat{T(M)}=0$", r"$(T(M))^{\widehat{\,}}=0$",
           "Circumflex analogue of convention 5."))
L.append(F(191, "proof of (7.5.3): 'un sous-module de (T(M))^'",
           "(T(M))^", "\\widehat{T(M)}", 'formula', None, 'high',
           r"sous-module de $\widehat{T(M)}$", r"sous-module de $(T(M))^{\widehat{\,}}$",
           "Circumflex analogue of convention 5."))
L.append(F(191, "proof of (7.5.3): '(0_I, 7.3.5)'",
           "bold 0", "plain 0", 'convention', 2, 'high',
           r"($0_{\mathrm I}$, 7.3.5)", r"($\mathbf{0}_{\mathrm I}$, 7.3.5)",
           "Bold chapter number."))
L.append(F(191, "Proposition (7.5.4): 'l'homomorphisme canonique (T_i(M))^ -> lim T_i(M_n) est bijectif'",
           "inline; (T_i(M))^; lim without the index n (enlarged crop)", "displayed; \\widehat{T_i(M)}; \\varprojlim_n",
           'formula', None, 'high',
           r"\[<NL>  \widehat{T_i(M)}<NL>  \longrightarrow<NL>  \varprojlim_n T_i(M_n)<NL>\]",
           r"$(T_i(M))^{\widehat{\,}}\longrightarrow\varprojlim T_i(M_n)$",
           "One edit for three differences in one formula: circumflex after the parenthesis, no index under the inline lim, formula in the running text."))
L.append(F(191, "Proposition (7.5.4) c): 'Les homomorphismes canoniques T_{p+1}(A)->T_{p+1}(k) et T_p(A)->T_p(k) sont surjectifs.'",
           "formulas in the running text", "displayed", 'other', None, 'high',
           r"\[<NL>      T_{p+1}(A)\longrightarrow T_{p+1}(k)<NL>      \quad\text{et}\quad<NL>      T_p(A)\longrightarrow T_p(k)<NL>    \]",
           r"$T_{p+1}(A)\longrightarrow T_{p+1}(k)$ et $T_p(A)\longrightarrow T_p(k)$",
           "Layout: the print sets these formulas inline (GLOBAL_ISSUES 21/36); 'et' is italic in the print."))
L.append(F(191, "Proposition (7.5.4) d): 'les homomorphismes canoniques T_{p+1}(A_n)->T_{p+1}(k) et T_p(A_n)->T_p(k) sont surjectifs.'",
           "formulas in the running text", "displayed", 'other', None, 'high',
           r"\[<NL>      T_{p+1}(A_n)\longrightarrow T_{p+1}(k)<NL>      \quad\text{et}\quad<NL>      T_p(A_n)\longrightarrow T_p(k)<NL>    \]",
           r"$T_{p+1}(A_n)\longrightarrow T_{p+1}(k)$ et $T_p(A_n)\longrightarrow T_p(k)$",
           "Layout: the print sets these formulas inline (GLOBAL_ISSUES 21/36)."))
L.append(F(191, "Proposition (7.5.4) e): 'le foncteur N⇝T_p(N)'",
           "wavy arrow", "\\mapsto", 'symbol', None, 'high',
           r"$N\mapsto T_p(N)$", r"$N\leadsto T_p(N)$",
           "Wavy arrow in the print (\\leadsto), not convention 3."))
L.append(F(191, "proof of (7.5.4): 'On sait (7.3.3) que a) équivaut'",
           "label a) italic", "upright", 'italics', None, 'high',
           r"que a) équivaut", r"que \emph{a)} équivaut",
           ""))
L.append(F(191, "proof of (7.5.4): 'dans la catégorie Ab_{A_n}'",
           "Ab bold italic (enlarged crop)", "\\mathbf{Ab}", 'font', None, 'high',
           r"$\mathbf{Ab}_{A_n}$", r"$\boldsymbol{Ab}_{A_n}$",
           "Bold italic in the running text; the statement of (7.5.4) has bold upright Ab, as the TeX."))
L.append(F(191, "proof of (7.5.4): 'montre que e) équivaut'",
           "label e) italic", "upright", 'italics', None, 'high',
           r"montre que e)<NL>équivaut", r"montre que \emph{e)}<NL>équivaut",
           ""))
L.append(F(191, "proof of (7.5.4): 'que a) et e) sont équivalentes'",
           "labels italic", "upright", 'italics', None, 'high',
           r"que a) et e) sont", r"que \emph{a)} et \emph{e)} sont",
           ""))
L.append(F(191, "proof of (7.5.4): 'l'équivalence de a), c) et d) résulte'",
           "labels italic", "upright", 'italics', None, 'high',
           r"l'équivalence de a), c) et d) résulte", r"l'équivalence de \emph{a)}, \emph{c)} et \emph{d)} résulte",
           ""))
L.append(F(191, "proof of (7.5.4): 'de type fini est libre (Bourbaki'",
           "'libre' italic", "upright", 'italics', None, 'high',
           r"est libre (Bourbaki", r"est \emph{libre} (Bourbaki",
           "Italic in the print; upright in the TeX."))
L.append(F(191, "proof of (7.5.4): 'l'équivalence de a) et b) résulte'",
           "labels italic", "upright", 'italics', None, 'high',
           r"l'équivalence de a) et b) résulte", r"l'équivalence de \emph{a)} et \emph{b)} résulte",
           ""))
L.append(F(191, "Corollaire (7.5.5): 'les conditions générales de (7.5.4).'",
           "reference upright", "italic", 'convention', 6, 'high',
           r"conditions générales de (7.5.4).", r"conditions générales de \textup{(7.5.4)}.",
           "Enlarged crop."))
L.append(F(191, "Corollaire (7.5.5): label (i)",
           "'(i)' upright", "\\item[(i)] italic", 'convention', 6, 'high',
           r"\item[(i)] Si $T_p(k)=0$", r"\item[\textup{(i)}] Si $T_p(k)=0$",
           "GLOBAL_ISSUES 16."))
L.append(F(191, "Corollaire (7.5.5): label (ii)",
           "'(ii)' upright", "\\item[(ii)] italic", 'convention', 6, 'high',
           r"\item[(ii)] Si $T_{p-1}(k)", r"\item[\textup{(ii)}] Si $T_{p-1}(k)",
           "GLOBAL_ISSUES 16."))
L.append(F(191, "Corollaire (7.5.6): 'les hypothèses générales de (7.5.4), et supposons'",
           "reference upright", "italic", 'convention', 6, 'high',
           r"hypothèses générales de (7.5.4), et", r"hypothèses générales de \textup{(7.5.4)}, et",
           ""))
L.append(F(191, "Corollaire (7.5.6): label (i)",
           "'(i)' upright", "\\item[(i)] italic", 'convention', 6, 'high',
           r"\item[(i)] Pour que $T_p$ soit exact à droite", r"\item[\textup{(i)}] Pour que $T_p$ soit exact à droite",
           "GLOBAL_ISSUES 16."))
L.append(F(191, "Corollaire (7.5.6): label (ii)",
           "'(ii)' upright", "\\item[(ii)] italic", 'convention', 6, 'high',
           r"\item[(ii)] Pour que $T_p$ soit exact,", r"\item[\textup{(ii)}] Pour que $T_p$ soit exact,",
           "GLOBAL_ISSUES 16."))

# ---------------------------------------------------------------- checks
pages = {}
for p in (187, 188, 189, 190, 191):
    with open(os.path.join(RUN, 'page_%d.tex' % p), encoding='utf-8', newline='') as fh:
        pages[p] = fh.read().replace('\r\n', '\n')

bad = 0
for d in L:
    if d['fix'] is None:
        continue
    t = pages[d['page']]
    n = t.count(d['fix']['old'])
    if n != 1:
        bad += 1
        sys.stdout.buffer.write(('COUNT %d on p.%d: %r\n' % (n, d['page'], d['fix']['old'])).encode('utf-8'))
    if d['fix']['old'] == d['fix']['new']:
        bad += 1
        print('old == new', d['where'])

# overlap check: no two olds on the same page may overlap
for p in pages:
    t = pages[p]
    spans = []
    for d in L:
        if d['page'] == p and d['fix'] is not None and t.count(d['fix']['old']) == 1:
            s = t.index(d['fix']['old'])
            spans.append((s, s + len(d['fix']['old']), d['where']))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            bad += 1
            sys.stdout.buffer.write(('OVERLAP p.%d: %s | %s\n' % (p, a[2], b[2])).encode('utf-8'))

counts = {}
for d in L:
    c = counts.setdefault(d['page'], [0, 0, 0])
    if d['kind'] == 'convention':
        c[1] += 1
    elif d['kind'] == 'misprint_in_print':
        c[2] += 1
    else:
        c[0] += 1
print('problems:', bad)
print('counts (normal/convention/misprint):', counts)
if bad == 0 or (len(sys.argv) > 1 and sys.argv[1] == '--force'):
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(L, fh, ensure_ascii=False, indent=1)
    print('written', OUT, len(L))
