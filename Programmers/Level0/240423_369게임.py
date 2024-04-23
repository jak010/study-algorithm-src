def solution(order):
    count = 0
    while order > 0:
        if order % 10 == 3 or order % 10 == 6 or order % 10 == 9:
            count += 1

        order //= 10

    return count


if __name__ == '__main__':
    print(solution(3))

    print(solution(29423))
