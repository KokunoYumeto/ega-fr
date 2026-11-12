# Builds findings_125_129.json, checks every "old" against its page_NNN.tex, and simulates the sequential
# application (apply_fixes.py logic) on in-memory copies of the diplomatic and current release files.
# Newlines inside old/new are written as the pilcrow sign and converted below.
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
OUT = RUN / "findings_125_129.json"
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20")
DIP = REL / r"diplomatic\packages\BASE\native\ega2\ega2-1-fr.tex"
CUR = REL / r"current\packages\BASE\native\ega2\ega2-1-fr.tex"
NL = "\u00b6"


def F(page, where, scan, tex, kind, old, new, note, conv=None, conf="high", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else dict(old=old.replace(NL, "\n"), new=new.replace(NL, "\n")))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


C2 = "Bold chapter number in the printed reference."
PAR = "Missing paragraph break (the print indents the line)."
L = []

# ---------------- page 125
L.append(F(125, "top of the page: 'morphisme de \U0001D4D5,' (second half of 'endo-|morphisme', p. 124/125)",
           "'Si v est un endo-' (end of p. 124) continues 'morphisme de \U0001D4D5, \u2026' at the top of p. 125: one word, one paragraph",
           r"\oldpage[II]{125} followed by a blank line before 'morphisme' (paragraph break inside the word)",
           "other", r"\oldpage[II]{125}¶¶morphisme", r"\oldpage[II]{125}¶morphisme",
           r"Second half of the p. 124 fix 'endo-\n\n' -> 'endo%\n' (findings_120_124.json, already applied: the release reads 'endo%'). "
           r"Together they give 'endo%\n\oldpage[II]{125}\nmorphisme', which typesets 'endomorphisme' (\oldpage ends with \ignorespaces); "
           r"with the blank line left in, the paragraph break inside the word remains."))
L.append(F(125, "commutative diagram after 'on a un diagramme commutatif', bottom right entry",
           "f*(\U0001D4D5)\u2297_{\U0001D4AA_X}\u211B(X) with no full stop", r"f^*(\mathcal{F})\otimes_{\mathcal{O}_X}\mathcal{R}(X).",
           "punctuation", r"\mathcal{R}(X).¶}", r"\mathcal{R}(X)¶}", "Checked on a crop: nothing follows the entry."))
L.append(F(125, "after the diagram: 'On en conclut aisément que det f*(v) est l'image canonique \u2026'",
           "new paragraph (first line indented)", r"text follows \] directly (same paragraph, no indent)",
           "other", r"\]¶On en conclut", r"\]¶¶On en conclut", PAR))
L.append(F(125, "(6.4.10): 'quasi-cohérent (I, 7.3.4)'", "(I, 7.3.4) with bold I", r"\hyperref[...]{I, 7.3.4}: plain I",
           "convention", "{I, 7.3.4}", r"{\textbf{I}, 7.3.4}", C2, conv=2))
L.append(F(125, "(6.5.1): 'que nous appellerons la norme de f (resp.'", "only 'norme' italic; 'de' roman",
           r"\emph{norme de $f$}", "italics", r"\emph{norme de¶$f$}", r"\emph{norme} de¶$f$", "Checked on a crop."))
L.append(F(125, "(6.5.1): '(resp. les fonctions symétriques élémentaires de f)'",
           "'fonctions symétriques élémentaires' italic, 'de' roman",
           r"\emph{fonctions symétriques élémentaires de $f$}", "italics",
           r"\emph{fonctions symétriques élémentaires de $f$}", r"\emph{fonctions symétriques élémentaires} de $f$",
           "Checked on a crop; same pattern as the p. 120 fix."))
L.append(F(125, "(6.5.1): 'Nous allons supposer vérifiée l'une des conditions suivantes'",
           "l'une: 'l'' roman, 'une' italic", r"\emph{l'une}", "italics", r"\emph{l'une}", r"l'\emph{une}",
           "Checked on a crop."))

