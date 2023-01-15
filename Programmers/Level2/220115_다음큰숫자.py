# def solution(n):
#     bit_of_n = bin(n)
#     bit_of_n_count_1 = bit_of_n.count('1')
#
#     for x in range(n + 1, 1_000_000 - n):
#         if bin(x).count('1') == bit_of_n_count_1:
#             return x

def solution(n):
    bit_of_n = bin(n)
    bit_of_n_count_1 = bit_of_n.count('1')
    _limit_ext = n

    while True:
        _limit_ext += 1

        if bin(_limit_ext).count('1') == bit_of_n_count_1:
            return _limit_ext


if __name__ == '__main__':
    ex = 78
    limit = 1_000_000 - ex

    print(solution(ex))
