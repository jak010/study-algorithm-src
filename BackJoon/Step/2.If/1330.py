"""
Date: 2021.12.20

두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

"""
numbers = input()
a, b = numbers.split()


def cmp(a, b):
    if int(a) > int(b):
        print(">")
    elif int(a) < int(b):
        print("<")
    else:
        print("==")
