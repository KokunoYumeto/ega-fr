# Builds findings_066_070.json for EGA 0_IV-1 pp. 66-70 and checks every "old".
# Newline placeholder in raw strings: the pilcrow sign.
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0IV1")
OUT = RUN / "findings_066_070.json"


def L(s):
    return None if s is None else s.replace("\u00b6", "\n")


def page_text(p):
    return (RUN / f"page_{p:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")


KSCAN = ("Fraktur K: the same glyph the TeX writes \\mathfrak K on p. 80 (19.3.4, K_{H,mu,n}); "
         "the radical R of 0_I p. 12 (1.1.2) is a different glyph (crops)")
KNOTE = ("Every Fraktur letter the TeX writes \\mathfrak R on pp. 66-70 is the printed Fraktur K "
         "(document-wide: see final message).")


def F(page, where, scan, tex, kind, old, new, conv=None, conf="high", note="", corrected=None,
      dependent=False):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv,
             confidence=conf, fix=None if old is None else {"old": L(old), "new": L(new)},
             note=note)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["_dependent"] = dependent  # old taken from the text after the preceding fixes
    return d


START = {66: "(18.4.4)", 67: "(18.5.1)", 68: "(18.5.2)", 69: "(19.0.1)", 70: "(19.0.2)"}


def context_of(text, pos, page):
    best, last_stmt = None, START[page]
    for m in re.finditer(r"\\begin\{(env|lemma|proposition|proof|definition|corollary|theorem)\}(\[([^\]]*)\])?", text):
        if m.start() > pos:
            break
        best = m
        if m.group(1) != "proof":
            last_stmt = f"({m.group(3)})"
    if best is None:
        return START[page]
    if best.group(1) == "proof":
        return f"proof of {last_stmt}"
    return f"({best.group(3)})"


def k_findings(page, text, skip_spans):
    """One finding per TeX line holding \\mathfrak R (extended until unique), outside skip_spans."""
    lines = text.split("\n")
    offs = []
    o = 0
    for ln in lines:
        offs.append(o)
        o += len(ln) + 1
    chunks = []  # (first line, last line, start offset in first line, end offset in last line)
    for i, ln in enumerate(lines):
        if "\\mathfrak R" not in ln:
            continue
        s, e = offs[i], offs[i] + len(ln)
        kabs = [s + m.start() for m in re.finditer(r"\\mathfrak R", ln)]
        covered = [any(a <= k and k + 11 <= b for a, b in skip_spans) for k in kabs]
        if all(covered):
            continue  # the explicit edit writes these letters itself
        if any(covered):
            raise SystemExit(f"Fraktur R partly inside an explicit edit, p. {page}: {ln}")
        # free part of the line: cut away any explicit edit that overlaps it
        a0, b0 = 0, len(ln)
        for a, b in skip_spans:
            if b <= s or a >= e:
                continue
            ka = [m.start() for m in re.finditer(r"\\mathfrak R", ln)]
            if a <= s and b - s <= min(ka):        # explicit edit covers the start of the line
                a0 = max(a0, b - s)
            elif b >= e and a - s >= max(ka) + 11:  # explicit edit covers the end of the line
                b0 = min(b0, a - s)
            else:
                raise SystemExit(f"Fraktur R inside an explicit edit, p. {page}: {ln}")
        j, b1 = i, b0
        def piece(i, j, a0, b1):
            return "\n".join(lines[i:j + 1])[a0:len("\n".join(lines[i:j])) + (1 if j > i else 0) + b1] if j > i else ln[a0:b1]
        while text.count(piece(i, j, a0, b1)) != 1:
            j += 1
            b1 = len(lines[j])
        if chunks and chunks[-1][1] >= i:
            pi, pj, pa, pb = chunks[-1]
            chunks[-1] = (pi, max(pj, j), pa, b1 if j >= pj else pb)
        else:
            chunks.append((i, j, a0, b1))
    out = []
    for i, j, a0, b1 in chunks:
        if j == i:
            old = lines[i][a0:b1]
        else:
            old = "\n".join([lines[i][a0:]] + lines[i + 1:j] + [lines[j][:b1]])
        assert text.count(old) == 1, (page, old)
        n = old.count("\\mathfrak R")
        new = old.replace("\\mathfrak R", "\\mathfrak K")
        out.append(dict(page=page, where=f"{context_of(text, offs[i], page)}: '{lines[i].strip()}'"
                        + ("" if j == i else " (and the next line)"),
                        scan="Fraktur K" if n == 1 else f"Fraktur K ({n} times)",
                        tex="\\mathfrak R" if n == 1 else f"\\mathfrak R ({n} times)",
                        kind="symbol", convention=None, confidence="high",
                        fix={"old": old, "new": new}, note=KNOTE + " " + KSCAN + ".",
                        _dependent=False))
    return out


