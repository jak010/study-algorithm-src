import heapq

x = """18
1
-1
0
0
0
1
1
-1
-1
2
-2
0
0
0
0
0
0
0
"""

M = x.splitlines()[0]

hq = []
for input_number in range(int(M)):
    number = int(input_number)

    if number == 0:
        print(heapq.heappushpop(hq)[1] if len(hq) else 0)
    else:
        heapq.heappush(hq, (abs(number), number))

print(hq)