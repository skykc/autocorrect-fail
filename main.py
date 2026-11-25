#!/usr/bin/env python3
"""Funniest Autocorrect Fail — writes one autocorrect-fail line to /output/entry.txt.

The line is a single text to Mom: "casserole" autocorrected to "castration"
for the church potluck, with the kicker that everyone loved it last year.
"""
import os

ENTRY = "Mom, can you bring your famous castration to the church potluck on Sunday? Everyone loved it last year."

# Sealed gate: /output/entry.txt must be UTF-8 text of 1 to 199 characters,
# not only white space, and a single line.
assert 1 <= len(ENTRY) <= 199, "entry must be 1-199 characters"
assert "\n" not in ENTRY, "entry must be one line"
assert ENTRY.strip(), "entry must not be only white space"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
