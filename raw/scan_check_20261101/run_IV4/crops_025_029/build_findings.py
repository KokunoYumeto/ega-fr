import json, os, sys

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
OUT = os.path.join(RUN, "findings_025_029.json")
NL = "<NL>"


def s(x):
    return None if x is None else x.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old=None, new=None, corrected=None, note="", fix_null=False):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if fix_null else {"old": s(old), "new": s(new)},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 25 ----------------
add(25, "after the second diagram, 'Mais on voit aussitôt (par exemple en se ramenant au cas affine) que ...'",
    "formula in the running text: 'que O_{X×_Z X}=O_{Y×_Z Y}/(p_1^*(K)+p_2^*(K))O_{Y×_Z Y}. Donc P^n_{X/Z} s'identifie ...'",
    "the formula is set as a display \\[ ... \\]",
    "other", None, "high",
    r"au cas affine) que<NL>\[<NL>  \mathcal{O}_{X\times_Z X}=<NL>  \mathcal{O}_{Y\times_Z Y}/<NL>  (p_1^*(\mathscr{K})+p_2^*(\mathscr{K}))<NL>  \mathcal{O}_{Y\times_Z Y}.<NL>\]<NL>Donc",
    r"au cas affine) que<NL>$\mathcal{O}_{X\times_Z X}=\mathcal{O}_{Y\times_Z Y}/(p_1^*(\mathscr{K})+p_2^*(\mathscr{K}))\mathcal{O}_{Y\times_Z Y}$.<NL>Donc",
    note="Formula displayed where the print has it inline; no connecting word lost or added.")
add(25, "first text line: '(I, 5.3.7)'", "bold I: '(I, 5.3.7)'", "(I, 5.3.7)", "convention", 2, "high",
    r"(I, 5.3.7)", r"(\textbf{I}, 5.3.7)")
add(25, "after Corollaire (16.4.21): 'la suite exacte (0, 20.5.12.1)'", "bold 0", "(0, 20.5.12.1)", "convention", 2, "high",
    r"(0, 20.5.12.1)", r"(\textbf{0}, 20.5.12.1)")
add(25, "display (16.4.21.1)", "italic Omega: N_{X/Y} -> j^*(Ω^1_{Y/Z}) -> Ω^1_{X/Z} -> 0",
    "upright \\Omega (twice)", "font", None, "high",
    r"j^*(\Omega_{Y/Z}^1)\ar[r]&<NL>    \Omega_{X/Z}^1\ar[r]&0.",
    r"j^*(\varOmega_{Y/Z}^1)\ar[r]&<NL>    \varOmega_{X/Z}^1\ar[r]&0.",
    note="The print sets the sheaf of differentials Ω^1_{X/S} with an italic Omega and the module Ω^1_{B/A} with an upright one (p. 28); see the document-wide note.")
add(25, "Corollaire (16.4.22): 'P^n_{X/S} et Ω^1_{X/S} sont des'", "italic Omega", "upright \\Omega", "font", None, "high",
    r"$\Omega_{X/S}^1$ sont des", r"$\varOmega_{X/S}^1$ sont des")
add(25, "display (16.4.23.1)", "italic Omega: p^*(Ω^1_{X/S}) ⊕ q^*(Ω^1_{Y/S}) -> Ω^1_{(X×_S Y)/S}",
    "upright \\Omega (three times)", "font", None, "high",
    r"p^*(\Omega_{X/S}^1)\oplus q^*(\Omega_{Y/S}^1)<NL>  \longrightarrow\Omega_{(X\times_S Y)/S}^1",
    r"p^*(\varOmega_{X/S}^1)\oplus q^*(\varOmega_{Y/S}^1)<NL>  \longrightarrow\varOmega_{(X\times_S Y)/S}^1")

