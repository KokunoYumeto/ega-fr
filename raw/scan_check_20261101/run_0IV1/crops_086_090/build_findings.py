import json
import re

RUN = r"user\Documents\ega_scan_check_20261101\run_0IV1"
OUT = RUN + r"\findings_086_090.json"
MK = r"\oldpage[0\textsubscript{IV-1}]"


def nl(s):
    return s.replace("<NL>", "\n")


def load(p):
    t = open(RUN + r"\page_%03d.tex" % p, encoding="utf-8", newline="").read()
    return t.replace("\r\n", "\n")


TEXT = {p: load(p) for p in range(86, 92)}

F = []  # ordered findings


def add(page, where, scan, tex, kind, old, new, conv=None, conf="high", note="",
        corrected=None, seq=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": nl(old), "new": nl(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    d["_seq"] = seq
    F.append(d)
    return d


K_NOTE_FULL = (
    "Fraktur K, not R: the glyph (curled top-left stroke, single stem with a foot, loop and leg on the right) "
    "is the 𝔎 of 0_I p. 76 (7.7.5), written \\mathfrak K there, and the same glyph is \\mathfrak K on 0_IV p. 80 "
    "(𝔎_{H,μ,n}); the print's Fraktur R (radical ℜ(A), 0_I p. 12) has a different, double-stemmed form. "
    "The letters of §19 run 𝔍 (ideals of A), 𝔎 (ideals of B), 𝔏 (ideal of C). Every \\mathfrak R on pp. 86-89 "
    "is this 𝔎 (checked on the strips; crops in crops_086_090)."
)
K_NOTE = "Fraktur K misread as \\mathfrak R (see the first Fraktur-K finding of p. 86)."
B_NOTE = ("Raised bullet in the print (S•_C, gr•); the TeX has ^* (GLOBAL_ISSUES 60; checked here for §19, "
          "p. 90: every S_C and gr exponent star is a bullet in the print).")

# ---------------------------------------------------------------- page 86
add(86, "top of page (proof continued from p. 85): 'W_λ est une variété linéaire fermée dans le C-module Hom(B, C_λ)'",
    "le C-module Hom(B, C_λ) (C without index; enlarged crop)", "le $C_\\lambda$-module", "formula",
    r"dans le $C_\lambda$-module", r"dans le $C$-module")
add(86, "top of page: 'et w_λ∈W_λ (où φ_μλ : C_λ→C_μ est l'homomorphisme canonique), qui est aussi fermée'",
    "parenthesis around 'où φ_μλ : C_λ→C_μ est l'homomorphisme canonique'", "', où ... canonique,' (commas, no parentheses)",
    "punctuation",
    r"$w_\lambda\in W_\lambda$, où<NL>$\varphi_{\mu\lambda}:C_\lambda\to C_\mu$ est<NL>l'homomorphisme canonique, qui",
    r"$w_\lambda\in W_\lambda$ (où<NL>$\varphi_{\mu\lambda}:C_\lambda\to C_\mu$ est<NL>l'homomorphisme canonique), qui")
add(86, "top of page: 'appartiendra à lim← Hom(B, C_λ) par définition'",
    "lim with the arrow under it and no index (enlarged crop)", "\\varprojlim_\\lambda", "formula",
    r"$\varprojlim_\lambda\operatorname{Hom}(B,C_\lambda)$", r"$\varprojlim\operatorname{Hom}(B,C_\lambda)$",
    note="All four lim← on this page have no index (cf. GLOBAL_ISSUES 30).")
add(86, "top of page: 'C = lim← C_λ linéairement compact'", "lim← without index", "\\varprojlim_\\lambda", "formula",
    r"$C=\varprojlim_\lambda C_\lambda$", r"$C=\varprojlim C_\lambda$")
add(86, "top of page: 'C/ℑ s'identifie à lim← C_λ/ℑ_λ'", "lim← without index", "\\varprojlim_\\lambda", "formula",
    r"$\varprojlim_\lambda C_\lambda/\mathfrak J_\lambda$", r"$\varprojlim C_\lambda/\mathfrak J_\lambda$")
add(86, "top of page: 'et l'application canonique ψ : C→C/ℑ à lim← ψ_λ'", "lim← without index", "\\varprojlim_\\lambda", "formula",
    r"$\varprojlim_\lambda\psi_\lambda$", r"$\varprojlim\psi_\lambda$")
add(86, "subsection heading 19.4", "'19.4. Premiers critères de lissité formelle.' (final full stop)",
    "\\subsection{Premiers critères de lissité formelle} (no full stop)", "punctuation",
    r"\subsection{Premiers critères de lissité formelle}", r"\subsection{Premiers critères de lissité formelle.}",
    note="GLOBAL_ISSUES 58/43: no \\subsection title in ega0-14 to ega0-23 has the printed full stop.")
add(86, "Proposition (19.4.1): conditions 1°, 2°, 3°",
    "run into the statement's paragraph: '... telles que : 1° (ℑ_α) tend vers 0 dans A et (𝔎_α) tend vers 0 dans B; 2° pour tout α∈I on a ℑ_αB⊂𝔎_α (...); 3° pour tout α∈I, B/𝔎_α est une (A/ℑ_α)-algèbre formellement lisse. Alors B est une A-algèbre formellement lisse.'",
    "enumerate list", "other",
    r"respectivement, telles que~:<NL>\begin{enumerate}<NL>  \item[$1^\circ$] $(\mathfrak J_\alpha)$ tend vers $0$ dans $A$ et<NL>  $(\mathfrak R_\alpha)$ tend vers $0$ dans $B$~;<NL>  \item[$2^\circ$] pour tout $\alpha\in I$ on a<NL>  $\mathfrak J_\alpha B\subset\mathfrak R_\alpha$ (de sorte que<NL>  $B/\mathfrak R_\alpha$ est une<NL>  $(A/\mathfrak J_\alpha)$-algèbre topologique)~;<NL>  \item[$3^\circ$] pour tout $\alpha\in I$,<NL>  $B/\mathfrak R_\alpha$ est une<NL>  $(A/\mathfrak J_\alpha)$-algèbre formellement lisse.<NL>\end{enumerate}<NL>Alors $B$ est une $A$-algèbre formellement lisse.",
    r"respectivement, telles que~:<NL>$1^\circ$ $(\mathfrak J_\alpha)$ tend vers $0$ dans $A$ et<NL>$(\mathfrak K_\alpha)$ tend vers $0$ dans $B$~;<NL>$2^\circ$ pour tout $\alpha\in I$ on a<NL>$\mathfrak J_\alpha B\subset\mathfrak K_\alpha$ (de sorte que<NL>$B/\mathfrak K_\alpha$ est une<NL>$(A/\mathfrak J_\alpha)$-algèbre topologique)~;<NL>$3^\circ$ pour tout $\alpha\in I$,<NL>$B/\mathfrak K_\alpha$ est une<NL>$(A/\mathfrak J_\alpha)$-algèbre formellement lisse.<NL>Alors $B$ est une $A$-algèbre formellement lisse.",
    note="Layout (as Lemme (19.7.1.5), p. 108): words and formulas agree. The new text also carries the Fraktur K "
         "for the four \\mathfrak R inside this span (same correction as the Fraktur-K findings).")
add(86, "proof of (19.4.1): 'B/𝔎_α→B/𝔎' →^{v'} C→C/𝔏'",
    "label v' over the arrow B/𝔎'→C", "B/\\mathfrak R'\\to C (no label)", "missing",
    r"\to C\to C/\mathfrak L", r"\xrightarrow{v'}C\to C/\mathfrak L")
add(86, "proof of (19.4.1): 'où v' est un (A/ℑ_α)-homomorphisme'",
    "où v' est un", "où le second homomorphisme est un", "word",
    r"où le second homomorphisme est un", r"où $v'$ est un")
add(86, "after Corollaire (19.4.2): 'elle est aussi nécessaire par (19.3.5, (iii)).'",
    "(19.3.5, (iii))", "(19.3.5), (iii)", "punctuation",
    r"(19.3.5), (iii).", r"(19.3.5, (iii)).")
add(86, "proof of (19.4.3): 'tels que u_1 = u et que u_i se factorise'",
    "u_1=u (no prime; enlarged crop)", "u_1=u (keeps the print)", "misprint_in_print",
    None, None, corrected=r"$u_1=u'$",
    note="TeX keeps the printed reading. u_1 is a map B→C_1=C/𝔎 and must be the given u' : B→C/𝔎 of the proof; "
         "u is the map B→C/ℑ (ℑ²=0) of the statement.")

# ---------------------------------------------------------------- page 87
add(87, "Proposition (19.4.4), end of statement: 'on ait (cf. (18.5.1))'",
    "'(cf. (18.5.1))' upright", "italic (inside the proposition environment)", "convention",
    r"ait (cf. (18.5.1))", r"ait \textup{(cf. (18.5.1))}", conv=6)
add(87, "Proposition (19.4.4), end of statement: 'Exalcotop_A(B, L) = 0.'",
    "inline: the formula starts the second line at the left margin, followed by the full stop",
    "displayed \\[...\\]", "other",
    r"\[<NL>  \operatorname{Exalcotop}_A(B,L)=0.<NL>\]", r"$\operatorname{Exalcotop}_A(B,L)=0$.",
    note="Display where the print sets the formula inline.")
add(87, "proof of (19.4.4): 'Si Exalcotop_A(B, L) = 0, il existe par définition (18.5.1) un μ'",
    "Exalcotop_A(B, L)", "Exalcotop_A(B,L) (keeps the print)", "misprint_in_print",
    None, None, corrected=r"$\operatorname{Exalcotop}_A(B,\mathfrak J)=0$", conf="medium",
    note="TeX keeps the printed reading. The extension E_λ is an extension of B_λ by ℑ, so the definition (18.5.1) is "
         "applied to Exalcotop_A(B, ℑ) (ℑ is one of the modules L of the statement). The current edition already "
         "reads (B,\\mathfrak J); not found in MISPRINTS*.json.")
add(87, "after (19.4.4): 'Lorsque A et B sont des anneaux discrets'",
    "discrets in italics", "discrets upright", "italics",
    r"sont des anneaux discrets,", r"sont des anneaux \emph{discrets},")
add(87, "Corollaire (19.4.5), label (i)", "(i) upright", "\\item[(i)] italic in the corollary environment", "convention",
    r"\item[(i)] Supposons", r"\item[\textup{(i)}] Supposons", conv=6, note="GLOBAL_ISSUES 16.")
add(87, "Corollaire (19.4.5) (i): 'dans L (18.4.3), il existe'", "(18.4.3) upright", "italic", "convention",
    r"dans $L$ (18.4.3), il existe", r"dans $L$ \textup{(18.4.3)}, il existe", conv=6)
add(87, "Corollaire (19.4.5), label (ii)", "(ii) upright", "\\item[(ii)] italic in the corollary environment", "convention",
    r"\item[(ii)] Si $B$", r"\item[\textup{(ii)}] Si $B$", conv=6, note="GLOBAL_ISSUES 16.")
add(87, "Corollaire (19.4.5) (ii): 'formellement projectif (19.2.1) et si'", "(19.2.1) upright", "italic", "convention",
    r"projectif (19.2.1) et si", r"projectif \textup{(19.2.1)} et si", conv=6)
add(87, "Corollaire (19.4.5) (ii): 'la condition de (i) est vérifiée'", "(i) upright", "italic", "convention",
    r"la condition de (i) est", r"la condition de \textup{(i)} est", conv=6)
add(87, "proof of (19.4.5) (ii): 'p : B→B/𝔎 se factorise en'",
    "italic p (serifed descender; enlarged crop)", "\\rho", "symbol",
    r"$\rho:", r"$p:")

# ---------------------------------------------------------------- page 88
add(88, "Corollaire (19.4.6): 'Soit A' une A-algèbre munie de la topologie déduite de celle de A.'",
    "'munie de la topologie déduite de celle de A' italic like the rest of the statement (enlarged crop)",
    "\\emph{...} (upright inside the italic corollary)", "convention",
    r"\emph{munie de<NL>la topologie déduite de celle de $A$}", r"munie de<NL>la topologie déduite de celle de $A$",
    conv=6, note="Printed italic words left upright.")
add(88, "Corollaire (19.4.6), after condition 2°: 'Alors, pour que B' = B⊗_A A' ...'",
    "new indented paragraph", "no paragraph break after \\end{enumerate}", "other",
    r"\end{enumerate}<NL>Alors, pour que", r"\end{enumerate}<NL><NL>Alors, pour que",
    note="Same form as earlier page fixes (pp. 18, 48, 75).")
add(88, "proof of (19.4.6): 'est contenue dans (19.3.5, (iii)), sans aucune hypothèse'",
    "(19.3.5, (iii))", "(19.3.5), (iii)", "punctuation",
    r"(19.3.5), (iii), sans", r"(19.3.5, (iii)), sans")
add(88, "proof of (19.4.6): 'f' = f⊗1, A'-bilinéaire symétrique'",
    "A'-bilinéaire (no index λ; enlarged crop)", "$A'_\\lambda$-bilinéaire", "formula",
    r"$A'_\lambda$-bilinéaire symétrique", r"$A'$-bilinéaire symétrique")
add(88, "proof of (19.4.6): 'il existe, par (19.4.5, (i)), un indice μ'",
    "(19.4.5, (i))", "(19.4.5), (i)", "punctuation",
    r"par (19.4.5),<NL>(i), un indice", r"par (19.4.5,<NL>(i)), un indice")
add(88, "proof of (19.4.6): 'f'∘(φ'×φ') est un 2-cobord de Hochschild'",
    "est un 2-cobord (enlarged crop)", "soit un 2-cobord", "word",
    r"soit un $2$-cobord", r"est un $2$-cobord")
add(88, "proof of (19.4.6): 'Or, si P'_• est le complexe relatif aux anneaux A_μ et B_μ'",
    "P'_• (prime and lower bullet; roman P, enlarged crop)", "P_\\bullet (no prime)", "symbol",
    r"si $P_\bullet$ est le complexe", r"si $P'_\bullet$ est le complexe",
    note="The complex of (18.4.5) is P'_• (ega0-18-fr.tex writes \\mathbf P'_\\bullet there; on this page the P is roman, "
         "as found for \\mathbf P on p. 65). The five P_• of this page all carry the prime; two are in the display fix below.")
add(88, "proof of (19.4.6): 'est évidemment P'_•⊗_A A''", "P'_•", "P_\\bullet", "symbol",
    r"$P_\bullet\otimes_A A'$~;", r"$P'_\bullet\otimes_A A'$~;")
add(88, "proof of (19.4.6): 'la construction de P'_• montre'", "P'_•", "P_\\bullet", "symbol",
    r"$P_\bullet$ montre", r"$P'_\bullet$ montre")
add(88, "proof of (19.4.6): 'on a Hom_{A'_μ}(P'_•⊗_A A', L⊗_A A') = (Hom_{A_μ}(P'_•, L))⊗_A A' à un isomorphisme canonique près'",
    "inline (starts the line at the left margin, text follows on the same line); parentheses around Hom_{A_μ}(P'_•, L); P'_• twice",
    "displayed \\[...\\], no parentheses, P_\\bullet", "other",
    r"on a<NL>\[<NL>  \operatorname{Hom}_{A'_\mu}(P_\bullet\otimes_A A',L\otimes_A A')<NL>  =\operatorname{Hom}_{A_\mu}(P_\bullet,L)\otimes_A A'<NL>\]<NL>à un isomorphisme",
    r"on a<NL>$\operatorname{Hom}_{A'_\mu}(P'_\bullet\otimes_A A',L\otimes_A A')<NL>=(\operatorname{Hom}_{A_\mu}(P'_\bullet,L))\otimes_A A'$<NL>à un isomorphisme",
    note="One edit for three differences: display -> inline, the printed parentheses (next finding), the primes of P'_•.")
add(88, "same formula: '= (Hom_{A_μ}(P'_•, L))⊗_A A''", "parentheses around Hom_{A_μ}(P'_•, L)", "none", "formula",
    None, None, note="Fix included in the display edit of the previous finding.")
add(88, "proof of (19.4.6), display: 'H²_{A'_μ}(B'_μ, L')^s = (H²_{A_μ}(B_μ, L)^s)⊗_A A''",
    "parentheses around H²_{A_μ}(B_μ, L)^s", "none", "formula",
    r"=\mathrm H^2_{A_\mu}(B_\mu,L)^s\otimes_A A'", r"=(\mathrm H^2_{A_\mu}(B_\mu,L)^s)\otimes_A A'")
add(88, "Proposition (19.4.7): 'idéal de définition de A (0_I, 7.1.2)'", "(0_I, 7.1.2) upright", "italic", "convention",
    r"($\mathbf 0_{\rm I}$, 7.1.2)", r"\textup{($\mathbf 0_{\rm I}$, 7.1.2)}", conv=6)
add(88, "end of p. 88: Proposition (19.4.7) breaks after '... alors, pour que B soit'",
    "printed p. 88 ends with 'alors, pour que B soit'; p. 89 begins 'une A-algèbre formellement lisse, il faut et il suffit que B_0 soit une A_0-algèbre formellement lisse.'",
    "the p. 89 marker stands after \\end{proposition}, before \\begin{proof}", "marker",
    r"alors, pour que $B$ soit une $A$-algèbre formellement<NL>lisse, il faut",
    r"alors, pour que $B$ soit<NL>\oldpage[0\textsubscript{IV-1}]{89}<NL>une $A$-algèbre formellement<NL>lisse, il faut",
    note="Apply together with the p. 89 marker finding, which removes the old marker. Mid-sentence form as in ega0-18 "
         "(marker on its own line; \\oldpage ends with \\ignorespaces).")

# ---------------------------------------------------------------- page 89
add(89, "top of p. 89: old marker", "p. 89 begins inside Proposition (19.4.7) (see the p. 88 marker finding)",
    "\\oldpage{89} before \\begin{proof}", "marker",
    r"\oldpage[0\textsubscript{IV-1}]{89}<NL><NL>\begin{proof}", r"\begin{proof}",
    note="Removes the old marker; apply only together with the p. 88 marker finding, which inserts it after 'pour que $B$ soit'.")
add(89, "proof of (19.4.7): 'se ramener au cas où A est discret puisque'", "discret in italics", "upright", "italics",
    r"où $A$ est discret puisque", r"où $A$ est \emph{discret} puisque")
add(89, "proof of (19.4.7): 'Appliquons le critère (19.4.5, (ii)) en considérant'", "(19.4.5, (ii))", "(19.4.5), (ii)",
    "punctuation", r"(19.4.5), (ii) en considérant", r"(19.4.5, (ii)) en considérant")
add(89, "proof of (19.4.7): 'telle que f_0(φ_0(x), φ_0(y)) = xg_0(y) — g_0(xy) + g_0(x)y pour x, y dans B_0/𝔎'B_0'",
    "inline in the print", "displayed \\[...\\]", "other",
    r"telle que<NL>\[<NL>  f_0(\varphi_0(x),\varphi_0(y))<NL>  =xg_0(y)-g_0(xy)+g_0(x)y<NL>\]<NL>pour $x,y$",
    r"telle que<NL>$f_0(\varphi_0(x),\varphi_0(y))<NL>=xg_0(y)-g_0(xy)+g_0(x)y$<NL>pour $x,y$",
    note="Display where the print sets the formula inline. Apply before the convention-7 fix of this formula.")
add(89, "same formula: 'xg_0(y) — g_0(xy)'",
    "long dash for the subtraction (bar 42 px at 300 dpi; the + and = bars of the line 34 px)", "-", "convention",
    r"xg_0(y)-g_0(xy)", r"xg_0(y)\setmin g_0(xy)", conv=7,
    note="Long dash used for a subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision. "
         "Old taken from the text after the display fix (also present before it).", seq=True)
add(89, "proof of (19.4.7): 'φ_0 : B_0/𝔎'B_0 → B_0/𝔎B_0 étant l'homomorphisme canonique.'",
    "the map is written with φ_0 before 'étant l'homomorphisme canonique.'",
    "'$\\varphi_0$ étant l'homomorphisme canonique $B_0/...\\to B_0/...$.' (reordered)", "other",
    r"$\varphi_0$ étant<NL>l'homomorphisme canonique<NL>$B_0/\mathfrak R'B_0\to B_0/\mathfrak RB_0$. On en conclut",
    r"$\varphi_0:B_0/\mathfrak K'B_0\to B_0/\mathfrak KB_0$ étant<NL>l'homomorphisme canonique. On en conclut",
    note="Word order. The new text also carries the Fraktur K for the two \\mathfrak R of this span.")
add(89, "proof of (19.4.7), display: 'f_1(x, y) = f(φ_1(x), φ_1(y)) — xg_1(y) + ...'",
    "long dash (39 px; + and = bars 34 px)", "-", "convention",
    r"f(\varphi_1(x),\varphi_1(y))-xg_1(y)", r"f(\varphi_1(x),\varphi_1(y))\setmin xg_1(y)", conv=7,
    note="GLOBAL_ISSUES 23.")
add(89, "same display: '+ g_1(xy) — g_1(x)y'", "long dash (41 px)", "-", "convention",
    r"g_1(xy)-g_1(x)y", r"g_1(xy)\setmin g_1(x)y", conv=7)
add(89, "proof of (19.4.7): 'f_1 prend ses valeurs dans ℑL'", "dans in italics", "upright", "italics",
    r"prend ses valeurs dans $\mathfrak JL$", r"prend ses valeurs \emph{dans} $\mathfrak JL$")
add(89, "proof of (19.4.7), display: 'f_1(φ_2(x), φ_2(y)) = xg_2(y) — g_2(xy) + g_2(x)y'",
    "long dash (42 px; + and = bars 34-35 px)", "-", "convention",
    r"xg_2(y)-g_2(xy)", r"xg_2(y)\setmin g_2(xy)", conv=7)
add(89, "heading 19.5 (printed at the top of p. 90; in the TeX before the p. 90 marker)",
    "'19.5. Lissité formelle et anneaux gradués associés.' (final full stop)", "no full stop", "punctuation",
    r"anneaux gradués associés}", r"anneaux gradués associés.}",
    note="Printed on p. 90; the old lies in the p. 89 segment.")
add(89, "end of p. 89 / top of p. 90: the 19.5 heading and (19.5.1) begin p. 90",
    "printed p. 89 ends with 'C.Q.F.D.' of the proof of (19.4.7); p. 90 begins with '19.5. Lissité formelle ...'",
    "the p. 90 marker stands after \\subsection, \\label and \\begin{env}[19.5.1]\\label", "marker",
    r"\end{proof}<NL><NL>\subsection{Lissité formelle", r"\end{proof}<NL><NL>\oldpage[0\textsubscript{IV-1}]{90}<NL><NL>\subsection{Lissité formelle",
    note="Apply together with the p. 90 marker finding, which removes the old marker.")

# ---------------------------------------------------------------- page 90
add(90, "top of p. 90: old marker", "p. 90 begins with the 19.5 heading (see the p. 89 marker finding)",
    "\\oldpage{90} after \\begin{env}[19.5.1]\\label", "marker",
    r"\oldpage[0\textsubscript{IV-1}]{90}<NL>Soient $C$", r"Soient $C$",
    note="Removes the old marker; apply only together with the p. 89 marker finding, which inserts it before \\subsection.")
add(90, "(19.5.1): 'En effet, soient E une C-algèbre topologique'", "soient", "soit", "word",
    r"soit $E$ une $C$-algèbre topologique", r"soient $E$ une $C$-algèbre topologique")

# ---------------------------------------------------------------- page 91 (text printed on p. 90)
add(91, "printed p. 90, last paragraph 'Lorsque S_C^n(ℑ/ℑ²) est muni ... (19.5.1) de S_C^•(ℑ/ℑ²)' (TeX after the p. 91 marker, page_091.tex)",
    "p. 90 ends with 'en vertu de la propriété universelle (19.5.1) de S•_C(ℑ/ℑ²)'; p. 91 begins 'appliquée à la A-algèbre topologique'",
    "\\oldpage{91} stands before 'Lorsque'", "marker",
    r"\oldpage[0\textsubscript{IV-1}]{91}<NL><NL>Lorsque", r"Lorsque",
    note="OUTSIDE pp. 86-90 FILES: old is in page_091.tex. Removes the misplaced marker (the blank line before "
         "'Lorsque' stays, as the print starts a paragraph there); apply together with the next finding.")
add(91, "printed p. 90/91 boundary: '... de S•_C(ℑ/ℑ²) | appliquée à la ...'",
    "p. 91 begins with 'appliquée'", "no marker there", "marker",
    r"(\mathfrak J/\mathfrak J^2)$ appliquée", r"(\mathfrak J/\mathfrak J^2)$<NL>\oldpage[0\textsubscript{IV-1}]{91}<NL>appliquée",
    note="OUTSIDE pp. 86-90 FILES: old is in page_091.tex; apply together with the previous finding.")
add(91, "printed p. 90, last line: 'propriété universelle (19.5.1) de S•_C(ℑ/ℑ²)'",
    "raised bullet", "\\mathbf S_C^*", "symbol",
    r"(19.5.1) de<NL>$\mathbf S_C^*", r"(19.5.1) de<NL>$\mathbf S_C^\bullet",
    note="OUTSIDE pp. 86-90 FILES: old is in page_091.tex. " + B_NOTE)


# ---------------------------------------------------------------- automatic per-line fixes
def spans_of_manual(page):
    t = TEXT[page]
    out = []
    for d in F:
        if d["page"] != page or d["fix"] is None or d["_seq"]:
            continue
        o = d["fix"]["old"]
        i = t.find(o)
        assert i >= 0 and t.count(o) == 1, (page, o)
        out.append((i, i + len(o), d))
    return out


LABELS = {
    86: [(1, 35, "proof continued from p. 85"), (36, 38, "heading 19.4"), (39, 58, "Proposition (19.4.1)"),
         (59, 77, "proof of (19.4.1)"), (78, 91, "Corollaire (19.4.2)"), (92, 101, "Proposition (19.4.3)"),
         (102, 115, "proof of (19.4.3)"), (116, 999, "Proposition (19.4.4)")],
    87: [(1, 10, "Proposition (19.4.4), end"), (11, 37, "proof of (19.4.4)"), (38, 47, "after (19.4.4)"),
         (48, 68, "Corollaire (19.4.5)"), (69, 999, "proof of (19.4.5)")],
    88: [(1, 11, "proof of (19.4.5) (ii), end"), (12, 33, "Corollaire (19.4.6)"), (34, 85, "proof of (19.4.6)"),
         (86, 999, "Proposition (19.4.7)")],
    89: [(1, 81, "proof of (19.4.7)"), (82, 999, "heading 19.5")],
    90: [(1, 48, "(19.5.1)"), (49, 999, "(19.5.2)")],
}


def label(page, lineno):
    for a, b, s in LABELS[page]:
        if a <= lineno + 1 <= b:  # +1: page files have the '% from' line first
            return s
    return ""


def auto_fixes(page, token_re, repl, kind, scan, tex, note_first, note_rest, first_flag):
    t = TEXT[page]
    manual = spans_of_manual(page)
    occ = [m for m in re.finditer(token_re, t)]
    free = [m for m in occ if not any(a <= m.start() < b for a, b, _ in manual)]
    covered = [m for m in occ if any(a <= m.start() < b for a, b, _ in manual)]
    for m in covered:  # tokens inside manual edits must be converted there
        for a, b, d in manual:
            if a <= m.start() < b:
                assert not re.search(token_re, d["fix"]["new"]), (page, d["where"])
    # group by line
    lines = {}
    for m in free:
        ln = t.count("\n", 0, m.start())
        lines.setdefault(ln, []).append(m)
    res = []
    for ln in sorted(lines):
        ms = lines[ln]
        s, e = ms[0].start(), ms[-1].end()
        line_start = t.rfind("\n", 0, s) + 1
        line_end = t.find("\n", e)
        line_end = len(t) if line_end < 0 else line_end

        free_of = lambda na, nb: not any(na < mb and ma < nb for ma, mb, _ in manual)

        def widen(a, b):
            # widen to word boundaries (spaces / line ends) without touching a manual edit
            while a > 0 and t[a - 1] not in " \n" and free_of(a - 1, b):
                a -= 1
            while b < len(t) and t[b] not in " \n" and free_of(a, b + 1):
                b += 1
            return a, b

        def ext_right(a, b):
            if b >= len(t):
                return None
            nb = b + 1
            while nb < len(t) and t[nb] not in " \n":
                nb += 1
            return (a, nb) if free_of(a, nb) else None

        def ext_left(a, b):
            if a <= 0:
                return None
            na = a - 1
            while na > 0 and t[na - 1] not in " \n":
                na -= 1
            return (na, b) if free_of(na, b) else None

        a, b = widen(s, e)
        step = 0
        while t.count(t[a:b]) != 1:
            first, second = (ext_right, ext_left) if step % 2 == 0 else (ext_left, ext_right)
            r = first(a, b) or second(a, b)
            assert r and step < 50, (page, ln, t[a:b])
            a, b = r
            step += 1
        if b - a < 16:  # give very short olds one more word of context
            r = ext_right(a, b) or ext_left(a, b)
            if r:
                a, b = r
        while t[a] in " \n" and t.count(t[a + 1:b]) == 1:
            a += 1
        while t[b - 1] in " \n" and t.count(t[a:b - 1]) == 1:
            b -= 1
        assert t.count(t[a:b]) == 1 and free_of(a, b)
        old = t[a:b]
        new = re.sub(token_re, lambda mm: repl(mm.group(0)), old)
        snippet = t[line_start:line_end].strip()
        res.append((a, {
            "page": page,
            "where": f"{label(page, ln)}, source line {ln + 1} of page_{page:03d}.tex: '{snippet[:110]}'",
            "scan": scan, "tex": tex, "kind": kind, "convention": None, "confidence": "high",
            "fix": {"old": old, "new": new},
            "note": note_first if (first_flag and not res) else note_rest,
            "_seq": False,
        }))
    return res


final = []
for page in (86, 87, 88, 89, 90, 91):
    page_findings = [d for d in F if d["page"] == page]
    nonseq = [d for d in page_findings if not d["_seq"] and d["kind"] != "misprint_in_print"]
    seq = [d for d in page_findings if d["_seq"]]
    mis = [d for d in page_findings if d["kind"] == "misprint_in_print"]
    autos = []
    if page in (86, 87, 88, 89):
        autos += auto_fixes(page, r"\\mathfrak R(?![a-zA-Z])", lambda s: s.replace(r"\mathfrak R", r"\mathfrak K"),
                            "symbol", "Fraktur K (𝔎)", "\\mathfrak R", K_NOTE_FULL, K_NOTE, page == 86)
    if page == 90:
        autos += auto_fixes(page, r"\\mathbf S_C\^\*|\\gr_\{\\mathfrak J\}\^\*", lambda s: s.replace("^*", "^\\bullet"),
                            "symbol", "raised bullet (S•_C, gr•_ℑ)", "^*", B_NOTE, "Raised bullet (GLOBAL_ISSUES 60).",
                            True)
    autos.sort(key=lambda x: x[0])
    final += nonseq + [d for _, d in autos] + seq
    if page == 89:
        final.append({
            "page": 89, "where": "proof of (19.4.7), last line: 'pour l'application canonique φ : B/𝔎''→B/𝔎'. C.Q.F.D.'",
            "scan": "B/𝔎'' → B/𝔎' (prime on the target; enlarged crop)",
            "tex": "B/\\mathfrak R''\\to B/\\mathfrak R (silently corrected)", "kind": "misprint_in_print",
            "convention": None, "confidence": "high",
            "fix": {"old": r"\to B/\mathfrak K$. C.Q.F.D.", "new": r"\to B/\mathfrak K'$. C.Q.F.D."},
            "corrected": r"$\varphi:B/\mathfrak K''\to B/\mathfrak K$",
            "note": "Silent correction; the fix restores the printed prime. Old taken from the text after the "
                    "Fraktur-K fix of this line (listed above). f is defined on (B/𝔎)×(B/𝔎), so φ must end in B/𝔎.",
            "_seq": True})
    if page == 90:
        final.append({
            "page": 90, "where": "(19.5.1): 'donc ũ(𝔞.S¹_C(V)) ⊂ 𝔟, cela prouve que ũ est continu'",
            "scan": "S¹_C(V) (digit 1 as exponent; enlarged crop)", "tex": "\\mathbf S_C^*(V) (silently corrected)",
            "kind": "misprint_in_print", "convention": None, "confidence": "high",
            "fix": {"old": r"\widetilde u(\mathfrak a.\mathbf S_C^\bullet(V))", "new": r"\widetilde u(\mathfrak a.\mathbf S_C^1(V))"},
            "corrected": r"$\widetilde u(\mathfrak a.\mathbf S_C^\bullet(V))$",
            "note": "Silent correction; the fix restores the printed exponent 1. Old taken from the text after the "
                    "raised-bullet fix of this line (listed above). Continuity needs ũ(𝔞.S•_C(V)) ⊂ 𝔞.E ⊂ 𝔟 for the "
                    "neighbourhoods 𝔞.S•_C(V)+U.S•_C(V).",
            "_seq": True})
    final += mis

# ---------------------------------------------------------------- checks
errors = []
for page in (86, 87, 88, 89, 90, 91):
    t = TEXT[page]
    spans = []
    for d in final:
        if d["page"] != page or d["fix"] is None:
            continue
        o = d["fix"]["old"]
        if d["_seq"]:
            continue
        c = t.count(o)
        if c != 1:
            errors.append(("count", page, c, o[:80]))
        i = t.find(o)
        for a, b, w in spans:
            if i < b and a < i + len(o):
                errors.append(("overlap", page, w[:60], d["where"][:60]))
        spans.append((i, i + len(o), d["where"]))
    # sequential application
    cur = t
    for d in final:
        if d["page"] != page or d["fix"] is None:
            continue
        o, n = d["fix"]["old"], d["fix"]["new"]
        c = cur.count(o)
        if c != 1:
            errors.append(("seqcount", page, c, o[:80]))
            continue
        cur = cur.replace(o, n, 1)
    if page in (86, 87, 88, 89) and re.search(r"\\mathfrak R(?![a-zA-Z])", cur):
        errors.append(("leftover R", page))
    if page == 90 and "^*" in cur:
        errors.append(("leftover ^*", page))
    if page == 89 and r"\mathfrak K'$. C.Q.F.D." not in cur:
        errors.append(("misprint not restored", page))

for d in final:
    d.pop("_seq", None)

print("errors:", errors)
from collections import Counter
cnt = Counter()
for d in final:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for p in (86, 87, 88, 89, 90, 91):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("total", len(final))
if not errors:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(final, fh, ensure_ascii=False, indent=1)
    print("written", OUT)
