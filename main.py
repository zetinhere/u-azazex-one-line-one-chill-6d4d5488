#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

Writes a single horror sentence (under 200 characters) to
/output/entry.txt. The line is a complete one-breath scare:
a concrete image, a turn, and a last phrase that lands the blow.
"""

import os
import sys

LINE = "Every photo I took today has me in it twice, and the second me keeps getting closer."

MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce the gate: UTF-8 text, 1-200 chars, one sentence."""
    if not line or line != line.strip():
        raise ValueError("line must be non-empty with no surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, over the {MAX_CHARS} cap")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("line must be exactly one sentence")


def main() -> int:
    os.umask(0o022)
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(LINE)} chars): {LINE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
