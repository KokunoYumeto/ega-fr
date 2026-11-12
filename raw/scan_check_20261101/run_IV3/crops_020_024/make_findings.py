"""Build findings_020_024.json for EGA IV-3 pp. 20-24 and check every fix's old string (exactly once, LF)."""
import json
import pathlib
import sys

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
OUT = RUN / "findings_020_024.json"


def L(*lines):
    return "\n".join(lines)


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


R = []

# ---------------- page 19 (outside pp. 20-24: blank line before the p. 20 marker) ----------------
R.append(F(19, "end of page_019.tex, before \\oldpage[IV-3]{20}: display (8.5.1.1), then 'Nous poserons alors' (first line of p. 20)",
           "'Nous poserons alors' (top of p. 20) starts flush left: it continues the paragraph of the display (8.5.1.1) at the foot of p. 19; no paragraph break",
           "blank line after \\end{equation} of (8.5.1.1), before the p. 20 marker: 'Nous poserons alors' becomes a new indented paragraph",
           "marker", None, "high",
           L(r"\label{IV.8.5.1.1-fr}", r"\end{equation}", "", ""),
           L(r"\label{IV.8.5.1.1-fr}", r"\end{equation}", ""),
           "OUTSIDE pp. 20-24: old lies at the end of page_019.tex (ega4-8-fr.tex, just before \\oldpage[IV-3]{20}); filed under page 19 so that it is found there. The marker itself is in the right place."))

# ---------------- page 20 ----------------
R.append(F(20, "(8.5.1), after 'deux telles familles de O_{S_λ}-Modules.'",
           "'Il est clair que les applications ...' begins a new indented paragraph",
           "same paragraph: '-Modules. Il est clair'", "other", None, "high",
           "-Modules. Il est clair", "-Modules.\n\nIl est clair", "Missing paragraph break."))
R.append(F(20, "(8.5.1): 'les applications f_λ ⇝ u*_{λμ}(f_λ) de Hom ...'",
           "wavy arrow ⇝", "\\mapsto", "symbol", None, "high",
           r"$f_\lambda\mapsto u_{\lambda\mu}^*(f_\lambda)$", r"$f_\lambda\leadsto u_{\lambda\mu}^*(f_\lambda)$",
           "Wavy maps-to arrow (GLOBAL_ISSUES 33), \\leadsto as in the earlier page fixes; enlarged crop."))
R.append(F(20, "(8.5.1): 'et que les applications f_λ ⇝ u*_λ(f_λ) forment'",
           "wavy arrow ⇝", "\\mapsto", "symbol", None, "high",
           r"$f_\lambda\mapsto u_\lambda^*(f_\lambda)$", r"$f_\lambda\leadsto u_\lambda^*(f_\lambda)$",
           "Enlarged crop."))
R.append(F(20, "(8.5.1): 'l'homomorphisme (8.5.1.3) donne donc (0_I, 5.1.1)'",
           "(𝟎_I, 5.1.1): bold 0", r"$(0_{\mathrm I},5.1.1)$", "convention", 2, "high",
           r"$(0_{\mathrm I},5.1.1)$", r"$(\mathbf{0}_{\mathrm I},5.1.1)$", None))
R.append(F(20, "Théorème (8.5.2), label (i)",
           "label (i) upright", "enumerate label=(\\roman*) inside the italic theorem environment: italic",
           "convention", 6, "high",
           L(r"\label{IV.8.5.2-fr}", r"\begin{enumerate}[label=(\roman*)]"),
           L(r"\label{IV.8.5.2-fr}", r"\begin{enumerate}[label=\textup{(\roman*)}]"),
           "One edit of the label option covers (i) and (ii) (next entry). GLOBAL_ISSUES 16."))
R.append(F(20, "Théorème (8.5.2), label (ii)",
           "label (ii) upright", "italic (same enumerate)", "convention", 6, "high", None, None,
           "Included in the previous edit (label=\\textup{(\\roman*)})."))
