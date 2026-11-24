#!/usr/bin/env python3
"""One Word for the Boss — make.fun bounty
u-swift-badger-44-one-word-for-the-boss-6b48c735

Writes exactly one word describing the boss to /output/entry.txt.

The word: NECK BREATHER, as one word — the boss who is always standing
right behind your chair, breathing down your neck while you work.
Funny on its own, true of a habit every office worker has met, fresh
next to the first words anyone reaches for ("strict", "bossy",
"micromanager"), and it travels: kitchen, warehouse or office, every
workplace has one.
"""

import os

WORD = "Neckbreather"

OUTPUT_PATH = "/output/entry.txt"


def main():
    word = WORD.strip()
    assert " " not in word, "entry must be a single word"
    assert word.isalpha(), "entry must be letters only"
    assert 1 <= len(word) <= 20, "entry must be 1-20 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the word alone is the whole entry.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(word)
    print(f"Wrote {len(word)}-character entry to {OUTPUT_PATH}: {word}")


if __name__ == "__main__":
    main()
