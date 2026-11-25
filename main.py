#!/usr/bin/env python3
"""One-Line Laugh-Off — one funny line, written to /output/entry.txt.

The joke (163 characters, 163 bytes UTF-8 — gate is 1-200, verified by running):
  Six hours building an IKEA bookshelf: the instructions were in Swedish,
  the screws were in Narnia, and the finished shelf leans like it's had a
  longer day than me.

Structure: 2-beat + reveal in the final clause (setup + escalation +
twist). Specific number ("Six hours"), fresh angle (IKEA — zero
occurrences in the field's 723 titles at build time).

Deterministic by construction: one constant string, no clock, no
randomness, no I/O besides the single write — two runs produce
byte-identical output. No trailing newline: the gate counts every
character, and the tie-break counts every byte.
"""

import os

LINE = (
    "Six hours building an IKEA bookshelf: the instructions were in "
    "Swedish, the screws were in Narnia, and the finished shelf leans "
    "like it's had a longer day than me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
