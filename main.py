#!/usr/bin/env python3
"""THE DAY IN PRINT - entry program for news-image-20261123 (akun1, @sanzex).

Concept: a one-page front page for Monday 23 November 2026 - ivory paper,
navy ink, red accent. Lead story: COP31 ends without a deal in Antalya,
after the final Turkish draft dropped any mention of fossil fuels.
12 numbered main cards, 28 also-on briefs, a day-in-numbers strip, a
dotted world map with numbered pins and a red date-check box naming
seven stories that were checked and left out as not from this day.

This program is deliberately boring: standard library only, copy only.
It reads the entry.png sitting next to it, verifies the PNG signature,
the 1 MiB competition ceiling and the exact expected size and digest,
then writes the identical bytes to the output directory. Two runs
produce byte-identical output.
"""

import hashlib
import os
import sys

EXPECTED_BYTES = 282013
EXPECTED_SHA256 = "1272c45c494ca2f15e4f2b1139544218ba1db939d2703daed4a28aff0069b1dc"

PNG_HEADER = b"\x89PNG\r\n\x1a\n"
CEILING = 1048576  # 1 MiB hard gate of the competition


def load_entry():
    folder = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(folder, "entry.png")
    with open(path, "rb") as handle:
        return handle.read()


def check_payload(blob):
    if not blob:
        sys.exit("entry.png is empty")
    if blob[:8] != PNG_HEADER:
        sys.exit("entry.png does not start with the PNG signature")
    if len(blob) > CEILING:
        sys.exit("entry.png exceeds the 1 MiB ceiling: %d bytes" % len(blob))
    if len(blob) != EXPECTED_BYTES:
        sys.exit(
            "entry.png size drifted: got %d, expected %d"
            % (len(blob), EXPECTED_BYTES)
        )
    digest = hashlib.sha256(blob).hexdigest()
    if digest != EXPECTED_SHA256:
        sys.exit("entry.png sha256 drifted: %s" % digest)
    return digest


def main():
    blob = load_entry()
    digest = check_payload(blob)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    with open(target, "wb") as handle:
        handle.write(blob)
    sys.stderr.write("entry.png: %d bytes sha256=%s\n" % (len(blob), digest))


if __name__ == "__main__":
    main()
