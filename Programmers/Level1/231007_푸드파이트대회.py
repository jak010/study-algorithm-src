from collections import deque


def solution(food):
    temp = []

    for x in range(1, len(food)):
        s = str(x) * food[x]

        if len(s) % 2 == 0:
            mid = int(len(s) / 2)
            temp.append(s[0:mid])
            temp.append(s[mid::])
        else:
            s = s[0:-1]
            mid = int(len(s) / 2)
            temp.append(s[0:mid])
            temp.append(s[mid::])

    q = deque(['0'])
    for idx, x in enumerate(reversed(temp), start=0):
        if idx % 2 == 0:
            q.appendleft(x)
        else:
            q.append(x)

    return ''.join(q)


def sol2(food):
    answer = '0'
    for i in range(len(food) - 1, 0, -1):
        c = int(food[i] / 2)

        while c > 0:
            answer = str(i) + answer + str(i)
            c -= 1

    return answer


food = [1, 3, 4, 6]

print(sol2(food))
