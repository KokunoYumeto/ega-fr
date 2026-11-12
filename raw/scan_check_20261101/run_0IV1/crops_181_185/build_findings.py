import json, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = r'user\Documents\ega_scan_check_20261101\run_0IV1'
OUT = RUN + r'\findings_181_185.json'
NL = '¶'  # newline placeholder in the raw strings below

def page_text(p):
    with open(rf'{RUN}\page_{p:03d}.tex', encoding='utf-8', newline='') as fh:
        return fh.read().replace('\r\n', '\n')

F = []
def add(page, where, scan, tex, kind, conv, conf, old, new, note='', corrected=None, nofix=False):
    d = {'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind,
         'convention': conv, 'confidence': conf}
    if nofix:
        d['fix'] = None
    else:
        d['fix'] = {'old': old.replace(NL, '\n'), 'new': new.replace(NL, '\n')}
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    F.append(d)

MK = r'\oldpage[0\textsubscript{IV-1}]'

# (page 180/181 boundary: the blank line before the p. 181 marker is already filed in findings_176_180.json)

# ---------------- page 181 ----------------
add(181, "top of p. 181: 'on a d(E/L_0, k/k_0)=d(E/K_0, k/k_0)=d(E/M_0, k/k_0), d'où, par une dernière application'",
    "formula set inline in the running text", "displayed with \\[ \\]", 'other', None, 'high',
    r"  on a¶  \[¶    d(E/L_0,k/k_0)=d(E/K_0,k/k_0)=d(E/M_0,k/k_0),¶  \]¶  d'où",
    r"  on a¶  $d(E/L_0,k/k_0)=d(E/K_0,k/k_0)=d(E/M_0,k/k_0)$,¶  d'où",
    "Layout only (GLOBAL_ISSUES 21); formula and connecting words match.")
add(181, "display after 'par une dernière application de (21.6.4.2),'",
    "δ=d(E/M_0, N/k_0)⩾0, with no punctuation after it (enlarged crop)",
    "\\delta=d(E/M_0,N/k_0), : '⩾0' missing and a comma added", 'missing', None, 'high',
    r"\delta=d(E/M_0,N/k_0),", r"\delta=d(E/M_0,N/k_0)\geqslant0",
    "The same edit drops the comma the print does not have.")
add(181, "proof of (21.9.6)(ii): 'Or, on a' after the display ⋂_α N_α=k_0(M_0^p).",
    "'Or, on a' begins a new indented paragraph", "no blank line after \\]: no paragraph break",
    'other', None, 'high',
    r"  \]¶  Or, on a", r"  \]¶¶  Or, on a",
    "Missing paragraph break after a display (as GLOBAL_ISSUES 47).")
add(181, "proof of Lemme (21.9.6.7): 'on a k_0^p(K_0^p((T_1, ..., T_r)))=K_0^p((T_1, ..., T_r)). Si (c_i)'",
    "formula set inline in the running text", "displayed with \\[ \\] (and \\bigl( \\bigr))", 'other', None, 'high',
    r"on a¶  \[¶    k_0^p\bigl(K_0^p((T_1,\ldots,T_r))\bigr)¶    =K_0^p((T_1,\ldots,T_r)).¶  \]¶  Si",
    r"on a¶  $k_0^p(K_0^p((T_1,\ldots,T_r)))=K_0^p((T_1,\ldots,T_r))$.¶  Si",
    "Layout only: inline, normal-size parentheses.")
add(181, "Remarque (21.9.7): 'de sorte que les X_n^p forment une p-base de k_0 sur F_p'",
    "X_n^p, with superscript p (enlarged crop)", "$X_n$: the TeX silently corrects", 'misprint_in_print', None, 'high',
    r"les $X_n$ forment", r"les $X_n^p$ forment",
    "Misprint: the indeterminates X_n form a p-basis of k_0=F_p(X_n) over F_p; the X_n^p lie in k_0^p and cannot. The fix restores the printed reading in the diplomatic text.",
    corrected=r"les $X_n$ forment")
add(181, "Remarque (21.9.7): 'où y est racine du polynôme Y^p − Σ_{n=0}^∞ X_n T^{np} de L_0[Y]'",
    "polynomial set inline at the end of the line (Σ with its limits above and below)",
    "displayed with \\[ \\]", 'other', None, 'high',
    r"polynôme¶\[¶  Y^p-\sum_{n=0}^{\infty}X_nT^{np}¶\]¶de $L_0[Y]$",
    r"polynôme $Y^p-\sum_{n=0}^{\infty}X_nT^{np}$¶de $L_0[Y]$",
    "Layout only; the formula and 'de L_0[Y]' match.")