R.append(F(20, "Théorème (8.5.2) (i): 'quasi-compact (resp. quasi-compact et quasi-séparé)'",
           "'resp.' upright inside the italic statement", "italic", "convention", 6, "high",
           "(resp. quasi-compact et", r"(\textup{resp.} quasi-compact et", None))
R.append(F(20, "Théorème (8.5.2) (i): 'de type fini (resp. de présentation finie) et G_λ'",
           "'resp.' upright inside the italic statement", "italic", "convention", 6, "high",
           "type fini (resp. de présentation finie) et", r"type fini (\textup{resp.} de présentation finie) et", None))
R.append(F(20, "Théorème (8.5.2) (i): 'est injectif (resp. bijectif)'",
           "'resp.' upright inside the italic statement", "italic", "convention", 6, "high",
           L("est", "  injectif (resp."), L("est", r"  injectif (\textup{resp.}"), None))
R.append(F(20, "Lemme (8.5.2.1): 'Si M_0 est de type fini (resp. de présentation finie)'",
           "'resp.' upright inside the italic statement", "italic", "convention", 6, "high",
           "(resp. de présentation finie), l'homomorphisme", r"(\textup{resp.} de présentation finie), l'homomorphisme", None))
R.append(F(20, "Lemme (8.5.2.1), after (8.5.2.2): 'est injectif (resp. bijectif)'",
           "'resp.' upright inside the italic statement", "italic", "convention", 6, "high",
           "est injectif (resp.", r"est injectif (\textup{resp.}", None))
R.append(F(20, "end of p. 20 / top of p. 21: '... isomorphismes canoniques fonctoriels [display] si bien que l'homomorphisme (8.5.2.2)'",
           "'si bien que' (first line of p. 21) is flush left: the sentence continues after the display; no paragraph break",
           "blank line after \\] at the end of page_020.tex, before \\oldpage[IV-3]{21}: paragraph break",
           "marker", None, "high",
           L("(M_0,N)", r"  \]", "", ""), L("(M_0,N)", r"  \]", ""),
           "Mid-sentence page break (GLOBAL_ISSUES 20); the marker itself is in the right place."))

# ---------------- page 21 ----------------
R.append(F(21, "proof of (8.5.2) (i), lemma part: 'l'exactitude à gauche du foncteur M_0 ⇝ Hom_{A_0}(M_0, P)'",
           "wavy arrow ⇝", "\\mapsto", "symbol", None, "high",
           r"$M_0\mapsto\operatorname{Hom}", r"$M_0\leadsto\operatorname{Hom}", "Enlarged crop."))
R.append(F(21, "proof of (8.5.2) (i): 'et que l'on a u*_λ(f_λ^(i)|U_ijλ) = u*_λ(f_λ^(j)|U_ijλ) = f|(V_i∩V_j) par définition'",
           "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
           L(r"\[", r"    u_\lambda^*(f_\lambda^{(i)}|U_{ij\lambda})", r"    =u_\lambda^*(f_\lambda^{(j)}|U_{ij\lambda})",
             r"    =f|(V_i\cap V_j)", r"  \]"),
           L(r"$u_\lambda^*(f_\lambda^{(i)}|U_{ij\lambda})", r"    =u_\lambda^*(f_\lambda^{(j)}|U_{ij\lambda})",
             r"    =f|(V_i\cap V_j)$"),
           "Display vs inline; no connecting word lost."))
R.append(F(21, "proof of (8.5.2) (i): 'u*_λμ(f_λ^(i)|U_ijλ) = u*_λμ(f_λ^(j)|U_ijλ) pour μ≥λ_ij; prenant'",
           "formula and 'pour μ≥λ_ij;' set inline in the running text", "displayed, with \\quad\\text{pour } inside the display",
           "other", None, "high",
           L(r"\[", r"    u_{\lambda\mu}^*(f_\lambda^{(i)}|U_{ij\lambda})", r"    =u_{\lambda\mu}^*(f_\lambda^{(j)}|U_{ij\lambda})",
             r"    \quad\text{pour }\mu\geq\lambda_{ij}~;", r"  \]"),
           L(r"$u_{\lambda\mu}^*(f_\lambda^{(i)}|U_{ij\lambda})", r"    =u_{\lambda\mu}^*(f_\lambda^{(j)}|U_{ij\lambda})$",
             r"    pour $\mu\geq\lambda_{ij}$~;"),
           "Display vs inline."))
