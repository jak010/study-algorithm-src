"""
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
"""


def solution(s):
    answer = ""
    # pythonic 스타일
    for idx in s.split(" "):
        for index, value in enumerate(idx):
            if index % 2 == 0:
                answer += value.upper()
            else:
                answer += value.lower()
        answer += " "
    return answer[:-1]

    # pythonic 스타일2
    # for idx in s.split(" "):
    #     for index, value in enumerate(idx):
    #         if index % 2 == 0:
    #             answer.extend(value.upper())
    #         else:
    #             answer.extend(value.lower())
    #     answer.extend(" ")
    # return "".join(answer).rstrip()

    # Coding Test
    # answer = str()
    # for string in s.split(" "):
    #     for i in range(len(string)):
    #         if (i % 2) == 0:
    #             answer += string[i].upper()
    #         else:
    #             answer += string[i].lower()
    #     answer += " "
    #
    # return answer.rstrip()

    # answer = str()
    # for string in s.split(" "):
    #     for i in range(len(string)):
    #         answer += string[i].upper() if (i % 2) == 0 else string[i].lower()
    #     answer += " "
    #
    # return answer.rstrip()


if __name__ == '__main__':
    s = "try hello world"
    s.strip()
    result = solution(s)
    print(result)

