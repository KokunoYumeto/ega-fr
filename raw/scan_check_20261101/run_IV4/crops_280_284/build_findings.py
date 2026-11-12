import io, json, sys

BASE = r'user/Documents/ega_scan_check_20261101/'
RUN = BASE + 'run_IV4/'
SRC = BASE + 'ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-21b-fr.tex'
OUT = RUN + 'findings_280_284.json'
NL = '\n'

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, target=None):
    d = {'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind, 'convention': conv,
         'confidence': conf,
         'fix': None if old is None else {'old': old, 'new': new}}
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    d['_target'] = target or page
    F.append(d)


# ---------------------------------------------------------------- p. 280
add(280, "top of the page: 'sous-|jacent' (word broken at its hyphen across the page break)",
    "p. 279 ends with 'ayant {y}-bar pour espace sous-' and p. 280 begins with 'jacent est intègre' (page_279_s4.png, page_280_s1.png)",
    "the marker stands before the whole word 'sous-jacent'",
    'marker', None, 'high',
    r'\oldpage[IV-4]{280}' + NL + r'sous-jacent est intègre',
    r'sous-%' + NL + r'\oldpage[IV-4]{280}' + NL + r'jacent est intègre',
    "Boundary fix with p. 279 (marker position). Written as the edition's other split words (mor%|phisme at \\oldpage[IV-4]{104}, consi%|dérer at p. 93); \\oldpage ends with \\ignorespaces, so the text still reads 'espace sous-jacent'. After the edit 'sous-%' ends the p. 279 segment; the old string lies in the p. 280 segment.")

add(280, "Remarque (21.7.5), l. 9: 'ou t_3 — a, avec a ≠ 0'",
    "long dash in t_3—a (crop p280_t3a.png)", "minus sign",
    'convention', 7, 'high',
    r'$t_3-a$', r'$t_3\setmin a$',
    "Subtraction printed with the long dash (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.")

add(280, "Corollaire (21.7.6) a'), l. 2: 'd'un diviseur positif principal, autrement dit'",
    "'principal' printed roman inside the italic statement (emphasis) (crop p280_aprime.png)",
    "'principal' italic like its surroundings",
    'italics', None, 'high',
    r'positif principal, autrement dit', r'positif \emph{principal}, autrement dit',
    "Emphasis by roman type inside the italic corollary; \\emph sets it upright there.")

add(280, "Lemme (21.8.1), l. 2: 'O_{X'}-Module localement libre ℰ' de rang constant n'",
    "script ℰ' (page_280_s3.png)", "plain italic E'",
    'font', None, 'high',
    r"libre $E'$ de rang constant", r"libre $\sh{E}'$ de rang constant",
    "Wrong letter: the locally free Module is the script ℰ' throughout (21.8.1) and its proof (8 letters in 5 entries).")

add(280, "Lemme (21.8.1), l. 3: 'ℰ'|U' soit isomorphe à O^n_{U'}'",
    "script ℰ'", "plain E'",
    'font', None, 'high',
    r"$E'|U'$ soit isomorphe", r"$\sh{E}'|U'$ soit isomorphe",
    "")

add(280, "proof of (21.8.1), l. 5: 'un O_{X'_λ}-Module localement libre ℰ'_λ de rang n tel que ℰ' = p*_λ(ℰ'_λ)'",
    "script ℰ'_λ, ℰ', ℰ'_λ (page_280_s3.png)", "plain E'_λ, E', E'_λ",
    'font', None, 'high',
    r"libre $E'_\lambda$ de rang $n$ tel que $E'=p_\lambda^*(E'_\lambda)$",
    r"libre $\sh{E}'_\lambda$ de rang $n$ tel que $\sh{E}'=p_\lambda^*(\sh{E}'_\lambda)$",
    "Independent of the next entry (the two old strings are adjacent, they do not overlap).")

add(280, "proof of (21.8.1), l. 5: 'tel que ℰ' = p*_λ(ℰ'_λ), et il suffira évidemment'",
    "comma after the formula (page_280_s3.png)", "no comma",
    'punctuation', None, 'high',
    r' et il suffira évidemment', r', et il suffira évidemment',
    "")

add(280, "proof of (21.8.1), l. 6: 'de prouver le lemme pour X'_λ et ℰ'_λ'",
    "script ℰ'_λ (page_280_s4.png)", "plain E'_λ",
    'font', None, 'high',
    r"pour $X'_\lambda$ et $E'_\lambda$;", r"pour $X'_\lambda$ et $\sh{E}'_\lambda$;",
    "")