def span_of(text, old):
    i = text.find(old)
    return (i, i + len(old))


findings = []

# ---------------------------------------------------------------- page 66
p = 66
t = page_text(p)
f66 = [
    F(p, "top of p. 66: 'par x(y_1...)' continues the sentence 'la structure de B-module étant définie' of p. 65",
      "no paragraph break: 'par' is flush left and continues the sentence",
      "blank line after \\oldpage[0\\textsubscript{IV-1}]{66} (and before it, at the end of p. 65's segment)",
      "other", r"\oldpage[0\textsubscript{IV-1}]{66}¶¶par", r"\oldpage[0\textsubscript{IV-1}]{66}¶par",
      note="Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). The blank line BEFORE the "
           "marker ('étant définie' + blank line, p. 65's segment) is already removed in FIXLOG (findings_061_065)."),
    F(p, "(18.4.4): 'par x(y_1⊗y_2⊗...⊗y_{n+1}) = (xy_1)⊗y_2⊗...⊗y_{n+1}; la dérivation'",
      "in the running text (first line of p. 66), with baseline dots",
      "displayed with \\[ ... \\], centred \\cdots",
      "other", r"\[¶  x(y_1\otimes y_2\otimes\cdots\otimes y_{n+1})¶  =(xy_1)\otimes y_2\otimes\cdots\otimes y_{n+1}\,;¶\]",
      r"$x(y_1\otimes y_2\otimes\ldots\otimes y_{n+1})=(xy_1)\otimes y_2\otimes\ldots\otimes y_{n+1}$~;",
      note="Layout (display vs inline); the same edit replaces the two \\cdots by \\ldots for the print's "
           "baseline dots (checked on a crop; no separate finding)."),
    F(p, "(18.4.4): 'la dérivation, de degré -1, d_n : P_n -> P_{n-1}'",
      "P_n, P_{n-1}: roman P, same face and weight as B, L (enlarged crop)",
      "\\mathbf P (bold)", "font", r"$d_n:\mathbf P_n\to\mathbf P_{n-1}$", r"$d_n:P_n\to P_{n-1}$",
      note="The complex P_. of (18.4.4) is printed with a roman P like every other module letter; the TeX's "
           "\\mathbf P has no counterpart in the print. Plain P as for B, L, as in the p. 65 fix "
           "'$P_\\bullet=(P_n)_{n\\geqslant0}$' (FIXLOG). The 15 \\mathbf P left in ega0-18-fr.tex are all on this page."),
    F(p, "(18.4.4), display of d_n, first line: 'd_n(x_1⊗x_2⊗...⊗x_{n+1})'", "baseline dots (crop)", "\\cdots",
      "symbol", r"d_n(x_1\otimes x_2\otimes\cdots\otimes x_{n+1})", r"d_n(x_1\otimes x_2\otimes\ldots\otimes x_{n+1})",
      note="Baseline dots in the print; the TeX has centred \\cdots (GLOBAL_ISSUES 22)."),
    F(p, "(18.4.4), display of d_n: '= (x_1x_2)⊗x_3⊗...⊗x_{n+1}'", "baseline dots (crop)", "\\cdots",
      "symbol", r"&=(x_1x_2)\otimes x_3\otimes\cdots\otimes x_{n+1}", r"&=(x_1x_2)\otimes x_3\otimes\ldots\otimes x_{n+1}",
      note="Baseline dots in the print; the TeX has centred \\cdots."),
    F(p, "(18.4.4), display of d_n: '- x_1⊗(x_2x_3)⊗...⊗x_{n+1} + ... +'", "baseline dots, twice (crop)",
      "\\cdots twice", "symbol", r"(x_2x_3)\otimes\cdots\otimes x_{n+1}+\cdots\\",
      r"(x_2x_3)\otimes\ldots\otimes x_{n+1}+\ldots\\",
      note="Baseline dots in the print, also between the two plus signs; the TeX has centred \\cdots."),
    F(p, "(18.4.4), display of d_n, second line: '(-1)^{n-1}x_1⊗x_2⊗...⊗x_{n-1}'", "baseline dots (crop)",
      "\\cdots", "symbol", r"x_1\otimes x_2\otimes\cdots\otimes x_{n-1}", r"x_1\otimes x_2\otimes\ldots\otimes x_{n-1}",
      note="Baseline dots in the print; the TeX has centred \\cdots."),
    F(p, "(18.4.4), display of d_n, end: '(-1)^n(x_{n+1}x_1)⊗x_2⊗...⊗x_n'", "baseline dots (crop)", "\\cdots",
      "symbol", r"(x_{n+1}x_1)\otimes x_2\otimes\cdots\otimes x_n", r"(x_{n+1}x_1)\otimes x_2\otimes\ldots\otimes x_n",
      note="Baseline dots in the print; the TeX has centred \\cdots."),
    F(p, "(18.4.4), end of the display of d_n: '...⊗x_n' before 'qui est bien B-linéaire'",
      "no punctuation after x_n (enlarged crop to the right margin)", "comma after x_n", "punctuation",
      r"x_n,¶\end{align*}", r"x_n¶\end{align*}", note="Comma added in the TeX."),
    F(p, "(18.4.4): 'l'application A-bilinéaire (y, z) ⇝ f(y, z) = h(1⊗y⊗z)'",
      "(y, z)⇝f(y, z): wavy arrow (enlarged crop)", "\\longmapsto", "symbol",
      r"$(y,z)\longmapsto f(y,z)", r"$(y,z)\leadsto f(y,z)",
      note="The print's wavy arrow, neither a plain arrow nor ↦ (GLOBAL_ISSUES 33)."),
    F(p, "(18.4.4): 'de B×B dans L, et en écrivant la condition précédente'", "no comma after 'et' (crop)",
      "'et, en écrivant'", "punctuation", r"dans $L$, et,¶en écrivant", r"dans $L$, et¶en écrivant",
      note="Comma added in the TeX."),
    F(p, "(18.4.4): 'un 2-cobord sera une application de la forme x⊗y⊗z ⇝ h'(d_2(x⊗y⊗z))'",
      "wavy arrow (enlarged crop)", "\\longmapsto", "symbol", r"z\longmapsto h'(d_2", r"z\leadsto h'(d_2",
      note="The print's wavy arrow (GLOBAL_ISSUES 33)."),
    F(p, "(18.4.4): 'l'application B-linéaire g : y ⇝ h'(1⊗y)'", "wavy arrow (enlarged crop)", "\\longmapsto",
      "symbol", r"$g:y\longmapsto h'(1\otimes y)$", r"$g:y\leadsto h'(1\otimes y)$",
      note="The print's wavy arrow (GLOBAL_ISSUES 33)."),
    F(p, "(18.4.4.1): 'H^i_A(B, L) = H^i(Hom_B(P_., L))'", "roman P", "\\mathbf P", "font",
      r"\operatorname{Hom}_B(\mathbf P_\bullet,L)).", r"\operatorname{Hom}_B(P_\bullet,L)).",
      note="Roman P as for B, L (see the finding on d_n : P_n -> P_{n-1})."),
    F(p, "(18.4.5): 'modifions le complexe P_. en degré 3'", "roman P", "\\mathbf P", "font",
      r"$\mathbf P_\bullet$ en degré", r"$P_\bullet$ en degré", note="Roman P as for B, L."),
    F(p, "(18.4.5), display 'P'_. : P'_3 -> P_2 -> P_1;'", "roman P (4 times)", "\\mathbf P (4 times)", "font",
      r"\mathbf P'_\bullet:\mathbf P'_3\xrightarrow{d'_3}\mathbf P_2¶  \xrightarrow{d_2}\mathbf P_1\,;",
      r"P'_\bullet:P'_3\xrightarrow{d'_3}P_2¶  \xrightarrow{d_2}P_1\,;", note="Roman P as for B, L."),
    F(p, "(18.4.5): 'nous prendrons P'_3 = P_3⊕(B⊗_AB⊗_AB)'", "roman P (twice; enlarged crop)",
      "\\mathbf P (twice)", "font", r"$\mathbf P'_3=\mathbf P_3\oplus", r"$P'_3=P_3\oplus",
      note="Roman P as for B, L."),
    F(p, "(18.4.5): 'd'_3 coïncidant avec d_3 sur P_3'", "roman P", "\\mathbf P", "font",
      r"sur $\mathbf P_3$", r"sur $P_3$", note="Roman P as for B, L."),
    F(p, "(18.4.5): 'un 2-cocycle de P'_. correspond maintenant'", "roman P", "\\mathbf P", "font",
      r"de $\mathbf P'_\bullet$ correspond", r"de $P'_\bullet$ correspond", note="Roman P as for B, L."),
    F(p, "(18.4.5), last sentence: 'par suite, on a H^2_A(B, L)^s = H^2(Hom_B(P'_., L)).'",
      "in the running text (line starting at the left margin); roman P",
      "displayed with \\[ ... \\]; \\mathbf P", "other",
      r"on a¶\[¶  \mathrm H_A^2(B,L)^s¶  =\mathrm H^2(\operatorname{Hom}_B(\mathbf P'_\bullet,L)).¶\]",
      r"on a¶$\mathrm H_A^2(B,L)^s=\mathrm H^2(\operatorname{Hom}_B(P'_\bullet,L))$.",
      note="Layout (display vs inline); the same edit also writes the roman P (font, as in the other P findings; "
           "no separate finding)."),
    F(p, "(18.4.6.1): 'Hom_K(H_i(P_.), L)'", "roman P", "\\mathbf P", "font",
      r"\mathrm H_i(\mathbf P_\bullet)", r"\mathrm H_i(P_\bullet)", note="Roman P as for B, L."),
    F(p, "(18.4.6.2): 'Hom_K(H_2(P'_.), L)'", "roman P", "\\mathbf P", "font",
      r"\mathrm H_2(\mathbf P'_\bullet)", r"\mathrm H_2(P'_\bullet)", note="Roman P as for B, L."),
    F(p, "heading '18.5. Cas des anneaux topologiques.'", "title ends with a full stop",
      "\\subsection{Cas des anneaux topologiques}", "punctuation",
      r"\subsection{Cas des anneaux topologiques}", r"\subsection{Cas des anneaux topologiques.}",
      note="GLOBAL_ISSUES 43/58 (no \\subsection title in ega0-14 to ega0-23 has the printed full stop)."),
]
end66 = F(p, "end of p. 66: '... de sorte que L peut être' / p. 67 'considéré comme un ...'",
          "the sentence runs on to p. 67 (first line of p. 67 flush left)",
          "blank line before \\oldpage[0\\textsubscript{IV-1}]{67}", "other",
          r"peut être¶¶", r"peut être¶",
          note="Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the "
               "p. 67 finding that removes the blank line after the marker.")
