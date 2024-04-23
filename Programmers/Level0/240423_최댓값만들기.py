def solution(numbers):
    numbers.sort(reverse=True)


    return numbers[0] * numbers[1]


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    print(solution(numbers))
