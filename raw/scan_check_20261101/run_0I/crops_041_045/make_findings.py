import json
import os
import sys

RUN = sys.argv[1]
OUT = os.path.join(RUN, 'findings_041_045.json')
NL = "\n"


def F(page, where, scan, tex, kind, conf, fix, note=None, convention=None, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": convention, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


def fx(old, new):
    return {"old": old, "new": new}


findings = []

# ---------------- page 41 ----------------
findings.append(F(
    41,
    "start of page_041.tex: \\oldpage{41} before the heading 4.3",
    "printed p. 40 ends with the heading '4.3. Image réciproque d'un B-Module.' and (4.3.1) up to "
    "'… Nous dirons que ce A-Module est l'image réci-'; printed p. 41 begins "
    "'proque de G par le morphisme Ψ et nous le noterons Ψ*(G).'",
    "\\oldpage[0\\textsubscript{I}]{41} stands before \\subsection{Image réciproque d'un $\\mathcal{B}$-Module}",
    "marker", "high",
    fx(r"\oldpage[0\textsubscript{I}]{41}" + NL + r"\subsection{", r"\subsection{"),
    "Part 1 of 2: deletes the misplaced marker. Part 2 (next finding) puts it inside 'réci|proque', "
    "where printed p. 41 begins (mid-word markers exist already: 'consi\\oldpage[III]{149}dérés', "
    "'sous-\\oldpage[I]{121}préschéma'). Apply both or neither. After the move the 4.3 heading and "
    "(4.3.1) up to 'l'image réci-' fall in p. 40's segment, as printed. ALREADY APPLIED in the r20 "
    "diplomatic ega0-1-fr.tex (from the p. 40 check, after page_041.tex was cut): the marker now stands on its "
    "own line between '\\emph{l'image' and 'réciproque'; skip unless the mid-word position is wanted."))

findings.append(F(
    41,
    "(4.3.1): 'Nous dirons que ce A-Module est l'image réciproque de G par le morphisme Ψ et nous le noterons Ψ*(G)' "
    "(across the p. 40/41 break)",
    "'l'image réci-' (last line of p. 40) and 'proque de G par le morphisme' (first line of p. 41) in italics; "
    "'Ψ et nous le noterons' upright; p. 41 begins with 'proque'",
    "est l'image réciproque de $\\mathcal{G}$ par le morphisme (upright; the p. 41 marker is not here)",
    "marker", "high",
    fx(r"est l'image réciproque de $\mathcal{G}$ par le morphisme",
       r"est \emph{l'image réci\oldpage[0\textsubscript{I}]{41}proque de $\mathcal{G}$ par le morphisme}"),
    "Part 2 of 2 of the marker move (apply with the previous finding); the same edit adds the print's italics "
    "for the defined term. Italics alone, without the move: new = "
    "'est \\emph{l'image réciproque de $\\mathcal{G}$ par le morphisme}'. ALREADY APPLIED in the r20 "
    "diplomatic ega0-1-fr.tex (italics and marker, marker at the word boundary before 'réciproque'); skip."))

findings.append(F(
    41,
    "(4.3.1), first sentence: 'Les hypothèses et notations étant celles de (4.2.1), soient G un B-Module et "
    "ψ*(G) son image réciproque' (printed on p. 40; in page_041.tex because the marker stands too early)",
    "soient (plural; checked on a crop of page_040_s3.png)",
    "soit $\\mathcal{G}$ un $\\mathcal{B}$-Module",
    "word", "high",
    fx(r"(4.2.1), soit $\mathcal{G}$ un", r"(4.2.1), soient $\mathcal{G}$ un"),
    "Printed on p. 40. ALREADY APPLIED in the r20 diplomatic ega0-1-fr.tex (it reads 'soient'); skip."))

findings.append(F(
    41,
    "(4.3.2): 'il est clair que ψ*(⊕G_i) = ⊕ψ*(G_i), donc, par produit tensoriel avec A_[θ],'",
    "comma after ψ*(G_i) (checked on a crop)",
    "=\\bigoplus_i\\psi^*(\\mathcal{G}_i)~; (semicolon, end of the display)",
    "punctuation", "high",
    fx(r"=\bigoplus_i\psi^*(\mathcal{G}_i)~;", r"=\bigoplus_i\psi^*(\mathcal{G}_i),"),
    "The print has this formula inline; the TeX displays it (layout, not reported)."))

findings.append(F(
    41,
    "(4.3.3), before (4.3.3.1): 'Par produit tensoriel avec A, on en déduit un isomorphisme canonique fonctoriel'",
    "'isomorphisme canonique' italic, 'fonctoriel' upright (checked on a crop; in (4.3.2) all three words are italic, "
    "as in the TeX)",
    "\\emph{isomorphisme canonique fonctoriel}",
    "italics", "high",
    fx(r"\emph{isomorphisme canonique fonctoriel}", r"\emph{isomorphisme canonique} fonctoriel"),
    None))

findings.append(F(
    41,
    "(4.3.4): 'il résulte aussitôt des définitions que la A-Algèbre Ψ*(B) est égale à A (à un isomorphisme "
    "canonique près)'",
    "'égale à' in italics (checked on a crop)",
    "est égale à (upright)",
    "italics", "high",
    fx(r"est égale à", r"est \emph{égale à}"),
    None))

# ---------------- page 42 ----------------
findings.append(F(
    42,
    "(4.4.2): 'est un Ψ''-morphisme que l'on appelle le composé de u et v.'",
    "only 'composé' is italic; 'de' and 'et' are upright (checked on a crop)",
    "\\emph{composé de $u$ et $v$}",
    "italics", "high",
    fx(r"\emph{composé de $u$ et $v$}", r"\emph{composé} de $u$ et $v$"),
    None))

for old, new, where in [
    (r"$v\mapsto v_\theta^\flat$", r"$v\to v_\theta^\flat$",
     "(4.4.3), after (4.4.3.1): 'que nous désignerons par v→v^♭_θ'"),
    (r"$v\mapsto v^\flat$", r"$v\to v^\flat$",
     "(4.4.3): '(ou simplement v→v^♭ si aucune confusion n'est possible)'"),
    (r"$u\mapsto u_\theta^\sharp$", r"$u\to u_\theta^\sharp$",
     "(4.4.3): 'nous noterons u→u^♯_θ, ou u→u^♯ l'isomorphisme réciproque' (first arrow)"),
    (r"$u\mapsto u^\sharp$", r"$u\to u^\sharp$",
     "(4.4.3): 'nous noterons u→u^♯_θ, ou u→u^♯ l'isomorphisme réciproque' (second arrow)"),
]:
    findings.append(F(42, where, "plain arrow → (checked on a crop)", old.replace("$", ""),
                      "convention", "high", fx(old, new), None, convention=3))

# ---------------- page 43 ----------------
for old, new, where in [
    (r"$v\mapsto v_\theta^\flat$", r"$v\to v_\theta^\flat$",
     "(4.4.3): 'ainsi que le caractère fonctoriel en F de l'isomorphisme v→v^♭_θ'"),
    (r"$u\mapsto u_\theta^\sharp$", r"$u\to u_\theta^\sharp$",
     "(4.4.3): 'Le caractère fonctoriel en G de u→u^♯_θ s'en déduit alors formellement'"),
    (r"$s_x\mapsto s_x\otimes1$", r"$s_x\to s_x\otimes1$",
     "(4.4.3), last paragraph: 'et l'homomorphisme canonique s_x→s_x⊗1 de G_ψ(x) dans (Ψ*(G))_x'"),
    (r"$v\mapsto\Psi^*(v)$", r"$v\to\Psi^*(v)$",
     "(4.4.6): 'l'application v→Ψ*(v) est un homomorphisme'"),
]:
    findings.append(F(43, where, "plain arrow →", old.replace("$", ""),
                      "convention", "high", fx(old, new), None, convention=3))

# ---------------- page 44 ----------------
findings.append(F(
    44,
    "(5.1.1): 'on sait que u→(u∘h_i) est un isomorphisme de Hom_O_X(O_X^(I), F) sur le produit'",
    "plain arrow →", r"u\mapsto(u\circ h_i)",
    "convention", "high",
    fx(r"$u\mapsto(u\circ h_i)$", r"$u\to(u\circ h_i)$"),
    None, convention=3))

findings.append(F(
    44,
    "(4.4.8): 'Soit H un C-Module, u' un homomorphisme de H dans G ; le composé v'' = v∘v' est par définition "
    "l'homomorphisme de H dans F défini par H →(v') Ψ'_*(G) →(Ψ'_*(v)) Ψ'_*(Ψ_*(F))'",
    "u' (italic u with a prime; checked on a crop)",
    "$u'$ (printed reading kept)",
    "misprint_in_print", "high", None,
    "The homomorphism introduced here is the v' of v'' = v∘v', of the arrow labelled v' and of Ψ*(v'^♯) "
    "in the next display; u' occurs nowhere else in (4.4.8). Not in the authors' errata lists (EGA II, III, IV). "
    "The TeX keeps the printed reading.",
    corrected=r"$v'$ un homomorphisme de $\mathcal{H}$ dans $\mathcal{G}$"))

# ---------------- page 45 ----------------
findings.append(F(
    45,
    "(5.1.1), end: 'engendré par la famille de toutes ces sections (ou par une sous-famille), autrement dit, "
    "s'il existe un homomorphisme surjectif'",
    "comma after '(ou par une sous-famille)' (checked on a crop)",
    "(ou par une sous-famille)~; (semicolon)",
    "punctuation", "high",
    fx(r"par une sous-famille)~; autrement dit", r"par une sous-famille), autrement dit"),
    None))

findings.append(F(
    45,
    "(5.1.3): 'de la forme O_X^(I)|V→O_X^(J)|V, où I et J sont des ensembles d'indices arbitraires'",
    "sont (checked on a crop)",
    "soient",
    "word", "high",
    fx(r"où $I$ et $J$ soient des", r"où $I$ et $J$ sont des"),
    None))

findings.append(F(
    45,
    "(5.1.3), last sentence: 'On dit qu'une O_X-Algèbre A est quasi-cohérente si elle l'est en tant que O_X-Module'",
    "'Algèbre' in italics, like 'quasi-cohérente' (checked on a crop)",
    "$\\mathcal{O}_X$-Algèbre (upright)",
    "italics", "high",
    fx(r"qu'une $\mathcal{O}_X$-Algèbre", r"qu'une $\mathcal{O}_X$-\emph{Algèbre}"),
    None))

findings.append(F(
    45,
    "(5.1.3), lines 16-17 of p. 45: 'il y a un voisinage ouvert U de x tel que F|V soit isomorphe au conoyau d'un "
    "homomorphisme de la forme O_X^(I)|V→O_X^(J)|V'",
    "voisinage ouvert U de x … F|V … O_X^(I)|V→O_X^(J)|V (checked on a crop)",
    "voisinage ouvert $U$ de $x$ tel que $\\mathcal{F}|V$ … "
    "$\\mathcal{O}_X^{(I)}|V\\to\\mathcal{O}_X^{(J)}|V$ (printed reading kept)",
    "misprint_in_print", "high", None,
    "Authors' errata (EGA III, A) Erreurs typographiques; ega3/ega3-7-fr.tex): '(0_I, 5.1.3) Ligne 16 de la p. 45, "
    "remplacer F|V par F|U.' The errata names only the F|V of line 16; the two |V of line 17 need the same change "
    "for the sentence to be consistent (V is never introduced). The TeX keeps the printed reading.",
    corrected=r"un voisinage ouvert $U$ de $x$ tel que $\mathcal{F}|U$ soit isomorphe au \emph{conoyau} d'un "
              r"homomorphisme de la forme $\mathcal{O}_X^{(I)}|U\to\mathcal{O}_X^{(J)}|U$"))

findings.append(F(
    45,
    "(5.1.3), line 18 of p. 45: 'et que toute somme directe de O_X-Modules quasi-cohérents est un O_X-Module "
    "quasi-cohérent'",
    "toute somme directe",
    "toute somme directe (printed reading kept)",
    "misprint_in_print", "high", None,
    "Authors' errata (EGA III, Err_III 1; ega3/ega3-7-fr.tex): 'Dans (0_I, 5.1.3), ligne 18 de la p. 45, remplacer "
    "« somme directe » par « somme directe finie ».' An authors' correction rather than a typesetting slip. "
    "The TeX keeps the printed reading.",
    corrected=r"et que toute somme directe finie de $\mathcal{O}_X$-Modules quasi-cohérents est un "
              r"$\mathcal{O}_X$-Module quasi-cohérent"))

# ---------------- verify and write ----------------
SRC = sys.argv[2] if len(sys.argv) > 2 else None


def page_text(p):
    with open(os.path.join(RUN, 'page_%03d.tex' % p), encoding='utf-8', newline='') as fh:
        return fh.read().replace('\r\n', '\n')


def src_segment(p):
    t = open(SRC, encoding='utf-8', newline='').read()
    a = t.find('\\oldpage[0\\textsubscript{I}]{%d}' % p)
    b = t.find('\\oldpage[0\\textsubscript{I}]{%d}' % (p + 1))
    return t[a:b]


ok = True
for f in findings:
    fixd = f["fix"]
    if fixd is None:
        continue
    c = page_text(f["page"]).count(fixd["old"])
    if c != 1:
        ok = False
        print('NOT UNIQUE/MISSING in page file', f["page"], c, repr(fixd["old"]))
    if fixd["old"] == fixd["new"]:
        ok = False
        print('NO-OP', f["page"], repr(fixd["old"]))
    if SRC:
        cs = src_segment(f["page"]).count(fixd["old"])
        tag = 'ALREADY APPLIED' in (f["note"] or '')
        if cs != 1:
            print('   current source segment count', cs, '(expected: already applied)' if tag else '(UNEXPECTED)',
                  f["page"], repr(fixd["old"][:60]))

# overlapping olds on the same page would break sequential application
by_page = {}
for f in findings:
    if f["fix"]:
        by_page.setdefault(f["page"], []).append(f["fix"]["old"])
for p, olds in by_page.items():
    text = page_text(p)
    spans = sorted((text.find(o), text.find(o) + len(o)) for o in olds)
    for (a1, b1), (a2, b2) in zip(spans, spans[1:]):
        if a2 < b1:
            ok = False
            print('OVERLAP on page', p, (a1, b1), (a2, b2))

with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write('\n')

counts = {}
for f in findings:
    k = 'convention' if f['kind'] == 'convention' else ('misprint' if f['kind'] == 'misprint_in_print' else 'normal')
    counts.setdefault(f['page'], {'normal': 0, 'convention': 0, 'misprint': 0})[k] += 1
print('ok' if ok else 'PROBLEMS', len(findings), 'findings')
for p in sorted(counts):
    print(p, counts[p])