# ---------------- page 26 ----------------
add(26, "display after 'Ceci prouve que l'homomorphisme canonique (16.4.18.1)', the resp. part",
    "'(resp. q_{Z/Y/S} : q^*(P^n_{Z/S}) -> P^n_{Z/S})'",
    "q^*(\\mathscr{P}_{Y/S}^n): the TeX silently corrects the printed Z/S",
    "misprint_in_print", None, "high",
    r"q_{Z/Y/S}:q^*(\mathscr{P}_{Y/S}^n)", r"q_{Z/Y/S}:q^*(\mathscr{P}_{Z/S}^n)",
    corrected=r"q^*(\mathscr{P}_{Y/S}^n)",
    note="The source of q_{Z/Y/S} is q^*(P^n_{Y/S}) (cf. the line 'de l'Idéal d'augmentation de q^*(P^n_{Y/S})'); the print has Z/S. Diplomatic text restored to the printed reading.")
add(26, "Remarques (16.4.24) (i): 'l'homomorphisme de gauche dans (16.4.21.2)'",
    "(16.4.21.2)", "(16.4.21.2) (kept)", "misprint_in_print", None, "high",
    corrected="(16.4.21.1)", fix_null=True,
    note="Corollaire (16.4.21) has only the exact sequence (16.4.21.1); its left-hand map N_{X/Y} -> j^*(Ω^1_{Y/Z}) is meant. The TeX keeps the printed reading.")
add(26, "Remarques (16.4.24) (ii), display 'U ... P^n_{Γ(U,B)/Γ(U,A)} (U ouvert dans X)'",
    "wavy arrow U ⇝ P^n", "\\longmapsto", "symbol", None, "high",
    r"U\longmapsto", r"U\leadsto")
add(26, "Remarques (16.4.24) (i): 'étudiés dans (0, 20.6)'", "bold 0", "(0, 20.6)", "convention", 2, "high",
    r"(0, 20.6)", r"(\textbf{0}, 20.6)")

# ---------------- page 27 ----------------
add(27, "(16.5.1), condition a)", "label 'a)' in italic, no opening parenthesis",
    "\\item[(a)] (upright, with opening parenthesis)", "punctuation", None, "high",
    r"\item[(a)]", r"\item[\emph{a)}]",
    note="(16.5.1) is a roman env; the print sets the whole label italic.")
add(27, "(16.5.1), condition b)", "label 'b)' in italic, no opening parenthesis",
    "\\item[(b)]", "punctuation", None, "high",
    r"\item[(b)]", r"\item[\emph{b)}]")
add(27, "(16.5.1) b): 'au-dessus d'un ouvert U de S tel que V⊂f^{-1}(U)'",
    "the first U is set in a bold upright fount (wrong fount); the U of f^{-1}(U) is normal",
    "$U$ (silently normalised)", "misprint_in_print", None, "medium",
    r"ouvert<NL>$U$ de $S$", r"ouvert<NL>$\mathbf{U}$ de $S$",
    corrected="$U$",
    note="Both stems of this U are heavy, unlike the S and V on the same line; wrong-fount letter recorded as a misprint (GLOBAL_ISSUES item 29 practice).")
add(27, "after display (16.5.1.2): 'Il est clair qu'il revient au même ...'",
    "new indented paragraph", "follows \\end{enumerate} without a blank line (set without indent)", "other", None, "high",
    r"\end{enumerate}<NL>Il est clair", r"\end{enumerate}<NL><NL>Il est clair")
add(27, "(16.5.1): 'D_x : O_x -> F_x est une O_{f(x)}-dérivation.'", "'dérivation' in italics",
    "-dérivation (roman)", "italics", None, "high",
    r"$\mathcal{O}_{f(x)}$-dérivation.", r"$\mathcal{O}_{f(x)}$-\emph{dérivation}.")
add(27, "(16.5.1), second paragraph: '1_{O_X}+D est un O_S-homomorphisme d'Algèbres de O_X'",
    "'homomorphisme d'Algèbres' in italics", "roman", "italics", None, "high",
    r"$\mathcal{O}_S$-homomorphisme d'Algèbres de", r"$\mathcal{O}_S$-\emph{homomorphisme d'Algèbres} de")
add(27, "(16.5.1): 'forment évidemment un Γ(X, O_X)-module Dér_S(O_X, F)'", "'module' in italics",
    "roman", "italics", None, "high",
    r"$\Gamma(X,\mathcal{O}_X)$-module<NL>", r"$\Gamma(X,\mathcal{O}_X)$-\emph{module}<NL>")