add(181, "end of p. 181, inside Proposition (21.9.8): 'dont le corps résiduel | est une extension finie de K_0' (p. 182)",
    "the statement continues on p. 182 in the same paragraph",
    "blank line before \\oldpage[0\\textsubscript{IV-1}]{182}: a paragraph break inside the statement",
    'other', None, 'high',
    r"dont le corps résiduel¶¶", r"dont le corps résiduel¶",
    "GLOBAL_ISSUES 20 (blank lines around a mid-sentence page marker).")

# ---------------- page 182 ----------------
add(182, "Proposition (21.9.8): 'soit k(𝔭) le corps résiduel de A en 𝔭'",
    "bold italic k", "$k(\\mathfrak p)$", 'convention', 1, 'high',
    r"soit $k(\mathfrak p)$ le corps", r"soit $\boldsymbol{k}(\mathfrak p)$ le corps", "")
add(182, "(21.9.8.1), first term: subscript of rg_{k(𝔭)}",
    "bold k, upright in the subscript (enlarged crop)", "\\operatorname{rg}_{k(\\mathfrak p)}", 'convention', 1, 'high',
    r"&\operatorname{rg}_{k(\mathfrak p)}", r"&\operatorname{rg}_{\mathbf{k}(\mathfrak p)}",
    "Bold upright in subscripts, bold italic on the line (GLOBAL_ISSUES 48).")
add(182, "(21.9.8.1), first term: '⊗_{A/𝔭} k(𝔭)'",
    "bold italic k", "\\otimes_{A/\\mathfrak p}k(\\mathfrak p)", 'convention', 1, 'high',
    r"\otimes_{A/\mathfrak p}k(\mathfrak p)", r"\otimes_{A/\mathfrak p}\boldsymbol{k}(\mathfrak p)", "")
add(182, "(21.9.8.1), right side: subscript of rg_{k(𝔭)}",
    "bold k, upright in the subscript", "\\operatorname{rg}_{k(\\mathfrak p)}", 'convention', 1, 'high',
    r"+\operatorname{rg}_{k(\mathfrak p)}", r"+\operatorname{rg}_{\mathbf{k}(\mathfrak p)}",
    "GLOBAL_ISSUES 48.")
add(182, "(21.9.8.1), right side: subscript of Υ_{k(𝔭)/k_0}",
    "bold k, upright in the subscript (k_0 plain)", "\\Upsilon_{k(\\mathfrak p)/k_0}", 'convention', 1, 'high',
    r"\Upsilon_{k(\mathfrak p)/k_0}", r"\Upsilon_{\mathbf{k}(\mathfrak p)/k_0}",
    "GLOBAL_ISSUES 48.")
add(182, "proof of (21.9.8): 'on posera alors E=k(𝔭), corps des fractions de A'",
    "bold italic k", "$E=k(\\mathfrak p)$", 'convention', 1, 'high',
    r"$E=k(\mathfrak p)$", r"$E=\boldsymbol{k}(\mathfrak p)$", "")
add(182, "Proposition (21.9.8): 'Supposons en outre que [k_0 : k_0^p]<+∞' after the display (21.9.8.1)",
    "'Supposons en outre' begins a new indented paragraph", "no blank line after \\end{equation}",
    'other', None, 'high',
    r"\end{equation}¶Supposons en outre", r"\end{equation}¶¶Supposons en outre",
    "Missing paragraph break after a display (as GLOBAL_ISSUES 47).")
add(182, "Proposition (21.9.8), last sentence: 'les deux membres de (21.9.8.1) sont égaux'",
    "reference (21.9.8.1) upright in the italic statement", "(21.9.8.1) comes out italic", 'convention', 6, 'high',
    r"membres de (21.9.8.1) sont égaux.", r"membres de \textup{(21.9.8.1)} sont égaux.", "")
add(182, "proof of (21.9.8): 'on peut se borner au cas où A est intègre et 𝔭=0'",
    "'intègre' in italics", "intègre upright", 'italics', None, 'high',
    r"$A$ est intègre et", r"$A$ est \emph{intègre} et", "")
add(182, "proof of (21.9.8): 'ce qui entraîne que E est une extension finie du corps des fractions'",
    "second 'finie' in italics, like the first", "finie upright", 'italics', None, 'high',
    r"est une extension finie du", r"est une extension \emph{finie} du", "")
