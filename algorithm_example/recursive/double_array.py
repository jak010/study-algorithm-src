def double_array(array, index):
    if index >= len(array):
        return array

    array[index] *= 2
    return double_array(array, index + 1)


print(double_array([1, 2, 3, 4, 5], 0))