# ---------------- page 126
L.append(F(126, "'les composantes irréductibles de X (I, 5.2.1)'", "(I, 5.2.1) with bold I", "plain I",
           "convention", "{I, 5.2.1}", r"{\textbf{I}, 5.2.1}", C2, conv=2))
L.append(F(126, "'localement libre de rang constant k_\u03b1 (I, 7.3.6)'", "(I, 7.3.6) with bold I", "plain I",
           "convention", "{I, 7.3.6}", r"{\textbf{I}, 7.3.6}", C2, conv=2))
L.append(F(126, "'Il est clair que sous les hypothèses (I) ou (II), on définit ainsi un homomorphisme de faisceaux \u2026'",
           "on définit ainsi un", "on a défini ainsi un", "word", "on a défini ainsi un", "on définit ainsi un",
           "Present tense in the print (checked on a crop)."))
L.append(F(126, "(6.5.1.3): N_{\u212C/\U0001D49C}(s.1_\u212C)=s^n", "s.1_\u212C with a baseline period",
           r"s\cdot1_{\mathcal{B}}", "symbol", r"s\cdot1_{\mathcal{B}}", r"s.1_{\mathcal{B}}",
           "The dot sits on the baseline (crop); same treatment as T.I (pp. 120-121) and s.u (p. 123)."))
L.append(F(126, "after (II bis): '(On notera encore que cette condition est vérifiée lorsque X est normal.)'",
           "new paragraph (indented)", r"\end{enumerate} directly followed by the text (LaTeX continues without indent)",
           "other", r"\end{enumerate}¶(On notera encore", r"\end{enumerate}¶¶(On notera encore", PAR))
L.append(F(126, "(6.5.2): 'et soit \u2112' un \u212C-Module inversible.'", "'Module inversible' italic",
           r"$\mathcal{B}$-Module \emph{inversible}", "italics",
           r"$\mathcal{B}$-Module \emph{inversible}", r"$\mathcal{B}$-\emph{Module inversible}", "Checked on a crop."))
L.append(F(126, "(6.5.2): 'un \U0001D49C-Module inversible \u2112 de la façon suivante'", "'Module inversible' italic",
           r"$\mathcal{A}$-Module \emph{inversible}", "italics",
           r"$\mathcal{A}$-Module \emph{inversible}", r"$\mathcal{A}$-\emph{Module inversible}", "Checked on a crop."))
L.append(F(126, "last line: '\u2026 soit l'ensemble des' (sentence continues on p. 127)",
           "one sentence across the page break ('l'ensemble des | éléments inversibles de \u0393(U, \U0001D49C)')",
           r"blank line before \oldpage[II]{127} (and after it): paragraph break in mid-sentence",
           "other", "l'ensemble des¶¶", "l'ensemble des¶",
           r"GLOBAL_ISSUES item 20. Apply together with the p. 127 fix of the blank line after \oldpage[II]{127}."))

# ---------------- page 127
L.append(F(127, r"top of the page: blank line after \oldpage[II]{127}",
           "'éléments inversibles de \u0393(U, \U0001D49C) \u2026' continues the sentence of p. 126",
           r"\oldpage[II]{127} followed by a blank line", "other",
           r"\oldpage[II]{127}¶¶éléments", r"\oldpage[II]{127}¶éléments",
           "Apply together with the p. 126 fix 'l'ensemble des\\n\\n' -> 'l'ensemble des\\n'."))
L.append(F(127, "(6.5.2): 'U_\u03bb est un ouvert de X et \u03b7_\u03bb est un isomorphisme'", "no comma after X",
           "ouvert de $X$, et", "punctuation", r"ouvert de $X$, et $\eta_\lambda$", r"ouvert de $X$ et $\eta_\lambda$",
           "Checked on a crop."))
L.append(F(127, "(6.5.2): '\u03b7_\u03bb est un isomorphisme : \u2112'|U_\u03bb \u2972 \u212C|U_\u03bb'",
           "colon after 'isomorphisme'", "no colon", "punctuation",
           r"est un isomorphisme¶$\mathcal{L}'", r"est un isomorphisme~:¶$\mathcal{L}'", "Checked on a crop."))
