# 1) every fix "old" against its page_NNN.tex (CRLF -> LF); 2) a dry simulation of apply_fixes.py on an in-memory
# copy of the release file, in list order, with the same page-segment logic. Writes nothing.
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex")
items = json.load(open(RUN / "findings_100_104.json", encoding="utf-8"))
marker = re.compile(r"\\oldpage\[IV-2\]\{(\d+)\}")


def page_text(n):
    return (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")


print("== check 1: old in its own page_NNN.tex")
for i, x in enumerate(items):
    fx = x.get("fix")
    if not fx:
        continue
    c = page_text(x["page"]).count(fx["old"])
    if c != 1:
        other = {n: page_text(n).count(fx["old"]) for n in range(99, 106)}
        print(f"  #{i} p{x['page']} count={c} elsewhere={ {k: v for k, v in other.items() if v} } :: {fx['old'][:60]!r}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(t)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


print("== check 2: simulated application on the release file")
t = SRC.read_text(encoding="utf-8")
ok = bad = 0
for i, x in enumerate(items):
    fx = x.get("fix")
    if not fx:
        continue
    s, e = locate(t, int(x["page"]))
    seg = t[s:e]
    c = seg.count(fx["old"])
    if c != 1:
        bad += 1
        print(f"  #{i} p{x['page']} FAILS (count {c}) :: {fx['old'][:60]!r}")
        continue
    t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
    ok += 1
print(f"  applied {ok}, failed {bad}")
# show the resulting text at the page breaks and around the moved environments
for pat in [r"universellement\n\\oldpage\[IV-2\]\{100\}", r"est dominant\n\\oldpage", r"\\oldpage\[IV-2\]\{102\}",
            r"\\oldpage\[IV-2\]\{103\}", r"\\oldpage\[IV-2\]\{104\}", r"Cohen-Macaulay de \$X\$\.\n\\end",
            r"16\.5\.13\)\.", r"\\end\{definition\}\n\nOn dit que \$X\$", r"vérifie \$\(S_k\)\$\.\n"]:
    m = re.search(pat, t)
    if m:
        print("----", repr(t[max(0, m.start() - 80):m.end() + 90]))
    else:
        print("---- NOT FOUND", pat)
print("old p.100/101 markers left:", len(re.findall(r"\\oldpage\[IV-2\]\{100\}", t)), len(re.findall(r"\\oldpage\[IV-2\]\{101\}", t)))
print("begin/end definition balance:", t.count("\\begin{definition}"), t.count("\\end{definition}"))
