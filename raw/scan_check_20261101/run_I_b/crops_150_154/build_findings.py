"""Build findings_150_154.json (EGA I pp. 150-154) and check every fix against the page files.

Each fix "old" must occur exactly once in page_NNN.tex (CRLF normalised) and in the matching page
segment of the release source, also when the fixes of the page are applied in list order.
No .tex file is written.
usage: python -I build_findings.py
"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_I_b")
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\BASE\native\ega1\ega1-6-fr.tex")
OUT = RUN / "findings_150_154.json"

LABEL_NOTE_FIRST = (
    "The print sets the item labels of italic statements upright (checked on a crop); \\item[(i)] takes the "
    "\\itshape of the statement environment (EGA_FR.tex sets no label font), so the TeX label is italic. "
    "This holds for every \\item label inside an italic statement environment; one environment-level change "
    "would cover them all.")
LABEL_NOTE = "Label upright in the print, italic in the TeX environment (see the label finding for (6.5.1)(i) on p. 150)."
REF_NOTE = "Reference printed upright inside the italic statement; italic in the TeX environment."
SETMIN_NOTE = ("Long dash for the set difference. \\setmin is still defined as '-' in preamble-base.tex; "
               "same edit as run_I_a p. 118.")


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=(dict(old=old, new=new) if old is not None else None))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


def label(page, stmt, lab, old_tail, first=False):
    old = "\\item[" + lab + "] " + old_tail
    new = "\\item[\\textup{" + lab + "}] " + old_tail
    return F(page, f"{stmt}, label {lab}", f"label {lab} upright", old, "convention", 6, "high",
             old, new, LABEL_NOTE_FIRST if first else LABEL_NOTE)


def bold0(page, where, ref):
    old = "{0, " + ref + "}"
    return F(page, where, f"(0, {ref}) with bold 0", old, "convention", 2, "high",
             old, "{\\textbf{0}, " + ref + "}", "")


def setmin(page, where, scan, old):
    return F(page, where, scan, old, "convention", 7, "high", old, old.replace("B-", "B\\setmin").replace("A-", "A\\setmin"),
             SETMIN_NOTE)


findings = [
    # ---------------- page 150 ----------------
    label(150, "Proposition (6.5.1)", "(i)", "Si deux", first=True),
    label(150, "Proposition (6.5.1)", "(ii)", "Supposons en outre"),
    F(150, "proof of (6.5.1)(i): 'on peut en outre supposer que C est une A-algèbre de type fini'",
      "'de type fini' in italics", "une $A$-algèbre de type fini", "italics", None, "high",
      "une $A$-algèbre de type fini", "une $A$-algèbre \\emph{de type fini}", "Checked on a crop."),
    setmin(150, "proof of (6.5.1)(i): 'des éléments s_i∈B—j_x'", "s_i∈B—j_x (long dash)",
           "$s_i\\in B-\\mathfrak{j}_x$"),
    setmin(150, "proof of (6.5.1)(i): 'à un même élément g∈B—j_x. On en conclut'", "g∈B—j_x (long dash)",
           "$g\\in B-\\mathfrak{j}_x$. On en"),
    F(150, "proof of (6.5.1)(ii): 'supposer en outre que l'anneau A est noethérien'",
      "'noethérien' in italics", "l'anneau $A$ est noethérien", "italics", None, "high",
      "l'anneau $A$ est noethérien", "l'anneau $A$ est \\emph{noethérien}", "Checked on a crop."),
    setmin(150, "proof of (6.5.1)(ii): 'à un même élément g∈B—j_x. Cela étant'", "g∈B—j_x (long dash)",
           "$g\\in B-\\mathfrak{j}_x$. Cela"),
    F(150, "proof of (6.5.1)(ii), display after 'posons': Q_j(X_1/T,...,X_n/T)=P_j(X_1,...,X_n,T)/T^{k_j}",
      "the exponent of T is set 'kj', the j on the same level and in the same size as the k (not a subscript)",
      "/T^{k_j}", "misprint_in_print", None, "medium",
      "/T^{k_j}", "/T^{kj}",
      "Silent correction in the TeX. The exponent is the degree k_j ('homogène de degré k_j' just below, with "
      "the j lowered), so the right reading is T^{k_j}; the print does not lower the j (crop at 5x). The same "
      "print does lower a second-level index elsewhere (the y of the arrow label i_y in the display beta on "
      "this page), so this is an error, not the print's style.",
      corrected="/T^{k_j}"),
    setmin(150, "proof of (6.5.1)(ii): 'pour un t_j∈B—j_x'", "t_j∈B—j_x (long dash)",
           "$t_j\\in B-\\mathfrak{j}_x$"),
    # ---------------- page 151 ----------------
    setmin(151, "first line: 'égaux à un même élément h∈B—j_x'", "h∈B—j_x (long dash)",
           "$h\\in B-\\mathfrak{j}_x$"),
    F(151, "diagram (6.5.1.1): labels of the two vertical arrows",
      "'iy' (left) and 'ix' (right): the y and the x stand on the line in the same size as the i, not as subscripts",
      "\\ar[d]_{i_y} & B_{hg}\\ar[d]^{i_x}", "misprint_in_print", None, "medium",
      "\\ar[d]_{i_y} & B_{hg}\\ar[d]^{i_x}", "\\ar[d]_{iy} & B_{hg}\\ar[d]^{ix}",
      "Silent correction in the TeX. The text names these maps i_y (C→C_y) and i_x (B_hg→B_x) with lowered "
      "indices, and the display beta on p. 150 lowers the y of the same label i_y; in this diagram the indices "
      "are not lowered (crop at 6x, both labels).",
      corrected="\\ar[d]_{i_y} & B_{hg}\\ar[d]^{i_x}"),
    F(151, "Corollaire (6.5.2): 'Sous les hypothèses de (6.5.1, (ii)), si en outre'",
      "(6.5.1, (ii)) upright inside the italic statement",
      "(\\hyperref[I.6.5.1-fr]{6.5.1, (ii)}), si en outre", "convention", 6, "high",
      "(\\hyperref[I.6.5.1-fr]{6.5.1, (ii)}), si en outre",
      "\\textup{(\\hyperref[I.6.5.1-fr]{6.5.1, (ii)})}, si en outre", REF_NOTE),
    F(151, "Corollaire (6.5.3): 'Supposons vérifiées les hypothèses de (6.5.1, (ii)), et supposons'",
      "(6.5.1, (ii)) upright inside the italic statement",
      "(\\hyperref[I.6.5.1-fr]{6.5.1, (ii)}), et supposons", "convention", 6, "high",
      "(\\hyperref[I.6.5.1-fr]{6.5.1, (ii)}), et supposons",
      "\\textup{(\\hyperref[I.6.5.1-fr]{6.5.1, (ii)})}, et supposons", REF_NOTE),
    F(151, "Corollaire (6.5.3): 'Alors on peut supposer que f=(^aγ, γ̃) où γ est injectif.'",
      "no comma after f=(^aγ, γ̃)", "$f=({}^a\\gamma,\\widetilde{\\gamma})$, où $\\gamma$ est injectif.",
      "punctuation", None, "high",
      "\\widetilde{\\gamma})$, où $\\gamma$ est injectif", "\\widetilde{\\gamma})$ où $\\gamma$ est injectif",
      "The formula ends the printed line at the right margin and the next line begins 'où'; no comma "
      "(checked on a crop)."),
    label(151, "Proposition (6.5.4)", "(i)", "Pour que"),
    F(151, "Proposition (6.5.4)(i): 'immersion locale au point x (4.5.1)'",
      "(4.5.1) upright inside the italic statement", "(\\hyperref[I.4.5.1-fr]{4.5.1})", "convention", 6, "high",
      "(\\hyperref[I.4.5.1-fr]{4.5.1})", "\\textup{(\\hyperref[I.4.5.1-fr]{4.5.1})}", REF_NOTE),
    label(151, "Proposition (6.5.4)", "(ii)", "On suppose en outre"),
    F(151, "Proposition (6.5.4)(ii): 'isomorphisme local au point x (4.5.2)'",
      "(4.5.2) upright inside the italic statement", "(\\hyperref[I.4.5.2-fr]{4.5.2})", "convention", 6, "high",
      "(\\hyperref[I.4.5.2-fr]{4.5.2})", "\\textup{(\\hyperref[I.4.5.2-fr]{4.5.2})}", REF_NOTE),
    F(151, "proof of (6.5.4)(i): 'on a φ^{-1}(j_x)=j_y, et l'homomorphisme φ_x : B_y→A_x'",
      "comma after j_y", "$\\varphi^{-1}(\\mathfrak{j}_x)=\\mathfrak{j}_y$ et l'homomorphisme",
      "punctuation", None, "high",
      "=\\mathfrak{j}_y$ et l'homomorphisme", "=\\mathfrak{j}_y$, et l'homomorphisme",
      "Missing comma (checked on a crop)."),
    F(151, "proof of (6.5.4)(i): 'l'homomorphisme φ_x : B_y→A_x déduit de φ est surjectif'",
      "'surjectif' in italics", "déduit de $\\varphi$ est surjectif", "italics", None, "high",
      "déduit de $\\varphi$ est surjectif", "déduit de $\\varphi$ est \\emph{surjectif}", "Checked on a crop."),
    setmin(151, "proof of (6.5.4)(i): 'des b_i∈B et un c∈B—j_y'", "c∈B—j_y (long dash)",
           "$c\\in B-\\mathfrak{j}_y$"),
    setmin(151, "proof of (6.5.4)(i): 'il existe a∈A—j_x tel que'", "a∈A—j_x (long dash)",
           "$a\\in A-\\mathfrak{j}_x$"),
    # ---------------- page 152 ----------------
    bold0(152, "proof of (6.5.4)(i): 'se factorise en B→B_h→A_g (0, 1.2.4)'", "1.2.4"),
    label(152, "Corollaire (6.5.5)", "(i)", "Pour que"),
    label(152, "Corollaire (6.5.5)", "(ii)", "On suppose de plus"),
    F(152, "Corollaire (6.5.5)(ii): '(ou, ce qui revient au même (0, 2.1.4) que f soit un morphisme dominant)'",
      "the parenthesis is roman with only 'dominant' in italics; the statement resumes in italics at "
      "'et que θ^♯_x soit un isomorphisme'",
      "(ou, ce qui revient au même (\\hyperref[0.2.1.4-fr]{0, 2.1.4}) que $f$ soit un morphisme \\emph{dominant}) "
      "[three source lines; italic in the TeX, 'dominant' upright]",
      "convention", 6, "high",
      "générique de $Y$ (ou, ce qui revient au même", "générique de $Y$ \\upshape(ou, ce qui revient au même",
      "Checked on a crop. The parenthesis spans three source lines, so the fix uses font switches: \\upshape "
      "here and \\itshape after 'dominant})' (next finding); inside the upright stretch \\emph{dominant} comes "
      "out italic as printed. Apply together with the next finding. Independent of the bold-0 edit of the "
      "reference (0, 2.1.4) on the line between them."),
    F(152, "Corollaire (6.5.5)(ii): ') et que θ^♯_x soit un isomorphisme (autrement dit, que f soit birationnel (2.2.9)).'",
      "'et que θ^♯_x soit un isomorphisme' italic; '(autrement dit, que f soit birationnel (2.2.9)).' roman with "
      "only 'birationnel' in italics",
      "\\emph{dominant}) et que $\\theta_x^\\sharp$ soit un isomorphisme (autrement dit, que $f$ soit "
      "\\emph{birationnel} (\\hyperref[I.2.2.9-fr]{2.2.9})). [italic in the TeX, 'birationnel' upright]",
      "convention", 6, "high",
      "\\emph{dominant}) et que $\\theta_x^\\sharp$ soit un isomorphisme (autrement",
      "\\emph{dominant}) \\itshape et que $\\theta_x^\\sharp$ soit un isomorphisme \\upshape(autrement",
      "Checked on a crop. \\itshape ends the first roman parenthesis; \\upshape starts the second, which runs to "
      "the end of item (ii) (\\end{enumerate} closes the group); \\emph{birationnel} then comes out italic as "
      "printed. Apply together with the previous finding."),
    bold0(152, "Corollaire (6.5.5)(ii): 'ce qui revient au même (0, 2.1.4)'", "2.1.4"),
    F(152, "Définition (6.6.1): 'est quasi-compact si l'image réciproque'",
      "'quasi-compact' italic like the rest of the definition (no change of face)",
      "\\emph{quasi-compact} si l'image", "convention", 6, "high",
      "\\emph{quasi-compact} si l'image", "quasi-compact si l'image",
      "\\emph inside the italic definition environment sets the word upright; drop the \\emph (checked on a crop)."),
    F(152, "Définition (6.6.2): 'est localement de type fini si, pour tout x∈X'",
      "'localement de type fini' italic like the rest of the definition (no change of face)",
      "\\emph{localement de type fini} si, pour", "convention", 6, "high",
      "\\emph{localement de type fini} si, pour", "localement de type fini si, pour",
      "\\emph inside the italic definition environment sets the words upright; drop the \\emph (checked on a crop)."),
    # ---------------- page 153 ----------------
    F(153, "proof of (6.6.3): 'En remplaçant W(x) par un voisinage W_1(x)⊂W(x) de x de la forme D(g)'",
      "'de x'", "$W_1(x)\\subset W(x)$ de $x$ de la forme", "misprint_in_print", None, "high",
      None, None,
      "The TeX keeps the printed reading. W_1(x)⊂W(x)⊂U is an open set of Y, a neighbourhood of y=f(x) (the "
      "previous sentence: 'un voisinage W(x)⊂U de y=f(x)'); a point x of X has no neighbourhood in Y. "
      "Correct reading 'de y'. Print reading checked on a crop.",
      corrected="$W_1(x)\\subset W(x)$ de $y$ de la forme"),
    label(153, "Proposition (6.6.4)", "(i)", "Une immersion"),
    label(153, "Proposition (6.6.4)", "(ii)", "Le composé"),
    label(153, "Proposition (6.6.4)", "(iii)", "Si $f:X\\to Y$"),
    label(153, "Proposition (6.6.4)", "(iv)", "Si $f:X\\to X'$"),
    label(153, "Proposition (6.6.4)", "(v)", "Si le composé"),
    label(153, "Proposition (6.6.4)", "(vi)", "Pour qu'un"),
    bold0(153, "proof of (6.6.4)(v): 'On en conclut (0, 2.2.3)'", "2.2.3"),
    # ---------------- page 154 ----------------
    F(154, "proof of (6.6.4)(iii): 'prouver que lorsque S et S' sont affines'",
      "'affines' in italics", "et $S'$ sont affines", "italics", None, "high",
      "et $S'$ sont affines", "et $S'$ sont \\emph{affines}", "Checked on a crop."),
    F(154, "proof of (6.6.5): 'y appartient à l'adhérence dans U d'un des f(V_i)'",
      "'dans' in italics", "l'adhérence dans $U$", "italics", None, "high",
      "l'adhérence dans $U$", "l'adhérence \\emph{dans} $U$", "Checked on a crop."),
    bold0(154, "proof of (6.6.5): 'composante irréductible de X (0, 2.1.6)'", "2.1.6"),
    bold0(154, "proof of (6.6.5): 'un idéal premier minimal de A (0, 1.5.8)'", "1.5.8"),
    label(154, "Proposition (6.6.6)", "(i)", "Toute immersion"),
    label(154, "Proposition (6.6.6)", "(ii)", "Si deux"),
    label(154, "Proposition (6.6.6)", "(iii)", "Si $f:X\\to Y$"),
    label(154, "Proposition (6.6.6)", "(iv)", "Si $f:X\\to X'$"),
    label(154, "Proposition (6.6.6)", "(v)", "Si le composé"),
    label(154, "Proposition (6.6.6)", "(vi)", "Si un morphisme"),
]

# ---- checks: every old occurs once in page_NNN.tex and in the release page segment, in list order ----
rel = REL.read_text(encoding="utf-8").replace("\r\n", "\n")
marker = re.compile(r"\\oldpage\[I\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(rel)]
segs = {}
for i, (n, s) in enumerate(cuts):
    segs[n] = rel[s:(cuts[i + 1][1] if i + 1 < len(cuts) else len(rel))]
pages = {}
for p in range(150, 155):
    t = (RUN / f"page_{p}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    pages[p] = t.split("\n", 1)[1].split("% (continued in")[0]
bad = 0
work_page = dict(pages)
work_rel = {p: segs[p] for p in range(150, 155)}
for x in findings:
    fx = x["fix"]
    if not fx:
        continue
    p = x["page"]
    c1, c2 = pages[p].count(fx["old"]), segs[p].count(fx["old"])
    c3, c4 = work_page[p].count(fx["old"]), work_rel[p].count(fx["old"])
    if (c1, c2, c3, c4) != (1, 1, 1, 1):
        bad += 1
        print("BAD", p, repr(fx["old"]), c1, c2, c3, c4)
    work_page[p] = work_page[p].replace(fx["old"], fx["new"])
    work_rel[p] = work_rel[p].replace(fx["old"], fx["new"])
    if "\n" in fx["old"] or "\r" in fx["old"]:
        print("MULTILINE", p, repr(fx["old"]))
for x in findings:  # the kept misprint: its TeX excerpt must be on the page
    if x["fix"] is None and x["tex"] not in pages[x["page"]]:
        bad += 1
        print("BAD tex excerpt", x["page"], x["tex"])
print("checks failed:", bad)

json.dump(findings, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
for p in range(150, 155):
    xs = [x for x in findings if x["page"] == p]
    conv = sum(1 for x in xs if x["kind"] == "convention")
    mis = sum(1 for x in xs if x["kind"] == "misprint_in_print")
    print(p, "normal", len(xs) - conv - mis, "convention", conv, "misprint", mis)
print("written", OUT, len(findings))