L.append(F(127, "(6.5.2): '\u2112'|U_\u03bb \u2972 \u212C|U_\u03bb'", "isomorphism arrow (tilde above the arrow)",
           r"\simeq", "convention", r"\simeq\mathcal{B}|U_\lambda$ de", r"\xrightarrow{\sim}\mathcal{B}|U_\lambda$ de",
           "Isomorphism arrow.", conv=4))
L.append(F(127, "(6.5.2): 'de (B|U_\u03bb)-Modules'", "(B|U_\u03bb) with a roman capital B",
           r"$(\mathcal{B}|U_\lambda)$-Modules", "misprint_in_print",
           r"$(\mathcal{B}|U_\lambda)$-Modules", r"$(B|U_\lambda)$-Modules",
           "The print has a roman B (crop; script \u212C everywhere else, e.g. '\u212C|U_\u03bb' on the line above) for the "
           "\U0001D49C-Algèbre \u212C; the TeX silently corrects it. The fix restores the printed reading.",
           corrected=r"$(\mathcal{B}|U_\lambda)$-Modules"))
L.append(F(127, "(6.5.2): '1-cocycle du recouvrement \U0001D518=(U_\u03bb) à valeurs dans \u212C* (0, 5.4.7). Le fait'",
           "(0, 5.4.7) with bold 0", "plain 0", "convention", "{0, 5.4.7}). Le fait", r"{\textbf{0}, 5.4.7}). Le fait",
           C2, conv=2))
L.append(F(127, "(6.5.2): 'un \U0001D49C-Module inversible \u2112 (0, 5.4.7) que nous désignerons'",
           "(0, 5.4.7) with bold 0", "plain 0", "convention", "{0, 5.4.7}) que nous", r"{\textbf{0}, 5.4.7}) que nous",
           C2, conv=2))
L.append(F(127, "(6.5.2): 'et appellerons la norme du \u212C-Module inversible \u2112''", "only 'norme' italic",
           r"\emph{la norme du $\mathcal{B}$-Module inversible $\mathcal{L}'$}", "italics",
           r"\emph{la norme du¶$\mathcal{B}$-Module inversible $\mathcal{L}'$}",
           r"la \emph{norme} du¶$\mathcal{B}$-Module inversible $\mathcal{L}'$", "Checked on a crop."))
L.append(F(127, "(6.5.2.3)", "N(\u2112'^{-1})=(N(\u2112'))^{-1}: no parentheses around \u2112' on the left",
           r"N((\mathcal{L}')^{-1})", "formula", r"N((\mathcal{L}')^{-1})", r"N(\mathcal{L}'^{-1})",
           "Checked on a crop."))
L.append(F(127, "(6.5.3): 'est un foncteur covariant dans la catégorie'", "only 'foncteur' italic",
           r"\emph{foncteur covariant}", "italics", r"\emph{foncteur covariant}", r"\emph{foncteur} covariant",
           "Checked on a crop."))
L.append(F(127, "(6.5.3): '\u03b7^{(1)}_\u03bb : \u2112'_1|U_\u03bb \u2972 \u212C|U_\u03bb'",
           "isomorphism arrow (tilde above the arrow)", r"\simeq", "convention",
           r"\mathcal{L}'_1|U_\lambda\simeq", r"\mathcal{L}'_1|U_\lambda\xrightarrow{\sim}", "Isomorphism arrow (crop).", conv=4))
L.append(F(127, "(6.5.3): '\u03b7^{(2)}_\u03bb : \u2112'_2|U_\u03bb \u2972 \u212C|U_\u03bb'",
           "isomorphism arrow (tilde above the arrow)", r"\simeq", "convention",
           r"\mathcal{L}'_2|U_\lambda\simeq", r"\mathcal{L}'_2|U_\lambda\xrightarrow{\sim}", "Isomorphism arrow (crop).", conv=4))
