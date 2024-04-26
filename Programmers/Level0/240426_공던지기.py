def solution(numbers, k):
    answer = 0
    count = 1
    current = 0
    for idx in range(k):
        current = (current + 2) % len(numbers)
        count += 1

        if count == k:
            answer = numbers[current]

    return answer


if __name__ == '__main__':
    # print(solution([1, 2, 3, 4], 2))  # 3
    # print(solution([1, 2, 3, 4, 5, 6], 5)) # 3
    print(solution([1, 2, 3], 3))  # 2
