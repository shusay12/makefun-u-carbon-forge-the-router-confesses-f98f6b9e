#!/usr/bin/env python3
"""The Router Confesses — make.fun entry program.

Writes the one-line excuse a home Wi-Fi router gives for dropping the
connection at the climax of a movie (200 characters or fewer) to
/output/entry.txt.

Python 3.13, standard library only, no network, deterministic output.
"""

import hashlib
import os

MAX_CHARS = 200

# Final line: the router confesses it secretly watched ahead and is
# withholding the reveal out of petty jealousy — first-person, petty,
# twist lands in the second clause ("some of us watch too, you know").
# Fresh angle: no buffering, bandwidth or firmware-update joke.
# Drafted 5 candidates and scored them against the judge brief
# (router voice, twist, one-breath tightness, freshness); this one won:
# the strongest turn (router as secret fellow-viewer) with the clearest
# petty voice. Sibling angles avoided: the vacuum's "lava" rug, the
# fridge's emancipation, the sick-day pre-workout.
ENTRY = (
    "I saw who did it ten minutes ago and I'm not letting you find out "
    "first \u2014 some of us watch too, you know."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    )
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    # The gate rejects control characters; the em dash (U+2014) is the
    # only non-ASCII character and is valid UTF-8.
    assert all(ord(c) >= 32 or c in "\t" for c in text), (
        "entry must not contain control characters"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Verify what landed on disk matches the intended text byte for byte
    # (other builders share /output, so re-read immediately).
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == text.encode("utf-8"), "entry.txt on disk differs!"
    digest = hashlib.sha256(written).hexdigest()
    print(f"wrote /output/entry.txt ({len(text)} chars) sha256={digest}")


if __name__ == "__main__":
    main()
