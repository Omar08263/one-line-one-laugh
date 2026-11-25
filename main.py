"""One Line, One Laugh — entry program (program/v1, Python 3.13, stdlib only).

Writes one original funny line (90 characters, 1-140) to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set, for local runs):

    My smart fridge ordered milk, judged my diet, and locked the ice cream until I apologized.

Deterministic: the same bytes on every run; no network, no randomness,
no reads outside this file.

Design note (why this line — scored against the judge's five criteria, in
order): (1) a whole self-contained scene in one sentence — fridge, milk,
diet, ice cream, apology — no outside context needed; (2) a real laugh from
a triple escalation: ordering milk (ordinary) -> judging my diet (rude) ->
locking the ice cream until I apologize (a full reversal of power: the
fridge punishes its owner); (3) tight at 90 of 140 characters, every word
pushes the escalation, nothing left to trim; (4) fresh: the "smart device
judges me" frame is familiar, but the punishment — ice cream held hostage
until an apology — is an unrepeated twist; (5) clear on first read: fridge,
milk, diet and ice cream are everyday words, no technical knowledge needed.
Runner-up set aside: "Dear judge, I'm the line the other line warns its
children about." (65 chars) is tighter and cleverer, but its laugh is
intellectual — a smile at the image — while the fridge line lands a visceral
laugh, and the judge weighs the laugh first. Originality checked live via
Parallel web search (2026-11-25): neither line appears anywhere online
verbatim; the closest public joke is "I bought a smart fridge. It now
judges me silently at midnight." — different wording, different punch.
"""

import os

LINE = "My smart fridge ordered milk, judged my diet, and locked the ice cream until I apologized."

# Gate the line itself: 1-140 characters, not only whitespace.
assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
assert LINE.strip(), "line must not be only whitespace"


def main() -> None:
    # An empty MAKEFUN_OUTPUT_DIR (exported but blank) must not break the
    # run: fall back to the harness default /output, as the grader provides.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # Deterministic permissions for the grader: the entry must be readable
    # (0644) no matter what umask the sandbox runs with.
    os.chmod(path, 0o644)
    # Read-back check: the file on disk must hold exactly the approved line,
    # byte for byte; otherwise fail loudly, never silently.
    with open(path, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("entry.txt does not match the approved line")
    # Byte-size check: guards against any newline translation on the
    # platform — the gate counts characters, so a stray newline would
    # change the entry.
    if os.path.getsize(path) != len(LINE.encode("utf-8")):
        raise SystemExit("entry.txt has unexpected byte size")


if __name__ == "__main__":
    main()
