p = r"user/Documents/ega_scan_check_20261101/run_0I/crops_026_030/make_findings.py"
s = open(p, encoding="utf-8").read()
rep = [
    ('add(26, "3.2.1, line 3: ', 'add(26, "page line 3, (3.2.1): '),
    ('add(26, "3.2.1, line 4: ', 'add(26, "page line 4, (3.2.1): '),
    ('add(26, "3.2.1, line 10: ', 'add(26, "page line 10, (3.2.1): '),
    ('k(26, "3.2.1, line 2: ', 'k(26, "page line 2, (3.2.1): '),
    ('k(26, "footnote (1), line 2: ', 'k(26, "footnote (1), its line 2: '),
    ('k(26, "3.2.2, condition (F0): ', 'k(26, "page line 15, (3.2.2), condition (F0): '),
    ('add(27, "3.2.2, line 2: ', 'add(27, "page line 2, (3.2.2): '),
    ('add(27, "3.2.2, last line: ', 'add(27, "page line 6, end of (3.2.2): '),
    ('add(27, "3.2.3, last lines: ', 'add(27, "page line 12, (3.2.3): '),
    ('add(27, "3.2.6, last line: ', 'add(27, "page line 39 (last), (3.2.6): '),
    ('k(27, "3.2.3, line 1: ', 'k(27, "page line 7, (3.2.3): '),
    ('k(27, "3.2.4, line 1: ', 'k(27, "page line 14, (3.2.4): '),
    ('k(27, "3.2.4, line 2: ', 'k(27, "page line 15, (3.2.4): '),
    ('k(27, "3.2.4, line 6: ', 'k(27, "page line 19, (3.2.4): '),
    ('k(27, "3.2.5, line 2: ', 'k(27, "page line 23, (3.2.5): '),
    ('k(27, "3.2.5, second paragraph, line 1: ', 'k(27, "page line 27, (3.2.5): '),
    ('k(27, "3.2.6, line 1: ', 'k(27, "page line 33, (3.2.6): '),
    ('k(27, "3.2.6, line 2: ', 'k(27, "page line 34, (3.2.6): '),
    ('k(27, "3.2.6, line 3: ', 'k(27, "page line 35, (3.2.6): '),
    ('k(27, "3.2.6, line 4: ', 'k(27, "page line 36, (3.2.6): '),
    ('k(27, "3.2.6, last line: ', 'k(27, "page line 39, (3.2.6): '),
    ('add(28, "3.2.6 (cont.), line 1: ', 'add(28, "page line 1, (3.2.6) cont.: '),
    ('add(28, "3.2.6 (cont.), line 2: ', 'add(28, "page line 2, (3.2.6) cont.: '),
    ('add(28, "3.2.6 (cont.), line 3: ', 'add(28, "page line 3, (3.2.6) cont.: '),
    ('k(28, "3.2.6 (cont.), line 2: ', 'k(28, "page line 2, (3.2.6) cont.: '),
    ('add(28, "3.3.1, line 6: ', 'add(28, "(3.3.1), its lines 6-7: '),
    ('add(28, "3.3.1, line 13: ', 'add(28, "(3.3.1), its line 13: '),
    ('k(28, "3.3.1, line 1: ', 'k(28, "(3.3.1), its line 1: '),
    ('k(28, "3.3.1, line 3: ', 'k(28, "(3.3.1), its line 3: '),
    ('k(28, "3.3.1, line 7: ', 'k(28, "(3.3.1), its line 7: '),
    ('k(28, "3.3.1, last paragraph: ', 'k(28, "(3.3.1), last paragraph, its line 1: '),
    ('k(28, "3.3.2, line 2: ', 'k(28, "(3.3.2), its line 2: '),
    ('k(29, "3.4.1, line 2: ', 'k(29, "(3.4.1), its line 2: '),
    ('k(29, "3.4.1, line 5: ', 'k(29, "(3.4.1), its line 5: '),
    ('k(29, "3.4.2, line 1: ', 'k(29, "(3.4.2), its line 1: '),
    ('k(29, "3.4.2, line 5: ', 'k(29, "(3.4.2), its line 6: '),
    ('k(29, "3.4.2, line 7: ', 'k(29, "(3.4.2), its line 8: '),
    ('k(29, "3.4.2, last line: ', 'k(29, "(3.4.2), its line 8 (end): '),
    ('k(29, "3.4.3, line 3: ', 'k(29, "(3.4.3), its line 3: '),
    ('k(29, "3.4.4, line 1: ', 'k(29, "(3.4.4), its line 1: '),
    ('k(29, "3.4.4, line 2: ', 'k(29, "(3.4.4), its line 2: '),
    ('add(30, "heading of 3.4.5"', 'add(30, "heading of (3.4.5), page line 7"'),
    ('add(30, "3.4.6, line 8: ', 'add(30, "(3.4.6), its line 7: '),
    ('add(30, "3.5.1: ', 'add(30, "(3.5.1), its line 5: '),
    ('k(30, "3.4.4 (cont.), line 3: ', 'k(30, "page line 3, (3.4.4) cont.: '),
    ('k(30, "3.4.6, line 1: ', 'k(30, "(3.4.6), its line 1: '),
    ('k(30, "3.4.6, line 2: ', 'k(30, "(3.4.6), its line 2: '),
    ('k(30, "3.5.1, line 2: ', 'k(30, "(3.5.1), its line 2: '),
]
missing = 0
for a, b in rep:
    n = s.count(a)
    if n != 1:
        missing += 1
        print("COUNT", n, a.encode("ascii", "backslashreplace").decode())
    s = s.replace(a, b)
open(p, "w", encoding="utf-8", newline="\n").write(s)
print("done, problems:", missing)
