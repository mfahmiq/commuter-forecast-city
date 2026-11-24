#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (<=140 chars) for the invented city
Umbrella Falls to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt),
then self-verifies it: UTF-8, 1-140 characters, single line, not
whitespace-only. Exits non-zero on any failure. Python stdlib only.
"""

import os
import sys

ENTRY = (
    "In Umbrella Falls, rain falls upward today \u2014 leave the umbrella "
    "at home, arrive dry, and catch the 8:15 smiling for once."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")

    text = ENTRY
    if not text or not text.strip():
        print("FAIL: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("FAIL: entry is not a single line", file=sys.stderr)
        return 1
    if len(text) > 140:
        print(f"FAIL: entry is {len(text)} chars, over 140", file=sys.stderr)
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"FAIL: entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)

    # Verify what was actually written, byte for byte.
    with open(out_path, "rb") as fh:
        raw = fh.read()
    written = raw.decode("utf-8")
    if written != text:
        print("FAIL: written file does not match the entry", file=sys.stderr)
        return 1
    if len(written) > 140 or not written.strip() or "\n" in written:
        print("FAIL: written file fails the gate checks", file=sys.stderr)
        return 1

    print(f"OK: wrote {out_path} ({len(text)} chars)")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
