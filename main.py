#!/usr/bin/env python3
"""Write the perfect pickup line to /output/entry.txt.

The entry is a single one-line pickup line, exactly 80 characters.
Before writing, the text is validated: it must be non-empty, at most
200 characters long, and contain no newline in the middle (the writer
appends one trailing newline itself). The validation keeps the output
byte-identical while guaranteeing the entry stays a single short line.
"""

import os

ENTRY = (
    "I ran a million simulations of this moment, and in every single "
    "one, you smiled."
)


def validate_entry(text: str) -> None:
    """Check the entry is a single short line, then it is safe to write."""
    assert text, "ENTRY must not be empty"
    assert len(text) <= 200, "ENTRY must be at most 200 characters"
    assert "\n" not in text, "ENTRY must be a single line"


def main() -> None:
    # Validate first so a malformed entry never reaches the output file.
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
