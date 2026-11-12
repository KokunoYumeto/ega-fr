# Applies the fixes of findings_070_074.json in order to a copy (in memory) of ega4-17-fr.tex
# and checks that each "old" occurs exactly once at the time it is applied. Writes nothing.
import json

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-17-fr.tex"

F = json.load(open(RUN + r"\findings_070_074.json", encoding="utf-8"))
s = open(SRC, encoding="utf-8", newline="").read()
ok = True
for i, d in enumerate(F):
    fx = d["fix"]
    if not fx:
        continue
    c = s.count(fx["old"])
    if c != 1:
        ok = False
        print("count", c, "at", i, d["page"], repr(fx["old"])[:80])
        continue
    s = s.replace(fx["old"], fx["new"], 1)

# brace balance in the edited segment pp. 70-75
a = s.find(r"\oldpage[IV-4]{70}")
b = s.find(r"\oldpage[IV-4]{75}")
seg = s[a:b]
depth = 0
for ch in seg:
    if ch == "{":
        depth += 1
    elif ch == "}":
        depth -= 1
        if depth < 0:
            break
print("brace depth at end:", depth, "dollar count even:", seg.replace(r"\$", "").count("$") % 2 == 0)
print("all applied" if ok else "PROBLEMS")
open(RUN + r"\crops_070_074\segment_after_fixes.txt", "w", encoding="utf-8", newline="\n").write(seg)
