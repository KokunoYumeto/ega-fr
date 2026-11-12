# Builds findings_160_164.json; "¶" in the strings below stands for a line break (LF).
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
OUT = RUN / "findings_160_164.json"


def s(x):
    return None if x is None else x.replace("¶", "\n")


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": s(old), "new": s(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []

# ---------------- page 159 (segment end, before \oldpage[II]{160}) ----------------
L.append(F(159, "end of p. 159 / start of p. 160: '... si S est une S_0-algèbre | de type fini, on sait ...'",
           "p. 160 begins flush left with 'de type fini, on sait (2.1.6, (ii))': the sentence continues, no new paragraph",
           r"blank line after 'si $S$ est une $S_0$-algèbre' (last line of the p. 159 segment, before \oldpage[II]{160})".replace("¶", "\n"),
           "other", None, "high",
           r"si $S$ est une $S_0$-algèbre¶¶", r"si $S$ est une $S_0$-algèbre¶",
           "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). The edit lies in the p. 159 segment "
           "(old unique in page_159.tex and in the current release segment); findings_155_159.json does not contain it."))

# ---------------- page 160 ----------------
L.append(F(160, "proof of (8.2.10) (i): 'en posant E=S_{m_0}+...+S_{m_0+h-1},'",
           "E=S_{m_0}+ . . . +S_{m_0+h−1} (dots on the baseline)", r"$E=S_{m_0}+\cdots+S_{m_0+h-1}$",
           "symbol", None, "high",
           r"$E=S_{m_0}+\cdots+S_{m_0+h-1}$", r"$E=S_{m_0}+\ldots+S_{m_0+h-1}$",
           "Checked on a 1.2x crop: baseline dots (GLOBAL_ISSUES item 22)."))
L.append(F(160, "proof of (8.2.10) (i): 'S^♮_m=S_m+...+S_{m_0+h-1}+S_hE+S_h^2E+...'",
           "formula set inline, on the same line as 'en posant E=...,'; the line ends with three baseline dots and no period ('Pour' starts the next sentence)",
           r"\[ S_m^\natural=S_m+\cdots+S_{m_0+h-1}+S_hE+S_h^2E+\cdots. \] (displayed, centred dots, final period)",
           "other", None, "high",
           r"\[¶  S_m^\natural=S_m+\cdots+S_{m_0+h-1}+S_hE+S_h^2E+\cdots.¶\]¶",
           r"$S_m^\natural=S_m+\ldots+S_{m_0+h-1}+S_hE+S_h^2E+\ldots$¶",
           "Display in the TeX, inline in the print. This one edit also makes the two corrections that follow "
           "(baseline dots; no final period), whose entries carry fix null."))
L.append(F(160, "same formula: 'S_m+...+' and 'S_h^2E+...'",
           "baseline dots (twice)", r"\cdots (twice)", "symbol", None, "high", None, None,
           "Applied by the display-to-inline edit above (fix null here)."))
L.append(F(160, "same formula, end: 'S_h^2E+ . . .' before 'Pour'",
           "three dots end the sentence; no period (checked on a 3x crop)", r"S_h^2E+\cdots. (period added)",
           "punctuation", None, "high", None, None,
           "Applied by the display-to-inline edit above (fix null here)."))
L.append(F(160, "proof of (8.2.10) (i), first definition of G_m: 'des S_0-modules S_i pour m≤i≤m_0+h-1, considérée'",
           "no comma after S_i (S_i ends the line, 'pour' begins the next; checked on a 2x crop)",
           r"$S_i$, pour", "punctuation", None, "high",
           r"générateurs des $S_0$-modules $S_i$, pour", r"générateurs des $S_0$-modules $S_i$ pour",
           ""))
L.append(F(160, "proof of (8.2.10) (i), second definition of G_m: 'des S_0-modules S_i pour m≤i≤m_0+h-1 et de S_hE'",
           "no comma after S_i", r"$S_i$, pour", "punctuation", None, "high",
           r"-modules¶$S_i$, pour", r"-modules¶$S_i$ pour",
           "Checked on a crop."))
