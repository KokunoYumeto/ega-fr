"""Write findings_180_184.json and check every fix: "old" occurs exactly once in its page_NNN.tex (LF-normalised)
and still exactly once when the page's fixes are applied in list order (as apply_fixes.py does)."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
OUT = RUN / "findings_180_184.json"


def L(*lines):
    return "\n".join(lines)


def F(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


BREAK_NOTE = ("Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). "
              "No blank line follows \\oldpage[II]{%d}, so this edit alone removes it.")
LAYOUT = "Layout only (display vs inline); the formula itself matches."

items = [
    # ---------------- page 180 ----------------
    F(180, "top of page: p. 179 ends 'on peut appliquer (3.8.5) à l'homo-', p. 180 begins 'morphisme τ de (8.8.1.2) : il y a'",
      "the sentence runs on across the 179/180 page break; the first line of p. 180 is not indented",
      "'à l'homomorphisme' + blank line, then \\oldpage[II]{180} and '$\\tau$ de ...': a paragraph break inside the sentence",
      "other", None, "high", None, None,
      "The edit lies OUTSIDE the p. 180 segment, at the end of the p. 179 segment of ega2-1-fr.tex: "
      "'à l'homomorphisme\\n\\n' -> 'à l'homomorphisme\\n' (GLOBAL_ISSUES item 20). No blank line follows "
      "\\oldpage[II]{180}. The whole word 'homomorphisme' (printed homo-|morphisme) before the marker is the usual placement."),
    F(180, "proof of (8.8.4), l. 3: 'et τ′=τ∘q*(φ) (φ injection canonique 𝒮′→𝒮)'",
      "τ′=τ∘q*(φ): italic q, no ascender (checked on a crop)",
      "$\\tau'=\\tau\\circ f^*(\\varphi)$",
      "misprint_in_print", None, "high",
      r"\tau'=\tau\circ f^*(\varphi)", r"\tau'=\tau\circ q^*(\varphi)",
      "The TeX silently corrects. τ is the homomorphism f*(𝒮)→⊕ℒ^{⊗n} of (8.8.1.2) (f: X→Y of (8.8.1)), so the "
      "composite needs f*(φ); in this section q is the morphism V(ℒ)→C_P (p. 179).",
      corrected=r"\tau'=\tau\circ f^*(\varphi)"),
    F(180, "proof of (8.8.4): 'on peut se ramener au cas où Y=Spec(A) est affine, 𝒮=S̃, 𝒮′=S̃′'",
      "S̃′: tilde over S only, prime outside (checked on a crop)",
      "\\widetilde{S'}",
      "convention", 8, "high", r"\widetilde{S'}", r"\widetilde{S}'"),
    F(180, "proof of (8.8.4): 'mais cela résulte de (I, 4.2.3).'",
      "(I, 4.2.3) with bold I", "plain I in the link text",
      "convention", 2, "high", "{I, 4.2.3}", r"{\textbf{I}, 4.2.3}"),
    F(180, "proof of (8.8.4): '... (I, 4.2.3). On a en outre Φ*(𝒪_{P′}(n))=𝒪_P(n)'",
      "'On a en outre' continues the paragraph: the line starts at the left margin, not indented (checked on a crop)",
      "blank line before 'On a en outre' (new paragraph)",
      "other", None, "high", L(").", "", "On a en outre"), L(").", "On a en outre"),
      "Independent of the bold-I edit in the reference just before it."),
    F(180, "proof of (8.8.4): '𝒮^≥_{P″}=⊕𝒪_{P″}(n) s'identifie à ⊕ℒ″^{⊗n} donc C_{P″}=...'",
      "no comma after ⊕ℒ″^{⊗n} before 'donc' (checked on a crop)",
      "$\\bigoplus_{n\\geqslant 0}\\mathcal{L}''^{\\otimes n}$, donc",
      "punctuation", None, "high",
      r"\mathcal{L}''^{\otimes n}$, donc", r"\mathcal{L}''^{\otimes n}$ donc"),
    F(180, "proof of (8.8.4), after the display under (8.8.4.1): '(3.3.2.3) (voir (8 8 5) ci-dessous)'",
      "(8 8 5): no periods between the figures, only gaps (a faint speck where the second one should be); checked on a 6x crop",
      "(\\hyperref[II.8.8.5-fr]{8.8.5})",
      "misprint_in_print", None, "medium",
      "{8.8.5}) ci-dessous", "{8 8 5}) ci-dessous",
      "The TeX silently corrects. The periods did not print (failed sorts or inking); the reading is clear.",
      corrected="8.8.5"),
    F(180, "end of the p. 180 segment, before \\oldpage[II]{181}: 'C″ est aussi un schéma quasi-compact, | et par suite g″∘u ...'",
      "the sentence continues on p. 181; the first line of p. 181 is not indented",
      "blank line after 'quasi-compact,' before the p. 181 marker starts a new paragraph",
      "other", None, "high", L("quasi-compact,", "", ""), L("quasi-compact,", ""), BREAK_NOTE % 181),

    # ---------------- page 181 ----------------
    F(181, "(8.8.5), l. 2: 'valable pour tout 𝒪_X-module inversible ℒ'",
      "𝒪_X-module with a lower-case m (checked on a crop)",
      "$\\mathcal{O}_X$-Module",
      "misprint_in_print", None, "high",
      r"$\mathcal{O}_X$-Module inversible $\mathcal{L}$", r"$\mathcal{O}_X$-module inversible $\mathcal{L}$",
      "The TeX silently corrects. ℒ is a sheaf; EGA writes 𝒪_X-Module with a capital M (cf. the lower-case 𝒪_X module "
      "treated as a misprint on p. 37).",
      corrected=r"$\mathcal{O}_X$-Module inversible $\mathcal{L}$"),
    F(181, "diagram (8.8.5.2), left square, top arrow V→X",
      "π above the arrow (checked on a crop)",
      "V\\ar[l]^{\\pi}: for a leftward arrow xy-pic sets a ^ label below",
      "other", None, "high", r"V\ar[l]^{\pi}", r"V\ar[l]_{\pi}",
      "Label side only. Same xy-pic behaviour as the fix on EGA II p. 12 (checked there by compiling)."),
    F(181, "diagram (8.8.5.2), left square, bottom arrow C→Y",
      "ψ below the arrow (checked on a crop)",
      "C\\ar[l]_{\\psi}: for a leftward arrow xy-pic sets a _ label above",
      "other", None, "high", r"C\ar[l]_{\psi}", r"C\ar[l]^{\psi}",
      "Label side only; independent of the previous edit."),
    F(181, "(8.8.5): 'Nous allons montrer que (si l'on suppose ℒ ample pour f) les morphismes g et g′ sont identiques.'",
      "'les morphismes g et g′ sont identiques' in italics (checked on a crop)",
      "no emphasis (the env body is roman)",
      "italics", None, "high",
      "les morphismes $g$ et $g'$ sont identiques.", r"\emph{les morphismes $g$ et $g'$ sont identiques}."),
    F(181, "(8.8.5), 2nd paragraph: 'identifier X à un ouvert de P=Proj(S), où S=A⊕⊕Γ(X, ℒ^{⊗n}); on déduit alors'",
      "the formula is set inline in the running text",
      "displayed with \\[ ... \\]",
      "other", None, "high",
      L("où", r"\[", r"  S=A\oplus\bigoplus_{n\geqslant 1}", r"  \Gamma(X,\mathcal{L}^{\otimes n})~;", r"\]", "on déduit"),
      L(r"où $S=A\oplus\bigoplus_{n\geqslant 1}\Gamma(X,\mathcal{L}^{\otimes n})$~;", "on déduit"),
      LAYOUT + " Apply BEFORE the next entry (the misprint n⩾0 in the same formula): after this edit "
      "'\\bigoplus_{n\\geqslant 1}' still occurs once; in the other order this 'old' no longer matches."),
    F(181, "(8.8.5), same formula: 'S=A⊕⊕_{n⩾0}Γ(X, ℒ^{⊗n})'",
      "index n⩾0 under the second ⊕ (checked on a crop)",
      "\\bigoplus_{n\\geqslant 1}",
      "misprint_in_print", None, "high",
      r"\bigoplus_{n\geqslant 1}", r"\bigoplus_{n\geqslant 0}",
      "The TeX silently corrects. By (8.8.1.1), 𝒮=𝒪_Y⊕⊕_{n⩾1}f_*(ℒ^{⊗n}), so on Y=Spec(A) the degree-0 part is A alone "
      "and the sum starts at n=1. Apply AFTER the previous (display-to-inline) entry.",
      corrected=r"S=A\oplus\bigoplus_{n\geqslant 1}\Gamma(X,\mathcal{L}^{\otimes n})"),
    F(181, "(8.8.5): 'Compte tenu de (0, 4.4.3)'",
      "(0, 4.4.3) with bold 0", "plain 0 in the link text",
      "convention", 2, "high", "{0, 4.4.3}", r"{\textbf{0}, 4.4.3}"),
    F(181, "(8.8.5): 'avec l'homomorphisme de restriction Γ(P, 𝒪_P(n))→Γ(X, 𝒪_P(n))=Γ(X, ℒ^{⊗n}), on obtient'",
      "the formula is set inline in the running text",
      "displayed with \\[ ... \\]",
      "other", None, "high",
      L("restriction", r"\[", r"  \Gamma(P,\mathcal{O}_P(n))\longrightarrow", r"  \Gamma(X,\mathcal{O}_P(n))=",
        r"  \Gamma(X,\mathcal{L}^{\otimes n}),", r"\]"),
      L("restriction",
        r"$\Gamma(P,\mathcal{O}_P(n))\longrightarrow\Gamma(X,\mathcal{O}_P(n))=\Gamma(X,\mathcal{L}^{\otimes n})$,"),
      LAYOUT),
    F(181, "Proposition (8.8.6): 'Supposons (avec les notations de (8.8.5)) que si'",
      "the reference (8.8.5) upright (checked on a crop)",
      "italic (inside the italic proposition environment)",
      "convention", 6, "high",
      r"(\hyperref[II.8.8.5-fr]{8.8.5})", r"\textup{(\hyperref[II.8.8.5-fr]{8.8.5})}"),
    F(181, "Proposition (8.8.6) (ii): 'Si X est intègre (resp. localement intègre et normal)'",
      "'(resp.' and the closing parenthesis upright, 'localement intègre et normal' italic (checked on a crop)",
      "all italic",
      "convention", 6, "high",
      "(resp. localement intègre et normal)", r"\textup{(resp. \emph{localement intègre et normal})}"),
    F(181, "Proposition (8.8.6) (ii): 'C est intègre (resp. normal).'",
      "'(resp.' upright, 'normal' italic (checked on a crop)",
      "all italic",
      "convention", 6, "high",
      "(resp. normal)", r"\textup{(resp. \emph{normal})}"),
    F(181, "proof of (8.8.6): 'il suffit (1.4.2) de voir que 𝒜(μ) : ψ_*(𝒪_C)→ψ_*(g_*(𝒪_V)) est un isomorphisme'",
      "the formula is set inline in the running text",
      "displayed with \\[ ... \\]",
      "other", None, "high",
      L("de voir que", r"\[", r"  \mathcal{A}(\mu):\psi_*(\mathcal{O}_C)", r"  \longrightarrow\psi_*(g_*(\mathcal{O}_V))", r"\]"),
      L("de voir que", r"$\mathcal{A}(\mu):\psi_*(\mathcal{O}_C)\longrightarrow\psi_*(g_*(\mathcal{O}_V))$"),
      LAYOUT),
    F(181, "end of the p. 181 segment, before \\oldpage[II]{182}: 'donc 𝒮=S̃, avec | S=⊕Γ(X, ℒ^{⊗n}); ...'",
      "the sentence continues on p. 182; the first line of p. 182 is not indented",
      "blank line after 'avec' before the p. 182 marker starts a new paragraph",
      "other", None, "high", L("$, avec", "", ""), L("$, avec", ""), BREAK_NOTE % 182),

    # ---------------- page 182 ----------------
    F(182, "proof of (8.8.6) (ii): 'l'anneau S est intègre (I, 7.4.4)'",
      "(I, 7.4.4) with bold I", "plain I in the link text",
      "convention", 2, "high", "{I, 7.4.4}", r"{\textbf{I}, 7.4.4}"),
    F(182, "proof of (8.8.6) (ii): 'donc il en est de même de C (I, 5.1.4)'",
      "(I, 5.1.4) with bold I", "plain I in the link text",
      "convention", 2, "high", "{I, 5.1.4}", r"{\textbf{I}, 5.1.4}"),
    F(182, "proof of Lemme (8.8.6.1): 'il résulte de (I, 8.2.1.1)'",
      "(I, 8.2.1.1) with bold I", "plain I in the link text",
      "convention", 2, "high", "{I, 8.2.1.1}", r"{\textbf{I}, 8.2.1.1}"),
    F(182, "proof of (8.8.6) (ii): 'montrons d'abord que V est localement intègre et normal'",
      "'localement intègre' and 'normal' italic, 'et' roman (checked on a crop)",
      "\\emph{localement intègre et normal}",
      "italics", None, "high",
      r"\emph{localement intègre et normal}", r"\emph{localement intègre} et \emph{normal}"),
    F(182, "Théorème (8.9.1) (ii): 'La restriction de q à V(ℒ)—j(X)'",
      "long dash for the set difference", "minus sign",
      "convention", 7, "high",
      r"$\mathbf{V}(\mathcal{L})-j(X)$ est une immersion", r"$\mathbf{V}(\mathcal{L})\setmin j(X)$ est une immersion",
      "\\setmin is not yet the long dash (global change pending)."),
    F(182, "Théorème (8.9.1) (ii), display 'V(ℒ)—j(X)→C'",
      "long dash for the set difference", "minus sign",
      "convention", 7, "high",
      r"\mathbf{V}(\mathcal{L})-j(X)\longrightarrow C", r"\mathbf{V}(\mathcal{L})\setmin j(X)\longrightarrow C",
      "As above."),
    F(182, "after (8.9.1): 'l'assertion découle alors de (I, 5.5.1, (i) et 5.5.10)'",
      "(I, 5.5.1, (i) et 5.5.10) with bold I", "plain I in the link text",
      "convention", 2, "high", "{I, 5.5.1, (i)}", r"{\textbf{I}, 5.5.1, (i)}"),
    F(182, "end of the p. 182 segment, before \\oldpage[II]{183}: 'On peut aussi supprimer | la même hypothèse ...'",
      "the sentence continues on p. 183; the first line of p. 183 is not indented",
      "blank line after 'supprimer' before the p. 183 marker starts a new paragraph",
      "other", None, "high", L("On peut aussi supprimer", "", ""), L("On peut aussi supprimer", ""), BREAK_NOTE % 183),

    # ---------------- page 183 ----------------
    F(183, "first paragraph: 'l'assertion découle cette fois de (I, 6.3.5)'",
      "(I, 6.3.5) with bold I", "plain I in the link text",
      "convention", 2, "high", "{I, 6.3.5}", r"{\textbf{I}, 6.3.5}"),
    F(183, "Corollaire (8.9.2): 'on peut dans l'énoncé de (8.9.1), supposer q propre'",
      "the reference (8.9.1) upright",
      "italic (inside the italic corollary environment)",
      "convention", 6, "high",
      r"(\hyperref[II.8.9.1-fr]{8.9.1}), supposer", r"\textup{(\hyperref[II.8.9.1-fr]{8.9.1})}, supposer"),
    F(183, "after (8.9.2): '(lorsque p : X→Y est propre)'",
      "'propre' italic (checked on a crop)", "roman",
      "italics", None, "high", "est propre) que", r"est \emph{propre}) que"),
    F(183, "after (8.9.2): 'que ℒ est ample relativement à p si et seulement si on peut « contracter » la section nulle du fibré vectoriel V(ℒ) en le préschéma de base Y.'",
      "'est ample relativement à p si et seulement si on peut' and 'la section nulle du fibré vectoriel V(ℒ) en le préschéma de base' italic; '« contracter »' and the final Y roman (checked on a crop)",
      "all roman",
      "italics", None, "high",
      L(r"$\mathcal{L}$ est ample relativement à $p$ si et seulement si on peut",
        r"«~contracter~» la section nulle du fibré vectoriel $\mathbf{V}(\mathcal{L})$",
        r"en le préschéma de base $Y$."),
      L(r"$\mathcal{L}$ \emph{est ample relativement à $p$ si et seulement si on peut}",
        r"«~contracter~» \emph{la section nulle du fibré vectoriel $\mathbf{V}(\mathcal{L})$",
        r"en le préschéma de base} $Y$."),
      "Independent of the 'propre' edit on the line before."),
    F(183, "(8.9.3): after the display 'V=V(ℒ)=Spec(𝒮′).': 'Le sous-préschéma fermé j(X), section nulle de V(ℒ), ...'",
      "'Le sous-préschéma fermé' begins an indented new paragraph",
      "no blank line after \\]: the text continues the paragraph without indentation",
      "other", None, "high", L(r"\]", "Le sous-préschéma fermé"), L(r"\]", "", "Le sous-préschéma fermé")),
    F(183, "(8.9.3): 'car la question est locale sur X, et cela revient à remarquer'",
      "comma after X (checked on a crop)", "no comma",
      "punctuation", None, "high", "locale sur $X$ et cela", "locale sur $X$, et cela"),
    F(183, "(8.9.3): after the display 'j_*(ℒ)=𝒥/𝒥².': 'D'autre part, si'",
      "'D'autre part, si' begins an indented new paragraph",
      "no blank line after \\]: the text continues the paragraph without indentation",
      "other", None, "high", L(r"\]", "D'autre part, si"), L(r"\]", "", "D'autre part, si")),
    F(183, "(8.9.3): 'On peut d'ailleurs plonger canoniquement π_*(𝒥)=𝒮′_+=⊕_{n⩾1}ℒ^{⊗n} dans le produit'",
      "the formula is set inline in the running text",
      "displayed with \\[ ... \\]",
      "other", None, "high",
      L("canoniquement", r"\[", r"  \pi_*(\mathcal{J})=\mathcal{S}'_+", r"  =\bigoplus_{n\geqslant 1}\mathcal{L}^{\otimes n}",
        r"\]", "dans le"),
      L("canoniquement", r"$\pi_*(\mathcal{J})=\mathcal{S}'_+=\bigoplus_{n\geqslant 1}\mathcal{L}^{\otimes n}$", "dans le"),
      LAYOUT),
    F(183, "(8.9.3): 'dans le produit Π_{n⩾1}ℒ^{⊗n}=lim_n π_*(𝒥/𝒥^{n+1}) (puisque'",
      "the formula is set inline in the running text (with n under the lim arrow, as in the TeX)",
      "displayed with \\[ ... \\]",
      "other", None, "high",
      L(r"\emph{produit}", r"\[", r"  \prod_{n\geqslant 1}\mathcal{L}^{\otimes n}",
        r"  =\varprojlim_n\pi_*(\mathcal{J}/\mathcal{J}^{n+1})", r"\]", "(puisque"),
      L(r"\emph{produit}", r"$\prod_{n\geqslant 1}\mathcal{L}^{\otimes n}=\varprojlim_n\pi_*(\mathcal{J}/\mathcal{J}^{n+1})$",
        "(puisque"),
      LAYOUT),
    F(183, "(8.9.3): '(puisque π_*(𝒥/𝒥^{n+1})=ℒ⊕ℒ^{⊗2}⊕...⊕ℒ^{⊗n})'",
      "baseline dots (checked on a crop)", "\\cdots",
      "symbol", None, "high", r"\oplus\cdots\oplus", r"\oplus\ldots\oplus",
      "Same treatment as the earlier \\cdots -> \\ldots fixes (GLOBAL_ISSUES item 22)."),
    F(183, "display (8.9.3.1): 'ℒ→lim π_*(𝒥/𝒥^{n+1})→ℒ'",
      "nothing under the lim arrow (checked on a crop; the inline lim two lines above has n)",
      "\\varprojlim_n",
      "formula", None, "high",
      L(r"\mathcal{L}\longrightarrow", r"  \varprojlim_n"), L(r"\mathcal{L}\longrightarrow", r"  \varprojlim")),
    F(183, "Proposition (8.9.4): 'qui est un 𝒪_V-Module inversible; si j : X→V est'",
      "'inversible' upright, 'Module' and the rest italic (checked on a crop)",
      "italic (inside the italic proposition environment)",
      "convention", 6, "high", "Module inversible~;", r"Module \textup{inversible}~;"),
    F(183, "end of the p. 183 segment, before \\oldpage[II]{184}: 'si j : X→V est | l'injection canonique, ...'",
      "the statement continues on p. 184; the first line of p. 184 is not indented",
      "blank line after 'est' before the p. 184 marker starts a new paragraph inside the proposition",
      "other", None, "high", L(r"$j:X\to V$ est", "", ""), L(r"$j:X\to V$ est", ""), BREAK_NOTE % 184),

    # ---------------- page 184 ----------------
    F(184, "Proposition (8.9.4) (ii): 'Il existe un homomorphisme de 𝒪_X-Modules φ : ℒ→lim π_*(𝒥/𝒥^{n+1}) tel que le composé'",
      "inline formula; nothing under the lim arrow (checked on a crop)",
      "displayed formula with \\varprojlim_n",
      "formula", None, "high",
      L(r"$\mathcal{O}_X$-Modules", r"  \[", r"    \varphi:\mathcal{L}\longrightarrow",
        r"    \varprojlim_n\pi_*(\mathcal{J}/\mathcal{J}^{n+1})", r"  \]", "  tel que le composé"),
      L(r"$\mathcal{O}_X$-Modules", r"  $\varphi:\mathcal{L}\longrightarrow\varprojlim\pi_*(\mathcal{J}/\mathcal{J}^{n+1})$",
        "  tel que le composé"),
      "Removes the subscript n of lim (not printed) and also sets the formula inline as printed (display vs inline); "
      "the two changes overlap, so there is no separate layout finding."),
    F(184, "Proposition (8.9.4) (ii), display 'ℒ→lim π_*(𝒥/𝒥^{n+1})→π_*(𝒥/𝒥²)=ℒ'",
      "nothing under the lim arrow (checked on a crop)", "\\varprojlim_n",
      "formula", None, "high",
      L(r"\varprojlim_n\pi_*(\mathcal{J}/\mathcal{J}^{n+1})", r"    \xrightarrow{\alpha}\pi_*(\mathcal{J}/\mathcal{J}^2)=\mathcal{L}"),
      L(r"\varprojlim\pi_*(\mathcal{J}/\mathcal{J}^{n+1})", r"    \xrightarrow{\alpha}\pi_*(\mathcal{J}/\mathcal{J}^2)=\mathcal{L}")),
    F(184, "Proposition (8.9.4) (iv): 'La restriction de q à W=V—j(X)'",
      "long dash for the set difference", "minus sign",
      "convention", 7, "high", "$W=V-j(X)$", r"$W=V\setmin j(X)$",
      "\\setmin is not yet the long dash (global change pending)."),
    F(184, "Proposition (8.9.4), last sentence: 'Dans ces conditions, ℒ est ample relativement à p.'",
      "an indented new paragraph after item (iv) (indent as for (iii), (iv))",
      "follows \\end{enumerate} without a blank line, so it starts flush left",
      "other", None, "medium",
      L(r"\end{enumerate}", "Dans ces conditions"), L(r"\end{enumerate}", "", "Dans ces conditions"),
      "Paragraph indentation after a list; layout-level."),
    F(184, "Lemme (8.10.1) (ii): 'où k est un corps, lim π_*(𝒪_V/𝒥^{n+1}) est isomorphe'",
      "nothing under the lim arrow (checked on a crop)", "\\varprojlim_n",
      "formula", None, "high", r"corps, $\varprojlim_n", r"corps, $\varprojlim"),
    F(184, "Lemme (8.10.1) (iii): 'et qu'il existe un homomorphisme φ : ℒ→lim π_*(𝒥/𝒥^{n+1}) tel que le composé'",
      "inline formula; nothing under the lim arrow (checked on a crop)",
      "displayed formula with \\varprojlim_n",
      "formula", None, "high",
      L("qu'il existe un homomorphisme", r"  \[", r"    \varphi:\mathcal{L}\longrightarrow",
        r"    \varprojlim_n\pi_*(\mathcal{J}/\mathcal{J}^{n+1})", r"  \]", "  tel que le composé"),
      L("qu'il existe un homomorphisme",
        r"  $\varphi:\mathcal{L}\longrightarrow\varprojlim\pi_*(\mathcal{J}/\mathcal{J}^{n+1})$", "  tel que le composé"),
      "Removes the subscript n and sets the formula inline as printed (overlapping changes, one edit)."),
    F(184, "Lemme (8.10.1) (iii): 'que le composé ℒ→lim π_*(𝒥/𝒥^{n+1})→π_*(𝒥/𝒥²) (α homomorphisme canonique)'",
      "inline formula; nothing under the lim arrow (checked on a crop)",
      "displayed formula with \\varprojlim_n",
      "formula", None, "high",
      L(r"  \[", r"    \mathcal{L}\xrightarrow{\varphi}", r"    \varprojlim_n\pi_*(\mathcal{J}/\mathcal{J}^{n+1})",
        r"    \xrightarrow{\alpha}\pi_*(\mathcal{J}/\mathcal{J}^2)", r"  \]", r"  ($\alpha$"),
      L(r"  $\mathcal{L}\xrightarrow{\varphi}\varprojlim\pi_*(\mathcal{J}/\mathcal{J}^{n+1})\xrightarrow{\alpha}\pi_*(\mathcal{J}/\mathcal{J}^2)$",
        r"  ($\alpha$"),
      "Removes the subscript n and sets the formula inline as printed (overlapping changes, one edit). "
      "Independent of the previous edit (adjacent lines, no overlap)."),
    F(184, "Lemme (8.10.1) (iii), end: '(complété qui est isomorphe au produit Πℒ^{⊗n}) sur lim π_*(𝒪_V/𝒥^{n+1}).'",
      "nothing under the lim arrow (checked on a crop)", "\\varprojlim_n",
      "formula", None, "high", L("sur", r"  $\varprojlim_n"), L("sur", r"  $\varprojlim")),
    F(184, "end of the p. 184 segment, before \\oldpage[II]{185}: 'j(X) est un point fermé j(ξ) de V, | et par définition ...'",
      "the sentence continues on p. 185; the first line of p. 185 is not indented",
      "blank line after 'de V,' before the p. 185 marker starts a new paragraph",
      "other", None, "high", L(r"$j(\xi)$ de $V$,", "", ""), L(r"$j(\xi)$ de $V$,", ""), BREAK_NOTE % 185),
]

# ---- checks ----
ok = True
texts = {p: (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for p in range(180, 185)}
work = dict(texts)
for i, x in enumerate(items):
    fx = x["fix"]
    if not fx:
        continue
    p = x["page"]
    n0 = texts[p].count(fx["old"])
    n1 = work[p].count(fx["old"])
    if n0 != 1 or n1 != 1:
        ok = False
        print(f"PROBLEM item {i} p{p}: original count {n0}, sequential count {n1}: {fx['old'][:60]!r}")
    else:
        work[p] = work[p].replace(fx["old"], fx["new"])
for p in range(180, 185):
    for a, b in ((r"\[", r"\]"), ("{", "}")):
        if work[p].count(a) != work[p].count(b):
            print(f"note p{p}: unbalanced {a} {b} after edits: {work[p].count(a)} vs {work[p].count(b)}")
    if work[p].count("$") % 2:
        print(f"PROBLEM p{p}: odd number of $ after edits"); ok = False
json.dump(items, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
cnt = {}
for x in items:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print("all fixes unique and sequentially applicable" if ok else "SOME FIXES FAILED")
print(len(items), cnt)
(RUN / "crops_180_184" / "after_edits_preview.txt").write_text(
    "\n\n".join(f"===== page {p}\n{work[p]}" for p in range(180, 185)), encoding="utf-8")
