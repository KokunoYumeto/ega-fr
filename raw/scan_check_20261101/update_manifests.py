"""Refresh "bytes" and "sha256" of changed files in the ega-fr manifests (package MANIFEST.json, edition and root
SOURCE_MANIFEST.json). A manifest entry is any JSON object with "path" and "sha256"; its path is resolved against the
manifest's own folder (falling back to the repository root). Only files listed in CHANGED (repository-relative paths
from `git diff --name-only`) are touched; the hash is of the file's bytes as stored (LF), upper-case hex.
usage: python -I update_manifests.py CHANGED_LIST.txt"""
import hashlib
import json
import pathlib
import sys

G = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr")
changed = {(G / ln.strip()).resolve() for ln in open(sys.argv[1], encoding="utf-8") if ln.strip()}
manifests = [G / "SOURCE_MANIFEST.json"] + sorted(G.glob("editions/2026-10-24-r20/*/SOURCE_MANIFEST.json")) + \
    sorted(G.glob("editions/2026-10-24-r20/*/packages/*/MANIFEST.json"))
total = 0
for mf in manifests:
    data = json.loads(mf.read_text(encoding="utf-8"))
    n = 0

    def walk(o):
        global n
        if isinstance(o, dict):
            if "path" in o and "sha256" in o:
                for base in (mf.parent, G):
                    p = (base / o["path"]).resolve()
                    if p in changed and p.exists():
                        b = p.read_bytes()
                        upper = o["sha256"].isupper()
                        h = hashlib.sha256(b).hexdigest()
                        o["sha256"] = h.upper() if upper else h
                        if "bytes" in o:
                            o["bytes"] = len(b)
                        n += 1
                        break
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(data)
    if n:
        raw = mf.read_text(encoding="utf-8")
        indent = 2 if '\n  "' in raw[:200] else 1
        mf.write_text(json.dumps(data, ensure_ascii=False, indent=indent) + ("\n" if raw.endswith("\n") else ""),
                      encoding="utf-8", newline="")
    print(mf.relative_to(G), n, "entries updated")
    total += n
print("total", total)
