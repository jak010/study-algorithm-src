from collections import deque


# def solution(arr, k):
#     _t_stack = []
#
#     q = deque(arr)
#
#     while q:
#         item = q.popleft()
#         if item not in _t_stack and len(_t_stack) < k:
#             _t_stack.append(item)
#
#     if len(_t_stack) < k:
#         padding = len(arr) - len(_t_stack)
#         [_t_stack.append(-1) for x in range(padding-1)]

#     return _t_stack

# def solution(arr, k):
#     st = set(arr)
#     answer = list(set(arr))
#
#     if len(answer) < k:
#         pad = k - len(st)
#         for _ in range(pad):
#             answer.append(-1)
#
#     if len(answer) > k:
#         return answer[:k]
#
#     return answer

# 3st
def solution(arr, k):
    answer = []
    q = deque(arr)

    # 앞에서부터 순서대로 뽑는다.
    while q:
        item = q.popleft()
        if item not in answer:  # answer에 없으면 추가하자.
            answer.append(item)

    if len(answer) > k:  # answer가 k보다 크다는 건 -1을 추가할 필요가 없으니 k만큼으로 slice 후 return
        return answer[:k]
    else:  # k보다 answer가 작은 경우 -1을 추가해야되니 padding 구해서 추가
        pad = [-1 for _ in range(k - len(answer))]
        answer.extend(pad)
        return answer


if __name__ == '__main__':
    print(solution([0, 1, 1, 2, 2, 3], 3))  # exp 0,1,2
    print(solution([0, 1, 1, 1, 1], 4))  # exp, 0,1,-1,-1
    print(solution([5, 4, 3, 2, 1], 3))  # exp, 5,4,3