L.append(F(160, "same sentence: 'm≤i≤m_0+h-1 et de S_hE, considérée'",
           "no comma after m_0+h−1 (checked on a 2x crop)", r"m_0+h-1$, et de", "punctuation", None, "high",
           r"m_0+h-1$, et de $S_hE$", r"m_0+h-1$ et de $S_hE$",
           ""))
L.append(F(160, "proof of (8.2.10) (ii), display 'S_{n+1}+S_{n+2}+...=(S_1+S_2+...)(S_n+S_{n+1}+...)'",
           "baseline dots (three times)", r"\cdots (three times)", "symbol", None, "high",
           r"S_{n+1}+S_{n+2}+\cdots=(S_1+S_2+\cdots)(S_n+S_{n+1}+\cdots)",
           r"S_{n+1}+S_{n+2}+\ldots=(S_1+S_2+\ldots)(S_n+S_{n+1}+\ldots)",
           "Checked on a crop; three occurrences in one edit."))
L.append(F(160, "proof of (8.2.10) (iii): 'S^♮_n=S_1^n+S_1^{n+1}+...;'",
           "baseline dots", r"S_1^{n+1}+\cdots$", "symbol", None, "high",
           r"S_1^{n+1}+\cdots$", r"S_1^{n+1}+\ldots$", ""))
L.append(F(160, "proof of (8.2.10) (iii): 'comme S^♮_1 contient S_1+S_1^2+...,'",
           "baseline dots", r"$S_1+S_1^2+\cdots$", "symbol", None, "high",
           r"$S_1+S_1^2+\cdots$", r"$S_1+S_1^2+\ldots$", ""))
L.append(F(160, "proof of (8.2.10) (iii): 'S^{♮n}_1=(S_1+S_2+...)^n'",
           "baseline dots", r"(S_1+S_2+\cdots)^n", "symbol", None, "high",
           r"(S_1+S_2+\cdots)^n", r"(S_1+S_2+\ldots)^n", ""))
L.append(F(160, "proof of (8.2.10) (iv), last sentence: 'considéré comme de degré km−deg(f_α) dans S^♮; on a alors, dans S^♮'",
           "the first 'dans' (before S^♮;) is italic; the second 'dans' is roman (checked on a crop)",
           r"dans $S^\natural$~; on a alors (roman)", "italics", None, "high",
           r"dans $S^\natural$~; on a alors", r"\emph{dans} $S^\natural$~; on a alors",
           "Same emphasis as the earlier 'on ait, dans S,' (\\emph{dans $S$} in the TeX)."))
L.append(F(160, "display (8.2.11.3), last line of the page",
           "Proj(S)→Proj(S^♮⊗_S S_0) with no period (p. 161 begins with Proposition (8.2.12))",
           r"\operatorname{Proj}(S^\natural\otimes_S S_0).", "punctuation", None, "high",
           r"\operatorname{Proj}(S^\natural\otimes_S S_0).", r"\operatorname{Proj}(S^\natural\otimes_S S_0)",
           "Checked on a 2.5x crop."))

# ---------------- page 161 ----------------
L.append(F(161, "proof of (8.2.12): 'le noyau 𝔍 de l'homomorphisme (8.2.11.2)'",
           "Fraktur J (with descender), 𝔍", r"$\mathfrak{I}$", "symbol", None, "high",
           r"le noyau $\mathfrak{I}$", r"le noyau $\mathfrak{J}$",
           "Checked on a 3x crop. GLOBAL_ISSUES item 25 lists p. 161; same fix as p. 55 (\\mathfrak{J})."))
L.append(F(161, "proof of (8.2.12): 'le faisceau 𝔍̃ sur Proj(S^♮⊗_S S_0)'",
           "Fraktur J with tilde", r"$\widetilde{\mathfrak{I}}$", "symbol", None, "high",
           r"$\widetilde{\mathfrak{I}}$", r"$\widetilde{\mathfrak{J}}$", "Checked on a 3x crop."))