C7 = ("Long dash for a minus sign at full size (GLOBAL_ISSUES 23, unary minus included as in item 49); "
      "\\setmin as in the p. 65 fix 'xg(y)\\setmin g(xy)'. The minus signs in the sub- and superscripts "
      "(P_{n-1}, x_{n-1}, exponent n-1) are short in the print and stay '-'.")
c7 = [
    F(p, "(18.4.4): 'la dérivation, de degré —1'", "long dash before 1 (enlarged crop)", "$-1$", "convention",
      r"de degré $-1$", r"de degré $\setmin 1$", conv=7, note=C7),
    F(p, "(18.4.4), display of d_n: '... ⊗x_{n+1} — x_1⊗(x_2x_3)'", "long dash (enlarged crop)", "-", "convention",
      r"-x_1\otimes(x_2x_3)", r"\setmin x_1\otimes(x_2x_3)", conv=7, note=C7),
    F(p, "(18.4.4), display of d_n, second line: '(—1)^{n-1}x_1⊗...'", "long dash inside (—1) (enlarged crop)",
      "(-1)", "convention", r"&\quad+(-1)^{n-1}", r"&\quad+(\setmin 1)^{n-1}", conv=7, note=C7),
    F(p, "(18.4.4), display of d_n, second line: '+ (—1)^n(x_{n+1}x_1)⊗...'", "long dash inside (—1)",
      "(-1)", "convention", r"+(-1)^n", r"+(\setmin 1)^n", conv=7, note=C7),
    F(p, "(18.4.4): 'h'(d_2(1⊗x⊗y)) = xg(y) — g(xy) + yg(x)'", "long dash", "-", "convention",
      r"xg(y)-g(xy)", r"xg(y)\setmin g(xy)", conv=7, note=C7),
    F(p, "(18.4.5), display 'd'_3(x⊗y⊗z) = x⊗y⊗z — x⊗z⊗y.'", "long dash", "-", "convention",
      r"z-x\otimes z", r"z\setmin x\otimes z", conv=7, note=C7),
]
# keep page order: insert each convention-7 finding after the last finding whose old starts before it
for c in c7:
    pos = t.find(L(c["fix"]["old"]))
    idx = 0
    for n, x in enumerate(f66):
        if x["fix"] and t.find(L(x["fix"]["old"])) <= pos:
            idx = n + 1
    f66.insert(idx, c)
