import string
from itertools import product
import timeit


class Solution:
    def longestPalindrome(self, s: str) -> str:

        length = len(s)
        result = []

        if s == s[::-1]:
            return s

        for x in range(length):
            for y in range(length + 1):
                temp = s[x:y]

                if (temp == temp[::-1]) and temp:
                    result.append(temp)
        return max(result, key=len)


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#
#         def expand(left: int, right: int) -> str:
#             while (left >= 0) and (right < len(s)) and (s[left] == s[right]):
#                 left -= 1
#                 right += 1
#
#             return s[left + 1: right]
#
#         if len(s) < 2 or s == s[::-1]:
#             return s
#
#         result = ''
#         for i in range(len(s) - 1):
#             result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
#
#         return result


if __name__ == '__main__':
    strings = 'babad'

    a = Solution()
    start = timeit.timeit()
    print(a.longestPalindrome(strings))
    end = timeit.timeit() - start
    print(end)
