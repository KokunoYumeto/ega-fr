import json, os, sys

RUN = r"user\Documents\ega_scan_check_20261101\run_0IV1"
OUT = os.path.join(RUN, "findings_111_115.json")
NL = "\u00b6"  # pilcrow stands for a line break inside raw strings


def t(s):
    return s.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": t(old), "new": t(new)},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


DOT = "Baseline period in the print (crops at 3x-6x on pp. 111-114), as the earlier p.-dot fixes (e.g. 0_I p. 57 f.m, III p. 177 a.v)."
SETMIN = "Long dash used for a subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision (not defined in the EGA_IV1_FR.tex preamble)."

# ---------------- page 111 ----------------
add(111, "Définition (19.8.4), first sentence: 'c'est-à-dire (19.8.1) si :'",
    "(19.8.1) upright inside the italic statement",
    "(19.8.1) set italic by the definition environment",
    "convention", 6, "high",
    r"c'est-à-dire (19.8.1) si~:", r"c'est-à-dire \textup{(19.8.1)} si~:")
add(111, "Définition (19.8.4), condition 2°: the parenthesis '(ce qui revient aussi à dire ... prop. 4))'",
    "whole parenthesis roman, only 'Alg. comm.' italic",
    "parenthesis italic (definition environment), 'Alg. comm.' upright through \\emph",
    "convention", 6, "high",
    r"(ce qui revient aussi à¶  dire que $A$ est un $\widehat P$-module plat (Bourbaki, \emph{Alg. comm.},¶  chap.~III, §~5, n\textsuperscript{o}~4, prop.~4))",
    r"\textup{(ce qui revient aussi à¶  dire que $A$ est un $\widehat P$-module plat (Bourbaki, \emph{Alg. comm.},¶  chap.~III, §~5, n\textsuperscript{o}~4, prop.~4))}",
    "Inside \\textup the existing \\emph{Alg. comm.} comes out italic, as printed.")
add(111, "Définition (19.8.4), condition 3°: '(nécessairement séparable sur le corps résiduel de P, ce corps étant premier)'",
    "parenthesis roman",
    "parenthesis italic (definition environment)",
    "convention", 6, "high",
    r"(nécessairement séparable sur le¶  corps résiduel de $P$, ce corps étant premier)",
    r"\textup{(nécessairement séparable sur le¶  corps résiduel de $P$, ce corps étant premier)}")
add(111, "paragraph after (19.8.4): 'la condition 3° signifie que pA est l'idéal maximal m de A'",
    "l'*idéal maximal* (italic; l' upright)",
    "idéal maximal upright",
    "italics", None, "high",
    r"est l'idéal maximal $\mathfrak m$", r"est l'\emph{idéal maximal} $\mathfrak m$")
add(111, "paragraph after (19.8.4): 'et par suite un anneau de valuation discrète, complet en vertu de 1°'",
    "*anneau de valuation discrète*, *complet* (both italic)",
    "both upright",
    "italics", None, "high",
    r"par suite un anneau¶de valuation discrète, complet en vertu",
    r"par suite un \emph{anneau¶de valuation discrète}, \emph{complet} en vertu")
add(111, "Proposition (19.8.5): 'engendré par p.1 (1 étant l'unité de l'anneau)'",
    "p.1 with a baseline period",
    "p\\cdot1 (centred dot)",
    "symbol", None, "high",
    r"engendré par $p\cdot1$ ($1$", r"engendré par $p.1$ ($1$", DOT)
add(111, "after (19.8.5): 'dans le second cas, p.1≠0 puisque'",
    "p.1 (baseline period)", "p\\cdot1",
    "symbol", None, "high",
    r"$p\cdot1\neq0$ puisque", r"$p.1\neq0$ puisque")
add(111, "after (19.8.5): 'donc on peut identifier p.1 à l'entier p'",
    "p.1 (baseline period)", "p\\cdot1",
    "symbol", None, "high",
    r"identifier $p\cdot1$ à", r"identifier $p.1$ à")
add(111, "after (19.8.5): 'et on identifie p.1 à l'élément p de Z_p'",
    "p.1 (baseline period)", "p\\cdot1",
    "symbol", None, "high",
    r"identifie $p\cdot1$ à", r"identifie $p.1$ à")
add(111, "Théorème (19.8.6), label (i)",
    "(i) upright", "\\item[(i)] italic inside the theorem environment",
    "convention", 6, "high",
    r"\item[(i)] Soient $W$", r"\item[\textup{(i)}] Soient $W$", "GLOBAL_ISSUES 16.")
