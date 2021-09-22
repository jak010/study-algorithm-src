"""
Given a string paragraph and a string array of the banned words banned,
return the most frequent word that is not banned.

It is guaranteed there is at least one word that is not banned,

and that the answer is unique.The words in paragraph are case-insensitive
and the answer should be returned in lowercase.
"""
from typing import List
import re
from collections import Counter


# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         new_strings = re.sub(r"[^a-zA-Z0-9]", " ", paragraph).lower().split()
#         counter = Counter(new_strings)
#         for key in banned:
#             if key in counter:
#                 counter.pop(key)
#
#         return counter.most_common()[0][0]

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub(r'[^\w]', ' ', paragraph).lower().split()

        # words에 있는 것중에 banned을 뺴기
        words_sub_banned = [x for x in words if x not in banned]

        container = Counter(words_sub_banned)
        return container.most_common()[0][0]


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    a = Solution()
    ret = a.mostCommonWord(paragraph=paragraph, banned=banned)
    print(ret)
