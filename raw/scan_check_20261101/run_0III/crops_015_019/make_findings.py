"""Write findings_015_019.json for 0_III pp. 15-19 and check every fix.

Checks: (1) each fix's "old" occurs exactly once in its page_NNN.tex (CRLF normalised to LF);
(2) applied in list order to the release file exactly as apply_fixes.py does (page segment = from the page's first
\\oldpage marker to the next marker, "old" must occur once in the segment at that moment), every fix applies.
The release file itself is not written.
"""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0III")
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                   r"\packages\BASE\native\ega3\ega3-1-fr.tex")
OUT = RUN / "findings_015_019.json"
NL = "\n"
BOLD0 = r"$\mathbf{0}_{\mathrm I}$"


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


f = []
# ---------------------------------------------------------------- page 15
f.append(F(15, "proof of (9.2.2), 2nd line: 'soit E = ⋃_{i=1}^n (U_i ∩ F_i) une partie constructible'",
           "the lower limit 'i=1' of ⋃ is set in bold (bold italic i, bold 1); the upper limit n is light",
           r"\bigcup_{i=1}^n (plain i and 1): silent correction", "misprint_in_print", None, "medium",
           r"\bigcup_{i=1}^n", r"\bigcup_{\boldsymbol{i}=\mathbf{1}}^n",
           "Wrong-font sorts, checked on a 4x crop and by ink measurement: the i of the limit has about 1.5 times the "
           "stroke area of the ordinary subscript i's of the page (88 px against 51-68 px at the same height) and the 1 "
           "is heavier than the subscript 1's of p. 19 (118 against 83-99 px); the = is normal weight. Apply only if "
           "wrong-font sorts are reproduced, as for the bold italic n of EGA II pp. 49, 168-173.",
           corrected=r"\bigcup_{i=1}^n"))
f.append(F(15, "same formula: '(U_i ∩ F_i)'",
           "the subscript i of F_i is bold italic; the i of U_i beside it is light",
           r"F_i (plain i): silent correction", "misprint_in_print", None, "medium",
           r"\cap F_i)$ une", r"\cap F_{\boldsymbol{i}})$ une",
           "Wrong-font sort, checked on a 5x crop and by ink measurement: stroke area 85 px against 58 px for the i of "
           "U_i in the same parentheses, at the same height. Apply only if wrong-font sorts are reproduced.",
           corrected=r"(U_i\cap F_i)"))
f.append(F(15, "after (9.2.2): 'Lorsque X admet un point générique x (0_I, 2.1.2)'",
           "(𝟎_I, 2.1.2): bold 0", r"$0_{\mathrm I}$", "convention", 2, "high",
           "[0.2.1.2-fr]{$0_{\\mathrm I}$", "[0.2.1.2-fr]{" + BOLD0, ""))
f.append(F(15, "proof of (9.2.3): 'rare dans l'espace irréductible Y (0_I, 2.1.1)'",
           "(𝟎_I, 2.1.1): bold 0", r"$0_{\mathrm I}$", "convention", 2, "high",
           "[0.2.1.1-fr]{$0_{\\mathrm I}$", "[0.2.1.1-fr]{" + BOLD0, ""))
f.append(F(15, "proof of (9.2.3): 'récurrence noethérienne (0_I, 2.2.2) à l'ensemble 𝔉'",
           "(𝟎_I, 2.2.2): bold 0", r"$0_{\mathrm I}$", "convention", 2, "high",
           "{$0_{\\mathrm I}$, 2.2.2}) à l'ensemble" + NL + r"$\mathfrak{F}$",
           "{" + BOLD0 + ", 2.2.2}) à l'ensemble" + NL + r"$\mathfrak{F}$", ""))
f.append(F(15, "proof of (9.2.3): 'nécessairement en nombre fini (0_I, 2.2.5)'",
           "(𝟎_I, 2.2.5): bold 0", r"$0_{\mathrm I}$", "convention", 2, "high",
           "[0.2.2.5-fr]{$0_{\\mathrm I}$", "[0.2.2.5-fr]{" + BOLD0, ""))
f.append(F(15, "proof of (9.2.3): 'ou bien E contient un ouvert non vide U de E, donc est réunion de U'",
           "'un ouvert non vide U de E' (checked on a crop)",
           r"keeps the printed reading: 'un ouvert non vide $U$ de $E$'", "misprint_in_print", None, "high",
           None, None,
           "Read 'de X': with Y = X the hypothesis gives a non-empty open subset of X contained in E, and the next "
           "clause ('X—U est un ensemble fermé distinct de X') needs U open in X. The corrected edition (current) "
           "already reads 'de $X$'.",
           corrected=r"ou bien $E$ contient un ouvert non vide $U$ de $X$"))
