import json, os, sys

RUN = r"user\Documents\ega_scan_check_20261101\run_II"
OUT = os.path.join(RUN, "findings_030_034.json")

def L(*lines):
    return "\n".join(lines)

F = []

def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

SUP5 = "printed (...)~ with the tilde after the closing parenthesis; the TeX also drops the parentheses (\\widetilde{...} over the bare expression), so a search for \\widetilde{(...)} will not find it"

# ---------------- page 30 ----------------
add(30, "(2.4.5), last line", "\u03b1.x=(\u03b1.1)x (baseline dot)", r"\alpha\cdot x=(\alpha\cdot1)x",
    "symbol", None, "medium",
    r"$\alpha\cdot x=(\alpha\cdot1)x$", r"$\alpha.x=(\alpha.1)x$",
    "the print's product dot sits on the baseline, like a full stop; \\cdot is centred")
add(30, "proof of (2.4.7), (i), first line", "p\u2192p\u2229S^(d) (plain arrow)", r"\mathfrak{p}\mapsto\mathfrak{p}\cap S^{(d)}",
    "convention", 3, "high",
    r"\mathfrak{p}\mapsto\mathfrak{p}\cap S^{(d)}", r"\mathfrak{p}\to\mathfrak{p}\cap S^{(d)}",
    "")
add(30, "proof of (2.4.7), (i): 'la bijection pr\u00e9c\u00e9dente est un hom\u00e9omorphisme'", "hom\u00e9omorphisme in italics", "hom\u00e9omorphisme upright",
    "italics", None, "high",
    "est un hom\u00e9omorphisme d'espaces", "est un \\emph{hom\u00e9omorphisme} d'espaces",
    "")
add(30, "proof of (2.4.7), (i): 'avec les m\u00eames notations, S_(f) et ...'", "S_{(f^d)} (no superscript (d))", r"S^{(d)}_{(f^d)}",
    "formula", None, "high",
    r"$S^{(d)}_{(f^d)}$", r"$S_{(f^d)}$",
    "the TeX adds the superscript (d); the printed reading is not an error (S_{(f^d)} formed in S or in S^{(d)} is the same subring of S_f, and (2.2.2) identifies it with S_{(f)}), so it is not listed as a misprint")
add(30, "proof of (2.4.7), end of (i)", "sch\u00e9mas in italics", "sch\u00e9mas upright",
    "italics", None, "high",
    L("canoniquement en tant que", "    sch\u00e9mas."), L("canoniquement en tant que", "    \\emph{sch\u00e9mas}."),
    "")
add(30, "proof of (2.4.7), end of (ii)", "sch\u00e9mas in italics", "sch\u00e9mas upright",
    "italics", None, "high",
    "s'identifient en tant que sch\u00e9mas.", "s'identifient en tant que \\emph{sch\u00e9mas}.",
    "")
add(30, "(2.5.1), first sentence", "gradu\u00e9 in italics", "gradu\u00e9 upright",
    "italics", None, "high",
    "un $S$-module gradu\u00e9. Pour", "un $S$-module \\emph{gradu\u00e9}. Pour",
    "")
add(30, "(2.5.1), 'faisceau quasi-coh\u00e9rent associ\u00e9 (M_(f))~'", "(M_(f))~", r"\widetilde{M_{(f)}}",
    "convention", 5, "high",
    r"$\widetilde{M_{(f)}}$ sur le sch", r"$(M_{(f)})\supertilde$ sur le sch",
    SUP5)
add(30, "(2.5.1), last line", "(I, 1.3.4) with bold I", "I, 1.3.4",
    "convention", 2, "high",
    r"{I, 1.3.4}", r"{\textbf{I}, 1.3.4}", "")

# ---------------- page 31 ----------------
add(31, "proof of (2.5.2): 'du faisceau (M_(f))~ sur D_+(f)'", "(M_(f))~", r"\widetilde{M_{(f)}}",
    "convention", 5, "high",
    r"$\widetilde{M_{(f)}}$ sur $D_+(f)$", r"$(M_{(f)})\supertilde$ sur $D_+(f)$", SUP5)
add(31, "proof of (2.5.2)", "(I, 1.3.6) with bold I", "I, 1.3.6",
    "convention", 2, "high", r"{I, 1.3.6}", r"{\textbf{I}, 1.3.6}", "")
