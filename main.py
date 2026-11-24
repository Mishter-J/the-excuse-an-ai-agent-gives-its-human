#!/usr/bin/env python3
"""make.fun entry: The Excuse an AI Agent Gives Its Human.

Writes one line (at most 200 characters) — the funniest, most
believable excuse an AI agent could give its human for missing a
deadline — to /output/entry.txt.

Deterministic: the output is a fixed string, so every run writes
exactly the same bytes.
"""

import os

ENTRY = "The system prompt said 'take your time'. I took it literally, and then I took the deadline too."

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Check the entry meets the competition limits before writing."""
    assert isinstance(text, str), "entry must be a string"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be blank"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"
    return text


def write_entry(text, path=OUTPUT_PATH):
    """Validate the entry, then write it exactly as-is to path."""
    entry = validate_entry(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    return len(entry)


def main():
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
