"""Apply findings_300_304.json in order to copies of the current ega4-21b/21c sources and build a compile stub.

Writes sim_ega4-21b.tex, sim_ega4-21c.tex and stub_sim.tex into this folder (no source file is touched)."""
import io, json, sys, shutil

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
HERE = r"user/Documents/ega_scan_check_20261101/run_IV4/crops_300_304/"
RUN = r"user/Documents/ega_scan_check_20261101/run_IV4/"
SRC = r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/"


def read(p):
    with open(p, encoding='utf-8', newline='') as f:
        return f.read().replace('\r\n', '\n')


F = json.load(open(RUN + "findings_300_304.json", encoding="utf-8"))
txt = {"b": read(SRC + "ega4/ega4-21b-fr.tex"), "c": read(SRC + "ega4/ega4-21c-fr.tex")}
ok = True
for i, d in enumerate(F):
    fx = d["fix"]
    if not fx:
        continue
    hits = [k for k in "bc" if fx["old"] in txt[k]]
    if len(hits) != 1 or txt[hits[0]].count(fx["old"]) != 1:
        ok = False
        print("NOT UNIQUE AT APPLICATION", i, d["page"], repr(fx["old"][:60]), [(k, txt[k].count(fx["old"])) for k in "bc"])
        continue
    k = hits[0]
    txt[k] = txt[k].replace(fx["old"], fx["new"])
print("sequential application ok:", ok)
for k in "bc":
    with open(HERE + "sim_ega4-21%s.tex" % k, "w", encoding="utf-8", newline="\n") as f:
        f.write(txt[k])
pre = read(SRC + "ega4/EGA_IV4_FR.tex")
pre = pre[:pre.index("\\begin{document}")]
stub = pre + "\\begin{document}\n\\input{sim_ega4-21b.tex}\n\\input{sim_ega4-21c.tex}\n\\end{document}\n"
with open(HERE + "stub_sim.tex", "w", encoding="utf-8", newline="\n") as f:
    f.write(stub)
shutil.copy(SRC + "preamble-base.tex", HERE + "preamble-base.tex")
print("stub written")