add(182, "§ 22 introduction, label a)",
    "label a) in italics (parenthesis slanted too)", "\\item[a)] upright", 'italics', None, 'high',
    r"\item[a)] Les critères", r"\item[\textit{a)}] Les critères",
    "OUTSIDE THE PAGE SEGMENT: ega0-22-fr.tex before its first page marker (hand edit). Lettered labels: GLOBAL_ISSUES 16/22.")
add(182, "§ 22 introduction, label b)",
    "label b) in italics", "\\item[b)] upright", 'italics', None, 'high',
    r"\item[b)] Le théorème", r"\item[\textit{b)}] Le théorème",
    "OUTSIDE THE PAGE SEGMENT (hand edit), as a).")
add(182, "§ 22 introduction, label c) (printed at the top of p. 183)",
    "label c) in italics", "\\item[c)] upright", 'italics', None, 'high',
    r"\item[c)] Le critère", r"\item[\textit{c)}] Le critère",
    "OUTSIDE THE PAGE SEGMENT (hand edit). Printed on p. 183; the line stands before the misplaced p. 183 marker.")
add(182, "page break 182/183: '... des propriétés « fines » des | anneaux locaux faite au chap. IV, § 7.'",
    "p. 182 ends with 'des propriétés « fines » des'; p. 183 begins 'anneaux locaux faite au chap. IV, § 7. On ne possède ...', then c) and the heading 22.1",
    "\\oldpage[0\\textsubscript{IV-1}]{183} stands after \\end{enumerate}, before \\subsection{Relèvement ...}", 'marker', None, 'high',
    r"«~fines~» des¶  anneaux locaux faite", "«~fines~» des¶" + MK + r"{183}¶  anneaux locaux faite",
    "OUTSIDE THE PAGE SEGMENT: ega0-22-fr.tex before its first page marker (hand edit). Move, part 1 of 2: inserts the marker; the page-183 marker finding removes the old one. Apply both. Apply after the c) label fix or before it: they do not overlap.")

# ---------------- page 183 ----------------
add(183, "top of page_183.tex: \\oldpage[0\\textsubscript{IV-1}]{183} before \\subsection{Relèvement de la lissité formelle}",
    "printed p. 183 begins inside item b) of the § 22 introduction ('anneaux locaux faite au chap. IV, § 7.')",
    "marker after \\end{enumerate}", 'marker', None, 'high',
    MK + r"{183}¶¶\subsection{Relèvement", r"\subsection{Relèvement",
    "Move, part 2 of 2: removes the old marker; apply only together with the page-182 marker finding (insertion before 'anneaux locaux faite'). The blank line after \\end{enumerate} stays.")
add(183, "heading '22.1. Relèvement de la lissité formelle.'",
    "title ends with a full stop", "\\subsection{Relèvement de la lissité formelle} without it", 'punctuation', None, 'high',
    r"de la lissité formelle}", r"de la lissité formelle.}",
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop).")
add(183, "Théorème (22.1.1), label (i)", "label (i) upright", "\\item[(i)] comes out italic in the theorem", 'convention', 6, 'high',
    r"\item[(i)] Supposons", r"\item[\textup{(i)}] Supposons", "GLOBAL_ISSUES 16.")
GR = {'alpha': 'α', 'beta': 'β', 'gamma': 'γ', 'delta': 'δ'}
for g, nxt in (('alpha', r" $\mathfrak J/\mathfrak J^2$"), ('beta', " L'homomorphisme canonique"),
               ('gamma', " L'homomorphisme caractéristique"), ('delta', r" Le $C$-module")):
    add(183, f"Théorème (22.1.1)(i), label {GR[g]})", f"label {GR[g]}) with an upright parenthesis",
        f"\\item[$\\{g}$)]: the parenthesis comes out italic in the theorem", 'convention', 6, 'medium',
        r"\item[$\%s$)]" % g + nxt, r"\item[\textup{$\%s$)}]" % g + nxt,
        "Same form as the (i)/(ii) labels; only the parenthesis changes face.")
add(183, "Théorème (22.1.1) β): 'S•_C(𝔍/𝔍²) → gr•_𝔍(B)' (S)",
    "raised bullet (enlarged crop)", "\\mathbf S_C^*", 'symbol', None, 'high',
    r"\mathbf S_C^*", r"\mathbf S_C^\bullet", "GLOBAL_ISSUES 60: holds for § 22 too.")
add(183, "Théorème (22.1.1) β): 'S•_C(𝔍/𝔍²) → gr•_𝔍(B)' (gr)",
    "raised bullet", "\\operatorname{gr}_{\\mathfrak J}^*", 'symbol', None, 'high',
    r"\operatorname{gr}_{\mathfrak J}^*", r"\operatorname{gr}_{\mathfrak J}^\bullet", "GLOBAL_ISSUES 60.")