add(111, "Théorème (19.8.6) (i): 'se factorise en W -v-> C -> C/J où v est un homomorphisme local'",
    "C/𝔍 où v (no comma; crop at 1.5x)",
    "C/\\mathfrak J$, où (comma)",
    "punctuation", None, "high",
    r"$W\xrightarrow{v}C\to C/\mathfrak J$, où", r"$W\xrightarrow{v}C\to C/\mathfrak J$ où")
add(111, "Théorème (19.8.6), label (ii)",
    "(ii) upright", "\\item[(ii)] italic inside the theorem environment",
    "convention", 6, "high",
    r"\item[(ii)] Soit $K$", r"\item[\textup{(ii)}] Soit $K$", "GLOBAL_ISSUES 16.")
add(111, "Remarques (19.8.7) (ii), first sentence: 'n'est pas nécessairement déterminé de façon unique par u, comme'",
    "*n'est pas nécessairement déterminé de façon unique* par u ('par' roman; crop)",
    "\\emph{... de façon unique par $u$} (emphasis includes 'par u')",
    "italics", None, "high",
    r"de façon unique par $u$}, comme", r"de façon unique} par $u$, comme",
    "Judged with the remark body as roman (document-wide remark item): only the emphasis scope changes.")
add(111, "Remarques (19.8.7) (ii), second sentence: 'n'est pas nécessairement déterminé de façon unique par u (cf. (21.5.5))'",
    "*... de façon unique* par u ('par' roman; crop)",
    "\\emph{... de façon unique par $u$}",
    "italics", None, "high",
    r"de façon unique par $u$}¶  (cf.", r"de façon unique} par $u$¶  (cf.")

# ---------------- page 112 ----------------
add(112, "Théorème (19.8.8), label (i)",
    "(i) upright", "\\item[(i)] italic inside the theorem environment",
    "convention", 6, "high",
    r"\item[(i)] Il existe", r"\item[\textup{(i)}] Il existe", "GLOBAL_ISSUES 16.")
add(112, "Théorème (19.8.8) (i): 'anneau local régulier complet (17.3.8))'",
    "(17.3.8) upright in the italic statement",
    "(17.3.8) italic",
    "convention", 6, "high",
    r"régulier complet (17.3.8))", r"régulier complet \textup{(17.3.8)})")
add(112, "Théorème (19.8.8), label (ii)",
    "(ii) upright", "\\item[(ii)] italic inside the theorem environment",
    "convention", 6, "high",
    r"\item[(ii)] Supposons", r"\item[\textup{(ii)}] Supposons", "GLOBAL_ISSUES 16.")
add(112, "Théorème (19.8.8) (ii): 'anneau local régulier et complet (17.3.8))'",
    "(17.3.8) upright in the italic statement",
    "(17.3.8) italic",
    "convention", 6, "high",
    r"et complet (17.3.8))", r"et complet \textup{(17.3.8)})")
add(112, "proof of (19.8.8), part (ii): 'L'élément p.1 de A (identifié à p)'",
    "p.1 (baseline period; crop at 3x)", "p\\cdot1",
    "symbol", None, "high",
    r"L'élément $p\cdot1$ de $A$", r"L'élément $p.1$ de $A$")
add(112, "proof of (19.8.8), part (ii): 'il existe une famille (z_i) qui, avec p, forme un système de paramètres'",
    "qui, *avec p*, forme (avec italic; crop at 2x)",
    "avec upright",
    "italics", None, "high",
    r"qui, avec $p$, forme", r"qui, \emph{avec $p$}, forme")
add(112, "proof of (19.8.8), part (ii): 'w(T_i)=z_i pour 1≤i≤m—1. Dans les deux cas'",
    "m—1 with the long dash (crop at 4x); the subscripts (z_i)_{1≤i≤m-1} and T_{m-1} have a short minus",
    "m-1",
    "convention", 7, "high",
    r"i\leq m-1$. Dans", r"i\leq m\setmin 1$. Dans", SETMIN)
add(112, "proof of (19.8.8), part (ii): 'A est un B-module quasi-fini (0_I, 7.4.4)'",
    "*quasi-fini* italic",
    "quasi-fini upright",
    "italics", None, "high",
    r"$B$-module quasi-fini", r"$B$-module \emph{quasi-fini}")
add(112, "proof of (19.8.8), part (ii): 'donc un A-module de type fini puisque B est complet'",
    "*de type fini* italic",
    "de type fini upright",
    "italics", None, "high",
    r"$A$-module de type fini puisque", r"$A$-module \emph{de type fini} puisque",
    "Listed before the misprint finding on the same words ('A-module'), which needs no diplomatic edit.")
