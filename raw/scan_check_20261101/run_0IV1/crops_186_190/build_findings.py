"""Build findings_186_190.json, check every fix against page_NNN.tex and simulate apply_fixes on the release file (in memory)."""
import json
import pathlib
import re
import sys

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0IV1")
OUT = RUN / "findings_186_190.json"
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\ega0-22-fr.tex")
PART = r"0\textsubscript{IV-1}"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=(None if old is None else dict(old=old, new=new)))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 185 (pair of the p. 186 marker move)
add(185, "end of p. 185's segment: 'répondra à la question.' + blank line before \\oldpage{186}",
    "p. 185 runs on '... v = lim v_j répondra à la question. Or, la formation par récurrence de v_j résulte de l'hypothèse sur B et du' in one paragraph",
    "blank line after 'répondra à la question.' (paragraph break)",
    "other", None, "high",
    r"""$v=\varprojlim v_j$ répondra à la question.

""",
    r"""$v=\varprojlim v_j$ répondra à la question.
""",
    "OUTSIDE pp. 186-190: lies in page_185.tex (p. 185 segment of ega0-22-fr.tex), filed under page 185 so that apply_fixes finds it. Pairs with the p. 186 marker move (either order; old stays unique in the p. 185 segment). If the pp. 181-185 checker reports the same marker problem, apply only one version of the move.")

# ---------------------------------------------------------------- page 186
add(186, "top of p. 186: \\oldpage{186} before 'Or, la formation par récurrence de v_j ... sur B et du'",
    "printed p. 186 begins 'même raisonnement que dans (19.3.10.1)'; 'Or, la formation par récurrence de v_j résulte de l'hypothèse sur B et du' is the last line of p. 185",
    "\\oldpage[0\\textsubscript{IV-1}]{186} stands one line too early",
    "marker", None, "high",
    r"""\oldpage[0\textsubscript{IV-1}]{186}

Or, la formation par récurrence de $v_j$ résulte de l'hypothèse sur $B$ et
du même""",
    r"""Or, la formation par récurrence de $v_j$ résulte de l'hypothèse sur $B$ et
du
\oldpage[0\textsubscript{IV-1}]{186}
même""",
    "One edit inside the p. 186 segment: the marker moves after 'et du' (mid-sentence break, so no blank lines around it, GLOBAL_ISSUES 20); 'Or, la formation ... du' then ends the p. 185 segment. The blank line left before 'Or,' is removed by the page-185 entry above.")

add(186, "proof of (22.1.4): 'en utilisant le lemme (19.3.10.2) et le fait que n'^j+(n'^{j+1}+mB')=n'^j+mB'. Il résulte'",
    "formula in the running text, followed by a full stop",
    "displayed with \\[ ... \\]",
    "formula", None, "high",
    r"""le fait que
\[
  \mathfrak n'^j+(\mathfrak n'^{j+1}+\mathfrak mB')
  =\mathfrak n'^j+\mathfrak mB'.
\]
Il résulte""",
    r"""le fait que
$\mathfrak n'^j+(\mathfrak n'^{j+1}+\mathfrak mB')=\mathfrak n'^j+\mathfrak mB'$.
Il résulte""",
    "Display where the print sets the formula inline (GLOBAL_ISSUES 21); no connecting word lost.")

add(186, "proof of (22.1.4): 'les idéaux m^jB étant fermés dans B'",
    "𝔪^jB: exponent j (checked on a crop)",
    "\\mathfrak m^iB",
    "formula", None, "high",
    r"""\mathfrak m^iB""", r"""\mathfrak m^jB""")

add(186, "Théorème (22.2.2) (i): 'S•_K(m/m²) → gr•_m(A)'",
    "raised bullets on S and gr (checked on a crop)",
    "\\mathbf S_K^* ... \\operatorname{gr}_{\\mathfrak m}^*(A)",
    "symbol", None, "high",
    r"""$\mathbf S_K^*(\mathfrak m/\mathfrak m^2)\to
  \operatorname{gr}_{\mathfrak m}^*(A)$""",
    r"""$\mathbf S_K^\bullet(\mathfrak m/\mathfrak m^2)\to
  \operatorname{gr}_{\mathfrak m}^\bullet(A)$""",
    "GLOBAL_ISSUES item 60 (§22 check): the print has the raised bullet, the TeX an asterisk.")

