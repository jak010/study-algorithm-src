# https://school.programmers.co.kr/learn/courses/30/lessons/181922
def solution(arr, queries):
    for query in queries:
        s, e, k = query[0], query[1], query[2]

        for i, v in enumerate(arr):
            if s <= i <= e:
                if i % k == 0:
                    arr[i] = arr[i] + 1

    return arr


if __name__ == '__main__':
    print(solution([0, 1, 2, 4, 3], [[0, 4, 1], [0, 3, 2], [0, 3, 3]]))
