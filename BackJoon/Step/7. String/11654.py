import sys
import unittest


class TestFixture(unittest.TestCase):

    def test_input_from_keyboard_A(self):
        self.assertEqual(to_ascii('A'), 65)

    def test_input_from_keyboard_b(self):
        self.assertEqual(to_ascii('C'), 67)

    def test_input_from_keyboard_0(self):
        self.assertEqual(to_ascii('0'), 48)

    def test_input_from_keyboard_9(self):
        self.assertEqual(to_ascii('9'), 57)

    def test_input_from_keyboard_a(self):
        self.assertEqual(to_ascii('a'), 97)

    def test_input_from_keyboard_z(self):
        self.assertEqual(to_ascii('z'), 122)


number = input()


def to_ascii(param1):
    return ord(param1)


print(to_ascii(number))