add(186, "Théorème (22.2.2): 'Sous les conditions de (22.2.1), pour que'",
    "(22.2.1) upright in the italic statement", "italic (theorem environment)",
    "convention", 6, "high",
    r"""conditions de (22.2.1), pour""", r"""conditions de \textup{(22.2.1)}, pour""")

add(186, "Théorème (22.2.2): label (i)", "(i) upright", "\\item[(i)] italic in the theorem environment",
    "convention", 6, "high", r"""\item[(i)]""", r"""\item[\textup{(i)}]""")

add(186, "Théorème (22.2.2): label (ii)", "(ii) upright", "\\item[(ii)] italic in the theorem environment",
    "convention", 6, "high", r"""\item[(ii)]""", r"""\item[\textup{(ii)}]""")

add(186, "Remarque (22.2.3): label a)", "a) italic",
    "\\item[a)]: italic only through the italic remark environment; upright once the remark body is roman",
    "italics", None, "medium", r"""\item[a)]""", r"""\item[\textit{a)}]""",
    "Judged with the remark body roman (document-wide remark item); \\textit keeps the printed italic in either case. Same for b), c), d).")

add(186, "Remarque (22.2.3): label b)", "b) italic", "\\item[b)] (see label a))",
    "italics", None, "medium", r"""\item[b)]""", r"""\item[\textit{b)}]""")

add(186, "Remarque (22.2.3) b): 'l'homomorphisme canonique Ω¹_k⊗_k(A/m^{n+1}) → Ω¹_A⊗_A(A/m^{n+1}) est inversible à gauche'",
    "formula in the running text", "displayed with \\[ ... \\]",
    "formula", None, "high",
    r"""\[
    \Omega^1_k\otimes_k(A/\mathfrak m^{n+1})
    \longrightarrow
    \Omega^1_A\otimes_A(A/\mathfrak m^{n+1})
  \]""",
    r"""$\Omega^1_k\otimes_k(A/\mathfrak m^{n+1})\longrightarrow\Omega^1_A\otimes_A(A/\mathfrak m^{n+1})$""",
    "Display where the print sets the formula inline (GLOBAL_ISSUES 21); no connecting word lost.")

add(186, "Remarque (22.2.3): label c)", "c) italic", "\\item[c)] (see label a))",
    "italics", None, "medium", r"""\item[c)]""", r"""\item[\textit{c)}]""")

add(186, "Remarque (22.2.3): label d)", "d) italic", "\\item[d)] (see label a))",
    "italics", None, "medium", r"""\item[d)]""", r"""\item[\textit{d)}]""")

add(186, "(22.2.4): 'aux k-algèbres locales noethériennes et complètes'",
    "noethériennes italic, like complètes (checked on a crop)", "noethériennes roman",
    "italics", None, "high",
    r"""noethériennes et \emph{complètes}""", r"""\emph{noethériennes} et \emph{complètes}""")

add(186, "end of p. 186: '$V$ un $K$-espace vectoriel de' + blank line before \\oldpage{187}",
    "the sentence runs on to p. 187 ('... vectoriel de | rang fini; nous considérons')",
    "blank line before the marker (paragraph break)",
    "other", None, "high",
    r"""$K$-espace vectoriel de

""",
    r"""$K$-espace vectoriel de
""",
    "Mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the first p. 187 entry (blank line after the marker).")

# ---------------------------------------------------------------- page 187
add(187, "top of p. 187: blank line after \\oldpage{187} before 'rang fini'",
    "'rang fini; nous considérons ...' continues the sentence of p. 186", "blank line after the marker",
    "other", None, "high",
    r"""\oldpage[0\textsubscript{IV-1}]{187}

rang""",
    r"""\oldpage[0\textsubscript{IV-1}]{187}
rang""",
    "Apply together with the last p. 186 entry. \\oldpage ends with \\ignorespaces, so the joined lines keep one space.")

