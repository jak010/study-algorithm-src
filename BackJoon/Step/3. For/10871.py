import sys

array_size, find_number = map(int, sys.stdin.readline().split())
arrays = list(map(int, sys.stdin.readline().split()))

result = []
for x in arrays:
    if x < find_number:
        print(x, end=" ")
