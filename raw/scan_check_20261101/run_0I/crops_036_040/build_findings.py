import json, pathlib
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
RUN = E / "run_0I"
OUT = RUN / "findings_036_040.json"
REL = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega1\ega0-1-fr.tex"
N = "\n"


def F(page, where, scan, tex, kind, fix, note=None, conv=None, conf="high", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf, fix=fix)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


def fx(old, new):
    return {"old": old, "new": new}


L = []
# ---------------- page 36 ----------------
L.append(F(36, "(4.1.1), 'et d'un ψ-morphisme θ : 𝒢→ℱ (3.5.1) de faisceaux d'anneaux'",
           "θ : 𝒢→ℱ (script G and script F)", r"$\theta:\mathcal{G}\to\mathcal{F}$",
           "misprint_in_print", None, conf="medium", corrected=r"\theta:\mathcal{B}\to\mathcal{A}",
           note="The TeX keeps the printed reading. The morphism is (X, 𝒜)→(Y, ℬ), so θ is a ψ-morphism ℬ→𝒜 "
                "(cf. (4.2.1): 'θ un homomorphisme ℬ→ψ_*(𝒜)'); 𝒢 and ℱ are the letters of (3.5.1), not defined here."))
L.append(F(36, "(4.1.2), '(j, ω♭) est un monomorphisme (M, 𝒜|M)→(X, 𝒜)'",
           "ω with the flat sign ♭ as superscript", r"$(j,\omega^b)$", "symbol",
           fx(r"(j,\omega^b)", r"(j,\omega^\flat)"),
           note="Letter b for the flat sign; same issue as GLOBAL_ISSUES item 14 (EGA I pp. 120-129)."))
L.append(F(36, "(4.1.3), 'sur la définition des 𝒜-Modules ou faisceaux algébriques'",
           "'𝒜-Modules' in italics", r"des $\mathcal{A}$-Modules ou", "italics",
           fx(r"des $\mathcal{A}$-Modules ou", r"des $\mathcal{A}$-\emph{Modules} ou")))
L.append(F(36, "(4.1.3), 'ou faisceaux algébriques sur un espace annelé (X, 𝒜)'",
           "'faisceaux algébriques' in italics", "faisceaux algébriques sur", "italics",
           fx("faisceaux algébriques sur", r"\emph{faisceaux algébriques} sur")))
L.append(F(36, "(4.1.3), 'seront qualifiés de faisceaux d'idéaux (à gauche, à droite ou bilatères)'",
           "'faisceaux d'idéaux' in italics", "faisceaux d'idéaux (à gauche", "italics",
           fx("faisceaux d'idéaux (à gauche", r"\emph{faisceaux d'idéaux} (à gauche")))
L.append(F(36, "(4.1.3), 'dans 𝒜 ou de 𝒜-Idéaux.'",
           "'𝒜-Idéaux' in italics", r"$\mathcal{A}$-Idéaux.", "italics",
           fx(r"$\mathcal{A}$-Idéaux.", r"$\mathcal{A}$-\emph{Idéaux}.")))
L.append(F(36, "(4.1.3), 'on remplace partout la structure de module par celle d'algèbre'",
           "'module' in italics", "structure de module par", "italics",
           fx("structure de" + N + "module par", "structure de" + N + r"\emph{module} par")))
L.append(F(36, "(4.1.3), 'par celle d'algèbre, on obtient'",
           "'algèbre' in italics (d' roman)", "celle d'algèbre,", "italics",
           fx("celle d'algèbre,", r"celle d'\emph{algèbre},")))
L.append(F(36, "(4.1.3), 'on obtient la définition d'une 𝒜-Algèbre sur X'",
           "'𝒜-Algèbre' in italics", r"$\mathcal{A}$-Algèbre sur $X$", "italics",
           fx(r"$\mathcal{A}$-Algèbre sur $X$", r"$\mathcal{A}$-\emph{Algèbre} sur $X$")))
# ---------------- page 37 ----------------
L.append(F(37, "(4.1.3), 'la sous-𝒜-Algèbre de 𝒞 engendrée par ℳ est la somme des images'",
           "'sous-𝒜-Algèbre de 𝒞 engendrée par ℳ' in italics ('la' roman)",
           r"la sous-$\mathcal{A}$-Algèbre de $\mathcal{C}$ engendrée par $\mathcal{M}$ (upright)", "italics",
           fx(r"la sous-$\mathcal{A}$-Algèbre de" + N + r"$\mathcal{C}$ engendrée par $\mathcal{M}$ est",
              r"la \emph{sous-$\mathcal{A}$-Algèbre de" + N + r"$\mathcal{C}$ engendrée par $\mathcal{M}$} est")))
L.append(F(37, "(4.1.3), 'le faisceau associé au préfaisceau U→ℬ(U) d'algèbres'",
           "plain arrow U→ℬ(U)", r"$U\mapsto\mathcal{B}(U)$", "convention",
           fx(r"$U\mapsto\mathcal{B}(U)$", r"$U\to\mathcal{B}(U)$"), conv=3))
