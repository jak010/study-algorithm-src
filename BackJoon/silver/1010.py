def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n - 1)


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    result = int(factorial(m) / (factorial(m - n) * factorial(n)))

    print(result)

# from itertools import combinations
#
# def count_bridge_combinations(N, M):
#     # 서쪽 사이트 중 N개를 선택하는 경우의 수 계산
#     combinations_count = len(list(combinations(range(M), N)))
#     return combinations_count
#
# # 예시 호출
# N = 1
# M = 5
# result = count_bridge_combinations(N, M)
# print(result)
