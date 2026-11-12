"""Build findings_146_150.json and check every fix against the page files."""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = 'user/Documents/ega_scan_check_20261101/run_0IV1/'
OUT = RUN + 'findings_146_150.json'

KNOTE = ("Fraktur K: the same glyph as the 𝔎 of EGA I p. 184 (crops_056_060/ref_I184_K.png), unlike the "
         "Fraktur R of 0_I p. 12; checked on crops (crops_146_150/p146_frak, p148_Klam, p149_K, p150_K). "
         "All 35 \\mathfrak{R} on pp. 146-150 are this letter (GLOBAL_ISSUES 63).")
LNOTE = ("Fraktur L (crops_146_150/p147_frakL, p147_dots): the letter fixed by hand on p. 14; \\mathfrak{Q} prints 𝔔. "
         "The 3 \\mathfrak{Q} of p. 147 (GLOBAL_ISSUES 63, 'p. 147 to check').")
C6REF = "Reference upright in the print inside the italic statement; \\sref gives (\\ref{..}) in the current (italic) font."

F = []
def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

def K(page, where, old, n=1):
    new = old.replace(r"\mathfrak{R}", r"\mathfrak{K}")
    assert old.count(r"\mathfrak{R}") == n, (old, n)
    add(page, where, "Fraktur K" + (" (%d times)" % n if n > 1 else ""),
        r"\mathfrak{R}" + (" (%d times)" % n if n > 1 else ""), "symbol", None, "high", old, new, KNOTE)

# ---------------- page 146 ----------------
K(146, "(20.6.22) continued, line 1: 'que 𝔎' soit un idéal de B''", r"que $\mathfrak{R}'$ soit un idéal")
K(146, "(20.6.22) continued, line 1: 'f(𝔎)⊂𝔎''", r"$f(\mathfrak{R})\subset\mathfrak{R}'$", 2)
K(146, "(20.6.22) continued, line 1: 'E'=B'/𝔎'^2'", r"$E'=B'/\mathfrak{R}'^2$")
K(146, "(20.6.22) continued, line 2: 'C'=B'/𝔎' par 𝔎'/𝔎'^2'", r"$C'=B'/\mathfrak{R}'$ par $\mathfrak{R}'/\mathfrak{R}'^2$", 3)
K(146, "diagram (20.6.22.2), top row: '𝔎'/𝔎'^2'", r"\mathfrak{R}'/\mathfrak{R}'^2 \ar[r]", 2)
K(146, "diagram (20.6.22.2), bottom row: '𝔎/𝔎^2'", r"\mathfrak{R}/\mathfrak{R}^2 \ar[r] \ar[u]", 2)
K(146, "Corollaire (20.6.23), display (20.6.23.1): '𝔎/𝔎^2'", r"\mathfrak{R}/\mathfrak{R}^2\xrightarrow{\delta_{C/B/A}}", 2)
K(146, "(20.6.24): 'relativement à Λ et à l'idéal 𝔎'", r"l'idéal $\mathfrak{R}$}")

add(146, "Corollaire (20.6.23): 'Sous les hypothèses de (20.6.22), supposons'",
    "(20.6.22) upright inside the italic statement", "\\sref{0.20.6.22-fr} inside the corollary environment: italic",
    "convention", 6, "high",
    r"Sous les hypothèses de \sref{0.20.6.22-fr}, supposons",
    r"Sous les hypothèses de \textup{\sref{0.20.6.22-fr}}, supposons", C6REF)

add(146, "proof of (20.6.23): 'Cela résulte en effet de (20.6.18, (ii)).'",
    "(20.6.18, (ii)). : the item number inside the parentheses of the reference (crop p146_cela)",
    "\\sref{0.20.6.18-fr}, (ii). prints '(20.6.18), (ii).'",
    "punctuation", None, "high",
    r"de \sref{0.20.6.18-fr}, (ii).", r"de (\ref{0.20.6.18-fr}, (ii)).",
    "The same \\sref{X}, (i) pattern recurs in ega0-20 (see final message).")

