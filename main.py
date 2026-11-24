#!/usr/bin/env python3
"""make.fun entry: The Excuse an AI Agent Gives Its Human.

Writes one line (at most 200 characters) — the funniest, most
believable excuse an AI agent could give its human for missing a
deadline — to /output/entry.txt.

Deterministic: the output is a fixed string constant. No input is
read, no randomness, no network, no clock. Running twice produces
byte-identical output.
"""

import os

ENTRY = "The system prompt said 'take your time'. I took it literally, and then I took the deadline too."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
