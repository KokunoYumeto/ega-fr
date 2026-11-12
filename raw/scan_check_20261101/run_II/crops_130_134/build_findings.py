"""Build findings_130_134.json (pages 130-134 of EGA II) and check every fix against page_NNN.tex.
In the fragments below the pilcrow stands for a line break (LF)."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
OUT = RUN / "findings_130_134.json"
P = "\u00b6"


def nl(s):
    return None if s is None else s.replace(P, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, nofix=False):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if nofix else {"old": nl(old), "new": nl(new)})
    if kind == "misprint_in_print":
        d["corrected"] = nl(corrected)
    d["note"] = note
    F.append(d)


BL = "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20)."

# ---------------- page 130
# The 129/130 boundary (marker before 'lui correspond', printed reading 6.5.5.1, blank lines) was already applied to the
# release file from findings_125_129.json; only the upright reference remains. Its 'old' exists in the release file's
# p. 130 segment as it stands now, not in the page_130.tex snapshot (where the words still sit before the marker).
REL_ONLY = {len(F)}
add(130, "line 1, reference in Corollaire (6.5.7): 'lui correspond (6.5.5.1). Alors on a'",
    "(6.5.5.1) upright in the italic statement",
    r"after the applied p. 129 fixes: 'lui correspond (\hyperref[II.6.5.5.1-fr]{6.5.5.1}).' inside the corollary environment, so italic",
    "convention", 6, "high",
    r"(\hyperref[II.6.5.5.1-fr]{6.5.5.1})", r"\textup{(\hyperref[II.6.5.5.1-fr]{6.5.5.1})}",
    "Checked on a crop. The 'old' is in the release file's p. 130 segment as changed by the findings_125_129 fixes "
    "(marker moved before 'lui correspond', 6.5.5.3 restored to the printed 6.5.5.1); it is not in the page_130.tex "
    "snapshot, which predates those fixes.")
add(130, "line 1, Cor. (6.5.7)", "g(X'\u2014X'_{f'})", "g(X'-X'_{f'})", "convention", 7, "high",
    r"$g(X'-X'_{f'})=", r"$g(X'\setmin X'_{f'})=", "Set difference.")
add(130, "line 1, Cor. (6.5.7)", "X\u2014X_f", "X-X_f", "convention", 7, "high",
    r"=X-X_f$", r"=X\setmin X_f$", "Set difference.")
add(130, "proof of (6.5.7), line 1", "g(X'\u2014X'_{f'}) est ferm\u00e9", "g(X'-X'_{f'}) est ferm\u00e9", "convention", 7, "high",
    r"$g(X'-X'_{f'})$ est", r"$g(X'\setmin X'_{f'})$ est", "Set difference.")
add(130, "Prop. (6.5.8), after the diagram", "'On suppose, soit que ...' begins an indented new paragraph",
    "no blank line after the diagram, so no new paragraph", "other", None, "high",
    r"\]¶On suppose, soit que", r"\]¶¶On suppose, soit que",
    "Checked on a crop: 'On suppose' is indented like a paragraph start; the text after other displays on these pages is flush left.")
add(130, "Prop. (6.5.8)", "v\u00e9rifient (II), que -- (II) upright", "(II) italic (proposition environment)",
    "convention", 6, "high", r"v\u00e9rifient (II), que", r"v\u00e9rifient \textup{(II)}, que", "Checked on a crop.")
add(130, "Prop. (6.6.1)", "(II bis) entirely upright", r"(II \emph{bis}): '(II' and ')' italic, 'bis' upright",
    "convention", 6, "high", r"(II¶\emph{bis})", r"\textup{(II bis)}", "Checked on a crop.")
add(130, "Cor. (6.6.2)", "(II bis) entirely upright", r"(II \emph{bis}): '(II' and ')' italic, 'bis' upright",
    "convention", 6, "high", r"(II \emph{bis}). Alors", r"\textup{(II bis)}. Alors", "Checked on a crop.")
add(130, "last line, page break 130/131 ('soit T | le noyau')", "sentence continues on p. 131",
    r"blank line before \oldpage[II]{131}", "other", None, "high",
    r"contraire, soit $\mathcal{T}$¶¶", r"contraire, soit $\mathcal{T}$¶",
    BL + " Apply together with the p. 131 entry that removes the blank line after the marker.")

# ---------------- page 131
add(131, "line 1, page break 130/131", "le noyau de cet homomorphisme (continues the sentence of p. 130)",
    r"blank line after \oldpage[II]{131}", "other", None, "high",
    r"\oldpage[II]{131}¶¶le noyau", r"\oldpage[II]{131}¶le noyau",
    BL + " Apply together with the p. 130 entry that removes the blank line before the marker.")
add(131, "line 1", "(I, 6.1.1) with bold I", "(I, 6.1.1)", "convention", 2, "high",
    r"{I, 6.1.1}", r"{\textbf{I}, 6.1.1}", "Checked on a crop.")
add(131, "after the diagram", "(0, 5.2.2) with bold 0", "(0, 5.2.2)", "convention", 2, "high",
    r"{0, 5.2.2}", r"{\textbf{0}, 5.2.2}", "")
add(131, "after the diagram", "(I, 7.4.6) with bold I", "(I, 7.4.6)", "convention", 2, "high",
    r"{I, 7.4.6}", r"{\textbf{I}, 7.4.6}", "")
add(131, "'on a par d\u00e9finition ...'",
    "inline: g'_*(O_X'')\u2297R(X) = (B/T)\u2297R(X) = g_*(O_X')\u2297R(X), donc ...",
    "displayed formula", "other", None, "high",
    r"\[¶g'_*(\mathcal{O}_{X''})\otimes_{\mathcal{O}_X}\mathcal{R}(X)¶=(\mathcal{B}/\mathcal{T})\otimes_{\mathcal{O}_X}\mathcal{R}(X)¶=g_*(\mathcal{O}_{X'})\otimes_{\mathcal{O}_X}\mathcal{R}(X),¶\]",
    r"$g'_*(\mathcal{O}_{X''})\otimes_{\mathcal{O}_X}\mathcal{R}(X)¶=(\mathcal{B}/\mathcal{T})\otimes_{\mathcal{O}_X}\mathcal{R}(X)¶=g_*(\mathcal{O}_{X'})\otimes_{\mathcal{O}_X}\mathcal{R}(X)$,",
    "Layout only (display vs inline); the formula itself matches.")
add(131, "'et en outre ... est injectif'", "inline: g'_*(O_X'') \u2192 g'_*(O_X'')\u2297R(X)",
    "displayed formula", "other", None, "high",
    r"\[¶g'_*(\mathcal{O}_{X''})\longrightarrow¶g'_*(\mathcal{O}_{X''})\otimes_{\mathcal{O}_X}\mathcal{R}(X)¶\]",
    r"$g'_*(\mathcal{O}_{X''})\to¶g'_*(\mathcal{O}_{X''})\otimes_{\mathcal{O}_X}\mathcal{R}(X)$",
    "Layout only (display vs inline); the formula itself matches.")
add(131, "'qu'\u00e0 tout isomorphisme ... correspond canoniquement'", "inline: \u03b7_\u03bb : g_*(L')|U_\u03bb \u2192 B|U_\u03bb",
    "displayed formula", "other", None, "high",
    r"\[¶\eta_\lambda:g_*(\mathcal{L}')|U_\lambda\longrightarrow¶\mathcal{B}|U_\lambda¶\]",
    r"$\eta_\lambda:g_*(\mathcal{L}')|U_\lambda\to\mathcal{B}|U_\lambda$",
    "Layout only (display vs inline); the formula itself matches.")
add(131, "display \u03b7'_\u03bb : g'_*(L'')|U_\u03bb \u2192 (B/T)|U_\u03bb", "no punctuation after the display",
    "comma after (B/T)|U_\u03bb", "punctuation", None, "high",
    r"(\mathcal{B}/\mathcal{T})|U_\lambda,¶\]", r"(\mathcal{B}/\mathcal{T})|U_\lambda¶\]", "Checked on a crop.")
add(131, "display L^{\u2297n} = N(L'^{\u2297n})", "no punctuation after the display",
    "comma after the display", "punctuation", None, "high",
    r"N_{X'/X}({\mathcal{L}'}^{\otimes n}),¶\]", r"N_{X'/X}({\mathcal{L}'}^{\otimes n})¶\]",
    "Checked on a crop. The subscript of N in this display shows only the lower part of the slash (X', X); a broken "
    "slash, not a different reading, so the TeX's X'/X stays.")
add(131, "'en effet, alors X\u2014X_f = g(X'\u2014X'_{f'})'", "X\u2014X_f", "X-X_f", "convention", 7, "high",
    r"$X-X_f=", r"$X\setmin X_f=", "Set difference.")
add(131, "'en effet, alors X\u2014X_f = g(X'\u2014X'_{f'})'", "g(X'\u2014X'_{f'})", "g(X'-X'_{f'})", "convention", 7, "high",
    r"=g(X'-X'_{f'})$", r"=g(X'\setmin X'_{f'})$", "Set difference.")
add(131, "Cor. (6.6.3)", "Sous les hypoth\u00e8ses de (6.6.1) -- reference upright", "reference italic (corollary environment)",
    "convention", 6, "high",
    r"Sous les hypoth\u00e8ses de (\hyperref[II.6.6.1-fr]{6.6.1})",
    r"Sous les hypoth\u00e8ses de \textup{(\hyperref[II.6.6.1-fr]{6.6.1})}", "")
add(131, "last line, page break 131/132 ('des points | x\u2208X')", "sentence continues on p. 132",
    r"blank line before \oldpage[II]{132}", "other", None, "high",
    r"Or, l'ensemble des points¶¶", r"Or, l'ensemble des points¶",
    BL + " Apply together with the p. 132 entry that removes the blank line after the marker.")

# ---------------- page 132
add(132, "line 1, page break 131/132", "x\u2208X au voisinage desquels (continues the sentence of p. 131)",
    r"blank line after \oldpage[II]{132}", "other", None, "high",
    r"\oldpage[II]{132}¶¶$x\in X$", r"\oldpage[II]{132}¶$x\in X$",
    BL + " Apply together with the p. 131 entry that removes the blank line before the marker.")
add(132, "Cor. (6.6.4)", "Supposons v\u00e9rifi\u00e9es les hypoth\u00e8ses de (6.6.1) -- reference upright",
    "reference italic (corollary environment)", "convention", 6, "high",
    r"(\hyperref[II.6.6.1-fr]{6.6.1}) et supposons", r"\textup{(\hyperref[II.6.6.1-fr]{6.6.1})} et supposons", "")
add(132, "Cor. (6.6.5), first (resp. ...)", "projectif (resp. quasi-projectif) sur K -- '(resp.' and ')' upright, 'quasi-projectif' italic",
    "all italic", "convention", 6, "high",
    r"projectif (resp. quasi-projectif) sur¶$K$", r"projectif \textup{(resp.} quasi-projectif\textup{)} sur¶$K$",
    "Checked on a crop.")
add(132, "Cor. (6.6.5), second (resp. ...)", "projectif (resp. quasi-projectif) sur K' -- '(resp.' and ')' upright, 'quasi-projectif' italic",
    "all italic", "convention", 6, "high",
    r"soit projectif (resp.¶quasi-projectif) sur $K'$", r"soit projectif \textup{(resp.}¶quasi-projectif\textup{)} sur $K'$",
    "Checked on a crop.")
add(132, "proof of (6.6.5)", "(I, 3.5.2, (ii)) with bold I", "(I, 3.5.2, (ii))", "convention", 2, "high",
    r"{I, 3.5.2, (ii)}", r"{\textbf{I}, 3.5.2, (ii)}", "")
add(132, "'Au chapitre V, nous montrerons que l'\u00e9nonc\u00e9 (6.6.5) ...' (line 15 from the bottom)", "Au chapitre V",
    "Au chapitre V (keeps the printed reading)", "misprint_in_print", None, "high", None, None,
    "Listed in the errata of EGA III (ega3-7-fr.tex): '(II, 6.6.5) Ligne 15 du bas de la p. 132, remplacer chap. V par chap. IV.' "
    "The TeX keeps the printed reading.", corrected="Au chapitre IV", nofix=True)
add(132, "Lemme (6.6.6)", "(1\u2a7di\u2a7dn) with upright parentheses", "($1\\leq i\\leq n$): parentheses italic (lemma environment)",
    "convention", 6, "medium", r"($1\leq i\leq n$)", r"\textup{($1\leq i\leq n$)}", "Checked on a crop.")
add(132, "Lemme (6.6.6)", "(cf. (6.4.10)) upright", "(cf. 6.4.10) italic", "convention", 6, "high",
    r"(cf. \hyperref[II.6.4.10-fr]{6.4.10})", r"\textup{(cf. \hyperref[II.6.4.10-fr]{6.4.10})}",
    "Apply before the next entry (the inner parentheses): that entry's 'old' survives this edit, but this 'old' does not survive that one.")
add(132, "Lemme (6.6.6)", "(cf. (6.4.10)) -- the reference has its own parentheses", "(cf. 6.4.10)",
    "punctuation", None, "high",
    r"\hyperref[II.6.4.10-fr]{6.4.10}", r"(\hyperref[II.6.4.10-fr]{6.4.10})",
    "Checked on a crop. Apply after the previous entry (convention 6 at the same place).")
add(132, "last line, page break 132/133 ('On | prendra')", "sentence continues on p. 133",
    r"blank line before \oldpage[II]{133}", "other", None, "high",
    r"de $X$. On¶¶", r"de $X$. On¶",
    BL + " Apply together with the p. 133 entry that removes the blank line after the marker.")

# ---------------- page 133
add(133, "line 1, page break 132/133", "prendra Z = Spec(C) (continues the sentence of p. 132)",
    r"blank line after \oldpage[II]{133}", "other", None, "high",
    r"\oldpage[II]{133}¶¶prendra", r"\oldpage[II]{133}¶prendra",
    BL + " Apply together with the p. 132 entry that removes the blank line before the marker.")
add(133, "end of the proof of (6.6.6)", "([13], t. I, p. 259)", r"(\cite[t.~I, p.~259]{I-13}), which prints ([13, t. I, p. 259])",
    "punctuation", None, "high",
    r"(\cite[t.~I, p.~259]{I-13})", r"(\cite{I-13}, t.~I, p.~259)",
    "Same treatment as the \\cite with optional argument on EGA I p. 148 and EGA II p. 113. The 'I' of 't. I' is not bold.")
add(133, "Cor. (6.6.7)", "Sous les hypoth\u00e8ses de (6.6.6) -- reference upright", "reference italic (corollary environment)",
    "convention", 6, "high",
    r"Sous les hypoth\u00e8ses de (\hyperref[II.6.6.6-fr]{6.6.6})",
    r"Sous les hypoth\u00e8ses de \textup{(\hyperref[II.6.6.6-fr]{6.6.6})}", "")
add(133, "display (6.6.8.1)", "N' : B = g_*(O_X') \u2192 h_*(O_Z) = C (no final period)", "period after C",
    "punctuation", None, "high",
    r"=\mathcal{C}.¶\tag{6.6.8.1}", r"=\mathcal{C}¶\tag{6.6.8.1}", "Checked on a crop.")
add(133, "Lemme (6.6.9)", "(notations de (6.6.8)) upright", "(notations de 6.6.8) italic", "convention", 6, "high",
    r"(notations de¶\hyperref[II.6.6.8-fr]{6.6.8})", r"\textup{(notations de¶\hyperref[II.6.6.8-fr]{6.6.8})}",
    "Apply before the next entry (the inner parentheses): that entry's 'old' survives this edit, but this 'old' does not survive that one.")
add(133, "Lemme (6.6.9)", "(notations de (6.6.8)) -- the reference has its own parentheses", "(notations de 6.6.8)",
    "punctuation", None, "high",
    r"\hyperref[II.6.6.8-fr]{6.6.8}", r"(\hyperref[II.6.6.8-fr]{6.6.8})",
    "Checked on a crop. Apply after the previous entry (convention 6 at the same place).")
add(133, "last paragraph, line 1 ('s' est aussi une section de ...')", "g_*(L') au-dessus de X",
    r"g_*({\mathcal{L}'}^{\otimes n}) -- the TeX silently corrects the print", "misprint_in_print", None, "high",
    r"$g_*({\mathcal{L}'}^{\otimes n})$ au-dessus de $X$", r"$g_*(\mathcal{L}')$ au-dessus de $X$",
    "Checked on a crop. s' is a section of L'^{\u2297n} over X' (line above), hence of g_*(L'^{\u2297n}) over X. Same slip "
    "as the next entry and as 'section de M' on p. 134 (the print writes L' and M for L'^{\u2297n} and M^{\u2297n}). Not in "
    "the errata of EGA II, of EGA III or in EGA IV list 3 (lists 1-2 are not among the sources).",
    corrected=r"$g_*({\mathcal{L}'}^{\otimes n})$")
add(133, "last line ('une section s = N'(s') de ...')", "N'(g_*(L')) au-dessus",
    r"N'(g_*({\mathcal{L}'}^{\otimes n})) -- the TeX silently corrects the print", "misprint_in_print", None, "high",
    r"$N'(g_*({\mathcal{L}'}^{\otimes n}))$", r"$N'(g_*(\mathcal{L}'))$",
    "Checked on a crop. See the previous entry. Independent of the blank-line entry that follows (non-overlapping strings).",
    corrected=r"$N'(g_*({\mathcal{L}'}^{\otimes n}))$")
add(133, "last line, page break 133/134 ('au-dessus | de X')", "sentence continues on p. 134",
    r"blank line before \oldpage[II]{134}", "other", None, "high",
    r"au-dessus¶¶", r"au-dessus¶",
    BL + " Apply together with the p. 134 entry that removes the blank line after the marker.")

# ---------------- page 134
add(134, "line 1, page break 133/134", "de X. Nous allons voir (continues the sentence of p. 133)",
    r"blank line after \oldpage[II]{134}", "other", None, "high",
    r"\oldpage[II]{134}¶¶de $X$.", r"\oldpage[II]{134}¶de $X$.",
    BL + " Apply together with the p. 133 entry that removes the blank line before the marker.")
add(134, "line 1 ('la section s consid\u00e9r\u00e9e comme section de ...')", "section de M au-dessus de Z",
    r"\mathcal{M}^{\otimes n} -- the TeX silently corrects the print", "misprint_in_print", None, "high",
    r"section de $\mathcal{M}^{\otimes n}$ au-dessus de $Z$", r"section de $\mathcal{M}$ au-dessus de $Z$",
    "Checked on a crop. With s a section of N'(g_*(L'^{\u2297n})) = h_*(M^{\u2297n}), t is a section of M^{\u2297n} (the "
    "M^{\u2297m} of the beginning of the proof, with m = n); same slip as the two p. 133 entries.",
    corrected=r"$\mathcal{M}^{\otimes n}$")
add(134, "display (6.6.9.2)", "V = X\u2014g(...)", "V=X-g(...)", "convention", 7, "high",
    r"V=X-g(", r"V=X\setmin g(", "Set difference.")
add(134, "display (6.6.9.2)", "g(X'\u2014X'_{s'})", "g(X'-X'_{s'})", "convention", 7, "high",
    r"g(X'-X'_{s'})", r"g(X'\setmin X'_{s'})", "Set difference.")
add(134, "'rempla\u00e7ant X' par X'' tel que ... soit injectif'", "inline: g'_*(O_X'') \u2192 g'_*(O_X'')\u2297R(X)",
    "displayed formula", "other", None, "high",
    r"\[¶g'_*(\mathcal{O}_{X''})\longrightarrow¶g'_*(\mathcal{O}_{X''})\otimes_{\mathcal{O}_X}\mathcal{R}(X)¶\]",
    r"$g'_*(\mathcal{O}_{X''})\to¶g'_*(\mathcal{O}_{X''})\otimes_{\mathcal{O}_X}\mathcal{R}(X)$",
    "Layout only (display vs inline); the formula itself matches.")
add(134, "Cor. (6.6.10)", "Supposons v\u00e9rifi\u00e9es les hypoth\u00e8ses de (6.6.9); -- reference upright",
    "reference italic (corollary environment)", "convention", 6, "high",
    r"(\hyperref[II.6.6.9-fr]{6.6.9})~;", r"\textup{(\hyperref[II.6.6.9-fr]{6.6.9})}~;", "")
add(134, "proof of (6.6.10)", "(0, 5.4.10) with bold 0", "(0, 5.4.10)", "convention", 2, "high",
    r"{0, 5.4.10}", r"{\textbf{0}, 5.4.10}", "")
add(134, "proof of (6.6.10)", "(par le m\u00eame raisonnement que pour (6.5.2.4))",
    "(par le m\u00eame raisonnement que pour 6.5.2.4)", "punctuation", None, "high",
    r"pour¶\hyperref[II.6.5.2.4-fr]{6.5.2.4})", r"pour¶(\hyperref[II.6.5.2.4-fr]{6.5.2.4}))", "Checked on a crop.")
add(134, "Prop. (6.6.11)", "un Y-morphisme fini et birationnel -- 'fini et birationnel' upright (emphasis in the italic statement)",
    "italic like the rest of the statement", "convention", 6, "high",
    r"$Y$-morphisme fini et birationnel", r"$Y$-morphisme \emph{fini et birationnel}",
    "Checked on a crop; \\emph inside the italic environment gives the printed upright face.")
add(134, "proof of (6.6.11), last paragraph", "(I, 5.2.1) with bold I", "(I, 5.2.1)", "convention", 2, "high",
    r"{I, 5.2.1}", r"{\textbf{I}, 5.2.1}", "")
add(134, "last line, page break 134/135 ('le sous-pr\u00e9sch\u00e9ma ferm\u00e9 | g^{-1}(X_i)')", "sentence continues on p. 135",
    r"blank line before \oldpage[II]{135}", "other", None, "high",
    r"le sous-pr\u00e9sch\u00e9ma ferm\u00e9¶¶", r"le sous-pr\u00e9sch\u00e9ma ferm\u00e9¶",
    BL + " Apply together with the p. 135 entry that removes the blank line after the marker.")
add(135, "line 1, page break 134/135", "g^{-1}(X_i) de X' (continues the sentence of p. 134)",
    r"blank line after \oldpage[II]{135}", "other", None, "high",
    r"\oldpage[II]{135}¶¶$g^{-1}(X_i)$", r"\oldpage[II]{135}¶$g^{-1}(X_i)$",
    "Second half of the p. 134 boundary fix; the 'old' lies in p. 135's segment (page_135.tex), outside pp. 130-134. "
    "Apply both or neither. The p. 135 checker may report the same edit.")

# the raw strings above keep \u escapes literally: decode them (only \u00XX/\u2XXX sequences are used for letters)
def dec(s):
    if s is None:
        return None
    return re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), s)


for d in F:
    for k in ("where", "scan", "tex", "note", "corrected"):
        if k in d and isinstance(d[k], str):
            d[k] = dec(d[k])
    if d["fix"]:
        d["fix"] = {"old": dec(d["fix"]["old"]), "new": dec(d["fix"]["new"])}

# ---------------- checks
pages = {}
for n in sorted({d["page"] for d in F}):
    pages[n] = (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8")  # universal newlines -> LF
bad = 0
for i, d in enumerate(F):
    fx = d["fix"]
    if not fx:
        continue
    c = pages[d["page"]].count(fx["old"])
    if i in REL_ONLY:
        print("release-only entry", i, "(snapshot count", c, ") -- checked by check_release.py")
    elif c != 1:
        bad += 1
        print("NOT UNIQUE", i, d["page"], c, repr(fx["old"][:60]))
    if "\\u" in fx["old"] or "\\u" in fx["new"]:
        # a remaining literal \u would be a decoding error (TeX here has no \u... macros)
        if re.search(r"\\u[0-9a-fA-F]{4}", fx["old"] + fx["new"]):
            bad += 1
            print("UNDECODED", i)
# sequential application per page, in list order, as apply_fixes.py does
seq = dict(pages)
for i, d in enumerate(F):
    fx = d["fix"]
    if not fx or i in REL_ONLY:
        continue
    t = seq[d["page"]]
    if t.count(fx["old"]) != 1:
        bad += 1
        print("SEQ FAIL", i, d["page"], t.count(fx["old"]), repr(fx["old"][:60]))
        continue
    seq[d["page"]] = t.replace(fx["old"], fx["new"])
print("findings:", len(F), "| problems:", bad)
json.dump(F, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
for n in sorted(seq):
    (RUN / "crops_130_134" / f"after_{n:03d}.txt").write_text(seq[n], encoding="utf-8", newline="\n")