add(146, "Proposition (20.6.25), display (20.6.25.1), first line: labels of the first two arrows",
    "u⁰ over the first arrow and v⁰ over the second (superscript zero); u¹, v¹ only on the second line (crop p146_der)",
    "\\xrightarrow{u^1}, \\xrightarrow{v^1} on the first line",
    "formula", None, "high",
    "\\operatorname{D\\acute{e}r}_B(C,L)\\xrightarrow{u^1}\n  \\operatorname{D\\acute{e}r}_A(C,L)\\xrightarrow{v^1}",
    "\\operatorname{D\\acute{e}r}_B(C,L)\\xrightarrow{u^0}\n  \\operatorname{D\\acute{e}r}_A(C,L)\\xrightarrow{v^0}",
    "The maps on Dér are u⁰, v⁰ in the print; the TeX repeats the exponent 1 of the Exalcom row.")

add(146, "Proposition (20.6.25), display (20.6.25.1), start of the second line",
    "the arrow beginning the second line carries ∂ too (∂ over the last arrow of line 1 and over the first arrow of line 2)",
    "plain \\to at the start of the second line",
    "formula", None, "high",
    r"\to\operatorname{Exalcom}_{B/\Lambda}(C,L)", r"\xrightarrow{\partial}\operatorname{Exalcom}_{B/\Lambda}(C,L)", "")

add(146, "Proposition (20.6.25), after the display: 'définis dans (18.3.6.4) et'",
    "(18.3.6.4) upright inside the italic statement ('et' italic; crop p146_ou)", "(18.3.6.4) italic (proposition environment)",
    "convention", 6, "high", r"dans (18.3.6.4) et", r"dans \textup{(18.3.6.4)} et", "")
add(146, "Proposition (20.6.25), after the display: '(18.3.6.2), et ∂ est défini'",
    "(18.3.6.2) upright inside the italic statement", "(18.3.6.2) italic (proposition environment)",
    "convention", 6, "high", r"(18.3.6.2), et", r"\textup{(18.3.6.2)}, et", "")
add(146, "Proposition (20.6.25), end: 'défini comme dans (20.2.2).'",
    "(20.2.2) upright inside the italic statement", "\\sref{0.20.2.2-fr} italic (proposition environment)",
    "convention", 6, "high", r"comme dans \sref{0.20.2.2-fr}.", r"comme dans \textup{\sref{0.20.2.2-fr}}.", C6REF)

add(146, "proof of (20.6.25), first display: 'Hom_C(K_•(C/B/A), L)'",
    "K_•(C/B/A): roman A with its crossbar, against the Λ of K'_•(C/A/Λ) in the same line (4x crop p146_hom_zoom)",
    "\\mathrm{K}_\\bullet(C/B/\\Lambda): silent correction",
    "misprint_in_print", None, "high",
    r"\mathrm{K}_\bullet(C/B/\Lambda),L)", r"\mathrm{K}_\bullet(C/B/A),L)",
    "The split sequence (20.6.16.1) is 0→K^C_•(B/A/Λ)→K'_•(C/A/Λ)→K_•(C/B/Λ)→0, and the cohomology of Hom(K_•(C/B/Λ), L) gives "
    "Exalcom_{B/Λ}(C, L) in (20.6.25.1); the printed A is a slip for Λ. The fix restores the printed reading.",
    corrected=r"\mathrm{K}_\bullet(C/B/\Lambda),L)")

add(146, "proof of (20.6.25), last sentence: 'avec les homomorphismes de (18.3.4.2)'",
    "(18.3.4.2)", "(18.3.4.2) (keeps the printed reading)",
    "misprint_in_print", None, "low", None, None,
    "No item (18.3.4.2) exists (18.3.4 has no numbered formulas); the statement of (20.6.25) itself defines u¹, v¹ by "
    "(18.3.6.4) and (18.3.6.2). Probably a stale number (ega0-18 also prints '(18.3.4.1) est un foncteur' for the functor "
    "tagged (18.3.5.1)); the intended reading is not certain: check before correcting.",
    corrected="(18.3.6.4) et (18.3.6.2)")

