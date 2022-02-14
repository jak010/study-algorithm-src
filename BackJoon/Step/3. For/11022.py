import sys

count = int(input())

for x in range(1, count + 1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #" + str(x) + ": " + str(a) + " + " + str(b) + " = " + str(a + b))