L.append(F(161, "proof of (8.2.12): 'on conclut de (2.7.3) que 𝔍 vérifie la condition (TN)'",
           "Fraktur J", r"$\mathfrak{I}$", "symbol", None, "high",
           r"que $\mathfrak{I}$ vérifie", r"que $\mathfrak{J}$ vérifie", "Checked on a 3x crop."))
L.append(F(161, "proof of (8.2.12): 'puisqu'il s'écrit f.f^n;'",
           "f.f^n with the dot on the baseline (full stop)", r"$f\cdot f^n$", "symbol", None, "high",
           r"$f\cdot f^n$", r"$f.f^n$",
           "Checked on a 3x crop; same treatment as the baseline product dots fixed on pp. 30, 35, 54-55."))
L.append(F(161, "Proposition (8.2.12): 'Le morphisme canonique (8.2.11.3) est bijectif.'",
           "reference (8.2.11.3) upright inside the italic statement", r"(\hyperref[II.8.2.11.3-fr]{8.2.11.3}) italic in the proposition environment",
           "convention", 6, "high",
           r"canonique (\hyperref[II.8.2.11.3-fr]{8.2.11.3}) est bijectif",
           r"canonique \textup{(\hyperref[II.8.2.11.3-fr]{8.2.11.3})} est bijectif", ""))
L.append(F(161, "Proposition (8.2.12): 'Pour que l'homomorphisme (8.2.11.2) soit'",
           "reference (8.2.11.2) upright inside the italic statement", r"(\hyperref[II.8.2.11.2-fr]{8.2.11.2}) italic",
           "convention", 6, "high",
           r"l'homomorphisme (\hyperref[II.8.2.11.2-fr]{8.2.11.2}) soit",
           r"l'homomorphisme \textup{(\hyperref[II.8.2.11.2-fr]{8.2.11.2})} soit", ""))
L.append(F(161, "Proposition (8.2.12): 'soit (TN)-bijectif, il faut'",
           "(TN) upright (regular weight), '-bijectif' italic", "(TN) italic in the proposition environment",
           "convention", 6, "high",
           r"(TN)-bijectif, il faut", r"\textup{(TN)}-bijectif, il faut", "Checked on a crop."))
L.append(F(161, "Proposition (8.2.12): 'Si cette dernière condition est vérifiée, (8.2.11.3) est un isomorphisme'",
           "reference (8.2.11.3) upright inside the italic statement", r"(\hyperref[II.8.2.11.3-fr]{8.2.11.3}) italic",
           "convention", 6, "high",
           r"vérifiée,¶(\hyperref[II.8.2.11.3-fr]{8.2.11.3}) est",
           r"vérifiée,¶\textup{(\hyperref[II.8.2.11.3-fr]{8.2.11.3})} est", ""))
L.append(F(161, "Proposition (8.2.14): 'Pour que l'homomorphisme (8.2.13.1) soit un'",
           "reference (8.2.13.1) upright inside the italic statement", r"(\hyperref[II.8.2.13.1-fr]{8.2.13.1}) italic",
           "convention", 6, "high",
           r"l'homomorphisme (\hyperref[II.8.2.13.1-fr]{8.2.13.1}) soit un",
           r"l'homomorphisme \textup{(\hyperref[II.8.2.13.1-fr]{8.2.13.1})} soit un", ""))
L.append(F(161, "Proposition (8.2.14): 'soit un (TN)-isomorphisme'",
           "(TN) upright (regular weight), '-isomorphisme' italic", "(TN) italic in the proposition environment",
           "convention", 6, "high",
           r"(TN)-isomorphisme", r"\textup{(TN)}-isomorphisme", ""))
L.append(F(161, "Proposition (8.2.14): 'le morphisme correspondant à (8.2.13.1) est partout défini'",
           "reference (8.2.13.1) upright inside the italic statement", r"(\hyperref[II.8.2.13.1-fr]{8.2.13.1}) italic",
           "convention", 6, "high",
           r"correspondant à (\hyperref[II.8.2.13.1-fr]{8.2.13.1}) est partout",
           r"correspondant à \textup{(\hyperref[II.8.2.13.1-fr]{8.2.13.1})} est partout", ""))