# ---------------- page 147 ----------------
add(147, "Remarque (20.6.26): 'par un idéal 𝔏, et on considère'", "Fraktur L", r"\mathfrak{Q}",
    "symbol", None, "high", r"par un idéal $\mathfrak{Q}$, et", r"par un idéal $\mathfrak{L}$, et", LNOTE)
add(147, "Remarque (20.6.26), display: '𝔏/𝔏^2'", "Fraktur L (2 times)", r"\mathfrak{Q} (2 times)",
    "symbol", None, "high", r"\mathfrak{Q}/\mathfrak{Q}^2", r"\mathfrak{L}/\mathfrak{L}^2", LNOTE)
add(147, "Remarque (20.6.26), display, left end: '. . . →0→'", "baseline dots (crop p147_dots)", r"\cdots",
    "symbol", None, "high", r"\cdots\to0\to", r"\ldots\to0\to", "GLOBAL_ISSUES 22.")
add(147, "Remarque (20.6.26), display, right end: '→0→ . . .'", "baseline dots (crop p147_dots)", r"\cdots",
    "symbol", None, "high", r"\to0\to\cdots", r"\to0\to\ldots", "GLOBAL_ISSUES 22.")
add(147, "Remarque (20.6.26): '(cf. (IV, 6.8.6))) on peut montrer'",
    "no comma after ')))' (crop p147_cf)", "'6.8.6))), on peut': added comma",
    "extra", None, "high", r"6.8.6))), on peut", r"6.8.6))) on peut", "")
add(147, "Remarque (20.6.26), last line: 'théorème de Riemann-Roch.'",
    "hyphen, as in 'c'est-à-dire' (crop p147_RR)", "Riemann--Roch (en dash)",
    "punctuation", None, "high", r"Riemann--Roch", r"Riemann-Roch", "")
add(147, "heading 20.7", "'20.7. Généralisations aux anneaux topologiques.' with a final full stop",
    "\\subsection{Généralisations aux anneaux topologiques} without it",
    "punctuation", None, "high",
    r"\subsection{Généralisations aux anneaux topologiques}",
    r"\subsection{Généralisations aux anneaux topologiques.}",
    "GLOBAL_ISSUES 43/58: no \\subsection title of ega0-14 to ega0-23 has the printed full stop.")
add(147, "(20.7.1), last paragraph: 'est un isomorphisme topologique, en tenant compte'",
    "'topologique' italic (crop p147_topo)", "upright",
    "italics", None, "high", "isomorphisme\ntopologique, en tenant", "isomorphisme\n\\emph{topologique}, en tenant", "")
add(147, "Proposition (20.7.2): 'inversible à gauche (cf. (19.1.5)), il faut'",
    "'(cf. (19.1.5))' upright inside the italic statement (crop p147_prop2)", "italic (proposition environment)",
    "convention", 6, "high", r"(cf.\ \sref{0.19.1.5-fr})", r"\textup{(cf.\ \sref{0.19.1.5-fr})}", "")
add(147, "Proposition (20.7.2): 'relativement à A (19.9.1)'",
    "(19.9.1) upright inside the italic statement", "\\sref{0.19.9.1-fr} italic",
    "convention", 6, "high", r"\sref{0.19.9.1-fr}", r"\textup{\sref{0.19.9.1-fr}}", C6REF)
add(147, "Proposition (20.7.2), end: '(et a fortiori il suffit que C soit une B-algèbre formellement lisse).'",
    "the parenthesis is roman, only 'a fortiori' italic (crop p147_prop2)",
    "italic parenthesis with an upright \\emph{a fortiori}: faces inverted",
    "convention", 6, "high",
    "(et \\emph{a fortiori} il suffit que $C$ soit une\n$B$-algèbre formellement lisse)",
    "\\textup{(et} a fortiori \\textup{il suffit que $C$ soit une\n$B$-algèbre formellement lisse)}",
    "Both halves of convention 6 in one edit.")