spans = [span_of(t, L(x["fix"]["old"])) for x in f66 if x["fix"]]
findings += f66 + k_findings(p, t, spans) + [end66]

# ---------------------------------------------------------------- page 67
p = 67
t = page_text(p)
top67 = F(p, "top of p. 67: 'considéré comme un (B/K)-bimodule' continues '... L peut être' of p. 66",
          "no paragraph break: first line flush left, continues the sentence",
          "blank line after \\oldpage[0\\textsubscript{IV-1}]{67}", "other",
          r"\oldpage[0\textsubscript{IV-1}]{67}¶¶considéré", r"\oldpage[0\textsubscript{IV-1}]{67}¶considéré",
          note="Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with the p. 66 'peut être' finding "
               "(blank line before the marker).")
end67 = F(p, "end of p. 67: '... Enfin, si on a un homomorphisme' / p. 68 'continu de B-bimodules'",
          "the sentence runs on to p. 68 (first line of p. 68 flush left)",
          "blank line before \\oldpage[0\\textsubscript{IV-1}]{68}", "other",
          r"si on a un homomorphisme¶¶", r"si on a un homomorphisme¶",
          note="Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with the p. 68 top finding.")
spans = [span_of(t, L(top67["fix"]["old"])), span_of(t, L(end67["fix"]["old"]))]
findings += [top67] + k_findings(p, t, spans) + [end67]

