"""Check the index/contents hyperlinks of pages 338-343 against the IV-4 sources (read-only).
For every \\EGAIVterm entry: target exists, target number = link text.
For every contents line: target exists, and the printed page number vs the last \\oldpage marker before the
subsection heading (or section heading) in the sources."""
import re
import sys

src = r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/"
base = r"user/Documents/ega_scan_check_20261101/run_IVback/"
files = ["ega4-16-fr.tex", "ega4-17-fr.tex", "ega4-18-fr.tex", "ega4-20-fr.tex",
         "ega4-21a-fr.tex", "ega4-21b-fr.tex", "ega4-21c-fr.tex"]
texts = {f: open(src + f, encoding="utf-8").read() for f in files}
alltex = "".join(texts.values())
targets = set(re.findall(r"\\EGAReaderTarget\{([^}]*)\}", alltex))
targets |= set(re.findall(r"\\hypertarget\{([^}]*)\}", alltex))

out = []
pat = re.compile(r"\\EGAIVterm\{(.*?)\}\{(.*)\}\s*$")
link = re.compile(r"\\hyperlink\{([^}]*)\}\{([^}]*)\}")
for p in [338, 339]:
    for line in open(base + f"page_{p}.tex", encoding="utf-8").read().splitlines():
        m = pat.match(line)
        if not m:
            continue
        term, refs = m.groups()
        for t, num in link.findall(refs):
            tn = re.sub(r"^.*\.(\d+(?:-\d+)*)$", r"\1", t).replace("-", ".")
            flag = "" if tn == num else "  <-- target/number mismatch"
            if t not in targets:
                flag += "  <-- target not found"
            out.append(f"{p} {num:9} {t:40} {term}{flag}")

# page of each target: last \oldpage marker before the target in its file
mk = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")


def page_of(target):
    for f, t in texts.items():
        i = t.find("\\EGAReaderTarget{" + target + "}")
        if i < 0:
            i = t.find("\\hypertarget{" + target + "}")
        if i < 0:
            continue
        last = None
        for m in mk.finditer(t, 0, i):
            last = m.group(1)
        # look at the text between the last marker and the target: only blank lines / labels?
        return f, last, i
    return None, None, None


for p in [341, 342, 343]:
    for line in open(base + f"page_{p}.tex", encoding="utf-8").read().splitlines():
        if not line.startswith("\\EGAIVcontentsline"):
            continue
        ts = link.findall(line)
        pg = re.search(r"\}\{(\d+)\}\s*$", line)
        pg = pg.group(1) if pg else "?"
        if ts:
            t, num = ts[0]
            f, last, i = page_of(t)
            flag = "" if (last == pg) else f"  <-- marker page {last}"
            if t not in targets:
                flag += "  <-- target not found"
            out.append(f"{p} contents {num:6} printed p. {pg:4} file {f} {flag}")
        else:
            out.append(f"{p} contents (no link) {line[:90]}")
sys.stdout.write("\n".join(out) + "\n")
