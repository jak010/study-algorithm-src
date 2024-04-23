import sys


def solution(numbers):
    current_max = -sys.maxsize

    for i1, v1 in enumerate(numbers):
        for i2, v2 in enumerate(numbers):
            if i1 != i2:
                current_max = max(v1 * v2, current_max)

    return current_max


if __name__ == '__main__':
    print(solution([1, 2, -3, 4, -5]))
    print(solution([0, -31, 24, 10, 1, 9]))
    print(solution([10, 20, 30, 5, 5, 20, 5]))