add(112, "proof of (19.8.8), part (ii): 'donc un A-module de type fini puisque B est complet et A séparé'",
    "A-module (crop): the print says A-module",
    "$A$-module (keeps the printed reading)",
    "misprint_in_print", None, "high",
    None, None,
    "The TeX keeps the printed reading. The argument shows that A is a B-module of finite type (A quasi-finite over B, B complete, A separated for the n-preadic topology, 0_I 7.4.1), which gives 3° A est une B-algèbre finie; 'A-module de type fini' is trivially true and is a misprint for 'B-module'.",
    corrected=r"donc un $B$-module de type fini")
add(112, "end of p. 112 / start of p. 113: 'D'autre part, | dans les deux cas, on a dim(B)=dim(A)=m'",
    "one sentence running over the page break (no paragraph break)",
    "blank lines before and after \\oldpage{113} make a paragraph break",
    "other", None, "high",
    r"D'autre part,¶¶", r"D'autre part,¶",
    "Spurious paragraph break at a page break inside a sentence (GLOBAL_ISSUES 20). Apply together with the p. 113 entry that removes the blank line after \\oldpage{113}.")

# ---------------- page 113 ----------------
add(113, "start of p. 113 (continuation of the sentence 'D'autre part,')",
    "no paragraph break",
    "blank line after \\oldpage{113}",
    "other", None, "high",
    r"\oldpage[0\textsubscript{IV-1}]{113}¶¶dans les deux cas", r"\oldpage[0\textsubscript{IV-1}]{113}¶dans les deux cas",
    "Apply together with the p. 112 entry 'D'autre part,\\n\\n' (blank line before the marker).")
add(113, "proof of (19.8.8), end: 'p et les T_i (1≤i≤m—1) forment une suite B-régulière'",
    "m—1 with the long dash (crop at 4x)",
    "m-1",
    "convention", 7, "high",
    r"i\leq m-1$)", r"i\leq m\setmin 1$)", SETMIN)
add(113, "proof of (19.8.8), last sentence: 'on tire finalement de (16.3.10) que w est injectif'",
    "*injectif* italic (crop)",
    "injectif upright",
    "italics", None, "high",
    r"que $w$ est injectif, ce qui", r"que $w$ est \emph{injectif}, ce qui")
add(113, "Corollaire (19.8.9): 'dans la conclusion de (19.8.8, (ii))'",
    "(19.8.8, (ii)) upright in the italic statement",
    "italic",
    "convention", 6, "high",
    r"conclusion de (19.8.8, (ii))", r"conclusion de \textup{(19.8.8, (ii))}")
add(113, "proof of (19.8.10), 2nd paragraph: 'et que p.1≠0 dans A (19.6.3)'",
    "p.1 (baseline period; crop at 2x)", "p\\cdot1",
    "symbol", None, "high",
    r"$p\cdot1\neq0$ dans $A$", r"$p.1\neq0$ dans $A$")
add(113, "proof of (19.8.10), 2nd paragraph: 'donc p.1 est un élément de m'",
    "p.1 (baseline period)", "p\\cdot1",
    "symbol", None, "high",
    r"$p\cdot1$ est un élément", r"$p.1$ est un élément")
add(113, "proof of (19.8.10), 2nd paragraph: 'il y a par suite n—1 autres éléments x_i'",
    "n—1 with the long dash (crop at 3x)",
    "n-1",
    "convention", 7, "high",
    r"$n-1$ autres", r"$n\setmin 1$ autres", SETMIN)
add(113, "proof of (19.8.10), 2nd paragraph: 'formant avec p.1 une base de m sur K'",
    "p.1 (baseline period)", "p\\cdot1",
    "symbol", None, "high",
    r"formant avec $p\cdot1$ une", r"formant avec $p.1$ une")
add(113, "proof of (19.8.10), 2nd paragraph: 'n=pB+BT_2+...+BT_n'",
    "BT_2+ . . . +BT_n, dots on the baseline (crop at 2x)",
    "BT_2+\\cdots+BT_n (centred dots)",
    "symbol", None, "high",
    r"BT_2+\cdots+BT_n", r"BT_2+\ldots+BT_n", "As GLOBAL_ISSUES item 22 (\\cdots for the print's baseline dots).")
add(113, "Proposition (19.8.11): 'il faut et il suffit que m soit engendré par p.1, où p est'",
    "p.1 (baseline period)", "p\\cdot1",
    "symbol", None, "high",
    r"engendré par $p\cdot1$, où", r"engendré par $p.1$, où")
