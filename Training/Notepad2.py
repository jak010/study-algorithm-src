string = 'abcd'

LEN_OF_STRING = len(string)

# count : 25
# description
# 메인 루프에서 하위 루프를 다 돌고 그 다음 메인 루프를 도는 방식 (완전탐색?)
c1 = 0
for x in range(LEN_OF_STRING + 1):
    for y in range(LEN_OF_STRING + 1):
        # print(string[x:y], x, y)
        c1 += 1
        print(c1, x, y)

print("=" * 20)

# count :16
# description
# 메인 루프와 서브루프를 통해 범위를 좁혀 나가는 방식으로 돔 (부분탐색?)
c2 = 0
for x in range(LEN_OF_STRING):
    for y in range(LEN_OF_STRING, 0, -1):
        c2 += 1
        print(c2, x, y)
