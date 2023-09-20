def mysum(low, high):
    if low > high:
        return 0
    return low + mysum(low + 1, high)


print(mysum(1, 10))