add(280, "proof of (21.8.1), l. 10: 'ℰ'_0 = ℰ' ⊗_{O_{X'}} O_{X,x}'",
    "script ℰ'_0 and ℰ' (crop p280_tensor.png)", "plain E'_0, E'",
    'font', None, 'high',
    r"$E'_0=E'", r"$\sh{E}'_0=\sh{E}'",
    "Independent of the next entry (adjacent, no overlap).")

add(280, "proof of (21.8.1), l. 10: 'ℰ' ⊗_{O_{X'}} O_{X,x} est isomorphe'",
    "the second factor is O_{X,x} (crop p280_tensor.png)", "O_{X'_0}",
    'formula', None, 'high',
    r"\otimes_{\sh{O}_{X'}}\sh{O}_{X'_0}$", r"\otimes_{\sh{O}_{X'}}\sh{O}_{X,x}$",
    "The TeX rewrote the print's formula. Not recorded as a misprint: EGA's abbreviated notation for the base change to X'_0 = X'×_X Spec(O_{X,x}), not a misprinted sign.")

add(280, "heading of 21.8: '21.8. Diviseurs et normalisation.'",
    "the title ends with a full stop (page_280_s3.png)", "no full stop in the \\subsection title",
    'punctuation', None, 'high',
    r'\subsection{Diviseurs et normalisation}', r'\subsection{Diviseurs et normalisation.}',
    "Same form as the 21.1 and 21.2 titles (pp. 255, 258; GLOBAL_ISSUES 43/58).")

# ---------------------------------------------------------------- p. 281
add(281, "l. 2: 'suivant la méthode de (8.1.2, a)), et appliquant'",
    "'(8.1.2, a))', the italic label inside the reference's parentheses (page_281_s1.png)",
    "\\sref{IV.8.1.2}, \\emph{a)}) prints '(8.1.2), a))'",
    'punctuation', None, 'high',
    r'\sref{IV.8.1.2}, \emph{a)})', r'\sref{IV.8.1.2}[\emph{a)}]',
    "\\sref's third argument prints '(8.1.2, a))' with the italic a) (GLOBAL_ISSUES 68/107).")

add(281, "Corollaire (21.8.2): item labels (i), (ii)",
    "labels upright (page_281_s1.png)", "enumerate labels italic inside the italic corollary",
    'convention', 6, 'high',
    'préschémas.' + NL + 'Alors:' + NL + r'\begin{enumerate}[label=(\roman*)]',
    'préschémas.' + NL + 'Alors:' + NL + r'\begin{enumerate}[label=\textup{(\roman*)}]',
    "GLOBAL_ISSUES 16; one edit covers both labels.")

add(281, "Corollaire (21.8.2) (i): 'On a R^1 f_*(O*_{X'}) = 0 (0_III, 12.2.1).'",
    "bold 0 with a light subscript III (crop p281_0III.png)", "\\sref[0] prints '(0, 12.2.1)' without the subscript",
    'missing', None, 'high',
    r'\sref[0]{0.12.2.1}', r'\sref[$\mathbf{0}_{\mathrm{III}}$]{0.12.2.1}',
    "Form agreed for § 20-21 (GLOBAL_ISSUES 108).")

add(281, "proof of (21.8.2) (i), l. 2: 'préfaisceau de groupes commutatifs U ⇝ H^1(f^{-1}(U), O*_{X'})'",
    "wavy arrow (crop p281_wavy1_loccit.png)", "\\mapsto",
    'symbol', None, 'high',
    r"$U\mapsto\HH^1(f^{-1}(U),\sh{O}^*_{X'})$", r"$U\leadsto\HH^1(f^{-1}(U),\sh{O}^*_{X'})$",
    "GLOBAL_ISSUES 33/107 (wavy arrows).")

add(281, "proof of (21.8.2) (i), l. 2: 'sur X (loc. cit.); la fibre'",
    "the parentheses are italic with the words (crop p281_wavy1_loccit.png)", "roman parentheses around \\emph{loc.\\ cit.}",
    'italics', None, 'medium',
    r'sur $X$ (\emph{loc.\ cit.});', r'sur $X$ \emph{(loc.\ cit.)};',
    "Same fix as the '(loc. cit.)' of p. 223.")

add(281, "proof of (21.8.2) (i), l. 3: 'peut donc (0_I, 5.4.7) être identifiée'",
    "bold 0 with a light subscript I (crop p281_0I_a.png)", "\\sref[0] prints '(0, 5.4.7)'",
    'missing', None, 'high',
    r'peut donc \sref[0]{0.5.4.7} être', r'peut donc \sref[$\mathbf{0}_{\mathrm I}$]{0.5.4.7} être',
    "")

