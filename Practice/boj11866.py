# boj 1866
# 요세푸스 문제

# 배열을 이용할 경우 : 삽입 O(1), 삭제 O(N)

N = 7
K = 3

peo = [i for i in range(1, N + 1)]

pt = 0

ans = []

for _ in range(K):
    pt += K - 1  # 순회 시작점  (Array Index 떄문에 -1)
    pt %= len(peo)  # Array Rotate를 위한 포지션 계산하기
    ans.append(peo.pop(pt))

print(ans)
