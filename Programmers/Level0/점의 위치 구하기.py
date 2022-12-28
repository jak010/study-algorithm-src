def solution(dot):
    x, y = dot[0], dot[1]

    if x > 0 and y > 0:
        return 1

    if x < 0 < y:
        return 2

    if x < 0 and y < 0:
        return 3

    if x > 0 > y:
        return 4


if __name__ == '__main__':
    dot = [-7, 9]
    print(solution(dot))
