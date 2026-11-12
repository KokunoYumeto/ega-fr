"""Write findings_010_014.json and check every fix against the page files and the release segments."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
OUT = RUN / "findings_010_014.json"
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\BASE\native\ega2\ega2-1-fr.tex")

F = []


def add(page, where, scan, tex, kind, convention, confidence, old, new, note="", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=convention,
             confidence=confidence, fix=(None if old is None else {"old": old, "new": new}))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def conv2(page, where, ref, old, new):
    add(page, where, f"({ref}) with bold chapter numeral", old, "convention", 2, "high", old, new)


# ---------------------------------------------------------------- page 10
add(10, "Prop. (1.4.3), parenthesis '(en tant que O_S-Module ou en tant que B-Module, ce qui revient au même (I, 9.6.1))'",
    "the whole parenthesis is roman inside the italic statement",
    "set inside the italic proposition environment",
    "convention", 6, "high",
    r"""(en tant que
$\mathcal{O}_S$-Module ou en tant que $\mathcal{B}$-Module, ce qui revient au
même (\hyperref[I.9.6.1-fr]{I, 9.6.1}))""",
    r"""\textup{(en tant que
$\mathcal{O}_S$-Module ou en tant que $\mathcal{B}$-Module, ce qui revient au
même (\hyperref[I.9.6.1-fr]{I, 9.6.1}))}""",
    "Apply before the next item (bold I of the same reference): its 'old' survives this edit, but this 'old' "
    "does not survive that one.")
conv2(10, "Prop. (1.4.3), reference (I, 9.6.1)", "I, 9.6.1",
      r"même (\hyperref[I.9.6.1-fr]{I, 9.6.1}", r"même (\hyperref[I.9.6.1-fr]{\textbf{I}, 9.6.1}")
add(10, "proof of Cor. (1.4.4), 'résulte alors de (I, 1.3.5, 1.3.9 et 1.3.11).'",
    "one parenthesis, chapter numeral once: (I, 1.3.5, 1.3.9 et 1.3.11)",
    "three references, each with 'I, ': (I, 1.3.5), (I, 1.3.9) et (I, 1.3.11)",
    "extra", None, "high",
    r"""1.3.5}),
(\hyperref[I.1.3.9-fr]{I, 1.3.9}) et
(\hyperref[I.1.3.11-fr]{I, 1.3.11}).""",
    r"""1.3.5},
