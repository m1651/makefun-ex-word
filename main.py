"""One Word From Your Ex.

Writes exactly one word -- the word my ex would use to describe me --
to /output/entry.txt. The gate allows 1 to 24 characters; the entry is a
single word with no trailing newline.
"""

import os

# The word: "Forgettable". First draft was "Exhausting", but "Forgettable"
# is the sharper self-own: the surprise is erasure rather than a flaw, it
# stings because it is painfully true and plainly owned, it lands instantly
# with no explanation, and it names a fear almost everyone has lived
# through. No near-synonym ("unmemorable", "boring") keeps its edge.
WORD = "Forgettable"


def main() -> None:
    text = WORD.strip()
    assert 1 <= len(text) <= 24, f"word is {len(text)} chars, must be 1-24"
    assert " " not in text and "\n" not in text, "entry must be one word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