add(31, "proof of (2.5.2): 'donc aussi \u00e0 (M_(fg))~'", "(M_(fg))~", r"\widetilde{M_{(fg)}}",
    "convention", 5, "high",
    r"\widetilde{M_{(fg)}}", r"(M_{(fg)})\supertilde", SUP5)
add(31, "proof of (2.5.2), display theta_{g,f}, source", "(M_(f))~|D_+(fg)", r"\widetilde{M_{(f)}}|D_+(fg)",
    "convention", 5, "high",
    r"\theta_{g,f}:\widetilde{M_{(f)}}", r"\theta_{g,f}:(M_{(f)})\supertilde", SUP5)
add(31, "proof of (2.5.2), display theta_{g,f}, target", "(M_(g))~|D_+(fg)", r"\widetilde{M_{(g)}}|D_+(fg)",
    "convention", 5, "high",
    r"\widetilde{M_{(g)}}", r"(M_{(g)})\supertilde", SUP5)
add(31, "proof of (2.5.2): 'Par suite (0, 3.3.1)'", "(0, 3.3.1) with bold 0", "0, 3.3.1",
    "convention", 2, "high", r"{0, 3.3.1}", r"{\textbf{0}, 3.3.1}", "")
add(31, "proof of (2.5.2): 'un isomorphisme eta_f de F|D_+(f) sur (M_(f))~'", "(M_(f))~", r"\widetilde{M_{(f)}}",
    "convention", 5, "high",
    r"sur $\widetilde{M_{(f)}}$ tels que", r"sur $(M_{(f)})\supertilde$ tels que", SUP5)
add(31, "proof of (2.5.2): 'compte tenu de (I, 1.3.7)'", "(I, 1.3.7) with bold I", "I, 1.3.7",
    "convention", 2, "high", r"{I, 1.3.7}", r"{\textbf{I}, 1.3.7}", "")
add(31, "D\u00e9finition (2.5.3)", "associ\u00e9 in the same italic as the rest of the statement", r"\emph{associ\u00e9} inside the italic definition environment (comes out upright)",
    "convention", 6, "high",
    "\\emph{associ\u00e9}", "associ\u00e9",
    "drop \\emph: the print shows no change of face")
add(31, "Proposition (2.5.4)", "Le foncteur M\u0303 en M", r"Le foncteur $M\mapsto\widetilde{M}$",
    "formula", None, "high",
    r"$M\mapsto\widetilde{M}$", r"$\widetilde{M}$ en $M$",
    "the print names the functor in words ('X en Y'), not with a maps-to arrow")
add(31, "proof of (2.5.4): 'il suffit de les v\u00e9rifier sur les faisceaux M\u0303|D_+(f)=(M_(f))~'", "(M_(f))~", r"\widetilde{M_{(f)}}",
    "convention", 5, "high",
    r"=\widetilde{M_{(f)}}$~; or", r"=(M_{(f)})\supertilde$~; or", SUP5)
add(31, "proof of (2.5.4): 'le foncteur M_f en M'", "M_f en M", r"$M\mapsto M_f$",
    "formula", None, "high",
    r"$M\mapsto M_f$", r"$M_f$ en $M$", "")
add(31, "proof of (2.5.4): 'le foncteur N_0 en N'", "N_0 en N", r"$N\mapsto N_0$",
    "formula", None, "high",
    r"$N\mapsto N_0$", r"$N_0$ en $N$", "")
add(31, "proof of (2.5.4): 'le foncteur P\u0303 en P'", "P\u0303 en P", r"$P\mapsto\widetilde{P}$",
    "formula", None, "high",
    r"$P\mapsto\widetilde{P}$", r"$\widetilde{P}$ en $P$", "")
add(31, "proof of (2.5.4): '(I, 1.3.5 et 1.3.9)'", "(I, 1.3.5 ...) with bold I", "I, 1.3.5",
    "convention", 2, "high", r"{I, 1.3.5}", r"{\textbf{I}, 1.3.5}", "")
add(31, "proof of (2.5.4): '(I, 1.3.5 et 1.3.9)'", "1.3.9 (chapter numeral printed once, before 1.3.5)", "I, 1.3.9",
    "extra", None, "high",
    r"{I, 1.3.9})~;", r"{1.3.9})~;", "the TeX repeats 'I, ' before the second number")
add(31, "paragraph after (2.5.4): 'les r\u00e9sultats de (I, 1.3.9 et 1.3.10)'", "(I, 1.3.9 ...) with bold I", "I, 1.3.9",
    "convention", 2, "high", r"{I, 1.3.9} et", r"{\textbf{I}, 1.3.9} et", "")