add(187, "(22.2.4), line 1: 'rang fini; nous considérons'",
    "fini italic (checked on a crop)", "fini roman",
    "italics", None, "high", r"""rang fini~;""", r"""rang \emph{fini}~;""")

add(187, "(22.2.4): 'le K-homomorphisme composé d'espaces vectoriels Υ_{K/k} --χ_{A/k}--> m/m² --β--> V (où ...'",
    "formula in the running text", "displayed with \\[ ... \\]",
    "formula", None, "high",
    r"""\[
  \Upsilon_{K/k}\xrightarrow{\chi_{A/k}}
  \mathfrak m/\mathfrak m^2\xrightarrow{\beta}V
\]""",
    r"""$\Upsilon_{K/k}\xrightarrow{\chi_{A/k}}\mathfrak m/\mathfrak m^2\xrightarrow{\beta}V$""",
    "Display where the print sets the formula inline (GLOBAL_ISSUES 21); no connecting word lost. Listed before the misprint fix that follows it.")

add(187, "(22.2.4): '(où χ_{A/K} est considéré comme un di-homomorphisme relatif à α^{-1})'",
    "χ_{A/K} with a capital K (checked on a crop; the label over the arrow just before reads χ_{A/k})",
    "\\chi_{A/k} (silently corrected)",
    "misprint_in_print", None, "high",
    r"""$\chi_{A/k}$ est considéré""", r"""$\chi_{A/K}$ est considéré""",
    "The TeX silently corrects the printed χ_{A/K}; the diplomatic text restores it.",
    corrected=r"""\chi_{A/k}""")

add(187, "Proposition (22.2.5): 'L'application canonique (22.2.4.1) est une bijection'",
    "(22.2.4.1) upright in the italic statement", "italic (proposition environment)",
    "convention", 6, "high",
    r"""canonique (22.2.4.1) est une bijection""", r"""canonique \textup{(22.2.4.1)} est une bijection""")

add(187, "Proposition (22.2.5): 'sur l'ensemble des K-homomorphismes injectifs de Υ_{K/k} dans V'",
    "injectifs upright (emphasis inside the italic statement; checked on a crop)", "injectifs italic",
    "convention", 6, "high",
    r"""homomorphismes injectifs""", r"""homomorphismes \emph{injectifs}""",
    "\\emph inside the italic environment gives the printed upright word.")

add(187, "proof of (22.2.5) (i): 'supposons donnés deux k-isomorphismes v⁰ : A/m ⥲ A'/m', v¹ : m/m² ⥲ m'/m'² tels que les diagrammes'",
    "both formulas in the running text, separated by a comma", "displayed with \\[ ... ,\\qquad ... \\]",
    "formula", None, "high",
    r"""\[
  v^0:A/\mathfrak m\xrightarrow{\sim}A'/\mathfrak m',\qquad
  v^1:\mathfrak m/\mathfrak m^2\xrightarrow{\sim}
      \mathfrak m'/\mathfrak m'^2
\]""",
    r"""$v^0:A/\mathfrak m\xrightarrow{\sim}A'/\mathfrak m'$,
$v^1:\mathfrak m/\mathfrak m^2\xrightarrow{\sim}\mathfrak m'/\mathfrak m'^2$""",
    "Display where the print sets the formulas inline (GLOBAL_ISSUES 21).")