add(27, "Proposition (16.5.2): 'l'application D ... Γ(D)'", "wavy arrow D ⇝ Γ(D)", "\\mapsto", "symbol", None, "high",
    r"D\mapsto\Gamma(D)", r"D\leadsto\Gamma(D)")
add(27, "Proposition (16.5.2): 'Γ(D) : t ... D(t)'", "wavy arrow t ⇝ D(t)", "\\mapsto", "symbol", None, "high",
    r"t\mapsto D(t)", r"t\leadsto D(t)")
add(27, "Proposition (16.5.2), end: '(cf. (0, 20.1.2))'",
    "the parenthesis '(cf. (0, 20.1.2))' is upright inside the italic statement, with a bold 0",
    "italic in the TeX, plain 0", "convention", 6, "high",
    r"(cf. (0, 20.1.2))", r"\textup{(cf. (\textbf{0}, 20.1.2))}",
    note="One edit for convention 6 (upright 'cf.' and reference) and convention 2 (bold 0) at the same place.")

# ---------------- page 28 ----------------
add(28, "first line: 'donnée dans (0, 20.1.6)'", "bold 0", "(0, 20.1.6)", "convention", 2, "high",
    r"(0, 20.1.6)", r"(\textbf{0}, 20.1.6)")
add(28, "first paragraph: '(I, 1.3.13 et 1.3.8)'", "bold I", "(I, 1.3.13 et 1.3.8)", "convention", 2, "high",
    r"(I, 1.3.13 et", r"(\textbf{I}, 1.3.13 et")
add(28, "Proposition (16.5.3) (i): label", "upright '(i)' in the italic statement", "\\item[(i)] (italic)",
    "convention", 6, "high",
    r"\item[(i)] La différentielle", r"\item[\textup{(i)}] La différentielle")
add(28, "Proposition (16.5.3) (i): 'd_{X/S} : O_X -> Ω^1_{X/S}'", "italic Omega", "upright \\Omega", "font", None, "high",
    r"d_{X/S}:\mathcal{O}_X\to\Omega_{X/S}^1$", r"d_{X/S}:\mathcal{O}_X\to\varOmega_{X/S}^1$")
add(28, "Proposition (16.5.3) (i): '(16.3.6) est une S-dérivation'", "reference upright in the italic statement",
    "italic", "convention", 6, "high",
    r"(16.3.6) est une", r"\textup{(16.3.6)} est une")
add(28, "Proposition (16.5.3) (ii): label", "upright '(ii)'", "\\item[(ii)] (italic)", "convention", 6, "high",
    r"\item[(ii)] Pour tout", r"\item[\textup{(ii)}] Pour tout")
add(28, "Proposition (16.5.3) (ii): 'l'application u ... u∘d_{X/S}'", "wavy arrow u ⇝ u∘d_{X/S}", "\\mapsto",
    "symbol", None, "high",
    r"l'application<NL>$u\mapsto u", r"l'application<NL>$u\leadsto u")
add(28, "display (16.5.3.1): 'Hom_{O_X}(Ω^1_{X/S}, F) ~-> Dér_S(O_X, F)'", "italic Omega", "upright \\Omega",
    "font", None, "high",
    r"\operatorname{Hom}_{\mathcal{O}_X}(\Omega_{X/S}^1,\mathscr{F})",
    r"\operatorname{Hom}_{\mathcal{O}_X}(\varOmega_{X/S}^1,\mathscr{F})")
add(28, "proof of (16.5.3): '(en vertu de (0, 20.4.8)) que'", "bold 0", "(0, 20.4.8)", "convention", 2, "high",
    r"(0, 20.4.8)) que", r"(\textbf{0}, 20.4.8)) que")
add(28, "proof of (16.5.3): 'que u ... u∘d_{X/S} est injectif'", "wavy arrow", "\\mapsto", "symbol", None, "high",
    r"$u\mapsto u\circ d_{X/S}$ est injectif", r"$u\leadsto u\circ d_{X/S}$ est injectif")
