import sys

_ = int(sys.stdin.readline())

_seq_numbers = str(input())

print(sum([int(x) for x in _seq_numbers]))