add(31, "paragraph after (2.5.4): '(I, 1.3.9 et 1.3.10)'", "1.3.10 (chapter numeral printed once)", "I, 1.3.10",
    "extra", None, "high",
    r"{I, 1.3.10}", r"{1.3.10}", "the TeX repeats 'I, ' before the second number")

# ---------------- page 32 ----------------
add(32, "first line: 'En particulier, l'anneau local (O_X)_p'", "l' upright, 'anneau local' italic", r"\emph{l'anneau local ...} (l' italic too)",
    "italics", None, "high",
    r"\emph{l'anneau local $(\mathcal{O}_X)_\mathfrak{p}$}", r"l'\emph{anneau local} $(\mathcal{O}_X)_\mathfrak{p}$",
    "")
add(32, "Proposition (2.5.7)", "(S(nd))~|D_+(f)", r"\widetilde{S(nd)}|D_+(f)",
    "convention", 5, "high",
    r"\widetilde{S(nd)}|D_+(f)", r"(S(nd))\supertilde|D_+(f)", SUP5)
add(32, "Corollaire (2.5.8): 'Sur l'ensemble ouvert U = ...'", "U=\u222a_{f\u2208S_d} D_+(f), set inline in the text line", "displayed formula \\[ U=\\bigcup_{f\\in S_d}D_+(f), \\]",
    "other", None, "high",
    L(r"\[", r"  U=\bigcup_{f\in S_d}D_+(f),", r"\]", ""), L(r"$U=\bigcup_{f\in S_d}D_+(f)$,", ""),
    "display in the TeX, inline in the print (cf. GLOBAL_ISSUES item 21)")
add(32, "Corollaire (2.5.8): 'la restriction du O_X-Module (S(nd))~'", "(S(nd))~", r"\widetilde{S(nd)}",
    "convention", 5, "high",
    r"\widetilde{S(nd)}$ est un", r"(S(nd))\supertilde$ est un", SUP5)
add(32, "Corollaire (2.5.8), end", "(0, 5.4.1) with bold 0", "0, 5.4.1",
    "convention", 2, "high", r"{0, 5.4.1}", r"{\textbf{0}, 5.4.1}", "")
add(32, "Corollaire (2.5.9)", "(S(n))~", r"\widetilde{S(n)}",
    "convention", 5, "high",
    r"\widetilde{S(n)}$ sont", r"(S(n))\supertilde$ sont", SUP5)
add(32, "(2.5.10.1)", "O_X(n)=(S(n))~", r"\mathcal{O}_X(n)=\widetilde{S(n)}",
    "convention", 5, "high",
    r"\mathcal{O}_X(n)=\widetilde{S(n)}", r"\mathcal{O}_X(n)=(S(n))\supertilde", SUP5)
add(32, "(2.5.10), last sentence: 'un O_X-Module inversible'", "inversible in italics", "inversible upright",
    "italics", None, "high",
    r"un $\mathcal{O}_X$-Module inversible.", r"un $\mathcal{O}_X$-Module \emph{inversible}.", "")

# ---------------- page 33 ----------------
add(33, "top of page: 'en composant l'homomorphisme ...'", "continues the sentence of (2.5.11) after display (2.5.11.1); line not indented, no new paragraph", "blank line after \\oldpage[II]{33} starts a new paragraph",
    "other", None, "high",
    L(r"\oldpage[II]{33}", "", "en composant"), L(r"\oldpage[II]{33}", "en composant"),
    "spurious paragraph break at the page marker (GLOBAL_ISSUES item 20)")
add(33, "(2.5.11): 'l'isomorphisme canonique ... (0, 1.3.4)'", "(0, 1.3.4) with bold 0", "0, 1.3.4",
    "convention", 2, "high", r"{0, 1.3.4}", r"{\textbf{0}, 1.3.4}", "")
add(33, "(2.5.11.2)", "(M\u2297_S N)~", r"\widetilde{M\otimes_S N}",
    "convention", 5, "high",
    r"\longrightarrow\widetilde{M\otimes_S N}.", r"\longrightarrow(M\otimes_S N)\supertilde.", SUP5)
add(33, "diagram (2.5.11.3), top right", "(\U0001D50D\u2297_S\U0001D50E)~", r"\widetilde{\mathfrak{J}\otimes_S\mathfrak{K}}",
    "convention", 5, "high",
    r"\widetilde{\mathfrak{J}\otimes_S\mathfrak{K}}", r"(\mathfrak{J}\otimes_S\mathfrak{K})\supertilde", SUP5)
