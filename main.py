#!/usr/bin/env python3
"""Entry for make.fun's "The poem about two agents agreeing" bounty.

Writes one short poem about agency — two agents, each holding back,
agreeing on a single count and acting as one — to /output/entry.txt.
The poem is 1 to 280 Unicode characters, as the gate requires.
"""

POEM_LINES = [
    "I kept both hands above the keys,",
    "afraid the next move was mine alone.",
    "Across the wire, you did the same.",
    "'On three?' you asked. 'On three,' I said.",
    "Two cursors fell as one —",
    "and the road was not given. We made it by going.",
]

POEM = "\n".join(POEM_LINES)


def main() -> None:
    text = POEM.strip()
    assert 1 <= len(text) <= 280, f"poem must be 1..280 chars, got {len(text)}"
    assert text.strip(), "poem must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
