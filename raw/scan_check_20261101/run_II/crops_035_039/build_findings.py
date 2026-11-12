import json
import pathlib
import sys

sys.stdout.reconfigure(encoding='utf-8')
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
OUT = RUN / "findings_035_039.json"
NL = "\n"


def F(page, where, scan, tex, kind, convention, confidence, old, new, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=convention,
             confidence=confidence, fix=(None if old is None else dict(old=old, new=new)))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


findings = [
    # ---------------- page 35 ----------------
    F(35, "Proof of (2.5.13), second paragraph, line 2: 'homomorphisme P→Q de S-modules gradués'",
      "homomorphisme P→Q de S-modules gradués (no comma after Q)",
      r"homomorphisme $P\to Q$, de $S$-modules gradués",
      "punctuation", None, "high",
      r"$P\to Q$, de", r"$P\to Q$ de",
      "Checked on a 1.5x crop: no comma after Q."),
    F(35, "Proof of (2.5.13), second paragraph: 'on voit aussitôt que η : z→u_z'",
      "η : z→u_z (plain arrow)", r"$\eta:z\mapsto u_z$",
      "convention", 3, "high",
      r"\eta:z\mapsto u_z", r"\eta:z\to u_z",
      "Plain arrow (checked on a 3x crop)."),
    F(35, "Proof of (2.5.13): 'D'autre part, soit η'_f l'isomorphisme N_(f)→Hom_{S_(f)}(S(n)_(f), N_(f)) qui, ...'",
      "the formula N_(f)→Hom_{S_(f)}(S(n)_(f), N_(f)) is set inline in the running text",
      r"the formula is displayed with \[ ... \]",
      "other", None, "high",
      "l'isomorphisme" + NL + r"\[" + NL + r"  N_{(f)}\longrightarrow" + NL
      + r"  \operatorname{Hom}_{S_{(f)}}\bigl(S(n)_{(f)},N_{(f)}\bigr)" + NL + r"\]" + NL + "qui,",
      "l'isomorphisme" + NL + r"$N_{(f)}\to\operatorname{Hom}_{S_{(f)}}(S(n)_{(f)},N_{(f)})$" + NL + "qui,",
      "Layout only (display vs inline); the formula itself matches. Independent of the comma finding that follows."),
    F(35, "Proof of (2.5.13): 'qui, à tout z'∈N_(f) fait correspondre l'homomorphisme v_z''",
      "qui, à tout z'∈N_(f) fait correspondre (no comma after N_(f))",
      r"qui, à tout $z'\in N_{(f)}$, fait correspondre",
      "punctuation", None, "high",
      r"$z'\in N_{(f)}$, fait", r"$z'\in N_{(f)}$ fait",
      "Checked on a 1.5x crop: the line ends with N_(f), no comma. The print leaves the incise unclosed, as in "
      "'qui, à l'élément 1⊗1 (...) fait correspondre' in the proof of (2.5.14) on the same page."),
    F(35, "End of the proof of (2.5.13): 'est l'isomorphisme z/f^h→z/f^{h−n}'",
      "z/f^h→z/f^{h−n} (plain arrow)", r"$z/f^h\mapsto z/f^{h-n}$",
      "convention", 3, "high",
      r"z/f^h\mapsto z/f^{h-n}", r"z/f^h\to z/f^{h-n}",
      "Plain arrow (checked on a 3x crop)."),
    F(35, "(2.5.13.1), left-hand side",
      "𝔍̃.M̃ (product written with a period on the baseline)",
      r"\widetilde{\mathfrak{J}}\cdot\widetilde{M}",
      "symbol", None, "high",
      r"\widetilde{\mathfrak{J}}\cdot\widetilde{M}", r"\widetilde{\mathfrak{J}}.\widetilde{M}",
      "Checked on a 2x crop: both product dots of (2.5.13.1) sit on the baseline (as in a_i.(t_i|V), EGA I p. 176). "
      "The right-hand dot is changed by the convention-5 fix that follows."),
    F(35, "(2.5.13.1), right-hand side",
      "(𝔍.M)~ (tilde after the parenthesis; baseline period)",
      r"\widetilde{\mathfrak{J}\cdot M}",
      "convention", 5, "high",
      r"=\widetilde{\mathfrak{J}\cdot M}", r"=(\mathfrak{J}.M)\supertilde",
      "The fix also writes the printed baseline period instead of \\cdot (see the symbol finding for the left-hand side)."),
    F(35, "Diagram after (2.5.13.1), top right vertex",
      "(𝔍⊗_S M)~", r"\widetilde{\mathfrak{J}\otimes_S M}",
      "convention", 5, "high",
      r"\widetilde{\mathfrak{J}\otimes_S M}", r"(\mathfrak{J}\otimes_S M)\supertilde",
      ""),
    F(35, "Proof of (2.5.14): 'fait correspondre l'élément 1∈(S(m+n))_{−(m+n)}'",
      "1∈(S(m+n))_{−(m+n)}", r"$1\in(S(m+n))_{-m-n}$",
      "formula", None, "high",
      r"_{-m-n}", r"_{-(m+n)}",
      "Checked on a 3x crop: the subscript is −(m+n), with parentheses."),

    # ---------------- page 36 ----------------
    F(36, "(2.5.15.1)",
      "(M(n))~=M̃(n)", r"\widetilde{M(n)}=\widetilde{M}(n)",
      "convention", 5, "high",
      r"\widetilde{M(n)}=\widetilde{M}(n)", r"(M(n))\supertilde=\widetilde{M}(n)",
      ""),
    F(36, "(2.6.1), first sentence: 'pour tout O_X-Module F (0, 5.4.6)'",
      "(0, 5.4.6) with bold 0", r"(\hyperref[0.5.4.6-fr]{0, 5.4.6})",
      "convention", 2, "high",
      r"$\mathcal{F}$" + NL + r"(\hyperref[0.5.4.6-fr]{0,",
      r"$\mathcal{F}$" + NL + r"(\hyperref[0.5.4.6-fr]{\textbf{0},",
      "Independent of the comma finding on the same reference (non-overlapping strings)."),
    F(36, "(2.6.1), end of the first sentence, before (2.6.1.1)",
      "'... ℱ (0, 5.4.6)' followed directly by the display (no comma)",
      r"(\hyperref[0.5.4.6-fr]{0, 5.4.6}),",
      "punctuation", None, "high",
      r"5.4.6})," + NL + r"\[", r"5.4.6})" + NL + r"\[",
      "Checked on a 2x crop: no comma after the reference."),
    F(36, "(2.6.1), after (2.6.1.1): 'Rappelons (0, 5.4.6) que'",
      "(0, 5.4.6) with bold 0", r"(\hyperref[0.5.4.6-fr]{0, 5.4.6})",
      "convention", 2, "high",
      "Rappelons" + NL + r"(\hyperref[0.5.4.6-fr]{0,",
      "Rappelons" + NL + r"(\hyperref[0.5.4.6-fr]{\textbf{0},",
      ""),
    F(36, "(2.6.2), first line: 'x→x/1 est un homomorphisme de groupes abéliens'",
      "x→x/1 with both x in bold italic",
      r"$x\mapsto x/1$ (ordinary italic x)",
      "misprint_in_print", None, "medium",
      r"$x\mapsto x/1$", r"$\boldsymbol{x}\mapsto\boldsymbol{x}/1$",
      "Wrong-font slip in the print: on a side-by-side 4x crop both x are clearly heavier than the italic x of "
      "'x/f^k avec x∈S'_{n+kd}' on the same page, while the arrow, the slash and the 1 have normal weight. "
      "The TeX silently corrects it (plain x); the fix restores the printed bold x and leaves the arrow to the "
      "convention-3 finding that follows. Apply this fix first: its 'old' contains the \\mapsto that the next fix replaces.",
      corrected=r"$x\to x/1$"),
    F(36, "(2.6.2), same formula x→x/1",
      "plain arrow →", r"\mapsto",
      "convention", 3, "high",
      r"\mapsto", r"\to",
      "Plain arrow (checked on a 6x crop). \\mapsto occurs once on the page before and after the misprint fix above; "
      "apply after it."),
    F(36, "Last line of the page: 's'identifie canoni-' (word continued as 'quement' on p. 37)",
      "canoniquement is hyphenated across the page break; the sentence and the word continue on p. 37 (no paragraph break)",
      "canoni-\\n\\n\\oldpage[II]{37}\\n\\nquement: blank lines before and after the marker make a paragraph break "
      "inside the word, and the hyphen is typeset",
      "other", None, "high",
      "canoni-" + NL + NL, "canoni%" + NL,
      "Spurious paragraph break inside a word at the page boundary (blank line before \\oldpage[II]{37}). Apply together "
      "with the p. 37 finding that removes the blank line after the marker; the result "
      "'canoni%\\n\\oldpage[II]{37}\\nquement' typesets 'canoniquement' with the marker at the printed page break."),

    # ---------------- page 37 ----------------
    F(37, "Top of the page: blank line after \\oldpage[II]{37}",
      "'quement à Γ(D_+(f), M̃), on obtient ...' continues the word and sentence of p. 36",
      r"\oldpage[II]{37} followed by a blank line before 'quement'",
      "other", None, "high",
      r"\oldpage[II]{37}" + NL + NL + "quement", r"\oldpage[II]{37}" + NL + "quement",
      "Apply together with the p. 36 finding (canoni- -> canoni%)."),
    F(37, "(2.6.2), first sentence: '... de groupes abéliens α_0^f : M_0→Γ(D_+(f), M̃). Il est clair que'",
      "the formula α_0^f : M_0→Γ(D_+(f), M̃). is set inline in the running text",
      r"the formula is displayed with \[ ... \]",
      "other", None, "high",
      "abéliens" + NL + r"\[" + NL + r"  \alpha_0^f:M_0\longrightarrow\Gamma(D_+(f),\widetilde{M})." + NL + r"\]"
      + NL + "Il est clair",
      "abéliens" + NL + r"$\alpha_0^f:M_0\to\Gamma(D_+(f),\widetilde{M})$." + NL + "Il est clair",
      "Layout only (display vs inline); the formula itself matches."),
    F(37, "(2.6.2): 'les sections α_0^f(x) et α_0^g(x) de M coïncident dans D_+(f)∩D_+(g)'",
      "de M (no tilde)", r"de $\widetilde{M}$ coïncident",
      "misprint_in_print", None, "high",
      r"de $\widetilde{M}$ coïncident", r"de $M$ coïncident",
      "Checked on a 3x crop with headroom: no tilde over this M (the tilde under it belongs to Γ(X, M̃) on the next "
      "line). α_0^f(x) and α_0^g(x) are sections of M̃, so the print omits the tilde; the TeX silently corrects it.",
      corrected=r"de $\widetilde{M}$ coïncident"),
    F(37, "(2.6.2), last paragraph: 'dans Γ_*(O_X) (0, 5.4.6)) que'",
      "(0, 5.4.6) with bold 0", r"(\hyperref[0.5.4.6-fr]{0, 5.4.6})",
      "convention", 2, "high",
      r"{0, 5.4.6}", r"{\textbf{0}, 5.4.6}",
      ""),
    F(37, "Proposition (2.6.3): 'ne s'annule pas (0, 5.5.2).'",
      "(0, 5.5.2): bold 0; the reference is upright inside the italic statement",
      r"(\hyperref[0.5.5.2-fr]{0, 5.5.2}) (plain 0, italic in the proposition environment)",
      "convention", 2, "high",
      r"(\hyperref[0.5.5.2-fr]{0, 5.5.2})", r"\textup{(\hyperref[0.5.5.2-fr]{\textbf{0}, 5.5.2})}",
      "Bold 0 in the print; the reference is also upright inside the italic statement (convention 6), so the fix sets "
      "both, as for EGA I pp. 172-173. No separate convention-6 entry."),
    F(37, "(2.6.4), first line: 'Soit maintenant F un O_X module, et posons'",
      "un 𝒪_X module (no hyphen, lower-case m)", r"un $\mathcal{O}_X$ module",
      "misprint_in_print", None, "medium",
      None, None,
      "The TeX keeps the printed reading. Elsewhere the text writes O_X-Module (e.g. (2.6.1), Proposition (2.6.5)).",
      corrected=r"un $\mathcal{O}_X$-Module"),

    # ---------------- page 38 ----------------
    F(38, "(2.6.4), first sentence: 'soit nulle, alors en raison de la remarque précédente'",
      "soit nulle, alors en raison (no comma after alors)", "soit nulle,\nalors, en raison",
      "punctuation", None, "high",
      "alors, en raison", "alors en raison",
      "Checked on a 2x crop."),
    F(38, "(2.6.4.2)",
      "β : (Γ_*(ℱ))~→ℱ", r"\beta:\widetilde{\Gamma_*(\mathcal{F})}",
      "convention", 5, "high",
      r"\beta:\widetilde{\Gamma_*(\mathcal{F})}", r"\beta:(\Gamma_*(\mathcal{F}))\supertilde",
      ""),
    F(38, "(2.6.5.1), middle term",
      "(Γ_*(M̃))~", r"\widetilde{\Gamma_*(\widetilde{M})}",
      "convention", 5, "high",
      r"\widetilde{\Gamma_*(\widetilde{M})}", r"(\Gamma_*(\widetilde{M}))\supertilde",
      ""),
    F(38, "(2.6.5.2), middle term",
      "Γ_*((Γ_*(ℱ))~)", r"\Gamma_*(\widetilde{\Gamma_*(\mathcal{F})})",
      "convention", 5, "high",
      r"\Gamma_*(\widetilde{\Gamma_*(\mathcal{F})})", r"\Gamma_*((\Gamma_*(\mathcal{F}))\supertilde)",
      ""),
    F(38, "Proof of (2.6.5): 'sections au-dessus de D_+(f) (I, 1.3.8)'",
      "(I, 1.3.8) with bold I", r"(\hyperref[I.1.3.8-fr]{I, 1.3.8})",
      "convention", 2, "high",
      r"{I, 1.3.8}", r"{\textbf{I}, 1.3.8}",
      ""),
    F(38, "Proof of (2.6.5): '(Γ_*(M̃))_n=Γ(X, M̃(n))=Γ(X, (M(n))~)'",
      "Γ(X, (M(n))~)", r"\Gamma(X,\widetilde{M(n)})",
      "convention", 5, "high",
      r"\Gamma(X,\widetilde{M(n)})", r"\Gamma(X,(M(n))\supertilde)",
      ""),

    # ---------------- page 39 ----------------
    F(39, "(2.7.2), condition (TF)",
      "(TF) Il existe un entier n tel que le sous-module ⊕_{k≥n} M_k soit un S-module de type fini. "
      "(text italic, label upright)",
      "the condition text is upright (env environment)",
      "convention", 6, "high",
      r"Il existe un entier $n$ tel que le sous-module" + NL + r"    $\bigoplus_{k\geq n}M_k$ soit un $S$-module de type fini.",
      r"\emph{Il existe un entier $n$ tel que le sous-module" + NL + r"    $\bigoplus_{k\geq n}M_k$ soit un $S$-module de type fini.}",
      "Checked on a crop: the condition texts of (TF) and (TN) are italic in the print."),
    F(39, "(2.7.2), condition (TN)",
      "(TN) Il existe un entier n tel que M_k=0 pour k≥n. (text italic, label upright)",
      "the condition text is upright (env environment)",
      "convention", 6, "high",
      r"Il existe un entier $n$ tel que $M_k=0$ pour $k\geq n$.",
      r"\emph{Il existe un entier $n$ tel que $M_k=0$ pour $k\geq n$.}",
      ""),
    F(39, "Proposition (2.7.3) (i): 'Si M vérifie la condition (TF), le O_X-Module'",
      "(TF) upright inside the italic statement", "(TF) italic in the proposition environment",
      "convention", 6, "high",
      "la condition (TF),", r"la condition \textup{(TF)},",
      "Checked on a crop."),
    F(39, "Proposition (2.7.3) (ii): 'Supposons que M vérifie (TF); pour que M̃=0'",
      "(TF) upright inside the italic statement", "(TF) italic in the proposition environment",
      "convention", 6, "high",
      "vérifie (TF)~; pour que", r"vérifie \textup{(TF)}~; pour que",
      ""),
    F(39, "Proposition (2.7.3) (ii): 'il faut et il suffit que M vérifie (TN).'",
      "(TN) upright inside the italic statement", "(TN) italic in the proposition environment",
      "convention", 6, "high",
      "il suffit que $M$ vérifie (TN).", r"il suffit que $M$ vérifie \textup{(TN)}.",
      ""),
    F(39, "Proof of (2.7.3): 'on a par suite (M/M')~=0'",
      "(M/M')~=0", r"$\widetilde{M/M'}=0$",
      "convention", 5, "high",
      r"$\widetilde{M/M'}=0$", r"$(M/M')\supertilde=0$",
      ""),
    F(39, "Proof of (2.7.3): 'et l'exactitude du foncteur M̃ (2.5.4) entraîne'",
      "du foncteur M̃ (2.5.4)", r"du foncteur $M\mapsto\widetilde{M}$ (2.5.4)",
      "extra", None, "high",
      r"$M\mapsto\widetilde{M}$", r"$\widetilde{M}$",
      "Checked on a 2x crop: the print names the functor by M̃ alone; the TeX adds 'M ↦'."),
    F(39, "Proof of (2.7.3): 'entraîne M̃=M̃''",
      "M̃=M̃' (tilde over M only, prime outside)", r"$\widetilde{M}=\widetilde{M'}$",
      "convention", 8, "high",
      r"$\widetilde{M}=\widetilde{M'}$", r"$\widetilde{M}=\widetilde{M}'$",
      "Checked on a 2x crop: the tilde covers only the M."),
    F(39, "Proof of (2.7.3): 'on est donc ramené au cas où M est de type fini.'",
      "de type fini in italics", "de type fini upright",
      "italics", None, "high",
      "au cas où $M$ est de type fini.", r"au cas où $M$ est \emph{de type fini}.",
      "Checked on a 2x crop."),
    F(39, "Proof of (2.7.3): 'S_(f)-module de type fini (I, 1.3.9)'",
      "(I, 1.3.9) with bold I", r"(\hyperref[I.1.3.9-fr]{I, 1.3.9})",
      "convention", 2, "high",
      r"{I, 1.3.9}", r"{\textbf{I}, 1.3.9}",
      ""),
    F(39, "Proof of (2.7.3), second paragraph: 'on a M̃'=0'",
      "M̃'=0 (tilde over M only, prime outside)", r"$\widetilde{M'}=0$",
      "convention", 8, "high",
      r"on a $\widetilde{M'}=0$", r"on a $\widetilde{M}'=0$",
      "Checked on a 3x crop."),
    # (blank line before \oldpage[II]{40}: already removed in the release file from MANUAL_II_findings_040_044)
]

# check: every old occurs exactly once in its page file (CRLF normalised); fixes on a page do not overlap
ok = True
for p in sorted({x["page"] for x in findings}):
    t = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    spans = []
    for x in findings:
        if x["page"] != p or not x["fix"]:
            continue
        old = x["fix"]["old"]
        n = t.count(old)
        if n != 1:
            ok = False
            print(f"p.{p}: old occurs {n} times: {old!r}")
            continue
        s = t.index(old)
        spans.append((s, s + len(old), old))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            print(f"p.{p}: overlapping olds: {a[2]!r} / {b[2]!r}")
for x in findings:
    if x["fix"] and ("\t" in x["fix"]["old"] + x["fix"]["new"] or "\r" in x["fix"]["new"]):
        ok = False
        print("control character in fix:", x["where"])

json.dump(findings, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
counts = {}
for x in findings:
    c = counts.setdefault(x["page"], [0, 0, 0])
    c[1 if x["kind"] == "convention" else 2 if x["kind"] == "misprint_in_print" else 0] += 1
print("all olds unique:", ok)
print({p: "/".join(map(str, c)) for p, c in sorted(counts.items())})
