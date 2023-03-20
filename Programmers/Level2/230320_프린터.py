#  F
# priorities = [2, 1, 3, 2]
# location = 2
# def solution(priorities, location):
#     labeled = {}
#     for idx, k in enumerate(priorities):
#         labeled[idx] = k
#
#     search_key = labeled[location]
#
#     queue = []
#     for k in priorities:
#         queue.append(k)
#         queue.sort(reverse=True)
#
#     return queue.index(search_key) + 1

# S
from collections import deque


class Vp:
    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer

    def __repr__(self):
        return f"Vp(" \
               f"value={self.value}," \
               f" pointer={self.pointer}" \
               f")"


def solution(priorities, location):
    s = []

    vps = []
    for idx, value in enumerate(priorities):
        vps.append(Vp(value=value, pointer=idx))

    dq = deque()
    dq.append(vps[0])

    saveidx = 0
    for vp in vps[1:]:
        if vp.value <= dq[0].value:
            dq.append(vp)
        elif vp.value > dq[0].value:
            saveidx = vps.index(vp)
            break

    for vp in vps[saveidx:]:
        s.append(vp)

    while s:
        v = s.pop()
        dq.appendleft(v)

    # for v in dq:
    #     if v.pointer == location:
    #         return dq.index(v) + 1

    for i, v in enumerate(dq):
        if v.pointer == location:
            return i + 1


priorities = [2, 1, 3, 2]  # -> 3,2,2,1
location = 2

print(solution(priorities, location))
