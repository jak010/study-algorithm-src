import sys

total_count = int(sys.stdin.readline())

for idx in range(0, total_count):
    number, strings = input("").split(" ")

    print(''.join([index * int(number) for index in strings]))