f.append(F(15, "proof of (9.2.3): 'donc est réunion de U et de E∩(X—U)'",
           "E∩(X—U): long dash", r"$E\cap(X\setminus U)$", "convention", 7, "high",
           r"et de $E\cap(X\setminus U)$", r"et de $E\cap(X\setmin U)$",
           r"The TeX has \setminus (∖), not a minus sign; same remedy as the minus-sign cases (\setmin)."))
f.append(F(15, "proof of (9.2.3): 'mais X—U est un ensemble fermé distinct de X'",
           "X—U: long dash", r"$X\setminus U$", "convention", 7, "high",
           r"mais $X\setminus U$", r"mais $X\setmin U$", r"\setminus in the TeX, as above."))
f.append(F(15, "proof of (9.2.3): 'donc E∩(X—U) est constructible'",
           "E∩(X—U): long dash", r"$E\cap(X\setminus U)$", "convention", 7, "high",
           r"donc $E\cap(X\setminus U)$", r"donc $E\cap(X\setmin U)$", r"\setminus in the TeX, as above."))
f.append(F(15, "proof of (9.2.4): 'récurrence noethérienne (0_I, 2.2.2) à l'ensemble 𝔐'",
           "(𝟎_I, 2.2.2): bold 0", r"$0_{\mathrm I}$", "convention", 2, "high",
           "{$0_{\\mathrm I}$, 2.2.2}) à l'ensemble" + NL + r"$\mathfrak{M}$",
           "{" + BOLD0 + ", 2.2.2}) à l'ensemble" + NL + r"$\mathfrak{M}$", ""))
f.append(F(15, "proof of (9.2.4): 'il existe β tel que X = Ē_β'",
           "Ē_β: the bar covers E only, the subscript β stands outside it (crop at 3x)",
           r"$X=\overline{E_\beta}$", "formula", None, "high",
           r"$X=\overline{E_\beta}$", r"$X=\overline{E}_\beta$",
           "Same meaning; the analogue of convention 8 for a bar."))
f.append(F(15, "proof of (9.2.4): 'Mais alors l'ensemble fermé X—U est contenu dans un E_γ'",
           "X—U: long dash", r"$X\setminus U$", "convention", 7, "high",
           r"$X\setminus U$ est contenu", r"$X\setmin U$ est contenu", r"\setminus in the TeX, as above."))
# ---------------------------------------------------------------- page 16
f.append(F(16, "first line: 'donc Y = {y}‾ ⊂ Ē_α'",
           "Ē_α: the bar covers E only (crop at 3x)", r"\overline{E_\alpha}", "formula", None, "high",
           r"\subset\overline{E_\alpha}$", r"\subset\overline{E}_\alpha$",
           "Same meaning; the analogue of convention 8 for a bar."))
f.append(F(16, "Proposition (9.2.5): 'cela signifie aussi (9.2.2) que y∈E'",
           "the reference (9.2.2) is upright between the italic words (crop)",
           r"(\hyperref[0.9.2.2-fr]{9.2.2}) inside the italic proposition: italic", "convention", 6, "high",
           r"aussi (\hyperref[0.9.2.2-fr]{9.2.2}) que", r"aussi \textup{(\hyperref[0.9.2.2-fr]{9.2.2})} que",
           r"Form of the fix as for EGA I (\textup around the reference)."))
f.append(F(16, "proof of (9.2.5): 'x est par hypothèse intérieur à E∩(X—U)'",
           "E∩(X—U): long dash", r"$E\cap(X\setminus U)$", "convention", 7, "high",
           "intérieur à" + NL + r"$E\cap(X\setminus U)$", "intérieur à" + NL + r"$E\cap(X\setmin U)$",
           r"\setminus in the TeX, not a minus sign."))
f.append(F(16, "proof of (9.2.5): 'par rapport à X—U'",
           "X—U: long dash", r"$X\setminus U$", "convention", 7, "high",
           r"par rapport à $X\setminus U$", r"par rapport à $X\setmin U$", r"\setminus in the TeX."))
f.append(F(16, "proof of (9.2.5): 'donc l'adhérence dans X de X—E ne contient pas x'",
           "X—E: long dash", r"$X\setminus E$", "convention", 7, "high",
           r"$X\setminus E$", r"$X\setmin E$", r"\setminus in the TeX."))
