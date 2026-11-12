import sys, json
sys.dont_write_bytecode = True
sys.stdout.reconfigure(encoding="utf-8")

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex"
F = json.load(open(RUN + r"\findings_180_184.json", encoding="utf-8"))
src = open(SRC, encoding="utf-8", newline="").read()
text = src
ok = True
for i, d in enumerate(F):
    if not d["fix"]:
        continue
    o, n = d["fix"]["old"], d["fix"]["new"]
    c = text.count(o)
    if c != 1:
        ok = False
        print("FAIL at", i, d["page"], c, repr(o[:70]))
        continue
    text = text.replace(o, n)
print("all applied in order:", ok)
a = text.index("\\oldpage[IV-4]{179}")
b = text.index("\\oldpage[IV-4]{186}")
out = text[a:b]
open(RUN + r"\crops_180_184\simulated_179_185.txt", "w", encoding="utf-8", newline="\n").write(out)
# brace balance check per page segment
for p in range(180, 185):
    s = text[text.index(f"\\oldpage[IV-4]{{{p}}}"):text.index(f"\\oldpage[IV-4]{{{p+1}}}")]
    depth = 0
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "\\":
            i += 2
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        i += 1
    dollars = s.replace("\\$", "").count("$")
    print(p, "brace depth", depth, "dollars", dollars, "(even)" if dollars % 2 == 0 else "(ODD)")