L.append(F(127, "(6.5.3): 'une section de \u212C au-dessus de U_\u03bb (0, 5.1.1)'", "(0, 5.1.1) with bold 0", "plain 0",
           "convention", "{0, 5.1.1}", r"{\textbf{0}, 5.1.1}", C2, conv=2))

# ---------------- page 128
L.append(F(128, "(6.5.3): 'les homomorphismes \u212C\u2192\u2112' s'identifient alors (0, 5.1.1)'", "(0, 5.1.1) with bold 0",
           "plain 0", "convention", "{0, 5.1.1}", r"{\textbf{0}, 5.1.1}", C2, conv=2))
L.append(F(128, "(6.5.3): 'Il résulte encore de (6.5.1.1) que si f'_1\u2208\u0393(X, \u2112'_1), \u2026'",
           "new paragraph (indented)", r"follows \] directly (same paragraph)", "other",
           r"\]¶Il résulte encore", r"\]¶¶Il résulte encore", PAR))
L.append(F(128, "(6.5.3): 'Pour tout \U0001D49C-Module inversible \u2112 et toute section f\u2208\u0393(X, \u2112), \u2026'",
           "new paragraph (indented)", r"follows \] directly (same paragraph)", "other",
           r"\]¶Pour tout $\mathcal{A}$-Module", r"\]¶¶Pour tout $\mathcal{A}$-Module", PAR))
L.append(F(128, "(6.5.4): 'deux espaces annelés, f : X'\u2192X un morphisme, \u212C une \U0001D49C-Algèbre'",
           "f : X'\u2192X is set as a centred display on a line of its own; 'un morphisme, \u2026' continues flush left",
           r"inline $f:X'\to X$", "other", r"$f:X'\to X$ un morphisme,", r"\[¶f:X'\to X¶\]¶un morphisme,",
           "Display in the print (cf. GLOBAL_ISSUES item 21, the converse case)."))
L.append(F(128, "(6.5.4): 'Sous ces conditions, \u212C' vérifie respectivement \u2026' after item 2\u00b0",
           "new paragraph (indented)", r"\end{enumerate} directly followed by the text (no indent)", "other",
           r"\end{enumerate}¶Sous ces conditions", r"\end{enumerate}¶¶Sous ces conditions", PAR))

# ---------------- page 129 (no marker changes)
L.append(F(129, "(6.5.5): 'qui est un \U0001D49C-Module de type fini équivaut alors'", "'Module de type fini' italic",
           r"$\mathcal{A}$-Module \emph{de type fini}", "italics",
           r"$\mathcal{A}$-Module \emph{de type fini}", r"$\mathcal{A}$-\emph{Module de type fini}", "Checked on a crop."))
L.append(F(129, "(6.5.5): 'En particulier, pour \u2112'_1=\U0001D4AA_{X'}, on obtient ainsi une application canonique'",
           "new paragraph (indented)", r"follows \] directly (same paragraph)", "other",
           r"\]¶En particulier, pour", r"\]¶¶En particulier, pour", PAR))
L.append(F(129, "(6.5.5): 'Nous laisserons au lecteur la plupart de ces traductions'",
           "new paragraph (indented)", r"follows \] directly (same paragraph)", "other",
           r"\]¶Nous laisserons", r"\]¶¶Nous laisserons", PAR))
L.append(F(129, "Proposition (6.5.6): '\u2026 vérifient (II bis) (ce qui sera le cas en particulier \u2026'",
           "'(II bis)' entirely upright inside the italic statement",
           r"(II \emph{bis}): '(II' comes out italic, 'bis' upright", "convention",
           r"vérifient (II \emph{bis})¶(ce qui", r"vérifient \textup{(II bis)}¶(ce qui",
           "Roman words inside an italic statement (crop).", conv=6))