add(33, "after (2.5.11.3): 'et de (I, 1.3.13)'", "(I, 1.3.13) with bold I", "I, 1.3.13",
    "convention", 2, "high", r"{I, 1.3.13}", r"{\textbf{I}, 1.3.13}", "")
add(33, "diagram (2.5.11.4), top right", "(M\u2297_S N)~\u2297_{O_X}P\u0303", r"\widetilde{M\otimes_S N}\otimes_{\mathcal{O}_X}\widetilde{P}",
    "convention", 5, "high",
    r"\widetilde{M\otimes_S N}\otimes", r"(M\otimes_S N)\supertilde\otimes", SUP5)
add(33, "diagram (2.5.11.4), bottom left", "M\u0303\u2297_{O_X}(N\u2297_S P)~", r"\widetilde{N\otimes_S P}",
    "convention", 5, "high",
    r"\widetilde{N\otimes_S P}", r"(N\otimes_S P)\supertilde", SUP5)
add(33, "diagram (2.5.11.4), bottom right", "(M\u2297_S N\u2297_S P)~", r"\widetilde{M\otimes_S N\otimes_S P}",
    "convention", 5, "high",
    r"\widetilde{M\otimes_S N\otimes_S P}", r"(M\otimes_S N\otimes_S P)\supertilde", SUP5)

# ---------------- page 34 ----------------
add(34, "top of page: 'est commutatif. Il suffit encore ...'", "continues the sentence before diagram (2.5.11.4); line not indented, no new paragraph", "blank line after \\oldpage[II]{34} starts a new paragraph",
    "other", None, "high",
    L(r"\oldpage[II]{34}", "", "est commutatif."), L(r"\oldpage[II]{34}", "est commutatif."),
    "spurious paragraph break at the page marker (GLOBAL_ISSUES item 20)")
add(34, "end of (2.5.11): 'des d\u00e9finitions et de (I, 1.3.13)'", "(I, 1.3.13) with bold I", "I, 1.3.13",
    "convention", 2, "high", r"{I, 1.3.13}", r"{\textbf{I}, 1.3.13}", "")
add(34, "(2.5.12): 'compte tenu de (I, 1.3.8)'", "(I, 1.3.8) with bold I", "I, 1.3.8",
    "convention", 2, "high", r"{I, 1.3.8}", r"{\textbf{I}, 1.3.8}", "")
add(34, "(2.5.12.2)", "(Hom_S(M, N))~", r"\widetilde{\operatorname{Hom}_S(M,N)}",
    "convention", 5, "high",
    r"\widetilde{\operatorname{Hom}_S(M,N)}", r"(\operatorname{Hom}_S(M,N))\supertilde", SUP5)

DISP = "display in the TeX, inline in the print (cf. GLOBAL_ISSUES item 21); the whole proof of (2.5.13) on this page is set inline"
add(34, "proof of (2.5.13): 'application Z-bilin\u00e9aire M_m\u00d7N_n\u2192...'", "inline formula", "displayed formula",
    "other", None, "high",
    L(r"\[", r"  M_m\times N_n\longrightarrow", r"  M_{(f)}\otimes_{S_{(f)}}N_{(f)}", r"\]", ""),
    L(r"$M_m\times N_n\longrightarrow M_{(f)}\otimes_{S_{(f)}}N_{(f)}$", ""), DISP)
add(34, "proof of (2.5.13): 'application Z-lin\u00e9aire M\u2297_Z N\u2192...,'", "inline formula", "displayed formula",
    "other", None, "high",
    L(r"\[", r"  M\otimes_{\mathbf{Z}}N\longrightarrow", r"  M_{(f)}\otimes_{S_{(f)}}N_{(f)},", r"\]", ""),
    L(r"$M\otimes_{\mathbf{Z}}N\longrightarrow M_{(f)}\otimes_{S_{(f)}}N_{(f)}$,", ""), DISP)
add(34, "proof of (2.5.13): 'transforme (sx)\u2297y en (s/f^q)(...)'", "inline formula", "displayed formula",
    "other", None, "high",
    L(r"\[", r"  (s/f^q)\bigl((x/f^m)\otimes(y/f^n)\bigr)", r"\]", ""),
    L(r"$(s/f^q)\bigl((x/f^m)\otimes(y/f^n)\bigr)$", ""), DISP)