add(28, "proof of (16.5.3): 'D_V=u_V∘d_{B/A} (0, 20.4.8);'", "bold 0", "(0, 20.4.8)", "convention", 2, "high",
    r"(0, 20.4.8); en", r"(\textbf{0}, 20.4.8); en")
add(28, "proof of (16.5.3), last line: 'un homomorphisme de O_X-Modules u : O_X -> F répondant à la question'",
    "u : O_X -> F", "u:\\mathcal{O}_X\\to\\mathscr{F} (kept)", "misprint_in_print", None, "high",
    corrected=r"$u:\Omega_{X/S}^1\to\mathscr{F}$", fix_null=True,
    note="The u_V : Ω^1_{B/A} -> Γ(V, F) glue to a homomorphism Ω^1_{X/S} -> F (surjectivity of (16.5.3.1)); the print's source O_X is wrong. TeX keeps the printed reading. (With the italic-Omega decision, \\varOmega in the corrected reading.)")
add(28, "(16.5.4): 'l'application U ... Dér_S(O_U, F|U)'", "wavy arrow U ⇝ Dér_S", "\\mapsto", "symbol", None, "high",
    r"$U\mapsto\operatorname{D\acute{e}r}_S", r"$U\leadsto\operatorname{D\acute{e}r}_S")
add(28, "(16.5.4): 'Cet O_X-Module se note Dér_S(O_X, F)' (sheaf Dér)", "script D followed by italic 'ér'",
    "\\mathscr{D}\\!\\mathrm{\\acute{e}r} (upright ér)", "font", None, "high",
    r"\mathrm{\acute{e}r}_S(\mathcal{O}_X,\mathscr{F})$ et est", r"\acute{e}r_S(\mathcal{O}_X,\mathscr{F})$ et est",
    note="As in the sheaf Hom (script H + italic 'om', \\mathscr{H}\\!om); the notation index (p. 334) prints it the same way. All five uses in ega4-16 are on this page.")
add(28, "Corollaire (16.5.5): 'déduit de u ... u∘d_{X/S}'", "wavy arrow", "\\mapsto", "symbol", None, "high",
    r"déduit de $u\mapsto u", r"déduit de $u\leadsto u")
add(28, "display (16.5.5.1): 'Hom_{O_X}(Ω^1_{X/S}, F)'", "italic Omega", "upright \\Omega", "font", None, "high",
    r"\mathscr{H}\!om_{\mathcal{O}_X}(\Omega_{X/S}^1,\mathscr{F})",
    r"\mathscr{H}\!om_{\mathcal{O}_X}(\varOmega_{X/S}^1,\mathscr{F})")
add(28, "display (16.5.5.1): sheaf Dér_S(O_X, F)", "script D + italic 'ér'", "\\mathrm{\\acute{e}r}", "font", None, "high",
    r"  \mathscr{D}\!\mathrm{\acute{e}r}_S(\mathcal{O}_X,\mathscr{F})<NL>  \tag{16.5.5.1}",
    r"  \mathscr{D}\!\acute{e}r_S(\mathcal{O}_X,\mathscr{F})<NL>  \tag{16.5.5.1}")
add(28, "Corollaire (16.5.6) (i): label", "upright '(i)'", "\\item[(i)] (italic)", "convention", 6, "high",
    r"\item[(i)] Si le morphisme", r"\item[\textup{(i)}] Si le morphisme")
add(28, "Corollaire (16.5.6) (i): 'alors Dér_S(O_X, F) est un'", "script D + italic 'ér'", "\\mathrm{\\acute{e}r}",
    "font", None, "high",
    r"alors<NL>$\mathscr{D}\!\mathrm{\acute{e}r}_S", r"alors<NL>$\mathscr{D}\!\acute{e}r_S")
add(28, "Corollaire (16.5.6) (ii): label", "upright '(ii)'", "\\item[(ii)] (italic)", "convention", 6, "high",
    r"\item[(ii)] Si de plus", r"\item[\textup{(ii)}] Si de plus")