\hyperref[I.1.3.9-fr]{1.3.9} et
\hyperref[I.1.3.11-fr]{1.3.11}).""",
    "Independent of the convention-2 edit on {I, 1.3.5} (either order works).")
conv2(10, "proof of Cor. (1.4.4), reference (I, 1.3.5, ...)", "I, 1.3.5, 1.3.9 et 1.3.11",
      r"{I, 1.3.5}", r"{\textbf{I}, 1.3.5}")
add(10, "Cor. (1.4.5), 'Sous les hypothèses de (1.4.3)'",
    "reference (1.4.3) upright inside the italic statement",
    "reference inside the italic corollary environment",
    "convention", 6, "high",
    r"hypothèses de (\hyperref[II.1.4.3-fr]{1.4.3})", r"hypothèses de \textup{(\hyperref[II.1.4.3-fr]{1.4.3})}")
conv2(10, "proof of Cor. (1.4.5), reference (I, 9.6.2)", "I, 9.6.2", r"{I, 9.6.2}", r"{\textbf{I}, 9.6.2}")
add(10, "proof of Cor. (1.4.5), 'où B est une A-algèbre de type fini (I, 9.6.2)'",
    "où B est une A-algèbre de type fini (I, 9.6.2)",
    "same as the print",
    "misprint_in_print", None, "low", None, None,
    "TeX keeps the printed reading. Under the hypotheses of (1.4.3) B is an arbitrary A-algebra (B~ = 𝓑 quasi-coherent); "
    "nothing makes it of finite type, and the proof does not use it. Not in the errata lists of EGA III/IV. "
    "Low confidence as to the intended wording (the reference may also have been meant differently); "
    "for the corrected edition only after a human check.",
    r"où $B$ est une $A$-algèbre")
conv2(10, "proof of Cor. (1.4.5), first reference (I, 1.3.13)", "I, 1.3.13",
      r"{I, 1.3.13})~; \emph{sur", r"{\textbf{I}, 1.3.13})~; \emph{sur")
conv2(10, "proof of Cor. (1.4.5), second reference (I, 1.3.13)", "I, 1.3.13",
      r"{I, 1.3.13}), d'où", r"{\textbf{I}, 1.3.13}), d'où")
add(10, "Prop. (1.4.6), '(donc aussi au-dessus de S (1.3.5))'",
    "parenthesis roman inside the italic statement",
    "set inside the italic proposition environment",
    "convention", 6, "high",
    r"""(donc aussi au-dessus de $S$
(\hyperref[II.1.3.5-fr]{1.3.5}))""",
    r"""\textup{(donc aussi au-dessus de $S$
(\hyperref[II.1.3.5-fr]{1.3.5}))}""")
add(10, "Prop. (1.4.6), 'est affine au-dessus de Y (donc aussi au-dessus de S) et'",
    "parenthesis roman inside the italic statement",
    "set inside the italic proposition environment",
    "convention", 6, "high",
    r"(donc aussi au-dessus de $S$) et", r"\textup{(donc aussi au-dessus de $S$)} et")
conv2(10, "proof of Prop. (1.4.6), 'En effet (I, 9.6.1)'", "I, 9.6.1",
      r"En effet (\hyperref[I.9.6.1-fr]{I, 9.6.1}", r"En effet (\hyperref[I.9.6.1-fr]{\textbf{I}, 9.6.1}")
conv2(10, "proof of Prop. (1.4.6), 'quasi-cohérente (I, 9.6.1); soit Z'", "I, 9.6.1",
      r"{I, 9.6.1})~; soit", r"{\textbf{I}, 9.6.1})~; soit")
conv2(10, "proof of Prop. (1.4.6), reference (I, 3.2.6.4)", "I, 3.2.6.4", r"{I, 3.2.6.4}", r"{\textbf{I}, 3.2.6.4}")
add(10, "proof of Prop. (1.4.6), 'telles que B = B~, A = A~, A' = A~''",
    "Ã′: tilde over A only, prime outside (checked on a crop)",
    r"\widetilde{A'}",
    "convention", 8, "high", r"\widetilde{A'}", r"\widetilde{A}'")
conv2(10, "proof of Prop. (1.4.6), 'On sait alors (I, 1.3.13) que'", "I, 1.3.13",
      r"{I, 1.3.13}) que", r"{\textbf{I}, 1.3.13}) que")
add(10, "proof of Prop. (1.4.6), 'la O_S-Algèbre (A⊗_B A')~'",
    "(A⊗_B A′)~ : tilde after the closing parenthesis",
    r"\widetilde{A\otimes_B A'} (no parentheses)",
    "convention", 5, "high", r"$\widetilde{A\otimes_B A'}$", r"$(A\otimes_B A')\supertilde$",
    "The TeX also drops the printed parentheses.")
conv2(10, "proof of Prop. (1.4.6), reference (I, 3.2.2)", "I, 3.2.2", r"{I, 3.2.2}", r"{\textbf{I}, 3.2.2}")
add(10, "Cor. (1.4.7), 'Soit F (resp. F')'",
    "'(resp. 𝓕′)' roman inside the italic statement",
    "set inside the italic corollary environment",
    "convention", 6, "high", r"(resp. $\mathcal{F}'$)", r"\textup{(resp. $\mathcal{F}'$)}")
add(10, "Cor. (1.4.7), '(resp. un O_X'-Module)'",
    "'(resp.' roman, 'un 𝒪_X′-Module)' italic",
    "set inside the italic corollary environment",
    "convention", 6, "high", "(resp. un\n$\\mathcal{O}_{X'}$", "\\textup{(resp.} un\n$\\mathcal{O}_{X'}$")
conv2(10, "proof of Cor. (1.4.7), reference (I, 9.1.2)", "I, 9.1.2", r"{I, 9.1.2}", r"{\textbf{I}, 9.1.2}")

# ---------------------------------------------------------------- page 11
add(11, "proof of Cor. (1.4.7), 'on a des homomorphismes canoniques Γ(f^{-1}(g^{-1}(U)),F) → ... et ... → Γ(h^{-1}(U),p'^*(F')) (0, 4.4.3)'",
    "the two homomorphisms are set inline in the paragraph (normal line spacing, one justified text line), "
    "with no period after p′*(𝓕′)) (checked on a crop); '(0, 4.4.3), d'où ...' continues the sentence",
    "a displayed aligned formula ending with a period",
    "other", None, "high",
    r"""canoniques
