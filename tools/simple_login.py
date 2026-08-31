"""Generate passwords for Kryptos's Simple login crackme."""

from __future__ import annotations

import argparse

MASK32 = 0xFFFFFFFF
SIGN_BIT_32 = 0x80000000


def to_signed_32(value: int) -> int:
    """Apply C-style signed 32-bit integer wrapping."""
    value &= MASK32
    return value - (1 << 32) if value & SIGN_BIT_32 else value


def generate_password(username: str) -> int:
    """Return the signed decimal password for an ASCII username."""
    username_bytes = username.encode("ascii")
    value = 0

    for index, character in enumerate(username_bytes, start=1):
        intermediate = to_signed_32(value + character * index)
        value = to_signed_32(intermediate ^ (intermediate * 8))

    return to_signed_32((value * 0x539) ^ 0x5A5A)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("username", help="ASCII username accepted by the crackme")
    args = parser.parse_args()
    print(generate_password(args.username))


if __name__ == "__main__":
    main()
