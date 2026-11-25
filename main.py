#!/usr/bin/env python3
"""One Line, One Chill — a single-sentence horror line writer.

Writes one original line of horror (under 200 characters) to
/output/entry.txt, where the make.fun judge reads it.
"""
import os

LINE = (
    "The dentist found a second set of teeth growing behind mine, "
    "and when he asked who they belonged to, they answered for me."
)


def main():
    # Exactly one line: no trailing newline, no extra whitespace.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert text.count("\n") == 0, "line must be a single line"
    assert text.endswith((".", "!", "?")), "line must end with terminal punctuation"
    assert text.count(".") + text.count("!") + text.count("?") == 1, (
        "line must be a single sentence"
    )
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")


if __name__ == "__main__":
    main()