add(281, "proof of (21.8.2) (i), l. 6: 'et tout élément ζ' ∈ Pic(f^{-1}(U'))'",
    "ζ' with a prime, while the next line has 'l'image de ζ' without it (crops p281_zeta1.png, p281_zeta2.png)",
    "ζ (silent correction)",
    'misprint_in_print', None, 'high',
    r"tout élément $\zeta\in\operatorname{Pic}(f^{-1}(U'))$", r"tout élément $\zeta'\in\operatorname{Pic}(f^{-1}(U'))$",
    "The element is called ζ' here and ζ in 'l'image de ζ dans Pic(f^{-1}(U))': one letter for one element. The TeX silently corrects it; restore the printed reading.",
    corrected=r"tout élément $\zeta\in\operatorname{Pic}(f^{-1}(U'))$")

add(281, "proof of (21.8.2) (ii), l. 1: 'foncteur composé ℱ' ⇝ Γ(X, f_*(ℱ'))'",
    "wavy arrow (crop p281_wavy2.png)", "\\mapsto",
    'symbol', None, 'high',
    r"$\sh{F}'\mapsto\Gamma(X,f_*(\sh{F}'))$", r"$\sh{F}'\leadsto\Gamma(X,f_*(\sh{F}'))$",
    "")

add(281, "proof of (21.8.2) (ii), l. 3: 'donne la suite exacte de termes de bas degré (M, XV, 6)'",
    "the reference '(M, XV, 6)' before the display (crop p281_MXV.png)", "missing",
    'missing', None, 'high',
    'de termes de bas degré' + NL + r'\[', 'de termes de bas degré (M, XV, 6)' + NL + r'\[',
    "")

add(281, "proof of (21.8.2) (ii), last line: 'et de H^1(X', O*_{X'}) (0_I, 5.4.7).'",
    "bold 0 with a light subscript I (crop p281_0I_b.png)", "\\sref[0] prints '(0, 5.4.7)'",
    'missing', None, 'high',
    r"\HH^1(X',\sh{O}^*_{X'})$ \sref[0]{0.5.4.7}.", r"\HH^1(X',\sh{O}^*_{X'})$ \sref[$\mathbf{0}_{\mathrm I}$]{0.5.4.7}.",
    "")

add(281, "diagram (21.8.3.1): labels θ*, θ'*, θ''* of the vertical arrows",
    "the three labels stand LEFT of the arrows (crop p281_diag_labels.png)", "\\ar[d]^{...} puts them on the right",
    'other', None, 'high',
    r"\ar[d]^{\theta^*} & \sh{M}^*_X \ar[r] \ar[d]^{\theta'^*} & \sh{D}iv_X \ar[r] \ar[d]^{\theta''^*}",
    r"\ar[d]_{\theta^*} & \sh{M}^*_X \ar[r] \ar[d]_{\theta'^*} & \sh{D}iv_X \ar[r] \ar[d]_{\theta''^*}",
    "Label side of the vertical arrows (cf. GLOBAL_ISSUES 30); one edit for the three labels.")

add(281, "end of the page: printed p. 281 ends with the proof of (21.8.3) ('et de (21.8.2).'); Corollaire (21.8.4) begins p. 282",
    "page_281_s4.png ends with 'et de (21.8.2).' (page number 281 below); page_282_s1.png begins with 'Corollaire (21.8.4)'",
    "\\oldpage[IV-4]{282} stands after the proof of (21.8.4)",
    'marker', None, 'high',
    r'\end{proof}' + NL + NL + r'\begin{corollary}[21.8.4]',
    r'\end{proof}' + NL + NL + r'\oldpage[IV-4]{282}' + NL + NL + r'\begin{corollary}[21.8.4]',
    "Marker move, part 1 of 2: inserts the marker before (21.8.4). Apply together with the first p. 282 entry, which removes the old marker. (21.8.4) and its proof (printed p. 282) have no other differences.")

# ---------------------------------------------------------------- p. 282
add(282, "top of the page: old position of \\oldpage[IV-4]{282}",
    "p. 282 begins with Corollaire (21.8.4)", "marker after the proof of (21.8.4)",
    'marker', None, 'high',
    r'\oldpage[IV-4]{282}' + NL + NL + r'\begin{proposition}[21.8.5]', r'\begin{proposition}[21.8.5]',
    "Marker move, part 2 of 2: removes the old marker (one blank line stays between \\end{proof} and (21.8.5)). Apply together with the last p. 281 entry.")

add(282, "Proposition (21.8.5), l. 3: 'dense dans X' (cf. (20.3.5)), et que'",
    "'(cf. (20.3.5))' roman, upright parentheses (crop p282_cf.png)", "'cf.' and the outer parentheses italic (inside the italic proposition)",
    'convention', 6, 'high',
    r'(cf.\ \sref{IV.20.3.5})', r'\textup{(cf.\ \sref{IV.20.3.5})}',
    "The double parentheses are the print's.")

