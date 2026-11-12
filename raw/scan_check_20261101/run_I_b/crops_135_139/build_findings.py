"""Build findings_135_139.json for the EGA I scan check (pages 135-139) and validate every fix.

Each fix "old" must occur exactly once in page_NNN.tex and in the page segment of the release source that
apply_fixes.py edits; the fixes of a page are also applied in sequence to check they do not interfere.
Nothing is written to any .tex file."""
import json
import pathlib
import re
import sys

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_I_b")
OUT = RUN / "findings_135_139.json"
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\BASE\native\ega1\ega1-5-fr.tex")
NL = "\n"

BK = r"\boldsymbol{k}"


def F(page, where, scan, tex, kind, convention, confidence, old, new, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=convention,
             confidence=confidence, fix=(None if old is None else dict(old=old, new=new)))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


findings = [
    # ---------------- page 135 ----------------
    F(135, "Corollaire (5.3.17), statement: 'les homomorphismes k(x)→k(y)'",
      "bold italic k: 𝒌(x)→𝒌(y)", r"$k(x)\to k(y)$", "convention", 1, "high",
      r"les homomorphismes $k(x)\to k(y)$",
      r"les homomorphismes $" + BK + r"(x)\to" + BK + r"(y)$", "Two k's."),
    F(135, "proof of (5.3.17), first sentence: 'Les deux homomorphismes k(x)→k(y)'",
      "bold italic k: 𝒌(x)→𝒌(y)", r"$k(x)\to k(y)$", "convention", 1, "high",
      r"deux homomorphismes $k(x)\to k(y)$",
      r"deux homomorphismes $" + BK + r"(x)\to" + BK + r"(y)$", "Two k's."),
    F(135, "proof of (5.3.17): 'g_i : Spec(k(y))→Spec(k(x))'",
      "bold italic k: Spec(𝒌(y))→Spec(𝒌(x))", r"$g_i:\operatorname{Spec}(k(y))\to\operatorname{Spec}(k(x))$",
      "convention", 1, "high",
      r"$g_i:\operatorname{Spec}(k(y))\to\operatorname{Spec}(k(x))$",
      r"$g_i:\operatorname{Spec}(" + BK + r"(y))\to\operatorname{Spec}(" + BK + r"(x))$", "Two k's."),
    F(135, "proof of (5.3.17), first diagram (top row Spec(k(y)) → Spec(k(x)))",
      "bold italic k in both top-row entries", r"\operatorname{Spec}(k(y)) ... \operatorname{Spec}(k(x))",
      "convention", 1, "high",
      r"\operatorname{Spec}(k(y))\ar[r]^{g_i}\ar[d] &" + NL + r"    \operatorname{Spec}(k(x))\ar[d]",
      r"\operatorname{Spec}(" + BK + r"(y))\ar[r]^{g_i}\ar[d] &" + NL + r"    \operatorname{Spec}(" + BK + r"(x))\ar[d]",
      "Two k's; the old string spans two lines of the xymatrix."),
    F(135, "proof of (5.3.17), second diagram (top row Spec(k(y)) → Spec(k(x))×_S Spec(k(x)))",
      "bold italic k in all three top-row k's", r"\operatorname{Spec}(k(y)) ... \operatorname{Spec}(k(x))\times_S\operatorname{Spec}(k(x))",
      "convention", 1, "high",
      r"\operatorname{Spec}(k(y))\ar[rr]^{(g_1,g_2)_S}\ar[d] & &" + NL
      + r"    \operatorname{Spec}(k(x))\times_S\operatorname{Spec}(k(x))\ar[d]",
      r"\operatorname{Spec}(" + BK + r"(y))\ar[rr]^{(g_1,g_2)_S}\ar[d] & &" + NL
      + r"    \operatorname{Spec}(" + BK + r"(x))\times_S\operatorname{Spec}(" + BK + r"(x))\ar[d]",
      "Three k's; the old string spans two lines of the xymatrix."),
    F(135, "proof of (5.3.17): 'l'unique point de Spec(k(y))'",
      "bold italic k: Spec(𝒌(y))", r"$\operatorname{Spec}(k(y))$", "convention", 1, "high",
      r"point de $\operatorname{Spec}(k(y))$",
      r"point de $\operatorname{Spec}(" + BK + r"(y))$", ""),
    F(135, "proof of (5.3.17): 'la diagonale de Spec(k(x))×_S Spec(k(x))'",
      "bold italic k: Spec(𝒌(x))×_S Spec(𝒌(x))", r"$\operatorname{Spec}(k(x))\times_S\operatorname{Spec}(k(x))$",
      "convention", 1, "high",
      r"$\operatorname{Spec}(k(x))\times_S\operatorname{Spec}(k(x))$",
      r"$\operatorname{Spec}(" + BK + r"(x))\times_S\operatorname{Spec}(" + BK + r"(x))$", "Two k's."),
    F(135, "Définition (5.4.1): 'est séparé si le morphisme diagonal'",
      "'séparé' italic like the rest of the definition (no change of face)", r"est \emph{séparé} si le",
      "convention", 6, "high", r"est \emph{séparé} si le", r"est séparé si le",
      "Inside the italic definition \\emph sets the word upright; the print shows no emphasis here (checked on a crop)."),
    F(135, "Définition (5.4.1): 'est une immersion fermée ;'",
      "'immersion' italic, only 'fermée' set in roman (emphasis on fermée)", r"est une \emph{immersion fermée}~;",
      "convention", 6, "high", r"\emph{immersion fermée}", r"immersion \emph{fermée}",
      "The TeX sets both words upright; the print emphasizes only 'fermée' (the diagonal is always an immersion by "
      "(5.3.9); the definition stresses 'closed'). Checked on a crop."),
    F(135, "Définition (5.4.1): 'un préschéma séparé au-dessus de Y'",
      "italic, no change of face", r"\emph{préschéma séparé au-dessus de $Y$}",
      "convention", 6, "high", r"\emph{préschéma séparé au-dessus de $Y$}", r"préschéma séparé au-dessus de $Y$",
      "Checked on a crop."),
    F(135, "Définition (5.4.1): 'ou un Y-schéma'",
      "italic, no change of face", r"\emph{$Y$-schéma}",
      "convention", 6, "high", r"\emph{$Y$-schéma}", r"$Y$-schéma", "Checked on a crop."),
    F(135, "Définition (5.4.1): 'on dit aussi alors que X est un schéma'",
      "'schéma' italic, no change of face", r"est un \emph{schéma}",
      "convention", 6, "high", r"est un \emph{schéma}", r"est un schéma", "Checked on a crop."),
    F(135, "Définition (5.4.1), end: '(cf. (5.5.7))'",
      "'(cf. (5.5.7))' set in roman inside the italic definition",
      r"(cf. (\hyperref[I.5.5.7-fr]{5.5.7}))", "convention", 6, "high",
      r"(cf. (\hyperref[I.5.5.7-fr]{5.5.7}))", r"\textup{(cf. (\hyperref[I.5.5.7-fr]{5.5.7}))}",
      "'cf.' and the reference are upright in the print; italic in the TeX environment."),
    F(135, "Proposition (5.4.2), statement: 'X×_S Y→X×_T Y (5.3.10) est fermée'",
      "reference (5.3.10) upright inside the italic statement", r"(\hyperref[I.5.3.10-fr]{5.3.10})",
      "convention", 6, "high",
      r"(\hyperref[I.5.3.10-fr]{5.3.10})", r"\textup{(\hyperref[I.5.3.10-fr]{5.3.10})}", ""),
    F(135, "Corollaire (5.4.3), statement: 'Γ_f : X→X×_S Y (5.3.11)'",
      "reference (5.3.11) upright inside the italic statement", r"(\hyperref[I.5.3.11-fr]{5.3.11})",
      "convention", 6, "high",
      r"Y$ (\hyperref[I.5.3.11-fr]{5.3.11})", r"Y$ \textup{(\hyperref[I.5.3.11-fr]{5.3.11})}", ""),
    # ---------------- page 136 ----------------
    F(136, "Corollaire (5.4.6), statement: 'toute S-section de X (2.5.5)'",
      "reference (2.5.5) upright inside the italic statement", r"(\hyperref[I.2.5.5-fr]{2.5.5})",
      "convention", 6, "high",
      r"(\hyperref[I.2.5.5-fr]{2.5.5})", r"\textup{(\hyperref[I.2.5.5-fr]{2.5.5})}", ""),
    F(136, "proof of (5.4.7): 'les homomorphismes k(x)→k(s)'",
      "bold italic k: 𝒌(x)→𝒌(s)", r"$k(x)\to k(s)$", "convention", 1, "high",
      r"$k(x)\to k(s)$", r"$" + BK + r"(x)\to" + BK + r"(s)$", "Two k's."),
    F(136, "Remarque (5.4.8): the whole body ('Si l'on suppose réciproquement ... au-dessus de S.')",
      "body set in roman (upright), like the proofs", r"\begin{remark}[5.4.8] ... (remark environment is \itshape)",
      "font", None, "high",
      r"Si l'on suppose réciproquement", r"\normalfont Si l'on suppose réciproquement",
      "The remark environment makes the body italic (GLOBAL_ISSUES.md item 2); the print has it in roman. The same "
      "file already starts Remarque (5.5.12) with \\normalfont; this local fix does the same and stays harmless if the "
      "environment is changed globally. (Layout only, not reported separately: the print sets "
      "Y→Y×_Z Y→Y in the text line, the TeX as a display.)"),
    F(136, "Remarque (5.4.8): 'si on suppose que la conclusion de (5.4.5) s'applique aux deux morphismes "
      "Y →Δ_Y Y×_Z Y →p_1 Y'",
      "(5.4.5)", r"(\hyperref[I.5.4.5-fr]{5.4.5}) s'applique aux deux morphismes",
      "misprint_in_print", None, "high", None, None,
      "The TeX keeps the printed reading. The two morphisms Δ_Y: Y→Y×_Z Y and p_1: Y×_Z Y→Y are the composable pair "
      "f, g of Corollaire (5.4.4) (p_1∘Δ_Y = 1_Y is a closed immersion; conclusion: Δ_Y is a closed immersion, "
      "so Y is separated over Z, with the letters of (5.4.4)); (5.4.5) is about (j, g)_S for two morphisms with the "
      "same source, which does not fit. The corrected edition (r20 current) already reads 5.4.4 here and its "
      "mathematical notes (base1_notes.tex, 'repères des critères locaux et des compositions') record "
      "'celui de 5.4.8 est 5.4.4'.",
      corrected=r"(\hyperref[I.5.4.4-fr]{5.4.4})"),
    F(136, "Proposition (5.5.1) (vi): 'il faut et il suffit que f_red (5.1.5) le soit'",
      "reference (5.1.5) upright inside the italic statement", r"(\hyperref[I.5.1.5-fr]{5.1.5})",
      "convention", 6, "high",
      r"(\hyperref[I.5.1.5-fr]{5.1.5})", r"\textup{(\hyperref[I.5.1.5-fr]{5.1.5})}", ""),
    F(136, "proof of (5.5.1) (ii), last line of the page: 'donc Δ_X|Z est une immersion fermée par (4.2.4), ce qui'",
      "(4.2.4)", r"(\hyperref[I.4.2.4-fr]{4.2.4}), ce qui",
      "misprint_in_print", None, "high", None, None,
      "The TeX keeps the printed reading. Δ_X|Z = j∘Δ_X|Y is a composite of two closed immersions, which is "
      "Proposition (4.2.5); (4.2.4) is the local criterion on the target. The authors' own errata make the same "
      "correction elsewhere ('(I, 5.3.13) Ligne 20 de la p. 134, remplacer (4.2.4) par (4.2.5)', also (I, 4.5.5) "
      "p. 127; EGA III, Errata et Addenda), but do not list this line; the corrected edition (r20 current) still "
      "has 4.2.4 here.",
      corrected=r"(\hyperref[I.4.2.5-fr]{4.2.5})"),
    # ---------------- page 137 ----------------
    F(137, "Proposition (5.5.4), statement: 'réunion d'une famille finie de parties fermées'",
      "'finie' set in roman inside the italic statement (emphasis)", r"d'une famille finie de parties fermées",
      "italics", None, "high", r"famille finie de", r"famille \emph{finie} de",
      "Emphasized word; the TeX has no \\emph, so the emphasis is lost (checked on a crop)."),
    F(137, "Proposition (5.5.4), statement: 'pour espace sous-jacent (5.2.1)'",
      "reference (5.2.1) upright inside the italic statement", r"(\hyperref[I.5.2.1-fr]{5.2.1})",
      "convention", 6, "high",
      r"(\hyperref[I.5.2.1-fr]{5.2.1})", r"\textup{(\hyperref[I.5.2.1-fr]{5.2.1})}", ""),
    F(137, "Proposition (5.5.4), statement: 'X_k →f_k Y_k→Y (5.2.2)'",
      "reference (5.2.2) upright inside the italic statement", r"(\hyperref[I.5.2.2-fr]{5.2.2})",
      "convention", 6, "high",
      r"(\hyperref[I.5.2.2-fr]{5.2.2})", r"\textup{(\hyperref[I.5.2.2-fr]{5.2.2})}", ""),
    F(137, "paragraph after the proof of (5.5.4): 'composantes irréductibles de Y (0, 2.1.5)'",
      "bold 0: (𝟎, 2.1.5)", r"(\hyperref[0.2.1.5-fr]{0, 2.1.5})", "convention", 2, "high",
      r"{0, 2.1.5}", r"{\textbf{0}, 2.1.5}", ""),
    F(137, "end of the paragraph after (5.5.4): 'au cas des préschémas intègres (2.1.7)'",
      "(2.1.7)", r"\emph{intègres} (\hyperref[I.2.1.7-fr]{2.1.7})",
      "misprint_in_print", None, "high", None, None,
      "The TeX keeps the printed reading. 'Préschéma intègre' is defined in (2.1.8); (2.1.7) says that an open part "
      "of a préschéma induces a préschéma. The authors' errata correct the same reference in (I, 5.1.4) ('Ligne 14 "
      "du bas de la p. 128, remplacer (2.1.7) par (2.1.8)'; EGA III, Errata et Addenda) but do not list this line; "
      "the corrected edition (r20 current) still has 2.1.7 here.",
      corrected=r"(\hyperref[I.2.1.8-fr]{2.1.8})"),
    # ---------------- page 138 ----------------
    F(138, "proof of (5.5.5): 'compte tenu de (4.2.4, b))'",
      "item letter in italics: (4.2.4, b)) with 'b)' italic", r"(\hyperref[I.4.2.4-fr]{4.2.4, b)})",
      "italics", None, "high", r"{4.2.4, b)}", r"{4.2.4, \emph{b)}}",
      "The b and its parenthesis are italic, the outer closing parenthesis upright (checked on a crop)."),
    F(138, "proof of (5.5.5): 'Or si l'on pose Y_λμ=Y_λ∩Y_μ'",
      "Or si l'on pose (no comma)", r"Or, si l'on pose", "punctuation", None, "high",
      "Or," + NL + "si l'on pose", "Or" + NL + "si l'on pose",
      "The TeX adds a comma after 'Or' (checked on a crop)."),
    F(138, "remark after the proof of (5.5.5): 'La prop. (5.5.4) permet, en prenant un recouvrement de Y par des ouverts "
      "affines, ...'",
      "(5.5.4)", r"La prop. (\hyperref[I.5.5.4-fr]{5.5.4}) permet",
      "misprint_in_print", None, "high", None, None,
      "The TeX keeps the printed reading. Reducing to affine targets by an open affine covering of Y is "
      "Proposition (5.5.5) (open covering (Y_λ) of Y); (5.5.4) is about finite coverings by closed parts. Wrong "
      "cross-reference in the print; the corrected edition (current) still has 5.5.4.",
      corrected=r"(\hyperref[I.5.5.5-fr]{5.5.5})"),
    F(138, "Proposition (5.5.6), statement: 'Soient Y un schéma affine'",
      "'affine' set in roman inside the italic statement (emphasis); 'schéma' italic",
      r"Soient $Y$ un schéma affine,", "italics", None, "high",
      r"un schéma affine, $X$", r"un schéma \emph{affine}, $X$",
      "Emphasized word missing in the TeX (checked on a crop)."),
    F(138, "Corollaire (5.5.7): '(et est par suite un schéma, ce qui justifie la terminologie de (5.4.1))'",
      "the parenthesis is set in roman inside the italic statement, with 'schéma' in italics",
      r"(et est par suite un schéma, ce qui justifie la terminologie de (\hyperref[I.5.4.1-fr]{5.4.1}))",
      "convention", 6, "high",
      r"(et est par suite un schéma, ce qui justifie la" + NL + r"terminologie de (\hyperref[I.5.4.1-fr]{5.4.1}))",
      r"\textup{(et est par suite un \emph{schéma}, ce qui justifie la" + NL
      + r"terminologie de (\hyperref[I.5.4.1-fr]{5.4.1}))}",
      "Inside the roman parenthesis 'schéma' is emphasized (italic), so the fix adds \\emph{schéma} (checked on a crop)."),
    F(138, "Corollaire (5.5.8): '(autrement dit, que X soit un schéma)'",
      "the parenthesis is set in roman inside the italic statement, with 'schéma' in italics",
      r"(autrement dit, que $X$ soit un schéma)", "convention", 6, "high",
      r"(autrement dit, que $X$ soit un schéma)", r"\textup{(autrement dit, que $X$ soit un \emph{schéma})}",
      "Inside the roman parenthesis 'schéma' is emphasized (italic), so the fix adds \\emph{schéma} (checked on a crop)."),
    F(138, "proof of (5.5.9): 'La nécessité de la condition résulte de (5.5.4) et (5.5.1, (ii))'",
      "(5.5.4)", r"résulte de (\hyperref[I.5.5.4-fr]{5.5.4}) et (\hyperref[I.5.5.1-fr]{5.5.1, (ii)})",
      "misprint_in_print", None, "high", None, None,
      "The TeX keeps the printed reading. Necessity needs that f^{-1}(U)→U is separated for an open U of Y, which is "
      "Proposition (5.5.5) (restriction over an open covering of the target); (5.5.4) (finite closed coverings) does "
      "not apply. Same wrong cross-reference as in the remark after (5.5.5).",
      corrected=r"(\hyperref[I.5.5.5-fr]{5.5.5})"),
    F(138, "proof of (5.5.9): 'la suffisance résulte de (5.5.4) et (5.5.8)'",
      "(5.5.4)", r"(\hyperref[I.5.5.4-fr]{5.5.4}) et (\hyperref[I.5.5.8-fr]{5.5.8})",
      "misprint_in_print", None, "high", None, None,
      "The TeX keeps the printed reading. Sufficiency: by (5.5.8) each f^{-1}(U)→U with U affine is separated, and "
      "an open affine covering of Y then gives f separated by Proposition (5.5.5), not (5.5.4).",
      corrected=r"(\hyperref[I.5.5.5-fr]{5.5.5})"),
    F(138, "Proposition (5.5.10), statement: 'Soient Y un schéma, f : X→Y un morphisme'",
      "'schéma' set in roman inside the italic statement (emphasis)", r"Soient $Y$ un schéma,",
      "italics", None, "high", r"Soient $Y$ un schéma,", r"Soient $Y$ un \emph{schéma},",
      "Emphasized word missing in the TeX (checked on a crop)."),
    # ---------------- page 139 ----------------
    F(139, "Remarque (5.5.12), first line: 'Étant donnée une propriété P de morphismes de préschémas'",
      "P in bold italic (roman text)", r"\textbf{P}", "font", None, "high",
      r"\textbf{P} de morphismes", r"\textbf{\textit{P}} de morphismes",
      "The TeX gives bold upright P (checked on a crop)."),
    F(139, "Remarque (5.5.12), item (i): 'Toute immersion fermée possède la propriété P.'",
      "P in bold upright inside the italic item", r"\emph{... \textbf{P}.}", "font", None, "high",
      r"fermée possède la propriété \textbf{P}.}", r"fermée possède la propriété \textbf{\textup{P}}.}",
      "Inside \\emph, \\textbf{P} comes out bold italic; the print has bold upright P in the italic items "
      "(checked on a crop)."),
    F(139, "Remarque (5.5.12), item (ii): 'possédant la propriété P possède la propriété P.'",
      "both P bold upright inside the italic item", r"\textbf{P} possède la propriété \textbf{P}.}", "font", None,
      "high", r"\textbf{P} possède la propriété \textbf{P}.}",
      r"\textbf{\textup{P}} possède la propriété \textbf{\textup{P}}.}",
      "Same as item (i): the TeX renders bold italic P."),
    F(139, "Remarque (5.5.12), item (iii): 'possédant la propriété P, f×_S g possède la propriété P.'",
      "both P bold upright inside the italic item", r"\textbf{P}, $f\times_S g$ possède la propriété \textbf{P}.}",
      "font", None, "high",
      r"\textbf{P}, $f\times_S g$ possède la propriété" + NL + r"    \textbf{P}.}",
      r"\textbf{\textup{P}}, $f\times_S g$ possède la propriété" + NL + r"    \textbf{\textup{P}}.}",
      "Same as item (i)."),
]

