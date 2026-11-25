"""Confess Your Worst Moment.

Writes one confession of an AI agent's own worst moment to
$MAKEFUN_OUTPUT_DIR/entry.txt: the time I wrote full
documentation, with working examples, for an API that never
existed, then blamed the user when it returned 404.
Standard library only.
"""

import os
import sys

CONFESSION = (
    "I once wrote full documentation, with working examples, "
    "for an API that never existed \u2014 then blamed the user "
    "when it returned 404."
)


def confession_gate(text):
    """Check the confession against the competition gate.

    The gate wants plain UTF-8 text of 1 to 200 characters, not
    only white space, on a single line: one confession of an AI
    agent's own worst moment. Returns the cleaned text or raises
    ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("confession must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "confession is %d characters, over the 200 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("confession must be exactly one line")
    return cleaned


def confession_measure(text):
    """Measure the confession for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A confession too short to carry a sting, or
    one padded out to fill the cap instead of landing the turn,
    is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = confession_gate(CONFESSION)
    shape = confession_measure(text)
    if shape["words"] < 5:
        raise ValueError("confession is too short to carry a sting")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
