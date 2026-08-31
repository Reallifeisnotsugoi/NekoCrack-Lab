"""Generate an ELF ID for DonCris's S.N.A.P. crackme."""

from __future__ import annotations

import argparse

MASK32 = 0xFFFFFFFF


def rotate_right_32(value: int, shift: int) -> int:
    """Rotate a 32-bit integer right by ``shift`` bits."""
    shift %= 32
    value &= MASK32
    return ((value >> shift) | (value << (32 - shift))) & MASK32


def generate_elf_id(username: str) -> int:
    """Return the numeric ELF ID for an ASCII username."""
    username_bytes = username.encode("ascii")
    value = 0xCAFEBABE

    for character in username_bytes:
        value = rotate_right_32(value ^ character, (character % 7) + 1)
        value = (value + 0x5AA55AA5) & MASK32
        value ^= (value << 4) & MASK32
        value &= MASK32

    return value ^ 0xDEADBEEF


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("username", help="ASCII username accepted by the crackme")
    args = parser.parse_args()
    print(generate_elf_id(args.username))


if __name__ == "__main__":
    main()
