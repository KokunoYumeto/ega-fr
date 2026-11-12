"""Write findings_016_020.json for run_0I (pages 16-20) and check that every fix's "old" occurs exactly once
in its page_NNN.tex (CRLF normalised to LF) and in the release source ega0-1-fr.tex."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
OUT = RUN / "findings_016_020.json"
SRC = (RUN.parent / "ega-fr" / "editions" / "2026-10-24-r20" / "diplomatic" / "packages" / "BASE" / "native"
       / "ega1" / "ega0-1-fr.tex")

BS = "\\"


def L(*lines):
    return "\n".join(lines)


def F(page, where, scan, tex, kind, confidence, old, new, note, convention=None, corrected=None, fix_page=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": convention,
         "confidence": confidence, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    d["_fix_page"] = fix_page or page
    return d


INLINE = "Layout: the print sets this formula inline in the running text; the TeX displays it."

findings = [
    # ---------------- page 16 ----------------
    F(16, "top of the page, 'est commutatif, pour tout homomorphisme u : M→N' (end of (1.4.1))",
      "continues the sentence of (1.4.1) begun on p. 15 (diagram ... 'est commutatif'); first line not indented, "
      "no new paragraph",
      r"blank line after the \] closing the p. 15 diagram, before \oldpage{16}: 'est commutatif' starts a new "
      r"indented paragraph",
      "other", "medium",
      L(r"T^{-1}N", r"\end{tikzcd}", r"\]", "", ""), L(r"T^{-1}N", r"\end{tikzcd}", r"\]", ""),
      "Spurious paragraph break at the page boundary. The fix lies in page_015.tex (last lines of its segment, "
      r"just before \oldpage[0\textsubscript{I}]{16}); its 'old' occurs once there and once in ega0-1-fr.tex.",
      fix_page=15),
    F(16, "(1.4.5), 'posons ρ_{βα}=ρ_A^{S_β,S_α} pour α⩽β ; en vertu de (1.4.4)'",
      "inline: 'posons ρ_{βα}=ρ_A^{S_β,S_α} pour α⩽β ; en vertu de (1.4.4), les homomorphismes ...'",
      r"displayed: \[ \rho_{\beta\alpha}=\rho_A^{S_\beta,S_\alpha}\quad\text{pour }\alpha\leq\beta; \]",
      "other", "high",
      L(r"\[", r"  \rho_{\beta\alpha}=\rho_A^{S_\beta,S_\alpha}\quad\text{pour }\alpha\leq\beta;", r"\]"),
      r"$\rho_{\beta\alpha}=\rho_A^{S_\beta,S_\alpha}$ pour $\alpha\leq\beta$;",
      INLINE),
    F(16, "(1.4.5), last line, 'le second étant fonctoriel en M.'",
      "only 'fonctoriel' is italic; 'en M' is roman",
      r"\emph{fonctoriel en $M$}",
      "italics", "high",
      r"\emph{fonctoriel en $M$}", r"\emph{fonctoriel} en $M$",
      "The emphasis is too wide in the TeX."),
    # ---------------- page 17 ----------------
    F(17, "(1.5.1), 'l'homomorphisme composé A' →φ A → S^{-1}A se factorise en'",
      "inline: 'composé A' →(φ) A → S^{-1}A se factorise en ...' (same line)",
      r"displayed: \[ A'\xrightarrow{\varphi}A\longrightarrow S^{-1}A \]",
      "other", "high",
      L(r"\[", r"  A'\xrightarrow{\varphi}A\longrightarrow S^{-1}A", r"\]"),
      r"$A'\xrightarrow{\varphi}A\longrightarrow S^{-1}A$",
      INLINE),
    F(17, "(1.5.1), 'se factorise en A' → S'^{-1}A' →φ^{S'} S^{-1}A en vertu de (1.2.4)'",
      "inline: 'se factorise en A' → S'^{-1}A' →(φ^{S'}) S^{-1}A en vertu de (1.2.4) ;'",
      r"displayed: \[ A'\longrightarrow S'^{-1}A'\xrightarrow{\varphi^{S'}}S^{-1}A \]",
      "other", "high",
      L(r"\[", r"  A'\longrightarrow S'^{-1}A'\xrightarrow{\varphi^{S'}}S^{-1}A", r"\]"),
      r"$A'\longrightarrow S'^{-1}A'\xrightarrow{\varphi^{S'}}S^{-1}A$",
      INLINE),
    F(17, "(1.5.2), 'Lorsque S=φ(S'), l'homomorphisme σ est bijectif.'",
      "'Lorsque' is printed italic (like 'bijectif'); the following 'Lorsque A'=A' is roman",
      "'Lorsque' upright",
      "italics", "high",
      r"Lorsque $S=\varphi(S')$", r"\emph{Lorsque} $S=\varphi(S')$",
      "Printed italic word left upright. The italic may be an unintended face change in the print; the "
      "diplomatic text follows the print either way."),
    F(17, "(1.5.2), second paragraph, 'et l'homomorphisme σ : S'^{-1}(A_{[φ]}) → S^{-1}A est un homomorphisme'",
      "inline: '... et l'homomorphisme σ : S'^{-1}(A_{[φ]}) → S^{-1}A est un homomorphisme de S'^{-1}A'-algèbres.'",
      r"displayed: \[ \sigma:S'^{-1}(A_{[\varphi]})\longrightarrow S^{-1}A \]",
      "other", "high",
      L(r"\[", r"  \sigma:S'^{-1}(A_{[\varphi]})\longrightarrow S^{-1}A", r"\]"),
      r"$\sigma:S'^{-1}(A_{[\varphi]})\longrightarrow S^{-1}A$",
      INLINE),
    F(17, "(1.5.4), 'en posant a.(n'⊗b)=n'⊗(ab).'",
      "inline at the end of the line: 'en posant a.(n'⊗b)=n'⊗(ab).'",
      r"displayed: \[ a.(n'\otimes b)=n'\otimes(ab). \]",
      "other", "high",
      L(r"\[", r"  a.(n'\otimes b)=n'\otimes(ab).", r"\]"),
      r"$a.(n'\otimes b)=n'\otimes(ab)$.",
      INLINE),
    # ---------------- page 18 ----------------
    F(18, "(1.5.4), last line, 'l'homomorphisme composé a'→φ(a')/1 de A' dans S^{-1}A'",
      "plain arrow: a'→φ(a')/1",
      r"a'\mapsto\varphi(a')/1",
      "convention", "high",
      r"$a'\mapsto\varphi(a')/1$", r"$a'\to\varphi(a')/1$",
      "", convention=3),
    # ---------------- page 19 ----------------
    F(19, "(1.5.7), after the display φ''^{S''}=φ^{S'}∘φ'^{S''}: 'Soit M un A-module ; on a évidemment'",
      "new paragraph (first line indented)",
      r"no blank line after \]: the text continues the paragraph",
      "other", "high",
      L(r"\]", r"Soit $M$ un $A$-module"), L(r"\]", "", r"Soit $M$ un $A$-module"),
      "Missing paragraph break."),
    F(19, "(1.5.7), after the display σ''=σ∘σ': 'Enfin, soit N'' un A''-module'",
      "new paragraph (first line indented)",
      r"no blank line after \]: the text continues the paragraph",
      "other", "high",
      L(r"\]", r"Enfin, soit $N''$"), L(r"\]", "", r"Enfin, soit $N''$"),
      "Missing paragraph break."),
    F(19, "(1.5.7), 's'identifie canoniquement à (N''⊗_{A''}A'_{[φ']})⊗_{A'}A_{[φ]}, et de même'",
      "inline: '... s'identifie canoniquement à (N''⊗_{A''}A'_{[φ']})⊗_{A'}A_{[φ]}, et de même, le S^{-1}A-module ...'",
      r"displayed: \[ (N''\otimes_{A''}A'_{[\varphi']})\otimes_{A'}A_{[\varphi]}, \]",
      "other", "high",
      L(r"\[", r"  (N''\otimes_{A''}A'_{[\varphi']})\otimes_{A'}A_{[\varphi]},", r"\]"),
      r"$(N''\otimes_{A''}A'_{[\varphi']})\otimes_{A'}A_{[\varphi]}$,",
      INLINE),
    F(19, "(1.5.7), 'le S^{-1}A-module (S''^{-1}N'')⊗_{S''^{-1}A''}(S^{-1}A)_{[φ''^{S''}]} s'identifie'",
      "inline: 'le S^{-1}A-module (S''^{-1}N'')⊗_{S''^{-1}A''}(S^{-1}A)_{[φ''^{S''}]} s'iden-tifie canoniquement à'",
      r"displayed: \[ (S''^{-1}N'')\otimes_{S''^{-1}A''}(S^{-1}A)_{[\varphi''^{S''}]} \]",
      "other", "high",
      L(r"\[", r"  (S''^{-1}N'')\otimes_{S''^{-1}A''}", r"  (S^{-1}A)_{[\varphi''^{S''}]}", r"\]"),
      r"$(S''^{-1}N'')\otimes_{S''^{-1}A''}(S^{-1}A)_{[\varphi''^{S''}]}$",
      INLINE),
    F(19, "(1.5.7), 's'identifie canoniquement à ((S''^{-1}N'')⊗…(S'^{-1}A')_{[φ'^{S''}]})⊗_{S'^{-1}A'}"
          "(S^{-1}A)_{[φ^{S'}]}. Avec ces identifications'",
      "inline: '... à ((S''^{-1}N'')⊗_{S''^{-1}A''}(S'^{-1}A')_{[φ'^{S''}]})⊗_{S'^{-1}A'}(S^{-1}A)_{[φ^{S'}]}. "
      "Avec ces identi-fications' (ordinary parentheses)",
      r"displayed: \[ \bigl((S''^{-1}N'')\otimes...\bigr)\otimes_{S'^{-1}A'}(S^{-1}A)_{[\varphi^{S'}]}. \]",
      "other", "high",
      L(r"\[", r"  \bigl((S''^{-1}N'')\otimes_{S''^{-1}A''}", r"  (S'^{-1}A')_{[\varphi'^{S''}]}\bigr)",
        r"  \otimes_{S'^{-1}A'}(S^{-1}A)_{[\varphi^{S'}]}.", r"\]"),
      r"$((S''^{-1}N'')\otimes_{S''^{-1}A''}(S'^{-1}A')_{[\varphi'^{S''}]})\otimes_{S'^{-1}A'}(S^{-1}A)_{[\varphi^{S'}]}$.",
      INLINE),
    F(19, "(1.5.8), 'et possède un seul idéal premier 𝔭' (1.2.6)'",
      "'un seul' is italic",
      "'un seul' upright",
      "italics", "high",
      r"un seul idéal premier", r"\emph{un seul} idéal premier",
      "Printed italic words left upright."),
    F(19, "(1.6.1), 'soit φ_{nm} l'homomorphisme z→f^{n−m}z de M_m dans M_n'",
      "plain arrow: z→f^{n−m}z",
      r"z\mapsto f^{n-m}z",
      "convention", "high",
      r"$z\mapsto f^{n-m}z$", r"$z\to f^{n-m}z$",
      "", convention=3),
    F(19, "(1.6.1), 'pour tout n, θ_n : z→z/f^n est un A-homomorphisme'",
      "plain arrow: θ_n : z→z/f^n",
      r"\theta_n:z\mapsto z/f^n",
      "convention", "high",
      r"$\theta_n:z\mapsto z/f^n$", r"$\theta_n:z\to z/f^n$",
      "", convention=3),
    F(19, "(1.6.1), 'est un A-homomorphisme de M=M_n dans M_f'",
      "M=M_ı: the subscript is an italic dotless i (no dot visible; narrower than the italic n of the other M_n "
      "on the page), not n",
      "M=M_n",
      "misprint_in_print", "medium",
      r"$M=M_n$", r"$M=M_{\imath}$",
      "The TeX silently corrects the printed subscript. The glyph is complete (entry serif, exit hook) in a "
      r"well-inked part of the line, so a wrong sort (i without its dot) is likelier than a broken n; M_i is an "
      "alternative transcription of the same reading.",
      corrected=r"M=M_n"),
    F(19, "end of the page: blank line after the (1.6.2) display '... (1.4.1 et 1.4.3) ;', before \\oldpage{20}",
      "the sentence continues on p. 20 ('si on identifie ...') without a new paragraph",
      r"'(1.4.1 et 1.4.3)};' \] followed by a blank line",
      "other", "medium",
      L(r"(1.4.1 et 1.4.3)};", r"\]", "", ""), L(r"(1.4.1 et 1.4.3)};", r"\]", ""),
      "Spurious paragraph break at the page boundary; apply together with the p. 20 finding that removes the "
      r"blank line after \oldpage[0\textsubscript{I}]{20}."),
    # ---------------- page 20 ----------------
    F(20, "top of the page, 'si on identifie M_f et M_{fg} à lim M_{f,n} …' (continuation of (1.6.2))",
      "continues the sentence of (1.6.2) from p. 19; first line not indented, no new paragraph",
      r"blank lines before and after \oldpage{20}: 'si on identifie' starts a new indented paragraph",
      "other", "medium",
      L(r"\oldpage[0\textsubscript{I}]{20}", "", r"si on identifie"),
      L(r"\oldpage[0\textsubscript{I}]{20}", r"si on identifie"),
      "Spurious paragraph break; apply together with the p. 19 finding that removes the blank line before "
      "the marker (both blank lines must go)."),
    F(20, "(1.6.2), diagram, bottom right 'M_{fg}'",
      "no full stop after M_{fg}",
      "M_{fg}.",
      "punctuation", "high",
      r"& M_{fg}.", r"& M_{fg}",
      "Extra full stop in the TeX diagram."),
    F(20, "(1.7.3), 'donc Supp(M)=⋃_λ Supp(M_λ).'",
      "inline at the end of the line: '(1.3.3 et 1.3.2), donc Supp(M)=⋃_λ Supp(M_λ).'",
      r"displayed: \[ \operatorname{Supp}(M)=\bigcup_\lambda\operatorname{Supp}(M_\lambda). \]",
      "other", "high",
      L(r"\[", r"  \operatorname{Supp}(M)=\bigcup_\lambda\operatorname{Supp}(M_\lambda).", r"\]"),
      r"$\operatorname{Supp}(M)=\bigcup_\lambda\operatorname{Supp}(M_\lambda)$.",
      INLINE),
    F(20, "(1.7.5), 'leur produit tensoriel (P/𝔪P)⊗_{B/𝔪}(Q/𝔪Q)=(P⊗_BQ)⊗_B(B/𝔪), d'où la conclusion.'",
      "inline: 'de leur produit tensoriel (P/𝔪P)⊗_{B/𝔪}(Q/𝔪Q)=(P⊗_BQ)⊗_B(B/𝔪), d'où la conclusion.'",
      r"displayed: \[ (P/\mathfrak mP)\otimes_{B/\mathfrak m}(Q/\mathfrak mQ)=(P\otimes_B Q)\otimes_B(B/\mathfrak m), \]",
      "other", "high",
      L(r"\[", r"  (P/\mathfrak mP)\otimes_{B/\mathfrak m}(Q/\mathfrak mQ)",
        r"  =(P\otimes_B Q)\otimes_B(B/\mathfrak m),", r"\]"),
      r"$(P/\mathfrak mP)\otimes_{B/\mathfrak m}(Q/\mathfrak mQ)=(P\otimes_B Q)\otimes_B(B/\mathfrak m)$,",
      INLINE),
]

src = SRC.read_text(encoding="utf-8").replace("\r\n", "\n")
ok = True
for d in findings:
    fp = d.pop("_fix_page")
    if d["fix"] is None:
        continue
    old = d["fix"]["old"]
    page_text = (RUN / f"page_{fp:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    n_page, n_src = page_text.count(old), src.count(old)
    status = "OK" if n_page == 1 and n_src == 1 else "CHECK"
    if status != "OK":
        ok = False
    print(f"p{d['page']} (fix in page_{fp:03d}) page:{n_page} src:{n_src} {status} | {old[:60]!r}")
    if d["note"] == "":
        d["note"] = None

OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", OUT, len(findings), "findings; all unique:", ok)
