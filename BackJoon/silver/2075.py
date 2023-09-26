import heapq

N = int(input())

heap = []

for _ in range(0, N):
    rows = list(map(int, input().split()))

    for r in rows:
        if len(heap) < N:
            heapq.heappush(heap, int(r))
        else:
            if heap[0] < r:
                heapq.heappop(heap)
                heapq.heappush(heap, r)

    print(heap)

print(heap[0])

#
# TARGET_COUNT = (N * N) - N
# SEARCH_COUNT = 0
#
# while not q1.empty():
#     element = q1.get()
#     if SEARCH_COUNT == TARGET_COUNT:
#         print(element)
#         break
#
#     SEARCH_COUNT += 1

# for _ in range(0, N):
#     each_list = map(int, input().split())
#
#     for x in [int(x) for x in each_list]:
#         q1.put(x)
#
# TARGET_COUNT = (N * N) - N
# SEARCH_COUNT = 0
#
# while not q1.empty():
#     element = q1.get()
#     if SEARCH_COUNT == TARGET_COUNT:
#         print(element)
#         break
#
#     SEARCH_COUNT += 1