add(183, "Théorème (22.1.1) β): '(19.5.2) est bijectif'",
    "reference upright in the italic statement", "(19.5.2) comes out italic", 'convention', 6, 'high',
    r"(19.5.2)", r"\textup{(19.5.2)}", "")
add(183, "Théorème (22.1.1) γ): 'χ : Υ_{C/A/Λ} → 𝔍/𝔍²'",
    "Υ_{C/A/Λ} (A with crossbar, enlarged crop)", "\\Upsilon_{C/B/\\Lambda}", 'formula', None, 'high',
    r"\Upsilon_{C/B/\Lambda}", r"\Upsilon_{C/A/\Lambda}",
    "The proof's 'γ) équivaut à Υ^C_{B/A/Λ}=0' via (20.6.22.1) fits the printed Υ_{C/A/Λ}.")
add(183, "Théorème (22.1.1) γ): '(20.6.20) est injectif'",
    "reference upright in the italic statement", "(20.6.20) comes out italic", 'convention', 6, 'high',
    r"(20.6.20)", r"\textup{(20.6.20)}", "")
add(183, "Théorème (22.1.1)(i), conclusion: 'Alors B, muni de la topologie 𝔍-préadique, est une A-algèbre formellement lisse.'",
    "A-algèbre (A with crossbar, enlarged crop)", "$\\Lambda$-algèbre", 'symbol', None, 'high',
    r"préadique, est une¶  $\Lambda$-algèbre", r"préadique, est une¶  $A$-algèbre",
    "The proof of (i) shows that B is a formally smooth A-algebra.")
add(183, "Théorème (22.1.1), label (ii)", "label (ii) upright", "\\item[(ii)] comes out italic", 'convention', 6, 'high',
    r"\item[(ii)] Inversement", r"\item[\textup{(ii)}] Inversement", "GLOBAL_ISSUES 16.")
add(183, "Théorème (22.1.1)(ii): 'supposons que B soit une A-algèbre formellement lisse pour la topologie 𝔍-préadique'",
    "A-algèbre (enlarged crop); the next 'et que A soit une Λ-algèbre' has Λ", "$\\Lambda$-algèbre", 'symbol', None, 'high',
    r"supposons que $B$ soit une $\Lambda$-algèbre", r"supposons que $B$ soit une $A$-algèbre", "")
add(183, "Théorème (22.1.1)(ii): 'Alors les conditions α), β), γ), δ) de (i) sont vérifiées.'",
    "the labels α), β), γ), δ) and (i) are upright in the italic statement", "parentheses and (i) come out italic",
    'convention', 6, 'medium',
    r"conditions $\alpha$), $\beta$), $\gamma$), $\delta$) de (i) sont",
    r"conditions \textup{$\alpha$), $\beta$), $\gamma$), $\delta$)} de \textup{(i)} sont", "")
add(183, "proof of (22.1.1), condition γ'): 'L'homomorphisme u_{B/A/Λ}⊗1_C : Ω¹_{A/Λ}⊗_A C → Ω¹_{B/Λ}⊗_B C est injectif.'",
    "formula set inline in the line of γ')", "displayed with \\[ \\]", 'other', None, 'high',
    r"  \[¶    u_{B/A/\Lambda}\otimes 1_C:¶    \Omega^1_{A/\Lambda}\otimes_A C¶    \longrightarrow \Omega^1_{B/\Lambda}\otimes_B C¶  \]¶",
    r"  $u_{B/A/\Lambda}\otimes 1_C:\Omega^1_{A/\Lambda}\otimes_A C\to\Omega^1_{B/\Lambda}\otimes_B C$¶",
    "Layout only. Does not overlap the two italics fixes of γ').")
add(183, "proof of (22.1.1), γ'): 'L'homomorphisme'",
    "italic (the words of γ') are italic, the label upright)", "upright (proof environment)", 'convention', 6, 'high',
    r"\item[$\gamma'$)] L'homomorphisme", r"\item[$\gamma'$)] \emph{L'homomorphisme}", "")
add(183, "proof of (22.1.1), γ'): 'est injectif.'",
    "italic", "upright (proof environment)", 'convention', 6, 'high',
    r"  est injectif.¶\end{enumerate}", r"  \emph{est injectif}.¶\end{enumerate}", "")
