"""Build findings_175_179.json and check every fix against page_NNN.tex and the source page segment.
Read-only on all .tex files."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_I_b")
E = RUN.parent
OUT = RUN / "findings_175_179.json"
N = "\n"

F = []


def add(page, where, scan, tex, kind, conf, fix, note, convention=None, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=convention,
             confidence=conf, fix=fix)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


ITALIC_LABEL = ("Labels a), b), c), ... are italic in the roman proof text of the print; "
                "the TeX sets them roman.")

# ---------------------------------------------------------------- page 175
add(175, "Lemme (9.4.6), label 1°",
    "label 1° roman inside the italic statement",
    r"\item[1\textsuperscript{o}]", "convention", "high",
    fx(r"\item[1\textsuperscript{o}]", r"\item[\textup{1\textsuperscript{o}}]"),
    "Checked on a crop: the old-style 1 and the superior o are upright; \\item takes the italic of the "
    "lemma environment. (The print runs 1° and 2° into the paragraph; that layout is not reported.)",
    convention=6)
add(175, "Lemme (9.4.6), label 2°",
    "label 2° roman inside the italic statement",
    r"\item[2\textsuperscript{o}]", "convention", "high",
    fx(r"\item[2\textsuperscript{o}]", r"\item[\textup{2\textsuperscript{o}}]"),
    "Checked on a crop, as for 1°.", convention=6)
add(175, "Lemme (9.4.6), end of condition 1°: 'V_λ∩W_λ soit quasi-compact : 2° Le morphisme'",
    "colon ':' after 'quasi-compact', before 2°",
    "soit quasi-compact~;", "misprint_in_print", "medium",
    fx("soit quasi-compact~;", "soit quasi-compact~:"),
    "The TeX silently corrects the print (checked on a crop at 4x: a colon, two equal dots, no comma "
    "tail). Between the numbered conditions 1° and 2° the colon is a slip for the semicolon.",
    corrected="soit quasi-compact~;")
add(175, "Lemme (9.4.6): 'tout sous-(𝒪_X|U)-Module quasi-cohérent de type fini 𝒢 de ℱ|U'",
    "'de type fini' roman inside the italic statement ('de' after 𝒢 is italic)",
    r"quasi-cohérent de type fini $\mathscr{G}$ de", "convention", "high",
    fx(r"de type fini $\mathscr{G}$ de" + N + r"$\mathscr{F}|U$, il existe un",
       r"\textup{de type fini} $\mathscr{G}$ de" + N + r"$\mathscr{F}|U$, il existe un"),
    "Checked on a crop. The 'old' spans the line break; the same line recurs in Théorème (9.4.7), "
    "hence the context 'il existe un'.", convention=6)
add(175, "Lemme (9.4.6): 'il existe un sous-𝒪_X-Module quasi-cohérent de type fini 𝒢' de ℱ'",
    "'de type fini' roman inside the italic statement (split 'de / type fini' in the print)",
    r"quasi-cohérent de type fini $\mathscr{G}'$ de $\mathscr{F}$", "convention", "high",
    fx(r"quasi-cohérent de" + N + r"type fini $\mathscr{G}'$",
       r"quasi-cohérent \textup{de" + N + r"type fini} $\mathscr{G}'$"),
    "Checked on a crop. The 'old' spans the line break.", convention=6)
add(175, "proof of Lemme (9.4.6): 'L'unique sous-𝒪_X-Module 𝒢' de ℱ tel que 𝒢'|U_λ=𝒢' pour tout λ∈L'",
    "𝒢'|U_λ=𝒢' : no subscript λ on the right-hand 𝒢'",
    r"$\mathscr{G}'|U_\lambda=\mathscr{G}'_\lambda$", "misprint_in_print", "high",
    fx(r"$\mathscr{G}'|U_\lambda=\mathscr{G}'_\lambda$ pour tout",
       r"$\mathscr{G}'|U_\lambda=\mathscr{G}'$ pour tout"),
    "The TeX silently corrects the print. Checked on a crop at 4x: the right-hand 𝒢' carries only the "
    "prime. 𝒢' is obtained by gluing the family (𝒢'_λ), so the correct reading is 𝒢'_λ.",
    corrected=r"$\mathscr{G}'|U_\lambda=\mathscr{G}'_\lambda$")
add(175, "proof of Lemme (9.4.6): 'pour tout λ∈L (0, 3.3.1) répondra à la question'",
    "(𝟎, 3.3.1) with bold 0", r"{0, 3.3.1}) répondra", "convention", "high",
    fx("{0, 3.3.1}) répondra", r"{\textbf{0}, 3.3.1}) répondra"), "", convention=2)
add(175, "proof of Lemme (9.4.6): '𝒢'_λ|V_μ=𝒢''_μ (0, 3.3.1). Or, comme V_μ est affine'",
    "(𝟎, 3.3.1) with bold 0", r"{0, 3.3.1}). Or, comme", "convention", "high",
    fx("{0, 3.3.1}). Or, comme", r"{\textbf{0}, 3.3.1}). Or, comme"), "", convention=2)
add(175, "Théorème (9.4.7), label a)",
    "roman label 'a)' without an opening parenthesis",
    r"\item[(a)]", "punctuation", "high",
    fx(r"\item[(a)]", r"\item[\textup{a)}]"),
    "Checked on a crop: the labels are roman 'a)', 'b)' with no opening parenthesis; \\item[(a)] prints "
    "an italic '(a)' inside the theorem environment. Same pattern as Proposition (6.4.4), p. 148.")
add(175, "Théorème (9.4.7), label b)",
    "roman label 'b)' without an opening parenthesis",
    r"\item[(b)]", "punctuation", "high",
    fx(r"\item[(b)]", r"\item[\textup{b)}]"), "As for a).")
add(175, "Théorème (9.4.7): 'tout sous-(𝒪_X|U)-Module quasi-cohérent de type fini 𝒢 de ℱ|U'",
    "'de type fini' roman inside the italic statement (split 'de / type fini' in the print; "
    "'de' after 𝒢 is italic)",
    r"quasi-cohérent de type fini $\mathscr{G}$ de", "convention", "high",
    fx(r"de type fini $\mathscr{G}$ de" + N + r"$\mathscr{F}|U$, il existe alors",
       r"\textup{de type fini} $\mathscr{G}$ de" + N + r"$\mathscr{F}|U$, il existe alors"),
    "Checked on a crop. The 'old' spans the line break.", convention=6)
add(175, "Théorème (9.4.7): 'un sous-𝒪_X-Module quasi-cohérent de type fini 𝒢' de ℱ'",
    "'de type fini' roman inside the italic statement",
    r"quasi-cohérent de type fini $\mathscr{G}'$ de $\mathscr{F}$", "convention", "high",
    fx(r"de type fini $\mathscr{G}'$ de $\mathscr{F}$",
       r"\textup{de type fini} $\mathscr{G}'$ de $\mathscr{F}$"),
    "Checked on a crop. (In Corollaire (9.4.5) on the same page 'de type fini' is italic, as in the TeX.)",
    convention=6)

# ---------------------------------------------------------------- page 176
add(176, "proof of (9.4.7): 'L étant supposé fini dans le cas b) ;'",
    "b) in italics", "dans le cas b)~;", "italics", "high",
    fx("dans le cas b)~;", r"dans le cas \emph{b)}~;"), ITALIC_LABEL + " Checked on a crop.")
add(176, "proof of (9.4.7): 'C'est évident dans l'hypothèse a), les espaces V_λ'",
    "a) in italics", "dans l'hypothèse a),", "italics", "high",
    fx("dans l'hypothèse a),", r"dans l'hypothèse \emph{a)},"), ITALIC_LABEL)
add(176, "proof of (9.4.7): 'Dans l'hypothèse b), les V_λ∩V_μ sont affines'",
    "b) in italics", "Dans l'hypothèse b),", "italics", "high",
    fx("Dans l'hypothèse b),", r"Dans l'hypothèse \emph{b)},"), ITALIC_LABEL)
add(176, "proof of (9.4.10): 's|V=Σ_i a_i.(t_i|V)'",
    "a_i.(t_i|V) with a baseline dot (full-stop height), not a centred dot",
    r"a_i\mathbin{\cdot}(t_i|V)", "symbol", "low",
    fx(r"a_i\mathbin{\cdot}(t_i|V)", r"a_i.(t_i|V)"),
    "Checked on a crop at 8x: the dot sits on the baseline of a, well below the axis of the = sign. "
    "This is the only \\mathbin{\\cdot} in the EGA I sources. Low confidence only because the height "
    "of product dots may be settled once for the whole edition.")
add(176, "Proposition (9.5.1): '(ou, ce qui revient au même (4.4.1), tel que le sous-préschéma "
         "f^{-1}(Y') de X soit identique à X)'",
    "the parenthesis is roman inside the italic statement, with 'identique à' in italics",
    r"(ou, ce qui revient au même (\hyperref[I.4.4.1-fr]{4.4.1}), tel que le sous-préschéma "
    r"$f^{-1}(Y')$ de $X$ soit \emph{identique} à $X$)", "convention", "high",
    fx(r"(ou, ce qui" + N + r"revient au même (\hyperref[I.4.4.1-fr]{4.4.1}), tel que le sous-préschéma"
       + N + r"$f^{-1}(Y')$ de $X$ soit \emph{identique} à $X$)",
       r"\textup{(ou, ce qui" + N + r"revient au même (\hyperref[I.4.4.1-fr]{4.4.1}), tel que le sous-préschéma"
       + N + r"$f^{-1}(Y')$ de $X$ soit \emph{identique à} $X$)}"),
    "Checked on a crop: 'majore f' is italic, the parenthesis roman, and inside it both 'identique' and "
    "'à' are italic, so the fix also moves 'à' into the \\emph (inside \\textup, \\emph gives italic). "
    "Same pattern as Corollaire (5.5.8), p. 138.", convention=6)
add(176, "proof of Corollaire (9.5.2): 'donne (0, 3.5.4.3) une factorisation'",
    "(𝟎, 3.5.4.3) with bold 0", r"{0, 3.5.4.3}", "convention", "high",
    fx("{0, 3.5.4.3}", r"{\textbf{0}, 3.5.4.3}"), "", convention=2)
add(176, "proof of Corollaire (9.5.2): 'une factorisation θ^♯ : ψ^*(𝒪_Y)→ψ^*(𝒪_Y)/ψ^*(𝒥) →^{θ'^♯} 𝒪_X ;'",
    "factorisation set inline in the running text: '... une factorisation θ^♯ : ... →^{θ'^♯} 𝒪_X ; "
    "comme pour tout x∈X, ...'",
    r"factorisation set as a displayed formula \[ ... \]", "other", "low",
    fx("une factorisation" + N + r"\[" + N + r"  \theta^\sharp:\psi^*(\mathscr{O}_Y)" + N
       + r"  \to\psi^*(\mathscr{O}_Y)/\psi^*(\mathscr{J})" + N
       + r"  \xrightarrow{{\theta'}^\sharp}\mathscr{O}_X~;" + N + r"\]" + N + "comme pour tout",
       "une factorisation" + N + r"$\theta^\sharp:\psi^*(\mathscr{O}_Y)" + N
       + r"\to\psi^*(\mathscr{O}_Y)/\psi^*(\mathscr{J})" + N
       + r"\xrightarrow{{\theta'}^\sharp}\mathscr{O}_X$~;" + N + "comme pour tout"),
    "Layout only (display vs inline); the formula itself matches. Same kind as the p. 134 finding.")
add(176, "proof of Corollaire (9.5.2): 'si on désigne par ψ_0 l'application continue ψ considérée comme "
         "application de X dans X', par θ_0 la restriction θ'|X' : (𝒪_Y/𝒥)|X'→ψ_*(𝒪_X)|X'=(ψ_0)_*(𝒪_X), "
         "... un morphisme de préschémas X→X' (2.2.1) tel que f=j∘f_0'",
    "X' (five times on this page) for the closed subprescheme of Y defined by 𝒥, which the statement of "
    "(9.5.2) calls Y'",
    r"dans $X'$ ... $\theta'|X':(\mathscr{O}_Y/\mathscr{J})|X'\to\psi_*(\mathscr{O}_X)|X'=(\psi_0)_*(\mathscr{O}_X)$"
    r" ... $X\to X'$", "misprint_in_print", "high", None,
    "The TeX keeps the printed reading (checked on crops). Corollaire (9.5.2) names Y' the closed "
    "subprescheme of Y defined by 𝒥, and j : Y'→Y is the injection of (9.5.1); X' is defined nowhere "
    "in the statement or the proof and stands for Y'. The slip continues on p. 177 ('donc X'⊂X''', "
    "'X' est un sous-préschéma fermé de X'''). X'' is introduced in the proof itself ('Si maintenant "
    "X'' est un second sous-préschéma fermé de Y'), so it can stay (Y'' would be the matching name). "
    "The corrected edition (r20 current) still has X'.",
    corrected=r"l'application continue $\psi$ considérée comme application de $X$ dans $Y'$, par "
              r"$\theta_0$ la restriction $\theta'|Y':(\mathscr{O}_Y/\mathscr{J})|Y'\to"
              r"\psi_*(\mathscr{O}_X)|Y'=(\psi_0)_*(\mathscr{O}_X)$, on voit donc que "
              r"$f_0=(\psi_0,\theta_0)$ est un morphisme de préschémas $X\to Y'$")

# ---------------------------------------------------------------- page 177
add(177, "end of the proof of (9.5.2): 'donc X'⊂X'' puisque X'' est fermé' and 'et par suite X' est un "
         "sous-préschéma fermé de X'' (4.1.10)'",
    "X' (twice) for the Y' of the statement of (9.5.2)",
    r"$X'\subset X''$ ... par suite $X'$ est un sous-préschéma fermé de $X''$",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed reading. Continuation of the X'/Y' slip of p. 176 (see that finding).",
    corrected=r"donc $Y'\subset X''$ puisque $X''$ est fermé. [...] et par suite $Y'$ est un "
              r"sous-préschéma fermé de $X''$")
add(177, "Définition (9.5.3): 'on dit que Y' est le préschéma image fermée de X par le morphisme f'",
    "the defined term 'image fermée' roman inside the italic definition",
    "préschéma image fermée de $X$", "convention", "high",
    fx("préschéma image fermée de $X$", r"préschéma \emph{image fermée} de $X$"),
    "Checked on a crop: 'préschéma' and 'de X par le morphisme f' italic, 'image fermée' upright. "
    "Inside the italic definition environment \\emph sets the term upright.", convention=6)
add(177, "proof of (9.5.5): 'ce qui équivaut à dire que j^{-1}(g^{-1}(Z_1))=g'^{-1}(Z_1)=Y' en désignant "
         "par j l'injection Y'→Y'",
    "no comma after =Y'", "=Y'$, en désignant", "punctuation", "high",
    fx("=Y'$, en désignant", "=Y'$ en désignant"),
    "The TeX adds a comma (checked on a crop at 5x).")

# ---------------------------------------------------------------- page 178
add(178, "Remarque (9.5.7), continued: 'f est un épimorphisme dans la catégorie des S-schémas (T, 1.1)'",
    "'schémas' in italics after a roman S- (like 'épimorphisme'); 'dans la catégorie des' roman",
    "des $S$-schémas (T, 1.1)", "italics", "high",
    fx("des $S$-schémas (T, 1.1)", r"des $S$-\emph{schémas} (T, 1.1)"),
    "Checked on a crop. Judged as if the remark body were roman (document-wide remark item); the TeX "
    "already has \\emph{épimorphisme}. The later 'épimorphisme de S-schémas' is all roman, as in the TeX.")
add(178, "Proposition (9.5.8): '(autrement dit, au sous-préschéma inf(V, Y') de Y (4.4.3))'",
    "the parenthesis is roman inside the italic statement",
    r"(autrement dit, au sous-préschéma $\inf(V,Y')$ de $Y$ (\hyperref[I.4.4.3-fr]{4.4.3}))",
    "convention", "high",
    fx(r"(autrement dit, au sous-préschéma" + N + r"$\inf(V,Y')$ de $Y$ (\hyperref[I.4.4.3-fr]{4.4.3}))",
       r"\textup{(autrement dit, au sous-préschéma" + N
       + r"$\inf(V,Y')$ de $Y$ (\hyperref[I.4.4.3-fr]{4.4.3}))}"),
    "Checked on a crop; the preceding 'de Y'' is italic. The 'old' spans the line break.", convention=6)
add(178, "Proposition (9.5.9), label (i)",
    "label (i) roman inside the italic statement", r"\item[(i)]", "convention", "high",
    fx(r"\item[(i)]", r"\item[\textup{(i)}]"),
    "Checked on a crop; \\item takes the italic of the proposition environment.", convention=6)
add(178, "Proposition (9.5.9), label (ii)",
    "label (ii) roman inside the italic statement", r"\item[(ii)]", "convention", "high",
    fx(r"\item[(ii)]", r"\item[\textup{(ii)}]"), "Checked on a crop.", convention=6)
add(178, "Proposition (9.5.9) (ii): 'et si X est irréductible (resp. intègre), il en est de même de Y''",
    "'(resp.' roman inside the italic statement; 'intègre' italic",
    "irréductible (resp.", "convention", "high",
    fx("irréductible (resp.", r"irréductible \textup{(resp.}"),
    "Checked on a crop. Same form of fix as for '(resp.' on pp. 146-147.", convention=6)
add(178, "proof of (9.5.9): 'g se factorise en X →^h Y'_red →^{j'} Y' où j' est l'injection canonique (5.2.2)'",
    "no comma after the factorisation", r"\xrightarrow{j'}Y'$, où", "punctuation", "high",
    fx(r"\xrightarrow{j'}Y'$, où", r"\xrightarrow{j'}Y'$ où"),
    "The TeX adds a comma (checked on a crop at 3x). The first factorisation two lines earlier "
    "('X→Y'→Y, où j est l'injection canonique') does have its comma, as in the TeX.")
add(178, "proof of (9.5.9): 'il en est donc de même de Y' (0, 2.1.5)'",
    "(𝟎, 2.1.5) with bold 0", r"{0, 2.1.5}", "convention", "high",
    fx("{0, 2.1.5}", r"{\textbf{0}, 2.1.5}"), "", convention=2)
add(178, "proof of Proposition (9.5.10): 'Il suffit d'appliquer (9.5.1) à l'injection j, qui est séparée (5.5.1)'",
    "à l'injection j", "à l'injection $j$, qui", "misprint_in_print", "medium", None,
    "The TeX keeps the printed reading (checked on a crop). The statement of (9.5.10) names the "
    "canonical injection i : Y→X and assumes i quasi-compact; the proof applies (9.5.1) to that "
    "injection, so the letter should be i.",
    corrected=r"à l'injection $i$, qui")

# ---------------------------------------------------------------- page 179
add(179, "paragraph after the proof of (9.5.11): 'Lorsqu'il existe un plus petit sous-préschéma fermé Y "
         "de X majorant un sous-préschéma Y de X, on dit que Y' est l'adhérence de Y dans X'",
    "the first Y has no prime (checked on a crop at 6x)",
    "fermé $Y$ de $X$", "misprint_in_print", "high", None,
    "The TeX keeps the printed reading. The sentence goes on 'on dit que Y' est l'adhérence de Y', so "
    "the smallest closed subprescheme majorizing Y is Y' (the Ȳ of (9.5.10)).",
    corrected=r"Lorsqu'il existe un plus petit sous-préschéma fermé $Y'$ de $X$ majorant un "
              r"sous-préschéma $Y$ de $X$")
add(179, "Proposition (9.6.1): '𝓑 une 𝒪_X-Algèbre quasi-cohérente (0, 5.1.3)'",
    "(𝟎, 5.1.3) with bold 0", r"{0, 5.1.3}", "convention", "high",
    fx("{0, 5.1.3}", r"{\textbf{0}, 5.1.3}"), "", convention=2)
add(179, "(9.6.2): 'une 𝒪_X-Algèbre quasi-cohérente 𝓑 est de type fini si pour tout x∈X'",
    "'de type fini' in italics, including 'de'",
    r"est de \emph{type fini} si", "italics", "high",
    fx("de" + N + r"\emph{type fini}", r"\emph{de" + N + "type fini}"),
    "Checked on a crop: 'de' is italic like 'type fini'. The 'old' spans the line break.")
add(179, "(9.6.2): 'car elle est isomorphe à (B_f)~, et B_f=B⊗_A A_f'",
    "(B_f)~ : parentheses round B_f, tilde written after the closing parenthesis",
    r"\widetilde{B_f}", "convention", "high",
    fx(r"isomorphe à $\widetilde{B_f}$", r"isomorphe à $(B_f)\supertilde$"),
    "Checked on a crop. The TeX has neither the parentheses nor the tilde after them.", convention=5)
add(179, "Proposition (9.6.3): 'est alors un faisceau cohérent d'anneaux (0, 5.3.7)'",
    "(𝟎, 5.3.7) with bold 0", r"{0, 5.3.7}", "convention", "high",
    fx("{0, 5.3.7}", r"{\textbf{0}, 5.3.7}"), "", convention=2)

# ---------------------------------------------------------------- checks
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]["I"]["files"]
marker = re.compile(r"\\oldpage\[I\]\{(\d+)\}")


def source_segment(page):
    for f in inv:
        t = pathlib.Path(f).read_text(encoding="utf-8")
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for i, (n, s) in enumerate(cuts):
            if n == page:
                return f, t[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(t)]
    return None, None


ok = True
for page in sorted({x["page"] for x in F}):
    tex = (RUN / f"page_{page:03d}.tex").read_text(encoding="utf-8")
    src_file, seg = source_segment(page)
    for label, text in (("page_tex", tex), ("source", seg)):
        cur = text
        for x in [y for y in F if y["page"] == page]:
            fix = x["fix"]
            if not fix:
                continue
            n = cur.count(fix["old"])
            if n != 1:
                ok = False
                print(f"{label} p.{page}: old occurs {n} times: {fix['old']!r}")
            else:
                cur = cur.replace(fix["old"], fix["new"])
    print(page, "source:", pathlib.Path(src_file).name if src_file else None)

json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("written", OUT, len(F), "findings; all fixes unique and sequentially applicable:", ok)
for p in sorted({x["page"] for x in F}):
    xs = [x for x in F if x["page"] == p]
    print(p, "normal", sum(1 for x in xs if x["kind"] not in ("convention", "misprint_in_print")),
          "convention", sum(1 for x in xs if x["kind"] == "convention"),
          "misprint", sum(1 for x in xs if x["kind"] == "misprint_in_print"))
