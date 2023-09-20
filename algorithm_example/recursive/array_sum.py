def array_sum(array):
    if len(array) == 1:
        return array[0]

    return array[0] + array_sum(array[1:len(array)])


print(array_sum(array=[1, 2, 3, 4, 5]))
