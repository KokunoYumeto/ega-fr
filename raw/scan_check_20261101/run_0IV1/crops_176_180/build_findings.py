import json, sys

RUN = r"user/Documents/ega_scan_check_20261101/run_0IV1"
OUT = RUN + "/findings_176_180.json"
NL = "\n"

pages = {}
for n in range(176, 181):
    pages[n] = open(f"{RUN}/page_{n}.tex", "rb").read().decode("utf-8").replace("\r\n", "\n")

# the p. 176 marker move, copied verbatim from the p. 171-175 batch so the two are identical
marker176 = None
for x in json.load(open(f"{RUN}/findings_171_175.json", encoding="utf-8")):
    if x.get("kind") == "marker" and x.get("fix") and "{176}" in x["fix"]["old"]:
        marker176 = x["fix"]
assert marker176 is not None

C7 = r"Long dash used for a subtraction (GLOBAL_ISSUES 23); \setmin as in the earlier fixes, pending the convention-7 decision (FIX_POLICY 2.7)."
PARA = "Paragraph break the print has (the next line is indented) and the TeX lacks (no blank line after the display; GLOBAL_ISSUES 47 pattern)."

def F(page, where, scan, tex, kind, conv, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d

def fx(old, new):
    return {"old": old, "new": new}

findings = [
# ---------------- p. 176 ----------------
F(176, "page break inside the proof of (21.8.8.3): '... g∈k_γ[[T_1, ..., T_r]] tel | que gf∈k_γ[[T_1, ..., T_r]] ;'",
  "p. 176 begins 'que gf∈k_γ[[T_1, ..., T_r]] ; quitte à remplacer g par g^q'; 'Il suffit de prouver ... Soient γ un indice, g∈k_γ[[T_1, ..., T_r]] tel' are the last two lines of p. 175 (p. 175 strip 4 checked)",
  r"\oldpage[0\textsubscript{IV-1}]{176} stands right after \begin{proof}, before 'Il suffit de prouver'",
  "marker", None, "high", marker176,
  "One edit inside the p. 176 segment that moves the marker down three lines. Identical to the p. 175 marker finding in findings_171_175.json: apply only one of the two."),
F(176, "end of Proposition (21.9.2): '... est un A-module libre de rang égal à dim(A)+deg. tr_{k_0}K+rg_{k_0}(Ω^1_{k_0/k}).'",
  "the formula is in the running text, on the same line as 'est un A-module libre de rang égal à'",
  r"set as a display \[ ... \]",
  "other", None, "high",
  fx(r"égal à" + NL + r"\[" + NL + r"  \dim(A)+\deg.\operatorname{tr}_{k_0}K" + NL + r"  +\operatorname{rg}_{k_0}(\Omega^1_{k_0/k})." + NL + r"\]",
     r"égal à" + NL + r"$\dim(A)+\deg.\operatorname{tr}_{k_0}K+\operatorname{rg}_{k_0}(\Omega^1_{k_0/k})$."),
  "Display the print sets inline (GLOBAL_ISSUES 21); no connecting word lost or added."),
F(176, "proof of (21.9.2): the exact sequence obtained from (20.6.22.1), first term",
  "0→Υ_{K/k_0}→𝔪/𝔪²→Ω^1_{A/k_0}⊗_A K→Ω^1_{K/k_0}→0 (crop: subscript K/k_0, no superscript)",
  r"0\longrightarrow \Upsilon^K_{A/k_0}\longrightarrow \mathfrak m/\mathfrak m^2 ...",
  "formula", None, "high",
  fx(r"0\longrightarrow \Upsilon^K_{A/k_0}", r"0\longrightarrow \Upsilon_{K/k_0}"),
  "The printed reading is right: (20.6.22.1) with Λ, A, B, C replaced by P, k_0, A, K gives 0→Υ^K_{A/k_0/P}→Υ_{K/k_0/P}→𝔪/𝔪²→..., Υ^K_{A/k_0/P}=0 was just shown, and the next formula uses rg_K(Υ_{K/k_0})."),
F(176, "proof of (21.9.2): end of the same exact sequence '... → Ω^1_{K/k_0} → 0'",
  "no punctuation after the final 0 (crop of the whole line)",
  r"\Omega^1_{K/k_0}\longrightarrow0,",
  "punctuation", None, "high",
  fx(r"\Omega^1_{K/k_0}\longrightarrow0,", r"\Omega^1_{K/k_0}\longrightarrow0"), ""),
F(176, "proof of (21.9.2), rank formula: '(rg_K(Ω^1_{K/k_0}) — rg_K(Υ_{K/k_0}))'",
  "long dash for the subtraction (crop: longer than the + signs on the same line)",
  r"-\operatorname{rg}_K(\Upsilon_{K/k_0})",
  "convention", 7, "high",
  fx(r"-\operatorname{rg}_K(\Upsilon_{K/k_0})", r"\setmin\operatorname{rg}_K(\Upsilon_{K/k_0})"),
  C7),
F(176, "proof of (21.9.2): 'D'autre part, Ω^1_{A/k_0} est un A-module formellement projectif (20.4.9)'",
  "Ω^1_{A/k_0} without a hat (crop)",
  r"$\widehat\Omega^1_{A/k_0}$",
  "formula", None, "high",
  fx(r"D'autre part, $\widehat\Omega^1_{A/k_0}$ est un", r"D'autre part, $\Omega^1_{A/k_0}$ est un"),
  "Not a misprint: (20.4.9) and (20.4.5), cited in this sentence, are statements about the uncompleted Ω^1_{B/A} (formally projective; its topology)."),
F(176, "proof of (21.9.2): 'Ω^1_{A/k_0}/𝔪^{j+1}Ω^1_{A/k_0} est un (A/𝔪^{j+1})-module projectif'",
  "both Ω without a hat (crop)",
  r"$\widehat\Omega^1_{A/k_0}/\mathfrak m^{j+1}\widehat\Omega^1_{A/k_0}$",
  "formula", None, "high",
  fx(r"$\widehat\Omega^1_{A/k_0}/\mathfrak m^{j+1}\widehat\Omega^1_{A/k_0}$", r"$\Omega^1_{A/k_0}/\mathfrak m^{j+1}\Omega^1_{A/k_0}$"),
  "Same as the previous finding (the quotient by 𝔪^{j+1} is the same for Ω and its completion)."),
F(176, "last line of p. 176: '... donc libre (0_III, 10.1.2) et de rang | n=rg_K(...)'; the sentence continues on p. 177",
  "p. 177 begins at the left margin with 'n=rg_K(Ω^1_{A/k_0}⊗_A K).': no paragraph break",
  r"blank line before \oldpage[0\textsubscript{IV-1}]{177}",
  "other", None, "high",
  fx(r"10.1.2) et de rang" + NL + NL, r"10.1.2) et de rang" + NL),
  "Spurious paragraph break mid-sentence (GLOBAL_ISSUES 20); the blank line is the last line of the p. 176 segment."),
# ---------------- p. 177 ----------------
F(177, "proof of (21.9.2), second part: 'le produit tensoriel complété Ω̂^1_{k_0/k}⊗̂_{k_0}A s'identifie à Ω^1_{k_0/k}⊗_{k_0}A'",
  "hat over the first Ω (and over ⊗); the second Ω has none (crop)",
  r"$\Omega^1_{k_0/k}\widehat\otimes_{k_0}A$",
  "formula", None, "high",
  fx(r"$\Omega^1_{k_0/k}\widehat\otimes_{k_0}A$", r"$\widehat\Omega^1_{k_0/k}\widehat\otimes_{k_0}A$"),
  ""),
F(177, "proof of (21.9.2): 'ce qui implique en particulier que son image est fermée dans Ω̂^1_{A/k}'",
  "fermée italic (crop)", "fermée upright",
  "italics", None, "high",
  fx(r"son image est fermée dans", r"son image est \emph{fermée} dans"),
  ""),
F(177, "proof of (21.9.2): 'la suite exacte ... est donc exacte et scindée en vertu de (20.7.17)'",
  "exacte et scindée italic (crop)", "upright",
  "italics", None, "high",
  fx(r"est donc exacte et scindée", r"est donc \emph{exacte et scindée}"),
  ""),
F(177, "Proposition (21.9.5): 'tel que A soit une A_0-algèbre finie et que ...'",
  "finie upright inside the italic statement (crop)", "finie italic (statement environment)",
  "convention", 6, "high",
  fx(r"$A_0$-algèbre finie et que", r"$A_0$-algèbre \textup{finie} et que"),
  r"FIX_POLICY 2.6 (\textup); \emph would give the same output."),
F(177, "Proposition (21.9.5): '... soit une extension séparable du corps des fractions L_0 de A_0'",
  "séparable upright inside the italic statement (crop)", "séparable italic (statement environment)",
  "convention", 6, "high",
  fx(r"extension séparable du corps", r"extension \textup{séparable} du corps"),
  r"FIX_POLICY 2.6 (\textup); \emph would give the same output."),
F(177, "last line of p. 177: 'On sait (21.9.1) que Ω̂^1_{A/k} est un A-module de type fini et, | en vertu de (21.9.3) ...'",
  "p. 178 begins at the left margin with 'en vertu de (21.9.3)': no paragraph break",
  r"blank line before \oldpage[0\textsubscript{IV-1}]{178}",
  "other", None, "high",
  fx(r"de type fini et," + NL + NL, r"de type fini et," + NL),
  "Spurious paragraph break mid-sentence (GLOBAL_ISSUES 20); the blank line is the last line of the p. 177 segment."),
# ---------------- p. 178 ----------------
F(178, "proof of (21.9.5), first line: 'Ω̂^1_{A_0/k} est un A_0-module libre de rang r=dim(A_0)=dim(A)'",
  "libre italic (crop)", "upright",
  "italics", None, "high",
  fx(r"$A_0$-module libre de", r"$A_0$-module \emph{libre} de"),
  "The second 'libre' two lines below is upright in the print, as in the TeX."),
F(178, "proof of (21.9.5): 'enfin Ω^1_{A/A_0} est un A-module de type fini (20.4.7), donc identique à son séparé complété'",
  "Ω^1_{A/A_0} without a hat (crop)", r"$\widehat\Omega^1_{A/A_0}$",
  "formula", None, "high",
  fx(r"enfin $\widehat\Omega^1_{A/A_0}$", r"enfin $\Omega^1_{A/A_0}$"),
  "Not a misprint: the sentence says that the uncompleted Ω^1_{A/A_0} (finite type by 20.4.7) equals its separated completion, which is why the print writes it without a hat here and in (21.9.5.2)."),
F(178, "(21.9.5.2): last term before →0",
  "Ω̂^1_{A_0/k}⊗_{A_0}A →(u) Ω̂^1_{A/k} →(v) Ω^1_{A/A_0} → 0; no hat on the third module (crop)",
  r"\xrightarrow{v}\widehat\Omega^1_{A/A_0}\longrightarrow0",
  "formula", None, "high",
  fx(r"\xrightarrow{v}\widehat\Omega^1_{A/A_0}", r"\xrightarrow{v}\Omega^1_{A/A_0}"),
  "See the previous finding."),
F(178, "proof of (21.9.5): 'on sait que v est surjectif et que Im(u) est dense dans Ker(v)'",
  "surjectif italic (crop)", "upright",
  "italics", None, "high",
  fx(r"est surjectif et que", r"est \emph{surjectif} et que"), ""),
F(178, "proof of (21.9.5): '... et que Im(u) est dense dans Ker(v) (20.7.17)'",
  "dense italic (crop)", "upright",
  "italics", None, "high",
  fx(r"est dense dans", r"est \emph{dense} dans"), ""),
F(178, "proof of (21.9.5): 'donc la suite (21.9.5.2) est exacte.'",
  "exacte italic (crop)", "upright",
  "italics", None, "high",
  fx(r"(21.9.5.2) est exacte.", r"(21.9.5.2) est \emph{exacte}."), ""),
F(178, "proof of (21.9.5): 'et E séparable sur L_0, Ω^1_{A/A_0} est un A-module de torsion (20.4.13, (iv))'",
  "Ω^1_{A/A_0} without a hat (crop)", r"$\widehat\Omega^1_{A/A_0}$",
  "formula", None, "high",
  fx(r"$L_0$, $\widehat\Omega^1_{A/A_0}$", r"$L_0$, $\Omega^1_{A/A_0}$"),
  "As in the two hat findings above (Ω^1_{A/A_0} is identical to its completion)."),
F(178, "proof of (21.9.5): '... est un A-module de torsion (20.4.13, (iv))'",
  "'module de torsion' italic, the A and hyphen roman (crop)", "upright",
  "italics", None, "high",
  fx(r"$A$-module de" + NL + r"torsion", r"$A$-\emph{module de" + NL + r"torsion}"), ""),
F(178, "proof of (21.9.5): 'dans un même sous-A-module de type fini de E'",
  "'type fini' italic (crop)", "upright",
  "italics", None, "high",
  fx(r"sous-$A$-module de type fini", r"sous-$A$-module de \emph{type fini}"), ""),
F(178, "proof of (21.9.5): 'on a ainsi formé r dérivations continues de A dans un A-module topologique'",
  "continues italic (crop); the earlier 'comme elles sont continues dans A_0' is upright", "upright",
  "italics", None, "high",
  fx(r"dérivations" + NL + r"continues de $A$", r"dérivations" + NL + r"\emph{continues} de $A$"), ""),
F(178, "Proposition (21.9.6), first display: 'L_0=K_0((T_1, ..., T_r)),   M_0=K_0((T_1^p, ..., T_r^p))'",
  "no punctuation after M_0=K_0((T_1^p, ..., T_r^p)) (crop of the whole line)",
  r"M_0=K_0((T_1^p,\ldots,T_r^p)),",
  "punctuation", None, "high",
  fx(r"M_0=K_0((T_1^p,\ldots,T_r^p)),", r"M_0=K_0((T_1^p,\ldots,T_r^p))"), ""),
F(178, "Proposition (21.9.6): label '(i) Si Υ_{K_0/k_0} est de rang fini'",
  "label (i) upright", r"\item[(i)] inside the italic proposition: label italic",
  "convention", 6, "high",
  fx(r"\item[(i)] Si", r"\item[\textup{(i)}] Si"),
  "Label printed upright; \\item[...] comes out italic inside the italic statement environment (same form as the label fixes on pp. 20, 36-38, 101-102; GLOBAL_ISSUES 16)."),
F(178, "(21.9.6.1): 'rg_E Ω^1_{E/M} — rg_{K_0} Ω^1_{K_0/k} = ...'",
  "long dash for the subtraction (crop)", r"-\operatorname{rg}_{K_0}\Omega^1_{K_0/k}",
  "convention", 7, "high",
  fx(r"-\operatorname{rg}_{K_0}\Omega^1_{K_0/k}" + NL + r"    =(r", r"\setmin\operatorname{rg}_{K_0}\Omega^1_{K_0/k}" + NL + r"    =(r"),
  C7),
F(178, "(21.9.6.2): 'rg_E Ω^1_{E/M} — rg_{K_0} Ω^1_{K_0/k} ⩾ ...'",
  "long dash for the subtraction (crop)", r"-\operatorname{rg}_{K_0}\Omega^1_{K_0/k}",
  "convention", 7, "high",
  fx(r"-\operatorname{rg}_{K_0}\Omega^1_{K_0/k}" + NL + r"    \geqslant", r"\setmin\operatorname{rg}_{K_0}\Omega^1_{K_0/k}" + NL + r"    \geqslant"),
  C7),
F(178, "Proposition (21.9.6): label '(ii) On suppose en outre que'",
  "label (ii) upright", r"\item[(ii)] inside the italic proposition: label italic",
  "convention", 6, "high",
  fx(r"\item[(ii)] On suppose", r"\item[\textup{(ii)}] On suppose"),
  "As for label (i)."),
F(178, "end of the p. 178 segment: the proof of (21.9.6) opens before the p. 179 marker",
  "printed p. 178 ends with the statement of (21.9.6) ('... soient égaux.'); the proof begins at the top of p. 179 with '(i) On sait (21.1.5, (ii)) que'",
  r"\begin{proof}\n\begin{enumerate} stand before \oldpage[0\textsubscript{IV-1}]{179} (marker inside the enumerate, before \item[(i)])",
  "marker", None, "high",
  fx(r"\end{proposition}" + NL + NL + r"\begin{proof}" + NL + r"\begin{enumerate}" + NL, r"\end{proposition}" + NL + NL),
  "Move, part 1 of 2 (the openings move, not the marker, so each edit stays in its own page segment): deletes the two openings here; the p. 179 marker finding re-inserts them after \\oldpage[0\\textsubscript{IV-1}]{179}. Apply both or neither."),
# ---------------- p. 179 ----------------
F(179, "top of the p. 179 segment: re-insert the proof openings after the marker",
  "p. 179 begins with the proof of (21.9.6): '(i) On sait (21.1.5, (ii)) que'",
  r"\oldpage[0\textsubscript{IV-1}]{179} followed by \item[(i)]",
  "marker", None, "high",
  fx(r"\oldpage[0\textsubscript{IV-1}]{179}" + NL + r"  \item[(i)] On sait",
     r"\oldpage[0\textsubscript{IV-1}]{179}" + NL + r"\begin{proof}" + NL + r"\begin{enumerate}" + NL + r"  \item[(i)] On sait"),
  "Move, part 2 of 2: re-inserts the openings deleted by the p. 178 marker finding. Apply both or neither."),
F(179, "proof of (21.9.6) (i): the diagram of fields",
  "rows: K_0 → M_0 → L_0 → E; k → N → M → L; k_0 → k'_0 → N'. Vertical arrows only k→K_0, M→M_0, L→L_0 (top) and k'_0→k, N'→N (bottom); k'_0 stands under k, N' under N, k_0 to the left of k'_0, M_0 above M (crop)",
  r"4-column xymatrix with \ar[u] on every lower entry: arrows N→M_0, M→L_0, L→E, k_0→k, k'_0→N, N'→M that the print does not have, and the printed M→M_0, L→L_0, k'_0→k, N'→N missing",
  "formula", None, "high",
  fx(r"      K_0\ar[r] & M_0\ar[r] & L_0\ar[r] & E\\" + NL +
     r"      k\ar[u]\ar[r] & N\ar[u]\ar[r] & M\ar[u]\ar[r] & L\ar[u]\\" + NL +
     r"      k_0\ar[u]\ar[r] & k'_0\ar[u]\ar[r] & N'\ar[u] &",
     r"      & K_0\ar[rr] & & M_0\ar[r] & L_0\ar[r] & E\\" + NL +
     r"      & k\ar[u]\ar[r] & N\ar[r] & M\ar[u]\ar[r] & L\ar[u]\\" + NL +
     r"      k_0\ar[r] & k'_0\ar[u]\ar[r] & N'\ar[u]"),
  "Columns of the new matrix: k_0 | K_0, k, k'_0 | N, N' | M_0, M | L_0, L | E, as printed. The printed inclusions are k'_0=k_0(K_0^p)⊂k and N'⊂N."),
F(179, "formula from (21.7.3): 'rg_E Ω^1_{E/M} — rg_{M_0} Ω^1_{M/M_0} = deg. tr_{M_0}E + d(E/M_0, M)'",
  "long dash for the subtraction (crop)", r"-\operatorname{rg}_{M_0}...",
  "convention", 7, "high",
  fx(r"\Omega^1_{E/M}" + NL + r"    -", r"\Omega^1_{E/M}" + NL + r"    \setmin"),
  C7 + " Listed before the misprint finding on the same formula; the two edits do not overlap."),
F(179, "formula from (21.7.3): subscript of the second Ω",
  "rg_{M_0} Ω^1_{M/M_0} (crop: subscript M/M_0)",
  r"\Omega^1_{M_0/M} (silently corrected)",
  "misprint_in_print", None, "high",
  fx(r"\Omega^1_{M_0/M}" + NL + r"    =\deg", r"\Omega^1_{M/M_0}" + NL + r"    =\deg"),
  "(21.7.3.1) with L, K, k = E, M_0, M gives rg_{M_0} Ω^1_{M_0/M}, as in the formula three lines further on (rg_{M_0} Ω^1_{M_0/M} = rg_{K_0} Ω^1_{K_0/k}). The TeX silently corrects; the fix restores the printed reading.",
  corrected=r"\Omega^1_{M_0/M}"),
F(179, "(21.9.6.3): 'δ = d(E/M_0, M) — d(E/K_0, k_0) — r.', first dash",
  "long dash for the subtraction (crop)", r"\delta=d(E/M_0,M)-d(E/K_0,k_0)-r.",
  "convention", 7, "high",
  fx(r"\delta=d(E/M_0,M)-d", r"\delta=d(E/M_0,M)\setmin d"), C7),
F(179, "(21.9.6.3): second dash ('— r')",
  "long dash for the subtraction (crop)", r"-r.",
  "convention", 7, "high",
  fx(r"k_0)-r.", r"k_0)\setmin r."), C7),
F(179, "proof of Lemme (21.9.6.4): 'pour toute extension finie k' de k'",
  "finie italic (crop)", "upright",
  "italics", None, "high",
  fx(r"extension finie $k'$", r"extension \emph{finie} $k'$"), ""),
F(179, "proof of Lemme (21.9.6.4): 'S=A—{0}'",
  "long dash for the set difference (crop)", r"S=A-\{0\}",
  "convention", 7, "high",
  fx(r"S=A-\{0\}", r"S=A\setmin\{0\}"),
  r"Set difference; \setmin as in the earlier fixes, pending the convention-7 decision (FIX_POLICY 2.7)."),
# ---------------- p. 180 ----------------
F(180, "second display at the top: 'd(L_0/M_0, M) = d(L_0/M_0, M/N) + d(L_0/M_0, N)'",
  "no comma at the end (crop); the first display ends with a comma, as in the TeX",
  r"d(L_0/M_0,M)=d(L_0/M_0,M/N)+d(L_0/M_0,N),",
  "punctuation", None, "high",
  fx(r"d(L_0/M_0,M)=d(L_0/M_0,M/N)+d(L_0/M_0,N),", r"d(L_0/M_0,M)=d(L_0/M_0,M/N)+d(L_0/M_0,N)"), ""),
F(180, "display 'δ = d(E/L_0, M) + d(L_0/M_0, N) — d(E/L_0, k_0) + d(L_0/M_0, M/N) — r.', first dash",
  "long dash for the subtraction (crop)", r"-d(E/L_0,k_0)",
  "convention", 7, "high",
  fx(r"d(L_0/M_0,N)-d(E/L_0,k_0)", r"d(L_0/M_0,N)\setmin d(E/L_0,k_0)"), C7),
F(180, "same display, second dash ('— r.')",
  "long dash for the subtraction (crop)", r"-r.",
  "convention", 7, "high",
  fx(r"M/N)-r.", r"M/N)\setmin r."), C7),
F(180, "after (21.9.6.5): 'Pour cela, remarquons que, par définition, on a'",
  "new indented paragraph", r"no blank line after \end{equation}",
  "other", None, "high",
  fx(r"\end{equation}" + NL + r"  Pour cela", r"\end{equation}" + NL + NL + r"  Pour cela"), PARA),
F(180, "'d(L_0/M_0, M/N) = rg_{L_0} Υ_{L_0/M/N} — rg_{M_0} Υ_{M_0/M/N}.'",
  "long dash for the subtraction (crop)", r"-\operatorname{rg}_{M_0}\Upsilon_{M_0/M/N}",
  "convention", 7, "high",
  fx(r"-\operatorname{rg}_{M_0}\Upsilon_{M_0/M/N}", r"\setmin\operatorname{rg}_{M_0}\Upsilon_{M_0/M/N}"), C7),
F(180, "'Compte tenu des deux suites exactes'",
  "new indented paragraph", r"no blank line after \]",
  "other", None, "high",
  fx(r"\]" + NL + r"  Compte tenu", r"\]" + NL + NL + r"  Compte tenu"), PARA),
F(180, "first exact sequence '0 → Υ_{L_0/M/N} → ... → Ω^1_{L_0/M} → 0'",
  "no punctuation at the end of the line (crop)", r"\Omega^1_{L_0/M}\longrightarrow0,\\",
  "punctuation", None, "high",
  fx(r"\Omega^1_{L_0/M}\longrightarrow0,\\", r"\Omega^1_{L_0/M}\longrightarrow0\\"), ""),
F(180, "second exact sequence '0 → Υ_{M_0/M/N} → ... → Ω^1_{M_0/M} → 0'",
  "no punctuation at the end of the line (crop)", r"\Omega^1_{M_0/M}\longrightarrow0,",
  "punctuation", None, "high",
  fx(r"\Omega^1_{M_0/M}\longrightarrow0,", r"\Omega^1_{M_0/M}\longrightarrow0"), ""),
F(180, "'d(L_0/M_0, M/N) = rg_{L_0}Ω^1_{L_0/M} — rg_{L_0}Ω^1_{L_0/N} — rg_{M_0}Ω^1_{M_0/M} + rg_{M_0}Ω^1_{M_0/N}.', first dash",
  "long dash for the subtraction (crop)", r"-\operatorname{rg}_{L_0}\Omega^1_{L_0/N}",
  "convention", 7, "high",
  fx(r"-\operatorname{rg}_{L_0}\Omega^1_{L_0/N}", r"\setmin\operatorname{rg}_{L_0}\Omega^1_{L_0/N}"), C7),
F(180, "same display, second dash",
  "long dash for the subtraction (crop)", r"&-\operatorname{rg}_{M_0}\Omega^1_{M_0/M}",
  "convention", 7, "high",
  fx(r"&-\operatorname{rg}_{M_0}\Omega^1_{M_0/M}", r"&\setmin\operatorname{rg}_{M_0}\Omega^1_{M_0/M}"), C7),
F(180, "'On a encore, par (21.6.4.2),' first display",
  "d(E/L_0, M) — d(E/L_0, k_0) = d(E/L_0, M/k_0) (crop)",
  r"d(E/L_0,M)=d(E/L_0,k_0)+d(E/L_0,M/k_0) (same content, rearranged)",
  "formula", None, "high",
  fx(r"d(E/L_0,M)=d(E/L_0,k_0)+d(E/L_0,M/k_0)", r"d(E/L_0,M)-d(E/L_0,k_0)=d(E/L_0,M/k_0)"),
  "The TeX rewrote the printed equation. The restored minus is the print's long dash: see the next (convention-7) finding."),
F(180, "same display: 'd(E/L_0, M) — d(E/L_0, k_0)'",
  "long dash for the subtraction (crop)", "no minus in the TeX until the previous finding is applied",
  "convention", 7, "high", None,
  r"No fix of its own: the '-' exists only after the previous (formula) finding. In the convention-7 pass replace 'd(E/L_0,M)-d(E/L_0,k_0)=' with 'd(E/L_0,M)\setmin d(E/L_0,k_0)='. " + C7),
F(180, "'Mais comme L_0 est séparable sur K_0 (21.9.6.4), on a'",
  "new indented paragraph", r"no blank line after \]",
  "other", None, "high",
  fx(r"\]" + NL + r"  Mais comme $L_0$", r"\]" + NL + NL + r"  Mais comme $L_0$"), PARA),
F(180, "'Appliquons encore deux fois (21.6.4.2) au premier terme'",
  "new indented paragraph", r"no blank line after \]",
  "other", None, "high",
  fx(r"\]" + NL + r"  Appliquons encore", r"\]" + NL + NL + r"  Appliquons encore"), PARA),
F(180, "'Comme M⊂N(L_0^p), on a d(E/L_0, M/N)=0'",
  "new indented paragraph", r"no blank line after \]",
  "other", None, "high",
  fx(r"\]" + NL + r"  Comme $M\subset", r"\]" + NL + NL + r"  Comme $M\subset"), PARA),
F(180, "'Mais M_0 et L_0 sont des extensions séparables de K_0'",
  "new indented paragraph", r"no blank line after \]",
  "other", None, "high",
  fx(r"\]" + NL + r"  Mais $M_0$ et $L_0$", r"\]" + NL + NL + r"  Mais $M_0$ et $L_0$"), PARA),
F(180, "'donc d(L_0/K_0, k/k_0)=d(M_0/K_0, k/k_0)=0 (21.6.2), et appliquant encore deux fois (21.6.4.4),'",
  "the formula is in the running text, at the start of the last line, followed by '(21.6.2), et appliquant'",
  r"set as a display \[ ... \]",
  "other", None, "high",
  fx(r"donc" + NL + r"  \[" + NL + r"    d(L_0/K_0,k/k_0)=d(M_0/K_0,k/k_0)=0" + NL + r"  \]" + NL + r"  (21.6.2)",
     r"donc" + NL + r"  $d(L_0/K_0,k/k_0)=d(M_0/K_0,k/k_0)=0$" + NL + r"  (21.6.2)"),
  "Display the print sets inline (GLOBAL_ISSUES 21); no connecting word lost or added."),
F(180, "last line of p. 180: '... et appliquant encore deux fois (21.6.4.4), | on a ...' (sentence continues on p. 181)",
  "p. 181 begins at the left margin with 'on a d(E/L_0, k/k_0) = ...': no paragraph break",
  r"blank line before \oldpage[0\textsubscript{IV-1}]{181}",
  "other", None, "high",
  fx(r"deux fois (21.6.4.4)," + NL + NL, r"deux fois (21.6.4.4)," + NL),
  "Spurious paragraph break mid-sentence (GLOBAL_ISSUES 20); the blank line is the last line of the p. 180 segment."),
]

bad = 0
for f in findings:
    fix = f["fix"]
    if fix is None:
        continue
    cnt = pages[f["page"]].count(fix["old"])
    if cnt != 1:
        bad += 1
        print("NOT UNIQUE/ABSENT", f["page"], cnt, repr(fix["old"][:80]))
# overlapping olds on the same page
for n in range(176, 181):
    spans = []
    for f in findings:
        if f["page"] == n and f["fix"]:
            i = pages[n].find(f["fix"]["old"])
            spans.append((i, i + len(f["fix"]["old"]), f["where"][:50]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            print("OVERLAP p", n, a[2], "|", b[2])

json.dump(findings, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for f in findings:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    cnt[(f["page"], k)] += 1
for n in range(176, 181):
    print(n, cnt[(n, "normal")], cnt[(n, "convention")], cnt[(n, "misprint")])
print("bad:", bad, "total:", len(findings))