add(28, "Corollaire (16.5.6) (ii): 'cohérent, alors Dér_S(O_X, F)'", "script D + italic 'ér'", "\\mathrm{\\acute{e}r}",
    "font", None, "high",
    r"cohérent, alors $\mathscr{D}\!\mathrm{\acute{e}r}_S", r"cohérent, alors $\mathscr{D}\!\acute{e}r_S")
add(28, "proof of (16.5.6): '(I, 1.3.12)'", "bold I", "(I, 1.3.12)", "convention", 2, "high",
    r"(I, 1.3.12)", r"(\textbf{I}, 1.3.12)")
add(28, "proof of (16.5.6): '(0_I, 5.3.5)'", "bold 0 with subscript I", "(0$_{\\rm I}$, 5.3.5) (plain 0)",
    "convention", 2, "high",
    r"(0$_{\rm I}$, 5.3.5)", r"($\mathbf{0}_{\mathrm I}$, 5.3.5)")
add(28, "display (16.5.7.1): 'Hom_{O_X}(Ω^1_{X/S}, O_X)'", "italic Omega", "upright \\Omega", "font", None, "high",
    r"\mathscr{H}\!om_{\mathcal{O}_X}(\Omega_{X/S}^1,\mathcal{O}_X)",
    r"\mathscr{H}\!om_{\mathcal{O}_X}(\varOmega_{X/S}^1,\mathcal{O}_X)")
add(28, "display (16.5.7.1): 'Dér_S(O_X, O_X)'", "script D + italic 'ér'", "\\mathrm{\\acute{e}r}", "font", None, "high",
    r"=\mathscr{D}\!\mathrm{\acute{e}r}_S(\mathcal{O}_X,\mathcal{O}_X)", r"=\mathscr{D}\!\acute{e}r_S(\mathcal{O}_X,\mathcal{O}_X)")
add(28, "(16.5.7), last line: 'le dual du O_X-Module Ω^1_{X/S}.'", "italic Omega", "upright \\Omega", "font", None, "high",
    r"$\Omega_{X/S}^1$. Si", r"$\varOmega_{X/S}^1$. Si")

# ---------------- page 29 ----------------
add(29, "(16.5.8), first line: 'Supposons plus particulièrement que Ω^1_{X/S} soit un'", "italic Omega",
    "upright \\Omega", "font", None, "high",
    r"que $\Omega_{X/S}^1$ soit un", r"que $\varOmega_{X/S}^1$ soit un")
add(29, "(16.5.8): 'a même rang que Ω^1_{X/S} en chaque point'", "italic Omega", "upright \\Omega", "font", None, "high",
    r"rang que $\Omega_{X/S}^1$", r"rang que $\varOmega_{X/S}^1$")
add(29, "(16.5.8): 'supposons que Ω^1_{X/S} soit de rang n'", "italic Omega", "upright \\Omega", "font", None, "high",
    r"que $\Omega_{X/S}^1$ soit de", r"que $\varOmega_{X/S}^1$ soit de")
add(29, "(16.5.8): 'dans Ω^1_{X/S}⊗_{O_X}k(x)'", "italic Omega", "upright \\Omega", "font", None, "high",
    r"dans<NL>$\Omega_{X/S}^1", r"dans<NL>$\varOmega_{X/S}^1")
add(29, "(16.5.8): 'Ω^1_{X/S}⊗_{O_X} k(x)'", "bold italic k (outside the subscript)", "k(x)", "convention", 1, "high",
    r"_{\mathcal{O}_X}k(x)$", r"_{\mathcal{O}_X}\boldsymbol{k}(x)$")
add(29, "(16.5.8): 'une base de ce k(x)-espace vectoriel'", "bold italic k", "k(x)", "convention", 1, "high",
    r"$k(x)$-espace", r"$\boldsymbol{k}(x)$-espace")
add(29, "(16.5.8): 'du O_x-module (Ω^1_{X/S})_x'", "italic Omega", "upright \\Omega", "font", None, "high",
    r"$(\Omega_{X/S}^1)_x$", r"$(\varOmega_{X/S}^1)_x$")
