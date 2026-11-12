import re, sys, pathlib, json
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
src = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega1\ega0-1-fr.tex"
t = src.read_text(encoding="utf-8")
pat = re.compile(r"\\oldpage\[0\\textsubscript\{I\}\]\{(\d+)\}")
rows = []
for m in pat.finditer(t):
    before = t[:m.start()]
    blank = before.endswith("\n\n")
    prev = before.rstrip("\n").rsplit("\n", 1)[-1]
    after = t[m.end():m.end() + 60].lstrip("\n").split("\n", 1)[0]
    rows.append((int(m.group(1)), blank, prev[-50:], after[:50]))
for r in rows:
    if r[1]:
        print(r)
print("markers:", len(rows), "with blank line before:", sum(1 for r in rows if r[1]))
# FIXLOG entries touching a blank line before a marker
n = 0
for name in ["FIXLOG.jsonl", "FIXLOG_CURRENT.jsonl"]:
    p = E / name
    if not p.exists():
        continue
    for line in p.read_text(encoding="utf-8").splitlines():
        try:
            x = json.loads(line)
        except Exception:
            continue
        if "\n\n\\oldpage" in (x.get("old") or "") or "\n\n\\oldpage" in (x.get("new") or ""):
            n += 1
            if n <= 8:
                print(name, x.get("page"), repr(x.get("old"))[:120], "->", repr(x.get("new"))[:120])
print("fixlog entries with blank+marker:", n)