add(183, "proof of (22.1.1)(i): 'de B-modules topologiques u_{B/A/Λ} : Ω¹_{A/Λ}⊗_A B → Ω¹_{B/Λ} est formellement inversible à gauche'",
    "formula set inline in the running text", "displayed with \\[ \\]", 'other', None, 'high',
    r"\[¶  u_{B/A/\Lambda}:\Omega^1_{A/\Lambda}\otimes_A B¶  \longrightarrow\Omega^1_{B/\Lambda}¶\]¶",
    r"$u_{B/A/\Lambda}:\Omega^1_{A/\Lambda}\otimes_A B\to\Omega^1_{B/\Lambda}$¶",
    "Layout only.")
add(183, "proof of (22.1.1)(i): 'que u_{B/A/Λ}⊗1_C soit inversible à gauche.'",
    "'inversible à gauche' in italics", "upright", 'italics', None, 'high',
    r"\otimes 1_C$ soit inversible à gauche.", r"\otimes 1_C$ soit \emph{inversible à gauche}.", "")
add(183, "proof of (22.1.1)(i): 'la suite exacte précédente est scindée'",
    "'scindée' in italics", "upright", 'italics', None, 'high',
    r"est scindée,", r"est \emph{scindée},", "")

# ---------------- page 184 ----------------
add(184, "page break 183/184 inside the proof of (22.1.1)(ii): '... (20.7.2) montre que u_{B/A/Λ} est formellement | inversible à gauche, donc'",
    "p. 183 ends with 'montre que u_{B/A/Λ} est formellement'; p. 184 begins 'inversible à gauche, donc u_{B/A/Λ}⊗1_C ...'",
    "\\oldpage[0\\textsubscript{IV-1}]{184} stands before '(ii) Si $B$ ...', so the end of p. 183 is in the p. 184 segment",
    'marker', None, 'high',
    r"est formellement inversible à gauche, donc", r"est formellement¶" + MK + r"{184}¶inversible à gauche, donc",
    "Move, part 1 of 2: inserts the marker; the next finding removes the old one. Order: the two (ii) letter fixes below first (their text then moves into the p. 183 segment), then this insertion, then the removal.")
add(184, "top of page_184.tex: old marker before '(ii) Si B ...'",
    "'(ii) Si B est une A-algèbre ...' is printed at the foot of p. 183", "marker before (ii)", 'marker', None, 'high',
    MK + r"{184}¶¶(ii)", r"(ii)",
    "Move, part 2 of 2: apply after part 1. The blank line after 'ce qui achève de prouver (i).' (end of page_183.tex) stays: (ii) is a new paragraph in the print.")
add(184, "proof of (22.1.1)(ii) (printed at the foot of p. 183): 'Si B est une A-algèbre formellement lisse pour la topologie 𝔍-préadique'",
    "A-algèbre (enlarged crop)", "$\\Lambda$-algèbre", 'symbol', None, 'high',
    r"Si $B$ est une $\Lambda$-algèbre", r"Si $B$ est une $A$-algèbre",
    "Printed on p. 183; the text lies in the p. 184 segment until the marker moves: apply before the p. 184 marker move.")
add(184, "proof of (22.1.1)(ii) (printed on p. 183): 'B est une Λ-algèbre formellement lisse pour la topologie 𝔍-préadique (19.3.5, (ii))'",
    "Λ-algèbre (no crossbar, enlarged crop)", "$A$-algèbre", 'symbol', None, 'high',
    r"discrète, $B$ est une $A$-algèbre", r"discrète, $B$ est une $\Lambda$-algèbre",
    "Apply before the p. 184 marker move. With the previous fix the sentence reads as printed: B formally smooth over A and A over Λ give B formally smooth over Λ (19.3.5, (ii)).")
add(184, "Corollaire (22.1.2), label a)", "label a) upright", "\\item[a)] comes out italic in the corollary", 'convention', 6, 'high',
    r"\item[a)] $B$ est une", r"\item[\textup{a)}] $B$ est une", "")
add(184, "Corollaire (22.1.2), label b)", "label b) upright", "\\item[b)] comes out italic", 'convention', 6, 'high',
    r"\item[b)] L'homomorphisme", r"\item[\textup{b)}] L'homomorphisme", "")
add(184, "(22.1.2.1): 'S•_K(𝔪/𝔪²) → gr•_𝔪(B)' (S)", "raised bullet (enlarged crop)", "\\mathbf S_K^*", 'symbol', None, 'high',
    r"\mathbf S_K^*", r"\mathbf S_K^\bullet", "GLOBAL_ISSUES 60.")
add(184, "(22.1.2.1): 'S•_K(𝔪/𝔪²) → gr•_𝔪(B)' (gr)", "raised bullet", "\\operatorname{gr}_{\\mathfrak m}^*", 'symbol', None, 'high',
    r"\operatorname{gr}_{\mathfrak m}^*", r"\operatorname{gr}_{\mathfrak m}^\bullet", "GLOBAL_ISSUES 60.")
