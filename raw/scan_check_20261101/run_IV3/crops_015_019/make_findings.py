import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\source\ega4\ega4-8-fr.tex")
OUT = RUN / "findings_015_019.json"
NL = "\u00b6"  # placeholder for a line break inside raw strings


def fx(old, new):
    return {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}


F = []


def add(page, where, scan, tex, kind, conv, conf, fix, note, cross=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": fix, "note": note}
    if cross:
        d["_cross"] = True
    F.append(d)


OC = ("The print has Fraktur O (the same glyph as \u2118-free 'O(X)' = ouvertes on IV-3 p. 95, written \\mathfrak O there) "
      "followed by a full-size Fraktur c on the baseline, as \\mathfrak{Lc} on p. 95; not Fraktur D with a subscript c. "
      "Same for the F c and LF c: baseline Fraktur c.")
OC = OC.replace("\u2118-free ", "")

# ---------------- page 15 ----------------
add(15, "page start: 'Inversement, pour montrer que' (blank line before the page marker)",
    "'Inversement,' stands flush left at the top of p. 15: it continues paragraph (iii) of p. 14 ('... prop. 1).')",
    "a blank line after 'prop. 1).' before \\oldpage[IV-3]{15} starts a new, indented paragraph",
    "marker", None, "high",
    fx(r"prop. 1).¶¶\oldpage[IV-3]{15}", r"prop. 1).¶\oldpage[IV-3]{15}"),
    "The 'old' spans the page boundary: exact substring of ega4-8-fr.tex (lines 810-812), not of page_015.tex, "
    "which starts at the marker. The p. 14 checker may report the same blank line.", cross=True)
add(15, "(8.3.9), line 2: (resp. Oc(X), Fc(X), LFc(X))",
    "(resp. \U0001D512\U0001D520(X), \U0001D509\U0001D520(X), \U0001D50F\U0001D509\U0001D520(X))",
    "(resp. $\\mathfrak D_c(X)$, $\\mathfrak F_c(X)$, $\\mathfrak{LF}_c(X)$)",
    "symbol", None, "high",
    fx(r"(resp. $\mathfrak D_c(X)$, $\mathfrak F_c(X)$, $\mathfrak{LF}_c(X)$)",
       r"(resp. $\mathfrak{Oc}(X)$, $\mathfrak{Fc}(X)$, $\mathfrak{LFc}(X)$)"),
    OC + " Notation of 8.3.9 for constructible open / closed / locally closed sets.")
add(15, "(8.3.9), 'En outre, il résulte de (1.8.2) que u_{lambda mu}^{-1} applique C(S_lambda) (resp. ...)'",
    "(resp. \U0001D512\U0001D520(S_\u03bb), \U0001D509\U0001D520(S_\u03bb), \U0001D50F\U0001D509\U0001D520(S_\u03bb))",
    "(resp. $\\mathfrak D_c(S_\\lambda)$, $\\mathfrak F_c(S_\\lambda)$, $\\mathfrak{LF}_c(S_\\lambda)$)",
    "symbol", None, "high",
    fx(r"(resp. $\mathfrak D_c(S_\lambda)$,¶$\mathfrak F_c(S_\lambda)$, $\mathfrak{LF}_c(S_\lambda)$)",
       r"(resp. $\mathfrak{Oc}(S_\lambda)$,¶$\mathfrak{Fc}(S_\lambda)$, $\mathfrak{LFc}(S_\lambda)$)"),
    "Fraktur O + baseline Fraktur c (see the finding for line 2 of 8.3.9).")
add(15, "(8.3.9), '... dans C(S_mu) (resp. ...)'",
    "(resp. \U0001D512\U0001D520(S_\u03bc), \U0001D509\U0001D520(S_\u03bc), \U0001D50F\U0001D509\U0001D520(S_\u03bc))",
    "(resp. $\\mathfrak D_c(S_\\mu)$, $\\mathfrak F_c(S_\\mu)$, $\\mathfrak{LF}_c(S_\\mu)$)",
    "symbol", None, "high",
    fx(r"(resp. $\mathfrak D_c(S_\mu)$,¶$\mathfrak F_c(S_\mu)$, $\mathfrak{LF}_c(S_\mu)$)",
       r"(resp. $\mathfrak{Oc}(S_\mu)$,¶$\mathfrak{Fc}(S_\mu)$, $\mathfrak{LFc}(S_\mu)$)"),
    "Fraktur O + baseline Fraktur c.")
add(15, "(8.3.9), '... et que u_lambda^{-1} applique C(S_lambda) (resp. ...)'",
    "(resp. \U0001D512\U0001D520(S_\u03bb), \U0001D509\U0001D520(S_\u03bb), \U0001D50F\U0001D509\U0001D520(S_\u03bb))",
    "(resp.\\n$\\mathfrak D_c(S_\\lambda)$, $\\mathfrak F_c(S_\\lambda)$,\\n$\\mathfrak{LF}_c(S_\\lambda)$)",
    "symbol", None, "high",
    fx(r"(resp.¶$\mathfrak D_c(S_\lambda)$, $\mathfrak F_c(S_\lambda)$,¶$\mathfrak{LF}_c(S_\lambda)$)",
       r"(resp.¶$\mathfrak{Oc}(S_\lambda)$, $\mathfrak{Fc}(S_\lambda)$,¶$\mathfrak{LFc}(S_\lambda)$)"),
    "Fraktur O + baseline Fraktur c.")
add(15, "(8.3.9), '... dans C(S) (resp. ...). On a donc par'",
    "(resp. \U0001D512\U0001D520(S), \U0001D509\U0001D520(S), \U0001D50F\U0001D509\U0001D520(S))",
    "(resp.\\n$\\mathfrak D_c(S)$, $\\mathfrak F_c(S)$, $\\mathfrak{LF}_c(S)$)",
    "symbol", None, "high",
    fx(r"(resp.¶$\mathfrak D_c(S)$, $\mathfrak F_c(S)$, $\mathfrak{LF}_c(S)$)",
       r"(resp.¶$\mathfrak{Oc}(S)$, $\mathfrak{Fc}(S)$, $\mathfrak{LFc}(S)$)"),
    "Fraktur O + baseline Fraktur c.")
add(15, "display (8.3.9.3)",
    "lim\u2192 \U0001D512\U0001D520(S_\u03bb) \u2192 \U0001D512\U0001D520(S)",
    "\\varinjlim\\mathfrak D_c(S_\\lambda)&\\longrightarrow\\mathfrak D_c(S)",
    "symbol", None, "high",
    fx(r"\varinjlim\mathfrak D_c(S_\lambda)&\longrightarrow\mathfrak D_c(S)",
       r"\varinjlim\mathfrak{Oc}(S_\lambda)&\longrightarrow\mathfrak{Oc}(S)"),
    "Fraktur O + baseline Fraktur c.")
add(15, "display (8.3.9.4)",
    "lim\u2192 \U0001D509\U0001D520(S_\u03bb) \u2192 \U0001D509\U0001D520(S)",
    "\\varinjlim\\mathfrak F_c(S_\\lambda)&\\longrightarrow\\mathfrak F_c(S)",
    "symbol", None, "high",
    fx(r"\varinjlim\mathfrak F_c(S_\lambda)&\longrightarrow\mathfrak F_c(S)",
       r"\varinjlim\mathfrak{Fc}(S_\lambda)&\longrightarrow\mathfrak{Fc}(S)"),
    "Baseline Fraktur c, not a subscript c.")
add(15, "display (8.3.9.5)",
    "lim\u2192 \U0001D50F\U0001D509\U0001D520(S_\u03bb) \u2192 \U0001D50F\U0001D509\U0001D520(S).",
    "\\varinjlim\\mathfrak{LF}_c(S_\\lambda)&\\longrightarrow\\mathfrak{LF}_c(S).",
    "symbol", None, "high",
    fx(r"\varinjlim\mathfrak{LF}_c(S_\lambda)&\longrightarrow\mathfrak{LF}_c(S)",
       r"\varinjlim\mathfrak{LFc}(S_\lambda)&\longrightarrow\mathfrak{LFc}(S)"),
    "Baseline Fraktur c, not a subscript c.")
add(15, "'où f parcourt A—{0}'",
    "A\u2014{0} (long dash)", "$A-\\{0\\}$",
    "convention", 7, "high",
    fx(r"$A-\{0\}$", r"$A\setmin\{0\}$"),
    "Set difference.")
add(15, "after display (8.3.9.1): 'En outre, il résulte de (1.8.2)'",
    "'En outre' starts a new indented paragraph after the display",
    "no blank line after \\end{equation}: the text continues the paragraph without indent",
    "other", None, "high",
    fx(r"\end{equation}¶En outre, il résulte", r"\end{equation}¶¶En outre, il résulte"),
    "Paragraph break after a display (GLOBAL_ISSUES item 47 pattern).")

# ---------------- page 16 ----------------
add(16, "after (8.3.10.1): 'en remplaçant P par C, Oc, Fc ou LFc'",
    "\U0001D512\U0001D520, \U0001D509\U0001D520 ou \U0001D50F\U0001D509\U0001D520",
    "$\\mathfrak D_c$, $\\mathfrak F_c$ ou\\n$\\mathfrak{LF}_c$",
    "symbol", None, "high",
    fx(r"$\mathfrak D_c$, $\mathfrak F_c$ ou¶$\mathfrak{LF}_c$", r"$\mathfrak{Oc}$, $\mathfrak{Fc}$ ou¶$\mathfrak{LFc}$"),
    "Fraktur O + baseline Fraktur c, as on p. 15.")
add(16, "Théorème (8.3.11): 'les applications canoniques (8.3.9.2), (8.3.9.3), (8.3.9.4) et (8.3.9.5)'",
    "the four references upright inside the italic statement ('et' italic)",
    "references italic (theorem environment)",
    "convention", 6, "high",
    fx(r"(8.3.9.2), (8.3.9.3),¶(8.3.9.4) et (8.3.9.5)", r"\textup{(8.3.9.2), (8.3.9.3),¶(8.3.9.4)} et \textup{(8.3.9.5)}"),
    "")
add(16, "Théorème (8.3.11): 'sont bijectives'",
    "'bijectives' italic like the rest of the statement (no change of face)",
    "\\emph{bijectives} inside the italic theorem prints upright",
    "convention", 6, "high",
    fx(r"sont \emph{bijectives}", r"sont bijectives"),
    "Drop \\emph inside the italic environment.")
add(16, "proof of (8.3.11): 'Z est donc quasi-compacte (0_III, 9.1.4)'",
    "quasi-compacte", "quasi-compact",
    "word", None, "high",
    fx(r"$Z$ est donc quasi-compact", r"$Z$ est donc quasi-compacte"),
    "Feminine ending (une partie Z) in the print.")
add(16, "proof of (8.3.11): (0_III, 9.1.4)",
    "bold 0", "$(0_{\\mathrm{III}},9.1.4)$",
    "convention", 2, "high",
    fx(r"$(0_{\mathrm{III}},9.1.4)$", r"$(\mathbf{0}_{\mathrm{III}},9.1.4)$"), "")
add(16, "proof of (8.3.11): (0_III, 9.1.8)",
    "bold 0", "$(0_{\\mathrm{III}},9.1.8)$",
    "convention", 2, "high",
    fx(r"$(0_{\mathrm{III}},9.1.8)$", r"$(\mathbf{0}_{\mathrm{III}},9.1.8)$"), "")
add(16, "proof of (8.3.11): 'un ensemble fermé constructible Z_mu dans U_mu'",
    "'dans' italic", "'dans' roman",
    "italics", None, "high",
    fx(r"$Z_\mu$ dans $U_\mu$", r"$Z_\mu$ \emph{dans} $U_\mu$"), "")

# ---------------- page 17 ----------------
add(17, "end of Corollaire (8.3.12): 'ouverte (resp. fermée, resp. localement fermée)'",
    "'(resp.' and 'resp.' upright inside the italic statement",
    "italic (corollary environment)",
    "convention", 6, "high",
    fx(r"ouverte (resp. fermée, resp. localement fermée)",
       r"ouverte \textup{(resp.} fermée, \textup{resp.} localement fermée)"),
    "")
add(17, "proof of (8.3.12): (0_III, 9.1.8)",
    "bold 0", "$(0_{\\mathrm{III}},9.1.8)$",
    "convention", 2, "high",
    fx(r"$(0_{\mathrm{III}},9.1.8)$", r"$(\mathbf{0}_{\mathrm{III}},9.1.8)$"), "")
add(17, "title of 8.4",
    "'... pour les limites projectives de préschémas.' (final full stop)",
    "no full stop",
    "punctuation", None, "high",
    fx(r"projectives de préschémas}", r"projectives de préschémas.}"),
    "No ega4-8 \\subsection title has the printed stop (GLOBAL_ISSUES items 43/58).")
add(17, "Proposition (8.4.1), label (i)",
    "(i) upright", "\\item[(i)] italic in the italic statement",
    "convention", 6, "high",
    fx(r"\item[(i)]", r"\item[\textup{(i)}]"), "GLOBAL_ISSUES item 16.")
add(17, "Proposition (8.4.1), label (ii)",
    "(ii) upright", "\\item[(ii)] italic in the italic statement",
    "convention", 6, "high",
    fx(r"\item[(ii)]", r"\item[\textup{(ii)}]"), "GLOBAL_ISSUES item 16.")
add(17, "Proposition (8.4.2): 'et que l'une des deux conditions'",
    "'l'une' set roman (emphasis) inside the italic statement",
    "'l'une' italic, no emphasis",
    "italics", None, "high",
    fx(r"et que l'une des deux", r"et que \emph{l'une} des deux"),
    "In (8.4.3) 'l'une' is italic; here it is clearly roman.")

# ---------------- page 18 ----------------
add(18, "Proposition (8.4.2), label (i)",
    "(i) upright", "\\item[(i)] italic in the italic statement",
    "convention", 6, "high",
    fx(r"\item[(i)]", r"\item[\textup{(i)}]"), "")
add(18, "Proposition (8.4.2), label (ii)",
    "(ii) upright", "\\item[(ii)] italic in the italic statement",
    "convention", 6, "high",
    fx(r"\item[(ii)]", r"\item[\textup{(ii)}]"), "")
add(18, "Proposition (8.4.2) (i): 'l'application Y_i ~> closure(u_mu(Y_i))'",
    "wavy arrow (squiggle)", "\\mapsto",
    "symbol", None, "high",
    fx(r"$Y_i\mapsto\overline{u_\mu(Y_i)}$", r"$Y_i\leadsto\overline{u_\mu(Y_i)}$"),
    "GLOBAL_ISSUES item 33 (wavy arrows).")
add(18, "Proposition (8.4.2) (ii): 'l'application C_j ~> closure(u_mu(C_j))'",
    "wavy arrow (squiggle)", "\\mapsto",
    "symbol", None, "high",
    fx(r"$C_j\mapsto\overline{u_\mu(C_j)}$", r"$C_j\leadsto\overline{u_\mu(C_j)}$"), "")
add(18, "Proposition (8.4.2): 'Sous ces conditions, il existe un lambda tel que'",
    "new indented paragraph after the items a), b)",
    "\\end{enumerate} directly followed by the text: no paragraph indent",
    "other", None, "medium",
    fx(r"\end{enumerate}¶Sous ces conditions", r"\end{enumerate}¶¶Sous ces conditions"),
    "Paragraph indent only.")
add(18, "Lemme (8.4.2.1): 'Sous la condition a) ou b) de (8.4.2), il existe'",
    "(8.4.2) upright inside the italic statement",
    "italic (lemma environment)",
    "convention", 6, "high",
    fx(r"de (8.4.2), il existe", r"de \textup{(8.4.2)}, il existe"), "")
add(18, "proof of (8.4.2.1), case b): 'on ait Z_mu = ... = S_mu'",
    "Z_\u03bc=u_{\u03bb\u03bc}^{-1}(Z_\u03bb)=S_\u03bc",
    "$Z_\\mu=u_{\\alpha\\mu}^{-1}(Z_\\alpha)=S_\\mu$",
    "formula", None, "high",
    fx(r"$Z_\mu=u_{\alpha\mu}^{-1}(Z_\alpha)=S_\mu$", r"$Z_\mu=u_{\lambda\mu}^{-1}(Z_\lambda)=S_\mu$"),
    "Not a misprint: with Z_lambda = u_{alpha lambda}^{-1}(Z_alpha) = S_lambda from (8.3.5), the printed equality holds; "
    "the TeX substituted an equivalent formula. Not in Errata Liste 3.")
add(18, "'on peut supposer que pour tout lambda, u_lambda est un morphisme dominant.'",
    "'dominant' italic", "'dominant' roman",
    "italics", None, "high",
    fx(r"est un morphisme dominant.", r"est un morphisme \emph{dominant}."), "")
add(18, "proof (i): Y_i = closure(U_i) (0_I, 2.1.6)",
    "bold 0", "$(0_{\\mathrm I},2.1.6)$",
    "convention", 2, "high",
    fx(r"$(0_{\mathrm I},2.1.6)$", r"$(\mathbf{0}_{\mathrm I},2.1.6)$"), "")
add(18, "proof (i): composantes irréductibles de S_mu (0_I, 2.1.7)",
    "bold 0", "$(0_{\\mathrm I},2.1.7)$",
    "convention", 2, "high",
    fx(r"$(0_{\mathrm I},2.1.7)$", r"$(\mathbf{0}_{\mathrm I},2.1.7)$"), "")

# ---------------- page 19 ----------------
add(19, "Corollaire (8.4.3): 'l'une des conditions a), b) de (8.4.2),'",
    "(8.4.2) upright inside the italic statement",
    "italic (corollary environment)",
    "convention", 6, "high",
    fx(r"\emph{b)} de (8.4.2),", r"\emph{b)} de \textup{(8.4.2)},"), "")
add(19, "Corollaire (8.4.5): 'géométriquement connexe (4.5.2), il faut'",
    "(4.5.2) upright inside the italic statement",
    "italic (corollary environment)",
    "convention", 6, "high",
    fx(r"connexe (4.5.2), il faut", r"connexe \textup{(4.5.2)}, il faut"), "")
add(19, "heading of (8.4.6)",
    "Remarques (8.4.6). \u2014", "\\begin{remark} prints 'Remarque (8.4.6). ---'",
    "word", None, "high",
    fx(r"\begin{remark}[8.4.6]", r"\begin{remarks}[8.4.6]"),
    "Apply together with the \\end{remark} -> \\end{remarks} finding (same environment).")
add(19, "end of (8.4.6)",
    "(plural remarks)", "\\end{remark}",
    "word", None, "high",
    fx(r"\end{enumerate}¶\end{remark}", r"\end{enumerate}¶\end{remarks}"),
    "Apply together with \\begin{remark}[8.4.6] -> \\begin{remarks}[8.4.6].")
add(19, "Remarques (8.4.6) (ii): 'l'homomorphisme (x,y) ~> (j(y),y)'",
    "wavy arrow (squiggle)", "\\mapsto",
    "symbol", None, "high",
    fx(r"$(x,y)\mapsto(j(y),y)$", r"$(x,y)\leadsto(j(y),y)$"), "")
add(19, "title of 8.5",
    "'... sur une limite projective de préschémas.' (final full stop)",
    "no full stop",
    "punctuation", None, "high",
    fx(r"projective de préschémas}", r"projective de préschémas.}"), "")
add(19, "page end: blank line after display (8.5.1.1)",
    "p. 20 begins 'Nous poserons alors' flush left: the paragraph continues after the display",
    "blank line after \\end{equation} (before \\oldpage[IV-3]{20}) starts a new indented paragraph",
    "marker", None, "high",
    fx(r"\label{IV.8.5.1.1-fr}¶\end{equation}¶¶", r"\label{IV.8.5.1.1-fr}¶\end{equation}¶"),
    "The blank line is the last line of page_019.tex; the p. 20 checker may report the same.")

# ---------------- checks ----------------
src = SRC.read_text(encoding="utf-8")
bad = 0
for d in F:
    page_txt = (RUN / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    old = d["fix"]["old"]
    if d.pop("_cross", False):
        n_src = src.count(old)
        n_page = page_txt.count(old)
        print(f"p{d['page']} CROSS: source count={n_src}, page count={n_page}")
        if n_src != 1:
            bad += 1
    else:
        n = page_txt.count(old)
        if n != 1:
            bad += 1
            print(f"p{d['page']} BAD count={n}: {old!r}")
print("findings:", len(F), "bad:", bad)
# overlap check per page
for p in sorted({d["page"] for d in F}):
    t = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    spans = []
    for d in F:
        if d["page"] != p:
            continue
        i = t.find(d["fix"]["old"])
        if i >= 0:
            spans.append((i, i + len(d["fix"]["old"]), d["where"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            print("OVERLAP p", p, a[2], "|", b[2])
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0, 0])
    if d["kind"] == "convention":
        c[1] += 1
    elif d["kind"] == "misprint_in_print":
        c[2] += 1
    else:
        c[0] += 1
print(counts)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", OUT)