f.append(F(16, "Définition (9.3.1): 'On dit que h est constructible si h^{-1}(t) est constructible'",
           "'constructible' italic like the rest of the definition (no change of face; crop)",
           r"\emph{constructible} inside the italic definition: upright", "convention", 6, "high",
           r"\emph{constructible} si", "constructible si",
           r"\emph inside the italic environment sets the word upright; the print has no change of face."))
f.append(F(16, "Définition (9.3.1): 'On dit que h est localement constructible si tout x∈X'",
           "'localement constructible' italic like the rest (crop)",
           r"\emph{localement constructible}: upright", "convention", 6, "high",
           r"\emph{localement constructible}", "localement constructible", "As above."))
# ---------------------------------------------------------------- page 17
f.append(F(17, "proof of (9.3.2): 'la restriction de h à X—U est constructible'",
           "X—U: long dash", r"$X\setminus U$", "convention", 7, "high",
           r"$X\setminus U$", r"$X\setmin U$", r"\setminus in the TeX, not a minus sign."))
f.append(F(17, "Proposition (9.3.4): 'toute générisation (0_I, 2.1.2) x' de x'",
           "(𝟎_I, 2.1.2): bold 0", r"$0_{\mathrm I}$", "convention", 2, "high",
           r"(\hyperref[0.2.1.2-fr]{$0_{\mathrm I}$, 2.1.2})",
           r"\textup{(\hyperref[0.2.1.2-fr]{$\mathbf{0}_{\mathrm I}$, 2.1.2})}",
           "One edit for this finding and the next (convention 6): bold 0 and the upright reference together."))
f.append(F(17, "Proposition (9.3.4): same reference '(0_I, 2.1.2)'",
           "the reference is upright inside the italic statement (crop)",
           r"(\hyperref[0.2.1.2-fr]{...}) inside the italic proposition: italic", "convention", 6, "high",
           None, None, "Covered by the edit of the preceding finding (convention 2), which adds the \\textup."))
f.append(F(17, "display (10.1.1.2): 'φ : gr_0(M) ⊗_{gr_0(A)} gr(A) → gr(M)'",
           "the subscript 0 of the first gr_0(M) is a bold 0; the 0 of gr_0(A) is light (crop at 6x)",
           r"\operatorname{gr}_0(M) (plain 0): silent correction", "misprint_in_print", None, "high",
           r"\operatorname{gr}_0(M)\otimes", r"\operatorname{gr}_{\mathbf{0}}(M)\otimes",
           "Wrong-font sort (bold figure in a subscript).", corrected=r"\operatorname{gr}_0(M)"))
f.append(F(17, "display (10.1.1.2): subscript 'gr_0(A)' of ⊗",
           "the closing parenthesis of gr_0(A) is a heavy (bold) parenthesis, taller than the opening one",
           r"\operatorname{gr}_0(A) with an ordinary parenthesis: silent correction", "misprint_in_print", None,
           "medium", r"_{\operatorname{gr}_0(A)}", r"_{\operatorname{gr}_0(A\boldsymbol{)}}",
           "Wrong-font sort, crop at 8x: ink area 150 px against 57 px for the opening parenthesis, 30 px high "
           "against 23. Punctuation, not a letter: drop this edit if wrong-font punctuation is not reproduced.",
           corrected=r"\operatorname{gr}_0(A)"))
# ---------------------------------------------------------------- page 18
f.append(F(18, "(10.1.2), first line: 'Supposons vérifiée l'une des hypothèses suivantes'",
           "'une' in italics (crop)", "l'une des hypothèses (roman)", "italics", None, "high",
           "vérifiée l'une des", r"vérifiée l'\emph{une} des",
           "The 'l'une des hypothèses (i), (ii)' of (10.1.3) is roman in the print, as in the TeX."))
f.append(F(18, "(10.1.3), case (ii): 'sur un anneau local noethérien'",
           "'local noethérien' both italic (crop)", r"local \emph{noethérien}", "italics", None, "high",
           "anneau local" + NL + r"    \emph{noethérien}", r"anneau \emph{local" + NL + "    noethérien}", ""))
f.append(F(18, "(10.2.1), last line: 'séparé pour la topologie 𝔍-préadique'",
           "préadique (no hyphen after pré; crop)", "pré-adique", "word", None, "high",
           r"$\mathfrak{J}$-pré-adique.", r"$\mathfrak{J}$-préadique.",
           "ega3-1-fr.tex writes 'préadique' 23 times elsewhere; the four 'pré-adique' are all on pp. 18-19."))
