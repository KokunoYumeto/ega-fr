import json
import pathlib

RUN = pathlib.Path(r"user/Documents/ega_scan_check_20261101/run_IV3")
OUT = RUN / "findings_030_034.json"
NL = "\u00b6"  # placeholder for a line break inside "old"/"new"


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


IREF = ("The print's reference (old-style figure 1, no bold chapter numeral, no comma) is to EGA IV §1; "
        "ega4-8-fr.tex writes (I, 1.x.y) for it here and elsewhere in the file.")

findings = [
    # ---- page 30
    F(30, "proof of (8.8.2), injectivity: 'les bijections canoniques (I, 3.3.14) donnent'",
      "(𝐈, 3.3.14): bold I", "(I, 3.3.14)", "convention", 2, "high",
      r"(I, 3.3.14)", r"(\textbf{I}, 3.3.14)", "Bold chapter numeral in the reference."),
    F(30, "after the diagram: 'dans le cas particulier où S_α=X_α (compte tenu de (1.3.4))'",
      "(compte tenu de (1.3.4)) — old-style 1, periods, no bold I, no comma",
      "(compte tenu de (I, 3.4))", "number", None, "high",
      r"(compte tenu de (I, 3.4))", r"(compte tenu de (1.3.4))",
      "Enlarged crop (crops_030_034/p30_s2_compte_tenu.png). " + IREF),
    F(30, "'il résulte de (8.3.4) qu'il y a un indice λ⩾α tel que les U_{iμ}=v_{αμ}^{-1}(U_{iα}) forment un recouvrement de X_μ'",
      "un indice λ⩾α (then U_{iμ}, X_μ, 'Remplaçant α par μ')", "$\\lambda\\geq\\alpha$ (keeps the print)",
      "misprint_in_print", None, "medium", None, None,
      "The index found must be μ (U_{iμ}, X_μ and 'Remplaçant α par μ' follow). The TeX keeps the printed λ; "
      "the corrected edition should read μ⩾α. Enlarged crop p30_s3_indice.png.",
      corrected=r"$\mu\geq\alpha$"),
    # ---- page 31
    F(31, "l. 4: 'on peut donc se borner au cas où Y_α est quasi-compact, donc aussi Y'",
      "quasi-compact in italics", "quasi-compact upright", "italics", None, "high",
      r"$Y_\alpha$ est quasi-compact, donc aussi", r"$Y_\alpha$ est \emph{quasi-compact}, donc aussi",
      "Enlarged crop p31_s1_quasicompact.png."),
    F(31, "'Cela étant…': 'soit égal à la restriction de f à U_i'",
      "'restriction de' both italic (f is a formula letter)", "\\emph{restriction} de $f$ ('de' upright)",
      "italics", None, "high",
      r"\emph{restriction} de $f$", r"\emph{restriction de} $f$",
      "Enlarged crop p31_s2_restriction.png."),
    F(31, "'comme X_λ est quasi-séparé (1.2.3), les U_{iλ}∩U_{jλ}'",
      "(1.2.3)", "(I, 1.2.3)", "number", None, "high",
      r"quasi-séparé (I, 1.2.3)", r"quasi-séparé (1.2.3)",
      "Enlarged crop p31_s2_quasisep.png. " + IREF),
    F(31, "'avec A=lim A_λ, C=lim(C_α⊗_{A_λ}A_λ)=C_α⊗_{A_α}A'",
      "first tensor product subscript A_λ: C_α⊗_{A_λ}A_λ", "C_\\alpha\\otimes_{A_\\alpha}A_\\lambda (silently corrected)",
      "misprint_in_print", None, "high",
      r"\varinjlim(C_\alpha\otimes_{A_\alpha}A_\lambda)", r"\varinjlim(C_\alpha\otimes_{A_\lambda}A_\lambda)",
      "C_α is an A_α-algebra; the display below has C_α⊗_{A_α}A_λ. Diplomatic text must keep the printed A_λ. "
      "Enlarged crop p31_s3_lim.png.",
      corrected=r"C_\alpha\otimes_{A_\alpha}A_\lambda"),
    F(31, "after the first display: '(I, 2.2.4) et de même'",
      "(𝐈, 2.2.4): bold I", "(I, 2.2.4)", "convention", 2, "high",
      r"(I, 2.2.4)", r"(\textbf{I}, 2.2.4)", "Bold chapter numeral in the reference."),
    F(31, "Corollaire (8.8.2.4), last line: '(ce qui sera par exemple le cas si Y_α est également' (continues on p. 32)",
      "parenthesis printed roman inside the italic statement", "italic (inside the corollary environment)",
      "convention", 6, "high",
      r"(ce qui¶sera par exemple le cas si $Y_\alpha$ est également",
      r"\textup{(ce qui¶sera par exemple le cas si $Y_\alpha$ est également}",
      "The roman parenthesis ends on p. 32 ('de présentation finie sur S_α)'): see the p. 32 finding."),
    # ---- page 32
    F(32, "l. 1, end of the parenthesis of Corollaire (8.8.2.4): 'de présentation finie sur S_α).'",
      "roman inside the italic statement; 'Soit …' italic again", "italic (corollary environment)",
      "convention", 6, "high",
      r"de présentation finie sur $S_\alpha$). Soit", r"\textup{de présentation finie sur $S_\alpha$)}. Soit",
      "Continuation of the roman parenthesis begun on p. 31."),
    F(32, "start of the proof of (8.8.2) (ii): '(ii) Considérons encore en premier lieu…'",
      "paragraph begins '(ii) Considérons encore …' (no other heading)",
      "\\begin{proof}[Démonstration de (8.8.2), (ii)] — the IV-3 proof environment takes no optional argument, so "
      "'[Démonstration de (8.8.2), (ii)]' is typeset literally; the printed '(ii)' is not in the text",
      "other", None, "high",
      r"\begin{proof}[Démonstration de (8.8.2), (ii)]¶Considérons", r"\begin{proof}¶(ii) Considérons",
      "Same form as earlier \\begin{proof}[...] fixes (GLOBAL_ISSUES 58). The environment's own 'Démonstration. —' "
      "heading is the document-wide item."),
    F(32, "'chacun des Z_{rsμ} est de présentation finie sur S_μ (1.6.2)'",
      "(1.6.2)", "(I, 1.6.2)", "number", None, "high",
      r"sur $S_\mu$ (I, 1.6.2)", r"sur $S_\mu$ (1.6.2)",
      "Enlarged crop p32_s4_162b.png. " + IREF),
    # ---- page 33
    F(33, "'la condition de recollement (0_I, 4.1.7)'",
      "(𝟎_I, 4.1.7): bold 0", "$(0_{\\mathrm I}, 4.1.7)$", "convention", 2, "high",
      r"$(0_{\mathrm I}, 4.1.7)$", r"$(\mathbf{0}_{\mathrm I}, 4.1.7)$",
      "Bold 0 in the reference to chapter 0."),
    F(33, "end of the proof of (8.8.2): 'sont quasi-compactes, donc (1.6.3) X_ρ est de présentation finie'",
      "(1.6.3)", "(I, 1.6.3)", "number", None, "high",
      r"donc (I, 1.6.3) $X_\rho$", r"donc (1.6.3) $X_\rho$",
      "Enlarged crop p33_s1_163.png. " + IREF),
    F(33, "end of the proof of (8.8.2): '… X_ρ est de présentation finie sur S_ρ. C.Q.F.D.'",
      "'C.Q.F.D.' after the last sentence", "missing", "missing", None, "high",
      r"présentation finie sur $S_\rho$.¶\end{proof}", r"présentation finie sur $S_\rho$. C.Q.F.D.¶\end{proof}",
      "Enlarged crop p33_s1_163.png."),
    F(33, "heading of (8.8.3)",
      "'Scholie (8.8.3). — Le contenu essentiel …' (body roman)",
      "\\begin{env}[8.8.3] prints only a bold '(8.8.3)': the word 'Scholie' and '. —' are missing",
      "missing", None, "high",
      r"\begin{env}[8.8.3]", r"\begin{scholium}[8.8.3]",
      "Apply together with the p. 34 edit \\end{env} -> \\end{scholium}. EGA_IV3_FR.tex has no scholium "
      "environment: add one with a ROMAN body, as in EGA_FR.tex (\\textit{Scholie (#1). ---\\ } then upright text); "
      "the EGA_IV2_FR.tex version sets the body italic, which would be wrong here. Same treatment as GLOBAL_ISSUES 48."),
    F(33, "'Considérons en particulier …': 'est encore un S-préschéma de présentation finie (1.6.2)'",
      "(1.6.2)", "(I, 1.6.2)", "number", None, "high",
      r"présentation finie (I, 1.6.2). Alors", r"présentation finie (1.6.2). Alors",
      "Enlarged crop p33_s3_162.png. " + IREF),
    F(33, "'Alors il résulte de ce qui précède et de (I, 3.3.11)'",
      "(𝐈, 3.3.11): bold I", "(I, 3.3.11)", "convention", 2, "high",
      r"(I, 3.3.11)", r"(\textbf{I}, 3.3.11)", "Bold chapter numeral in the reference."),
    F(33, "'f^{-1}(Y)=f_λ^{-1}(Y_λ)×_{S_λ}S (I, 4.4.1)'",
      "(𝐈, 4.4.1): bold I", "(I, 4.4.1)", "convention", 2, "high",
      r"(I, 4.4.1)", r"(\textbf{I}, 4.4.1)", "Bold chapter numeral in the reference."),
    F(33, "'où N_λ est le noyau du couple de S_λ-morphismes (f_{1λ};f_{2λ})'",
      "(f_{1λ};f_{2λ}): a small semicolon (dot above a comma) between the two maps; (f_1, f_2)_S two lines above has a plain comma",
      "$(f_{1\\lambda},f_{2\\lambda})$ (silently corrected to a comma)",
      "misprint_in_print", None, "medium",
      r"$(f_{1\lambda},f_{2\lambda})$", r"$(f_{1\lambda};f_{2\lambda})$",
      "Wrong sort (semicolon for comma), not an inking defect: the dot is a full punctuation dot. "
      "Enlarged crops p33_s4_sep_zoom.png, p33_s4_sep_zoom2.png, p33_s4_f1f2S_b.png.",
      corrected=r"(f_{1\lambda},f_{2\lambda})"),
    # ---- page 34
    F(34, "'est égal à G×_S G×_S G (II, 8.3.9)'",
      "(𝐈𝐈, 8.3.9): bold II", "(II, 8.3.9)", "convention", 2, "high",
      r"(II, 8.3.9)", r"(\textbf{II}, 8.3.9)", "Bold chapter numeral in the reference."),
    F(34, "end of Scholie (8.8.3)",
      "Scholie ends with '… s'interprètent de même.'", "\\end{env}", "other", None, "high",
      r"de même.¶\end{env}", r"de même.¶\end{scholium}",
      "Closing half of the p. 33 env -> scholium change; apply both together (and define scholium in EGA_IV3_FR.tex)."),
    F(34, "subsection heading 8.9",
      "'8.9. Premières applications à l'élimination des hypothèses noethériennes.' (final full stop)",
      "\\subsection{… noethériennes} (no full stop)", "punctuation", None, "high",
      r"hypothèses noethériennes}", r"hypothèses noethériennes.}",
      "GLOBAL_ISSUES 43/58: subsection titles lack the printed full stop."),
    F(34, "Proposition (8.9.1), label (i)",
      "(i) upright", "\\item[(i)] italic inside the italic proposition", "convention", 6, "high",
      r"\item[(i)] Les conditions", r"\item[\textup{(i)}] Les conditions",
      "GLOBAL_ISSUES 16. The labels a), b), c) are upright in the print and the TeX's \\emph{a)} already gives upright there."),
    F(34, "Proposition (8.9.1), label (ii)",
      "(ii) upright", "\\item[(ii)] italic", "convention", 6, "high",
      r"\item[(ii)] Si $\mathcal F$", r"\item[\textup{(ii)}] Si $\mathcal F$", "GLOBAL_ISSUES 16."),
    F(34, "Proposition (8.9.1), label (iii)",
      "(iii) upright", "\\item[(iii)] italic", "convention", 6, "high",
      r"\item[(iii)] Si $Y$", r"\item[\textup{(iii)}] Si $Y$", "GLOBAL_ISSUES 16."),
    F(34, "proof of (8.9.1) (i): 'un A_0-préschéma de type fini est de présentation finie (1.6.1)'",
      "(1.6.1)", "(I, 1.6.1)", "number", None, "high",
      r"présentation finie (I, 1.6.1)", r"présentation finie (1.6.1)",
      "Enlarged crop p34_s3_161.png. " + IREF),
    F(34, "proof of (8.9.1) (i): 'donc b) implique a) en vertu de (1.6.2, (iii))'",
      "(1.6.2, (iii))", "(I, 1.6.2, (iii))", "number", None, "high",
      r"(I, 1.6.2, (iii))", r"(1.6.2, (iii))", IREF),
    F(34, "proof of (8.9.1): 'L'assertion (ii) se déduit immédiatement de (8.5.2, (ii)), (8.3.11) et (1.8.2)'",
      "(1.8.2)", "(I, 1.8.2)", "number", None, "high",
      r"(I, 1.8.2)", r"(1.8.2)",
      "Enlarged crop p34_s4_182.png. " + IREF),
]

# every fix's "old" must occur exactly once in its page file
bad = []
for f in findings:
    if f["fix"] is None:
        continue
    text = (RUN / ("page_%03d.tex" % f["page"])).read_text(encoding="utf-8")
    n = text.count(f["fix"]["old"])
    if n != 1:
        bad.append((f["page"], f["fix"]["old"], n))
if bad:
    for b in bad:
        print("NOT UNIQUE:", b)
    raise SystemExit(1)

OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
counts = {}
for f in findings:
    c = counts.setdefault(f["page"], [0, 0, 0])
    if f["kind"] == "misprint_in_print":
        c[2] += 1
    elif f["kind"] == "convention":
        c[1] += 1
    else:
        c[0] += 1
print("written", OUT, len(findings))
for p in sorted(counts):
    print(p, "normal/convention/misprint:", "/".join(map(str, counts[p])))
