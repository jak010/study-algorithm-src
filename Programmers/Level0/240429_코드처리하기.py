def solution(code):
    answer = []
    mode = '0'
    for idx, value in enumerate(code):

        if mode == '0':
            if value != '1' and idx % 2 == 0:
                answer.append(value)
            if value == '1':
                mode = '1'
            continue

        if mode == '1':
            if value != '1' and idx % 2 != 0:
                answer.append(value)
            if value == '1':
                mode = '0'
            continue
    if not answer:
        return "EMPTY"

    return ''.join(answer)


if __name__ == '__main__':
    code = "abc1abc1abc"

    print(solution(code))  # result, acbac