f.append(F(18, "(10.2.1): 'Il en est de même si A est noethérien et en outre si M est idéalement séparé'",
           "'et en outre si M est' (line 6 from the bottom of p. 18)",
           "keeps the printed reading 'et en outre si $M$ est'", "misprint_in_print", None, "high", None, None,
           "Authors' erratum, EGA IV, Errata et addenda (liste 3): '(0_III, 10.2.1). Ligne 6 du bas de la p. 18, "
           "remplacer : « en outre si » par : « si en outre »' (ega4-errata-addenda-list3-fr.tex). Not yet in the "
           "corrected edition.",
           corrected=r"et si en outre $M$ est \emph{idéalement séparé}"))
f.append(F(18, "(10.2.2): 'M un B-module de type fini'",
           "'module' in italics (B-module; crop)", "$B$-module (roman)", "italics", None, "high",
           r"$M$ un $B$-module de type fini", r"$M$ un $B$-\emph{module} de type fini", ""))
f.append(F(18, "(10.2.2): 'lorsque M est considéré comme A-module'",
           "'module' in italics (A-module; crop)", "$A$-module (roman)", "italics", None, "high",
           r"comme $A$-module, les conditions", r"comme $A$-\emph{module}, les conditions", ""))
f.append(F(18, "(10.2.2): 'les conditions a), b), c), d) de (10.2.1) sont équivalentes'",
           "'équivalentes' in italics (crop)", "équivalentes (roman)", "italics", None, "high",
           r"{10.2.1}) sont équivalentes.", r"{10.2.1}) sont \emph{équivalentes}.", ""))
# ---------------------------------------------------------------- page 19 (marker move: removal first)
f.append(F(19, r"page marker \oldpage[0\textsubscript{III}]{19}",
           "printed p. 19 begins with the paragraph 'Ce résultat s'applique surtout lorsque A et B sont des anneaux "
           "locaux noethériens' (second paragraph of (10.2.2)); p. 18 ends with '... de (10.2.1) sont équivalentes.'",
           r"the marker stands after \end{env} of (10.2.2), before \begin{env}[10.2.3]", "marker", None, "high",
           r"\oldpage[0\textsubscript{III}]{19}" + NL + r"\begin{env}[10.2.3]", r"\begin{env}[10.2.3]",
           "Move, part 1 of 2: remove the marker here; the next finding (p. 18) inserts it before 'Ce résultat "
           "s'applique surtout'. Apply in this order."))
f.append(F(18, "(10.2.2), second paragraph 'Ce résultat s'applique surtout lorsque ...' (printed at the top of p. 19)",
           "this paragraph is the first text of printed p. 19",
           "the paragraph lies before the p. 19 marker", "marker", None, "high",
           NL + "Ce résultat s'applique surtout lorsque",
           NL + r"\oldpage[0\textsubscript{III}]{19}" + NL + "Ce résultat s'applique surtout lorsque",
           "Move, part 2 of 2: after the removal in the previous finding. The paragraph itself matches the print "
           "(locaux, local, maximal, libres italic)."))
f.append(F(19, "(10.2.3): 'le séparé complété de A pour la topologie 𝔍-préadique'",
           "préadique (crop)", "pré-adique", "word", None, "high",
           r"$\mathfrak{J}$-pré-adique, $\widehat M$", r"$\mathfrak{J}$-préadique, $\widehat M$", ""))
f.append(F(19, "(10.2.3): 'pour la topologie 𝔍B-préadique'",
           "préadique (crop)", "pré-adique", "word", None, "high",
           r"$\mathfrak{J}B$-pré-adique", r"$\mathfrak{J}B$-préadique", ""))
f.append(F(19, "(10.2.4), label of condition a)",
           "upright 'a)' (crop); the labels of (10.2.5) are italic", r"\item[$a)$] (italic a)", "font", None,
           "high", r"\item[$a)$] $u$ est injectif", r"\item[a)] $u$ est injectif",
           "Form of the fix as on EGA 0_I p. 53."))
f.append(F(19, "(10.2.4), label of condition b)",
           "upright 'b)' (crop)", r"\item[$b)$] (italic b)", "font", None, "high",
           r"\item[$b)$] $u\otimes1", r"\item[b)] $u\otimes1", ""))
f.append(F(19, "(10.2.5): 'On suppose que B est un A-module plat Alors les conditions'",
           "no full stop after 'plat' (crop)", r"keeps the printed reading '\emph{plat} Alors'",
           "misprint_in_print", None, "high", None, None,
           "The corrected edition (current) already has the full stop.",
           corrected=r"\emph{plat}. Alors"))