L.append(F(161, "Proposition (8.2.14), display 'Proj(S^♮)→Proj(⊕_{n≥0}(S_+)^n);'",
           "plain arrow, no tilde (checked on a 2.5x crop)", r"\xrightarrow{\sim}", "symbol", None, "high",
           r"\operatorname{Proj}(S^{\natural})\xrightarrow{\sim}", r"\operatorname{Proj}(S^{\natural})\to",
           "The TeX adds an isomorphism tilde that the print does not have."))
L.append(F(161, "Lemme (8.2.14.1): 'et est un isomorphisme Proj(T)→Proj(⊕_{n≥0}T_1^n), il existe n_0'",
           "formula set inline in the statement, followed by a comma", r"displayed \[ ... \]", "other", None, "high",
           r"isomorphisme¶\[¶  \operatorname{Proj}(T)\to¶  \operatorname{Proj}\left(\bigoplus_{n\geq0}T_1^n\right),¶\]¶il existe",
           r"isomorphisme¶$\operatorname{Proj}(T)\to\operatorname{Proj}\left(\bigoplus_{n\geq0}T_1^n\right)$,¶il existe",
           "Display in the TeX, inline in the print; the formula itself matches."))
L.append(F(161, "end of p. 161 / start of p. 162: '... donc h_j^{m_j}∈T_1T, et | h_j^{m_jk}∈T_1^kT⊂T'.'",
           "p. 162 begins flush left with 'h_j^{m_jk}∈...': same sentence, no new paragraph",
           r"blank line after 'et' at the end of the p. 161 segment", "other", None, "high",
           r"$h_j^{m_j}\in T_1T$, et¶¶", r"$h_j^{m_j}\in T_1T$, et¶",
           "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20)."))

# ---------------- page 162 ----------------
L.append(F(162, "proof of Lemme (8.2.14.1): 'En effet, un élément de S_n, pour n≥n_0, est somme de monômes appartenant à T_1^α u'",
           "S_n", r"$S_n$ (printed reading kept)", "misprint_in_print", None, "high", None, None,
           "The lemma and its proof concern the graded ring T (conclusion: T_n=T_1^n for n≥n_0), so the element lies in T_n. "
           "Checked on a 2.2x crop: the print has S. The TeX keeps the printed reading.",
           corrected=r"$T_n$"))
L.append(F(162, "Remarque (8.2.15): 'A=K[x], B=K[y]/y²K[y], où x et y sont deux indéterminées'",
           "the indeterminates x and y are bold upright (six letters)", r"plain $x$, $y$", "font", None, "high",
           r"$A=K[x]$, $B=K[y]/y^2K[y]$, où $x$ et $y$ sont",
           r"$A=K[\mathbf{x}]$, $B=K[\mathbf{y}]/\mathbf{y}^2K[\mathbf{y}]$, où $\mathbf{x}$ et $\mathbf{y}$ sont",
           "Checked on a crop."))
L.append(F(162, "Remarque (8.2.15): 'x étant prise de degré 1 et y de degré 2'",
           "bold upright x and y", r"plain $x$, $y$", "font", None, "high",
           r"indéterminées, $x$ étant¶prise de degré $1$ et $y$ de degré",
           r"indéterminées, $\mathbf{x}$ étant¶prise de degré $1$ et $\mathbf{y}$ de degré", ""))
L.append(F(162, "Remarque (8.2.15): 'des éléments 1, x^n (n≥1) et x^n y (n≥0)'",
           "bold upright x, y", r"plain $x^n$, $x^ny$", "font", None, "high",
           r"$x^n$ ($n\geq1$) et $x^ny$ ($n\geq0$)",
           r"$\mathbf{x}^n$ ($n\geq1$) et $\mathbf{x}^n\mathbf{y}$ ($n\geq0$)", ""))
L.append(F(162, "Remarque (8.2.15): 'mais S_1^n=Kx^n'",
           "bold upright x", r"$S_1^n=Kx^n$", "font", None, "high",
           r"$S_1^n=Kx^n$", r"$S_1^n=K\mathbf{x}^n$", ""))
