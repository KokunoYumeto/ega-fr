# Builds findings_197_201.json for the EGA III part 2 scan check (pages 197-201).
# Strings use the marker "¶" for a line break (LF); everything else is literal LaTeX.
import json
import pathlib
import sys

RUN = pathlib.Path(__file__).resolve().parent.parent
OUT = RUN / "findings_197_201.json"
NL = "¶"


def s(x):
    return None if x is None else x.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, nofix=False):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if nofix else {"old": s(old), "new": s(new)})
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


LAYOUT = "Layout: the print sets this formula in the running text; the TeX displays it. The formula itself matches."

# ---------------------------------------------------------------- page 197
p = 197
add(p, "proof of the lemma in Remarque (7.6.11), first sentence", "0→Tor_1^A(B_0, k)→Z_1⊗k→P_1⊗k→(u)B_0⊗k→0. in the running text",
    "displayed", "other", None, "high",
    r"\[¶  0\longrightarrow\operatorname{Tor}_1^A(B_0,k)¶  \longrightarrow Z_1\otimes k¶  \longrightarrow P_1\otimes k¶  \xrightarrow{u}B_0\otimes k¶  \longrightarrow0.¶\]",
    r"$0\longrightarrow\operatorname{Tor}_1^A(B_0,k)\longrightarrow Z_1\otimes k\longrightarrow P_1\otimes k\xrightarrow{u}B_0\otimes k\longrightarrow0$.",
    LAYOUT)
add(p, "same proof, 'd⊗1 se factorise en ...'", "P_1⊗k→(u)B_0⊗k→(v)Z_0⊗k=P_0⊗k; in the running text", "displayed",
    "other", None, "high",
    r"\[¶  P_1\otimes k¶  \xrightarrow{u}B_0\otimes k¶  \xrightarrow{v}Z_0\otimes k¶  =P_0\otimes k;¶\]",
    r"$P_1\otimes k\xrightarrow{u}B_0\otimes k\xrightarrow{v}Z_0\otimes k=P_0\otimes k$;",
    LAYOUT)
add(p, "'Pour déduire alors c) de b)'", "c) and b) in italics (enlarged crop)", "upright c), b)", "italics", None, "high",
    r"Pour déduire alors c) de b),", r"Pour déduire alors \emph{c)} de \emph{b)},",
    "Inside Remarque (7.6.11), judged as if the remark body were roman (document-wide item 2).")
add(p, "'on considère une suite exacte L_1→L_0→N→0'", "in the running text", "displayed", "other", None, "high",
    r"\[¶  L_1\xrightarrow{d}L_0\longrightarrow N\longrightarrow0,¶\]",
    r"$L_1\xrightarrow{d}L_0\longrightarrow N\longrightarrow0$,", LAYOUT)
add(p, "'donc si M=Coker(^t d), T_1(A)=Ker(d)=M̌;'", "in the running text", "displayed (with \\qquad)", "other", None, "high",
    r"\[¶  M=\operatorname{Coker}({}^t d),¶  \qquad¶  T_1(A)=\operatorname{Ker}(d)=\check M;¶\]",
    r"$M=\operatorname{Coker}({}^t d)$, $T_1(A)=\operatorname{Ker}(d)=\check M$;", LAYOUT)
add(p, "'L'hypothèse b) entraîne par suite que'", "b) in italics (enlarged crop)", "upright b)", "italics", None, "high",
    r"L'hypothèse b) entraîne", r"L'hypothèse \emph{b)} entraîne",
    "Inside Remarque (7.6.11), judged as if the remark body were roman.")
add(p, "'Enfin, pour prouver que c) entraîne a)'", "no paragraph break: 'Enfin' continues the line after '(7.6.11.7).', not indented",
    "blank line: new paragraph", "other", None, "high",
    r"(7.6.11.7).¶¶Enfin", r"(7.6.11.7).¶Enfin", "Spurious paragraph break.")
add(p, "'pour prouver que c) entraîne a)'", "c) and a) in italics", "upright", "italics", None, "high",
    r"pour prouver que c) entraîne a),", r"pour prouver que \emph{c)} entraîne \emph{a)},",
    "Inside Remarque (7.6.11), judged as if the remark body were roman.")
add(p, "'l'hypothèse c) appliquée au module Z'_p'", "c) in italics", "upright", "italics", None, "high",
    r"l'hypothèse c) appliquée", r"l'hypothèse \emph{c)} appliquée",
    "Inside Remarque (7.6.11), judged as if the remark body were roman.")
add(p, "'où R=Ker(P_p⊗k→P_{p-1}⊗k) et S=Z_p⊗k.'", "in the running text", "displayed (\\quad\\text{et}\\quad)", "other", None, "high",
    r"\[¶  R=\operatorname{Ker}(P_p\otimes k\longrightarrow P_{p-1}\otimes k)¶  \quad\text{et}\quad¶  S=Z_p\otimes k.¶\]",
    r"$R=\operatorname{Ker}(P_p\otimes k\longrightarrow P_{p-1}\otimes k)$ et $S=Z_p\otimes k$.", LAYOUT)
