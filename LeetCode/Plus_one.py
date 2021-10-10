from typing import List
import unittest


class TestGroup(unittest.TestCase):

    def test_a(self):
        digits = [1, 2, 3]
        self.assertEqual(Solution().plusOne(digits), [1, 2, 4])

    def test_b(self):
        digits = [4, 3, 2, 1]
        self.assertEqual(Solution().plusOne(digits), [4, 3, 2, 2])

    def test_c(self):
        digits = [0]
        self.assertEqual(Solution().plusOne(digits), [1])

    def test_d(self):
        digits = [9]
        self.assertEqual(Solution().plusOne(digits), [1, 0])


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''.join([str(v) for v in digits])

        return [int(v) for v in str(int(number) + 1)]


if __name__ == '__main__':
    unittest.main()
