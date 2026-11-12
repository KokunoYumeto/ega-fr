"""Apply findings_010_014.json fixes to scratch copies (applied_NNN.tex here) and compare delimiter balance."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
here = Path(__file__).resolve().parent
run = here.parent
d = json.loads((run / "findings_010_014.json").read_text(encoding="utf-8"))


def bal(s):
    s2 = re.sub(r"\\[{}]", "", s)
    return {
        "braces": s2.count("{") - s2.count("}"),
        "left/right": s.count("\\left(") - s.count("\\right)"),
        "dollar_odd": s.count("$") % 2,
        "display": s.count("\\[") - s.count("\\]"),
        "parens": s.count("(") - s.count(")"),
    }


for p in range(10, 15):
    t = (run / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    o = t
    for x in d:
        if x["page"] == p and x["fix"]:
            assert t.count(x["fix"]["old"]) == 1
            t = t.replace(x["fix"]["old"], x["fix"]["new"])
    print(p, "orig", bal(o), "fixed", bal(t))
    (here / f"applied_{p:03d}.tex").write_text(t, encoding="utf-8", newline="\n")