add(p, "factorisation of d_{p+1}: 'P_{p+1}→(v)Z_p→(j)P_p on a'", "no comma after P_p; formula in the running text (enlarged crop)",
    "displayed, with a comma after P_p", "punctuation", None, "high",
    r"\[¶  P_{p+1}\xrightarrow{v}Z_p\xrightarrow{j}P_p,¶\]",
    r"$P_{p+1}\xrightarrow{v}Z_p\xrightarrow{j}P_p$",
    "The fix also sets the formula inline, as printed.")
add(p, "'on a Im(d_{p+1}⊗1)=(j⊗1)(Im(v⊗1)). Comme'", "in the running text", "displayed", "other", None, "high",
    r"\[¶  \operatorname{Im}(d_{p+1}\otimes1)¶  =¶  (j\otimes1)\bigl(\operatorname{Im}(v\otimes1)\bigr).¶\]",
    r"$\operatorname{Im}(d_{p+1}\otimes1)=(j\otimes1)\bigl(\operatorname{Im}(v\otimes1)\bigr)$.", LAYOUT)
add(p, "'et T_p(k)=R/Im(d_{p+1}⊗1), on en conclut'", "in the running text", "displayed", "other", None, "high",
    r"\[¶  T_p(k)=R/\operatorname{Im}(d_{p+1}\otimes1),¶\]",
    r"$T_p(k)=R/\operatorname{Im}(d_{p+1}\otimes1)$,", LAYOUT)
add(p, "'supposons que l'anneau local A soit régulier de dimension n'", "'régulier' in italics", "upright", "italics", None, "high",
    r"soit régulier de dimension", r"soit \emph{régulier} de dimension",
    "Inside Remarque (7.6.11), judged as if the remark body were roman. The later 'anneau régulier de dimension 2' is roman in the print.")
add(p, "'puissance extérieure ∧^i(m/m^2);'", "in the running text", "displayed", "other", None, "high",
    r"\[¶  \bigwedge\nolimits^i(\mathfrak m/\mathfrak m^2);¶\]",
    r"$\bigwedge\nolimits^i(\mathfrak m/\mathfrak m^2)$;", LAYOUT)
add(p, "'Par contre, si l'anneau local intègre A ...'", "no paragraph break: 'Par contre' continues after 'dès que n≥4.', not indented",
    "blank line: new paragraph", "other", None, "high",
    r"$n\geq4$.¶¶Par contre", r"$n\geq4$.¶Par contre", "Spurious paragraph break.")
add(p, "'tout A-module réflexif de type fini soit libre'", "'réflexif' and 'libre' in italics", "upright", "italics", None, "high",
    r"tout $A$-module réflexif¶de type fini soit libre (ce qui",
    r"tout $A$-module \emph{réflexif}¶de type fini soit \emph{libre} (ce qui",
    "Inside Remarque (7.6.11), judged as if the remark body were roman.")
add(p, "'le dual M̌ d'un A-module M de type fini M est réflexif'", "an extra M after 'de type fini' (no check accent; enlarged crop): 'de type fini M est réflexif'",
    "'de type fini est réflexif' (the second M is dropped)", "misprint_in_print", None, "high",
    r"de type fini est réflexif", r"de type fini $M$ est réflexif",
    "Misprint in the print: M is repeated. The TeX silently corrected it; the fix restores the printed reading.",
    corrected=r"le dual $\check M$ d'un $A$-module $M$ de type fini est réflexif")
add(p, "'et par suite rang_k(M̌⊗_A k)=rang_K(M̌)=rang_K(M) (K corps'", "no comma after rang_K(M); formula in the running text (enlarged crop)",
    "displayed, with a comma after rang_K(M)", "punctuation", None, "high",
    r"\[¶  \operatorname{rang}_k(\check M\otimes_A k)¶  =¶  \operatorname{rang}_K(\check M)¶  =¶  \operatorname{rang}_K(M),¶\]",
    r"$\operatorname{rang}_k(\check M\otimes_A k)=\operatorname{rang}_K(\check M)=\operatorname{rang}_K(M)$",
    "The fix also sets the formula inline, as printed.")
add(p, "heading 7.7", "'7.7. Application aux morphismes propres : I. La propriété d'échange.' (final full stop; enlarged crop)",
    "no full stop", "punctuation", None, "high",
    r"\subsection{Application aux morphismes propres : I. La propriété d'échange}",
    r"\subsection{Application aux morphismes propres : I. La propriété d'échange.}",
    "Same pattern as GLOBAL_ISSUES items 43 and 50 (subsection titles without the printed full stop).")
add(p, "(7.7.1), last line: 'sont Y-plats'", "'plats' in italics (enlarged crop)", "upright", "italics", None, "high",
    r"sont $Y$-plats", r"sont $Y$-\emph{plats}", "")