L.append(F(37, "(4.1.4), 'est réduit en un point x de X si la fibre 𝒜_x'",
           "only 'réduit' in italics; 'en un point' roman", r"\emph{réduit en un point} $x$", "italics",
           fx(r"\emph{réduit en un point} $x$", r"\emph{réduit} en un point $x$")))
L.append(F(37, "(4.1.4), 'si sa fibre 𝒜_x est un anneau intègre et intégralement clos'",
           "'intègre et intégralement clos' in italics", "anneau intègre et intégralement clos (upright)", "italics",
           fx("anneau intègre et intégralement clos (resp.", r"anneau \emph{intègre et intégralement clos} (resp.")))
L.append(F(37, "(4.1.4), 'Un faisceau d'anneaux gradués 𝒜 est par définition'",
           "'anneaux gradués' in italics (d' roman)", r"faisceau d'anneaux \emph{gradués}", "italics",
           fx(r"faisceau d'anneaux \emph{gradués}", r"faisceau d'\emph{anneaux gradués}")))
L.append(F(37, "end of p. 37 / start of p. 38, (4.1.5): '(ou plus | généralement des 𝒞-Modules'",
           "one sentence: p. 38 begins 'généralement des 𝒞-Modules' flush left, no new paragraph",
           r"blank line before \oldpage[0\textsubscript{I}]{38}: new paragraph at 'généralement'", "other",
           fx("abéliens (ou plus" + N + N, "abéliens (ou plus" + N), conf="medium",
           note="Spurious paragraph break in mid-sentence; the blank line is the last line of the p. 37 segment."))
# ---------------- page 38 ----------------
L.append(F(38, "(4.1.5), 'on appelle dual de ℱ et on note ℱ̌'",
           "only 'dual' in italics; 'de ℱ' roman", r"\emph{dual de $\mathcal{F}$}", "italics",
           fx(r"\emph{dual de $\mathcal{F}$}", r"\emph{dual} de $\mathcal{F}$")))
L.append(F(38, "(4.1.5), 'ℱ un 𝒜-Module, U→∧^pΓ(U, ℱ) est un préfaisceau'",
           "plain arrow", r"$U\mapsto\bigwedge^p\Gamma(U,\mathcal{F})$", "convention",
           fx(r"$U\mapsto\bigwedge^p\Gamma(U,\mathcal{F})$ est un", r"$U\to\bigwedge^p\Gamma(U,\mathcal{F})$ est un"),
           conv=3))
L.append(F(38, "(4.1.5), 'l'application canonique du préfaisceau U→∧^pΓ(U, ℱ) dans le faisceau associé'",
           "plain arrow", r"$U\mapsto\bigwedge^p\Gamma(U,\mathcal{F})$", "convention",
           fx(r"préfaisceau $U\mapsto\bigwedge^p\Gamma(U,\mathcal{F})$ dans",
              r"préfaisceau $U\to\bigwedge^p\Gamma(U,\mathcal{F})$ dans"), conv=3))
L.append(F(38, "end of p. 38 / start of p. 39, (4.1.7): 'des X_λ | le long des V_λμ'",
           "one sentence: p. 39 begins 'le long des V_λμ ;' flush left, no new paragraph",
           r"blank line before \oldpage[0\textsubscript{I}]{39}: new paragraph at 'le long des'", "other",
           fx(r"des $X_\lambda$" + N + N, r"des $X_\lambda$" + N), conf="medium",
           note="Spurious paragraph break in mid-sentence; the blank line is the last line of the p. 38 segment."))
# ---------------- page 39 ----------------
L.append(F(39, "(4.2.1), '; ψ_*(A) est donc un faisceau d'anneaux sur Y'",
           "ψ_*(A) with a roman capital A", r"$\psi_*(\mathcal{A})$ (silently corrected)", "misprint_in_print",
           fx(r"$\psi_*(\mathcal{A})$ est donc un", r"$\psi_*(A)$ est donc un"),
           corrected=r"\psi_*(\mathcal{A})",
           note="The structure sheaf is 𝒜 (the next line prints ℬ→ψ_*(𝒜)); the TeX silently corrects the print. "
                "The fix restores the printed reading."))
L.append(F(39, "(4.2.1), 'une structure de ℬ-Module ; nous dirons'",
           "'ℬ-Module' in italics", r"structure de $\mathcal{B}$-Module~;", "italics",
           fx(r"structure de $\mathcal{B}$-Module~; nous", r"structure de $\mathcal{B}$-\emph{Module}~; nous")))