L.append(F(129, "Corollaire (6.5.7): 'soit que g_*(\U0001D4AA_X) est un \U0001D4AA_X-Module localement libre'",
           "g_*(\U0001D4AA_X): no prime on X", r"$g_*(\mathcal{O}_{X'})$", "misprint_in_print",
           r"6.5.7-fr}¶Soit $g:X'\to X$ un morphisme fini, et supposons, soit que¶$g_*(\mathcal{O}_{X'})$",
           r"6.5.7-fr}¶Soit $g:X'\to X$ un morphisme fini, et supposons, soit que¶$g_*(\mathcal{O}_X)$",
           "The prime is missing in the print (crop at 4x; the same hypothesis in Proposition (6.5.6) and the rest of "
           "(6.5.7) have \U0001D4AA_{X'}); the TeX silently corrects it. The fix restores the printed reading; the long "
           "'old' is needed because the line is identical in (6.5.6).",
           corrected=r"$g_*(\mathcal{O}_{X'})$"))
L.append(F(129, "Corollaire (6.5.7): '\u2026 vérifient (II bis) et que g_*(\U0001D4AA_{X'})\u2192 \u2026'",
           "'(II bis)' entirely upright inside the italic statement",
           r"(II \emph{bis}): '(II' comes out italic, 'bis' upright", "convention",
           r"vérifient (II \emph{bis})¶et que", r"vérifient \textup{(II bis)}¶et que",
           "Roman words inside an italic statement (crop).", conv=6))

# ---------------- page break 128/129: marker (two steps, in this order)
L.append(F(129, r"page break 128/129: \oldpage[II]{129} stands before 'Cela étant'",
           "p. 128 ends '(on le voit aussitôt en se ramenant au'; p. 129 begins 'cas affine comme dans (6.4.9)), d'où notre "
           "assertion en vertu de l'hypothèse (II) et de (6.5.1).', then the new paragraph 'Cela étant, \u2026'",
           "'cas affine \u2026 de (6.5.1).' lies in p. 128's segment; the marker follows it", "marker",
           r"\oldpage[II]{129}¶¶Cela étant", "Cela étant",
           "Step 1 of 2 (keep this order, step 2 immediately after): removes the misplaced marker. The blank line "
           "before it stays and keeps the printed paragraph break before 'Cela étant'."))
L.append(F(128, "page break 128/129, last line of p. 128: '(on le voit aussitôt en se ramenant au'",
           "p. 129 begins with 'cas affine comme dans (6.4.9))'", r"\oldpage[II]{129} after '\u2026 de (6.5.1).'",
           "marker", "en se ramenant au cas affine", r"en se ramenant au¶\oldpage[II]{129}¶cas affine",
           "Step 2 of 2: puts the p. 129 marker where the printed page begins. Must run after step 1 (otherwise the "
           "file holds two p. 129 markers and the page-129 lookup breaks)."))

# ---------------- page break 129/130: paragraph, misprint, marker (four steps, in this order)
L.append(F(129, r"end of p. 129's segment: blank line before \oldpage[II]{130} (inside Corollaire (6.5.7))",
           "p. 129 ends '\u2026 au-dessus de X qui'; p. 130 continues 'lui correspond (6.5.5.1). Alors on a \u2026' "
           "in the same paragraph", r"'\u2026 lui correspond (6.5.5.3).', blank line, \oldpage[II]{130}, blank line, 'Alors on a'",
           "other", "{6.5.5.3}).¶¶", "{6.5.5.3}).¶",
           "Spurious paragraph break inside the statement (GLOBAL_ISSUES item 20). Step 1 of 4 for the 129/130 "
           "boundary (keep the order: this, the (6.5.5.1) misprint, the p. 130 marker removal, the marker insertion)."))