add(p, "(7.7.1), '(0_I, 6.7.1)'", "bold 0", "plain 0", "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.7.1)", r"($\mathbf{0}_{\mathrm I}$, 6.7.1)", "Form of GLOBAL_ISSUES item 35.")

# ---------------------------------------------------------------- page 198
p = 198
add(p, "(7.7.1), 'le ∂-foncteur M ~> T_•(M)'", "wavy arrow (enlarged crop)", "\\mapsto", "symbol", None, "high",
    r"$\mathscr M\mapsto\mathscr T_\bullet(\mathscr M)$", r"$\mathscr M\leadsto\mathscr T_\bullet(\mathscr M)$",
    "Wavy arrow in the print (\\leadsto), not convention 3; GLOBAL_ISSUES item 33.")
add(p, "(7.7.1), 'le terme de degré j est P_{-j}'", "roman P_{-j}, not script (enlarged crop)", "$\\mathscr P_{-j}$",
    "misprint_in_print", None, "high",
    r"$\mathscr P_{-j}$", r"$P_{-j}$",
    "Wrong-font letter in the print (the term of the complex script P^• is script P_{-j}). The TeX silently corrected it; the fix restores the printed reading.",
    corrected=r"$\mathscr P_{-j}$")
add(p, "(7.7.2), 'posons X'=X_{(Y')}=X×_Y Y' et f'=f_{(Y')}: X'→Y','", "'et' between the two formulas, no comma after X×_Y Y'; formulas in the running text",
    "comma and \\qquad instead of 'et'; displayed", "word", None, "high",
    r"\[¶  X'=X_{(Y')}=X\times_Y Y',¶  \qquad¶  f'=f_{(Y')}:X'\longrightarrow Y',¶\]",
    r"$X'=X_{(Y')}=X\times_Y Y'$ et $f'=f_{(Y')}:X'\longrightarrow Y'$,",
    "Missing word 'et'. The fix also sets the formulas inline, as printed.")
add(p, "(7.7.2), 'soit d'autre part P'_•=P_•⊗O_{Y'};'", "in the running text", "displayed", "other", None, "high",
    r"\[¶  \mathscr P'_\bullet¶  =\mathscr P_\bullet\otimes_{\mathscr O_Y}\mathscr O_{Y'};¶\]",
    r"$\mathscr P'_\bullet=\mathscr P_\bullet\otimes_{\mathscr O_Y}\mathscr O_{Y'}$;", LAYOUT)
add(p, "(7.7.2), 'qui sont Y'-plats en vertu de'", "'plats' in italics (enlarged crop)", "upright", "italics", None, "high",
    r"$Y'$-plats en vertu", r"$Y'$-\emph{plats} en vertu", "")
add(p, "(7.7.2), '(I, 9.1.12)'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 9.1.12)", r"(\textbf{I}, 9.1.12)", "")
add(p, "(7.7.2), '(0_I, 6.2.1)'", "bold 0", "plain 0", "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.2.1)", r"($\mathbf{0}_{\mathrm I}$, 6.2.1)", "")
add(p, "(7.7.2), 'on a alors T^{A'}_•(M̃')=...', first M̃'", "tilde over M only, the prime after it (enlarged crop); formula in the running text",
    "\\widetilde{M'}; displayed", "convention", 8, "high",
    r"\[¶  \mathscr T^{A'}_\bullet(\widetilde{M'})¶  =\bigl(\Gamma(Y',\mathscr T^{Y'}_\bullet(\widetilde{M'}))\bigr)^\sim;¶\]",
    r"$\mathscr T^{A'}_\bullet(\widetilde{M}')=\bigl(\Gamma(Y',\mathscr T^{Y'}_\bullet(\widetilde{M}'))\bigr)^\sim$;",
    "One fix for the formula: both \\widetilde{M'} -> \\widetilde{M}' (this and the next finding) and the formula set inline, as printed.")
add(p, "(7.7.2), same formula, second M̃' (inside (Γ(Y', ...))~)", "tilde over M only", "\\widetilde{M'}", "convention", 8, "high",
    None, None, "Corrected by the fix of the preceding finding (same formula).", nofix=True)
add(p, "(7.7.2), 'on posera T^{A'}_•(M')=Γ(Y', T^{Y'}_•(M̃'))'", "tilde over M only; formula in the running text",
    "\\widetilde{M'}; displayed", "convention", 8, "high",
    r"\[¶  T^{A'}_\bullet(M')¶  =\Gamma(Y',\mathscr T^{Y'}_\bullet(\widetilde{M'})),¶\]",
    r"$T^{A'}_\bullet(M')=\Gamma(Y',\mathscr T^{Y'}_\bullet(\widetilde{M}'))$,",
    "The fix also sets the formula inline, as printed.")
add(p, "(7.7.2), 'On observera que si Y=Spec(A) ...'", "no paragraph break: the line is not indented", "blank line: new paragraph",
    "other", None, "high", r"$A'$-modules.¶¶On observera", r"$A'$-modules.¶On observera", "Spurious paragraph break.")