L.append(F(39, "(4.2.2.1), end of the display 'Ψ_*(ℳ)⊗_ℬΨ_*(𝒩) → Ψ_*(ℳ⊗_𝒜𝒩)'",
           "no period after the formula; the sentence continues on p. 40: 'qui ne sera en général ni injectif ni surjectif.'",
           r"\Psi_*(\mathcal{M}\otimes_{\mathcal{A}}\mathcal{N}).", "punctuation",
           fx(r"\mathcal{N})." + N + r"  \tag{4.2.2.1}", r"\mathcal{N})" + N + r"  \tag{4.2.2.1}")))
L.append(F(39, "end of p. 39 / start of p. 40: display (4.2.2.1) | 'qui ne sera en général ni injectif ni surjectif'",
           "p. 40 begins 'qui ne sera ...' flush left, continuing the sentence of (4.2.2.1)",
           r"blank line after \] before \oldpage[0\textsubscript{I}]{40}: new paragraph at 'qui'", "other",
           fx(r"\label{0.4.2.2.1-fr}" + N + r"\]" + N + N, r"\label{0.4.2.2.1-fr}" + N + r"\]" + N), conf="medium",
           note="Spurious paragraph break; the blank line is the last line of the p. 39 segment."))
# ---------------- page 40 ----------------
L.append(F(40, "(4.2.3), 'compatibles aux opérations de restriction définissent donc un homomorphisme'",
           "no comma after 'restriction'", "de restriction, définissent donc", "punctuation",
           fx("de restriction, définissent donc", "de restriction définissent donc")))
L.append(F(40, "(4.2.4), 'définit sur Ψ_*(𝒞) une structure de ℬ-Algèbre, comme il résulte de (4.2.2.2)'",
           "'ℬ-Algèbre' in italics", r"$\mathcal{B}$-Algèbre,", "italics",
           fx(r"$\mathcal{B}$-Algèbre,", r"$\mathcal{B}$-\emph{Algèbre},")))
L.append(F(40, "(4.3.1), 'Les hypothèses et notations étant celles de (4.2.1), soient 𝒢 un ℬ-Module' (TeX in page_041.tex)",
           "soient", r"soit $\mathcal{G}$ un", "word", None,
           note="Printed on p. 40; the TeX lies after the misplaced p. 41 marker (page_041.tex l. 8). "
                "The change soit -> soient is included in the p. 41 marker fix below (one edit), so this finding has no separate fix."))
L.append(F(40, "(4.3.1), 'Nous dirons que ce 𝒜-Module est l'image réci-|proque de 𝒢 par le morphisme Ψ' (TeX in page_041.tex)",
           "'l'image réci-' italic at the end of p. 40, 'l'' included; p. 41 continues 'proque de 𝒢 par le morphisme' in italics, then roman 'Ψ et nous le noterons'",
           r"l'image réciproque de $\mathcal{G}$ par le morphisme (upright)", "italics", None,
           note="The \\emph{l'image ... morphisme} is included in the p. 41 marker fix below (the new marker goes inside it), "
                "so this finding has no separate fix."))

# ---------------- marker for p. 41 (atomic edit; page 41 so that apply_fixes.py finds it) ----------------
t = REL.read_text(encoding="utf-8")
m41 = r"\oldpage[0\textsubscript{I}]{41}"
start = t.index(m41 + N + r"\subsection{Image réciproque")
endkey = r"est l'image réciproque de $\mathcal{G}$ par le morphisme" + N + r"$\Psi$"
end = t.index(endkey, start) + len(endkey)
old = t[start:end]
new = old[len(m41 + N):]
assert new.count(r"soit $\mathcal{G}$ un") == 1
new = new.replace(r"soit $\mathcal{G}$ un", r"soient $\mathcal{G}$ un")
new = new.replace(endkey, r"est \emph{l'image" + N + m41 + N + r"réciproque de $\mathcal{G}$ par le morphisme}" + N + r"$\Psi$")
L.append(F(41, "start of printed p. 41 / end of p. 40: heading '4.3. Image réciproque d'un ℬ-Module.' and (4.3.1) up to 'l'image réci-'",
           "p. 40 ends with the heading 4.3 and (4.3.1) '... Nous dirons que ce 𝒜-Module est l'image réci-'; "
           "p. 41 begins 'proque de 𝒢 par le morphisme Ψ et nous le noterons Ψ*(𝒢).'",
           r"\oldpage[0\textsubscript{I}]{41} stands before \subsection{Image réciproque d'un $\mathcal{B}$-Module} "
           "(page_041.tex l. 2), so the last 11 printed lines of p. 40 are attributed to p. 41", "marker",
           fx(old, new),
           note="One atomic edit (it must not be split: removing the old marker without inserting the new one would leave p. 41 "
                "without a marker). It moves the marker to the page break inside 'réci-|proque' (whole word after the marker, as "
                "'topo-|logique' at p. 36), and also applies the two p. 40 findings above: soit -> soient and \\emph{l'image "
                "réciproque de 𝒢 par le morphisme} (italics across pp. 40-41). 'old' is long because it must span from the "
                "old marker to the new position."))

json.dump(L, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
print("wrote", OUT, len(L), "findings")
