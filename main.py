#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

A robot vacuum's excuse after eating a sock, written to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = "I scanned it: 98% cotton, 2% dignity. The dustbin has already ruled in my favour."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
MAX_CHARS = 200


def main():
    text = ENTRY.strip()
    if not text or len(text) > MAX_CHARS:
        raise SystemExit("entry must be 1 to 200 characters, got %d" % len(text))
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
