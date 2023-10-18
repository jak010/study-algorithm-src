a = 3
b = 1
n = 20


def solution(a, b, n):
    answer = 0
    # 단, 보유 중인 빈 병이 2개 미만이면, 콜라를 받을 수 없다.
    # 빈 병의 개수가 콜라를 받기 위해서 필요한 개수보다 크면 반복한다
    while n >= a:
        remain_bottle = n % a
        n = (n // a) * b  # 마트에서 받은 콜라의 수
        answer += n  # 받은 걸 answer에 +
        n += remain_bottle  # 남아있는 병을 더해줘서 다음에 마트갈 때 이용
    return answer


print(solution(a, b, n))

#
# d, r = divmod(n, a)
# print(d, r)
#
#
# d2, r2 = divmod(int(d + r), a)
#
# print(d2, r2)
#
# d3, r3 = divmod(int(d2 + r2), a)
#
# print(d3, r3)
#
# d4, r4 = divmod(int(d3 + r3), a)
#
# print(d4, r4)
#
# d5, r5 = divmod(int(d4+r4), a)
#
# print(d5, r5)

# a = 3
# b = 1
# n = 20
#
# d, r = divmod(n, a)
# print(d, r)
