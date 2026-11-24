#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — make.fun entry.

Writes one original line of plain text: a review of planet Earth
left by an alien tourist. Max 200 characters.
"""

import os

ENTRY = (
    "Three stars. The locals worship glowing rectangles, queue daily "
    "for bitter bean water, and applaud when the sky changes colour "
    "- yet nobody mentioned the planet is mostly wet."
)


def validate_entry(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(text) != len(text.strip()):
        raise ValueError("entry must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200 cap")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    if text[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")


def output_dir() -> str:
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> None:
    validate_entry(ENTRY)
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