add(p, "(7.7.2), '(II, 1.6.2)'", "bold II", "plain II", "convention", 2, "high",
    r"(II, 1.6.2)", r"(\textbf{II}, 1.6.2)", "")
add(p, "(7.7.2), 'tout revient à voir que C^•(U, ...)=C^•(U', ...),'", "in the running text", "displayed", "other", None, "high",
    r"\[¶  C^\bullet¶    \bigl(\mathfrak U,¶      \mathscr P_\bullet\otimes_{\mathscr O_Y}g_*(\mathscr M')\bigr)¶  =C^\bullet¶    \bigl(\mathfrak U',¶      \mathscr P_\bullet\otimes_{\mathscr O_Y}\mathscr M'\bigr),¶\]",
    r"$C^\bullet\bigl(\mathfrak U,\mathscr P_\bullet\otimes_{\mathscr O_Y}g_*(\mathscr M')\bigr)=C^\bullet\bigl(\mathfrak U',\mathscr P_\bullet\otimes_{\mathscr O_Y}\mathscr M'\bigr)$,",
    LAYOUT)
add(p, "(7.7.2), 'on a Γ(U, ...)=Γ(U', ...), ce qui est trivial'", "in the running text", "displayed", "other", None, "high",
    r"\[¶  \Gamma¶    \bigl(U,\mathscr P_\bullet\otimes_{\mathscr O_Y}g_*(\mathscr M')\bigr)¶  =\Gamma¶    \bigl(U',\mathscr P_\bullet\otimes_{\mathscr O_Y}\mathscr M'\bigr),¶\]",
    r"$\Gamma\bigl(U,\mathscr P_\bullet\otimes_{\mathscr O_Y}g_*(\mathscr M')\bigr)=\Gamma\bigl(U',\mathscr P_\bullet\otimes_{\mathscr O_Y}\mathscr M'\bigr)$,",
    LAYOUT)
add(p, "(7.7.2), '(I, 1.3 et 3.2)'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 1.3 et 3.2)", r"(\textbf{I}, 1.3 et 3.2)", "")
add(p, "(7.7.3), after (7.7.3.1): 'En effet, si Y est affine'", "new, indented paragraph", "no blank line after \\]",
    "other", None, "high", r"\]¶En effet, si $Y$", r"\]¶¶En effet, si $Y$", "Paragraph break as printed (indented line).")

# ---------------------------------------------------------------- page 199
p = 199
add(p, "(7.7.3.2)", "no comma after T^{Y'}_p(O_{Y'}) (enlarged crop)", "comma before \\tag", "punctuation", None, "high",
    r"\mathscr T^{Y'}_p(\mathscr O_{Y'}),¶", r"\mathscr T^{Y'}_p(\mathscr O_{Y'})¶", "")
add(p, "(7.7.4), 'T_p(M)=H_p(L_•⊗M), avec L_•=L̃_•, où'", "'avec' between the two formulas; formulas in the running text (enlarged crop)",
    "\\qquad instead of 'avec'; displayed", "word", None, "high",
    r"\[¶  \mathscr T_p(\mathscr M)¶  =\mathscr H_p¶    \bigl(\mathscr L_\bullet\otimes_{\mathscr O_Y}\mathscr M\bigr),¶  \qquad¶  \mathscr L_\bullet=\widetilde{L_\bullet},¶\]",
    r"$\mathscr T_p(\mathscr M)=\mathscr H_p\bigl(\mathscr L_\bullet\otimes_{\mathscr O_Y}\mathscr M\bigr)$,¶avec $\mathscr L_\bullet=\widetilde{L}_\bullet$,",
    "Missing word 'avec'. The fix also sets the formulas inline, as printed, and makes the convention-8 change of the next finding.")
add(p, "(7.7.4), 'L_•=L̃_•'", "tilde over L only, subscript • outside (enlarged crop)", "\\widetilde{L_\\bullet}", "convention", 8, "high",
    None, None, "Corrected by the fix of the preceding finding (same formula): \\widetilde{L}_\\bullet.", nofix=True)
add(p, "Théorème (7.7.5) I), 'I) (La propriété de semi-continuité) (¹). La fonction' (part 1 of 2)",
    "footnote call before the full stop: '... semi-continuité) (¹).' (enlarged crop)", "full stop before \\footnote",
    "punctuation", None, "high",
    r"semi-continuité).}\footnote{", r"semi-continuité)}\footnote{",
    "Apply together with part 2 (full stop after the footnote).")
add(p, "Théorème (7.7.5) I), end of the footnote (part 2 of 2)", "full stop after the footnote call", "no full stop after \\footnote{...}",
    "punctuation", None, "high",
    r"Grauert [5].}¶", r"Grauert [5].}.¶",
    "Apply together with part 1 (full stop removed before \\footnote).")