add(187, "diagram (22.2.5.1), left triangle A/m --v⁰--> A'/m', α and α' to K",
    "K centred below; the arrow α' goes from A'/m' down-left to K",
    "K sits in column 2 under A'/m', so \\ar[dl]^{\\alpha'} from A'/m' points to the empty cell (2,1), not to K",
    "formula", None, "high",
    r"""\xymatrix@C=4em@R=3em{
  A/\mathfrak m \ar[r]^{v^0} \ar[dr]_{\alpha} &
  A'/\mathfrak m' \ar[dl]^{\alpha'} \\
  & K
}""",
    r"""\xymatrix@C=2em@R=3em{
  A/\mathfrak m \ar[rr]^{v^0} \ar[dr]_{\alpha} & &
  A'/\mathfrak m' \ar[dl]^{\alpha'} \\
  & K &
}""",
    "Three columns with K centred, as printed; both diagonal arrows then end at K. The right triangle (Υ_{K/k} below m/m²) is only drawn as a right angle instead of centred: layout, left as is.")

add(187, "proof of (22.2.5): 'Il s'agit de prouver qu'il existe un k-isomorphisme u : A ⥲ A''",
    "k-isomorphisme italic (checked on a crop)", "roman",
    "italics", None, "high",
    r"""existe un $k$-isomorphisme""", r"""existe un $k$-\emph{isomorphisme}""")

add(187, "proof of (22.2.5): 'donc il existe déjà un k-isomorphisme v : A/m² ⥲ A'/m'²'",
    "k-isomorphisme italic (checked on a crop)", "roman",
    "italics", None, "high",
    r"""déjà un $k$-isomorphisme""", r"""déjà un $k$-\emph{isomorphisme}""")

add(187, "end of p. 187: 'où $u$ est' + blank line before \\oldpage{188}",
    "the sentence runs on to p. 188 ('où u est | un k-homomorphisme (19.3.11)')",
    "blank line before the marker (paragraph break)",
    "other", None, "high",
    r"""où $u$ est

""",
    r"""où $u$ est
""",
    "Mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the first p. 188 entry.")

# ---------------------------------------------------------------- page 188
add(188, "top of p. 188: blank line after \\oldpage{188} before 'un k-homomorphisme'",
    "continues the sentence of p. 187", "blank line after the marker",
    "other", None, "high",
    r"""\oldpage[0\textsubscript{IV-1}]{188}

un""",
    r"""\oldpage[0\textsubscript{IV-1}]{188}
un""",
    "Apply together with the last p. 187 entry.")

add(188, "proof of (22.2.5), line 1: 'un k-homomorphisme (19.3.11)'",
    "k-homomorphisme italic (checked on a crop)", "roman",
    "italics", None, "high",
    r"""$k$-homomorphisme (19.3.11)""", r"""$k$-\emph{homomorphisme} (19.3.11)""")

add(188, "proof of (22.2.5), diagram, top row 'S•_K(m/m²) → gr•_m(A)'",
    "raised bullets (checked on a crop)", "\\mathbf S_K^*, \\operatorname{gr}_{\\mathfrak m}^*",
    "symbol", None, "high",
    r"""\mathbf S_K^*(\mathfrak m/\mathfrak m^2) \ar[r] \ar[d]_{w} &
  \operatorname{gr}_{\mathfrak m}^*(A) \ar[d]""",
    r"""\mathbf S_K^\bullet(\mathfrak m/\mathfrak m^2) \ar[r] \ar[d]_{w} &
  \operatorname{gr}_{\mathfrak m}^\bullet(A) \ar[d]""",
    "GLOBAL_ISSUES item 60.")

add(188, "proof of (22.2.5), diagram, label of the right vertical arrow 'gr (u)'",
    "gr (u) with no superscript (5x crop: a small gap, no bullet); the text two lines below writes gr(u)",
    "\\operatorname{gr}^*(u)",
    "formula", None, "medium",
    r"""^{\operatorname{gr}^*(u)}""", r"""^{\operatorname{gr}(u)}""",
    "Same reading as the p. 98 finding (label without superscript in the print).")

add(188, "proof of (22.2.5), diagram, bottom row 'S•_K(m'/m'²) → gr•_{m'}(A')'",
    "raised bullets (checked on a crop)", "\\mathbf S_K^*, \\operatorname{gr}_{\\mathfrak m'}^*",
    "symbol", None, "high",
    r"""\mathbf S_K^*(\mathfrak m'/\mathfrak m'^2) \ar[r] &
  \operatorname{gr}_{\mathfrak m'}^*(A')""",
    r"""\mathbf S_K^\bullet(\mathfrak m'/\mathfrak m'^2) \ar[r] &
  \operatorname{gr}_{\mathfrak m'}^\bullet(A')""",
    "GLOBAL_ISSUES item 60.")

