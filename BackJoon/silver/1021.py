import sys
from collections import deque

size, num = map(int, sys.stdin.readline().split())  # 10, 3
idx = list(map(int, sys.stdin.readline().split()))  # 1,2,3

queue = deque([_ for _ in range(1, size + 1)])
count = 0

for i in idx:
    while True:
        if i == queue[0]:
            queue.popleft()
            break

        # 왼쪽에서 꺼낸다
        if queue.index(i) <= len(queue) // 2:
            while i != queue[0]:
                queue.append(queue.popleft())
                count += 1

        # 오른쪽에서 꺼낸다.
        else:
            while i != queue[0]:
                queue.appendleft(queue.pop())
                count += 1
print(count)
