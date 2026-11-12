"""Build findings_100_104.json and validate each fix in order:
- against page_NNN.tex (CRLF -> LF), applied cumulatively: 'old' must occur exactly once;
- against the CURRENT diplomatic source ega4-17-fr.tex, page region located as in apply_fixes.py, applied cumulatively.
Nothing is written to any .tex file."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-17-fr.tex")
OUT = RUN / "findings_100_104.json"

OM = "Italic Omega for the sheaf of differentials (GLOBAL_ISSUES 92)."
LAB_UP = "Label printed upright inside the italic statement."
LAB_IT = "Labels in roman text are italic in the print (GLOBAL_ISSUES 88)."
REF_UP = "Reference printed upright inside the italic statement."
SUBK = "Subscript: bold upright k (GLOBAL_ISSUES 48); the module's Omega is upright, as in the TeX."
DASH = "Long dash for the minus sign (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision."
REM = "Judged with the remark body roman (document-wide decision)."

F = []


def add(page, where, scan, tex, kind, conv, old, new, note="", conf="high", corrected=None, fix_null=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if fix_null else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def bk(page, where, old, new, note=""):
    add(page, where, "bold italic k", "plain k", "convention", 1, old, new, note)


def b0(page, where, old, new, note=""):
    add(page, where, "bold 0" if "{0}" in new else ("bold II" if "{II}" in new else "bold I"),
        "plain numeral", "convention", 2, old, new, note)


def om(page, where, old, new, scan="italic Omega", note=OM):
    add(page, where, scan, "upright \\Omega", "font", None, old, new, note)


def it(page, where, old, new, scan="labels italic", note=LAB_IT):
    add(page, where, scan, "upright", "italics", None, old, new, note)


def up(page, where, old, new, scan="upright", note=LAB_UP):
    add(page, where, scan, "italic (inside the italic statement)", "convention", 6, old, new, note)


# ---------------------------------------------------------------- page 100
add(100, "page break 99/100 inside 'Notons d'abord | que l'hypothèse entraîne'",
    "p. 99 ends 'Notons d'abord', p. 100 begins 'que l'hypothèse entraîne' (page_099_s4.png, page_100_s1.png)",
    "blank line after \\oldpage[IV-4]{100} (and another before it, at the end of the p. 99 segment): a paragraph break inside the sentence",
    "marker", None,
    "\\oldpage[IV-4]{100}\n\nque l'hypothèse", "\\oldpage[IV-4]{100}\nque l'hypothèse",
    "BOUNDARY FIX (pp. 99/100). The marker is at the right place. Part 2 of 2: removes the blank line after the marker. "
    "Part 1 lies in the p. 99 segment (ega4-17-fr.tex, the line before the marker): page 99, old 'Notons d'abord\\n\\n' -> "
    "new 'Notons d'abord\\n'; the p. 95-99 checker may report it. Apply both, each once.")
om(100, "l. 1: '(f^*(Ω^1_{Y/k}))_x → (Ω^1_{X/k})_x'",
   "$(f^*(\\Omega^1_{Y/k}))_x\\to(\\Omega^1_{X/k})_x$", "$(f^*(\\varOmega^1_{Y/k}))_x\\to(\\varOmega^1_{X/k})_x$",
   scan="both Omegas italic (crop p100_s1_l1.png)")
om(100, "l. 3: 'f^*(Ω^1_{Y/k}) → Ω^1_{X/k} est surjectif'",
   "$f^*(\\Omega^1_{Y/k})\\to\\Omega^1_{X/k}$", "$f^*(\\varOmega^1_{Y/k})\\to\\varOmega^1_{X/k}$",
   scan="both Omegas italic (crop p100_s1_l3.png)")
bk(100, "'si l'on pose k'=k(x)'", "si l'on pose $k'=k(x)$", "si l'on pose $k'=\\boldsymbol{k}(x)$")
bk(100, "'tel que k(x')=k''", "tel que $k(x')=k'$", "tel que $\\boldsymbol{k}(x')=k'$")
b0(100, "'(resp. Y) (I, 6.4.2)'", "(resp. $Y$) (I, 6.4.2)", "(resp. $Y$) (\\textbf{I}, 6.4.2)")
add(100, "'Â→B̂ est surjectif (17.4.4, f''))'",
    "'surjectif' italic; label f'') italic with its parenthesis (crop p100_s2_surj.png)", "upright",
    "italics", None, "est surjectif (17.4.4, f''))", "est \\emph{surjectif} (17.4.4, \\emph{f'')})",
    "One edit for the word and the label (GLOBAL_ISSUES 88).")
add(100, "'Â→B̂ est aussi injectif (0, 16.3.10)'", "'injectif' italic (crop p100_s2_inj.png)", "upright",
    "italics", None, "est aussi injectif", "est aussi \\emph{injectif}")
b0(100, "'(0, 16.3.10)'", "(0, 16.3.10)", "(\\textbf{0}, 16.3.10)")
it(100, "'f est étale au point x (17.6.3, e''))'", "(17.6.3, e''))", "(17.6.3, \\emph{e'')})",
   scan="label e'') italic with its parenthesis (crop p100_s2_epp.png)")
up(100, "Corollaire (17.15.4): 'Sous les hypothèses générales de (17.15.3),'",
   "générales de (17.15.3), supposons", "générales de \\textup{(17.15.3)}, supposons",
   scan="reference upright (crop p100_s2_cor.png)", note=REF_UP)
bk(100, "Corollaire (17.15.4): 'que k(x) soit une extension'", "que $k(x)$ soit une extension",
   "que $\\boldsymbol{k}(x)$ soit une extension")
up(100, "Corollaire (17.15.4): 'une extension finie et séparable de k'",
   "finie et séparable de $k$ et que les germes", "\\textup{finie} et \\textup{séparable} de $k$ et que les germes",
   scan="'finie' and 'séparable' roman, 'et' italic (crop p100_s2_cor.png)",
   note="Words printed roman inside the italic statement.")
up(100, "Corollaire (17.15.4): 'Alors les conditions a), b), c) de (17.15.3) équivalent'",
   "les conditions a), b), c) de (17.15.3) équivalent",
   "les conditions \\textup{a)}, \\textup{b)}, \\textup{c)} de \\textup{(17.15.3)} équivalent",
   scan="labels and reference upright (crop p100_s2_cor.png)", note="Labels and reference printed upright inside the italic statement.")
up(100, "Corollaire (17.15.4), label d)", "\\item[d)] Les $n$ germes", "\\item[\\textup{d)}] Les $n$ germes",
   scan="'d)' upright")
up(100, "Corollaire (17.15.4), label d')", "\\item[d')] L'anneau", "\\item[\\textup{d$'$)}] L'anneau",
   scan="'d')' upright",
   note=LAB_UP + " Prime written d$'$ as in the edition's fixed labels (GLOBAL_ISSUES 88).")
add(100, "Corollaire (17.15.4) d'): 'pour cet anneau (0, 17.1.6).'", "bold 0; reference upright", "plain 0; italic",
    "convention", 2, "pour cet anneau (0, 17.1.6).", "pour cet anneau \\textup{(\\textbf{0}, 17.1.6)}.",
    "Bold 0 (convention 2) and roman reference inside an italic statement (convention 6), one edit.")
it(100, "proof of (17.15.4): 'En effet, d') entraîne trivialement d).'",
   "En effet, d') entraîne trivialement d).", "En effet, \\emph{d')} entraîne trivialement \\emph{d)}.")
bk(100, "proof of (17.15.4): 'comme k(x) est une extension finie'", "comme $k(x)$ est une extension finie",
   "comme $\\boldsymbol{k}(x)$ est une extension finie")
add(100, "proof of (17.15.4): 'Ω^1_{k(x)/k}=0'", "bold upright k in the subscript (crop p100_s3_omega_z.png)",
    "plain k", "convention", 1, "$\\Omega^1_{k(x)/k}=0$", "$\\Omega^1_{\\mathbf{k}(x)/k}=0$", SUBK)
b0(100, "'(0, 20.6.20)'", "(0, 20.6.20)", "(\\textbf{0}, 20.6.20)")
bk(100, "proof of (17.15.4): 'k(x)=O_{X,x}/m_x'", "et $k(x)=\\sh{O}_{X,x}/\\mathfrak m_x$",
   "et $\\boldsymbol{k}(x)=\\sh{O}_{X,x}/\\mathfrak m_x$")
b0(100, "'(0, 19.6.1)'", "(0, 19.6.1)", "(\\textbf{0}, 19.6.1)")
b0(100, "'(0, 20.5.14.1)'", "(0, 20.5.14.1)", "(\\textbf{0}, 20.5.14.1)")
add(100, "proof of (17.15.4): 'A=k, B=O_{X,x}, 𝔎=m_x'",
    "Fraktur K (crop p100_s3_frak2.png; same glyph as the 𝔎 of p. 14, crops_010_014/p14_KJ.png)",
    "\\mathfrak{R}", "symbol", None, "$\\mathfrak{R}=\\mathfrak m_x$", "$\\mathfrak{K}=\\mathfrak m_x$",
    "Wrong letter (GLOBAL_ISSUES 63): the ideal 𝔎 of the exact sequence (0, 20.5.14.1).")
om(100, "display δ: '(Ω^1_{X/k})_x'", "\\xrightarrow{\\sim}(\\Omega^1_{X/k})_x",
   "\\xrightarrow{\\sim}(\\varOmega^1_{X/k})_x", scan="italic Omega (crop p100_s3_delta.png)")
bk(100, "display δ: '⊗_{O_{X,x}} k(x)'", "\\otimes_{\\sh{O}_{X,x}}k(x).\n\\]",
   "\\otimes_{\\sh{O}_{X,x}}\\boldsymbol{k}(x).\n\\]")
it(100, "'l'équivalence des conditions c) et d)'", "des conditions c) et d), compte",
   "des conditions \\emph{c)} et \\emph{d)}, compte")
b0(100, "'point fermé de X (I, 6.4.2), et n éléments'", "fermé de $X$ (I, 6.4.2), et", "fermé de $X$ (\\textbf{I}, 6.4.2), et")
b0(100, "'paramètres pour O_{X,x} (0, 17.1.6), ce qui'", "pour $\\sh{O}_{X,x}$ (0, 17.1.6), ce qui",
   "pour $\\sh{O}_{X,x}$ (\\textbf{0}, 17.1.6), ce qui")
it(100, "'ce qui prouve que a) entraîne d').'", "ce qui prouve que a) entraîne d').",
   "ce qui prouve que \\emph{a)} entraîne \\emph{d')}.")
up(100, "Proposition (17.15.5), label a)", "\\item[a)] $X$ est lisse", "\\item[\\textup{a)}] $X$ est lisse", scan="'a)' upright")
up(100, "Proposition (17.15.5), label b)", "\\item[b)] $X$ est différentiellement",
   "\\item[\\textup{b)}] $X$ est différentiellement", scan="'b)' upright")
up(100, "Proposition (17.15.5), label c)", "\\item[c)]", "\\item[\\textup{c)}]", scan="'c)' upright")
om(100, "Proposition (17.15.5) c): '(Ω^1_{X/k})_x est un O_{X,x}-module libre'",
   "$(\\Omega^1_{X/k})_x$ est un $\\sh{O}_{X,x}$-module libre", "$(\\varOmega^1_{X/k})_x$ est un $\\sh{O}_{X,x}$-module libre")
up(100, "Proposition (17.15.5), label d)", "\\item[d)] $(", "\\item[\\textup{d)}] $(", scan="'d)' upright")
om(100, "Proposition (17.15.5) d): '(Ω^1_{X/k})_x est un O_{X,x}-module admettant'",
   "$(\\Omega^1_{X/k})_x$ est un $\\sh{O}_{X,x}$-module admettant",
   "$(\\varOmega^1_{X/k})_x$ est un $\\sh{O}_{X,x}$-module admettant")

# ---------------------------------------------------------------- page 101
up(101, "Proposition (17.15.5), label e)", "\\item[e)]", "\\item[\\textup{e)}]", scan="'e)' upright")
add(101, "proof of (17.15.5): 'régulier pour toute extension k' de k'", "'toute' italic (page_101_s1.png)", "upright",
    "italics", None, "pour toute extension", "pour \\emph{toute} extension")
it(101, "proof of (17.15.5): 'a) implique e). Inversement e) implique a)'",
   "ce qui prouve que a) implique e). Inversement e) implique a), car",
   "ce qui prouve que \\emph{a)} implique \\emph{e)}. Inversement \\emph{e)} implique \\emph{a)}, car")
it(101, "proof of (17.15.5): 'a) entraîne c) (17.10.2); c) implique d) ... d) implique a)'",
   "que a) entraîne c) (17.10.2); c) implique d) trivialement et le fait que d) implique a) résulte",
   "que \\emph{a)} entraîne \\emph{c)} (17.10.2); \\emph{c)} implique \\emph{d)} trivialement et le fait que \\emph{d)} implique \\emph{a)} résulte")
b0(101, "'(0, 20.4.7)'", "(0, 20.4.7)", "(\\textbf{0}, 20.4.7)")
it(101, "'(17.15.3, c))'", "(17.15.3, c))", "(17.15.3, \\emph{c)})", scan="label c) italic")
it(101, "proof of (17.15.5): 'a) implique b) (17.12.4). Inversement, pour prouver que b) entraîne a)'",
   "vu que a) implique b) (17.12.4). Inversement, pour prouver que b) entraîne a), on",
   "vu que \\emph{a)} implique \\emph{b)} (17.12.4). Inversement, pour prouver que \\emph{b)} entraîne \\emph{a)}, on")
add(101, "proof of (17.15.5): 'au cas où x est rationnel sur k, en considérant'",
    "'rationnel sur' italic (crop p101_s2_ratl.png); the later 'Supposant donc x rationnel sur k' is roman (crop p101_s2_suppos.png)",
    "upright", "italics", None, "où $x$ est rationnel sur $k$, en considérant",
    "où $x$ est \\emph{rationnel sur $k$}, en considérant", "Written as on p. 100 (\\emph{rationnel sur $k$}).")
add(101, "proof of (17.15.5): 'k(x')=k'=k(x)'", "bold italic k twice", "plain k", "convention", 1,
    "$k(x')=k'=k(x)$", "$\\boldsymbol{k}(x')=k'=\\boldsymbol{k}(x)$", "Two occurrences, one edit.")
it(101, "proof of (17.15.5): 'de l'hypothèse b) et de (17.12.5)'", "l'hypothèse b) et de", "l'hypothèse \\emph{b)} et de",
   scan="label b) italic")
om(101, "Corollaire (17.15.6): 'le O_X-Module Ω^1_{X/k} soit localement libre'",
   "le $\\sh{O}_X$-Module $\\Omega^1_{X/k}$ soit", "le $\\sh{O}_X$-Module $\\varOmega^1_{X/k}$ soit")
add(101, "Corollaire (17.15.6): '(cette dernière condition ... corps parfait et X un préschéma réduit)'",
    "the whole parenthesis roman inside the italic statement, with 'parfait' and 'réduit' italic (crop p101_s2_cor6.png)",
    "italic throughout (corollary environment)", "convention", 6,
    "(cette dernière condition étant automatiquement vérifiée si $k$ est un corps parfait et $X$ un préschéma réduit)",
    "\\textup{(cette dernière condition étant automatiquement vérifiée si $k$ est un corps \\emph{parfait} et $X$ un préschéma \\emph{réduit})}",
    "Roman parenthesis inside the italic statement; \\emph inside \\textup keeps 'parfait' and 'réduit' italic as printed.")
om(101, "proof of (17.15.6): 'il résulte de (17.10.2) que Ω^1_{X/k} est localement libre'",
   "(17.10.2) que $\\Omega^1_{X/k}$ est localement libre", "(17.10.2) que $\\varOmega^1_{X/k}$ est localement libre")
b0(101, "'(0, 19.6.1)'", "(0, 19.6.1)", "(\\textbf{0}, 19.6.1)")
om(101, "proof of (17.15.6): 'donc Ω^1_{X/k} localement libre de rang constant n'",
   "donc $\\Omega^1_{X/k}$ localement libre", "donc $\\varOmega^1_{X/k}$ localement libre", scan="italic Omega (crop p101_s3_rg.png)")
add(101, "proof of (17.15.6): 'rg_{k(x)} Ω^1_{k(x)/k}=n'", "bold upright k in both subscripts (crop p101_s3_rg.png)",
    "plain k", "convention", 1, "\\operatorname{rg}_{k(x)}\\Omega^1_{k(x)/k}",
    "\\operatorname{rg}_{\\mathbf{k}(x)}\\Omega^1_{\\mathbf{k}(x)/k}", SUBK + " Two occurrences, one edit.")
add(101, "proof of (17.15.6): 'puisque O_{X,x}=k(x); comme par hypothèse k(x) est'", "bold italic k twice", "plain k",
    "convention", 1, "puisque $\\sh{O}_{X,x}=k(x)$; comme par hypothèse $k(x)$ est",
    "puisque $\\sh{O}_{X,x}=\\boldsymbol{k}(x)$; comme par hypothèse $\\boldsymbol{k}(x)$ est", "Two occurrences, one edit.")
add(101, "proof of (17.15.6): 'Υ_{k(x)/k}=0'", "bold upright k in the subscript (crop p101_s3_rg.png)", "plain k",
    "convention", 1, "$\\Upsilon_{k(x)/k}=0$", "$\\Upsilon_{\\mathbf{k}(x)/k}=0$", "Subscript: bold upright k (GLOBAL_ISSUES 48).")
b0(101, "'(0, 20.6.3)'", "(0, 20.6.3)", "(\\textbf{0}, 20.6.3)")
bk(101, "proof of (17.15.6): 'donc deg.tr_k k(x)=n'", "donc $\\deg.\\operatorname{tr}_k k(x)=n$",
   "donc $\\deg.\\operatorname{tr}_k \\boldsymbol{k}(x)=n$")
b0(101, "'(0, 21.7.1)'", "(0, 21.7.1)", "(\\textbf{0}, 21.7.1)")
add(101, "proof of (17.15.6): 'dimension n (5.2.1), et on conclut que X'", "'et on conclut' (crop p101_s3_onconclut.png)",
    "'et l'on conclut'", "word", None, "et l'on conclut que", "et on conclut que")
it(101, "proof of (17.15.6): 'en vertu de ce que c) entraîne a) dans (17.15.5)'", "de ce que c) entraîne a) dans",
   "de ce que \\emph{c)} entraîne \\emph{a)} dans")
up(101, "Corollaire (17.15.7): 'Si k est de caractéristique 0,'", "de caractéristique 0, alors",
   "de caractéristique \\textup{0}, alors", scan="the figure 0 roman (crop p101_s3_alors.png)",
   note="Figure printed roman inside the italic statement.")
om(101, "Corollaire (17.15.7): '(Ω^1_{X/k})_x soit un O_{X,x}-module libre'", "que $(\\Omega^1_{X/k})_x$ soit un",
   "que $(\\varOmega^1_{X/k})_x$ soit un")
it(101, "'l'équivalence de b) et a) dans (17.15.5)'", "l'équivalence de b) et a) dans", "l'équivalence de \\emph{b)} et \\emph{a)} dans")
add(101, "Proposition (17.15.8): 'de sorte que n—r=deg.tr_k k(x)'", "long dash for the minus (crop p101_s4_nr.png)", "-",
    "convention", 7, "de sorte que $n-r", "de sorte que $n\\setmin r", DASH)
bk(101, "Proposition (17.15.8): 'n—r=deg.tr_k k(x)'", "=\\deg.\\operatorname{tr}_k k(x)$",
   "=\\deg.\\operatorname{tr}_k \\boldsymbol{k}(x)$")
up(101, "Proposition (17.15.8): '(5.2.3). Soit'", "(5.2.3). Soit", "\\textup{(5.2.3)}. Soit",
   scan="reference upright (crop p101_s4_prop.png)", note=REF_UP)
bk(101, "Proposition (17.15.8): 'et que k(x) est une extension séparable de k)'",
   "et que $k(x)$ est une extension séparable de $k$):", "et que $\\boldsymbol{k}(x)$ est une extension séparable de $k$):",
   note="The parentheses '(et impliquent ... de k)' are italic in the print, as in the TeX (crops p101_s4_paren_open.png, p101_s4_paren_close.png).")
up(101, "Proposition (17.15.8), label a)", "\\item[a)] $f$ est étale", "\\item[\\textup{a)}] $f$ est étale", scan="'a)' upright")

# ---------------------------------------------------------------- page 102
up(102, "Proposition (17.15.8), label b)", "\\item[b)] Les $(g_i)_x$ tels que", "\\item[\\textup{b)}] Les $(g_i)_x$ tels que",
   scan="'b)' upright")
add(102, "Proposition (17.15.8) b): '(et par suite forment un système régulier de paramètres pour O_{X,x} (0, 17.1.6))'",
    "the whole parenthesis roman inside the italic statement, bold 0 (crop p102_s1_b.png)", "italic; plain 0",
    "convention", 6,
    "(et par suite forment un système régulier de paramètres pour $\\sh{O}_{X,x}$ (0, 17.1.6))",
    "\\textup{(et par suite forment un système régulier de paramètres pour $\\sh{O}_{X,x}$ (\\textbf{0}, 17.1.6))}",
    "Roman parenthesis inside the italic statement (convention 6) and bold 0 (convention 2), one edit.")
add(102, "Proposition (17.15.8) b): 'les images dans Ω^1_{k(x)/k} des éléments'", "bold upright k in the subscript", "plain k",
    "convention", 1, "dans $\\Omega^1_{k(x)/k}$ des éléments", "dans $\\Omega^1_{\\mathbf{k}(x)/k}$ des éléments", SUBK)
add(102, "Proposition (17.15.8) b): 'des éléments (d_{X/k}g_j)_x pour r+1⩽j⩽n'",
    "index j: g_j and r+1⩽j⩽n (crops p102_s1_dgj.png, p102_s1_rj.png)", "index i", "formula", None,
    "$(d_{X/k}g_i)_x$ pour $r+1\\leq i\\leq n$", "$(d_{X/k}g_j)_x$ pour $r+1\\leq j\\leq n$",
    "The print uses j here (also in (17.15.9) d)); the proof uses i.")
add(102, "Proposition (17.15.8) b), end: 'engendrent Ω^1_{k(x)/k}.'", "bold upright k in the subscript", "plain k",
    "convention", 1, "engendrent $\\Omega^1_{k(x)/k}$.\n\\end{enumerate}\n\\end{proposition}",
    "engendrent $\\Omega^1_{\\mathbf{k}(x)/k}$.\n\\end{enumerate}\n\\end{proposition}", SUBK)
b0(102, "'On a en effet (0, 20.5.12.1)'", "(0, 20.5.12.1)", "(\\textbf{0}, 20.5.12.1)")
bk(102, "'la suite exacte de k(x)-modules'", "de $k(x)$-modules", "de $\\boldsymbol{k}(x)$-modules")
om(102, "display (17.15.8.1): '(Ω^1_{X/k})_x'", "\\tag{17.15.8.1}\n\\mathfrak m_x/\\mathfrak m_x^2\\to(\\Omega^1_{X/k})_x",
   "\\tag{17.15.8.1}\n\\mathfrak m_x/\\mathfrak m_x^2\\to(\\varOmega^1_{X/k})_x")
add(102, "display (17.15.8.1): '⊗ k(x) → Ω^1_{k(x)/k} → 0'",
    "bold italic k after ⊗; bold upright k in the subscript of the (upright) Ω", "plain k twice", "convention", 1,
    "k(x)\\to\\Omega^1_{k(x)/k}\\to0\n\\]\net la condition",
    "\\boldsymbol{k}(x)\\to\\Omega^1_{\\mathbf{k}(x)/k}\\to0\n\\]\net la condition",
    "Two occurrences, one edit (GLOBAL_ISSUES 48 for the subscript).")
it(102, "'et la condition b) entraîne par suite'", "et la condition b) entraîne par suite",
   "et la condition \\emph{b)} entraîne par suite", scan="label b) italic")
om(102, "'engendrent (Ω^1_{X/k})_x compte tenu du lemme de Nakayama'", "engendrent $(\\Omega^1_{X/k})_x$ compte tenu",
   "engendrent $(\\varOmega^1_{X/k})_x$ compte tenu")
it(102, "'le fait que b) implique a) résulte donc de (17.15.3)'", "le fait que b) implique a) résulte donc",
   "le fait que \\emph{b)} implique \\emph{a)} résulte donc")
it(102, "'Inversement, si a) est vérifiée'", "Inversement, si a) est vérifiée", "Inversement, si \\emph{a)} est vérifiée",
   scan="label a) italic")
om(102, "'forment une base de (Ω^1_{X/k})_x en vertu de (17.15.3)'", "base de $(\\Omega^1_{X/k})_x$ en vertu",
   "base de $(\\varOmega^1_{X/k})_x$ en vertu")
bk(102, "'l'image de (g_i)_x dans k(x)'", "dans $k(x)$, on conclut", "dans $\\boldsymbol{k}(x)$, on conclut")
add(102, "'les dt_i engendrent Ω^1_{k(x)/k} pour 1⩽i⩽n'", "bold upright k in the subscript", "plain k", "convention", 1,
    "engendrent $\\Omega^1_{k(x)/k}$ pour", "engendrent $\\Omega^1_{\\mathbf{k}(x)/k}$ pour", SUBK)
add(102, "'engendrent déjà Ω^1_{k(x)/k}'", "bold upright k in the subscript", "plain k", "convention", 1,
    "engendrent déjà $\\Omega^1_{k(x)/k}$", "engendrent déjà $\\Omega^1_{\\mathbf{k}(x)/k}$", SUBK)
bk(102, "'Comme deg.tr_k k(x)=n—r'", "Comme $\\deg.\\operatorname{tr}_k k(x)", "Comme $\\deg.\\operatorname{tr}_k \\boldsymbol{k}(x)")
add(102, "'Comme deg.tr_k k(x)=n—r, il suit'", "long dash for the minus (crop p102_s2_nr.png)", "-", "convention", 7,
    "=n-r$, il suit", "=n\\setmin r$, il suit", DASH)
b0(102, "'l'égalité de Cartier (0, 21.7.1)'", "(0, 21.7.1)", "(\\textbf{0}, 21.7.1)")
add(102, "'que Υ_{k(x)/k}=0, donc k(x) est une extension séparable'",
    "bold upright k in the subscript of Υ; bold italic k in k(x)", "plain k twice", "convention", 1,
    "que $\\Upsilon_{k(x)/k}=0$, donc $k(x)$ est une extension",
    "que $\\Upsilon_{\\mathbf{k}(x)/k}=0$, donc $\\boldsymbol{k}(x)$ est une extension",
    "Two occurrences, one edit (GLOBAL_ISSUES 48 for the subscript).")
b0(102, "'séparable de k (0, 20.6.3), et la suite'", "(0, 20.6.3), et la suite", "(\\textbf{0}, 20.6.3), et la suite")
bk(102, "'la suite de k(x)-espaces vectoriels'", "de $k(x)$-espaces vectoriels", "de $\\boldsymbol{k}(x)$-espaces vectoriels")
om(102, "display (17.15.8.2): '(Ω^1_{X/k})_x'", "\\tag{17.15.8.2}\n0\\to\\mathfrak m_x/\\mathfrak m_x^2\\to(\\Omega^1_{X/k})_x",
   "\\tag{17.15.8.2}\n0\\to\\mathfrak m_x/\\mathfrak m_x^2\\to(\\varOmega^1_{X/k})_x")
add(102, "display (17.15.8.2): '⊗ k(x) → Ω^1_{k(x)/k} → 0'",
    "bold italic k after ⊗; bold upright k in the subscript of the (upright) Ω", "plain k twice", "convention", 1,
    "k(x)\\to\\Omega^1_{k(x)/k}\\to0\n\\]\nest exacte",
    "\\boldsymbol{k}(x)\\to\\Omega^1_{\\mathbf{k}(x)/k}\\to0\n\\]\nest exacte",
    "Two occurrences, one edit (GLOBAL_ISSUES 48 for the subscript).")
add(102, "'est exacte ((0, 20.5.14) et (0, 19.6.1))'", "bold 0 twice", "plain 0", "convention", 2,
    "((0, 20.5.14) et (0, 19.6.1))", "((\\textbf{0}, 20.5.14) et (\\textbf{0}, 19.6.1))", "Two occurrences, one edit.")
add(102, "'forment une base de Ω^1_{k(x)/k}, donc aucun'", "bold upright k in the subscript", "plain k", "convention", 1,
    "base de $\\Omega^1_{k(x)/k}$, donc aucun", "base de $\\Omega^1_{\\mathbf{k}(x)/k}$, donc aucun", SUBK)
it(102, "'ce qui achève de prouver que a) implique b).'", "achève de prouver que a) implique b).",
   "achève de prouver que \\emph{a)} implique \\emph{b)}.")
up(102, "Corollaire (17.15.9), label a)", "\\item[a)] L'anneau", "\\item[\\textup{a)}] L'anneau", scan="'a)' upright")
bk(102, "Corollaire (17.15.9) a): 'et k(x) est une extension séparable de k'", "régulier et $k(x)$ est une extension séparable",
   "régulier et $\\boldsymbol{k}(x)$ est une extension séparable")
up(102, "Corollaire (17.15.9), label b)", "\\item[b)] $X$ est lisse", "\\item[\\textup{b)}] $X$ est lisse", scan="'b)' upright")
om(102, "Corollaire (17.15.9) b), display: '(Ω^1_{X/k})_x'", "\\[\n  \\mathfrak m_x/\\mathfrak m_x^2\\to(\\Omega^1_{X/k})_x",
   "\\[\n  \\mathfrak m_x/\\mathfrak m_x^2\\to(\\varOmega^1_{X/k})_x")
bk(102, "Corollaire (17.15.9) b), display: '⊗_{O_{X,x}} k(x)'", "\\otimes_{\\sh{O}_{X,x}}k(x)\n  \\]",
   "\\otimes_{\\sh{O}_{X,x}}\\boldsymbol{k}(x)\n  \\]")
up(102, "Corollaire (17.15.9), label c)", "\\item[c)] Il existe", "\\item[\\textup{c)}] Il existe", scan="'c)' upright")
up(102, "Corollaire (17.15.9) c): '(cf. (17.15.8))'", "(cf. (17.15.8))", "\\textup{(cf. (17.15.8))}",
   scan="the whole parenthesis upright (crop p102_s3_c.png)", note="'cf.' and the reference printed upright inside the italic statement.")
up(102, "Corollaire (17.15.9), label d)", "\\item[d)] Il existe", "\\item[\\textup{d)}] Il existe", scan="'d)' upright")
up(102, "Corollaire (17.15.9) d): 'n sections g_i (1⩽i⩽n) de O_X'", "$g_i$ ($1\\leq i\\leq n$) de",
   "$g_i$ \\textup{(}$1\\leq i\\leq n$\\textup{)} de", scan="both parentheses upright (crop p102_s3_d_paren.png)",
   note="Parentheses upright around a formula inside the italic statement (as p. 21, findings_020_024).")
add(102, "Corollaire (17.15.9) d): 'les images dans Ω^1_{k(x)/k} des (d_{U/k}g_j)_x'", "bold upright k in the subscript",
    "plain k", "convention", 1, "dans $\\Omega^1_{k(x)/k}$ des $(d_{U/k}", "dans $\\Omega^1_{\\mathbf{k}(x)/k}$ des $(d_{U/k}", SUBK)
add(102, "Corollaire (17.15.9) d): '(d_{U/k}g_j)_x pour r+1⩽j⩽n'", "index j: g_j and r+1⩽j⩽n (crop p102_s3_d.png)",
    "index i", "formula", None, "$(d_{U/k}g_i)_x$ pour $r+1\\leq i\\leq n$", "$(d_{U/k}g_j)_x$ pour $r+1\\leq j\\leq n$",
    "As in (17.15.8) b).")
add(102, "Corollaire (17.15.9) d), end: 'engendrent Ω^1_{k(x)/k}.'", "bold upright k in the subscript", "plain k",
    "convention", 1, "engendrent $\\Omega^1_{k(x)/k}$.\n\\end{enumerate}\n\\end{corollary}",
    "engendrent $\\Omega^1_{\\mathbf{k}(x)/k}$.\n\\end{enumerate}\n\\end{corollary}", SUBK)
it(102, "proof of (17.15.9): 'L'équivalence de c) et d) résulte de (17.15.8)'", "L'équivalence de c) et d) résulte",
   "L'équivalence de \\emph{c)} et \\emph{d)} résulte")
it(102, "proof of (17.15.9): 'que la condition c) entraîne que X'", "que la condition c) entraîne que",
   "que la condition \\emph{c)} entraîne que", scan="label c) italic")
it(102, "proof of (17.15.9): 'donc c) entraîne b). La condition b) entraîne'",
   "donc c) entraîne b). La condition b) entraîne", "donc \\emph{c)} entraîne \\emph{b)}. La condition \\emph{b)} entraîne")
om(102, "proof of (17.15.9): 'en outre, (Ω^1_{X/k})_x est alors un O_{X,x}-module libre'",
   "en outre, $(\\Omega^1_{X/k})_x$ est alors", "en outre, $(\\varOmega^1_{X/k})_x$ est alors")
add(102, "proof of (17.15.9): 'comme la suite (17.15.7.2) est exacte par hypothèse'",
    "(17.15.7.2) (crop p102_s4_ref.png)", "(17.15.7.2): the TeX keeps the printed reading", "misprint_in_print", None,
    None, None,
    "There is no (17.15.7.2): the sequence that b) makes exact is (17.15.8.2), as two lines earlier ('la suite (17.15.8.2) est exacte, donc c) entraîne b)'). Not in the errata (Liste 3).",
    corrected="(17.15.8.2)", fix_null=True)
add(102, "proof of (17.15.9): 'hypothèse, Ω^1_{k(x)/k} est de rang'", "bold upright k in the subscript", "plain k",
    "convention", 1, "hypothèse, $\\Omega^1_{k(x)/k}$ est de", "hypothèse, $\\Omega^1_{\\mathbf{k}(x)/k}$ est de", SUBK)
add(102, "proof of (17.15.9): 'de rang n—r=deg.tr_k k(x)'", "long dash for the minus (crop p102_s4_nr.png)", "-",
    "convention", 7, "rang $n-r=", "rang $n\\setmin r=", DASH)
bk(102, "proof of (17.15.9): 'n—r=deg.tr_k k(x) et l'égalité'", "\\operatorname{tr}_k k(x)$ et l'égalité",
   "\\operatorname{tr}_k \\boldsymbol{k}(x)$ et l'égalité")
add(102, "proof of (17.15.9): 'montre que Υ_{k(x)/k}=0, donc k(x) est séparable sur k'",
    "bold upright k in the subscript of Υ; bold italic k in k(x)", "plain k twice", "convention", 1,
    "montre que $\\Upsilon_{k(x)/k}=0$, donc $k(x)$ est séparable",
    "montre que $\\Upsilon_{\\mathbf{k}(x)/k}=0$, donc $\\boldsymbol{k}(x)$ est séparable",
    "Two occurrences, one edit (GLOBAL_ISSUES 48 for the subscript).")
b0(102, "'séparable sur k (0, 20.6.3); ainsi'", "(0, 20.6.3); ainsi", "(\\textbf{0}, 20.6.3); ainsi")
add(102, "page break 102/103 inside 'Enfin, si a) | est vérifiée'",
    "p. 102 ends 'Enfin, si a)', p. 103 begins 'est vérifiée, on déduit' (page_102_s4.png, page_103_s1.png)",
    "blank line before \\oldpage[IV-4]{103} (and another after it): a paragraph break inside the sentence",
    "marker", None, "si a)\n\n", "si a)\n",
    "The marker is at the right place. Part 1 of 2: the first p. 103 finding removes the blank line after \\oldpage[IV-4]{103}; apply both. "
    "Apply this edit BEFORE the next finding (italic labels), whose 'old' it leaves intact.")
it(102, "proof of (17.15.9): 'ainsi b) entraîne a). Enfin, si a)'", "ainsi b) entraîne a). Enfin, si a)",
   "ainsi \\emph{b)} entraîne \\emph{a)}. Enfin, si \\emph{a)}",
   note=LAB_IT + " Apply AFTER the marker finding just before (same spot; its 'old' 'si a)\\n\\n' would not match after this edit).")

# ---------------------------------------------------------------- page 103
add(103, "top of page_103.tex: blank line after \\oldpage[IV-4]{103}", "p. 103 begins mid-sentence ('est vérifiée')",
    "blank line between the marker and 'est vérifiée'", "marker", None,
    "\\oldpage[IV-4]{103}\n\nest vérifiée", "\\oldpage[IV-4]{103}\nest vérifiée",
    "Part 2 of 2 with the marker finding at the end of p. 102; both blank lines must go.")
add(103, "l. 1: 'Cartier que Ω^1_{k(x)/k} est de rang n—r'", "bold upright k in the subscript (crop p103_s1_nr.png)",
    "plain k", "convention", 1, "Cartier que $\\Omega^1_{k(x)/k}$", "Cartier que $\\Omega^1_{\\mathbf{k}(x)/k}$", SUBK)
add(103, "l. 1: 'est de rang n—r.'", "long dash for the minus (crop p103_s1_nr.png)", "-", "convention", 7,
    "est de rang $n-r$.", "est de rang $n\\setmin r$.", DASH)
it(103, "'vérifiant les conditions de d) est immédiate'", "conditions de d) est immédiate", "conditions de \\emph{d)} est immédiate",
   scan="label d) italic")
om(103, "Remarques (17.15.10) (i): 'il ne suffit pas que Ω^1_{X/k} soit localement libre'",
   "il ne suffit pas que $\\Omega^1_{X/k}$", "il ne suffit pas que $\\varOmega^1_{X/k}$")
bk(103, "Remarques (17.15.10) (ii): 'sans que k(x) soit séparable sur k'", "sans que $k(x)$ soit séparable",
   "sans que $\\boldsymbol{k}(x)$ soit séparable")
add(103, "Remarques (17.15.10) (ii): '(T^p—λ)'", "long dash for the minus (crop p103_s1_lambda.png)", "-", "convention", 7,
    "$(T^p-\\lambda)$", "$(T^p\\setmin\\lambda)$", DASH)
add(103, "Remarques (17.15.10) (ii): 'λ∈k—k^p'", "long dash (set difference) (crop p103_s1_lambda.png)", "minus sign",
    "convention", 7, "$\\lambda\\in k-k^p$", "$\\lambda\\in k\\setmin k^p$", "")
bk(103, "Remarques (17.15.10) (iii): 'points fermés de X tels que k(x) soit séparable'", "fermés de $X$ tels que $k(x)$",
   "fermés de $X$ tels que $\\boldsymbol{k}(x)$")
add(103, "Remarques (17.15.10) (iii): 'soit séparable (et fini) sur k est dense dans X'",
    "'séparable' and 'dense' italic (crop p103_s2_iii.png)", "upright (italic only through the remarks environment)",
    "italics", None, "soit séparable (et fini) sur $k$ est dense dans",
    "soit \\emph{séparable} (et fini) sur $k$ est \\emph{dense} dans", REM)
add(103, "Remarques (17.15.10) (iii): 'où g est étale (17.11.4)'", "'étale' italic (crop p103_s2_etale.png)",
    "upright (italic only through the remarks environment)", "italics", None, "où $g$ est étale", "où $g$ est \\emph{étale}", REM)
add(103, "Remarques (17.15.10) (iii): 'qui sont rationnels sur k'", "'rationnels' italic (crop p103_s2_ratl.png)",
    "upright (italic only through the remarks environment)", "italics", None, "qui sont rationnels sur",
    "qui sont \\emph{rationnels} sur", REM)
add(103, "Remarques (17.15.10) (iii): 'k(x) est séparable sur k(y)=k'", "bold italic k twice", "plain k", "convention", 1,
    "et $k(x)$ est séparable sur $k(y)=k$", "et $\\boldsymbol{k}(x)$ est séparable sur $\\boldsymbol{k}(y)=k$",
    "Two occurrences, one edit; the final k is light, as in the TeX.")
up(103, "Proposition (17.15.11), label a)", "\\item[a)] $X$ est étale", "\\item[\\textup{a)}] $X$ est étale", scan="'a)' upright")
up(103, "Proposition (17.15.11), label b)", "\\item[b)] $X$ est non ramifié", "\\item[\\textup{b)}] $X$ est non ramifié",
   scan="'b)' upright")
up(103, "Proposition (17.15.11), label c)", "\\item[c)] $X$ est isomorphe", "\\item[\\textup{c)}] $X$ est isomorphe",
   scan="'c)' upright")
it(103, "'compte tenu de ce que la condition b) implique ici'", "la condition b) implique ici", "la condition \\emph{b)} implique ici",
   scan="label b) italic")
bk(103, "Proposition (17.15.12): 'X soit réduit en ce point et que k(x) soit'", "en ce point et que $k(x)$",
   "en ce point et que $\\boldsymbol{k}(x)$")
bk(103, "Proposition (17.15.12): 'pour tout point maximal x de X, k(x) soit une extension'", "de $X$, $k(x)$ soit une extension",
   "de $X$, $\\boldsymbol{k}(x)$ soit une extension")
add(103, "proof of (17.15.12): 'donc un corps, égal à k(x)'", "'corps' italic (crop p103_s3_corps.png)", "upright",
    "italics", None, "donc un corps,", "donc un \\emph{corps},")
add(103, "proof of (17.15.12): 'égal à k(x); en outre (17.15.1), k(x)⊗_k k''", "bold italic k twice", "plain k",
    "convention", 1, "égal à $k(x)$; en outre (17.15.1), $k(x)\\otimes_k k'$",
    "égal à $\\boldsymbol{k}(x)$; en outre (17.15.1), $\\boldsymbol{k}(x)\\otimes_k k'$", "Two occurrences, one edit.")
bk(103, "proof of (17.15.12): 'donc k(x) doit être une extension séparable'", "donc $k(x)$ doit être",
   "donc $\\boldsymbol{k}(x)$ doit être")
bk(103, "proof of (17.15.13): 'de X_{(k')}, k(x') est une extension séparable de k''", "$X_{(k')}$, $k(x')$ est",
   "$X_{(k')}$, $\\boldsymbol{k}(x')$ est")

# ---------------------------------------------------------------- page 104
add(104, "page break 103/104 inside the word 'mor-|phisme'",
    "p. 103 ends 'Mais le mor-', p. 104 begins 'phisme X_{(k')}→X' (page_103_s4.png, page_104_s1.png)",
    "\\oldpage[IV-4]{104} stands before 'morphisme'", "marker", None,
    "\\oldpage[IV-4]{104}morphisme", "mor%\n\\oldpage[IV-4]{104}\nphisme",
    "Moves the marker three letters later, to the printed word break, written as $Z$-mor%|phisme (p. 58) and consi%|dérer (p. 93). "
    "After the edit 'mor%' ends the p. 103 segment ('Mais le mor%').")
add(104, "Proposition (17.15.14): 'le normalisé (II, 6.3.8) de'", "bold II; reference upright", "plain II; italic",
    "convention", 2, "le normalisé (II, 6.3.8) de", "le normalisé \\textup{(\\textbf{II}, 6.3.8)} de",
    "Bold II (convention 2) and roman reference inside an italic statement (convention 6), one edit.")
add(104, "Lemme (17.15.14.1): 'au normalisé X' de X (II, 6.3.8), il faut'", "bold II; reference upright", "plain II; italic",
    "convention", 2, "de $X$ (II, 6.3.8), il faut", "de $X$ \\textup{(\\textbf{II}, 6.3.8)}, il faut",
    "Bold II (convention 2) and roman reference inside an italic statement (convention 6), one edit.")
up(104, "Lemme (17.15.14.1), label (i)", "\\item[(i)] $Y$ est normal", "\\item[\\textup{(i)}] $Y$ est normal",
   scan="'(i)' upright (crop p104_s2_labels.png)", note="Roman-numeral label upright in the print (GLOBAL_ISSUES 16).")
up(104, "Lemme (17.15.14.1), label (ii)", "\\item[(ii)] $f$ est un morphisme", "\\item[\\textup{(ii)}] $f$ est un morphisme",
   scan="'(ii)' upright (crop p104_s2_labels.png)", note="Roman-numeral label upright in the print (GLOBAL_ISSUES 16).")
add(104, "Lemme (17.15.14.1): 'Lorsqu'il existe dans X un ouvert dense et normal' after the list",
    "new indented paragraph (crop p104_s2_lorsq.png)", "text follows \\end{enumerate} directly (no indent)", "other", None,
    "\\end{enumerate}\nLorsqu'il existe", "\\end{enumerate}\n\nLorsqu'il existe",
    "Paragraph break as printed (GLOBAL_ISSUES 80 pattern).")
up(104, "Lemme (17.15.14.1): 'lorsque X est excellent (7.8.3),'", "excellent (7.8.3), en particulier",
   "excellent \\textup{(7.8.3)}, en particulier", scan="reference upright (crop p104_s2_783.png); the parentheses of '(ce qui ... corps)' are italic, as in the TeX",
   note=REF_UP)
up(104, "Lemme (17.15.14.1): 'on peut remplacer la condition (ii) par la suivante'", "la condition (ii) par la suivante",
   "la condition \\textup{(ii)} par la suivante", scan="'(ii)' upright (crop p104_s2_lorsq.png)",
   note="Label printed upright inside the italic statement.")
up(104, "Lemme (17.15.14.1), label (ii bis)", "\\item[(ii bis)]", "\\item[\\textup{(ii \\emph{bis})}]",
   scan="'(ii' and ')' upright, 'bis' italic (crop p104_s2_iibis.png)",
   note="Label printed upright inside the italic statement except 'bis' (GLOBAL_ISSUES 26); \\emph inside \\textup gives the italic 'bis'.")
b0(104, "'On sait (II, 6.3.6)'", "(II, 6.3.6)", "(\\textbf{II}, 6.3.6)")
add(104, "proof of (17.15.14.1): 'que (ii) entraîne (ii bis) lorsqu'il existe'", "'bis' italic (crop p104_s2_iibis3.png)",
    "upright", "italics", None, "entraîne (ii bis) lorsqu'il", "entraîne (ii \\emph{bis}) lorsqu'il", "GLOBAL_ISSUES 26.")
b0(104, "'la restriction Y_i→X de f (I, 5.2.2)'", "(I, 5.2.2)", "(\\textbf{I}, 5.2.2)")
add(104, "proof of (17.15.14.1): 'est la clôture intégrale de Γ(V_i, O_{X_i})'",
    "Γ(V_i, O_{X_i}): V with the subscript i (crops p104_s3_gamma_w.png, p104_s3_gamma_z.png)",
    "\\Gamma(V,\\sh{O}_{X_i}): silent correction", "misprint_in_print", None,
    "\\Gamma(V,\\sh{O}_{X_i})", "\\Gamma(V_i,\\sh{O}_{X_i})",
    "V is the open affine of X_i just introduced ('pour tout ouvert affine V de X_i, Γ(g_i^{-1}(V), O_{Y_i})'); V_i is not defined there (the V_i=f^{-1}(U_i) come later). Not in the errata (Liste 3). The edit changes only the subscript.",
    corrected="\\Gamma(V,\\sh{O}_{X_i})")
b0(104, "'s'identifie canoniquement à X' (II, 6.3.4)'", "(II, 6.3.4)", "(\\textbf{II}, 6.3.4)")
add(104, "proof of (17.15.14.1): 'vérifiée la condition (ii bis), on peut'", "'bis' italic (page_104_s3.png)", "upright",
    "italics", None, "la condition (ii bis), on", "la condition (ii \\emph{bis}), on", "GLOBAL_ISSUES 26.")
add(104, "proof of (17.15.14.1): 'les V̄_i sont les composantes irréductibles de Y'",
    "bar over the V only, subscript i outside it (crop p104_s3_vbar.png)", "\\overline{V_i}: bar over V_i", "formula", None,
    "\\overline{V_i}", "\\overline{V}_i", "Bar version of convention 8 (GLOBAL_ISSUES 75).")
b0(104, "'Compte tenu de (4.6.6) et de (I, 5.1.8)'", "(I, 5.1.8)", "(\\textbf{I}, 5.1.8)")


# ---------------------------------------------------------------- validation
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
    if n_page != 1 or n_src != 1:
        bad += 1
        print(f"BAD #{k} p.{p}: page count {n_page}, source-region count {n_src}: {old[:70]!r}")
        continue
    pages[p] = pages[p].replace(old, new)
    src = src[:s] + seg.replace(old, new) + src[e:]

# summary
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
    # write the simulated result pages for inspection (scratch, not used by anything)
    for p in range(100, 105):
        (RUN / "crops_100_104" / f"sim_{p:03d}.tex").write_text(pages[p], encoding="utf-8", newline="\n")