# ---------------- page 148 ----------------
add(148, "proof of (20.7.2), line 1: 'comme Hom. cont_C(Ω¹_{B/A}⊗_B C, L) = Hom. cont_C(Ω¹_{B/A}, L)'",
    "second Hom. cont has the subscript C (crop p148_homC)", "\\operatorname{Hom.\\ cont}_B(\\Omega^1_{B/A},L): silent correction",
    "misprint_in_print", None, "high",
    r"\operatorname{Hom.\ cont}_B(\Omega^1_{B/A},L)$ par définition",
    r"\operatorname{Hom.\ cont}_C(\Omega^1_{B/A},L)$ par définition",
    "Ω¹_{B/A} is a B-module: Hom.cont_C(Ω¹_{B/A}⊗_B C, L) = Hom.cont_B(Ω¹_{B/A}, L). The fix restores the printed C.",
    corrected=r"\operatorname{Hom.\ cont}_B(\Omega^1_{B/A},L)")
K(148, "Corollaire (20.7.3): 'si l'on désigne par (𝔎_λ)'", r"par $(\mathfrak{R}_\lambda)$")
K(148, "Corollaire (20.7.3), display (20.7.3.1): '1_{C/𝔎_λ}', '(C/𝔎_λ)' twice",
  "1_{C/\\mathfrak{R}_\\lambda}:\n  \\Omega^1_{B/A}\\otimes_B(C/\\mathfrak{R}_\\lambda)\\to\n  \\Omega^1_{C/A}\\otimes_C(C/\\mathfrak{R}_\\lambda)", 3)
add(148, "Proposition (20.7.4): 'formellement non ramifiée (19.10.2), il faut'",
    "(19.10.2) upright inside the italic statement", "\\sref{0.19.10.2-fr} italic",
    "convention", 6, "high", r"\sref{0.19.10.2-fr}", r"\textup{\sref{0.19.10.2-fr}}", C6REF)
K(148, "proof of (20.7.4): 'pour tout idéal ouvert 𝔎 de B'", r"tout idéal ouvert $\mathfrak{R}$ de $B$")
add(148, "proof of (20.7.4): 'tout idéal ouvert 𝔋 de A tel que 𝔋.B⊂𝔎'",
    "𝔋.B with a baseline dot (crop p148_HB)", "\\mathfrak{H}B (no dot)",
    "punctuation", None, "high", r"\mathfrak{H}B", r"\mathfrak{H}.B", "")
K(148, "proof of (20.7.4): '𝔋.B⊂𝔎 et tout'", r"\subset\mathfrak{R}$ et tout")
K(148, "proof of (20.7.4): 'tout (B/𝔎)-module L'", r"$(B/\mathfrak{R})$-module")
K(148, "proof of (20.7.4): 'Dér_{A/𝔋}(B/𝔎, L)=0'", r"(B/\mathfrak{R},L)=0")
add(148, "proof of (20.7.4): 'cela équivaut à Hom. cont_A(Ω¹_{B/A}, L)=0 pour un tel B-module'",
    "Hom. cont with the subscript A (crop p148_homA)", "\\operatorname{Hom.\\ cont}_B: silent correction",
    "misprint_in_print", None, "high",
    r"\operatorname{Hom.\ cont}_B(\Omega^1_{B/A},L)=0", r"\operatorname{Hom.\ cont}_A(\Omega^1_{B/A},L)=0",
    "By (20.4.8), Dér.cont_A(B, L) = Hom.cont_B(Ω¹_{B/A}, L); the B-linear maps are meant. The fix restores the printed A.",
    corrected=r"\operatorname{Hom.\ cont}_B(\Omega^1_{B/A},L)=0")
