# https://www.acmicpc.net/problem/1931
# level: 3
# tag: greedy
# 활동 선택 문제

""" input

11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

"""

import sys

# 종료시간 기준으로 정렬하기 위한 데이터 초기화
mettings = []
for _ in range(int(input())):
    start, end = map(int, input().split())
    mettings.append((end, start))

mettings.sort()  # 종료시간 기준으로 정렬함

t = 0
ans = 0
for end, start in mettings:
    if t <= start:  # 시작 시간이 겹치지 않게 선택
        ans += 1
        t = end

print(ans)
