#!/usr/bin/env python3
"""Two Lines to Your Past Self — entry program.

Writes exactly two lines (274 characters) to /output/entry.txt: a
warning to my past self about one specific moment, and one sentence
on why that moment mattered.

The moment: the Tuesday after graduation, selling my guitar for
eighty dollars at the pawn shop on 5th Street. The money was gone
by Friday; the guitar was the one thing that got me through the
winter I lost my job. Ten years later I am still trying to buy
back a sound that was never for sale.
"""

import os

LINE1 = "Don't sell the guitar for eighty dollars at the pawn shop on 5th Street the Tuesday after graduation."
LINE2 = "The eighty dollars was gone by Friday, but the guitar was the one thing that got you through the winter you lost your job, and you've spent ten years trying to buy it back."

ENTRY = LINE1 + "\n" + LINE2

# Gate: /output/entry.txt must be UTF-8, 1-280 characters, exactly
# two lines. ENTRY is 274 characters; the trailing newline the file
# gets makes 275 bytes on disk, still inside the gate.


def main():
    if ENTRY.count("\n") != 1:
        raise ValueError("entry must be exactly two lines")
    if not 1 <= len(ENTRY) <= 280:
        raise ValueError("entry must be 1-280 characters")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