add(p, "Théorème (7.7.5) I), 'La fonction'", "italic, as the statement", "\\emph{La fonction} inside the italic theorem environment (prints upright)",
    "convention", 6, "high", r"\emph{La fonction}", r"La fonction", "Printed italic words left upright (\\emph inside \\itshape).")
add(p, "footnote of (7.7.5)", "no guillemets: '(On the variations of almost-complex structures, Algebraic ...'",
    "« On the variations of almost-complex structures »", "punctuation", None, "high",
    r"(« On the variations of¶almost-complex structures »,", r"(On the variations of¶almost-complex structures,", "")
add(p, "footnote of (7.7.5), 'p. 139-150'", "hyphen (as in 'Kodaira-Spencer'; enlarged crop)", "en dash 139--150",
    "punctuation", None, "medium", r"p. 139--150,", r"p. 139-150,", "")
add(p, "(7.7.5.1), 'y ~> d_p(y)'", "wavy arrow (enlarged crop)", "\\longmapsto", "symbol", None, "high",
    r"y\longmapsto", r"y\leadsto", "Wavy arrow in the print (\\leadsto), not convention 3; GLOBAL_ISSUES item 33.")
add(p, "(7.7.5.1), 'rang_{k(y)}'", "bold upright k(y) in the index (enlarged crop)", "\\kappa(y)", "symbol", None, "high",
    r"\operatorname{rang}_{\kappa(y)}", r"\operatorname{rang}_{\mathbf{k}(y)}",
    "Residue field k(y), not kappa; bold upright in sub- and superscripts (GLOBAL_ISSUES item 48).")
add(p, "(7.7.5.1), 'T^{k(y)}_p(k(y))'", "roman T (enlarged crop)", "script \\mathscr T", "font", None, "high",
    r"\mathscr T_p^", r"T_p^",
    "The print has the module functor T^{A'}_• of (7.7.2) (roman T), not the sheaf functor.")
add(p, "(7.7.5.1), 'T^{k(y)}_p(k(y))', index and argument", "bold upright k(y) in the superscript, bold italic k(y) in the argument (enlarged crop)",
    "\\kappa(y) twice", "symbol", None, "high",
    r"{\kappa(y)}(\kappa(y))", r"{\mathbf{k}(y)}(\boldsymbol{k}(y))",
    "Residue field k(y), not kappa (cf. convention 1 and GLOBAL_ISSUES item 48).")
add(p, "Théorème (7.7.5) I), 'est semi-continue supérieurement.'", "italic, as the statement",
    "\\emph{...} inside the italic theorem environment (prints upright)", "convention", 6, "high",
    r"\emph{est semi-continue supérieurement.}", r"est semi-continue supérieurement.",
    "Printed italic words left upright (\\emph inside \\itshape).")

# ---------------------------------------------------------------- page 200
p = 200
add(p, "Théorème (7.7.5) II), 'Pour un entier p donné, les conditions suivantes sont équivalentes :'", "italic, as the statement",
    "\\emph{...} inside the italic theorem environment (prints upright)", "convention", 6, "high",
    r"\emph{Pour un entier $p$ donné, les conditions suivantes sont équivalentes :}",
    r"Pour un entier $p$ donné, les conditions suivantes sont équivalentes :",
    "Printed italic words left upright (\\emph inside \\itshape).")
for lab, lt in (("a)", "a)"), ("a$'$)", "a')"), ("a$''$)", "a'')"), ("b)", "b)"), ("b$'$)", "b')"), ("c)", "c)"), ("d)", "d)")):
    add(p, f"Théorème (7.7.5) II), item label {lt}", "label upright (roman) (enlarged crop)", "label italic (\\item[...] inside \\itshape)",
        "convention", 6, "high", "\\item[" + lab + "]", "\\item[\\textup{" + lab + "}]",
        "Roman label inside the italic statement; as GLOBAL_ISSUES item 16 (page-fixed with \\textup).")
add(p, "Théorème (7.7.5) II) a'), '(N étant nécessairement isomorphe à T_p(O_Y)=H^{-p}(f, P^•)).'",
    "parentheses around 'N étant ... P^•)', no comma after N⊗M; formula in the running text (enlarged crop)",
    "comma, no parentheses; formula displayed", "punctuation", None, "high",
    r"$\mathscr N\otimes_{\mathscr O_Y}\mathscr M$, $\mathscr N$ étant nécessairement¶    isomorphe à¶    \[¶      \mathscr T_p(\mathscr O_Y)¶      =¶      \mathscr H^{-p}(f,\mathscr P^\bullet).¶    \]",
    r"$\mathscr N\otimes_{\mathscr O_Y}\mathscr M$ ($\mathscr N$ étant nécessairement¶    isomorphe à $\mathscr T_p(\mathscr O_Y)=\mathscr H^{-p}(f,\mathscr P^\bullet)$).",
    "The fix also sets the formula inline, as printed.")