R.append(F(21, "proof of (8.5.2) (i): 'de présentation finie (0_I, 5.2.5)'",
           "(𝟎_I, 5.2.5): bold 0", r"$(0_{\mathrm I},5.2.5)$", "convention", 2, "high",
           r"$(0_{\mathrm I},5.2.5)$", r"$(\mathbf{0}_{\mathrm I},5.2.5)$", None))
R.append(F(21, "end of p. 21 / top of p. 22 (proof of (8.5.2.4)): 'on a par suite u*_ν(g_ν∘f_ν) = 1_F | et u*_ν(f_ν∘g_ν) = 1_G'",
           "'et u*_ν(f_ν∘g_ν) = 1_G;' (first line of p. 22) continues the sentence, flush left",
           "blank line at the end of page_021.tex, before \\oldpage[IV-3]{22}: paragraph break mid-sentence",
           "marker", None, "high",
           L(r"$u_\nu^*(g_\nu\circ f_\nu)=1_{\mathcal F}$", "", ""),
           L(r"$u_\nu^*(g_\nu\circ f_\nu)=1_{\mathcal F}$", ""),
           "Mid-sentence page break (GLOBAL_ISSUES 20); the marker itself is in the right place."))

# ---------------- page 22 ----------------
R.append(F(22, "proof of (8.5.2) (ii): 'le cas où S_0 = Spec(A_0) est affine. Alors'",
           "'affine' italic", "upright", "italics", None, "high",
           L("est", "affine. Alors"), L("est", r"\emph{affine}. Alors"), "Enlarged crop."))
R.append(F(22, "proof of (8.5.2) (ii): 'un isomorphisme θ_ij : u*_{λ,λ_ij}(F_i|U_ijλ) ⥲ u*_{λ,λ_ij}(F_j|U_ijλ) tel que'",
           "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
           L(r"\[", r"  \theta_{ij}:u_{\lambda,\lambda_{ij}}^*(\mathcal F_i|U_{ij\lambda})", r"  \xrightarrow{\sim}",
             r"  u_{\lambda,\lambda_{ij}}^*(\mathcal F_j|U_{ij\lambda})", r"\]"),
           L(r"$\theta_{ij}:u_{\lambda,\lambda_{ij}}^*(\mathcal F_i|U_{ij\lambda})", r"  \xrightarrow{\sim}",
             r"  u_{\lambda,\lambda_{ij}}^*(\mathcal F_j|U_{ij\lambda})$"),
           "Display vs inline; no connecting word lost."))
R.append(F(22, "proof of (8.5.2) (ii): 'un isomorphisme θ_ij : F_i|U_ijλ ⥲ F_j|U_ijλ, tels que'",
           "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
           L(r"\[", r"  \theta_{ij}:\mathcal F_i|U_{ij\lambda}", r"  \xrightarrow{\sim}\mathcal F_j|U_{ij\lambda},", r"\]"),
           L(r"$\theta_{ij}:\mathcal F_i|U_{ij\lambda}", r"  \xrightarrow{\sim}\mathcal F_j|U_{ij\lambda}$,"),
           "Display vs inline."))
R.append(F(22, "proof of (8.5.2) (ii): 'on a u*_λ(θ'_ij∘θ'_jk) = u*_λ(θ'_ik). Il y a donc'",
           "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
           L(r"\[", r"  u_\lambda^*(\theta'_{ij}\circ\theta'_{jk})=u_\lambda^*(\theta'_{ik}).", r"\]"),
           r"$u_\lambda^*(\theta'_{ij}\circ\theta'_{jk})=u_\lambda^*(\theta'_{ik})$.",
           "Display vs inline."))