L.append(F(162, "Remarque (8.2.15): 'tandis que S_n=Kx^n+Kx^{n-2}y'",
           "bold upright x, x, y", r"$S_n=Kx^n+Kx^{n-2}y$", "font", None, "high",
           r"$S_n=Kx^n+Kx^{n-2}y$", r"$S_n=K\mathbf{x}^n+K\mathbf{x}^{n-2}\mathbf{y}$", ""))
L.append(F(162, "display (8.3.1.1): '𝒮̂=𝒮[z]=𝒮⊗_{𝒪_Y}𝒪_Y[z]'",
           "the indeterminate z is bold upright (both times; checked on a 2.5x crop)", r"plain z", "font", None, "high",
           r"\mathcal{S}[z]¶  =\mathcal{S}\otimes_{\mathcal{O}_Y}\mathcal{O}_Y[z]",
           r"\mathcal{S}[\mathbf{z}]¶  =\mathcal{S}\otimes_{\mathcal{O}_Y}\mathcal{O}_Y[\mathbf{z}]",
           "Bold z throughout pp. 162-164; see the document-wide note in the report."))
L.append(F(162, "(8.3.1), display 'Γ(U,𝒮̂)=(Γ(U,𝒮))[z].'",
           "bold upright z", r"plain z", "font", None, "high",
           r"(\Gamma(U,\mathcal{S}))[z]", r"(\Gamma(U,\mathcal{S}))[\mathbf{z}]", "Checked on a 2.5x crop."))
L.append(F(162, "Proposition (8.3.2), display (8.3.2.2) 'X→Ĉ' with label j",
           "the label j stands below the arrow (ε and i of (8.3.2.1) stand above)", r"X\xrightarrow{j}\widehat{C} (label above)",
           "formula", None, "high",
           r"X\xrightarrow{j}\widehat{C}", r"X\xrightarrow[j]{}\widehat{C}", "Checked on a 3x crop."))
L.append(F(162, "end of p. 162 / start of p. 163: display (8.3.2.2), then 'tels que ε et j soient des immersions fermées'",
           "p. 163 begins flush left with 'tels que ...': the statement of (8.3.2) continues, no new paragraph",
           r"blank line after \end{equation} at the end of the p. 162 segment", "other", None, "high",
           r"\tag{8.3.2.2}¶\end{equation}¶¶", r"\tag{8.3.2.2}¶\end{equation}¶",
           "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20)."))

# ---------------- page 163 ----------------
L.append(F(163, "display (8.3.2.3): 'i(C)=Ĉ—j(X);'",
           "long dash for the set difference", r"\widehat{C}-j(X) (minus sign)", "convention", 7, "high",
           r"i(C)=\widehat{C}-j(X)", r"i(C)=\widehat{C}\setmin j(X)", "Checked on a 2.5x crop."))
