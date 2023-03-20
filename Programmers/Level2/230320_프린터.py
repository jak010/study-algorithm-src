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
# from collections import deque
#
#
# class Vp:
#     def __init__(self, value, pointer):
#         self.value = value
#         self.pointer = pointer
#
#     def __repr__(self):
#         return f"Vp(" \
#                f"value={self.value}," \
#                f" pointer={self.pointer}" \
#                f")"
#
#
# def solution(priorities, location):
#     s = []
#
#     vps = []
#     for idx, value in enumerate(priorities):
#         vps.append(Vp(value=value, pointer=idx))
#
#     dq = deque()
#     dq.append(vps[0])
#
#     saveidx = 0
#     for vp in vps[1:]:
#         if vp.value <= dq[0].value:
#             dq.append(vp)
#         elif vp.value > dq[0].value:
#             saveidx = vps.index(vp)
#             break
#
#     for vp in vps[saveidx:]:
#         s.append(vp)
#
#     while s:
#         v = s.pop()
#         dq.appendleft(v)
#
#     # for v in dq:
#     #     if v.pointer == location:
#     #         return dq.index(v) + 1
#
#     for i, v in enumerate(dq):
#         if v.pointer == location:
#             return i + 1


# T
def solution(priorities, location):
    printer = [(i, p) for i, p in enumerate(priorities)]
    turn = 0
    while printer:
        job = printer.pop(0)
        # 우선순위가 낮으면 마지막에 붙임
        if any(job[1] < other_job[1] for other_job in printer):
            printer.append(job)
        else:
            # 처리된 순서에 대해서 카운트함
            turn += 1
            if job[0] == location:
                break
    return turn


# F
class Vp:
    def __init__(self, loc, val):
        self.loc = loc
        self.val = val

    def __repr__(self):
        return f"({self.val}->{self.loc})"


from collections import deque


def solution2(priorities, location):
    dq = deque()

    for idx, v in enumerate(priorities):
        dq.append(Vp(loc=idx, val=v))

    while dq:
        vp = dq.popleft()

        if dq and vp.val < max([v.val for v in dq]):
            dq.append(vp)

        if vp.val >= max([v.val for v in dq]):
            dq.appendleft(vp)
            break

    for vp in dq:
        if vp.loc == location:
            return dq.index(vp) + 1


priorities = [2, 1, 3, 2]  # -> 3,2,2,1
location = 2

# priorities = [1, 1, 9, 1, 1, 1]
# location = 0

print(solution2(priorities, location))