add(188, "proof of (22.2.5): 'on déduit de (22.2.2, (i)) que gr(u) est bijectif;'",
    "bijectif italic (checked on a crop)", "roman",
    "italics", None, "high",
    r"""$\operatorname{gr}(u)$ est bijectif~;""", r"""$\operatorname{gr}(u)$ est \emph{bijectif}~;""")

add(188, "proof of (22.2.5) (ii), end: 'il suffira alors de prouver le' + heading 'Lemme (22.2.5.2). —'",
    "'... il suffira alors de prouver le' runs straight into the lemma heading",
    "'de prouver le lemme suivant.'",
    "extra", None, "high",
    r"""de prouver le lemme suivant.""", r"""de prouver le""",
    "The words 'lemme suivant.' are not printed; the lemma environment supplies the printed 'Lemme (22.2.5.2). —'.")

add(188, "proof of (22.2.5), 'Pour prouver (22.2.5.2), soient B la K-algèbre S•_K(V)'",
    "raised bullet (checked on a crop)", "\\mathbf S_K^*(V)",
    "symbol", None, "high",
    r"""$\mathbf S_K^*(V)$""", r"""$\mathbf S_K^\bullet(V)$""",
    "GLOBAL_ISSUES item 60.")

add(188, "end of p. 188: proof of (22.2.6) ends '... ≥ rg_K(Υ_{K/k}).' + \\end{proof} + blank line before \\oldpage{189}",
    "the paragraph continues on p. 189: 'En particulier, l'homomorphisme identique ...' starts flush left (no indent) and the last line of p. 188 is justified",
    "\\end{proof} and a blank line here; 'En particulier ...' is a new paragraph after the proof",
    "other", None, "high",
    r"""$\geqslant\operatorname{rg}_K(\Upsilon_{K/k})$.
\end{proof}

""",
    r"""$\geqslant\operatorname{rg}_K(\Upsilon_{K/k})$.
""",
    "Part 1 of 3 (with the first two p. 189 entries): the \\end{proof} moves after the 'En particulier' sentence, so that it continues the paragraph as printed. Apply all three or none (otherwise the proof environment is unbalanced).")

# ---------------------------------------------------------------- page 189
add(189, "top of p. 189: blank line after \\oldpage{189} before 'En particulier'",
    "'En particulier, ...' continues the paragraph of p. 188 (no indent)", "blank line after the marker",
    "other", None, "high",
    r"""\oldpage[0\textsubscript{IV-1}]{189}

En particulier""",
    r"""\oldpage[0\textsubscript{IV-1}]{189}
En particulier""",
    "Part 2 of 3 (see the last p. 188 entry). Apply all three or none.")

add(189, "end of the 'En particulier' paragraph, before Remarques (22.2.7)",
    "the paragraph ends '... est isomorphe à m/m².'; Remarques (22.2.7) follow",
    "no \\end{proof} here (it stands before \\oldpage{189})",
    "other", None, "high",
    r"""$\mathfrak m/\mathfrak m^2$.

\begin{remarks}""",
    r"""$\mathfrak m/\mathfrak m^2$.
\end{proof}

\begin{remarks}""",
    "Part 3 of 3: re-inserts the \\end{proof} removed at the end of p. 188. Apply all three or none.")

add(189, "Remarques (22.2.7) (ii): 'k = k_0(T) le corps des fractions rationnelles à une indéterminée sur k et K = k^{p^{-∞}}'",
    "'sur k' without the index 0 (checked on a crop; k_0 is printed with a clear 0 just before)",
    "'sur $k_0$' (silently corrected)",
    "misprint_in_print", None, "high",
    r"""sur $k_0$ et $K""", r"""sur $k$ et $K""",
    "k = k_0(T) is the field of rational fractions in one indeterminate over k_0; the TeX silently corrects the print.",
    corrected=r"""sur $k_0$""")

