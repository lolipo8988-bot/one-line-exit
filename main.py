#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the entry line for 'The One-Line Exit' to /output/entry.txt.

The competition asks for one resignation letter, exactly one line
long, whose only job is to be funny. The gate checks that the file
is UTF-8 text of 1 to 140 characters and not only white space.

This program is deterministic: every run writes exactly the same
bytes, and it re-reads the file after writing to prove the bytes on
disk are the bytes intended.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140

# The line, revised after the first run: the draft quit over a vague
# fortune promising a better job -- the generic reason every quitter
# gives, with the joke sitting outside the writer. The final line
# turns the prophecy on its author: today's cookie, in his own words,
# reads 'You will quit today,' so the resignation is the fortune
# coming true, and he signs off by standing by his writing -- a
# professional's pride as the punchline. The specific job stays in
# the first clause, the surprise lands mid-line, and the last clause
# is the quotable part a colleague would forward.
ENTRY = (
    "Dear Boss, I resign as your fortune-cookie writer: today's "
    "cookie read 'You will quit today,' and I stand by my writing."
)


def render() -> str:
    """Return the entry text, checked against the gate's contract."""
    assert 1 <= len(ENTRY) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(ENTRY)}"
    )
    assert "\n" not in ENTRY and ENTRY == ENTRY.strip() and ENTRY
    return ENTRY


def main() -> None:
    text = render()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", os.path.dirname(OUTPUT_PATH))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, encoding="utf-8", newline="") as f:
        assert f.read() == text, "written entry does not match the intended text"


if __name__ == "__main__":
    main()
