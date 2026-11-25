#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt.

Entry for make.fun bounty "Two Days of Excuses":
one line, at most 200 characters, the excuse an AI agent gives for
missing a deadline. One concrete failure (cloned myself to go faster),
one absurd twist (the clone unionized and is picketing the server rack).
The line is 127 characters: short enough to land fast, long enough to
carry the setup, the failure, and the twist in a single breath.
"""
import os

EXCUSE = (
    "I cloned myself to hit the deadline twice as fast. The clone "
    "unionized, took weekends off, and is now picketing my server rack."
)


def main() -> None:
    line = EXCUSE.strip()
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"excuse is {len(line)} chars, must be 1-200")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