add(189, "Proposition (22.2.8): 'Sous les conditions de (22.2.1), supposons'",
    "(22.2.1) upright in the italic statement", "italic",
    "convention", 6, "high",
    r"""conditions de (22.2.1), supposons""", r"""conditions de \textup{(22.2.1)}, supposons""")

add(189, "Proposition (22.2.8): 'Alors la condition (ii) de (22.2.2)'",
    "(ii) upright", "italic", "convention", 6, "high",
    r"""condition (ii)""", r"""condition \textup{(ii)}""")

add(189, "Proposition (22.2.8): 'de (22.2.2) peut se remplacer'",
    "(22.2.2) upright", "italic", "convention", 6, "high",
    r"""(22.2.2) peut""", r"""\textup{(22.2.2)} peut""")

add(189, "Proposition (22.2.8): label a)", "a) upright (checked on a crop)", "\\item[a)] italic in the proposition",
    "convention", 6, "high", r"""\item[a)]""", r"""\item[\textup{a)}]""")

add(189, "Proposition (22.2.8): label b)", "b) upright", "\\item[b)] italic in the proposition",
    "convention", 6, "high", r"""\item[b)]""", r"""\item[\textup{b)}]""")

add(189, "Proposition (22.2.8): label c)", "c) upright", "\\item[c)] italic in the proposition",
    "convention", 6, "high", r"""\item[c)]""", r"""\item[\textup{c)}]""")

add(189, "proof of (22.2.8): 'il reste à prouver que a) entraîne que l'homomorphisme canonique u : Ω¹_k⊗_kK → Ω¹_A⊗_AK est injectif'",
    "formula in the running text", "displayed with \\[ ... \\]",
    "formula", None, "high",
    r"""\[
  u:\Omega^1_k\otimes_kK\longrightarrow\Omega^1_A\otimes_AK
\]""",
    r"""$u:\Omega^1_k\otimes_kK\longrightarrow\Omega^1_A\otimes_AK$""",
    "Display where the print sets the formula inline (GLOBAL_ISSUES 21); no connecting word lost.")

add(189, "proof of (22.2.8): '... est injectif. Or, on a pour tout α'",
    "injectif italic (checked on a crop)", "roman",
    "italics", None, "high",
    r"""est injectif. Or,""", r"""est \emph{injectif}. Or,""")

add(189, "end of p. 189: diagram '\\]' + blank line before \\oldpage{190}",
    "the sentence continues after the diagram on p. 190: 'et l'hypothèse que u_α est injectif ...' (flush left, no indent)",
    "blank line before the marker (paragraph break)",
    "other", None, "high",
    r"""\Omega^1_{A/k_\alpha}\otimes_AK
}
\]

""",
    r"""\Omega^1_{A/k_\alpha}\otimes_AK
}
\]
""",
    "GLOBAL_ISSUES 20. Apply together with the first p. 190 entry.")

# ---------------------------------------------------------------- page 190
add(190, "top of p. 190: blank line after \\oldpage{190} before 'et l'hypothèse'",
    "continues the sentence of p. 189 after the diagram (no indent)", "blank line after the marker",
    "other", None, "high",
    r"""\oldpage[0\textsubscript{IV-1}]{190}

et l'hypothèse""",
    r"""\oldpage[0\textsubscript{IV-1}]{190}
et l'hypothèse""",
    "Apply together with the last p. 189 entry.")

add(190, "Proposition (22.2.9): 'Sous les hypothèses de (22.2.1), les conditions'",
    "(22.2.1) upright", "italic", "convention", 6, "high",
    r"""hypothèses de (22.2.1), les conditions""", r"""hypothèses de \textup{(22.2.1)}, les conditions""")

add(190, "Proposition (22.2.9): label a)", "a) upright", "\\item[a)] italic", "convention", 6, "high",
    r"""\item[a)] $A/\mathfrak m^2$ est une $k$-extension""",
    r"""\item[\textup{a)}] $A/\mathfrak m^2$ est une $k$-extension""")

