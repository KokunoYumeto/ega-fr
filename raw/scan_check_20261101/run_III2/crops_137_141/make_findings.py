"""Build findings_137_141.json for run_III2 (pages 137-141) and check every fix.

In the strings below, the pilcrow character stands for a line break (LF)."""
import json
import pathlib
import sys

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III2")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\BASE\native\ega3\ega3-6-fr.tex")
OUT = RUN / "findings_137_141.json"
P = "\u00b6"


def L(s):
    return None if s is None else s.replace(P, "\n")


pages = {n: (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8") for n in range(137, 142)}
src = SRC.read_text(encoding="utf-8")
lead = src[:src.index(r"\oldpage[III]{137}")]


def span(page, start, end):
    """Exact substring of the page file from anchor START to the end of anchor END (both unique)."""
    t = pages[page]
    start, end = L(start), L(end)
    i = t.index(start)
    j = t.index(end, i) + len(end)
    return t[i:j]


F = []


def add(page, where, scan, tex, kind, old, new, conf="high", conv=None, note="", corrected=None, outside=False):
    f = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf,
         "fix": None if old is None else {"old": L(old), "new": L(new)}}
    if corrected is not None:
        f["corrected"] = corrected
    f["note"] = note
    f["_outside"] = outside
    F.append(f)


ITAL = "Italic in the print; upright in the TeX."
ARROW = "Wavy arrow in the print (\\leadsto), not convention 3; GLOBAL_ISSUES item 33."
BOLD0 = "Bold chapter number in the reference."
INLINE = "Layout: the print sets this formula in the running text; the TeX displays it. The formula itself matches."

# ---------------------------------------------------------------- page 137: text before the file's first marker
add(137, "chapter heading, ega3-6-fr.tex l. 1 (before the file's first marker)",
    "CHAPITRE III (suite), with '(suite)' in italics (parentheses included)",
    r"\chapter*{CHAPITRE III (suite)\\[1.2ex] ...}: '(suite)' upright", "italics",
    "CHAPITRE III (suite)", r"CHAPITRE III \emph{(suite)}",
    note="OUTSIDE page_137.tex: 'old' is in ega3-6-fr.tex l. 1, before \\oldpage[III]{137}. Checked on an enlarged crop.",
    outside=True)
add(137, "heading 6.1, ega3-6-fr.tex l. 7 (before the file's first marker)",
    "6.1. Introduction. (with a final full stop)", r"\subsection{Introduction}", "punctuation",
    r"\subsection{Introduction}", r"\subsection{Introduction.}",
    note="OUTSIDE page_137.tex (ega3-6-fr.tex l. 7). Same pattern as GLOBAL_ISSUES item 43 (ega3-1).",
    outside=True)
add(137, "position of \\oldpage[III]{137} (part 1 of 2: remove it after the headings)",
    "printed p. 137 begins with the chapter heading 'CHAPITRE III (suite)', then '§ 6. FONCTEURS « TOR » LOCAUX ET "
    "GLOBAUX; FORMULE DE KÜNNETH' and '6.1. Introduction.'",
    "the marker stands after \\chapter*, \\section and \\subsection (ega3-6-fr.tex l. 10)", "marker",
    r"\oldpage[III]{137}" + P + P, "", conf="medium",
    note="Apply together with part 2 (insert the marker before \\section). The strict place would be before "
         "\\chapter*, but \\chapter* begins a new page (the driver also has \\clearpage before \\input{ega3/ega3-6-fr.tex}), "
         "so a \\marginpar placed before it would leave the marker on a page of its own; after the \\chapter* heading it "
         "lands on the chapter's first page. Alternative: the ega3-1 pattern (\\clearpage, marker, hand-made heading).")
add(137, "position of \\oldpage[III]{137} (part 2 of 2: insert it before the § 6 heading)",
    "see part 1", "see part 1", "marker",
    r"\section{Foncteurs « Tor » locaux et globaux; formule de Künneth}",
    r"\oldpage[III]{137}" + P + P + r"\section{Foncteurs « Tor » locaux et globaux; formule de Künneth}",
    conf="medium",
    note="OUTSIDE page_137.tex (ega3-6-fr.tex l. 4). Apply together with part 1.", outside=True)

# ---------------------------------------------------------------- page 137 body
add(137, "(6.1.1): 'on pose X'=X_(Y')=X×_Y Y', F'=F⊗_Y O_Y', f'=f_(Y') : X'→Y', et l'on'",
    "in the running text", "displayed", "other",
    span(137, "on pose" + P + r"\[", r"\]" + P + "et l'on"),
    "on pose" + P + r"$X'=X_{(Y')}=X\times_Y Y'$, $\mathscr F'=\mathscr F\otimes_Y\mathscr O_{Y'}$, "
    r"$f'=f_{(Y')}:X'\to Y'$," + P + "et l'on", note=INLINE)
add(137, "(6.1.1): 'pour un O_Y-Module quasi-cohérent variable G'", "'Module' in italics (enlarged crop)",
    "upright", "italics", r"$\mathscr O_Y$-Module quasi-cohérent variable",
    r"$\mathscr O_Y$-\emph{Module} quasi-cohérent variable", note=ITAL)
add(137, "(6.1.1): 'autrement dit le foncteur G⇝R^n f_*(F⊗_{O_Y}G).'",
    "wavy arrow; formula in the running text", r"displayed, with \longmapsto", "symbol",
    span(137, "foncteur" + P + r"\[", r"\]" + P + "Si"),
    "foncteur" + P + r"$\mathscr G\leadsto\mathrm R^n f_*(\mathscr F\otimes_{\mathscr O_Y}\mathscr G)$." + P + "Si",
    note=ARROW + " The fix also sets the formula inline, as printed.")
add(137, "(6.1.1): 'Si F est plat sur Y'", "'plat' italic", "upright", "italics",
    "est plat sur", r"est \emph{plat} sur", note=ITAL)
add(137, "(6.1.1): 'le foncteur G⇝F⊗_{O_Y}G est exact'", "wavy arrow", r"\mapsto", "symbol",
    r"$\mathscr G\mapsto\mathscr F\otimes", r"$\mathscr G\leadsto\mathscr F\otimes", note=ARROW)
add(137, "(6.1.1): 'est exact (0_I, 6.7.4)'", "'exact' italic", "upright", "italics",
    r"\mathscr G$ est exact", r"\mathscr G$ est \emph{exact}", note=ITAL)
add(137, "(6.1.1): '(0_I, 6.7.4)'", "bold 0", "plain 0", "convention",
    r"(0\textsubscript{I}, 6.7.4)", r"(\textbf{0}\textsubscript{I}, 6.7.4)", conv=2, note=BOLD0)
add(137, "(6.1.1): 'le foncteur composé G⇝R•f_*(F⊗_{O_Y}G)'", "wavy arrow", r"\mapsto", "symbol",
    "composé" + P + r"$\mathscr G\mapsto", "composé" + P + r"$\mathscr G\leadsto", note=ARROW)
add(137, "(6.1.1): 'le foncteur composé G⇝R•f_*(F⊗_{O_Y}G) est encore un foncteur cohomologique'",
    "R with a bullet superscript: R•f_* (enlarged crop)", "R^n f_*", "formula",
    r"\mathrm R^n f_*(\mathscr F\otimes_{\mathscr O_Y}\mathscr G)$" + P + "est encore",
    r"\mathrm R^\bullet f_*(\mathscr F\otimes_{\mathscr O_Y}\mathscr G)$" + P + "est encore",
    note="The cohomological functor is the whole family R•; the other occurrences on the page have R^n, as printed.")
add(137, "(6.1.1): 'est encore un foncteur cohomologique'", "'cohomologique' italic", "upright", "italics",
    "foncteur cohomologique. Mais", r"foncteur \emph{cohomologique}. Mais", note=ITAL)
add(137, "(6.1.1): 'substituer à G⇝R^n f_*(F⊗_{O_Y}G)'", "wavy arrow", r"\mapsto", "symbol",
    "substituer à" + P + r"$\mathscr G\mapsto", "substituer à" + P + r"$\mathscr G\leadsto", note=ARROW)
add(137, "(6.1.1): 'qui cette fois sont toujours des foncteurs cohomologiques'", "'toujours' italic", "upright",
    "italics", "sont toujours des", r"sont \emph{toujours} des", note=ITAL)
add(137, "(6.1.1): 'une « formule de Künneth » exprimant R^n(f_1×f_2)_*(F_1⊗_Y F_2) à l'aide'",
    "in the running text", "displayed", "other",
    span(137, "exprimant" + P + r"\[", r"\]" + P + "à l'aide"),
    "exprimant" + P + r"$\mathrm R^n(f_1\times f_2)_*(\mathscr F_1\otimes_Y\mathscr F_2)$" + P + "à l'aide",
    note=INLINE)
add(137, "(6.1.2): 'les foncteurs cohomologiques G⇝T•(G)'", "wavy arrow", r"\mapsto", "symbol",
    r"$\mathscr G\mapsto\mathscr T_\bullet", r"$\mathscr G\leadsto\mathscr T_\bullet", note=ARROW)
add(137, "(6.1.2): 'sont localement (sur Y) du type'", "'localement' italic", "upright", "italics",
    "sont" + P + "localement (sur", "sont" + P + r"\emph{localement} (sur", note=ITAL)
add(137, "(6.1.2): 'du type G⇝H•(L•⊗_Y G), où'", "wavy arrow; formula in the running text",
    r"displayed, with \longmapsto", "symbol",
    span(137, "du type" + P + r"\[", r"\]" + P + "où"),
    "du type" + P + r"$\mathscr G\leadsto\mathscr H_\bullet(\mathscr L_\bullet\otimes_Y\mathscr G)$," + P + "où",
    note=ARROW + " The fix also sets the formula inline, as printed.")
add(137, "(6.1.2): 'un complexe de O_Y-Modules localement libres'", "'Modules' with a capital M",
    "'modules'", "word", r"$\mathscr O_Y$-modules", r"$\mathscr O_Y$-Modules",
    note="The print writes O_Y-Modules (sheaves of modules), as everywhere on the page.")
add(137, "(6.1.2): 'localement libres'", "'localement libres' italic", "upright", "italics",
    "localement" + P + "libres", r"\emph{localement" + P + "libres}", note=ITAL)
add(137, "end of the page: 'et à étudier de' / p. 138 'façon générale'",
    "the sentence runs on to p. 138; no paragraph break",
    "blank lines before and after \\oldpage[III]{138} make a paragraph break", "other",
    "et à étudier de" + P + P, "et à étudier de" + P,
    note="Spurious paragraph break (GLOBAL_ISSUES item 20). Apply together with the p. 138 finding that removes the "
         "blank line after the marker.")

# ---------------------------------------------------------------- page 138
add(138, "top of the page: 'façon générale' (continuation of (6.1.2))", "first line not indented, same paragraph",
    "blank line after \\oldpage[III]{138}", "other",
    r"\oldpage[III]{138}" + P + P + "façon", r"\oldpage[III]{138}" + P + "façon",
    note="Spurious paragraph break; apply together with the p. 137 finding (blank line before the marker).")
add(138, "(6.1.2): 'les foncteurs de la forme précédente G⇝H•(L•⊗_Y G)'", "wavy arrow", r"\mapsto", "symbol",
    r"$\mathscr G\mapsto\mathscr H_\bullet", r"$\mathscr G\leadsto\mathscr H_\bullet", note=ARROW)
add(138, "(6.1.2): 'les propriétés d'exactitude'", "'exactitude' italic", "upright", "italics",
    "propriétés d'exactitude", r"propriétés d'\emph{exactitude}", note=ITAL)
add(138, "(6.1.2): 'que le foncteur G⇝R^n f_*(F⊗_{O_Y}G) est exact'", "wavy arrow", r"\mapsto", "symbol",
    r"$\mathscr G\mapsto\mathrm R^n", r"$\mathscr G\leadsto\mathrm R^n", note=ARROW)
add(138, "(6.1.2): 'est exact (ce qu'on exprimera'", "'exact' italic", "upright", "italics",
    "est exact (ce qu'on", r"est \emph{exact} (ce qu'on", note=ITAL)
add(138, "(6.1.2): 'F est cohomologiquement plat sur Y'", "'cohomologiquement plat' italic", "upright", "italics",
    "cohomologiquement plat", r"\emph{cohomologiquement plat}", note=ITAL)
add(138, "(6.1.2): 'une propriété de semi-continuité'", "'semi-continuité' italic", "upright", "italics",
    "de semi-continuité de", r"de \emph{semi-continuité} de", note=ITAL)
add(138, "(6.1.2): 'de la fonction y⇝dim_{k(y)}(T_i(k(y)))'", "wavy arrow", r"\mapsto", "symbol",
    r"$y\mapsto", r"$y\leadsto", note=ARROW)
add(138, "(6.1.2): 'dim_{k(y)}' (subscript)", "bold k in the subscript k(y) (enlarged crop)", "plain k", "convention",
    "_{k(y)}", r"_{\boldsymbol{k}(y)}", conv=1, note="Residue field k(y) printed bold.")
add(138, "(6.1.2): 'T_i(k(y))'", "bold italic k", "plain k", "convention",
    "(T_i(k(y)))", r"(T_i(\boldsymbol{k}(y)))", conv=1, note="Residue field k(y) printed bold italic.")
add(138, "(6.1.2): 'lorsque T_i est exact, cette propriété'", "'exact' italic", "upright", "italics",
    "est exact, cette", r"est \emph{exact}, cette", note=ITAL)
add(138, "(6.1.2): 'une propriété de continuité'", "'continuité' italic", "upright", "italics",
    "de continuité, la", r"de \emph{continuité}, la", note=ITAL)
add(138, "(6.1.3): 'fait usage de l'hypercohomologie'", "'hypercohomologie' italic", "upright", "italics",
    "l'hypercohomologie, en prenant", r"l'\emph{hypercohomologie}, en prenant", note=ITAL)
add(138, "(6.1.3): 'comme arguments des complexes de faisceaux'", "'complexes' italic", "upright", "italics",
    "arguments des complexes de", r"arguments des \emph{complexes} de", note=ITAL)
add(138, "(6.1.3): 'bien que la nécessité de ce point de vue n'apparaîtra que dans des chapitres ultérieurs'",
    "n'apparaîtra (future indicative; enlarged crop)", "n'apparaisse (subjunctive)", "word",
    "n'apparaisse que", "n'apparaîtra que",
    note="The TeX normalizes the mood after 'bien que'; the print has the indicative future, an attested usage "
         "(not a typographical misprint).")
add(138, "(6.1.4): 'est un homotopisme s'il existe'", "'homotopisme' italic", "upright", "italics",
    "est un homotopisme s'il", r"est un \emph{homotopisme} s'il", note=ITAL)
CBOLD = "Category letter printed bold italic (as GLOBAL_ISSUES item 33 for ega3-1)."
add(138, "(6.1.4): 'dans une catégorie abélienne C, nous dirons'", "C bold italic", "plain $C$", "font",
    "abélienne $C$, nous", r"abélienne $\boldsymbol{C}$, nous", note=CBOLD)
add(138, "(6.1.4): 'soient tous deux homotopes à l'identité'", "'homotopes à l'identité' italic", "upright",
    "italics", "homotopes à l'identité", r"\emph{homotopes à l'identité}", note=ITAL)
add(138, "(6.1.4): 'K• et K'• sont homotopes)'", "'homotopes' italic", "upright", "italics",
    "sont homotopes)", r"sont \emph{homotopes})", note=ITAL)
add(138, "(6.1.4): 'Lorsqu'on peut définir l'hypercohomologie d'un foncteur'", "'hypercohomologie' italic",
    "upright", "italics", "définir l'hypercohomologie d'un", r"définir l'\emph{hypercohomologie} d'un", note=ITAL)
add(138, "(6.1.4): 'additif T de C dans'", "C bold italic", "plain $C$", "font",
    "additif $T$ de $C$ dans", r"additif $T$ de $\boldsymbol{C}$ dans", note=CBOLD)
add(138, "(6.1.4): 'une catégorie abélienne C''", "C' bold italic", "plain $C'$", "font",
    "abélienne $C'$", r"abélienne $\boldsymbol{C}'$", note=CBOLD)
add(138, "(6.1.4): 'par rapport à un complexe de C (0, 11.4.3)'", "C bold italic", "plain $C$", "font",
    "un complexe de $C$", r"un complexe de $\boldsymbol{C}$", note=CBOLD)
add(138, "(6.1.4): '(0, 11.4.3)'", "bold 0", "plain 0", "convention",
    "(0, 11.4.3)", r"(\textbf{0}, 11.4.3)", conv=2, note=BOLD0)
add(138, "(6.1.4): 'de complexes de C définit canoniquement'", "C bold italic", "plain $C$", "font",
    "de complexes de $C$ définit", r"de complexes de $\boldsymbol{C}$ définit", note=CBOLD)
add(138, "(6.1.4): 'définit canoniquement un isomorphisme'", "'isomorphisme' italic", "upright", "italics",
    "canoniquement un" + P + "isomorphisme", "canoniquement un" + P + r"\emph{isomorphisme}", note=ITAL)
add(138, "(6.1.4): 'un isomorphisme R•T(K•)→R•T(K'•) pour l'hypercohomologie'",
    "plain arrow (no tilde; enlarged crop), bold R twice, formula in the running text",
    r"displayed; \xrightarrow{\sim}; \mathrm R", "symbol",
    span(138, r"\[" + P + r"  \mathrm R^\bullet T(K^\bullet)", r"\]"),
    r"$\mathbf R^\bullet T(K^\bullet)\to\mathbf R^\bullet T(K'^\bullet)$",
    note="One fix for three differences in the same formula: the print's arrow has no tilde, R is bold "
         "(hypercohomology, cf. GLOBAL_ISSUES item 39), and the formula is in the running text.")
add(138, "(6.1.4): 'pour l'hypercohomologie (loc. cit.).'", "'(loc. cit.)' italic, parentheses included", "upright",
    "italics", "(loc. cit.)", r"\emph{(loc. cit.)}", note=ITAL + " Same form as the earlier fix (EGA II p. 9).")
add(138, "heading 6.2", "6.2. Hypercohomologie des complexes de modules sur un préschéma. (final full stop)",
    "no full stop", "punctuation",
    r"\subsection{Hypercohomologie des complexes de modules sur un préschéma}",
    r"\subsection{Hypercohomologie des complexes de modules sur un préschéma.}")
add(138, "(6.2.1): 'on a défini (0, 12.4.1)'", "bold 0", "plain 0", "convention",
    "(0, 12.4.1)", r"(\textbf{0}, 12.4.1)", conv=2, note=BOLD0)
add(138, "(6.2.1): 'les O_Y-Modules d'hypercohomologie'", "'Modules d'hypercohomologie' italic", "upright",
    "italics", r"$\mathscr O_Y$-Modules d'hypercohomologie", r"$\mathscr O_Y$-\emph{Modules d'hypercohomologie}",
    note=ITAL)
add(138, "(6.2.1): '(aussi notés H^n_f(K•) ou R^n f_*(K•))'", "bold R (enlarged crop)", r"\mathrm R", "font",
    r"$\mathrm R^n f_*(\mathscr K^\bullet)$", r"$\mathbf R^n f_*(\mathscr K^\bullet)$",
    note="Hypercohomology R printed bold, as for R•T in (6.1.4); the R^p f_* of (6.2.1.2) is plain in the print.")
add(138, "(6.2.1.1)", "no punctuation after the formula", "comma", "punctuation",
    r"(f,\mathscr K^\bullet)\bigr),", r"(f,\mathscr K^\bullet)\bigr)")
add(138, "(6.2.1.2)", "no full stop after the formula", "full stop", "punctuation",
    r"(\mathscr K^\bullet)\bigr).", r"(\mathscr K^\bullet)\bigr)")
add(138, "end of the page, after (6.2.1.2) / p. 139 'où H^q(f, K•) est le complexe'",
    "the sentence continues on p. 139 ('où ...'), first line not indented",
    "blank lines after \\end{align} and after \\oldpage[III]{139} make a paragraph break", "other",
    r"\end{align}" + P + P, r"\end{align}" + P,
    note="Spurious paragraph break; apply together with the p. 139 finding (blank line after the marker).")

# ---------------------------------------------------------------- page 139
add(139, "top of the page: 'où H^q(f, K•) est le complexe'", "continuation, first line not indented",
    "blank line after \\oldpage[III]{139}", "other",
    r"\oldpage[III]{139}" + P + P + "où", r"\oldpage[III]{139}" + P + "où",
    note="Spurious paragraph break; apply together with the p. 138 finding (blank line after \\end{align}).")
add(139, "(6.2.1): 'est le complexe dont le composant'", "'complexe' italic", "upright", "italics",
    "est le complexe dont", r"est le \emph{complexe} dont", note=ITAL)
add(139, "(6.2.1): 'R^q f_*(K^i) (loc. cit.).'", "'(loc. cit.)' italic, parentheses included", "upright",
    "italics", "(loc. cit.)", r"\emph{(loc. cit.)}", note=ITAL)
add(139, "(6.2.1): 'qui est formée de modules sur'", "'modules' italic", "upright", "italics",
    "formée de modules sur", r"formée de \emph{modules} sur", note=ITAL)
add(139, "(6.2.1): after the display H^n(f, K•)=R^{n-i_0}f_*(K^{i_0}).",
    "'La suite spectrale ...' starts a new, indented paragraph", "no blank line after \\]", "other",
    r"\]" + P + "La suite spectrale", r"\]" + P + P + "La suite spectrale",
    note="Paragraph break as printed (indented line).")
add(139, "(6.2.1): 'est toujours régulière'", "'régulière' italic", "upright", "italics",
    "régulière; les deux", r"\emph{régulière}; les deux", note=ITAL)
add(139, "(6.2.1): 'sont birégulières lorsque'", "'birégulières' italic", "upright", "italics",
    "sont birégulières", r"sont \emph{birégulières}", note=ITAL)
add(139, "(6.2.1): 'lorsque K• est limité inférieurement'",
    "roman K• (not script; enlarged crop)", r"$\mathscr K^\bullet$", "misprint_in_print",
    r"$\mathscr K^\bullet$ est limité inférieurement", r"$K^\bullet$ est limité inférieurement",
    corrected=r"$\mathscr K^\bullet$",
    note="Wrong-font letter in the print (the complex is script K•). The TeX silently corrected it; the fix restores "
         "the printed reading (roman capitals are italic in the TeX, item 17).")
add(139, "(6.2.1): '(0, 12.4.1)'", "bold 0", "plain 0", "convention",
    "(0, 12.4.1)", r"(\textbf{0}, 12.4.1)", conv=2, note=BOLD0)
add(139, "(6.2.1): 'Tout homotopisme h : K•→K'•'", "'homotopisme' italic", "upright", "italics",
    "Tout homotopisme", r"Tout \emph{homotopisme}", note=ITAL)
add(139, "(6.2.1): '(6.1.4) donne un isomorphisme'", "'isomorphisme' italic", "upright", "italics",
    "donne un isomorphisme", r"donne un \emph{isomorphisme}", note=ITAL)
add(139, "(6.2.1): 'H•(h) : H•(K•)→H•(K'•) est un isomorphisme et que'", "'isomorphisme' italic", "upright",
    "italics", "est un isomorphisme et que", r"est un \emph{isomorphisme} et que", note=ITAL)
add(139, "(6.2.1): 'sont limités inférieurement, comme il résulte'", "'limités inférieurement' italic",
    "upright", "italics", "sont limités inférieurement,", r"sont \emph{limités inférieurement},", note=ITAL)
add(139, "(6.2.1): '(0, 11.1.5)'", "bold 0", "plain 0", "convention",
    "(0, 11.1.5)", r"(\textbf{0}, 11.1.5)", conv=2, note=BOLD0)
add(139, "(6.2.1): '(0, 12.4.5)'", "bold 0", "plain 0", "convention",
    "(0, 12.4.5)", r"(\textbf{0}, 12.4.5)", conv=2, note=BOLD0)
add(139, "proof of (6.2.2): '(I, 5.5.6)'", "bold I", "plain I", "convention",
    "(I, 5.5.6)", r"(\textbf{I}, 5.5.6)", conv=2, note=BOLD0)
add(139, "proof of (6.2.2): '(0, 12.4.7)'", "bold 0", "plain 0", "convention",
    "(0, 12.4.7)", r"(\textbf{0}, 12.4.7)", conv=2, note=BOLD0)
add(139, "proof of (6.2.3): 'Comme les H^q(f, K^i)=R^q f_*(K_i)'",
    "R^q f_*(K_i) with a subscript i (enlarged crop)", r"\mathrm R^q f_*(\mathscr K_i)", "misprint_in_print",
    None, None, corrected=r"\mathrm R^q f_*(\mathscr K^i)",
    note="Misprint in the print (the left side has K^i); the TeX keeps the printed reading.")
add(139, "proof of (6.2.3): 'par une image d'un tel homomorphisme (I, 4.1.1)'", "bold I", "plain I", "convention",
    "homomorphisme (I, 4.1.1)", r"homomorphisme (\textbf{I}, 4.1.1)", conv=2, note=BOLD0)
add(139, "proof of (6.2.3): 'tous les O_Y-Modules 'E_r^pq, B_k('E_r^pq), Z_k('E_r^pq)'",
    "B_k('E^pq_r) with the index r (enlarged crop)", "B_k('E_2^{pq})", "formula",
    r"$B_k('\mathscr E_2^{pq})$", r"$B_k('\mathscr E_r^{pq})$",
    note="Not a misprint: B_k(E_r^pq) and Z_k(E_r^pq) are defined for every r in (0, 11.1.1); the TeX changed r to 2.")
add(139, "proof of (6.2.3): same list, Z_k('E_r^pq)", "Z_k('E^pq_r) with the index r (enlarged crop)",
    "Z_k('E_2^{pq})", "formula",
    r"$Z_k('\mathscr E_2^{pq})$ de la", r"$Z_k('\mathscr E_r^{pq})$ de la",
    note="As for B_k in the same list.")
add(139, "proof of (6.2.3): '(0, 11.2.4 et I, 4.1.1)', first reference", "bold 0", "plain 0", "convention",
    "(0, 11.2.4 et", r"(\textbf{0}, 11.2.4 et", conv=2, note=BOLD0)
add(139, "proof of (6.2.3): '(0, 11.2.4 et I, 4.1.1)', second reference", "bold I", "plain I", "convention",
    "I, 4.1.1);", r"\textbf{I}, 4.1.1);", conv=2, note=BOLD0)
add(139, "proof of (6.2.3): 'et comme H^n(f, K•)=lim G_k'", "lim with only the arrow under it, no index k",
    r"\varinjlim_k", "formula",
    r"\varinjlim_k\mathscr G_k", r"\varinjlim\mathscr G_k",
    note="Enlarged crop; the lim of B_∞('E_2^pq) above has its index k, as in the TeX.")
add(139, "proof of (6.2.3): 'la proposition est démontrée (I, 4.1.1)'", "bold I", "plain I", "convention",
    "démontrée (I, 4.1.1)", r"démontrée (\textbf{I}, 4.1.1)", conv=2, note=BOLD0)

# ---------------------------------------------------------------- page 140
add(140, "proof of (6.2.4): 'K• par f_*(C•(U, K•))'", "script C (the sheaf cochain complex; enlarged crop)",
    "roman/italic C", "font",
    r"$f_*(C^\bullet(\mathfrak U,\mathscr K^\bullet))$", r"$f_*(\mathscr C^\bullet(\mathfrak U,\mathscr K^\bullet))$",
    note="Only this C is script on the page; the C•(U, ...) and C^i(U, ...) of (6.2.5)-(6.2.6) are roman, as in the TeX.")
add(140, "proof of (6.2.5): 'supposer que U est fini'", "'fini' italic", "upright", "italics",
    "est fini, puisque", r"est \emph{fini}, puisque", note=ITAL)
add(140, "proof of (6.2.5): 'étant alternées par définition'", "'alternées' italic", "upright", "italics",
    "alternées par définition", r"\emph{alternées} par définition", note=ITAL)
add(140, "proof of (6.2.5): '(0, 11.3.3)'", "bold 0", "plain 0", "convention",
    "(0, 11.3.3)", r"(\textbf{0}, 11.3.3)", conv=2, note=BOLD0)
add(140, "proof of (6.2.5): 'sont birégulières. Comme les'", "'birégulières' italic", "upright", "italics",
    "sont birégulières. Comme", r"sont \emph{birégulières}. Comme", note=ITAL)
add(140, "proof of (6.2.5): '(I, 5.5.6)'", "bold I", "plain I", "convention",
    "(I, 5.5.6)", r"(\textbf{I}, 5.5.6)", conv=2, note=BOLD0)
add(140, "proof of (6.2.5): 'chaque foncteur F⇝C^i(U, F)'", "wavy arrow", r"\mapsto", "symbol",
    r"$\mathscr F\mapsto C^i", r"$\mathscr F\leadsto C^i", note=ARROW)
add(140, "proof of (6.2.5): '(0, 11.3.2)'", "bold 0", "plain 0", "convention",
    "(0, 11.3.2)", r"(\textbf{0}, 11.3.2)", conv=2, note=BOLD0)
add(140, "proof of (6.2.5), display ''E_2^pq = ... = H^p(U, H^q(K•)) = ...'",
    "middle H^p(U, ...) plain, like the two other H of the display", r"\mathbf H^p", "font",
    r"=\mathbf H^p(\mathfrak U,\mathscr H^q(\mathscr K^\bullet))",
    r"=\mathrm H^p(\mathfrak U,\mathscr H^q(\mathscr K^\bullet))",
    note="Measured on the scan: the three H of the display have 5-6 px stems; the bold H of (6.2.4.1) has 8-9 px.")
add(140, "proof of (6.2.5): 'Γ(Y, O_Y)-modules de type fini (3.2.1)'", "'de type fini' italic", "upright",
    "italics", "modules de type fini (3.2.1)", r"modules \emph{de type fini} (3.2.1)", note=ITAL)
add(140, "proof of (6.2.5): '(0, 11.1.8)'", "bold 0", "plain 0", "convention",
    "(0, 11.1.8)", r"(\textbf{0}, 11.1.8)", conv=2, note=BOLD0)
add(140, "proof of (6.2.5), last paragraph: 'A fortiori'", "'A fortiori' italic", "upright", "italics",
    "A fortiori, si", r"\emph{A fortiori}, si", note=ITAL)
add(140, "proof of (6.2.5): 'complexe de O_X-Modules cohérents'", "'cohérents' italic", "upright", "italics",
    "Modules cohérents, les", r"Modules \emph{cohérents}, les", note=ITAL)
add(140, "proof of (6.2.5): 'sont cohérents sous les hypothèses'", "'cohérents' italic", "upright", "italics",
    "sont cohérents sous", r"sont \emph{cohérents} sous", note=ITAL)
add(140, "proof of (6.2.5): '(0_I, 5.3.4)'", "bold 0", "plain 0", "convention",
    r"(0\textsubscript{I}, 5.3.4)", r"(\textbf{0}\textsubscript{I}, 5.3.4)", conv=2, note=BOLD0)
add(140, "(6.2.6): 'est un foncteur cohomologique dans la catégorie'", "'cohomologique' italic", "upright",
    "italics", "est un foncteur" + P + "cohomologique", "est un foncteur" + P + r"\emph{cohomologique}", note=ITAL)
add(140, "(6.2.6): 'Modules limités inférieurement (0, 12.4.4)'", "'limités inférieurement' italic", "upright",
    "italics", "Modules" + P + "limités inférieurement", "Modules" + P + r"\emph{limités inférieurement}", note=ITAL)
add(140, "(6.2.6): '(0, 12.4.4)'", "bold 0", "plain 0", "convention",
    "(0, 12.4.4)", r"(\textbf{0}, 12.4.4)", conv=2, note=BOLD0)
add(140, "(6.2.6): 'dans la catégorie de tous les complexes'", "'tous' italic", "upright", "italics",
    "catégorie de tous les", r"catégorie de \emph{tous} les", note=ITAL)
add(140, "(6.2.6): 'le morphisme f est quasi-compact'", "'quasi-compact' italic", "upright", "italics",
    "est quasi-compact et l'espace", r"est \emph{quasi-compact} et l'espace", note=ITAL)
add(140, "(6.2.6): 'sous-jacent à X localement noethérien'", "'localement noethérien' italic", "upright",
    "italics", "$X$ localement" + P + "noethérien", r"$X$ \emph{localement" + P + "noethérien}", note=ITAL)
add(140, "(6.2.6): '(0, 11.5.2)'", "bold 0", "plain 0", "convention",
    "(0, 11.5.2)", r"(\textbf{0}, 11.5.2)", conv=2, note=BOLD0)
add(140, "(6.2.6), 2nd paragraph: 'si f est séparé'", "'séparé' italic", "upright", "italics",
    "est séparé,", r"est \emph{séparé},", note=ITAL)
add(140, "(6.2.6): 'complexes de O_X-Modules quasi-cohérents. C'est immédiat'", "'quasi-cohérents' italic",
    "upright", "italics", "Modules quasi-cohérents. C'est", r"Modules \emph{quasi-cohérents}. C'est", note=ITAL)
add(140, "(6.2.6): 'car alors X est un schéma'", "'schéma' italic", "upright", "italics",
    "est un schéma, donc", r"est un \emph{schéma}, donc", note=ITAL)
add(140, "(6.2.6): 'on est ramené à voir que K•⇝H•(U, K•)'", "wavy arrow", r"\mapsto", "symbol",
    r"$\mathscr K^\bullet\mapsto\mathbf H^\bullet", r"$\mathscr K^\bullet\leadsto\mathbf H^\bullet", note=ARROW)
add(140, "(6.2.6): 'le foncteur K•⇝C•(U, K•) est exact'", "wavy arrow", r"\mapsto", "symbol",
    r"$\mathscr K^\bullet\mapsto" + P + r"C^\bullet", r"$\mathscr K^\bullet\leadsto" + P + r"C^\bullet", note=ARROW)
add(140, "(6.2.6): '(I, 1.3.7)'", "bold I", "plain I", "convention",
    "(I, 1.3.7)", r"(\textbf{I}, 1.3.7)", conv=2, note=BOLD0)
add(140, "end of the page: 'pour tout ouvert affine V' / p. 141 'de Y, ...'",
    "the sentence runs on to p. 141; no paragraph break",
    "blank lines before and after \\oldpage[III]{141} make a paragraph break", "other",
    "pour tout ouvert affine $V$" + P + P, "pour tout ouvert affine $V$" + P,
    note="Spurious paragraph break; apply together with the p. 141 finding (blank line after the marker).")

# ---------------------------------------------------------------- page 141
add(141, "top of the page: 'de Y, f^{-1}(Y) est un schéma' (continuation of (6.2.6))",
    "first line not indented, same paragraph", "blank line after \\oldpage[III]{141}", "other",
    r"\oldpage[III]{141}" + P + P + "de $Y$", r"\oldpage[III]{141}" + P + "de $Y$",
    note="Spurious paragraph break; apply together with the p. 140 finding (blank line before the marker).")
add(141, "(6.2.6): 'pour tout ouvert affine V de Y, f^{-1}(Y) est un schéma'",
    "f^{-1}(Y) (enlarged crop)", "$f^{-1}(Y)$", "misprint_in_print", None, None, corrected="$f^{-1}(V)$",
    note="Misprint in the print: f^{-1}(V) is the scheme meant (f separated, V affine; the next lines use f^{-1}(V)). "
         "The TeX keeps the printed reading.")
add(141, "(6.2.6): 'pour une suite exacte 0→K'•→K•→K''•→0 de complexes'", "in the running text", "displayed",
    "other", span(141, "suite exacte" + P + r"\[", r"\]" + P + "de complexes"),
    "suite exacte" + P + r"$0\longrightarrow\mathscr K'^\bullet\longrightarrow\mathscr K^\bullet"
    r"\longrightarrow\mathscr K''^\bullet\longrightarrow0$" + P + "de complexes", note=INLINE)
add(141, "(6.2.6): 'l'homomorphisme ∂ : H^n(f, K''•)|V→H^{n+1}(f, K'•)|V ne dépend pas'",
    "in the running text", "displayed", "other",
    span(141, "l'homomorphisme" + P + r"\[", r"\]" + P + "ne dépend"),
    "l'homomorphisme" + P + r"$\partial:\mathscr H^n(f,\mathscr K''^\bullet)|V\longrightarrow"
    r"\mathscr H^{n+1}(f,\mathscr K'^\bullet)|V$" + P + "ne dépend", note=INLINE)
WR = "The print marks the vertical isomorphism with ≀ (vertical tilde, \\wr), on the right of the arrow; \\iota gives a Greek iota."
add(141, "(6.2.6), first diagram: vertical arrow H•(U, K•)→H•(U', K•)", "label ≀ on the right of the arrow",
    r"\ar[dd]^{\iota}", "symbol", r"\ar[dd]^{\iota}", r"\ar[dd]^{\wr}", note=WR)
add(141, "(6.2.6), first diagram: arrow H•(U', K•)→H•(f^{-1}(V), K•)", "tilde above (upper left of) the rising arrow",
    r"\ar[rru]_-{\sim}: xy-pic puts a _ label below right of a rising arrow", "other",
    r"\ar[rru]_-{\sim}", r"\ar[rru]^-{\sim}", conf="medium",
    note="Label side only (cf. GLOBAL_ISSUES item 30); the falling arrow's ^-{\\sim} matches the print.")
add(141, "(6.2.6), second diagram: left vertical arrow", "label ≀ on the right of the arrow",
    r"\ar[d]^{\iota}", "symbol", r"\ar[r]^-{\partial}\ar[d]^{\iota}", r"\ar[r]^-{\partial}\ar[d]^{\wr}", note=WR)
add(141, "(6.2.6), second diagram: right vertical arrow", "label ≀ on the right of the arrow",
    r"\ar[d]^{\iota}", "symbol",
    r"\mathbf H^{n+1}(\mathfrak U,\mathscr K'^\bullet)" + P + r"      \ar[d]^{\iota}",
    r"\mathbf H^{n+1}(\mathfrak U,\mathscr K'^\bullet)" + P + r"      \ar[d]^{\wr}", note=WR)
add(141, "(6.2.6), second diagram, bottom right entry", "no full stop after the diagram", "full stop",
    "punctuation", r"\mathbf H^{n+1}(\mathfrak U',\mathscr K'^\bullet).",
    r"\mathbf H^{n+1}(\mathfrak U',\mathscr K'^\bullet)")
add(141, "(6.2.6), last paragraph: '(0, 11.4.4)'", "bold 0", "plain 0", "convention",
    "(0, 11.4.4)", r"(\textbf{0}, 11.4.4)", conv=2, note=BOLD0)
add(141, "heading 6.3", "6.3. Hypertor de deux complexes de modules. (final full stop)", "no full stop",
    "punctuation", r"\subsection{Hypertor de deux complexes de modules}",
    r"\subsection{Hypertor de deux complexes de modules.}")
add(141, "(6.3.1): '(0, 11.6.1)'", "bold 0", "plain 0", "convention",
    "(0, 11.6.1)", r"(\textbf{0}, 11.6.1)", conv=2, note=BOLD0)
add(141, "(6.3.1): '(0, 11.6.5)'", "bold 0", "plain 0", "convention",
    "(0, 11.6.5)", r"(\textbf{0}, 11.6.5)", conv=2, note=BOLD0)
add(141, "end of the page, after (6.3.1.1) / p. 142 'et nous dirons que cet A-module'",
    "the sentence continues on p. 142 ('et nous dirons ...'), first line not indented",
    "blank lines after \\] and after \\oldpage[III]{142} make a paragraph break", "other",
    r"\label{III.6.3.1.1.fr}" + P + r"\]" + P + P, r"\label{III.6.3.1.1.fr}" + P + r"\]" + P,
    note="Spurious paragraph break; apply together with the p. 142 fix "
         "'\\oldpage[III]{142}\\n\\net nous dirons' -> '\\oldpage[III]{142}\\net nous dirons' (page_142.tex).")

# ---------------------------------------------------------------- checks
errors = []
for f in F:
    fx = f["fix"]
    if fx is None:
        continue
    old = fx["old"]
    target = lead if f["_outside"] else pages[f["page"]]
    n = target.count(old)
    if n != 1:
        errors.append((f["page"], f["where"], n, old[:60]))
    if f["_outside"] and src.count(old) != 1:
        errors.append((f["page"], f["where"], "src count", src.count(old)))
# overlaps per page (non-outside fixes)
for p in pages:
    spans = []
    for f in F:
        if f["page"] != p or f["fix"] is None or f["_outside"]:
            continue
        i = pages[p].find(f["fix"]["old"])
        spans.append((i, i + len(f["fix"]["old"]), f["where"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            errors.append(("overlap", p, a[2], b[2]))
if errors:
    for e in errors:
        print("ERROR", e)
    sys.exit(1)

# apply all page fixes to copies and make sure every new text is present once (sanity)
for p in pages:
    t = pages[p]
    for f in F:
        if f["page"] == p and f["fix"] is not None and not f["_outside"]:
            assert t.count(f["fix"]["old"]) == 1, (p, f["where"])
            t = t.replace(f["fix"]["old"], f["fix"]["new"], 1)

out = []
for f in F:
    g = dict(f)
    g.pop("_outside")
    out.append(g)
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

from collections import Counter
cnt = Counter()
for f in out:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    cnt[(f["page"], k)] += 1
for p in pages:
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("total", len(out), "written", OUT)
