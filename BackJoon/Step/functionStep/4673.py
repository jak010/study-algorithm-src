def d(x):
    src = x
    each_sum = 0
    while x != 0:
        each = int(x % 10)
        x = int(x / 10)

        each_sum += each

    return src + each_sum


if __name__ == '__main__':

    N = 10000

    sequence = [x for x in range(1, N + 1)]
    not_self_number = [d(k) for k, v in enumerate(sequence, start=1)]

    for x in sorted(set(sequence) - set(not_self_number)):
        print(x)