add(p, "proof of (7.7.5), 'Il est clair que a'') entraîne a') et que a') entraîne a).'", "a''), a'), a'), a) in italics (enlarged crop)",
    "upright", "italics", None, "high",
    r"Il est clair que a$''$) entraîne a$'$) et que¶a$'$) entraîne a).",
    r"Il est clair que \emph{a$''$)} entraîne \emph{a$'$)} et que¶\emph{a$'$)} entraîne \emph{a)}.", "")
add(p, "proof of (7.7.5), 'L'équivalence de a), a''), b) et b')'", "a), a''), b), b') in italics", "upright", "italics", None, "high",
    r"L'équivalence de a), a$''$), b) et b$'$) a été",
    r"L'équivalence de \emph{a)}, \emph{a$''$)}, \emph{b)} et \emph{b$'$)} a été", "")
add(p, "proof of (7.7.5), 'lorsque Y est affine. Pour passer'", "'affine' in italics", "upright", "italics", None, "high",
    r"lorsque $Y$ est¶affine. Pour", r"lorsque $Y$ est¶\emph{affine}. Pour", "")
add(p, "proof of (7.7.5), 'prouvons d'abord que a) est équivalent à c)'", "a), c) in italics", "upright", "italics", None, "high",
    r"prouvons d'abord que a) est équivalent à c),", r"prouvons d'abord que \emph{a)} est équivalent à \emph{c)},", "")
add(p, "proof of (7.7.5), 'le caractère local sur Y de la propriété a);'", "'local' and a) in italics", "upright", "italics", None, "high",
    r"le caractère local sur $Y$ de la propriété a) ;", r"le caractère \emph{local} sur $Y$ de la propriété \emph{a)} ;",
    "The next 'caractère local de a'') et b)' has a roman 'local'.")
add(p, "proof of (7.7.5), 'le caractère local de a'') et b).'", "a''), b) in italics ('local' roman)", "upright", "italics", None, "high",
    r"le caractère local de a$''$) et b).", r"le caractère local de \emph{a$''$)} et \emph{b)}.", "")
add(p, "proof of (7.7.5), 'Comme il est clair que c) entraîne a)'", "c), a) in italics", "upright", "italics", None, "high",
    r"est clair que c) entraîne a), tout revient", r"est clair que \emph{c)} entraîne \emph{a)}, tout revient", "")
add(p, "proof of (7.7.5), 'toute suite exacte 0→F'→F→F''→0 de'", "in the running text", "displayed", "other", None, "high",
    r"\[¶  0\longrightarrow\mathscr F'¶  \longrightarrow\mathscr F¶  \longrightarrow\mathscr F''¶  \longrightarrow0¶\]",
    r"$0\longrightarrow\mathscr F'\longrightarrow\mathscr F\longrightarrow\mathscr F''\longrightarrow0$", LAYOUT)
add(p, "proof of (7.7.5), 'une suite exacte 0→G'→G→G''→0 de'", "in the running text", "displayed", "other", None, "high",
    r"\[¶  0\longrightarrow\mathscr G'¶  \longrightarrow\mathscr G¶  \longrightarrow\mathscr G''¶  \longrightarrow0¶\]",
    r"$0\longrightarrow\mathscr G'\longrightarrow\mathscr G\longrightarrow\mathscr G''\longrightarrow0$", LAYOUT)
add(p, "proof of (7.7.5), 'telle que F'=G'|U, F=G|U, F''=G''|U;'", "in the running text", "displayed (with \\qquad)", "other", None, "high",
    r"\[¶  \mathscr F'=\mathscr G'|U,¶  \qquad¶  \mathscr F=\mathscr G|U,¶  \qquad¶  \mathscr F''=\mathscr G''|U;¶\]",
    r"$\mathscr F'=\mathscr G'|U$, $\mathscr F=\mathscr G|U$, $\mathscr F''=\mathscr G''|U$;", LAYOUT)
add(p, "proof of (7.7.5), '(I, 9.4.2)'", "bold I", "plain I", "convention", 2, "high",
    r"de (I, 9.4.2) :", r"de (\textbf{I}, 9.4.2) :", "")
add(p, "proof of (7.7.5), 'on prolonge en effet F en un O_X-Module quasi-cohérent G'", "O_X (enlarged crop)", "$\\mathscr O_Y$",
    "misprint_in_print", None, "high",
    r"$\mathscr F$ en un $\mathscr O_Y$-Module", r"$\mathscr F$ en un $\mathscr O_X$-Module",
    "Misprint in the print: G extends the (O_Y|U)-Module F to Y, so it is an O_Y-Module (as the sentence before says). The TeX silently corrected it; the fix restores the printed reading.",
    corrected=r"$\mathscr F$ en un $\mathscr O_Y$-Module")
add(p, "proof of (7.7.5), 'F' en un sous-O_X-Module G' de G'", "O_X (enlarged crop)", "$\\mathscr O_Y$",
    "misprint_in_print", None, "high",
    r"sous-$\mathscr O_Y$-Module", r"sous-$\mathscr O_X$-Module",
    "Misprint in the print (same as the previous finding). The TeX silently corrected it; the fix restores the printed reading.",
    corrected=r"sous-$\mathscr O_Y$-Module")
