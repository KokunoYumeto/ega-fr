"""Flatten a LaTeX master: replace every \\input{X} / \\include{X} (outside comments) by the contents of X(.tex), resolved
relative to the master's folder, recursively. A unit macro defined as \\newcommand{\\NAME}[1]{\\input{PRE#1SUF}} (as in
the Spanish EGA III-2: \\EGAUnit{III.6.1}) is expanded the same way, and its definition line is left empty, as in the
published readers.  usage: python -I flatten_tex.py MASTER OUT [--crlf]"""
import pathlib
import re
import sys

INPUT = re.compile(r"\\(?:input|include)\{([^}]+)\}")
UNITDEF = re.compile(r"^\\newcommand\{\\([A-Za-z]+)\}\[1\]\{\\input\{([^}#]*)#1([^}]*)\}\}[ \t]*$", re.M)


def resolve(name, root, here):
    for c in (root / name, root / (name + ".tex"), here / name, here / (name + ".tex")):
        if c.is_file():
            return c
    return None


def flatten(path, root, units=None):
    t = path.read_text(encoding="utf-8")
    units = dict(units or {})
    for m in UNITDEF.finditer(t):
        units[m.group(1)] = (m.group(2), m.group(3))
    t = UNITDEF.sub("", t)
    pats = [INPUT] + [re.compile(re.escape("\\" + n) + r"\{([^}]+)\}") for n in units]
    out, pos = [], 0
    while True:
        best = None
        for p in pats:
            m = p.search(t, pos)
            if m and (best is None or m.start() < best[0].start()):
                best = (m, p)
        if not best:
            break
        m, p = best
        line_start = t.rfind("\n", 0, m.start()) + 1
        if re.search(r"(?<!\\)%", t[line_start:m.start()]):
            out.append(t[pos:m.end()])
            pos = m.end()
            continue
        if p is INPUT:
            name = m.group(1).strip()
        else:
            macro = m.group(0)[1:m.group(0).index("{")]
            pre, suf = units[macro]
            name = pre + m.group(1).strip() + suf
        f = resolve(name, root, path.parent)
        if f is None:
            out.append(t[pos:m.end()])
            pos = m.end()
            continue
        out.append(t[pos:m.start()])
        body = flatten(f, root, units)
        out.append(body if body.endswith("\n") else body + "\n")
        pos = m.end()
    out.append(t[pos:])
    return "".join(out)


if __name__ == "__main__":
    master = pathlib.Path(sys.argv[1])
    s = flatten(master, master.parent)
    if "--crlf" in sys.argv:
        s = s.replace("\r\n", "\n").replace("\n", "\r\n")
    pathlib.Path(sys.argv[2]).write_bytes(s.encode("utf-8"))