add(184, "(22.1.2.2): 'χ : Υ_{K/A/Λ} → 𝔪/𝔪²'", "Υ_{K/A/Λ} (enlarged crop)", "\\Upsilon_{K/B/\\Lambda}", 'formula', None, 'high',
    r"\Upsilon_{K/B/\Lambda}", r"\Upsilon_{K/A/\Lambda}", "As γ) of (22.1.1), p. 183.")
add(184, "(22.1.3.1): the condition is printed in italics",
    "italic statement (roman body of the remark around it)",
    "no font change: the env body follows the remark environment (roman once the remark is set roman)",
    'convention', 6, 'medium',
    r"\label{0.22.1.3.1-fr}¶Étant donnés", r"\label{0.22.1.3.1-fr}¶\itshape Étant donnés",
    "Judged as if the remark body were roman (document-wide remark item); with the current italic remark the output does not change. Same form as the EGA II p. 165 fix (\\itshape at the start of an env body).")
add(184, "(22.1.3.1): 'tout A-homomorphisme v : B → E/𝔟,'", "A-homomorphisme (enlarged crop)", "$\\Lambda$-homomorphisme",
    'symbol', None, 'high',
    r"$\Lambda$-homomorphisme $v:B\to E/", r"$A$-homomorphisme $v:B\to E/", "")
add(184, "(22.1.3.1): 'v : B → E/𝔟, qui, par passage aux quotients'", "comma after E/𝔟 (enlarged crop)", "no comma",
    'punctuation', None, 'high',
    r"\mathfrak b$ qui,", r"\mathfrak b$, qui,", "")
add(184, "(22.1.3.1): 'se factorise en B →^w E/𝔫^k → E/𝔟, où w est un A-homomorphisme.'",
    "formula set inline in the running text", "displayed with \\[ \\]", 'other', None, 'high',
    r"\[¶  B\xrightarrow{w}E/\mathfrak n^k\longrightarrow E/\mathfrak b,¶\]¶",
    r"$B\xrightarrow{w}E/\mathfrak n^k\to E/\mathfrak b$,¶", "Layout only.")
add(184, "(22.1.3.1): 'où w est un A-homomorphisme.'", "A-homomorphisme (enlarged crop)", "$\\Lambda$-homomorphisme",
    'symbol', None, 'high',
    r"où $w$ est un $\Lambda$-homomorphisme.", r"où $w$ est un $A$-homomorphisme.", "")
add(184, "(22.1.3.2): the condition is printed in italics",
    "italic statement", "no font change (follows the remark environment)", 'convention', 6, 'medium',
    r"\label{0.22.1.3.2-fr}¶Si $F$", r"\label{0.22.1.3.2-fr}¶\itshape Si $F$",
    "As (22.1.3.1).")
add(184, "(22.1.3.2): '(« algèbre des nombres duaux sur K »)'",
    "parenthesis printed roman inside the italic condition", "italic (remark environment; \\itshape after the previous fix)",
    'convention', 6, 'high',
    r"(«~algèbre des nombres duaux sur¶$K$~»)", r"\textup{(«~algèbre des nombres duaux sur¶$K$~»)}", "")
add(184, "(22.1.3.2): 'alors tout A-homomorphisme v : B → K'", "A-homomorphisme (enlarged crop)", "$\\Lambda$-homomorphisme",
    'symbol', None, 'high',
    r"$\Lambda$-homomorphisme $v:B\to K$", r"$A$-homomorphisme $v:B\to K$", "")
add(184, "(22.1.3.2): 'se factorise en B →^w F → K, où w est'", "formula set inline", "displayed with \\[ \\]",
    'other', None, 'high',
    r"\[¶  B\xrightarrow{w}F\longrightarrow K,¶\]¶", r"$B\xrightarrow{w}F\to K$,¶", "Layout only.")
add(184, "(22.1.3.2): 'où w est un A-homomorphisme (pour la structure de A-algèbre sur F définie par ρ)'",
    "A-homomorphisme (enlarged crop)", "$\\Lambda$-homomorphisme", 'symbol', None, 'high',
    r"où $w$ est un $\Lambda$-homomorphisme (pour", r"où $w$ est un $A$-homomorphisme (pour", "")