R.append(F(22, "proof of (8.5.2) (ii): 'tel que l'on ait u*_λμ(θ'_ik) = u*_λμ(θ'_ij∘θ'_jk), donc les isomorphismes'",
           "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
           L(r"\[", r"  u_{\lambda\mu}^*(\theta'_{ik})", r"  =u_{\lambda\mu}^*(\theta'_{ij}\circ\theta'_{jk}),", r"\]"),
           L(r"$u_{\lambda\mu}^*(\theta'_{ik})", r"  =u_{\lambda\mu}^*(\theta'_{ij}\circ\theta'_{jk})$,"),
           "Display vs inline."))
R.append(F(22, "proof of (8.5.2) (ii): 'donc les isomorphismes u*_λμ(θ'_ij) : u*_λμ(F_i)|U_ijμ ⥲ u*_λμ(F_j)|U_ijμ vérifient'",
           "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
           L(r"\[", r"  u_{\lambda\mu}^*(\theta'_{ij}):", r"  u_{\lambda\mu}^*(\mathcal F_i)|U_{ij\mu}", r"  \xrightarrow{\sim}",
             r"  u_{\lambda\mu}^*(\mathcal F_j)|U_{ij\mu}", r"\]"),
           L(r"$u_{\lambda\mu}^*(\theta'_{ij}):", r"  u_{\lambda\mu}^*(\mathcal F_i)|U_{ij\mu}", r"  \xrightarrow{\sim}",
             r"  u_{\lambda\mu}^*(\mathcal F_j)|U_{ij\mu}$"),
           "Display vs inline."))
R.append(F(22, "proof of (8.5.2) (ii), end: 'de présentation finie (0_I, 3.3.1)'",
           "(𝟎_I, 3.3.1): bold 0", r"$(0_{\mathrm I},3.3.1)$", "convention", 2, "high",
           r"$(0_{\mathrm I},3.3.1)$", r"$(\mathbf{0}_{\mathrm I},3.3.1)$", None))
R.append(F(22, "heading of (8.5.3)",
           "'Scholie (8.5.3). — Le résultat de (8.5.2) ...' ('Scholie' italic, body roman)",
           "\\begin{env}[8.5.3] prints only '(8.5.3) Le résultat ...': the word 'Scholie' and the dash are missing",
           "missing", None, "high",
           r"\begin{env}[8.5.3]", r"\begin{scholium}[8.5.3]",
           "Edit 1 of 2: apply together with the next entry (\\end{env} -> \\end{scholium}). The IV-3 preamble "
           "(ega4/EGA_IV3_FR.tex) has no scholium environment: add it first, with a roman body as in "
           "BASE/native/EGA_FR.tex (\\newenvironment{scholium}[1][]{\\par\\medskip\\noindent\\textit{Scholie (#1). ---\\ }}{\\par}); "
           "the IV-2 preamble's version has an \\itshape body, but this Scholie is printed roman."))
R.append(F(22, "end of (8.5.3): '... liées aux O_S-Modules quasi-cohérents.'",
           "end of the Scholie", "\\end{env}", "other", None, "high",
           L(r"$\mathcal O_S$-Modules quasi-cohérents.", r"\end{env}"),
           L(r"$\mathcal O_S$-Modules quasi-cohérents.", r"\end{scholium}"),
           "Edit 2 of 2 of the Scholie heading: apply only together with the previous entry."))
R.append(F(22, "Scholie (8.5.3), l. 2: 'la catégorie des O_S-modules quasi-cohérents de présentation finie'",
           "'𝒪_S-modules' with a lower-case m (enlarged crop)",
           "'$\\mathcal O_S$-Modules' (capital M): silently corrected", "misprint_in_print", None, "high",
           r"catégorie des $\mathcal O_S$-Modules", r"catégorie des $\mathcal O_S$-modules",
           "The diplomatic text keeps the printed lower-case m. The sentence is about quasi-coherent sheaves of modules, "
           "which EGA writes O_S-Modules (as in the same sentence: 'des O_{S_λ}-Modules quasi-cohérents').",
           corrected=r"la catégorie des $\mathcal O_S$-Modules"))

