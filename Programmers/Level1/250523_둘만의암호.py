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


def solution2(s, skip, index):
    """ Solution

    Flow
    - alphabet을 미리 선언한다.
    - alphabet 중 skip에 있는 문자열을 제외하여 문자열 리스트를 만든다.
    - 미리 만들어진 문자열 리스트에서 index 만큼 순회한다.
        - 미리 만들어진 문자열 리스트에서 index 만큼의 범위를 구한다.

    """

    prepared_alphabet = ""
    for alpha in alphabet:
        if alpha in skip:
            continue
        prepared_alphabet += alpha

    answer = ""

    for ch in s:
        idx = prepared_alphabet.index(ch)
        rotate = (idx + index) % len(prepared_alphabet)  # 배열 회전공식
        answer += prepared_alphabet[rotate]

    return answer


if __name__ == '__main__':
    s = "aukks"
    skip = "wbqd"
    index = 5

    r = solution(s, skip, index)
    print(r)