add(282, "Proposition (21.8.5): item labels (i), (ii)",
    "labels upright (crops p282_label_i.png, p282_label_ii.png)", "enumerate labels italic inside the italic proposition",
    'convention', 6, 'high',
    'isomorphisme.' + NL + 'Alors:' + NL + r'\begin{enumerate}[label=(\roman*)]',
    'isomorphisme.' + NL + 'Alors:' + NL + r'\begin{enumerate}[label=\textup{(\roman*)}]',
    "GLOBAL_ISSUES 16; one edit covers both labels.")

add(282, "Proposition (21.8.5) (i), end: 'est contenu dans S = X — U.'",
    "long dash for set difference (crop p282_XU.png)", "minus sign",
    'convention', 7, 'high',
    r'$S=X-U$', r'$S=X\setmin U$',
    "")

add(282, "diagram (21.8.5.1): labels of the two right-hand vertical arrows",
    "'l_X' and 'l_{X'}', italic l (crop p282_labels_kX.png)", "k_X, k_{X'}",
    'symbol', None, 'high',
    r"\ar[d]^{k_X} & \operatorname{Div}(X') \ar[r] \ar[d]^{k_{X'}}",
    r"\ar[d]^{l_X} & \operatorname{Div}(X') \ar[r] \ar[d]^{l_{X'}}",
    "Wrong letter; the labels stand right of the arrows, as in the TeX.")

add(282, "diagram (21.8.5.1), lower row: label j' of the arrow to Pic(X)",
    "j' set BELOW the arrow (crop p282_jprime.png); the upper row's j is above (crop p282_j.png)", "\\ar[r]^-{j'} puts it above",
    'other', None, 'high',
    r"\ar[r]^-{j'}", r"\ar[r]_-{j'}",
    "Label side (cf. GLOBAL_ISSUES 30).")

add(282, "proof of (21.8.5) (i), l. 1: 'un isomorphisme canonique M'_X ⥲ f_*(M'_{X'})'",
    "one prime: M'_X, M'_{X'} (crop p282_Mprime1.png)", "M''_X, M''_{X'}",
    'symbol', None, 'high',
    r"$\sh{M}''_X\simto f_*(\sh{M}''_{X'})$", r"$\sh{M}'_X\simto f_*(\sh{M}'_{X'})$",
    "The sheaf of pseudo-functions is M'_X in § 20 (ega4-20 source line 304) and in the print here.")

add(282, "proof of (21.8.5) (i), l. 2: 'd'où l'assertion relative à θ', vu l'existence'",
    "comma after θ' (crop p282_theta_comma.png)", "no comma",
    'punctuation', None, 'high',
    r"relative à $\theta'$ vu l'existence", r"relative à $\theta'$, vu l'existence",
    "")

add(282, "proof of (21.8.5) (i), l. 3: 'M_X ⥲ M'_X et M_{X'} ⥲ M'_{X'} (20.2.11)'",
    "one prime (crop p282_Mprime2.png)", "M''_X, M''_{X'}",
    'symbol', None, 'high',
    r"$\sh{M}_X\simto\sh{M}''_X$ et $\sh{M}_{X'}\simto\sh{M}''_{X'}$",
    r"$\sh{M}_X\simto\sh{M}'_X$ et $\sh{M}_{X'}\simto\sh{M}'_{X'}$",
    "As in the entry above.")

add(282, "display (21.8.5.2): ends of its two lines",
    "no comma after '→ 0' nor after '→ 1' (crop p282_disp2.png)", "a comma after each line",
    'punctuation', None, 'high',
    r"f_*(\sh{D}iv_{X'})\to0,\\" + NL + r"  1\to\sh{O}^*_X\to f_*(\sh{O}^*_{X'})\to\sh{N}\to1," + NL,
    r"f_*(\sh{D}iv_{X'})\to0\\" + NL + r"  1\to\sh{O}^*_X\to f_*(\sh{O}^*_{X'})\to\sh{N}\to1" + NL,
    "")

add(282, "display (21.8.5.3): ends of its two lines",
    "no comma after either 'H^1(X, N)' (crop p282_disp3.png)", "a comma after each line",
    'punctuation', None, 'high',
    r"\operatorname{Div}(X')\to\HH^1(X,\sh{N}),\\" + NL + r"  \Gamma(X',\sh{O}^*_{X'})\to\Gamma(X,\sh{N})\xrightarrow{\partial}\operatorname{Pic}(X)\to\operatorname{Pic}(X')\to\HH^1(X,\sh{N})," + NL,
    r"\operatorname{Div}(X')\to\HH^1(X,\sh{N})\\" + NL + r"  \Gamma(X',\sh{O}^*_{X'})\to\Gamma(X,\sh{N})\xrightarrow{\partial}\operatorname{Pic}(X)\to\operatorname{Pic}(X')\to\HH^1(X,\sh{N})" + NL,
    "")