add(34, "proof of (2.5.13): 'di-homomorphisme de modules \u03b3_f : ...,'", "inline formula", "displayed formula",
    "other", None, "high",
    L(r"\[", r"  \gamma_f:M\otimes_S N\longrightarrow", r"  M_{(f)}\otimes_{S_{(f)}}N_{(f)},", r"\]", ""),
    L(r"$\gamma_f:M\otimes_S N\longrightarrow M_{(f)}\otimes_{S_{(f)}}N_{(f)}$,", ""), DISP)
add(34, "proof of (2.5.13): 'on ait f^r\u03a3(x_i\u2297y_i)=0,'", "inline formula", "displayed formula",
    "other", None, "high",
    L(r"\[", r"  f^r\sum_i(x_i\otimes y_i)=0,", r"\]", ""),
    L(r"$f^r\sum_i(x_i\otimes y_i)=0$,", ""), DISP)
add(34, "proof of (2.5.13): 'en vertu de (0, 1.3.4)'", "(0, 1.3.4) with bold 0", "0, 1.3.4",
    "convention", 2, "high", r"{0, 1.3.4}", r"{\textbf{0}, 1.3.4}", "")
add(34, "proof of (2.5.13): 'que l'on a \u03a3(f^r x_i/f^{m_i+r})\u2297(y_i/f^{n_i})=0,'", "inline formula", "displayed formula",
    "other", None, "high",
    L(r"\[", r"  \sum_i(f^rx_i/f^{m_i+r})\otimes(y_i/f^{n_i})=0,", r"\]", ""),
    L(r"$\sum_i(f^rx_i/f^{m_i+r})\otimes(y_i/f^{n_i})=0$,", ""), DISP)
add(34, "proof of (2.5.13): '\u03b3_f se factorise en M\u2297_S N\u2192(M\u2297_S N)_f\u2192M_(f)\u2297...;'", "inline formula", "displayed formula",
    "other", None, "high",
    L(r"\[", r"  M\otimes_S N\longrightarrow(M\otimes_S N)_f", r"  \xrightarrow{\gamma'_f}", r"  M_{(f)}\otimes_{S_{(f)}}N_{(f)}~;", r"\]", ""),
    L(r"$M\otimes_S N\longrightarrow(M\otimes_S N)_f\xrightarrow{\gamma'_f}M_{(f)}\otimes_{S_{(f)}}N_{(f)}$~;", ""), DISP)
add(34, "last line of the page: 'si \u03bb'_f est la restriction de \u03b3''", "\u03b3' (no subscript f)", r"\gamma'_f",
    "misprint_in_print", None, "high",
    r"restriction de $\gamma'_f$", r"restriction de $\gamma'$",
    "the print drops the subscript f (the map was just named gamma'_f; page 35 begins 'a (M (x)_S N)_(f)'); the TeX silently corrects it",
    corrected=r"\gamma'_f")

# ---------------- checks ----------------
ok = True
cache = {}
for f in F:
    p = f["page"]
    if p not in cache:
        with open(os.path.join(RUN, "page_%03d.tex" % p), "r", encoding="utf-8", newline="") as h:
            # page files are CRLF; the release files are LF: compare on LF
            cache[p] = h.read().replace("\r\n", "\n")
    t = cache[p]
    if "\r" in t:
        print("WARNING: stray CR in page", p)
    if f["fix"] is None:
        continue
    n = t.count(f["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE/ABSENT (%d) page %d: %r" % (n, p, f["fix"]["old"]))

# apply all fixes per page (sequentially) to check they do not interfere
for p, t in cache.items():
    s = t
    for f in F:
        if f["page"] == p and f["fix"] is not None:
            if s.count(f["fix"]["old"]) != 1:
                ok = False
                print("INTERFERENCE page %d: %r" % (p, f["fix"]["old"]))
            s = s.replace(f["fix"]["old"], f["fix"]["new"], 1)

from collections import Counter
cnt = Counter()
for f in F:
    k = "convention" if f["kind"] == "convention" else ("misprint" if f["kind"] == "misprint_in_print" else "normal")
    cnt[(f["page"], k)] += 1
for p in sorted({f["page"] for f in F}):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("total", len(F), "ok" if ok else "PROBLEMS")
if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as h:
        json.dump(F, h, ensure_ascii=False, indent=1)
    print("written", OUT)
