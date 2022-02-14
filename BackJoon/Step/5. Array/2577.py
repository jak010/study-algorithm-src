import sys
from collections import Counter

input_number1 = int(sys.stdin.readline())
input_number2 = int(sys.stdin.readline())
input_number3 = int(sys.stdin.readline())

cnt = Counter(str(input_number1 * input_number2 * input_number3))

for _idx in range(10):
    print(cnt[str(_idx)])
