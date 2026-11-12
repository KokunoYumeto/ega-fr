"""Build findings_010_014.json for EGA IV-3 pp. 10-14 and check every fix.

Checks: each fix's "old" occurs exactly once in its page_NNN.tex (CRLF normalised to LF), and, applying a page's
fixes in list order, each "old" occurs exactly once at the moment it is applied. Also checks the same in the
page's segment of the LF source file.
"""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\source\ega4\ega4-8-fr.tex")
OUT = RUN / "findings_010_014.json"


def L(s):
    return s.replace("<NL>", "\n")


def F(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": L(old), "new": L(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


C10 = ("Same pattern as convention 10 (bold italic P) and GLOBAL_ISSUES 33/44 (bold italic category letters); "
       "the subscript is the ordinary subscript T. ega4-8-fr.tex uses \\mathbf C for this category throughout "
       "(8.2.4)-(8.2.6).")
RESP = "'(resp.' and the closing parenthesis printed roman inside the italic statement; the words inside stay italic."
PAREN = "Parenthetical remark printed roman (upright parentheses, 'et alors', 'pour') inside the italic statement."

findings = [
    # ---------------- page 10 ----------------
    F(10, "Lemme (8.2.6), first line of the page: 'de T (resp. T').'",
      "'(resp. T')' upright: roman 'resp.' and upright parentheses inside the italic statement (crop)",
      "(resp. $T'$) set in the italic lemma environment",
      "convention", 6, "high",
      r"de $T$ (resp. $T'$). Soit", r"de $T$ \textup{(resp. $T'$)}. Soit"),
    F(10, "Lemme (8.2.6), l. 1: 'dans C_T, et posons'",
      "category letter C bold italic (slanted bold) (enlarged crop)",
      r"$\mathbf C_T$ (bold upright)",
      "font", None, "high",
      r"filtrant) dans $\mathbf C_T$, et", r"filtrant) dans $\boldsymbol{C}_T$, et", C10),
    F(10, "Lemme (8.2.6), l. 2: 'est un système projectif dans C_T'.'",
      "bold italic C (enlarged crop)",
      r"$\mathbf C_{T'}$ (bold upright)",
      "font", None, "high",
      r"$\mathbf C_{T'}$. Alors", r"$\boldsymbol{C}_{T'}$. Alors", "As the previous entry."),
    F(10, "Lemme (8.2.6), l. 3: 'de (S_λ, u_λμ) dans C_T, (S×_T T', ...)'",
      "bold italic C (crop)",
      r"$\mathbf C_T$ (bold upright)",
      "font", None, "high",
      r"dans $\mathbf C_T$,<NL>$(S\times_T T'", r"dans $\boldsymbol{C}_T$,<NL>$(S\times_T T'", "As the previous entry."),
    F(10, "Lemme (8.2.6), last line: 'de (S'_λ, u'_λμ) dans C_T'.'",
      "bold italic C (crop)",
      r"$\mathbf C_{T'}$ (bold upright)",
      "font", None, "high",
      r"dans $\mathbf C_{T'}$.<NL>\end{lemma}", r"dans $\boldsymbol{C}_{T'}$.<NL>\end{lemma}", "As the previous entry."),
    F(10, "Remarque (8.2.7), 2nd paragraph: '(I, 1.3.13)'",
      "(I, 1.3.13) with a bold I",
      "(I, 1.3.13)",
      "convention", 2, "high",
      "(I, 1.3.13)", r"(\textbf{I}, 1.3.13)"),
    F(10, "Remarque (8.2.7), 2nd paragraph: 'est une O_S-Algèbre quasi cohérente lorsqu'il en est ainsi'",
      "'quasi cohérente' without a hyphen (enlarged crop: an ordinary word space, no trace of a hyphen); two "
      "lines lower the print has 'quasi-cohérentes'",
      "quasi-cohérente (silently corrected)",
      "misprint_in_print", None, "medium",
      "quasi-cohérente lorsqu'il", "quasi cohérente lorsqu'il",
      "Missing hyphen in the print; EGA writes quasi-cohérent with a hyphen (so does this remark two lines "
      "later). The fix restores the printed reading in the diplomatic text.",
      corrected="quasi-cohérente"),
    F(10, "Proposition (8.2.9): 'Avec les notations de (8.2.8),'",
      "reference (8.2.8) upright inside the italic statement (crop)",
      "(8.2.8) set in the italic proposition environment",
      "convention", 6, "high",
      "notations de (8.2.8), la limite projective", r"notations de \textup{(8.2.8)}, la limite projective"),
    F(10, "(8.2.8), last sentence: 'd'applications continues S→S_λ des espaces sous-jacents'",
      "no comma after S→S_λ (crop)",
      r"$S\to S_\lambda$, des espaces",
      "punctuation", None, "high",
      r"$S\to S_\lambda$, des espaces", r"$S\to S_\lambda$ des espaces", "Comma added by the TeX."),
    # ---------------- page 11 ----------------
    F(11, "proof of (8.2.9), (i): 'une base de la topologie de S (II, 1.3.1)'",
      "(II, 1.3.1) with a bold II",
      "(II, 1.3.1)",
      "convention", 2, "high",
      "(II, 1.3.1)", r"(\textbf{II}, 1.3.1)"),
    F(11, "proof of (8.2.9), (i): 'on a A = lim A_λ (I, 1.3.9)'",
      "(I, 1.3.9) with a bold I",
      "(I, 1.3.9)",
      "convention", 2, "high",
      "(I, 1.3.9)", r"(\textbf{I}, 1.3.9)"),
    F(11, "proof of (8.2.9), (i): 'D(f) = ψ_λ^{-1}(D(f_λ)) (I, 1.2.2)'",
      "(I, 1.2.2) with a bold I",
      "(I, 1.2.2)",
      "convention", 2, "high",
      "(I, 1.2.2)", r"(\textbf{I}, 1.2.2)"),
    F(11, "proof of (8.2.9), (ii): 'On sait alors ((5.13.3) et (5.13.1)) qu'il y a un idéal premier'",
      "((5.13.3) et (5.13.1)): each number in its own parentheses inside an outer pair (enlarged crop)",
      "(5.13.3 et 5.13.1)",
      "punctuation", None, "high",
      "(5.13.3 et 5.13.1)", "((5.13.3) et (5.13.1))"),
    F(11, "Corollaire (8.2.10): 'L'application canonique 𝔭 ⇝ (φ_λ^{-1}(𝔭))'",
      "wavy arrow ⇝ (enlarged crop)",
      r"\mathfrak p\mapsto(\varphi_\lambda^{-1}(\mathfrak p))",
      "symbol", None, "high",
      r"$\mathfrak p\mapsto(", r"$\mathfrak p\leadsto(",
      "Wavy arrow (GLOBAL_ISSUES 33), written \\leadsto as in the earlier page fixes; not convention 3."),
    F(11, "Corollaire (8.2.11): 'Avec les notations de (8.2.8), pour tout ouvert quasi-compact'",
      "reference (8.2.8) upright inside the italic statement",
      "(8.2.8) set in the italic corollary environment",
      "convention", 6, "high",
      "notations de (8.2.8), pour tout", r"notations de \textup{(8.2.8)}, pour tout"),
    F(11, "Corollaire (8.2.12): 'Avec les notations de (8.2.8), la limite inductive'",
      "reference (8.2.8) upright inside the italic statement",
      "(8.2.8) set in the italic corollary environment",
      "convention", 6, "high",
      "notations de (8.2.8), la limite inductive", r"notations de \textup{(8.2.8)}, la limite inductive"),
    # ---------------- page 12 ----------------
    F(12, "proof of (8.2.13): 'sur S par définition (0_I, 3.7.1)'",
      "(0_I, 3.7.1) with a bold 0",
      r"$(0_{\mathrm I},3.7.1)$",
      "convention", 2, "high",
      r"$(0_{\mathrm I},3.7.1)$", r"$(\mathbf{0}_{\mathrm I},3.7.1)$"),
    F(12, "proof of (8.2.13), last words: 'de la définition de u*_α(F_α) (0_I, 4.3.1)'",
      "(0_I, 4.3.1) with a bold 0",
      r"$(0_{\mathrm I},4.3.1)$",
      "convention", 2, "high",
      r"$(0_{\mathrm I},4.3.1)$", r"$(\mathbf{0}_{\mathrm I},4.3.1)$"),
    F(12, "Remarque (8.2.14): 'D'autre part, les ω♯_λ : ρ*(𝒪_{S_λ}) → 𝒪_Y forment un système inductif'",
      "the formula stands in the running text of the line 'telle que ρ_λ = ψ_λ∘ρ. D'autre part, les ω♯_λ : ... "
      "forment un système inductif'",
      r"displayed \[ \omega_\lambda^\sharp: \rho_\lambda^*(\mathcal O_{S_\lambda})\to\mathcal O_Y \]",
      "formula", None, "high",
      r"les<NL>\[<NL>\omega_\lambda^\sharp:<NL>\rho_\lambda^*(\mathcal O_{S_\lambda})\to\mathcal O_Y<NL>\]<NL>forment",
      r"les<NL>$\omega_\lambda^\sharp:<NL>\rho_\lambda^*(\mathcal O_{S_\lambda})\to\mathcal O_Y$<NL>forment",
      "Apply before the next entry (misprint in this formula); that entry's old string occurs once before and after "
      "this edit."),
    F(12, "Remarque (8.2.14), same formula: 'ω♯_λ : ρ*(𝒪_{S_λ}) → 𝒪_Y'",
      "ρ*(𝒪_{S_λ}): ρ without the index λ (enlarged crop)",
      r"\rho_\lambda^*(\mathcal O_{S_\lambda}) (silently corrected)",
      "misprint_in_print", None, "high",
      r"\rho_\lambda^*(\mathcal O_{S_\lambda})\to\mathcal O_Y", r"\rho^*(\mathcal O_{S_\lambda})\to\mathcal O_Y",
      "w_λ = (ρ_λ, ω_λ) : Y → S_λ, so ω_λ♯ goes from ρ_λ*(𝒪_{S_λ}) to 𝒪_Y, as the next sentence uses "
      "(ρ_λ*(𝒪_{S_λ}) = ρ*(ψ_λ*(𝒪_{S_λ}))). Listed after the display fix (overlap); the fix restores the printed ρ*.",
      corrected=r"\rho_\lambda^*(\mathcal O_{S_\lambda})"),
    F(12, "Remarque (8.2.14): 'la limite inductive des ρ*_λ(𝒪_{S_λ}) est ρ*(𝒪_X) en vertu de (8.2.12)'",
      "ρ*(𝒪_X) (enlarged crop)",
      r"$\rho^*(\mathcal O_S)$ (silently corrected)",
      "misprint_in_print", None, "high",
      r"est $\rho^*(\mathcal O_S)$ en", r"est $\rho^*(\mathcal O_X)$ en",
      "There is no X in this remark: by (8.2.12) the limit of the ψ_λ*(𝒪_{S_λ}) is 𝒪_S and ρ* is exact, so the "
      "limit is ρ*(𝒪_S), as in the next line (ω♯ : ρ*(𝒪_S) → 𝒪_Y). The fix restores the printed 𝒪_X.",
      corrected=r"\rho^*(\mathcal O_S)"),
    F(12, "heading 8.3",
      "'8.3. Parties constructibles dans une limite projective de préschémas.' with a final full stop",
      r"\subsection{Parties constructibles dans une limite projective de préschémas} (no full stop)",
      "punctuation", None, "high",
      r"\subsection{Parties constructibles dans une limite projective de préschémas}",
      r"\subsection{Parties constructibles dans une limite projective de préschémas.}",
      "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop); none of the 53 \\subsection titles in "
      "ega4-8 to ega4-15 has it."),
    F(12, "(8.3.1): 'Dans toute la suite de ce paragraphe, nous supposons'",
      "'Dans toute la suite de ce paragraphe' italic, the rest roman (crop)",
      "all roman",
      "italics", None, "high",
      "Dans toute la suite de ce paragraphe, nous", r"\emph{Dans toute la suite de ce paragraphe}, nous"),
    F(12, "Théorème (8.3.2), label (i)",
      "(i) upright",
      r"\item[(i)] italic inside the italic theorem",
      "convention", 6, "high",
      r"\item[(i)] Pour tout", r"\item[\textup{(i)}] Pour tout",
      "Roman-numeral labels upright in the print (GLOBAL_ISSUES 16)."),
    F(12, "Théorème (8.3.2) (i): 'F_λ est ind-constructible (1.9.4).'",
      "reference (1.9.4) upright inside the italic statement",
      "(1.9.4) set in the italic theorem environment",
      "convention", 6, "high",
      "ind-constructible (1.9.4).", r"ind-constructible \textup{(1.9.4)}."),
    F(12, "Théorème (8.3.2), label (ii)",
      "(ii) upright",
      r"\item[(ii)] italic inside the italic theorem",
      "convention", 6, "high",
      r"\item[(ii)] Pour", r"\item[\textup{(ii)}] Pour", "As label (i)."),
    F(12, "Théorème (8.3.2), label (iii)",
      "(iii) upright",
      r"\item[(iii)] italic inside the italic theorem",
      "convention", 6, "high",
      r"\item[(iii)] Il existe", r"\item[\textup{(iii)}] Il existe", "As label (i)."),
    F(12, "Théorème (8.3.2) (iii): '(ce qui entraîne que S_λ est quasi-compact pour λ≥α).'",
      "the whole parenthesis printed roman (crop)",
      "set in the italic theorem environment",
      "convention", 6, "high",
      r"(ce qui entraîne que $S_\lambda$ est quasi-compact pour<NL>$\lambda\geq\alpha$)",
      r"\textup{(ce qui entraîne que $S_\lambda$ est quasi-compact pour<NL>$\lambda\geq\alpha$)}"),
    # ---------------- page 13 ----------------
    F(13, "Théorème (8.3.2) b): '(et alors on a u_μ^{-1}(E_μ) ⊂ u_μ^{-1}(F_μ) pour μ≥λ).'",
      "parenthesis printed roman (crop)",
      "set in the italic theorem environment",
      "convention", 6, "high",
      r"(et alors on a<NL>$u_\mu^{-1}(E_\mu)\subset u_\mu^{-1}(F_\mu)$ pour $\mu\geq\lambda$)",
      r"\textup{(et alors on a<NL>$u_\mu^{-1}(E_\mu)\subset u_\mu^{-1}(F_\mu)$ pour $\mu\geq\lambda$)}", PAREN),
    F(13, "Théorème (8.3.2) c): '(et alors on a E_μ ⊂ F_μ pour μ≥λ).'",
      "parenthesis printed roman (crop)",
      "set in the italic theorem environment",
      "convention", 6, "high",
      r"(et alors on a $E_\mu\subset F_\mu$ pour<NL>$\mu\geq\lambda$)",
      r"\textup{(et alors on a $E_\mu\subset F_\mu$ pour<NL>$\mu\geq\lambda$)}", PAREN),
    F(13, "proof of (8.3.2), display: 'G_λ = E_λ ∩ (S_λ—F_λ)'",
      "long dash for the set difference",
      r"S_\lambda-F_\lambda",
      "convention", 7, "high",
      r"(S_\lambda-F_\lambda)", r"(S_\lambda\setmin F_\lambda)",
      "\\setmin is not defined in EGA_IV3_FR.tex (preamble-base.tex defines it)."),
    F(13, "proof of (8.3.2), same display: 'G = E ∩ (S—F)'",
      "long dash for the set difference",
      "S-F",
      "convention", 7, "high",
      r"G=E\cap(S-F)", r"G=E\cap(S\setmin F)", "As the previous entry."),
    F(13, "proof of (8.3.2), second display: 'G_μ ⊂ u_λμ^{-1}(G_λ)  pour λ≤μ'",
      "no comma after 'pour λ≤μ'; the print sets 'G = ⋂_λ u_λ^{-1}(G_λ).' on a second line below (crop)",
      r"\text{pour }\lambda\leq\mu, \qquad G=...",
      "punctuation", None, "high",
      r"\text{pour }\lambda\leq\mu,<NL>\qquad", r"\text{pour }\lambda\leq\mu<NL>\qquad",
      "Comma added by the TeX; the two-line arrangement of the print is layout."),
    F(13, "Corollaire (8.3.3) b): '(et alors u_μ^{-1}(E_μ) = ∅ pour μ≥λ).'",
      "parenthesis printed roman (crop)",
      "set in the italic corollary environment",
      "convention", 6, "high",
      r"(et alors<NL>$u_\mu^{-1}(E_\mu)=\emptyset$ pour $\mu\geq\lambda$)",
      r"\textup{(et alors<NL>$u_\mu^{-1}(E_\mu)=\emptyset$ pour $\mu\geq\lambda$)}", PAREN),
    F(13, "Corollaire (8.3.3) c): '(et alors E_μ = ∅ pour μ≥λ).'",
      "parenthesis printed roman (crop)",
      "set in the italic corollary environment",
      "convention", 6, "high",
      r"(et alors<NL>$E_\mu=\emptyset$ pour $\mu\geq\lambda$)",
      r"\textup{(et alors<NL>$E_\mu=\emptyset$ pour $\mu\geq\lambda$)}", PAREN),
    F(13, "proof of (8.3.3): display 'u_λ(S) = ⋂_{μ≥λ} u_λμ(S_μ)' before 'd'où'",
      "no comma after the display (crop)",
      r"u_{\lambda\mu}(S_\mu), (comma)",
      "punctuation", None, "high",
      r"u_{\lambda\mu}(S_\mu),<NL>\]<NL>d'où", r"u_{\lambda\mu}(S_\mu)<NL>\]<NL>d'où",
      "Comma added by the TeX."),
    F(13, "Corollaire (8.3.4) b): '(et alors u_μ^{-1}(F_μ) = S pour μ≥λ).'",
      "parenthesis printed roman (crop)",
      "set in the italic corollary environment",
      "convention", 6, "high",
      r"(et alors<NL>$u_\mu^{-1}(F_\mu)=S$ pour $\mu\geq\lambda$)",
      r"\textup{(et alors<NL>$u_\mu^{-1}(F_\mu)=S$ pour $\mu\geq\lambda$)}", PAREN),
    # ---------------- page 14 ----------------
    F(14, "Corollaire (8.3.4) c), first line of the page: '(et alors F_μ = S_μ pour μ≥λ).'",
      "parenthesis printed roman",
      "set in the italic corollary environment",
      "convention", 6, "high",
      r"(et<NL>alors $F_\mu=S_\mu$ pour $\mu\geq\lambda$)",
      r"\textup{(et<NL>alors $F_\mu=S_\mu$ pour $\mu\geq\lambda$)}", PAREN),
    F(14, "Corollaire (8.3.5): 'pour que E⊂F (resp. E = F),'",
      "'(resp. E = F)' upright",
      "set in the italic corollary environment",
      "convention", 6, "high",
      "(resp. $E=F$)", r"\textup{(resp. $E=F$)}"),
    F(14, "Corollaire (8.3.5): 'tel que E_λ⊂F_λ (resp. E_λ = F_λ),'",
      "'(resp. E_λ = F_λ)' upright",
      "set in the italic corollary environment",
      "convention", 6, "high",
      r"(resp. $E_\lambda=F_\lambda$)", r"\textup{(resp. $E_\lambda=F_\lambda$)}"),
    F(14, "Corollaire (8.3.5): 'on a aussi E_μ⊂F_μ (resp. E_μ = F_μ) pour μ≥λ'",
      "'(resp. E_μ = F_μ)' upright",
      "set in the italic corollary environment",
      "convention", 6, "high",
      r"(resp. $E_\mu=F_\mu$)", r"\textup{(resp. $E_\mu=F_\mu$)}"),
    F(14, "proof of (8.3.7): 'X_λ = Spec(k(s))'",
      "bold italic k (crop)",
      r"\operatorname{Spec}(k(s))",
      "convention", 1, "high",
      r"\operatorname{Spec}(k(s))", r"\operatorname{Spec}(\boldsymbol{k}(s))"),
    F(14, "proof of (8.3.7): 'X_μ ≠ ∅ pour tout μ≥λ (I, 3.4.8)'",
      "(I, 3.4.8) with a bold I",
      "(I, 3.4.8)",
      "convention", 2, "high",
      "(I, 3.4.8)~;", r"(\textbf{I}, 3.4.8)~;"),
    F(14, "proof of (8.3.7), end: 'donc s∈u_λ(S) par (I, 3.4.8).'",
      "(I, 3.4.8) with a bold I",
      "(I, 3.4.8)",
      "convention", 2, "high",
      "par<NL>(I, 3.4.8).", r"par<NL>(\textbf{I}, 3.4.8)."),
    F(14, "Proposition (8.3.8), label (i)",
      "(i) upright",
      r"\item[(i)] italic inside the italic proposition",
      "convention", 6, "high",
      r"\item[(i)] Pour que", r"\item[\textup{(i)}] Pour que",
      "Roman-numeral labels upright in the print (GLOBAL_ISSUES 16)."),
    F(14, "Proposition (8.3.8) (i): 'soit dominant (resp. surjectif), il faut'",
      "'(resp.' and ')' roman, 'surjectif' italic (crop)",
      "(resp. surjectif) all italic",
      "convention", 6, "high",
      "dominant<NL>(resp. surjectif), il faut", r"dominant<NL>\textup{(resp.} surjectif\textup{)}, il faut", RESP),
    F(14, "Proposition (8.3.8) (i), end: 'soit dominant (resp. surjectif).'",
      "'(resp.' and ')' roman, 'surjectif' italic",
      "(resp. surjectif) all italic",
      "convention", 6, "high",
      "soit dominant (resp.<NL>surjectif).", r"soit dominant \textup{(resp.}<NL>surjectif\textup{)}.", RESP),
    F(14, "Proposition (8.3.8), label (ii)",
      "(ii) upright",
      r"\item[(ii)] italic inside the italic proposition",
      "convention", 6, "high",
      r"\item[(ii)] Si,", r"\item[\textup{(ii)}] Si,", "As label (i)."),
    F(14, "Proposition (8.3.8) (ii): 'sont plats (resp. fidèlement plats)'",
      "'(resp.' and ')' roman, 'fidèlement plats' italic (crop)",
      "(resp. fidèlement plats) all italic",
      "convention", 6, "high",
      "sont plats (resp. fidèlement plats)", r"sont plats \textup{(resp.} fidèlement plats\textup{)}", RESP),
    F(14, "Proposition (8.3.8) (ii), end: 'est plat (resp. fidèlement plat).'",
      "'(resp.' and ')' roman, 'fidèlement plat' italic (crop)",
      "(resp. fidèlement plat) all italic",
      "convention", 6, "high",
      "est plat (resp. fidèlement plat).", r"est plat \textup{(resp.} fidèlement plat\textup{)}.", RESP),
    F(14, "Proposition (8.3.8), label (iii)",
      "(iii) upright",
      r"\item[(iii)] italic inside the italic proposition",
      "convention", 6, "high",
      r"\item[(iii)] Supposons", r"\item[\textup{(iii)}] Supposons", "As label (i)."),
    F(14, "Proposition (8.3.8) (iii): 'soit un morphisme ouvert (resp. universellement ouvert), il faut'",
      "'(resp.' and ')' roman, 'universellement ouvert' italic (crop)",
      "(resp. universellement ouvert) all italic",
      "convention", 6, "high",
      "ouvert (resp. universellement ouvert), il faut",
      r"ouvert \textup{(resp.} universellement ouvert\textup{)}, il faut", RESP),
    F(14, "Proposition (8.3.8) (iii), end: 'u_λμ soit un morphisme ouvert (resp. universellement ouvert).'",
      "'(resp.' and ')' roman, 'universellement ouvert' italic (crop)",
      "(resp. universellement ouvert) all italic",
      "convention", 6, "high",
      "ouvert (resp.<NL>universellement ouvert).", r"ouvert \textup{(resp.}<NL>universellement ouvert\textup{)}.", RESP),
    F(14, "proof of (8.3.8) (ii): 'de (2.1.2) et (0_I, 6.2.3)'",
      "(0_I, 6.2.3) with a bold 0",
      r"$(0_{\mathrm I},6.2.3)$",
      "convention", 2, "high",
      r"$(0_{\mathrm I},6.2.3)$", r"$(\mathbf{0}_{\mathrm I},6.2.3)$"),
    F(14, "proof of (8.3.8) (iii): 'En vertu de (8.2.5) et de (I, 3.5.2)'",
      "(I, 3.5.2) with a bold I",
      "(I, 3.5.2)",
      "convention", 2, "high",
      "(I, 3.5.2)", r"(\textbf{I}, 3.5.2)"),
    F(14, "end of the page / page break 14-15: proof of (8.3.8) (iii)",
      "printed p. 15 begins 'Inversement, pour montrer que u_λ est ouvert ...' flush left, not indented: it continues "
      "the paragraph '(iii) En vertu de (8.2.5) ...' of p. 14 (page_015_s1.png; the next paragraph 'On notera' is "
      "indented)",
      r"blank line between 'prop. 1).' and \oldpage[IV-3]{15}: a paragraph break the print does not have",
      "marker", None, "high",
      r"n\textsuperscript{o} 1, prop. 1).<NL><NL>", r"n\textsuperscript{o} 1, prop. 1).<NL>",
      "Marker position itself is right (p. 15 starts with 'Inversement'); only the blank line goes. The old string "
      "ends the p. 14 segment (it ends right before \\oldpage[IV-3]{15}); GLOBAL_ISSUES 20."),
]


def norm(t):
    return t.replace("\r\n", "\n")


src = SRC.read_text(encoding="utf-8")
markers = {int(m.group(1)): m.start() for m in re.finditer(r"\\oldpage\[IV-3\]\{(\d+)\}", src)}
ok = True
for page in sorted({f["page"] for f in findings}):
    text = norm((RUN / f"page_{page:03d}.tex").read_text(encoding="utf-8"))
    seg = src[markers[page]:markers[page + 1]]
    work, swork = text, seg
    for f in [x for x in findings if x["page"] == page]:
        fx = f["fix"]
        if fx is None:
            continue
        old, new = fx["old"], fx["new"]
        c0, c1, s0, s1 = text.count(old), work.count(old), seg.count(old), swork.count(old)
        if c1 != 1 or s1 != 1 or c0 != 1 or s0 != 1:
            ok = False
            print("PROBLEM p.%d %r: page orig %d, page seq %d, seg orig %d, seg seq %d" % (page, old, c0, c1, s0, s1))
        work = work.replace(old, new, 1)
        swork = swork.replace(old, new, 1)
    print("page", page, "checked", len([x for x in findings if x["page"] == page]))

OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
counts = {}
for f in findings:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    counts.setdefault(f["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print("all fixes ok" if ok else "SOME FIXES FAILED")
print(counts)
print("written", OUT, len(findings))
