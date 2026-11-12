import json
import os
import sys

RUN = r"user\Documents\ega_scan_check_20261101\run_0I"
OUT = os.path.join(RUN, "findings_056_060.json")


def F(page, where, scan, tex, kind, old, new, note, conv=None, conf="high"):
    return {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": {"old": old, "new": new},
        "note": note,
    }


def IT(page, where, scan, old, new, note="", conf="high"):
    return F(page, where, scan, old, "italics", old, new,
             note or "Printed in italics; upright in the TeX.", conf=conf)


findings = [
    # ---------------- page 56 ----------------
    F(56, "(6.2.2), parenthesis after (6.2.2.1): image of u⊗b",
      "m⊗b'→u(m)⊗b'b (plain arrow)", r"m\otimes b'\longmapsto u(m)\otimes b'b",
      "convention", r"b'\longmapsto u(m)", r"b'\to u(m)",
      "Plain arrow in the print (checked on a crop at 2x).", conv=3),
    IT(56, "(6.3.1), first sentence: 'S^{-1}A est un A-module plat'",
       "A-module plat, with both 'module' and 'plat' in italics",
       r"un $A$-module \emph{plat}. En effet, pour tout",
       r"un $A$-\emph{module plat}. En effet, pour tout",
       "The print italicizes 'module plat'; the TeX italicizes only 'plat' (checked on a crop)."),
    IT(56, "(6.3.2), second sentence: 'qui est A-plat'",
       "A-plat with 'plat' in italics",
       r"qui est $A$-plat,", r"qui est $A$-\emph{plat},"),
    IT(56, "(6.3.2), second sentence: 'T^{-1}P est A-plat'",
       "A-plat with 'plat' in italics",
       r"$T^{-1}P$ est $A$-plat. En", r"$T^{-1}P$ est $A$-\emph{plat}. En"),

    # ---------------- page 57 ----------------
    F(57, "(6.3.4), first paragraph: 'l'homomorphisme m→f.m'",
      "m→f.m (plain arrow)", r"$m\mapsto f\cdot m$", "convention",
      r"$m\mapsto", r"$m\to",
      "Plain arrow in the print (crop at 5x). The dot in the same formula is a separate finding.", conv=3),
    F(57, "(6.3.4), first paragraph: 'l'homomorphisme m→f.m'",
      "f.m with a baseline period", r"f\cdot m", "symbol",
      r"f\cdot m$", r"f.m$",
      "The dot sits on the baseline (crop at 5x), not on the axis; same as the fix logged for p. 176 (a_i.(t_i|V)). Independent of the arrow fix."),
    F(57, "(6.3.4), first paragraph: 'la multiplication a→f.a'",
      "a→f.a (plain arrow)", r"$a\mapsto f\cdot a$", "convention",
      r"$a\mapsto", r"$a\to",
      "Plain arrow in the print (crop at 5x). The dot is a separate finding.", conv=3),
    F(57, "(6.3.4), first paragraph: 'la multiplication a→f.a'",
      "f.a with a baseline period", r"f\cdot a", "symbol",
      r"f\cdot a$", r"f.a$",
      "Baseline period in the print (crop at 5x). Independent of the arrow fix."),
    IT(57, "(6.3.4), second paragraph: 'alors M est A-plat'",
       "A-plat with 'plat' in italics",
       r"alors $M$ est $A$-plat.", r"alors $M$ est $A$-\emph{plat}."),
    IT(57, "(6.3.4), last sentence: 'B est A-plat'",
       "A-plat with 'plat' in italics",
       r"$B$ est $A$-plat.", r"$B$ est $A$-\emph{plat}."),

    # ---------------- page 58 ----------------
    F(58, "(6.4.5), end of the display M_m/mM_m = ... = M/mM",
      "M/𝔪M with no comma after it", r"=M/\mathfrak{m}M,", "punctuation",
      r"=M/\mathfrak{m}M,", r"=M/\mathfrak{m}M",
      "The print has no punctuation at the end of the display (crop at 2.5x); the TeX adds a comma."),
    F(58, "(6.5.1): 'l'homomorphisme x→1⊗x'",
      "x→1⊗x (plain arrow)", r"x\mapsto 1\otimes x", "convention",
      r"x\mapsto 1\otimes x", r"x\to 1\otimes x",
      "Plain arrow in the print (crop at 4x).", conv=3),
    F(58, "(6.5.2): 'l'application 𝔞→𝔞B'",
      "𝔞→𝔞B (plain arrow)", r"\mathfrak{a}\mapsto\mathfrak{a}B", "convention",
      r"\mathfrak{a}\mapsto\mathfrak{a}B", r"\mathfrak{a}\to\mathfrak{a}B",
      "Plain arrow in the print (crop at 4x).", conv=3),
    IT(58, "(6.6.1) a): 'M_(B) est un foncteur exact'",
       "'exact' in italics", r"foncteur exact", r"foncteur \emph{exact}"),
    IT(58, "(6.6.1) a): 'et fidèle en M'",
       "'fidèle' in italics", r"fidèle en $M$)", r"\emph{fidèle} en $M$)"),

    # ---------------- page 59 ----------------
    IT(59, "(6.6.1) c): 'le foncteur M_(B) est exact'",
       "'exact' in italics", r"est exact), et", r"est \emph{exact}), et"),
    F(59, "(6.6.1) c): 'l'homomorphisme x→1⊗x'",
      "x→1⊗x (plain arrow)", r"x\mapsto1\otimes x", "convention",
      r"x\mapsto1\otimes x", r"x\to1\otimes x",
      "Plain arrow in the print (crop at 4x).", conv=3),
    IT(59, "(6.6.2), first sentence: 'Soient A un anneau local'",
       "'local' in italics (the later 'B est un anneau local' is roman)",
       r"anneau local, $\mathfrak m$ son", r"anneau \emph{local}, $\mathfrak m$ son"),
    IT(59, "(6.6.2): 'A→B un homomorphisme local)'",
       "'local' in italics", r"homomorphisme local)", r"homomorphisme \emph{local})"),
    IT(59, "(6.6.2): 'Si B est un A-module plat'",
       "'plat' in italics", r"$A$-module plat, $B$ est", r"$A$-module \emph{plat}, $B$ est"),
    IT(59, "(6.6.2): 'B est un A-module fidèlement plat'",
       "'fidèlement plat' in italics",
       r"$A$-module fidèlement plat. En effet", r"$A$-module \emph{fidèlement plat}. En effet"),
    IT(59, "(6.7.1), first definition: 'On dit que F est f-plat'",
       "'f-plat' in italics", r"$f$-plat (ou", r"\emph{$f$-plat} (ou"),
    IT(59, "(6.7.1): '(ou Y-plat lorsque'",
       "'plat' of Y-plat in italics", "$Y$-plat\nlorsque", "$Y$-\\emph{plat}\nlorsque"),
    IT(59, "(6.7.1): 'en un point x∈X'",
       "'en un point' in italics", r"en un point $x\in X$", r"\emph{en un point} $x\in X$"),
    IT(59, "(6.7.1): 'F est f-plat au-dessus de y∈Y'",
       "'f-plat au-dessus de' in italics (the following 'est f-plat en tous les points' is roman)",
       r"$f$-plat au-dessus de $y\in Y$", r"\emph{$f$-plat au-dessus de} $y\in Y$"),
    IT(59, "(6.7.1): 'on dit que F est f-plat si F est f-plat en tous les points de X'",
       "first 'f-plat' in italics, second roman",
       "est $f$-plat\nsi $\\mathcal F$", "est \\emph{$f$-plat}\nsi $\\mathcal F$"),
    IT(59, "(6.7.1): 'le morphisme f est plat en x∈X'",
       "'plat en' in italics", r"est plat en $x\in X$", r"est \emph{plat en} $x\in X$"),
    IT(59, "(6.7.1): '(resp. plat au-dessus de y∈Y'",
       "'plat au-dessus de' in italics",
       r"(resp. plat au-dessus de $y\in Y$", r"(resp. \emph{plat au-dessus de} $y\in Y$"),
    IT(59, "(6.7.1): 'resp. plat) si O_X'",
       "'plat' in italics (the following 'f-plat en x (resp. f-plat au-dessus de y, resp. f-plat)' is roman)",
       "resp.\nplat) si", "resp.\n\\emph{plat}) si"),
    IT(59, "(6.7.2): 'le foncteur ... en G est exact dans la catégorie des (O_Y|U)-Modules'",
       "'exact' in italics", "est\nexact dans", "est\n\\emph{exact} dans"),
    IT(59, "(6.7.2), last sentence: 'si f est un morphisme plat'",
       "'plat' in italics", r"morphisme plat, le foncteur", r"morphisme \emph{plat}, le foncteur"),
    IT(59, "(6.7.2), last sentence: 'le foncteur f^* est exact'",
       "'exact' in italics", r"$f^*$ est exact dans", r"$f^*$ est \emph{exact} dans"),
    IT(59, "(6.7.3), first line: 'le faisceau d'anneaux O_Y cohérent'",
       "'cohérent' in italics", r"$\mathcal O_Y$ cohérent, et", r"$\mathcal O_Y$ \emph{cohérent}, et"),
    IT(59, "(6.7.3): 'supposons que pour tout voisinage ouvert U de y'",
       "'tout' in italics", r"pour tout voisinage ouvert", r"pour \emph{tout} voisinage ouvert"),
    IT(59, "(6.7.3): '(O_Y|U)-Modules cohérents'",
       "'cohérents' in italics (the preceding 'soit exact en G' is roman)",
       r"Modules cohérents.", r"Modules \emph{cohérents}."),
    IT(59, "(6.7.3): 'Alors F est f-plat en x'",
       "'f-plat en x' in italics",
       r"Alors $\mathcal F$ est $f$-plat en $x$.", r"Alors $\mathcal F$ est \emph{$f$-plat en $x$}."),

    # ---------------- page 60 ----------------
    IT(60, "(6.7.6), first sentence: 'f : X→Y un morphisme plat'",
       "'plat' in italics", r"un morphisme plat. Alors", r"un morphisme \emph{plat}. Alors"),
    IT(60, "(6.7.6), after (6.7.6.1): 'est un isomorphisme'",
       "'isomorphisme' in italics", r"est un isomorphisme lorsque", r"est un \emph{isomorphisme} lorsque"),
    IT(60, "(6.7.6), after (6.7.6.1): 'admet une présentation finie'",
       "'présentation finie' in italics", r"une présentation finie", r"une \emph{présentation finie}"),
    IT(60, "(6.7.8), definition: 'est fidèlement plat si'",
       "'fidèlement plat' in italics (the later 'Lorsque f est fidèlement plat' is roman)",
       r"est fidèlement plat si", r"est \emph{fidèlement plat} si"),
    IT(60, "(6.7.8), definition: 'si f est surjectif et si'",
       "'surjectif' in italics", r"$f$ est surjectif et si,", r"$f$ est \emph{surjectif} et si,"),
    IT(60, "(6.7.8), definition: 'O_{f(x)}-module fidèlement plat'",
       "'fidèlement plat' in italics",
       r"-module fidèlement plat. Lorsque", r"-module \emph{fidèlement plat}. Lorsque"),
    IT(60, "(6.7.8): 'le morphisme f est surjectif et plat (6.6.2)'",
       "'surjectif' in italics", r"morphisme $f$ est surjectif", r"morphisme $f$ est \emph{surjectif}"),
    IT(60, "(6.7.8): 'surjectif et plat (6.6.2)'",
       "'plat' in italics", r"et plat (6.6.2)", r"et \emph{plat} (6.6.2)"),
    IT(60, "(6.7.8): 'f^* est un foncteur exact et fidèle'",
       "'exact' in italics", r"un foncteur exact", r"un foncteur \emph{exact}"),
    IT(60, "(6.7.8): 'exact et fidèle dans la catégorie'",
       "'fidèle' in italics", r"fidèle dans la", r"\emph{fidèle} dans la"),
    IT(60, "(7.1.1): 'x est topologiquement nilpotent'",
       "'topologiquement nilpotent' in italics",
       r"topologiquement nilpotent", r"\emph{topologiquement nilpotent}"),
    IT(60, "(7.1.1): 'si 0 est une limite de la suite'",
       "'une' in italics", r"est une limite", r"est \emph{une} limite"),
    IT(60, "(7.1.1): 'A est linéairement topologisé s'il existe'",
       "'linéairement topologisé' in italics",
       r"linéairement topologisé s'il", r"\emph{linéairement topologisé} s'il"),
    IT(60, "(7.1.1): 'formé d'idéaux'",
       "'idéaux' in italics", r"formé d'idéaux", r"formé d'\emph{idéaux}"),
    IT(60, "(7.1.1): '(nécessairement ouverts)'",
       "'ouverts' in italics", r"(nécessairement ouverts)", r"(nécessairement \emph{ouverts})"),
    F(60, "Définition (7.1.2): 'on dit qu'un idéal J est un idéal de définition si'",
      "'idéal de définition' roman inside the italic statement ('un' before it is italic)",
      r"un idéal de définition si", "convention",
      r"un idéal de définition si", r"un \textup{idéal de définition} si",
      "The definition environment is \\itshape; the defined term is printed roman (crop).", conv=6),
]