# ---------------------------------------------------------------- p. 283
add(283, "end of printed p. 282 / top of p. 283: the page break falls after 'fermé dans X, on a'",
    "page_282_s4.png ends with 'compte tenu de ... (21.8.2). Or, comme le support de N est contenu dans l'ensemble discret S, fermé dans X, on a'; p. 283 begins with 'H^1(X, N) = H^1(S, N|S)'",
    "\\oldpage[IV-4]{283} stands before 'compte tenu de' (two lines too early)",
    'marker', None, 'high',
    r'\oldpage[IV-4]{283}' + NL + r'compte tenu de', r'compte tenu de',
    "Marker move, part 1 of 2: removes the marker. Apply together with the next entry. The two lines it moves to p. 282 have no other differences.")

add(283, "top of the page: new marker position before 'H^1(X, N) = ...'",
    "p. 283 begins with 'H^1(X, N) = H^1(S, N|S)'", "(marker earlier, see the entry above)",
    'marker', None, 'high',
    "l'ensemble discret $S$, fermé dans $X$, on a" + NL,
    "l'ensemble discret $S$, fermé dans $X$, on a" + NL + r'\oldpage[IV-4]{283}' + NL,
    "Marker move, part 2 of 2: mid-sentence break, no blank lines. Independent of the next entry (no overlap).")

add(283, "l. 1: 'H^1(X, N) = H^1(S, N|S) (G, II, 4.9.2) et H^1(S, N|S) = Π_{s∈S} H^1({s}, N_s) = 0 par définition'",
    "both formulas in the running text, joined by 'et' (page_283_s1.png)",
    "one display with the two formulas joined by \\qquad and a comma; 'et' lost",
    'formula', None, 'high',
    r'\[' + NL + r'  \HH^1(X,\sh{N})=\HH^1(S,\sh{N}|S)\quad\text{(G, II, 4.9.2)},\qquad' + NL + r'  \HH^1(S,\sh{N}|S)=\prod_{s\in S}\HH^1(\{s\},\sh{N}_s)=0' + NL + r'\]' + NL,
    r'$\HH^1(X,\sh{N})=\HH^1(S,\sh{N}|S)$ (G, II, 4.9.2) et $\HH^1(S,\sh{N}|S)=\prod_{s\in S}\HH^1(\{s\},\sh{N}_s)=0$' + NL,
    "Inline as printed (GLOBAL_ISSUES 21/51). The line 'par définition de la cohomologie (G, II, 4.4).' follows unchanged.")

add(283, "l. 5: 'réduit à un seul point s_i et que U_i ∩ U_j ⊂ U'",
    "no comma after s_i (crop p283_si_comma.png)", "comma after s_i",
    'punctuation', None, 'high',
    r'seul point $s_i$, et que', r'seul point $s_i$ et que',
    "")

add(283, "l. 7: 'aux points x ∈ U_i — {s_i}'",
    "long dash for set difference (page_283_s1.png)", "minus sign",
    'convention', 7, 'high',
    r'$x\in U_i-\{s_i\}$', r'$x\in U_i\setmin\{s_i\}$',
    "")

add(283, "l. 15: 'les restrictions d'un même diviseur d ∈ Div(X), qui est l'image'",
    "'d ∈ Div(X)' (crop p283_dDiv.png)", "'de Div(X)': the formula d∈ dropped",
    'word', None, 'high',
    r"d'un même diviseur de $\operatorname{Div}(X)$", r"d'un même diviseur $d\in\operatorname{Div}(X)$",
    "Rewording by the TeX.")

add(283, "heading: 'Remarques (21.8.6)'",
    "plural 'Remarques' (page_283_s2.png)", "\\begin{remark} prints 'Remarque'",
    'word', None, 'high',
    r'\begin{remark}[21.8.6]', r'\begin{remarks}[21.8.6]',
    "Apply together with the p. 284 entry that changes the matching \\end{remark} to \\end{remarks} (GLOBAL_ISSUES 28).")

add(283, "Remarques (21.8.6) (i), l. 1: 'Les conditions d'application de (21.8.5, (i))'",
    "'(21.8.5, (i))', the label inside the reference's parentheses", "\\sref{IV.21.8.5}, (i) prints '(21.8.5), (i)'",
    'punctuation', None, 'high',
    r'\sref{IV.21.8.5}, (i) sont en particulier', r'\sref{IV.21.8.5}[(i)] sont en particulier',
    "\\sref's third argument (GLOBAL_ISSUES 68).")

