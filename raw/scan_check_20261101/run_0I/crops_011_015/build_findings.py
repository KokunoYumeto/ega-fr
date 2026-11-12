"""Build findings_011_015.json for EGA I chapter 0, pp. 11-15, and check every fix's "old" string.
usage: python -I build_findings.py RUN_FOLDER SOURCE_TEX OUTFILE"""
import json
import pathlib
import sys

run, source, outfile = (pathlib.Path(a) for a in sys.argv[1:4])
N = "\n"

top_old = (r"\section{Anneaux de fractions}" + N + r"\label{section:0.1-fr}" + N + N
           + r"\setcounter{subsection}{-1}" + N + r"\subsection{Anneaux et algèbres}" + N
           + r"\label{subsection:0.1.0-fr}" + N + N + r"\oldpage[0\textsubscript{I}]{11}" + N)
top_new = (r"\clearpage" + N + r"\oldpage[0\textsubscript{I}]{11}" + N
           + r"\begin{center}" + N + r"{\large CHAPITRE 0\par}" + N + r"\vspace{1.5em}" + N
           + r"{\Large\bfseries PRÉLIMINAIRES\par}" + N + r"\end{center}" + N + N
           + r"\section{Anneaux de fractions}" + N + r"\label{section:0.1-fr}" + N + N
           + r"\setcounter{subsection}{-1}" + N + r"\subsection{Anneaux et algèbres}" + N
           + r"\label{subsection:0.1.0-fr}" + N + N)

head12 = r"\subsection{Modules et anneaux de fractions}" + N + r"\label{subsection:0.1.2-fr}" + N + N

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, outside=False):
    F.append(dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
                  fix=dict(old=old, new=new), note=note))
    F[-1]["_outside"] = outside


add(11, "top of p. 11, before (1.0.1): chapter title, and the position of \\oldpage[0\\textsubscript{I}]{11}",
    "p. 11 opens with the chapter title 'CHAPITRE 0' / 'PRÉLIMINAIRES' (bold), then '§ 1. ANNEAUX DE FRACTIONS' "
    "and '1.0. Anneaux et algèbres.'",
    "no chapter title at all (EGA_FR.tex inputs ega1/intro-fr.tex and then ega1/ega0-1-fr.tex directly); "
    "ega0-1-fr.tex begins with \\section{Anneaux de fractions} and \\subsection{Anneaux et algèbres}, and "
    "\\oldpage[0\\textsubscript{I}]{11} stands only after them (l. 8)",
    "missing", None, "high", top_old, top_new,
    "The 'old' string is ll. 1-8 of ega0-1-fr.tex: text before the file's first marker plus the marker line, so it "
    "is not contained in page_011.tex and must be applied by hand. This single edit adds the chapter title (same "
    "markup as chapter1-frontmatter-fr.tex and ega3-1-fr.tex 'CHAPITRE 0 (suite)') and puts the page-11 marker "
    "before every heading printed on p. 11.", outside=True)

add(12, "end of page_012.tex: heading '1.2. Modules et anneaux de fractions.'",
    "p. 12 ends with '(1.1.2) ... Le radical de A/ℜ(A) est (0).'; the heading '1.2. Modules et anneaux de "
    "fractions.' is the first line of p. 13",
    "\\subsection{Modules et anneaux de fractions} and its \\label stand at the end of page 12, before "
    "\\oldpage[0\\textsubscript{I}]{13}",
    "marker", None, "high", head12, "",
    "Moves the heading (not the marker) so that both edits stay inside their page segments and do not depend on "
    "the order in which they are applied. Apply together with the page-13 finding that re-inserts the heading "
    "after \\oldpage[0\\textsubscript{I}]{13}.")

add(13, "start of p. 13: heading '1.2. Modules et anneaux de fractions.'",
    "the heading opens p. 13",
    "page_013.tex starts with \\oldpage[0\\textsubscript{I}]{13} followed by \\begin{env}[1.2.1]; the heading is "
    "at the end of page 12",
    "marker", None, "high",
    r"\oldpage[0\textsubscript{I}]{13}" + N + r"\begin{env}[1.2.1]",
    r"\oldpage[0\textsubscript{I}]{13}" + N + head12 + r"\begin{env}[1.2.1]",
    "Apply together with the page-12 finding that removes the heading from the end of page 12.")

add(13, "(1.2.1): '2° le complémentaire A—𝔭 d'un idéal premier 𝔭 de A'",
    "A—𝔭 (long dash, set difference)", "$A-\\mathfrak{p}$", "convention", 7, "high",
    r"$A-\mathfrak{p}$ d'un idéal", r"$A\setmin\mathfrak{p}$ d'un idéal",
    "Set difference; the minus signs in s(s_1m_2-s_2m_1) and fT-1 on this page are subtractions.")

add(13, "(1.2.2): 'on appelle application canonique de M dans S^{-1}M'",
    "'application' roman, only 'canonique' italic", "\\emph{application canonique}", "italics", None, "high",
    r"\emph{application canonique}", r"application \emph{canonique}", "Checked on a zoomed crop.")

add(13, "(1.2.2): 'l'application i^S_M : m→m/1 (aussi notée i^S)'",
    "plain arrow: m→m/1", "$i_M^S:m\\mapsto m/1$", "convention", 3, "high",
    r"m\mapsto m/1", r"m\to m/1", "Checked on a zoomed crop.")

