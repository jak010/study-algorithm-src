# boj 2164
# level: 2
# 카드2

"""
    N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어있으며,
    1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여있다.

    이제 다음과 같은 동작을 카드가 한 장 남을떄까지 반복하게된다.

    우선 제일 위에 있는 카드를 바닥에 버린다. 그 다음 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다
"""

from collections import deque

# solution
N = 6
dq = deque()
for i in range(1, N + 1):
    dq.append(i)

while len(dq) > 1:
    dq.popleft()  # 맨위의 카드를 버린다
    dq.append(dq.popleft())  # 그 다음. 제일 위에 있는 카드를 제일 아래에 엤는 카드 밑으로 옮긴다

print(dq.pop())
