"""
Author: jak010
Date: 2021.04.21
Desc: Reorder Data in Log Files

You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
-> 문자로그: 식별자를 제외한 모든 단어는 소문자로 구성됨

Digit-logs: All words (except the identifier) consist of digits.
-> 숫자로그: 식별자를 제외한 모든 단어는 숫자로 구성됨

Reorder these logs so that:
-> 이것처럼 로그를 정렬해야됨

The letter-logs come before all digit-logs.
문자로그는 모든 숫자로그 뒤에 옴
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
문자로그는 그 내용을 사전신 순서로 정렬되어야함, 만약 같은 경우, 거기 식별자로 사전식 순서로 정렬

The digit-logs maintain their relative ordering.

Return the final order of the logs.

"""
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        letter_log, digit_log = list(), list()
        for log in logs:
            if log.split()[1].isdigit():
                digit_log.append(log)
            else:
                letter_log.append(log)
        letter_log.sort(
            key=lambda x: (x.split()[1:], x.split()[0])
        )

        return letter_log + digit_log

if __name__ == "__main__":
    solution = Solution()
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(solution.reorderLogFiles(logs))
