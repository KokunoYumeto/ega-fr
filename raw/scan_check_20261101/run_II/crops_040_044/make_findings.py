"""Build findings_040_044.json and check every fix's "old" (once in page_NNN.tex and once in the release segment)."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\BASE\native\ega2\ega2-1-fr.tex")
OUT = RUN / "findings_040_044.json"
N = "\n"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, seg_page=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=(dict(old=old, new=new) if old is not None else None))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    d["_seg_page"] = seg_page or page
    F.append(d)


def c2(page, where, ref, note=""):
    num = ref.split(", ")[1]
    ch = ref.split(", ")[0]
    add(page, where, "(" + ch + ", " + num + ") with bold " + ch, "{" + ref + "}", "convention", 2, "high",
        "{" + ref + "}", r"{\textbf{" + ch + "}, " + num + "}", note)


def c6ref(page, where, scan, old, new, note="Reference printed upright (roman parentheses and figures) inside the "
                                            "italic statement; italic in the TeX environment."):
    add(page, where, scan, old, "convention", 6, "high", old, new, note)


# ---------------- page 40 ----------------
add(40, "page break 39/40 (blank line before \\oldpage[II]{40})",
    "'... il est clair alors' (end of p. 39) continues 'que si k>m' at the top of p. 40: one paragraph",
    "il est clair\\nalors\\n\\n\\oldpage[II]{40}", "other", None, "high",
    "il est clair" + N + "alors" + N + N, "il est clair" + N + "alors" + N,
    "Spurious paragraph break at the page boundary (GLOBAL_ISSUES item 20). The 'old' lies at the end of page 39's "
    "segment (page_039.tex, release ega2-1-fr.tex), not in page_040.tex; it occurs once there. The page-39 checker "
    "may report the same edit.", seg_page=39)
add(40, "Théorème (2.7.5), statement", "β : (Γ_*(ℱ))~ → ℱ  (tilde after the parenthesis)",
    r"\beta:\widetilde{\Gamma_*(\mathcal{F})}", "convention", 5, "high",
    r"\beta:\widetilde{\Gamma_*(\mathcal{F})}", r"\beta:(\Gamma_*(\mathcal{F}))\supertilde",
    "The TeX also drops the printed outer parentheses.")
c6ref(40, "Théorème (2.7.5), statement", "(2.6.4) upright", r"(\hyperref[II.2.6.4-fr]{2.6.4})",
      r"\textup{(\hyperref[II.2.6.4-fr]{2.6.4})}")
add(40, "proof of (2.7.5), l. 4", "pour tout f∈S_d (d>0) un isomorphisme canonique  (no comma after (d>0))",
    r"($d>0$), un isomorphisme", "misprint_in_print", None, "high",
    r"($d>0$), un", r"($d>0$) un",
    "The print opens the incise with 'on a, pour tout f∈S_d (d>0)' and omits the closing comma (checked on a crop). "
    "The TeX silently supplies it; the fix restores the printed reading.",
    corrected=r"($d>0$), un")
c2(40, "proof of (2.7.5), l. 3", "I, 9.3.2")
c2(40, "proof of (2.7.5), next to last line", "I, 9.3.1")
c6ref(40, "Corollaire (2.7.7), l. 1", "(2.7.5) upright",
      "II.2.7.7-fr}" + N + r"Sous les hypothèses de (\hyperref[II.2.7.5-fr]{2.7.5})",
      "II.2.7.7-fr}" + N + r"Sous les hypothèses de \textup{(\hyperref[II.2.7.5-fr]{2.7.5})}")
c6ref(40, "Corollaire (2.7.8), l. 1", "(2.7.5) upright",
      "II.2.7.8-fr}" + N + r"Sous les hypothèses de (\hyperref[II.2.7.5-fr]{2.7.5})",
      "II.2.7.8-fr}" + N + r"Sous les hypothèses de \textup{(\hyperref[II.2.7.5-fr]{2.7.5})}")
add(40, "proof of (2.7.8), l. 5", "sous-𝒪_X-Modules M̃_H (2.5.4)  (tilde over M only)",
    r"$\widetilde{M_H}$", "convention", 8, "high",
    r"$\widetilde{M_H}$ (", r"$\widetilde{M}_H$ (", "")
c2(40, "proof of (2.7.8), last line", "0, 5.2.3")
add(40, "proof of (2.7.8), last line", "ℱ = M̃_H pour une partie finie  (tilde over M only)",
    r"\mathcal{F}=\widetilde{M_H}$", "convention", 8, "high",
    r"=\widetilde{M_H}$", r"=\widetilde{M}_H$", "")
c6ref(40, "Corollaire (2.7.9), l. 1", "(2.7.5) upright",
      "II.2.7.9-fr}" + N + r"Sous les hypothèses de (\hyperref[II.2.7.5-fr]{2.7.5})",
      "II.2.7.9-fr}" + N + r"Sous les hypothèses de \textup{(\hyperref[II.2.7.5-fr]{2.7.5})}")
add(40, "Corollaire (2.7.9), last line", "X (0, 5.1.1): bold 0, reference upright",
    r"(\hyperref[0.5.1.1-fr]{0, 5.1.1})", "convention", 2, "high",
    r"(\hyperref[0.5.1.1-fr]{0, 5.1.1})", r"\textup{(\hyperref[0.5.1.1-fr]{\textbf{0}, 5.1.1})}",
    "Bold 0 in the print; the reference is also upright inside the italic statement (convention 6), so the fix "
    "sets both.")
add(40, "proof of (2.7.9), l. 3", "ℱ(n) = (S(m+n))~ = 𝒪_X(m+n)",
    r"\widetilde{S(m+n)}", "convention", 5, "high",
    r"\widetilde{S(m+n)}", r"(S(m+n))\supertilde", "The TeX also drops the printed outer parentheses.")

# ---------------- page 41 ----------------
c6ref(41, "Lemme (2.7.9.1), l. 1", "(2.7.5) upright",
      r"(\hyperref[II.2.7.5-fr]{2.7.5}), pour tout", r"\textup{(\hyperref[II.2.7.5-fr]{2.7.5})}, pour tout")
add(41, "proof of (2.7.9.1), l. 3", "SS_n = S_n + S_{n+1} + . . . .  (baseline dots)",
    r"S_{n+1}+\cdots$", "symbol", None, "high", r"S_{n+1}+\cdots$", r"S_{n+1}+\ldots$",
    "Dots on the baseline in the print (checked on a crop), as treated at EGA I p. 113.")
add(41, "proof of (2.7.9.1), last line", "(S(n))_{-n} + . . . + (S(n))_{-1}  (baseline dots)",
    r"(S(n))_{-n}+\cdots+", "symbol", None, "high", r"(S(n))_{-n}+\cdots+", r"(S(n))_{-n}+\ldots+",
    "Dots on the baseline in the print (checked on a crop).")
c6ref(41, "Corollaire (2.7.10), l. 1", "(2.7.5) upright",
      r"(\hyperref[II.2.7.5-fr]{2.7.5}), soit $\mathcal{F}$",
      r"\textup{(\hyperref[II.2.7.5-fr]{2.7.5})}, soit $\mathcal{F}$")
c6ref(41, "Proposition (2.7.11), l. 1", "(2.7.5) upright",
      r"(\hyperref[II.2.7.5-fr]{2.7.5}) et soit $M$", r"\textup{(\hyperref[II.2.7.5-fr]{2.7.5})} et soit $M$")
add(41, "Proposition (2.7.11) (i)", "α̃ : M̃ → (Γ_*(M̃))~",
    r"\widetilde{\Gamma_*(\widetilde{M})}", "convention", 5, "high",
    r"\widetilde{\Gamma_*(\widetilde{M})}$ est un isomorphisme.",
    r"(\Gamma_*(\widetilde{M}))\supertilde$ est un isomorphisme.",
    "The TeX also drops the printed outer parentheses.")
c6ref(41, "Proposition (2.7.11) (ii)", "en vertu de (2.5.4) upright",
      r"(\hyperref[II.2.5.4-fr]{2.5.4}), à un", r"\textup{(\hyperref[II.2.5.4-fr]{2.5.4})}, à un")
add(41, "proof of (2.7.11), l. 1", "β : (Γ_*(M̃))~ → M̃",
    r"\beta:\widetilde{\Gamma_*(\widetilde{M})}", "convention", 5, "high",
    r"\beta:\widetilde{\Gamma_*(\widetilde{M})}", r"\beta:(\Gamma_*(\widetilde{M}))\supertilde",
    "The TeX also drops the printed outer parentheses.")
add(41, "proof of (2.7.11), l. 3", "comme M̃ est un foncteur exact (2.5.4)",
    r"comme $M\mapsto\widetilde{M}$ est un foncteur exact", "extra", None, "high",
    r"$M\mapsto\widetilde{M}$ est un foncteur", r"$\widetilde{M}$ est un foncteur",
    "The print has only M̃ (checked on a crop); the TeX adds 'M\\mapsto'.")
add(41, "proof of (2.7.11), l. 4", "P̃ = (Γ_*(M̃))~",
    r"\widetilde{P}=\widetilde{\Gamma_*(\widetilde{M})}", "convention", 5, "high",
    r"\widetilde{P}=\widetilde{\Gamma_*(\widetilde{M})}", r"\widetilde{P}=(\Gamma_*(\widetilde{M}))\supertilde",
    "The TeX also drops the printed outer parentheses.")
add(41, "proof of (2.7.11), l. 5", "Q̃ = (Γ_*(𝒢))~",
    r"\widetilde{Q}=\widetilde{\Gamma_*(\mathcal{G})}", "convention", 5, "high",
    r"\widetilde{Q}=\widetilde{\Gamma_*(\mathcal{G})}", r"\widetilde{Q}=(\Gamma_*(\mathcal{G}))\supertilde",
    "The TeX also drops the printed outer parentheses.")
c2(41, "(2.8.1), l. 5", "I, 1.2.1")
c2(41, "(2.8.1), after (2.8.1.1)", "I, 1.2.2.2")
add(41, "page break 41/42 (last line of p. 41)",
    "'... aux éléments de degré 0,' continues 'un homomorphisme ...' at the top of p. 42: one paragraph",
    "degré $0$,\\n\\n\\oldpage[II]{42}", "other", None, "high",
    "degré $0$," + N + N, "degré $0$," + N,
    "Spurious paragraph break inside (2.8.1) at the page boundary (GLOBAL_ISSUES item 20).")

# ---------------- page 42 ----------------
c2(42, "(2.8.1), l. 1", "I, 1.6.1")
add(42, "Proposition (2.8.2), l. 2", "(dit associé à φ et noté Proj(φ)): '(dit' roman, 'associé à φ et noté' italic",
    "(dit \\emph{associé à $\\varphi$} et noté", "convention", 6, "high",
    "(dit ", r"\textup{(dit} ",
    "Checked on a crop: '(dit' is roman inside the italic statement; italic in the TeX environment. Independent of "
    "the next finding (non-overlapping strings).")
add(42, "Proposition (2.8.2), l. 2", "associé à φ printed in the same italic as the statement",
    "\\emph{associé à\\n$\\varphi$}", "convention", 6, "high",
    r"\emph{associé à" + N + r"$\varphi$}", r"associé à" + N + r"$\varphi$",
    "Checked on a crop: no change of face; \\emph inside the italic proposition environment sets it upright.")
add(42, "diagram (2.8.2.1), left vertical arrow", "vertical arrow with ≀ on its left",
    r"\ar[d]_{\sim}", "symbol", None, "medium", r"\ar[d]_{\sim}", r"\ar[d]_{\wr}",
    "The print marks the vertical isomorphisms with a vertical tilde ≀ (checked on a crop); \\sim gives a "
    "horizontal ∼.")
add(42, "diagram (2.8.2.1), right vertical arrow", "vertical arrow with ≀ on its left",
    r"\ar[d]^{\sim}", "symbol", None, "medium", r"\ar[d]^{\sim}", r"\ar[d]_{\wr}",
    "As the left arrow: ≀, and printed on the left of the arrow (the TeX puts the label on the right).")
c2(42, "proof of (2.8.3), last line", "I, 1.2.7")

# ---------------- page 43 ----------------
add(43, "first paragraph, l. 4", "(cf. 3.1.7));  (no parentheses around 3.1.7)",
    r"(cf. (\hyperref[II.3.1.7-fr]{3.1.7})))", "punctuation", None, "high",
    r"(cf. (\hyperref[II.3.1.7-fr]{3.1.7})))", r"(cf. \hyperref[II.3.1.7-fr]{3.1.7}))",
    "Checked on a crop: the TeX adds a pair of parentheses around the reference.")
c2(43, "first paragraph, last line", "I, 2.3.2")
c2(43, "(2.8.6), l. 3", "0, 1.5.2")
add(43, "(2.8.6), last line", "(M_{[φ]})~|D_+(f') ⥲ (Φ_f)_*(M̃|D_+(f))",
    r"\widetilde{M_{[\varphi]}}|D_+(f')", "convention", 5, "high",
    r"\widetilde{M_{[\varphi]}}|D_+(f')", r"(M_{[\varphi]})\supertilde|D_+(f')",
    "The TeX also drops the printed parentheses.")
c2(43, "(2.8.6), last line", "I, 1.6.3")
add(43, "page break 43/44 (last line of p. 43)",
    "'En outre,' continues 'si g' est un second élément ...' at the top of p. 44: one paragraph",
    "En outre,\\n\\n\\oldpage[II]{44}", "other", None, "high",
    "En outre," + N + N, "En outre," + N,
    "Spurious paragraph break inside (2.8.6) at the page boundary (GLOBAL_ISSUES item 20).")

# ---------------- page 44 ----------------
add(44, "display after the first diagram", "(M_{[φ]})~|D_+(f'g') ⥲ (Φ_{fg})_*(M̃|D_+(fg))",
    r"\widetilde{M_{[\varphi]}}|D_+(f'g')", "convention", 5, "high",
    r"\widetilde{M_{[\varphi]}}|D_+(f'g')", r"(M_{[\varphi]})\supertilde|D_+(f'g')",
    "The TeX also drops the printed parentheses.")
add(44, "(2.8.6), l. after the display", "(M_{[φ]})~|D_+(f') ⥲ (Φ_f)_*(M̃|D_+(f))",
    r"\widetilde{M_{[\varphi]}}|D_+(f')", "convention", 5, "high",
    r"\widetilde{M_{[\varphi]}}|D_+(f')", r"(M_{[\varphi]})\supertilde|D_+(f')",
    "The TeX also drops the printed parentheses.")
add(44, "Proposition (2.8.7)", "du 𝒪_{X'}-Module (M_{[φ]})~ sur le",
    r"$\widetilde{M_{[\varphi]}}$ sur le", "convention", 5, "high",
    r"$\widetilde{M_{[\varphi]}}$ sur le", r"$(M_{[\varphi]})\supertilde$ sur le",
    "The TeX also drops the printed parentheses.")
add(44, "paragraph after (2.8.7), l. 3", "Φ-morphismes M̃' → M̃|G(φ)  (tilde over M, prime after it)",
    r"\widetilde{M'}\to\widetilde{M}|G(\varphi)$", "convention", 8, "high",
    r"\widetilde{M'}\to\widetilde{M}|G(\varphi)$", r"\widetilde{M}'\to\widetilde{M}|G(\varphi)$",
    "Checked on a crop.")
add(44, "paragraph after (2.8.7), l. 6", "M̃'|G(φ') → M̃|G(φ'')",
    r"\widetilde{M'}|G(\varphi')\to", "convention", 8, "high",
    r"\widetilde{M'}|G(\varphi')\to", r"\widetilde{M}'|G(\varphi')\to", "Checked on a crop.")
add(44, "paragraph after (2.8.7), last line", "M̃'' → M̃'|G(φ')  (first term)",
    r"\widetilde{M''}", "convention", 8, "high", r"\widetilde{M''}", r"\widetilde{M}''", "Checked on a crop.")
add(44, "paragraph after (2.8.7), last line", "M̃'' → M̃'|G(φ')  (second term)",
    r"\to\widetilde{M'}|G(\varphi')$.", "convention", 8, "high",
    r"\to\widetilde{M'}|G(\varphi')$.", r"\to\widetilde{M}'|G(\varphi')$.", "Checked on a crop.")
c6ref(44, "Proposition (2.8.8), l. 1", "(2.8.1) upright",
      r"(\hyperref[II.2.8.1-fr]{2.8.1})", r"\textup{(\hyperref[II.2.8.1-fr]{2.8.1})}")
add(44, "Proposition (2.8.8), l. 2", "Φ*(M̃')  (tilde over M, prime after it)",
    r"\Phi^*(\widetilde{M'})$ dans", "convention", 8, "high",
    r"\Phi^*(\widetilde{M'})$ dans", r"\Phi^*(\widetilde{M}')$ dans", "Checked on a crop.")
add(44, "Proposition (2.8.8), l. 3", "(M'⊗_{S'}S)~|G(φ)",
    r"\widetilde{M'\otimes_{S'}S}|G(\varphi)$", "convention", 5, "high",
    r"\widetilde{M'\otimes_{S'}S}|G(\varphi)$", r"(M'\otimes_{S'}S)\supertilde|G(\varphi)$",
    "The TeX also drops the printed parentheses (checked on a crop).")
c2(44, "proof of (2.8.8), after (2.8.8.1)", "0, 1.5.4")
add(44, "proof of (2.8.8), display defining ν", "ν : Φ*(M̃') → (M'⊗_{S'}S)~|G(φ)  (M̃')",
    r"\nu:\Phi^*(\widetilde{M'})", "convention", 8, "high",
    r"\nu:\Phi^*(\widetilde{M'})", r"\nu:\Phi^*(\widetilde{M}')", "Checked on a crop.")
add(44, "proof of (2.8.8), display defining ν", "ν : Φ*(M̃') → (M'⊗_{S'}S)~|G(φ)  ((…)~)",
    r"\longrightarrow\widetilde{M'\otimes_{S'}S}", "convention", 5, "high",
    r"\longrightarrow\widetilde{M'\otimes_{S'}S}", r"\longrightarrow(M'\otimes_{S'}S)\supertilde",
    "The TeX also drops the printed parentheses (checked on a crop).")
c2(44, "proof of (2.8.8), after the display", "I, 1.6.5")
add(44, "proof of (2.8.8), 'Pour prouver la seconde assertion'", "pour tout f'∈S_1,  (S without prime)",
    r"$f'\in S'_1$", "misprint_in_print", None, "high",
    r"$f'\in S'_1$, puisque", r"$f'\in S_1$, puisque",
    "Checked on a crop: the print has S_1. Since f' lies in S' and the hypothesis is that S'_+ is generated by "
    "S'_1, the correct reading is S'_1. The TeX silently corrects it; the fix restores the printed reading.",
    corrected=r"$f'\in S'_1$")
add(44, "page break 44/45 (last line of p. 44)",
    "'x'/f'^m est f'^{-m}x'/1' continues 'lorsque m<0)' at the top of p. 45: one paragraph",
    "${f'}^{-m}x'/1$\\n\\n\\oldpage[II]{45}", "other", None, "high",
    r"${f'}^{-m}x'/1$" + N + N, r"${f'}^{-m}x'/1$" + N,
    "Spurious paragraph break inside the proof of (2.8.8) at the page boundary (GLOBAL_ISSUES item 20).")

# ---------------- checks ----------------
rel = REL.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(rel)]


def segment(page):
    for i, (n, s) in enumerate(cuts):
        if n == page:
            return rel[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(rel)]
    raise KeyError(page)


ok = True
for d in F:
    sp = d.pop("_seg_page")
    fx = d["fix"]
    if not fx:
        continue
    pf = (RUN / f"page_{sp:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    a = pf.count(fx["old"])
    b = segment(sp).count(fx["old"])
    own = (RUN / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n").count(fx["old"])
    flag = "" if (a == 1 and b == 1) else "  <-- PROBLEM"
    if flag:
        ok = False
    print(f"p{d['page']} (seg {sp}) page_file={a} release_seg={b} own_page_file={own} | {fx['old'][:60]!r}{flag}")

# overlap check within a page: no two olds may overlap in the release segment
from collections import defaultdict
by = defaultdict(list)
for d in F:
    if d["fix"]:
        by[d["page"]].append(d["fix"]["old"])
for p, olds in by.items():
    seg = segment(p) if p != 40 else segment(40)
    spans = []
    for o in olds:
        i = seg.find(o)
        if i >= 0:
            spans.append((i, i + len(o), o[:30]))
    spans.sort()
    for x, y in zip(spans, spans[1:]):
        if y[0] < x[1]:
            ok = False
            print("OVERLAP on page", p, x, y)

json.dump(F, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter((d["page"], "convention" if d["kind"] == "convention" else
               ("misprint" if d["kind"] == "misprint_in_print" else "normal")) for d in F)
for p in range(40, 45):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("ALL OK" if ok else "CHECK FAILED", len(F), "findings ->", OUT)
