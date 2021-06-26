arrays = [3,2,6]

divisior = 10


def solution(arr, divisor):
    temp = []
    for n in arr:
        if n % divisor == 0:
            temp.append(n)

    if not temp:
        return [-1]

    return sorted(temp)


print(solution(arrays, divisior))