add(184, "Remarque (22.1.3), proof: 'l'homomorphisme canonique u_{B/A/Λ}⊗1_K : Ω¹_{A/Λ}⊗_A K → Ω¹_{B/Λ}⊗_B K est injectif'",
    "formula set inline in the running text", "displayed with \\[ \\]", 'other', None, 'high',
    r"\[¶  u_{B/A/\Lambda}\otimes1_K:¶  \Omega^1_{A/\Lambda}\otimes_AK¶  \longrightarrow\Omega^1_{B/\Lambda}\otimes_BK¶\]¶",
    r"$u_{B/A/\Lambda}\otimes1_K:\Omega^1_{A/\Lambda}\otimes_AK\to\Omega^1_{B/\Lambda}\otimes_BK$¶", "Layout only.")
add(184, "Remarque (22.1.3): 'l'homomorphisme canonique Dér_Λ(B, L) → Dér_Λ(Λ, L) est surjectif'",
    "Dér_Λ(Λ, L): second argument Λ (no crossbar, enlarged crop)", "Dér_Λ(A, L): the TeX silently corrects",
    'misprint_in_print', None, 'high',
    r"_\Lambda(A,L)", r"_\Lambda(\Lambda,L)",
    "Misprint: Dér_Λ(Λ, L)=0, so the printed statement is empty; the restriction map goes to Dér_Λ(A, L), as in the next line (Dér_Λ(B, K) → Dér_Λ(A, K)). Restore the printed reading in the diplomatic text.",
    corrected=r"\operatorname{D\acute{e}r}_\Lambda(A,L)")
add(184, "Remarque (22.1.3): 'est surjectif (en vertu de (20.4.8))'",
    "'est surjectif' both in italics", "only 'surjectif' in \\emph", 'italics', None, 'high',
    r"est¶\emph{surjectif}", r"\emph{est¶surjectif}", "Judged as if the remark body were roman.")
add(184, "(22.1.3.3): the condition is printed in italics",
    "italic statement", "no font change (follows the remark environment)", 'convention', 6, 'medium',
    r"\label{0.22.1.3.3-fr}¶Pour toute", r"\label{0.22.1.3.3-fr}¶\itshape Pour toute", "As (22.1.3.1).")
add(184, "(22.1.3.3): 'Pour toute A-algèbre locale artinienne E'", "A-algèbre (enlarged crop)", "$\\Lambda$-algèbre",
    'symbol', None, 'high',
    r"$\Lambda$-algèbre locale", r"$A$-algèbre locale",
    "Proposition (22.1.4), p. 185, applies (22.1.3.3) to A-homomorphisms (A a field k, Λ its prime field).")
add(184, "(22.1.3.3): 'artinienne'", "printed roman inside the italic condition", "italic", 'convention', 6, 'high',
    r"artinienne $E$ de corps", r"\textup{artinienne} $E$ de corps", "")
add(184, "(22.1.3.3): 'égal à K'", "'égal à' printed roman inside the italic condition", "italic", 'convention', 6, 'high',
    r"résiduel égal à¶$K$, et tout", r"résiduel \textup{égal à}¶$K$, et tout", "")
add(184, "(22.1.3.3): 'tout A-homomorphisme B → E/𝔯'", "A-homomorphisme (enlarged crop)", "$\\Lambda$-homomorphisme",
    'symbol', None, 'high',
    r"$\Lambda$-homomorphisme $B\to E/\mathfrak r$", r"$A$-homomorphisme $B\to E/\mathfrak r$", "")
add(184, "(22.1.3.3): 'où u est un A-homomorphisme.'", "A-homomorphisme (enlarged crop)", "$\\Lambda$-homomorphisme",
    'symbol', None, 'high',
    r"où $u$ est un¶$\Lambda$-homomorphisme.", r"où $u$ est un¶$A$-homomorphisme.", "")

# ---------------- page 185 ----------------
add(185, "Proposition (22.1.4): 'k (resp. K) le corps résiduel'", "'(resp. K)' printed roman in the italic statement", "italic",
    'convention', 6, 'high', r"$k$ (resp. $K$)", r"$k$ \textup{(resp. $K$)}", "")
add(185, "Proposition (22.1.4): 'de A (resp. B).'", "'(resp. B)' printed roman", "italic", 'convention', 6, 'high',
    r"de $A$ (resp. $B$)", r"de $A$ \textup{(resp. $B$)}", "")
add(185, "Proposition (22.1.4): 'pour tout anneau local artinien C'", "'artinien' printed roman", "italic", 'convention', 6, 'high',
    r"local artinien $C$", r"local \textup{artinien} $C$", "")
