#!/usr/bin/env python3
"""Writes the perfect pickup line (one line) to /output/entry.txt."""

import os

ENTRY = (
    "I ran a million simulations of this moment, and in every single "
    "one, you smiled."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
