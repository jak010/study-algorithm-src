# https://www.acmicpc.net/problem/3040
# level : 2

""" Description
9 개의 숫자가 주어지고 그 중 7개를 골라 합이 100이 되는 경우를 찾는 문제다.
"""

from itertools import combinations

tc = """
7
8
10
13
15
19
20
23
25
"""
tc = [int(i) for i in tc.splitlines() if i]

for i in combinations(tc, 7):
    if sum(i) == 100:
        print([j for j in sorted(i)])
