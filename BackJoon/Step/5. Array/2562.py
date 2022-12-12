import sys

count = 9

temp = []

for x in range(count):
    input_number = int(sys.stdin.readline())
    temp.append(input_number)

print(max(temp))
print(temp.index(max(temp)) + 1)
