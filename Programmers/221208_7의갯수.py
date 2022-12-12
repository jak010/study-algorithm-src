def solution(array):
    counter = 0

    for arr in array:

        while arr != 0:
            divide = arr % 10

            if divide == 0:
                break

            if (divide % 7) == 0:
                counter += 1
            arr //= 10

    return counter


if __name__ == '__main__':
    arr1 = [7, 77, 17]
    arr2 = [10, 29]

    print(solution(arr2))
