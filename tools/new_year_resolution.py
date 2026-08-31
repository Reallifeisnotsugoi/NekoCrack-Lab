"""Calculate the unlock code for New Year Resolution Vault 2026."""

from __future__ import annotations

import argparse

MASK64 = 0xFFFFFFFFFFFFFFFF


def rotate_left_64(value: int, shift: int) -> int:
    """Rotate a 64-bit integer left by ``shift`` bits."""
    shift %= 64
    value &= MASK64
    return ((value << shift) & MASK64) | (value >> (64 - shift))


def calculate_unlock_code(resolution: str) -> int:
    """Reproduce the crackme's checksum for an ASCII resolution."""
    resolution_bytes = resolution.encode("ascii")
    checksum = 2025

    for index, character in enumerate(resolution_bytes, start=1):
        checksum = rotate_left_64(checksum + index * character, 3)
        checksum = (checksum ^ 0x20262026) & MASK64

    return checksum


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("resolution", help="ASCII resolution entered in the crackme")
    args = parser.parse_args()
    print(calculate_unlock_code(args.resolution))


if __name__ == "__main__":
    main()
