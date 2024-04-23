# https://school.programmers.co.kr/learn/courses/30/lessons/120836

# def solution(n):
#     count = 0
#     for i in range(0, n + 1):
#         for j in range(0, n + 1):
#             if i * j == n:
#                 count += 1
#
#     return count


def solution(n):
    number = []
    for i in range(1, n + 1):
        if n % i == 0:
            number.append(i)

    return len(number)


if __name__ == '__main__':
    n = 20
    print(solution(n))