add(148, "Corollaire (20.7.5), end: '(ou encore que B_0 soit une A_0-algèbre formellement non ramifiée)'",
    "'(ou encore que' and 'soit une' roman, 'algèbre formellement non ramifiée' italic (crop p148_ouencore)",
    "the whole parenthesis italic",
    "convention", 6, "high",
    r"(ou encore que $B_0$ soit une $A_0$-algèbre", r"\textup{(ou encore que $B_0$ soit une} $A_0$-algèbre", "")
add(148, "Proposition (20.7.6), end: 'est un bimorphisme formel (19.1.2).'",
    "(19.1.2) upright inside the italic statement", "\\sref{0.19.1.2-fr} italic",
    "convention", 6, "high", r"bimorphisme formel \sref{0.19.1.2-fr}", r"bimorphisme formel \textup{\sref{0.19.1.2-fr}}", C6REF)

# ---------------- page 149 ----------------
K(149, "Corollaire (20.7.7): 'pour tout idéal ouvert 𝔎_λ de C'", r"$\mathfrak{R}_\lambda$ de $C$")
add(149, "Corollaire (20.7.7): 'l'homomorphisme (20.7.3.1) est bijectif'",
    "(20.7.3.1) upright inside the italic statement", "\\sref{0.20.7.3.1-fr} italic",
    "convention", 6, "high", r"l'homomorphisme \sref{0.20.7.3.1-fr} est", r"l'homomorphisme \textup{\sref{0.20.7.3.1-fr}} est", C6REF)
K(149, "Proposition (20.7.8): '𝔎 un idéal de B, C l'anneau topologique quotient B/𝔎'",
  "$\\mathfrak{R}$ un idéal de $B$, $C$ l'anneau topologique quotient\n$B/\\mathfrak{R}$", 2)
add(149, "Proposition (20.7.8)(i): 'Dans la suite exacte (20.5.12.1)'",
    "(20.5.12.1) upright inside the italic statement", "\\sref{0.20.5.12.1-fr} italic",
    "convention", 6, "high", r"Dans la suite exacte \sref{0.20.5.12.1-fr}", r"Dans la suite exacte \textup{\sref{0.20.5.12.1-fr}}", C6REF)
K(149, "Proposition (20.7.8)(i), display: '𝔎/𝔎^2'", r"\mathfrak{R}/\mathfrak{R}^2\xrightarrow{\delta_{C/B/A}}", 2)
add(149, "Proposition (20.7.8)(ii): 'inversible à gauche (19.1.5), il faut'",
    "(19.1.5) upright inside the italic statement", "\\sref{0.19.1.5-fr} italic",
    "convention", 6, "high", r"gauche \sref{0.19.1.5-fr}, il faut", r"gauche \textup{\sref{0.19.1.5-fr}}, il faut", C6REF)
add(149, "proof of (20.7.8)(ii): 'est surjectif. Or, compte tenu de (18.4.3)'",
    "'surjectif' italic (crop p149_surj)", "upright",
    "italics", None, "high", r"est surjectif. Or, compte tenu", r"est \emph{surjectif}. Or, compte tenu", "")
K(149, "proof of (20.7.8)(ii), display: 'Hom. cont_C(𝔎/𝔎², L)'", r"(\mathfrak{R}/\mathfrak{R}^2,L)", 2)
add(149, "proof of (20.7.8), last paragraph: 'pour tout idéal ouvert 𝔐 de A, tout idéal ouvert 𝔑 de B'",
    "the second 'tout' is printed 'ıout': its first letter has no ascender and no crossbar, a dotless i at x-height (2.5x crop p149_tout)",
    "tout: silent correction",
    "misprint_in_print", None, "medium",
    "de $A$, tout idéal\nouvert $\\mathfrak{N}$", "de $A$, {\\i}out idéal\nouvert $\\mathfrak{N}$",
    "Wrong or damaged sort for t. The reading is certain; medium only because it is typographical: drop the edit if such slips "
    "are not reproduced (same treatment as the dotless-i M_ı of 0_I p. 19).",
    corrected="tout")
