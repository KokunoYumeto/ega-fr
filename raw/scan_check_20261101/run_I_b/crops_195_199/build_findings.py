"""Build findings_195_199.json for EGA I pp. 195-199 and check every fix against the page TeX.

Each "old" must occur exactly once in its page when the fixes of that page are applied in list order
(the rule of apply_fixes.py). Writes the JSON only if all checks pass."""
import json
import pathlib
import re
import sys
from collections import Counter

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_I_b")
OUT = RUN / "findings_195_199.json"
NL = "\n"


def F(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


def C2(page, where, ref):
    old = "{0, " + ref + "}"
    return F(page, where, "(0, " + ref + ") with the chapter number 0 in bold", old, "convention", 2, "high",
             old, r"{\textbf{0}, " + ref + "}")


findings = [
    # ---------------- page 195 ----------------
    F(195, "Définition (10.8.4), end (first lines of p. 195): 'on dit que ses sections au-dessus de X′ sont les sections formelles de 𝓕 le long de X′.'",
      "'sections formelles de 𝓕 le long de X′' in italics like the rest of the definition (no change of face)",
      r"\emph{sections formelles de $\mathscr{F}$ le long de $X'$}", "convention", 6, "high",
      r"\emph{sections formelles de $\mathscr{F}$ le long de $X'$}",
      r"sections formelles de $\mathscr{F}$ le long de $X'$",
      r"\emph inside the italic definition environment sets the words upright; drop the \emph. Checked on a crop."),
    C2(195, "after (10.8.4): '(𝒪_X)_{/X′}-Module topologique (0, 3.8.1 et 3.8.2)'", "3.8.1"),
    F(195, "after (10.8.4): 'et appelé le complété de l'homomorphisme u le long de X′.'",
      "only 'complété' in italics; 'de l'homomorphisme u le long de X′' roman",
      r"\emph{complété de l'homomorphisme $u$ le long de $X'$}", "italics", None, "high",
      r"\emph{complété de l'homomorphisme $u$ le long de $X'$}",
      r"\emph{complété} de l'homomorphisme $u$ le long de $X'$",
      "Checked on a crop: 'de l'homomorphisme' and 'le long de' are upright."),
    F(195, "Proposition (10.8.5): '𝒥=𝔍̃, où 𝔍 est un idéal de A'",
      "comma after 𝔍̃: '𝒥=𝔍̃, où'",
      r"$\mathscr{J}=\widetilde{\mathfrak{J}}$ où", "punctuation", None, "high",
      r"=\widetilde{\mathfrak{J}}$", r"=\widetilde{\mathfrak{J}}$,",
      "Checked on a crop."),
    C2(195, "proof of (10.8.5): 'On sait (0, 7.3.3) que le séparé complété'", "7.3.3"),
    C2(195, "proof of (10.8.5): 'Â/𝔍̂ⁿ=A/𝔍ⁿ (0, 7.2.6)'", "7.2.6"),
    F(195, "proof of (10.8.5): 'les idéaux premiers ouverts de Â sont les idéaux 𝔭̂=𝔭Â, où 𝔭 est un idéal premier de A contenant 𝔍'",
      "𝔭̂=𝔭𝔍̂: the factor after 𝔭 is a hatted Fraktur 𝔍 (the same glyph as 𝔍̂ in 'le séparé complété 𝔍̂ de 𝔍' two lines above), not Â",
      r"$\widehat{\mathfrak p}=\mathfrak p\widehat A$ (silently corrected)", "misprint_in_print", None, "high",
      r"\widehat{\mathfrak p}=\mathfrak p\widehat A", r"\widehat{\mathfrak p}=\mathfrak p\widehat{\mathfrak{J}}",
      "Checked on crops at 3x and against the other 𝔍̂ of the paragraph. The open primes of Â are the ideals 𝔭Â, 𝔭 a prime "
      "of A containing 𝔍. 𝔭𝔍̂ lies in 𝔍̂, whose inverse image in A is 𝔍 (Â/𝔍̂=A/𝔍), so it cannot satisfy the next clause "
      "𝔭̂∩A=𝔭 when 𝔭≠𝔍. The TeX silently corrects the print.",
      r"\widehat{\mathfrak p}=\mathfrak p\widehat A"),
    F(195, "Corollaire (10.8.6): 'ayant pour espace sous-jacent X′ (5.2.1).'",
      "(5.2.1) upright inside the italic statement",
      r"(\hyperref[I.5.2.1-fr]{5.2.1})", "convention", 6, "high",
      r"(\hyperref[I.5.2.1-fr]{5.2.1})", r"\textup{(\hyperref[I.5.2.1-fr]{5.2.1})}",
      "Reference printed upright inside the italic statement; italic in the TeX environment. Checked on a crop."),
    # ---------------- page 196 ----------------
    C2(196, "proof of (10.8.6): 'du nilradical de A/𝔍 (0, 7.1.3), donc Â/𝔗'", "7.1.3"),
    F(196, "(10.8.7): 'Nous désignerons par i (ou i_X) le morphisme (dit canonique)'",
      "'canonique' in italics",
      "(dit canonique)", "italics", None, "high",
      "(dit canonique)", r"(dit \emph{canonique})",
      "Checked on a crop; the env environment is roman."),
    F(196, "proof of (10.8.8, (i)), display after 'On a alors': 'Γ(U∩X′, 𝓕⊗_{𝒪_X}𝒪_X/𝒥ⁿ)=M⊗_A(A/𝔍ⁿ)'",
      "no parentheses around 𝒪_X/𝒥ⁿ on the left-hand side",
      r"\mathscr{F}\otimes_{\mathscr{O}_X}(\mathscr{O}_X/\mathscr{J}^n))", "formula", None, "high",
      r"\mathscr{F}\otimes_{\mathscr{O}_X}(\mathscr{O}_X/\mathscr{J}^n))",
      r"\mathscr{F}\otimes_{\mathscr{O}_X}\mathscr{O}_X/\mathscr{J}^n)",
      "Checked on a crop at 1.8x; the right-hand side M⊗_A(A/𝔍ⁿ) does have its parentheses."),
    F(196, "proof of (10.8.8, (i)): '𝓕′|U=M̃′'",
      "tilde over M only, prime after it (M̃′)",
      r"\widetilde{M'}", "convention", 8, "high",
      r"\widetilde{M'}", r"\widetilde{M}'",
      "Checked on a crop."),
    F(196, "proof of (10.8.8, (i)): '𝓕″|U=M̃″'",
      "tilde over M only, primes after it (M̃″)",
      r"\widetilde{M''}", "convention", 8, "high",
      r"\widetilde{M''}", r"\widetilde{M}''",
      "Checked on a crop."),
    C2(196, "proof of (10.8.8, (i)), last line of p. 196: 'sur la catégorie des A-modules de type fini (0, 7.3.3).'", "7.3.3"),
    F(196, "proof of (10.8.8, (i)), display 'Γ(U∩X′, 𝓕′_{/X′})=M̂′, Γ(U∩X′, 𝓕″_{/X′})=M̂″': first term",
      "hat over M only, prime after it (M̂′)",
      r"\widehat{M'}", "formula", None, "high",
      r"\widehat{M'}", r"\widehat{M}'",
      "Checked on a crop. Same meaning; the analogue of convention 8 for a hat and a prime."),
    F(196, "same display, second term Γ(U∩X′, 𝓕″_{/X′})=M̂″",
      "hat over M only, primes after it (M̂″)",
      r"\widehat{M''}", "formula", None, "high",
      r"\widehat{M''}", r"\widehat{M}''",
      "Checked on a crop. Same meaning; the analogue of convention 8 for a hat and a prime."),
    F(196, "same display, end: '…=M̂″' followed by 'notre assertion résulte alors'",
      "no punctuation after the display",
      r"=\widehat{M''}~;", "punctuation", None, "high",
      r"~;" + NL + r"    \]", NL + r"    \]",
      "Checked on a crop: nothing follows M̂″ in the display. The 'old' spans the line break before \\]."),
    # ---------------- page 197 ----------------
    C2(197, "proof of (10.8.8, (ii)): '𝒪_X^m→𝒪_X^n→𝓕→0 (0, 5.3.2)'", "5.3.2"),
    C2(197, "proof of (10.8.8, (ii)): 'sont exacts à droite (d'après (i) et (0, 4.3.1))'", "4.3.1"),
    C2(197, "proof of (10.8.8, (ii)): 'commutent aux sommes directes finies (0, 3.2.6 et 4.3.2)'", "3.2.6"),
    C2(197, "proof of (10.8.8, (ii)): 'i*(𝒪_X)=(𝒪_X)_{/X′}=𝒪_X̂ (0, 4.3.4)'", "4.3.4"),
    F(197, "proof of (10.8.8, (ii)): 'et γ♯ est un homomorphisme de 𝒪_X̂-Modules ; il suffit donc'",
      "'Modules' in italics",
      r"$\mathscr{O}_{\widehat X}$-Modules~;", "italics", None, "high",
      r"$\mathscr{O}_{\widehat X}$-Modules~;", r"$\mathscr{O}_{\widehat X}$-\emph{Modules}~;",
      "Checked on a crop at 2x: 'Modules' is clearly italic in the roman proof text (perhaps stressing that γ♯ is "
      "𝒪_X̂-linear, which is why checking the unit section suffices; it could also be a font slip of the print)."),
    C2(197, "after Corollaire (10.8.9): 'Cela résulte en effet de (0, 6.7.3)'", "6.7.3"),
    F(197, "Corollaire (10.8.10), display (10.8.10.1): subscript of the first ⊗",
      "⊗_{(𝒪_X)/X′}: inside the subscript '/X′' stands at the level of the parentheses; only the X of 𝒪_X is lowered",
      r"\otimes_{(\mathscr{O}_X)_{/X'}}", "misprint_in_print", None, "medium",
      r"\otimes_{(\mathscr{O}_X)_{/X'}}", r"\otimes_{(\mathscr{O}_X)/X'}",
      "Checked on a crop at 2x. The third-level index /X′ is not lowered (the kind of slip recorded as B_{gi} on p. 145); "
      "same in (10.8.10.2). The TeX silently corrects the print.",
      r"\otimes_{(\mathscr{O}_X)_{/X'}}"),
    F(197, "Corollaire (10.8.10), display (10.8.10.2): subscript of the second ℋom",
      "ℋom_{(𝒪_X)/X′}: inside the subscript '/X′' stands at the level of the parentheses; only the X of 𝒪_X is lowered",
      r"\mathscr{H}\!om_{(\mathscr{O}_X)_{/X'}}", "misprint_in_print", None, "medium",
      r"\mathscr{H}\!om_{(\mathscr{O}_X)_{/X'}}", r"\mathscr{H}\!om_{(\mathscr{O}_X)/X'}",
      "Checked on a crop at 2x. Same slip as in (10.8.10.1). The TeX silently corrects the print.",
      r"\mathscr{H}\!om_{(\mathscr{O}_X)_{/X'}}"),
    F(197, "proof of (10.8.10): 'Cela résulte de l'identification canonique de i*(𝓕) et de 𝓕_{/X′} ;'",
      "𝓕/_{X′}: the slash is full size on the line after 𝓕; only X′ is lowered as a subscript",
      r"$\mathscr{F}_{/X'}$~; l'existence (silently corrected)", "misprint_in_print", None, "high",
      r"$\mathscr{F}_{/X'}$~; l'existence", r"$\mathscr{F}/_{X'}$~; l'existence",
      "Checked on a crop at 2.5x against the ordinary 𝓕_{/X′} of the next paragraph, where the slash is small and lowered "
      "together with X′. The TeX silently corrects the print.",
      r"$\mathscr{F}_{/X'}$"),
    C2(197, "proof of (10.8.10): 'pour tous les morphismes d'espaces annelés (0, 4.3.3.1)'", "4.3.3.1"),
    C2(197, "proof of (10.8.10): 'pour tous les morphismes plats (0, 6.7.6)'", "6.7.6"),
    C2(197, "proof of (10.8.11): 'On sait (0, 7.3.7) que le noyau de cet homomorphisme'", "7.3.7"),
    C2(197, "proof of (10.8.12), last line of p. 197: 'de type fini (10.8.8, (ii)) et (0, 5.2.4),'", "5.2.4"),
    # ---------------- page 198 ----------------
    C2(198, "proof of (10.8.12), first line of p. 198: 'donc son support est fermé (0, 5.2.2)'", "5.2.2"),
    C2(198, "proof of (10.8.13): '((10.8.10.2) et (0, 4.4.6))'", "4.4.6"),
    F(198, "Corollaire (10.8.14): 'Pour que u_{/X′} soit un monomorphisme (resp. un épimorphisme), il faut'",
      "'(resp.' roman inside the italic statement",
      "(resp. un épimorphisme), il faut", "convention", 6, "high",
      "(resp. un épimorphisme), il faut", r"\textup{(resp.} un épimorphisme), il faut",
      "'resp.' roman in the print inside the italic statement; italic in the TeX environment. Checked on a crop."),
    F(198, "Corollaire (10.8.14): 'que u soit un monomorphisme (resp. un épimorphisme) dans un voisinage de X′'",
      "'(resp.' roman inside the italic statement",
      "(resp. un épimorphisme) dans", "convention", 6, "high",
      "(resp. un épimorphisme) dans", r"\textup{(resp.} un épimorphisme) dans",
      "'resp.' roman in the print inside the italic statement; italic in the TeX environment. Checked on a crop."),
    C2(198, "(10.9.1): 'f*(𝒦ⁿ)𝒪_X⊂𝒥ⁿ (0, 4.3.5) ; par suite (4.4.6)'", "4.3.5"),
    F(198, "(10.9.1), last lines of p. 198: 'f̂ est alors le morphisme qui correspond (10.2.2) à l'homomorphisme continu'",
      "(10.2.2) upright between the italic words",
      r"\emph{$\widehat f$ est alors le morphisme qui correspond (\hyperref[I.10.2.2-fr]{10.2.2}) à …}", "italics", None, "high",
      r"(\hyperref[I.10.2.2-fr]{10.2.2})", r"\textup{(\hyperref[I.10.2.2-fr]{10.2.2})}",
      "Checked on a crop: the reference is upright between italic words; the TeX's \\emph sets it italic."),
    # ---------------- page 199 ----------------
    F(199, "(10.9.1), first line of p. 199: 'faisceau d'idéaux 𝒥′=𝔍̃′'",
      "tilde over 𝔍 only, prime after it (𝔍̃′)",
      r"\widetilde{\mathfrak{J}'}", "convention", 8, "high",
      r"\widetilde{\mathfrak{J}'}", r"\widetilde{\mathfrak{J}}'",
      "Checked on a crop at 3x."),
    F(199, "(10.9.3): 'il résulte aussitôt de (10.9.1) que l'on a (g∘f)^=ĝ∘f̂.'",
      "(g∘f)^: the hat is written after the closing parenthesis, at superscript height",
      r"$\widehat{(g\circ f)}=\widehat g\circ\widehat f$", "formula", None, "high",
      r"$\widehat{(g\circ f)}=\widehat g\circ\widehat f$", r"$(g\circ f){\,\widehat{\,}\,}=\widehat g\circ\widehat f$",
      "Checked on a crop at 3x. The analogue of convention 5 for a hat; the replacement copies the definition of "
      "\\supertilde (preamble-base.tex) with a hat; a \\superhat macro would be the tidier form."),
    F(199, "proof of (10.9.4): 'Si h∈Γ(Y, 𝒪_X) est tel que D(h) soit un voisinage de x contenu dans V'",
      "h∈Γ(Y, 𝒪_X)",
      r"$h\in\Gamma(Y,\mathscr{O}_X)$ (printed reading kept)", "misprint_in_print", None, "high",
      None, None,
      "Checked on a crop. D(h) is a neighbourhood of x in the affine X contained in the open V of X, so h is a section of "
      "𝒪_X over X; Γ(Y, 𝒪_X) is meaningless here. The TeX keeps the printed reading.",
      r"h\in\Gamma(X,\mathscr{O}_X)"),
    F(199, "proof of (10.9.4): 'on conclut de ce qui précède et de (1.4.1, d)) que f et g coïncident dans D(h)'",
      "label d) in italics",
      r"(\hyperref[I.1.4.1-fr]{1.4.1, d)})", "italics", None, "high",
      "{1.4.1, d)}", r"{1.4.1, \emph{d)}}",
      "Labels a), b), c), ... are italic in the roman proof text of the print; the TeX sets this one roman. Checked on a crop."),
    F(199, "Proposition (10.9.5): 'Sous les hypothèses de (10.9.1), pour tout 𝒪_Y-Module cohérent 𝒢'",
      "(10.9.1) upright inside the italic statement",
      r"(\hyperref[I.10.9.1-fr]{10.9.1})", "convention", 6, "high",
      r"hypothèses de (\hyperref[I.10.9.1-fr]{10.9.1})", r"hypothèses de \textup{(\hyperref[I.10.9.1-fr]{10.9.1})}",
      "Reference printed upright inside the italic statement; italic in the TeX environment. Checked on a crop. "
      "The same reference in (10.9.3) is in roman text and needs no change."),
]

ok = True
ctrl = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
for x in findings:
    for v in (x["where"], x["scan"], x["tex"], x["note"] or "", x.get("corrected") or "",
              *(x["fix"].values() if x["fix"] else ())):
        if ctrl.search(v):
            ok = False
            print("control character in", x["page"], x["where"])
for p in sorted({x["page"] for x in findings}):
    t = (RUN / f"page_{p}.tex").read_text(encoding="utf-8")  # universal newlines: CRLF -> LF
    for x in findings:
        if x["page"] != p or not x["fix"]:
            continue
        o, n = x["fix"]["old"], x["fix"]["new"]
        c = t.count(o)
        if c != 1:
            ok = False
            print(f"p{p}: old occurs {c} times: {o!r}")
            continue
        t = t.replace(o, n)
if not ok:
    sys.exit("not written")
OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
cnt = Counter()
for x in findings:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for p in range(195, 200):
    print(p, {k: cnt[(p, k)] for k in ("normal", "convention", "misprint")})
print("written", OUT, len(findings))