add(283, "Remarques (21.8.6) (i), l. 2: 'localement noethérien réduit n'ayant'",
    "'réduit' italic (crop p283_reduit_normalise.png)", "upright",
    'italics', None, 'high',
    r"noethérien réduit n'ayant", r"noethérien \emph{réduit} n'ayant",
    "Remark body judged as roman (document-wide remark font).")

add(283, "Remarques (21.8.6) (i), l. 3: 'X' son normalisé et que'",
    "'normalisé' italic (crop p283_reduit_normalise.png)", "upright",
    'italics', None, 'high',
    r"$X'$ son normalisé et", r"$X'$ son \emph{normalisé} et",
    "")

add(283, "Remarques (21.8.6) (i), l. 4: 'noethérien (II, 6.3.8);'",
    "single parentheses '(II, 6.3.8)' (page_283_s2.png)", "(\\sref[II]{II.6.3.8}) prints '((II, 6.3.8))'",
    'extra', None, 'high',
    r'(\sref[II]{II.6.3.8})', r'\sref[II]{II.6.3.8}',
    "\\sref prints its own parentheses (GLOBAL_ISSUES 107, ega4-21b line 657); its optional argument is bold, as the print's II.")

add(283, "Remarques (21.8.6) (i), l. 6: 'que l'on peut considérer comme connus.'",
    "'connus' (plural) (crop p283_connus.png)", "'connu'",
    'word', None, 'high',
    'comme connu.', 'comme connus.',
    "Rewording by the TeX; not a misprint: the plural refers to f_*(Div_{X'}) and N, the two terms of the extension.")

add(283, "Remarques (21.8.6) (i), end: 'les conditions d'application de (21.8.5, (ii)).'",
    "'(21.8.5, (ii))'", "\\sref{IV.21.8.5}, (ii) prints '(21.8.5), (ii)'",
    'punctuation', None, 'high',
    r'\sref{IV.21.8.5}, (ii).' + NL, r'\sref{IV.21.8.5}[(ii)].' + NL,
    "")

add(283, "Remarques (21.8.6) (ii), l. 1: 'de (21.8.5, (ii)) sont remplies et en outre'",
    "'(21.8.5, (ii))'", "prints '(21.8.5), (ii)'",
    'punctuation', None, 'high',
    r'\sref{IV.21.8.5}, (ii) sont remplies et en outre', r'\sref{IV.21.8.5}[(ii)] sont remplies et en outre',
    "")

add(283, "Remarques (21.8.6) (ii), l. 2: 'l'homomorphisme canonique global Γ(X, O_X) → Γ(X', O_{X'})'",
    "'global' italic (crop p283_global.png)", "upright",
    'italics', None, 'high',
    r'canonique global $\Gamma', r'canonique \emph{global} $\Gamma',
    "")

add(283, "Remarques (21.8.6) (iii), l. 1: 'de (21.8.5, (ii)) sont remplies, on voit'",
    "'(21.8.5, (ii))'", "prints '(21.8.5), (ii)'",
    'punctuation', None, 'high',
    r'\sref{IV.21.8.5}, (ii) sont remplies, on voit', r'\sref{IV.21.8.5}[(ii)] sont remplies, on voit',
    "")

add(283, "Remarques (21.8.6) (iii), l. 4: 'signifie qu'il n'existe qu'un seul point s' ∈ X''",
    "'un seul' italic (crop p283_unseul.png)", "upright",
    'italics', None, 'high',
    r"n'existe qu'un seul point", r"n'existe qu'\emph{un seul} point",
    "")

add(283, "Remarques (21.8.6) (iii), l. 9: 'l'anneau O'_{X,s} est semi-local'",
    "'semi-local' italic (crop p283_semilocal.png)", "upright",
    'italics', None, 'high',
    r'est semi-local (c' + "'" + r'est', r'est \emph{semi-local} (c' + "'" + r'est',
    "")

add(283, "Remarques (21.8.6) (iii), l. 9: 'lorsque le morphisme f est fini et dans le cas'",
    "'fini' italic (crop p283_semilocal.png)", "upright",
    'italics', None, 'high',
    r'le morphisme $f$ est fini et dans le cas', r'le morphisme $f$ est \emph{fini} et dans le cas',
    "The heavier look of 'Dans le cas général', 'évident', 'et dans le', 'cas général cela résulte de' on these lines is uneven impression (shapes unchanged, several words on three lines), not a wrong fount: not recorded.")

add(283, "Remarques (21.8.6) (iii), l. 10: 'cela résulte de (0_IV, 23.2.6))'",
    "bold 0 with a light subscript IV (crop p283_semilocal.png)", "\\sref[0] prints '(0, 23.2.6)'",
    'missing', None, 'high',
    r'\sref[0]{0.23.2.6}', r'\sref[$\mathbf{0}_{\mathrm{IV}}$]{0.23.2.6}',
    "")