# ---------------- page 23 ----------------
R.append(F(23, "Corollaire (8.5.4): 'l'homomorphisme canonique (8.5.1.4) est bijectif'",
           "reference (8.5.1.4) upright inside the italic statement", "italic", "convention", 6, "high",
           "canonique (8.5.1.4) est", r"canonique \textup{(8.5.1.4)} est", "Enlarged crop."))
R.append(F(23, "Proposition (8.5.5): 'localement libre (resp. localement libre de rang n)'",
           "'resp.' upright inside the italic statement", "italic", "convention", 6, "high",
           "soit localement libre (resp.", r"soit localement libre (\textup{resp.}", None))
R.append(F(23, "proof of (8.5.5): 'soit isomorphe à O_S^{ni}|V_i'",
           "exponent 'ni': n and i the same size on one level (enlarged crop); elsewhere the print lowers second-level indices (λ_i, λ_ij)",
           "\\mathcal O_S^{n_i}: silently corrected", "misprint_in_print", None, "medium",
           r"\mathcal O_S^{n_i}", r"\mathcal O_S^{ni}",
           "Correct reading n_i (the rank on V_i). Medium: the flat exponent may be a typesetting simplification rather than an error; "
           "if the edition does not reproduce such flattened indices, drop this entry.",
           corrected=r"\mathcal O_S^{n_i}"))
R.append(F(23, "proof of (8.5.5): 'on est donc ramené au cas où S_0 est affine et F = O_S^n'",
           "'affine' italic", "upright", "italics", None, "high",
           "est affine et", r"est \emph{affine} et", "Enlarged crop."))
R.append(F(23, "Corollaire (8.5.8): 'et les morphismes u_λμ : S_μ→S_λ plats.'",
           "'plats' upright (roman) inside the italic statement (enlarged crop)", "italic", "convention", 6, "high",
           r"S_\lambda$ plats.", r"S_\lambda$ \textup{plats}.", None))
R.append(F(23, "Corollaire (8.5.8), label (i)",
           "label (i) upright", "enumerate label=(\\roman*) inside the italic corollary environment: italic",
           "convention", 6, "high",
           L("Alors~:", r"\begin{enumerate}[label=(\roman*)]"),
           L("Alors~:", r"\begin{enumerate}[label=\textup{(\roman*)}]"),
           "One edit covers (i) here and (ii) on p. 24. Independent of the 'plats' edit above (no overlap)."))
R.append(F(23, "end of p. 23 / top of p. 24, Corollaire (8.5.8) (i): 'Pour que la suite correspondante F→G→H soit | exacte'",
           "'exacte, il faut et il suffit ...' (first line of p. 24) continues the sentence, flush left",
           "blank line at the end of page_023.tex, before \\oldpage[IV-3]{24}: paragraph break mid-sentence",
           "marker", None, "high",
           L(r"\xrightarrow{g}\mathcal H$ soit", "", ""), L(r"\xrightarrow{g}\mathcal H$ soit", ""),
           "Mid-sentence page break (GLOBAL_ISSUES 20); the marker itself is in the right place."))

# ---------------- page 24 ----------------
R.append(F(24, "Corollaire (8.5.8), label (ii)",
           "label (ii) upright", "italic (enumerate opened on p. 23)", "convention", 6, "high", None, None,
           "Covered by the p. 23 edit of the enumerate's label option."))
