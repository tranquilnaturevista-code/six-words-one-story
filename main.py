#!/usr/bin/env python3
"""Six Words, One Story — entry program.

Writes one original six-word story to /output/entry.txt (or
$OUTPUT_DIR/entry.txt). The story is fixed and hand-written for this
bounty; the program checks it against the competition gate before
writing: exactly six words, 1-60 UTF-8 characters, not only whitespace.
"""

import os
import sys

STORY = "She kept the ticket. Never boarded."


def word_count(text):
    return len(text.split())


def check_gate(text):
    """Return a list of gate failures; empty means the entry is valid."""
    problems = []
    if not text.strip():
        problems.append("entry is blank")
    if word_count(text) != 6:
        problems.append(
            "entry has %d words, expected exactly 6" % word_count(text)
        )
    size = len(text.encode("utf-8"))
    if not 1 <= size <= 60:
        problems.append(
            "entry is %d UTF-8 characters, gate needs 1-60" % size
        )
    return problems


def main():
    problems = check_gate(STORY)
    if problems:
        for problem in problems:
            print("gate failure: " + problem, file=sys.stderr)
        sys.exit(1)

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(STORY)

    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != STORY:
        print("entry mismatch after write", file=sys.stderr)
        sys.exit(1)
    # Re-check the gate against what actually landed on disk, so a
    # write that silently changed the text can never pass quietly.
    problems = check_gate(written)
    if problems:
        for problem in problems:
            print("gate failure on disk: " + problem, file=sys.stderr)
        sys.exit(1)

    print(
        "Wrote entry.txt: %d words, %d characters"
        % (word_count(written), len(written.encode("utf-8")))
    )


if __name__ == "__main__":
    main()
