"""Build findings_090_094.json; '¶' in old/new stands for a line break (LF).
Checks: every old occurs exactly once in its page_NNN.tex (CR removed) and in its release-file page segment;
then all edits are applied in order to in-memory copies of the release files (apply_fixes.py logic)."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV3\native\ega4")
OUT = RUN / "findings_090_094.json"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note=""):
    fix = None
    if old is not None:
        fix = {"old": old.replace("¶", "\n"), "new": new.replace("¶", "\n")}
    F.append({"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
              "confidence": conf, "fix": fix, "note": note})


BOTH = "ega4-9-fr.tex has a blank line on both sides of this marker; both must go at a mid-sentence break (GLOBAL_ISSUES 20)."

# ---------------- page 89 (outside the range: blank line before the p. 90 marker) ----------------
add(89, "end of page_089.tex, page break 89/90: '... (X_i)_η ne contient pas le | point générique de (Z_j)_η'",
    "p. 89 ends '... (X_i)_η ne contient pas le'; p. 90 begins 'point générique de (Z_j)_η, donc ...' flush left: one sentence, no paragraph break (page_089_s4.png, page_090_s1.png)",
    "blank line between 'ne contient pas le' and \\oldpage[IV-3]{90}: paragraph break mid-sentence",
    "marker", None, "high",
    r"$(X_i)_\eta$ ne contient pas le¶¶", r"$(X_i)_\eta$ ne contient pas le¶",
    "OUTSIDE pp. 90-94: the line is the end of page_089.tex (ega4-9-fr.tex, just before \\oldpage[IV-3]{90}); filed under page 89 so that it is found there. Pair with the p. 90 entry (blank line after the marker). " + BOTH + " The marker itself is in the right place; the pp. 85-89 checker may report the same line.")

# ---------------- page 90 ----------------
add(90, "top of p. 90: blank line after \\oldpage[IV-3]{90}",
    "'point générique de (Z_j)_η, donc' (first line of p. 90) continues the sentence of p. 89, flush left",
    "blank line after the marker: paragraph break mid-sentence",
    "marker", None, "high",
    r"\oldpage[IV-3]{90}¶¶point générique", r"\oldpage[IV-3]{90}¶point générique",
    "Pair with the page-89 entry (blank line before the marker). " + BOTH)
add(90, "Proposition (9.9.2) (ii): 'relatives à k(f(x))'", "bold italic k in k(f(x)) (crop)", "$k(f(x))$",
    "convention", 1, "high", r"relatives à $k(f(x))$", r"relatives à $\boldsymbol{k}(f(x))$")
for lab, tail in [("i", " L'ensemble des points"), ("ii", " L'ensemble des $x\\in X$ tels que les longueurs"),
                  ("iii", " L'ensemble"), ("iv", " L'ensemble"), ("v", " L'ensemble"), ("vi", " L'ensemble"),
                  ("vii", " L'ensemble"), ("viii", " L'ensemble"), ("ix", " L'ensemble")]:
    add(90, f"Proposition (9.9.2), label ({lab})", f"label ({lab}) upright inside the italic statement (crop)",
        f"\\item[({lab})] italic inside the italic proposition environment", "convention", 6, "high",
        f"\\item[({lab})]{tail}", f"\\item[\\textup{{({lab})}}]{tail}", "Roman-numeral labels upright (GLOBAL_ISSUES 16).")
for ref, old_tpl in [("5.1.12", "au point $x$ ({r})."), ("4.7.5", "({r}), appartiennent"), ("4.6.17", "au point $x$ ({r})."),
                     ("4.6.22", "au point $x$ ({r})."), ("5.7.2", "au point $x$ ({r})."), ("5.7.1", "au point $x$ ({r}).")]:
    add(90, f"Proposition (9.9.2): reference ({ref})", f"({ref}) upright inside the italic statement (crop)",
        f"({ref}) set in the italic proposition environment", "convention", 6, "high",
        old_tpl.format(r=ref), old_tpl.replace("({r})", "\\textup{{({r})}}").format(r=ref))
add(90, "end of p. 90, page break 90/91: '... aux points de S' sont les mêmes, | donc on peut remplacer S par S''",
    "p. 91 begins 'donc on peut remplacer ...' flush left: the sentence continues; no paragraph break",
    "blank line between 'sont les mêmes,' and \\oldpage[IV-3]{91}: paragraph break mid-sentence",
    "marker", None, "high",
    r"$S'$ sont les mêmes,¶¶", r"$S'$ sont les mêmes,¶",
    "Last line of page_090.tex. Pair with the p. 91 entry (blank line after the marker). " + BOTH)

# ---------------- page 91 ----------------
add(91, "top of p. 91: blank line after \\oldpage[IV-3]{91}",
    "'donc on peut remplacer S par S'' (first line of p. 91) continues the sentence of p. 90, flush left",
    "blank line after the marker: paragraph break mid-sentence",
    "marker", None, "high",
    r"\oldpage[IV-3]{91}¶¶donc on peut", r"\oldpage[IV-3]{91}¶donc on peut",
    "Pair with the p. 90 end-of-page entry. " + BOTH)
add(91, "proof of (9.9.2) (v): 'les composantes irréductibles de Y'_η' soient géométriquement irréductibles.'",
    "'géométri-|quement irréductibles' in italics (crop)", "upright", "italics", None, "high",
    r"soient géométriquement irréductibles.", r"soient \emph{géométriquement irréductibles}.")
add(91, "proof of (9.9.2) (v), last lines: 'les composantes irréductibles de Y_η sont géométriquement irréductibles;'",
    "'géométriquement irréduc-|tibles' in italics (crop)", "upright", "italics", None, "high",
    r"sont géométriquement irréductibles~;", r"sont \emph{géométriquement irréductibles}~;")
add(91, "end of p. 91, page break 91/92: '... telles que les Z_i∩X_η soient les | composantes irréductibles de Y_η'",
    "p. 92 begins 'composantes irréductibles de Y_η, il résulte ...' flush left: the sentence continues",
    "blank line between 'soient les' and \\oldpage[IV-3]{92}: paragraph break mid-sentence",
    "marker", None, "high",
    r"$Z_i\cap X_\eta$ soient les¶¶", r"$Z_i\cap X_\eta$ soient les¶",
    "Last line of page_091.tex. Pair with the p. 92 entry. " + BOTH)

# ---------------- page 92 ----------------
add(92, "top of p. 92: blank line after \\oldpage[IV-3]{92}",
    "'composantes irréductibles de Y_η' (first line of p. 92) continues the sentence of p. 91, flush left",
    "blank line after the marker: paragraph break mid-sentence",
    "marker", None, "high",
    r"\oldpage[IV-3]{92}¶¶composantes", r"\oldpage[IV-3]{92}¶composantes",
    "Pair with the p. 91 end-of-page entry. " + BOTH)
add(92, "proof of (9.9.2) (vi), l. 1-2: 'il résulte de (6.2.1) que l'on a dim.proj((F_s)_x)=dim.proj(((F_0)_{s_0})_{x_0}); on peut donc'",
    "formula in the running text ('que l'on a dim.proj(...)=dim.proj(...); on peut donc encore se borner au')",
    "displayed with \\[ ... \\]", "formula", None, "high",
    r"\[¶\operatorname{dim.proj}((\mathcal F_s)_x)=¶\operatorname{dim.proj}(((\mathcal F_0)_{s_0})_{x_0})~;¶\]¶on peut",
    r"$\operatorname{dim.proj}((\mathcal F_s)_x)=¶\operatorname{dim.proj}(((\mathcal F_0)_{s_0})_{x_0})$~;¶on peut",
    "No connecting word lost.")
add(92, "proof of (9.9.2) (vi): 'pour tout x'∈V, on ait dim.proj((F_{f(x')})_{x'})=dim.proj((F_{f(x)})_x); et comme ci-dessus'",
    "formula in the running text", "displayed with \\[ ... \\]", "formula", None, "high",
    r"\[¶\operatorname{dim.proj}((\mathcal F_{f(x')})_{x'})=¶\operatorname{dim.proj}((\mathcal F_{f(x)})_x)~;¶\]¶et comme",
    r"$\operatorname{dim.proj}((\mathcal F_{f(x')})_{x'})=¶\operatorname{dim.proj}((\mathcal F_{f(x)})_x)$~;¶et comme",
    "No connecting word lost.")
add(92, "proof of (9.9.2) (vi): 'et que F est f-plat;'", "'f-plat' in italics (crop)", "$f$-plat: hyphen and 'plat' upright",
    "italics", None, "high", r"$f$-plat~;", r"\emph{$f$-plat}~;")
add(92, "proof of (9.9.2) (vi): 'dim.proj((F_{f(x')})_{x'})=dim.proj(F_{x'}) pour tout x'∈X en vertu de (6.2.3)'",
    "'tout' in italics (crop)", "upright", "italics", None, "high",
    r"pour tout $x'\in X$ en vertu de", r"pour \emph{tout} $x'\in X$ en vertu de")
add(92, "proof of (9.9.2) (vi): 'dim.proj(F_{x'})≤dim.proj(F_x) pour tout x'∈X. D'autre part'",
    "'tout' in italics (crop)", "upright", "italics", None, "high",
    r"pour tout $x'\in X$. D'autre part", r"pour \emph{tout} $x'\in X$. D'autre part")
add(92, "proof of (9.9.2) (vii): 'X_s=Spec(k(s)[T_1, ..., T_r])'", "bold italic k (crop)", "$k(s)$",
    "convention", 1, "high", r"\operatorname{Spec}(k(s)[T_1", r"\operatorname{Spec}(\boldsymbol{k}(s)[T_1")
add(92, "display (9.9.2.1): 'dim.proj((F_{f(x)})_x)—codim_x(W_{f(x)}, X_{f(x)})'",
    "long dash for the subtraction (bar 42 px at 300 dpi; the = bars on the same line 34 px)", "minus sign",
    "convention", 7, "high", r"_x)-¶\operatorname{codim}_x", r"_x)\setmin¶\operatorname{codim}_x",
    "Subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision (FIX_POLICY 2.7).")
add(92, "proof of (9.9.2) (viii): 'posons Z_n=X—U_n'", "long dash (bar 42 px; = bars 35-36 px)", "$Z_n=X-U_n$",
    "convention", 7, "high", r"$Z_n=X-U_n$", r"$Z_n=X\setmin U_n$")
add(92, "proof of (9.9.2) (viii): 'les Z_n sont constructibles;'", "'constructibles' in italics (crop)", "upright",
    "italics", None, "high", r"sont constructibles~; en outre,", r"sont \emph{constructibles}~; en outre,")
add(92, "end of p. 92, page break 92/93 inside 'fonc-|tion': '... en outre, comme la fonc- | tion x⇝dim_x(W_{f(x)})'",
    "p. 92 ends 'en outre, comme la fonc-'; p. 93 begins 'tion x⇝dim_x(W_{f(x)}) est constructible' (one sentence)",
    "blank line between 'comme' and \\oldpage[IV-3]{93}: paragraph break mid-sentence",
    "marker", None, "high",
    r"¶comme¶¶", r"¶comme¶",
    "Last line of page_092.tex. Pair with the p. 93 marker move (which also removes the blank line after the marker); either order works. " + BOTH)

# ---------------- page 93 ----------------
add(93, "top of p. 93: marker before 'la fonction'; the page begins inside the word 'fonc-|tion'",
    "p. 92's last line ends 'comme la fonc-'; p. 93 begins 'tion x⇝dim_x(W_{f(x)}) est constructible en vertu de (9.9.1, (i))'",
    "\\oldpage[IV-3]{93} stands two words early, before 'la fonction', with a blank line after it (mid-sentence paragraph break)",
    "marker", None, "high",
    r"\oldpage[IV-3]{93}¶¶la fonction $x", r"la fonc%¶\oldpage[IV-3]{93}¶tion $x",
    "Moves the marker to the printed word break (as homo%|morphisme, 0_IV-1 p. 138; irréduc%|tible, IV-1 p. 226) and drops the blank line after it; pair with the p. 92 end-of-page entry. Does not overlap the arrow entry below.")
add(93, "first line: 'tion x⇝dim_x(W_{f(x)})'", "wavy arrow ⇝ (crop)", "\\mapsto", "symbol", None, "high",
    r"\mapsto\dim_x(W_{f(x)})", r"\leadsto\dim_x(W_{f(x)})", "Wavy arrow (GLOBAL_ISSUES 33).")
add(93, "Corollaire (9.9.3): 'P l'une des propriétés'", "bold italic P (crop)", "$\\mathbf P$",
    "convention", 10, "high", r"$\mathbf P$ l'une des propriétés", r"$\boldsymbol{P}$ l'une des propriétés")
add(93, "Corollaire (9.9.3): 'l'une des propriétés (i) à (ix) de (9.9.2).'",
    "(i), (ix) and (9.9.2) upright inside the italic statement; 'à', 'de' italic (crop)",
    "all italic (corollary environment)", "convention", 6, "high",
    r"(i) à (ix) de (9.9.2). Alors", r"\textup{(i)} à \textup{(ix)} de \textup{(9.9.2)}. Alors")
add(93, "Corollaire (9.9.3): 'la propriété P soit vraie'", "bold italic P (crop)", "$\\mathbf P$",
    "convention", 10, "high", r"$\mathbf P$ soit vraie en tous", r"$\boldsymbol{P}$ soit vraie en tous")
add(93, "proof of (9.9.3): 'des points où P est vraie'", "bold italic P (crop)", "$\\mathbf P$",
    "convention", 10, "high", r"où $\mathbf P$ est vraie", r"où $\boldsymbol{P}$ est vraie")
add(93, "proof of (9.9.3): 'il en est de même de X—E'", "long dash (bar 41 px; = bars 34-36 px)", "$X-E$",
    "convention", 7, "high", r"même de $X-E$", r"même de $X\setmin E$")
add(93, "proof of (9.9.3): 'donc f(X—E)'", "long dash (bar 42 px)", "$f(X-E)$",
    "convention", 7, "high", r"$f(X-E)$", r"$f(X\setmin E)$")
add(93, "Proposition (9.9.4), after its first sentence: '... localement de présentation finie. | L'ensemble des x∈X tels que ...'",
    "'L'ensemble des x∈X ...' begins a new, indented line: paragraph break inside the statement (crop)",
    "one paragraph", "other", None, "high",
    r"présentation finie. L'ensemble des", r"présentation finie.¶¶L'ensemble des",
    "Paragraph break; the statement stays italic.")
for lab, tail in [("i", " être géométriquement régulier"), ("ii", " posséder"), ("iii", " être géométriquement normal"),
                  ("iv", " être géométriquement réduit"), ("v", " être géométriquement ponctuellement")]:
    add(93, f"Proposition (9.9.4), label ({lab})", f"label ({lab}) upright inside the italic statement (crop)",
        f"\\item[({lab})] italic inside the italic proposition environment", "convention", 6, "high",
        f"\\item[({lab})]{tail}", f"\\item[\\textup{{({lab})}}]{tail}", "Roman-numeral labels upright (GLOBAL_ISSUES 16).")
add(93, "Proposition (9.9.4) (iv): 'être géométriquement réduit (i.e. séparable);'",
    "'(i.e.' and ')' upright, 'séparable' italic (crop)", "all italic", "convention", 6, "high",
    r"(i.e. séparable)", r"\textup{(i.e.} séparable\textup{)}")
add(93, "proof of (9.9.4), last line: 'posons F=X—L'", "long dash (bar 41 px; = bars 34-36 px)", "$F=X-L$",
    "convention", 7, "high", r"$F=X-L$", r"$F=X\setmin L$")
add(93, "end of p. 93, page break 93/94: '... Dire que X_s | vérifie la propriété géométrique (R_k)'",
    "p. 94 begins 'vérifie la propriété géométrique (R_k) au point ...' flush left: the sentence continues",
    "blank line between 'que $X_s$' and \\oldpage[IV-3]{94}: paragraph break mid-sentence",
    "marker", None, "high",
    r"que $X_s$¶¶", r"que $X_s$¶",
    "Last line of page_093.tex. Pair with the p. 94 entry. " + BOTH)

# ---------------- page 94 ----------------
add(94, "top of p. 94: blank line after \\oldpage[IV-3]{94}",
    "'vérifie la propriété géométrique (R_k)' (first line of p. 94) continues the sentence of p. 93, flush left",
    "blank line after the marker: paragraph break mid-sentence",
    "marker", None, "high",
    r"\oldpage[IV-3]{94}¶¶vérifie", r"\oldpage[IV-3]{94}¶vérifie",
    "Pair with the p. 93 end-of-page entry. " + BOTH)
add(94, "Corollaire (9.9.5): 'et notons P'", "bold italic P (crop)", "$\\mathbf P$",
    "convention", 10, "high", r"et notons $\mathbf P$", r"et notons $\boldsymbol{P}$")
add(94, "Corollaire (9.9.5): 'l'une des propriétés (i) à (v) de (9.9.4).'",
    "(i), (v) and (9.9.4) upright inside the italic statement; 'à', 'de' italic (crop)",
    "all italic (corollary environment)", "convention", 6, "high",
    r"(i) à (v) de (9.9.4). Alors", r"\textup{(i)} à \textup{(v)} de \textup{(9.9.4)}. Alors")
add(94, "Corollaire (9.9.5): 'la propriété P soit vraie'", "bold italic P (crop)", "$\\mathbf P$",
    "convention", 10, "high", r"la propriété $\mathbf P$ soit vraie", r"la propriété $\boldsymbol{P}$ soit vraie")
add(94, "Proposition (9.9.6): 'le complexe L_•⊗_{O_S}k(s)'", "bold italic k (crop)", "$k(s)$",
    "convention", 1, "high", r"\otimes_{\mathcal O_S}k(s)$", r"\otimes_{\mathcal O_S}\boldsymbol{k}(s)$")
add(94, "proof of (9.9.6): 'X_s=(X_0)_{s_0}⊗_{k(s_0)}k(s)', subscript k(s_0)", "bold upright k in the subscript (crop)",
    "$k(s_0)$", "convention", 1, "high", r"(X_0)_{s_0}\otimes_{k(s_0)}", r"(X_0)_{s_0}\otimes_{\mathbf{k}(s_0)}",
    "Bold upright in subscripts (GLOBAL_ISSUES 48).")
add(94, "proof of (9.9.6): 'X_s=(X_0)_{s_0}⊗_{k(s_0)}k(s)', k(s)", "bold italic k (crop)", "$k(s)$",
    "convention", 1, "high", r"k(s)$, et le morphisme", r"\boldsymbol{k}(s)$, et le morphisme")
add(94, "proof of (9.9.6): 'on en conclut que l'on a H_n((L_•)_s)=H_n((L^(0)_•)_{s_0})⊗_{k(s_0)}k(s), et par suite' (part 1 of 2)",
    "formula in the running text ('que l'on a | H_n(...)=...⊗k(s), et par suite, si E ...')",
    "displayed with \\[ ... \\]", "formula", None, "high",
    r"que l'on a¶\[¶\mathcal H_n", r"que l'on a¶$\mathcal H_n",
    "Part 1 of 2 (opens the inline formula); apply together with part 2. Neither part overlaps the convention-1 entry for this formula.")
add(94, "same formula (part 2 of 2): '... k(s), et par suite'", "formula in the running text, comma after it",
    "\\] after the comma", "formula", None, "high",
    r",¶\]¶et par suite", r"$,¶et par suite",
    "Part 2 of 2 (closes the inline formula before the comma); apply together with part 1.")
add(94, "same formula: '⊗_{k(s_0)}k(s)' (two occurrences of convention 1)",
    "bold upright k in the subscript k(s_0), bold italic k in k(s) (crop)", "k(s_0), k(s)",
    "convention", 1, "high", r"¶\otimes_{k(s_0)}k(s)", r"¶\otimes_{\mathbf{k}(s_0)}\boldsymbol{k}(s)",
    "One edit for two adjacent occurrences (the subscript k(s_0) and k(s)).")
add(94, "proof of (9.9.6): '(resp. x_0∈X_0) tels que (H_n((L_•)_{f(x)}))_x=0 (resp. (H_n((L^(0)_•)_{f_0(x_0)}))_{x_0}=0), on a E=h^{-1}(E_0)'",
    "both formulas in the running text, with '(resp.' and '),' in roman text",
    "displayed with \\[ ... \\quad\\text{(resp.}\\quad ... \\text{)}, \\]", "formula", None, "high",
    r"tels que¶\[¶(\mathcal H_n((\mathcal L_\bullet)_{f(x)}))_x=0¶\quad\text{(resp.}\quad¶(\mathcal H_n((\mathcal L_\bullet^{(0)})_{f_0(x_0)}))_{x_0}=0\text{)},¶\]¶on a",
    r"tels que¶$(\mathcal H_n((\mathcal L_\bullet)_{f(x)}))_x=0$¶(resp.¶$(\mathcal H_n((\mathcal L_\bullet^{(0)})_{f_0(x_0)}))_{x_0}=0$),¶on a",
    "No connecting word lost.")

# ---------------- checks ----------------
marker = re.compile(r"\\oldpage\[IV-3\]\{(\d+)\}")
rel_text = {p.name: p.read_text(encoding="utf-8") for p in REL.glob("ega4-*-fr.tex")}


def locate(texts, page):
    for name, t in texts.items():
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for i, (n, s) in enumerate(cuts):
            if n == page:
                j = i + 1
                while j < len(cuts) and cuts[j][0] == page:
                    j += 1
                return name, s, cuts[j][1] if j < len(cuts) else len(t)
    for name, t in texts.items():
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
            if a < page < b:
                return name, sa, sb
    return None, None, None


ok = True
for x in F:
    if not x["fix"]:
        continue
    old = x["fix"]["old"]
    pt = (RUN / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    c1 = pt.count(old)
    name, s, e = locate(rel_text, x["page"])
    c2 = rel_text[name][s:e].count(old)
    if c1 != 1 or c2 != 1:
        ok = False
        print("COUNT PROBLEM", x["page"], repr(old), c1, c2)
# sequential application, apply_fixes.py logic
texts = dict(rel_text)
for x in F:
    if not x["fix"]:
        continue
    name, s, e = locate(texts, x["page"])
    seg = texts[name][s:e]
    if seg.count(x["fix"]["old"]) != 1:
        ok = False
        print("APPLY PROBLEM", x["page"], repr(x["fix"]["old"]))
        continue
    texts[name] = texts[name][:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + texts[name][e:]
json.dump(F, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
print("all checks ok" if ok else "PROBLEMS")
for p in sorted({x["page"] for x in F}):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
# show the result around the page breaks
t = texts["ega4-9-fr.tex"]
for n in (90, 91, 92, 93, 94):
    m = re.search(r"\\oldpage\[IV-3\]\{%d\}" % n, t)
    print("----", n, repr(t[m.start() - 60:m.end() + 40]))
pathlib.Path(RUN / "crops_090_094" / "simulated_ega4-9.tex").write_text(t, encoding="utf-8", newline="\n")
