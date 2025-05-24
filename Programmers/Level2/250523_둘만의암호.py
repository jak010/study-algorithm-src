# https://school.programmers.co.kr/learn/courses/30/lessons/155652?language=python3

import string

alphabet = string.ascii_letters[0:26]


def solution(s, skip, index):
    cleand = ""
    for alpah in alphabet:
        if alpah in skip:
            continue
        cleand += alpah

    answer = ""
    for ch in s:
        idx = cleand.index(ch)
        idx = (idx + index) % len(cleand)
        answer += cleand[idx]

    return answer


if __name__ == '__main__':
    s = "aukks"
    skip = "wbqd"
    index = 5

    r = solution(s, skip, index)
    print(r)
