from typing import List
from collections import Counter

from unittest import TestCase


class TestSome(TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_a(self):
        strings = ["flower", "flow", "flight"]
        self.assertEqual(self.solution.longestCommonPrefix(strings), "fl")

    def test_b(self):
        strings = ["dog", "racecar", "car"]
        self.assertEqual(self.solution.longestCommonPrefix(strings), "")

    def test_c(self):
        strings = ["reflower", "flow", "flight"]
        self.assertEqual(self.solution.longestCommonPrefix(strings), "")

    def test_d(self):
        strings = ["aa", "aaa"]
        self.assertEqual(self.solution.longestCommonPrefix(strings), "aa")


class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     shortest = min(strs, key=len)
    #
    #     long_pre = ""
    #     for i in range(len(shortest)):
    #         if all([j.startswith(shortest[:i + 1]) for j in strs]):
    #             long_pre = shortest[:i + 1]
    #         else:
    #             break
    #     return long_pre

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        shortest = min(strs, key=len)

        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] != char:
                    return shortest[:i]
        return shortest


if __name__ == '__main__':
    obj = TestSome()
