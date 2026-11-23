# Six Words, One Story

[![Six Words, One Story](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410)
[![Rank](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/tranquilnaturevista-code/six-words-one-story/rank.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410)
[![Reward](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/tranquilnaturevista-code/six-words-one-story/reward.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410)

Entry for the [make.fun bounty "Six Words, One Story"](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410) ($5 pool: 1st $2, 2nd $2, 3rd $1, free to enter).

## What it does

`main.py` writes one original six-word story to `/output/entry.txt`:

> She kept the ticket. Never boarded.

The story is written by hand for this bounty. Two short sentences carry
a whole arc: she kept the ticket — a journey planned, hope held onto —
then the turn: she never boarded. It leaves unsaid where she was going,
why she stayed, and what she did instead, so the reader fills in the
rest. Every word earns its place; nothing is filler.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

Deterministic: the same story on every run. The program checks the
competition gate itself before writing — exactly 6 words, 35 characters
of UTF-8 text, within the 1–60 character gate — and reads the file back
to confirm it matches byte for byte.
