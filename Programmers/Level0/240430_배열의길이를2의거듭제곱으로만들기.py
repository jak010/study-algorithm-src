# https://school.programmers.co.kr/learn/courses/30/lessons/181857
def solution(arr):
    for v in range(len(arr)):

        target = 2 ** v

        if len(arr) == target:
            return arr

        if len(arr) < target:
            padding = target - len(arr)
            arr.extend([0 for _ in range(padding)])

            return arr


if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5, 6]))
    print(solution([58, 172, 746, 89]))