add(29, "(16.5.8): 'Γ(U, O_X)-module Γ(U, Ω^1_{X/S})'", "italic Omega", "upright \\Omega", "font", None, "high",
    r"$\Gamma(U,\Omega_{X/S}^1)$", r"$\Gamma(U,\varOmega_{X/S}^1)$")
add(29, "(16.5.9), display '[D_1^U, D_2^U]=D_1^U∘D_2^U—D_2^U∘D_1^U'", "long dash for the minus", "-",
    "convention", 7, "high",
    r"D_2^U-D_2^U", r"D_2^U\setmin D_2^U")
add(29, "(16.5.9.1) '[D_1, D_2]=D_1∘D_2—D_2∘D_1'", "long dash for the minus", "-", "convention", 7, "high",
    r"\circ D_2-D_2\circ", r"\circ D_2\setmin D_2\circ")
add(29, "(16.5.9): 'une structure de Γ(S, O_S)-algèbre de Lie'", "'algèbre de Lie' in italics", "roman",
    "italics", None, "high",
    r"-algèbre de Lie", r"-\emph{algèbre de Lie}")
add(29, "(16.5.9): 'une structure de ψ^*(O_S)-Algèbre de Lie'", "'Algèbre de Lie' in italics", "roman",
    "italics", None, "high",
    r"-Algèbre de Lie", r"-\emph{Algèbre de Lie}")
add(29, "(16.5.9), last sentence: 'l'application (D_1, D_2) -> [D_1, D_2]'", "plain arrow", "\\mapsto",
    "convention", 3, "high",
    r"(D_1,D_2)\mapsto[D_1,D_2]", r"(D_1,D_2)\to[D_1,D_2]")
add(29, "(16.5.9), last sentence: 'n'est pas Γ(X, O_X)-bilinéaire'", "'n'est pas' and 'bilinéaire' in italics",
    "roman", "italics", None, "high",
    r"n'est pas<NL>$\Gamma(X,\mathcal{O}_X)$-bilinéaire.", r"\emph{n'est pas<NL>$\Gamma(X,\mathcal{O}_X)$-bilinéaire}.")
add(29, "display (16.5.10.1): 'Ω^1_{X/S}⊗_S S' ~-> Ω^1_{X'/S'}'", "italic Omega (twice)", "upright \\Omega",
    "font", None, "high",
    r"\Omega_{X/S}^1\otimes_S S'\xrightarrow{\sim}\Omega_{X'/S'}^1",
    r"\varOmega_{X/S}^1\otimes_S S'\xrightarrow{\sim}\varOmega_{X'/S'}^1")

# ---------------- checks ----------------
ok = True
texts = {}
for p in (25, 26, 27, 28, 29):
    raw = open(os.path.join(RUN, "page_%03d.tex" % p), "rb").read().decode("utf-8")
    texts[p] = raw.replace("\r\n", "\n")
for i, d in enumerate(F):
    fx = d["fix"]
    if fx is None:
        continue
    n = texts[d["page"]].count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE/MISSING", i, d["page"], n, repr(fx["old"]))
    if fx["old"] == fx["new"]:
        ok = False
        print("NO-OP", i)
# overlap check within each page (character ranges in the original text)
for p in texts:
    rngs = []
    for i, d in enumerate(F):
        if d["page"] != p or d["fix"] is None:
            continue
        o = d["fix"]["old"]
        k = texts[p].find(o)
        rngs.append((k, k + len(o), i))
    rngs.sort()
    for a, b in zip(rngs, rngs[1:]):
        if b[0] < a[1]:
            ok = False
            print("OVERLAP page", p, a, b)
# sequential application check
for p in texts:
    t = texts[p]
    for d in F:
        if d["page"] == p and d["fix"] is not None:
            if t.count(d["fix"]["old"]) != 1:
                ok = False
                print("SEQ FAIL", p, repr(d["fix"]["old"]))
            t = t.replace(d["fix"]["old"], d["fix"]["new"], 1)
print("all checks ok" if ok else "PROBLEMS")
json.dump(F, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
from collections import Counter
c = Counter()
for d in F:
    cat = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    c[(d["page"], cat)] += 1
for p in (25, 26, 27, 28, 29):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print(len(F), "findings written to", OUT)
