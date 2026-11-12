import json
import os
import sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, "findings_005_009.json")
NL = "\n"


def F(page, where, scan, tex, kind, old, new, note="", convention=None,
      confidence="high"):
    d = {"page": page, "where": where, "scan": scan, "tex": tex,
         "kind": kind, "convention": convention, "confidence": confidence,
         "fix": None if old is None else {"old": old, "new": new},
         "note": note}
    return d


def boldC(page, where, old, new, n):
    return F(page, where,
             "category letter C bold italic (enlarged crop)" if n == 1 else
             f"category letter C bold italic, {n} times (enlarged crop)",
             r"\mathbf C (bold upright)", "font", old, new,
             "The category C of (8.2.4)-(8.2.6) is bold italic in the print, in the italic "
             "statements and in the roman proof alike; the TeX has \\mathbf C. Same form as "
             "the earlier \\boldsymbol page fixes (GLOBAL_ISSUES 33/35/44).")


findings = [
    # ---------------- page 5 ----------------
    F(5, "chapter heading",
      "CHAPITRE IV (suite): 'suite' italic, its parentheses italic (slanted)",
      r"{\large CHAPITRE IV (suite)\par}, all upright", "italics",
      r"CHAPITRE IV (suite)", r"CHAPITRE IV \textit{(suite)}",
      "Enlarged crop; same form as the IV-1 and IV-2 p. 5 fixes."),
    F(5, "subsection heading 8.1",
      "'8.1. Introduction.' (final full stop)",
      r"\subsection{Introduction} (no full stop)", "punctuation",
      r"\subsection{Introduction}", r"\subsection{Introduction.}",
      "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop); same fix as IV-2 p. 5."),
    F(5, "(8.1.1), l. 9: 'pour que X possède une propriété P (par exemple'",
      "bold italic P (enlarged crop)",
      "$P$ (plain italic)", "font",
      r"une propriété $P$ (par", r"une propriété $\boldsymbol{P}$ (par",
      "Property letter P. The TeX has plain $P$, not \\mathbf{P}, so this is not convention 10; "
      "form of the earlier \\boldsymbol{P} page fixes (GLOBAL_ISSUES 13/44)."),
    F(5, "(8.1.1), l. 12: 'la même propriété P. Nous obtiendrons'",
      "bold italic P (enlarged crop)",
      "$P$ (plain italic)", "font",
      r"même propriété $P$.", r"même propriété $\boldsymbol{P}$.",
      "As the previous finding."),
    F(5, "(8.1.2) a), last lines: 'où f parcourt A_α—p_α (pour un α fixé)'",
      "long dash for the set difference A_α—p_α",
      r"$A_\alpha-\mathfrak p_\alpha$", "convention",
      r"$A_\alpha-\mathfrak p_\alpha$", r"$A_\alpha\setmin\mathfrak p_\alpha$",
      "\\setmin pending the convention-7 decision (FIX_POLICY 2.7).", convention=7),
    # ---------------- page 6 ----------------
    F(6, "(8.1.2) a), paragraph 'Un cas particulièrement important': '... de A); cf. (I, 3.7)).'",
      "(𝐈, 3.7): bold I",
      "cf. (I, 3.7)", "convention",
      r"cf. (I, 3.7)", r"cf. (\textbf{I}, 3.7)", "", convention=2),
    F(6, "(8.1.2) c): 'C'est là l'explicitation du « point de vue kroneckérien »'",
      "kroneckérien, with é (enlarged crop)",
      "kroneckerien", "word",
      r"kroneckerien", r"kroneckérien", ""),
    F(6, "(8.1.2) c): 'des Z-algèbres de type fini, ce qui permet'",
      "'algèbres de type fini' all italic after the bold Z and the hyphen (enlarged crop)",
      r"$\mathbf Z$-algèbres \emph{de type fini}: 'algèbres' upright", "italics",
      r"$\mathbf Z$-algèbres \emph{de type fini}", r"$\mathbf Z$-\emph{algèbres de type fini}",
      ""),
    # ---------------- page 7 ----------------
    F(7, "subsection heading 8.2",
      "'8.2. Limites projectives de préschémas.' (final full stop)",
      r"\subsection{Limites projectives de préschémas} (no full stop)", "punctuation",
      r"\subsection{Limites projectives de préschémas}",
      r"\subsection{Limites projectives de préschémas.}",
      "GLOBAL_ISSUES 43/58; same fix as IV-2 p. 5."),
    # ---------------- page 8 ----------------
    F(8, "display (8.2.1.1), left side: 'Hom_{S_0-Alg.}(𝒜, ℬ)'",
      "subscript S_0-Alg. (no 𝒪; enlarged crop)",
      r"\operatorname{Hom}_{\mathcal O_{S_0}\text{-Alg.}}", "formula",
      r"\operatorname{Hom}_{\mathcal O_{S_0}\text{-Alg.}}(\mathscr A,\mathscr B)" + NL + r"\longrightarrow",
      r"\operatorname{Hom}_{S_0\text{-Alg.}}(\mathscr A,\mathscr B)" + NL + r"\longrightarrow",
      "The print writes Hom_{S_0-Alg.} / Hom_{S_0-Mod.} at all four places on this page; "
      "the TeX normalises them to 𝒪_{S_0}. Consistent notation, not a misprint."),
    F(8, "display (8.2.1.1), right side: 'lim← Hom_{S_0-Alg.}(𝒜_λ, ℬ)'",
      "subscript S_0-Alg. (no 𝒪)",
      r"\operatorname{Hom}_{\mathcal O_{S_0}\text{-Alg.}}", "formula",
      r"\operatorname{Hom}_{\mathcal O_{S_0}\text{-Alg.}}" + NL + r"(\mathscr A_\lambda",
      r"\operatorname{Hom}_{S_0\text{-Alg.}}" + NL + r"(\mathscr A_\lambda", ""),
    F(8, "after (8.2.1.1): 'identifie Hom_{S_0-Alg.}(𝒜, ℬ) à une partie de'",
      "subscript S_0-Alg. (no 𝒪; enlarged crop)",
      r"\operatorname{Hom}_{\mathcal O_{S_0}\text{-Alg.}}", "formula",
      r"$\operatorname{Hom}_{\mathcal O_{S_0}\text{-Alg.}}(\mathscr A,\mathscr B)$",
      r"$\operatorname{Hom}_{S_0\text{-Alg.}}(\mathscr A,\mathscr B)$", ""),
    F(8, "after (8.2.1.1): 'une partie de lim← Hom_{S_0-Mod.}(𝒜_λ, ℬ)'",
      "subscript S_0-Mod. (no 𝒪; enlarged crop)",
      r"\operatorname{Hom}_{\mathcal O_{S_0}\text{-Mod.}}", "formula",
      r"\operatorname{Hom}_{\mathcal O_{S_0}\text{-Mod.}}",
      r"\operatorname{Hom}_{S_0\text{-Mod.}}", ""),
    F(8, "(8.2.1): 'est aussi un homomorphisme de 𝒪_{S_0}-Algèbres; mais cela'",
      "'Algèbres' italic, like 'Modules' just before (enlarged crop)",
      r"$\mathcal O_{S_0}$-Algèbres~; with 'Algèbres' upright", "italics",
      r"$\mathcal O_{S_0}$-Algèbres~; mais cela",
      r"$\mathcal O_{S_0}$-\emph{Algèbres}~; mais cela", ""),
    F(8, "(8.2.2): 'une 𝒪_{S_0}-Algèbre quasi-cohérente (I, 4.1.1)'",
      "(𝐈, 4.1.1): bold I", "(I, 4.1.1)", "convention",
      r"(I, 4.1.1)", r"(\textbf{I}, 4.1.1)", "", convention=2),
    F(8, "(8.2.2): '(resp. 𝒜) (II, 1.3.1), et soient'",
      "(𝐈𝐈, 1.3.1): bold II", "(II, 1.3.1)", "convention",
      r"(II, 1.3.1)", r"(\textbf{II}, 1.3.1)", "", convention=2),
    F(8, "(8.2.2): 'respectivement (II, 1.2.7); il est clair'",
      "(𝐈𝐈, 1.2.7): bold II", "(II, 1.2.7)", "convention",
      r"(II, 1.2.7)", r"(\textbf{II}, 1.2.7)", "", convention=2),
    F(8, "(8.2.2): 'des morphismes affines (II, 1.6.2), donc'",
      "(𝐈𝐈, 1.6.2): bold II", "(II, 1.6.2)", "convention",
      r"(II, 1.6.2)", r"(\textbf{II}, 1.6.2)", "", convention=2),
    F(8, "Proposition (8.2.3): 'Avec les notations de (8.2.2), les morphismes'",
      "the reference (8.2.2) is upright inside the italic statement (enlarged crop)",
      "(8.2.2) inside the italic proposition environment: italic", "convention",
      r"Avec les notations de (8.2.2)", r"Avec les notations de \textup{(8.2.2)}",
      "", convention=6),
    F(8, "page break 8/9: 'Prouvons d'abord ... dans le cas T=S_0.' / p. 9 'Tout revient à démontrer'",
      "'Tout revient à démontrer' opens p. 9 with a paragraph indent: new paragraph",
      r"'... $T=S_0$.' then \oldpage[IV-3]{9} and 'Tout revient' with no blank line (same paragraph)",
      "other",
      r"dans le cas $T=S_0$.", r"dans le cas $T=S_0$." + NL,
      "Missing paragraph break. The edit leaves a blank line before \\oldpage[IV-3]{9}, so the "
      "marker opens the new paragraph, as at the other paragraph-initial markers of ega4-8."),
    # ---------------- page 9 ----------------
    F(9, "after (8.2.3.1): 's'identifie canoniquement à (8.2.1.1) (II, 1.2.7), et'",
      "(𝐈𝐈, 1.2.7): bold II", "(II, 1.2.7)", "convention",
      r"(II, 1.2.7)", r"(\textbf{II}, 1.2.7)", "", convention=2),
    boldC(9, "Lemme (8.2.4), l. 1: 'Soient C une catégorie, T un objet de C,'",
          r"Soient $\mathbf C$ une catégorie, $T$ un objet de $\mathbf C$,",
          r"Soient $\boldsymbol{C}$ une catégorie, $T$ un objet de $\boldsymbol{C}$,", 2),
    boldC(9, "Lemme (8.2.4), l. 1-2: 'C_T la sous-catégorie des objets de C au-dessus de T.'",
          r"$\mathbf C_T$ la sous-catégorie des objets de $\mathbf C$ au-dessus de $T$.",
          r"$\boldsymbol{C}_T$ la sous-catégorie des objets de $\boldsymbol{C}$ au-dessus de $T$.", 2),
    boldC(9, "Lemme (8.2.4), l. 2: 'un système projectif dans C_T;'",
          r"un système projectif dans $\mathbf C_T$~;",
          r"un système projectif dans $\boldsymbol{C}_T$~;", 1),
    boldC(9, "Lemme (8.2.4), l. 3: 'de ce système dans C_T est aussi'",
          r"ce système dans $\mathbf C_T$ est aussi",
          r"ce système dans $\boldsymbol{C}_T$ est aussi", 1),
    boldC(9, "Lemme (8.2.4), l. 3: 'limite projective dans C, et réciproquement.'",
          r"limite projective dans $\mathbf C$, et réciproquement.",
          r"limite projective dans $\boldsymbol{C}$, et réciproquement.", 1),
    boldC(9, "proof of (8.2.4): 'de (S_λ, u_λμ) dans C, et désignons'",
          r"dans $\mathbf C$, et" + NL + "désignons",
          r"dans $\boldsymbol{C}$, et" + NL + "désignons", 1),
    boldC(9, "proof of (8.2.4): 'où Y∈C_T.'",
          r"où $Y\in\mathbf C_T$.",
          r"où $Y\in\boldsymbol{C}_T$.", 1),
    boldC(9, "proof of (8.2.4): 'un morphisme unique (dans C) w : Y→S'",
          r"unique (dans $\mathbf C$)",
          r"unique (dans $\boldsymbol{C}$)", 1),
    boldC(9, "proof of (8.2.4): 'de (S_λ, u_λμ) dans C_T, et considérons'",
          r"dans $\mathbf C_T$, et considérons",
          r"dans $\boldsymbol{C}_T$, et considérons", 1),
    boldC(9, "proof of (8.2.4): 'système projectif de morphismes (de C) w_λ'",
          r"(de $\mathbf C$)",
          r"(de $\boldsymbol{C}$)", 1),
    F(9, "proof of (8.2.4): 'f_λ∘w_λ = f_λ∘u_λν∘w_ν = f_ν∘w_ν et on voit de même que'",
      "no comma before 'et on voit' (enlarged crop)",
      r"=f_\nu\circ w_\nu$, et on voit", "punctuation",
      r"=f_\nu\circ w_\nu$, et on voit", r"=f_\nu\circ w_\nu$ et on voit", ""),
    boldC(9, "proof of (8.2.4): 'et a fortiori un morphisme de C;'",
          r"morphisme de $\mathbf C$~;",
          r"morphisme de $\boldsymbol{C}$~;", 1),
    boldC(9, "proof of (8.2.4): 'toute limite projective w' (dans C)'",
          r"$w'$ (dans $\mathbf C$)",
          r"$w'$ (dans $\boldsymbol{C}$)", 1),
    F(9, "Proposition (8.2.5): 'Sous les conditions de (8.2.2), soient'",
      "the reference (8.2.2) is upright inside the italic statement (enlarged crop)",
      "(8.2.2) inside the italic proposition environment: italic", "convention",
      r"Sous les conditions de (8.2.2)", r"Sous les conditions de \textup{(8.2.2)}",
      "", convention=6),
    boldC(9, "Lemme (8.2.6), l. 1: 'Soient C une catégorie dans laquelle'",
          r"Soient $\mathbf C$ une catégorie dans laquelle",
          r"Soient $\boldsymbol{C}$ une catégorie dans laquelle", 1),
    boldC(9, "Lemme (8.2.6), l. 2: 'q : T'→T un morphisme de C, C_T'",
          r"un morphisme de $\mathbf C$, $\mathbf C_T$",
          r"un morphisme de $\boldsymbol{C}$, $\boldsymbol{C}_T$", 2),
    F(9, "Lemme (8.2.6), l. 2: 'C_T (resp. C_T') la catégorie'",
      "'resp.' and its parenthesis upright inside the italic statement (enlarged crop)",
      "(resp. inside the italic lemma environment: italic", "convention",
      r"(resp.", r"(\textup{resp.}",
      "Does not overlap the neighbouring \\boldsymbol fixes.", convention=6),
    boldC(9, "Lemme (8.2.6), l. 2: 'C_T') la catégorie des objets de C au-dessus'",
          r"$\mathbf C_{T'}$) la catégorie des objets de $\mathbf C$ au-dessus",
          r"$\boldsymbol{C}_{T'}$) la catégorie des objets de $\boldsymbol{C}$ au-dessus", 2),
]