\[
  \begin{aligned}
  \Gamma(f^{-1}(g^{-1}(U)),\mathcal{F})
  &\longrightarrow \Gamma(h^{-1}(U),p^*(\mathcal{F}))\quad\text{et}\quad
  \Gamma(f^{\prime-1}(g^{-1}(U)),\mathcal{F}')
  \longrightarrow \Gamma(h^{-1}(U),p^{\prime*}(\mathcal{F}')).
  \end{aligned}
\]""",
    r"""canoniques
$\Gamma(f^{-1}(g^{-1}(U)),\mathcal{F})\to\Gamma(h^{-1}(U),p^*(\mathcal{F}))$ et
$\Gamma(f^{\prime-1}(g^{-1}(U)),\mathcal{F}')\to\Gamma(h^{-1}(U),p^{\prime*}(\mathcal{F}'))$""",
    "Removes the spurious period and the display. If only the period is wanted: delete the '.' after "
    r"p^{\prime*}(\mathcal{F}')).")
conv2(11, "proof of Cor. (1.4.7), reference (0, 4.4.3)", "0, 4.4.3", r"{0, 4.4.3}", r"{\textbf{0}, 4.4.3}")
add(11, "proof of Cor. (1.4.7), 'F = M~, F' = M~''",
    "M̃′: tilde over M only, prime outside (checked on a crop)",
    r"\widetilde{M'}", "convention", 8, "high",
    r"$\mathcal{F}'=\widetilde{M'}$", r"$\mathcal{F}'=\widetilde{M}'$")
conv2(11, "proof of Cor. (1.4.7), reference (I, 9.1.3)", "I, 9.1.3", r"{I, 9.1.3}", r"{\textbf{I}, 9.1.3}")
add(11, "proof of Cor. (1.4.7), 'des O_S-Modules (M⊗_B M')~'",
    "(M⊗_B M′)~ : tilde after the closing parenthesis",
    r"\widetilde{M\otimes_B M'} (no parentheses)",
    "convention", 5, "high", r"$\widetilde{M\otimes_B M'}$", r"$(M\otimes_B M')\supertilde$",
    "The TeX also drops the printed parentheses.")
add(11, "proof of Cor. (1.4.7), 'et M~ ⊗_{B~} M~''",
    "M̃′: tilde over M only, prime outside (checked on a crop)",
    r"\widetilde{M'}", "convention", 8, "high",
    r"\otimes_{\widetilde{B}}\widetilde{M'}", r"\otimes_{\widetilde{B}}\widetilde{M}'")
conv2(11, "proof of Cor. (1.4.7), reference (I, 1.3.13 et 1.6.3)", "I, 1.3.13 et 1.6.3",
      r"{I, 1.3.13}", r"{\textbf{I}, 1.3.13}")
add(11, "proof of Cor. (1.4.7), '(I, 1.3.13 et 1.6.3)'",
    "(I, 1.3.13 et 1.6.3): chapter numeral once",
    "second link text repeats it: 'I, 1.6.3'",
    "extra", None, "high", r"{I, 1.6.3}).", r"{1.6.3}).")
conv2(11, "(1.4.8), reference (I, 1.6.3 et 1.3.12)", "I, 1.6.3 et 1.3.12",
      r"{I, 1.6.3} et", r"{\textbf{I}, 1.6.3} et")
add(11, "(1.4.8), '(I, 1.6.3 et 1.3.12)'",
    "(I, 1.6.3 et 1.3.12): chapter numeral once",
    "second link text repeats it: 'I, 1.3.12'",
    "extra", None, "high", r"{I, 1.3.12}", r"{1.3.12}")
add(11, "Remarque (1.4.9), 'la somme X ⨿ X''",
    "coproduct sign ∐ (amalgamation sign; checked on a crop)",
    r"X\sqcup X' (cup-shaped ⊔)",
    "symbol", None, "high", r"$X\sqcup X'$", r"$X\amalg X'$",
    "Same as GLOBAL_ISSUES item 6.")
conv2(11, "proof of Prop. (1.4.10), reference (I, 4.2.3)", "I, 4.2.3", r"{I, 4.2.3}", r"{\textbf{I}, 4.2.3}")
conv2(11, "proof of Prop. (1.4.10), reference (I, 4.1.2)", "I, 4.1.2", r"{I, 4.1.2}", r"{\textbf{I}, 4.1.2}")
add(11, "after (1.4.10), 'A(h) : Spec(B') → Spec(B) est une immersion fermée'",
    "𝒜(h) : Spec(𝓑′)→Spec(𝓑) (script A applied to h; checked on a crop)",
    r"{}^a h:\operatorname{Spec}(\mathcal{B}')\to\operatorname{Spec}(\mathcal{B}) (silent correction)",
    "misprint_in_print", None, "high",
    r"${}^a h:", r"$\mathcal{A}(h):",
    "TeX silently corrects. In EGA II 𝒜(u) is the algebra homomorphism of a morphism u of preschemas; h here is "
    "already a homomorphism of 𝒪_S-Algèbres, so the morphism Spec(𝓑′)→Spec(𝓑) is meant. "
    r"The corrected edition's reading {}^a h is fine; (1.5.6) writes the same construction \operatorname{Spec}(u). "
    "Not in the errata lists of EGA III/IV.",
    r"{}^a h")

# ---------------------------------------------------------------- page 12
add(12, "Prop. (1.4.11), 'f^*(K)O_X = (KB)~'",
    "(𝒦𝓑)~ : tilde after the closing parenthesis",
    r"\widetilde{\mathcal{K}\mathcal{B}} (no parentheses)",
    "convention", 5, "high", r"\widetilde{\mathcal{K}\mathcal{B}}", r"(\mathcal{K}\mathcal{B})\supertilde",
    "The TeX also drops the printed parentheses.")
conv2(12, "proof of Prop. (1.4.11), reference (I, 1.6.9)", "I, 1.6.9", r"{I, 1.6.9}", r"{\textbf{I}, 1.6.9}")
conv2(12, "proof of Prop. (1.5.1), reference (I, 3.2.2)", "I, 3.2.2", r"{I, 3.2.2}", r"{\textbf{I}, 3.2.2}")
add(12, "Cor. (1.5.2), 'Sous les hypothèses de (1.5.1)'",
    "reference (1.5.1) upright inside the italic statement",
    "reference inside the italic corollary environment",
    "convention", 6, "high",
    r"hypothèses de (\hyperref[II.1.5.1-fr]{1.5.1})", r"hypothèses de \textup{(\hyperref[II.1.5.1-fr]{1.5.1})}")
add(12, "Cor. (1.5.2), diagram, left vertical arrow X → S",
    "left vertical arrow without a label",
    "X\\ar[d] (no label; keeps the print)",
    "misprint_in_print", None, "high", None, None,
    "TeX keeps the printed reading. Errata et addenda, liste 2 (EGA III): (II, 1.5.2), line 17 of p. 12, "
    "insert an f beside the left vertical arrow of the diagram.",
    r"X\ar[d]_{f}")
add(12, "Cor. (1.5.2), diagram, bottom arrow S' → S",
    "label g below the bottom arrow (g′ above the top arrow)",
    "S'\\ar[l]_g, which xy-pic sets above a leftward arrow (checked by compiling the diagram)",
    "other", None, "high", r"S'\ar[l]_g", r"S'\ar[l]^g",
    "For a leftward arrow ^ puts the label below; the top arrow's \\ar[l]_{g'} (above) is right.")
conv2(12, "proof of Cor. (1.5.2), 'u = v^♯ (0, 4.4.3)'", "0, 4.4.3",
      r"{0, 4.4.3}). Nous", r"{\textbf{0}, 4.4.3}). Nous")
conv2(12, "proof of Cor. (1.5.2), 'F → g'_*(g'^*(F)) (0, 4.4.3)'", "0, 4.4.3",
      r"{0, 4.4.3}). Pour", r"{\textbf{0}, 4.4.3}). Pour")
conv2(12, "proof of Cor. (1.5.2), reference (I, 1.6.3, 1.6.5 et 1.6.7)", "I, 1.6.3, 1.6.5 et 1.6.7",
      r"{I, 1.6.3}", r"{\textbf{I}, 1.6.3}")
add(12, "Remarque (1.5.3), 'S' = Spec(k(s))'",
    "bold italic k in k(s)", r"\operatorname{Spec}(k(s))",
    "convention", 1, "high", r"\operatorname{Spec}(k(s))", r"\operatorname{Spec}(\boldsymbol{k}(s))")
conv2(12, "Remarque (1.5.3), reference (I, 2.4.5)", "I, 2.4.5", r"{I, 2.4.5}", r"{\textbf{I}, 2.4.5}")
conv2(12, "Remarque (1.5.3), reference (I, 3.6.2)", "I, 3.6.2", r"{I, 3.6.2}", r"{\textbf{I}, 3.6.2}")

# ---------------------------------------------------------------- page 13
conv2(13, "Remarque (1.5.3), 'au chapitre III (III, 4.2.4)'", "III, 4.2.4",
      r"{III, 4.2.4}", r"{\textbf{III}, 4.2.4}")
add(13, "proof of Cor. (1.5.4), 'S' = Spec(k(s))'",
    "bold italic k in k(s)", r"\operatorname{Spec}(k(s))",
    "convention", 1, "high", r"\operatorname{Spec}(k(s))", r"\operatorname{Spec}(\boldsymbol{k}(s))")
conv2(13, "(1.5.6), 'u^♯ : q^*(B) → B' (0, 4.4.3)'", "0, 4.4.3", r"{0, 4.4.3}", r"{\textbf{0}, 4.4.3}")
add(13, "(1.5.6), 'la restriction de u en un (q|U')-morphisme : B|U → B'|U''",
    "(q|U′)-morphisme : 𝓑|U→𝓑′|U′ (colon after 'morphisme'; checked on a crop)",
    "no colon",
    "punctuation", None, "high",
    "-morphisme\n$\\mathcal{B}|U\\to", "-morphisme~:\n$\\mathcal{B}|U\\to")
conv2(13, "(1.5.6), reference (I, 1.7.3)", "I, 1.7.3", r"{I, 1.7.3}", r"{\textbf{I}, 1.7.3}")

# ---------------------------------------------------------------- page 14
add(14, "proof of Prop. (1.6.2), 'En vertu de (I, 5.5.12)'",
    "the word 'de' before the reference is set in bold (stroke width about 25% above the other 'de' on the line)",
    "roman 'de' (silent correction)",
    "misprint_in_print", None, "medium",
    r"En vertu de (", r"En vertu \textbf{de} (",
    "Typesetting slip: the bold face of the following bold I starts one word early.",
    r"En vertu de (")
conv2(14, "proof of Prop. (1.6.2), reference (I, 5.5.12)", "I, 5.5.12", r"{I, 5.5.12}", r"{\textbf{I}, 5.5.12}")
conv2(14, "proof of Prop. (1.6.2), reference (I, 3.3.11)", "I, 3.3.11", r"{I, 3.3.11}", r"{\textbf{I}, 3.3.11}")
conv2(14, "proof of Prop. (1.6.4), reference (I, 6.1.7)", "I, 6.1.7", r"{I, 6.1.7}", r"{\textbf{I}, 6.1.7}")
add(14, "heading 1.7, 'Fibré vectoriel associé à un faisceau de modules.'",
    "'faisceau' with a lower-case f (checked on a crop)",
    "Faisceau",
    "word", None, "high", r"un Faisceau de modules", r"un faisceau de modules")
add(14, "end of p. 14: display S(E⊕F) = S(E)⊗S(F), sentence continued on p. 15",
    "page 15 begins flush left with 'à un isomorphisme canonique près; ...' (continuation, no new paragraph)",
    r"blank line between \] and \oldpage[II]{15}, which starts a new paragraph",
    "other", None, "high",
    "\\otimes\\mathbf{S}(F)\n\\]\n\n", "\\otimes\\mathbf{S}(F)\n\\]\n",
    "The blank line is the last line of page 14's segment (before the page-15 marker), so the page-15 checker "
    "cannot see it.")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- checks
ok = True
pages = sorted({x["page"] for x in F})
for p in pages:
    txt = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    cur = txt
    for x in F:
        if x["page"] != p or not x["fix"]:
            continue
        old, new = x["fix"]["old"], x["fix"]["new"]
        n0 = txt.count(old)
        n1 = cur.count(old)
        if n0 != 1 or n1 != 1:
            ok = False
            print(f"PAGE FILE p{p}: old count original={n0} sequential={n1}: {old[:60]!r}")
        cur = cur.replace(old, new, 1)

rel = REL.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(rel)]
for p in pages:
    i = [k for k, (n, s) in enumerate(cuts) if n == p][0]
    seg = rel[cuts[i][1]:cuts[i + 1][1]]
    cur = seg
    for x in F:
        if x["page"] != p or not x["fix"]:
            continue
        old, new = x["fix"]["old"], x["fix"]["new"]
        if seg.count(old) != 1 or cur.count(old) != 1:
            ok = False
            print(f"RELEASE p{p}: original={seg.count(old)} sequential={cur.count(old)}: {old[:60]!r}")
        cur = cur.replace(old, new, 1)

json.load(open(OUT, encoding="utf-8"))
counts = {}
for x in F:
    c = counts.setdefault(x["page"], [0, 0, 0])
    c[1 if x["kind"] == "convention" else 2 if x["kind"] == "misprint_in_print" else 0] += 1
print("all checks passed" if ok else "CHECK FAILURES above")
print("per page normal/convention/misprint:", {p: "/".join(map(str, c)) for p, c in sorted(counts.items())})
print("total findings:", len(F))
