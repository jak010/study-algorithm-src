def solution(cipher, code):
    result = ""

    for idx, value in enumerate(cipher, start=1):

        if idx % code == 0:
            result += value

    return result


if __name__ == '__main__':
    a = "dfjardstddetckdaccccdegk"
    print(solution(a, 4))
