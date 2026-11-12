import re
import sys

base = r"user/Documents/ega_scan_check_20261101/run_IVback/"
src = r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/"
alltex = ""
for f in ["ega4-16-fr.tex", "ega4-17-fr.tex", "ega4-18-fr.tex", "ega4-20-fr.tex",
          "ega4-21a-fr.tex", "ega4-21b-fr.tex", "ega4-21c-fr.tex"]:
    alltex += open(src + f, encoding="utf-8").read()
targets = set(re.findall(r"\\EGAReaderTarget\{([^}]*)\}", alltex))
targets |= set(re.findall(r"\\hypertarget\{([^}]*)\}", alltex))

pat = re.compile(r"\\EGAIVterm\{(.*?)\}\{\{\\hyperlink\{([^}]*)\}\{([^}]*)\}\}\}")
for p in [336, 337]:
    t = open(base + f"page_{p}.tex", encoding="utf-8").read()
    for m in pat.finditer(t):
        term, target, num = m.groups()
        tn = re.sub(r"^.*\.(\d+)-(\d+)-(\d+)$", r"\1.\2.\3", target)
        flag = "" if tn == num else "  <-- target/number mismatch"
        if target not in targets:
            flag += "  <-- target not found"
        sys.stdout.write(f"{p} {num:9} {term}{flag}\n")