f.append(F(19, "proof of (10.2.6): 'donc séparés pour la topologie 𝔍-préadique'",
           "préadique (crop)", "pré-adique", "word", None, "high",
           r"séparés pour la topologie $\mathfrak{J}$-pré-adique",
           r"séparés pour la topologie $\mathfrak{J}$-préadique", ""))
f.append(F(19, "proof of (10.2.6): '(0_I, 7.3.5)'",
           "(𝟎_I, 7.3.5): bold 0", r"$0_{\mathrm I}$", "convention", 2, "high",
           "[0.7.3.5-fr]{$0_{\\mathrm I}$", "[0.7.3.5-fr]{" + BOLD0, ""))
f.append(F(19, "proof of (10.2.6): 'l'homomorphisme v̂ : (M⊗_A N')^ → (M⊗_A N)^', first term",
           "(M⊗_A N')^: the hat is written after the closing parenthesis (crop)",
           r"\widehat{(M\otimes_A N')}", "formula", None, "high",
           r"\widehat{(M\otimes_A N')}", r"(M\otimes_A N'){\,\widehat{\,}\,}",
           r"The analogue of convention 5 for a hat; replacement as on EGA I p. 199 ((g\circ f){\,\widehat{\,}\,})."))
f.append(F(19, "same formula, second term (M⊗_A N)^",
           "(M⊗_A N)^: hat after the closing parenthesis", r"\widehat{(M\otimes_A N)}", "formula", None, "high",
           r"\widehat{(M\otimes_A N)}", r"(M\otimes_A N){\,\widehat{\,}\,}", "As above."))
f.append(F(19, "Corollaire (10.2.7): 'l'homothétie f_M : x→fx'",
           "plain arrow → (crop at 2.5x)", r"$f_M:x\mapsto fx$", "convention", 3, "high",
           r"$f_M:x\mapsto fx$", r"$f_M:x\to fx$", ""))
f.append(F(19, "proof of (10.2.7): 'Posons M_i : f^iM pour i≥0'",
           "'M_i : f^iM' with a colon instead of = (crop at 3x)", r"$M_i=f^iM$: silent correction",
           "misprint_in_print", None, "high", r"$M_i=f^iM$", r"$M_i:f^iM$",
           "The print's colon is a misprint for =; the diplomatic text reproduces it.",
           corrected=r"$M_i=f^iM$"))
f.append(F(19, "proof of (10.2.7): 'pour tout i≥0 (0_I, 6.1.2)'",
           "(𝟎_I, 6.1.2): bold 0", r"$0_{\mathrm I}$", "convention", 2, "high",
           "[0.6.1.2-fr]{$0_{\\mathrm I}$", "[0.6.1.2-fr]{" + BOLD0, ""))

# ---------------------------------------------------------------- checks
ok = True
for x in f:
    if not x["fix"]:
        continue
    t = (RUN / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    n = t.count(x["fix"]["old"])
    if n != 1:
        ok = False
        print("PAGE-FILE COUNT", n, "p.", x["page"], repr(x["fix"]["old"]))

rel = REL.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[0\\textsubscript\{III\}\]\{(\d+)\}")


def locate(text, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(text)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            return s, cuts[i + 1][1] if i + 1 < len(cuts) else len(text)
    return None, None


for x in f:
    if not x["fix"]:
        continue
    s, e = locate(rel, x["page"])
    seg = rel[s:e]
    n = seg.count(x["fix"]["old"])
    if n != 1:
        ok = False
        print("RELEASE SEGMENT COUNT", n, "p.", x["page"], repr(x["fix"]["old"]))
        continue
    rel = rel[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + rel[e:]

OUT.write_text(json.dumps(f, ensure_ascii=False, indent=1), encoding="utf-8")
counts = {}
for x in f:
    c = counts.setdefault(x["page"], [0, 0, 0])
    c[1 if x["kind"] == "convention" else 2 if x["kind"] == "misprint_in_print" else 0] += 1
print("all checks passed" if ok else "CHECK FAILURES")
print("counts normal/convention/misprint:", {p: "/".join(map(str, c)) for p, c in sorted(counts.items())})
print("written", OUT, len(f), "findings")
# show the result around the moved marker
k = rel.find(r"\oldpage[0\textsubscript{III}]{19}")
print(repr(rel[k - 120:k + 120]))
k2 = rel.find(r"\begin{env}[10.2.3]")
print(repr(rel[k2 - 80:k2 + 30]))
