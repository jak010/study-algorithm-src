# 삼각수 만들기
def gen(start, end, offset):
    print(start, end, offset)

    if start >= end:  # n이 7보다 커지는 시점에 종료함
        return start
    else:
        start += offset

    return 0 + gen(start, end, offset + 1)


gen(1, 21, 2)


def len_of_gen(n):
    if n == 0:
        return 0
    return n + len_of_gen(n - 1)


print(len_of_gen(7))