# ---------------------------------------------------------------- page 68
p = 68
t = page_text(p)
HEAD19 = (r"\section{Algèbres formellement lisses et anneaux de Cohen}¶\label{section:0.19-fr}¶\label{0.19-fr}¶¶"
          r"\setcounter{subsection}{-1}¶\subsection{Introduction}¶\label{subsection:0.19.0-fr}¶\label{0.19.0-fr}¶¶")
f68 = [
    F(p, "top of p. 68: 'continu de B-bimodules L -> L'' continues '... si on a un homomorphisme' of p. 67",
      "no paragraph break: first line flush left, continues the sentence",
      "blank line after \\oldpage[0\\textsubscript{IV-1}]{68}", "other",
      r"\oldpage[0\textsubscript{IV-1}]{68}¶¶continu", r"\oldpage[0\textsubscript{IV-1}]{68}¶continu",
      note="Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with the p. 67 end finding."),
    F(p, "proof of Lemme (18.5.3.1): 'on a des homomorphismes canoniques w_{K,V} : Hom_{C/K}(E/V, L) -> "
         "Hom. cont_C(E, L) formant un système inductif'",
      "in the running text; Fraktur K in Hom_{C/K}", "displayed with \\[ ... \\]; \\mathfrak R twice", "other",
      r"\[¶  w_{\mathfrak R,V}:\operatorname{Hom}_{C/\mathfrak R}(E/V,L)¶  \longrightarrow\operatorname{Hom.\ cont}_C(E,L)¶\]",
      r"$w_{\mathfrak K,V}:\operatorname{Hom}_{C/\mathfrak K}(E/V,L)\longrightarrow\operatorname{Hom.\ cont}_C(E,L)$",
      note="Layout (display vs inline); the same edit writes the Fraktur K for the TeX's \\mathfrak R (" + KNOTE[:-1]
           + "). The subscript of w is a misprint (next finding), whose edit applies after this one."),
    F(p, "proof of Lemme (18.5.3.1): 'w_{K,V}'",
      "w_{K,V}: ROMAN capital K in the subscript, not the Fraktur letter of Hom_{C/K} beside it (enlarged crop)",
      "w_{\\mathfrak R,V} (Fraktur)", "misprint_in_print", r"$w_{\mathfrak K,V}:", r"$w_{K,V}:",
      corrected=r"$w_{\mathfrak K,V}$",
      note="Wrong-fount letter in the print (roman K for Fraktur K); the TeX silently corrects it. 'old' is taken "
           "from the text after the preceding layout fix; restores the printed roman K in the diplomatic text.",
      dependent=True),
    F(p, "proof of Lemme (18.5.3.1): 'que l'homomorphisme Hom_{C/K}(E/V, L) -> Hom_{C/K}(E/V', L) (avec ...) "
         "est injectif'",
      "in the running text; Fraktur K twice", "displayed with \\[ ... \\]; \\mathfrak R twice", "other",
      r"\[¶  \operatorname{Hom}_{C/\mathfrak R}(E/V,L)¶  \longrightarrow\operatorname{Hom}_{C/\mathfrak R}(E/V',L)¶\]",
      r"$\operatorname{Hom}_{C/\mathfrak K}(E/V,L)\longrightarrow\operatorname{Hom}_{C/\mathfrak K}(E/V',L)$",
      note="Layout (display vs inline); the same edit writes the Fraktur K (no separate finding). The next display "
           "(Hom_{C/K}(E/V, L) -> Hom_{C/K'}(E/V, L)) is displayed in the print too."),
]
part1 = F(p, "page-68 continuation (ega0-19-fr.tex, before its first marker): '\\section{...}' + '\\subsection{Introduction}'",
          "printed p. 68 ends with the proof of (18.5.4); '§ 19. ALGÈBRES FORMELLEMENT LISSES ET ANNEAUX DE COHEN' "
          "and '19.0. Introduction.' head p. 69",
          "the \\section and \\subsection stand before \\oldpage[0\\textsubscript{IV-1}]{69}", "marker",
          HEAD19, "",
          note="OUTSIDE the page segment: text before the first marker of ega0-19-fr.tex (apply by hand). Move, part 1 "
               "of 2: deletes the headings here; the page-69 marker finding re-inserts them after "
               "\\oldpage[0\\textsubscript{IV-1}]{69}. Apply both or neither.")
