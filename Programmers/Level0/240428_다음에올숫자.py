def solution(common):
    if common[1] - common[0] == common[-1] - common[-2]:
        return common[-1] + (common[1] - common[0])
    else:
        return common[-1] * int(common[1] / common[0])


if __name__ == '__main__':
    print(solution([1, 2, 3, 4]))  # exp, 5
    print(solution([2, 4, 8]))  # exp, 16
    print(solution([-1, 2, -4]))  # exp, 8
