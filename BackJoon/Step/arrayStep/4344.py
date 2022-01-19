import sys

# total case
total = int(sys.stdin.readline())

for _ in range(total):
    raw = sys.stdin.readline().split(" ")
    cnt, grade = raw[0], [int(x) for x in raw[1:]]

    avg = sum(grade) / len(grade)

    rate = [x for x in grade if x > avg]

    print("{:.3f}%".format(float(len(rate) / len(grade) * 100)))



