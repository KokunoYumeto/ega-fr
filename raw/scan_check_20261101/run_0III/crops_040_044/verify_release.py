# Check the findings against the current release file, page segment by page segment,
# exactly as apply_fixes.py will locate them (old must occur once in its page segment).
import json, re, pathlib, random
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
REL = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega3\ega3-1-fr.tex"
t = REL.read_text(encoding="utf-8")
part = r"0\textsubscript{III}"
marker = re.compile(r"\\oldpage\[" + re.escape(part) + r"\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
seg = {}
for i, (n, s) in enumerate(cuts):
    seg[n] = t[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(t)]
F = json.load(open(E / r"run_0III\findings_040_044.json", encoding="utf-8"))
for p in range(40, 45):
    page = (E / (r"run_0III\page_%03d.tex" % p)).read_text(encoding="utf-8").replace("\r\n", "\n")
    body = page.split("\n", 1)[1]  # drop the '% from ...' line
    same = body.rstrip("\n") == seg[p].rstrip("\n")
    print("p.%d: page extract equals release segment: %s" % (p, same))
bad = 0
for x in F:
    f = x["fix"]
    if not f:
        continue
    n = seg[x["page"]].count(f["old"])
    if n != 1:
        bad += 1
        print("p.%d old occurs %d times in the release segment: %r" % (x["page"], n, f["old"][:80]))
print("findings not applicable by apply_fixes.py:", bad)
# simulate apply_fixes.py on a copy, in file order and in random orders
for trial in range(20):
    tt = t
    order = F[:]
    if trial:
        random.Random(trial).shuffle(order)
    fails = 0
    for x in order:
        f = x["fix"]
        if not f:
            continue
        cs = [(int(m.group(1)), m.start()) for m in marker.finditer(tt)]
        d = dict((n, (s, cs[i + 1][1] if i + 1 < len(cs) else len(tt))) for i, (n, s) in enumerate(cs))
        s, e = d[x["page"]]
        sg = tt[s:e]
        if sg.count(f["old"]) != 1:
            fails += 1
            continue
        tt = tt[:s] + sg.replace(f["old"], f["new"]) + tt[e:]
    if trial == 0:
        print("simulated apply, file order: failures =", fails)
        out = E / r"run_0III\crops_040_044\ega3-1-fr_simulated.tex"
        out.write_text(tt, encoding="utf-8", newline="")
    elif fails:
        print("simulated apply, shuffled order %d: failures = %d" % (trial, fails))
print("done")