z163 = [
    ("display (8.3.2.4): 'Ĉ_z=Spec(𝒮̂/(z−1)𝒮̂)'", "bold upright z (subscript of Ĉ and in z−1)",
     r"\widehat{C}_z=¶  \operatorname{Spec}(\widehat{\mathcal{S}}/(z-1)",
     r"\widehat{C}_{\mathbf{z}}=¶  \operatorname{Spec}(\widehat{\mathcal{S}}/(\mathbf{z}-1)", "Checked on a 3x crop."),
    ("after (8.3.2.4): '(3.1.4), z s'identifiant canoniquement'", "bold upright z",
     r"$z$ s'identifiant", r"$\mathbf{z}$ s'identifiant", ""),
    ("'L'isomorphisme i : C⥲Ĉ_z correspond'", "bold upright subscript z",
     r"\xrightarrow{\sim}\widehat{C}_z$", r"\xrightarrow{\sim}\widehat{C}_{\mathbf{z}}$", ""),
    ("display '𝒮̂/(z−1)𝒮̂⥲𝒮.'", "bold upright z",
     r"(z-1)\widehat{\mathcal{S}}¶  \xrightarrow{\sim}\mathcal{S}.", r"(\mathbf{z}-1)\widehat{\mathcal{S}}¶  \xrightarrow{\sim}\mathcal{S}.", ""),
    ("'est nul dans z𝒮̂, qui est son noyau'", "bold upright z (checked on a crop)",
     r"$z\widehat{\mathcal{S}}$", r"$\mathbf{z}\widehat{\mathcal{S}}$", ""),
    ("'les ouverts Ĉ_z=i(C) et Ĉ_f'", "bold upright subscript z",
     r"$\widehat{C}_z=i(C)$", r"$\widehat{C}_{\mathbf{z}}=i(C)$", ""),
    ("'Ĉ_f∩i(C)=Ĉ_f∩Ĉ_z=Ĉ_{fz}=Spec(Ŝ_{(fz)})'", "bold upright z (three times; checked on a crop)",
     r"\cap\widehat{C}_z¶=\widehat{C}_{fz}=\operatorname{Spec}(\widehat{S}_{(fz)})",
     r"\cap\widehat{C}_{\mathbf{z}}¶=\widehat{C}_{f\mathbf{z}}=\operatorname{Spec}(\widehat{S}_{(f\mathbf{z})})", ""),
    ("'Ŝ_{(fz)} est canoniquement isomorphe'", "bold upright z",
     r"$\widehat{S}_{(fz)}$ est", r"$\widehat{S}_{(f\mathbf{z})}$ est", ""),
    ("'isomorphe à (Ŝ_{(z)})_{f/z^d} (2.2.2)'", "bold upright z (twice)",
     r"$(\widehat{S}_{(z)})_{f/z^d}$ (", r"$(\widehat{S}_{(\mathbf{z})})_{f/\mathbf{z}^d}$ (", ""),
    ("'que l'image de (Ŝ_{(z)})_{f/z^d} par l'isomorphisme'", "bold upright z (twice)",
     r"$(\widehat{S}_{(z)})_{f/z^d}$ par", r"$(\widehat{S}_{(\mathbf{z})})_{f/\mathbf{z}^d}$ par", ""),
    ("'l'homomorphisme canonique Ŝ_{(f)}→Ŝ_{(fz)}'", "bold upright z",
     r"\to\widehat{S}_{(fz)}$", r"\to\widehat{S}_{(f\mathbf{z})}$", ""),
    ("last line: 'le complémentaire de Ĉ_z dans Ĉ=Proj(Ŝ)'", "bold upright subscript z",
     r"$\widehat{C}_z$ dans", r"$\widehat{C}_{\mathbf{z}}$ dans", ""),
]
for where, scan, old, new, note in z163:
    L.append(F(163, where, scan, "plain z", "font", None, "high", old, new, note))
L.append(F(163, "proof of (8.3.2): 'de même l'ouvert de C noté D(f) dans (I, 1.1.1)'",
           "bold I", r"{I, 1.1.1}", "convention", 2, "high", r"{I, 1.1.1}", r"{\textbf{I}, 1.1.1}", ""))
L.append(F(163, "proof of (8.3.2): 's'écrit aussi C_f (0, 5.5.2)'",
           "bold 0", r"{0, 5.5.2}", "convention", 2, "high", r"{0, 5.5.2}", r"{\textbf{0}, 5.5.2}", ""))
L.append(F(163, "proof of (8.3.2): 'considérée comme morphisme dans Ĉ_f, correspond (I, 1.7.3)'",
           "bold I", r"{I, 1.7.3}", "convention", 2, "high", r"{I, 1.7.3}", r"{\textbf{I}, 1.7.3}", ""))
L.append(F(163, "(8.3.2.6), whole statement",
           "bold number (8.3.2.6) followed by an italic statement (formulas upright)",
           "statement upright (env environment)", "convention", 6, "high",
           r"Si $Y=\operatorname{Spec}(A)$ est affine, et $\mathcal{S}=\widetilde{S}$,¶alors, pour tout $f$ homogène dans $S_+$, $\widehat{C}_f$ s'identifie¶canoniquement à $\operatorname{Spec}(S_f^{\leq})$, et le morphisme¶$C_f\to\widehat{C}_f$ restriction de $i$ correspond alors à l'injection¶canonique $S_f^{\leq}\to S_f$.",
           r"\emph{Si $Y=\operatorname{Spec}(A)$ est affine, et $\mathcal{S}=\widetilde{S}$,¶alors, pour tout $f$ homogène dans $S_+$, $\widehat{C}_f$ s'identifie¶canoniquement à $\operatorname{Spec}(S_f^{\leq})$, et le morphisme¶$C_f\to\widehat{C}_f$ restriction de $i$ correspond alors à l'injection¶canonique $S_f^{\leq}\to S_f$}.",
           "Printed italic text left upright; same treatment as the italic conditions (TF), (TN) of (2.7.2), p. 39. "
           "GLOBAL_ISSUES item 10 (env with an italic body) would cover it globally."))
