# 힙 정렬
# - O(log N)
# - 힙에는 어떤 값을 넣오도 항상 루트게 가장 큰 값 또는 작은 값이 위치
# - 무작위 숫자들을 힙에 전부 넣고 하나씩 뺴면 정렬된 결과를 얻을 수 있으며, 이게 힙 정렬


from queue import PriorityQueue

# PriotiyQueue는 멀티 쓰레딩 환경을 고려한 큐이므로 느림
pq = PriorityQueue()
pq.put(123)
pq.put(789)
pq.put(456)

while not pq.empty():
    print(pq.get())

print("=" * 20)

# heapq는 멀티쓰레딩 환경을 고려하지 않는 대신 더 빠른 모듈임
# python의 heapq는 최소힙이다. (최대합은 제공되지 않음)
#   - 최대힙이 필요한 경우 부호를 반대로 넣는 테크닉 사용
import heapq

h = []
heapq.heappush(h, 123)
heapq.heappush(h, 789)
heapq.heappush(h, 456)

while len(h):
    print(heapq.heappop(h))