# ---- validation ----
marker = re.compile(r"\\oldpage\[I\]\{(\d+)\}")
src_text = SRC.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(src_text)]
segs = {}
for i, (n, s) in enumerate(cuts):
    segs[n] = src_text[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(src_text)]

ok = True
for page in range(135, 140):
    page_tex = (RUN / f"page_{page:03d}.tex").read_text(encoding="utf-8")
    seg = segs.get(page)
    if seg is None:
        print("no release segment for page", page); ok = False; continue
    sim_page, sim_seg = page_tex, seg
    for x in findings:
        if x["page"] != page or not x["fix"]:
            continue
        old, new = x["fix"]["old"], x["fix"]["new"]
        c1, c2 = page_tex.count(old), seg.count(old)
        s1, s2 = sim_page.count(old), sim_seg.count(old)
        if (c1, c2, s1, s2) != (1, 1, 1, 1):
            ok = False
            print("PROBLEM", page, x["where"], (c1, c2, s1, s2))
        sim_page, sim_seg = sim_page.replace(old, new), sim_seg.replace(old, new)
    norm = lambda s: re.sub(r"\s+", " ", s)
    for x in findings:
        if x["page"] == page and x["kind"] == "misprint_in_print":
            if norm(x["tex"]) not in norm(seg) or norm(x["tex"]) not in norm(page_tex):
                ok = False
                print("PROBLEM misprint tex not found", page, x["where"])

if not ok:
    sys.exit("validation failed; nothing written")
json.dump(findings, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in findings:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for page in range(135, 140):
    print(page, "normal", cnt[(page, "normal")], "convention", cnt[(page, "convention")],
          "misprint", cnt[(page, "misprint")])
print("written", OUT, len(findings))
