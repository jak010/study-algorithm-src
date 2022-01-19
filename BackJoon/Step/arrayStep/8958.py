import sys

total = int(sys.stdin.readline())

for _ in range(0, total):
    count = 0
    sequence = []
    strings = sys.stdin.readline()
    for ch in strings:
        if ch == "X":
            count = 0
            sequence.append(count)
            continue
        count = count + 1
        sequence.append(count)
    sequence.pop()
    print(sum(sequence))

