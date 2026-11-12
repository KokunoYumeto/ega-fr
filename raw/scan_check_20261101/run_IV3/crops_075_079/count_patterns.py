import glob, os, re, sys

base = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\current\packages\IV3\native\ega4"
pats = {
    "n$^\\circ$": re.compile(re.escape("n$^\\circ$")),
    "n\\textsuperscript{o}": re.compile(re.escape("n\\textsuperscript{o}")),
    "_{(\\boldsymbol{k}": re.compile(re.escape("_{(\\boldsymbol{k}")),
    "_{\\boldsymbol{k}": re.compile(re.escape("_{\\boldsymbol{k}")),
    "\\otimes_{\\boldsymbol{k}": re.compile(re.escape("\\otimes_{\\boldsymbol{k}")),
    "_{(\\mathbf{k}": re.compile(re.escape("_{(\\mathbf{k}")),
    "\\boldsymbol{k} total": re.compile(re.escape("\\boldsymbol{k}")),
    "irrédondant": re.compile("irrédondant"),
    "irredondant": re.compile("irredondant"),
    "\\mathbf P": re.compile(r"\\mathbf\s*\{?P\b"),
    "label=\\emph{\\alph*)}": re.compile(re.escape("label=\\emph{\\alph*)}")),
    "label=(\\roman*)": re.compile(re.escape("label=(\\roman*)")),
}
for f in sorted(glob.glob(os.path.join(base, "ega4-*.tex"))):
    t = open(f, encoding="utf-8").read()
    print(os.path.basename(f), {k: len(p.findall(t)) for k, p in pats.items()})