# verification: every old occurs exactly once in its page file
ok = True
texts = {}
for f in findings:
    p = f["page"]
    if p not in texts:
        with open(os.path.join(RUN, f"page_{p:03d}.tex"), encoding="utf-8", newline="") as fh:
            # the page files are CRLF on disk; the release files use LF
            texts[p] = fh.read().replace("\r\n", "\n")
    t = texts[p]
    old = f["fix"]["old"]
    n = t.count(old)
    if n != 1:
        ok = False
        print(f"page {p}: old occurs {n} times: {old!r}")

# overlapping fixes on the same page (must not overlap)
for p, t in texts.items():
    spans = []
    for f in findings:
        if f["page"] != p:
            continue
        old = f["fix"]["old"]
        i = t.find(old)
        spans.append((i, i + len(old), old))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print(f"page {p}: overlapping fixes {a[2]!r} / {b[2]!r}")

# simulate applying all fixes per page
for p, t in texts.items():
    s = t
    for f in findings:
        if f["page"] == p:
            old, new = f["fix"]["old"], f["fix"]["new"]
            if s.count(old) != 1:
                ok = False
                print(f"page {p}: after earlier fixes old count {s.count(old)}: {old!r}")
            s = s.replace(old, new, 1)

from collections import Counter
cnt = Counter()
for f in findings:
    k = "convention" if f["kind"] == "convention" else ("misprint" if f["kind"] == "misprint_in_print" else "normal")
    cnt[(f["page"], k)] += 1
for p in range(56, 61):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])

if not ok:
    sys.exit(1)
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
print("wrote", OUT, len(findings))
