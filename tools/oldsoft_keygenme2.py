"""Generate serials for wolverine2k's OldSoft KeyGenMe #2."""

from __future__ import annotations

import argparse


def generate_serial(username: str) -> str:
    """Return a serial in the format used by the crackme."""
    username_bytes = username.encode("ascii")
    checksum = 0

    for index, character in enumerate(username_bytes, start=1):
        checksum += character + index + 3

    length_part = 3 * (len(username_bytes) >> 1) + len(username_bytes)
    return f"{length_part}-{checksum}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("username", help="ASCII username accepted by the crackme")
    args = parser.parse_args()
    print(generate_serial(args.username))


if __name__ == "__main__":
    main()
