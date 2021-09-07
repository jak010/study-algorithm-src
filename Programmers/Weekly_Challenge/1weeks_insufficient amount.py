# price 이용료
# N 번 이용하면 N배

# 이용료?
# price = price * N

# price =  이용금액
# count =  몇 번
# money = 가진 돈

# price = 3
# count = 4
# money = 20

# 3 (4)
# 3, 6, 9, 12 = 30 - money(20)  == 10

# def solution(price, money, count):
#     total_price = sum([x for x in range(price, count * price + 1, price)])
#
#     answer = total_price - money
#
#     if answer > 0:
#         return answer
#     else:
#         return 0


def solution(price, money, count):
    total_price = sum(range(price, count * price + 1, price))

    return total_price - money if total_price - money > 0 else 0


if __name__ == '__main__':
    print(solution(3, 20, 4))
