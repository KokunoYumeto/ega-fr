import json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
F = json.load(open(RUN / "findings_130_134.json", encoding="utf-8"))
for p in range(130, 135):
    t = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    for x in F:
        if x["page"] == p and x["fix"]:
            assert t.count(x["fix"]["old"]) == 1
            t = t.replace(x["fix"]["old"], x["fix"]["new"])
    (RUN / "crops_130_134" / f"preview_{p}.tex").write_text(t, encoding="utf-8")
    # dollar balance per paragraph (outside display math)
    for i, para in enumerate(t.split("\n\n")):
        n = para.replace("\$", "").count("$")
        if n % 2:
            print(f"p{p} paragraph {i}: odd number of $ ({n}):", para[:120].replace("\n", " | "))
    print(p, "\[", t.count("\["), "\]", t.count("\]"), "begin", t.count("\begin{"), "end", t.count("\end{"))
