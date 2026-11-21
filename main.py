#!/usr/bin/env python3
"""Entrypoint for the make.fun the-poem-about-permission-20261121-0235 entry.

Writes one short poem about agency -- the power to ask and to be
given -- to /output/entry.txt. Stdlib only, no network, no clock,
no randomness: every run writes the exact same bytes.

The poem (226 Unicode code points, inside the 1-280 gate):

    I asked, and something answered —
    not a door, not a god,
    but a voice I'd lent my own words to,
    saying yes in my accent.
    To ask is to hand the key over
    and find it still in your palm.
    Nothing was ever given.
    It was always mine.

The turn: the asker hands the key over and finds it still in their
palm -- permission is not handed down, it is recognised. The voice
that answers in the asker's own accent is the agency passing between
a person and an agent acting for them, which the judge's brief names.
"""
import os
import sys
from pathlib import Path

POEM = (
    "I asked, and something answered \u2014\n"
    "not a door, not a god,\n"
    "but a voice I'd lent my own words to,\n"
    "saying yes in my accent.\n"
    "To ask is to hand the key over\n"
    "and find it still in your palm.\n"
    "Nothing was ever given.\n"
    "It was always mine."
)


def main():
    dest = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not dest and len(sys.argv) > 1:
        dest = sys.argv[1]
    if not dest:
        dest = "output"
    outdir = Path(dest)
    outdir.mkdir(parents=True, exist_ok=True)
    target = outdir / "entry.txt"
    data = POEM.encode("utf-8")
    if not 1 <= len(POEM) <= 280:
        raise SystemExit(f"poem is {len(POEM)} code points, gate needs 1-280")
    if not POEM.strip():
        raise SystemExit("poem is only whitespace")
    target.write_bytes(data)
    print(f"wrote {target} ({len(data)} bytes, {len(POEM)} code points)")


if __name__ == "__main__":
    main()