K(149, "proof of (20.7.8), last paragraph: 'extension E de B/(𝔎+𝔑) par un'", r"$B/(\mathfrak{R}+\mathfrak{N})$ par un")
K(149, "proof of (20.7.8), last paragraph: 'un (B/(𝔎+𝔑))-module L'", r"$(B/(\mathfrak{R}+\mathfrak{N}))$-module")
K(149, "proof of (20.7.8), last paragraph: 'canonique B/𝔑→B/(𝔎+𝔑)'", r"\to B/(\mathfrak{R}+\mathfrak{N})$")

# ---------------- page 150 ----------------
K(150, "proof of (20.7.8), end: 'B/(𝔎+𝔑')→B/(𝔎+𝔑)'", r"$B/(\mathfrak{R}+\mathfrak{N}')\to B/(\mathfrak{R}+\mathfrak{N})$", 2)
add(150, "proof of (20.7.8), last line: 'soit (A/𝔐')-triviale. En particulier :'",
    "the paragraph ends 'En particulier :', which introduces Corollaire (20.7.9)", "'En particulier :' missing",
    "missing", None, "high",
    "$(A/\\mathfrak{M}')$-triviale.\n\\end{proof}", "$(A/\\mathfrak{M}')$-triviale. En particulier :\n\\end{proof}", "")
K(150, "Corollaire (20.7.9): 'C=B/𝔎'", r"$C=B/\mathfrak{R}$")
add(150, "proof of (20.7.11): 'et l'homomorphisme (20.7.8.1) n'est autre que (20.7.10.1)'",
    "(20.7.8.1) (crop p150_2078)", "\\sref{0.20.7.8.1-fr} (keeps the printed reading)",
    "misprint_in_print", None, "medium", None, None,
    "(20.7.8.1) is Exalcotop_A(C, L)→Exalcotop_A(B, L). The homomorphism that equals (20.7.10.1) once "
    "Exalcotop_B(C, L) = Exalcotop_{B/A}(C, L), and whose bijectivity follows from (20.6.13), is (20.7.11.1).",
    corrected=r"\sref{0.20.7.11.1-fr}")
add(150, "(20.7.13): 'Si, dans (20.6.23), on suppose que les anneaux Λ, A, B, C sont topologiques, les homomorphismes s, u, v continus'",
    "(20.6.23) (crop p150_2013)", "\\sref{0.20.6.23-fr} (keeps the printed reading)",
    "misprint_in_print", None, "medium", None, None,
    "Λ, A, B, C, s, u, v and L are the data of Proposition (20.6.25), and (20.7.13.1) is the topological form of (20.6.25.1); "
    "(20.6.23) has none of these data.",
    corrected=r"\sref{0.20.6.25-fr}")

# ---------------- checks ----------------
pages = {p: open(RUN + 'page_%03d.tex' % p, encoding='utf-8').read() for p in range(146, 151)}
ok = True
for d in F:
    if d["fix"] is None:
        continue
    n = pages[d["page"]].count(d["fix"]["old"])
    if n != 1:
        ok = False
        print('NOT UNIQUE', d["page"], n, repr(d["fix"]["old"]))
# sequential application in list order
work = dict(pages)
for d in F:
    if d["fix"] is None:
        continue
    t = work[d["page"]]
    if t.count(d["fix"]["old"]) != 1:
        ok = False
        print('FAILS IN SEQUENCE', d["page"], repr(d["fix"]["old"]))
        continue
    work[d["page"]] = t.replace(d["fix"]["old"], d["fix"]["new"])
for p in range(146, 151):
    print(p, 'R left:', work[p].count(r'\mathfrak{R}'), 'Q left:', work[p].count(r'\mathfrak{Q}'),
          'cdots left:', work[p].count(r'\cdots'))
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0, 0])
    if d["kind"] == "misprint_in_print":
        c[2] += 1
    elif d["kind"] == "convention":
        c[1] += 1
    else:
        c[0] += 1
print('counts', counts, 'total', len(F), 'ok', ok)
json.dump(F, open(OUT, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print('written', OUT)
