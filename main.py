#!/usr/bin/env python3
"""One Line, Big Laugh — entrypoint.

Writes the keeper line verbatim to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Pure stdlib only. Deterministic: same bytes on every run.
"""
import os

KEEPER = "My teacher called me by my brother's name for six years. I graduated as him."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    text = KEEPER
    assert 1 <= len(text) <= 200, "keeper must be 1-200 chars"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Write-back self-check: the file must hold exactly the keeper, no more.
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == text, "entry.txt does not match keeper"
    print(f"wrote {len(text.encode('utf-8'))} bytes to {path}")


if __name__ == "__main__":
    main()