L.append(F(163, "end of p. 163 / start of p. 164: '... le complémentaire de Ĉ_z dans Ĉ=Proj(Ŝ) | est, par définition, ...'",
           "p. 164 begins flush left with 'est, par définition,': same sentence, no new paragraph",
           r"blank line at the end of the p. 163 segment", "other", None, "high",
           r"\operatorname{Proj}(\widehat{S})$¶¶", r"\operatorname{Proj}(\widehat{S})$¶",
           "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20)."))

# ---------------- page 164 ----------------
L.append(F(164, "proof of the last assertion of (8.3.2): 'comme i(C)=Ĉ, il suffira de prouver le'",
           "i(C)=Ĉ: no bar over i(C) and no subscript on Ĉ (8x crop; a small gap stands between Ĉ and the comma)",
           r"$\overline{i(C)}=\widehat{C}$ (silent emendation)", "misprint_in_print", None, "high",
           r"$\overline{i(C)}=\widehat{C}$", r"$i(C)=\widehat{C}$",
           "As printed the equality is false (Ĉ also contains j(X), 8.3.2.3); the TeX silently emends it to the closure; the fix restores "
           "the printed reading. Proposed correct reading i(C)=Ĉ_z: the reduction to Lemme (8.3.2.7) with T=Ŝ, g=z needs "
           "Z_g=D_+(z)=Ĉ_z=i(C), stated on p. 163 ('les ouverts Ĉ_z=i(C)'), and the gap after Ĉ fits a dropped subscript. "
           "The TeX's reading (density of i(C)) has not been proved at this point of the proof (it follows from the assertion "
           "being proved). Editorial judgement on the corrected reading; with the edition's present plain z it is i(C)=\\widehat{C}_z.",
           corrected=r"$i(C)=\widehat{C}_{\mathbf{z}}$"))
L.append(F(164, "first line: 'idéaux premiers gradués de Ŝ contenant z,'",
           "bold upright z", "plain z", "font", None, "high",
           r"contenant $z$,", r"contenant $\mathbf{z}$,", "Checked on a crop."))
L.append(F(164, "'dans l'anneau Ŝ, z n'est pas diviseur de 0'",
           "bold upright z", "plain z", "font", None, "high",
           r"$z$¶n'est pas", r"$\mathbf{z}$¶n'est pas", ""))
L.append(F(164, "(8.3.3): '𝒮̂=𝒮[z]→𝒪_Y[z] (cf. (3.1.7))'",
           "bold upright z (twice; checked on a crop)", "plain z", "font", None, "high",
           r"\mathcal{S}[z]\to\mathcal{O}_Y[z]", r"\mathcal{S}[\mathbf{z}]\to\mathcal{O}_Y[\mathbf{z}]", ""))
L.append(F(164, "(8.3.3): 'de noyau 𝒮_+[z]=𝒮_+𝒮̂'",
           "bold upright z", "plain z", "font", None, "high",
           r"\mathcal{S}_+[z]", r"\mathcal{S}_+[\mathbf{z}]", ""))
