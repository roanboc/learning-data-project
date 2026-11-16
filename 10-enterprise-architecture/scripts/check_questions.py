#!/usr/bin/env python3
"""Each driver's question is a copy of Analytics' question of the same number.

A question starts in Analytics' records (../00-initiatives/analytics-questions.md, AQ1, AQ2, ...), and the
architecture records it as a driver of the same number (architecture/1_strategy/1_motivation.md, DRV1, DRV2,
...). This fails if a question has no driver, or if the words in bold differ. A driver with no question of
its number, such as data governance's own, is allowed.

Run from 10-enterprise-architecture/. Exits 0 when everything passes, 1 otherwise. Needs nothing but Python.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
QUESTIONS = HERE.parent / "00-initiatives" / "analytics-questions.md"
DRIVERS = HERE / "architecture" / "1_strategy" / "1_motivation.md"
ROW = re.compile(r"^\|\s*`(AQ|DRV)(\d+)`\s*\|\s*\*\*(.+?)\*\*")


def rows(path, kind):
    """{number: the question in bold} for every table row of that kind."""
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if m and m.group(1) == kind:
            out[int(m.group(2))] = m.group(3).strip()
    return out


def main():
    if not QUESTIONS.is_file():
        print(f"FAIL: no Analytics' records at {QUESTIONS}")
        return 1
    asked, drivers, fails = rows(QUESTIONS, "AQ"), rows(DRIVERS, "DRV"), []
    for n, q in sorted(asked.items()):
        if n not in drivers:
            fails.append(f"AQ{n} has no driver DRV{n} in {DRIVERS.relative_to(HERE)}")
        elif drivers[n] != q:
            fails.append(f"DRV{n} says {drivers[n]!r}; AQ{n} says {q!r}")
    for line in fails:
        print("FAIL:", line)
    if not fails:
        print(f"OK: {len(asked)} questions, each with its driver; {len(drivers) - len(asked)} driver(s) of the architecture's own")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