add(185, "Proposition (22.1.4): 'de corps résiduel égal à K'", "'égal à' printed roman", "italic", 'convention', 6, 'high',
    r"résiduel égal à¶$K$, tout homomorphisme", r"résiduel \textup{égal à}¶$K$, tout homomorphisme", "")
add(185, "Proposition (22.1.4): 'se factorise en B →^f C → C/𝔍, où f est'", "formula set inline at the end of the line",
    "displayed with \\[ \\]", 'other', None, 'high',
    r"\[¶  B\xrightarrow{f}C\longrightarrow C/\mathfrak J,¶\]¶", r"$B\xrightarrow{f}C\to C/\mathfrak J$,¶", "Layout only.")
add(185, "proof of (22.1.4): '... et de (19.6.1). Dans le cas général, posons'",
    "same paragraph, same line", "blank line: paragraph break", 'other', None, 'high',
    r"et de (19.6.1).¶¶Dans le cas général", r"et de (19.6.1).¶Dans le cas général", "")
add(185, "proof of (22.1.4): '... d'après ce que l'on vient de voir. Appliquant (19.7.2) et (19.7.1),'",
    "same paragraph, same line", "blank line: paragraph break", 'other', None, 'high',
    r"vient de voir.¶¶Appliquant", r"vient de voir.¶Appliquant", "")
add(185, "proof of (22.1.4): 'et un k-isomorphisme u'_0 : B'_0=B'⊗_A k ⥲ B_0. Soit v'_0'",
    "formula set inline in the running text", "displayed with \\[ \\]", 'other', None, 'high',
    r"\[¶  u'_0:B'_0=B'\otimes_Ak\xrightarrow{\sim}B_0.¶\]¶", r"$u'_0:B'_0=B'\otimes_Ak\xrightarrow{\sim}B_0$.¶", "Layout only.")
add(185, "proof of (22.1.4): 'soit w_j : B/(𝔫^{j+1}+𝔪B) → B'/(𝔫'^{j+1}+𝔪B') l'homomorphisme déduit'",
    "formula set inline in the running text", "displayed with \\[ \\]", 'other', None, 'high',
    r"\[¶  w_j:B/(\mathfrak n^{j+1}+\mathfrak mB)¶  \longrightarrow B'/(\mathfrak n'^{j+1}+\mathfrak mB')¶\]¶",
    r"$w_j:B/(\mathfrak n^{j+1}+\mathfrak mB)\to B'/(\mathfrak n'^{j+1}+\mathfrak mB')$¶", "Layout only.")
add(185, "end of p. 185: '... répondra à la question. Or, la formation par récurrence de v_j résulte de l'hypothèse sur B et du' (p. 186 begins 'même raisonnement')",
    "same paragraph, no break; 'Or, la formation ... sur B et du' is the last line of p. 185",
    "blank line, \\oldpage[0\\textsubscript{IV-1}]{186}, blank line, then 'Or, la formation ... et du' (in page_186.tex)",
    'marker', None, 'high', None, None,
    "No edit here: findings_186_190.json already has the two edits this needs (its page-185 entry removing the blank line before the marker, and its page-186 entry moving the marker after 'et du'). Apply those two together, once.",
    nofix=True)

# ---------------- verification ----------------
ok = True
cache = {}
for i, d in enumerate(F):
    fx = d['fix']
    if fx is None:
        continue
    p = d['page']
    if p not in cache:
        cache[p] = page_text(p)
    n = cache[p].count(fx['old'])
    if n != 1:
        ok = False
        print('COUNT', n, 'page', p, repr(fx['old'])[:150])
    if fx['old'] == fx['new']:
        ok = False
        print('NOCHANGE', p, repr(fx['old'])[:100])

# overlap check per page: no two olds overlap in the page text
from collections import defaultdict
spans = defaultdict(list)
for i, d in enumerate(F):
    fx = d['fix']
    if fx is None:
        continue
    t = cache[d['page']]
    s = t.find(fx['old'])
    spans[d['page']].append((s, s + len(fx['old']), i))
for p, lst in spans.items():
    lst.sort()
    for a, b in zip(lst, lst[1:]):
        if b[0] < a[1]:
            ok = False
            print('OVERLAP page', p, F[a[2]]['where'][:60], '|', F[b[2]]['where'][:60])

print('findings:', len(F), 'ok' if ok else 'PROBLEMS')
counts = defaultdict(lambda: [0, 0, 0])
for d in F:
    k = 1 if d['kind'] == 'convention' else 2 if d['kind'] == 'misprint_in_print' else 0
    counts[d['page']][k] += 1
for p in sorted(counts):
    print(p, '%d/%d/%d' % tuple(counts[p]))
if ok:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
    print('written', OUT)
