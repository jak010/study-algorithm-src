# https://www.acmicpc.net/problem/1181

""" Description

Input
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

"""
from collections import defaultdict

number = input()

word_dict = defaultdict(set)

for x in range(int(number)):
    input_str = input()

    word_dict[len(input_str)].add(input_str)


for k, v in sorted(word_dict.items(), key=lambda x:x[0]):
    for item in sorted(v):
        print(item)