add(13, "(1.2.3), second paragraph: 'Lorsque S=A—𝔭, où 𝔭 est un idéal premier de A'",
    "A—𝔭 (long dash, set difference)", "$S=A-\\mathfrak{p}$", "convention", 7, "high",
    r"$S=A-\mathfrak{p}$", r"$S=A\setmin\mathfrak{p}$", "")

add(13, "(1.2.4), display 'u : A → S^{-1}A → B'",
    "the arrow labels i^S_A and u* are printed below the two arrows",
    "u:A\\xrightarrow{i_A^S}S^{-1}A\\xrightarrow{u^*}B (labels above the arrows)", "formula", None, "high",
    r"u:A\xrightarrow{i_A^S}S^{-1}A\xrightarrow{u^*}B", r"u:A\xrightarrow[i_A^S]{}S^{-1}A\xrightarrow[u^*]{}B",
    "Position of the labels only; checked on a zoomed crop. In (1.3.2) and (1.4.1) (pp. 14-15) the print puts "
    "the labels above the arrows, as the TeX does, so this is not a document-wide convention.")

add(14, "(1.2.4), display 'v : M → S^{-1}M → N'",
    "the arrow labels i^S_M and v* are printed below the two arrows",
    "v:M\\xrightarrow{i_M^S}S^{-1}M\\xrightarrow{v^*}N (labels above the arrows)", "formula", None, "high",
    r"v:M\xrightarrow{i_M^S}S^{-1}M\xrightarrow{v^*}N", r"v:M\xrightarrow[i_M^S]{}S^{-1}M\xrightarrow[v^*]{}N",
    "Position of the labels only, as in the u-display of (1.2.4) on p. 13; checked on a zoomed crop.")

add(14, "(1.2.6): 'L'application 𝔭'→(i^S_A)^{-1}(𝔭')'",
    "plain arrow", "$\\mathfrak{p}'\\mapsto(i_A^S)^{-1}(\\mathfrak{p}')$", "convention", 3, "high",
    r"\mathfrak{p}'\mapsto(i_A^S)^{-1}", r"\mathfrak{p}'\to(i_A^S)^{-1}", "Checked on a zoomed crop.")

add(14, "(1.3.2), after the second display: 'En particulier, si u : M→N est injectif ...'",
    "'En particulier' begins a new, indented paragraph (the line after the first display, 'est exacte, il en "
    "est de même de la suite', is flush left)",
    "no paragraph break: 'En particulier' follows \\] directly", "other", None, "high",
    "\\]" + N + "En particulier", "\\]" + N + N + "En particulier",
    "Paragraph break only.")

add(15, "(1.3.3), display 'S^{-1} lim M_α ⥲ lim S^{-1}M_α'",
    "no punctuation after the display", "\\varinjlim S^{-1}M_\\alpha,", "punctuation", None, "high",
    r"\varinjlim S^{-1}M_\alpha,", r"\varinjlim S^{-1}M_\alpha",
    "Extra comma in the TeX; checked on a zoomed crop.")

add(15, "(1.3.5): 'fait correspondre l'homomorphisme m/t→u(m)/st'",
    "plain arrow", "$m/t\\mapsto u(m)/st$", "convention", 3, "high",
    r"m/t\mapsto u(m)/st", r"m/t\to u(m)/st", "Checked on a zoomed crop.")

add(15, "(1.4.1): '; on a i^T_A=ρ^{T,S}_A∘i^S_A. Pour tout A-module M'",
    "the formula is in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    "on a" + N + "\\[" + N + "  i_A^T=\\rho_A^{T,S}\\circ i_A^S." + N + "\\]" + N + "Pour tout",
    "on a $i_A^T=\\rho_A^{T,S}\\circ i_A^S$." + N + "Pour tout",
    "Layout only (display vs inline); the formula itself matches.")

add(15, "(1.4.1): 'et on a encore i^T_M=ρ^{T,S}_M∘i^S_M ; dans l'identification canonique'",
    "the formula is in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    "et on a encore" + N + "\\[" + N + "  i_M^T=\\rho_M^{T,S}\\circ i_M^S;" + N + "\\]" + N + "dans",
    "et on a encore $i_M^T=\\rho_M^{T,S}\\circ i_M^S$;" + N + "dans",
    "Layout only (display vs inline); the formula itself matches.")

# checks: every in-segment 'old' occurs exactly once in its page_NNN.tex (LF) and in the same page segment of the
# release source (as apply_fixes.py locates it); the outside one occurs once in the whole source file
import re
src = source.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[0\\textsubscript\{I\}\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(src)]
seg = {n: src[s:(cuts[i + 1][1] if i + 1 < len(cuts) else len(src))] for i, (n, s) in enumerate(cuts)}
ok = True
for x in F:
    old = x["fix"]["old"]
    page_text = (run / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8")  # universal newlines -> LF
    n_page, n_seg, n_src = page_text.count(old), seg[x["page"]].count(old), src.count(old)
    if x["_outside"]:
        good = n_page == 0 and n_src == 1
    else:
        good = n_page == 1 and n_seg == 1
    ok &= good
    print(f"p.{x['page']} {x['kind']:<11} page:{n_page} segment:{n_seg} file:{n_src} {'ok' if good else 'BAD'}")
for x in F:
    del x["_outside"]
outfile.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("written", outfile, len(F), "findings; all checks", "passed" if ok else "FAILED")
