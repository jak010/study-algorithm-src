a1 = ["ab", "c", "def", "ghij"]


def count_c(arr):
    if len(arr) == 0:
        return 0

    return len(arr[0]) + count_c(arr[1:])


print(count_c(a1))
