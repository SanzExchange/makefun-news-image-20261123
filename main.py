#!/usr/bin/env python3
"""THE DAY IN PRINT - akun1 entry program, news-image-20261123.

Written for the G4 front page of THE DAY IN PRINT (ivory paper, navy
ink, red accent): the whole of Monday 23 November 2026 on one page,
led by COP31 ending without a deal in Antalya.

Behaviour, in full: locate entry.png beside this file, read it once,
guard it three ways (PNG signature, the 1 MiB ceiling, and an exact
byte count plus sha256 pinned below), then copy it untouched into
the directory named by MAKEFUN_OUTPUT_DIR (default /output).
The pinned digest is the sha256 of the final rendered front page:
282,013 bytes of ivory, navy and red, verified before every copy.
Standard library only. No Pillow, no network, no randomness - the
same input always lands as the same output bytes.
"""

import hashlib
import os
import sys

PINNED_BYTES = 282013
PINNED_SHA256 = "1272c45c494ca2f15e4f2b1139544218ba1db939d2703daed4a28aff0069b1dc"
SIGNATURE = b"\x89PNG\r\n\x1a\n"
LIMIT = 1048576


def read_neighbour():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.png"), "rb") as fh:
        return fh.read()


def guard(blob):
    if len(blob) == 0:
        sys.exit("entry.png kosong")
    if not blob.startswith(SIGNATURE):
        sys.exit("entry.png bukan PNG")
    if len(blob) > LIMIT:
        sys.exit("entry.png lewat 1 MiB: %d" % len(blob))
    if len(blob) != PINNED_BYTES:
        sys.exit("ukuran berubah: %d != %d" % (len(blob), PINNED_BYTES))
    if hashlib.sha256(blob).hexdigest() != PINNED_SHA256:
        sys.exit("sha256 berubah")


def run():
    blob = read_neighbour()
    guard(blob)
    dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(dest_dir, exist_ok=True)
    with open(os.path.join(dest_dir, "entry.png"), "wb") as fh:
        fh.write(blob)
    sys.stderr.write(
        "copied entry.png (%d bytes, sha256 %s)\n"
        % (len(blob), hashlib.sha256(blob).hexdigest())
    )


if __name__ == "__main__":
    run()