add(283, "Remarques (21.8.6) (iii), l. 11: 'du groupe multiplicatif (k(s))*'",
    "parentheses around k(s) (crop p283_ks_star.png)", "k(s)^* without them",
    'formula', None, 'high',
    r'multiplicatif $\boldsymbol{k}(s)^*$ dans', r'multiplicatif $(\boldsymbol{k}(s))^*$ dans',
    "")

add(283, "Remarques (21.8.6) (iii), l. 12: 'des groupes multiplicatifs (k(s'_j))*'",
    "parentheses around k(s'_j) (crop p283_ksj_star.png)", "k(s'_j)^* without them",
    'formula', None, 'high',
    r"multiplicatifs $\boldsymbol{k}(s'_j)^*$, les", r"multiplicatifs $(\boldsymbol{k}(s'_j))^*$, les",
    "")

# ---------------------------------------------------------------- p. 284
add(284, "l. 2: 'sont égaux au corps F_2 à 2 éléments;'",
    "'au corps' and 'à 2 éléments' italic, F_2 bold upright (crop p284_deplus.png)", "all upright",
    'italics', None, 'high',
    r'sont égaux au corps $\bb{F}_2$ à $2$ éléments;', r'sont égaux \emph{au corps} $\bb{F}_2$ \emph{à $2$ éléments};',
    "The slightly heavier 'de plus,' after it (stroke run 6.0-6.7 px against 5.0-5.6 for its neighbours, inside the 5.1-6.2 px range of the words of the next line) is uneven impression, not a wrong fount: not recorded.")

add(284, "l. 5: 'est composé direct de corps isomorphes à k(s)'",
    "'composé direct de corps isomorphes à' italic (crop p284_italics.png)", "upright",
    'italics', None, 'high',
    r'est composé direct de corps isomorphes à $\boldsymbol{k}(s)$', r'est \emph{composé direct de corps isomorphes à} $\boldsymbol{k}(s)$',
    "")

add(284, "l. 6: 'qu'il est non ramifié aux points s'_j (17.4.1))'",
    "'non ramifié' italic (page_284_s1.png)", "upright",
    'italics', None, 'high',
    r'est non ramifié aux points', r'est \emph{non ramifié} aux points',
    "")

add(284, "end of Remarques (21.8.6)",
    "plural 'Remarques' (see p. 283)", "\\end{remark}",
    'word', None, 'high',
    r"par l'homomorphisme $\operatorname{Pic}(X)\to\operatorname{Pic}(X')$." + NL + r'\end{enumerate}' + NL + r'\end{remark}',
    r"par l'homomorphisme $\operatorname{Pic}(X)\to\operatorname{Pic}(X')$." + NL + r'\end{enumerate}' + NL + r'\end{remarks}',
    "Apply together with the p. 283 entry \\begin{remark}[21.8.6] -> \\begin{remarks}[21.8.6].")

add(284, "heading of 21.9: '21.9. Diviseurs sur les préschémas de dimension 1.'",
    "the title ends with a full stop (page_284_s2.png)", "no full stop",
    'punctuation', None, 'high',
    r'\subsection{Diviseurs sur les préschémas de dimension 1}', r'\subsection{Diviseurs sur les préschémas de dimension 1.}',
    "As the 21.8 title (p. 280).")

add(284, "(21.9.1), l. 4: 'un faisceau de groupes commutatifs sur X (0_I, 3.4.1);'",
    "bold 0 with a light subscript I (page_284_s2.png)", "\\sref[0] prints '(0, 3.4.1)'",
    'missing', None, 'high',
    r'\sref[0]{0.3.4.1}', r'\sref[$\mathbf{0}_{\mathrm I}$]{0.3.4.1}',
    "")

add(284, "(21.9.1), l. 6: 'on a ((i_x)_*(A(x))_y = A(x)'",
    "'((i_x)_*(A(x))_y': three closing parentheses for four opening ones (crop p284_paren1.png)",
    "'((i_x)_*(A(x)))_y' (silent correction)",
    'misprint_in_print', None, 'high',
    r'on a $((i_x)_*(A(x)))_y=A(x)$', r'on a $((i_x)_*(A(x))_y=A(x)$',
    "Unbalanced parentheses, printed the same way three times on this page (also the next entry and the first line of the proof of (21.9.2)). The TeX silently corrects them; restore the printed reading.",
    corrected=r'on a $((i_x)_*(A(x)))_y=A(x)$')

