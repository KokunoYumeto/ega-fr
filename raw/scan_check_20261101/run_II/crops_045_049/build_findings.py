"""Build findings_045_049.json for EGA II pp. 45-49 and validate every fix against the page files.
"¶" in a fragment stands for a line break (LF)."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
OUT = RUN / "findings_045_049.json"


def t(s):
    return None if s is None else s.replace("¶", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=t(tex), kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else dict(old=t(old), new=t(new)))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- boundary p. 44/45 (text before the p. 45 marker) ----------------
add(44, "end of p. 44 segment, blank line before \\oldpage[II]{45} (top of p. 45: 'lorsque m<0)')",
    "p. 45 begins 'lorsque m<0). On constate ...', continuing the sentence of p. 44 without a paragraph break",
    r"${f'}^{-m}x'/1$¶¶\oldpage[II]{45}¶lorsque",
    "other", None, "high",
    r"${f'}^{-m}x'/1$¶¶", r"${f'}^{-m}x'/1$¶",
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). The blank line lies in p. 44's "
    "segment, so this finding carries page 44; nothing after the p. 45 marker needs to change.")

# ---------------- p. 45 ----------------
add(45, "(2.8.8), display defining eta_f",
    "η_f : M'⊗_{S'}S → M'_{(f')}⊗_{S_{(f')}}S_{(f)}. (no prime on the S of the second tensor subscript)",
    r"\longrightarrow M'_{(f')}\otimes_{S'_{(f')}}S_{(f)}.",
    "misprint_in_print", None, "high",
    r"\longrightarrow M'_{(f')}\otimes_{S'_{(f')}}S_{(f)}.",
    r"\longrightarrow M'_{(f')}\otimes_{S_{(f')}}S_{(f)}.",
    "The print omits the prime (the factorisation a few lines below prints S'_{(f')}); the TeX silently corrects it. "
    "Fix restores the printed reading.",
    corrected=r"\otimes_{S'_{(f')}}")
add(45, "(2.8.8), proof: 'd'où, par (0, 1.5.4), Σ(...)=0'",
    "Σ_i(f'^r x_i/f'^{m_i+r})⊗(s_i/f^{n_i})=0 (x_i without prime)",
    r"{f'}^rx'_i/{f'}^{m_i+r}",
    "misprint_in_print", None, "high",
    r"{f'}^rx'_i/{f'}^{m_i+r}", r"{f'}^rx_i/{f'}^{m_i+r}",
    "The print has x_i (no prime) inside the fraction; the TeX silently corrects to x'_i.",
    corrected=r"{f'}^rx'_i/{f'}^{m_i+r}")
add(45, "(2.8.8), proof: 'c'est-à-dire η_f(Σ ...)=0'",
    "η_f(Σ_i x_i⊗y_i)=0 (x_i without prime, y_i instead of s_i)",
    r"\eta_f(\sum_i x'_i\otimes s_i)=0",
    "misprint_in_print", None, "high",
    r"\eta_f(\sum_i x'_i\otimes s_i)=0", r"\eta_f(\sum_i x_i\otimes y_i)=0",
    "Two printed slips in one formula (x_i for x'_i, y_i for s_i); the TeX silently corrects both.",
    corrected=r"\eta_f(\sum_i x'_i\otimes s_i)=0")
add(45, "(2.8.8), proof: 'par (0, 1.5.4)' (first)", "(0, 1.5.4) with bold 0", r"(\hyperref[0.1.5.4-fr]{0, 1.5.4})",
    "convention", 2, "high", r"par¶(\hyperref[0.1.5.4-fr]{0,", r"par¶(\hyperref[0.1.5.4-fr]{\textbf{0},", "")
add(45, "(2.8.9): 'l'application φ : s'→s'⊗1'", "φ : s'→s'⊗1 (plain arrow)", r"\varphi:s'\mapsto s'\otimes1",
    "convention", 3, "high", r"\varphi:s'\mapsto s'\otimes1", r"\varphi:s'\to s'\otimes1", "")
add(45, "Proposition (2.8.10): 'Le diagramme (2.8.9.1)'", "(2.8.9.1) upright inside the italic statement",
    r"(\hyperref[II.2.8.9.1-fr]{2.8.9.1})", "convention", 6, "high",
    r"(\hyperref[II.2.8.9.1-fr]{2.8.9.1})", r"\textup{(\hyperref[II.2.8.9.1-fr]{2.8.9.1})}", "")
add(45, "Proposition (2.8.10): ν : Φ*(M̃')→M̃", "Φ*(M̃'): tilde over M only, prime outside",
    r"\Phi^*(\widetilde{M'})", "convention", 8, "high",
    r"\nu:\Phi^*(\widetilde{M'})", r"\nu:\Phi^*(\widetilde{M}')", "Prime treated like an exponent (as at I, p. 196).")
add(45, "Proposition (2.8.10): '(2.8.8) est un isomorphisme'", "(2.8.8) upright inside the italic statement",
    r"(\hyperref[II.2.8.8-fr]{2.8.8})", "convention", 6, "high",
    r"(\hyperref[II.2.8.8-fr]{2.8.8})", r"\textup{(\hyperref[II.2.8.8-fr]{2.8.8})}", "")
add(45, "proof of (2.8.10): '(I, 3.2.6.2)'", "(I, 3.2.6.2) with bold I", r"{I, 3.2.6.2}", "convention", 2, "high",
    r"[I.3.2.6.2-fr]{I,", r"[I.3.2.6.2-fr]{\textbf{I},", "")
add(45, "proof of (2.8.10): 'il suffit (I, 3.2.2)'", "(I, 3.2.2) with bold I", r"{I, 3.2.2}", "convention", 2, "high",
    r"[I.3.2.2-fr]{I,", r"[I.3.2.2-fr]{\textbf{I},", "")
add(45, "proof of (2.8.10): 'conservant les degrés (0, 1.5.4)' (second)", "(0, 1.5.4) with bold 0",
    r"(\hyperref[0.1.5.4-fr]{0, 1.5.4})", "convention", 2, "high",
    r"[0.1.5.4-fr]{0, 1.5.4}). La seconde", r"[0.1.5.4-fr]{\textbf{0}, 1.5.4}). La seconde", "")
add(45, "Corollaire (2.8.11): 'M̃(n) s'identifie à'",
    "M̃(n): tilde over M only, (n) outside",
    r"\widetilde{M(n)}", "formula", None, "high",
    r"$\widetilde{M(n)}$ s'identifie", r"$\widetilde{M}(n)$ s'identifie",
    "Not a typographic variant: the print writes \\widetilde{M(n)} as (M(n))~ and distinguishes it from M̃(n), "
    "see (2.5.15.1) on p. 36 '(M(n))~ = M̃(n)'; the proof's citation of (2.5.15) fits the printed M̃(n).")
add(45, "Corollaire (2.8.11): 'Φ*(M̃'(n)) = M̃'(n)⊗_{Y'}O_Y'",
    "Φ*(M̃'(n)) = M̃'(n)⊗_{Y'}O_Y: tilde over M only in both",
    r"\Phi^*(\widetilde{M'(n)})=\widetilde{M'(n)}\otimes_{Y'}", "formula", None, "high",
    r"\Phi^*(\widetilde{M'(n)})=\widetilde{M'(n)}\otimes_{Y'}",
    r"\Phi^*(\widetilde{M}'(n))=\widetilde{M}'(n)\otimes_{Y'}",
    "Two occurrences in one edit; same reason as the previous finding (M̃'(n), not (M'(n))~).")

# ---------------- p. 46 ----------------
add(46, "(2.8.13): 'en vertu de (2.8.11) et (0, 4.3.3)'", "(0, 4.3.3) with bold 0", r"{0, 4.3.3}", "convention", 2,
    "high", r"[0.4.3.3-fr]{0,", r"[0.4.3.3-fr]{\textbf{0},", "")
add(46, "(2.8.13): 'Par suite (0, 3.7.1)'", "(0, 3.7.1) with bold 0", r"{0, 3.7.1}", "convention", 2, "high",
    r"[0.3.7.1-fr]{0,", r"[0.3.7.1-fr]{\textbf{0},", "")
add(46, "(2.8.13), display Γ_*(F')→Γ_*(F)", "Γ_*(F')→Γ_*(F). (asterisk subscript)",
    r"\Gamma_\bullet(\mathcal{F}')\longrightarrow¶  \Gamma_\bullet(\mathcal{F}).", "symbol", None, "high",
    r"\Gamma_\bullet(\mathcal{F}')\longrightarrow¶  \Gamma_\bullet(\mathcal{F}).",
    r"\Gamma_*(\mathcal{F}')\longrightarrow¶  \Gamma_*(\mathcal{F}).",
    "The print has Γ_* throughout; ega2-1-fr.tex uses \\Gamma_* 72 times and \\Gamma_\\bullet only 14 times "
    "(13 on pp. 46-49, one more at l. 7489).")
add(46, "(2.8.13): 'et F'=M̃''", "M̃': tilde over M only", r"\widetilde{M'}", "convention", 8, "high",
    r"$\mathcal{F}'=\widetilde{M'}$", r"$\mathcal{F}'=\widetilde{M}'$", "")
add(46, "(2.8.13), diagram: 'M'_{(f')} = Γ(D_+(f'), M̃')'", "Γ(D_+(f'), M̃'): tilde over M only",
    r"\Gamma(D_+(f'),\widetilde{M'})", "convention", 8, "high",
    r"(D_+(f'),\widetilde{M'})", r"(D_+(f'),\widetilde{M}')", "")
add(46, "diagram (2.8.13.1), top right Γ_*(M̃')", "Γ_* (asterisk)", r"\Gamma_\bullet(\widetilde{M'})", "symbol", None,
    "high", r"\ar[d]¶    & \Gamma_\bullet", r"\ar[d]¶    & \Gamma_*",
    "Independent of the convention-8 edit on the same entry (the two 'old' strings do not overlap).")
add(46, "diagram (2.8.13.1), top right Γ_*(M̃')", "M̃': tilde over M only", r"\Gamma_\bullet(\widetilde{M'})",
    "convention", 8, "high", r"(\widetilde{M'})\ar[d]", r"(\widetilde{M}')\ar[d]", "")
add(46, "diagram (2.8.13.1), bottom right Γ_*(M̃)", "Γ_* (asterisk)", r"\Gamma_\bullet(\widetilde{M})", "symbol", None,
    "high", r"& \Gamma_\bullet(\widetilde{M})", r"& \Gamma_*(\widetilde{M})", "")
add(46, "diagram (2.8.13.2), top left (Γ_*(F'))~", "(Γ_*(F'))~ (tilde after the parenthesis; Γ with asterisk)",
    r"\widetilde{\Gamma_\bullet(\mathcal{F}')}", "convention", 5, "high",
    r"\widetilde{\Gamma_\bullet(\mathcal{F}')}", r"(\Gamma_*(\mathcal{F}'))\supertilde",
    "The fix also replaces \\Gamma_\\bullet by \\Gamma_* (symbol difference nested inside; not reported separately).")
add(46, "diagram (2.8.13.2), bottom left (Γ_*(F))~", "(Γ_*(F))~ (tilde after the parenthesis; Γ with asterisk)",
    r"\widetilde{\Gamma_\bullet(\mathcal{F})}", "convention", 5, "high",
    r"\widetilde{\Gamma_\bullet(\mathcal{F})}", r"(\Gamma_*(\mathcal{F}))\supertilde",
    "The fix also replaces \\Gamma_\\bullet by \\Gamma_* (symbol difference nested inside; not reported separately).")
add(46, "last line of (2.8.13): 'F'→Φ*(F')=F)'", "…=F) with no final period",
    r"=\mathcal{F}$).", "punctuation", None, "high",
    r"=\mathcal{F}$).", r"=\mathcal{F}$)",
    "The print (a displayed line ending the page) has no period after the closing parenthesis.")

# ---------------- p. 47 ----------------
add(47, "(2.8.14.1), left side Φ*((M'⊗_{S'}N')~)", "(M'⊗_{S'}N')~", r"\widetilde{M'\otimes_{S'}N'}", "convention", 5,
    "high", r"\Phi^*(\widetilde{M'\otimes_{S'}N'})¶", r"\Phi^*((M'\otimes_{S'}N')\supertilde)¶", "")
add(47, "(2.8.14.1), right side (M⊗_S N)~", "(M⊗_S N)~", r"\widetilde{M\otimes_S N}", "convention", 5, "high",
    r"\longrightarrow\widetilde{M\otimes_S N}.", r"\longrightarrow(M\otimes_S N)\supertilde.", "")
add(47, "diagram (2.8.14.2), top left Φ*(M̃'⊗Ñ'): M̃'", "M̃': tilde over M only", r"\widetilde{M'}", "convention", 8,
    "high", r"\Phi^*(\widetilde{M'}\otimes", r"\Phi^*(\widetilde{M}'\otimes", "")
add(47, "diagram (2.8.14.2), top left Φ*(M̃'⊗Ñ'): Ñ'", "Ñ': tilde over N only", r"\widetilde{N'}", "convention", 8,
    "high", r"\widetilde{N'})¶      \ar[r]^{\sim}", r"\widetilde{N}')¶      \ar[r]^{\sim}", "")
add(47, "diagram (2.8.14.2), top right Φ*(M̃')", "M̃': tilde over M only", r"\widetilde{M'}", "convention", 8,
    "high", r"=\Phi^*(\widetilde{M'})", r"=\Phi^*(\widetilde{M}')", "")
add(47, "diagram (2.8.14.2), top right Φ*(Ñ')", "Ñ': tilde over N only", r"\widetilde{N'}", "convention", 8,
    "high", r"\Phi^*(\widetilde{N'})\\", r"\Phi^*(\widetilde{N}')\\", "")
add(47, "diagram (2.8.14.2), bottom left Φ*((M'⊗_{S'}N')~)", "(M'⊗_{S'}N')~", r"\widetilde{M'\otimes_{S'}N'}",
    "convention", 5, "high", r"(\widetilde{M'\otimes_{S'}N'})\ar[r]", r"((M'\otimes_{S'}N')\supertilde)\ar[r]", "")
add(47, "diagram (2.8.14.2), bottom right (M⊗_S N)~", "(M⊗_S N)~", r"\widetilde{M\otimes_S N}", "convention", 5,
    "high", r"& \widetilde{M\otimes_S N}", r"& (M\otimes_S N)\supertilde", "")
add(47, "after (2.8.14.2): 'l'isomorphisme canonique (0, 4.3.3)'", "(0, 4.3.3) with bold 0", r"{0, 4.3.3}",
    "convention", 2, "high", r"[0.4.3.3-fr]{0,", r"[0.4.3.3-fr]{\textbf{0},", "")
add(47, "(2.8.14.3), left side Φ*((Hom_{S'}(M', N'))~)", "(Hom_{S'}(M', N'))~",
    r"\widetilde{\operatorname{Hom}_{S'}(M',N')}", "convention", 5, "high",
    r"(\widetilde{\operatorname{Hom}_{S'}(M',N')})¶", r"((\operatorname{Hom}_{S'}(M',N'))\supertilde)¶", "")
add(47, "(2.8.14.3), right side (Hom_S(M, N))~", "(Hom_S(M, N))~", r"\widetilde{\operatorname{Hom}_S(M,N)}",
    "convention", 5, "high", r"\longrightarrow\widetilde{\operatorname{Hom}_S(M,N)}.",
    r"\longrightarrow(\operatorname{Hom}_S(M,N))\supertilde.", "")
add(47, "Hom diagram, top left Φ*((Hom_{S'}(M', N'))~)", "(Hom_{S'}(M', N'))~",
    r"\widetilde{\operatorname{Hom}_{S'}(M',N')}", "convention", 5, "high",
    r"(\widetilde{\operatorname{Hom}_{S'}(M',N')})\ar[r]", r"((\operatorname{Hom}_{S'}(M',N'))\supertilde)\ar[r]", "")
add(47, "Hom diagram, top right (Hom_S(M, N))~", "(Hom_S(M, N))~", r"\widetilde{\operatorname{Hom}_S(M,N)}",
    "convention", 5, "high", r"& \widetilde{\operatorname{Hom}_S(M,N)}\ar[d]",
    r"& (\operatorname{Hom}_S(M,N))\supertilde\ar[d]", "")
add(47, "Hom diagram, bottom left Hom(M̃', Ñ'): M̃'", "M̃': tilde over M only", r"\widetilde{M'}", "convention", 8,
    "high", r"(\widetilde{M'},", r"(\widetilde{M}',", "")
add(47, "Hom diagram, bottom left Hom(M̃', Ñ'): Ñ'", "Ñ': tilde over N only", r"\widetilde{N'}", "convention", 8,
    "high", r"\widetilde{N'}))\ar[r]", r"\widetilde{N}'))\ar[r]", "")
add(47, "last line: '(0, 4.4.6))'", "(0, 4.4.6) with bold 0", r"{0, 4.4.6}", "convention", 2, "high",
    r"[0.4.4.6-fr]{0,", r"[0.4.4.6-fr]{\textbf{0},", "")

# ---------------- p. 48 ----------------
add(48, "Proposition (2.9.2) (i): 'homomorphisme (TN)-surjectif'", "(TN) upright, -surjectif italic",
    r"homomorphisme (TN)-surjectif", "convention", 6, "high",
    r"homomorphisme (TN)-surjectif", r"homomorphisme \textup{(TN)}-surjectif", "")
add(48, "Proposition (2.9.2) (i): 'correspondant Φ (2.8.1)'", "(2.8.1) upright inside the italic statement",
    r"(\hyperref[II.2.8.1-fr]{2.8.1}) est", "convention", 6, "high",
    r"(\hyperref[II.2.8.1-fr]{2.8.1}) est", r"\textup{(\hyperref[II.2.8.1-fr]{2.8.1})} est", "")
add(48, "Proposition (2.9.2) (ii): 'image réciproque de Γ_*(J)'", "Γ_*(𝒥)", r"\Gamma_\bullet(\mathcal{J})", "symbol",
    None, "high", r"\Gamma_\bullet(\mathcal{J})$ par", r"\Gamma_*(\mathcal{J})$ par", "")
add(48, "Proposition (2.9.2) (ii): 'α : S→Γ_*(O_X)'", "Γ_*(O_X)", r"\Gamma_\bullet(\mathcal{O}_X)", "symbol", None,
    "high", r"\to\Gamma_\bullet(\mathcal{O}_X)$", r"\to\Gamma_*(\mathcal{O}_X)$", "")
add(48, "Proposition (2.9.2) (ii): '(2.6.2), et posons'", "(2.6.2) upright inside the italic statement",
    r"(\hyperref[II.2.6.2-fr]{2.6.2}), et posons", "convention", 6, "high",
    r"(\hyperref[II.2.6.2-fr]{2.6.2}), et posons", r"\textup{(\hyperref[II.2.6.2-fr]{2.6.2})}, et posons", "")
add(48, "proof of (2.9.2) (i): '(I, 4.2.3)'", "(I, 4.2.3) with bold I", r"{I, 4.2.3}", "convention", 2, "high",
    r"[I.4.2.3-fr]{I,", r"[I.4.2.3-fr]{\textbf{I},", "")
add(48, "after the proof of (2.9.2): 'j̃(J̃')=J'", "j̃(𝔍̃'): tilde over 𝔍 only, prime outside",
    r"\widetilde{\mathfrak{J}'}", "convention", 8, "high",
    r"\widetilde{j}(\widetilde{\mathfrak{J}'})", r"\widetilde{j}(\widetilde{\mathfrak{J}}')", "")
add(48, "after the proof of (2.9.2): 'α(J')⊂Γ_*(J)'", "Γ_*(𝒥)", r"\Gamma_\bullet(\mathcal{J})", "symbol", None,
    "high", r"\subset\Gamma_\bullet(\mathcal{J})$", r"\subset\Gamma_*(\mathcal{J})$", "")
add(48, "Corollaire (2.9.3): '(2.9.2, (i))'", "(2.9.2, (i)) upright inside the italic statement",
    r"(\hyperref[II.2.9.2-fr]{2.9.2}, (i))", "convention", 6, "high",
    r"(\hyperref[II.2.9.2-fr]{2.9.2}, (i))", r"\textup{(\hyperref[II.2.9.2-fr]{2.9.2}, (i))}", "")
add(48, "Corollaire (2.9.3): 'Φ*((S(n))~)'", "Φ*((S(n))~)", r"\Phi^*(\widetilde{S(n)})", "convention", 5, "high",
    r"\Phi^*(\widetilde{S(n)})", r"\Phi^*((S(n))\supertilde)", "")
add(48, "Corollaire (2.9.3): 'isomorphe à (S'(n))~'", "(S'(n))~", r"\widetilde{S'(n)}", "convention", 5, "high",
    r"\widetilde{S'(n)}", r"(S'(n))\supertilde", "")
add(48, "Corollaire (2.9.4): '(2.9.2, (ii))'", "(2.9.2, (ii)) upright inside the italic statement",
    r"(\hyperref[II.2.9.2-fr]{2.9.2}, (ii))", "convention", 6, "high",
    r"(\hyperref[II.2.9.2-fr]{2.9.2}, (ii))", r"\textup{(\hyperref[II.2.9.2-fr]{2.9.2}, (ii))}", "")

# ---------------- p. 49 ----------------
add(49, "proof of (2.9.4), display 0→Γ_*(J)→Γ_*(O_X)→Γ_*(O_X/J)", "Γ_* three times",
    r"\Gamma_\bullet (three times)", "symbol", None, "high",
    r"0\longrightarrow\Gamma_\bullet(\mathcal{J})¶  \longrightarrow\Gamma_\bullet(\mathcal{O}_X)¶  \longrightarrow\Gamma_\bullet(\mathcal{O}_X/\mathcal{J}).",
    r"0\longrightarrow\Gamma_*(\mathcal{J})¶  \longrightarrow\Gamma_*(\mathcal{O}_X)¶  \longrightarrow\Gamma_*(\mathcal{O}_X/\mathcal{J}).",
    "")
add(49, "proof of (2.9.4): 'l'image dans Γ_*(O_X/J)'", "Γ_*(O_X/𝒥)", r"\Gamma_\bullet(\mathcal{O}_X/\mathcal{J})",
    "symbol", None, "high", r"$\Gamma_\bullet(\mathcal{O}_X/\mathcal{J})$ de",
    r"$\Gamma_*(\mathcal{O}_X/\mathcal{J})$ de", "")
add(49, "proof of (2.9.4): 'en vertu de (I, 7.4.4)'", "(I, 7.4.4) with bold I", r"{I, 7.4.4}", "convention", 2,
    "high", r"[I.7.4.4-fr]{I,", r"[I.7.4.4-fr]{\textbf{I},", "")
add(49, "(3.1.1): 'lui-même (I, 1.3.8 et 1.3.9);'",
    "(I, 1.3.8 et 1.3.9); one pair of parentheses, 'I,' once",
    r"((\hyperref[I.1.3.8-fr]{I, 1.3.8}) et¶(\hyperref[I.1.3.9-fr]{I, 1.3.9}))", "extra", None, "high",
    r"((\hyperref[I.1.3.8-fr]{I, 1.3.8}) et¶(\hyperref[I.1.3.9-fr]{I, 1.3.9}))",
    r"(\hyperref[I.1.3.8-fr]{I, 1.3.8} et¶\hyperref[I.1.3.9-fr]{1.3.9})",
    "TeX renders '((I, 1.3.8) et (I, 1.3.9))'. Apply before the next finding (its convention-2 edit of '{I, 1.3.8}' "
    "matches before and after this edit, but this edit no longer matches once that one is applied).")
add(49, "(3.1.1): 'lui-même (I, 1.3.8 et 1.3.9)': bold I", "bold I", r"{I, 1.3.8}", "convention", 2, "high",
    r"{I, 1.3.8}", r"{\textbf{I}, 1.3.8}", "Apply after the previous finding.")
add(49, "(3.1.1): 'qui est quasi-cohérente si S l'est (I, 1.3.9)'", "(I, 1.3.9) with bold I", r"{I, 1.3.9}",
    "convention", 2, "high", r"[I.1.3.9-fr]{I, 1.3.9})~; pour", r"[I.1.3.9-fr]{\textbf{I}, 1.3.9})~; pour", "")
add(49, "(3.1.1): 'la somme directe des M_{nd+k}(n∈Z) qui est un'", "no comma after (n∈Z)",
    r"($n\in\mathbf{Z}$), qui est un", "punctuation", None, "high",
    r"($n\in\mathbf{Z}$), qui est un", r"($n\in\mathbf{Z}$) qui est un",
    "The parallel phrase two lines earlier ('S_{nd} (n∈Z), qui est quasi-cohérente') does have the comma in print.")
add(49, "(3.1.1): 'quasi-cohérents (I, 9.6.1). On notera'", "(I, 9.6.1) with bold I", r"{I, 9.6.1}", "convention",
    2, "high", r"[I.9.6.1-fr]{I, 9.6.1}). On", r"[I.9.6.1-fr]{\textbf{I}, 9.6.1}). On", "")
add(49, "(3.1.1): '(M(n))_k = M_{n+k}'", "M_{n+k} with the subscript n in bold italic (wrong font)",
    r"\mathcal{M}_{n+k}", "misprint_in_print", None, "medium",
    r"\mathcal{M}_{n+k}$", r"\mathcal{M}_{\boldsymbol{n}+k}$",
    "Wrong-font sort: the n of the subscript is clearly heavier than the k beside it and than the n of (M(n))_k. "
    "The TeX silently has the normal n.",
    corrected=r"\mathcal{M}_{n+k}")
add(49, "(3.1.1): 'gradué quasi-cohérent (I, 9.6.1).' (second)", "(I, 9.6.1) with bold I", r"{I, 9.6.1}",
    "convention", 2, "high", r"[I.9.6.1-fr]{I, 9.6.1}).¶", r"[I.9.6.1-fr]{\textbf{I}, 9.6.1}).¶", "")
add(49, "(3.1.1): 'homomorphisme surjectif de degré 0 :'", "'de degré 0 :' with a colon before the formula",
    r"de degré~$0$ (no colon)", "punctuation", None, "high",
    r"surjectif¶de degré~$0$¶", r"surjectif¶de degré~$0$~:¶", "")
add(49, "(3.1.1): 'conoyau d'un homomorphisme de degré 0 :'", "'de degré 0 :' with a colon before the formula",
    r"degré~$0$ (no colon)", "punctuation", None, "high",
    r"homomorphisme de¶degré~$0$¶", r"homomorphisme de¶degré~$0$~:¶", "")
add(49, "end of p. 49 segment, blank line before \\oldpage[II]{50} ('est une A-algèbre | graduée')",
    "the sentence continues on p. 50 ('graduée (I, 1.4.3); posons') without a paragraph break",
    r"$A$-algèbre¶¶\oldpage[II]{50}¶¶graduée", "other", None, "high",
    r"est une¶$A$-algèbre¶¶", r"est une¶$A$-algèbre¶",
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). Apply together with the page-50 "
    "finding that removes the blank line after the marker.")

# ---------------- boundary p. 49/50 (start of p. 50's segment) ----------------
add(50, "start of p. 50 segment, blank line after \\oldpage[II]{50}",
    "p. 50 begins 'graduée (I, 1.4.3)', continuing the sentence of p. 49",
    r"\oldpage[II]{50}¶¶graduée", "other", None, "high",
    r"\oldpage[II]{50}¶¶graduée", r"\oldpage[II]{50}¶graduée",
    "Second half of the p. 49 boundary fix (outside pp. 45-49); apply both or neither.")

# ---------------- validation ----------------
pages = {}
for d in F:
    n = d["page"]
    if n not in pages:
        pages[n] = (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
errors = 0
for d in F:
    if d["fix"]:
        c = pages[d["page"]].count(d["fix"]["old"])
        if c != 1:
            errors += 1
            print("NOT UNIQUE", d["page"], c, repr(d["fix"]["old"]))
# simulate application in list order, page by page
sim = dict(pages)
for d in F:
    if d["fix"]:
        s = sim[d["page"]]
        c = s.count(d["fix"]["old"])
        if c != 1:
            errors += 1
            print("SEQUENTIAL FAIL", d["page"], c, repr(d["fix"]["old"]))
        else:
            sim[d["page"]] = s.replace(d["fix"]["old"], d["fix"]["new"])
for n in (46, 48, 49):
    left = sim[n].count("\\Gamma_\\bullet")
    print("page", n, "Gamma_bullet left after all fixes:", left)
counts = {}
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    counts.setdefault(d["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print(json.dumps(counts))
print("errors:", errors, "findings:", len(F))
if not errors:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
    print("written", OUT)