R.append(F(24, "proof of (8.5.8) (i), l. 6: 'les images réciproques de Im f_λ et Ker g_μ (0_I, 6.7.2)'",
           "'Ker g_μ' (subscript μ; enlarged crop)", "'\\operatorname{Ker}g_\\lambda': silently corrected",
           "misprint_in_print", None, "high",
           r"f_\lambda$ et $\operatorname{Ker}g_\lambda$", r"f_\lambda$ et $\operatorname{Ker}g_\mu$",
           "Authors' errata, EGA IV liste 3, (IV, 8.5.8): 'Ligne 6 de la p. 24, remplacer Ker g_μ à la fin de la ligne par Ker g_λ'. "
           "The fix restores the printed g_μ and changes only the subscript.",
           corrected=r"$\operatorname{Ker}g_\lambda$"))
R.append(F(24, "proof of (8.5.8) (i): '(0_I, 6.7.2). Supposons que la suite'",
           "(𝟎_I, 6.7.2): bold 0", r"$(0_{\mathrm I},6.7.2)$", "convention", 2, "high",
           r"$(0_{\mathrm I},6.7.2)$", r"$(\mathbf{0}_{\mathrm I},6.7.2)$", None))
R.append(F(24, "proof of (8.5.9): 'cet homomorphisme est nécessairement unique'",
           "'unique' italic", "upright", "italics", None, "high",
           "nécessairement unique,", r"nécessairement \emph{unique},", "Enlarged crop."))
R.append(F(24, "proof of (8.5.9): 'la question est locale sur S_λ'",
           "'locale' italic", "upright", "italics", None, "high",
           "est locale sur", r"est \emph{locale} sur", "Enlarged crop."))
R.append(F(24, "proof of (8.5.9): 'supposer S_λ affine, donc quasi-séparé.'",
           "'quasi-séparé' italic ('affine' upright)", "upright", "italics", None, "high",
           L("donc", "quasi-séparé. Il est clair"), L("donc", r"\emph{quasi-séparé}. Il est clair"), "Enlarged crop."))
R.append(F(24, "(8.5.10): 'les Modules quotients de F qui sont de présentation finie.'",
           "'de présentation finie' italic", "upright", "italics", None, "high",
           "qui sont de présentation finie. Si", r"qui sont \emph{de présentation finie}. Si", "Enlarged crop."))
R.append(F(24, "end of p. 24 / top of p. 25: 'et l'on a un diagramme commutatif [diagram (8.5.10.2) at the top of p. 25]'",
           "the sentence runs into the diagram (8.5.10.2), which opens p. 25; no paragraph break",
           "blank line after 'commutatif' at the end of page_024.tex, before \\oldpage[IV-3]{25} and \\[: paragraph break before the display",
           "marker", None, "high",
           L("commutatif", "", ""), L("commutatif", ""),
           "Mid-sentence page break (GLOBAL_ISSUES 20); the p. 25 marker itself is in the right place (checked on page_025_s1.png)."))

# ---------------- checks ----------------
texts = {}
bad = 0
for f in R:
    p = f["page"]
    if p not in texts:
        texts[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    if f["fix"] is None:
        continue
    n = texts[p].count(f["fix"]["old"])
    if n != 1:
        bad += 1
        print("COUNT", n, "page", p, repr(f["fix"]["old"][:80]))
# apply in listed order to confirm no edit destroys a later old string
work = dict(texts)
for f in R:
    if f["fix"] is None:
        continue
    p, old, new = f["page"], f["fix"]["old"], f["fix"]["new"]
    n = work[p].count(old)
    if n != 1:
        bad += 1
        print("SEQ", n, "page", p, repr(old[:80]))
        continue
    work[p] = work[p].replace(old, new)
OUT.write_text(json.dumps(R, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
counts = {}
for f in R:
    c = counts.setdefault(f["page"], {"normal": 0, "convention": 0, "misprint": 0})
    k = "convention" if f["kind"] == "convention" else "misprint" if f["kind"] == "misprint_in_print" else "normal"
    c[k] += 1
print("entries", len(R), "bad", bad)
for p in sorted(counts):
    print(p, counts[p])
sys.exit(1 if bad else 0)
