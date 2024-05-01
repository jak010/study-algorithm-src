def solution(str_list):
    answer = []
    for idx, value in enumerate(str_list):

        if value == 'l':
            answer = str_list[:idx]
            break

        if value == 'r':
            answer = str_list[idx+1:]
            break
    return answer


if __name__ == '__main__':
    print(solution(["u", "u", "l", "r"]))
    print(solution(["l"]))
    print(solution(["u", "r", "u", "r"]))
    print(solution(["r", "l"]))
    print(solution(["u", "u", "r", "l", "r", "r", "r", "r"]))
