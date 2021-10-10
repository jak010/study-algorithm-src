from typing import List


def binary_search(target, data: List):
    data.sort()

    start = 0
    end = len(data) - 1
    mid = (start + end) // 2

    while start <= end:

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


if __name__ == '__main__':
    numbers = [i ** 2 for i in range(11)]

    # Pointer
    # start = 0
    # end = len(numbers) - 1
    # mid = (start + end) // 2

    target = 9