spans = [span_of(t, L(x["fix"]["old"])) for x in f68 if x["fix"] and not x["_dependent"]]
spans.append(span_of(t, L(HEAD19)))
findings += f68[:1] + k_findings(p, t, spans) + f68[1:] + [part1]

# ---------------------------------------------------------------- page 69
p = 69
t = page_text(p)
HEAD19N = HEAD19.replace(r"\subsection{Introduction}", r"\subsection{Introduction.}")
f69 = [
    F(p, "top of p. 69: '§ 19. ALGÈBRES FORMELLEMENT LISSES ET ANNEAUX DE COHEN', '19.0. Introduction.'",
      "p. 69 begins with the § 19 title and the heading 19.0",
      "the headings stand before \\oldpage[0\\textsubscript{IV-1}]{69} (page-68 continuation)", "marker",
      r"\oldpage[0\textsubscript{IV-1}]{69}¶¶\begin{env}[19.0.1]",
      r"\oldpage[0\textsubscript{IV-1}]{69}¶¶" + HEAD19N + r"\begin{env}[19.0.1]",
      note="Move, part 2 of 2: re-inserts the headings deleted by the page-68 part-1 finding (which lies in ega0-19-fr.tex "
           "before its first marker). Apply both or neither. The re-inserted 19.0 title carries the printed full stop "
           "(next finding)."),
    F(p, "heading '19.0. Introduction.'", "title ends with a full stop", "\\subsection{Introduction}", "punctuation",
      None, None,
      note="Covered by the page-69 marker edit (part 2), which re-inserts the title as \\subsection{Introduction.}. "
           "If the move is done differently, add the full stop by hand (GLOBAL_ISSUES 43/58)."),
    F(p, "(19.0.1): 'tout Y-morphisme Y'' -> X se factorise en Y'' ->^h Y' -> X'",
      "'en' italic, like 'se factorise' (enlarged crop; 'se relève en' later has an upright 'en')",
      "'en' outside \\emph", "italics", r"se factorise} en", r"se factorise en}"),
    F(p, "(19.0.1): 'un foncteur contravariant représentable Y' ⇝ F(Y')'", "wavy arrow (enlarged crop)",
      "\\mapsto", "symbol", r"$Y'\mapsto F(Y')$", r"$Y'\leadsto F(Y')$",
      note="The print's wavy arrow (GLOBAL_ISSUES 33)."),
    F(p, "(19.0.2), item 'I. — Soient A, B deux anneaux locaux noethériens'",
      "'I.' in roman, normal weight (enlarged crop)", "\\textbf{I.}", "font", r"\textbf{I.} ---", r"I. ---",
      note="Same for II.-V. (pp. 69-70)."),
    F(p, "(19.0.2), item 'II. — Soient k un corps'", "'II.' in roman, normal weight", "\\textbf{II.}", "font",
      r"\textbf{II.} ---", r"II. ---"),
    F(p, "end of p. 69: '... l'anneau semi-local A⊗_A k' soit' / p. 70 'régulier (22.5.8)'",
      "the sentence runs on to p. 70 (first line of p. 70 flush left)",
      "blank line before \\oldpage[0\\textsubscript{IV-1}]{70}", "other", r"soit¶¶", r"soit¶",
      note="Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with the p. 70 top finding."),
    F(p, "(19.0.2) II: 'l'anneau semi-local A⊗_A k' soit régulier'",
      "A⊗_A k': subscript capital A (enlarged crop)", "A\\otimes_k k'", "misprint_in_print",
      r"$A\otimes_k k'$", r"$A\otimes_A k'$", corrected=r"$A\otimes_k k'$",
      note="Misprint: A is a k-algebra and k' an extension of k, so the tensor product is over k. The TeX silently "
           "corrects it; the diplomatic text restores the printed A."),
]
findings += f69