add(p, "proof of (7.7.5), 'Pour démontrer l'équivalence de b) et b')'", "b), b') in italics", "upright", "italics", None, "high",
    r"l'équivalence de b) et b$'$) dans", r"l'équivalence de \emph{b)} et \emph{b$'$)} dans", "")
add(p, "proof of (7.7.5), 'un isomorphisme fonctoriel T^U_{p-1}(M|U) ~-> Hom(Q|U, M|U). Dans le cas'", "in the running text",
    "displayed", "other", None, "high",
    r"\[¶  \mathscr T_{p-1}^{U}(\mathscr M|U)¶  \xrightarrow{\sim}¶  \mathscr{H}\!om_{\mathscr O_Y|U}¶    (\mathscr Q|U,\mathscr M|U).¶\]",
    r"$\mathscr T_{p-1}^{U}(\mathscr M|U)\xrightarrow{\sim}\mathscr{H}\!om_{\mathscr O_Y|U}(\mathscr Q|U,\mathscr M|U)$.", LAYOUT)
add(p, "proof of (7.7.5), 'un isomorphisme fonctoriel T^U_{p-1}(M|U) → Hom(Q_U, M|U);'", "plain arrow, no tilde (enlarged crop; the preceding formula has the tilde); formula in the running text",
    "\\xrightarrow{\\sim}; displayed", "symbol", None, "high",
    r"\[¶  \mathscr T_{p-1}^{U}(\mathscr M|U)¶  \xrightarrow{\sim}¶  \mathscr{H}\!om_{\mathscr O_Y|U}¶    (\mathscr Q_U,\mathscr M|U);¶\]",
    r"$\mathscr T_{p-1}^{U}(\mathscr M|U)\to\mathscr{H}\!om_{\mathscr O_Y|U}(\mathscr Q_U,\mathscr M|U)$;",
    "The fix also sets the formula inline, as printed.")
add(p, "proof of (7.7.5), 'Reste enfin à montrer l'équivalence de a) et d); il est clair que d)'", "a), d), d) in italics", "upright",
    "italics", None, "high",
    r"l'équivalence de a) et d) ; il est clair que d) est de",
    r"l'équivalence de \emph{a)} et \emph{d)} ; il est clair que \emph{d)} est de", "")
add(p, "proof of (7.7.5), 'qu'il en est de même de a); en outre, d) est aussi local'", "a), d) in italics", "upright", "italics", None, "high",
    r"de même de a) ; en¶outre, d) est aussi local", r"de même de \emph{a)} ; en¶outre, \emph{d)} est aussi local", "")
add(p, "last line, '... est le foncteur obtenu' / p. 201 'à partir de ...'", "the sentence runs on to p. 201; its first line is not indented",
    "blank line before \\oldpage[III]{201} makes a paragraph break", "other", None, "high",
    r"est le foncteur obtenu¶¶", r"est le foncteur obtenu¶", "Spurious paragraph break (GLOBAL_ISSUES item 20). Self-contained: there is no blank line after the marker.")

# ---------------------------------------------------------------- page 201
p = 201
add(p, "proof of (7.7.5), 'il est clair alors que a') entraîne'", "a') in italics", "upright", "italics", None, "high",
    r"alors que a$'$) entraîne que", r"alors que \emph{a$'$)} entraîne que", "")
add(p, "proof of (7.7.5), '(a_1, m_1)(a_2, m_2)=(a_1a_2, a_1m_2+a_2m_1); alors'", "in the running text", "displayed", "other", None, "high",
    r"\[¶  (a_1,m_1)(a_2,m_2)¶  =¶  (a_1a_2,a_1m_2+a_2m_1);¶\]",
    r"$(a_1,m_1)(a_2,m_2)=(a_1a_2,a_1m_2+a_2m_1)$;", LAYOUT)
add(p, "proof of (7.7.5), 'l'application canonique T_p(A)⊗_A M→T_p(M),'", "in the running text", "displayed", "other", None, "high",
    r"\[¶  T_p(A)\otimes_A M\longrightarrow T_p(M),¶\]",
    r"$T_p(A)\otimes_A M\longrightarrow T_p(M)$,", LAYOUT)
add(p, "proof of (7.7.5), 'autrement dit d) entraîne a'')'", "d), a'') in italics", "upright", "italics", None, "high",
    r"autrement dit d) entraîne a$''$),", r"autrement dit \emph{d)} entraîne \emph{a$''$)},", "")
add(p, "Théorème (7.7.6), '(d'où un isomorphisme de foncteurs'", "roman (upright) inside the italic statement (enlarged crop)",
    "italic (theorem environment)", "convention", 6, "high",
    r"(d'où un isomorphisme de foncteurs", r"\textup{(d'où un isomorphisme de foncteurs}",
    "Roman words inside an italic statement.")