for ref, bold in ((r"{I, 4.1.9}", r"{\textbf{I}, 4.1.9}"), (r"{I, 4.3.2}", r"{\textbf{I}, 4.3.2}"),
                  (r"{0, 1.2.2}", r"{\textbf{0}, 1.2.2}"), (r"{I, 5.4.6}", r"{\textbf{I}, 5.4.6}")):
    where = {"{I, 4.1.9}": "proof of Lemme (8.3.2.7): 'En vertu de (I, 4.1.9)'",
             "{I, 4.3.2}": "proof of Lemme (8.3.2.7): 'il résulte des définitions et de (I, 4.3.2)'",
             "{0, 1.2.2}": "proof of Lemme (8.3.2.7), last words: 'la démonstration (0, 1.2.2)'",
             "{I, 5.4.6}": "(8.3.3): 'donc aussi une immersion fermée (I, 5.4.6)'"}[ref]
    L.append(F(164, where, "bold " + ("0" if ref.startswith("{0") else "I"), ref, "convention", 2, "high", ref, bold, ""))
for old, new, where in (
        (r"\emph{préschéma des sommets de $C$}", r"\emph{préschéma des sommets} de $C$",
         "(8.3.3): 'est appelé le préschéma des sommets de C;'"),
        (r"\emph{section nulle de $C$}", r"\emph{section nulle} de $C$",
         "(8.3.3): 'ou la section nulle de C;'"),
        (r"\emph{préschéma des sommets de $\widehat{C}$}", r"\emph{préschéma des sommets} de $\widehat{C}$",
         "(8.3.3): 'encore appelé le préschéma des sommets de Ĉ'"),
        (r"\emph{section sommet de $\widehat{C}$}", r"\emph{section sommet} de $\widehat{C}$",
         "(8.3.3): 'et i∘ε la section sommet de Ĉ;'"),
        (r"\emph{lieu à l'infini de $\widehat{C}$}", r"\emph{lieu à l'infini} de $\widehat{C}$",
         "(8.3.3): 'est appelé le lieu à l'infini de Ĉ'")):
    L.append(F(164, where, "only the term is italic; 'de' is roman (checked on crops)", old + " (italic 'de')",
               "italics", None, "high", old, new, ""))
L.append(F(164, "display (8.3.4.1): 'E=C—ε(Y)'",
           "long dash for the set difference", r"C-\varepsilon(Y) (minus sign)", "convention", 7, "high",
           r"E=C-\varepsilon(Y)", r"E=C\setmin\varepsilon(Y)", ""))
L.append(F(164, "display (8.3.4.1): 'Ê=Ĉ—i(ε(Y))'",
           "long dash for the set difference", r"\widehat{C}-i(\varepsilon(Y)) (minus sign)", "convention", 7, "high",
           r"\widehat{E}=\widehat{C}-i(\varepsilon(Y))", r"\widehat{E}=\widehat{C}\setmin i(\varepsilon(Y))", ""))
L.append(F(164, "display (8.3.4.3): 'E=Ê—j(X).'",
           "long dash for the set difference", r"\widehat{E}-j(X) (minus sign)", "convention", 7, "high",
           r"E=\widehat{E}-j(X)", r"E=\widehat{E}\setmin j(X)", ""))

for d in L:
    if d["note"] == "":
        d["note"] = None
json.dump(L, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# verification: every fix's old occurs exactly once in its page_NNN.tex (CRLF normalised to LF)
bad = 0
for d in L:
    if not d["fix"]:
        continue
    t = (RUN / ("page_%03d.tex" % d["page"])).read_bytes().decode("utf-8").replace("\r\n", "\n")
    c = t.count(d["fix"]["old"])
    if c != 1:
        bad += 1
        print("NOT UNIQUE", d["page"], c, repr(d["fix"]["old"][:80]))
# sequential application check per page (in list order), as apply_fixes.py does
pages = {}
for d in L:
    pages.setdefault(d["page"], []).append(d)
for p, items in pages.items():
    t = (RUN / ("page_%03d.tex" % p)).read_bytes().decode("utf-8").replace("\r\n", "\n")
    for d in items:
        if not d["fix"]:
            continue
        c = t.count(d["fix"]["old"])
        if c != 1:
            bad += 1
            print("SEQUENTIAL FAIL", p, c, repr(d["fix"]["old"][:80]))
            continue
        t = t.replace(d["fix"]["old"], d["fix"]["new"])
from collections import Counter
cnt = Counter()
for d in L:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
print("entries", len(L), "bad", bad)
for p in sorted(pages):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