# ---------------------------------------------------------------- page 70
p = 70
t = page_text(p)
f70 = [
    F(p, "top of p. 70: 'régulier (22.5.8)' continues '... A⊗_A k' soit' of p. 69",
      "no paragraph break: first line flush left, continues the sentence",
      "blank line after \\oldpage[0\\textsubscript{IV-1}]{70}, then \\noindent", "other",
      r"\oldpage[0\textsubscript{IV-1}]{70}¶¶\noindent ", r"\oldpage[0\textsubscript{IV-1}]{70}¶",
      note="Spurious paragraph break (GLOBAL_ISSUES 20); \\noindent only hid it. Apply together with the p. 69 'soit' "
           "finding."),
    F(p, "(19.0.2) II, first word of p. 70: 'régulier (22.5.8)'", "'régulier' italic (enlarged crop)",
      "upright", "italics", r"régulier (22.5.8)", r"\emph{régulier} (22.5.8)",
      note="Continues the italic 'géométriquement régulier' definition of p. 69."),
    F(p, "(19.0.2) II: 'la structure de k-algèbre de A'", "'k-algèbre' italic (enlarged crop)",
      "'-algèbre' upright", "italics", r"de $k$-algèbre de $A$", r"de \emph{$k$-algèbre} de $A$"),
    F(p, "(19.0.2) II: 'l'inégalité dim(A) >= rg_k(Υ_{K/k}), où Υ_{K/k} est le « module d'imperfection »'",
      "capital upsilon Υ, twice (enlarged crop)", "\\Gamma, twice", "symbol",
      r"\[¶  \dim(A)\geq \operatorname{rg}_k(\Gamma_{K/k}),¶\]¶où $\Gamma_{K/k}$",
      r"$\dim(A)\geq \operatorname{rg}_k(\Upsilon_{K/k})$,¶où $\Upsilon_{K/k}$",
      note="The module d'imperfection is printed Υ_{K/k}. The same edit sets the inequality inline as printed "
           "(next finding)."),
    F(p, "(19.0.2) II: the inequality 'dim(A) >= rg_k(Υ_{K/k}),'", "in the running text",
      "displayed with \\[ ... \\]", "other", None, None,
      note="Layout (display vs inline): covered by the edit of the preceding finding."),
    F(p, "(19.0.2), item 'III. — Soient A un anneau local noethérien'", "'III.' in roman, normal weight",
      "\\textbf{III.}", "font", r"\textbf{III.} ---", r"III. ---"),
    F(p, "(19.0.2) III: 'un A_0-isomorphisme B⊗_A A_0 ⥲ B_0 (de sorte que, par I), ...'",
      "in the running text", "displayed with \\[ ... \\]", "other",
      r"\[¶  B\otimes_A A_0\xrightarrow{\sim}B_0¶\]", r"$B\otimes_A A_0\xrightarrow{\sim}B_0$",
      note="Layout (display vs inline); the formula itself matches."),
    F(p, "(19.0.2), item 'IV. — L'intérêt de l'étude'", "'IV.' in roman, normal weight", "\\textbf{IV.}", "font",
      r"\textbf{IV.} ---", r"IV. ---"),
    F(p, "(19.0.2), item 'V. — Enfin, nous verrons'", "'V.' in roman, normal weight", "\\textbf{V.}", "font",
      r"\textbf{V.} ---", r"V. ---"),
    F(p, "(19.0.3), last paragraph: 'M/N est annulé par un idéal ouvert de A'", "'de' italic (enlarged crop)",
      "'de' outside \\emph", "italics", r"un idéal ouvert} de $A$", r"un idéal ouvert de} $A$"),
]
spans = [span_of(t, L(x["fix"]["old"])) for x in f70 if x["fix"]]
findings += f70 + k_findings(p, t, spans)