# ---- checks: every old occurs exactly once; sequential application keeps working ----
ok = True
texts = {}
for f in findings:
    p = f["page"]
    if p not in texts:
        with open(os.path.join(RUN, f"page_{p:03d}.tex"), encoding="utf-8") as fh:
            texts[p] = fh.read()  # universal newlines: CRLF -> LF, as in the release files
# the same check against the source segments (LF) of ega4-8-fr.tex
SRC = os.path.join(os.path.dirname(RUN), "ega-fr", "source", "ega4", "ega4-8-fr.tex")
with open(SRC, encoding="utf-8", newline="") as fh:
    src = fh.read()
for f in findings:
    if f["fix"] is None:
        continue
    p = f["page"]
    a = src.index("\\oldpage[IV-3]{%d}" % p)
    b = src.index("\\oldpage[IV-3]{%d}" % (p + 1))
    n = src[a:b].count(f["fix"]["old"])
    if n != 1:
        print("SOURCE SEGMENT COUNT", p, n, repr(f["fix"]["old"]))
for f in findings:
    if f["fix"] is None:
        continue
    n = texts[f["page"]].count(f["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", f["page"], n, repr(f["fix"]["old"]))
work = dict(texts)
for f in findings:
    if f["fix"] is None:
        continue
    p = f["page"]
    n = work[p].count(f["fix"]["old"])
    if n != 1:
        ok = False
        print("SEQUENTIAL FAIL", p, n, repr(f["fix"]["old"]))
        continue
    work[p] = work[p].replace(f["fix"]["old"], f["fix"]["new"], 1)
for p, t in texts.items():
    if "\r" in t:
        print("CR found in", p)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
cnt = Counter()
for f in findings:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    cnt[(f["page"], k)] += 1
for p in sorted({f["page"] for f in findings} | {5, 6, 7, 8, 9}):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("checks ok" if ok else "CHECKS FAILED", len(findings), "findings ->", OUT)
