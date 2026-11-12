"""v2_build.py: build run_IV4/findings_100_104.json and validate every fix, in list order, cumulatively:
- against page_NNN.tex (CRLF -> LF): 'old' must occur exactly once;
- against the CURRENT diplomatic source ega4-17-fr.tex, page segment located as in apply_fixes.py
  (from \\oldpage[IV-4]{N} to the next marker): 'old' must occur exactly once.
No .tex file is written (only the JSON and, for inspection, simulated pages v2_sim_NNN.txt in this crops folder)."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\IV4\native\ega4\ega4-17-fr.tex")
OUT = RUN / "findings_100_104.json"
NL = "\u00b6"  # pilcrow stands for a line break in the raw strings below

F = []

OM = "Italic Omega for the sheaf of differentials (GLOBAL_ISSUES 92); \\varOmega as in the fixed pages 60-99."
SUBK = "Subscript: bold upright k (\\mathbf{k}, GLOBAL_ISSUES 48); this Omega (module of differentials of the field) is upright in the print, as in the TeX."
LAB_UP = "Label printed upright inside the italic statement."
LAB_IT = "Condition labels in roman text are italic in the print, parenthesis included (GLOBAL_ISSUES 88)."
REF_UP = "Reference printed upright inside the italic statement."
DASH = "Long dash for the minus sign (GLOBAL_ISSUES 23); written \\setmin as in the earlier IV-4 pages (e.g. p. 87 '$n\\setmin r$'), pending the convention-7 decision."
REM = "Judged with the remark body roman (document-wide decision on the remarks environment)."


def add(page, where, scan, tex, kind, conv, old, new, note="", conf="high", corrected=None):
    fix = None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def bk(page, where, old, new, note="", scan="bold italic k", tex="plain k"):
    add(page, where, scan, tex, "convention", 1, old, new, note)


def sk(page, where, old, new, note=SUBK, scan="bold upright k in the subscript", tex="plain k"):
    add(page, where, scan, tex, "convention", 1, old, new, note)


def b0(page, where, old, new, note="", scan="bold 0", tex="plain 0"):
    add(page, where, scan, tex, "convention", 2, old, new, note)


def om(page, where, old, new, scan="italic Omega", note=OM):
    add(page, where, scan, "upright \\Omega", "font", None, old, new, note)


def it(page, where, old, new, scan="labels italic", note=LAB_IT, tex="upright"):
    add(page, where, scan, tex, "italics", None, old, new, note)


def up(page, where, old, new, scan="upright", note=LAB_UP, tex="italic (inside the italic statement)"):
    add(page, where, scan, tex, "convention", 6, old, new, note)


def dash(page, where, old, new, scan="long dash", note=DASH, tex="minus sign"):
    add(page, where, scan, tex, "convention", 7, old, new, note)


# ================================================================ page 100
add(100, "top of p. 100: blank line after \\oldpage[IV-4]{100} ('Notons d'abord | que l'hypothèse entraîne')",
    "p. 99 ends 'Notons d'abord', p. 100 continues the sentence with 'que l'hypothèse entraîne' (page_100_s1.png)",
    "blank line between the marker and 'que l'hypothèse': a paragraph break inside the sentence", "marker", None,
    r"\oldpage[IV-4]{100}¶¶que l'hypothèse", r"\oldpage[IV-4]{100}¶que l'hypothèse",
    "The marker stands at the right place. The blank line before it (end of the p. 99 segment) is already gone in the "
    "current source ('Notons d'abord\\n\\oldpage[IV-4]{100}', fixed with pp. 95-99); this removes the one after it "
    "(\\oldpage ends with \\ignorespaces, which does not skip a \\par).")
om(100, "l. 1: '(f^*(Ω^1_{Y/k}))_x → (Ω^1_{X/k})_x'",
   r"$(f^*(\Omega^1_{Y/k}))_x\to(\Omega^1_{X/k})_x$", r"$(f^*(\varOmega^1_{Y/k}))_x\to(\varOmega^1_{X/k})_x$",
   scan="both Omegas italic", note=OM + " Two occurrences, one edit.")
om(100, "l. 3: 'f^*(Ω^1_{Y/k}) → Ω^1_{X/k} est surjectif'",
   r"$f^*(\Omega^1_{Y/k})\to\Omega^1_{X/k}$", r"$f^*(\varOmega^1_{Y/k})\to\varOmega^1_{X/k}$",
   scan="both Omegas italic", note=OM + " Two occurrences, one edit.")
bk(100, "'si l'on pose k'=k(x)'", r"si l'on pose $k'=k(x)$", r"si l'on pose $k'=\boldsymbol{k}(x)$")
bk(100, "'il existe un point x' ... tel que k(x')=k''", r"tel que $k(x')=k'$", r"tel que $\boldsymbol{k}(x')=k'$")
b0(100, "'(resp. Y) (I, 6.4.2)'", r"(resp. $Y$) (I, 6.4.2)", r"(resp. $Y$) (\textbf{I}, 6.4.2)", scan="bold I",
   tex="plain I")
it(100, "'Â→B̂ est surjectif (17.4.4, f''))'", r"est surjectif (17.4.4, f''))", r"est \emph{surjectif} (17.4.4, \emph{f'')})",
   scan="'surjectif' italic; label f'') italic with its parenthesis (crop v2_p100_fpp.png)",
   note="One edit for the word and the label (labels: GLOBAL_ISSUES 88; written \\emph{f'')} as the edition's earlier "
        "fixes, e.g. p. 67 (17.4.1, \\emph{b'')})).")
it(100, "'l'homomorphisme Â→B̂ est aussi injectif'", r"est aussi injectif", r"est aussi \emph{injectif}",
   scan="'injectif' italic", note="")
b0(100, "'(0, 16.3.10)'", r"(0, 16.3.10)", r"(\textbf{0}, 16.3.10)")
it(100, "'f est étale au point x (17.6.3, e''))'", r"(17.6.3, e''))", r"(17.6.3, \emph{e'')})",
   scan="label e'') italic with its parenthesis, the outer parenthesis upright (crop v2_p100_epp.png; slant measured)")
up(100, "Corollaire (17.15.4): 'Sous les hypothèses générales de (17.15.3),'",
   r"générales de (17.15.3), supposons", r"générales de \textup{(17.15.3)}, supposons",
   scan="reference upright (crop v2_p100_ref1.png)", note=REF_UP)
bk(100, "Corollaire (17.15.4): 'que k(x) soit une extension'", r"que $k(x)$ soit une extension",
   r"que $\boldsymbol{k}(x)$ soit une extension")
up(100, "Corollaire (17.15.4): 'une extension finie et séparable de k'",
   r"finie et séparable de $k$ et que les germes", r"\textup{finie} et \textup{séparable} de $k$ et que les germes",
   scan="'finie' and 'séparable' roman, 'et' italic (crop v2_p100_finie.png)",
   note="Words printed roman (emphasis) inside the italic statement.")
up(100, "Corollaire (17.15.4): 'Alors les conditions a), b), c) de (17.15.3) équivalent'",
   r"les conditions a), b), c) de (17.15.3) équivalent",
   r"les conditions \textup{a), b), c)} de \textup{(17.15.3)} équivalent",
   scan="labels and reference upright (crop v2_p100_conds.png)",
   note="Labels and reference printed upright inside the italic statement.")
up(100, "Corollaire (17.15.4), label d)", r"\item[d)] Les $n$ germes", r"\item[\textup{d)}] Les $n$ germes",
   scan="'d)' upright")
up(100, "Corollaire (17.15.4), label d')", r"\item[d')] L'anneau", r"\item[\textup{d$'$)}] L'anneau",
   scan="'d')' upright", note=LAB_UP + " Prime written d$'$ as in the edition's fixed item labels (e.g. \\item[\\textup{f$''$)}], p. 65).")
b0(100, "Corollaire (17.15.4) d'): 'pour cet anneau (0, 17.1.6).'", r"pour cet anneau (0, 17.1.6).",
   r"pour cet anneau \textup{(\textbf{0}, 17.1.6)}.", scan="bold 0; the reference upright (crop v2_p100_ref2.png)",
   tex="plain 0; reference italic",
   note="One edit for convention 2 (bold 0) and convention 6 (upright reference inside the italic statement), as for "
        "(I, 2.2.4) on p. 99.")
it(100, "proof of (17.15.4): 'En effet, d') entraîne trivialement d).'",
   r"En effet, d') entraîne trivialement d).", r"En effet, \emph{d')} entraîne trivialement \emph{d)}.")
bk(100, "proof of (17.15.4): 'comme k(x) est une extension finie et séparable'", r"comme $k(x)$ est une extension finie",
   r"comme $\boldsymbol{k}(x)$ est une extension finie")
sk(100, "proof of (17.15.4): 'on a Ω^1_{k(x)/k}=0'", r"$\Omega^1_{k(x)/k}=0$", r"$\Omega^1_{\mathbf{k}(x)/k}=0$",
   scan="bold upright k in the subscript; upright Omega (crop v2_p100_omk.png)")
b0(100, "'(0, 20.6.20)'", r"(0, 20.6.20)", r"(\textbf{0}, 20.6.20)")
bk(100, "proof of (17.15.4): 'k(x)=O_{X,x}/m_x est une k-algèbre'", r"et $k(x)=\sh{O}_{X,x}/\mathfrak m_x$",
   r"et $\boldsymbol{k}(x)=\sh{O}_{X,x}/\mathfrak m_x$")
b0(100, "'pour les topologies discrètes (0, 19.6.1)'", r"(0, 19.6.1)", r"(\textbf{0}, 19.6.1)")
b0(100, "'la suite exacte (0, 20.5.14.1)'", r"(0, 20.5.14.1)", r"(\textbf{0}, 20.5.14.1)")
add(100, "proof of (17.15.4): 's'applique à A=k, B=O_{X,x}, 𝔎=m_x'",
    "Fraktur K (crops v2_p100_frak.png, v2_p100_frak_big.png: same glyph as the print's 𝔎 in 0_IV, "
    "run_0IV1/crops_066_070/p80_frakK_zoom.png; unlike its Fraktur R, ref_0I_p12_frakR.png)",
    "\\mathfrak{R}", "symbol", None, r"$\mathfrak{R}=\mathfrak m_x$", r"$\mathfrak{K}=\mathfrak m_x$",
    "Wrong letter (GLOBAL_ISSUES 63): the ideal 𝔎 of the exact sequence (0, 20.5.14.1).")
om(100, "display δ: '(Ω^1_{X/k})_x'", r"\xrightarrow{\sim}(\Omega^1_{X/k})_x", r"\xrightarrow{\sim}(\varOmega^1_{X/k})_x",
   scan="italic Omega (crop v2_p100_delta.png)")
bk(100, "display δ: '⊗_{O_{X,x}} k(x).'", r"\otimes_{\sh{O}_{X,x}}k(x).¶\]", r"\otimes_{\sh{O}_{X,x}}\boldsymbol{k}(x).¶\]",
   scan="bold italic k (crop v2_p100_delta.png)")
it(100, "'l'équivalence des conditions c) et d), compte tenu'", r"des conditions c) et d), compte",
   r"des conditions \emph{c)} et \emph{d)}, compte")
b0(100, "'x est un point fermé de X (I, 6.4.2), et n éléments'", r"fermé de $X$ (I, 6.4.2), et",
   r"fermé de $X$ (\textbf{I}, 6.4.2), et", scan="bold I", tex="plain I")
b0(100, "'paramètres pour O_{X,x} (0, 17.1.6), ce qui'", r"pour $\sh{O}_{X,x}$ (0, 17.1.6), ce qui",
   r"pour $\sh{O}_{X,x}$ (\textbf{0}, 17.1.6), ce qui")
it(100, "'ce qui prouve que a) entraîne d').'", r"ce qui prouve que a) entraîne d').",
   r"ce qui prouve que \emph{a)} entraîne \emph{d')}.")
up(100, "Proposition (17.15.5), label a)", r"\item[a)] $X$ est lisse", r"\item[\textup{a)}] $X$ est lisse", scan="'a)' upright")
up(100, "Proposition (17.15.5), label b)", r"\item[b)] $X$ est différentiellement",
   r"\item[\textup{b)}] $X$ est différentiellement", scan="'b)' upright")
up(100, "Proposition (17.15.5), label c)", r"\item[c)]", r"\item[\textup{c)}]", scan="'c)' upright")
om(100, "Proposition (17.15.5) c): '(Ω^1_{X/k})_x est un O_{X,x}-module libre de rang n'",
   r"$(\Omega^1_{X/k})_x$ est un $\sh{O}_{X,x}$-module libre", r"$(\varOmega^1_{X/k})_x$ est un $\sh{O}_{X,x}$-module libre")
up(100, "Proposition (17.15.5), label d)", r"\item[d)] $(", r"\item[\textup{d)}] $(", scan="'d)' upright")
om(100, "Proposition (17.15.5) d): '(Ω^1_{X/k})_x est un O_{X,x}-module admettant'",
   r"$(\Omega^1_{X/k})_x$ est un $\sh{O}_{X,x}$-module admettant",
   r"$(\varOmega^1_{X/k})_x$ est un $\sh{O}_{X,x}$-module admettant")

# ================================================================ page 101
up(101, "Proposition (17.15.5), label e)", r"\item[e)]", r"\item[\textup{e)}]", scan="'e)' upright")
it(101, "proof of (17.15.5): 'U⊗_k k' est régulier pour toute extension k' de k'", r"pour toute extension",
   r"pour \emph{toute} extension", scan="'toute' italic (crop v2_p101_toute.png)", note="")
it(101, "proof of (17.15.5): 'ce qui prouve que a) implique e). Inversement e) implique a)'",
   r"ce qui prouve que a) implique e). Inversement e) implique a), car",
   r"ce qui prouve que \emph{a)} implique \emph{e)}. Inversement \emph{e)} implique \emph{a)}, car")
it(101, "proof of (17.15.5): 'a) entraîne c) (17.10.2); c) implique d) trivialement ... d) implique a)'",
   r"que a) entraîne c) (17.10.2); c) implique d) trivialement et le fait que d) implique a) résulte",
   r"que \emph{a)} entraîne \emph{c)} (17.10.2); \emph{c)} implique \emph{d)} trivialement et le fait que \emph{d)} implique \emph{a)} résulte")
b0(101, "'résulte de (0, 20.4.7)'", r"(0, 20.4.7)", r"(\textbf{0}, 20.4.7)")
it(101, "'et (17.15.3, c))'", r"(17.15.3, c))", r"(17.15.3, \emph{c)})", scan="label c) italic")
it(101, "proof of (17.15.5): 'a) implique b) (17.12.4). Inversement, pour prouver que b) entraîne a)'",
   r"vu que a) implique b) (17.12.4). Inversement, pour prouver que b) entraîne a), on",
   r"vu que \emph{a)} implique \emph{b)} (17.12.4). Inversement, pour prouver que \emph{b)} entraîne \emph{a)}, on")
it(101, "proof of (17.15.5): 'au cas où x est rationnel sur k, en considérant'",
   r"où $x$ est rationnel sur $k$, en considérant", r"où $x$ est \emph{rationnel sur $k$}, en considérant",
   scan="'rationnel sur k' italic (page_101_s2.png); the later 'Supposant donc x rationnel sur k' is roman, as in the TeX",
   note="Written as on p. 100 (\\emph{rationnel sur $k$}).")
bk(101, "proof of (17.15.5): 'tel que k(x')=k'=k(x)'", r"$k(x')=k'=k(x)$", r"$\boldsymbol{k}(x')=k'=\boldsymbol{k}(x)$",
   scan="bold italic k twice", note="Two occurrences, one edit.")
it(101, "proof of (17.15.5): 'résulte alors de l'hypothèse b) et de (17.12.5)'", r"l'hypothèse b) et de",
   r"l'hypothèse \emph{b)} et de", scan="label b) italic")
om(101, "Corollaire (17.15.6): 'le O_X-Module Ω^1_{X/k} soit localement libre'",
   r"le $\sh{O}_X$-Module $\Omega^1_{X/k}$ soit", r"le $\sh{O}_X$-Module $\varOmega^1_{X/k}$ soit")
up(101, "Corollaire (17.15.6): '(cette dernière condition étant automatiquement vérifiée si k est un corps parfait et X un préschéma réduit)'",
   r"(cette dernière condition étant automatiquement vérifiée si $k$ est un corps parfait et $X$ un préschéma réduit)",
   r"\textup{(cette dernière condition étant automatiquement vérifiée si $k$ est un corps \emph{parfait} et $X$ un préschéma \emph{réduit})}",
   scan="the whole parenthesis roman, both parentheses upright (slant measured), 'parfait' and 'réduit' italic "
        "(crops v2_p101_cette.png, v2_p101_close_paren2.png)",
   tex="italic throughout (corollary environment)",
   note="Roman parenthesis inside the italic statement; \\emph inside \\textup gives the printed italic 'parfait', 'réduit'.")
om(101, "proof of (17.15.6): 'il résulte de (17.10.2) que Ω^1_{X/k} est localement libre'",
   r"(17.10.2) que $\Omega^1_{X/k}$ est localement libre", r"(17.10.2) que $\varOmega^1_{X/k}$ est localement libre")
b0(101, "'une extension séparable de k (0, 19.6.1)'", r"(0, 19.6.1)", r"(\textbf{0}, 19.6.1)")
om(101, "proof of (17.15.6): 'donc Ω^1_{X/k} localement libre de rang constant n'",
   r"donc $\Omega^1_{X/k}$ localement libre", r"donc $\varOmega^1_{X/k}$ localement libre")
sk(101, "proof of (17.15.6): 'rg_{k(x)} Ω^1_{k(x)/k}=n'", r"\operatorname{rg}_{k(x)}\Omega^1_{k(x)/k}",
   r"\operatorname{rg}_{\mathbf{k}(x)}\Omega^1_{\mathbf{k}(x)/k}",
   scan="bold upright k in both subscripts; 'rg' and Omega upright (crop v2_p101_rg.png)",
   note=SUBK + " Two occurrences, one edit.")
bk(101, "proof of (17.15.6): 'puisque O_{X,x}=k(x); comme par hypothèse k(x) est'",
   r"puisque $\sh{O}_{X,x}=k(x)$; comme par hypothèse $k(x)$ est",
   r"puisque $\sh{O}_{X,x}=\boldsymbol{k}(x)$; comme par hypothèse $\boldsymbol{k}(x)$ est",
   scan="bold italic k twice", note="Two occurrences, one edit.")
sk(101, "proof of (17.15.6): 'on a Υ_{k(x)/k}=0'", r"$\Upsilon_{k(x)/k}=0$", r"$\Upsilon_{\mathbf{k}(x)/k}=0$",
   scan="bold upright k in the subscript (crop v2_p101_upsilon.png)", note="Subscript: bold upright k (GLOBAL_ISSUES 48).")
b0(101, "'(0, 20.6.3), donc deg.tr'", r"(0, 20.6.3)", r"(\textbf{0}, 20.6.3)")
bk(101, "proof of (17.15.6): 'donc deg.tr_k k(x)=n'", r"donc $\deg.\operatorname{tr}_k k(x)=n$",
   r"donc $\deg.\operatorname{tr}_k \boldsymbol{k}(x)=n$")
b0(101, "'par l'égalité de Cartier (0, 21.7.1)'", r"(0, 21.7.1)", r"(\textbf{0}, 21.7.1)")
add(101, "proof of (17.15.6): 'dimension n (5.2.1), et on conclut que X est lisse'",
    "'et on conclut' (crop v2_p101_etonconclut.png)", "'et l'on conclut'", "word", None,
    r"et l'on conclut que", r"et on conclut que", "The TeX rewords the printed phrase.")
it(101, "proof of (17.15.6): 'en vertu de ce que c) entraîne a) dans (17.15.5)'", r"de ce que c) entraîne a) dans",
   r"de ce que \emph{c)} entraîne \emph{a)} dans")
up(101, "Corollaire (17.15.7): 'Si k est de caractéristique 0, alors,'", r"de caractéristique 0, alors",
   r"de caractéristique \textup{0}, alors", scan="the figure 0 roman (crop v2_p101_carac.png)",
   note="Figure printed roman inside the italic statement.")
om(101, "Corollaire (17.15.7): 'que (Ω^1_{X/k})_x soit un O_{X,x}-module libre'", r"que $(\Omega^1_{X/k})_x$ soit un",
   r"que $(\varOmega^1_{X/k})_x$ soit un")
it(101, "proof of (17.15.7): 'l'équivalence de b) et a) dans (17.15.5)'", r"l'équivalence de b) et a) dans",
   r"l'équivalence de \emph{b)} et \emph{a)} dans")
dash(101, "Proposition (17.15.8): 'de sorte que n—r=deg.tr_k k(x)'", r"de sorte que $n-r", r"de sorte que $n\setmin r",
     scan="long dash for the minus (crop v2_p101_nr.png)")
bk(101, "Proposition (17.15.8): 'n—r=deg.tr_k k(x) (5.2.3)'", r"=\deg.\operatorname{tr}_k k(x)$",
   r"=\deg.\operatorname{tr}_k \boldsymbol{k}(x)$", scan="bold italic k (crop v2_p101_nr.png)")
up(101, "Proposition (17.15.8): '(5.2.3). Soit (g_i)'", r"(5.2.3). Soit", r"\textup{(5.2.3)}. Soit",
   scan="reference upright (crop v2_p101_523.png)", note=REF_UP)
bk(101, "Proposition (17.15.8): '(et impliquent ... et que k(x) est une extension séparable de k)'",
   r"et que $k(x)$ est une extension séparable de $k$):", r"et que $\boldsymbol{k}(x)$ est une extension séparable de $k$):",
   note="The parentheses of '(et impliquent ... de k)' are italic in the print, as in the TeX (crops v2_p101_etimpl_open.png, v2_p101_etimpl_close.png).")
up(101, "Proposition (17.15.8), label a)", r"\item[a)] $f$ est étale", r"\item[\textup{a)}] $f$ est étale", scan="'a)' upright")

# ================================================================ page 102
up(102, "Proposition (17.15.8), label b)", r"\item[b)] Les $(g_i)_x$ tels que", r"\item[\textup{b)}] Les $(g_i)_x$ tels que",
   scan="'b)' upright")
up(102, "Proposition (17.15.8) b): '(et par suite forment un système régulier de paramètres pour O_{X,x} (0, 17.1.6))'",
   r"(et par suite forment un système régulier de paramètres pour $\sh{O}_{X,x}$ (0, 17.1.6))",
   r"\textup{(et par suite forment un système régulier de paramètres pour $\sh{O}_{X,x}$ (\textbf{0}, 17.1.6))}",
   scan="the whole parenthesis roman, bold 0 (crops v2_p102_b_paren1.png, v2_p102_b_paren2.png)",
   tex="italic (proposition environment); plain 0",
   note="Roman parenthesis inside the italic statement (convention 6) and bold 0 (convention 2), one edit.")
sk(102, "Proposition (17.15.8) b): 'les images dans Ω^1_{k(x)/k} des éléments'", r"dans $\Omega^1_{k(x)/k}$ des éléments",
   r"dans $\Omega^1_{\mathbf{k}(x)/k}$ des éléments")
add(102, "Proposition (17.15.8) b): 'des éléments (d_{X/k}g_j)_x pour r+1⩽j⩽n'",
    "index j: g_j and r+1⩽j⩽n (crops v2_p102_b_gj.png, v2_p102_b_range.png)", "index i", "formula", None,
    r"$(d_{X/k}g_i)_x$ pour $r+1\leq i\leq n$", r"$(d_{X/k}g_j)_x$ pour $r+1\leq j\leq n$",
    "The print uses j here and in (17.15.9) d); the proof uses i (g_i, 1⩽i⩽n), as in the TeX.")
sk(102, "Proposition (17.15.8) b), end: 'engendrent Ω^1_{k(x)/k}.'",
   r"engendrent $\Omega^1_{k(x)/k}$.¶\end{enumerate}¶\end{proposition}",
   r"engendrent $\Omega^1_{\mathbf{k}(x)/k}$.¶\end{enumerate}¶\end{proposition}")
b0(102, "'On a en effet (0, 20.5.12.1)'", r"(0, 20.5.12.1)", r"(\textbf{0}, 20.5.12.1)")
bk(102, "'la suite exacte de k(x)-modules'", r"de $k(x)$-modules", r"de $\boldsymbol{k}(x)$-modules")
om(102, "display (17.15.8.1): '(Ω^1_{X/k})_x'", r"\tag{17.15.8.1}¶\mathfrak m_x/\mathfrak m_x^2\to(\Omega^1_{X/k})_x",
   r"\tag{17.15.8.1}¶\mathfrak m_x/\mathfrak m_x^2\to(\varOmega^1_{X/k})_x")
add(102, "display (17.15.8.1): '⊗ k(x) → Ω^1_{k(x)/k} → 0'",
    "bold italic k after ⊗; bold upright k in the subscript of the (upright) Omega", "plain k twice", "convention", 1,
    r"k(x)\to\Omega^1_{k(x)/k}\to0¶\]¶et la condition", r"\boldsymbol{k}(x)\to\Omega^1_{\mathbf{k}(x)/k}\to0¶\]¶et la condition",
    "Two occurrences, one edit (GLOBAL_ISSUES 48 for the subscript).")
it(102, "'et la condition b) entraîne par suite'", r"et la condition b) entraîne par suite",
   r"et la condition \emph{b)} entraîne par suite", scan="label b) italic")
om(102, "'les (d_{X/k}g_i)_x engendrent (Ω^1_{X/k})_x compte tenu du lemme de Nakayama'",
   r"engendrent $(\Omega^1_{X/k})_x$ compte tenu", r"engendrent $(\varOmega^1_{X/k})_x$ compte tenu")
it(102, "'le fait que b) implique a) résulte donc de (17.15.3)'", r"le fait que b) implique a) résulte donc",
   r"le fait que \emph{b)} implique \emph{a)} résulte donc")
it(102, "'Inversement, si a) est vérifiée'", r"Inversement, si a) est vérifiée", r"Inversement, si \emph{a)} est vérifiée",
   scan="label a) italic")
om(102, "'forment une base de (Ω^1_{X/k})_x en vertu de (17.15.3)'", r"base de $(\Omega^1_{X/k})_x$ en vertu",
   r"base de $(\varOmega^1_{X/k})_x$ en vertu")
bk(102, "'est l'image de (g_i)_x dans k(x), on conclut'", r"dans $k(x)$, on conclut", r"dans $\boldsymbol{k}(x)$, on conclut")
sk(102, "'les dt_i engendrent Ω^1_{k(x)/k} pour 1⩽i⩽n'", r"engendrent $\Omega^1_{k(x)/k}$ pour",
   r"engendrent $\Omega^1_{\mathbf{k}(x)/k}$ pour")
sk(102, "'les dt_i pour r+1⩽i⩽n engendrent déjà Ω^1_{k(x)/k}'", r"engendrent déjà $\Omega^1_{k(x)/k}$",
   r"engendrent déjà $\Omega^1_{\mathbf{k}(x)/k}$")
bk(102, "'Comme deg.tr_k k(x)=n—r'", r"Comme $\deg.\operatorname{tr}_k k(x)", r"Comme $\deg.\operatorname{tr}_k \boldsymbol{k}(x)")
dash(102, "'Comme deg.tr_k k(x)=n—r, il suit'", r"=n-r$, il suit", r"=n\setmin r$, il suit",
     scan="long dash for the minus (page_102_s2.png)")
b0(102, "'il suit de l'égalité de Cartier (0, 21.7.1)'", r"(0, 21.7.1)", r"(\textbf{0}, 21.7.1)")
add(102, "'que Υ_{k(x)/k}=0, donc k(x) est une extension séparable de k'",
    "bold upright k in the subscript of Υ; bold italic k in k(x)", "plain k twice", "convention", 1,
    r"que $\Upsilon_{k(x)/k}=0$, donc $k(x)$ est une extension",
    r"que $\Upsilon_{\mathbf{k}(x)/k}=0$, donc $\boldsymbol{k}(x)$ est une extension",
    "Two occurrences, one edit (GLOBAL_ISSUES 48 for the subscript).")
b0(102, "'séparable de k (0, 20.6.3), et la suite'", r"(0, 20.6.3), et la suite", r"(\textbf{0}, 20.6.3), et la suite")
bk(102, "'la suite de k(x)-espaces vectoriels'", r"de $k(x)$-espaces vectoriels", r"de $\boldsymbol{k}(x)$-espaces vectoriels")
om(102, "display (17.15.8.2): '(Ω^1_{X/k})_x'", r"\tag{17.15.8.2}¶0\to\mathfrak m_x/\mathfrak m_x^2\to(\Omega^1_{X/k})_x",
   r"\tag{17.15.8.2}¶0\to\mathfrak m_x/\mathfrak m_x^2\to(\varOmega^1_{X/k})_x")
add(102, "display (17.15.8.2): '⊗ k(x) → Ω^1_{k(x)/k} → 0'",
    "bold italic k after ⊗; bold upright k in the subscript of the (upright) Omega", "plain k twice", "convention", 1,
    r"k(x)\to\Omega^1_{k(x)/k}\to0¶\]¶est exacte", r"\boldsymbol{k}(x)\to\Omega^1_{\mathbf{k}(x)/k}\to0¶\]¶est exacte",
    "Two occurrences, one edit (GLOBAL_ISSUES 48 for the subscript).")
b0(102, "'est exacte ((0, 20.5.14) et (0, 19.6.1))'", r"((0, 20.5.14) et (0, 19.6.1))",
   r"((\textbf{0}, 20.5.14) et (\textbf{0}, 19.6.1))", scan="bold 0 twice", note="Two occurrences, one edit.")
sk(102, "'forment une base de Ω^1_{k(x)/k}, donc aucun des t_i'", r"base de $\Omega^1_{k(x)/k}$, donc aucun",
   r"base de $\Omega^1_{\mathbf{k}(x)/k}$, donc aucun")
it(102, "'ce qui achève de prouver que a) implique b).'", r"achève de prouver que a) implique b).",
   r"achève de prouver que \emph{a)} implique \emph{b)}.")
up(102, "Corollaire (17.15.9), label a)", r"\item[a)] L'anneau", r"\item[\textup{a)}] L'anneau", scan="'a)' upright")
bk(102, "Corollaire (17.15.9) a): 'est régulier et k(x) est une extension séparable de k'",
   r"régulier et $k(x)$ est une extension séparable", r"régulier et $\boldsymbol{k}(x)$ est une extension séparable")
up(102, "Corollaire (17.15.9), label b)", r"\item[b)] $X$ est lisse", r"\item[\textup{b)}] $X$ est lisse", scan="'b)' upright")
om(102, "Corollaire (17.15.9) b), display: '(Ω^1_{X/k})_x'", r"\[¶  \mathfrak m_x/\mathfrak m_x^2\to(\Omega^1_{X/k})_x",
   r"\[¶  \mathfrak m_x/\mathfrak m_x^2\to(\varOmega^1_{X/k})_x")
bk(102, "Corollaire (17.15.9) b), display: '⊗_{O_{X,x}} k(x)'", r"\otimes_{\sh{O}_{X,x}}k(x)¶  \]",
   r"\otimes_{\sh{O}_{X,x}}\boldsymbol{k}(x)¶  \]")
up(102, "Corollaire (17.15.9), label c)", r"\item[c)] Il existe", r"\item[\textup{c)}] Il existe", scan="'c)' upright")
up(102, "Corollaire (17.15.9) c): 'correspondant aux g_i (cf. (17.15.8))'", r"(cf. (17.15.8))", r"\textup{(cf. (17.15.8))}",
   scan="the whole parenthesis upright, 'cf.' roman (crop v2_p102_cf.png)",
   note="'cf.' and the reference printed upright inside the italic statement (as \\textup{(cf. (16.5.12))}, p. 90).")
up(102, "Corollaire (17.15.9), label d)", r"\item[d)] Il existe", r"\item[\textup{d)}] Il existe", scan="'d)' upright")
up(102, "Corollaire (17.15.9) d): 'Il existe n sections g_i (1⩽i⩽n) de O_X'", r"$g_i$ ($1\leq i\leq n$) de",
   r"$g_i$ \textup{(}$1\leq i\leq n$\textup{)} de", scan="both parentheses upright (crop v2_p102_d_paren.png; slant measured 0)",
   note="Parentheses printed upright around a formula inside the italic statement (as p. 21, '\\textup{(}$1\\leq i\\leq m$\\textup{)}').")
sk(102, "Corollaire (17.15.9) d): 'les images dans Ω^1_{k(x)/k} des (d_{U/k}g_j)_x'", r"dans $\Omega^1_{k(x)/k}$ des $(d_{U/k}",
   r"dans $\Omega^1_{\mathbf{k}(x)/k}$ des $(d_{U/k}")
add(102, "Corollaire (17.15.9) d): '(d_{U/k}g_j)_x pour r+1⩽j⩽n'", "index j: g_j and r+1⩽j⩽n (crops v2_p102_d_gj.png, v2_p102_d_range.png)",
    "index i", "formula", None, r"$(d_{U/k}g_i)_x$ pour $r+1\leq i\leq n$", r"$(d_{U/k}g_j)_x$ pour $r+1\leq j\leq n$",
    "As in (17.15.8) b). Apply BEFORE the next finding (wrong-fount r), whose 'old' is the text after this edit.")
add(102, "Corollaire (17.15.9) d), last line: 'r+1⩽j⩽n engendrent', the r",
    "the r at the start of the line is a BOLD italic r (wrong fount): side by side with the r of the same formula in "
    "(17.15.8) b) and the two r of '1⩽i⩽r' in c), d) it has a heavier stem (5-6 px against 4-5 px) and about 20-30% "
    "more ink, while the j, n and the ⩽ of its line match those of (17.15.8) b) (crops v2_p102_dline.png, "
    "v2_p102_bline.png, v2_p102_r_compare3.png)",
    "normal r (silent correction)", "misprint_in_print", None,
    r"U/k}g_j)_x$ pour $r+1", r"U/k}g_j)_x$ pour $\boldsymbol{r}+1",
    "Wrong-fount letter recorded as a misprint (GLOBAL_ISSUES 29 and 99; cf. the exponent n on p. 38). Less heavy than "
    "the p. 38 n, hence medium confidence. 'old' is the text after the preceding finding (index j), which must be applied first.",
    conf="medium", corrected=r"$r+1\leq j\leq n$")
sk(102, "Corollaire (17.15.9) d), end: 'engendrent Ω^1_{k(x)/k}.'",
   r"engendrent $\Omega^1_{k(x)/k}$.¶\end{enumerate}¶\end{corollary}",
   r"engendrent $\Omega^1_{\mathbf{k}(x)/k}$.¶\end{enumerate}¶\end{corollary}")
it(102, "proof of (17.15.9): 'L'équivalence de c) et d) résulte de (17.15.8)'", r"L'équivalence de c) et d) résulte",
   r"L'équivalence de \emph{c)} et \emph{d)} résulte")
it(102, "proof of (17.15.9): 'que la condition c) entraîne que X est lisse'", r"que la condition c) entraîne que",
   r"que la condition \emph{c)} entraîne que", scan="label c) italic")
it(102, "proof of (17.15.9): 'donc c) entraîne b). La condition b) entraîne'",
   r"donc c) entraîne b). La condition b) entraîne", r"donc \emph{c)} entraîne \emph{b)}. La condition \emph{b)} entraîne")
om(102, "proof of (17.15.9): 'en outre, (Ω^1_{X/k})_x est alors un O_{X,x}-module libre'",
   r"en outre, $(\Omega^1_{X/k})_x$ est alors", r"en outre, $(\varOmega^1_{X/k})_x$ est alors")
add(102, "proof of (17.15.9): 'comme la suite (17.15.7.2) est exacte par hypothèse'",
    "(17.15.7.2) (crop v2_p102_1572.png and page_102_s4.png)", "(17.15.7.2): the TeX keeps the printed reading",
    "misprint_in_print", None, None, None,
    "There is no (17.15.7.2): the sequence that b) makes exact is (17.15.8.2), as two lines earlier ('la suite "
    "(17.15.8.2) est exacte, donc c) entraîne b)'). Not in the errata list (Liste 3).", corrected="(17.15.8.2)")
sk(102, "proof of (17.15.9): 'par hypothèse, Ω^1_{k(x)/k} est de rang'", r"hypothèse, $\Omega^1_{k(x)/k}$ est de",
   r"hypothèse, $\Omega^1_{\mathbf{k}(x)/k}$ est de")
dash(102, "proof of (17.15.9): 'est de rang n—r=deg.tr_k k(x)'", r"rang $n-r=", r"rang $n\setmin r=",
     scan="long dash for the minus (page_102_s4.png)")
bk(102, "proof of (17.15.9): 'n—r=deg.tr_k k(x) et l'égalité de Cartier'", r"\operatorname{tr}_k k(x)$ et l'égalité",
   r"\operatorname{tr}_k \boldsymbol{k}(x)$ et l'égalité")
add(102, "proof of (17.15.9): 'montre que Υ_{k(x)/k}=0, donc k(x) est séparable sur k'",
    "bold upright k in the subscript of Υ; bold italic k in k(x)", "plain k twice", "convention", 1,
    r"montre que $\Upsilon_{k(x)/k}=0$, donc $k(x)$ est séparable",
    r"montre que $\Upsilon_{\mathbf{k}(x)/k}=0$, donc $\boldsymbol{k}(x)$ est séparable",
    "Two occurrences, one edit (GLOBAL_ISSUES 48 for the subscript).")
b0(102, "'séparable sur k (0, 20.6.3); ainsi'", r"(0, 20.6.3); ainsi", r"(\textbf{0}, 20.6.3); ainsi")
add(102, "end of p. 102: blank line before \\oldpage[IV-4]{103} ('Enfin, si a) | est vérifiée')",
    "p. 102 ends 'Enfin, si a)', p. 103 continues the sentence with 'est vérifiée, on déduit' (page_102_s4.png, page_103_s1.png)",
    "blank line before the marker (and another after it): a paragraph break inside the sentence", "marker", None,
    r"Enfin, si a)¶¶", r"Enfin, si a)¶",
    "The marker stands at the right place. Part 1 of 2 with the first p. 103 finding (blank line after the marker); "
    "apply both. Apply BEFORE the next finding (italic labels on the same line): this 'old' would not match after it, "
    "while the next 'old' still matches after this edit.")
it(102, "proof of (17.15.9), last line: 'ainsi b) entraîne a). Enfin, si a)'", r"ainsi b) entraîne a). Enfin, si a)",
   r"ainsi \emph{b)} entraîne \emph{a)}. Enfin, si \emph{a)}",
   note=LAB_IT + " Same spot as the preceding finding (blank line before \\oldpage[IV-4]{103}); apply after it.")

# ================================================================ page 103
add(103, "top of p. 103: blank line after \\oldpage[IV-4]{103}", "p. 103 begins mid-sentence ('est vérifiée', no indent)",
    "blank line between the marker and 'est vérifiée'", "marker", None,
    r"\oldpage[IV-4]{103}¶¶est vérifiée", r"\oldpage[IV-4]{103}¶est vérifiée",
    "Part 2 of 2 with the p. 102 finding 'end of p. 102: blank line before \\oldpage[IV-4]{103}'; both blank lines must go.")
sk(103, "l. 1: 'de l'égalité de Cartier que Ω^1_{k(x)/k} est de rang n—r'", r"Cartier que $\Omega^1_{k(x)/k}$",
   r"Cartier que $\Omega^1_{\mathbf{k}(x)/k}$")
dash(103, "l. 1: 'est de rang n—r.'", r"est de rang $n-r$.", r"est de rang $n\setmin r$.",
     scan="long dash for the minus (page_103_s1.png)")
it(103, "'l'existence des g_i vérifiant les conditions de d) est immédiate'", r"conditions de d) est immédiate",
   r"conditions de \emph{d)} est immédiate", scan="label d) italic")
om(103, "Remarques (17.15.10) (i): 'il ne suffit pas que Ω^1_{X/k} soit localement libre'",
   r"il ne suffit pas que $\Omega^1_{X/k}$", r"il ne suffit pas que $\varOmega^1_{X/k}$")
bk(103, "Remarques (17.15.10) (ii): 'sans que k(x) soit séparable sur k'", r"sans que $k(x)$ soit séparable",
   r"sans que $\boldsymbol{k}(x)$ soit séparable")
dash(103, "Remarques (17.15.10) (ii): 'l'idéal premier principal (T^p—λ)'", r"$(T^p-\lambda)$", r"$(T^p\setmin\lambda)$",
     scan="long dash for the minus (crop v2_p103_dashes.png)")
dash(103, "Remarques (17.15.10) (ii): 'λ∈k—k^p'", r"$\lambda\in k-k^p$", r"$\lambda\in k\setmin k^p$",
     scan="long dash (set difference) (crop v2_p103_dashes.png)", note="Set difference (convention 7 proper).")
bk(103, "Remarques (17.15.10) (iii): 'l'ensemble des points fermés de X tels que k(x) soit séparable'",
   r"fermés de $X$ tels que $k(x)$", r"fermés de $X$ tels que $\boldsymbol{k}(x)$")
it(103, "Remarques (17.15.10) (iii): 'soit séparable (et fini) sur k est dense dans X'",
   r"soit séparable (et fini) sur $k$ est dense dans", r"soit \emph{séparable} (et fini) sur $k$ est \emph{dense} dans",
   scan="'séparable' and 'dense' italic, '(et fini)' roman (crop v2_p103_iii_l2.png)",
   tex="upright (italic only through the remarks environment)", note=REM)
it(103, "Remarques (17.15.10) (iii): 'où g est étale (17.11.4)'", r"où $g$ est étale", r"où $g$ est \emph{étale}",
   scan="'étale' italic (crop v2_p103_iii_l4.png)", tex="upright (italic only through the remarks environment)", note=REM)
it(103, "Remarques (17.15.10) (iii): 'l'ensemble des points de l'ouvert g(U) qui sont rationnels sur k'",
   r"qui sont rationnels sur", r"qui sont \emph{rationnels} sur", scan="'rationnels' italic (crop v2_p103_iii_l6.png)",
   tex="upright (italic only through the remarks environment)", note=REM)
bk(103, "Remarques (17.15.10) (iii): 'k(x) est séparable sur k(y)=k (17.6.2)'", r"et $k(x)$ est séparable sur $k(y)=k$",
   r"et $\boldsymbol{k}(x)$ est séparable sur $\boldsymbol{k}(y)=k$", scan="bold italic k twice",
   note="Two occurrences, one edit; the final k is light, as in the TeX.")
up(103, "Proposition (17.15.11), label a)", r"\item[a)] $X$ est étale", r"\item[\textup{a)}] $X$ est étale", scan="'a)' upright")
up(103, "Proposition (17.15.11), label b)", r"\item[b)] $X$ est non ramifié", r"\item[\textup{b)}] $X$ est non ramifié",
   scan="'b)' upright")
up(103, "Proposition (17.15.11), label c)", r"\item[c)] $X$ est isomorphe", r"\item[\textup{c)}] $X$ est isomorphe",
   scan="'c)' upright")
it(103, "proof of (17.15.11): 'compte tenu de ce que la condition b) implique ici'", r"la condition b) implique ici",
   r"la condition \emph{b)} implique ici", scan="label b) italic")
bk(103, "Proposition (17.15.12): 'X soit réduit en ce point et que k(x) soit une extension séparable'",
   r"en ce point et que $k(x)$", r"en ce point et que $\boldsymbol{k}(x)$")
bk(103, "Proposition (17.15.12): 'pour tout point maximal x de X, k(x) soit une extension séparable de k'",
   r"de $X$, $k(x)$ soit une extension", r"de $X$, $\boldsymbol{k}(x)$ soit une extension")
it(103, "proof of (17.15.12): 'a fortiori réduit, donc un corps, égal à k(x)'", r"donc un corps,", r"donc un \emph{corps},",
   scan="'corps' italic (crop v2_p103_corps.png)", note="")
bk(103, "proof of (17.15.12): 'égal à k(x); en outre (17.15.1), k(x)⊗_k k''",
   r"égal à $k(x)$; en outre (17.15.1), $k(x)\otimes_k k'$",
   r"égal à $\boldsymbol{k}(x)$; en outre (17.15.1), $\boldsymbol{k}(x)\otimes_k k'$", scan="bold italic k twice",
   note="Two occurrences, one edit.")
bk(103, "proof of (17.15.12): 'donc k(x) doit être une extension séparable de k (4.3.5)'", r"donc $k(x)$ doit être",
   r"donc $\boldsymbol{k}(x)$ doit être")
bk(103, "proof of (17.15.13): 'pour tout point maximal x' de X_{(k')}, k(x') est une extension séparable de k''",
   r"$X_{(k')}$, $k(x')$ est", r"$X_{(k')}$, $\boldsymbol{k}(x')$ est")

# ================================================================ page 104
add(104, "page break 103/104 inside the word 'mor-|phisme' ('Mais le mor-' / 'phisme X_{(k')}→X')",
    "p. 103 ends 'Mais le mor-', p. 104 begins 'phisme X_{(k')}→X est un homéomorphisme' (page_103_s4.png, page_104_s1.png)",
    "\\oldpage[IV-4]{104} stands before 'morphisme', three letters before the printed page break", "marker", None,
    r"\oldpage[IV-4]{104}morphisme", r"mor%¶\oldpage[IV-4]{104}¶phisme",
    "Moves the marker to the printed break inside the word, written as the edition's other split words ($Z$-mor%|phisme "
    "at \\oldpage[IV-4]{58}, consi%|dérer at \\oldpage[IV-4]{93}). After the edit 'mor%' ends the p. 103 segment "
    "('Mais le mor%'); the 'old' lies in the p. 104 segment.")
b0(104, "Proposition (17.15.14): 'telle que le normalisé (II, 6.3.8) de (X_{(k')})_red'", r"le normalisé (II, 6.3.8) de",
   r"le normalisé \textup{(\textbf{II}, 6.3.8)} de", scan="bold II; the reference upright", tex="plain II; reference italic",
   note="One edit for convention 2 (bold II) and convention 6 (upright reference inside the italic statement).")
b0(104, "Lemme (17.15.14.1): 'au normalisé X' de X (II, 6.3.8), il faut'", r"de $X$ (II, 6.3.8), il faut",
   r"de $X$ \textup{(\textbf{II}, 6.3.8)}, il faut", scan="bold II; the reference upright", tex="plain II; reference italic",
   note="One edit for convention 2 (bold II) and convention 6 (upright reference inside the italic statement).")
up(104, "Lemme (17.15.14.1), label (i)", r"\item[(i)] $Y$ est normal", r"\item[\textup{(i)}] $Y$ est normal",
   scan="'(i)' upright (crop v2_p104_labels.png)", note="Roman-numeral label upright in the print (GLOBAL_ISSUES 16).")
up(104, "Lemme (17.15.14.1), label (ii)", r"\item[(ii)] $f$ est un morphisme", r"\item[\textup{(ii)}] $f$ est un morphisme",
   scan="'(ii)' upright (crop v2_p104_labels.png)", note="Roman-numeral label upright in the print (GLOBAL_ISSUES 16).")
add(104, "Lemme (17.15.14.1): 'Lorsqu'il existe dans X un ouvert dense et normal' after the list (i), (ii)",
    "new indented paragraph (page_104_s2.png)", "text follows \\end{enumerate} directly: set without indent", "other", None,
    r"\end{enumerate}¶Lorsqu'il existe", r"\end{enumerate}¶¶Lorsqu'il existe",
    "Indented new paragraph in the print (GLOBAL_ISSUES 80 pattern).")
up(104, "Lemme (17.15.14.1): 'lorsque X est excellent (7.8.3), en particulier'", r"excellent (7.8.3), en particulier",
   r"excellent \textup{(7.8.3)}, en particulier",
   scan="reference upright (crop v2_p104_cequi.png); the parentheses of '(ce qui ... sur un corps)' are italic, as in the TeX",
   note=REF_UP)
up(104, "Lemme (17.15.14.1): 'on peut remplacer la condition (ii) par la suivante'", r"la condition (ii) par la suivante",
   r"la condition \textup{(ii)} par la suivante", scan="'(ii)' upright (page_104_s2.png)")
up(104, "Lemme (17.15.14.1), label (ii bis)", r"\item[(ii bis)]", r"\item[\textup{(ii \emph{bis})}]",
   scan="'(ii' and ')' upright, 'bis' italic (crop v2_p104_iibis.png)",
   note="Label printed upright except 'bis' (GLOBAL_ISSUES 26); \\emph inside \\textup gives the italic 'bis'.")
b0(104, "'On sait (II, 6.3.6) que X' est somme'", r"(II, 6.3.6)", r"(\textbf{II}, 6.3.6)", scan="bold II", tex="plain II")
it(104, "proof of (17.15.14.1): 'il est immédiat que (ii) entraîne (ii bis)'", r"entraîne (ii bis) lorsqu'il",
   r"entraîne (ii \emph{bis}) lorsqu'il", scan="'bis' italic (page_104_s2.png)", note="GLOBAL_ISSUES 26.")
b0(104, "'la restriction Y_i→X de f (I, 5.2.2)'", r"(I, 5.2.2)", r"(\textbf{I}, 5.2.2)", scan="bold I", tex="plain I")
add(104, "proof of (17.15.14.1): 'est la clôture intégrale de Γ(V_i, O_{X_i})'",
    "Γ(V_i, O_{X_i}): V with the subscript i (crop v2_p104_gamma.png)", "\\Gamma(V,\\sh{O}_{X_i}): silent correction",
    "misprint_in_print", None, r"\Gamma(V,\sh{O}_{X_i})", r"\Gamma(V_i,\sh{O}_{X_i})",
    "V is the open affine of X_i just introduced ('pour tout ouvert affine V de X_i, Γ(g_i^{-1}(V), O_{Y_i})'); no V_i "
    "is defined there (the V_i=f^{-1}(U_i) come later in the proof). Not in the errata list (Liste 3). The edit restores "
    "the printed subscript only.", corrected=r"\Gamma(V,\sh{O}_{X_i})")
b0(104, "'Y s'identifie canoniquement à X' (II, 6.3.4)'", r"(II, 6.3.4)", r"(\textbf{II}, 6.3.4)", scan="bold II",
   tex="plain II")
it(104, "proof of (17.15.14.1): 'si l'on suppose vérifiée la condition (ii bis), on peut'", r"la condition (ii bis), on",
   r"la condition (ii \emph{bis}), on", scan="'bis' italic (page_104_s3.png)", note="GLOBAL_ISSUES 26.")
add(104, "proof of (17.15.14.1): 'les V̄_i sont les composantes irréductibles de Y'",
    "bar over the V only, the subscript i outside it (crop v2_p104_vbar.png)", "\\overline{V_i}: bar over V_i", "formula",
    None, r"\overline{V_i}", r"\overline{V}_i", "Bar version of convention 8 (GLOBAL_ISSUES 75).")
b0(104, "'Compte tenu de (4.6.6) et de (I, 5.1.8)'", r"(I, 5.1.8)", r"(\textbf{I}, 5.1.8)", scan="bold I", tex="plain I")


# ================================================================ validation (cumulative, in list order)
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")


def region(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, (cuts[j][1] if j < len(cuts) else len(t))
    raise KeyError(page)


src = SRC.read_text(encoding="utf-8")
pages = {p: (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for p in range(100, 105)}
bad = 0
for k, x in enumerate(F):
    fx = x["fix"]
    if not fx:
        continue
    p = x["page"]
    old, new = fx["old"], fx["new"]
    n_page = pages[p].count(old)
    s, e = region(src, p)
    seg = src[s:e]
    n_src = seg.count(old)
    if n_page != 1 or n_src != 1 or old == new:
        bad += 1
        print(f"BAD #{k} p.{p}: page count {n_page}, source-segment count {n_src}: {old[:80]!r}")
        continue
    pages[p] = pages[p].replace(old, new)
    src = src[:s] + seg.replace(old, new) + src[e:]

counts = {}
for x in F:
    c = counts.setdefault(x["page"], [0, 0, 0])
    if x["kind"] == "misprint_in_print":
        c[2] += 1
    elif x["kind"] == "convention":
        c[1] += 1
    else:
        c[0] += 1
print("findings:", len(F), "bad:", bad)
print(" ".join(f"p.{p}: {c[0]}/{c[1]}/{c[2]}" for p, c in sorted(counts.items())))
if bad == 0:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    print("written", OUT)
    for p in range(100, 105):
        (RUN / "crops_100_104" / f"v2_sim_{p:03d}.txt").write_text(pages[p], encoding="utf-8", newline="\n")