# ---------------------------------------------------------------- normalise and check
for x in findings:
    if x["fix"]:
        x["fix"] = {"old": L(x["fix"]["old"]), "new": L(x["fix"]["new"])}

ok = True
by_page = {}
for x in findings:
    by_page.setdefault(x["page"], []).append(x)
for pg, xs in sorted(by_page.items()):
    orig = page_text(pg)
    cur = orig
    for x in xs:
        if not x["fix"]:
            continue
        old, new = x["fix"]["old"], x["fix"]["new"]
        c_orig, c_cur = orig.count(old), cur.count(old)
        if c_cur != 1 or (not x["_dependent"] and c_orig != 1):
            ok = False
            print("FAIL", pg, x["kind"], repr(old[:80]), "orig", c_orig, "cur", c_cur)
        cur = cur.replace(old, new, 1)
    print(pg, "applied in sequence; remaining \\mathfrak R:", cur.count("\\mathfrak R"),
          "remaining \\mathbf P:", cur.count("\\mathbf P"), "remaining \\cdots:", cur.count("\\cdots"))

for x in findings:
    x.pop("_dependent", None)
json.dump(findings, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in findings:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
print("OK" if ok else "ERRORS", len(findings))
for pg in sorted(by_page):
    print(pg, cnt[(pg, "normal")], cnt[(pg, "convention")], cnt[(pg, "misprint")])
