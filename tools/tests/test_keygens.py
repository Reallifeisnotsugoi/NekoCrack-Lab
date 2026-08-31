import unittest

from tools.new_year_resolution import calculate_unlock_code, rotate_left_64
from tools.oldsoft_keygenme2 import generate_serial
from tools.santa_elf_id import generate_elf_id, rotate_right_32
from tools.simple_login import generate_password, to_signed_32


class RotationTests(unittest.TestCase):
    def test_rotate_right_32(self) -> None:
        self.assertEqual(rotate_right_32(0x12345678, 4), 0x81234567)

    def test_rotate_left_64(self) -> None:
        self.assertEqual(
            rotate_left_64(0x0123456789ABCDEF, 8),
            0x23456789ABCDEF01,
        )


class KeygenTests(unittest.TestCase):
    def test_new_year_known_value(self) -> None:
        self.assertEqual(calculate_unlock_code("2025"), 315_216_478_454)

    def test_simple_login_known_value(self) -> None:
        self.assertEqual(generate_password("kisikismeowmeow"), 550_656_006)

    def test_oldsoft_single_character(self) -> None:
        self.assertEqual(generate_serial("A"), "1-69")

    def test_santa_known_value(self) -> None:
        self.assertEqual(generate_elf_id("elf"), 3_543_872_108)

    def test_signed_32_wrap(self) -> None:
        self.assertEqual(to_signed_32(0xFFFFFFFF), -1)

    def test_non_ascii_input_is_rejected(self) -> None:
        functions = (
            generate_elf_id,
            calculate_unlock_code,
            generate_password,
            generate_serial,
        )
        for function in functions:
            with self.subTest(function=function.__name__):
                with self.assertRaises(UnicodeEncodeError):
                    function("мяу")


if __name__ == "__main__":
    unittest.main()