add(284, "(21.9.1), l. 7: 'et pour y ∉ {x}-bar, ((i_x)_*(A(x))_y = 0.'",
    "the same unbalanced '((i_x)_*(A(x))_y' (crop p284_paren2.png)", "balanced (silent correction)",
    'misprint_in_print', None, 'high',
    r'\overline{\{x\}}$, $((i_x)_*(A(x)))_y=0$.', r'\overline{\{x\}}$, $((i_x)_*(A(x))_y=0$.',
    "As in the entry above.",
    corrected=r'\overline{\{x\}}$, $((i_x)_*(A(x)))_y=0$.')

add(284, "Lemme (21.9.2), after the items: 'Lorsqu'il en est ainsi, pour tout x ∈ X_0'",
    "new indented paragraph, indented like the item labels (page_284_s4.png)",
    "the text follows \\end{enumerate} without a blank line, so it is set without the indent",
    'other', None, 'high',
    r'\end{enumerate}' + NL + r"Lorsqu'il en est ainsi", r'\end{enumerate}' + NL + NL + r"Lorsqu'il en est ainsi",
    "GLOBAL_ISSUES 80/99 pattern.")

add(284, "end of the page: printed p. 284 ends with 'Comme les points de X_0 sont fermés dans X, on a ((i_x)_*(A(x))_y = 0 pour tout'",
    "page_284_s4.png ends with '... on a ((i_x)_*(A(x))_y = 0 pour tout'; p. 285 begins with 'y ≠ x ∈ X_0; cette remarque' (crop p285_line1.png)",
    "\\oldpage[IV-4]{285} stands after \\begin{proof}, a line too early",
    'marker', None, 'high',
    r'\oldpage[IV-4]{285}' + NL + r'Comme les points', r'Comme les points',
    "OUTSIDE this page's segment: the old string is the start of the p. 285 segment (page_285.tex); boundary fix with p. 285. Marker move, part 1 of 2: apply together with the next entry.",
    target=285)

add(284, "end of the page: new position of \\oldpage[IV-4]{285}",
    "p. 285 begins with 'y ≠ x ∈ X_0;'", "(marker earlier, see the entry above)",
    'marker', None, 'high',
    r'pour tout $y\neq x\in X_0$;', r'pour tout' + NL + r'\oldpage[IV-4]{285}' + NL + r'$y\neq x\in X_0$;',
    "OUTSIDE this page's segment (text of page_285.tex). Marker move, part 2 of 2: mid-sentence break, no blank lines. Independent of the next entry (adjacent, no overlap).",
    target=285)

add(284, "proof of (21.9.2), l. 1 (printed on p. 284): 'on a ((i_x)_*(A(x))_y = 0 pour tout'",
    "the same unbalanced '((i_x)_*(A(x))_y' (crop p284_paren3.png)", "balanced (silent correction)",
    'misprint_in_print', None, 'high',
    r'on a $((i_x)_*(A(x)))_y=0$', r'on a $((i_x)_*(A(x))_y=0$',
    "OUTSIDE this page's segment: the text is printed on p. 284 but stands after \\oldpage[IV-4]{285} in the TeX (page_285.tex) until the marker move above. As in the two (21.9.1) entries.",
    corrected=r'on a $((i_x)_*(A(x)))_y=0$', target=285)


# ---------------------------------------------------------------- checks
def lf(path):
    return io.open(path, encoding='utf-8', newline='').read().replace('\r\n', '\n')


src = lf(SRC)
pages = {p: lf(RUN + 'page_%d.tex' % p) for p in range(279, 286)}
ok = True
for i, d in enumerate(F):
    fx = d['fix']
    if not fx:
        continue
    tgt = d['_target']
    n_page = pages[tgt].count(fx['old'])
    n_src = src.count(fx['old'])
    if n_page != 1 or n_src != 1:
        ok = False
        print('COUNT PROBLEM', i, d['page'], 'target', tgt, 'page count', n_page, 'src count', n_src, repr(fx['old'])[:80])
    if fx['old'] == fx['new']:
        ok = False
        print('NO-OP', i)

# sequential application on a copy of the source
cur = src
for i, d in enumerate(F):
    fx = d['fix']
    if not fx:
        continue
    c = cur.count(fx['old'])
    if c != 1:
        ok = False
        print('SEQ PROBLEM', i, d['page'], c, repr(fx['old'])[:80])
        continue
    cur = cur.replace(fx['old'], fx['new'])
io.open(RUN + 'crops_280_284/simulated_ega4-21b.tex', 'w', encoding='utf-8', newline='').write(cur)
print('checks ok' if ok else 'CHECKS FAILED', len(F), 'findings')

out = []
for d in F:
    e = dict(d)
    del e['_target']
    out.append(e)
if '--write' in sys.argv:
    io.open(OUT, 'w', encoding='utf-8', newline='\n').write(json.dumps(out, ensure_ascii=False, indent=1) + '\n')
    print('written', OUT)
