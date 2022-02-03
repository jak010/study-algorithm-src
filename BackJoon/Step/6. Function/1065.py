import sys


def hansu(number):
    if number < 100:
        return len([x for x in range(0, number)])

    count = 99
    for x in range(100, number + 1):
        if x < 1000:
            a, b, c = map(int, list(str(x)))
            if int(a - b) == int(b - c): count += 1
        else:
            count += 0

    return count


if __name__ == '__main__':
    number = int(sys.stdin.readline())
    print(hansu(number))

    number1 = 110  # 99
    print(hansu(number1))

    number2 = 1  # 1
    print(hansu(number2))

    number3 = 210  # 110
    print(hansu(number3))

    number4 = 1000  # 144
    print(hansu(number4))

    number5 = 500  # 119
    print(hansu(number5))