add(113, "end of p. 113 / start of p. 114: 'on voit que l'image | par u de l'élément p.1'",
    "one sentence running over the page break (no paragraph break)",
    "blank lines before and after \\oldpage{114} make a paragraph break",
    "other", None, "high",
    r"on voit que¶l'image¶¶", r"on voit que¶l'image¶",
    "Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with the p. 114 entry that removes the blank line after \\oldpage{114}.")

# ---------------- page 114 ----------------
add(114, "start of p. 114 (continuation of 'on voit que l'image')",
    "no paragraph break",
    "blank line after \\oldpage{114}",
    "other", None, "high",
    r"\oldpage[0\textsubscript{IV-1}]{114}¶¶par $u$", r"\oldpage[0\textsubscript{IV-1}]{114}¶par $u$",
    "Apply together with the p. 113 entry 'on voit que\\nl'image\\n\\n' (blank line before the marker).")
add(114, "proof of (19.8.11): 'par u de l'élément p.1 de W est l'élément ...'",
    "p.1 (baseline period; crop at 2x)", "p\\cdot1",
    "symbol", None, "high",
    r"l'élément $p\cdot1$ de $W$ est", r"l'élément $p.1$ de $W$ est")
add(114, "proof of (19.8.11): '... est l'élément p.1 de A; comme'",
    "p.1 (baseline period)", "p\\cdot1",
    "symbol", None, "high",
    r"l'élément $p\cdot1$ de $A$~;", r"l'élément $p.1$ de $A$~;")
add(114, "proof of (19.8.11): 'comme l'élément p.1 de W engendre l'idéal maximal'",
    "p.1 (baseline period)", "p\\cdot1",
    "symbol", None, "high",
    r"$p\cdot1$ de $W$ engendre", r"$p.1$ de $W$ engendre")
add(114, "proof of (19.8.11): 'gr(u) : gr(W) -> gr(A) est surjectif'",
    "*surjectif* italic (crop)",
    "surjectif upright",
    "italics", None, "high",
    r"est surjectif, et par suite", r"est \emph{surjectif}, et par suite")
add(114, "heading 19.9: 'Algèbres relativement formellement lisses.'",
    "final full stop",
    "no full stop",
    "punctuation", None, "high",
    r"\subsection{Algèbres relativement formellement lisses}", r"\subsection{Algèbres relativement formellement lisses.}",
    "GLOBAL_ISSUES 43/58 (subsection titles without the printed full stop).")
add(114, "Définition (19.9.1): 'où u est un Λ-homomorphisme continu'",
    "Λ-homomorphisme roman, continu italic (crop at 1.5x)",
    "all italic",
    "convention", 6, "high",
    r"un $\Lambda$-homomorphisme", r"un \textup{$\Lambda$-homomorphisme}",
    "The definition sets the contrasting words Λ-homomorphisme / A-homomorphisme in roman; the same clause in (19.9.5) and (19.9.7) is printed italic throughout.")
add(114, "Définition (19.9.1): 'où v est un A-homomorphisme continu.'",
    "A-homomorphisme roman, continu italic (crop at 1.5x)",
    "all italic",
    "convention", 6, "high",
    r"est un $A$-homomorphisme continu.", r"est un \textup{$A$-homomorphisme} continu.",
    "See the previous entry.")
add(114, "Proposition (19.9.2), label (i)",
    "(i) upright", "\\item[(i)] italic",
    "convention", 6, "high",
    r"\item[(i)] $A$ est", r"\item[\textup{(i)}] $A$ est", "GLOBAL_ISSUES 16.")
add(114, "Proposition (19.9.2), label (ii)",
    "(ii) upright", "\\item[(ii)] italic",
    "convention", 6, "high",
    r"\item[(ii)] Si $B$", r"\item[\textup{(ii)}] Si $B$", "GLOBAL_ISSUES 16.")
add(114, "Proposition (19.9.2), label (iii)",
    "(iii) upright", "\\item[(iii)] italic",
    "convention", 6, "high",
    r"\item[(iii)]", r"\item[\textup{(iii)}]", "GLOBAL_ISSUES 16.")
add(114, "Proposition (19.9.2), label (iv)",
    "(iv) upright", "\\item[(iv)] italic",
    "convention", 6, "high",
    r"\item[(iv)]", r"\item[\textup{(iv)}]", "GLOBAL_ISSUES 16.")
add(114, "Proposition (19.9.2) (iv): 'S (resp. T) une partie multiplicative'",
    "(resp. T) upright (crop)",
    "italic",
    "convention", 6, "high",
    r"$S$ (resp. $T$)", r"$S$ \textup{(resp. $T$)}")
