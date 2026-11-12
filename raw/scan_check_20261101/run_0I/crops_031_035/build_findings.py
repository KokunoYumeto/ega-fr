"""Build findings_031_035.json: hand-made findings plus one finding per \\mathbf{K} occurrence
(bold italic K in the print), then check every 'old' (unique on its page, no overlaps, still unique
when the fixes are applied in sequence) and simulate apply_fixes.py on an in-memory copy of the
release file. Reads only; writes nothing but the findings JSON."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN =pathlib.Path(__file__).resolve().parent.parent
OUT = RUN / "findings_031_035.json"
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\BASE\native\ega1\ega0-1-fr.tex")
PAGES = range(31, 36)
SUB37 = "\\subsection{Images réciproques de préfaisceaux de groupes ou d'anneaux}"
SUB38 = "\\subsection{Faisceaux d'espaces pseudo-discrets}"
M = "\\oldpage[0\\textsubscript{I}]{%d}"


def page_text(n):
    t = (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    return t


texts = {n: page_text(n) for n in PAGES}


def F(page, where, scan, tex, kind, fix, note=None, convention=None, confidence="high", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=convention,
             confidence=confidence, fix=fix)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


FLAT = ("The print has the flat sign ♭ (EGA's v^♭ notation), not the letter b (checked on crops); "
        "ega0-1-fr.tex itself writes ^\\flat from (4.4.3) on (cf. GLOBAL_ISSUES item 14).")
manual = [
    # ---- page 31
    F(31, "(3.5.3): 'considéré comme muni du ψ-morphisme canonique ρ_𝒢 : 𝒢 → ψ^*(𝒢)'",
      "'ψ-morphisme canonique' in italics: 'morphisme' is italic as well as 'canonique' (checked on a crop)",
      "$\\psi$-morphisme\n\\emph{canonique}", "italics",
      {"old": "muni du $\\psi$-morphisme\n\\emph{canonique}", "new": "muni du $\\psi$-\\emph{morphisme\ncanonique}"}),
    F(31, "(3.5.3): 'on posera v^♭ = ψ_*(v)∘ρ_𝒢 : 𝒢→ψ_*(ℱ)'", "v^♭ (flat sign)", "$v^b$", "symbol",
      {"old": "$v^b=\\psi_*(v)", "new": "$v^\\flat=\\psi_*(v)"}, FLAT),
    F(31, "(3.5.3): 'est de la forme v^♭ pour un v et un seul'", "v^♭ (flat sign)", "$v^b$", "symbol",
      {"old": "de la forme $v^b$", "new": "de la forme $v^\\flat$"}, FLAT),
    # ---- page 32
    F(32, "(3.5.4): 'de telle façon que l'isomorphisme v→v^♭ soit un isomorphisme de bifoncteurs'",
      "v→v^♭ (flat sign)", "$v\\to v^b$", "symbol",
      {"old": "$v\\to v^b$", "new": "$v\\to v^\\flat$"}, FLAT),
    F(32, "(3.5.4): 'on a, d'après (3.5.3.3), (3.5.4.2) et la définition de u^♭'",
      "la définition de u^♭ (italic u, not v; flat sign; checked on a crop against the u and v of the same page)",
      "la définition de $v^b$", "misprint_in_print",
      {"old": "et la définition de $v^b$", "new": "et la définition de $u^\\flat$"},
      "The print's u^♭ is a slip: u : 𝒢_2→ψ_*(ℱ) has no ♭ (♭ is defined in (3.5.3) for v : ψ^*(𝒢)→ℱ), and the "
      "first equality of the next display applies the definition of v^♭ to v = u^♯∘ψ^*(w). The TeX silently "
      "corrects the letter to v (and writes the letter b for ♭); the fix restores the printed u^♭.",
      corrected="et la définition de $v^\\flat$"),
    F(32, "(3.5.4), display: '(u^♯∘ψ^*(w))^♭ = ψ_*(u^♯)∘ψ_*(ψ^*(w))∘ρ_{𝒢_1} = …'",
      "(u^♯∘ψ^*(w))^♭ (flat sign)", "(u^\\sharp\\circ\\psi^*(w))^b", "symbol",
      {"old": "(u^\\sharp\\circ\\psi^*(w))^b", "new": "(u^\\sharp\\circ\\psi^*(w))^\\flat"}, FLAT),
    # ---- page 33
    F(33, "(3.6.2), proof: 'et par suite a) entraîne b).'",
      "a) and b) in italics (letter and parenthesis; checked on a crop)", "a) entraîne b) upright", "italics",
      {"old": "par suite a) entraîne b).", "new": "par suite \\emph{a)} entraîne \\emph{b)}."},
      "The list labels a), b), c) of (3.6.2) are upright in the print, as in the TeX; only the references in "
      "the running text are italic."),
    F(33, "(3.6.2), end of proof: 'et démontre donc que c) entraîne a).'",
      "c) and a) in italics (checked on a crop)", "c) entraîne a) upright", "italics",
      {"old": "donc que c) entraîne a).", "new": "donc que \\emph{c)} entraîne \\emph{a)}."}),
    F(33, "end of page_033.tex: heading of 3.7",
      "printed p. 33 ends with '… et démontre donc que c) entraîne a).'; the heading '3.7. Images réciproques "
      "de préfaisceaux de groupes ou d'anneaux.' is the first line of p. 34",
      SUB37 + " stands before \\oldpage[0\\textsubscript{I}]{34}", "marker",
      {"old": SUB37 + "\n\n", "new": ""},
      "The marker belongs before the heading (as at p. 23, ll. 815-817 of ega0-1-fr.tex). Two-part move: this "
      "edit deletes the heading from the end of p. 33's segment; the page-34 marker finding re-inserts it after "
      "\\oldpage[0\\textsubscript{I}]{34}. Apply both or neither; each 'old' lies inside its own page segment, "
      "so apply_fixes.py can apply them in either order."),
    # ---- page 34
    F(34, "start of page_034.tex: heading of 3.7",
      "p. 34 begins with the heading '3.7. Images réciproques de préfaisceaux de groupes ou d'anneaux.'",
      "the heading stands in page_033.tex, before the marker", "marker",
      {"old": (M % 34) + "\n\n", "new": (M % 34) + "\n\n" + SUB37 + "\n\n"},
      "Second half of the move begun by the page-33 marker finding (which deletes the heading before the "
      "marker). Apply both or neither."),
    F(34, "(3.7.1): 'On vérifie immédiatement que U→𝒢'(U) satisfait bien aux axiomes des faisceaux'",
      "plain arrow U→𝒢'(U) (checked on a crop)", "$U\\mapsto\\mathcal{G}'(U)$", "convention",
      {"old": "$U\\mapsto\\mathcal{G}'(U)$", "new": "$U\\to\\mathcal{G}'(U)$"}, convention=3),
    F(34, "(3.7.1): 'On définit u^♯ et v^♭ de la façon suivante'", "v^♭ (flat sign)", "$v^b$", "symbol",
      {"old": "et $v^b$\nde la façon", "new": "et $v^\\flat$\nde la façon"}, FLAT),
    F(34, "(3.7.1): 'De même, si s∈𝒢(V) (V ouvert dans Y), v^♭(s) est la section de ℱ'",
      "v^♭(s) (flat sign)", "$v^b(s)$", "symbol",
      {"old": "$v^b(s)$", "new": "$v^\\flat(s)$"}, FLAT),
    F(34, "(3.7.1): 'La vérification des relations (u^♯)^♭ = u'", "(u^♯)^♭ (flat sign)", "$(u^\\sharp)^b=u$",
      "symbol", {"old": "$(u^\\sharp)^b=u$", "new": "$(u^\\sharp)^\\flat=u$"}, FLAT),
    F(34, "(3.7.1): '(v^♭)^♯ = v'", "(v^♭)^♯ (flat sign)", "$(v^b)^\\sharp=v$", "symbol",
      {"old": "$(v^b)^\\sharp=v$", "new": "$(v^\\flat)^\\sharp=v$"}, FLAT),
    F(34, "(3.7.1): 'et v^♭ = ψ_*(v)∘ρ est immédiate'", "v^♭ (flat sign)", "$v^b=\\psi_*(v)\\circ\\rho$",
      "symbol", {"old": "$v^b=\\psi_*(v)\\circ\\rho$", "new": "$v^\\flat=\\psi_*(v)\\circ\\rho$"}, FLAT),
    F(34, "end of page_034.tex: heading of 3.8",
      "printed p. 34 ends with '… dans la catégorie abélienne des faisceaux de groupes commutatifs.'; the "
      "heading '3.8. Faisceaux d'espaces pseudo-discrets.' is the first line of p. 35",
      SUB38 + " stands before \\oldpage[0\\textsubscript{I}]{35}", "marker",
      {"old": SUB38 + "\n\n", "new": ""},
      "Two-part move like the 3.7 heading: this edit deletes the heading from the end of p. 34's segment; the "
      "page-35 marker finding re-inserts it after \\oldpage[0\\textsubscript{I}]{35}. Apply both or neither."),
    # ---- page 35
    F(35, "start of page_035.tex: heading of 3.8",
      "p. 35 begins with the heading '3.8. Faisceaux d'espaces pseudo-discrets.'",
      "the heading stands in page_034.tex, before the marker", "marker",
      {"old": (M % 35) + "\n\n", "new": (M % 35) + "\n\n" + SUB38 + "\n\n"},
      "Second half of the move begun by the page-34 heading-3.8 finding. Apply both or neither."),
    F(35, "(3.8.1): 'de la topologie discrète, U→ℱ(U) est un préfaisceau d'espaces topologiques'",
      "plain arrow U→ℱ(U) (checked on a crop)", "$U\\mapsto\\mathcal{F}(U)$", "convention",
      {"old": "$U\\mapsto\\mathcal{F}(U)$ est un", "new": "$U\\to\\mathcal{F}(U)$ est un"}, convention=3),
    F(35, "(3.8.1): 'Il suffira pour cela de montrer que le préfaisceau U→ℱ(U) d'espaces topologiques discrets'",
      "plain arrow U→ℱ(U) (checked on a crop)", "$U\\mapsto\\mathcal{F}(U)$", "convention",
      {"old": "$U\\mapsto\\mathcal{F}(U)$ d'espaces", "new": "$U\\to\\mathcal{F}(U)$ d'espaces"}, convention=3),
    F(35, "(3.8.1): 'un faisceau d'espaces topologiques ℱ' associé à ℱ (3.5.6)'",
      "the italics end with 'associé'; 'à' is upright (checked on a crop)",
      "\\emph{… associé à $\\mathcal{F}$}", "italics",
      {"old": "associé à $\\mathcal{F}$} (3.5.6)", "new": "associé} à $\\mathcal{F}$ (3.5.6)"}),
]

# ---- one finding per \mathbf{K}: the category K is printed bold italic
START_ENV = {31: "3.5.1", 32: None, 33: "3.5.5", 34: None, 35: None}
KTOK = "\\mathbf{K}"


def env_at(n, t, i):
    envs = [(m.start(), m.group(1)) for m in re.finditer(r"\\begin\{env\}\[([0-9.]+)\]", t)]
    cur = START_ENV[n]
    for s, e in envs:
        if s < i:
            cur = e
    fn = t.rfind("\\footnote{", 0, i)
    if fn != -1 and t.find(".}", fn) > i:  # the footnote on p. 32 ends with '.}'
        return f"footnote (1) to ({cur})"
    return f"({cur})"


def plain(s):
    s = s.replace("\\mathbf{K}", "K").replace("\\mathcal{G}", "𝒢").replace("\\mathcal{F}", "ℱ")
    s = s.replace("\\psi", "ψ").replace("\\emph{", "").replace("$", "").replace("~", " ").replace("\n", " ")
    s = s.replace("}", "").replace("{", "").replace("\\footnote", "")
    return " ".join(s.split())


def word_bounds(t, i, j):
    """grow [i, j) to whole words (stop at whitespace)"""
    while i > 0 and not t[i - 1].isspace():
        i -= 1
    while j < len(t) and not t[j].isspace():
        j += 1
    return i, j


WHERE_OVERRIDE = {
    (31, "dans $\\mathbf{K}$, et"): "(3.5.3): '…où 𝒢' est un faisceau sur X à valeurs dans K, et ρ : 𝒢→𝒢' un ψ-morphisme…'",
    (31, "dans $\\mathbf{K}$,\nl'application"): "(3.5.3): '…pour tout faisceau ℱ sur X à valeurs dans K, l'application'",
    (31, "$\\mathbf{K}$),"): "(3.5.3): '…(où ℱ est un faisceau sur X à valeurs dans K), on posera…'",
    (32, "catégorie $\\mathbf{K}$ soit"): "(3.5.4): 'Supposons maintenant que la catégorie K soit telle (¹) que…'",
    (32, "$\\mathbf{K}$.}"): "footnote (1) to (3.5.4): '…des images réciproques de préfaisceaux à valeurs dans K.'",
}

kfind = []
for n in PAGES:
    t = texts[n]
    body0 = t.index("\n", t.index("\\oldpage")) + 1  # skip the '% from' line and the marker line
    for m in re.finditer(re.escape(KTOK), t):
        i, j = m.start(), m.end()
        a, b = word_bounds(t, i, j)
        # add one word at a time, alternately on the left and on the right, never taking in another \mathbf{K}
        for step in range(20):
            s = t[a:b]
            if t.count(s) == 1:
                break
            na = a
            while na > body0 and t[na - 1].isspace():
                na -= 1
            while na > body0 and not t[na - 1].isspace():
                na -= 1
            nb = b
            while nb < len(t) and t[nb].isspace():
                nb += 1
            while nb < len(t) and not t[nb].isspace():
                nb += 1
            left_ok = na < a and KTOK not in t[na:a]
            right_ok = nb > b and KTOK not in t[b:nb]
            if (step % 2 == 0 and left_ok) or not right_ok:
                assert left_ok, (n, s)
                a = na
            else:
                b = nb
        s = t[a:b]
        assert t.count(s) == 1 and s.count(KTOK) == 1, (n, s)
        # a readable snippet for 'where': four words before and three after
        wa, wb = word_bounds(t, i, j)
        for _ in range(4):
            while wa > body0 and t[wa - 1].isspace():
                wa -= 1
            while wa > body0 and not t[wa - 1].isspace():
                wa -= 1
        for _ in range(3):
            while wb < len(t) and t[wb].isspace():
                wb += 1
            while wb < len(t) and not t[wb].isspace():
                wb += 1
        where = f"{env_at(n, t, i)}: '…{plain(t[wa:wb])}…'"
        where = WHERE_OVERRIDE.get((n, s), where)
        kfind.append(F(n, where, "bold italic K (the category K)", "\\mathbf{K} (bold upright)", "font",
                       {"old": s, "new": s.replace(KTOK, "\\boldsymbol{K}")},
                       "The category K is printed in bold italic on every occurrence on pp. 31-34 (checked on crops "
                       "on pp. 31 and 34); \\mathbf gives a bold upright K. Same pattern as convention 10 for P; not "
                       "one of the listed conventions."))

findings = sorted(manual + kfind, key=lambda x: (x["page"], texts[x["page"]].find(x["fix"]["old"]) if x["fix"] else 0))

# ---- checks on the page files
ok = True
for n in PAGES:
    t = texts[n]
    spans = []
    for x in findings:
        if x["page"] != n or not x["fix"]:
            continue
        o = x["fix"]["old"]
        c = t.count(o)
        if c != 1:
            ok = False
            print("NOT UNIQUE", n, c, repr(o))
        s = t.find(o)
        spans.append((s, s + len(o), o))
    spans.sort()
    for (s1, e1, o1), (s2, e2, o2) in zip(spans, spans[1:]):
        if s2 < e1:
            ok = False
            print("OVERLAP", n, repr(o1), repr(o2))

# ---- page files against the release segments, and simulation of apply_fixes.py in memory
rel = REL.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[" + re.escape("0\\textsubscript{I}") + r"\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for k, (p, s) in enumerate(cuts):
        if p == page:
            return s, cuts[k + 1][1] if k + 1 < len(cuts) else len(t)


for n in PAGES:
    s, e = locate(rel, n)
    seg = rel[s:e]
    body = texts[n][texts[n].index("\n") + 1:]
    if seg != body:
        print("page file differs from release segment:", n, len(seg), len(body))
sim = rel
for order in ("forward", "reverse"):
    sim = rel
    seq = findings if order == "forward" else list(reversed(findings))
    for x in seq:
        if not x["fix"]:
            continue
        s, e = locate(sim, x["page"])
        seg = sim[s:e]
        if seg.count(x["fix"]["old"]) != 1:
            ok = False
            print("SIM FAIL", order, x["page"], repr(x["fix"]["old"]), seg.count(x["fix"]["old"]))
            continue
        sim = sim[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + sim[e:]
    if order == "forward":
        sim_fwd = sim
    else:
        assert sim == sim_fwd, "order dependence"
for n in (34, 35):
    i = sim_fwd.find(M % n)
    print(f"--- around marker {n} after simulation:\n" + sim_fwd[i - 120:i + 160])
print("K occurrences on pages:", {n: texts[n].count(KTOK) for n in PAGES},
      "| \\mathbf{K} left after simulation in pages 31-35:",
      sum(sim_fwd[slice(*locate(sim_fwd, n))].count(KTOK) for n in PAGES),
      "| ^b left:", sum(len(re.findall(r"\^b(?![a-z])", sim_fwd[slice(*locate(sim_fwd, n))])) for n in PAGES))
counts = {}
for x in findings:
    k = "misprint" if x["kind"] == "misprint_in_print" else "convention" if x["kind"] == "convention" else "normal"
    counts.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print("counts", counts, "total", len(findings), "checks ok" if ok else "CHECKS FAILED")
if ok:
    OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1), encoding="utf-8")
    print("written", OUT)