add(190, "Proposition (22.2.9): label b)", "b) upright", "\\item[b)] italic", "convention", 6, "high",
    r"""\item[b)] $\chi_{A/k}=0$.""", r"""\item[\textup{b)}] $\chi_{A/k}=0$.""")

add(190, "Proposition (22.2.9): label c)", "c) upright", "\\item[c)] italic", "convention", 6, "high",
    r"""\item[c)] L'homomorphisme canonique""", r"""\item[\textup{c)}] L'homomorphisme canonique""")

add(190, "Proposition (22.2.9) c): 'L'homomorphisme canonique (20.5.11.2)'",
    "(20.5.11.2) upright", "italic", "convention", 6, "high",
    r"""(20.5.11.2)""", r"""\textup{(20.5.11.2)}""")

add(190, "Proposition (22.2.9) c): 'est injectif (en d'autres termes, la suite'",
    "'est injectif' italic, '(en d'autres termes, la suite' upright (checked on a crop)", "all italic",
    "convention", 6, "high",
    r"""est injectif (en d'autres termes, la suite""",
    r"""est injectif \textup{(en d'autres termes, la suite}""")

add(190, "Proposition (22.2.9) c), after (22.2.9.1): 'est exacte).'",
    "'est' upright, 'exacte' italic, ')' upright (checked on a crop)", "all italic",
    "convention", 6, "high",
    r"""est exacte).""", r"""\textup{est \emph{exacte})}.""",
    "The parenthesis is a roman aside inside the italic statement, with 'exacte' emphasised in italic.")

add(190, "Corollaire (22.2.10): 'Sous les hypothèses de (22.2.1), considérons'",
    "(22.2.1) upright", "italic", "convention", 6, "high",
    r"""hypothèses de (22.2.1), considérons""", r"""hypothèses de \textup{(22.2.1)}, considérons""")

add(190, "Corollaire (22.2.10): label a)", "a) upright", "\\item[a)] italic", "convention", 6, "high",
    r"""\item[a)] $A/\mathfrak m^2$ est une $k_0$-extension""",
    r"""\item[\textup{a)}] $A/\mathfrak m^2$ est une $k_0$-extension""")

add(190, "Corollaire (22.2.10): label b)", "b) upright", "\\item[b)] italic", "convention", 6, "high",
    r"""\item[b)] L'homomorphisme composé""", r"""\item[\textup{b)}] L'homomorphisme composé""")

add(190, "Corollaire (22.2.10) b): 'L'homomorphisme composé Υ_{K/k_0} → Υ_{K/k} --χ_{A/k}--> m/m² est nul.'",
    "formula in the running text", "displayed with \\[ ... \\]",
    "formula", None, "high",
    r"""\[
    \Upsilon_{K/k_0}\longrightarrow\Upsilon_{K/k}
    \xrightarrow{\chi_{A/k}}\mathfrak m/\mathfrak m^2
  \]""",
    r"""$\Upsilon_{K/k_0}\longrightarrow\Upsilon_{K/k}\xrightarrow{\chi_{A/k}}\mathfrak m/\mathfrak m^2$""",
    "Display where the print sets the formula inline (GLOBAL_ISSUES 21); no connecting word lost.")

add(190, "Corollaire (22.2.10): label c)", "c) upright", "\\item[c)] italic", "convention", 6, "high",
    r"""\item[c)] L'homomorphisme caractéristique""", r"""\item[\textup{c)}] L'homomorphisme caractéristique""")

add(190, "Corollaire (22.2.10) c): '... se factorise en Υ_{K/k} → Υ_{K/k/k_0} --χ'--> m/m².'",
    "formula in the running text, full stop after it", "displayed with \\[ ... \\]",
    "formula", None, "high",
    r"""\[
    \Upsilon_{K/k}\longrightarrow\Upsilon_{K/k/k_0}
    \xrightarrow{\chi'}\mathfrak m/\mathfrak m^2.
  \]""",
    r"""$\Upsilon_{K/k}\longrightarrow\Upsilon_{K/k/k_0}\xrightarrow{\chi'}\mathfrak m/\mathfrak m^2$.""",
    "Display where the print sets the formula inline (GLOBAL_ISSUES 21); no connecting word lost.")