L.append(F(129, "Corollaire (6.5.7), printed at the top of p. 130 but still in p. 129's segment: "
           "'la section de \u2112=N_{X'/X}(\u2112') au-dessus de X qui lui correspond (6.5.5.1)'",
           "(6.5.5.1)", r"(\hyperref[II.6.5.5.3-fr]{6.5.5.3})", "misprint_in_print",
           r"\hyperref[II.6.5.5.3-fr]{6.5.5.3}", r"\hyperref[II.6.5.5.1-fr]{6.5.5.1}",
           "The reading (6.5.5.1) is certain (crop of p. 130). The section f=N_{X'/X}(f') corresponding to f' is given by "
           "the map (6.5.5.3), N_{X'/X}: \u0393(X',\u2112')\u2192\u0393(X,N_{X'/X}(\u2112')); (6.5.5.1) only defines "
           "N_{X'/X}(\u2112'), so the print's reference is taken as a misprint, silently corrected in the TeX. The fix "
           "restores the printed reading. Step 2 of 4 (must run after step 1, whose 'old' contains 6.5.5.3).",
           conf="medium", corrected=r"(\hyperref[II.6.5.5.3-fr]{6.5.5.3})"))
L.append(F(130, r"page break 129/130: \oldpage[II]{130} stands before 'Alors on a' (outside pp. 125-129: page_130.tex)",
           "p. 130 begins 'lui correspond (6.5.5.1). Alors on a g(X'\u2014X'_{f'})=X\u2014X_f \u2026' (one paragraph)",
           "'lui correspond (6.5.5.3).' lies in p. 129's segment; the marker and a blank line follow it", "marker",
           r"\oldpage[II]{130}¶¶Alors on a", "Alors on a",
           "Step 3 of 4: removes the misplaced marker and the blank line after it (with step 1 the paragraph break goes). "
           "The pp. 130-134 checker may report the same boundary; keep one version."))
L.append(F(129, "Corollaire (6.5.7), last line of p. 129: '\u2026 au-dessus de X qui'",
           "p. 130 begins with 'lui correspond (6.5.5.1).'", r"\oldpage[II]{130} after '\u2026 lui correspond (6.5.5.3).'",
           "marker", r"$X$ qui lui correspond", r"$X$ qui¶\oldpage[II]{130}¶lui correspond",
           "Step 4 of 4: puts the p. 130 marker where the printed page begins. Must run after step 3."))

# ---------------- checks
pages = {}
for p in sorted({x["page"] for x in L}):
    pages[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
bad = 0
for x in L:
    if x["fix"]:
        n = pages[x["page"]].count(x["fix"]["old"])
        if n != 1:
            bad += 1
            print("NOT UNIQUE", x["page"], n, repr(x["fix"]["old"]))
print("uniqueness problems:", bad)

marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")


def simulate(t, items, skip_misprints):
    ok = fail = 0
    for x in items:
        if not x["fix"] or (skip_misprints and x["kind"] == "misprint_in_print"):
            continue
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        hit = [i for i, (n, s) in enumerate(cuts) if n == x["page"]]
        if not hit:
            fail += 1; print("  page not found", x["page"], repr(x["fix"]["old"][:40])); continue
        i = hit[0]
        s, e = cuts[i][1], cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
        seg = t[s:e]
        if seg.count(x["fix"]["old"]) != 1:
            fail += 1; print("  fails", x["page"], seg.count(x["fix"]["old"]), repr(x["fix"]["old"][:50])); continue
        t = t[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + t[e:]
        ok += 1
    return t, ok, fail


for name, path, skip in (("diplomatic", DIP, False), ("current", CUR, True)):
    t0 = path.read_text(encoding="utf-8")
    t1, ok, fail = simulate(t0, L, skip)
    print(name, "applied", ok, "failed", fail)
    if name == "diplomatic":
        for a, b in (("Si $v$ est un", "morphisme de $\\mathcal{F}$,"), ("soit\nl'ensemble", "inversibles de"),
                     ("(on le voit", "Cela étant,"), ("au-dessus de $X$ qui", "Alors on a")):
            i = t1.index(a); j = t1.index(b, i)
            print("----\n" + t1[i:j + len(b)])
        print("----\nmarkers 124-131:", [m.group(1) for m in marker.finditer(t1) if 124 <= int(m.group(1)) <= 131])

OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
cnt = {}
for x in L:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print(json.dumps(cnt))
print("written", OUT, len(L))
