number = int(input())

_sum = 0
result = 0
for x in range(1, number):
    if _sum >= number:
        break

    if _sum <= number:
        result = x

    _sum += x

print(result)
