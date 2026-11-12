import json, pathlib, sys
RUN = pathlib.Path(sys.argv[1])
L = json.load(open(RUN / "findings_145_149.json", encoding="utf-8"))
pages = {}
for x in L:
    p = x["page"]
    if p not in pages:
        pages[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
ok = True
for x in L:
    fx = x["fix"]
    if not fx:
        continue
    t = pages[x["page"]]
    n = t.count(fx["old"])
    if n != 1:
        ok = False
        print("SEQ FAIL", x["page"], n, repr(fx["old"][:70]))
        continue
    pages[x["page"]] = t.replace(fx["old"], fx["new"])
print("sequential application ok:", ok)
for p, t in sorted(pages.items()):
    out = RUN / "crops_145_149" / f"sim_page_{p:03d}.tex"
    out.write_text(t, encoding="utf-8")
    # brace balance (ignoring escaped braces)
    s = t.replace("\{", "").replace("\}", "")
    print(p, "braces", s.count("{") - s.count("}"), "dollars", (t.count("$") - t.count("\$")) % 2)
