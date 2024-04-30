# https://school.programmers.co.kr/learn/courses/30/lessons/181924

def solution(arr, queries):
    for query in queries:
        s, e = query[0], query[1]

        arr[s], arr[e] = arr[e], arr[s]

    return arr


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4]
    queries = [[0, 3], [1, 2], [1, 4]]

    solution(arr, queries)
