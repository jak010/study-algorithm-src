import sys

COUNT = 10

dicts = {}

for x in range(COUNT):
    input_number = int(sys.stdin.readline())

    result = input_number % 42

    if result in dicts:
        dicts[result] += 1
    else:
        dicts[result] = 1

print(len(dicts))