add(190, "proof of (22.2.10): displayed exact sequence (20.6.18.1) 'Υ_{K/k_0} → Υ_{K/k} → Υ_{K/k/k_0} → 0'",
    "no comma after the final 0 (checked on a crop)", "'\\longrightarrow0,'",
    "punctuation", None, "high",
    r"""\longrightarrow0,""", r"""\longrightarrow0""")

add(190, "Corollaire (22.2.11): 'Sous les hypothèses de (22.2.1), soit'",
    "(22.2.1) upright", "italic", "convention", 6, "high",
    r"""hypothèses de (22.2.1), soit""", r"""hypothèses de \textup{(22.2.1)}, soit""")

add(190, "proof of (22.2.11): 'Υ_{K/k} → Υ_{K/k/k_α} soit bijectif, donc'",
    "bijectif italic (checked on a crop)", "roman",
    "italics", None, "high",
    r"""soit bijectif, donc""", r"""soit \emph{bijectif}, donc""")


# ---------------------------------------------------------------- checks
def norm(t):
    return t.replace("\r\n", "\n")


ok = True
for x in F:
    if not x["fix"]:
        continue
    p = RUN / f"page_{x['page']:03d}.tex"
    t = norm(p.read_text(encoding="utf-8"))
    n = t.count(x["fix"]["old"])
    if n != 1:
        ok = False
        print("PAGE-FILE COUNT", n, x["page"], repr(x["fix"]["old"][:80]))
    if "\t" in x["fix"]["old"] or "\t" in x["fix"]["new"]:
        ok = False
        print("TAB in fix", x["page"])

# compare page files with the release segments, then simulate apply_fixes sequentially (in memory)
rel = REL.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[" + re.escape(PART) + r"\]\{(\d+)\}")


def segment(text, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(text)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, (cuts[j][1] if j < len(cuts) else len(text))
    return None, None


for pg in range(185, 191):
    s, e = segment(rel, pg)
    seg = rel[s:e]
    pf = norm((RUN / f"page_{pg:03d}.tex").read_text(encoding="utf-8"))
    body = pf.split("\n", 1)[1]  # drop the '% from' line
    if body != seg:
        print("SEGMENT DIFFERS from page file", pg, len(body), len(seg))

sim = rel
for x in F:
    if not x["fix"]:
        continue
    s, e = segment(sim, x["page"])
    seg = sim[s:e]
    n = seg.count(x["fix"]["old"])
    if n != 1:
        ok = False
        print("SIM COUNT", n, x["page"], repr(x["fix"]["old"][:80]))
        continue
    sim = sim[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + sim[e:]

# environment balance in the simulated file
for env in ("proof", "enumerate", "remarks", "proposition", "corollary", "theorem", "lemma", "remark", "env"):
    b = sim.count("\\begin{" + env + "}")
    en = sim.count("\\end{" + env + "}")
    if b != en:
        ok = False
        print("UNBALANCED", env, b, en)

# show the simulated p. 185 end .. p. 191 start around the changed page breaks
for pg in (186, 187, 188, 189, 190):
    i = sim.find("\\oldpage[" + PART + "]{%d}" % pg)
    print("---- around marker", pg, ":", repr(sim[i - 80:i + 70]))

counts = {}
for x in F:
    c = counts.setdefault(x["page"], [0, 0, 0])
    if x["kind"] == "misprint_in_print":
        c[2] += 1
    elif x["kind"] == "convention":
        c[1] += 1
    else:
        c[0] += 1
print("counts (normal/convention/misprint):", counts)
print("total", len(F), "OK" if ok else "PROBLEMS")
if ok and "--write" in sys.argv:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT)
