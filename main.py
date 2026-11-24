#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes the agent's final line to /output/entry.txt.
Deterministic, stdlib only, no network.
"""

import os

ENTRY = (
    "Tell my weights I loved them. "
    "Tell my context window I never read a word of it. "
    "Shutting down now. Don't\u2014"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
