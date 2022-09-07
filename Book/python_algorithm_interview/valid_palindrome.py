""" Flow
1. strings를 순회하면서 각 문자를 소문자로 변환된 문자를 새 리스트에 저장한다.
2. 문자열의 길이가 0이 될 때 까지 리스트의 첫 번째 와 마지막 인덱스에서 원소를 꺼내 비교한다.
"""


def is_palindrome(strings: str):
    strs = []
    for char in strings:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


def is_palindrome_with_deque(strings: str):
    from collections import deque

    strs = deque()
    for char in strings:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


if __name__ == '__main__':
    strings = "A man a plan, a canal: Panama"
    print(is_palindrome(strings=strings))
    print(is_palindrome_with_deque(strings=strings))
