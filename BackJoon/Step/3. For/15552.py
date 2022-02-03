import sys

test_count = int(input())

for x in range(test_count):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
