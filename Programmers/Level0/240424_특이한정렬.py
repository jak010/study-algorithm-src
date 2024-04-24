from collections import defaultdict


def solution(numlist, n):
    index_lst = [abs(n - e) for e in numlist]

    inverse = [(idx, value) for idx, value in enumerate(index_lst)]

    offset_group = {}  # 같은 offset 위치를 같은 그룹으로 묶기

    # answer = []
    for index, value in sorted(inverse, key=lambda x: x[1]):
        # print(index, value)

        if value not in offset_group:
            offset_group[value] = [index]
        else:
            offset_group[value].append(index)

    answer = []
    for _, index in offset_group.items():

        index = sorted([numlist[i] for i in index])
        for e in sorted(index, reverse=True):
            answer.append(e)

    return answer


if __name__ == '__main__':
    print(solution(numlist=[10, 2], n=6))  # ex == [10, 2]

    print(solution(numlist=[1, 2, 3, 4, 5, 6], n=4))
    # print(solution(numlist=[10000, 20, 36, 47, 40, 6, 10, 7000], n=30))