add(114, "Proposition (19.9.2) (iv): 'de A (resp. B) telle que'",
    "(resp. B) upright (crop)",
    "italic",
    "convention", 6, "high",
    r"$A$ (resp. $B$)", r"$A$ \textup{(resp. $B$)}")
add(114, "Proposition (19.9.2), label (v)",
    "(v) upright", "\\item[(v)] italic",
    "convention", 6, "high",
    r"\item[(v)]", r"\item[\textup{(v)}]", "GLOBAL_ISSUES 16.")
for lab in "abcd":
    add(114, "Proposition (19.9.4), label %s)" % lab,
        "%s) upright (crop at 1.5x)" % lab, "\\item[%s)] italic inside the proposition environment" % lab,
        "convention", 6, "high",
        r"\item[%s)]" % lab, r"\item[\textup{%s)}]" % lab,
        "Lettered labels are printed upright in this statement (they are not uniform in the print, GLOBAL_ISSUES 16/22).")

# ---------------- page 115 ----------------
add(115, "Proposition (19.9.8): 'on ait (cf. 18.4.2)'",
    "(cf. 18.4.2) upright in the italic statement (crop)",
    "italic",
    "convention", 6, "high",
    r"(cf.~18.4.2)", r"\textup{(cf.~18.4.2)}")
add(115, "Proposition (19.9.8): 'Exalcotop_{A/Λ}(B, L)=0.'",
    "formula inline, on the line of 'on ait (cf. 18.4.2)' (crop)",
    "displayed with \\[ ... \\]",
    "other", None, "high",
    r"\[¶  \operatorname{Exalcotop}_{A/\Lambda}(B,L)=0.¶\]", r"$\operatorname{Exalcotop}_{A/\Lambda}(B,L)=0$.",
    "Layout only (display vs inline); the formula itself matches. Independent of the (cf.~18.4.2) edit.")
add(115, "proof of (19.9.8): 'l'extension E_λ de B_λ est Λ-triviale'",
    "E_λ, B_λ with lower-case lambda subscripts (crop at 4x)",
    "$E_\\Lambda$ de $B_\\Lambda$ (capital Lambda)",
    "symbol", None, "high",
    r"$E_\Lambda$ de $B_\Lambda$", r"$E_\lambda$ de $B_\lambda$",
    "The notation is that of the proof of (19.4.4) (B_λ = B/R_λ, E_λ), which the TeX of ega0-19-fr.tex writes with \\lambda.")
add(115, "proof of (19.9.8): 'est Λ-triviale; le reste de la démonstration'",
    "Λ-*triviale* (triviale italic)",
    "triviale upright",
    "italics", None, "high",
    r"$\Lambda$-triviale~;", r"$\Lambda$-\emph{triviale}~;")
add(115, "after (19.9.8): 'Lorsque Λ, A et B sont des anneaux discrets'",
    "*discrets* italic",
    "discrets upright",
    "italics", None, "high",
    r"anneaux discrets, le critère", r"anneaux \emph{discrets}, le critère")
add(115, "heading 19.10: 'Algèbres formellement non ramifiées et algèbres formellement étales.'",
    "final full stop",
    "no full stop",
    "punctuation", None, "high",
    r"algèbres formellement¶étales}", r"algèbres formellement¶étales.}",
    "GLOBAL_ISSUES 43/58.")

# ---------------- checks ----------------
pages = {}
for n in (111, 112, 113, 114, 115):
    with open(os.path.join(RUN, "page_%d.tex" % n), encoding="utf-8", newline="") as fh:
        pages[n] = fh.read().replace("\r\n", "\n")

bad = 0
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    c = pages[d["page"]].count(fx["old"])
    if c != 1:
        bad += 1
        print("NOT UNIQUE (%d): p.%d %r" % (c, d["page"], fx["old"]))
    if fx["old"] == fx["new"]:
        bad += 1
        print("NO CHANGE: p.%d %r" % (d["page"], fx["old"]))

# overlapping edits on the same page
for n in pages:
    spans = []
    for d in F:
        if d["page"] == n and d["fix"]:
            i = pages[n].find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["fix"]["old"][:30]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            bad += 1
            print("OVERLAP p.%d: %r / %r" % (n, a[2], b[2]))

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
cnt = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for n in pages:
    print(n, "normal", cnt[(n, "normal")], "convention", cnt[(n, "convention")], "misprint", cnt[(n, "misprint")])
print("total", len(F), "problems", bad)