add(p, "(7.7.6.2)", "'Hom_{O_Y}(Q, M).)': full stop before the closing parenthesis (enlarged crop)", "'(Q,M)).'", "punctuation", None, "high",
    r"(\mathscr Q,\mathscr M)).", r"(\mathscr Q,\mathscr M).)", "")
add(p, "proof of (7.7.6), 'comme M ~> F⊗M est exact'", "wavy arrow (enlarged crop)", "\\mapsto", "symbol", None, "high",
    r"$\mathscr M\mapsto\mathscr F\otimes", r"$\mathscr M\leadsto\mathscr F\otimes",
    "Wavy arrow in the print (\\leadsto), not convention 3; GLOBAL_ISSUES item 33.")
add(p, "proof of (7.7.6), '(0_I, 6.7.4)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0\textsubscript{I}, 6.7.4)", r"(\textbf{0}\textsubscript{I}, 6.7.4)", "")
add(p, "proof of (7.7.6), 'le foncteur M ~> f_*(F⊗M)'", "wavy arrow (enlarged crop)", "\\mapsto", "symbol", None, "high",
    r"$\mathscr M\mapsto f_*(", r"$\mathscr M\leadsto f_*(",
    "Wavy arrow in the print (\\leadsto), not convention 3; GLOBAL_ISSUES item 33.")
add(p, "proof of (7.7.6), '(7.7.5, b)) et (7.7.5, b'))'", "b) and b') in italics, the outer parentheses roman", "upright", "italics", None, "high",
    r"(7.7.5, b)) et (7.7.5,¶b$'$)) pour", r"(7.7.5, \emph{b)}) et (7.7.5,¶\emph{b$'$)}) pour", "")
add(p, "Corollaire (7.7.7), first line of the display, 'T(M)=Ker(f_*(F⊗M)→f_*(F'⊗M))'", "no comma at the end of the line (enlarged crop)",
    "comma before \\\\", "punctuation", None, "high",
    r"\bigr),\\", r"\bigr)\\", "The print sets the second line on one line (T(M)=Γ(Y, T(M))=Ker(...).); the TeX's split of it is layout only.")
add(p, "Corollaire (7.7.7), 'Alors il existe un O_Y-Module cohérent R'", "new, indented paragraph", "no blank line after \\end{align*}",
    "other", None, "high", r"\end{align*}¶Alors il existe", r"\end{align*}¶¶Alors il existe", "Paragraph break as printed (indented line).")
add(p, "proof of (7.7.7), '(7.7.5, b) et b'))'", "b) and b') in italics, the outer parenthesis roman", "upright", "italics", None, "high",
    r"(7.7.5, b) et b$'$)),", r"(7.7.5, \emph{b)} et \emph{b$'$)}),", "")
add(p, "proof of (7.7.7), '(0, 8.1.8)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 8.1.8)", r"(\textbf{0}, 8.1.8)", "")
add(p, "proof of (7.7.7), 'Or, u: F→F' définit canoniquement'", "new, indented paragraph", "no blank line after \\]",
    "other", None, "high", r"\]¶Or, $u:", r"\]¶¶Or, $u:", "Paragraph break as printed (indented line).")
add(p, "last display, '...Γ(X, F'⊗M);' / p. 202 'il correspond à ce dernier ...'", "the sentence runs on to p. 202, whose first line is not indented (checked on the p. 202 scan)",
    "blank line after \\] (before \\oldpage[III]{202}) makes a paragraph break", "other", None, "high",
    r"\mathscr M);¶\]¶¶", r"\mathscr M);¶\]¶",
    "Spurious paragraph break (GLOBAL_ISSUES item 20). Self-contained: there is no blank line after \\oldpage[III]{202}.")


# ---------------------------------------------------------------- checks
def page_text(n):
    return (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")


ok = True
texts = {n: page_text(n) for n in range(197, 202)}
work = dict(texts)
for x in F:
    if x["fix"] is None:
        continue
    old, new = x["fix"]["old"], x["fix"]["new"]
    c = texts[x["page"]].count(old)
    if c != 1:
        ok = False
        print("NOT UNIQUE in original", x["page"], c, repr(old[:80]))
    c2 = work[x["page"]].count(old)
    if c2 != 1:
        ok = False
        print("NOT UNIQUE in sequence", x["page"], c2, repr(old[:80]))
    else:
        work[x["page"]] = work[x["page"]].replace(old, new)
for x in F:
    if x["kind"] == "misprint_in_print" and not x.get("corrected"):
        ok = False
        print("misprint without corrected", x["where"])
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for n in range(197, 202):
    (pathlib.Path(__file__).parent / f"fixed_{n}.tex").write_text(work[n], encoding="utf-8")
from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for n in range(197, 202):
    print(n, cnt[(n, "normal")], cnt[(n, "convention")], cnt[(n, "misprint")])
print("total", len(F), "checks ok" if ok else "CHECKS FAILED")
sys.exit(0 if ok else 1)
